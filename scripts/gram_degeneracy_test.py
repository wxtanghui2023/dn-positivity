#!/usr/bin/env python3
# 决定性计算：算术平移 Gram 几何 G_X(s) 在 ζ_X 零点处的退化测试
# G_X(s)_{r,q} = Σ_{n≥1} e^{-n/X}(n+r)^{-s}(n+q)^{-s̄}——N×N Gram（半正定——）
# 测试：零点处是否出现特殊退化（最小特征值 → 0 / det → 0）——对比非零点
import numpy as np

def gram_matrix(s, X, N, nmax_factor=10):
    """G_X(s)_{r,q} = Σ_n e^{-n/X}(n+r)^{-s}(n+q)^{-conj(s)}——N×N"""
    sg, t = s.real, s.imag
    nmax = max(int(nmax_factor*X), 200)
    n = np.arange(1, nmax+1, dtype=np.float64)
    w = np.exp(-n/X)
    G = np.zeros((N, N), dtype=np.complex128)
    for r in range(N):
        for q in range(N):
            # Σ_n e^{-n/X} (n+r)^{-σ-it} (n+q)^{-σ+it}
            nr = n + r
            nq = n + q
            val = np.sum(w * nr**(-sg-1j*t) * nq**(-sg+1j*t))
            G[r, q] = val
    return G

def zeta_X(s, X):
    nmax = max(int(15*X), 300)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    ns = np.exp(-complex(s) * logn)
    return np.sum(ns * np.exp(-n/X))

def refine(seed, X):
    z = complex(seed)
    for it in range(60):
        f = zeta_X(z, X)
        h = 1e-6+1e-6j
        fp = (zeta_X(z+h, X)-zeta_X(z-h, X))/(2*h)
        step = f/fp
        z = z - step
        if abs(step) < 1e-12: break
    return z

# 测试：X=200——主族 γ1 零点——G 的特征值谱
X = 200
rho = refine(complex(0.4923, 14.1347), X)
print(f'X={X}: ζ_X 零点 ρ = {rho.real:.6f} + {rho.imag:.6f}i')
print()
print('=== G_X(s) 特征值谱（N=5——）在零点 vs 非零点 ===')
for label, s in [('零点 ρ', rho),
                  ('同γ σ=0.5', complex(0.5, rho.imag)),
                  ('同γ σ=0.45', complex(0.45, rho.imag)),
                  ('同γ σ=0.55', complex(0.55, rho.imag)),
                  ('同σ γ+5', complex(rho.real, rho.imag+5)),
                  ('随机点', complex(0.3, 7.0))]:
    G = gram_matrix(s, X, 5)
    ev = np.linalg.eigvalsh(G)  # 半正定——实特征值
    ev = np.sort(ev)[::-1]
    det = np.prod(ev)
    print(f'{label}: λ = {[f"{e:.3e}" for e in ev[:4]]}...  det = {det:.3e}  λ_min = {ev[-1]:.3e}')
