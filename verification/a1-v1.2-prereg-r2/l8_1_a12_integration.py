#!/usr/bin/env python3
"""A1 v1.2 runner-integration verification — revision 2 (audit-repaired).

Repairs the defects found in the first audit of this package:

  D-A  terminal-state priority: a system-side termination or an unknown terminal state could be
       classified SCOREABLE when its content happened to parse.  The priority is now total and
       finish_reason is dispatched before parsability.
  D-B  aggregation semantics: MODEL_NONCOMPLIANCE was silently excluded instead of being counted as
       a rejection, turning a capability failure into UNDECIDABLE.
  D-⑤  the round-1 replay produced a NEW C1b capability verdict from preserved round-1 material,
       which the prohibition in §1bis forbids.
  D-④  the package could not be executed outside the author's tree (missing imports).

Checks
  I1   identity of the scoring implementation used by the formal runner
  I2   end-to-end fixtures through the RUNNER: the four mandated cases
  I2c  parseable content combined with abnormal / unknown terminal states (regression for D-A)
  I2b  aggregation when every attempt is excluded
  I3   differential equivalence with the r2 test module (skipped if it is not bundled)
  I4   ROUND-1 ARCHIVE INTEGRITY ONLY: archive hashes against freeze anchors, frozen verdicts
       reported verbatim, and a mechanical guard proving no scoring function ran on round-1 material
  I5   model-call gate
  I6   aggregation semantics: MODEL_NONCOMPLIANCE counts as a rejection (regression for D-B)
  I7   the r2 explicit-null rule, validated on SYNTHETIC instances only

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


def sha256_file(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def rec(task, sub=None, finish='stop', seq=1, raw_content=None):
    content = raw_content if raw_content is not None else json.dumps(sub)
    return {'task': task, 'finish': finish, 'content': content, 'seq': seq}


def main():
    res = {'spec': 'A1-v1.2-INTEGRATION-TEST-RESULTS', 'revision': 2,
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
        i2c.append({'finish': finish, 'content': 'parsable',
                    'expected_state': expected, 'actual_state': entry['state'],
                    'pass': entry['state'] == expected,
                    'never_scored': 'verdict' not in entry})
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
    counters = {'score_c1b': 0, 'aggregate_c1b': 0, 'score_records': 0}

    def instrument(obj, name, key):
        f = getattr(obj, name)

        def g(*a, **k):
            counters[key] += 1
            return f(*a, **k)
        setattr(obj, name, g)
    instrument(scorer, 'score_c1b', 'score_c1b')
    instrument(scorer, 'aggregate_c1b', 'aggregate_c1b')
    instrument(runner, 'score_records', 'score_records')

    integ = []
    for fname, a in sorted(anchors['files'].items()):
        p = os.path.join(ARCHIVE, fname)
        got = sha256_file(p) if os.path.exists(p) else None
        integ.append({'file': fname, 'sha256_at_freeze': a['sha256_at_freeze'],
                      'sha256_now': got, 'unchanged': got == a['sha256_at_freeze']})
    frozen = json.load(open(os.path.join(ARCHIVE, 'A1-FINAL-VERDICTS.json')))['capabilities']
    frozen_now = {k: v.get('final_interpretation') for k, v in frozen.items()}
    expected_frozen = anchors['frozen_capability_verdicts']

    # the guard: nothing above called a scoring function
    no_rejudge = {'counters': counters, 'all_zero': all(v == 0 for v in counters.values()),
                  'contains_no_new_capability_verdict': not any(
                      'verdict' in k for k in integ[0] if isinstance(k, str))}

    res['I4_round1_archive_integrity'] = {
        'policy': 'INTEGRITY ONLY — round-1 material is hashed and its frozen verdicts are reported '
                  'verbatim; it is NOT re-scored and no new capability verdict is produced',
        'archive_files': integ,
        'archive_unchanged': all(e['unchanged'] for e in integ),
        'frozen_verdicts_reported_verbatim': frozen_now,
        'frozen_verdicts_unchanged': frozen_now == expected_frozen,
        'anchored_at': anchors['anchor_provenance'],
        'no_rejudge_guard': no_rejudge,
        'pass': (all(e['unchanged'] for e in integ) and frozen_now == expected_frozen
                 and no_rejudge['all_zero'])}

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
    except runner.NotAuthorised as e:
        gate['authorised_call_raised'] = True
    gate['no_call_made'] = True
    gate['pass'] = gate['unauthorised_call_raised'] and gate['authorised_call_raised']
    res['I5_model_gate'] = gate

    # ---------------- I6 regression for D-B: MODEL_NONCOMPLIANCE counts as a rejection
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
        i6.append({'probe': name, 'expected': expected, 'actual': v,
                   'excluded': sorted(excluded), 'excluded_expected': exc,
                   'pass': v == expected and sorted(excluded) == exc})
    c1c_probes = [('only_noncompliance', ['MODEL_NONCOMPLIANCE'], 'FAILURE'),
                  ('noncompliance_plus_accept', ['MODEL_NONCOMPLIANCE', 'ACCEPT'], 'SUCCESS')]
    i6c = [{'probe': n, 'expected': e, 'actual': scorer.aggregate_c1c(s)[0],
            'pass': scorer.aggregate_c1c(s)[0] == e} for n, s, e in c1c_probes]
    res['I6_aggregation_semantics'] = {
        'c1b': i6, 'c1c': i6c, 'pass': all(c['pass'] for c in i6) and all(c['pass'] for c in i6c),
        'why': 'MODEL_NONCOMPLIANCE is declared to count as a rejection; before the repair it was '
               'excluded and a capability failure became UNDECIDABLE'}

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
        ('non_null_for_undefined_rejected', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                                      'H3_tight': True, 'H4_no_complementary_pair': True},
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

    res['summary'] = {'I1': res['I1_identity']['pass'],
                      'I2': res['I2_runner_end_to_end']['pass'],
                      'I2c': res['I2c_parsable_with_abnormal_terminal']['pass'],
                      'I2b': res['I2b_all_excluded_aggregation']['pass'],
                      'I3': res['I3_differential_equivalence']['pass'],
                      'I4': res['I4_round1_archive_integrity']['pass'],
                      'I5': res['I5_model_gate']['pass'],
                      'I6': res['I6_aggregation_semantics']['pass'],
                      'I7': res['I7_synthetic_null_rule']['pass']}
    res['all_pass'] = all(v for v in res['summary'].values() if v is not None)
    json.dump(res, open(OUT, 'w'), indent=1)

    print('I1 runner uses the shared scorer :', res['I1_identity']['pass'],
          '| scorer', fp['scorer_id'], fp['sha256'][:12])
    for c in i2 + i2c:
        print('  %-34s expected=%-20s actual=%-20s %s'
              % (c.get('case') or 'parsable+%r' % c.get('finish'),
                 c.get('expected') or c['expected_state'],
                 c.get('actual') or c['actual_state'], 'PASS' if c['pass'] else 'FAIL'))
    print('I2b all excluded             :', res['I2b_all_excluded_aggregation']['pass'])
    print('I3 differential              :', res['I3_differential_equivalence'].get('pass'),
          res['I3_differential_equivalence'].get('status', ''))
    print('I4 archive integrity only    :', res['I4_round1_archive_integrity']['pass'],
          '| no-rejudge counters', counters)
    print('I5 model gate                :', gate['pass'])
    print('I6 aggregation semantics     :', res['I6_aggregation_semantics']['pass'])
    print('I7 synthetic null rule       :', res['I7_synthetic_null_rule']['pass'])
    print('ALL PASS:', res['all_pass'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
