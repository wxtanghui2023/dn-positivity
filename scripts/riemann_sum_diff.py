#!/usr/bin/env python3
"""正确的黎曼和差验证：r(n) 振荡 = Σ_k f_n(γ_k) − ∫_2^∞ f_n(t)N₀'(t)dt
f_n(t) = 4sin²(nθ₁(t))，θ₁(t) = arctan(1/2t)（8/22 的权威定义——rn-o1-final-summary）

对比 8/23 的 f̃ 核：f̃ = cos(2nθ₁) − cos((2n+2)θ₁) = 2sin((2n+1)θ₁)sin(θ₁)
f_n = 4sin²(nθ₁) = 2 − 2cos(2nθ₁)

关系：∫f_n dS = 2∫dS − 2∫cos(2nθ₁)dS——∫dS = S(T)−S(2) 无界——需主项抵消
r(n)（振荡）= Σ f_n(γ_k) − ∫ f_n N₀' dt（黎曼和差）
"""
import numpy as np
from scipy import integrate

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def N0(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) + 7/8

def N0p(t):
    return np.log(t/(2*np.pi))/(2*np.pi)

def th1(t):
    return np.arctan(1/(2*t))

def fn(t, n):
    return 4*np.sin(n*th1(t))**2

K = 2000000
z = load_zeros(K)
Tmax = z[-1]

print(f"K={K}, γ_max={Tmax:.1f}")
print(f"\n{'n':>6} {'Σf_n(γ_k)':>14} {'∫f_n N₀'':>14} {'黎曼和差':>14} {'r(n)参考':>10}")
# r(n) 参考值（8/22 已知：n=50: 2.25, n=100: 1.38, n=200: 2.89, n=500: -0.07, n=1000: 2.51/-0.13）
ref = {50: 2.25, 100: 1.38, 200: 2.89, 500: -0.07, 1000: 2.51}
for n in [50, 100, 200, 500, 1000]:
    fv = fn(z, n)
    Sf = np.sum(fv)  # Σ f_n(γ_k)——到 γ_max
    # ∫_2^Tmax f_n(t)N₀'(t)dt——数值积分（f_n 振荡——用高精度）
    def integrand(t):
        return fn(t, n)*N0p(t)
    # 分段积分：每个零点区间 [γ_k, γ_{k+1}]——f_n 缓变时可近似，但 n 大时振荡
    # 用 quad 对每区间太慢——用 8 点 Gauss 或直接向量化
    # 简化：∫_2^Tmax = Σ_k ∫_{γ_k}^{γ_{k+1}}——用 Simpson/高精度每区间
    # 但 2M 区间太慢——用大步长 + f_n 的解析近似
    # 直接：∫f_n N₀' ≈ Σ_k f_n(mid_k)·N₀'(mid_k)·Δγ_k（中点黎曼——f_n 振荡时误差）
    # 更精确：对每区间用 4 点 Gauss
    from numpy.polynomial.legendre import leggauss
    xg, wg = leggauss(4)
    total = 0.0
    for k in range(K-1):
        a, b = z[k], z[k+1]
        mid = 0.5*(b-a)
        ts = mid*xg + 0.5*(a+b)
        total += 0.5*(b-a)*np.sum(wg*fn(ts, n)*N0p(ts))
    # 尾部 [γ_max, ∞)——f_n ~ n²/t² 衰减——∫_γmax^∞ ≈ n²·∫dt/t²·log t/2π
    # f_n(t) ≈ 4·(n/(2t))² = n²/t²（t 大）
    # ∫_T∞ n²/t²·log(t/2π)/2π dt = n²/(2π)·[log(T/2π)/T + 1/T]（分部积分）
    tail = n**2/(2*np.pi)*(np.log(Tmax/(2*np.pi))/Tmax + 1/Tmax)
    Int = total + tail
    diff = Sf - Int
    r_ref = ref.get(n, float('nan'))
    print(f"{n:6d} {Sf:+14.4f} {Int:+14.4f} {diff:+14.4f} {r_ref:10.2f}")
