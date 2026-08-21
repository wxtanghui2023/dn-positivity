#!/usr/bin/env python3
"""
Deep analysis of epsilon_m decay structure for strictification.
Focus: 
1. Decay rate of |eps_m| as function of m
2. eps_m = J_m - Jsm_m decomposition: which part dominates error?
3. Is eps_m bounded by C * (m-th block main term) * (small factor)?
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*math.atan(2*t)

def full_analysis(n):
    th = np.array([theta(g) for g in z])
    phi = (n+0.5)*th
    f = 2*np.sin(phi)*np.sin(th/2.0)
    mask = phi >= math.pi
    phi_n, f_n, th_n = phi[mask], f[mask], th[mask]
    m_idx = np.floor(phi_n/math.pi).astype(int)
    Mmax = m_idx.max() if len(m_idx) else 0
    J = np.zeros(Mmax+1); cnt = np.zeros(Mmax+1)
    for i, m in enumerate(m_idx):
        J[m] += f_n[i]; cnt[m] += 1
    Jsm = np.zeros(Mmax+1)
    for m in range(1, Mmax+1):
        xi = (m+0.5)*math.pi
        Jsm[m] = (-1)**m * math.log((n+0.5)/(2*math.pi*xi))/(math.pi*xi)
    eps = J[1:Mmax+1] - Jsm[1:Mmax+1]
    mlist = np.arange(1, Mmax+1)
    aeps = np.abs(eps)
    # decay fit: |eps_m| ~ C / m^p ?
    # check ratio eps_{m+1}/eps_m and m*|eps_m|
    print(f"\n=== n={n} 衰减分析 (M={Mmax}) ===")
    print(f"  {'m':>4} {'|eps_m|':>10} {'|J_m|':>10} {'|Jsm_m|':>10} {'m·|eps|':>10} {'m²·|eps|':>10}")
    for m in mlist[:12]:
        print(f"  {m:4d} {aeps[m-1]:10.6f} {abs(J[m]):10.6f} {abs(Jsm[m]):10.6f} {m*aeps[m-1]:10.6f} {m*m*aeps[m-1]:10.6f}")
    # ratio analysis over stable range
    r = aeps[1:]/np.maximum(aeps[:-1],1e-12)
    print(f"  eps 比值 r_m=eps_{'{m+1}'}/eps_m (m=2..10):")
    print("   ", [f"{r[i]:.3f}" for i in range(1,10)])
    # main term ratio: Jsm decays ~ log(n/m)/m, so m*|Jsm| ~ log(n/m)/pi^2
    print(f"  m·|Jsm_m| (m=1..8): {[f'{m*abs(Jsm[m]):.4f}' for m in range(1,9)]}")
    # key question: is |eps_m| <= C * (log n)/m^2 ? (summable => O(1))
    c2 = np.max(aeps * mlist**2 / math.log(n))
    print(f"  max m²·|eps_m|/log n = {c2:.5f}")
    # is |eps_m| <= C/m^1.5 ?
    c15 = np.max(aeps * mlist**1.5)
    print(f"  max m^1.5·|eps_m| = {c15:.5f}")
    # tail sum from m0
    for m0 in [10, 20, 50]:
        print(f"  Σ_{{m≥{m0}}}|eps_m| = {aeps[m0-1:].sum():.5f}")
    return aeps, mlist, J, Jsm, eps

for n in [10000, 20000]:
    aeps, mlist, J, Jsm, eps = full_analysis(n)
