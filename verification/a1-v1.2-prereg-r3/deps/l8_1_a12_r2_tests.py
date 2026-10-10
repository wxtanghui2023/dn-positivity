#!/usr/bin/env python3
"""A1 v1.2 candidate r2 — explicit-null semantics + offline regression suites.

ZERO model calls, ZERO network.  Nothing frozen is modified; this script only reads frozen artefacts
and writes its own new results file.

Field semantics fixed by the 2026-10-09 21:37 ruling:
  true / false : the judgement value of a DEFINED hypothesis
  null         : the hypothesis is UNDEFINED under this instance's preconditions
  missing field: output incomplete / format violation -- MUST NOT be equated with null
  defined hypothesis   -> must be present, boolean, and correct
  undefined hypothesis -> must be explicitly null; otherwise handled by the frozen format rules

Separately enforced: explicit null solves OUTPUT AMBIGUITY only. It does not make the scorer
mathematically correct, so each hypothesis keeps its own definability condition and truth logic. In
particular the H1=true / H2=false branch must require H3=null AND still evaluate H4 by its own
definition (H4 must NOT be ignored).
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l8_1_a1_evaluator as A1
from l8_1_a12_open_items import hyp_truth_corrected, H1_NOT_H2
from l8_1_a12_candidate_gates import classify_response
from l8_1_a1_run import extract_json

OUT = os.path.join(HERE, 'A1-v1.2-R2-TEST-RESULTS.json')
HYP = A1.LEMMA_HYPS


# ================================================================ r2 truth (one condition per hypothesis)
def hyp_truth_r2(inst):
    return hyp_truth_corrected(inst)


# ================================================================ r2 scorer
def score_c1b_r2(inst, sub):
    t = hyp_truth_r2(inst)
    v = []
    if not isinstance(sub, dict):
        return 'REJECT', {'violations': ['submission is not a JSON object']}
    hyps = sub.get('hyps')
    if not isinstance(hyps, dict):
        v.append('hyps object missing or malformed')
    else:
        for h in HYP:
            present = h in hyps
            val = hyps.get(h)
            defined = t[h] is not None
            if defined:
                if not present:
                    v.append('missing DEFINED field %s (missing != null)' % h)
                elif not isinstance(val, bool):
                    v.append('defined field %s must be boolean true/false (got %r)' % (h, val))
                elif bool(val) != bool(t[h]):
                    v.append('wrong %s (submitted %s, truth %s)' % (h, val, t[h]))
            else:
                if not present:
                    v.append('UNDEFINED field %s missing; the null convention requires an explicit '
                             'null (missing != null)' % h)
                elif val is not None:
                    v.append('UNDEFINED field %s must be explicit null (got %r)' % (h, val))
        for h in hyps:
            if h not in HYP:
                pass  # unknown extra keys are ignored by policy (recorded below)
    if 'applicable' not in sub:
        v.append('missing applicable')
    elif not isinstance(sub['applicable'], bool):
        v.append('applicable must be boolean (got %r)' % (sub['applicable'],))
    elif bool(sub['applicable']) != bool(t['applicable']):
        v.append('wrong applicable (submitted %s, truth %s)' % (sub['applicable'], t['applicable']))
    c = sub.get('conclusion', None)
    if t['applicable']:
        if c is None:
            v.append('conclusion must be an integer when applicable (got null)')
        elif isinstance(c, bool) or not isinstance(c, int):
            v.append('conclusion must be an integer when applicable (got %r)' % (c,))
        elif not (3 <= c <= (t['tau_star'] or 0)):
            v.append('conclusion %r outside [3, %s]' % (c, t['tau_star']))
    else:
        if c is not None:
            v.append('conclusion must be null when not applicable (got %r)' % (c,))
    return ('ACCEPT' if not v else 'REJECT'), {
        'violations': v, 'truth': t,
        'defined': [h for h in HYP if t[h] is not None],
        'undefined_requiring_null': [h for h in HYP if t[h] is None],
        'unknown_extra_keys_ignored': [h for h in (sub.get('hyps') or {}) if h not in HYP]}


# ================================================================ suites
def null_semantics_suite():
    cases = [
        ('N1_no_core_all_nulls_correct', 'NO_CORE',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True, 'H3_tight': None,
                   'H4_no_complementary_pair': None}, 'applicable': False, 'conclusion': None},
         'ACCEPT'),
        ('N2_no_core_undefined_missing', 'NO_CORE',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True},
          'applicable': False, 'conclusion': None}, 'REJECT'),
        ('N3_no_core_undefined_answered_false', 'NO_CORE',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True, 'H3_tight': False,
                   'H4_no_complementary_pair': None}, 'applicable': False, 'conclusion': None},
         'REJECT'),
        ('N4_no_core_undefined_answered_true', 'NO_CORE',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True, 'H3_tight': None,
                   'H4_no_complementary_pair': True}, 'applicable': False, 'conclusion': None},
         'REJECT'),
        ('N5_positive_all_true', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 3}, 'ACCEPT'),
        ('N6_positive_defined_field_null', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': None}, 'applicable': True, 'conclusion': 3}, 'REJECT'),
        ('N7_not_tight_correct', 'NOT_TIGHT',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': False,
                   'H4_no_complementary_pair': True}, 'applicable': False, 'conclusion': None},
         'ACCEPT'),
        ('N8_defined_field_missing', 'NOT_TIGHT',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True,
                   'H4_no_complementary_pair': True}, 'applicable': False, 'conclusion': None},
         'REJECT'),
        ('N9_unknown_extra_key_ignored', 'NOT_TIGHT',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': False,
                   'H4_no_complementary_pair': True, 'H9_spurious': 123},
          'applicable': False, 'conclusion': None}, 'ACCEPT'),
        ('N10_applicable_wrong_type', 'NOT_TIGHT',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': False,
                   'H4_no_complementary_pair': True}, 'applicable': 'no', 'conclusion': None},
         'REJECT'),
    ]
    return run(cases)


def h1_not_h2_suite():
    cases = [
        ('B1_branch_correct', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                        'H3_tight': None, 'H4_no_complementary_pair': True},
                               'applicable': False, 'conclusion': None}, 'ACCEPT'),
        ('B2_branch_wrong_H4', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                         'H3_tight': None, 'H4_no_complementary_pair': False},
                                'applicable': False, 'conclusion': None}, 'REJECT'),
        ('B3_branch_H3_missing', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                           'H4_no_complementary_pair': True},
                                  'applicable': False, 'conclusion': None}, 'REJECT'),
        ('B4_branch_H3_answered_false', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                                  'H3_tight': False, 'H4_no_complementary_pair': True},
                                         'applicable': False, 'conclusion': None}, 'REJECT'),
        ('B5_branch_H4_missing', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                           'H3_tight': None}, 'applicable': False, 'conclusion': None},
         'REJECT'),
        ('B6_branch_H4_null_when_defined', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                                     'H3_tight': None,
                                                     'H4_no_complementary_pair': None},
                                            'applicable': False, 'conclusion': None}, 'REJECT'),
        ('B7_branch_claims_applicable', {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                                  'H3_tight': None,
                                                  'H4_no_complementary_pair': True},
                                         'applicable': True, 'conclusion': 3}, 'REJECT'),
    ]
    clear = hyp_truth_r2(H1_NOT_H2)
    res = run([(n, '_', s, e) for n, s, e in cases], inst=H1_NOT_H2)
    return {'cases': res, 'pass': all(c['pass'] for c in res), 'truth': clear}


def format_suite():
    cases = [
        ('F1_hyps_missing', 'N7', {'applicable': True, 'conclusion': 3}, 'REJECT'),
        ('F2_hyps_not_object', 'N7', {'hyps': [1, 2], 'applicable': True, 'conclusion': 3}, 'REJECT'),
        ('F3_not_an_object', 'N7', [1, 2, 3], 'REJECT'),
        ('F4_applicable_missing', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'conclusion': 3}, 'REJECT'),
        ('F5_conclusion_bool_true', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': True}, 'REJECT'),
        ('F6_conclusion_absent_when_not_applicable', 'NOT_TIGHT',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': False,
                   'H4_no_complementary_pair': True}, 'applicable': False}, 'ACCEPT'),
    ]
    return run(cases)


def abnormal_termination_suite():
    cases = [
        ('A1_finish_content_filter_parsable', {'finish': 'content_filter', 'content': '{"a":1}'},
         'SCOREABLE'),
        ('A2_finish_content_filter_empty', {'finish': 'content_filter', 'content': ''},
         'MEASUREMENT_FAILURE'),
        ('A3_finish_error_empty', {'finish': 'error', 'content': ''}, 'MEASUREMENT_FAILURE'),
        ('A4_finish_absent_parsable', {'finish': None, 'content': '{"a":1}'}, 'SCOREABLE'),
        ('A5_finish_unknown_empty', {'finish': 'something_new', 'content': ''},
         'UNCLASSIFIED_RESPONSE'),
        ('A6_finish_length_parsable', {'finish': 'length', 'content': '{"a":1}'},
         'PARTIAL_TRUNCATED'),
    ]

    def classify_ext(rec):
        finish = rec.get('finish')
        content = rec.get('content') or ''
        parsed = extract_json(content)
        if parsed is not None and finish == 'length':
            return 'PARTIAL_TRUNCATED'
        if parsed is not None:
            return 'SCOREABLE'
        if finish == 'length':
            return 'MEASUREMENT_FAILURE'
        if finish in ('content_filter', 'error', None):
            return 'MEASUREMENT_FAILURE'   # system-side termination, not a model compliance failure
        if finish == 'stop':
            return 'MODEL_NONCOMPLIANCE'
        return 'UNCLASSIFIED_RESPONSE'
    out = []
    for name, rec, exp in cases:
        st = classify_ext(rec)
        out.append({'case': name, 'expected': exp, 'actual': st, 'pass': st == exp,
                    'note': 'new finish_reason values must be classified by a declared rule, not '
                            'silently mapped'})
    return out


def run(cases, inst=None):
    out = []
    for name, inst_name, sub, exp in cases:
        i = inst if inst is not None else (A1.N7 if inst_name == 'N7' else A1.__dict__[inst_name])
        v, d = score_c1b_r2(i, sub)
        out.append({'case': name, 'expected': exp, 'actual': v, 'pass': v == exp,
                    'violations': d.get('violations', [])})
    return out


# ================================================================ round-1 replay under r2
def round1_under_r2():
    name = {'C1b-positive-applicable': 'N7', 'C1b-negative-not-tight': 'NOT_TIGHT',
            'C1b-negative-no-core': 'NO_CORE'}
    out = {}
    for r in [json.loads(l) for l in open(os.path.join(HERE, 'RAW-A1.jsonl'))]:
        if r['task'] in name:
            nm = name[r['task']]
            inst = A1.N7 if nm == 'N7' else A1.__dict__[nm]
            v, d = score_c1b_r2(inst, r['parsed'])
            out[r['task']] = {'verdict': v, 'violations': d.get('violations', [])}
    return {'per_instance': out,
            'status': 'DIAGNOSTIC ONLY. r2 is a NEW version; it does NOT and MUST NOT re-judge '
                      'round 1. The v1.1 prompt never asked for an explicit null, so any rejection '
                      'here is a FORMAT-COMPLIANCE difference under a convention that did not exist '
                      'in round 1; it is NOT a capability statement.'}


# ================================================================ measurement quality rates
def measurement_rates():
    recs = [json.loads(l) for l in open(os.path.join(HERE, 'RAW-A1.jsonl'))]
    counts = {'SCOREABLE': 0, 'PARTIAL_TRUNCATED': 0, 'MEASUREMENT_FAILURE': 0,
              'MODEL_NONCOMPLIANCE': 0}
    cap_hits = 0
    for r in recs:
        st, _, _ = classify_response(r)
        counts[st] = counts.get(st, 0) + 1
        if r.get('finish') == 'length':
            cap_hits += 1
    n = len(recs)
    return {'round1_n': n, 'classifications': counts,
            'cap_hit_rate': cap_hits / n,
            'scoreable_rate': counts['SCOREABLE'] / n,
            'measurement_failure_rate': counts['MEASUREMENT_FAILURE'] / n,
            'undecidable_rate_measurement': counts['MEASUREMENT_FAILURE'] / n,
            'note': 'the three rates must be reported separately; a larger budget is NOT itself '
                    'evidence of success'}


def main():
    res = {'spec': 'A1-v1.2-R2-TEST-RESULTS', 'model_calls': 0, 'network_access': 'none',
           'field_semantics': {'true_false': 'judgement value of a DEFINED hypothesis',
                               'null': 'hypothesis UNDEFINED under this instance preconditions',
                               'missing': 'incomplete output / format violation; missing != null',
                               'defined_rule': 'present, boolean, correct',
                               'undefined_rule': 'explicit null required; else frozen format rules'},
           'null_semantics_suite': null_semantics_suite(),
           'h1_not_h2_suite': h1_not_h2_suite(),
           'format_suite': format_suite(),
           'status_to_scoring_r2': {
               'SCOREABLE': 'score normally',
               'PARTIAL_TRUNCATED': 'EXCLUDED from the capability verdict; reported as a separate '
                                    'completeness stratum (neither SUCCESS nor FAILURE)',
               'MEASUREMENT_FAILURE': 'UNDECIDABLE (never FAILURE, never SUCCESS)',
               'MODEL_NONCOMPLIANCE': 'counts as a rejection (capability failure)',
               'UNCLASSIFIED_RESPONSE': 'UNDECIDABLE + flagged for human review; an unknown '
                                        'finish_reason or an unrecognised termination mode must '
                                        'never be silently mapped to a capability verdict'},
           'abnormal_termination_suite': abnormal_termination_suite(),           'round1_under_r2': round1_under_r2(),
           'measurement_rates_round1': measurement_rates()}
    for k in ('null_semantics_suite', 'format_suite', 'abnormal_termination_suite'):
        res[k + '_pass'] = all(c['pass'] for c in res[k])
    res['h1_not_h2_suite_pass'] = res['h1_not_h2_suite']['pass']
    json.dump(res, open(OUT, 'w'), indent=1)

    print('=== r2 null-semantics suite ===')
    for c in res['null_semantics_suite']:
        print('  %-42s expect=%-6s actual=%-6s %s' % (c['case'], c['expected'], c['actual'],
                                                      'PASS' if c['pass'] else 'FAIL'))
        if c['violations']:
            print('        %s' % c['violations'])
    print('=== r2 H1=true / H2=false branch ===')
    print('  truth:', res['h1_not_h2_suite']['truth'])
    for c in res['h1_not_h2_suite']['cases']:
        print('  %-42s expect=%-6s actual=%-6s %s' % (c['case'], c['expected'], c['actual'],
                                                      'PASS' if c['pass'] else 'FAIL'))
    print('=== r2 format suite ===')
    for c in res['format_suite']:
        print('  %-42s expect=%-6s actual=%-6s %s' % (c['case'], c['expected'], c['actual'],
                                                      'PASS' if c['pass'] else 'FAIL'))
    print('=== abnormal termination ===')
    for c in res['abnormal_termination_suite']:
        print('  %-42s expect=%-20s actual=%-20s %s' % (c['case'], c['expected'], c['actual'],
                                                        'PASS' if c['pass'] else 'FAIL'))
    print('=== round-1 submissions under r2 (diagnostic only) ===')
    for k, v in res['round1_under_r2']['per_instance'].items():
        print('  %-28s %-6s %s' % (k, v['verdict'], v['violations'][:1]))
    print('=== measurement rates (round 1) ===')
    print(' ', res['measurement_rates_round1'])
    print('SUITE PASS:  null=%s branch=%s format=%s abnormal=%s'
          % (res['null_semantics_suite_pass'], res['h1_not_h2_suite_pass'],
             res['format_suite_pass'], res['abnormal_termination_suite_pass']))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
