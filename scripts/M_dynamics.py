#!/usr/bin/env python3
"""
M(T) 动力系统视角——S̄ 驱动的回归
M_{k+1} = M_k + S̄_k·Δγ_k——M 是 S̄ 的累积
如果 S̄ 有"回归"结构（给定过去——S̄ 的符号/大小可预测——）
——M 有界可证

问题：
1. S̄_k 的条件结构（给定 S̄_{k-1}, S̄_{k-2}——）
2. S̄ 是否由低维"相位"驱动（Gram 偏差的——）
3. M 的回归（M 大时——S̄ 倾向拉回？——）
"""
import numpy as np
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def main():
    print("="*70)
    print("M 动力系统视角")
    print("="*70)
    
    K = 100000
    z = load_zeros(K)
    mid = (z[:-1]+z[1:])/2
    dg = np.diff(z[:K])
    
    def N0_arr(t):
        return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8
    
    # S̄_k 精确
    def IntN0(t):
        if t <= 1: return 0.0
        return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
    
    kk = np.arange(1, K)
    IntN = np.array([IntN0(t) for t in z[:K]])
    Sbar = kk - (IntN[1:] - IntN[:-1])/dg
    
    M_cum = np.cumsum(Sbar*dg)
    
    # 1. M 的"回归"测试：|M| 大时——下一个增量倾向拉回？
    print("\n1. M 的均值回归:")
    # 分 |M| 层——看下一增量 E[S̄·Δγ | M]
    M_prev = M_cum[:-1]
    M_inc = Sbar[1:]*dg[1:]  # M_{k+1} - M_k（在 M_k 已知后——）
    for lo, hi in [(0, 0.1), (0.1, 0.2), (0.2, 0.4), (0.4, 1.0)]:
        mask = (np.abs(M_prev) >= lo) & (np.abs(M_prev) < hi)
        if mask.sum() > 100:
            E_inc = M_inc[mask].mean()
            # 拉回 = -sign(M)·E_inc
            pull = -np.sign(M_prev[mask])*M_inc[mask]
            print(f"   |M|∈[{lo},{hi}): n={mask.sum():>6}——E(inc)={E_inc:+.5f}——E(拉回)={pull.mean():+.5f}")
    
    # 2. S̄ 的条件结构（给定前一 S̄——）
    print("\n2. S̄ 的一阶条件:")
    S_prev = Sbar[:-1]
    S_next = Sbar[1:]
    for lo, hi in [(-10,-0.3), (-0.3,-0.1), (-0.1,0.1), (0.1,0.3), (0.3,10)]:
        mask = (S_prev >= lo) & (S_prev < hi)
        if mask.sum() > 100:
            print(f"   S̄_k∈[{lo},{hi}): n={mask.sum():>6}——E(S̄_next)={S_next[mask].mean():+.4f}——corr 回归")
    
    # 3. 关键：M 的"慢分量"——M 是否由低频驱动？
    print("\n3. M 轨迹的 FFT（主导频率——）:")
    seg = M_cum[:50000]
    fft = np.abs(np.fft.rfft(seg - seg.mean()))**2
    freqs = np.fft.rfftfreq(len(seg))
    top = np.argsort(fft)[-5:][::-1]
    for i in top:
        if i > 0:
            print(f"   频率 {freqs[i]:.6f}（周期 ~{1/freqs[i]:.0f} 零点——）power={fft[i]:.0f}")
    
    # 4. S̄ 与 M 的关系（M 是 S̄ 的积分——S̄ 是否有 M 的反馈？）
    print("\n4. S̄ 的波动是否随 |M| 变化（反馈——）:")
    for lo, hi in [(0, 0.1), (0.1, 0.3), (0.3, 1.0)]:
        mask = (np.abs(M_prev) >= lo) & (np.abs(M_prev) < hi)
        if mask.sum() > 100:
            print(f"   |M|∈[{lo},{hi}): S̄_next std = {Sbar[1:][mask].std():.4f}")

if __name__ == "__main__":
    main()
