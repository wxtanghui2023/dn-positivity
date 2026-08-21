#!/usr/bin/env python3
# Split Main = (1/π)∫_{γ1}^n g_n θ_RS'dγ + (1/π)∫_n^∞ g_n θ_RS'dγ
# Verify: tail part ≈ (log n)/(2π)? main part (γ<n) = O(1)?
import numpy as np
from scipy.integrate import quad
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
def g_n_doc(t, n):
    th = theta_doc(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)
def tp_rs(t):
    t = float(t)
    if t < 50:
        z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
        return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4)

print(f"{'n':>7} {'Main_<n':>10} {'Main_>n':>10} {'total':>10} {'log n/2π':>10}")
for n in [100, 200, 500, 1000, 2000, 5000, 10000]:
    # γ < n part
    I1, _ = quad(lambda t: g_n_doc(t,n)*tp_rs(t), g1, min(n, gmax-1), limit=3000)
    # γ > n part (up to gmax + tail)
    I2, _ = quad(lambda t: g_n_doc(t,n)*tp_rs(t), n, gmax, limit=3000)
    tail = (2*n+1)*(np.log(gmax/(2*np.pi))+1)/(4*np.pi*gmax)  # g_n≈(2n+1)/(2γ²) for γ>gmax
    total = (I1+I2)/np.pi + tail
    print(f"{n:7d} {I1/np.pi:+10.4f} {(I2/np.pi+tail):+10.4f} {total:+10.4f} {np.log(n)/(2*np.pi):10.4f}")
