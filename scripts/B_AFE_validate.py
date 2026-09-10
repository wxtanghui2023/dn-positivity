#!/usr/bin/env python3
"""B-G5：AFE 在基准点与更远处的交叉验证
Φ_w(s) = S1 + S2 + 2/(s−w) − 2/s   （X=1，已验证）
Ξ_w(t) = s(s−w)/(4w)·Φ_w(s)
"""
import mpmath as mp

MMAX = 200
R = [[0]*(MMAX+1) for _ in range(MMAX+1)]
R[0][0] = 1
for k in range(1, MMAX+1):
    for m in range(k, MMAX+1):
        s = 0; j = 1
        while j*j <= m:
            s += R[k-1][m-j*j]; j += 1
        R[k][m] = s

def binom_w(w, k):
    p = mp.mpf(1)
    for i in range(k): p *= (mp.mpf(w)-i)
    for i in range(1, k+1): p /= i
    return p

_ca = {}
def a_m(w, m):
    key = (str(w), m)
    if key in _ca: return _ca[key]
    t = mp.mpf(0)
    for k in range(1, m+1):
        if R[k][m]: t += binom_w(w, k)*(2**k)*R[k][m]
    _ca[key] = t
    return t

def Xi_AFE(w, t, dps):
    mp.mp.dps = dps
    s = mp.mpc(mp.mpf(w)/2, t)
    w = mp.mpf(w)
    M = int(3*mp.mpf(t)/(2*mp.pi)) + 30
    S1 = mp.mpf(0); S2 = mp.mpc(0)
    for m in range(1, M+1):
        am = a_m(w, m)
        if am == 0: continue
        S1 += am*(mp.pi*m)**(-s/2)*mp.gammainc(s/2, mp.pi*m, mp.inf)
        S2 += am*(mp.pi*m)**(s/2-w/2)*mp.gammainc((w-s)/2, mp.pi*m, mp.inf)
    phi = S1 + S2 + 2/(s-w) - 2/s
    return (s*(s-w)/(4*w)*phi).real, M

print('=== 精度需求对比（同一 (w,t)，只变 dps）===')
for (w, t) in [('0.02', 60), ('0.01', 154)]:
    for dps in [25, 30, 35, 40, 50, 60]:
        v, M = Xi_AFE(w, t, dps)
        print(f'  w={w} t={t} dps={dps:>3} M={M:>4}: Ξ = {mp.nstr(v, 10)}')
    print()

print('=== 基准点交叉验证（AFE vs 直接积分）===')
ref = {('0.02',40):'2.9196367e-11', ('0.02',60):'5.4516077e-18',
       ('0.01',140):'2.6027029e-44', ('0.01',144):'5.4134435e-48',
       ('0.01',154):'1.1506023e-49', ('0.017715',154):'~0 (切触点)'}
for (w, t), r in ref.items():
    dps = int(30 + float(mp.pi*mp.mpf(t)/4/mp.log(10)) + 15)
    v, M = Xi_AFE(w, t, dps)
    print(f'  w={w:>8} t={t:>4} dps={dps:>4} M={M:>4}: AFE Ξ = {mp.nstr(v,8):>16}   '
          f'直接积分={r}')

print()
print('=== 推进到直接积分做不到的区域（t=200, 300）===')
for (w, t) in [('0.01', 200), ('0.01', 300), ('0.005', 200)]:
    dps = int(30 + float(mp.pi*mp.mpf(t)/4/mp.log(10)) + 15)
    v, M = Xi_AFE(w, t, dps)
    print(f'  w={w} t={t} dps={dps} M={M}: Ξ = {mp.nstr(v,8)}  '
          f'({"正" if v > 0 else "负"})')
