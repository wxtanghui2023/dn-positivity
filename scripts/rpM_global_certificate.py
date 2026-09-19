#!/usr/bin/env python3
"""
(RP_M) 全域证书：min_{phi in [0,pi]^M} max_{1<=k<=5M} Σ_j cos(k phi_j) 的下界
方法：单元中心 grid + Lipschitz（严格）
  F_k 的梯度：|grad F_k| = k sqrt(Σ_j sin^2(k phi_j)) <= k sqrt(M) <= K sqrt(M) =: L
  单元（边长 h 的 M-方体）半对角 = h sqrt(M)/2  ⟹ |g(x)-g(center)| <= L h sqrt(M)/2 =: err
  求值误差 <= 1e-12（双精度，10~50 项求和）
用法：python3 rpM_global_certificate.py M N
"""
import sys, time
import numpy as np

M = int(sys.argv[1]); N = int(sys.argv[2])
K = 5 * M
h = np.pi / N
ax = (np.arange(N) + 0.5) * h
L = K * np.sqrt(M)
err = L * h * np.sqrt(M) / 2.0
EVAL_ERR = 1e-12
print(f"M={M} N={N} K={K} h={h:.6f} L={L:.4f} 单元Lipschitz余项={err:.6f}")
Ks = np.arange(1, K + 1)
rest = (N,) * (M - 1)
best = 9.0
t0 = time.time()
BLK = max(1, int(2e6 // max(1, N ** (M - 1))))
for s in range(0, N, BLK):
    S = ax[s:s + BLK]
    G = np.full((len(S),) + rest, -9.0)
    for k in Ks:
        term = np.cos(k * S).reshape([len(S)] + [1] * (M - 1))
        for d in range(M - 1):
            sh = [1] * M
            sh[1 + d] = N
            term = term + np.cos(k * ax).reshape(sh)
        G = np.maximum(G, term)
    m = float(G.min())
    if m < best:
        best = m
cert = best - err - EVAL_ERR
print(f"网格最小 g = {best:.9f}   (用时 {time.time()-t0:.1f}s)")
print(f"★ 认证下界 = {cert:.9f}   > 1/2 ? {cert > 0.5}")
