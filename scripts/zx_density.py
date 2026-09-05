#!/usr/bin/env python3
# 连接框架：ζ_X（平滑截断——）的 u_X=Re ζ_X=0 密度——是否也有 σ=½ 分界？
import numpy as np

def zeta_X(s, X, nmax_factor=20):
    nmax = max(int(nmax_factor*X), 300)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def count_uX0(sg, X, t_max=60.0, step=0.1):
    cnt = 0
    ts = np.arange(1, t_max, step)
    prev = None
    for t in ts:
        u = zeta_X(complex(sg, t), X).real
        if prev is not None and prev*u < 0:
            cnt += 1
        prev = u
    return cnt

print("=== ζ_X 的 u_X=0 密度随 σ（X=50——t 到 60——）——是否有 σ=½ 分界？ ===")
print("σ       u_X=0 计数")
for sg in np.arange(0.30, 0.90, 0.05):
    cnt = count_uX0(sg, 50)
    print(f"{sg:.2f}   {cnt:>5}")
