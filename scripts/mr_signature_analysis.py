#!/usr/bin/env python3
# 任务1+2: Maier-Rassias 签名依赖分析 + 扰动测试
import numpy as np

def signature(N, sigma0, gamma0, A, B):
    return (A * N**(2*sigma0-1) * np.cos(2*gamma0*np.log(N)) + B * N**(2*sigma0-1)) / np.log(N)**2

print("=== Task 1: signature dependence ===")
print("\n--- sigma0 effect (exponent N^(2*sigma0-1)) ---")
N = 10**6
for sigma0 in [0.51, 0.55, 0.6, 0.7, 0.8, 0.9]:
    d2 = signature(N, sigma0, 100, 1.0, 2.0)
    print(f"sigma0={sigma0:.2f} (2s-1={2*sigma0-1:.2f}): d2@N=1e6 = {d2:.4e}")

print("\n--- gamma0 effect (frequency) ---")
for gamma0 in [10, 50, 100, 200, 500]:
    Ns = np.logspace(3, 7, 100)
    vals = signature(Ns, 0.6, gamma0, 1.0, 2.0)
    signs = np.sign(vals)
    crossings = np.sum(signs[1:] != signs[:-1])
    theory = 2*gamma0*(np.log(1e7)-np.log(1e3))/np.pi
    print(f"gamma0={gamma0}: crossings={crossings} (theory~{theory:.0f})")

print("\n--- A/B effect (d2 >= 0 constraint |A|<=B) ---")
for (A, B) in [(1.0, 2.0), (2.0, 2.0), (2.5, 2.0), (-1.0, 2.0)]:
    Ns = np.logspace(2, 8, 500)
    vals = signature(Ns, 0.6, 100, A, B)
    neg = np.sum(vals < 0)
    print(f"A={A}, B={B}: negative pts {neg}/{len(Ns)}")

print("\n=== Task 2: perturbation tests ===")
print("\n--- perturb sigma0 ---")
for d_sigma in [-0.05, -0.01, 0, 0.01, 0.05]:
    s0 = 0.6 + d_sigma
    ratio = signature(10**8, s0, 100, 1.0, 2.0) / signature(10**8, 0.6, 100, 1.0, 2.0)
    print(f"sigma0 0.6->{s0:.2f} (d={d_sigma:+.2f}): signature@N=1e8 x{ratio:.3f}")

print("\n--- perturb gamma0 (envelope unchanged, freq changes) ---")
for d_gamma in [0, 1, 10, 100]:
    g0 = 100 + d_gamma
    env_base = signature(np.array([10**6]), 0.6, 100, 1.0, 0.0)[0]
    env_new = signature(np.array([10**6]), 0.6, g0, 1.0, 0.0)[0]
    print(f"gamma0 100->{g0} (dg={d_gamma:+}): envelope {env_base:.4e} -> {env_new:.4e} (freq only)")

print("\n--- multi-quadruplet superposition ---")
def sig_multi(N, configs):
    total = 0
    for (s0, g0, A, B) in configs:
        total += signature(N, s0, g0, A, B)
    return total

c1 = [(0.6, 100, 1.0, 2.0)]
c2 = [(0.6, 100, 1.0, 2.0), (0.55, 200, 0.5, 1.0)]
c3 = [(0.6, 100, 1.0, 2.0), (0.65, 300, 0.8, 1.5)]
print(f"{'N':>8} {'single':>14} {'dual(low)':>14} {'dual(high)':>14}")
for Nv in [10**4, 10**6, 10**8]:
    print(f"{Nv:>8.0e} {sig_multi(Nv, c1):>14.4e} {sig_multi(Nv, c2):>14.4e} {sig_multi(Nv, c3):>14.4e}")
print("note: multi-quad superposition - max sigma0 dominates at large N")
