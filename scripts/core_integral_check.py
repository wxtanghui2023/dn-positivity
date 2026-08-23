#!/usr/bin/env python3
"""验证核心积分：∫sin(t log p)·w'(t)dt——van der Corput 界
w'(t) = 4n·sin(2nθ₁)·θ₁'——θ₁' = −2/(4t²+1)——振荡 + 衰减
关键：这个积分是否 O(1/log p) 或更小——决定 Σ_p 收敛
"""
import numpy as np
import math
from math import log, pi
from scipy.integrate import quad

def wp(t, n):
    th = np.arctan(1/(2*t))
    thp = -2.0/(4*t*t+1)
    return 4*n*np.sin(2*n*th)*thp

# ∫sin(t log p)·w'(t)dt——数值（从 γ₁ 到 1e7）
G1 = 14.134725142
for n in [100, 1000]:
    print(f"\nn={n}: ∫_γ₁^∞ sin(t log p)·w'(t)dt")
    for p in [2, 3, 5, 11, 101, 1009]:
        val, err = quad(lambda t: np.sin(t*log(p))*wp(t, n), G1, 2e6, limit=2000, epsabs=1e-8)
        # 尾部估计：|w'| ~ 2n/t²——∫_2e6^∞ ~ 2n/(2e6·log p)·(1/log p)
        print(f"  p={p:5d}: ∫ = {val:+.5f}  （1/log p = {1/log(p):.4f}——比值 {abs(val)*log(p):.3f}）")
