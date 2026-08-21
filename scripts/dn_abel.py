#!/usr/bin/env python3
"""
Strictification attempt via Abel summation / partial summation of S.

eps_m = int_{B_m} f~ dS.  Sum over m = int_{theta*}^{theta1} f~ dS.
IBP: sum eps = -f~(theta1) S(theta1) - int S f~' dtheta   (exact)

Key: split f~' = 2(n+1/2)cos(phi)sin(theta/2) + sin(phi)cos(theta/2)

Term A: int S(θ) sin(θ/2) cos(λθ) dθ,  λ = n+1/2  -- HIGH FREQUENCY
Term B: int S(θ) cos(θ/2) sin(λθ) dθ   -- HIGH FREQUENCY

van der Corput: if S is BV with total variation V, then
|int S g' cos(λθ)| style bounds give O(V/λ).

But V(S) ~ N(T*) ~ n log n / 2π (huge!). Need finer: use M boundedness.

Alternative: SECOND IBP using M(T) = int S:
int S(θ) cos(λθ) sin(θ/2) dθ
  = [M(θ) cos(λθ) sin(θ/2)] - int M(θ) [cos(λθ) sin(θ/2)]' dθ
  where dM/dθ = S(θ)·dt/dθ?? NO — M(t)=∫S dt, dM/dt=S, so dM/dθ = S·dt/dθ.

Hmm the Jacobian matters. Let me set things up carefully in t-coordinate instead.

In t: theta(t) decreasing. eps total = int_{t*}^{t1} g_n(t) dS(t)  (t1=gamma_1, t*=T*)
Actually g_n = f~ in theta... let me use direct t-coordinate:
g_n(t) = [t sin(nθ) + (1/2)cos(nθ)]/(1/4+t^2)
sum eps = int_{t*}^{infinity}? NO — negative region is gamma <= t*, i.e., t in [gamma_1, t*].
So sum eps = int_{gamma_1}^{t*} g_n(t) dS(t).

IBP: = [g_n S]_{gamma_1}^{t*} - int_{gamma_1}^{t*} S g_n' dt
g_n(t*) = g_n at t* = (n+1/2)/pi: sin(nθ*) + ... θ* = θ(t*) = pi/(n+1/2)... 
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*math.atan(2*t)

def g_n(t, n):
    th = theta(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)

def dtheta(t): return -4.0/(1+4*t*t)

def g_n_prime(t, n):
    th = theta(t); dth = dtheta(t)
    num = np.sin(n*th) + t*n*np.cos(n*th)*dth - 0.5*n*np.sin(n*th)*dth
    return (num*(0.25+t*t) - (t*np.sin(n*th)+0.5*np.cos(n*th))*2*t)/(0.25+t*t)**2

# Test IBP identity: int g dS vs block sum
for n in [1000]:
    th_arr = np.array([theta(g) for g in z]); phi=(n+0.5)*th_arr
    f_arr = 2*np.sin(phi)*np.sin(th_arr/2)
    mask = phi >= math.pi
    m_idx = np.floor(phi[mask]/math.pi).astype(int); Mmax=m_idx.max()
    J = np.zeros(Mmax+1)
    for i,m in enumerate(m_idx): J[m]+=f_arr[mask][i]
    Jsm = np.zeros(Mmax+1)
    for m in range(1,Mmax+1):
        xi=(m+0.5)*math.pi; Jsm[m]=(-1)**m*math.log((n+0.5)/(2*math.pi*xi))/(math.pi*xi)
    eps = J[1:]-Jsm[1:]
    direct = eps.sum()
    # IBP in t: sum eps = int_{gamma1}^{t*} g_n dS (approx via blocks of S jumps)
    # S jumps +1 at each zero. So int g dS ≈ sum_{zeros in range} g_n(gamma_k)*1 - smooth
    # Actually eps_m already = J_m - Jsm_m where J_m = sum f~(theta_k) in block.
    # sum_m J_m = sum_{neg zeros} f~(theta_k) = sum_{neg zeros} g_n(gamma_k) (telescoping? no)
    # Verify: f~(theta) = 2 sin(phi) sin(theta/2), and g_n(t) = sin(nθ) t/(1/4+t²)+...
    # f~ vs g_n: g_n(t) = sinθ sin(nθ) + (1-cosθ) cos(nθ) = cos(nθ)-cos((n+1)θ) (telescoping!)
    # f~(θ)=2sin((n+1/2)θ)sin(θ/2) = cos(nθ)-cos((n+1)θ) ✓ SAME!
    print(f"f~ == g_n verified: {np.allclose(f_arr, np.array([g_n(g,n) for g in z]), atol=1e-10)}")
    print(f"direct Σeps = {direct:+.6f}")
