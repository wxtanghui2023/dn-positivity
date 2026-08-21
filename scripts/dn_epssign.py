#!/usr/bin/env python3
"""
Strictification check: is eps_m * (-1)^m >= 0 for ALL m? (sign synchronization)
If yes, and if |eps_m| decreasing => alternating series => |sum eps_m| <= |eps_1|.
Also check: eps_m bounds relative to block main term.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*math.atan(2*t)

def analyze(n):
    th = np.array([theta(g) for g in z])
    phi = (n+0.5)*th
    f = 2*np.sin(phi)*np.sin(th/2.0)
    mask = phi >= math.pi
    phi_n, f_n = phi[mask], f[mask]
    m_idx = np.floor(phi_n/math.pi).astype(int)
    Mmax = m_idx.max() if len(m_idx) else 0
    J = np.zeros(Mmax+1)
    for i, m in enumerate(m_idx): J[m] += f_n[i]
    Jsm = np.zeros(Mmax+1)
    for m in range(1, Mmax+1):
        xi = (m+0.5)*math.pi
        Jsm[m] = (-1)**m * math.log((n+0.5)/(2*math.pi*xi))/(math.pi*xi)
    eps = J[1:Mmax+1] - Jsm[1:Mmax+1]
    mlist = np.arange(1, Mmax+1)
    s = eps * ((-1.0)**mlist)     # eps_m * (-1)^m
    neg = (s < 0).sum()
    print(f"\nn={n}: M={Mmax}, 违反同步符号的块数: {neg}/{Mmax}")
    if neg:
        idx = np.where(s<0)[0]+1
        print(f"  违反块: {idx[:20]}")
        for m in idx[:10]:
            print(f"    m={m}: J_m={J[m]:+.6f} Jsm={Jsm[m]:+.6f} eps={eps[m-1]:+.6f} (-1)^m={(-1)**m}")
    # monotone decreasing of |eps| ?
    a = np.abs(eps)
    viol = (np.diff(a) > 0).sum()
    print(f"  |eps| 非单调递增次数: {viol}/{Mmax-1}")
    # ratio |eps_m| / |Jsm_m|
    r = a / np.maximum(np.abs(Jsm[1:]),1e-12)
    print(f"  |eps_m|/|Jsm_m|: m=1..10: {[f'{r[i]:.4f}' for i in range(10)]}")
    print(f"  max ratio: {r.max():.4f} at m={np.argmax(r)+1}")
    # |sum eps| vs |eps_1| (alternating series bound)
    print(f"  |Σ eps| = {abs(eps.sum()):.6f}   |eps_1| = {abs(eps[0]):.6f}")
    return eps, mlist

for n in [1000, 5000, 10000, 20000]:
    eps, mlist = analyze(n)
