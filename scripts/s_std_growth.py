#!/usr/bin/env python3
"""验证 S(t) 数值行为（修复版——逐点 float64）vs Selberg 二阶矩"""
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

# S(γ_k⁺) = k − N₀(γ_k)——float64 逐点
S_k = np.array([(k+1) - N0(z[k]) for k in range(K)], dtype=np.float64)
print(f"S(γ_k⁺): min={np.min(S_k):+.4f} max={np.max(S_k):+.4f} std={np.std(S_k):.4f}")

print("\n分块 std（每 200k 零点——S 无界证据）：")
for i in range(0, K, 200000):
    seg = S_k[i:i+200000]
    print(f"  k={i+1:7d}-{min(i+200000,K):7d}: std={np.std(seg):.4f}  max|S|={np.max(np.abs(seg)):.3f}")

# 分块 max|S| 的增长——用更大的块（每 500k）看趋势
print("\n更大块（每 500k）：")
for i in range(0, K, 500000):
    seg = S_k[i:i+500000]
    print(f"  k={i+1:7d}-{min(i+500000,K):7d}: std={np.std(seg):.4f}  max|S|={np.max(np.abs(seg)):.3f}")
