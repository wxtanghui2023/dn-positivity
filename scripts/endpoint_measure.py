#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 多高度终点测量：12 个零点（γ 14→90）——验证 β(X) ≈ ½ − c/X（截距 = ½——终点常数？）
# c(γ) = −Re[ζ(ρ−1)/ζ'(ρ)]（精确公式——已验证 4 个——）
# β(X=1000) 数值（平滑截断——）vs 预测 ½ − c/1000——残差小 ⟹ 截距 ½
import numpy as np
import mpmath as mp
mp.mp.dps = 15

# ζ 零点虚部（前 12 个）
known = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862,
         40.9187, 43.3271, 48.0052, 49.7738, 52.9703, 56.4462]

def c_formula(gamma):
    """c(γ) = −Re[ζ(ρ−1)/ζ'(ρ)]——ρ = ½+iγ"""
    rho = 0.5 + 1j*gamma
    z_m1 = mp.zeta(rho - 1)
    z1 = mp.zeta(rho, derivative=1)
    return -float(mp.re(z_m1 / z1))

def zeta_smooth_np(s, X, nmax_factor=30):
    nmax = max(int(nmax_factor*X), 300)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def beta_numeric(X, gamma, beta_guess=0.5):
    """ζ_X 在 γ≈gamma 的零点实部（数值——牛顿——）"""
    z = complex(beta_guess, gamma)
    for it in range(60):
        f = zeta_smooth_np(z, X)
        h = 1e-6 + 1e-6j
        fp = (zeta_smooth_np(z+h, X) - zeta_smooth_np(z-h, X)) / (2*h)
        step = f/fp
        z = z - step
        if abs(step) < 1e-10:
            break
    return z.real

X = 1000
print(f"=== 终点测量：β(X={X}) vs ½ − c/X——12 个零点 ===")
print(f"{'γ':>8} {'c(γ)':>8} {'β_num':>9} {'½−c/X':>9} {'残差':>10}")
resid_all = []
for g in known:
    c = c_formula(g)
    pred = 0.5 - c/X
    b = beta_numeric(X, g)
    resid = abs(b - pred)
    resid_all.append(resid)
    flag = "✓" if resid < 3e-4 else "  <-- 偏离!"
    print(f"{g:>8.4f} {c:>8.3f} {b:>9.6f} {pred:>9.6f} {resid:>10.2e} {flag}")

print(f"\n残差统计: max={max(resid_all):.2e}  mean={np.mean(resid_all):.2e}")
print(f"如果全部残差 < 3e-4 ⟹ β(X) = ½ − c/X 精确（截距 = ½——终点常数——）")
