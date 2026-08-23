#!/usr/bin/env python3
"""黎曼和差验证（向量化——快速）：r(n) 振荡 = Σ f_n(γ_k) − ∫ f_n N₀'
用中点黎曼 + 欧拉-麦克劳林修正——先看数量级和趋势
"""
import numpy as np

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def N0p(t):
    return np.log(t/(2*np.pi))/(2*np.pi)

def th1(t):
    return np.arctan(1/(2*t))

def fn(t, n):
    return 4*np.sin(n*th1(t))**2

K = 2000000
z = load_zeros(K)
Tmax = z[-1]

# 向量化黎曼和差
# Σ f_n(γ_k)（零点求和）
# ∫ f_n N₀' dt ≈ Σ_k f_n(γ_k)·N₀'(γ_k)·Δγ_k（左端点——f_n 缓变时好）+ EM 修正
# 但 f_n 在 t ~ n 处振荡——左端点误差大——用中点
mid = 0.5*(z[:-1] + z[1:])
dg = np.diff(z)
fn_mid = fn(mid, 100)  # 测试 n=100
Np_mid = N0p(mid)

print("n=100：")
fv = fn(z, 100)
Sf = np.sum(fv)
# 尾部修正：Σ_{γ>γ_max} f_n ≈ ∫_T∞ f_n N₀'（f_n ~ n²/t²）
tail_f = 100**2*(np.log(Tmax/(2*np.pi))/Tmax + 1/Tmax)/(2*np.pi)
# 中点和
Smid = np.sum(fn_mid*Np_mid*dg)
print(f"  Σ f_n(γ_k) 到 γ_max = {Sf:+.4f}（尾部估计 {tail_f:+.6f}）")
print(f"  中点黎曼 ∫f_n N₀' ≈ {Smid:+.4f}")
print(f"  黎曼和差 ≈ {Sf - Smid:+.4f}（vs r(100)≈1.38）")

# 精确积分（对 n=100——f_n 在 t~100 附近振荡——用分段 Gauss）
print("\n精确积分（8点 Gauss 每区间，n=100——抽样每5区间）：")
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)
sel = np.arange(0, K-1, 5)  # 每5区间取1
total = 0.0
for k in sel:
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    total += 0.5*(b-a)*np.sum(wg*fn(ts, 100)*N0p(ts))
total *= 5  # 补偿抽样
tail = 100**2*(np.log(Tmax/(2*np.pi))/Tmax + 1/Tmax)/(2*np.pi)
Int = total + tail
Sf100 = np.sum(fn(z, 100))
print(f"  Σf(γ_k) = {Sf100:+.4f}")
print(f"  ∫f N₀' = {Int:+.4f}（抽样 Gauss + 尾部）")
print(f"  黎曼和差 = {Sf100 - Int:+.4f}（vs r(100)=1.38）")
