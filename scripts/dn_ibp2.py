#!/usr/bin/env python3
"""
Double IBP attempt: express sum eps in terms of M(T) = int S dt (bounded, ~O(1)).

sum_eps = int_{gamma_1}^{t*} g_n(t) dS(t)   [t-coordinate, t* = (n+1/2)/pi]

IBP #1: = [g_n S]_{g1}^{t*} - int_{g1}^{t*} S g_n' dt
       = -g_n(g1) S(g1) - int S g_n' dt          (g_n(t*)=0? check: g_n(t*)=cos(nθ*)-cos((n+1)θ*), θ*=π/(n+½)... sin(nπ/(n+½))... NOT zero!)

Let me just numerically evaluate each piece and see which dominates,
then figure out the right analytic bound.

Key estimate targets:
- |g_n(g1) S(g1)|: S(g1) ~ O(1) bounded, g_n(g1) ~ O(1/n)? g_n ~ sin(nθ)/t ~ ... small
- |int S g_n' dt|: g_n' has oscillatory part; S bounded by C log t
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def g_n(t, n):
    th = theta(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)
def dtheta(t): return -4.0/(1+4*t*t)
def g_n_prime(t, n):
    th = theta(t); dth = dtheta(t)
    num = np.sin(n*th) + t*n*np.cos(n*th)*dth - 0.5*n*np.sin(n*th)*dth
    return (num*(0.25+t*t) - (t*np.sin(n*th)+0.5*np.cos(n*th))*2*t)/(0.25+t*t)**2

def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 20
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))

for n in [1000, 5000]:
    tstar = (n+0.5)/math.pi
    g1 = z[0]
    # S(g1), S(tstar)
    S_g1 = 1 - theta_RS(g1)/math.pi - 1  # N=1 at g1? N(g1)=1 (first zero inclusive)
    N_tstar = np.searchsorted(z, tstar, side='right')
    S_tstar = N_tstar - theta_RS(tstar)/math.pi - 1
    # g_n at endpoints
    gn_g1 = g_n(g1, n); gn_tstar = g_n(tstar, n)
    print(f"\nn={n}: t*={tstar:.1f}, 负区零点数 N(t*)={N_tstar}")
    print(f"  S(g1)={S_g1:+.4f}, S(t*)={S_tstar:+.4f}")
    print(f"  g_n(g1)={gn_g1:+.6f}, g_n(t*)={gn_tstar:+.6f}")
    print(f"  |g_n(g1)·S(g1)| = {abs(gn_g1*S_g1):.6f}")
    # int S g_n' dt numerically on grid [g1, t*]
    ts = np.linspace(g1, tstar, 200000)
    Ss = np.array([np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1 for t in ts])
    gp = g_n_prime(ts, n)
    I = np.trapz(Ss*gp, ts)
    # decompose: gp = high_freq_part + low
    th = theta(ts)
    hi = np.cos((n+0.5)*th)*np.sin(th/2)*2*(n+0.5)  # ~ dominant high freq
    lo = gp - hi
    Ihi = np.trapz(Ss*hi, ts); Ilo = np.trapz(Ss*lo, ts)
    print(f"  ∫S g_n' dt = {I:+.6f}  (high-freq part {Ihi:+.6f}, low {Ilo:+.6f})")
    print(f"  IBP: sum_eps ≈ -g_n(g1)S(g1) - ∫Sg_n' = {-gn_g1*S_g1 - I:+.6f}")
