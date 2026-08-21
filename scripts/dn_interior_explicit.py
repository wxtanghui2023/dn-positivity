#!/usr/bin/env python3
"""
The interior term is EXPLICIT (no S!):
S'(t) = -theta_RS'(t)/pi between zeros (N(t) constant between zeros).
So interior = int phi sinphi * S'(t) dt/dphi dphi
            = -int phi sinphi * (theta_RS'(t)/pi) * (dt/dphi) dphi

dt/dphi = 1/phi' = 1/((n+1/2)theta'(t)). theta' = -4/(1+4t^2).
So interior = -int phi sinphi * (theta_RS'(t)/pi) / ((n+1/2)theta'(t)) dphi
            = -(1/(n+1/2)) int phi sinphi * (theta_RS'(t)/theta'(t)) / pi dphi

theta_RS'(t)/theta'(t): theta_RS' ~ (1/2)log(t/2pi), theta' ~ -1/t^2 (large t)
  => ratio ~ -(1/2)t^2 log(t/2pi). phi ~ n/t (since theta~1/t => phi=(n+1/2)theta ~ n/t)
  => integrand phi sinphi * ratio ~ (n/t)*sinphi*(1/2)t^2 log ~ (n t / 2) sinphi log(t/2pi)
  hmm that's large. BUT sinphi oscillates! phi from pi to ~0.07n.

KEY: this is now an EXPLICIT oscillatory integral (no S!):
  interior/n = -(1/(n+1/2)^2) int_{pi}^{phi_max} phi sinphi (theta_RS'(t)/theta'(t))/pi dphi
Verify numerically, then apply van der Corput to the explicit integrand.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def dtheta(t): return -4.0/(1+4*np.asarray(t, dtype=float)**2)
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def dtheta_RS(t):
    # theta_RS'(t) = Re psi(1/4 + it/2)/2 - (1/2)log(pi)
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.re(mp.digamma(mp.mpc(0.25, t/2)))/2 - mp.log(mp.pi)/2)
def t_of_phi(phi, n):
    th = phi/(n+0.5)
    return 0.5/np.tan(th/2)

print("验证: interior(数值, 用S') vs interior(显式, 用theta_RS'/theta')")
for n in [1000, 5000, 10000]:
    g1 = z[0]; phi_max = (n+0.5)*theta(g1); tstar = (n+0.5)/math.pi
    # numeric interior via S'
    zz = z[(z >= g1) & (z <= tstar)]
    phi_zeros = (n+0.5)*theta(zz)
    edges = np.concatenate([[phi_max], phi_zeros, [math.pi]])
    J = 0.0
    for i in range(len(edges)-1):
        a, b = edges[i], edges[i+1]
        if abs(a-b) < 1e-10: continue
        Smid = S = None
        # S'(t) = -theta_RS'/pi in this interval (no zeros inside)
        mid = t_of_phi(0.5*(a+b), n)
        Sp = -dtheta_RS(mid)/math.pi
        phs = np.linspace(b, a, 300)
        ts = t_of_phi(phs, n)
        dt_dphi = 1.0/((n+0.5)*dtheta(ts))
        J += np.trapz(phs*np.sin(phs)*Sp*dt_dphi, phs)
    interior_num = J  # int phi sinphi S' dt/dphi dphi  (unnormalized)
    # explicit version: S' replaced by -theta_RS'/pi, same thing... 
    # Actually interior_num IS the explicit version. Compare with direct:
    # int phi sinphi * (-theta_RS'(t)/pi) * dt/dphi dphi = same. OK it's the same.
    # Now check: interior/(n+0.5) vs previous I_total - bdry
    print(f"n={n}: interior_un = {interior_num:+.5f}, /n = {interior_num/(n+0.5):+.6f}")
    # van der Corput target: |interior| = |int phi sinphi Sp dt/dphi dphi| 
    # Sp = -theta_RS'/pi ~ -(1/2pi)log(t/2pi), dt/dphi ~ -t^2/n
    # integrand ~ phi sinphi * (1/2pi)log(t/2pi) * t^2/n, t ~ n/phi
    # ~ phi sinphi * log(n/phi) * n/(2pi phi^2) = sinphi log(n/phi) n/(2pi phi)
    # int |sinphi| log(n/phi)/phi dphi ~ (2/pi) * (1/2)(log(n/pi))^2 ~ (log n)^2/pi  [!!]
    # so |interior| <= (n/(2pi)) * (1/pi)(log n)^2 / ... wait need to redo carefully
    # integrand magnitude: (n/(2pi)) * |sinphi| log(n/phi)/phi
    # int_{pi}^{0.07n} |sinphi| log(n/phi)/phi dphi: |sinphi| avg 2/pi, log(n/phi)/phi
    # ~ (2/pi) int log(n/phi)/phi dphi = (2/pi)(1/2)(log n - log pi)^2 ~ (log n)^2/pi
    # So |interior| <= (n/2pi)*(log n)^2/pi * (n/(n+1/2))... no wait
    # interior = -(1/(n+1/2)) int phi sinphi (theta_RS'/theta')/pi dphi  -- need consistent form
    # From dt/dphi = 1/((n+1/2)theta'), theta_RS'/theta' ~ -(1/2)t^2 log(t/2pi):
    # interior = -(1/(n+1/2)) int phi sinphi (theta_RS'/theta')/pi dphi
    #          = -(1/(n+1/2)) int phi sinphi * (-(1/2)t^2 log(t/2pi))/pi dphi
    #          = (1/(2pi(n+1/2))) int phi sinphi t^2 log(t/2pi) dphi,  t ~ n/phi
    #          = (1/(2pi(n+1/2))) int phi sinphi (n/phi)^2 log(n/(2pi phi)) dphi
    #          = (n^2/(2pi(n+1/2))) int sinphi log(n/(2pi phi))/phi dphi
    # |int sinphi log(n/phi)/phi dphi| <= int |sinphi| log(n/phi)/phi dphi ~ (log n)^2/pi
    # |interior| <= n^2/(2pi n) * (log n)^2/pi = n (log n)^2/(2pi^2) -- DIVERGES with n!!
    # This can't be right numerically (interior/n ~ 0.03 bounded). The |sinphi| bound is too crude;
    # sinphi oscillates so int sinphi log(n/phi)/phi dphi is actually O(1) (oscillatory),
    # not O((log n)^2). Van der Corput with phase phi: d/dphi[log(n/phi)/phi] ~ bounded...
    print(f"   检查: sinphi 振荡积分 int sinphi log(n/phi)/phi dphi 实际值:")
    phs = np.linspace(math.pi, 0.07*n, 200000)
    v = np.trapz(np.sin(phs)*np.log(n/0.0+1e-30)/(phs+1e-30), phs) if False else None
    phs = np.linspace(math.pi, 0.07*n, 200000)
    kern = np.log(n/np.maximum(phs,1e-9))/np.maximum(phs,1e-9)
    v = np.trapz(np.sin(phs)*kern, phs)
    print(f"   int sinphi log(n/phi)/phi dphi = {v:+.4f}  (log n = {math.log(n):.2f})")
