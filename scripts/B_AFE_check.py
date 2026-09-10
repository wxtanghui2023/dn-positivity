#!/usr/bin/env python3
"""B：AFE 身份式数值验证
Φ_w(s) = S1 + S2 − 2X^{s/2}/s   （X=1）
S1 = Σ a_m (πm)^{-s/2} Γ(s/2, πmX)
S2 = Σ a_m (πm)^{-(w-s)/2} Γ((w-s)/2, πm/X)
Ξ_w(t) = s(s-w)/(4w)·Φ_w(s),  s = w/2 + it

验证：① w=1, s=2,3 时 Φ_1 = 2ζ̂(s)（已知）
      ② w=0.02 t=40 / w=0.01 t=140 与直接积分值比较
"""
import mpmath as mp
mp.mp.dps = 35

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
    key = (w, m)
    if key in _ca: return _ca[key]
    t = mp.mpf(0)
    for k in range(1, m+1):
        if R[k][m]: t += binom_w(w, k)*(2**k)*R[k][m]
    _ca[key] = t
    return t

def Phi_AFE(w, s, M=200, X=mp.mpf(1)):
    s = mp.mpc(s); w = mp.mpf(w)
    S1 = mp.mpf(0); S2 = mp.mpc(0)
    for m in range(1, M+1):
        am = a_m(w, m)
        if am == 0: continue
        z1 = mp.pi*m*X
        g1 = mp.gammainc(s/2, z1, mp.inf)
        S1 += am*(mp.pi*m)**(-s/2)*g1
        z2 = mp.pi*m/X
        g2 = mp.gammainc((w-s)/2, z2, mp.inf)
        S2 += am*(mp.pi*m)**(-(w-s)/2)*g2
    return S1 + S2 + 2/(s-w) - 2*X**(s/2)/s

print('=== ① 校验：w=1, Φ_1(s) ?= 2ζ̂(s) = 2π^{-s/2}Γ(s/2)ζ(s) ===')
for s in [mp.mpc(2), mp.mpc(3), mp.mpc(4)]:
    got = Phi_AFE(1, s, M=300)
    want = 2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
    print(f'  s={s}: AFE={mp.nstr(got,15)}  2ζ̂={mp.nstr(want,15)}  '
          f'相对差={mp.nstr(abs(got-want)/abs(want),4)}')

print()
print('=== ② 大 t 检验：Ξ_w(t) = s(s−w)/(4w)·Φ_w(s) ===')
tests = [(mp.mpf('0.02'), 40, mp.mpf('2.9196367e-11')),
         (mp.mpf('0.02'), 60, mp.mpf('5.4516077e-18')),
         (mp.mpf('0.01'), 140, mp.mpf('2.6027029e-44')),
         (mp.mpf('0.01'), 144, mp.mpf('5.4134435e-48'))]
for (w, t, ref) in tests:
    s = mp.mpc(w/2, t)
    M = int(3*t/(2*mp.pi)) + 20
    ph = Phi_AFE(w, s, M=M)
    val = (s*(s-w)/(4*w)*ph).real
    print(f'  w={mp.nstr(w,4)} t={t}: AFE Ξ={mp.nstr(val,8)}   '
          f'直接积分={mp.nstr(ref,8)}  比={mp.nstr(val/ref,8) if ref!=0 else "-"}  (M={M}, dps={mp.mp.dps})')
