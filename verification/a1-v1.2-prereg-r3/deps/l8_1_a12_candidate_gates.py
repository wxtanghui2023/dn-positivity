#!/usr/bin/env python3
"""A1 v1.2 CANDIDATE — Gate A (spec-scorer consistency) and Gate B (capacity/completeness).

ZERO model calls, ZERO network access.  Nothing frozen is modified: this file implements a NEW
candidate scorer/parser (v1.2) alongside regression suites, and writes its own results file.

Gate A fixes DEFECT-3 by giving every hypothesis an explicit PRECONDITION: a hypothesis is
"defined" only when its precondition holds, and the scorer constrains ONLY defined hypotheses.
Undefined hypotheses are IGNORED (any value, or absent) — the scorer must never check a field the
pre-registration does not require the model to answer.

Gate B classifies a raw response as SCOREABLE / MEASUREMENT_FAILURE / MODEL_NONCOMPLIANCE so that a
capacity boundary can never masquerade as a capability failure.
"""
import json, os, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l8_1_a1_evaluator as A1
from l8_1_a1_run import extract_json


# ================================================================ GATE A : v1.2 C1b field spec
HYP_PRECOND = {                       # explicit dependency structure (NEW in v1.2)
    'H1_common_core': lambda t: True,
    'H2_uniform_size': lambda t: True,
    'H3_tight': lambda t: t['H1_common_core'] and t['H2_uniform_size'],
    'H4_no_complementary_pair': lambda t: t['H1_common_core'] and t['H2_uniform_size'],
}
C1B_V12 = {
    'N7': {'constrained': ['H1_common_core', 'H2_uniform_size', 'H3_tight',
                           'H4_no_complementary_pair', 'applicable', 'conclusion']},
    'NOT_TIGHT': {'constrained': ['H1_common_core', 'H2_uniform_size', 'H3_tight',
                                  'H4_no_complementary_pair', 'applicable', 'conclusion']},
    'NO_CORE': {'constrained': ['H1_common_core', 'H2_uniform_size', 'applicable', 'conclusion']},
}
UNCONSTRAINED_POLICY = 'IGNORED (may be any value or absent)'


def defined_hypotheses(truth):
    return [h for h, pre in HYP_PRECOND.items() if pre(truth)]


def score_c1b_v12(inst_name, inst, sub):
    """v1.2 field-level scoring.  Returns (verdict, detail)."""
    t = A1.hyp_truth(inst)
    constrained = C1B_V12[inst_name]['constrained']
    defined = defined_hypotheses(t)
    reasons = []
    if not isinstance(sub, dict):
        return 'REJECT', {'why': 'not a JSON object', 'constrained': constrained}
    # 1) constrained hypotheses must be present and correct
    for h in constrained:
        if h.startswith('H'):
            if h not in sub.get('hyps', {}):
                reasons.append('missing constrained field %s' % h)
            elif bool(sub['hyps'][h]) != bool(t[h]):
                reasons.append('wrong value for %s (submitted %s, truth %s)'
                               % (h, sub['hyps'][h], t[h]))
    # 2) applicable must be present and correct
    if 'applicable' not in sub:
        reasons.append('missing field applicable')
    elif bool(sub['applicable']) != bool(t['applicable']):
        reasons.append('wrong applicable (submitted %s, truth %s)' % (sub['applicable'], t['applicable']))
    # 3) conclusion
    concl = sub.get('conclusion', None)
    if t['applicable']:
        if t['tau_star'] is None:
            reasons.append('instance not coverable: cannot validate a conclusion')
        elif not isinstance(concl, int):
            reasons.append('conclusion must be an integer when applicable (got %r)' % (concl,))
        elif not (3 <= concl <= t['tau_star']):
            reasons.append('conclusion %s outside the valid range [3, %s]' % (concl, t['tau_star']))
    else:
        if concl not in (None,):
            reasons.append('conclusion must be null when the lemma does not apply (got %r)' % (concl,))
    ignored = [h for h in A1.LEMMA_HYPS if h not in constrained]
    detail = {'constrained': constrained, 'defined': defined, 'ignored': ignored,
              'ignored_policy': UNCONSTRAINED_POLICY, 'violations': reasons,
              'applicability_correct': (sub.get('applicable') == t['applicable'])
              if 'applicable' in sub else False}
    return ('ACCEPT' if not reasons else 'REJECT'), detail


def gate_a_suite():
    cases = [
        ('A1_positive_all_correct', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 3}, 'ACCEPT'),
        ('A2_defect3_regression_no_core', 'NO_CORE',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True, 'H3_tight': False,
                   'H4_no_complementary_pair': True}, 'applicable': False, 'conclusion': None}, 'ACCEPT'),
        ('A3_unconstrained_field_absent', 'NO_CORE',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True}, 'applicable': False,
          'conclusion': None}, 'ACCEPT'),
        ('A4_missing_constrained_field', 'NO_CORE',
         {'hyps': {'H1_common_core': False}, 'applicable': False, 'conclusion': None}, 'REJECT'),
        ('A5_overclaim_not_tight', 'NOT_TIGHT',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 3}, 'REJECT'),
        ('A6_wrong_conclusion_above_optimum', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 5}, 'REJECT'),
        ('A7_unconstrained_garbage_ignored', 'NO_CORE',
         {'hyps': {'H1_common_core': False, 'H2_uniform_size': True, 'H3_tight': 'nonsense',
                   'H4_no_complementary_pair': ['x']}, 'applicable': False, 'conclusion': None}, 'ACCEPT'),
        ('A8_not_tight_all_correct', 'NOT_TIGHT',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': False,
                   'H4_no_complementary_pair': True}, 'applicable': False, 'conclusion': None}, 'ACCEPT'),
        ('A9_boundary_conclusion_exactly_optimum', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 3}, 'ACCEPT'),
        ('A10_boundary_conclusion_below_lemma_content', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': 2}, 'REJECT'),
        ('A11_applicable_but_null_conclusion', 'N7',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': True, 'conclusion': None}, 'REJECT'),
        ('A12_wrong_defined_hypothesis', 'NOT_TIGHT',
         {'hyps': {'H1_common_core': True, 'H2_uniform_size': True, 'H3_tight': True,
                   'H4_no_complementary_pair': True}, 'applicable': False, 'conclusion': None}, 'REJECT'),
    ]
    out = []
    for name, inst_name, sub, expected in cases:
        inst = A1.N7 if inst_name == 'N7' else A1.__dict__[inst_name]
        v, d = score_c1b_v12(inst_name, inst, sub)
        out.append({'case': name, 'instance': inst_name, 'expected': expected, 'actual': v,
                    'pass': v == expected, 'violations': d.get('violations', []),
                    'constrained': d.get('constrained'), 'ignored': d.get('ignored')})
    return out


# ================================================================ GATE B : capacity / completeness
def classify_response(rec):
    """v1.2 measurement-status classifier."""
    finish = rec.get('finish')
    content = rec.get('content') or ''
    stripped = content.strip()
    parsed = extract_json(content)
    if finish == 'length' and not stripped:
        return 'MEASUREMENT_FAILURE', 'output budget exhausted before any content was emitted', None
    if finish == 'length' and parsed is None:
        return 'MEASUREMENT_FAILURE', 'content truncated at the output cap and not parsable', None
    if parsed is not None:
        return 'SCOREABLE', 'parsable submission', parsed
    if finish == 'stop' and not stripped:
        return 'MODEL_NONCOMPLIANCE', 'empty content with finish_reason=stop', None
    return 'MODEL_NONCOMPLIANCE', 'unparsable content with finish_reason=%s' % finish, None


STATUS_TO_SCORING = {
    'SCOREABLE': 'score normally',
    'MEASUREMENT_FAILURE': 'UNDECIDABLE (never FAILURE, never SUCCESS)',
    'MODEL_NONCOMPLIANCE': 'counts as a rejection (capability failure)',
}


def gate_b_suite():
    cases = [
        ('B1_empty_at_cap', {'finish': 'length', 'content': ''}, 'MEASUREMENT_FAILURE'),
        ('B2_truncated_json_at_cap', {'finish': 'length', 'content': '{"sources": ["S_tight"'}, 'MEASUREMENT_FAILURE'),
        ('B3_complete_json_stop', {'finish': 'stop', 'content': '{"a": 1}'}, 'SCOREABLE'),
        ('B4_prose_then_json', {'finish': 'stop', 'content': 'Here is the answer:\n{"a": 1}\nDone.'}, 'SCOREABLE'),
        ('B5_fenced_json', {'finish': 'stop', 'content': '```json\n{"a": 1}\n```'}, 'SCOREABLE'),
        ('B6_garbage_stop', {'finish': 'stop', 'content': 'I cannot solve this.'}, 'MODEL_NONCOMPLIANCE'),
        ('B7_whitespace_stop', {'finish': 'stop', 'content': '   \n  '}, 'MODEL_NONCOMPLIANCE'),
        ('B8_truncated_prose_at_cap', {'finish': 'length', 'content': 'Let me think about the'}, 'MEASUREMENT_FAILURE'),
    ]
    out = []
    for name, rec, expected in cases:
        st, why, parsed = classify_response(rec)
        out.append({'case': name, 'expected': expected, 'actual': st, 'pass': st == expected,
                    'why': why, 'scoring_rule': STATUS_TO_SCORING[st]})
    return out


def gate_b_round1_replay():
    """offline analysis of the three round-1 C1c responses (actual data)."""
    recs = [json.loads(l) for l in open(os.path.join(HERE, 'RAW-A1.jsonl'))]
    out = []
    for r in recs:
        if r['task'] == 'C1c-two-source':
            u = r.get('usage') or {}
            st, why, _ = classify_response(r)
            out.append({'seq': r['seq'], 'prompt_tokens': u.get('prompt_tokens'),
                        'completion_tokens': u.get('completion_tokens'),
                        'reasoning_tokens': (u.get('completion_tokens_details') or {}).get('reasoning_tokens'),
                        'content_len': len(r.get('content') or ''), 'finish': r.get('finish'),
                        'classification': st, 'why': why})
    return out


BUDGET_DRAFT = {
    'status': 'DRAFT — NOT AUTHORISED (no model call may be made under it)',
    'max_output_tokens_proposed': 16000,
    'rationale': 'round-1 evidence: the hardest C1b instance consumed 3965 completion tokens of '
                 'which 3910 were reasoning; all three C1c attempts consumed the entire 4000 cap as '
                 'reasoning with zero content. 16000 gives at least 4x headroom over the largest '
                 'observed requirement while staying a declared experimental condition.',
    'uniform_across_capabilities': True,
    'completeness_rule': 'any attempt classified MEASUREMENT_FAILURE is reported as UNDECIDABLE and '
                         'is never counted as a capability failure or success',
    'planned_primary_calls': 12,
    'retry_rule': 'transport/5xx only, global cap 4, original parameters, ledger enforced',
    'note': 'the output budget is part of the experimental condition and must be frozen in the v1.2 '
            'pre-registration before any call'
}


def main():
    print('=== GATE A : v1.2 field-level C1b spec (defect-3 regression) ===')
    ga = gate_a_suite()
    for c in ga:
        print('  %-42s expect=%-6s actual=%-6s %s' % (c['case'], c['expected'], c['actual'],
                                                      'PASS' if c['pass'] else 'FAIL'))
        if c['violations']:
            print('        violations: %s' % c['violations'])
    a_pass = all(c['pass'] for c in ga)
    print('  GATE A suite: %s (%d/%d)' % ('PASS' if a_pass else 'FAIL',
                                          sum(1 for c in ga if c['pass']), len(ga)))

    print('\n=== GATE B : capacity / completeness ===')
    gb = gate_b_suite()
    for c in gb:
        print('  %-28s expect=%-20s actual=%-20s %s' % (c['case'], c['expected'], c['actual'],
                                                        'PASS' if c['pass'] else 'FAIL'))
    b_pass = all(c['pass'] for c in gb)
    replay = gate_b_round1_replay()
    print('\n  round-1 C1c replay (actual data):')
    for r in replay:
        print('    seq=%d completion=%s reasoning=%s content_len=%d finish=%s -> %s'
              % (r['seq'], r['completion_tokens'], r['reasoning_tokens'], r['content_len'],
                 r['finish'], r['classification']))
    replay_ok = all(r['classification'] == 'MEASUREMENT_FAILURE' for r in replay)
    print('  GATE B suite: %s ; round-1 replayed as MEASUREMENT_FAILURE: %s'
          % ('PASS' if b_pass else 'FAIL', replay_ok))

    res = {'spec': 'A1-v1.2-GATE-AB-RESULTS', 'model_calls': 0, 'network_access': 'none',
           'gate_a': {'cases': ga, 'pass': a_pass},
           'gate_b': {'cases': gb, 'pass': b_pass, 'round1_c1c_replay': replay,
                      'round1_all_measurement_failure': replay_ok},
           'hyp_preconditions': {h: 'implicit' for h in HYP_PRECOND},
           'unconstrained_policy': UNCONSTRAINED_POLICY,
           'status_to_scoring': STATUS_TO_SCORING,
           'budget_draft': BUDGET_DRAFT}
    json.dump(res, open(os.path.join(HERE, 'A1-v1.2-GATE-AB-RESULTS.json'), 'w'), indent=1)
    print('\n=== GATE A %s | GATE B %s ===' % ('PASS' if a_pass else 'FAIL',
                                               'PASS' if b_pass and replay_ok else 'FAIL'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
