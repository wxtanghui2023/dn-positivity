#!/usr/bin/env python3
"""全量主项模型 vs 真实零点——干净分解 Σcos/Σsin 的主项贡献与 S 部分贡献
主项零点 γ_k^main 由 N₀(t) = k - 1/2 反演（Gram 点）
关键问题：Σcos(γ_k·log p) 的线性增长来自主项还是 S？
"""
import numpy as np

def N0(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) + 7/8

def inv_N0_vec(y):
    """向量化反演 N₀(t) = y（3 次牛顿迭代）"""
    t = y * 2*np.pi / np.log(y + 10)
    for _ in range(4):
        t = t - (N0(t) - y) / (np.log(t/(2*np.pi))/(2*np.pi))
    return t

K = 2000000
k_arr = np.arange(1, K+1, dtype=float)
print("computing 2M main-term zeros (vectorized)...", flush=True)
g_main = inv_N0_vec(k_arr - 0.5)
print(f"done. γ_1^main={g_main[0]:.3f} γ_2M^main={g_main[-1]:.3f}")

# 真实零点
path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())
print(f"real zeros: γ_1={z[0]:.3f} γ_2M={z[-1]:.3f}")
print(f"偏差: mean(γ_main-γ_real)={np.mean(g_main-z):.4f}, max={np.max(np.abs(g_main-z)):.4f}")

for x, lab in [(np.log(2), 'log2'), (np.log(3), 'log3'), (np.log(5), 'log5'), (np.log(7), 'log7'), (1.0, '1.0'), (2.0, '2.0')]:
    cm = np.cumsum(np.cos(g_main*x)); sm = np.cumsum(np.sin(g_main*x))
    cr = np.cumsum(np.cos(z*x)); sr = np.cumsum(np.sin(z*x))
    # S 部分 = 真实 - 主项
    cs = cr - cm; ss = sr - sm
    print(f"\n{x:.4f} ({lab}):")
    print(f"  主项模型: Σcos={cm[-1]:+.1f} ({cm[-1]/K:+.5f}K)  Σsin={sm[-1]:+.3f}  max|Σsin|={np.max(np.abs(sm)):.3f}")
    print(f"  真实零点: Σcos={cr[-1]:+.1f} ({cr[-1]/K:+.5f}K)  Σsin={sr[-1]:+.3f}  max|Σsin|={np.max(np.abs(sr)):.3f}")
    print(f"  S部分  : Σcos={cs[-1]:+.1f} ({cs[-1]/K:+.5f}K)  Σsin={ss[-1]:+.3f}  max|Σsin|={np.max(np.abs(ss)):.3f}")
