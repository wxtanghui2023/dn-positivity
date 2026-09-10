#!/usr/bin/env python3
"""B-F1..B-F5 合并测试
恒等式（任意 X>0）：
Φ_w(s;X) = Σ a_m(πm)^{-s/2}Γ(s/2,πmX) + Σ a_m(πm)^{(s-w)/2}Γ((w-s)/2,πm/X)
           + 2X^{(s-w)/2}/(s-w) - 2X^{s/2}/s
Ξ_w(t) = s(s-w)/(4w)·Φ_w(s)
"""
import mpmath as mp

MMAX = 600
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
    key = (str(w), m, mp.mp.dps)   # 【修正】按 dps 缓存，避免低精度系数污染高精度调用
    if key in _ca: return _ca[key]
    t = mp.mpf(0)
    for k in range(1, m+1):
        if R[k][m]: t += binom_w(w, k)*(2**k)*R[k][m]
    _ca[key] = t
    return t

def Phi_AFE(w, s, dps, X=mp.mpf(1), M=None):
    mp.mp.dps = dps
    s = mp.mpc(s); w = mp.mpf(w); X = mp.mpf(X)
    if M is None: M = int(3*abs(s.imag)/(2*mp.pi)) + 30
    S1 = mp.mpf(0); S2 = mp.mpc(0)
    for m in range(1, M+1):
        am = a_m(w, m)
        if am == 0: continue
        S1 += am*(mp.pi*m)**(-s/2)*mp.gammainc(s/2, mp.pi*m*X, mp.inf)
        S2 += am*(mp.pi*m)**(s/2-w/2)*mp.gammainc((w-s)/2, mp.pi*m/X, mp.inf)
    return S1 + S2 + 2*X**((s-w)/2)/(s-w) - 2*X**(s/2)/s, M

def Xi_AFE(w, t, dps=None, X=mp.mpf(1)):
    if dps is None:
        dps = int(30 + float(mp.pi*mp.mpf(t)/4/mp.log(10)) + 20)
    w = mp.mpf(w)
    s = mp.mpc(w/2, t)
    ph, M = Phi_AFE(w, s, dps, X)
    return (s*(s-w)/(4*w)*ph).real, M, dps

print('='*70)
print('B-F1: t=154 附近锁 w_*(154)')
for w in ['0.0175','0.0177','0.017715','0.01773','0.0180']:
    v, M, dps = Xi_AFE(w, 154)
    print(f'  w={w:>9} t=154: Ξ = {mp.nstr(v,10):>18}  ({"正" if v>0 else "负"})  M={M} dps={dps}')

print()
print('='*70)
print('B-F2: t=74 伪点反证（应全为正）')
for w in ['1e-6','0.01','0.03','0.1','0.5']:
    v, M, dps = Xi_AFE(w, 74)
    print(f'  w={w:>7} t=74: Ξ = {mp.nstr(v,10):>18}  ({"正" if v>0 else "负"})  M={M} dps={dps}')

print()
print('='*70)
print('B-F4: X 不变性（(w,t)=(0.02,60)）')
for X in ['0.5','1','2']:
    w = mp.mpf('0.02'); s = mp.mpc(w/2, 60)
    ph, M = Phi_AFE(w, s, 60, X=mp.mpf(X))
    v = (s*(s-w)/(4*w)*ph).real
    print(f'  X={X}: Φ={mp.nstr(ph,12)}  Ξ={mp.nstr(v,10)}  M={M}')

print()
print('='*70)
print('B-F3: w=0.01 远端符号序列（找第一次真实穿零）')
for t in [160, 180, 200, 250, 300, 350, 400]:
    v, M, dps = Xi_AFE('0.01', t)
    print(f'  t={t:>4}: Ξ = {mp.nstr(v, 10):>18}  ({"正" if v>0 else "负"})  M={M} dps={dps}')

print()
print('='*70)
print('B-F3b: w=0.005 / 0.0177 抽查')
for (w, t) in [('0.005', 200), ('0.005', 300), ('0.0177', 200), ('0.0177', 300)]:
    v, M, dps = Xi_AFE(w, t)
    print(f'  w={w} t={t}: Ξ = {mp.nstr(v,10):>18}  ({"正" if v>0 else "负"})  M={M} dps={dps}')

print()
print('='*70)
print('B-F6: 修正缓存后重测 (0.01, 140/154)（对照直接积分 2.60e-44 / 1.15e-49）')
for t in [140, 154]:
    v, M, dps = Xi_AFE('0.01', t)
    print(f'  w=0.01 t={t}: Ξ = {mp.nstr(v,10):>18}  ({"正" if v>0 else "负"})  M={M} dps={dps}')
    for d in [dps+20, dps+40]:
        v2, M2, d2 = Xi_AFE('0.01', t, d)
        print(f'      稳定性检查 dps={d}: Ξ = {mp.nstr(v2,10)}  '
              f'({"一致" if abs(v2-v) < abs(v)*mp.mpf('1e-5') else "【不一致】"})')
