#!/usr/bin/env python3
# 采集 c(gamma): beta(X) = 1/2 - c/X 的常数——对前 12 个零点——拟合 c 与 gamma 的关系
import numpy as np
import mpmath as mp

def zeta_smooth_vec(s, X, nmax_factor=25):
    nmax = max(int(nmax_factor*X), 200)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def zeta_smooth_mp(s, X):
    nmax = max(int(25*X), 200)
    total = mp.mpc(0)
    for k in range(1, nmax+1):
        total += mp.mpf(k)**(-s) * mp.e**(-mp.mpf(k)/X)
    return total

def zero_at_X(seed, X):
    """从种子出发——找 ζ_X 最近零点（numpy 初 + mpmath 精）"""
    z = complex(seed[0], seed[1])
    for it in range(40):
        f = zeta_smooth_vec(z, X)
        h = 1e-6 + 1e-6j
        fp = (zeta_smooth_vec(z+h, X) - zeta_smooth_vec(z-h, X)) / (2*h)
        step = f/fp
        z = z - step
        if abs(step) < 1e-9:
            break
    zm = mp.mpc(z.real, z.imag)
    def fmp(s):
        return zeta_smooth_mp(s, X)
    zm = mp.findroot(fmp, zm, tol=1e-11, maxsteps=30)
    return float(zm.real), float(zm.imag)

# ζ 的真实零点虚部（前 12 个）
known = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187,
         43.3271, 48.0052, 49.7738, 52.9703, 56.4462]

print("=== c(γ) 采集：β(X) = ½ − c/X——X=100 和 X=200 ===")
print(f"{'γ_ζ':>8} {'β(100)':>8} {'c(100)':>8} {'β(200)':>8} {'c(200)':>8} {'c_avg':>8}")
cs = []
for gk in known:
    b100, g100 = zero_at_X((0.5, gk), 100)
    b200, g200 = zero_at_X((0.5, gk), 200)
    c100 = (0.5 - b100) * 100
    c200 = (0.5 - b200) * 200
    cavg = (c100 + c200) / 2
    cs.append((gk, cavg))
    print(f"{gk:>8.4f} {b100:>8.4f} {c100:>8.3f} {b200:>8.4f} {c200:>8.3f} {cavg:>8.3f}")

# 拟合 c vs gamma
print("\n=== 拟合 c(γ) ===")
gs = np.array([c[0] for c in cs])
cvs = np.array([c[1] for c in cs])
# 试 c ~ a*log(γ) + b
A = np.vstack([np.log(gs), np.ones(len(gs))]).T
coef, res, _, _ = np.linalg.lstsq(A, cvs, rcond=None)
print(f"c ~ {coef[0]:.4f}·log γ + {coef[1]:.4f}")
pred = coef[0]*np.log(gs) + coef[1]
print(f"max err: {np.max(np.abs(pred-cvs)):.4f}")
# 试 c ~ a*sqrt(γ)
A2 = np.vstack([np.sqrt(gs), np.ones(len(gs))]).T
coef2, _, _, _ = np.linalg.lstsq(A2, cvs, rcond=None)
pred2 = coef2[0]*np.sqrt(gs) + coef2[1]
print(f"c ~ {coef2[0]:.4f}·√γ + {coef2[1]:.4f}  max err: {np.max(np.abs(pred2-cvs)):.4f}")
# 试 c ~ a*γ/log(γ)
A3 = np.vstack([gs/np.log(gs), np.ones(len(gs))]).T
coef3, _, _, _ = np.linalg.lstsq(A3, cvs, rcond=None)
pred3 = coef3[0]*gs/np.log(gs) + coef3[1]
print(f"c ~ {coef3[0]:.4f}·γ/log γ + {coef3[1]:.4f}  max err: {np.max(np.abs(pred3-cvs)):.4f}")
