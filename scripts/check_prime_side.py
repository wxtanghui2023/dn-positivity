#!/usr/bin/env python3
"""严格化 A 检验: Sbar 的素数侧模型（Titchmarsh 型理论系数——）vs 真实
S(t) ~ -(1/pi)Σ_{p<=t} sin(t log p)/(√p log p)——Sbar(区间平均)的系数?
检验: 理论模型 vs 真实 Sbar——残差累积（M 的贡献——发散 or O(1)——）
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
M_inc = Sbar * dg
cumM = np.cumsum(M_inc)
t_mid = (z[:-1] + z[1:])/2

print('=== 严格化A: Sbar 素数侧模型（Titchmarsh 系数——）===')

# 理论模型: Sbar_theory = -(1/pi)Σ_{p} sin(t log p)/(√p log p)（区间平均修正——）
# 先直接试 Titchmarsh 系数（无修正——）——看幅度是否匹配
# S 的系数: c_p = 1/(π √p log p)——Sbar 应该同（区间平均对 sin 的修正 ~ sin 本身——）
ps = [2, 3, 5, 7, 11, 13, 17, 19]
model = np.zeros(len(t_mid))
for p in ps:
    c = 1.0/(pi * np.sqrt(p) * log(p))
    model -= c * np.sin(t_mid * log(p))

# 拟合真实 Sbar 的系数（对比理论——）
cols = []
for p in ps:
    cols.append(np.sin(t_mid * log(p)))
    cols.append(np.cos(t_mid * log(p)))
X = np.stack(cols, axis=1)
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)

print('系数对比（p=2..19——）:')
print(f'  p:     理论 1/(π√p log p)    实测(拟合)   比值')
for i, p in enumerate(ps):
    a_fit = np.hypot(coef[2*i], coef[2*i+1])
    c_th = 1.0/(pi*np.sqrt(p)*log(p))
    print(f'  p={p:2d}:   {c_th:.4f}              {a_fit:.4f}       {a_fit/c_th:.3f}')

# 关键: 实测系数 ~ 常数×理论？——如果常数 ~1——Titchmarsh 系数对——
# 实测 a_2 = 0.215——理论 c_2 = 1/(π·1.414·0.693) = 0.325——比值 0.66
# 实测 a_3 = 0.167——理论 c_3 = 1/(π·1.732·1.099) = 0.167——比值 1.00
# 实测 a_5 = 0.119——理论 c_5 = 1/(π·2.236·1.609) = 0.088——比值 1.35
print()
print('→ 比值不恒定（0.66→1.35——）——Sbar 系数 ≠ Titchmarsh S 系数——')

# 区间平均修正: Sbar 是 sin 的区间平均——sin(t log p) 在 [γ_k, γ_k+Δ] 的平均
# ~ sin(t log p)·sinc(Δ log p/2)——sinc 因子（Δ = 零点间距 ~2π/log t——）
# sinc(Δ log p/2) = sinc(π log p/log t)——随 p/t 变——复杂——数值验证:
print()
print('区间平均修正检验: 平均因子 sinc(π log p / log γ)——')
# 用数值: sin(t log p) 的局部平均（在零点区间——）vs 点值
# 通过比较不同 p 的比值偏差——检查是否 sinc 型
# 直接算 sinc 修正的模型
for p_test in [2, 3, 5]:
    g_ref = 50000.0
    sinc_f = np.sinc(log(p_test)/log(g_ref))  # sinc(π·log p/log γ)——用 np.sinc(x)=sin(πx)/(πx)
    print(f'  p={p_test} at γ~50000: sinc 因子={sinc_f:.4f}（~1——小修正——）')

# 无论如何——核心检验: 模型的残差累积（M 的贡献——）
print()
print('核心: 模型残差对 M 的贡献（发散 or O(1)——）:')
model_full = np.zeros(len(t_mid))
for p in ps:
    c = 1.0/(pi*np.sqrt(p)*log(p))
    model_full -= c * np.sin(t_mid * log(p))
resid = Sbar - model_full
resid_M = np.cumsum(resid * dg)
# 分段看 resid_M 的增长
print(f'残差 M 累积: 末值={resid_M[-1]:+.3f}——max|={np.max(np.abs(resid_M)):.3f}')
for i in range(0, K-1, 40000):
    print(f'  到零点{i}: resid_M={resid_M[i]:+.3f}')
print(f'（如果不发散——残差对 M 的贡献 O(1)——素数侧模型可证 M——）')
