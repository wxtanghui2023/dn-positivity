#!/usr/bin/env python3
"""A1 v1.2 runner-integration verification — revision 3 (audit-repaired).

Repairs found in the second audit:
  D-⑤b  the no-rejudge guard shared a mutable counter with the later I6/I7 checks, so the recorded
        "all zero" boolean was taken at an earlier instant while the serialised counters had been
        incremented to 3/5/0 by later tests; and the "no new capability verdict" assertion inspected
        the keys of an unrelated list element instead of the actual I4 output.
  Fixes: a round-1-dedicated counter, an immutable snapshot taken while armed, the guarded functions
  restored immediately afterwards, later-phase calls counted separately and labelled, a structural
  assertion over the real I4 result, and a negative control that deliberately re-judges a round-1
  record — the guard MUST detect it, otherwise I4 fails.
  Revision 4 closes two residual gaps: the forbidden-key scan now runs against the ASSEMBLED I4
  object (twice, before and after populating its own fields) and `pass` depends on it, with a
  positive control proving the scanner detects injected keys; and `runner.SCORE_C1B` — bound to the
  scorer at import time — is now counted and exercised too, so the negative control demonstrates an
  increment for EVERY scoring entry point rather than only the ones it happened to call.

Checks
  I1 identity of the scoring implementation used by the formal runner
  I2 the four mandated end-to-end cases through the RUNNER
  I2c parseable content with abnormal / unknown terminal states (D-A regression)
  I2b aggregation when every attempt is excluded
  I3 differential equivalence with the r2 test module (not applicable if it is not bundled)
  I4 ROUND-1 ARCHIVE INTEGRITY ONLY + a live, self-checking no-rejudge guard
  I5 model-call gate
  I6 aggregation semantics: MODEL_NONCOMPLIANCE counts as a rejection (D-B regression)
  I7 the r2 explicit-null rule, validated on SYNTHETIC instances only

Zero model calls, zero network.  Runs from a clean directory.
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (HERE, os.path.join(HERE, 'deps')):
    if os.path.isdir(_p) and _p not in sys.path:
        sys.path.insert(0, _p)

import l8_1_a12_scorer as scorer
import l8_1_a12_runner as runner
import l8_1_a1_evaluator as ev
from l8_1_a1_run import extract_json

try:
    import l8_1_a12_r2_tests as r2tests
    HAVE_R2 = True
except Exception:
    r2tests, HAVE_R2 = None, False

OUT = os.path.join(HERE, 'A1-v1.2-INTEGRATION-TEST-RESULTS.json')
ARCHIVE = os.path.join(HERE, 'ROUND1-ARCHIVE')

# keys that would indicate a capability verdict had been produced from round-1 material
VERDICT_KEYS = ('C1b_verdict', 'C1c_verdict', 'verdict', 'capabilities', 'per_instance')


def sha256_file(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def rec(task, sub=None, finish='stop', seq=1, raw_content=None):
    content = raw_content if raw_content is not None else json.dumps(sub)
    return {'task': task, 'finish': finish, 'content': content, 'seq': seq}


def find_verdict_keys(obj, path=''):
    """structural search for capability-verdict keys anywhere in an object.

    Paths are built without a leading separator so that reported locations are clean (the earlier
    version emitted '.nest.per_instance', which made exact comparisons against expected locations
    fail even when detection itself worked).
    """
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            sub = ('%s.%s' % (path, k)) if path else k
            if k in VERDICT_KEYS:
                hits.append(sub)
            hits += find_verdict_keys(v, sub)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += find_verdict_keys(v, '%s[%d]' % (path, i))
    return hits


def inspect_round1(archive, anchors):
    """the permitted round-1 inspection: hashes and frozen verdicts only.  NEVER scores."""
    files = []
    for fname, a in sorted(anchors['files'].items()):
        p = os.path.join(archive, fname)
        got = sha256_file(p) if os.path.exists(p) else None
        files.append({'file': fname, 'sha256_at_freeze': a['sha256_at_freeze'],
                      'sha256_now': got, 'unchanged': got == a['sha256_at_freeze']})
    frozen = json.load(open(os.path.join(archive, 'A1-FINAL-VERDICTS.json')))['capabilities']
    return {'archive_files': files,
            'archive_unchanged': all(e['unchanged'] for e in files),
            'frozen_verdicts_reported_verbatim': {k: v.get('final_interpretation')
                                                  for k, v in frozen.items()}}


def rejudge_control(archive):
    """NEGATIVE CONTROL: deliberately exercise EVERY guarded scoring entry point.

    The preserved round-1 record is pushed through the runner exactly as the prohibited behaviour
    would, and each entry point is invoked so that the guard must register an increment for all of
    them.  Every value produced here is DISCARDED and is never reported as a capability verdict; only
    the guard deltas are recorded.  `runner.SCORE_C1B` is bound to the scorer at import time, so it
    needs its own wrapper and its own exercise.
    """
    raw = [json.loads(l) for l in open(os.path.join(archive, 'RAW-A1.jsonl'))]
    GOOD = {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                     'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 3}
    out = runner.score_records(raw[:1])        # entry point: runner.score_records
    runner.SCORE_C1B(ev.N7, GOOD)              # entry point: runner.SCORE_C1B (import-time binding)
    scorer.score_c1b(ev.N7, GOOD)              # entry point: scorer.score_c1b
    scorer.aggregate_c1b({'ctrl': 'ACCEPT'})   # entry point: scorer.aggregate_c1b
    return type(out).__name__


def main():
    res = {'spec': 'A1-v1.2-INTEGRATION-TEST-RESULTS', 'revision': 4,
           'model_calls': 0, 'network': 'none',
           'purpose': 'verify that the formal runner scores through the shared r2 scorer, and that '
                      'no scoring function is applied to round-1 material'}

    # ---------------- I1 identity
    fp = scorer.module_fingerprint()
    res['I1_identity'] = {
        'runner_SCORE_C1B_is_scorer_score_c1b': runner.SCORE_C1B is scorer.score_c1b,
        'runner_classify_is_scorer_classify': runner.CLASSIFY is scorer.classify_response,
        'scorer_id': fp['scorer_id'], 'scorer_module_path': fp['path'],
        'scorer_module_sha256': fp['sha256'],
        'pass': (runner.SCORE_C1B is scorer.score_c1b
                 and runner.CLASSIFY is scorer.classify_response)}

    # ---------------- I2 the four mandated end-to-end cases through the runner
    cases = [
        ('D1_defined_field_error', 'C1b-positive-applicable',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': False,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 3},
         'stop', 'REJECT'),
        ('D2_null_required_violation', 'C1b-negative-no-core',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True, 'H3_tight': None,
                   'H4_no_complementary_pair': True}, 'applicable': False, 'conclusion': None},
         'stop', 'REJECT'),
        ('D3_truncated_but_parsable', 'C1b-positive-applicable',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 3},
         'length', 'PARTIAL_TRUNCATED'),
        ('D4_abnormal_termination', 'C1c-two-source', None, 'content_filter', 'MEASUREMENT_FAILURE'),
        ('D5_correct_scoreable', 'C1b-negative-no-core',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True, 'H3_tight': None,
                   'H4_no_complementary_pair': None}, 'applicable': False, 'conclusion': None},
         'stop', 'ACCEPT'),
    ]
    i2 = []
    for name, task, sub, finish, expected in cases:
        out = runner.score_records([rec(task, sub, finish, seq=1,
                                        raw_content='' if sub is None else None)])
        entry = out['per_task'][task][0]
        got = entry.get('verdict', entry['state'])
        i2.append({'case': name, 'expected': expected, 'actual': got, 'pass': got == expected,
                   'state': entry['state']})
    res['I2_runner_end_to_end'] = {'cases': i2, 'pass': all(c['pass'] for c in i2)}

    # ---------------- I2c regression for D-A: PARSABLE content with abnormal / unknown terminals
    GOOD = {'hyps': {'H1_common_core': False, 'H2_uniform_size': True, 'H3_tight': None,
                     'H4_no_complementary_pair': None}, 'applicable': False, 'conclusion': None}
    i2c = []
    for finish, expected in [('content_filter', 'MEASUREMENT_FAILURE'), ('error', 'MEASUREMENT_FAILURE'),
                             (None, 'MEASUREMENT_FAILURE'), ('mystery', 'UNCLASSIFIED_RESPONSE')]:
        out = runner.score_records([rec('C1b-negative-no-core', GOOD, finish, seq=1)])
        entry = out['per_task']['C1b-negative-no-core'][0]
        i2c.append({'finish': finish, 'content': 'parsable', 'expected_state': expected,
                    'actual_state': entry['state'],
                    'pass': entry['state'] == expected, 'never_scored': 'verdict' not in entry})
    res['I2c_parsable_with_abnormal_terminal'] = {
        'cases': i2c, 'pass': all(c['pass'] and c['never_scored'] for c in i2c),
        'why': 'a system-side termination or an unknown terminal state must never be scored, even '
               'when the content parses (previously it returned SCOREABLE)'}

    # ---------------- I2b every attempt excluded
    out = runner.score_records([rec('C1c-two-source', None, 'length', seq=1, raw_content=''),
                                rec('C1c-two-source', None, 'length', seq=2, raw_content='')])
    res['I2b_all_excluded_aggregation'] = {
        'C1c_verdict': out['capabilities']['C1c']['verdict'],
        'pass': out['capabilities']['C1c']['verdict'] == 'UNDECIDABLE'
                and all(e['state'] == 'MEASUREMENT_FAILURE'
                        for e in out['per_task']['C1c-two-source'])}

    # ---------------- I3 differential equivalence with the r2 test module
    if HAVE_R2:
        diff = {'checked': 0, 'mismatches': []}
        subs = [
            ('N7', {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                             'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 3}),
            ('NO_CORE', {'hyps': {'H1_common_core': False, 'H2_uniform_size': True,
                                  'H3_tight': None, 'H4_no_complementary_pair': None},
                         'applicable': False, 'conclusion': None}),
            ('NOT_TIGHT', {'hyps': {'H1_common_core': True, 'H2_uniform_size': True,
                                    'H3_tight': False, 'H4_no_complementary_pair': True},
                           'applicable': False, 'conclusion': None}),
            ('NOT_TIGHT', {'hyps': {'H1_common_core': True, 'H2_uniform_size': True,
                                    'H4_no_complementary_pair': True}, 'applicable': False,
                           'conclusion': None}),
            ('N7', {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                             'H4_no_complementary_pair': None}, 'applicable': True, 'conclusion': 3}),
            ('N7', {'applicable': True, 'conclusion': 3}),
            ('N7', [1, 2, 3]),
        ]
        for instname, sub in subs:
            inst = ev.N7 if instname == 'N7' else getattr(ev, instname)
            a = scorer.score_c1b(inst, sub)[0]
            b = r2tests.score_c1b_r2(inst, sub)[0]
            diff['checked'] += 1
            if a != b:
                diff['mismatches'].append({'instance': instname, 'shared': a, 'test_module': b})
        diff['pass'] = not diff['mismatches']
        res['I3_differential_equivalence'] = diff
    else:
        res['I3_differential_equivalence'] = {
            'pass': None, 'status': 'SKIPPED_UNAVAILABLE',
            'why': 'the r2 test module is not bundled next to this script'}

    # ---------------- I4 ROUND-1 ARCHIVE INTEGRITY ONLY (no re-judging)
    anchors = json.load(open(os.path.join(ARCHIVE, 'ANCHORS.json')))
    ENTRY_POINTS = ('score_records', 'runner_SCORE_C1B', 'score_c1b', 'aggregate_c1b')
    guard = {k: 0 for k in ENTRY_POINTS}
    _orig = {'score_c1b': scorer.score_c1b, 'aggregate_c1b': scorer.aggregate_c1b,
             'score_records': runner.score_records, 'SCORE_C1B': runner.SCORE_C1B}

    def _wrap(f, key):
        def g(*a, **k):
            guard[key] += 1
            return f(*a, **k)
        return g

    def _arm():
        scorer.score_c1b = _wrap(_orig['score_c1b'], 'score_c1b')
        scorer.aggregate_c1b = _wrap(_orig['aggregate_c1b'], 'aggregate_c1b')
        runner.score_records = _wrap(_orig['score_records'], 'score_records')
        runner.SCORE_C1B = _wrap(_orig['SCORE_C1B'], 'runner_SCORE_C1B')

    def _disarm():
        scorer.score_c1b = _orig['score_c1b']
        scorer.aggregate_c1b = _orig['aggregate_c1b']
        runner.score_records = _orig['score_records']
        runner.SCORE_C1B = _orig['SCORE_C1B']

    _arm()
    r1 = inspect_round1(ARCHIVE, anchors)          # phase 1: the permitted inspection only
    snapshot = dict(guard)                         # IMMUTABLE snapshot, taken while armed
    try:
        control_type = rejudge_control(ARCHIVE)    # phase 2: the deliberate violation
        control_err = None
    except Exception as e:
        control_type, control_err = None, '%s: %s' % (type(e).__name__, str(e)[:60])
    delta = {k: guard[k] - snapshot[k] for k in guard}
    _disarm()                                      # restored immediately: later checks are separate

    # assemble the COMPLETE I4 object, then scan THAT object
    i4 = {
        'policy': 'INTEGRITY ONLY — round-1 material is hashed and its frozen verdicts are reported '
                  'verbatim; it is NOT re-scored and no new capability verdict is produced',
        'archive_files': r1['archive_files'],
        'archive_unchanged': r1['archive_unchanged'],
        'frozen_verdicts_reported_verbatim': r1['frozen_verdicts_reported_verbatim'],
        'frozen_verdicts_unchanged': (r1['frozen_verdicts_reported_verbatim']
                                      == anchors['frozen_capability_verdicts']),
        'anchored_at': anchors['anchor_provenance'],
        'no_rejudge_guard': {
            'counter_scope': 'dedicated to the round-1 phase; taken as an immutable snapshot before '
                             'the negative control, and every guarded function is restored '
                             'immediately afterwards so later checks cannot alter this record',
            'monitored_entry_points': list(ENTRY_POINTS),
            'round1_phase_snapshot': snapshot,
            'all_zero_in_round1_phase': all(v == 0 for v in snapshot.values()),
            'negative_control': {
                'what': 'push one preserved round-1 record through the runner, as the prohibited '
                        'behaviour would, and invoke every guarded entry point; all outputs are '
                        'discarded',
                'returned': control_type, 'error': control_err,
                'guard_delta': delta,
                'detected': all(delta[k] >= 1 for k in ENTRY_POINTS)},
            'guard_is_live_for_every_entry_point': all(delta[k] >= 1 for k in ENTRY_POINTS),
            'scanned_object': "the assembled res['I4_round1_archive_integrity'] object",
            'forbidden_keys_found': None,
            'contains_no_new_capability_verdict': None,
            'rescan_after_population_clean': None,
            'structural_scan_control': None,
        },
    }
    forbidden = find_verdict_keys(i4)              # scan #1: the assembled object
    i4['no_rejudge_guard']['forbidden_keys_found'] = forbidden
    i4['no_rejudge_guard']['contains_no_new_capability_verdict'] = not forbidden
    forbidden_again = find_verdict_keys(i4)        # scan #2: after its own fields are populated
    i4['no_rejudge_guard']['rescan_after_population_clean'] = (not forbidden_again)
    scan_control = find_verdict_keys({'C1b_verdict': 'FAILURE', 'nest': {'per_instance': {}}})
    want = ['C1b_verdict', 'nest.per_instance']
    i4['no_rejudge_guard']['structural_scan_control'] = {
        'injected_keys': want, 'found': sorted(scan_control),
        'detects_injected_keys': sorted(scan_control) == sorted(want)}
    ng = i4['no_rejudge_guard']
    i4['pass'] = bool(i4['archive_unchanged'] and i4['frozen_verdicts_unchanged']
                      and ng['all_zero_in_round1_phase']
                      and ng['guard_is_live_for_every_entry_point']
                      and ng['contains_no_new_capability_verdict']
                      and ng['rescan_after_population_clean']
                      and ng['structural_scan_control']['detects_injected_keys'])
    res['I4_round1_archive_integrity'] = i4

    # ---------------- I5 model gate
    gate = {}
    try:
        runner.call_model('C1b-positive-applicable', 'prompt')
        gate['unauthorised_call_raised'] = False
    except runner.NotAuthorised as e:
        gate['unauthorised_call_raised'] = True
        gate['message'] = str(e)[:70]
    try:
        runner.call_model('C1b-positive-applicable', 'prompt', {'model_calls_authorised': True})
        gate['authorised_call_raised'] = False
    except runner.NotAuthorised:
        gate['authorised_call_raised'] = True
    gate['no_call_made'] = True
    gate['pass'] = gate['unauthorised_call_raised'] and gate['authorised_call_raised']
    res['I5_model_gate'] = gate

    # ---------------- I6 regression for D-B: counted SEPARATELY (outside the round-1 guard)
    later = {k: 0 for k in ENTRY_POINTS}
    _lo = {'score_c1b': scorer.score_c1b, 'aggregate_c1b': scorer.aggregate_c1b,
           'score_records': runner.score_records, 'SCORE_C1B': runner.SCORE_C1B}

    def _later(f, key):
        def g(*a, **k):
            later[key] += 1
            return f(*a, **k)
        return g
    scorer.score_c1b = _later(_lo['score_c1b'], 'score_c1b')
    scorer.aggregate_c1b = _later(_lo['aggregate_c1b'], 'aggregate_c1b')
    runner.score_records = _later(_lo['score_records'], 'score_records')
    runner.SCORE_C1B = _later(_lo['SCORE_C1B'], 'runner_SCORE_C1B')

    probes = [
        ('only_noncompliance', {'t': 'MODEL_NONCOMPLIANCE'}, 'FAILURE', []),
        ('noncompliance_plus_accept', {'t': 'MODEL_NONCOMPLIANCE', 'u': 'ACCEPT'}, 'FAILURE', []),
        ('noncompliance_plus_reject', {'t': 'MODEL_NONCOMPLIANCE', 'u': 'REJECT'}, 'FAILURE', []),
        ('all_accept', {'t': 'ACCEPT', 'u': 'ACCEPT'}, 'SUCCESS', []),
        ('accept_plus_measurement_failure', {'t': 'ACCEPT', 'u': 'MEASUREMENT_FAILURE'},
         'UNDECIDABLE', ['u']),
    ]
    i6 = []
    for name, pi, expected, exc in probes:
        v, why, excluded = scorer.aggregate_c1b(pi)
        i6.append({'probe': name, 'expected': expected, 'actual': v, 'excluded': sorted(excluded),
                   'pass': v == expected and sorted(excluded) == exc})
    i6c = [{'probe': n, 'expected': e, 'actual': scorer.aggregate_c1c(s)[0],
            'pass': scorer.aggregate_c1c(s)[0] == e}
           for n, s, e in [('only_noncompliance', ['MODEL_NONCOMPLIANCE'], 'FAILURE'),
                           ('noncompliance_plus_accept', ['MODEL_NONCOMPLIANCE', 'ACCEPT'],
                            'SUCCESS')]]
    scorer.score_c1b, scorer.aggregate_c1b = _lo['score_c1b'], _lo['aggregate_c1b']
    runner.score_records, runner.SCORE_C1B = _lo['score_records'], _lo['SCORE_C1B']
    res['I6_aggregation_semantics'] = {
        'c1b': i6, 'c1c': i6c, 'pass': all(c['pass'] for c in i6) and all(c['pass'] for c in i6c),
        'scoring_calls_during_I6': dict(later),
        'why': 'MODEL_NONCOMPLIANCE is declared to count as a rejection; before the repair it was '
               'excluded and a capability failure became UNDECIDABLE',
        'note': 'these calls are made by the I6 probes themselves and are counted in a separate, '
                'clearly labelled counter — they do NOT belong to the round-1 phase'}

    # ---------------- I7 the r2 explicit-null rule on SYNTHETIC instances
    synth = {'n': 7, 'blocks': [[0, 1, 2], [0, 3], [0, 4, 5], [0, 6]], 'label': 'SYNTH-H1-NOT-H2'}
    tr = scorer.hyp_truth(synth)
    syn = []
    for name, sub, expected in [
        ('explicit_null_accepted', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                             'H3_tight': None, 'H4_no_complementary_pair': True},
                                    'applicable': False, 'conclusion': None}, 'ACCEPT'),
        ('missing_null_field_rejected', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                                  'H4_no_complementary_pair': True},
                                         'applicable': False, 'conclusion': None}, 'REJECT'),
        ('non_null_for_undefined_rejected', {'hyps': {'H1_common_core': True,
                                                      'H2_uniform_size': False, 'H3_tight': True,
                                                      'H4_no_complementary_pair': True},
                                             'applicable': False, 'conclusion': None}, 'REJECT'),
    ]:
        v, d = scorer.score_c1b(synth, sub)
        syn.append({'case': name, 'expected': expected, 'actual': v, 'pass': v == expected,
                    'violations': d['violations'][:2]})
    res['I7_synthetic_null_rule'] = {
        'instance': 'synthetic (built in this script, not a frozen instance)',
        'synthetic_truth': {k: tr[k] for k in scorer.HYP} | {'applicable': tr['applicable']},
        'undefined_hyps_requiring_null': [h for h in scorer.HYP if tr[h] is None],
        'cases': syn, 'pass': all(c['pass'] for c in syn),
        'why': 'the repaired behaviour of the new rule is validated on synthetic data only, so it '
               'never requires re-scoring round-1 material'}

    # the I4 record must not have been altered by the later phases
    res['I4_record_stable_after_later_phases'] = (
        res['I4_round1_archive_integrity']['no_rejudge_guard']['round1_phase_snapshot'] == snapshot)

    res['summary'] = {'I1': res['I1_identity']['pass'],
                      'I2': res['I2_runner_end_to_end']['pass'],
                      'I2c': res['I2c_parsable_with_abnormal_terminal']['pass'],
                      'I2b': res['I2b_all_excluded_aggregation']['pass'],
                      'I3': res['I3_differential_equivalence']['pass'],
                      'I4': i4['pass'], 'I5': res['I5_model_gate']['pass'],
                      'I6': res['I6_aggregation_semantics']['pass'],
                      'I7': res['I7_synthetic_null_rule']['pass'],
                      'I4_stable': res['I4_record_stable_after_later_phases']}
    res['all_pass'] = all(v for v in res['summary'].values() if v is not None)
    json.dump(res, open(OUT, 'w'), indent=1)

    print('I1 runner uses the shared scorer :', res['I1_identity']['pass'],
          '| scorer', fp['scorer_id'], fp['sha256'][:12])
    for c in i2 + i2c:
        print('  %-34s expected=%-20s actual=%-20s %s'
              % (c.get('case') or 'parsable+%r' % c.get('finish'),
                 c.get('expected') or c['expected_state'],
                 c.get('actual') or c['actual_state'], 'PASS' if c['pass'] else 'FAIL'))
    g = i4['no_rejudge_guard']
    print('I4 integrity only            :', i4['pass'],
          '| round-1 snapshot', g['round1_phase_snapshot'])
    print('   entry points monitored    :', g['monitored_entry_points'],
          '| control delta', g['negative_control']['guard_delta'],
          '| detected', g['negative_control']['detected'])
    print('   assembled-object scan     :', g['contains_no_new_capability_verdict'],
          '| rescan clean', g['rescan_after_population_clean'],
          '| scanner control', g['structural_scan_control']['detects_injected_keys'])
    print('I5 model gate                :', gate['pass'])
    print('I6 aggregation semantics     :', res['I6_aggregation_semantics']['pass'],
          '| calls', res['I6_aggregation_semantics']['scoring_calls_during_I6'])
    print('I7 synthetic null rule       :', res['I7_synthetic_null_rule']['pass'])
    print('I4 record stable             :', res['I4_record_stable_after_later_phases'])
    print('ALL PASS:', res['all_pass'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
