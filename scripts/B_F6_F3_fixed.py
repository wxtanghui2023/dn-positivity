#!/usr/bin/env python3
"""B-F6 + B-F3（修正缓存 bug 后重跑）
—— 每个报出的值都附 dps 稳定性检查（同一个数在更高精度下必须复现）
"""
import mpmath as mp

MMAX = 700
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
    key = (str(w), m, mp.mp.dps)      # 【按 dps 缓存】修正污染
    if key in _ca: return _ca[key]
    t = mp.mpf(0)
    for k in range(1, m+1):
        if R[k][m]: t += binom_w(w, k)*(2**k)*R[k][m]
    _ca[key] = t
    return t

def Xi_AFE(w, t, dps):
    mp.mp.dps = dps
    w = mp.mpf(w)
    s = mp.mpc(w/2, t)
    M = int(3*mp.mpf(t)/(2*mp.pi)) + 30
    S1 = mp.mpf(0); S2 = mp.mpc(0)
    for m in range(1, M+1):
        am = a_m(w, m)
        if am == 0: continue
        S1 += am*(mp.pi*m)**(-s/2)*mp.gammainc(s/2, mp.pi*m, mp.inf)
        S2 += am*(mp.pi*m)**(s/2-w/2)*mp.gammainc((w-s)/2, mp.pi*m, mp.inf)
    phi = S1 + S2 + 2/(s-w) - 2/s
    return (s*(s-w)/(4*w)*phi).real, M

def certified(w, t):
    d0 = int(30 + float(mp.pi*mp.mpf(t)/4/mp.log(10)) + 25)
    v1, M = Xi_AFE(w, t, d0)
    v2, _ = Xi_AFE(w, t, d0 + 25)
    ok = abs(v2-v1) <= abs(v1)*mp.mpf('1e-8') + mp.mpf(10)**(-d0+10)
    return v1, M, d0, ok

print('=== B-F6: (0.01, 140) / (0.01, 154) —— 对照直接积分 2.60e-44 / 1.15e-49 ===')
for t in [140, 154]:
    v, M, d, ok = certified('0.01', t)
    print(f'  w=0.01 t={t}: Ξ = {mp.nstr(v,10):>18} ({"正" if v>0 else "负"})  '
          f'M={M} dps={d} 稳定性={"✓" if ok else "✗"}', flush=True)

print()
print('=== B-F3: w=0.01 远端符号序列（每点带稳定性证书）===')
for t in [160, 180, 200, 250, 300, 350, 400]:
    v, M, d, ok = certified('0.01', t)
    print(f'  t={t:>4}: Ξ = {mp.nstr(v,10):>18} ({"正" if v>0 else "负"})  '
          f'M={M} dps={d} 稳定性={"✓" if ok else "✗"}', flush=True)
