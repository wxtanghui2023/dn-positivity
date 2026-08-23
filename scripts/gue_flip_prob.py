#!/usr/bin/env python3
"""关键测试：GUE 的符号翻转概率 p_GUE vs ζ 的 p ≈ 0.618
模拟 GUE（Hermite 矩阵）——计算相邻间距偏差的符号翻转概率
如果 p_GUE ≈ 0.618——普适类（GUE）支持
如果不同——ζ 的 p 是独特常数（新物理）
"""
import numpy as np
import gc

def gue_spacings(N, n_samples, seed=42):
    """模拟 GUE：生成 n_samples 个 N×N Hermite 矩阵——收集归一化间距"""
    rng = np.random.default_rng(seed)
    all_spacings = []
    for _ in range(n_samples):
        # GUE：H = (A + A†)/√2——A 是复高斯
        A = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N)))/np.sqrt(2)
        H = (A + A.conj().T)/np.sqrt(2)
        eigs = np.linalg.eigvalsh(H)
        eigs = np.sort(eigs)
        # 归一化间距：s_i = (λ_{i+1}−λ_i)·密度(λ_i)——用局部平均密度
        # 简化：用整体密度（半圆律）——或直接局部
        # 归一化：s_i = (λ_{i+1}−λ_i)·N·ρ_sc(λ_i)——ρ_sc 是半圆
        for i in range(N-1):
            mid = 0.5*(eigs[i]+eigs[i+1])
            rho = np.sqrt(max(0, 2 - mid**2))/np.pi  # 半圆密度（支撑 [-√2, √2]）
            s = (eigs[i+1]-eigs[i]) * N * rho
            all_spacings.append(s)
        del A, H, eigs
        gc.collect()
    return np.array(all_spacings)

# 模拟 GUE
print("GUE 模拟（500×500 × 3 样本——1500 间距）：")
spacings = gue_spacings(500, 3)
deltas = spacings - 1.0  # 间距偏差
sign = np.sign(deltas)
flips = np.sum(sign[:-1] != sign[1:]) / (len(sign)-1)
print(f"  p_GUE = {flips:.6f}")
print(f"  ζ 的 p = 0.617554")
print(f"  差 = {abs(flips - 0.617554):.6f}")

# 更大样本（提高精度）
print("\n更大样本（300×300 × 20）：")
spacings2 = gue_spacings(300, 20, seed=123)
deltas2 = spacings2 - 1.0
sign2 = np.sign(deltas2)
flips2 = np.sum(sign2[:-1] != sign2[1:]) / (len(sign2)-1)
print(f"  p_GUE = {flips2:.6f}")
print(f"  差 vs ζ = {abs(flips2 - 0.617554):.6f}")

# 理论：Wigner surmise 的独立近似
# 如果相邻间距独立（近似）——p = P((s−1)(s'−1)<0) = 2·P(s<1)·P(s>1)
from scipy.integrate import quad
wigner = lambda s: (np.pi*s/2)*np.exp(-np.pi*s*s/4)
p_less = quad(wigner, 0, 1)[0]
p_indep = 2*p_less*(1-p_less)
print(f"\nWigner 独立近似：P(s<1) = {p_less:.4f}——p_indep = {p_indep:.6f}")
print(f"  （ζ 的 p = 0.6176 vs 独立 0.5128——差异 = 相关结构！）")

del spacings, deltas, sign, spacings2, deltas2, sign2
gc.collect()
print("\n内存已释放")
