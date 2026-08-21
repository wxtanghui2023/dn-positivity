#!/usr/bin/env python3
"""
Analytic Main_pos constant. Main_pos = (1/pi) int_{t*}^inf f(t) theta_RS'(t) dt
u = (n+1/2)theta(t) substitution: t = (n+1/2)/u roughly (theta ~ 1/t)
theta_RS'(t) = (1/2)log(t/2pi) - 1/(12t^2) + O(1/t^4)
f = 2 sin(u) sin(theta/2), dt = -t^2/(n+1/2) du  [since dtheta/du = 1/(n+1/2), theta'=dtheta/dt]
Let me do the substitution EXACTLY numerically to find the constant, avoiding the
tail problem by integrating to large T with EXACT f and theta_RS' and subtracting
the known asymptotic.

Actually better: compute Main_pos(t*) EXACTLY for the true theta(t) (not 1/t approx)
and compare with c log n + C0 to nail C0.
"""
import numpy as np, math
import mpmath as mp
mp.mp.dps = 20

def theta(t): return math.pi - 2*math.atan(2*t)
def dtheta(t): return -4.0/(1+4*t*t)
def theta_RS(t):
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def dtheta_RS(t):
    return float(mp.re(mp.digamma(mp.mpc(0.25, t/2)))/2 - mp.log(mp.pi)/2)

# Use u = (n+1/2)theta as variable: from u=0 (t=inf) to u=pi (t=t*)
# Main_pos = (1/pi) int f theta_RS' dt, dt = du/((n+1/2)theta')
# f = 2 sin u sin(theta/2), theta = u/(n+1/2)
# So Main_pos = (1/pi) int_0^pi 2 sin(u) sin(u/(2(n+1/2))) theta_RS'(t(u)) / ((n+1/2) theta'(t(u))) du
c = 0.294744936
for n in [500, 1000, 5000, 10000, 50000]:
    n12 = n + 0.5
    us = np.linspace(1e-8, math.pi, 20000)
    ths = us/n12
    ts = 0.5/np.tan(ths/2)   # exact inverse of theta
    dtrs = np.array([dtheta_RS(t) for t in ts])
    dth = np.array([dtheta(t) for t in ts])
    integrand = 2*np.sin(us)*np.sin(ths/2)*dtrs/(n12*dth)
    Mp = np.trapz(integrand, us)/math.pi
    C_meas = Mp - c*math.log(n)
    print(f"n={n:6d}: Main_pos={Mp:10.5f}, c·logn={c*math.log(n):9.5f}, C_meas={C_meas:+.5f}")
