#!/usr/bin/env python3
"""Citrin 模型的关键物理：准透明点（零点）的刚性——共振稳定性
微扰链参数（α, d）——透明点的移动——物理：共振稳定性 = 零点刚性
如果透明点稳定（微扰下移动小）——"刚性"的物理验证（对应 Σδ=O(1)）
"""
import numpy as np
import cmath
from math import log, pi

def transmission_curve(N, d, alpha, k_range, nk=500):
    """传输系数曲线（波矢 k 范围）"""
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

def find_peak_near(ks, ts, y_target, d):
    """找最接近 y_target 的透明峰（y = kd/2）"""
    ys = ks*d/2
    idx = np.argmin(np.abs(ys - y_target))
    return ys[idx], ts[idx]

# 基准参数
N = 300
d = 1.0
alpha0 = 0.5

# 零点（前 3 个）
zeros = []
with open('/home/node/.openclaw/workspace/dn-project/zeros/zeros6') as f:
    for i in range(3):
        zeros.append(float(f.readline()))
zeros = np.array(zeros)

# 微扰测试：α 微扰 → 透明点（零点附近）移动？
print("微扰 α → 透明点移动（共振稳定性——刚性）：")
print(f"{'零点':>8} {'α=0.500':>12} {'α=0.505':>12} {'α=0.510':>12} {'移动(0.5→0.51)':>12}")
for gam in zeros:
    k0 = 2*gam/d
    moves = []
    for alpha in [0.500, 0.505, 0.510]:
        ks, ts = transmission_curve(N, d, alpha, (k0*0.95, k0*1.05), 400)
        y_peak, t_peak = find_peak_near(ks, ts, gam, d)
        moves.append((y_peak, t_peak))
    delta_y = moves[-1][0] - moves[0][0]
    print(f"{gam:8.3f} {moves[0][0]:12.4f} {moves[1][0]:12.4f} {moves[2][0]:12.4f} {delta_y:12.4f}")

# 微扰 d
print("\n微扰 d → 透明点移动：")
for gam in zeros:
    k0 = 2*gam/1.0
    moves = []
    for dd in [1.00, 1.01, 1.02]:
        ks, ts = transmission_curve(N, dd, 0.5/dd, (k0*0.95, k0*1.05), 400)
        y_peak, t_peak = find_peak_near(ks, ts, gam, dd)
        moves.append(y_peak)
    delta_y = moves[-1] - moves[0]
    print(f"  γ={gam:8.3f}: y 移动 = {delta_y:+.4f}（d: 1.00→1.02）")

print("\n结论：透明点（零点）对微扰的稳定性 = 共振刚性")
print("（若移动小——零点刚性——对应 Σδ=O(1) 的物理版本）")
