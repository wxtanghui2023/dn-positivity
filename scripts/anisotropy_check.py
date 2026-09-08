#!/usr/bin/env python3
# 运动学各向异性（正确导数——mp.diff——）
import mpmath as mp
mp.mp.dps = 20

def find_zero(seed):
    z = mp.mpc(0.5, seed)
    for _ in range(20):
        f = mp.zeta(z)
        fp = mp.diff(mp.zeta, z)
        z = z - f/fp
    return z

zeros = [find_zero(s) for s in [14.1347, 21.0220, 25.0109, 30.4249]]
print("=== 运动学各向异性（精确零点——正确导数）===")
print("gamma          Re[w]           Im[w]          |Re|/|Im|")
for rho in zeros:
    w = mp.zeta(rho-1)/mp.diff(mp.zeta, rho)
    r = abs(w.real)/abs(w.imag) if abs(w.imag) > 1e-30 else float('inf')
    print(f"gamma={float(rho.imag):.6f}:  {float(w.real):+.6f}   {float(w.imag):+.6f}   {float(r):.4f}")

print()
print("=== 二阶 delta2 实部抵消（gamma1——X=100）===")
rho = zeros[0]
X = mp.mpf(100)
zp = mp.diff(mp.zeta, rho)
w = mp.zeta(rho-1)/zp
d1 = w/X
zpp = mp.diff(mp.zeta, rho, 2)
zp1 = mp.diff(mp.zeta, rho-1)   # zeta'(rho-1)
z2 = mp.zeta(rho-2)
num = -mp.mpc(0.5)*zpp*d1**2 + zp1*d1 - mp.mpc(0.5)*z2
num_full = num/zp
print(f"Re[d2]*X^2 = {float(num_full.real*X**2):+.6f}（beta 方向）")
print(f"Im[d2]*X^2 = {float(num_full.imag*X**2):+.6f}（gamma 方向）")
t1 = -mp.mpc(0.5)*zpp*d1**2
t2 = zp1*d1
t3 = -mp.mpc(0.5)*z2
print(f"三项实部（分子）：t1={float(t1.real):+.6f}  t2={float(t2.real):+.6f}  t3={float(t3.real):+.6f}  和={float((t1+t2+t3).real):+.6f}")
print(f"三项虚部（分子）：t1={float(t1.imag):+.6f}  t2={float(t2.imag):+.6f}  t3={float(t3.imag):+.6f}  和={float((t1+t2+t3).imag):+.6f}")
