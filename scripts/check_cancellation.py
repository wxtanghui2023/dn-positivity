#!/usr/bin/env python3
"""验证 Σ e^{iγ_k log p} = O(1) 的抵消机制
Stieltjes 分部积分：Σ_{k≤K} e^{iγ_k x} = ∫ e^{itx} dN(t)
N(t) = (t/2π)log(t/2π) - t/2π + 7/8 + S(t) + O(1/t)

关键检验：主项 M(t) = (t/2π)log(t/2π) - t/2π 的贡献是否精确抵消？
Σ_M = e^{iTx}M(T) - ∫_2^T M(t)·ix·e^{itx} dt
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
T = z[-1]
print(f"K={len(z)}, γ_K = {T:.3f}")

def N_exact(t):
    """Riemann-von Mangoldt: N(t) = (1/π)arg ξ(½+it) 的主项"""
    return (t/(2*np.pi))*(np.log(t/(2*np.pi))) - t/(2*np.pi) + 7/8

def M_contrib(x):
    """主项贡献: e^{iTx}M(T) - ∫_2^T M(t)·ix·e^{itx} dt（解析计算）"""
    # ∫_2^T (t/2π)log(t/2π)·ix·e^{itx} dt 解析
    # 用数值积分验证抵消
    from scipy import integrate
    def integrand(t):
        return N_exact(t) * 1j * x * np.exp(1j*t*x)
    # 用高精度 quad（需要复数——拆实虚）
    re = integrate.quad(lambda t: N_exact(t)*x*np.sin(t*x)*(-1), 2, T, limit=500)[0]  # Re(-ix N e^{itx}) 仔细推导
    im = integrate.quad(lambda t: N_exact(t)*x*np.cos(t*x), 2, T, limit=500)[0]
    # -∫ M·ix·e^{itx} = -∫ M·ix·(cos+isin) = -∫ M·(ix cos - x sin) = ∫ M·x·sin - i∫M·x·cos
    val = np.exp(1j*T*x)*N_exact(T) - (re + 1j*im)
    return val

for x in [np.log(2), np.log(3), np.log(5), 1.0, 2.0]:
    val = M_contrib(x)
    print(f"x={x:.4f}: 主项贡献 = {val.real:+.4f} {val.imag:+.4f}i  |ρ|={abs(val):.4f}")
