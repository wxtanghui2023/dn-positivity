#!/usr/bin/env python3
# 外推验证：β(X) = β_∞ − c/X——X→∞——截距 β_∞ 是否 = ½？（运动终点是否支持离轴）
import numpy as np
import mpmath as mp

def zeta_smooth_np(s, X, nmax_factor=30):
    """纯 numpy——float64 精度（β ~1e-4 够）"""
    nmax = max(int(nmax_factor*X), 300)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def zero_beta(X, seed_gamma, beta_guess=0.5):
    """找 ζ_X 在 γ≈seed 附近的零点（β 输出——）"""
    z = complex(beta_guess, seed_gamma)
    for it in range(60):
        f = zeta_smooth_np(z, X)
        h = 1e-6 + 1e-6j
        fp = (zeta_smooth_np(z+h, X) - zeta_smooth_np(z-h, X)) / (2*h)
        step = f/fp
        z = z - step
        if abs(step) < 1e-11:
            break
    return z.real, z.imag

# 对前 4 个零点——X 从 200 到 2000——β(X)——外推截距
known = [14.1347, 21.0220, 25.0109, 30.4249]
X_list = [200, 300, 500, 800, 1200, 2000]

print("=== β(X) 外推（X→∞——截距 = 终点 β_ζ？——） ===")
for gk in known:
    print(f"\n--- γ_ζ ≈ {gk} ---")
    betas = []
    for X in X_list:
        b, g = zero_beta(X, gk)
        betas.append((X, b))
        print(f"   X={X:>5}: β = {b:.6f}  (½−β)·X = {(0.5-b)*X:.4f}")
    # 线性外推 β vs 1/X——截距
    xs = np.array([1.0/X for X, _ in betas])
    ys = np.array([b for _, b in betas])
    coef = np.polyfit(xs, ys, 1)  # β = coef[0]/X + coef[1]
    print(f"   外推: β(X) = {coef[0]:.4f}/X + {coef[1]:.6f}  ⟹ β_∞ = {coef[1]:.6f}  (½−β_∞ = {0.5-coef[1]:+.2e})")
