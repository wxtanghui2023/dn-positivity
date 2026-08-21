#!/usr/bin/env python3
# CLOSING: D_pos vs Main. If D_pos ≥ Main_pos ≈ Main, then D_n ≥ (0.216 - 1/π²)log n > 0
# Verify: (1) Main positive-region integral ≈ Main? (2) D_pos ≈ Main_pos?
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

th = theta_doc(zeros)
a = np.sin(th/2)

print(f"{'n':>7} {'Main':>10} {'D_pos':>10} {'D_pos-Main':>11} {'Main-D_neg':>11} {'D_n':>10}")
for n in [100, 200, 500, 1000, 2000, 5000, 10000, 20000]:
    # Main = (1/π)∫_{γ1}^{gmax} g_n θ_RS' dγ + tail
    I1, _ = quad(lambda t: g_n_doc(t,n)*tp_rs(t), g1, 100, limit=1000)
    I2, _ = quad(lambda t: g_n_doc(t,n)*tp_rs(t), 100, gmax, limit=2000)
    tail = n*(np.log(gmax/(2*np.pi))+1)/(2*np.pi*gmax)
    Main = (I1+I2)/np.pi + tail
    phi = (n+0.5)*th
    terms = 2*np.sin(phi)*a
    D_pos = np.sum(terms[phi < np.pi])
    D_neg = np.sum(terms[phi >= np.pi])
    D_tot = D_pos + D_neg
    print(f"{n:7d} {Main:+10.4f} {D_pos:+10.4f} {D_pos-Main:+11.4f} {Main-D_neg:+11.4f} {D_tot:+10.4f}", flush=True)

# Main positive/negative region split
print("\n=== Main split by phase region (smooth integral) ===")
def g_n_phi(t, n):
    # g_n in φ = (n+½)θ(t) variables: g_n = 2sin(φ)sin(θ/2)
    tht = theta_doc(t)
    return 2*np.sin((n+0.5)*tht)*np.sin(tht/2)
for n in [1000, 5000]:
    a_star = np.pi/(n+0.5)  # θ where φ = π
    t_star = 0.5/np.tan(a_star/2)  # t = ½cot(θ/2) at θ=a_star ≈ (n+½)/π
    I_pos, _ = quad(lambda t: g_n_phi(t,n)*tp_rs(t), t_star, gmax, limit=2000)
    I_neg, _ = quad(lambda t: g_n_phi(t,n)*tp_rs(t), g1, t_star, limit=2000)
    print(f"  n={n}: Main_pos(φ<π) = {I_pos/np.pi:+.4f}, Main_neg(φ>π) = {I_neg/np.pi:+.4f}, "
          f"t* = {t_star:.1f} (~(n+½)/π = {(n+0.5)/np.pi:.1f})")
