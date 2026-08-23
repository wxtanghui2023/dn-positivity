#!/usr/bin/env python3
"""诊断：γ_k·x mod 2π 的分布——为什么 Σ cos(γx) 线性增长而 Σ sin(γx) 有界？
关键猜想：γ_k x mod 2π 的相位不是均匀的——慢进动/聚集/共振结构
"""
import numpy as np

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(2000000)

for x, lab in [(np.log(2), 'log2'), (np.log(3), 'log3'), (np.log(5), 'log5'), (1.0, '1.0'), (2.0, '2.0')]:
    ph = (z * x) % (2*np.pi)  # 相位 mod 2π
    # 分布统计
    bins = np.histogram(ph, bins=12, range=(0, 2*np.pi))[0]
    print(f"\n{x:.4f} ({lab}): 相位直方图 (12 bins, 0~2π):")
    print("  " + " ".join(f"{b:6d}" for b in bins))
    print(f"  mean(cos): {np.mean(np.cos(ph)):+.4f}  mean(sin): {np.mean(np.sin(ph)):+.4f}")
    # 相位增量分析（相邻）
    dph = np.diff(ph)
    dph_wrapped = (dph + np.pi) % (2*np.pi) - np.pi  # 到 (-π, π]
    print(f"  相邻相位增量: mean={np.mean(dph_wrapped):+.5f} std={np.std(dph_wrapped):.5f} |中位数|={np.median(np.abs(dph_wrapped)):.5f}")
    # 累积和检查：S_cos, S_sin 的最后值
    Sc = np.cumsum(np.cos(ph)); Ss = np.cumsum(np.sin(ph))
    print(f"  Σcos(K)={Sc[-1]:+.1f}  Σsin(K)={Ss[-1]:+.3f}  max|Σcos|={np.max(np.abs(Sc)):.1f}  max|Σsin|={np.max(np.abs(Ss)):.3f}")
    # 检查相位是否集中在特定值
    print(f"  相位 <0.1 rad 占比: {np.mean(ph < 0.1)*100:.2f}%  相位 >6.1 rad 占比: {np.mean(ph > 6.1)*100:.2f}%")
