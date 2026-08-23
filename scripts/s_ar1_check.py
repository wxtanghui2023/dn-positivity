#!/usr/bin/env python3
"""探索 S 的近 AR(1)：γ(2) ≈ 0（一步记忆）——未充分利用的结构
如果 γ(2) ≈ 0 稳定——S 的记忆只有一步——所有相关性由 ρ₁ 决定
—— p = 0.618（arcsin）的完整推导路径
验证：γ(2) 的稳定性 + 高阶 γ(j) 的衰减 + AR(1) 预测 vs 实际
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

z = load_zeros(1000000)

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

S_k = np.array([(k+1) - N0(z[k]) for k in range(1000000)], dtype=float)
del z
gc.collect()

s = S_k - np.mean(S_k)
g0 = np.var(s)

# γ(j) 的衰减——AR(1) 预测 vs 实际
print("S 的自协方差 γ(j)——AR(1) 预测 vs 实际：")
print(f"{'j':>3} {'γ(j) 实际':>12} {'AR(1): φ^j·γ(0)':>14} {'比值':>8}")
phi = 0.232  # 之前测的 φ
for j in [1, 2, 3, 4, 5, 10, 20]:
    gj = np.mean(s[:-j]*s[j:])
    ar1 = phi**j * g0
    print(f"{j:3d} {gj:12.6f} {ar1:14.6f} {gj/ar1 if ar1!=0 else 0:8.3f}")

# γ(j) 随高度的稳定性（分块）
print("\nγ(2)/γ(0) 随高度（一步记忆的稳定性）：")
for b in range(5):
    lo = b*200000
    hi = (b+1)*200000
    sb = s[lo:hi]
    g0b = np.var(sb)
    g1b = np.mean(sb[:-1]*sb[1:])
    g2b = np.mean(sb[:-2]*sb[2:])
    print(f"  块{b+1}: φ = {g1b/g0b:.4f}  γ(2)/γ(0) = {g2b/g0b:+.5f}")

# 关键：γ(2) ≈ 0 的含义——S 的"一步记忆"——但 φ ≠ 0
# 如果 γ(2) = 0 精确——S_{k+2} 与 S_k 无关（给定 S_{k+1}）
print("\n一步记忆检验：E[S_{k+2}|S_{k+1}, S_k] 是否只依赖 S_{k+1}？")
# 部分相关：corr(S_{k+2}, S_k | S_{k+1})
# 用回归：S_{k+2} = a·S_{k+1} + b·S_k + ε——如果 b ≈ 0——一步记忆
from numpy.linalg import lstsq
X = np.vstack([s[1:-1], s[:-2]]).T
y = s[2:]
coef, _, _, _ = lstsq(X, y, rcond=None)
print(f"  S_{'{k+2}'} = {coef[0]:.4f}·S_{'{k+1}'} + {coef[1]:.4f}·S_k + ε")
print(f"  （b ≈ 0 = 一步记忆——AR(1)——b ≠ 0 = 二阶记忆）")

# 高阶：AR(2) 的系数 vs AR(1)
print(f"\n  φ₁（AR1）= {np.mean(s[:-1]*s[1:])/g0:.4f}")
print(f"  AR(2): φ₁ = {coef[0]:.4f}（应 ≈ φ₁ AR1）φ₂ = {coef[1]:.4f}（应 ≈ 0）")

del S_k, s
gc.collect()
print("内存已释放")
