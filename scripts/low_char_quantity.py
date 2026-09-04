#!/usr/bin/env python3
# Low-region characteristic-quantity analysis: A1/A2 of log-xi expansion at each low zero.
# A_k(gamma0, eps): expansion of log xi(1/2 + z0 + w), z0 = i*gamma0 + eps.
# On-line zero at gamma0: A1 ~ +1/eps (positive), A2 ~ -1/(2 eps^2).
# A1 sign flip point (scan eps) = beta0 - 1/2.
import numpy as np
import mpmath as mp
mp.mp.dps = 30

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')

def logxi_deriv1(s):
    """d/ds log xi(s) = 1/s + 1/(s-1) - 0.5 log pi + 0.5 psi(s/2) + zeta'/zeta(s)"""
    return (1/s + 1/(s-1) - 0.5*mp.log(mp.pi)
            + 0.5*mp.digamma(s/2) + mp.zeta(s, derivative=1)/mp.zeta(s))

def logxi_deriv2(s):
    """d^2/ds^2 log xi(s) = -1/s^2 - 1/(s-1)^2 + 0.25 psi'(s/2) + [zeta''/zeta - (zeta'/zeta)^2]"""
    z = mp.zeta(s)
    z1 = mp.zeta(s, derivative=1)
    z2 = mp.zeta(s, derivative=2)
    return (-1/s**2 - 1/(s-1)**2 + 0.25*mp.digamma(s/2, derivative=1)
            + z2/z - (z1/z)**2)

# A_k in expansion log xi(1/2+z0+w) = sum A_k w^k : A1 = deriv1, A2 = deriv2/2
print(f"{'k':>3} {'gamma_k':>10} {'eps':>6} {'Re(A1)*eps':>12} {'Im(A1)*eps':>12} {'Re(A2)*eps^2':>14}  (on-line: ReA1*eps~1)")
for k in range(30):
    gamma = zeros[k]
    eps = 0.01
    s0 = 0.5 + 1j*gamma + eps
    A1 = logxi_deriv1(s0)
    A2 = logxi_deriv2(s0)/2
    a1e = float(mp.re(A1)*eps)
    a1i = float(mp.im(A1)*eps)
    a2e = float(mp.re(A2)*eps**2)
    flag = ""
    if a1e < 0.5:  # suspicious: A1 not ~ +1/eps
        flag = "  <-- CHECK (A1 not positive-dominant)"
    print(f"{k+1:>3} {gamma:>10.4f} {eps:>6.3f} {a1e:>12.4f} {a1i:>12.4f} {a2e:>14.4f}{flag}")

# eps-scan for first zero: A1 sign flip would be at eps = beta-1/2; on-line => always positive
print(f"\n=== eps-scan gamma1 (on-line => Re A1>0 for all eps>0) ===")
g1 = zeros[0]
for eps in [0.5, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002]:
    s0 = 0.5 + 1j*g1 + eps
    A1 = logxi_deriv1(s0)
    print(f"  eps={eps:.3f}: Re A1 = {float(mp.re(A1)):+.4f}  Im A1 = {float(mp.im(A1)):+.2e}  (ReA1*eps = {float(mp.re(A1)*eps):+.4f})")
