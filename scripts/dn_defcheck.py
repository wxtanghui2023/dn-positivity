#!/usr/bin/env python3
"""
CLARIFY THE DEFINITION: is D_neg = {phi >= pi} (ALL blocks m>=1) or {sin(phi)<0} (odd blocks only)?
This determines whether sum_{m=1}^{M'} eps_m (my bound) is exactly the D_neg error term.

From the paper: phase-region split D_n = D_pos + D_neg with
  D_pos = {phi_k < pi}, D_neg = {phi_k >= pi}  (GEOMETRIC split by phi, not by sign of sin)
Check numerically: D_neg = sum_{k: phi_k>=pi} f(gamma_k) == sum_{m=1}^{M'} J_m (all m) ?
And: is D_pos all-positive terms? Is D_neg an alternating sum over blocks m=1..M'?
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))

for n in [100, 1000, 5000]:
    th = theta(z); phi = (n+0.5)*th
    f = 2*np.sin(phi)*np.sin(th/2)
    # Definition A: D_neg = {phi >= pi}, D_pos = {phi < pi}
    mask_neg = phi >= math.pi
    Dneg_A = f[mask_neg].sum()
    Dpos_A = f[~mask_neg].sum()
    # Definition B: D_neg = {sin(phi) < 0}
    mask_negB = np.sin(phi) < 0
    Dneg_B = f[mask_negB].sum()
    Dpos_B = f[~mask_negB].sum()
    # Block sum: J_m = sum over B_m, m=1..M'
    phi_neg = phi[mask_neg]
    m_idx = np.floor(phi_neg/math.pi).astype(int)
    Mmax = m_idx.max() if len(m_idx) else 0
    J = np.zeros(Mmax+1)
    for i, m in enumerate(m_idx): J[m] += f[mask_neg][i]
    block_sum = J[1:].sum()
    print(f"n={n}: M'={Mmax}")
    print(f"  D_neg(A, phi>=pi) = {Dneg_A:+.5f}   vs Σ J_m (m=1..M') = {block_sum:+.5f}   match={abs(Dneg_A-block_sum)<1e-9}")
    print(f"  D_pos(A, phi<pi)  = {Dpos_A:+.5f}   (所有项为正? {np.all(f[~mask_neg]>0)})")
    print(f"  D_neg(B, sin<0)   = {Dneg_B:+.5f}   D_pos(B, sin>=0) = {Dpos_B:+.5f}")
    print(f"  J_m 符号: m=1..8: {[f'{J[m]:+.4f}' for m in range(1,min(9,Mmax+1))]}")
    print()
