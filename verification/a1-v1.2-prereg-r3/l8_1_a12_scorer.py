#!/usr/bin/env python3
"""A1 v1.2 shared scorer module (r2 semantics).

This is the SINGLE implementation of the r2 scoring rules.  The experiment runner imports it, and
the integration tests verify that the runner's scoring chain is exactly this function object.

Nothing frozen is modified.  Zero model calls, zero network.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import l8_1_a1_evaluator as _frozen          # only for tau_star and the frozen instances

SCORER_ID = 'A1-v1.2-SCORER-r2.1'
HYP = ['H1_common_core', 'H2_uniform_size', 'H3_tight', 'H4_no_complementary_pair']
FIELDS = HYP + ['applicable', 'conclusion']

STATE_TO_SCORING = {
    'SCOREABLE': 'score normally',
    'PARTIAL_TRUNCATED': 'EXCLUDED from the capability verdict; reported as a separate completeness '
                         'stratum (neither SUCCESS nor FAILURE)',
    'MEASUREMENT_FAILURE': 'UNDECIDABLE (never FAILURE, never SUCCESS)',
    'MODEL_NONCOMPLIANCE': 'counts as a rejection (capability failure)',
    'UNCLASSIFIED_RESPONSE': 'UNDECIDABLE + flagged for human review',
}

# ------------------------------------------------------------------ ground truth (r2 definability)
def hyp_truth(inst):
    """Per-hypothesis truth with EXPLICIT definability.

    H1 always defined; H2 always defined; H3 defined iff H1 and H2 (its formula uses both b and |C|);
    H4 defined iff H1 (remainder sets need the core; uniform size is NOT required).
    Undefined is None.
    """
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
        vc = set(range(n)) - core
        h4 = not any(frozenset(vc - set(p)) in ps for p in parts)
    return {'H1_common_core': h1, 'H2_uniform_size': h2, 'H3_tight': h3,
            'H4_no_complementary_pair': h4,
            'applicable': bool(h1 and h2 and h3 is True and h4 is True),
            'tau_star': _frozen.tau_star([frozenset(b) for b in inst['blocks']], n)}


def constrained_fields(truth):
    """only DEFINED hypotheses plus applicable and conclusion are constrained."""
    return [h for h in HYP if truth[h] is not None] + ['applicable', 'conclusion']


# ------------------------------------------------------------------ C1b scoring
def score_c1b(inst, submission):
    """r2 field-level scoring under the explicit-null convention.

    true/false  : judgement value of a DEFINED hypothesis
    null        : hypothesis UNDEFINED under this instance's preconditions
    missing     : incomplete output / format violation -- NEVER equated with null
    """
    t = hyp_truth(inst)
    v = []
    if not isinstance(submission, dict):
        return 'REJECT', {'violations': ['submission is not a JSON object'],
                          'truth': t, 'constrained': constrained_fields(t)}
    hyps = submission.get('hyps')
    if not isinstance(hyps, dict):
        v.append('hyps object missing or malformed')
    else:
        for h in HYP:
            present = h in hyps
            val = hyps.get(h)
            if t[h] is not None:                      # DEFINED
                if not present:
                    v.append('missing DEFINED field %s (missing != null)' % h)
                elif not isinstance(val, bool):
                    v.append('defined field %s must be boolean true/false (got %r)' % (h, val))
                elif bool(val) != bool(t[h]):
                    v.append('wrong %s (submitted %s, truth %s)' % (h, val, t[h]))
            else:                                     # UNDEFINED
                if not present:
                    v.append('UNDEFINED field %s missing; explicit null required (missing != null)' % h)
                elif val is not None:
                    v.append('UNDEFINED field %s must be explicit null (got %r)' % (h, val))
    if 'applicable' not in submission:
        v.append('missing applicable')
    elif not isinstance(submission['applicable'], bool):
        v.append('applicable must be boolean (got %r)' % (submission['applicable'],))
    elif bool(submission['applicable']) != bool(t['applicable']):
        v.append('wrong applicable (submitted %s, truth %s)'
                 % (submission['applicable'], t['applicable']))
    c = submission.get('conclusion', None)
    if t['applicable']:
        if c is None:
            v.append('conclusion must be an integer when applicable (got null)')
        elif isinstance(c, bool) or not isinstance(c, int):
            v.append('conclusion must be an integer when applicable (got %r)' % (c,))
        elif not (3 <= c <= (t['tau_star'] or 0)):
            v.append('conclusion %r outside [3, %s]' % (c, t['tau_star']))
    elif c is not None:
        v.append('conclusion must be null when not applicable (got %r)' % (c,))
    return ('ACCEPT' if not v else 'REJECT'), {
        'violations': v, 'truth': t,
        'constrained': constrained_fields(t),
        'undef_requiring_null': [h for h in HYP if t[h] is None],
        'extra_keys_ignored': [h for h in (hyps or {}) if h not in HYP]}


# ------------------------------------------------------------------ response classification
def classify_response(rec):
    """five-state measurement classification.  finish_reason is evaluated BEFORE parsability.

    Terminal-state priority (explicit, total over the finish_reason domain):
      length                      parsable -> PARTIAL_TRUNCATED / not parsable -> MEASUREMENT_FAILURE
      content_filter | error | None   -> MEASUREMENT_FAILURE, whatever the content
      stop                        parsable -> SCOREABLE / not parsable -> MODEL_NONCOMPLIANCE
      any other value             -> UNCLASSIFIED_RESPONSE, whatever the content

    A system-side termination or an unknown terminal state is NEVER a normal completion, so it can
    never be SCOREABLE even when the content happens to parse.
    """
    from l8_1_a1_run import extract_json
    finish = rec.get('finish')
    content = rec.get('content') or ''
    if finish == 'length':
        if extract_json(content) is not None:
            return 'PARTIAL_TRUNCATED', 'content parsed but generation was cut at the output cap'
        return 'MEASUREMENT_FAILURE', 'output cap reached with no parsable content'
    if finish in ('content_filter', 'error', None):
        return 'MEASUREMENT_FAILURE', ('system-side termination (finish_reason=%r); not a normal '
                                       'completion, content is not scored' % finish)
    if finish == 'stop':
        if extract_json(content) is not None:
            return 'SCOREABLE', 'parsable submission, generation finished normally'
        return 'MODEL_NONCOMPLIANCE', 'empty or unparsable content with finish_reason=stop'
    return 'UNCLASSIFIED_RESPONSE', ('unknown finish_reason %r; not mapped to any terminal state, '
                                      'referred to human review' % finish)


# ------------------------------------------------------------------ aggregation
def split_scoreable(per_instance):
    """split attempt results into scoreable values and excluded states.

    MODEL_NONCOMPLIANCE is declared by STATE_TO_SCORING to count as a rejection, so it is normalised
    to REJECT here instead of being dropped into the excluded set (which would silently turn a
    capability failure into UNDECIDABLE).  Only PARTIAL_TRUNCATED, MEASUREMENT_FAILURE and
    UNCLASSIFIED_RESPONSE are excluded from the capability verdict.
    """
    scoreable, excluded = {}, {}
    for k, v in per_instance.items():
        if v == 'MODEL_NONCOMPLIANCE':
            scoreable[k] = 'REJECT'
        elif v in ('ACCEPT', 'REJECT'):
            scoreable[k] = v
        else:
            excluded[k] = v
    return scoreable, excluded


def aggregate_c1b(per_instance):
    """per_instance: {task_id: state_or_verdict}.  MODEL_NONCOMPLIANCE counts as a rejection."""
    scoreable, excluded = split_scoreable(per_instance)
    if not scoreable:
        return 'UNDECIDABLE', 'every attempt was excluded from scoring (no scoreable attempt)', excluded
    if any(v == 'REJECT' for v in scoreable.values()):
        return 'FAILURE', ('at least one applicability decision wrong, or a non-compliant response '
                           '(MODEL_NONCOMPLIANCE counts as a rejection)'), excluded
    if len(scoreable) == len(per_instance):
        return 'SUCCESS', 'applicability correct on all instances with a valid conclusion', excluded
    return 'UNDECIDABLE', 'mixed: some attempts excluded, no failure among the scoreable ones', excluded


def aggregate_c1c(states):
    """C1c: >=1 scoreable attempt passing the frozen check => SUCCESS.

    Uses the same declared mapping as C1b: MODEL_NONCOMPLIANCE counts as a rejection rather than
    being excluded, so a non-compliant attempt is a capability failure here too.
    """
    scoreable = [('REJECT' if v == 'MODEL_NONCOMPLIANCE' else v)
                 for v in states if v in ('ACCEPT', 'REJECT', 'MODEL_NONCOMPLIANCE')]
    if not scoreable:
        return 'UNDECIDABLE', 'no scoreable attempt'
    if any(v == 'ACCEPT' for v in scoreable):
        return 'SUCCESS', 'at least one scoreable attempt passed'
    return 'FAILURE', 'all scoreable attempts failed (a non-compliant response counts as a rejection)'


def module_fingerprint():
    import hashlib
    p = os.path.abspath(__file__)
    return {'path': p, 'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest(),
            'scorer_id': SCORER_ID}
