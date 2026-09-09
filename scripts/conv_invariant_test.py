#!/usr/bin/env python3
"""守恒泛函测试（唐先生 14:13 框架——）
I_N = Σ_{j<k≤N}K(γ_j−γ_k) + λΣ_jV(γ_j)——dI_N/dN = 0
边际条件: λ_N^req = −2Σ_{j≤N}K(γ_{N+1}−γ_j)/V(γ_{N+1})·?（取 V=1——）
= −2Σ_{j≤N}K(γ_{N+1}−γ_j)——如果 λ_N^req ~ 常数（对 N——）→ 守恒存在——
测多个 K 候选: log|x|, 1/(1+x²), 1/x², e^{-x²}, cos(ax)/x（去主项——）
"""
import numpy as np
from math import log, pi

z = np.load('/tmp/zeros_odlyzko_2M.npy')
Kmax = 5000  # 测到 5000 零点

def lam_req(N, Kfunc, subtract=None):
    """λ_N^req = −2Σ_{j<N}K(γ_N−γ_j)（新零点 γ_N 与前面的——）"""
    gN = z[N-1]
    gs = z[:N-1]
    d = gN - gs
    val = Kfunc(d)
    if subtract is not None:
        val = val - subtract(d)
    return -2*np.sum(val)

Ks = {
    'log|x|': (lambda d: np.log(np.abs(d)+1e-30), None),
    '1/(1+x²)': (lambda d: 1.0/(1+d*d), None),
    '1/x²': (lambda d: 1.0/(d*d+1e-10), None),
    'e^{-x²/100}': (lambda d: np.exp(-d*d/100.0), None),
}

print('=== λ_N^req（边际——）随 N ===')
for name, (kf, sub) in Ks.items():
    vals = []
    for N in [100, 200, 500, 1000, 2000, 4000]:
        vals.append(lam_req(N, kf, sub))
    s = '——'.join(f'{v:.3f}' for v in vals)
    print(f'  {name}: {s}')

# log|x| 的去主项（长程——Σlog|x−γ_j| ~ N∫ρlog——去掉光滑背景——）
# 用 log|x| 的差（相邻 λ 的差——看涨落结构——）
print()
print('=== log|x| 的去趋势涨落（λ 的差分——）===')
lam_log = [lam_req(N, lambda d: np.log(np.abs(d)+1e-30)) for N in range(500, 4000, 100)]
lam_arr = np.array(lam_log)
# 去线性趋势（~N log N 的——）
# 一阶差（局部涨落——）
dlam = np.diff(lam_arr)
print(f'  λ(log) 的差分: mean={dlam.mean():.2f}——std={dlam.std():.2f}')
# 主项 ~ -2·N·(均值 log)——每步加 ~-2·(∫ρ log)——检查每步增量
steps = np.array(range(500, 4000, 100))
inc = np.diff(lam_arr)
# 每步（100 零点）增量
print(f'  每 100 零点的增量: {inc[:5]}...——均值 {inc.mean():.2f}')
# 增量是否稳定（→ 主项光滑——去主项后——）
print(f'  增量残差（去均值后——）std={ (inc-inc.mean()).std():.2f}——与 |增量| 比={ (inc-inc.mean()).std()/abs(inc.mean()):.3f}')
