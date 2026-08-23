#!/usr/bin/env python3
"""验证 Fujii discrepancy 界 vs 我们的数值——相位均匀性的差距量化
Fujii: D_{N(T)}(uγ_n) = O(loglog T/log T)——uγ_n 模 1 的 discrepancy（无条件）
我们的数值：Σsin(γ_k log p) = O(1)——这比均匀分布（o(N)）强得多
对比：均匀分布预测 vs 实际
"""
import numpy as np
import math

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(2000000)
K = len(z)
T = z[-1]

# 检查 (u·γ_n) 模 1 的 discrepancy——u = log 2/(2π)（使 γ·u 的频率合理）
# 实际我们的对象：γ_k·log p 模 2π——等价于 (γ_k·log p/(2π)) 模 1
for p in [2, 3, 5]:
    u = math.log(p)/(2*math.pi)
    ph = (z*u) % 1.0
    # discrepancy：10 个区间
    bins = 10
    hist = np.histogram(ph, bins=bins, range=(0,1))[0]
    D = np.max(np.abs(hist/len(ph) - 1/bins))
    print(f"p={p}: D(uγ_n) = {D:.6f}  （Fujii 预测 O(loglog T/log T) = {math.log(math.log(T))/math.log(T):.6f}）")

# 关键：均匀分布意味着 Σe^{2πiuγ} = o(N)——但我们的 Σsin = O(1)
# 对比：|Σsin(γ log p)| vs N（均匀分布的随机游走预测 √N）
print(f"\n对比（K={K}）：")
for p in [2, 3, 5, 47]:
    Ssin = np.sum(np.sin(z*math.log(p)))
    print(f"  p={p:2d}: |Σsin(γ log p)| = {abs(Ssin):.2f}  vs √K = {math.sqrt(K):.0f}（随机游走）vs K = {K}")

# 检查：Σe^{2πiuγ} 的 Weyl 和（均匀分布的检验）
print(f"\nWeyl 和 (1/N)Σe^{{2πiuγ}}（均匀分布应 → 0）：")
for p in [2, 3, 5]:
    u = math.log(p)/(2*math.pi)
    S = np.sum(np.exp(2j*np.pi*u*z))
    print(f"  p={p}: (1/N)|Σe^{{2πiuγ}}| = {abs(S)/K:.6f}")
