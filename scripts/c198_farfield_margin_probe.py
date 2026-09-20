#!/usr/bin/env python3
"""
C-198: T13-B / w=2 —— 远场 margin 探针（【探索性】，不是证书！）
目的：只回答"远场是否存在 F-1 极小的窄脊/边界层"，以决定远场走一尺度还是两尺度。
"""
import numpy as np
from scipy.optimize import minimize
np.set_printoptions(precision=6, suppress=True)

P1, P2 = np.pi/3, np.pi/2
KMAX = 10
R = 0.1

def F(d1, d2):
    return max(2*np.cos(k*(P1+d1)) + np.cos(k*(P2+d2)) for k in range(1, KMAX+1))

def Fvec(D1, D2):
    V = np.full(D1.shape, -9.0)
    for k in range(1, KMAX+1):
        V = np.maximum(V, 2*np.cos(k*(P1+D1)) + np.cos(k*(P2+D2)))
    return V

def active(d1, d2, tol=1e-9):
    vals = {k: 2*np.cos(k*(P1+d1)) + np.cos(k*(P2+d2)) for k in range(1, KMAX+1)}
    m = max(vals.values())
    return [k for k, v in vals.items() if m - v < tol], m

print("="*80)
print("C-198  远场 margin 探针（探索性，非证书）   F = max_{k<=10} Sk")
print("="*80)

# ---------- ① 粗网格定位（全域 + 用户子盒） ----------
N = 2000
d1 = np.linspace(-np.pi/3, 2*np.pi/3, N+1)
d2 = np.linspace(-np.pi/2, np.pi/2, N+1)
D1, D2 = np.meshgrid(d1, d2, indexing='ij')
V = Fvec(D1, D2)
ball = (D1**2 + D2**2) <= R*R
Vfar = np.where(ball, np.inf, V)

def report(mask_name, M):
    i, j = np.unravel_index(np.nanargmin(M), M.shape)
    x1, x2 = D1[i, j], D2[i, j]
    dist = max(0.0, float(np.hypot(x1, x2)) - R)
    act, mx = active(x1, x2)
    print(f"\n--- {mask_name} ---")
    print(f"  粗略 min F          = {M[i,j]:.12f}")
    print(f"  粗略 margin (min F-1) = {M[i,j]-1.0:+.6e}")
    print(f"  最危险点 (δ1,δ2)     = ({x1:+.9f}, {x2:+.9f})   [φ/π = ({(P1+x1)/np.pi:.9f}, {(P2+x2)/np.pi:.9f})]")
    print(f"  到 r=0.1 边界的距离   = {dist:.6e}")
    print(f"  该点 active k 集合    = {act}   (F = {mx:.12f})")
    return (x1, x2), M[i,j]

pt_full, m_full = report("全域 D_far = [−π/3,2π/3]×[−π/2,π/2] \\ B_{0.1}", Vfar)
sub = ball | (D1 < -np.pi/3-1e-12) | (D1 > np.pi/3+1e-12) | (D2 < -np.pi/3-1e-12) | (D2 > np.pi/3+1e-12)
pt_sub, m_sub = report("用户子盒 D_far = [−π/3,π/3]² \\ B_{0.1}", np.where(sub, np.inf, V))

# ---------- 危险区面积占比 ----------
print("\n--- 危险区面积占比（全域内，F-1 ≤ ε 的比例）---")
Vf = V[~ball]-1.0
for eps in (1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4):
    frac = float((Vf <= eps).mean())
    print(f"  ε={eps:.0e}: {frac*100:8.4f}%   （{int(frac*Vf.size)} 点）")

# ---------- ② 局部连续最小化（约束 δ1²+δ2² ≥ R²）----------
print("\n--- ② 局部连续最小化（SLSQP，约束 δ1²+δ2² ≥ 0.01；允许落在圆边界）---")
Vt = np.where(ball, np.inf, V)
flat = np.argsort(Vt.ravel())[:20]
starts = [(D1.ravel()[t], D2.ravel()[t]) for t in flat]
best = (np.inf, None)
for s in starts:
    con = {'type': 'ineq', 'fun': lambda x: x[0]**2 + x[1]**2 - R*R}
    r = minimize(lambda x: F(x[0], x[1]), s, method='SLSQP',
                 constraints=[con], options={'maxiter': 400, 'ftol': 1e-14})
    if r.fun < best[0]: best = (r.fun, r.x)
    # 也从圆边界上的投影点起
    n = np.hypot(*s);
    if n > 0:
        s2 = np.array(s)/n*R
        r2 = minimize(lambda x: F(x[0], x[1]), s2, method='SLSQP',
                      constraints=[con], options={'maxiter': 400, 'ftol': 1e-14})
        if r2.fun < best[0]: best = (r2.fun, r2.x)

mf, xf = best
actf, _ = active(xf[0], xf[1])
distf = float(np.hypot(*xf) - R)
print(f"  精修 min F         = {mf:.12f}")
print(f"  精修 margin        = {mf-1.0:+.6e}")
print(f"  精修最危险点        = ({xf[0]:+.9f}, {xf[1]:+.9f})   |δ| = {np.hypot(*xf):.9f}")
print(f"  到 r=0.1 的距离     = {distf:+.6e}   {'（落在圆边界上 ✓）' if abs(distf)<1e-6 else ''}")
print(f"  active k            = {actf}")

# ---------- ③ 工程分叉 ----------
print("\n--- ③ 工程分叉估算 ---")
Lglob = 10*np.sqrt(5)
for tag, mu in (("全域粗网格", m_full-1.0), ("精修", mf-1.0)):
    h = mu/Lglob
    Nneed = (2*np.pi/3)/h if h > 0 else np.inf
    print(f"  [{tag}] margin={mu:+.4e}  ⟹ L=10√5={Lglob:.4f} 下 h≈{h:.3e}, 均匀网格侧长≈{Nneed:.3e} ⟹ 点数≈{Nneed**2:.3e}")
print(f"\n  注：active-k 分区可显著降低局部 Lipschitz 常数。最危险点处的逐 k 梯度模：")
for k in range(1, KMAX+1):
    g = np.hypot(2*k*np.sin(k*(P1+xf[0])), k*np.sin(k*(P2+xf[1])))
    if k in actf: print(f"     k={k:2d}  |∇Sk| = {g:.6f}   ← active")
print(f"\n  分叉判断：margin ≳ 1e-2 → 一尺度有希望；~1e-4 → 需两尺度；≈0 且有新结构 → 先做结构分析")
