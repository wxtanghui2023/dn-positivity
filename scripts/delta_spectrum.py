#!/usr/bin/env python3
"""δ 的功率谱分析——低频压制（信号处理视角）
如果 δ 的谱在低频被压制（S_δ(0) ≈ 0）——Σδ = O(1) 的谱解释
f_n 核（频率 ~ n/γ²）的加权和 O(1) 需要谱在相关频率小
"""
import numpy as np
import math
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)

dg = np.diff(z)
Np = np.log(z[:-1]/(2*pi))/(2*pi)
delta = dg - 1.0/Np
d = delta - np.mean(delta)

# 功率谱（FFT——均匀采样近似——δ 序列）
N = len(d)
# 用 Welch 方法（分段平均——降噪）
from numpy.fft import fft, fftfreq

# 直接 FFT（全长）
spec = np.abs(fft(d))**2 / N
freqs = fftfreq(N)
# 低频部分（前 1%）
print("δ 的功率谱（低频行为——对数）：")
print(f"{'频率':>12} {'功率谱':>12}")
for i in [1, 2, 5, 10, 50, 100, 500, 1000, 5000]:
    if i < N//2:
        print(f"{freqs[i]:12.6f} {spec[i]:12.6e}")

# 累积谱（低频压制检查）
cum_spec = np.cumsum(spec[1:N//2])
total_spec = np.sum(spec[1:N//2])
print(f"\n低频功率占比：")
for frac in [0.001, 0.005, 0.01, 0.05]:
    idx = int(frac*N//2)
    print(f"  前 {frac*100:.1f}% 频率：{cum_spec[idx-1]/total_spec*100:.2f}% 功率")

# 对比：白噪声（谱应平坦）
rng = np.random.default_rng(42)
white = rng.standard_normal(N)
spec_w = np.abs(fft(white))**2 / N
cum_w = np.cumsum(spec_w[1:N//2])
tot_w = np.sum(spec_w[1:N//2])
print(f"白噪声对照：")
for frac in [0.001, 0.005, 0.01, 0.05]:
    idx = int(frac*N//2)
    print(f"  前 {frac*100:.1f}% 频率：{cum_w[idx-1]/tot_w*100:.2f}% 功率")
