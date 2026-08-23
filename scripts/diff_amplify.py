#!/usr/bin/env python3
"""差分放大（高通滤波）——放大 r(n) 的高频差额
r(n) 的抵消 ~1e3 量级（相对 1e-3）——差分（Δr, Δ²r）去掉低频背景（γ₁ 主导）
高频分量——差额的振荡——频谱分析——找结构（素数频率？）
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

z = load_zeros(300000)

def th1(t):
    return np.arctan(1/(2*t))

def lam_n(n, z):
    return 4*np.sum(np.sin(n*th1(z))**2)

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

gamma_E = 0.5772156649015329
c = 0.5*(gamma_E - 1 - log(2*pi))

def r_n(n, z):
    return lam_n(n, z) - (0.5*n*log(n) + c*n)

# r(n) 序列 + 差分
ns = np.arange(50, 800)
rs = np.array([r_n(n, z) for n in ns])
d1 = np.diff(rs)
d2 = np.diff(d1)
d3 = np.diff(d2)

print(f"r(n)（n∈[50,800]——{len(rs)} 个）：std = {np.std(rs):.4f}")
print(f"Δr：std = {np.std(d1):.4f}  max = {np.max(np.abs(d1)):.4f}")
print(f"Δ²r：std = {np.std(d2):.4f}  max = {np.max(np.abs(d2)):.4f}")
print(f"Δ³r：std = {np.std(d3):.4f}  max = {np.max(np.abs(d3)):.4f}")

# 差分后的频谱（找高频结构）
def spectrum(x):
    xd = x - np.mean(x)
    spec = np.abs(np.fft.rfft(xd))**2
    freqs = np.fft.rfftfreq(len(xd), d=1.0)
    return freqs, spec

print("\nΔ²r 的频谱（放大后的差额——找峰）：")
freqs, spec = spectrum(d2)
peaks = []
for i in range(1, len(spec)-1):
    if spec[i] > spec[i-1] and spec[i] > spec[i+1] and spec[i] > np.mean(spec)*2:
        peaks.append((freqs[i], spec[i]))
peaks.sort(key=lambda x: -x[1])
print(f"  max/mean = {np.max(spec)/np.mean(spec):.1f}")
for f, s in peaks[:8]:
    print(f"    频率 f={f:.4f}（周期 {1/f:.1f} n）: 能量 {s:.2f}")

# 关键：差分后的"拍"结构——与 θ₁(γ₁) 的关系
th1_g1 = np.arctan(1/(2*14.135))
freq_g1 = th1_g1/pi
print(f"\nγ₁ 的 n 频率：θ₁(γ₁)/π = {freq_g1:.4f}（周期 {1/freq_g1:.1f} n）")
print(f"θ₁(γ₁) = {th1_g1:.6f}——2θ₁/π = {2*th1_g1/pi:.4f}（cos(2nθ₁) 频率）")

del z
gc.collect()
print("内存已释放")
