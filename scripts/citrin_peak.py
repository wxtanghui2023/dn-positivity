#!/usr/bin/env python3
"""验证：零点 = 传输系数 t(E) 的局部极值（峰）——极值稳定性 = 刚性
峰的宽度（共振宽度）——窄峰 = 强共振 = 强刚性
"""
import numpy as np
import cmath
from math import log, pi

def t_curve(N, d, alpha, k_range, nk=300):
    z = d*np.log(np.arange(1, N+1))
    ks = np.linspace(k_range[0], k_range[1], nk)
    ts = np.zeros(nk)
    for i, k in enumerate(ks):
        T = np.eye(2, dtype=complex)
        for j in range(N-1, -1, -1):
            cj = (-1)**(j+1) * np.exp(-alpha*z[j])
            Mj = np.array([[1 - 1j*cj/(2*k), -1j*cj/(2*k)],
                           [1j*cj/(2*k), 1 + 1j*cj/(2*k)]])
            if j < N-1:
                dz = z[j+1] - z[j]
                P = np.array([[np.exp(1j*k*dz), 0], [0, np.exp(-1j*k*dz)]])
                T = T @ Mj @ P
            else:
                T = T @ Mj
        ts[i] = 1.0/np.abs(T[0,0])**2
    return ks, ts

# 参数
N = 300
d = 1.0
alpha = 0.5

# 零点
zeros = []
with open('/home/node/.openclaw/workspace/dn-project/zeros/zeros6') as f:
    for i in range(5):
        zeros.append(float(f.readline()))
zeros = np.array(zeros)

# t(E) 在零点附近——局部极大？
print("t(E) 在零点附近（局部极值检验——E = y = kd/2）：")
for gam in zeros[:4]:
    k0 = 2*gam/d
    ks, ts = t_curve(N, d, alpha, (k0*0.98, k0*1.02), 200)
    ys = ks*d/2
    # 找峰值
    imax = np.argmax(ts)
    y_peak = ys[imax]
    t_peak = ts[imax]
    # 峰宽（半高全宽——FWHM）
    half = (1 - t_peak)/2 + 0.5*t_peak  # 半高（t_peak 和 1 之间？——t 接近 1）
    # 用 t < t_peak - 0.1 的宽度
    mask = ts > t_peak - 0.1
    if np.sum(mask) > 2:
        idxs = np.where(mask)[0]
        width = ys[idxs[-1]] - ys[idxs[0]]
    else:
        width = float('nan')
    print(f"  γ={gam:8.3f}: 峰在 y={y_peak:.4f}（t={t_peak:.6f}）宽度(>t−0.1)={width:.4f}")

# 零点是否精确 = 峰？
print("\n零点 vs 峰位置：")
for gam in zeros[:4]:
    k0 = 2*gam/d
    ks, ts = t_curve(N, d, alpha, (k0*0.995, k0*1.005), 200)
    ys = ks*d/2
    imax = np.argmax(ts)
    print(f"  γ={gam:8.3f}: 峰 y={ys[imax]:.4f}（差 {abs(ys[imax]-gam):.4f}）t={ts[imax]:.6f}")

# 峰的形状（曲率——极值性质）
print("\n峰的曲率（t(E) 在零点附近——极值）：")
for gam in zeros[:2]:
    k0 = 2*gam/d
    ks, ts = t_curve(N, d, alpha, (k0*0.999, k0*1.001), 100)
    ys = ks*d/2
    imax = np.argmax(ts)
    if 1 < imax < len(ts)-2:
        # 二阶差分（曲率）
        curv = ts[imax+1] - 2*ts[imax] + ts[imax-1]
        print(f"  γ={gam:8.3f}: 二阶差分 = {curv:.6f}（负 = 局部极大 ✓）")
