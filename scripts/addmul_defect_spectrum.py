#!/usr/bin/env python3
# 整数加乘交换缺陷谱 —— T1/T2 测试
# K_N[m,n] = Σ_k C_add(m,k)·C_mul(n,k)  (J: 加法行与乘法行共享整数 k -> 1)
# K_N(s) = D(s)* K D(s),  D(s) = diag(n^{-s})
import numpy as np

def build_K(N):
    F_add = np.zeros((N, N))  # F_add[m,k] = #加行含 m 且含 k
    F_mul = np.zeros((N, N))
    # 加法行 (a,b,a+b)
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a + b <= N:
                c = a + b
                for m in (a, b, c):
                    mm = m - 1
                    for k in (a, b, c):
                        F_add[mm, k - 1] += 1
    # 乘法行 (a,b,ab)
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a * b <= N:
                c = a * b
                for m in (a, b, c):
                    mm = m - 1
                    for k in (a, b, c):
                        F_mul[mm, k - 1] += 1
    K = F_add @ F_mul.T + F_mul @ F_add.T  # 对称化 (J 含 add-mul 与 mul-add)
    return K

def K_s(K, s):
    """K_N(s,s̄)[m,n] = m^{-s̄} K[m,n] n^{-s}  (Hermitian)"""
    N = K.shape[0]
    n = np.arange(1, N + 1)
    d = n ** (-s)                     # n^{-s}
    return K * np.outer(np.conj(d), d)

def lmin(K, s):
    Hs = K_s(K, s)
    ev = np.linalg.eigvalsh(Hs)
    return ev[0], ev  # 最小特征值 + 全部

if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    K = build_K(N)
    print(f"N={N}  K shape={K.shape}  sym={np.allclose(K, K.T)}")
    ev0 = np.linalg.eigvalsh(K)
    print(f"  K (s=0) 谱: min={ev0[0]:.4f}  max={ev0[-1]:.4f}  #neg={np.sum(ev0<0)}")
    # 快速看 λ_min 随 σ (γ=0) 的行为
    print("  λ_min(N, σ+i·0):")
    for sigma in [0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8, 0.9]:
        lm, _ = lmin(K, sigma + 0j)
        print(f"    σ={sigma:.2f}: λ_min={lm:.6e}")
