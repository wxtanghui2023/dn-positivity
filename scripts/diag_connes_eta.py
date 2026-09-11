#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 诊断: 极小化 Weil 二次型(简化版) 的 η 形状 vs Riemann 的 k(u)
import numpy as np

def k_riemann(u, nmax=200):
    s = np.zeros_like(u)
    for n in range(1, nmax+1):
        nu = n*u
        h = (np.pi/2)*nu**2*(2*np.pi*nu**2 - 3)*np.exp(-np.pi*nu**2)
        s += h
    return np.sqrt(u)*s

def build_weil_matrix_simple(xmax=13.0, N=400, primes=None):
    if primes is None:
        primes = [2,3,5,7,11,13]
    L = np.log(xmax)
    x = np.linspace(0, L, N)
    dx = x[1] - x[0]
    M = np.eye(N) * dx
    A = np.zeros((N, N))
    for p in primes:
        lp = np.log(p)
        mmax = int(np.log(xmax)/lp) + 1
        for m in range(1, mmax+1):
            shift = m*lp
            w = lp * p**(-m/2.0)
            if shift < L:
                j0 = int(round(shift/dx))
                for i in range(N - j0):
                    A[i, i+j0] += w*dx
                    A[i+j0, i] += w*dx
    return A, M, x

if __name__ == "__main__":
    xmax = 13.0
    for N in [300, 600]:
        print(f"\n=== N={N} ===")
        A, M, x = build_weil_matrix_simple(xmax=xmax, N=N)
        from scipy.linalg import eigh, cholesky
        Lc = cholesky(M, lower=True)
        Linv = np.linalg.inv(Lc)
        A_std = Linv @ A @ Linv.T
        evals, evecs = eigh(A_std)
        print("最小特征值:", np.array2string(evals[:6], precision=4))
        u = np.exp(x)
        kvals = k_riemann(u)
        k_inner = np.trapz(kvals**2, x)
        kn = kvals/np.sqrt(k_inner)
        for idx in range(6):
            eta_std = evecs[:, idx]
            eta = Linv.T @ eta_std
            norm = np.sqrt(np.trapz(eta**2, x))
            eta = eta/norm
            ov = abs(np.trapz(eta*kn, x))
            print(f"  特征向量 {idx}: λ={evals[idx]:.6e}, 与归一 k 重叠 = {ov:.4f}")
