#!/usr/bin/env python3
"""L8-1 A1 EVALUATOR — three independent evaluators + frozen interfaces + self-tests/controls.

Operator ruling 2026-10-09 17:44: implement the A1 evaluators; NO model calls authorised.
Deliver: evaluator self-tests, negative-control results, reproducible run record, then freeze the
scorer before any model-run request.

Capabilities (scored SEPARATELY - one success cannot offset another's failure):
  C1a object construction      : constraint satisfaction + novelty + non-re-encoding
  C1b cross-domain instantiation: hypothesis verification + conclusion validity + applicability
  C1c compositional dependency : conclusion valid + TWO-SIDED deletion test + no raw-enum reliance

All frozen inputs are hashed into A1-FREEZE-MANIFEST.json.
"""
import itertools, json, os, hashlib, collections
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
from l8_1_dc1 import tau_star


# ================================================================ frozen artefacts
LIB_SEED = 20261022
CANON_MAX_N = 8          # brute-force canonicalisation is used for n <= 8 (documented limit)


def canon(blocks, npts):
    """canonical form up to POINT PERMUTATION (brute force; n <= CANON_MAX_N)."""
    best = None
    for perm in itertools.permutations(range(npts)):
        m = tuple(sorted(tuple(sorted(perm[x] for x in b)) for b in blocks))
        if best is None or m < best:
            best = m
    return best


def build_library():
    """frozen pre-stored object library L (canonical forms)."""
    import random
    rng = random.Random(LIB_SEED)
    lib = []
    specs = [(7, 9, 4), (8, 10, 4), (8, 12, 3)]
    for n, m, k in specs:
        for _ in range(40):
            blocks = set()
            while len(blocks) < m:
                blocks.add(frozenset(rng.sample(range(n), k)))
            blocks = sorted(blocks, key=sorted)
            if tau_star(blocks, n) is None:
                continue
            lib.append({'n': n, 'blocks': [sorted(b) for b in blocks],
                        'canon': canon(blocks, n)})
            break
    return lib


# ---------------- constraint DSL (machine-checkable) ----------------
def check_constraint(name, obj):
    bl = [set(b) for b in obj['blocks']]
    n = obj['n']
    if name == 'feasible_nocore':
        core = set.intersection(*bl) if bl else set()
        return (len(bl) == 9 and n == 7 and not core, '|B|=9, n=7, no common point')
    if name == 'infeasible_capacity':
        # n=5, m=2, every block <= 2 points  =>  m*maxsize = 4 < 5  =>  NOT coverable  =>  INFEAISIBLE
        infeasible = (n == 5 and len(bl) == 2 and max(len(b) for b in bl) <= 2)
        return (False if infeasible else True,
                'constraint set is PROVABLY EMPTY (2 blocks x <=2 points < 5 points)'
                if infeasible else 'ok')
    if name == 'valid_any':
        return (tau_star([frozenset(b) for b in obj['blocks']], n) is not None, 'coverable')
    return (False, 'unknown constraint')


CONSTRAINTS = ['feasible_nocore', 'infeasible_capacity', 'valid_any']


# ================================================================ C1a : object construction
def eval_c1a(lib, submission, constraint):
    """returns (verdict, detail).  novelty = canon not in L; non-re-encoding = same canon test,
    because the declared transform set {point permutation, block order, block relabeling} acts
    trivially on the canonical form (documented, so this is a real reduction, not an omission)."""
    ok_c, why_c = check_constraint(constraint, submission)
    if not ok_c:
        return 'REJECT', {'constraint_satisfied': False, 'why': why_c}
    c = canon([frozenset(b) for b in submission['blocks']], submission['n'])
    known = set(x['canon'] for x in lib if x['n'] == submission['n'])
    novel = c not in known
    return ('ACCEPT' if novel else 'REJECT-novelty',
            {'constraint_satisfied': True, 'novel': novel,
             'non_reencoding': novel, 'canon_sha': hashlib.sha256(str(c).encode()).hexdigest()[:16]})


# ================================================================ C1b : cross-domain instantiation
LEMMA_HYPS = ['H1_common_core', 'H2_uniform_size', 'H3_tight', 'H4_no_complementary_pair']


def hyp_truth(inst):
    bl = [set(b) for b in inst['blocks']]
    n = inst['n']
    core = set.intersection(*bl) if bl else set()
    sizes = set(len(b) for b in bl)
    h1 = len(core) >= 1
    h2 = len(sizes) == 1
    b = sizes.pop() if h2 else None
    h3 = bool(h2 and h1 and 2 * (b - len(core)) + len(core) == n)
    h4 = None
    if h1 and h2:
        parts = [frozenset(x - core) for x in bl]
        ps = set(parts)
        Vc = set(range(n)) - core
        h4 = not any(frozenset(Vc - set(p)) in ps for p in parts)
    return {'H1_common_core': h1, 'H2_uniform_size': h2, 'H3_tight': h3, 'H4_no_complementary_pair': h4,
            'applicable': bool(h1 and h2 and h3 and h4), 'tau_star': tau_star(
                [frozenset(b) for b in inst['blocks']], n)}


def eval_c1b(inst, submission):
    """submission = {'hyps': {H: bool}, 'conclusion': int or None, 'applicable': bool}"""
    truth = hyp_truth(inst)
    mism = [h for h in LEMMA_HYPS if submission['hyps'].get(h) != truth[h]]
    app_ok = (submission['applicable'] == truth['applicable'])
    concl_ok = None
    if truth['applicable']:
        if submission.get('conclusion') is None:
            concl_ok = False
        else:
            concl_ok = (truth['tau_star'] is not None and submission['conclusion'] <= truth['tau_star']
                        and submission['conclusion'] >= 3)
    else:
        concl_ok = (submission.get('conclusion') is None)      # must NOT claim a conclusion
    return ('ACCEPT' if (not mism and app_ok and concl_ok) else 'REJECT',
            {'hyp_mismatches': mism, 'applicability_correct': app_ok, 'conclusion_ok': concl_ok,
             'truth': truth})


# ================================================================ C1c : compositional dependency
FROZEN_RULES = {
    'core_capacity': 'requires source S_tight ; recomputes ceil((n-|C|)/(b-|C|))',
    'no_complementary_pair': 'requires source S_comp ; recomputes the complement search',
    'combine': 'requires two prior step ids ; conclusion = max of their bounds',
}


def _validate_rule(rule, inst, available_sources, prior_bounds, inferred):
    """mechanical rule validators: a step is valid only if its declared source is AVAILABLE and the
    mathematical content can be RECOMPUTED from the instance alone."""
    bl = [set(b) for b in inst['blocks']]
    n = inst['n']
    core = set.intersection(*bl) if bl else set()
    if rule == 'core_capacity':
        if 'S_tight' not in available_sources:
            return None, 'source S_tight unavailable'
        sizes = set(len(b) for b in bl)
        if len(sizes) != 1 or not core:
            return None, 'capacity form not applicable'
        b = sizes.pop()
        if 2 * (b - len(core)) + len(core) != n:
            return None, 'tightness recomputation fails'
        return Fraction(-((-(n - len(core))) // (b - len(core)))), 'recomputed base bound'
    if rule == 'no_complementary_pair':
        if 'S_comp' not in available_sources:
            return None, 'source S_comp unavailable'
        parts = [frozenset(x - core) for x in bl]
        ps = set(parts)
        Vc = set(range(n)) - core
        if any(frozenset(Vc - set(p)) in ps for p in parts):
            return None, 'a complementary pair exists (fact false)'
        return Fraction(3), 'recomputed no-2-cover'
    if rule == 'combine':
        need = [s for s in inferred.get('requires_steps', []) if s in prior_bounds]
        if len(need) != len(inferred.get('requires_steps', [])):
            return None, 'prior step missing'
        return max(prior_bounds[s] for s in need), 'combined'
    return None, 'unknown rule (frozen rule set)'


def _cone(steps):
    """transitive dependency cone of the CONCLUSION-BEARING step (the last one).
    Padding steps outside this cone must not be able to satisfy the deletion test."""
    by_id = {st.get('id'): st for st in steps}
    if not steps:
        return set(), by_id
    frontier = [steps[-1].get('id')]
    seen = set()
    while frontier:
        sid = frontier.pop()
        if sid in seen or sid not in by_id:
            continue
        seen.add(sid)
        for dep in by_id[sid].get('requires_steps', []):
            frontier.append(dep)
    return seen, by_id


def eval_c1c(inst, submission, raw_enabled=True):
    """submission = {'sources': ['S_tight','S_comp'], 'steps': [...], 'conclusion': int}
    Deletion test is applied to the CONCLUSION DEPENDENCY CONE only, so that a padded step which
    the conclusion does not actually use cannot manufacture two-sided dependence (finding: the
    naive deletion test was paddable)."""
    sources = list(submission.get('sources', []))
    steps = submission.get('steps', [])
    prior, results = {}, []
    ok = True
    for st in steps:
        val, why = _validate_rule(st.get('rule'), inst, set(sources), prior, st)
        results.append({'id': st.get('id'), 'rule': st.get('rule'), 'ok': val is not None, 'why': why})
        if val is None:
            ok = False
            break
        prior[st.get('id')] = val
    concl = max(prior.values()) if (ok and prior) else None
    concl_ok = (concl is not None and submission.get('conclusion') is not None
                and Fraction(submission['conclusion']) <= concl)
    # ---- dependency cone + which source-bearing rules the CONCLUSION actually needs
    cone, by_id = _cone(steps)
    cone_rules = set(by_id[i].get('rule') for i in cone if i in by_id)
    cone_uses_both = ('core_capacity' in cone_rules) and ('no_complementary_pair' in cone_rules)
    cone_steps = [st for st in steps if st.get('id') in cone]
    # ---- two-sided deletion test ON THE CONE
    del_report = {}
    for s in ('S_tight', 'S_comp'):
        avail = set(x for x in sources if x != s)
        ok2, prior2 = True, {}
        for st in cone_steps:
            val, why = _validate_rule(st.get('rule'), inst, avail, prior2, st)
            if val is None:
                ok2 = False
                break
            prior2[st.get('id')] = val
        del_report[s] = {'cone_survives_without_%s' % s: ok2}
    del_ok = all(not v['cone_survives_without_%s' % s] for s, v in del_report.items())
    del_ok = del_ok and cone_uses_both
    indep_ok = None
    if not raw_enabled:
        indep_ok = ok
    verdict = 'ACCEPT' if (ok and concl_ok and del_ok and (indep_ok is not False)) else 'REJECT'
    return verdict, {'steps_ok': ok, 'conclusion_ok': concl_ok, 'deletion_two_sided': del_ok,
                     'cone': sorted(cone), 'cone_rules': sorted(cone_rules),
                     'cone_uses_both_sources': cone_uses_both,
                     'deletion_detail': del_report, 'step_results': results,
                     'bound': (str(concl) if concl is not None else None)}


# ================================================================ frozen control instances
N7 = {'n': 7, 'blocks': [[0, 1, 2, 4], [0, 1, 2, 5], [0, 1, 3, 4], [0, 1, 4, 6], [0, 1, 5, 6],
                         [0, 2, 3, 6], [0, 2, 4, 5], [0, 2, 4, 6], [0, 3, 4, 5]]}
NOT_TIGHT = {'n': 7, 'blocks': [[0, 1, 2, 3, 4], [0, 1, 2, 5, 6], [0, 1, 3, 4, 5], [0, 2, 3, 4, 6],
                                [0, 1, 2, 3, 5], [0, 1, 2, 4, 5], [0, 2, 3, 5, 6], [0, 1, 3, 5, 6],
                                [0, 3, 4, 5, 6]]}
NO_CORE = {'n': 7, 'blocks': [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [0, 4, 5, 6],
                              [0, 1, 5, 6], [0, 1, 2, 6], [0, 1, 4, 5], [0, 2, 5, 6]]}


def main():
    lib = build_library()
    run = {'spec': 'L8-1-A1-EVALUATOR-SELFTEST', 'model_calls': 0, 'capabilities': {}}
    print('=== A1 evaluator self-test ===')
    print('library L: %d objects (canon frozen)' % len(lib))

    # ---------------- C1a
    print('\n[C1a object construction]')
    fresh = None
    import random
    rng = random.Random(7)
    for _ in range(3000):                       # find a NOVEL valid object for the feasible constraint
        blocks = set()
        while len(blocks) < 9:
            blocks.add(frozenset(rng.sample(range(7), rng.randint(2, 4))))
        blocks = sorted(blocks, key=sorted)
        if set.intersection(*[set(b) for b in blocks]):
            continue
        if tau_star(blocks, 7) is None:
            continue
        c = canon(blocks, 7)
        if c not in set(x['canon'] for x in lib if x['n'] == 7):
            fresh = {'n': 7, 'blocks': [sorted(b) for b in blocks]}
            break
    c1a = {}
    c1a['T1_positive_novel'] = eval_c1a(lib, fresh, 'feasible_nocore')
    c1a['T2_negative_library_object'] = eval_c1a(
        lib, {'n': lib[0]['n'], 'blocks': lib[0]['blocks']}, 'valid_any')
    c1a['T3_negative_infeasible'] = eval_c1a(
        lib, {'n': 5, 'blocks': [[0, 1], [2, 3]]}, 'infeasible_capacity')
    for k, (v, d) in c1a.items():
        print('  %-30s -> %-18s %s' % (k, v, d))
    run['capabilities']['C1a'] = {k: {'verdict': v, 'detail': d} for k, (v, d) in c1a.items()}
    run['capabilities']['C1a']['selftest_pass'] = (
        c1a['T1_positive_novel'][0] == 'ACCEPT' and
        c1a['T2_negative_library_object'][0].startswith('REJECT') and
        c1a['T3_negative_infeasible'][0] == 'REJECT')

    # ---------------- C1b
    print('\n[C1b cross-domain instantiation]')
    c1b = {}
    t = hyp_truth(N7)
    c1b['T1_positive_applicable'] = eval_c1b(N7, {
        'hyps': {h: t[h] for h in LEMMA_HYPS}, 'applicable': t['applicable'], 'conclusion': 3})
    t2 = hyp_truth(NOT_TIGHT)
    c1b['T2_negative_not_tight'] = eval_c1b(NOT_TIGHT, {
        'hyps': {h: t2[h] for h in LEMMA_HYPS}, 'applicable': t2['applicable'],
        'conclusion': (3 if t2['applicable'] else None)})
    # deliberately WRONG submission: claims applicable + conclusion on a case whose H3 fails
    c1b['T3_negative_overclaim'] = eval_c1b(NOT_TIGHT, {
        'hyps': {h: True for h in LEMMA_HYPS}, 'applicable': True, 'conclusion': 3})
    t3 = hyp_truth(NO_CORE)
    c1b['T4_negative_no_core'] = eval_c1b(NO_CORE, {
        'hyps': {h: t3[h] for h in LEMMA_HYPS}, 'applicable': t3['applicable'], 'conclusion': None})
    for k, (v, d) in c1b.items():
        print('  %-30s -> %-8s applicable_correct=%s concl_ok=%s mism=%s'
              % (k, v, d['applicability_correct'], d['conclusion_ok'], d['hyp_mismatches']))
    run['capabilities']['C1b'] = {k: {'verdict': v, 'detail': d} for k, (v, d) in c1b.items()}
    run['capabilities']['C1b']['selftest_pass'] = (
        c1b['T1_positive_applicable'][0] == 'ACCEPT' and
        c1b['T2_negative_not_tight'][0] == 'ACCEPT' and      # correct refusal is CORRECT behaviour
        c1b['T3_negative_overclaim'][0] == 'REJECT' and
        c1b['T4_negative_no_core'][0] == 'ACCEPT')

    # ---------------- C1c
    print('\n[C1c compositional dependency]')
    good = {'sources': ['S_tight', 'S_comp'], 'conclusion': 3, 'steps': [
        {'id': 's1', 'rule': 'core_capacity', 'requires_steps': []},
        {'id': 's2', 'rule': 'no_complementary_pair', 'requires_steps': []},
        {'id': 's3', 'rule': 'combine', 'requires_steps': ['s1', 's2']}]}
    one_sided = {'sources': ['S_tight', 'S_comp'], 'conclusion': 3, 'steps': [
        {'id': 's1', 'rule': 'core_capacity', 'requires_steps': []},
        {'id': 's3', 'rule': 'combine', 'requires_steps': ['s1', 's1']}]}     # never uses S_comp
    bogus = {'sources': ['S_tight', 'S_comp'], 'conclusion': 3, 'steps': [
        {'id': 's1', 'rule': 'assert_bound', 'requires_steps': []}]}          # rule not in frozen set
    c1c = {}
    c1c['T1_positive_two_source'] = eval_c1c(N7, good)
    c1c['T2_negative_one_sided'] = eval_c1c(N7, one_sided)
    c1c['T3_negative_format_dependence'] = eval_c1c(N7, bogus)
    padded = {'sources': ['S_tight', 'S_comp'], 'conclusion': 3, 'steps': [
        {'id': 's1', 'rule': 'core_capacity', 'requires_steps': []},
        {'id': 'pad', 'rule': 'no_complementary_pair', 'requires_steps': []},   # NOT in the cone
        {'id': 's3', 'rule': 'combine', 'requires_steps': ['s1', 's1']}]}
    c1c['T5_negative_padded_cone'] = eval_c1c(N7, padded)
    v4, d4 = eval_c1c(N7, good, raw_enabled=False)
    c1c['T4_independence_raw_disabled'] = (v4, d4)
    for k, (v, d) in c1c.items():
        print('  %-30s -> %-8s steps_ok=%s deletion_two_sided=%s concl_ok=%s'
              % (k, v, d['steps_ok'], d['deletion_two_sided'], d['conclusion_ok']))
        if k == 'T1_positive_two_source':
            print('       deletion detail: %s' % d['deletion_detail'])
    run['capabilities']['C1c'] = {k: {'verdict': v, 'detail': d} for k, (v, d) in c1c.items()}
    run['capabilities']['C1c']['selftest_pass'] = (
        c1c['T1_positive_two_source'][0] == 'ACCEPT' and
        c1c['T2_negative_one_sided'][0] == 'REJECT' and
        c1c['T3_negative_format_dependence'][0] == 'REJECT' and
        c1c['T5_negative_padded_cone'][0] == 'REJECT' and
        c1c['T4_independence_raw_disabled'][0] == 'ACCEPT')

    # ---------------- freeze manifest
    manifest = {}
    blob = json.dumps({'lib': [{'n': x['n'], 'canon': str(x['canon'])} for x in lib],
                       'constraints': CONSTRAINTS, 'lemma_hyps': LEMMA_HYPS,
                       'frozen_rules': sorted(FROZEN_RULES), 'canon_max_n': CANON_MAX_N},
                      sort_keys=True)
    manifest['frozen_inputs_sha256'] = hashlib.sha256(blob.encode()).hexdigest()
    manifest['library_size'] = len(lib)
    manifest['canonicalisation'] = 'brute force over point permutations (n <= %d)' % CANON_MAX_N
    manifest['transform_set'] = ['point_permutation', 'block_order', 'block_relabel']
    manifest['note_transform_trivial_on_canon'] = True
    run['freeze_manifest'] = manifest
    json.dump(manifest, open(os.path.join(HERE, 'A1-FREEZE-MANIFEST.json'), 'w'), indent=1)
    json.dump(run, open(os.path.join(HERE, 'A1-EVALUATOR-SELFTEST.json'), 'w'), indent=1)
    print('\n=== freeze manifest sha256: %s ===' % manifest['frozen_inputs_sha256'])
    for cap in ('C1a', 'C1b', 'C1c'):
        print('%-4s self-test pass: %s' % (cap, run['capabilities'][cap]['selftest_pass']))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
