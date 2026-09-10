#!/usr/bin/env python3
"""A2/A4 决定性测试：直接算 Ξ_w(t) 的符号（不用 R 线性化）
① w=0.01, t∈[126,158]：检验一阶预测 t_*(0.01)≈144 是否成立
② w=0.02, t∈[96,114]：检验一阶预测 t_*(0.02)≈106
精度自适应：dps = 30 + πt/(4ln10) + 20
"""
import mpmath as mp

def dps_for(t):
    return int(30 + float(mp.pi*mp.mpf(t)/4/mp.log(10)) + 20)

def theta(x):
    s = mp.mpf(1)
    for n in range(1, 10):
        s += 2*mp.e**(-mp.pi*n*n*x)
    return s

def Xi(w, t):
    t = mp.mpf(t); w = mp.mpf(w)
    mp.mp.dps = dps_for(t)
    s = mp.mpc(w/2, t)
    f = lambda u: (theta(u**(-2))**w - 1) * (u**(-s) + u**(-(w-s))) / u
    I = mp.quad(f, [0, mp.mpf('1e-3'), mp.mpf('1e-2'),
                    mp.mpf('0.1'), mp.mpf('0.5'), 1], maxdegree=10)
    Zv = -1/s + 1/(s-w) + I
    return (s*(s-w)/(2*w) * Zv).real

print('=== ② w=0.02, t∈[96,114]（一阶预测 t*≈106）===', flush=True)
for t in range(96, 115, 2):
    v = Xi(mp.mpf('0.02'), t)
    print(f'  t={t:>4}  dps={dps_for(t)}  Ξ = {mp.nstr(v,8):>16}   '
          f'{"【负】" if v < 0 else "正"}', flush=True)

print()
print('=== ① w=0.01, t∈[126,158]（一阶预测 t*≈144）===', flush=True)
for t in range(126, 159, 2):
    v = Xi(mp.mpf('0.01'), t)
    print(f'  t={t:>4}  dps={dps_for(t)}  Ξ = {mp.nstr(v,8):>16}   '
          f'{"【负】" if v < 0 else "正"}', flush=True)
