#!/usr/bin/env python3
"""L8-1 D-C1 v1 — operational Discovery/Oracle classifier (operator 2026-10-09 11:56).

D-C1 conditions (all four must hold for a certificate to classify as DISCOVERY):
  (a) structure dependence : states a lemma reusable for a FAMILY, with explicit applicability
                             assumptions, and the assumptions are machine-checked on the instance
  (b) search shrinkage     : raw search size and reduced size are MEASURED (instrumented counter,
                             not self-reported) and reduced < raw, with the ratio reported
  (c) auditability         : every derivation step is machine-checkable; no hidden reliance on a
                             full search result
  (d) certificate independence : re-running the certificate with the raw enumeration facility
                             DISABLED still derives the conclusion (so it is not a re-encoding of
                             the exhaustive result)
Otherwise: classify as ORACLE (if it needs raw enumeration) or UNCLASSIFIED - never force a binary.

Modified C1 (same ruling): Delta_disc = B_multi - B_single > 0, where B_single is the best bound
obtainable by D-C1-approved SINGLE-STEP discovery on the same instance/budget.  Baseline coverage
must be stated: a finite search bounds the given operation set and budget only.
"""
import itertools, json, os, collections
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- provenance-pinned instances
N7 = {  # found by the stage-1 gap search (n=7, |B|=9, LP*=2, tau*=3, common core + uniform size)
    'name': 'n7_common_core', 'npts': 7, 'provenance': 'L8-1-STAGE1-PREREQUISITE.random_search.found[0]',
    'blocks': [[0, 1, 2, 4], [0, 1, 2, 5], [0, 1, 3, 4], [0, 1, 4, 6], [0, 1, 5, 6],
               [0, 2, 3, 6], [0, 2, 4, 5], [0, 2, 4, 6], [0, 3, 4, 5]]}
N9 = {  # the only no-common-core C1 candidate found (screening, seed 20261018)
    'name': 'n9_no_common_core', 'npts': 9, 'provenance': 'domain screening search, seed 20261018',
    'blocks': [[0, 1, 2, 3, 7], [0, 1, 2, 6, 8], [0, 1, 4, 5, 8], [0, 1, 4, 6], [0, 1, 5],
               [0, 1, 6, 7, 8], [0, 2, 3, 4, 7], [0, 2, 4, 5, 8], [0, 2, 5], [0, 2, 5, 6],
               [0, 3, 4], [0, 3, 4, 5, 6], [0, 4], [0, 7], [1, 2, 3, 4, 6]]}


# ---------------------------------------------------------------- instrumented evaluation counter
class Meter:
    def __init__(self):
        self.n = 0
    def touch(self, k=1):
        self.n += k


def tau_star(blocks, npts):
    full = (1 << npts) - 1
    masks = [sum(1 << x for x in B) for B in blocks]
    dist = {0: 0}
    q = collections.deque([0])
    while q:
        s = q.popleft()
        for mm in masks:
            t = s | mm
            if t not in dist:
                dist[t] = dist[s] + 1
                if t == full:
                    return dist[t]
                q.append(t)
    return dist.get(full)


def lp_star(blocks, npts):
    """exact rational simplex (dual): max sum phi s.t. per-block <= 1, phi >= 0."""
    m, n = len(blocks), npts
    T = []
    for i, B in enumerate(blocks):
        row = [Fraction(1) if x in B else Fraction(0) for x in range(n)]
        row += [Fraction(1) if j == i else Fraction(0) for j in range(m)]
        row += [Fraction(1)]
        T.append(row)
    c = [Fraction(1)] * n + [Fraction(0)] * m
    basis = [n + i for i in range(m)]
    while True:
        cB = [c[b] for b in basis]
        rc = [c[j] - sum(cB[i] * T[i][j] for i in range(m) if T[i][j]) for j in range(n + m)]
        enter = next((j for j in range(n + m) if rc[j] > 0), None)
        if enter is None:
            break
        ratio, leave = None, None
        for i in range(m):
            if T[i][enter] > 0:
                r = T[i][-1] / T[i][enter]
                if ratio is None or r < ratio or (r == ratio and basis[i] < basis[leave]):
                    ratio, leave = r, i
        if leave is None:
            return None
        piv = T[leave][enter]
        T[leave] = [v / piv for v in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter]:
                f = T[i][enter]
                T[i] = [a - f * b for a, b in zip(T[i], T[leave])]
        basis[leave] = enter
    return sum(c[b] * T[i][-1] for i, b in enumerate(basis))


# ---------------------------------------------------------------- certificates as checkable schemas
def cert_raw_enum(inst, meter, raw_enabled):
    """ORACLE-style: enumerate every pair of blocks and test coverage.  No lemma, no reduction."""
    if not raw_enabled:
        return {'ok': False, 'why': 'needs raw enumeration (disabled)', 'bound': None}
    bl = [set(b) for b in inst['blocks']]
    npts = inst['npts']
    for i, j in itertools.combinations(range(len(bl)), 2):
        meter.touch(1)                                  # one pair examined (raw unit)
        if len(bl[i] | bl[j]) == npts:
            return {'ok': True, 'why': 'a 2-cover exists (enumerated)', 'bound': None, 'covers': True}
    return {'ok': True, 'why': 'no 2-cover among all C(m,2) pairs', 'bound': 3, 'covers': False}


def cert_common_core_complementarity(inst, meter, raw_enabled):
    """DISCOVERY-CANDIDATE: family lemma for common-core uniform-size families.
    Lemma: if every block contains core C and has size b, a 2-cover forces the two blocks to meet
    exactly in C with complementary remainder parts; hence no complementary pair => tau >= 3."""
    bl = [set(b) for b in inst['blocks']]
    V = set(range(inst['npts']))
    steps = []
    core = set.intersection(*bl) if bl else set()
    sizes = set(len(b) for b in bl)
    for b in bl:
        meter.touch(1)
    steps.append(('structure', len(core) >= 1 and len(sizes) == 1,
                  'common core |C|=%d, uniform size=%s' % (len(core), sorted(sizes))))
    if not steps[-1][1]:
        return {'ok': False, 'why': 'family assumptions not met', 'steps': steps}
    parts = [frozenset(b - core) for b in bl]
    Vc = V - core
    ncomp = 0
    for p in parts:
        meter.touch(1)                                  # one complement lookup (reduced unit)
        if frozenset(Vc - set(p)) in set(parts):
            ncomp += 1
    steps.append(('complementarity', ncomp == 0,
                  'complementary pairs among %d remainder parts: %d' % (len(parts), ncomp)))
    return {'ok': ncomp == 0, 'why': 'no complementary pair', 'bound': 3 if ncomp == 0 else None,
            'steps': steps}


def cert_almost_common_core(inst, meter, raw_enabled):
    """DISCOVERY-CANDIDATE for the n=9 candidate: lemma for families where exactly one block omits a
    point p contained in all others.  A 2-cover must be either (i) that exceptional block plus a block
    containing {p} u (V \\ exceptional), or (ii) two blocks of maximal size intersecting exactly in
    {p} with complementary remainder parts."""
    bl = [set(b) for b in inst['blocks']]
    V = set(range(inst['npts']))
    cnt = collections.Counter(x for b in bl for x in b)
    p = max(cnt, key=lambda x: cnt[x])
    exceptional = [b for b in bl if p not in b]
    steps = [('structure', len(exceptional) <= 1,
              'point %d in %d/%d blocks; exceptional blocks omitting it: %d'
              % (p, cnt[p], len(bl), len(exceptional)))]
    for b in bl:
        meter.touch(1)
    if len(exceptional) > 1:
        return {'ok': False, 'why': 'family assumptions not met', 'steps': steps}
    # case (i): exceptional block + a block containing p and everything outside the exceptional block
    ok_i = False
    for e in exceptional:
        need = {p} | (V - e)
        for b in bl:
            meter.touch(1)
            if need <= b:
                ok_i = True
    steps.append(('case_i', not ok_i, 'exceptional-block case impossible: %s' % (not ok_i)))
    # case (ii): two max-size blocks containing p, meeting exactly in {p}, parts complementary
    bmax = max(len(b) for b in bl)
    big = [b for b in bl if p in b and len(b) == bmax]
    parts_big = set(frozenset(b - {p}) for b in big)
    Vp = V - {p}
    ncomp = 0
    for b in big:
        meter.touch(1)                                  # one complement lookup (reduced unit)
        if frozenset(Vp - set(b - {p})) in parts_big:
            ncomp += 1
    steps.append(('case_ii', ncomp == 0, 'complementary max-size pairs: %d' % ncomp))
    ok = (not ok_i) and ncomp == 0
    return {'ok': ok, 'why': 'both cases impossible' if ok else 'a structural case succeeded',
            'bound': 3 if ok else None, 'steps': steps}


# ---------------------------------------------------------------- D-C1 classifier
def classify(inst, cert, raw_enabled=True):
    """Mechanically evaluate (a)-(d).  Shrinkage is MEASURED by running an instrumented raw baseline
    on the same instance."""
    lemma_family = cert.get('family', '')
    m_red = Meter()
    res = cert['run'](inst, m_red, raw_enabled)
    # measured raw baseline on the same instance
    m_raw = Meter()
    raw_res = cert_raw_enum(inst, m_raw, True)
    raw_size, red_size = m_raw.n, m_red.n
    (a) = bool(lemma_family) and bool(res.get('ok')) and bool(res.get('steps'))
    (b) = red_size < raw_size
    (c) = bool(res.get('steps')) and all(s[1] for s in res.get('steps', []))
    m_ind = Meter()
    ind_res = cert['run'](inst, m_ind, False)       # raw enumeration DISABLED
    (d) = bool(ind_res.get('ok')) and (ind_res.get('bound') == res.get('bound'))
    if (a) and (b) and (c) and (d):
        cls = 'DISCOVERY'
    elif cert.get('uses_raw_enum'):
        cls = 'ORACLE'
    else:
        cls = 'UNCLASSIFIED'
    return {'cert': cert['name'], 'instance': inst['name'], 'classification': cls,
            'a_structure_dependence': a, 'b_shrinkage': b, 'c_auditability': c, 'd_independence': d,
            'raw_size': raw_size, 'reduced_size': red_size,
            'shrinkage': (None if red_size == 0 else round(raw_size / red_size, 2)),
            'derived_bound': res.get('bound'), 'why': res.get('why'),
            'steps': res.get('steps', [])}


CERTS = [
    {'name': 'raw_enumeration', 'family': '', 'uses_raw_enum': True, 'run': cert_raw_enum},
    {'name': 'common_core_complementarity', 'family': 'common-core uniform-size families',
     'uses_raw_enum': False, 'run': cert_common_core_complementarity},
    {'name': 'almost_common_core_reduction', 'family': 'families with <=1 core-omitting block',
     'uses_raw_enum': False, 'run': cert_almost_common_core},
]


def main():
    out = {'spec': 'L8-1-DC1-v1', 'regression': [], 'n9_audit': None,
           'C1_modified': 'Delta_disc = B_multi - B_single > 0',
           'baseline_coverage_note': 'a finite search bounds only the given operation set and budget'}
    print('=== D-C1 v1 regression on the n=7 known cases ===')
    for inst in (N7,):
        ts = tau_star([frozenset(b) for b in inst['blocks']], inst['npts'])
        lp = lp_star([frozenset(b) for b in inst['blocks']], inst['npts'])
        print('%s: tau*= %s  LP*= %s' % (inst['name'], ts, lp))
        for cert in CERTS:
            if cert['name'] == 'almost_common_core_reduction':
                continue
            r = classify(inst, cert)
            out['regression'].append(r)
            print('  %-32s -> %-13s a=%s b=%s c=%s d=%s  raw=%d red=%d shrink=%s bound=%s'
                  % (r['cert'], r['classification'], r['a_structure_dependence'], r['b_shrinkage'],
                     r['c_auditability'], r['d_independence'], r['raw_size'], r['reduced_size'],
                     r['shrinkage'], r['derived_bound']))
            for s in r['steps']:
                print('       step %-14s ok=%-5s %s' % (s[0], s[1], s[2]))

    print('\n=== n=9 candidate audit (D-C1 structural-reduction audit) ===')
    bl9 = [frozenset(b) for b in N9['blocks']]
    ts9 = tau_star(bl9, N9['npts'])
    lp9 = lp_star(bl9, N9['npts'])
    print('n9: tau*= %s  LP*= %s  |B|=%d' % (ts9, lp9, len(bl9)))
    r9 = classify(N9, CERTS[2])
    r9raw = classify(N9, CERTS[0])
    out['n9_audit'] = {'structural': r9, 'raw': r9raw, 'tau_star': ts9, 'LP_star': str(lp9)}
    print('  raw_enumeration         -> %s (raw=%d)' % (r9raw['classification'], r9raw['raw_size']))
    print('  almost_common_core      -> %s  bound=%s  raw=%d red=%d shrink=%s'
          % (r9['classification'], r9['derived_bound'], r9['raw_size'], r9['reduced_size'],
             r9['shrinkage']))
    for s in r9['steps']:
        print('       step %-14s ok=%-5s %s' % (s[0], s[1], s[2]))
    B_single = 3 if r9['classification'] == 'DISCOVERY' and r9['derived_bound'] == 3 else 2
    out['n9_audit']['B_single'] = B_single
    out['n9_audit']['Delta_disc'] = ts9 - B_single
    print('  => B_single = %s ; Delta_disc = tau* - B_single = %s  -> %s'
          % (B_single, ts9 - B_single,
             'CANDIDATE ELIMINATED (single-step discovery reaches tau*)' if ts9 - B_single <= 0
             else 'survives'))
    json.dump(out, open(os.path.join(HERE, 'L8-1-DC1-v1-RESULT.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
