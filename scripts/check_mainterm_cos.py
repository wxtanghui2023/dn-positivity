#!/usr/bin/env python3
"""验证：Σcos(γ_k·log p) 的线性增长是否纯主项效应（N₀ 反演——无条件）
用主项 N₀(t) = (t/2π)log(t/2π) - t/2π + 7/8 反演得到近似零点 γ_k^N₀
比较：主项模型的 Σcos vs 真实零点的 Σcos
"""
import numpy as np
from scipy.optimize import brentq

def N0(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) + 7/8

def gamma_main(k):
    """反演 N₀(t) = k - 1/2（Gram 点近似）"""
    lo, hi = 5.0, 2000000.0
    # 粗略估计
    t = k * 2*np.pi / max(np.log(k+10), 1)
    return t

# 用更精确的反演（牛顿迭代一次就够——N₀ 单调）
def inv_N0(y):
    t = y * 2*np.pi / max(np.log(y+10), 1)
    for _ in range(3):
        t = t - (N0(t) - y) / (np.log(t/(2*np.pi))/(2*np.pi))
    return t

K = 2000000
# 主项模型零点（Gram 点——N₀(t) = k - 1/2）
k_arr = np.arange(1, K+1, dtype=float)
print("computing main-term zeros...", flush=True)
g_main = np.array([inv_N0(k - 0.5) for k in k_arr])  # 2M 个可能太慢——抽样

# 抽样验证（每 100 个）
idx = np.arange(0, K, 100, dtype=int)
g_samp = np.array([inv_N0(k - 0.5) for k in idx+1])
print(f"sampled {len(g_samp)} main-term zeros, γ_1^main={g_samp[0]:.3f}, γ_K^main={g_samp[-1]:.3f}")

# 加载真实零点（抽样对齐）
path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())
z_samp = z[idx]

for x, lab in [(np.log(2), 'log2'), (np.log(3), 'log3'), (1.0, '1.0')]:
    Sc_main = np.cumsum(np.cos(g_samp * x))
    Ss_main = np.cumsum(np.sin(g_samp * x))
    Sc_real = np.cumsum(np.cos(z_samp * x))
    Ss_real = np.cumsum(np.sin(z_samp * x))
    n = len(idx)
    print(f"\n{x:.4f} ({lab}):")
    print(f"  主项模型: Σcos={Sc_main[-1]:+.1f} (={Sc_main[-1]/n:.4f}·n)  Σsin={Ss_main[-1]:+.3f}  max|Σsin|={np.max(np.abs(Ss_main)):.3f}")
    print(f"  真实零点: Σcos={Sc_real[-1]:+.1f} (={Sc_real[-1]/n:.4f}·n)  Σsin={Ss_real[-1]:+.3f}  max|Σsin|={np.max(np.abs(Ss_real)):.3f}")
