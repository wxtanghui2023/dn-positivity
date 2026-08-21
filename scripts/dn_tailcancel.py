#!/usr/bin/env python3
# Decisive: the "divergent" sum tail is cancelled by the integral tail.
# Show:  Σ_{γ>n} sinc(γ/n) ~ large (O(n log n) smooth part)
#        (1/π)∫_n^∞ θ'(t)sinc(t/n)dt ~ same large part
#        difference (the C(n) tail) is SMALL (~O(1))
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4)
def theta_prime_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)
def sinc(x):
    return np.where(x==0, 1.0, np.sin(x)/x)

print(f"{'n':>6} {'Σ_{γ>n} sinc':>14} {'(1/π)∫_n^∞θsinc':>16} {'差值(tail)':>12} {'理论O(nlogn)':>12}")
for n in [50, 100, 200, 500, 1000, 2000, 3000]:
    mask = zeros > n
    s_tail = np.sum(sinc(zeros[mask]/n))          # sum over γ in (n, 74921]
    # integral from n to gmax (θ' via mpmath near n, asy above 50)
    I1, _ = integrate.quad(lambda t: theta_prime_mp(t)*sinc(t/n), n, max(n+1,50.0), limit=200)
    tg = np.arange(max(n+1,50.0), gmax, 0.5)
    I2 = np.trapz(theta_prime_asy(tg)*sinc(tg/n), tg)
    I_tail = (I1+I2)/np.pi
    diff = s_tail - I_tail
    print(f"{n:6d} {s_tail:+14.4f} {I_tail:+16.4f} {diff:+12.4f} {0.1*n*np.log(n):12.1f}", flush=True)
