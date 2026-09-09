#!/usr/bin/env python3
"""验证: 区间平均是否滤掉 S(t) 展开误差
S(t)（逐点——）vs Sbar（区间平均——）的展开残差对比
如果 S(t) 残差 ~O(1)（Titchmarsh——）而 Sbar 残差小——平均滤掉是真效应——
如果 S(t) 残差也小——Titchmarsh O(1) 保守——证明可能容易——
"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 100000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

dg = np.diff(z[:K])
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar = kk - (IntN[1:] - IntN[:-1])/dg
t_mid = (z[:-1] + z[1:])/2

# S(t) 逐点（在零点处的右极限——S(γ_k+) = k - N0(γ_k)）
S_point = kk - IntN[:-1]  # N(γ_k) = k（近似——在零点——右——）

# 展开（理论——含谐波——）
primes = []
for n in range(2, 200):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)

def expansion(t, pmax, kmax, with_sign=True):
    """S 的展开: -(1/π)Σ_p Σ_k sin(k log p t)/(k p^(k/2))·(修正——)"""
    val = np.zeros(len(t))
    for p in primes:
        if p > pmax: break
        for k in range(1, kmax+1):
            if k == 1:
                # 基频: 1/(π√p log p)？（Titchmarsh 的 S 展开——）
                pass
    return val

# 简化: 用拟合系数展开（对 S_point 和 Sbar 都拟合——）看残差
def fit_expand(y, t, plist, kmax):
    cols = []
    for p in plist:
        cols.append(np.sin(t * log(p)))
        cols.append(np.cos(t * log(p)))
    for p in plist[:15]:
        for k in range(2, kmax+1):
            cols.append(np.sin(k*t * log(p)))
            cols.append(np.cos(k*t * log(p)))
    X = np.stack(cols, axis=1)
    c, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ c
    return resid, X @ c

plist = primes
# S_point 在零点处——t 用 z[:-1]（零点位置——）
t_pt = z[:-1]
# 采样（每 10 个——省时间——）
step = 10
t_s = t_mid[::step]
Sbar_s = Sbar[::step]
Spt_s = S_point[::step]
t_pts = t_pt[::step]

print('=== S(t) 逐点 vs Sbar 的展开残差 ===')
for kmax in [1, 2, 3]:
    r_bar, _ = fit_expand(Sbar_s, t_s, plist, kmax)
    r_pt, _ = fit_expand(Spt_s, t_pts, plist, kmax)
    print(f'k≤{kmax}: Sbar 残差 std={r_bar.std():.4f}——S(逐点) 残差 std={r_pt.std():.4f}')

# S(t) 逐点残差的性质——高频还是 O(1) 漂移?
print()
r_pt_full, _ = fit_expand(Spt_s, t_pts, plist, 3)
print(f'S(逐点) 残差（k≤3——）: mean={r_pt_full.mean():+.4f}——std={r_pt_full.std():.4f}——max={np.max(np.abs(r_pt_full)):.4f}')
# 分段看残差（是否 ~O(1) 漂移还是振荡——）
for i in range(0, len(r_pt_full), 2000):
    seg = r_pt_full[i:i+2000]
    print(f'  段{i}: mean={seg.mean():+.3f}——std={seg.std():.3f}——max|={np.max(np.abs(seg)):.3f}')
