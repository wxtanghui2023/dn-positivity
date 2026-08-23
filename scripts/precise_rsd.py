#!/usr/bin/env python3
"""精确验证：f̃ 核黎曼和差 = Σ_k f̃(γ_k) − ∫f̃ N₀' 是否 = r(n)（参考值）
每区间精确积分（8点 Gauss——不抽样）——用向量化块处理
同时验证 Σ w_k δ_k（Abel 项）与黎曼和差的关系：黎曼和差 = -Σw_kδ_k - ΣEM_k
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def N0p(t):
    return np.log(t/(2*np.pi))/(2*np.pi)

def ftilde(t, c):
    th = np.pi - 2*np.arctan(2*t)
    return 2*np.sin(c*th)*np.sin(th/2)

K = 2000000
z = load_zeros(K)
Tmax = z[-1]
xg, wg = leggauss(8)

def ftilde_rsd(c, verbose=False):
    """f̃ 核黎曼和差：Σ f̃(γ_k) − ∫_2^∞ f̃ N₀' dt（每区间 8点 Gauss——向量化）"""
    Sf = np.sum(ftilde(z, c))  # Σ f̃(γ_k)——含尾部分解
    # 每区间 [γ_k, γ_{k+1}] 积分——向量化（分块）
    a = z[:-1]; b = z[1:]
    half = 0.5*(b-a); mid = 0.5*(a+b)
    # 8点 Gauss 向量化：ts shape (K-1, 8)
    ts = half[:,None]*xg[None,:] + mid[:,None]
    fv = ftilde(ts, c)  # (K-1, 8)
    Nv = N0p(ts)
    vals = half[:,None]*wg[None,:]*fv*Nv  # 每区间积分贡献
    Int_interval = np.sum(vals, axis=1)
    Int = np.sum(Int_interval)
    # 尾部 [γ_max, ∞)：f̃ ~ c/t²（t 大——θ≈1/t——f̃ = 2sin(cθ)sin(θ/2) ≈ c/t²）
    tail = c*(np.log(Tmax/(2*np.pi))/Tmax + 1/Tmax)/(2*np.pi)
    Int_total = Int + tail
    if verbose:
        print(f"  Σf̃(γ_k) = {Sf:+.4f}, ∫f̃N₀' = {Int_total:+.4f}（区间 {Int:+.4f} + 尾 {tail:+.6f}）")
    return Sf - Int_total

ref = {50: 2.25, 100: 1.38, 200: 2.89, 500: -0.07, 1000: 2.51}
print("f̃ 核黎曼和差（精确每区间）vs r(n) 参考：")
for n in [50, 100, 200, 500, 1000]:
    c = n + 0.5
    D = ftilde_rsd(c, verbose=True)
    print(f"  n={n:4d}: f̃ 核黎曼和差 = {D:+8.4f}  |  r(n)参考 = {ref[n]:+8.2f}")

# 也检查 f_n 核（用每区间精确）——确认 r(n) 参考
print("\nf_n 核黎曼和差（精确每区间）vs r(n) 参考：")
def fn(t, n):
    return 4*np.sin(n*np.arctan(1/(2*t)))**2

for n in [100, 500]:
    Sf = np.sum(fn(z, n))
    a = z[:-1]; b = z[1:]
    half = 0.5*(b-a); mid = 0.5*(a+b)
    ts = half[:,None]*xg[None,:] + mid[:,None]
    fv = fn(ts, n); Nv = N0p(ts)
    Int = np.sum(np.sum(half[:,None]*wg[None,:]*fv*Nv, axis=1))
    tail = n**2*(np.log(Tmax/(2*np.pi))/Tmax + 1/Tmax)/(2*np.pi)
    print(f"  n={n:4d}: Σf_n={Sf:+.3f}, ∫f_nN₀'={Int+tail:+.3f}, 差={Sf-Int-tail:+8.4f} | r(n)参考={ref[n]:+.2f}")
