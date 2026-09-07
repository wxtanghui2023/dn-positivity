#!/usr/bin/env python3
"""
§7 C3 审计——concentration operator 谱的 β-可见性
C_{T,W} = P_T P̂_W P_T——Landau-Pollak——谱 μ_n(TW)
问题：μ_n 是否依赖任何"零点位置"（β——）或纯 TW？

已知：Slepian——μ_n ~ 1（n ≤ 2TW）然后指数 drop——纯 TW 函数
数值确认：μ_n(TW) 对"假设离轴零点"的响应 = 0（β-盲——）？
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
import mpmath as mp

def prolate_spectrum(c, N=100):
    """Landau-Pollak 谱——μ_n(c)——c = πTW（带宽——）
    用 prolate 微分方程的三对角近似或直接 SVD——
    简化：P_T P̂_W P_T 的数值——离散——"""
    # 离散化：区间 [-1,1]（时间——）频率限制 W——用傅里叶基
    # 简化：直接用已知 prolate 谱的数值近似（特征值 μ_n ~ 1/sqrt(1+e^{π(c-n/2)...}) 类）
    # 更直接：离散 prolate 矩阵
    M = N
    x = np.linspace(-1, 1, M)
    dx = x[1]-x[0]
    # P_T = 时间限制（已在 [-1,1]——恒等——）——需要频率限制
    # P̂_W = 乘性（频域——）——等价于卷积（sinc 核——）
    # 简化 Landau-Pollak：特征方程 ∫_{-1}^{1} sin(W(t-s))/(π(t-s)) φ(s) ds = μ φ(t)
    W = c / np.pi  # 使 c = πW——带宽
    K = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            d = W*(x[i]-x[j])
            if abs(d) < 1e-12:
                K[i, j] = W/np.pi
            else:
                K[i, j] = np.sin(d)/(np.pi*(x[i]-x[j]))
    K = K * dx  # 数值积分权重
    ev = np.linalg.eigvalsh(K)[::-1]
    return ev

def main():
    print("="*70)
    print("§7 C3 审计——concentration 谱的 β-可见性")
    print("="*70)
    
    # 1. Slepian 谱——不同 c（=πTW——）
    print("\n1. Landau-Pollak 谱 μ_n(c)（纯 TW 函数——）:")
    for c in [5.0, 10.0, 15.0]:
        ev = prolate_spectrum(c, 80)
        # 前几个
        n_above = sum(1 for e in ev if e > 0.5)
        print(f"  c={c}: μ₀={ev[0]:.4f}——μ₁={ev[1]:.4f}——μ₂={ev[2]:.4f}——μ>0.5 个数: {n_above}")
    
    # 2. β-敏感性：谱是否依赖任何"零点参数"？
    print("\n2. β-敏感性检查:")
    print("   Landau-Pollak 谱完全由 c = πTW 决定——无素数/零点参数——")
    print("   μ_n(c) 对'离轴零点'的响应 = 0（谱不含 δ——）")
    print("   → 普通 concentration 谱 β-盲——")
    
    # 3. 关键：semilocal 版（P^S——module 含素数——）是否改变？
    print("\n3. semilocal 版（P^S_T——module 含素数 S——）:")
    print("   公式 (22)：P^S_T, P̂^S_W 用 module 定义——含素数结构——")
    print("   但——素数 S 与零点位置 β 的关系——需显式公式（循环——）——")
    print("   module 的素数参数 ≠ 零点参数——除非经 Weil 求和——")
    
    # 4. 结论
    print("\n4. C3 初步结论:")
    print("   ① 普通 Slepian 谱：纯 TW——β-盲（无 δ——）")
    print("   ② semilocal 版：素数在 module——但到 β 需显式公式（循环——）")
    print("   ③ concentration 谱没有'天然的零点参数'——δ 不可见（除非插入——）")

if __name__ == "__main__":
    main()
