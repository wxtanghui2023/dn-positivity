# -*- coding: utf-8 -*-
# 仅用于离线数据分析（非研究结论）
import numpy as np, math, pandas as pd, time
t0=time.time()
z = pd.read_csv('zeros6', header=None, dtype=np.float64, engine='c').values.ravel()
N = len(z)
print(f"零点个数 N = {N:,}   最大 t = {z[-1]:.6f}   (用时 {time.time()-t0:.1f}s)")

# 展开（Riemann–von Mangoldt 光滑部分）: x_n = theta(t)/pi + 1
t = z
x = (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) - 1.0/8.0 + 1.0/(48*np.pi*t) + 7.0/(5760*np.pi*t**3) + 1.0
d = np.diff(x)
print(f"展开后平均间距 = {d.mean():.6f}（应为 1）  标准差 = {d.std():.6f}")

# [1] 归一化间隙分布 vs Wigner(Poise-like GUE surmise) vs Poisson
print("\n[1] 归一化间隙分布 s      实测       Wigner(GUE surmise)   Poisson")
for lo,hi in ((0.0,0.2),(0.2,0.4),(0.4,0.6),(0.6,0.8),(0.8,1.0),(1.0,1.4),(1.4,2.0),(2.0,3.0),(3.0,5.0)):
    obs = np.mean((d>=lo)&(d<hi))
    # Wigner surmise for GUE: p(s)=(32/pi^2) s^2 exp(-4 s^2/pi)
    f = lambda s: (32/math.pi**2)*s*s*math.exp(-4*s*s/math.pi)
    wg = np.mean([f(v) for v in np.linspace(lo,hi,60)])*(hi-lo)
    po = math.exp(-lo)-math.exp(-hi)
    print(f"   [{lo:.1f},{hi:.1f})   {obs:.5f}   {wg:.5f}   {po:.5f}")

# [2] 间隙自相关（对比素数间隙 lag1=-0.03556）
print("\n[2] 零点间隙自相关（素数间隙对照: lag1 = -0.03556, 40σ）")
for k in (1,2,3,4,5):
    a,b = d[:-k], d[k:]
    r = np.corrcoef(a,b)[0,1]
    print(f"   lag={k}: r = {r:+.5f}   (标准误≈{1/math.sqrt(len(a)):.5f}, |r|/se={abs(r)*math.sqrt(len(a)):.1f}σ)")

# [3] 配对相关 R2(s)（索引位移池化, s<=60）
print("\n[3] 配对相关 R2(s)  vs  GUE 1-(sin(pi s)/(pi s))^2")
nb, smax = 600, 60.0
edges = np.linspace(0, smax, nb+1)
hist = np.zeros(nb)
K = 90
for k in range(1, K+1):
    dk = x[k:] - x[:-k]
    dk = dk[dk <= smax]
    h,_ = np.histogram(dk, bins=edges)
    hist += h
bw = smax/nb
R2 = hist/(N*bw)   # 密度=1 归一
def r2gue(s):
    if s == 0: return 0.0
    return 1.0 - (math.sin(math.pi*s)/(math.pi*s))**2
print("   s_center   实测R2    GUE    Poisson(=1)")
for i in (5, 15, 25, 35, 50, 75, 100, 150, 200, 300, 450, 599):
    sc = (edges[i]+edges[i+1])/2
    print(f"   {sc:7.2f}   {R2[i]:7.4f}   {r2gue(sc):7.4f}   1.0000")

# [4] 刚性：数方差 Sigma^2(L)（长度 L 窗口内的计数方差）
print("\n[4] 数方差 Sigma^2(L)（展开后密度=1）  vs  Poisson=L  vs  GUE型 ~ a*log L + b")
starts = x[::50]
for L in (1,2,5,10,20,50,100,200,500,1000):
    idx = np.searchsorted(x, starts + L, side='left')
    cnt = idx - np.arange(len(starts))
    v = cnt.var()
    print(f"   L={L:5d}: Sigma^2 = {v:8.4f}    Poisson={L:8.4f}    比值={v/L:7.4f}")
# 拟合 a, b
Ls = np.array([2,5,10,20,50,100,200,500,1000], dtype=float)
Vs = []
for L in Ls:
    idx = np.searchsorted(x, starts + L, side='left')
    cnt = idx - np.arange(len(starts))
    Vs.append(cnt.var())
Vs = np.array(Vs)
A = np.vstack([np.log(Ls), np.ones(len(Ls))]).T
coef, *_ = np.linalg.lstsq(A, Vs, rcond=None)
print(f"\n   拟合 Sigma^2 ≈ a*log L + b  ⟹  a = {coef[0]:.4f}, b = {coef[1]:.4f}")
print(f"   对照: 2/pi^2 = {2/math.pi**2:.4f};  1/pi^2 = {1/math.pi**2:.4f}  ⚠️ 常数待核")
print(f"\n总用时 {time.time()-t0:.1f}s")
