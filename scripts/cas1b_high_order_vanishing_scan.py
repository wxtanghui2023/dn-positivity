#!/usr/bin/env python3
# cas1b_high_order_vanishing_scan.py —— CAS-1B：高阶消失阶判别实验（k=0..6）
# 【口径声明（本档约定，因唐先生记号有歧义）】 Q^(k) := 全 (kmax+1)x(kmax+1) Gram 的 (k+1)x(k+1) 主子矩阵（阶 0..k）
#   并同时报**归一化相关矩阵**（C_{kl}=Q_{kl}/sqrt(Q_kk Q_ll)）特征值，因高阶 Q_kk 量级差极大（数值健全性）
# 【对象】 Z=RS 实值函数；C=对照 sum cos(t log n)/sqrt n (n<=60)
# 【操作】 仅 shift + finite difference（Δ_h^k），h=2δ, δ=0.05；k<=6
# 【记录】 R_k=λmin/tr、κ_k=λmax/λmin、A_k=tr(Q^(k+1))/tr(Q^(k))、det(相关阵)、ζ vs C 跨尺度比较
import mpmath as mp
mp.mp.dps = 25
from math import comb

def Zfun(t):
    t = mp.mpf(t)
    th = mp.im(mp.loggamma(mp.mpf('0.25') + 1j*t/2)) - (t/2)*mp.log(mp.pi)
    return mp.re(mp.e**(1j*th) * mp.zeta(mp.mpf('0.5') + 1j*t))

NC = 60
def Cfun(t):
    t = mp.mpf(t); s = mp.mpf(0)
    for n in range(2, NC+1): s += mp.cos(t*mp.log(n))/mp.sqrt(n)
    return s

def scan(fun, T0, W, delta, hm, kmax=6):
    n = int(W/delta)
    cache = {}
    def f(t):
        key = int(round((t - T0)/delta))
        if key not in cache: cache[key] = fun(t)
        return cache[key]
    D = []
    for k in range(kmax+1):
        cf = [(-1)**(k-j)*comb(k, j) for j in range(k+1)]
        D.append([sum(cf[i]*f(T0 + j*delta + i*hm*delta) for i in range(k+1)) for j in range(n+1)])
    Q = [[sum(D[k][j]*D[l][j] for j in range(n+1)) for l in range(kmax+1)] for k in range(kmax+1)]
    return Q

def diag(Q, kmax=6):
    out = {}
    for k in range(kmax+1):
        sub = [[Q[i][j] for j in range(k+1)] for i in range(k+1)]
        ev = sorted([float(e) for e in mp.eigsy(mp.matrix(sub), eigvals_only=True)])
        tr = float(sum(sub[i][i] for i in range(k+1)))
        out[k] = dict(tr=tr, lmin=ev[0], lmax=ev[-1], R=(ev[0]/tr if tr else float('nan')),
                      kappa=(ev[-1]/ev[0] if ev[0] else float('inf')), ev=ev)
    # 相关阵（全阶）
    C = [[0]* (kmax+1) for _ in range(kmax+1)]
    for k in range(kmax+1):
        for l in range(kmax+1):
            d = mp.sqrt(Q[k][k]*Q[l][l])
            C[k][l] = float(Q[k][l]/d) if d != 0 else 0.0
    evc = sorted([float(e) for e in mp.eigsy(mp.matrix(C), eigvals_only=True)])
    return out, C, evc

if __name__ == '__main__':
    delta = mp.mpf('0.05'); hm = 2; kmax = 6
    print("=== CAS-1B 高阶消失阶判别（k<=6；h=2δ=0.1；W=100）===")
    print("【口径】 Q^(k) = 全 Gram 的 (k+1)x(k+1) 主子矩阵；另报归一化相关阵特征值（数值健全性）")
    summary = {}
    for T0 in (500, 1000, 2000):
        for tag, fun in (('Z', Zfun), ('C', Cfun)):
            Q = scan(fun, mp.mpf(T0), mp.mpf(100), delta, hm, kmax)
            d, C, evc = diag(Q, kmax)
            print(f"--- T0={T0} [{tag}] ---")
            for k in range(kmax+1):
                print(f"   k={k}: tr={d[k]['tr']:.6e} λmin={d[k]['lmin']:.4e} λmax={d[k]['lmax']:.4e} R_k={d[k]['R']:.6e} kappa={d[k]['kappa']:.3e}")
            Ak = [d[k+1]['tr']/d[k]['tr'] for k in range(kmax)]
            print("   A_k=tr(k+1)/tr(k): " + " ".join(f"{a:.6f}" for a in Ak))
            print("   A(k+1)/A(k):        " + " ".join(f"{Ak[i+1]/Ak[i]:.6f}" for i in range(len(Ak)-1)))
            print("   相关阵全阶特征值: " + " ".join(f"{e:.4e}" for e in evc))
            summary[(T0, tag)] = (d, Ak, evc)
    print()
    print("=== ζ 特异跨尺度锁定检查（Z 与 C 的 R_k / A_k 跨 T0 比较）===")
    for k in range(kmax+1):
        zz = [summary[(T, 'Z')][0][k]['R'] for T in (500, 1000, 2000)]
        cc = [summary[(T, 'C')][0][k]['R'] for T in (500, 1000, 2000)]
        print(f"   k={k}: R_k(Z)={['%.4e'%x for x in zz]} | R_k(C)={['%.4e'%x for x in cc]}")
