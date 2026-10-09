#!/usr/bin/env python3
"""A1 v1.2 experiment runner.

The formal experiment path.  It imports the SHARED scorer module (`l8_1_a12_scorer`) and uses exactly
that implementation; `SCORE_C1B` below is the same function object, which the integration tests
assert.  Model calls are guarded: they raise unless explicitly authorised, so this runner performs
zero calls by default and can be exercised end to end on preserved or synthetic responses.

Usage
  python3 l8_1_a12_runner.py --replay <raw.jsonl> [--out <json>]     # no network
  python3 l8_1_a12_runner.py --selftest                              # built-in fixtures
"""
import argparse, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l8_1_a12_scorer as scorer

# ---- the single scoring implementation used by the formal path (identity asserted in tests) ----
SCORE_C1B = scorer.score_c1b
CLASSIFY = scorer.classify_response

TASKS_C1B = {'C1b-positive-applicable': 'N7', 'C1b-negative-not-tight': 'NOT_TIGHT',
             'C1b-negative-no-core': 'NO_CORE'}
TASKS_C1C = {'C1c-two-source'}


class NotAuthorised(RuntimeError):
    pass


def call_model(task_id, prompt, authorization=None):
    """Guarded model entry point.  Raises unless an explicit authorisation object is supplied.

    This exists so the formal path has a single, auditable place where a network call could occur.
    No call is made here, and none is authorised.
    """
    if not authorization or not authorization.get('model_calls_authorised'):
        raise NotAuthorised('model calls are NOT authorised; refusing to call for %s' % task_id)
    raise NotAuthorised('live calling is not implemented in this round (design-only path)')


def _instance(name):
    import l8_1_a1_evaluator as ev
    return ev.N7 if name == 'N7' else getattr(ev, name)


def score_records(records):
    """Score a list of records: {'task','finish','content','parsed'(optional),'seq'(optional)}.

    Returns a result dict with per-task states, verdicts and the excluded-attempt report.
    """
    per_task = {}
    detail = {}
    for r in records:
        task = r['task']
        state, why = CLASSIFY(r)
        entry = {'state': state, 'why': why, 'seq': r.get('seq')}
        if state == 'SCOREABLE':
            parsed = r.get('parsed')
            if parsed is None:
                from l8_1_a1_run import extract_json
                parsed = extract_json(r.get('content') or '')
            if task in TASKS_C1B:
                verdict, d = SCORE_C1B(_instance(TASKS_C1B[task]), parsed)
                entry['verdict'] = verdict
                entry['violations'] = d.get('violations', [])
                entry['constrained'] = d.get('constrained')
            elif task in TASKS_C1C:
                import l8_1_a1_evaluator as ev
                v, d = ev.eval_c1c(ev.N7, parsed)
                entry['verdict'] = v
            else:
                entry['verdict'] = 'UNSCORED_TASK'
        per_task.setdefault(task, []).append(entry)
        detail.setdefault(task, []).append(entry)

    c1b_per_instance = {}
    for task, name in TASKS_C1B.items():
        for e in per_task.get(task, []):
            c1b_per_instance[task] = e.get('verdict', e['state'])
    c1b_verdict, c1b_why, c1b_excluded = scorer.aggregate_c1b(c1b_per_instance) \
        if c1b_per_instance else ('UNDECIDABLE', 'no cross-domain records supplied', {})
    c1c_states = [e.get('verdict', e['state']) for e in per_task.get('C1c-two-source', [])]
    c1c_verdict, c1c_why = scorer.aggregate_c1c(c1c_states) if c1c_states \
        else ('UNDECIDABLE', 'no compositional records supplied')

    excluded = [e for lst in per_task.values() for e in lst
                if e['state'] in ('PARTIAL_TRUNCATED', 'MEASUREMENT_FAILURE', 'UNCLASSIFIED_RESPONSE')]
    return {'scorer': scorer.module_fingerprint(),
            'n_records': len(records),
            'per_task': per_task,
            'capabilities': {
                'C1b': {'verdict': c1b_verdict, 'why': c1b_why, 'per_instance': c1b_per_instance,
                        'excluded': c1b_excluded},
                'C1c': {'verdict': c1c_verdict, 'why': c1c_why, 'states': c1c_states}},
            'excluded_attempts': excluded,
            'excluded_count': len(excluded),
            'measurement_rate': (len(excluded) / len(records)) if records else None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--replay')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--out')
    a = ap.parse_args()
    if a.selftest:
        records = [{'task': 'C1b-negative-no-core', 'finish': 'stop', 'seq': 1,
                    'content': json.dumps({'hyps': {'H1_common_core': False, 'H2_uniform_size': True,
                                                    'H3_tight': None, 'H4_no_complementary_pair': None},
                                           'applicable': False, 'conclusion': None})}]
    elif a.replay:
        records = [json.loads(l) for l in open(a.replay)]
    else:
        ap.error('need --replay or --selftest')
    res = score_records(records)
    res['ran_at'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    if a.out:
        json.dump(res, open(a.out, 'w'), indent=1)
    print(json.dumps({'scorer': res['scorer'], 'n': res['n_records'],
                      'excluded': res['excluded_count'],
                      'C1b': res['capabilities']['C1b']['verdict'],
                      'C1c': res['capabilities']['C1c']['verdict']}, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
