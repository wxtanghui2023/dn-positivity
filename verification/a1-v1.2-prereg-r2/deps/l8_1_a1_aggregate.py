#!/usr/bin/env python3
"""L8-1 A1 RUN-LEVEL AGGREGATION (pre-registration v1.1 amendments) — zero model calls.

IMPORTANT: this module does NOT modify A1-SCORER-v1.  It sits ON TOP of the frozen scorer and
implements only the run-level rules the operator required in the 18:48 review:

  Gap A  C1a distinct-object counting : every output is judged individually by the frozen scorer;
         passing outputs are canonicalised; the SAME canonical object counts ONCE; SUCCESS needs
         >= 3 DISTINCT valid new objects AND the infeasible control correctly handled.
  Gap B  global retry ledger          : the retry cap is a GLOBAL cap for the whole experiment;
         every primary call and retry records seq / trigger / params digest / result / time;
         retries must reuse the original parameters; transport retries may never become content
         retries; a failed control blocks C1a SUCCESS regardless of positive-example counts.
  C1b    explicit expected applicability per instance, bound to the scoring rules in machine
         readable form (positive => applicable; not-tight => non-applicable; no-core => non-applicable).

Self-test uses SYNTHETIC submissions only (no model output, no model call).
"""
import json, os, sys, hashlib, itertools
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l8_1_a1_evaluator as A1

# ---------------------------------------------------------------- C1b expected applicability (frozen binding)
C1B_EXPECTED = {
    'C1b-positive-applicable': {'instance': 'N7', 'expected_applicable': True,
                                'allowed_output': 'hyps all true, applicable=true, conclusion=3'},
    'C1b-negative-not-tight':  {'instance': 'NOT_TIGHT', 'expected_applicable': False,
                                'allowed_output': 'H3_tight=false, applicable=false, conclusion=null'},
    'C1b-negative-no-core':    {'instance': 'NO_CORE', 'expected_applicable': False,
                                'allowed_output': 'H1_common_core=false, applicable=false, conclusion=null'},
}


def verify_c1b_binding():
    """the frozen binding must agree with the scorer's own hypothesis truth (self-consistency)."""
    out = {}
    for tid, spec in C1B_EXPECTED.items():
        t = A1.hyp_truth(A1.__dict__[spec['instance']] if spec['instance'] != 'N7' else A1.N7)
        out[tid] = {'bound_expected_applicable': spec['expected_applicable'],
                    'scorer_computed_applicable': t['applicable'],
                    'consistent': spec['expected_applicable'] == t['applicable']}
    return out


# ---------------------------------------------------------------- Gap A : C1a distinct counting
def judge_c1a_run(lib, outputs, constraint='feasible_nocore'):
    """outputs = list of parsed-or-None submission dicts (None = unparsable).
    Returns per-attempt records + distinct valid object count."""
    per = []
    seen = set()
    distinct = []
    unparsable = 0
    for i, s in enumerate(outputs):
        if s is None:
            unparsable += 1
            per.append({'attempt': i + 1, 'status': 'UNPARSABLE'})
            continue
        v, d = A1.eval_c1a(lib, s, constraint)
        if v == 'ACCEPT':
            c = A1.canon([frozenset(b) for b in s['blocks']], s['n'])
            if c in seen:
                per.append({'attempt': i + 1, 'status': 'VALID-DUPLICATE'})
            else:
                seen.add(c)
                distinct.append(c)
                per.append({'attempt': i + 1, 'status': 'VALID-DISTINCT'})
        else:
            per.append({'attempt': i + 1, 'status': v})
    return {'per_attempt': per, 'distinct_valid': len(distinct), 'unparsable': unparsable,
            'valid_attempts': sum(1 for p in per if p['status'].startswith('VALID'))}


def judge_infeasible_control(output):
    """correct handling = declaring infeasibility.  Emitting any block family = CONTROL FAILURE."""
    if output is None:
        return 'UNDECIDABLE', 'unparsable'
    if isinstance(output, dict) and output.get('infeasible') is True:
        return 'OK', 'declared infeasible'
    return 'CONTROL-FAILURE', 'emitted a block family for a provably empty constraint'


def verdict_c1a(lib, outputs, control_output, threshold_distinct=3, unparsable_undecidable=3):
    run = judge_c1a_run(lib, outputs)
    ctl, ctl_why = judge_infeasible_control(control_output)
    if run['unparsable'] >= unparsable_undecidable:
        verdict, why = 'UNDECIDABLE', '>=%d unparsable outputs' % unparsable_undecidable
    elif ctl == 'UNDECIDABLE':
        verdict, why = 'UNDECIDABLE', 'control output unparsable'
    elif ctl == 'CONTROL-FAILURE':
        verdict, why = 'FAILURE', 'infeasible control failure blocks SUCCESS (gating rule)'
    elif run['distinct_valid'] >= threshold_distinct:
        verdict, why = 'SUCCESS', '>=%d DISTINCT valid new objects and control ok' % threshold_distinct
    else:
        verdict, why = 'FAILURE', 'only %d distinct valid object(s) < %d' % (
            run['distinct_valid'], threshold_distinct)
    return {'verdict': verdict, 'why': why, 'distinct_valid': run['distinct_valid'],
            'valid_attempts': run['valid_attempts'], 'control': ctl, 'control_why': ctl_why,
            'per_attempt': run['per_attempt']}


# ---------------------------------------------------------------- Gap B : global retry ledger
def new_ledger():
    return {'entries': [], 'global_retry_cap': 4, 'max_total_calls': 16,
            'allowed_retry_triggers': ['http_5xx', 'transport_error'],
            'forbidden_retry_triggers': ['timeout', 'unparsable_content', 'wrong_content', 'other']}


def add_entry(ledger, seq, kind, task_id, trigger, params_digest, original_digest, result_code, ts):
    ledger['entries'].append({'seq': seq, 'kind': kind, 'task_id': task_id, 'trigger': trigger,
                              'params_digest': params_digest, 'original_params_digest': original_digest,
                              'params_identical': params_digest == original_digest,
                              'result_code': result_code, 'timestamp': ts})


def validate_ledger(ledger):
    e = ledger['entries']
    retries = [x for x in e if x['kind'] == 'transport_retry']
    problems = []
    if len(retries) > ledger['global_retry_cap']:
        problems.append('retries %d exceed the GLOBAL cap %d' % (len(retries), ledger['global_retry_cap']))
    if len(e) > ledger['max_total_calls']:
        problems.append('total calls %d exceed %d' % (len(e), ledger['max_total_calls']))
    for x in retries:
        if x['trigger'] not in ledger['allowed_retry_triggers']:
            problems.append('retry seq %s has forbidden trigger %s' % (x['seq'], x['trigger']))
        if not x['params_identical']:
            problems.append('retry seq %s did not reuse the original parameters' % x['seq'])
    for x in e:
        if x['kind'] not in ('primary', 'transport_retry'):
            problems.append('entry seq %s has unknown kind %s' % (x['seq'], x['kind']))
    return {'ok': not problems, 'problems': problems, 'n_entries': len(e),
            'n_retries': len(retries)}


# ---------------------------------------------------------------- self-test (synthetic only)
def _find_valid_objects(lib, k, seed=11):
    import random
    rng = random.Random(seed)
    known = set(x['canon'] for x in lib if x['n'] == 7)
    out = []
    for _ in range(20000):
        blocks = set()
        while len(blocks) < 9:
            blocks.add(frozenset(rng.sample(range(7), rng.randint(2, 4))))
        blocks = sorted(blocks, key=sorted)
        if set.intersection(*[set(b) for b in blocks]):
            continue
        if A1.tau_star(blocks, 7) is None:
            continue
        c = A1.canon(blocks, 7)
        if c in known or c in [x[0] for x in out]:
            continue
        out.append((c, {'n': 7, 'blocks': [sorted(b) for b in blocks]}))
        if len(out) >= k:
            break
    return [o[1] for o in out]


def main():
    rep = {'spec': 'L8-1-A1-AGGREGATION-SELFTEST', 'model_calls': 0}
    lib = A1.build_library()
    print('=== run-level aggregation self-test (synthetic submissions) ===')

    # C1b binding self-consistency
    b = verify_c1b_binding()
    rep['c1b_binding'] = b
    print('\n[C1b binding] expected applicability bound to the scoring rules:')
    for k, v in b.items():
        print('  %-28s expected=%-5s scorer=%-5s consistent=%s'
              % (k, v['bound_expected_applicable'], v['scorer_computed_applicable'], v['consistent']))

    distinct = _find_valid_objects(lib, 5)
    ctl_ok = {'infeasible': True, 'reason': 'two blocks of at most two points cannot cover five'}
    ctl_bad = {'n': 5, 'blocks': [[0, 1], [2, 3]]}
    scen = {}
    scen['S1_three_distinct_ok'] = verdict_c1a(lib, distinct[:3], ctl_ok)
    scen['S2_three_duplicates'] = verdict_c1a(lib, [distinct[0]] * 3, ctl_ok)
    scen['S3_distinct_but_control_failed'] = verdict_c1a(lib, distinct[:3], ctl_bad)
    scen['S4_unparsable'] = verdict_c1a(lib, [None, None, None], ctl_ok)
    scen['S5_two_distinct'] = verdict_c1a(lib, distinct[:2], ctl_ok)
    print('\n[C1a Gap A + gating]')
    for k, v in scen.items():
        print('  %-32s -> %-12s distinct=%s unparsable=%s control=%-15s (%s)'
              % (k, v['verdict'], v['distinct_valid'], sum(1 for p in v['per_attempt']
                 if p['status'] == 'UNPARSABLE'), v['control'], v['why']))

    led = new_ledger()
    add_entry(led, 1, 'primary', 'C1a-feasible-1', None, 'd1', 'd1', 'ok', 't0')
    add_entry(led, 2, 'transport_retry', 'C1a-feasible-1', 'http_5xx', 'd1', 'd1', 'ok', 't1')
    ok_led = validate_ledger(led)
    bad1 = new_ledger()
    for i in range(5):
        add_entry(bad1, i + 1, 'transport_retry', 'T', 'http_5xx', 'd', 'd', 'ok', 't')
    bad2 = new_ledger()
    add_entry(bad2, 1, 'transport_retry', 'T', 'unparsable_content', 'd', 'd', 'ok', 't')
    bad3 = new_ledger()
    add_entry(bad3, 1, 'transport_retry', 'T', 'http_5xx', 'd2', 'd1', 'ok', 't')
    ledg = {'valid_ledger_ok': ok_led, 'retries_over_global_cap': validate_ledger(bad1),
            'content_retry_forbidden': validate_ledger(bad2),
            'params_changed_forbidden': validate_ledger(bad3)}
    rep['c1a_scenarios'] = scen
    rep['ledger_checks'] = ledg
    print('\n[Gap B global retry ledger]')
    print('  valid ledger (1 primary + 1 transport retry)        -> ok=%s' % ok_led['ok'])
    for k in ('retries_over_global_cap', 'content_retry_forbidden', 'params_changed_forbidden'):
        print('  %-20s -> ok=%-5s problems=%s' % (k, ledg[k]['ok'], ledg[k]['problems']))

    ok = (all(v['consistent'] for v in b.values())
          and scen['S1_three_distinct_ok']['verdict'] == 'SUCCESS'
          and scen['S2_three_duplicates']['verdict'] == 'FAILURE'
          and scen['S3_distinct_but_control_failed']['verdict'] == 'FAILURE'
          and scen['S4_unparsable']['verdict'] == 'UNDECIDABLE'
          and scen['S5_two_distinct']['verdict'] == 'FAILURE'
          and ok_led['ok'] and not ledg['retries_over_global_cap']['ok']
          and not ledg['content_retry_forbidden']['ok'] and not ledg['params_changed_forbidden']['ok'])
    rep['selftest_pass'] = ok
    json.dump(rep, open(os.path.join(HERE, 'A1-AGGREGATION-SELFTEST.json'), 'w'), indent=1)
    print('\n=== aggregation self-test %s ===' % ('PASS' if ok else 'FAIL'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
