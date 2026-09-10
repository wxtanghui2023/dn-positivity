#!/usr/bin/env python3
"""B-G5 决定性命中判据：w=1 时 Ξ₁(t) = Ξ(t) 有独立精确算法
  Ξ(t) = (1/2)s(s-1)π^{-s/2}Γ(s/2)ζ(s),  s = 1/2+it
AFE 若通过，则 AFE 表达式【精确】，可用于 w 小的情形并判定 t≥140 谁对
"""
import mpmath as mp

MMAX = 400
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
    return (s*(s-w)/(4*w)*phi).real

def Xi_exact(t, dps):
    mp.mp.dps = dps
    s = mp.mpc(mp.mpf(1)/2, t)
    return (s*(s-1)/2 * mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)).real

print('=== w=1 判定：AFE ?= 精确 Ξ(t) ===')
for t in [20, 50, 100, 154, 200]:
    dps_hi = int(40 + float(mp.pi*mp.mpf(t)/4/mp.log(10)))
    exact = Xi_exact(t, dps_hi)
    print(f'  t={t:>4}  精确 Ξ = {mp.nstr(exact, 10)}  (dps={dps_hi})')
    for dps in [30, 40, dps_hi]:
        v = Xi_AFE(1, t, dps)
        rel = abs(v-exact)/abs(exact) if exact != 0 else 0
        print(f'        AFE dps={dps:>4}: {mp.nstr(v, 10):>20}   相对差={mp.nstr(rel, 3)}')
    print()
