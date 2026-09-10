#!/usr/bin/env python3
"""Lagarias-Rains 双变量 zeta：独立数值验证 + w_c 复现
Z_Q(w,s) = -1/s + 1/(s-w) + ∫_0^1 (θ(u^{-2})^w - 1)(u^{-s}+u^{-(w-s)}) du/u
ξ_Q(w,s) = s(s-w)/(2w) Z_Q(w,s)
Ξ_w(t) = ξ_Q(w, w/2 + it)
检验：① FE Z(w,s)=Z(w,w-s)  ② w=1 时 Z(1,s)=ζ̂(s)  ③ w=0 平方公式
     ④ 正性扫描 + w_c 复现
"""
import mpmath as mp
mp.mp.dps = 25

def theta(x):
    """θ(x)=Σ_{n∈ℤ}e^{-πn²x}，x≥1 时极快收敛"""
    s = mp.mpf(1)
    for n in range(1, 8):
        s += 2*mp.e**(-mp.pi*n*n*x)
    return s

def Z(w, s, pts=(0, mp.mpf('0.3'), mp.mpf('0.7'), 1)):
    w = mp.mpf(w); s = mp.mpc(s)
    out = -1/s + 1/(s-w)
    f = lambda u: (theta(u**(-2))**w - 1) * (u**(-s) + u**(-(w-s))) / u
    return out + mp.quad(f, list(pts))

def xi(w, s):
    w = mp.mpf(w); s = mp.mpc(s)
    return s*(s-w)/(2*w) * Z(w, s)

def Xi(w, t):
    w = mp.mpf(w)
    return xi(w, mp.mpc(w/2, t))

print('=== ① 函数方程 Z(w,s) = Z(w,w-s) ? ===')
for (w, s) in [(1, mp.mpc(2,3)), (mp.mpf('0.7'), mp.mpc('0.4','1.1')),
               (-1, mp.mpc(2,1))]:
    a, b = Z(w, s), Z(w, w-s)
    print(f'  w={float(w)}, s={s}: 差 = {mp.nstr(abs(a-b), 5)}')

print()
print('=== ② w=1: ξ_Q(1,s) = Riemann ξ(s) ? ===')
# Riemann ξ(s) = (1/2)s(s-1)π^{-s/2}Γ(s/2)ζ(s)
def riemann_xi(s):
    s = mp.mpc(s)
    return mp.mpf(1)/2 * s*(s-1) * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)
for s in [mp.mpc(2), mp.mpc(3), mp.mpc('1','4'), mp.mpc('0.5','5')]:
    got, want = xi(1, s), riemann_xi(s)
    print(f'  s={s}: ξ_Q(1,s)={mp.nstr(got, 12)}  ξ(s)={mp.nstr(want, 12)}'
          f'  相对差={mp.nstr(abs(got-want)/abs(want), 4)}')

print()
print('=== ③ w→0: ξ_Q(0,it) = (t²/8)|1-2^{1+it/2}|²|ζ̂(it/2)|² ? ===')
def zeta_hat(s):
    s = mp.mpc(s)
    return mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
for t in [mp.mpf(5), mp.mpf(14.13), mp.mpf(28.26)]:
    rhs = t**2/8 * abs(1 - 2**(1+mp.mpc(0,t/2)))**2 * abs(zeta_hat(mp.mpc(0,t/2)))**2
    for w in [mp.mpf('0.01'), mp.mpf('0.001')]:
        lhs = Xi(w, t)
        print(f'  t={float(t):.2f}, w={float(w)}: Ξ={mp.nstr(lhs.real,10)} '
              f'(虚部 {mp.nstr(lhs.imag,3)})  RHS公式={mp.nstr(rhs,10)}  比={mp.nstr(lhs.real/rhs,6)}')
    print()

print('=== ④ 正性扫描：Ξ_w(t) 的极小值 ===')
for w in ['0.02','0.05','0.055','0.0585','0.06','0.07','0.1']:
    wf = mp.mpf(w)
    # 在 t∈[20,35] 粗扫找极小
    lo, lo_t = mp.inf, 0
    t = mp.mpf(20)
    while t <= 35:
        v = Xi(wf, t).real
        if v < lo:
            lo, lo_t = v, t
        t += mp.mpf('0.25')
    print(f'  w={w}: min Ξ ≈ {mp.nstr(lo,8)} at t≈{mp.nstr(lo_t,6)}  (符号 {"+" if lo>0 else "−"})')
