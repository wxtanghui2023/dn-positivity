#!/usr/bin/env python3
# ACPC A×M×A 闭环不变量——L_k 链计算 + κ 连通量
# L1 = Σ_{qm<=X} Λ(q)Λ(m) A(qm) A(m)
# L2 = Σ_{q1 q2 m<=X} Λ(q1)Λ(q2)Λ(m) A(q1q2m) A(q2m) A(m)
# L3 = Σ_{q1q2q3 m<=X} Λ(q1)Λ(q2)Λ(q3)Λ(m) A(q1q2q3m) A(q2q3m) A(q3m) A(m)
# κ1=L1, κ2=L2-½L1², κ3=L3-L1L2+⅓L1³
import numpy as np, math, time, sys

def sieve_primes(X):
    is_p = np.ones(X+1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(X**0.5)+1):
        if is_p[i]:
            is_p[i*i::i] = False
    return [int(i) for i in np.nonzero(is_p)[0]]

def prime_powers(X):
    """所有素幂 (值, log p), 排序"""
    items = []
    for p in sieve_primes(X):
        lp = math.log(p)
        pk = p
        while pk <= X:
            items.append((pk, lp))
            pk *= p
    items.sort()
    return items

def compute_A(X):
    """A(n) = Σ_{a+b=n} Λ(a)Λ(b)  (FFT 卷积)"""
    lam = np.zeros(X+1)
    # 素幂填充
    for p in sieve_primes(X):
        lp = math.log(p)
        pk = p
        while pk <= X:
            lam[pk] = lp
            pk *= p
    N = 1
    while N < 2*X+2:
        N <<= 1
    f = np.zeros(N)
    f[:X+1] = lam
    g = np.fft.rfft(f)
    h = np.fft.irfft(g*g)[:X+1]
    return h  # A[n] = Σ_{a+b=n}Λ(a)Λ(b), 含 a 或 b=1 (Λ(1)=0 自动排除)

def compute_Lk(X, A, pp):
    """计算 L1, L2, L3 (X 截断)"""
    pp_vals = [v for v,_ in pp]
    pp_lam = [l for _,l in pp]
    npp = len(pp_vals)
    # L1
    L1 = 0.0
    for i in range(npp):
        qi = pp_vals[i]; lqi = pp_lam[i]
        if qi > X//2: break
        lim = X // qi
        # m <= lim, m 素幂
        j = 0
        while j < npp and pp_vals[j] <= lim:
            mj = pp_vals[j]
            L1 += lqi*pp_lam[j]*A[qi*mj]*A[mj]
            j += 1
    # L2
    L2 = 0.0
    for i in range(npp):
        q1 = pp_vals[i]; l1 = pp_lam[i]
        if q1 > X//4: break
        for j in range(npp):
            q2 = pp_vals[j]
            q12 = q1*q2
            if q12 > X//2: break
            l12 = l1*pp_lam[j]
            lim = X // q12
            k = 0
            while k < npp and pp_vals[k] <= lim:
                m = pp_vals[k]
                L2 += l12*pp_lam[k]*A[q12*m]*A[q2*m]*A[m]
                k += 1
    # L3
    L3 = 0.0
    for i in range(npp):
        q1 = pp_vals[i]; l1 = pp_lam[i]
        if q1 > X//8: break
        for j in range(npp):
            q2 = pp_vals[j]
            q12 = q1*q2
            if q12 > X//4: break
            l12 = l1*pp_lam[j]
            for jj in range(npp):
                q3 = pp_vals[jj]
                q123 = q12*q3
                if q123 > X//2: break
                l123 = l12*pp_lam[jj]
                lim = X // q123
                k = 0
                while k < npp and pp_vals[k] <= lim:
                    m = pp_vals[k]
                    L3 += l123*pp_lam[k]*A[q123*m]*A[q3*q2*m]*A[q3*m]*A[m]
                    k += 1
    return L1, L2, L3

if __name__ == "__main__":
    Xs = [10000, 30000, 100000]  # 逐步
    if len(sys.argv) > 1:
        Xs = [int(sys.argv[1])]
    for X in Xs:
        t0 = time.time()
        A = compute_A(X)
        pp = prime_powers(X)
        print(f"X={X}: A 计算 {time.time()-t0:.1f}s, #pp={len(pp)}")
        t1 = time.time()
        L1, L2, L3 = compute_Lk(X, A, pp)
        print(f"  L 计算 {time.time()-t1:.1f}s")
        k1 = L1
        k2 = L2 - 0.5*L1*L1
        k3 = L3 - L1*L2 + (1.0/3.0)*L1**3
        print(f"  L1={L1:.6e}  L2={L2:.6e}  L3={L3:.6e}")
        print(f"  κ1={k1:.6e}  κ2={k2:.6e}  κ3={k3:.6e}")
        # 相对大小 (抵消检查)
        print(f"  κ2/L2={k2/L2:.6e}  κ3/L3={k3/L3:.6e}")
        print(f"  总耗时 {time.time()-t0:.1f}s")
        print()
