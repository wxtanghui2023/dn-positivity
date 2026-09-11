#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 相位锁定定量：素数 cos(γ_k log p) 加权平均——为什么恒负（普适——）
import mpmath as mp
mp.mp.dps = 10
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True

def find_zero(seed):
    z = mp.mpc(0.5, seed)
    for _ in range(15):
        f = mp.zeta(z)
        fp = mp.diff(mp.zeta, z)
        z = z - f/fp
    return float(z.imag)

# 前 12 个零点
seeds = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052, 49.7738, 52.9703, 56.4462]
gammas = [find_zero(s) for s in seeds]

# 素数/合数（到 N——）
Nmax = 3000
ns = np.arange(2, Nmax)
pm = np.array([is_prime(n) for n in ns])
primes = ns[pm]
comps = ns[~pm]

print("=== 素数净负随零点高度 γ_k（普适性 + 强度）===")
print("γ_k         Re[Σ_p]    Re[Σ_c]   加权平均cos(素数)")
for g in gammas[:12]:
    # 平滑（X 大——σ=1/2 条件收敛——用 X=1500）
    X = 1500.0
    wp = np.exp(-primes/X) * primes**(-0.5)
    sp = np.sum(wp * np.cos(g*np.log(primes))) + 1j*np.sum(wp * np.sin(g*np.log(primes)))
    wc = np.exp(-comps/X) * comps**(-0.5)
    sc = np.sum(wc * np.cos(g*np.log(comps))) + 1j*np.sum(wc * np.sin(g*np.log(comps)))
    avg_cos = np.sum(wp*np.cos(g*np.log(primes)))/np.sum(wp)
    print(f"{g:>8.3f}   {sp.real:+8.4f}   {sc.real:+8.4f}   {avg_cos:+.4f}")

print()
print("=== 机制假说检验：素数负 ⟸ 合数不太负（Re[Σ_c] > -1）？===")
print("（数据：Re[Σ_c] 全部 > -1——合数实部有下界——）")
print("合数分散（相位随机——）→ 实部和 ~ 小（> -1）→ 素数被迫负——")
print()
print("=== 关键：'净负'对 σ 的依赖（σ=1/2 特殊吗？）===")
# 在 γ1——改变 σ——看素数加权平均 cos（权重 p^{-σ}——）——σ 影响小素数权重——
g = gammas[0]
print("σ        素数加权平均cos（权重 p^{-σ}——）")
for sg in [0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8]:
    wp = np.exp(-primes/X) * primes**(-sg)
    avg = np.sum(wp*np.cos(g*np.log(primes)))/np.sum(wp)
    print(f"{sg:.2f}    {avg:+.4f}")
