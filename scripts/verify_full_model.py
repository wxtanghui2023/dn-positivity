#!/usr/bin/env python3
"""验证 Sbar 完整展开（基频 + 谐波 k=2——）的完备性和 M 完整模型
S̄ ~ -(1/π)Σ_p Σ_k sin(k·t·log p)/(k·p^(k/2))——加谐波后 R 的行为——
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
cumM = np.cumsum(M_inc)
t_mid = (z[:-1] + z[1:])/2

primes = []
for n in range(2, 200):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)

print('=== Sbar 完整展开（基频+谐波——）完备性 ===')
print(f'Sbar std={Sbar.std():.4f}——方差={Sbar.var():.4f}')

# 逐步加: 基频(46) + 谐波(2p, 3p 对小 p——)
def build_cols(ps, kmax):
    cols = []
    for p in ps:
        cols.append(np.sin(t_mid * log(p)))
        cols.append(np.cos(t_mid * log(p)))
    for k in range(2, kmax+1):
        for p in ps:
            if k*p > 200:  # 谐波频率限制（k log p ≤ log 200 类——避免过拟合——）
                pass
            cols.append(np.sin(k*t_mid * log(p)))
            cols.append(np.cos(k*t_mid * log(p)))
    return np.stack(cols, axis=1)

# 方案1: 基频 p≤199 + 谐波 2p≤199
cols1 = []
for p in primes:
    cols1.append(np.sin(t_mid * log(p)))
    cols1.append(np.cos(t_mid * log(p)))
# 谐波 2·log p 对前几个 p（2,3,5——）+ 3·log2
for p in primes[:10]:
    cols1.append(np.sin(2*t_mid * log(p)))
    cols1.append(np.cos(2*t_mid * log(p)))
for p in primes[:4]:
    cols1.append(np.sin(3*t_mid * log(p)))
    cols1.append(np.cos(3*t_mid * log(p)))
X1 = np.stack(cols1, axis=1)
coef1, _, _, _ = np.linalg.lstsq(X1, Sbar, rcond=None)
R1 = Sbar - X1 @ coef1
print(f'基频46 + 谐波(2p×10 + 3p×4): R²={1-R1.var()/Sbar.var():.4f}——残差std={R1.std():.4f}')

# 谐波的系数（实测——）
print()
print('谐波系数（实测 vs log ζ 理论 1/(k·π·p^(k/2))——）:')
n_base = 46*2
for i, p in enumerate(primes[:10]):
    # 2log p 谐波的系数位置
    idx = n_base + 2*i
    if idx+1 < len(coef1):
        a = np.hypot(coef1[idx], coef1[idx+1])
        c_th = 1.0/(2*pi*p)  # k=2: 1/(k·π·p^(k/2)) = 1/(2πp)
        print(f'  2·log{p} (k=2): 实测={a:.5f}——理论 1/(2πp)={c_th:.5f}——比值={a/c_th:.3f}')

# M 完整模型验证
print()
print('M 完整模型（基频+谐波——1-cos 积分——）:')
# 从拟合系数构造 M 模型——M_model = Σ c_pk/k·(1-cos)——但拟合系数已是 Sbar 的——
# 简化: M_model = Σ a_i·(1-cos(ω_i t))/ω_i（对每个拟合的 sin/cos 分量——）
# 直接: Sbar 拟合的积分 = Σ (coef_sin/ω)(1-cos) + (coef_cos/ω)sin——（∫sin= (1-cos)/ω——∫cos = sin/ω——）
M_model = np.zeros(len(t_mid))
freqs_list = []
for p in primes:
    freqs_list.append((log(p), 0))  # sin
    freqs_list.append((log(p), 1))  # cos
for p in primes[:10]:
    freqs_list.append((2*log(p), 0))
    freqs_list.append((2*log(p), 1))
for p in primes[:4]:
    freqs_list.append((3*log(p), 0))
    freqs_list.append((3*log(p), 1))

for i, (w, kind) in enumerate(freqs_list):
    c = coef1[i]
    if kind == 0:  # sin → ∫ = (1-cos(wt))/w
        M_model += c * (1 - np.cos(w*t_mid))/w
    else:  # cos → ∫ = sin(wt)/w
        M_model += c * np.sin(w*t_mid)/w

# 对比真实 M
sample = np.linspace(5000, len(t_mid)-1, 300).astype(int)
print(f'真实 M: mean={np.mean(cumM[sample]):.3f}——max={np.max(cumM[sample]):.3f}——min={np.min(cumM[sample]):.3f}')
print(f'模型 M: mean={np.mean(M_model[sample]):.3f}——max={np.max(M_model[sample]):.3f}——min={np.min(M_model[sample]):.3f}')
c = np.corrcoef(cumM[sample], M_model[sample])[0,1]
print(f'相关: {c:.4f}')
residM = cumM - M_model
print(f'残差M: std={residM[sample].std():.4f}——max|={np.max(np.abs(residM[sample])):.3f}')
