#!/usr/bin/env python3
"""
RH => strong PNT: verify |psi(x) - x| = O(sqrt(x) log^2 x) numerically.

Explicit formula: psi(x) = x - sum_rho x^rho/rho - log(2pi) - (1/2)log(1-x^-2)
With RH (rho = 1/2 + i gamma): x^rho = sqrt(x) e^{i gamma log x}
Error term = sqrt(x) * |sum_rho e^{i gamma log x}/rho|

Check: (1) psi(x) - x vs sqrt(x) log^2 x
       (2) the zero sum factor |sum e^{i gamma t}/rho| is bounded (O(log^2 x)?)
Use zeros from Odlyzko data + mpmath for psi computation.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
print(f"zeros loaded: {len(z)}")

def psi_zeros(x, N):
    """psi(x) via explicit formula with first N zeros (non-trivial, on 1/2 line under RH)."""
    s = x  # main term
    for k in range(N):
        g = z[k]
        rho = 0.5 + 1j*g
        s -= x**rho/rho  # both conjugates? x^rho + x^(1-rho): for x real, x^(1/2-ig)/ (1/2-ig) is conj
        s -= x**(1-rho)/(1-rho)
    s -= math.log(2*math.pi)
    s -= 0.5*math.log(1-x**(-2))
    return s.real

def psi_true(x):
    """psi(x) = sum_{p^k <= x} log p (Chebyshev psi)."""
    # compute via sieve of primes up to x
    # simple: sum over prime powers
    total = 0.0
    # sieve primes up to x
    n = int(x)
    bs = bytearray(b'\x01')*(n+1); bs[0:2]=b'\x00\x00'
    for i in range(2,int(n**0.5)+1):
        if bs[i]: bs[i*i:n+1:i]=b'\x00'*(((n-i*i)//i)+1)
    for p in range(2, n+1):
        if bs[p]:
            pk = p
            while pk <= n:
                total += math.log(p)
                pk *= p
    return total

# Verify psi via explicit formula vs true
print("\n=== psi(x) 显式公式 vs 真值 ===")
for x in [100, 500, 1000]:
    N = min(len(z), 2000)
    psi_e = psi_zeros(x, N)
    psi_t = psi_true(x)
    print(f"  x={x}: psi_formula={psi_e:.2f}, psi_true={psi_t:.2f}, 差={abs(psi_e-psi_t):.3f}")

# Main: |psi(x)-x| vs sqrt(x) log^2 x
print("\n=== |psi(x)-x| vs sqrt(x)log^2x ===")
print(f"{'x':>8} {'|psi-x|':>12} {'sqrt(x)log²x':>14} {'比值':>8}")
for x in [100, 500, 1000, 5000, 10000, 50000]:
    N = min(len(z), 5000)
    psi_e = psi_zeros(x, N)
    err = abs(psi_e - x)
    bd = math.sqrt(x)*math.log(x)**2
    print(f"{x:8d} {err:12.3f} {bd:14.3f} {err/bd:8.4f}")
