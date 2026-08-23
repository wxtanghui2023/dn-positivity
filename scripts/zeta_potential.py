#!/usr/bin/env python3
"""探索 ζ 的"排斥势"：log|ζ(½+it)| 的零点贡献 = Σ_γ log|1−(½+it)/(½+iγ)|
GUE 类比：对数气体的势（Vandermonde 对数排斥）——平衡测度
关键：势的凸性（φ'' > 0？）——GUE 刚性证明的核心条件
"""
import numpy as np
import math
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(200000)

# 势函数：φ(t) = Σ_γ log|1−(½+it)/(½+iγ)|（截断到 γ_max）
# |1−(½+it)/(½+iγ)|² = |(½+iγ)−(½+it)|²/|½+iγ|² = |i(γ−t)|²/(¼+γ²) = (γ−t)²/(¼+γ²)
# log|1−...| = ½log((γ−t)²) − ½log(¼+γ²) = log|γ−t| − ½log(¼+γ²)

def phi(t, z):
    """势（零点部分）——log|γ−t| 的和（发散——但差有定义）"""
    # φ(t) = Σ log|γ−t| − ½Σlog(¼+γ²)
    g = z
    # 排除 t 附近的零点（奇点）
    mask = np.abs(g - t) > 0.5
    return np.sum(np.log(np.abs(g[mask]-t))) - 0.5*np.sum(np.log(0.25+g[mask]**2))

# 平衡测度验证：φ'(t) ≈ 0 在零点之间（平衡位置）
# φ'(t) = Σ 1/(t−γ)（Cauchy 主值意义）
def phi_prime(t, z):
    g = z
    mask = np.abs(g - t) > 0.5
    return np.sum(1.0/(t - g[mask]))

print("势的导数 φ'(t)（平衡位置检验——零点之间应 ≈ 0？）：")
for t in [20, 50, 100, 200, 500, 1000, 2000]:
    # 找一个零点之间的点
    idx = np.searchsorted(z, t)
    if idx > 0 and idx < len(z):
        mid = 0.5*(z[idx-1] + z[idx])
        dphi = phi_prime(mid, z)
        print(f"  t={mid:10.2f}（γ_{idx} 和 γ_{idx+1} 之间）: φ' = {dphi:+.3f}")

# 关键：N₀'(t) 与势的关系——平均密度
print("\n平均密度 N₀'(t) = log(t/2π)/2π vs 势的曲率：")
for t in [50, 200, 1000, 5000]:
    Np = log(t/(2*pi))/(2*pi)
    # 零点局部密度（数值）
    idx = np.searchsorted(z, t)
    if idx > 10 and idx < len(z)-10:
        local_density = 10/(z[idx+5]-z[idx-5])
        print(f"  t={t:5d}: 局部密度 = {local_density:.4f} vs N₀' = {Np:.4f}")

# 势的凸性：φ''(t) = −Σ 1/(t−γ)² < 0（对数势——凹？GUE 是凸的平衡）
print("\n势的凸性 φ''(t) = −Σ 1/(t−γ)²：")
for t in [50, 200, 1000]:
    idx = np.searchsorted(z, t)
    mid = 0.5*(z[idx-1]+z[idx]) if idx>0 else t
    g = z
    mask = np.abs(g-mid) > 0.5
    d2 = -np.sum(1.0/(mid-g[mask])**2)
    print(f"  t={mid:10.2f}: φ'' = {d2:+.6f}（< 0 = 凹——注意 GUE 平衡是势的凸最小）")
