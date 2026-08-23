#!/usr/bin/env python3
"""验证 FSZ Lemma 1：Σ_{γ≤T} x^ρ ≈ −T·Λ(x)/(2π)（x 素数幂——主项）
预测：Σcos(γ_k log p) ≈ −T·log p/(2π√p)（线性系数）
对比我们数值发现的 c_p（Σcos ~ c_p·K）
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
T = z[-1]  # γ_max ~ 1131944

print(f"K = {K}, T = γ_max = {T:.1f}")
print(f"\nFSZ Lemma 1 预测 vs 数值（Σcos(γ log p) 的线性系数）：")
print(f"{'p':>4} {'预测 −T·logp/(2π√p)':>20} {'数值 Σcos':>12} {'预测/数值':>10}")

for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
    pred = -T*math.log(p)/(2*math.pi*math.sqrt(p))
    Sc = np.sum(np.cos(z*math.log(p)))
    print(f"{p:4d} {pred:20.0f} {Sc:12.0f} {pred/Sc:10.4f}")

# 更精确：主项 = −T·Λ(x)/(2π)·x^{−1/2}——考虑 (3.8) 的修正
print(f"\n精确匹配检查（p=2）：")
pred2 = -T*math.log(2)/(2*math.pi*math.sqrt(2))
num2 = np.sum(np.cos(z*math.log(2)))
print(f"  预测 = {pred2:+.1f}")
print(f"  数值 = {num2:+.1f}")
print(f"  差 = {pred2-num2:+.1f}（应 ~ O(T·log²p/log T)~{T*math.log(2)**2/math.log(T):.0f} 以内）")
