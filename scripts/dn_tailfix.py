#!/usr/bin/env python3
# Add truncation tail correction: n·D_n(true) = n·D_n(truncated) + tail
# tail = Σ_{γ>γmax} sinc(γ/n) - (1/π)∫_{γmax}^∞ θ'sinc dt ≈ -sinc(γmax/n)·S(γmax) + O(1/γmax)
# (integration by parts on ∫_{γmax}^∞ sinc dS)
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_asy(t):
    return 0.5*t*np.log(t/(2*np.pi)) - 0.5*t - np.pi/8 + 1/(48*t) + 7/(5760*t**3) + 31/(80640*t**5)
def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4) - 31/(16128*t**6)
def theta_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))
def theta_prime_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)
def sinc(x):
    return np.where(x==0, 1.0, np.sin(x)/x)

STEP = 0.25
tg = np.arange(0.0, gmax, STEP)
tp = np.zeros_like(tg)
small = tg < 50
for i in np.nonzero(small)[0]:
    tp[i] = theta_prime_mp(float(tg[i]))
tp[~small] = theta_prime_asy(tg[~small])

def ndn_trunc(n):
    return np.sum(sinc(zeros/n)) - np.trapz(tp*sinc(tg/n), tg)/np.pi

# S(γmax) = 100000 - θ(γmax)/π - 1
Sgmax = 100000 - theta_mp(gmax)/np.pi - 1.0
print(f"S(γmax) = {Sgmax:+.4f}")

print(f"\n{'n':>7} {'n·D_trunc':>10} {'tail≈-sinc·S':>14} {'n·D_corr':>10}")
for n in [5000, 8000, 10000, 15000, 20000, 30000, 40000, 50000, 60000]:
    v = ndn_trunc(n)
    # tail correction: ∫_{γmax}^∞ sinc(t/n)dS ≈ -sinc(γmax/n)S(γmax) - ∫ S·sinc'(t/n)/n dt (≈ -sinc·S for γmax>>n)
    corr = -sinc(gmax/n)*Sgmax
    print(f"{n:7d} {v:+10.4f} {corr:+14.4f} {v+corr:+10.4f}")
