#!/usr/bin/env python3
"""验证 r(n) 的完整分解——确认唯一缺口 = S(γ_max)（端点）
r(n) = 2(N₀+S) − 2Σcos − 主项
     = [2N₀ − 2∫cos·N₀' − 主项]（无条件） + 2S(γ_max) + O(1)（∫S·dcos）
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
K = len(z)
T = z[-1]

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8
def N0p(t):
    return np.log(t/(2*pi))/(2*pi)
def th1(t):
    return np.arctan(1/(2*t))

# 参数（c = ½(γ_E−1−log2π)）
gamma_E = 0.5772156649015329
c = 0.5*(gamma_E - 1 - log(2*pi))

# r(n) 直接（sin² 公式）
print("r(n) 分解验证（n=100, 500——各部分量级）：")
for n in [100, 500]:
    # 1. λ_n（采样）
    fn = 4*np.sin(n*th1(z))**2
    lam = np.sum(fn)
    # 2. 主项
    main = 0.5*n*log(n) + c*n
    # 3. r(n) 直接
    r_direct = lam - main
    # 4. 分解：λ_n = 2K − 2Σcos（f_n = 2−2cos）
    cos_sum = np.sum(np.cos(2*n*th1(z)))
    lam_check = 2*K - 2*cos_sum
    # 5. N₀ 和 S
    N0_T = N0(T)
    S_T = K - N0_T
    # 6. 主项抵消部分：2N₀ − 2∫cos·N₀' − 主项
    from scipy.integrate import quad
    int_cos, _ = quad(lambda t: np.cos(2*n*np.arctan(1/(2*t)))*N0p(t), z[0], T, limit=2000)
    main_comp = 2*N0_T - 2*int_cos - main
    print(f"\n  n={n}:")
    print(f"    r(n) 直接 = {r_direct:+.4f}")
    print(f"    λ_n = 2K−2Σcos = {lam_check:.4f}（直接 {lam:.4f}——差 {abs(lam_check-lam):.4f}）")
    print(f"    K = {K}  N₀(T) = {N0_T:.4f}  S(T) = {S_T:+.4f}")
    print(f"    主项抵消 [2N₀−2∫cos−主项] = {main_comp:+.4f}（应 O(1）——无条件）")
    print(f"    2S(T) = {2*S_T:+.4f}（端点——缺口）")
    print(f"    预测 r ≈ 主项抵消 + 2S(T) = {main_comp + 2*S_T:+.4f}（vs 直接 {r_direct:+.4f}）")

del z
gc.collect()
print("内存已释放")
