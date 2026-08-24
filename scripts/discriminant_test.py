#!/usr/bin/env python3
"""唐先生的数值验证方向：构造假想离轴配置——定理 B 的判别力
方案1：保持虚部 γ_k 不变——只改实部 β（某零点移到离轴）
  - Σ_k f_n(γ_k)（定理 B——虚部核）是否变化？（预期：不变——f_n 只看虚部）
  - λ_n（含 β）是否变化？（预期：变化——指数）
方案2：引入同虚部对称对（ρ 和 1−ρ̄——同虚部 γ——虚部重复）
  - Σ_k f_n(γ_k) 是否偏离定理 B 的界？
"""
import numpy as np
import gc
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(200000)

def th1(t):
    return np.arctan(1/(2*t))

def lam_n(n, z, beta_all=0.5):
    """λ_n（含 β——每个零点可离轴）——用无条件公式 Σ[1−(1−1/ρ)^n] 上下对"""
    # 简化：全部 β 相同（beta_all）——z 是虚部
    rho = beta_all + 1j*z
    omr = 1 - 1/rho
    # 上下对（ρ, ρ̄）的贡献：2 − 2Re[(1−1/ρ)^n]
    contrib = 2 - 2*np.real(omr**n)
    return np.sum(contrib)

def sum_fn(n, z):
    """Σ_k f_n(γ_k)——定理 B 的虚部核"""
    return 4*np.sum(np.sin(n*th1(z))**2)

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

gamma_E = 0.5772156649015329
c = 0.5*(gamma_E - 1 - log(2*pi))

# 方案1：保持虚部——改 β（全部零点移到 β₀≠½）
print("方案1：保持虚部 γ_k——改 β（所有零点 → β₀）：")
print(f"{'β₀':>6} {'Σ_k f_n（定理B）':>16} {'λ_n（含β）':>14} {'λ_n−主项':>12}")
for beta0 in [0.5, 0.45, 0.4, 0.3]:
    s_fn = sum_fn(100, z[:50000])
    l_n = lam_n(100, z[:50000], beta0)
    main = 0.5*100*log(100) + c*100
    print(f"{beta0:6.2f} {s_fn:16.4f} {l_n:14.4f} {l_n-main:+12.2f}")

# 方案2：引入同虚部对称对（第 100 个零点——同虚部两个——β=0.4 和 1−0.4）
print("\n方案2：同虚部对称对（γ_100 处两个零点——β=0.4 和 0.6）：")
print("  虚部序列变化：γ_100 出现两次（重复）——Σ_k f_n 多计数")
# 构造：z2 = z 前 100000 个 + 在 γ_100 处插入一个（同虚部）
z2 = np.concatenate([z[:100001], [z[100]]])  # 在 γ_100 后插入重复
# 但"重复"的零点其实是 1−ρ̄（同虚部——β=0.6）——对 Σ_k f_n 只看虚部——重复计数
for n in [100]:
    s_orig = sum_fn(n, z[:100001])
    s_dup = sum_fn(n, z2)
    print(f"  n={n}: Σ_k f_n 原始 = {s_orig:.4f}  重复 = {s_dup:.4f}  差 = {s_dup-s_orig:+.4f}")
    print(f"  （重复 +f_n(γ_100) = {4*np.sin(n*th1(z[100]))**2:.4f}——多计数的量）")
    # λ_n（含 β——同虚部两个：β=0.4 和 0.6——虚部 γ_100）
    rho1 = 0.4 + 1j*z[100]
    rho2 = 0.6 + 1j*z[100]
    contrib = (2 - 2*np.real((1-1/rho1)**n)) + (2 - 2*np.real((1-1/rho2)**n))
    print(f"  同虚部对的 λ_n 贡献（β=0.4 和 0.6）= {contrib:+.4f}")
    print(f"  （vs 临界线假设 2×4sin²(nθ₁(γ_100)) = {2*4*np.sin(n*th1(z[100]))**2:.4f}）")

del z, z2
gc.collect()
print("内存已释放")
