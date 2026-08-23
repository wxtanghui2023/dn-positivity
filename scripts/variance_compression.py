#!/usr/bin/env python3
"""验证"方差完全压缩"：1 + 2Σ_{j≥1}ρ(δ_k, δ_{k+j}) ≈ 0？
如果成立——Σ w_k δ_k 的方差 ~ 0——O(1) 的机制
关键：全滞后相关和 = −1/2 是否可从"密度守恒"（N = N₀ + S——恒等式）推出？
"""
import numpy as np

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 1000000  # 用 1M 快速
z = load_zeros(K)

# δ_k = Δγ_k - 1/N₀'(γ_k)
dg = np.diff(z)
Np = np.log(z[:-1]/(2*np.pi))/(2*np.pi)
delta = dg - 1.0/Np

# 标准化 δ（去均值）
d = delta - np.mean(delta)
s = np.std(d)

# 自相关（到 lag 100）
print("δ 的自相关（累积相关和）：")
cum = 1.0
print(f"  lag-0: ρ = 1.000  →  1+2Σ = {cum:.4f}")
for lag in [1, 2, 3, 5, 10, 20, 50, 100]:
    rho = np.mean(d[:-lag]*d[lag:])/(s*s)
    cum += 2*rho if lag == 1 else 0  # 先只算 lag-1 累积
    print(f"  lag-{lag}: ρ = {rho:+.4f}")

# 完整累积（到 lag 100）
cum_full = 1.0
for lag in range(1, 101):
    rho = np.mean(d[:-lag]*d[lag:])/(s*s)
    cum_full += 2*rho
print(f"\n  1 + 2Σ_{'{j=1..100}'}ρ = {cum_full:.4f}（→ 0 表示方差完全压缩）")

# 分块看方差压缩
print("\n分块 Σδ 的方差 vs 独立预测：")
block = 10000
nblocks = K//block
block_sums = []
for i in range(nblocks):
    block_sums.append(np.sum(delta[i*block:(i+1)*block]))
block_sums = np.array(block_sums)
print(f"  分块和 std = {np.std(block_sums):.3f}")
print(f"  独立预测 std = {np.std(delta[:block])*np.sqrt(block):.3f}（√block·单点std）")
print(f"  压缩比 = {np.std(block_sums)/(np.std(delta[:block])*np.sqrt(block)):.3f}")

# 关键：Σδ_k 的部分和（全量）——O(loglog) 验证
Sd = np.cumsum(delta)
print(f"\n  max|Σδ| = {np.max(np.abs(Sd)):.3f}（理论 O(loglog T)~{np.log(np.log(z[-1])):.2f}）")
