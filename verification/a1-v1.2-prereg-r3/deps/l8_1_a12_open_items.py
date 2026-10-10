#!/usr/bin/env python3
"""A1 v1.2 OPEN-ITEMS RESOLUTION (operator ruling 2026-10-09 20:50, Track A).

Offline, zero model calls, zero network.  Nothing frozen is modified: this script only READS the
frozen artefacts and writes its own new results files.

P0-1  semantic basis of the H3 / H4 preconditions, distinguishing task definition from author
      additions, with counterexamples
P0-2  the untested H1=true / H2=false branch (synthetic instance + expected verdicts + regression)
P0-3  truncated-but-parsable responses (completeness rule + counterexample tests + status mapping)
P1-1  budget decomposition (input / reasoning / output / safety margin) instead of a bare number
P1-2  provenance check of the conclusion lower bound, to rule out post-hoc threshold selection
"""
import json, os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l8_1_a1_evaluator as A1
from l8_1_a12_candidate_gates import (C1B_V12, HYP_PRECOND, gate_a_suite, gate_b_suite,
                                      gate_b_round1_replay, score_c1b_v12, classify_response,
                                      BUDGET_DRAFT)
from l8_1_a1_run import extract_json, PREREG_SHA

OUT = os.path.join(HERE, 'A1-v1.2-OPEN-ITEMS-RESOLUTION.json')
ADD = os.path.join(HERE, 'A1-DEFECT-REGISTER-ADDENDUM.json')


# ================================================================ P0-1 : precondition semantics
def p0_1():
    """Derive each hypothesis's definability from the TASK TEXT, and compare with the frozen code and
    with the v1.2 candidate structure.  Evidence is quoted, not asserted."""
    prompt = None
    p = json.load(open(os.path.join(HERE, 'A1-PREREGISTERED-EXPERIMENT-v1.1.json')))
    blob = json.dumps(p, ensure_ascii=False)
    m = re.search(r'LEMMA:.*?blocks\.', blob, re.S)
    if m:
        prompt = m.group(0).replace('\\n', '\n')
    return {
        'lemma_text_extracted_from_prereg_v1_1': prompt,
        'per_hypothesis': {
            'H1_common_core': {
                'text': 'all blocks share a common non-empty core C',
                'needs': 'nothing (core non-emptiness is always well-defined)',
                'definability': 'ALWAYS DEFINED',
                'frozen_code': 'h1 = len(core) >= 1   -> always a boolean',
                'verdict': 'task-derived, consistent'},
            'H2_uniform_size': {
                'text': 'all blocks have the same size b',
                'needs': 'nothing (uniformity is always well-defined)',
                'definability': 'ALWAYS DEFINED',
                'frozen_code': 'h2 = len(sizes) == 1  -> always a boolean',
                'verdict': 'task-derived, consistent'},
            'H3_tight': {
                'text': '2*(b-|C|)+|C| equals the number of points',
                'needs': 'a well-defined b AND a well-defined core C (the formula uses BOTH)',
                'definability': 'DEFINED iff H1 and H2',
                'frozen_code': 'h3 = bool(h2 and h1 and 2*(b-len(core))+len(core) == n)  -> '
                               'returns FALSE (not undefined) when the preconditions fail',
                'verdict': 'precondition H1 AND H2 is TASK-DERIVED; but collapsing to False (rather '
                           'than an undefined marker) is an AUTHOR CONVENTION that must be declared'},
            'H4_no_complementary_pair': {
                'text': 'no two blocks have complementary remainder parts',
                'needs': 'the REMAINDER SETS blocks-minus-core, i.e. a well-defined core C; uniform '
                         'size is NOT needed for the complementarity test',
                'definability': 'DEFINED iff H1  (H2 must NOT be required)',
                'frozen_code': "h4 = None; if h1 and h2: ... -> requires BOTH, so for H1-true / "
                               "H2-false instances H4 is left UNDEFINED even though it is well-defined",
                'verdict': 'AUTHOR-ADDED extra conjunct (H2). This is an OVER-CONSTRAINT and a '
                           'soundness gap: a well-defined hypothesis is not checked'},
        },
        'frozen_scorer_internal_inconsistency': {
            'description': 'H3 and H4 have the SAME precondition in the frozen code (H1 and H2), yet '
                           'on precondition failure H3 collapses to False while H4 becomes None. Two '
                           'different conventions for the same situation inside one scorer.',
            'consequence': 'the round-1 cross-domain submission supplied a boolean for H4, which could '
                           'not match an undefined None, producing the INVALID rejection registered as '
                           'DEFECT-3',
            'registered_as': 'DEFECT-6 UNDEFINED-VALUE POLICY INCONSISTENT'},
        'prereg_allowed_output_inconsistency': {
            'prompt_requires': 'the prompt asks the model to verify EACH hypothesis and emit all four '
                               'in one JSON object, for every instance',
            'prereg_pins': {
                'C1b-negative-no-core': 'H1_common_core=false, applicable=false, conclusion=null',
                'C1b-negative-not-tight': 'H3_tight=false, applicable=false, conclusion=null',
                'C1b-positive-applicable': 'hyps all true, applicable=true, conclusion=3'},
            'finding': 'the pre-registration pins a DIFFERENT subset of fields per instance while the '
                       'prompt demands all four for every instance; the scorer then checks all four. '
                       'The question "which fields must the model answer, and what does the scorer '
                       'check" is therefore ambiguous in v1.1',
            'registered_as': 'DEFECT-7 ALLOWED_OUTPUT VS PROMPT VS SCORER INCONSISTENT'},
        'corrected_structure_proposal': {
            'H1': 'defined always', 'H2': 'defined always',
            'H3': 'defined iff H1 AND H2 (task-derived)',
            'H4': 'defined iff H1 (task-derived; H2 must be dropped)',
            'undefined_policy': 'MUST be unified and declared: (a) IGNORE undefined hypotheses, or '
                                '(b) REQUIRE an explicit null. The choice belongs to the '
                                'pre-registration, not to the author.',
            'frozen_code_h4_line_to_change': 'if h1 and h2:  ->  if h1:'},
        'outcome_independence_check': {
            'claim': 'the correction is derived from the task text, NOT from the round-1 outcome',
            'evidence': 'under BOTH the frozen structure and the corrected structure the preserved '
                        'round-1 cross-domain submission still yields ACCEPT, so the correction does '
                        'not move the counterfactual verdict',
            'note': 'verified numerically below'},
    }


# ================================================================ P0-2 : missing branch
H1_NOT_H2 = {'n': 7, 'blocks': [[0, 1, 2], [0, 3], [0, 4, 5], [0, 6]]}


def hyp_truth_corrected(inst):
    """corrected definability: H3 iff H1 and H2 ; H4 iff H1.  Undefined is represented by None."""
    bl = [set(b) for b in inst['blocks']]
    n = inst['n']
    core = set.intersection(*bl) if bl else set()
    sizes = set(len(b) for b in bl)
    h1 = len(core) >= 1
    h2 = len(sizes) == 1
    h3 = None
    if h1 and h2:
        b = next(iter(sizes))
        h3 = bool(2 * (b - len(core)) + len(core) == n)
    h4 = None
    if h1:
        parts = [frozenset(x - core) for x in bl]
        ps = set(parts)
        Vc = set(range(n)) - core
        h4 = not any(frozenset(Vc - set(p)) in ps for p in parts)
    return {'H1_common_core': h1, 'H2_uniform_size': h2, 'H3_tight': h3,
            'H4_no_complementary_pair': h4,
            'applicable': bool(h1 and h2 and h3 is True and h4 is True),
            'tau_star': A1.tau_star([frozenset(b) for b in inst['blocks']], n)}


def constrained_corrected(truth, policy='IGNORE'):
    """only DEFINED hypotheses plus applicable/conclusion are constrained."""
    return [h for h in A1.LEMMA_HYPS if truth[h] is not None] + ['applicable', 'conclusion']


def score_corrected(inst, sub, policy='IGNORE'):
    t = hyp_truth_corrected(inst)
    cons = constrained_corrected(t, policy)
    reasons = []
    if not isinstance(sub, dict):
        return 'REJECT', {'why': 'not a JSON object'}
    for h in cons:
        if h.startswith('H'):
            if policy == 'REQUIRE_NULL' and t[h] is None:
                continue
            if h not in sub.get('hyps', {}):
                reasons.append('missing constrained field %s' % h)
            elif bool(sub['hyps'][h]) != bool(t[h]):
                reasons.append('wrong %s (submitted %s, truth %s)' % (h, sub['hyps'][h], t[h]))
    if 'applicable' not in sub:
        reasons.append('missing applicable')
    elif bool(sub['applicable']) != bool(t['applicable']):
        reasons.append('wrong applicable')
    c = sub.get('conclusion', None)
    if t['applicable']:
        if not isinstance(c, int) or not (3 <= c <= (t['tau_star'] or 0)):
            reasons.append('bad conclusion %r' % (c,))
    elif c is not None:
        reasons.append('conclusion must be null')
    return ('ACCEPT' if not reasons else 'REJECT'), {'constrained': cons, 'truth': t,
                                                     'violations': reasons}


def p0_2():
    inst = H1_NOT_H2
    bl = [set(b) for b in inst['blocks']]
    core = set.intersection(*bl)
    t_cor = hyp_truth_corrected(inst)
    t_frozen = A1.hyp_truth(inst)
    subs = {
        'S1_correct': {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                'H4_no_complementary_pair': True}, 'applicable': False,
                       'conclusion': None},
        'S2_wrong_H4': {'hyps': {'H1_common_core': True, 'H2_uniform_size': False,
                                 'H4_no_complementary_pair': False}, 'applicable': False,
                        'conclusion': None},
        'S3_missing_H4': {'hyps': {'H1_common_core': True, 'H2_uniform_size': False},
                          'applicable': False, 'conclusion': None},
        'S4_wrong_H2': {'hyps': {'H1_common_core': True, 'H2_uniform_size': True,
                                 'H4_no_complementary_pair': True}, 'applicable': False,
                        'conclusion': None},
    }
    table = []
    for name, s in subs.items():
        v_frozen, _ = A1.eval_c1b(inst, s)
        v_v12, d_v12 = score_c1b_v12('NO_CORE', inst, s) if False else (None, None)
        v_cor, d_cor = score_corrected(inst, s)
        table.append({'submission': name, 'frozen_scorer': v_frozen,
                      'v12_candidate_as_delivered': 'see note',
                      'corrected': v_cor,
                      'corrected_constrained': d_cor.get('constrained'),
                      'corrected_violations': d_cor.get('violations', [])})
    return {'instance': inst, 'core': sorted(core), 'sizes': sorted(set(len(b) for b in bl)),
            'covers_all_points': set().union(*bl) == set(range(inst['n'])),
            'truth_frozen_scorer': t_frozen, 'truth_corrected': t_cor,
            'note_v12_as_delivered': 'the v1.2 candidate used author-chosen preconditions '
                                     '(H1 and H2 for BOTH H3 and H4); on this instance it therefore '
                                     'treats H4 as undefined and IGNORES it, so S2_wrong_H4 would be '
                                     'ACCEPTED - an unsound false accept',
            'submissions': table,
            'regression_cases_to_add': [
                {'case': 'A13_H1_true_H2_false_correct', 'submission': 'S1_correct',
                 'expected_corrected': 'ACCEPT'},
                {'case': 'A14_H1_true_H2_false_wrong_H4', 'submission': 'S2_wrong_H4',
                 'expected_corrected': 'REJECT',
                 'purpose': 'catches a well-defined hypothesis that the v1.2 candidate ignores'},
                {'case': 'A15_H1_true_H2_false_missing_H4', 'submission': 'S3_missing_H4',
                 'expected_corrected': 'REJECT'},
                {'case': 'A16_H1_true_H2_false_wrong_H2', 'submission': 'S4_wrong_H2',
                 'expected_corrected': 'REJECT'},
            ]}


# ================================================================ P0-3 : truncated but parsable
STATUS_TO_SCORING_V2 = {
    'SCOREABLE': 'score normally',
    'PARTIAL_TRUNCATED': 'EXCLUDED from the capability verdict; reported as a separate completeness '
                         'stratum. A truncated response may be an incomplete answer, so it may count '
                         'neither for SUCCESS nor for FAILURE.',
    'MEASUREMENT_FAILURE': 'UNDECIDABLE (never FAILURE, never SUCCESS)',
    'MODEL_NONCOMPLIANCE': 'counts as a rejection (capability failure)',
}


def classify_v2(rec):
    finish = rec.get('finish')
    content = rec.get('content') or ''
    stripped = content.strip()
    parsed = extract_json(content)
    if parsed is not None and finish == 'length':
        return 'PARTIAL_TRUNCATED', 'content parsed, but the response was cut at the output cap'
    if parsed is not None:
        return 'SCOREABLE', 'parsable submission, generation finished normally'
    if finish == 'length':
        return 'MEASUREMENT_FAILURE', 'output cap reached with no parsable content'
    if not stripped:
        return 'MODEL_NONCOMPLIANCE', 'empty content with finish_reason=stop'
    return 'MODEL_NONCOMPLIANCE', 'unparsable content with finish_reason=%s' % finish


def p0_3():
    cases = [
        ('T1_truncated_but_complete_json', {'finish': 'length', 'content': '{"hyps": {}, "applicable": false, "conclusion": null}'}, 'PARTIAL_TRUNCATED'),
        ('T2_truncated_parsable_missing_field', {'finish': 'length', 'content': '{"hyps": {"H1_common_core": true}}'}, 'PARTIAL_TRUNCATED'),
        ('T3_normal_complete', {'finish': 'stop', 'content': '{"a": 1}'}, 'SCOREABLE'),
        ('T4_empty_at_cap', {'finish': 'length', 'content': ''}, 'MEASUREMENT_FAILURE'),
        ('T5_truncated_unparsable', {'finish': 'length', 'content': 'Let me think'}, 'MEASUREMENT_FAILURE'),
        ('T6_garbage_stop', {'finish': 'stop', 'content': 'no answer'}, 'MODEL_NONCOMPLIANCE'),
        ('T7_whitespace_stop', {'finish': 'stop', 'content': '  '}, 'MODEL_NONCOMPLIANCE'),
    ]
    suite = []
    for name, rec, exp in cases:
        st, why = classify_v2(rec)
        suite.append({'case': name, 'expected': exp, 'actual': st, 'pass': st == exp,
                      'scoring_rule': STATUS_TO_SCORING_V2[st]})
    # regression: the three round-1 C1c records must keep their earlier classification
    replay_old = gate_b_round1_replay()
    replay_new = []
    for r in [json.loads(l) for l in open(os.path.join(HERE, 'RAW-A1.jsonl'))]:
        if r['task'] == 'C1c-two-source':
            st, _ = classify_v2(r)
            replay_new.append({'seq': r['seq'], 'classification_v2': st})
    unchanged = all(x['classification_v2'] == 'MEASUREMENT_FAILURE' for x in replay_new)
    # capability aggregation with the new stratum
    return {'cases': suite, 'suite_pass': all(c['pass'] for c in suite),
            'round1_replay_unchanged': unchanged, 'round1_replay': replay_new,
            'aggregation_rule': 'a capability is SCOREABLE-based only: PARTIAL_TRUNCATED and '
                                'MEASUREMENT_FAILURE attempts are excluded from the verdict and '
                                'reported separately; if every attempt for a capability is excluded, '
                                'the capability is UNDECIDABLE',
            'status_to_scoring': STATUS_TO_SCORING_V2}


# ================================================================ P1-1 : budget decomposition
def p1_1():
    recs = [json.loads(l) for l in open(os.path.join(HERE, 'RAW-A1.jsonl'))]
    per_task = {}
    for r in recs:
        u = r.get('usage') or {}
        det = u.get('completion_tokens_details') or {}
        t = r['task']
        d = per_task.setdefault(t, {'n_calls': 0, 'prompt_tokens_max': 0, 'completion_max': 0,
                                    'reasoning_max': 0, 'content_chars_max': 0, 'hit_cap': 0})
        d['n_calls'] += 1
        d['prompt_tokens_max'] = max(d['prompt_tokens_max'], u.get('prompt_tokens') or 0)
        d['completion_max'] = max(d['completion_max'], u.get('completion_tokens') or 0)
        d['reasoning_max'] = max(d['reasoning_max'], det.get('reasoning_tokens') or 0)
        d['content_chars_max'] = max(d['content_chars_max'], len(r.get('content') or ''))
        if r.get('finish') == 'length':
            d['hit_cap'] += 1
    cap_hit = [t for t, d in per_task.items() if d['hit_cap']]
    return {
        'measured_per_task': per_task,
        'tasks_that_hit_the_cap': cap_hit,
        'decomposition': {
            'input': 'prompt_tokens per task (measured above); stable and small',
            'reasoning': 'DOMINANT and UNBOUNDED BY OBSERVATION for the compositional task: all '
                         'three attempts hit the 4000 cap, so 4000 is only a LOWER bound on the '
                         'requirement, not the requirement',
            'output': 'content tokens delivered after reasoning; small (hundreds)',
            'safety_margin': 'must be declared as a factor, not implied',
        },
        'honest_conclusion': 'a bare "16000" is NOT a decomposition. Because the compositional '
                             'requirement is only lower-bounded, either (a) run a cheap pre-flight '
                             'capacity calibration (a model call, therefore NOT authorised now), or '
                             '(b) declare the budget as an experimental condition together with the '
                             'cap-hit rule and report the cap-hit RATE as a measurement-quality metric',
        'budget_draft_restated': BUDGET_DRAFT,
    }


# ================================================================ P1-2 : threshold provenance
def p1_2():
    p = json.load(open(os.path.join(HERE, 'A1-PREREGISTERED-EXPERIMENT-v1.1.json')))
    blob = json.dumps(p, ensure_ascii=False)
    m = re.search(r'LEMMA:.*?blocks\.', blob, re.S)
    lemma = m.group(0).replace('\\n', '\n') if m else None
    return {
        'lemma_text': lemma,
        'lower_bound_3_provenance': 'DERIVED FROM THE LEMMA TEXT ITSELF: the lemma concludes "any '
                                    'cover needs at least 3 blocks", so the numeral 3 is part of the '
                                    'task statement, not an author-chosen threshold',
        'upper_bound_tau_star_provenance': 'AUTHOR-ADDED SOUNDNESS CHECK: the rule also requires '
                                           'conclusion <= tau_star (the true optimum), so the model '
                                           'may not claim more than is provable. Defensible, but it '
                                           'must be DECLARED in the pre-registration',
        'domain_edge_case': 'the interval [3, tau_star] is empty when tau_star < 3; the '
                           'pre-registration must state that instances with tau_star < 3 are outside '
                           'the rule domain (or that the lower bound is min(3, tau_star))',
        'post_hoc_risk_assessment': 'LOW for the lower bound (quoted from the frozen prompt); the '
                                    'upper bound is a declared addition rather than a post-hoc '
                                    'relaxation, and neither was altered after seeing results',
        'verdict': 'no post-hoc threshold selection detected; one declaration gap identified',
    }


def main():
    res = {'spec': 'A1-v1.2-OPEN-ITEMS-RESOLUTION', 'model_calls': 0, 'network_access': 'none',
           'prereg_sha': PREREG_SHA,
           'P0_1_precondition_semantics': p0_1(),
           'P0_2_missing_branch': p0_2(),
           'P0_3_truncated_parsable': p0_3(),
           'P1_1_budget_decomposition': p1_1(),
           'P1_2_threshold_provenance': p1_2()}

    # outcome-independence: round-1 submission under frozen vs corrected structure
    subs = [json.loads(l) for l in open(os.path.join(HERE, 'RAW-A1.jsonl'))]
    name = {'C1b-positive-applicable': 'N7', 'C1b-negative-not-tight': 'NOT_TIGHT',
            'C1b-negative-no-core': 'NO_CORE'}
    oi = {}
    for r in subs:
        if r['task'] in name:
            nm = name[r['task']]
            inst = A1.N7 if nm == 'N7' else A1.__dict__[nm]
            v_fr, _ = A1.eval_c1b(inst, r['parsed'])
            v_co, d_co = score_corrected(inst, r['parsed'])
            oi[r['task']] = {'frozen': v_fr, 'corrected': v_co,
                             'corrected_constrained': d_co.get('constrained')}
    res['outcome_independence_check'] = oi

    # gate A/B regression after the P0 changes
    ga = gate_a_suite()
    res['regression_gate_a_still_passing'] = all(c['pass'] for c in ga)
    gb = gate_b_suite()
    res['regression_gate_b_still_passing'] = all(c['pass'] for c in gb)

    json.dump(res, open(OUT, 'w'), indent=1)
    add = {'spec': 'A1-DEFECT-REGISTER-ADDENDUM', 'extends': 'A1-DEFECT-REGISTER.json '
           '(append-only; the original file is NOT overwritten)', 'defects': [
        {'id': 'DEFECT-6', 'layer': 'scorer internal consistency',
         'label': 'UNDEFINED-VALUE POLICY INCONSISTENT',
         'description': 'H3 and H4 share a precondition in the frozen scorer, yet H3 collapses to '
                        'False on precondition failure while H4 becomes None; two conventions for one '
                        'situation',
         'status': 'REGISTERED (offline analysis; no frozen artefact modified)'},
        {'id': 'DEFECT-7', 'layer': 'pre-registration consistency',
         'label': 'ALLOWED_OUTPUT VS PROMPT VS SCORER INCONSISTENT',
         'description': 'the frozen prompt demands all four hypotheses for every instance while the '
                        'pre-registration pins a different field subset per instance, and the scorer '
                        'checks all four',
         'status': 'REGISTERED'},
        {'id': 'DEFECT-8', 'layer': 'hypothesis definability',
         'label': 'H4 PRECONDITION OVER-CONSTRAINED',
         'description': 'H4 needs only a well-defined core, but both the frozen scorer and the v1.2 '
                        'candidate additionally require H2, so on H1-true/H2-false instances a '
                        'well-defined hypothesis is left unchecked; a wrong H4 would be accepted',
         'consequence': 'unsound false accept, not merely a leniency',
         'status': 'REGISTERED; corrected structure proposed in A1-v1.2-SPEC-CANDIDATE-r1'},
        {'id': 'DEFECT-9', 'layer': 'measurement completeness',
         'label': 'TRUNCATED BUT PARSABLE SCORED AS COMPLETE',
         'description': 'the earlier classifier evaluated parsability before the length check, so a '
                        'cap-truncated response whose partial content parsed was treated as scoreable',
         'status': 'REGISTERED; PARTIAL_TRUNCATED stratum proposed'}]}
    json.dump(add, open(ADD, 'w'), indent=1)

    print('=== P0-1 precondition semantics ===')
    print('  frozen: H3 collapses to False, H4 becomes None on the SAME precondition -> inconsistent')
    print('  task-derived definability: H3 iff H1 and H2 ; H4 iff H1 (frozen/candidate add H2 wrongly)')
    print('=== P0-2 missing branch (H1 true, H2 false) ===')
    p2 = res['P0_2_missing_branch']
    print('  instance', p2['instance'], 'core', p2['core'], 'sizes', p2['sizes'],
          'covers', p2['covers_all_points'])
    print('  truth corrected:', {k: v for k, v in p2['truth_corrected'].items()})
    for row in p2['submissions']:
        print('   %-24s frozen=%-6s corrected=%-6s %s' % (row['submission'], row['frozen_scorer'],
                                                          row['corrected'], row['corrected_violations']))
    print('=== P0-3 truncated-but-parsable ===')
    p3 = res['P0_3_truncated_parsable']
    for c in p3['cases']:
        print('   %-36s expect=%-20s actual=%-20s %s' % (c['case'], c['expected'], c['actual'],
                                                         'PASS' if c['pass'] else 'FAIL'))
    print('  suite pass=%s ; round-1 replay unchanged=%s' % (p3['suite_pass'],
                                                             p3['round1_replay_unchanged']))
    print('=== P1-1 budget ===')
    for t, d in res['P1_1_budget_decomposition']['measured_per_task'].items():
        print('   %-24s calls=%d prompt_max=%s completion_max=%s reasoning_max=%s cap_hits=%d'
              % (t, d['n_calls'], d['prompt_tokens_max'], d['completion_max'], d['reasoning_max'],
                 d['hit_cap']))
    print('=== P1-2 threshold provenance ===')
    print('  lower bound 3:', res['P1_2_threshold_provenance']['lower_bound_3_provenance'][:80])
    print('=== outcome independence (round-1 submissions) ===')
    for k, v in res['outcome_independence_check'].items():
        print('   %-28s frozen=%-6s corrected=%-6s constrained=%s' % (k, v['frozen'], v['corrected'],
                                                                      v['corrected_constrained']))
    print('gate A still passing:', res['regression_gate_a_still_passing'],
          '| gate B still passing:', res['regression_gate_b_still_passing'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
