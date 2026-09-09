#!/usr/bin/env python3
"""构造+验证轮4: Sbar 几乎周期模型能否复现波包结构（ρ(2)~-0.64 + 交替和有界——）
Sbar ~ Σ a_p sin(γ·log p + φ_p)——拟合真实——合成——对比波包统计——
"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 100000
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
t_mid = (z[:-1] + z[1:])/2

def wavepackets(signal, inc):
    """从信号提取波包面积——"""
    signs = np.sign(signal)
    flips = np.where(signs[:-1] != signs[1:])[0] + 1
    bounds = np.concatenate([[0], flips, [len(signal)]])
    areas = []
    for i in range(len(bounds)-1):
        a, b = bounds[i], bounds[i+1]
        if b - a >= 1:
            areas.append(inc[a:b].sum())
    return np.array(areas)

# 1. 拟合真实 Sbar 的主导频率（log p——）
print('=== 轮4: Sbar 几乎周期模型 vs 真实波包结构 ===')
# 用最小二乘拟合 Sbar ~ Σ_p a_p sin(t log p) + b_p cos(t log p)（前几个 p——）
ps = [2, 3, 5, 7, 11, 13]
cols = []
for p in ps:
    cols.append(np.sin(t_mid * log(p)))
    cols.append(np.cos(t_mid * log(p)))
X = np.stack(cols, axis=1)
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)
# 残差
fit_real = X @ coef
resid = Sbar - fit_real
print(f'拟合 p={ps}:')
for i, p in enumerate(ps):
    a, b = coef[2*i], coef[2*i+1]
    amp = np.hypot(a, b)
    print(f'  p={p}: amp={amp:.4f}——(理论 1/(√p·log p) 归一: {amp*np.sqrt(p)*log(p):.3f}——)')
print(f'  R² = {1 - resid.var()/Sbar.var():.4f}（拟合占比——）')

# 2. 用拟合合成 Sbar（无残差——）——波包分析
real_areas = wavepackets(Sbar, M_inc)
fit_areas = wavepackets(fit_real, fit_real * dg)  # 合成用 fit 的增量

def stats(areas, name):
    b = np.abs(areas)
    N = len(b)
    r2 = np.corrcoef(b[:-2], b[2:])[0,1] if N > 3 else 0
    # 交替和有界（交替和的最大漂移——）
    alt = np.cumsum(areas)
    maxalt = np.max(np.abs(alt))
    # 随机游走期望（√N·std——）
    rw = np.sqrt(N) * b.std()
    print(f'{name}: N={N}——|面积| mean={b.mean():.4f}——ρ(2)={r2:+.3f}——'
          f'交替和max={maxalt:.3f}——随机游走期望={rw:.1f}——比值={maxalt/max(rw,1e-9):.4f}')

print()
print('真实 vs 合成（拟合部分——）波包统计:')
stats(real_areas, '真实')
stats(fit_areas, '合成(仅log2-13)')

# 3. 残差的波包（如果残差也是波包结构——还是噪声——）
resid_areas = wavepackets(resid, resid * dg)
stats(resid_areas, '残差')

# 4. 关键: 只含 log2+log3 的合成——最简模型
X23 = np.stack([np.sin(t_mid*log(2)), np.cos(t_mid*log(2)),
                np.sin(t_mid*log(3)), np.cos(t_mid*log(3))], axis=1)
c23, _, _, _ = np.linalg.lstsq(X23, Sbar, rcond=None)
fit23 = X23 @ c23
fit23_areas = wavepackets(fit23, fit23 * dg)
stats(fit23_areas, '合成(log2+log3)')
