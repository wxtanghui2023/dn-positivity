#!/usr/bin/env python3
"""Test 5: 比值滤波验证（最关键——）
Q_p(H1,H2) = a_p(H1)/a_p(H2) 应 = sinc(H1 log p/2)/sinc(H2 log p/2)
——消掉未知 a_p(0)——如果通过——Test 1 从'相关'升级为定理候选——
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

t0, t1 = 500.0, 60000.0
ds = 0.3
t_grid = np.arange(t0, t1, ds)
S_grid = np.array([S_at(t) for t in t_grid])
print(f'网格: {len(t_grid)} 点')

def Sbar_H(H):
    nH = max(1, int(round(H/ds)))
    kernel = np.ones(nH)/nH
    sb = np.convolve(S_grid, kernel, mode='valid')
    tb = t_grid[nH//2 : nH//2 + len(sb)]
    return tb, sb

# 计算多个 H 的 Bohr 系数
Hs = [0.5, 1.0, 2.0, 4.0]
ps_list = [2, 3, 5, 7, 11, 13, 17, 19]
a_coeff = {}  # (H, p) -> a_p

for H in Hs:
    tb, sb = Sbar_H(H)
    T = tb[-1]
    for p in ps_list:
        a = np.trapz(sb * np.sin(tb*log(p)), tb)/T
        a_coeff[(H, p)] = a

def sinc_H(H, p):
    x = H*log(p)/2
    return np.sin(x)/x if abs(x) > 1e-9 else 1.0

print()
print('=== Test 5: Q_p(H1,H2) vs sinc 比 ===')
print(f'{"p":>3} | {"Q(0.5/2.0)":>12} {"sinc比":>12} {"匹配":>6} | {"Q(1/4)":>12} {"sinc比":>12} {"匹配":>6}')
all_ok = True
for p in ps_list:
    for (H1, H2, label) in [(0.5, 2.0, 'a'), (1.0, 4.0, 'b')]:
        Q = a_coeff[(H1, p)]/a_coeff[(H2, p)]
        sinc_ratio = sinc_H(H1, p)/sinc_H(H2, p)
        match = abs(Q - sinc_ratio)/abs(sinc_ratio)
        if H1 == 0.5:
            print(f'{p:3d} | {Q:12.4f} {sinc_ratio:12.4f} {match:6.3f}', end='')
        else:
            print(f' | {Q:12.4f} {sinc_ratio:12.4f} {match:6.3f}')
    print()
    if match > 0.05: all_ok = False

print(f'\n整体匹配（<5% 偏差——）: {"✅ 通过" if all_ok else "❌ 有偏差"}')
