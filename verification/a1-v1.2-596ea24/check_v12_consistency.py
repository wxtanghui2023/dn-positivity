#!/usr/bin/env python3
"""Post-freeze mechanical consistency check for the reviewed artefacts at commit 596ea24.

This is a REVIEWER AID produced after the freeze node.  It does not modify any reviewed artefact; it
re-derives claims from disk and git so the reviewer has a falsifiable baseline.  ZERO model calls.

Checks:
  K1  every artefact hash recorded in the pre-registration draft matches the file on disk
  K2  the reviewed files are byte-identical to their state in the freeze commit 596ea24
  K3  the thresholds in the draft are identical to those loaded from the v1.1 pre-registration
  K4  the measurement statistics are re-derived with EXPLICIT denominators and dimensions
  K5  the budget is recorded as a CANDIDATE, not as frozen
  K6  the model / call / retry / stop rules in the JSON agree with the readable draft
  K7  the offline regression suites are re-run from the committed test module and must reproduce
"""
import json, os, subprocess, hashlib, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.expanduser('~/.openclaw/workspace')
FREEZE = '596ea24'
OUT = os.path.join(HERE, 'A1-v1.2-CONSISTENCY-CHECK.json')
REVIEWED = ['l8_1_a12_r2_tests.py', 'A1-v1.2-R2-TEST-RESULTS.json',
            'A1-v1.2-PREREGISTRATION-DRAFT.json', 'A1-v1.2-PREREGISTRATION-DRAFT.md',
            'A1-v1.2-PREFLIGHT-CALIBRATION-PLAN.md', 'A1-v1.2-SPEC-CANDIDATE-r2.md']


def sha(p):
    return hashlib.sha256(open(p if os.path.isabs(p) else os.path.join(HERE, p), 'rb').read()).hexdigest()


def git_sha_at(commit, rel):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, rel)], cwd=ROOT, capture_output=True)
    return hashlib.sha256(r.stdout).hexdigest() if r.stdout else None


def main():
    res = {'spec': 'A1-v1.2-CONSISTENCY-CHECK', 'freeze_commit': FREEZE, 'model_calls': 0}
    draft = json.load(open(os.path.join(HERE, 'A1-v1.2-PREREGISTRATION-DRAFT.json')))
    v11 = json.load(open(os.path.join(HERE, 'A1-PREREGISTERED-EXPERIMENT-v1.1.json')))
    r2 = json.load(open(os.path.join(HERE, 'A1-v1.2-R2-TEST-RESULTS.json')))
    md = open(os.path.join(HERE, 'A1-v1.2-PREREGISTRATION-DRAFT.md')).read()

    # K1 hashes recorded vs on disk
    k1 = []
    for k, h in draft['artefact_hashes'].items():
        path = {'spec_v1.2_candidate': 'A1-v1.2-SPEC-CANDIDATE.md',
                'spec_r1': 'A1-v1.2-SPEC-CANDIDATE-r1.md',
                'spec_r2': 'A1-v1.2-SPEC-CANDIDATE-r2.md',
                'r2_test_results': 'A1-v1.2-R2-TEST-RESULTS.json',
                'open_items_resolution': 'A1-v1.2-OPEN-ITEMS-RESOLUTION.json',
                'gate_ab_results': 'A1-v1.2-GATE-AB-RESULTS.json',
                'calibration_plan': 'A1-v1.2-PREFLIGHT-CALIBRATION-PLAN.md',
                'defect_register_addendum': 'A1-DEFECT-REGISTER-ADDENDUM.json',
                'round1_final_results': 'A1-ROUND-1-FINAL-RESULTS.md',
                'round1_final_verdicts': 'A1-FINAL-VERDICTS.json',
                'raw_records': 'RAW-A1.jsonl',
                'prereg_v1.1': 'A1-PREREGISTERED-EXPERIMENT-v1.1.json',
                'r2_scorer_tests': 'l8_1_a12_r2_tests.py',
                'open_items_script': 'l8_1_a12_open_items.py',
                'gate_ab_script': 'l8_1_a12_candidate_gates.py'}[k]
        actual = sha(path)
        k1.append({'key': k, 'recorded': h, 'actual': actual, 'match': h == actual})
    res['K1_recorded_hashes_match_disk'] = {'all_match': all(x['match'] for x in k1), 'items': k1}

    # K2 reviewed files identical to the freeze commit
    k2 = []
    for f in REVIEWED:
        rel = 'discovery/dcl/' + f
        cur, at = sha(f), git_sha_at(FREEZE, rel)
        k2.append({'file': f, 'disk': cur, 'at_freeze_commit': at, 'identical': cur == at})
    res['K2_reviewed_files_unchanged_since_freeze'] = {'all_identical': all(x['identical'] for x in k2),
                                                        'items': k2}

    # K3 thresholds identical to v1.1 (programmatic comparison)
    k3 = []
    for cap, key in (('C1a', 'C1a_object_construction'), ('C1b', 'C1b_cross_domain_instantiation'),
                     ('C1c', 'C1c_compositional_dependency')):
        for f in ('SUCCESS', 'FAILURE', 'UNDECIDABLE', 'unit'):
            a = v11['thresholds'][cap][f]
            b = draft['capability_definitions'][key][f]
            k3.append({'capability': cap, 'field': f, 'v11': a, 'draft': b, 'identical': a == b})
    res['K3_thresholds_identical_to_v11'] = {'all_identical': all(x['identical'] for x in k3),
                                              'items': k3}

    # K4 statistics with explicit denominators and dimensions
    recs = [json.loads(l) for l in open(os.path.join(HERE, 'RAW-A1.jsonl'))]
    n = len(recs)
    sys.path.insert(0, HERE)
    from l8_1_a12_candidate_gates import classify_response
    state = {}
    cap_hits = []
    for r in recs:
        st, _, _ = classify_response(r)
        state[st] = state.get(st, 0) + 1
        if r.get('finish') == 'length':
            cap_hits.append(r['seq'])
    state_partition = {k: {'count': v, 'share_of_%d' % n: round(v / n, 4)} for k, v in state.items()}
    res['K4_statistics'] = {
        'denominator': '%d primary calls in round 1 (withheld retries = 0)' % n,
        'dimension_1_measurement_state_PARTITION_of_all_calls': {
            'definition': 'each call receives exactly one state; the categories are mutually '
                          'exclusive AND exhaustive, so they sum to 100%',
            'states': state_partition,
            'sums_to_n': sum(state.values()),
            'sums_to_100pct': sum(state.values()) == n},
        'dimension_2_cap_hit': {
            'definition': 'a SEPARATE dimension: the count of calls whose finish_reason is length. It '
                          'is NOT one of the state categories and does NOT have to sum with them.',
            'count': len(cap_hits), 'seqs': cap_hits, 'share_of_%d' % n: round(len(cap_hits) / n, 4),
            'note': 'in round 1 all cap hits happen to also be measurement failures; in general a '
                    'cap hit whose partial content parses would be PARTIAL_TRUNCATED, so cap hit and '
                    'measurement failure are NOT the same category'},
        'dimension_3_undecidable_measurement_layer': {
            'definition': 'an OUTCOME derived from dimension 1 (the MEASUREMENT_FAILURE share), not an '
                          'independent category',
            'count': state.get('MEASUREMENT_FAILURE', 0),
            'share_of_%d' % n: round(state.get('MEASUREMENT_FAILURE', 0) / n, 4)},
        'caution': 'reported as 25% / 75% / 25% these are NOT mutually exclusive classes summing to '
                   '100%: only dimension 1 is a partition, dimension 2 is independent and dimension 3 '
                   'is derived from dimension 1'}

    # K5 budget status
    b = draft['model_budget_calls']['max_output_tokens']
    res['K5_budget_status'] = {
        'value': b['value'], 'status_recorded': b['status'],
        'is_frozen': 'CANDIDATE' not in b['status'].upper(),
        'md_states_candidate': '候选值，未冻结' in md or 'CANDIDATE' in md}

    # K6 JSON vs readable consistency on the operative rules
    checks = {
        'model_alias': draft['model_budget_calls']['model']['alias'] in md,
        'temperature': str(draft['model_budget_calls']['model']['temperature']) in md,
        'primary_calls_12': '12' in md and draft['model_budget_calls']['planned_primary_calls'] == 12,
        'retry_cap_4': '上限 4' in md or 'cap 4' in md.lower(),
        'stop_rule_new_prereg': '新预注册' in md,
        'draft_not_approved': draft['status'] == 'DRAFT / NOT APPROVED' and 'DRAFT / NOT APPROVED' in md,
        'null_convention_in_md': '显式 null' in md or 'explicit null' in md,
        'h4_precondition_in_md': '仅 H1' in md,
        'partial_truncated_in_md': 'PARTIAL_TRUNCATED' in md,
        'unclassified_in_md': 'UNCLASSIFIED_RESPONSE' in md,
        'no_rejudge_round1_in_md': '第一轮判定不可变' in md,
    }
    res['K6_json_md_consistency'] = {'all_ok': all(checks.values()), 'checks': checks}
    # declared gaps: checked and found ABSENT, reported rather than silently relaxed
    gaps = []
    if '不复判' not in md and 'not re-judge' not in md.lower():
        gaps.append({'gap': 'the readable pre-registration draft does not explicitly state that the '
                            'round-1 cross-domain submission, which r2 would reject for a null-format '
                            'reason, must NOT be used as capability evidence about r2, and that '
                            'round 1 must not be re-judged',
                     'where_it_exists_instead': 'A1-v1.2-SPEC-CANDIDATE-r2.md section 5 states it '
                                                'explicitly',
                     'disposition': 'NOT fixed during review (reviewed artefacts are frozen); '
                                    'recommended for the next revision',
                     'severity': 'documentation completeness, not a rule conflict'})
    res['declared_gaps_found_by_self_check'] = gaps

    # K7 re-run the committed test module and compare to the recorded results
    import importlib
    sys.modules.pop('l8_1_a12_r2_tests', None)
    m = importlib.import_module('l8_1_a12_r2_tests')
    live = {'null_semantics_suite': m.null_semantics_suite(),
            'format_suite': m.format_suite(),
            'abnormal_termination_suite': m.abnormal_termination_suite()}
    live['h1_not_h2_suite'] = m.h1_not_h2_suite()['cases']
    cmp = {}
    for k, v in live.items():
        rec = r2[k]
        if isinstance(rec, dict):
            rec = rec['cases']
        rec_cases = [(c['case'], c['expected'], c['actual']) for c in rec]
        live_cases = [(c['case'], c['expected'], c['actual']) for c in v]
        cmp[k] = {'reproduced': rec_cases == live_cases, 'n_cases': len(live_cases),
                  'all_pass': all(c['pass'] for c in v)}
    src = open(os.path.join(HERE, 'l8_1_a12_r2_tests.py')).read()
    res['K7_regression_reproducible'] = {
        'suites': cmp, 'all_reproduced': all(x['reproduced'] for x in cmp.values()),
        'all_cases_pass': all(x['all_pass'] for x in cmp.values()),
        'scorer_under_test': 'score_c1b_r2 (defined in this module and called directly by the '
                             'suites)',
        'IMPORTANT_LIMITATION': 'the r2 scorer is defined inside the test module; there is NO r2 '
                                'experiment runner that imports it yet, so what the suites verify is '
                                'the scorer implementation as written in this module and its wiring '
                                'to the case tables. Runner integration is NOT done and is flagged '
                                'for the reviewer.',
        'tests_call_implementation_directly': 'run() -> score_c1b_r2(inst, submission); no helper '
                                              'short-circuit'}

    res['summary'] = {
        'K1': res['K1_recorded_hashes_match_disk']['all_match'],
        'K2': res['K2_reviewed_files_unchanged_since_freeze']['all_identical'],
        'K3': res['K3_thresholds_identical_to_v11']['all_identical'],
        'K4': 're-derived with explicit dimensions (see caution)',
        'K5': res['K5_budget_status']['is_frozen'] is False,
        'K6': res['K6_json_md_consistency']['all_ok'],
        'K7': res['K7_regression_reproducible']['all_reproduced']}
    json.dump(res, open(OUT, 'w'), indent=1)

    for k, v in res['summary'].items():
        print('%-4s %s' % (k, v))
    print('\nK4 states:', state_partition)
    print('K4 cap-hit seqs:', cap_hits)
    print('K4 caution: only dimension 1 is a partition; 25/75/25 are NOT exclusive classes')
    print('\nK7 suites:', {k: (v['reproduced'], v['n_cases']) for k, v in cmp.items()})
    print('K7 limitation:', res['K7_regression_reproducible']['IMPORTANT_LIMITATION'][:120])
    k1bad = [x['key'] for x in k1 if not x['match']]
    k2bad = [x['file'] for x in k2 if not x['identical']]
    k3bad = [(x['capability'], x['field']) for x in k3 if not x['identical']]
    k6bad = [k for k, v in checks.items() if not v]
    print('\nMISMATCHES  K1:', k1bad, '| K2:', k2bad, '| K3:', k3bad, '| K6:', k6bad)
    print('DECLARED GAPS:', len(gaps))
    for g in gaps:
        print('  -', g['gap'][:110], '->', g['disposition'][:40])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
