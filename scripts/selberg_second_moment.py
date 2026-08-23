#!/usr/bin/env python3
"""验证 S(t) 的数值行为 vs Selberg 二阶矩——S 是否无界（慢）？
∫_0^T S(t)²dt ~ (1/2π²)·T·log log T（Selberg 1946——无条件）
S(t) 在区间 [γ_k, γ_{k+1}) 上 = k − N₀(t)（线性下降——精确）
"""
import numpy as np

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def N0(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) + 7/8

K = 2000000
z = load_zeros(K)
T = z[-1]

# S(γ_k⁺) = k − N₀(γ_k)
S_k = np.arange(1, K+1) - N0(z)
print(f"S(γ_k⁺): min={np.min(S_k):+.4f} max={np.max(S_k):+.4f} std={np.std(S_k):.4f}")

# ∫S² dt：分段精确——区间 [γ_k, γ_{k+1}) 上 S(t) = k − N₀(t)（线性——N₀ 缓变）
# 用 4 点 Gauss 每区间（向量化）
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(4)
a = z[:-1]; b = z[1:]
half = 0.5*(b-a); mid = 0.5*(a+b)
ts = half[:,None]*xg[None,:] + mid[:,None]  # (K-1, 4)
ks = np.arange(1, K)[:,None]  # 区间 [γ_k, γ_{k+1}) 上 S = k − N₀
S_vals = ks - N0(ts)
# ∫S² dt per interval
integ = np.sum(half[:,None]*wg[None,:]*S_vals**2, axis=1)
total = np.sum(integ)
# 最后区间 [γ_K, T]——S = K − N₀(t)（T = γ_K——区间退化）
print(f"\n∫_2^T S²dt = {total:.3f}（数值——分段 Gauss）")
print(f"T·log log T/(2π²) = {T*np.log(np.log(T))/(2*np.pi**2):.3f}（Selberg 预测）")
print(f"比值 = {total/(T*np.log(np.log(T))/(2*np.pi**2)):.3f}")

# 分块看 std 增长（S 无界的证据）
print("\n分块 std（每 200k 零点）：")
for i in range(0, K, 200000):
    seg = S_k[i:i+200000]
    print(f"  k={i+1:7d}-{i+200000:7d}: std={np.std(seg):.4f}  max|S|={np.max(np.abs(seg)):.3f}")
