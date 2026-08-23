#!/usr/bin/env python3
"""最后探测：r(n) 的频谱（n 域 FFT——差额的频率指纹）
r(n) = O(1）的振荡——频谱结构？
如果频谱有峰（素数 log p 或其他频率）——相位均匀性的频率指纹
如果平坦（白噪声）——r(n) 的 O(1）是"随机"的（无隐藏周期）
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

z = load_zeros(500000)

def th1(t):
    return np.arctan(1/(2*t))

def lam_n(n, z):
    return 4*np.sum(np.sin(n*th1(z))**2)

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

gamma_E = 0.5772156649015329
c = 0.5*(gamma_E - 1 - log(2*pi))

# r(n) 序列（n = 50 到 1000）
ns = np.arange(50, 1000)
rs = np.array([lam_n(n, z) - (0.5*n*log(n) + c*n) for n in ns])
print(f"r(n) 序列：n ∈ [50, 1000]——{len(rs)} 个值")
print(f"  r(n) 统计：mean = {np.mean(rs):+.4f}  std = {np.std(rs):.4f}  max|·| = {np.max(np.abs(rs)):.4f}")

# 频谱（n 域 FFT）
r_d = rs - np.mean(rs)
Nf = len(r_d)
spec = np.abs(np.fft.rfft(r_d))**2
freqs = np.fft.rfftfreq(Nf, d=1.0)  # 频率（每 n 单位）

# 找峰
print("\nr(n) 的频谱（n 域——频率 = 每 n 的振荡）：")
print(f"  总能量 = {np.sum(spec):.2f}")
# 峰值（排除直流）
peaks = []
for i in range(1, len(spec)-1):
    if spec[i] > spec[i-1] and spec[i] > spec[i+1] and spec[i] > np.mean(spec)*3:
        peaks.append((freqs[i], spec[i]))
peaks.sort(key=lambda x: -x[1])
print(f"  显著峰（>3×平均）：")
for f, s in peaks[:10]:
    print(f"    频率 f={f:.4f}（周期 1/f={1/f if f>0 else float('inf'):.1f} n）: 能量 = {s:.2f}")

# 关键：与素数频率对比
print(f"\n素数频率（n 域的什么频率？——如果 r(n) 有 sin(α·n) 结构——α = θ₁(γ) 的分布）：")
print(f"  平均频率 = {np.mean(freqs):.4f}")

# 白噪声检验（频谱平坦？）
print(f"\n频谱形状：max/mean = {np.max(spec)/np.mean(spec):.2f}（1 = 白噪声——>1 = 有结构）")

del z
gc.collect()
print("内存已释放")
