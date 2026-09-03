#!/usr/bin/env python3
# Arithmetic Domain Flow: J_ω essential spectrum 测试
# x_{k+1} = 1/(p_k + x_k), θ_k = x_k
# a_k = 1/θ_k, b_k = θ_k + θ_{k+1}
# J_ω: (Jf)_k = a_k f_{k+1} + a_{k-1} f_{k-1} + b_k f_k  (ℓ²(N) Jacobi)
# 判据: Spec_ess(J_ω) 对不同 ω 是否不同 / 是否携带不可约 prime-history
import numpy as np, math

def jacobi_spectrum(primes, N, x1=0.5):
    """构造 J_ω 的 N×N 截断, 返回特征值"""
    # x 递归
    x = [0.0]*(N+2)
    x[1] = x1
    for k in range(1, N+1):
        p = primes[min(k-1, len(primes)-1)]  # 周期/截断使用
        x[k+1] = 1.0/(p + x[k])
    # 系数
    a = [0.0]*(N+1)
    b = [0.0]*(N+1)
    for k in range(1, N+1):
        a[k] = 1.0/x[k]
        b[k] = x[k] + x[k+1]
    # 三对角 (1-indexed -> 0-indexed: 行 k-1)
    diag = np.array([b[k] for k in range(1, N+1)])
    off = np.array([a[k] for k in range(1, N)])  # a_k 在 (k-1, k)
    return np.linalg.eigvalsh(np.diag(diag) + np.diag(off, 1) + np.diag(off, -1))

def primes_list(n):
    """前 n 个素数"""
    is_p = np.ones(1000000, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(1000000**0.5)+1):
        if is_p[i]:
            is_p[i*i::i] = False
    ps = [int(i) for i in np.nonzero(is_p)[0]]
    return ps[:n]

if __name__ == "__main__":
    N = 400
    nat = primes_list(N)
    envs = {
        "全2": [2]*N,
        "全3": [3]*N,
        "全5": [5]*N,
        "自然素数": nat,
        "交替2,3": [2,3]*(N//2+1),
        "2,3,5循环": [2,3,5]*(N//3+2),
    }
    print(f"J_ω 截断谱 (N={N}) — essential spectrum 近似:")
    print(f"{'环境':>12} {'min':>10} {'max':>10} {'谱宽':>10} {'密度(中心)':>10}")
    for name, ps in envs.items():
        ev = jacobi_spectrum(ps, N)
        # 中心密度 (中段特征值间距)
        mid = ev[len(ev)//2]
        lo = ev[len(ev)//2 - 50] if len(ev) > 100 else ev[0]
        hi = ev[len(ev)//2 + 50] if len(ev) > 100 else ev[-1]
        dens = 100/(hi-lo) if hi > lo else 0
        print(f"{name:>12} {ev[0]:>10.3f} {ev[-1]:>10.3f} {ev[-1]-ev[0]:>10.3f} {dens:>10.4f}")
        # 特征值中间段样本
        if name in ("全2","全3","自然素数"):
            print(f"    中段特征值: {[round(v,3) for v in ev[N//2-2:N//2+3]]}")
