#!/usr/bin/env python3
"""Test 6: 拆 k=1——加谐波(k≥2)到 Bohr 模型——残差积分是否降
如果加 k≥2 后 ∫R → O(1)——困难全在 k=1（谐波容易——）
如果仍在随机游走——k≥2 也难——
"""
import numpy as np
from math import log, pi
from bisect import bisect_right

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 200000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

def N0(t):
    if t <= 1: return 0.0
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

def S_at(u):
    k = bisect_right(z, u)
    return k - N0(u)

primes_t = []
for n in range(2, 80):
    if all(n % p for p in primes_t if p*p <= n):
        primes_t.append(n)

t0, t1 = 500.0, 60000.0
ds = 0.3
t_grid = np.arange(t0, t1, ds)
S_grid = np.array([S_at(t) for t in t_grid])
H = 1.0
nH = max(1, int(round(H/ds)))
kernel = np.ones(nH)/nH
sb = np.convolve(S_grid, kernel, mode='valid')
tb = t_grid[nH//2 : nH//2 + len(sb)]
T = tb[-1]

print('=== Test 6: 拆 k=1（固定 H=1——）===')
print(f'S̄ std={sb.std():.4f}')

def model_parts(include_k2, include_k3):
    model = np.zeros(len(tb))
    n_terms = 0
    for p in primes_t:
        # k=1
        a1 = np.trapz(sb*np.sin(tb*log(p)), tb)/T
        model += a1 * np.sin(tb*log(p))
        n_terms += 1
        # k=2（谐波——2 log p——）
        if include_k2:
            a2 = np.trapz(sb*np.sin(2*tb*log(p)), tb)/T
            model += a2 * np.sin(2*tb*log(p))
            n_terms += 1
        # k=3
        if include_k3:
            a3 = np.trapz(sb*np.sin(3*tb*log(p)), tb)/T
            model += a3 * np.sin(3*tb*log(p))
            n_terms += 1
    return model, n_terms

for k2, k3, name in [(False, False, '仅 k=1'), (True, False, 'k=1+2'), (True, True, 'k=1+2+3')]:
    model, nt = model_parts(k2, k3)
    R = sb - model
    cumR = np.cumsum(R) * ds
    # 随机游走基线
    rw = R.std() * np.sqrt(len(R)) * ds
    print(f'\n{name}（{nt} 项——）: 残差 std={R.std():.4f}——∫R max|={np.max(np.abs(cumR)):.3f}——'
          f'末值={cumR[-1]:+.3f}——随机游走基线={rw:.1f}——比值={np.max(np.abs(cumR))/max(rw,1e-9):.3f}')

# 谐波系数的大小（k=2——）——看是否小（易——）
print()
print('谐波系数（k=2——2log p——）幅度（vs k=1——）:')
for p in primes_t[:6]:
    a1 = np.trapz(sb*np.sin(tb*log(p)), tb)/T
    a2 = np.trapz(sb*np.sin(2*tb*log(p)), tb)/T
    print(f'  p={p}: a_1={a1:+.4f}——a_2={a2:+.4f}（比值 {abs(a2/a1) if abs(a1)>1e-6 else float("inf"):.3f}——）')
