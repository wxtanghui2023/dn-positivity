#!/usr/bin/env python3
"""
QW_λ 高效实现——cos 基卷积闭式
F_i(t) = cos(πit/L)——支撑 [−L,L]
(F_i * F_j)(t) = ∫cos(πiu/L)cos(πj(t−u)/L)du——解析闭式
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def conv_cos(i, j, L, t):
    """(F_i*F_j)(t)——F_k(t)=cos(πkt/L) 支撑 [−L,L]——解析"""
    a = mp.pi*i/L
    b = mp.pi*j/L
    # ∫_{lo}^{hi} cos(au)cos(b(t-u)) du
    # = ½∫cos((a-b)u + bt)du + ½∫cos((a+b)u - bt)du
    lo = max(-L, t-L)
    hi = min(L, t+L)
    if lo >= hi:
        return mp.mpf('0')
    def I(alpha, beta):
        # ∫ cos(alpha*u + beta) du from lo to hi
        if abs(alpha) < 1e-12:
            return (hi-lo)*mp.cos(beta)
        return (mp.sin(alpha*hi+beta) - mp.sin(alpha*lo+beta))/alpha
    val = mp.mpf('0.5')*I(a-b, b*t) + mp.mpf('0.5')*I(a+b, -b*t)
    return val

def Wp_conv(i, j, L, p, m_max=40):
    lp = mp.log(p)
    total = mp.mpf('0')
    for m in range(1, m_max+1):
        t1 = m*lp
        if t1 < 2*L:  # 卷积支撑 [-2L, 2L]
            c1 = conv_cos(i, j, L, t1)
            c2 = conv_cos(i, j, L, -t1)
            total += p**(-m/2.0)*(c1+c2)
    return lp*total

def WR_conv(i, j, L):
    gE = mp.euler
    g1 = conv_cos(i, j, L, mp.mpf('0'))
    total = (mp.log(4*mp.pi)+gE)*g1
    def integrand(x):
        lx = mp.log(x)
        gx = conv_cos(i, j, L, lx)
        gix = conv_cos(i, j, L, -lx)
        if lx > 2*L:  # 卷积支撑外
            gx = mp.mpf('0')
        if -lx > 2*L or lx < -2*L:
            gix = mp.mpf('0')
        return (gx + gix - 2*x**(-0.5)*g1) * x**0.5/(x-x**(-1)) / x
    # 积分 1 到 e^{2L}（卷积支撑——）然后解析尾部
    total += mp.quad(integrand, [1, mp.e**(2*L)])
    # 尾部（x > e^{2L}——g(x)=0——g(1/x) 项——）
    def tail(x):
        lx = mp.log(x)
        gix = conv_cos(i, j, L, -lx) if -lx <= 2*L else mp.mpf('0')
        return (gix - 2*x**(-0.5)*g1) * x**0.5/(x-x**(-1)) / x
    total += mp.quad(tail, [mp.e**(2*L), mp.inf])
    return total

def main():
    print("="*70)
    print("QW_λ 高效实现（cos 卷积闭式——）")
    print("="*70)
    
    for lam in [2.0, 3.0, 5.0]:
        L = mp.log(lam)
        primes = [p for p in [2, 3, 5, 7, 11, 13] if p <= lam]
        Nbasis = 6
        QW = np.zeros((Nbasis, Nbasis))
        for i in range(Nbasis):
            for j in range(Nbasis):
                val = mp.mpf('0')
                for p in primes:
                    val += Wp_conv(i, j, L, p)
                val += WR_conv(i, j, L)
                QW[i, j] = float(val)
        QWsym = (QW + QW.T)/2
        evals, evecs = np.linalg.eigh(QWsym)
        gap = evals[1]-evals[0]
        print(f"\nλ={lam}: 特征值 = {np.array2string(evals, precision=4)}")
        print(f"  最小 {evals[0]:.6e}——第二 {evals[1]:.6e}——gap {gap:.2e}——simple? {gap > 1e-8}")
        v0 = evecs[:, 0]
        print(f"  最小特征向量: {np.array2string(v0, precision=3)}")

if __name__ == "__main__":
    main()
