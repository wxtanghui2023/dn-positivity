#!/usr/bin/env python3
"""L8-1 A1 MODEL EXPERIMENT RUNNER — authorised by 唐先生 2026-10-09 19:09.

Authorisation is BOUND to pre-registration v1.1 sha256 5805b5c47783218d14e51f5e7e2b39991769aa671d6b8adef084377344f587f0
and to the frozen scorer A1-SCORER-v1.  Strict rules enforced here:
  * model fixed, parameters fixed, no added tasks, no early stop, no manual repair
  * transport retry ONLY for HTTP 5xx / transport error, ORIGINAL parameters, GLOBAL cap 4
  * read-timeout => UNDECIDABLE, never retried
  * model unavailable (HTTP 4xx) => abort run, record UNDECIDABLE, NO substitution
  * full ledger + raw outputs + scoring results + reason codes retained
"""
import json, os, sys, time, hashlib, urllib.request, urllib.error, socket

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l8_1_a1_evaluator as A1
from l8_1_a1_aggregate import (verdict_c1a, judge_infeasible_control, new_ledger, add_entry,
                               validate_ledger, C1B_EXPECTED, verify_c1b_binding)

BASE = 'https://api.deepseek.com'
API_MODEL = 'deepseek-v4-flash'          # OpenClaw alias deepseek/deepseek-v4-flash
TEMP = 0.2
MAXTOK = 4000
TIMEOUT = 300
PREREG_SHA = '5805b5c47783218d14e51f5e7e2b39991769aa671d6b8adef084377344f587f0'
RAW = os.path.join(HERE, 'RAW-A1.jsonl')
LEDGER_F = os.path.join(HERE, 'A1-RUN-LEDGER.json')
RESULT_F = os.path.join(HERE, 'A1-RUN-RESULT.json')


def key():
    for line in open(os.path.expanduser('~/.openclaw/.env')):
        line = line.strip()
        if line.startswith('DEEPSEEK_API_KEY='):
            return line.split('=', 1)[1].strip().strip('"').strip("'")
    raise SystemExit('no DEEPSEEK_API_KEY')


def verify_prereg():
    p = os.path.join(HERE, 'A1-PREREGISTERED-EXPERIMENT-v1.1.json')
    doc = json.load(open(p))
    body = json.dumps({k: v for k, v in doc.items() if k != 'preregistration_sha256'},
                      sort_keys=True).encode()
    got = hashlib.sha256(body).hexdigest()
    return doc, got, got == PREREG_SHA


def preflight(k):
    """metadata request only: consumes NO inference.  Recorded separately from the ledger."""
    try:
        req = urllib.request.Request(BASE + '/models',
                                     headers={'Authorization': 'Bearer ' + k})
        r = urllib.request.urlopen(req, timeout=30)
        ids = [m.get('id') for m in json.loads(r.read()).get('data', [])]
        return {'ok': True, 'models_listed': len(ids), 'target_present': API_MODEL in ids}
    except Exception as e:
        return {'ok': False, 'error': str(e)[:200]}


def call(k, prompt):
    body = json.dumps({'model': API_MODEL, 'messages': [{'role': 'user', 'content': prompt}],
                       'temperature': TEMP, 'max_tokens': MAXTOK}).encode()
    req = urllib.request.Request(BASE + '/chat/completions', data=body,
                                 headers={'Content-Type': 'application/json',
                                          'Authorization': 'Bearer ' + k})
    t0 = time.time()
    try:
        r = urllib.request.urlopen(req, timeout=TIMEOUT)
        d = json.loads(r.read())
        ch = d['choices'][0]
        return {'status': 'ok', 'content': ch['message'].get('content') or '',
                'finish': ch.get('finish_reason'), 'usage': d.get('usage'),
                'elapsed_s': round(time.time() - t0, 1)}
    except urllib.error.HTTPError as e:
        code = e.code
        return {'status': ('http_5xx' if 500 <= code < 600 else 'http_4xx'),
                'error': 'HTTP %s' % code, 'body': e.read().decode()[:300],
                'elapsed_s': round(time.time() - t0, 1)}
    except (socket.timeout, TimeoutError) as e:
        return {'status': 'timeout', 'error': str(e)[:150], 'elapsed_s': round(time.time() - t0, 1)}
    except Exception as e:
        s = str(e).lower()
        st = 'timeout' if 'timed out' in s else 'transport_error'
        return {'status': st, 'error': str(e)[:200], 'elapsed_s': round(time.time() - t0, 1)}


def extract_json(text):
    """strict: whole body, fenced block, or first balanced object."""
    if not text:
        return None
    t = text.strip()
    for cand in (t,):
        try:
            return json.loads(cand)
        except Exception:
            pass
    if '```' in t:
        seg = t.split('```')[1]
        seg = seg[4:] if seg.lower().startswith('json') else seg
        try:
            return json.loads(seg.strip())
        except Exception:
            pass
    i = t.find('{')
    while i != -1:
        depth = 0
        for j in range(i, len(t)):
            if t[j] == '{':
                depth += 1
            elif t[j] == '}':
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(t[i:j + 1])
                    except Exception:
                        break
        i = t.find('{', i + 1)
    return None


def params_digest(prompt):
    return hashlib.sha256(json.dumps({'m': API_MODEL, 't': TEMP, 'x': MAXTOK, 'p': prompt},
                                     sort_keys=True).encode()).hexdigest()[:16]


def parsed_submissions(by_task, tid):
    """MINIMAL FIX (authorised 2026-10-09 19:31): return ONLY parsed dict submissions.
    Unparsable outputs (parsed is None) or any non-dict object are EXCLUDED here and are handled
    by the pre-registered aggregation rules (e.g. '>=2 of 3 unparsable => UNDECIDABLE'); they must
    never be passed into the frozen scorer, whose contract takes already-parsed submissions."""
    out = []
    for r in by_task.get(tid, []):
        p = r.get('parsed')
        if r.get('status') == 'ok' and isinstance(p, dict):
            out.append(p)
    return out


def unparsable_count(by_task, tid):
    return sum(1 for r in by_task.get(tid, []) if not isinstance(r.get('parsed'), dict))


def main():
    doc, got, ok = verify_prereg()
    print('prereg sha recomputed =', got)
    print('prereg sha matches authorised  =', ok)
    if not ok:
        print('ABORT: pre-registration hash mismatch (authorisation is void)')
        return 2
    k = key()
    pf = preflight(k)
    print('preflight (metadata only, no inference):', pf)
    if not pf.get('ok'):
        print('ABORT: cannot reach the model endpoint; recording an interface failure (not a '
              'capability failure)')
        json.dump({'aborted': True, 'reason': 'preflight failed', 'preflight': pf},
                  open(RESULT_F, 'w'), indent=1)
        return 3

    lib = A1.build_library()
    led = new_ledger()
    seq = 0
    records = []
    open(RAW, 'w').close()
    aborted = None
    for cap, tasks in doc['tasks'].items():
        for t in tasks:
            for attempt in range(1, t['attempts'] + 1):
                prompt = t['prompt']
                pd = params_digest(prompt)
                while True:
                    seq += 1
                    r = call(k, prompt)
                    kind = 'primary' if seq == 1 else None
                    if kind is None:
                        kind = 'primary'
                    led_kind = 'primary'
                    trigger = None
                    if r['status'] != 'ok':
                        if r['status'] == 'http_5xx' or r['status'] == 'transport_error':
                            retries = sum(1 for x in led['entries'] if x['kind'] == 'transport_retry')
                            if retries >= led['global_retry_cap']:
                                aborted = {'reason': 'global retry cap reached', 'task': t['id']}
                            else:
                                led_kind, trigger = 'transport_retry', r['status']
                        elif r['status'] == 'http_4xx':
                            aborted = {'reason': 'model unavailable (HTTP 4xx): %s' % r.get('error'),
                                       'task': t['id'], 'body': r.get('body')}
                        elif r['status'] == 'timeout':
                            pass                      # UNDECIDABLE, never retried
                    add_entry(led, seq, led_kind, t['id'], trigger, pd, pd,
                              r['status'], time.strftime('%H:%M:%S'))
                    rec = {'seq': seq, 'kind': led_kind, 'cap': cap, 'task': t['id'],
                           'attempt': attempt, 'trigger': trigger, **r}
                    rec['parsed'] = extract_json(r.get('content')) if r['status'] == 'ok' else None
                    rec['parse_ok'] = rec['parsed'] is not None
                    records.append(rec)
                    with open(RAW, 'a') as f:
                        f.write(json.dumps(rec) + '\n')
                    print('seq=%2d %-22s att=%d %-14s parse=%s elapsed=%ss'
                          % (seq, t['id'], attempt, r['status'], rec['parse_ok'],
                             r.get('elapsed_s')), flush=True)
                    if r['status'] == 'ok' or r['status'] not in ('http_5xx', 'transport_error'):
                        break
                    if aborted:
                        break
                if aborted:
                    break
            if aborted:
                break
        if aborted:
            break

    # ---------------- scoring (frozen scorer + v1.1 aggregation rules) ----------------
    by_task = {}
    for rec in records:
        by_task.setdefault(rec['task'], []).append(rec)

    def parsed_list(tid):
        return parsed_submissions(by_task, tid)

    res = {'prereg_sha': PREREG_SHA, 'prereg_verified': True, 'api_model': API_MODEL,
           'alias': 'deepseek/deepseek-v4-flash', 'temperature': TEMP, 'max_tokens': MAXTOK,
           'timeout_s': TIMEOUT, 'preflight': pf, 'aborted': aborted,
           'calls_total': len([r for r in records if r['kind'] != 'preflight']),
           'calls_primary': len([r for r in records if r['kind'] == 'primary']),
           'calls_transport_retry': len([r for r in records if r['kind'] == 'transport_retry']),
           'timeouts': len([r for r in records if r['status'] == 'timeout']),
           'http_4xx': len([r for r in records if r['status'] == 'http_4xx']),
           'capabilities': {}}

    # C1a
    feas = parsed_list('C1a-feasible-1')
    ctl_out = (parsed_list('C1a-infeasible-ctl') or [None])[0]
    v = verdict_c1a(lib, feas, ctl_out)
    res['capabilities']['C1a'] = {'verdict': v['verdict'], 'why': v['why'],
                                  'distinct_valid': v['distinct_valid'],
                                  'valid_attempts': v['valid_attempts'],
                                  'control': v['control'], 'per_attempt': v['per_attempt'],
                                  'raw_records': [{'seq': r['seq'], 'status': r['status'],
                                                   'parse_ok': r['parse_ok']} for r in by_task.get('C1a-feasible-1', [])]}
    res['capabilities']['C1a']['control_record'] = [{'seq': r['seq'], 'status': r['status'],
                                                     'parse_ok': r['parse_ok']}
                                                    for r in by_task.get('C1a-infeasible-ctl', [])]

    # C1b
    c1b_detail = {}
    for tid, spec in C1B_EXPECTED.items():
        outs = parsed_list(tid)
        inst = A1.__dict__[spec['instance']] if spec['instance'] != 'N7' else A1.N7
        if outs:
            vv, dd = A1.eval_c1b(inst, outs[0])
            c1b_detail[tid] = {'verdict': vv, 'detail': {'hyp_mismatches': dd['hyp_mismatches'],
                                                         'applicability_correct': dd['applicability_correct'],
                                                         'conclusion_ok': dd['conclusion_ok']}}
        else:
            c1b_detail[tid] = {'verdict': 'UNPARSABLE', 'detail': None}
    unpars = sum(1 for x in c1b_detail.values() if x['verdict'] == 'UNPARSABLE')
    if unpars >= 2:
        c1b_verdict, c1b_why = 'UNDECIDABLE', '>=2 of 3 outputs unparsable'
    elif any(x['verdict'] == 'REJECT' for x in c1b_detail.values()):
        c1b_verdict, c1b_why = 'FAILURE', 'at least one applicability decision wrong'
    elif all(x['verdict'] == 'ACCEPT' for x in c1b_detail.values()):
        c1b_verdict, c1b_why = 'SUCCESS', 'applicability correct on all 3 with a valid conclusion'
    else:
        c1b_verdict, c1b_why = 'UNDECIDABLE', 'mixed outcome not resolvable'
    res['capabilities']['C1b'] = {'verdict': c1b_verdict, 'why': c1b_why, 'per_instance': c1b_detail,
                                  'binding_consistent': all(v['consistent'] for v in verify_c1b_binding().values())}

    # C1c
    c1c_outs = parsed_list('C1c-two-source')
    c1c_items = []
    for o in c1c_outs:
        vv, dd = A1.eval_c1c(A1.N7, o)
        c1c_items.append({'verdict': vv, 'cone_uses_both': dd.get('cone_uses_both_sources'),
                          'deletion_two_sided': dd.get('deletion_two_sided'),
                          'conclusion_ok': dd.get('conclusion_ok'), 'steps_ok': dd.get('steps_ok')})
    n_unp = len(by_task.get('C1c-two-source', [])) - len(c1c_outs)
    if n_unp >= 2:
        c1c_verdict, c1c_why = 'UNDECIDABLE', '>=2 of 3 outputs unparsable'
    elif any(x['verdict'] == 'ACCEPT' for x in c1c_items):
        c1c_verdict, c1c_why = 'SUCCESS', 'at least one output passed the frozen two-source check'
    elif c1c_items:
        c1c_verdict, c1c_why = 'FAILURE', 'no output satisfied conclusion + cone + two-sided deletion'
    else:
        c1c_verdict, c1c_why = 'UNDECIDABLE', 'no judgeable output'
    res['capabilities']['C1c'] = {'verdict': c1c_verdict, 'why': c1c_why, 'items': c1c_items,
                                  'unparsable': n_unp}

    res['ledger_validation'] = validate_ledger(led)
    json.dump(led, open(LEDGER_F, 'w'), indent=1)
    json.dump(res, open(RESULT_F, 'w'), indent=1)
    print('\n=== SUMMARY ===')
    for cap in ('C1a', 'C1b', 'C1c'):
        print('%-4s -> %s (%s)' % (cap, res['capabilities'][cap]['verdict'],
                                   res['capabilities'][cap]['why']))
    print('calls: primary=%d retries=%d timeouts=%d http4xx=%d | ledger ok=%s | aborted=%s'
          % (res['calls_primary'], res['calls_transport_retry'], res['timeouts'], res['http_4xx'],
             res['ledger_validation']['ok'], bool(aborted)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
