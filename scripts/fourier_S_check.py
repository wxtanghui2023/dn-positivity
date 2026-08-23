#!/usr/bin/env python3
"""精确表述 Σsin(γ_k log p) = O(1) 为 S 的傅里叶问题：
Σ sin(γ_k x) = ∫sin(tx)N₀'dt + sin(Tx)S(T) - x∫cos(tx)S(t)dt + O(1)

定义 F_x(T) = x∫_2^T cos(tx)S(t)dt - sin(Tx)S(T) + cos(Tx)log(T/2π)/(2πx)
目标：验证 F_x(T) = O(1)？—— S 的傅里叶"去端点"界
S(t) 在 [γ_k, γ_{k+1}) 上 = k - N₀(t)（连续）——分段精确积分

原函数推导：
∫cos(tx)·(t/2π)log(t/2π)dt = [t·log(t/2π)sin(tx)/x + (log(t/2π)+1)cos(tx)/x² - Ci(tx)/x²]/(2π)
∫cos(tx)·(-t/2π)dt = -[t·sin(tx)/x + cos(tx)/x²]/(2π)
∫cos(tx)·(7/8)dt = (7/8)sin(tx)/x
∫cos(tx)·k dt = k·sin(tx)/x
"""
import numpy as np
from scipy.special import expi

def Ci(u):
    return 0.5*(expi(1j*u) + expi(-1j*u)).real

def N0(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) + 7/8

def H(t, k, x):
    """∫^t cos(ux)(k - N₀(u))du 的原函数值（在 t 处）"""
    # ∫cos·(k - N₀) = k·sin(tx)/x - ∫cos·N₀
    A_log = (t*np.log(t/(2*np.pi))*np.sin(t*x)/x + (np.log(t/(2*np.pi))+1)*np.cos(t*x)/(x*x) - Ci(t*x)/(x*x))/(2*np.pi)
    B_minus = -(t*np.sin(t*x)/x + np.cos(t*x)/(x*x))/(2*np.pi)
    C_78 = (7/8)*np.sin(t*x)/x
    int_N0 = A_log + B_minus + C_78  # ∫cos(tx)·N₀(t)dt
    return k*np.sin(t*x)/x - int_N0

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 2000000
z = load_zeros(K)
T = z[-1]

for x, lab in [(np.log(2), 'log2'), (np.log(3), 'log3'), (np.log(5), 'log5'), (1.0, '1.0'), (2.0, '2.0')]:
    # 分段积分 ∫_2^T cos(tx)S(t)dt = Σ_k [H(γ_{k+1}, k+1, x) - H(γ_k, k+1, x)]
    # 区间 [γ_k, γ_{k+1}) 上 S = (k+1) - N₀（γ_k 处右极限 k+1？不——S(γ_k⁺) = k - N₀(γ_k)）
    # 仔细：N(γ_k) = k（右连续，含 γ_k）。S(γ_k) = k - N₀(γ_k)。区间 [γ_k, γ_{k+1}) 上 N = k。
    # 所以 S(t) = k - N₀(t) on [γ_k, γ_{k+1})，k = 1..K-1；最后 [γ_K, T] 上 S = K - N₀(t)
    total = 0.0
    # [2, γ₁): N=0, S = -N₀
    total += H(z[0], 0, x) - H(2.0, 0, x)
    for k in range(1, K):  # [γ_k, γ_{k+1}) 上 N = k
        total += H(z[k], k, x) - H(z[k-1], k, x)
    # [γ_K, T]: N = K
    total += H(T, K, x) - H(z[K-1], K, x)
    
    S_T = K - N0(T)
    F = x*total - np.sin(T*x)*S_T + np.cos(T*x)*np.log(T/(2*np.pi))/(2*np.pi*x)
    Ssum = np.sum(np.sin(z*x))
    print(f"{x:.4f} ({lab}): ∫cos·S={total:+.4f}  F_x(T)={F:+.4f}  Σsin={Ssum:+.4f}")
