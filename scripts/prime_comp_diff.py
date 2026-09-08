#!/usr/bin/env python3
# 素数 vs 合数的不同点比较（找减速机制）
import numpy as np

gamma1 = 14.1347

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True

# 素数/合数列表（到 N）
N = 3000
X = 1500.0
ns = np.arange(2, N)
pm = np.array([is_prime(n) for n in ns])
primes = ns[pm]
comps = ns[~pm]
w_p = np.exp(-primes/X)
w_c = np.exp(-comps/X)

def P(sg, t):
    return np.sum(primes**(-sg-1j*t) * w_p)

def C(sg, t):
    return np.sum(comps**(-sg-1j*t) * w_c)

def dP(sg, t):
    return np.sum(-np.log(primes) * primes**(-sg-1j*t) * w_p)

def dC(sg, t):
    return np.sum(-np.log(comps) * comps**(-sg-1j*t) * w_c)

print("=== 素数 vs 合数：集体贡献与速度（γ1——沿 σ）===")
print("σ      |P|(素数)  |C|(合数)  |dP/dσ|    |dC/dσ|   速度比(|dP|/|dC|)")
for sg in [0.4, 0.45, 0.5, 0.52, 0.55, 0.6, 0.7]:
    p = abs(P(sg, gamma1))
    c = abs(C(sg, gamma1))
    dp = abs(dP(sg, gamma1))
    dc = abs(dC(sg, gamma1))
    print(f"{sg:.2f}   {p:8.3f}  {c:8.3f}  {dp:9.3f}  {dc:9.3f}  {dp/dc:8.3f}")

print()
print("=== 关键：'速度的减速'——随 σ 接近 1/2——素数 vs 合数 ===")
print("（看谁在 σ=1/2 附近'减速'（速度变化特殊——））")
print("σ      Re[Σ_p](素数实部)  Re[Σ_c](合数实部)")
for sg in [0.45, 0.48, 0.5, 0.52, 0.55]:
    rp = P(sg, gamma1).real
    rc = C(sg, gamma1).real
    print(f"{sg:.2f}   {rp:+10.4f}      {rc:+10.4f}")

print()
print("=== 相位锁定（cos 加权）——素数 vs 合数——随 σ ===")
for sg in [0.45, 0.5, 0.55]:
    cp = np.sum(w_p * primes**(-sg) * np.cos(gamma1*np.log(primes)))/np.sum(w_p*primes**(-sg))
    cc = np.sum(w_c * comps**(-sg) * np.cos(gamma1*np.log(comps)))/np.sum(w_c*comps**(-sg))
    print(f"σ={sg:.2f}: 素数加权cos={cp:+.4f}  合数加权cos={cc:+.4f}")
