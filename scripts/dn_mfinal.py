#!/usr/bin/env python3
"""
Final chain verification: M(T)=O(1) (bounded) -> sum eps = O(1).
Use double IBP with M(T):
  sum_eps = -g_n(g1)S(g1) - int S g_n' dt
  int S g_n' dt = [M g_n'] - int M g_n'' dt   (M'=S, dM/dt=S)
  = M(t*)g_n'(t*) - M(g1)g_n'(g1) - int_{g1}^{t*} M g_n'' dt

If M is bounded (|M| <= K), then:
  |int S g_n' dt| <= K(|g_n'(t*)|+|g_n'(g1)|) + K int |g_n''| dt

Now compute: does int |g_n''| dt stay bounded as n grows? That's the crux.
g_n ~ cos(nθ)-cos((n+1)θ), θ~1/t, so g_n'' ~ n²·θ'²·cos ~ n²/t⁴ · ... 
int_{g1}^{t*} |g_n''| dt: near t~n the θ'~1/t² so n²·(1/t²)²·(stuff)...
Actually the oscillation frequency of g_n is n·θ' ~ n/t². Number of oscillations ~
integral of n/t² dt from g1 to t* ~ n(1/g1 - 1/t*) ~ n·0.07. Each oscillation
amplitude ~ 1/t ~ 1/n near t~n... this gives int|g_n''| ~ n·(1/n)·(1/n)?? unclear.

Let me just measure numerically.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def dtheta(t): return -4.0/(1+4*np.asarray(t, dtype=float)**2)
def g_n(t, n):
    th = theta(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)

def g_n_prime(t, n):
    th = theta(t); dth = dtheta(t)
    num = np.sin(n*th) + t*n*np.cos(n*th)*dth - 0.5*n*np.sin(n*th)*dth
    return (num*(0.25+t*t) - (t*np.sin(n*th)+0.5*np.cos(n*th))*2*t)/(0.25+t*t)**2

def g_n_dprime(t, n):
    # numerical derivative of g_n_prime
    h = 1e-4
    return (g_n_prime(t+h, n) - g_n_prime(t-h, n))/(2*h)

for n in [1000, 5000, 20000]:
    tstar = (n+0.5)/math.pi; g1 = z[0]
    ts = np.linspace(g1, tstar, 50000)
    gp = g_n_prime(ts, n)
    gpp = g_n_dprime(ts, n)
    I_abs = np.trapz(np.abs(gpp), ts)
    I_abs_gp = np.trapz(np.abs(gp), ts)
    print(f"n={n}: ∫|g_n''|dt = {I_abs:.4f}, ∫|g_n'|dt = {I_abs_gp:.4f}, g_n'(t*)={gp[-1]:.5f}, g_n'(g1)={gp[0]:.5f}")
