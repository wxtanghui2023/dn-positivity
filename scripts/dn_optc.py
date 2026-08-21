#!/usr/bin/env python3
# Option C experiment: normalized test functions g_n(t) = (1/n)·h(t/n)
# Then D_n = ∫g_n dS = Σg_n(γ) - (1/π)∫θ'g_n = -∫S g_n'  (integration by parts)
# |S(t)| = O(log t)  =>  |D_n| ≤ ∫|S||g_n'| ~ O(log n / n)  =>  n·D_n = O(log n), NOT linear
import mpmath as mp
import numpy as np
from scipy import integrate
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_2000.npy')
T_max = float(zeros[-1])

def theta_cont(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))

def theta_prime(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)

def g_sinc(t, n):      # h(x)=sin x / x  -> g_n(t) = sin(t/n)/t
    return np.sin(t/n)/t
def g_sinc2(t, n):     # h(x)=(sin x/x)^2 -> g_n(t) = n·sin²(t/n)/t²
    x = t/n
    return n*(np.sin(x)/x)**2

def compute(h_type, ns):
    print(f"\n=== g_n = (1/n)·h(t/n), h = {h_type} ===")
    print(f"{'n':>6} {'Σg_n(γ)':>14} {'-(1/π)∫θg':>14} {'D_n':>14} {'n·D_n':>12}")
    for n in ns:
        g = g_sinc if h_type=='sinc' else g_sinc2
        s = sum(g(float(z), n) for z in zeros)
        I, eI = integrate.quad(lambda t: theta_prime(t)*g(t, n), 0.0, T_max, limit=2000)
        ti = I/np.pi
        D = s - ti
        print(f"{n:6d} {s:+14.8f} {-ti:+14.8f} {D:+14.8f} {n*D:+12.6f}   (int err {eI:.1e})", flush=True)

compute('sinc',  [10,20,50,100,200,500,1000,2000])
compute('sinc2', [10,20,50,100,200,500,1000,2000])
