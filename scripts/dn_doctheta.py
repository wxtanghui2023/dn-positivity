#!/usr/bin/env python3
# Decisive experiment with the DOCUMENT's theta: θ(t) = π - 2·arctan(2t)
# g_n(t) = sin(nθ(t))/t ;  D_n = Σ_γ g_n(γ) - (1/π)∫_0^T θ'(t) g_n(t) dt
import numpy as np
from scipy import integrate

zeros = np.load('/tmp/zeros_2000.npy')
T_max = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)

def theta_doc_prime(t):
    return -4.0/(1.0 + 4.0*t*t)

def g_n(t, n):
    return np.sin(n*theta_doc(t))/t

# check the comment: θ(γ) ≈ 1/γ
print("theta_doc(14.1347) = %.6f  vs 1/γ = %.6f" % (theta_doc(14.1347), 1/14.1347))
print("theta_doc(2515.3)  = %.6f  vs 1/γ = %.6f" % (theta_doc(2515.3), 1/2515.3))

# analytic: (1/π)∫_0^∞ θ' g_n dt = 2·(-1)^n  (derived from substitution θ=π-2atan(2t), t=½cot(θ/2))
print("\nCheck analytic integral (1/π)∫θ'g_n = 2(-1)^n:")
for n in [1,2,3,10]:
    I, _ = integrate.quad(lambda t: theta_doc_prime(t)*g_n(t,n), 0.0, T_max, limit=2000)
    print(f"  n={n:2d}: numeric (1/π)I = {I/np.pi:+.8f}   analytic 2(-1)^n = {2*(-1)**n:+.8f}")

print("\n=== DOCUMENT θ: D_n = Σg_n(γ) - (1/π)∫θ'g_n ===")
print(f"{'n':>6} {'Σg_n(γ)':>14} {'-(1/π)∫θg':>14} {'D_n':>14} {'n·D_n':>12}")
for n in [10,20,30,40,50,60,80,100,200,300,500,700,1000,1500,2000]:
    s = sum(g_n(float(z), n) for z in zeros)
    I, eI = integrate.quad(lambda t: theta_doc_prime(t)*g_n(t,n), 0.0, T_max, limit=2000)
    ti = I/np.pi
    D = s - ti
    print(f"{n:6d} {s:+14.6f} {-ti:+14.6f} {D:+14.6f} {n*D:+12.2f}   (err {eI:.1e})", flush=True)
