#!/usr/bin/env python3
"""R(t) = Ξ_0(t) / (−∂_w Ξ_w(t)|_{w=0})
——t_*(w) = min{t: R(t) ≤ w}，w_*(T) = min_{t≤T} R(t)
——关键问题：inf_t R(t) = 0 ?（= 对每个 w>0 都有线上零点）
Ξ_0(t) 用精确平方公式 (t²/8)|1-2^{1+it/2}|²|ζ̂(it/2)|² 高效计算
∂_w Ξ 用有限差分（w=1e-4, 2e-4 + Richardson）
"""
import mpmath as mp
mp.mp.dps = 55

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

def Xi0_exact(t):
    """Ξ_0(t) = (t²/8)|1-2^{1+it/2}|²|ζ̂(it/2)|²（精确平方）"""
    t = mp.mpf(t)
    return t**2/8 * abs(1 - 2**(1+mp.mpc(0,t/2)))**2 * abs(zeta_hat(mp.mpc(0,t/2)))**2

def dXi_dw(t, h=mp.mpf('1e-4')):
    """∂_w Ξ_w|_{w=0}，用两点 Richardson"""
    a = Xi(h, t); b = Xi(2*h, t)
    # 一阶近似 (Ξ(h)-Ξ_0)/h；这里直接用 Ξ(h),Ξ(2h) 消 Ξ_0
    d1 = (b - a)/h            # ≈ ∂_w + (3/2)h ∂²_w
    return d1

print('=== Ξ_0(t) 精确公式 vs 数值极限（校验）===')
for t in ['20','28.26','40']:
    tt = mp.mpf(t)
    print(f'  t={t}: Ξ_0(公式)={mp.nstr(Xi0_exact(tt),10)}  '
          f'Ξ(1e-3)={mp.nstr(Xi(mp.mpf("1e-3"),tt),10)}')

print()
print('=== R(t) 扫描 ===')
print('  t        Ξ_0(t)             ∂_wΞ(t)             R(t)=Ξ_0/(-∂_wΞ)')
rt_best = (mp.inf, 0)
rows = []
t = mp.mpf(10)
while t <= 130:
    x0 = Xi0_exact(t)
    d  = dXi_dw(t)
    if d != 0:
        R = x0/(-d) if d < 0 else -x0/d   # 记录带符号
        rows.append((t, x0, d, R))
    t += mp.mpf(2)
for (t, x0, d, R) in rows:
    mark = ''
    if d < 0 and R < rt_best[0]:
        rt_best = (R, t); mark = '  <-- new min'
    print(f'  {mp.nstr(t,6):>8} {mp.nstr(x0,8):>16} {mp.nstr(d,8):>16} '
          f'{mp.nstr(R,8):>16}{mark}', flush=True)

print()
print(f'=== R(t) 在 t≤130 的最小值（∂_wΞ<0 分支）: R_min = {mp.nstr(rt_best[0],8)} at t={mp.nstr(rt_best[1],6)} ===')
print('  预测：t_*(w) ≈ 最小满足 R(t)≤w 的 t')
for w in ['0.06','0.04','0.03','0.02','0.01']:
    wf = mp.mpf(w)
    hit = [t for (t,x0,d,R) in rows if d < 0 and R <= wf]
    print(f'  w={w}: 预测 t_*(w) ≈ {mp.nstr(min(hit),6) if hit else ">130"}')
