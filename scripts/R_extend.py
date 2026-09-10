#!/usr/bin/env python3
"""R(t) 延伸扫描：t ∈ [96, 190]，dps=68
目的：把 R_min(t) 的衰减律从 t≤130 推向 t~190，判定 R_min → 0 还是 plateau
"""
import mpmath as mp
mp.mp.dps = 68

def theta(x):
    s = mp.mpf(1)
    for n in range(1, 10):
        s += 2*mp.e**(-mp.pi*n*n*x)
    return s

def Z(w, s):
    w = mp.mpf(w); s = mp.mpc(s)
    out = -1/s + 1/(s-w)
    f = lambda u: (theta(u**(-2))**w - 1) * (u**(-s) + u**(-(w-s))) / u
    return out + mp.quad(f, [0, mp.mpf('1e-3'), mp.mpf('1e-2'),
                             mp.mpf('0.1'), mp.mpf('0.5'), 1])

def Xi(w, t):
    w = mp.mpf(w)
    s = mp.mpc(w/2, t)
    return (s*(s-w)/(2*w) * Z(w, s)).real

def zeta_hat(s):
    s = mp.mpc(s)
    return mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)

def Xi0(t):
    t = mp.mpf(t)
    return t**2/8 * abs(1 - 2**(1+mp.mpc(0,t/2)))**2 * abs(zeta_hat(mp.mpc(0,t/2)))**2

def dXi(t, h=mp.mpf('1e-4')):
    return (Xi(2*h, t) - Xi(h, t))/h

print('=== R(t) 延伸 [96,190] ===', flush=True)
best = (mp.inf, 0)
t = mp.mpf(96)
while t <= 190:
    x0 = Xi0(t); d = dXi(t)
    R = x0/(-d) if d < 0 else mp.mpf('nan')
    mark = ''
    if d < 0 and R < best[0]:
        best = (R, t); mark = '  <-- new min'
    print(f'  t={mp.nstr(t,5):>6}  Ξ0={mp.nstr(x0,6):>13}  dXi={mp.nstr(d,6):>13}  '
          f'R={mp.nstr(R,6):>12}{mark}', flush=True)
    t += mp.mpf(2)

print()
print(f'=== t≤190 的 R_min = {mp.nstr(best[0],6)} at t={mp.nstr(best[1],5)} ===')
print('  （对照：t≤130 的 R_min = 0.01653 at t=130）')
