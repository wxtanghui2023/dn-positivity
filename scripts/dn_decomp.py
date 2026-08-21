#!/usr/bin/env python3
# Exact decomposition of n·D_n to locate the "1":
# n·D_n = Σ_γ sinc(γ/n) - (1/π)∫₀^∞ θ'(t)sinc(t/n)dt
# Using N(T) = (1/π)θ(T) + 1 + S(T), split at first zero γ₁:
#   Σ_γ sinc(γ/n) = (1/π)∫_{γ₁}^∞ θ'sinc dt - sinc(γ₁/n) + ∫_{γ₁}^∞ sinc dS
#   (Stieltjes: ∫ f dN = ∫ f d[θ/π] + ∫ f d[1] + ∫ f dS; the d[1] term = -f(γ₁) boundary... careful)
# So:  n·D_n = -(1/π)∫₀^{γ₁} θ'(t)sinc(t/n)dt - sinc(γ₁/n) + ∫_{γ₁}^∞ sinc(t/n)dS(t)
# Verify numerically: each piece + compare to n·D_n from direct computation.
import mpmath as mp
import numpy as np
from scipy import integrate
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
g1 = float(zeros[0])

def theta_cont(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))

def theta_prime(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)

def sinc(x):
    return np.sin(x)/x if x != 0 else 1.0

def S_of_T(T):
    N = int(np.searchsorted(zeros, T, side='right'))
    return N - theta_cont(T)/np.pi - 1.0

ns = [20, 100, 500, 2000]
print(f"{'n':>6} {'n·D_n(direct)':>14} {'pieceA':>12} {'pieceB':>12} {'pieceC':>12} {'sum':>12}")
for n in ns:
    # piece A: -(1/π)∫₀^{γ₁} θ'(t)sinc(t/n)dt
    A, _ = integrate.quad(lambda t: theta_prime(t)*sinc(t/n), 0.0, g1, limit=500)
    A = -A/np.pi
    # piece B: -sinc(γ₁/n)
    B = -sinc(g1/n)
    # piece C: ∫_{γ₁}^∞ sinc(t/n)dS(t)  -- S jumps +1 at each zero; between zeros S is smooth.
    # Split: C = Σ_{γ≥γ₁} sinc(γ/n)·1 (jumps) + ∫_{γ₁}^∞ sinc(t/n)·S_smooth'(t)dt
    # But S_smooth' = (1/π)Re(ζ'/ζ)(1/2+it)-ish... instead use: dS = dN - (1/π)θ'dt - d[1]... 
    # Simpler: C = Σ_γ sinc(γ/n) - (1/π)∫_{γ₁}^∞ θ'sinc dt - [-sinc(γ₁/n)]  (from N=θ/π+1+S)
    # i.e. C = [Σ_γ sinc(γ/n) - (1/π)∫_{γ₁}^∞ θ'sinc dt + sinc(γ₁/n)]
    Ssum = sum(sinc(float(z)/n) for z in zeros)
    Ib, _ = integrate.quad(lambda t: theta_prime(t)*sinc(t/n), g1, float(zeros[-1]), limit=2000)
    C = Ssum - Ib/np.pi + sinc(g1/n)
    # direct n·D_n
    s = sum(sinc(float(z)/n) for z in zeros)
    I, _ = integrate.quad(lambda t: theta_prime(t)*sinc(t/n), 0.0, float(zeros[-1]), limit=2000)
    ndn = s - I/np.pi
    print(f"{n:6d} {ndn:+14.6f} {A:+12.6f} {B:+12.6f} {C:+12.6f} {A+B+C:+12.6f}", flush=True)

# also: check piece A asymptotics as n large: A -> -θ(γ₁)/π ≈ +0.550
print(f"\nθ(γ₁)/π = {theta_cont(g1)/np.pi:+.4f}  -> piece A limit ≈ {-theta_cont(g1)/np.pi:+.4f}")
print(f"piece B limit (n→∞) = -1")
