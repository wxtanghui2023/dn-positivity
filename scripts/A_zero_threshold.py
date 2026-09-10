#!/usr/bin/env python3
"""A：零阈值收敛审计（四层）
A1: R(t) 延伸 t∈[10,220] step2，自适应 dps，记录所有局部极小 → 拟合 R_min~Ct^-α
A2/A3: 【直接】对每个深凹 t_j 解 Ξ_w(t_j)=0 求 w_j（不依赖 R 线性化）
       → 得到真实临界曲线 (t_j, w_j)
A4: 检验 w_j 随 t_j 衰减 → 外推 w_*(T)→0 ？
"""
import mpmath as mp

def dps_for(t, extra=12):
    """Ξ ~ e^{-πt/4}；需 ~πt/4/ln10 有效位"""
    need = mp.pi*mp.mpf(t)/4/mp.log(10)
    return int(30 + need + extra)

def theta(x):
    s = mp.mpf(1)
    for n in range(1, 10):
        s += 2*mp.e**(-mp.pi*n*n*x)
    return s

def Xi(w, t, dps=None):
    if dps: mp.mp.dps = dps
    w = mp.mpf(w); t = mp.mpf(t)
    s = mp.mpc(w/2, t)
    f = lambda u: (theta(u**(-2))**w - 1) * (u**(-s) + u**(-(w-s))) / u
    I = mp.quad(f, [0, mp.mpf('1e-3'), mp.mpf('1e-2'),
                    mp.mpf('0.1'), mp.mpf('0.5'), 1])
    Zv = -1/s + 1/(s-w) + I
    return (s*(s-w)/(2*w) * Zv).real

def zeta_hat(s):
    s = mp.mpc(s)
    return mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)

def Xi0(t):
    t = mp.mpf(t)
    return t**2/8 * abs(1 - 2**(1+mp.mpc(0,t/2)))**2 * abs(zeta_hat(mp.mpc(0,t/2)))**2

# ---------------- A1 ----------------
print('=== A1: R(t) 扫描 [10,220] step 2 ===', flush=True)
rows = []
t = mp.mpf(10)
while t <= 220:
    tt = t
    d = dps_for(tt)
    x0 = Xi0(tt)                                    # 精确平方（不耗积分）
    mp.mp.dps = d
    xh = Xi(mp.mpf('1e-4'), tt, d)
    dxi = (xh - x0)/mp.mpf('1e-4')
    R = x0/(-dxi) if dxi < 0 else mp.mpf('nan')
    rows.append((tt, x0, dxi, R))
    t += 2
    if t <= 60 or int(t) % 10 == 0:
        print(f'  t={mp.nstr(tt,5):>6} R={mp.nstr(R,6)}', flush=True)

# 提取局部极小（滑动窗口）
locs = []
for i in range(1, len(rows)-1):
    if rows[i][3] == rows[i][3] and rows[i-1][3] == rows[i-1][3] and rows[i+1][3] == rows[i+1][3]:
        if rows[i][3] < rows[i-1][3] and rows[i][3] < rows[i+1][3]:
            locs.append((rows[i][0], rows[i][3]))
print('\n局部极小（t, R）:', flush=True)
for (tt, R) in locs:
    print(f'   t={mp.nstr(tt,5):>6}  R={mp.nstr(R,6)}', flush=True)

# 运行最小值序列（用于拟合）
run = []
cur = mp.inf
for (tt, x0, dxi, R) in rows:
    if R == R and R < cur:
        cur = R; run.append((tt, R))
print('\n运行最小值序列:', flush=True)
for (tt, R) in run:
    print(f'   t={mp.nstr(tt,5):>6}  Rmin={mp.nstr(R,6)}', flush=True)

# 拟合 R_min ~ C t^{-α}（用 t≥28 部分）
pts = [(tt, R) for (tt, R) in run if tt >= 28]
if len(pts) >= 3:
    n = len(pts)
    sx = sum(mp.log(tt) for tt, _ in pts); sy = sum(mp.log(R) for _, R in pts)
    sxx = sum(mp.log(tt)**2 for tt, _ in pts)
    sxy = sum(mp.log(tt)*mp.log(R) for tt, R in pts)
    slope = (n*sxy - sx*sy)/(n*sxx - sx*sx)
    inter = (sy - slope*sx)/n
    print(f'\n=== A1 拟合：log R_min = {mp.nstr(inter,6)} + ({mp.nstr(slope,6)})·log t '
          f'  → α = {mp.nstr(-slope,6)}（n={n}）===', flush=True)

# ---------------- A2/A3：直接求 (t_j, w_j) ----------------
print('\n=== A3: 直接解 Ξ_w(t_j)=0（临界曲线，不依赖 R）===', flush=True)
# 取深凹位置（每频带最深一个）
cands = [mp.mpf(x) for x in ['28','50','74','96','106','144','154','178']]
for tj in cands:
    d = dps_for(tj)
    lo, hi = mp.mpf('1e-6'), mp.mpf('0.5')
    vlo, vhi = Xi(lo, tj, d), Xi(hi, tj, d)
    if vlo*vhi > 0:
        print(f'  t_j={mp.nstr(tj,5)}: Ξ 在 w∈[{mp.nstr(lo,2)},{mp.nstr(hi,3)}] 内不变号 '
              f'(Ξ(1e-6)={mp.nstr(vlo,4)}, Ξ(0.5)={mp.nstr(vhi,4)})', flush=True)
        continue
    for _ in range(40):
        mid = (lo+hi)/2
        if Xi(mid, tj, d)*vlo <= 0: hi = mid
        else: lo = mid; vlo = Xi(lo, tj, d)
    wj = (lo+hi)/2
    print(f'  t_j={mp.nstr(tj,5):>6} → w_j = {mp.nstr(wj,8)}', flush=True)
