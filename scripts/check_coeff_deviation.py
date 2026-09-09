#!/usr/bin/env python3
"""系数偏离结构: 实测 a_p vs 理论 1/(π√p log p)——比值 f(p) 的模式
f(p): p=2:0.66, 3:1.00, 5:1.34, 7:1.49, 11:1.60, 13:1.60, 17:1.58, 19:1.55
——f(p) 随 p 增到 ~1.6 饱和？——f(p) ~ 1/(1-1/log p) 类？或 log 修正——
"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 200000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

dg = np.diff(z[:K])
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar = kk - (IntN[1:] - IntN[:-1])/dg
t_mid = (z[:-1] + z[1:])/2

ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
cols = []
for p in ps:
    cols.append(np.sin(t_mid * log(p)))
    cols.append(np.cos(t_mid * log(p)))
X = np.stack(cols, axis=1)
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)

print('=== 系数偏离结构 f(p) ===')
print('p:     实测a_p   理论c_p      f=a/c     候选: f~log p? f~1+1/log p?')
fits = []
for i, p in enumerate(ps):
    a_fit = np.hypot(coef[2*i], coef[2*i+1])
    c_th = 1.0/(pi*np.sqrt(p)*log(p))
    f = a_fit/c_th
    fits.append((p, f))
    print(f'p={p:2d}:  {a_fit:.4f}   {c_th:.4f}   {f:.3f}')

# 检验 f(p) 的候选形式
print()
print('候选拟合:')
for p, f in fits:
    # f ~ A·log(p·e^γ)?  f ~ 1 + a/log p?  f ~ (log p + b)/log p?
    print(f'  p={p:2d}: f={f:.3f}——1+1/log p={1+1/log(p):.3f}——log(ep)/log p={log(np.e*p)/log(p):.3f}——1/log p={1/log(p):.3f}')

# 更系统的: f(p) vs 1/log p（线性？）
fp = np.array([f for _, f in fits])
invlp = np.array([1/log(p) for p, _ in fits])
# 线性拟合 f = A + B/log p
A, B = np.polyfit(invlp, fp, 1)
print()
print(f'f vs 1/log p 线性拟合: f = {A:.3f} + {B:.3f}/log p')
print(f'  外推 log p→∞ (p→∞): f → {A:.3f}')

# f(p) 的另一种可能: 区间平均的精确修正（不是 sinc——而是零点密度的——）
# Sbar = 区间平均——平均权重 = 零点密度（非均匀——）
# 或者: Sbar 的定义（IntN 差/dg——）的离散效应——检查
# Sbar_k = k - (IntN[k+1]-IntN[k])/dg[k]——用 IntN 的离散差——如果 IntN 差有系统误差——
print()
print('注: 若 f(p)→~1.6（p→∞——）——则 a_p ~ 1.6/(π√p log p)——Σa_p/log p 仍收敛——')
print('   系数偏离不影响 M 有界性（收敛由 1/√p 主导——）——')
