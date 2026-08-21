#!/usr/bin/env python3
"""
Strictification of I = (1/(n+1/2)) * int_{pi}^{phi_max} [phi cosphi + sinphi] S(t(phi)) dphi

KEY: I has factor 1/n. Need: |int [phi cosphi + sinphi] S(t(phi)) dphi| <= C * n * log n
(so that |I| <= C log n, and we need C < 0.1934... but actually even C~1 gives O(log n)
which combined with E=O(1) might work if the Leibniz main term margin holds).

The kernel K(phi) = phi cosphi + sinphi. Observe: d/dphi[phi sinphi] = sinphi + phi cosphi = K(phi)!
So int K(phi) S(t(phi)) dphi = int d/dphi[phi sinphi] S(t(phi)) dphi
= [phi sinphi S(t(phi))] - int phi sinphi * d/dphi[S(t(phi))] dphi   (IBP)

Boundary: phi_max sin(phi_max) S(t(phi_max)) - pi*sin(pi)*S(t(pi)) = phi_max sin(phi_max) S(gamma1)
  |...| <= phi_max * |S(gamma1)| ~ (0.07n)*0.55 ~ 0.04n  -- O(n), divided by n -> O(1) OK!
Interior: int phi sinphi * S'(t) dt/dphi dphi. |S'(t)| is bounded between zeros...
  S'(t) = d/dt[N - theta_RS/pi - 1] = -theta_RS'(t)/pi between zeros (N constant!)
  = -(1/2pi)log(t/2pi) - O(1/t^2)... 
  So interior = -int phi sinphi * (theta_RS'(t)/pi) * dt/dphi dphi
  dt/dphi = 1/phi' = 1/((n+1/2)theta'(t)) ~ -t^2/n
  |interior| <= int |phi sinphi| * (1/2pi)log(t/2pi) * t^2/n dphi ~ (1/n) int phi * log(phi/n)... 
  hmm let me just verify numerically the IBP split.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1
def t_of_phi(phi, n):
    th = phi/(n+0.5)
    return 0.5/np.tan(th/2)

print("IBP decomposition of interior integral (in phi-coord):")
print("n        |boundary phi_max sin S|/n   |interior int phi sinphi S'|/n   I_total")
for n in [1000, 5000, 10000, 20000]:
    g1 = z[0]; phi_max = (n+0.5)*theta(g1); tstar = (n+0.5)/math.pi
    # IBP boundary
    bdry = phi_max*math.sin(phi_max)*S_of_t(g1)/(n+0.5)
    # interior via direct: int phi sinphi * S'(t) * dt/dphi dphi  (S'=-theta_RS'/pi between zeros)
    # better: compute interior = I_total_unnorm - bdry_unnorm where I_total_unnorm = int K S dphi
    zz = z[(z >= g1) & (z <= tstar)]
    phi_zeros = (n+0.5)*theta(zz)
    edges = np.concatenate([[phi_max], phi_zeros, [math.pi]])
    J = 0.0  # int K(phi) S dphi
    for i in range(len(edges)-1):
        a, b = edges[i], edges[i+1]
        if abs(a-b) < 1e-10: continue
        Smid = S_of_t(t_of_phi(0.5*(a+b), n))
        phs = np.linspace(b, a, 300)
        J += np.trapz((phs*np.cos(phs)+np.sin(phs))*Smid, phs)
    bdry_un = phi_max*math.sin(phi_max)*S_of_t(g1)  # - pi*sin(pi)*S = 0
    interior_un = J - bdry_un
    print(f"{n:7d}  {abs(bdry)/1:12.6f}  {abs(interior_un)/(n+0.5):12.6f}  {J/(n+0.5):+10.6f}")
    print(f"         (bdry/n={bdry_un/(n+0.5):+.6f}, interior/n={interior_un/(n+0.5):+.6f})")
