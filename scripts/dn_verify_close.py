#!/usr/bin/env python3
"""
Verify the closing bound actually HOLDS for small n (43, 44, 50, 100):
D_n >= 0.294745 log n - 0.456 - g(xi1) - 0.0389 - g(pi)/pi
Check ALL the inequalities that feed into this:
1. Main_pos >= c log n + C0 - small: verify Main_pos numerically vs c log n - 0.456
2. |Leibniz| <= g(xi1): verify sum_m (-1)^m g(xi_m) <= g(xi1)
3. |sum eps| <= 0.0389 + g(pi)/pi: verify
4. D_n >= bound: verify with TRUE D_n
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def dtheta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.re(mp.digamma(mp.mpc(0.25, t/2)))/2 - mp.log(mp.pi)/2)

def Main_pos_num(n):
    tstar = (n+0.5)/math.pi
    gmax = z[-1]
    ts = np.linspace(tstar, gmax, 5000)
    th = theta(ts); phi = (n+0.5)*th
    f = 2*np.sin(phi)*np.sin(th/2)
    dtrs = np.array([dtheta_RS(t) for t in ts])
    return np.trapz(f*dtrs, ts)/math.pi

def D_n(n):
    th = theta(z); phi = (n+0.5)*th
    f = np.cos(n*th) - np.cos((n+1)*th)
    return f.sum()

print("n        D_n真值  Main_pos数值  c·logn+C0   下界公式   真值>下界?")
c = 0.294744936; C0 = -0.456053
for n in [43, 44, 50, 100, 500, 1000]:
    Dn = D_n(n)
    Mp = Main_pos_num(n)
    lb_formula = c*math.log(n) + C0
    xi1 = 1.5*math.pi
    gxi1 = math.log((n+0.5)/(2*math.pi*xi1))/(math.pi*xi1)
    gpi = math.log((n+0.5)/(2*math.pi**2))/math.pi
    lb_full = c*math.log(n) + C0 - gxi1 - 0.0389 - gpi/math.pi
    print(f"{n:5d} {Dn:+9.4f} {Mp:+10.4f} {lb_formula:+10.4f} {lb_full:+9.4f}   {Dn > lb_full}")
    # 检查 Main_pos 是否 >= c log n + C0
    ok_Mp = Mp >= lb_formula - 0.01
    print(f"       Main_pos ≥ c·logn+C0-0.01? {ok_Mp} (差={Mp-lb_formula:+.4f})")
