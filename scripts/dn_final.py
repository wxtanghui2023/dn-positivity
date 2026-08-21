#!/usr/bin/env python3
# FINAL CLOSING: verify Main_pos asymptotics precisely
# Main_pos ≈ (1/2π)[Si(π)·log((n+½)/2π) - C₁], C₁ = ∫₀^π sin(u)log(u)/u du
# Then D_n = Main_pos + D_neg ≥ c₁·log n - (log n)/π² with c₁ = Si(π)/(2π) ≈ 0.2947
import numpy as np
from scipy.integrate import quad
from scipy.special import sici
import mpmath as mp
mp.mp.dps = 20

# exact constants
Si_pi, Ci_pi = sici(np.pi)
print(f"Si(π) = {Si_pi:.6f}")
C1, _ = quad(lambda u: np.sin(u)*np.log(u)/u, 1e-12, np.pi, limit=500)
print(f"C₁ = ∫₀^π sin(u)log(u)/u du = {C1:.6f}")
c_asy = Si_pi/(2*np.pi)
print(f"asymptotic coefficient c = Si(π)/(2π) = {c_asy:.6f}")
print(f"1/π² = {1/np.pi**2:.6f}")
print(f"margin: c - 1/π² = {c_asy - 1/np.pi**2:.6f} > 0 ✓\n")

# verify Main_pos against asymptotic formula
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

print(f"{'n':>7} {'Main_pos':>10} {'asy: c·log n':>14} {'D_neg':>10} {'Main_pos+D_neg':>14} {'margin/log':>11}")
for n in [100, 200, 500, 1000, 2000, 5000, 10000, 20000]:
    t_star = (n+0.5)/np.pi
    I_pos, _ = quad(lambda t: g_n_doc(t,n)*tp_rs(t), t_star, gmax, limit=2000)
    Main_pos = I_pos/np.pi
    asy = c_asy*np.log(n) - c_asy*np.log(2*np.pi) + 0  # log((n+½)/2π) ≈ log n - log 2π
    # D_neg from sum
    th = theta_doc(zeros)
    a = np.sin(th/2)
    phi = (n+0.5)*th
    terms = 2*np.sin(phi)*a
    D_neg = np.sum(terms[phi >= np.pi])
    D_tot = Main_pos + D_neg
    print(f"{n:7d} {Main_pos:+10.4f} {asy:+14.4f} {D_neg:+10.4f} {D_tot:+14.4f} {(Main_pos-abs(D_neg))/np.log(n):11.4f}")

# final: D_n vs Main_pos + D_neg (should equal D_n exactly)
print("\n=== consistency: D_n = Main_pos + D_neg ===")
for n in [500, 2000]:
    th = theta_doc(zeros)
    a = np.sin(th/2)
    phi = (n+0.5)*th
    terms = 2*np.sin(phi)*a
    D_direct = np.sum(terms)
    t_star = (n+0.5)/np.pi
    I_pos, _ = quad(lambda t: g_n_doc(t,n)*tp_rs(t), t_star, gmax, limit=2000)
    Main_pos = I_pos/np.pi
    D_neg = np.sum(terms[phi >= np.pi])
    print(f"  n={n}: D_direct={D_direct:+.4f}  Main_pos+D_neg={Main_pos+D_neg:+.4f}  diff={D_direct-(Main_pos+D_neg):+.4f}")
