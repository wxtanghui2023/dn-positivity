#!/usr/bin/env python3
"""复现 Citrin 2024 的 1D 对数链模型：准透明态 = 零点？
链：z_j = d·ln(j+1)——形状因子 (−1)^{j+1}e^{−αz_j}——αd = ½
传输矩阵（1D δ-势散射）——传输系数 vs 波矢 k——透明点 = 零点（y = kd/2）
"""
import numpy as np
import cmath
from math import log, pi

def transfer_matrix_chain(N, d, alpha, k, z0=1.0):
    """1D 链的传输矩阵——δ-势——强度 c_j = (−1)^{j+1}e^{−αz_j}
    返回总传输矩阵 T = T_N ... T_1
    """
    z = z0 + d*np.log(np.arange(1, N+1))  # z_j = d·ln(j+1)（+z0 平移）
    T = np.eye(2, dtype=complex)
    # 从右到左（j=N 到 1）
    for j in range(N-1, -1, -1):
        cj = (-1)**(j+1) * np.exp(-alpha*z[j])  # 形状因子（强度）
        # δ-势的传输矩阵（在 z_j 处）
        Mj = np.array([[1 - 1j*cj/(2*k), -1j*cj/(2*k)],
                       [1j*cj/(2*k), 1 + 1j*cj/(2*k)]])
        # 自由传播（z_j 到 z_{j+1}）
        if j < N-1:
            dz = z[j+1] - z[j]
            P = np.array([[np.exp(1j*k*dz), 0], [0, np.exp(-1j*k*dz)]])
            T = T @ Mj @ P
        else:
            T = T @ Mj
    return T

def transmission(T):
    """传输系数 t = 1/|T11|²（入射从左——透射到右）"""
    return 1.0/np.abs(T[0,0])**2

# 参数
d = 1.0
alpha = 0.5/d  # αd = ½
N = 500

# 零点（前几个）
zeros = []
with open('/home/node/.openclaw/workspace/dn-project/zeros/zeros6') as f:
    for i in range(30):
        zeros.append(float(f.readline()))
zeros = np.array(zeros)

# 传输系数 vs 能量 y（y = kd/2——k = 2y/d）
print("传输系数 vs 能量（准透明峰 = 零点？）：")
print(f"{'零点 γ_n':>10} {'t(2γ/d)':>12} {'峰值检测':>8}")
for gam in zeros[:10]:
    k = 2*gam/d
    T = transfer_matrix_chain(N, d, alpha, k)
    t = transmission(T)
    print(f"{gam:10.3f} {t:12.6f}")

# 扫描传输系数——找峰
print("\n扫描传输系数（找透明峰）：")
ks = np.linspace(2*zeros[0]/d, 2*zeros[9]/d, 200)
ts = []
for k in ks:
    T = transfer_matrix_chain(N, d, alpha, k)
    ts.append(transmission(T))
ts = np.array(ts)
# 峰值
peaks = []
for i in range(1, len(ts)-1):
    if ts[i] > ts[i-1] and ts[i] > ts[i+1] and ts[i] > 0.5:
        peaks.append((ks[i]*d/2, ts[i]))  # (y, t)
print(f"  检测到 {len(peaks)} 个峰（y > 0.5 的传输）")
for y, t in peaks[:10]:
    print(f"  峰在 y = {y:.3f}（t = {t:.3f}）")
print(f"  前 10 个零点：{[f'{g:.3f}' for g in zeros[:10]]}")
