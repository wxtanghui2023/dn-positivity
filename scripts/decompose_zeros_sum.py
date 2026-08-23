#!/usr/bin/env python3
"""精确分解 Σ e^{iγ_k x}：Stieltjes 分部积分 + 各项贡献
Σ_{k≤K} e^{iγ_k x} = e^{iTx}N(T) - ∫_2^T N(t)·ix·e^{itx}dt  （精确，N 阶梯）

N(t) = M(t) + 7/8 + S(t) + O(1/t), M(t) = (t/2π)log(t/2π) - t/2π

精确分解（用阶梯 N 分段积分）：
∫ N(t)ix e^{itx}dt = Σ_k k·(e^{iγ_{k+1}x} - e^{iγ_k x})   ← 精确

然后分别算：
E_M = e^{iTx}M(T) - ix∫ M(t)e^{itx}dt （M 连续——解析可算）
E_78 = e^{iTx}(7/8) - ix∫(7/8)e^{itx}dt = (7/8)e^{i2x}
E_S = e^{iTx}S(T) - ix∫ S(t)e^{itx}dt （S = N - M - 7/8——阶梯残余）
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
K = len(z)
T = z[-1]
print(f"K={K}, γ_K={T:.3f}")

def M(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi)

def analyze(x):
    # 左侧：精确零点指数和
    lhs = np.sum(np.exp(1j * z * x))
    # 右侧：e^{iTx}·K - Σ_k k·(e^{iγ_{k+1}x}-e^{iγ_k x})   （N 阶梯——N(t)=k 在 [γ_k,γ_{k+1})）
    # ∫_2^T N(t)ix e^{itx}dt = Σ_{k=1}^{K-1} k·(e^{iγ_{k+1}x} - e^{iγ_k x})
    expz = np.exp(1j * z * x)
    # 注意：N(T) = K（含端点——右连续）
    rhs = np.exp(1j*T*x)*K - np.sum(np.arange(1, K) * (expz[1:] - expz[:-1]))
    print(f"\nx={x:.4f}:")
    print(f"  Σ e^(iγx)      = {lhs.real:+.6f} {lhs.imag:+.6f}i   |·|={abs(lhs):.6f}")
    print(f"  分部积分右侧   = {rhs.real:+.6f} {rhs.imag:+.6f}i   |·|={abs(rhs):.6f}")
    print(f"  差             = {abs(lhs-rhs):.2e}")
    # 分解：E_M（M 连续部分）
    # E_M = e^{iTx}M(T) - ix∫_2^T M(t)e^{itx}dt = M(2)e^{i2x} + ∫_2^T M'(t)e^{itx}dt
    # M'(t) = (1/2π)log(t/2π)
    # ∫_2^T (1/2π)log(t/2π)e^{itx}dt = (1/2π)[log(t/2π)e^{itx}/(ix) - (1/(ix))∫(1/t)e^{itx}dt]
    # = (1/2π)[(log(T/2π)e^{iTx} - log(1/π)e^{i2x})/(ix) - (1/(ix))(Ei(ixT)-Ei(ix2))]
    from scipy.special import expi
    EiT = expi(1j*x*T); Ei2 = expi(1j*x*2)
    EM = M(2)*np.exp(1j*2*x) + (1/(2*np.pi))*((np.log(T/(2*np.pi))*np.exp(1j*T*x) - np.log(1/np.pi)*np.exp(1j*2*x))/(1j*x) - (EiT - Ei2)/(1j*x))
    print(f"  E_M（主项）    = {EM.real:+.6f} {EM.imag:+.6f}i   |·|={abs(EM):.6f}")
    # E_78
    E78 = (7/8)*np.exp(1j*2*x)
    print(f"  E_78（常数）   = {E78.real:+.6f} {E78.imag:+.6f}i   |·|={abs(E78):.6f}")
    # E_S = 右侧 - E_M - E_78（S 部分的贡献——阶梯残余）
    ES = rhs - EM - E78
    print(f"  E_S（S 部分）  = {ES.real:+.6f} {ES.imag:+.6f}i   |·|={abs(ES):.6f}")
    return lhs, EM, ES

for x in [np.log(2), np.log(3), np.log(5), np.log(7), 1.0, 2.0]:
    analyze(x)
