#!/usr/bin/env python3
"""唐先生的攻击点验证：∫f_n·S·g = O(1) 无条件？
I_p(n) = ∫f_n(t)·sin(t·log p)·g(t)dt——f_n = 4sin²(nθ₁)——分解为：
  第一部分：½∫sin(t log p)g（van der Corput——无条件小）
  第二部分：½∫cos(2nθ₁)sin(t log p)g（双振荡——积化和差——stationary phase）
验证 |I_p(n)| ≤ C/(p·log³p)？
"""
import numpy as np
import gc
from math import log, pi
from scipy.integrate import quad

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(300000)
T = z[-1]

def th1(t):
    return np.arctan(1/(2*t))
def g(t):
    return 2*pi/(t*np.log(t/(2*pi))**2)
def f_n(t, n):
    return 4*np.sin(n*np.arctan(1/(2*t)))**2

# I_p(n) 数值
print("I_p(n) = ∫f_n·sin(t log p)·g dt 的量级：")
print(f"{'p':>5} {'n=10':>12} {'n=100':>12} {'n=500':>12} {'C/(p·log³p)':>14}")
ps = [2, 3, 5, 7, 11, 101]
for p in ps:
    row = []
    for n in [10, 100, 500]:
        val, err = quad(lambda t: f_n(t, n)*np.sin(t*log(p))*g(t), z[0], T, limit=2000)
        row.append(val)
    bound = 1.0/(p*log(p)**3)
    print(f"{p:5d} {row[0]:+12.4f} {row[1]:+12.4f} {row[2]:+12.4f} {bound:14.6f}")

# 分解验证：f_n = 2 − 2cos(2nθ₁)——第一部分 + 第二部分
print("\n分解验证（n=100, p=3）：")
n, p = 100, 3
th = th1(np.linspace(z[0], T, 20000))
# 第一部分：∫2·sin(t log p)·g
I1, _ = quad(lambda t: 2*np.sin(t*log(p))*g(t), z[0], T, limit=2000)
# 第二部分：∫−2cos(2nθ₁)sin(t log p)·g
I2, _ = quad(lambda t: -2*np.cos(2*n*np.arctan(1/(2*t)))*np.sin(t*log(p))*g(t), z[0], T, limit=2000)
print(f"  I1（½部分）= {I1:+.6f}  I2（cos部分）= {I2:+.6f}  和 = {I1+I2:+.6f}")

# 第二部分的双振荡分解：cos(2nθ₁)sin(t log p) = ½[sin(t log p+2nθ₁)+sin(t log p−2nθ₁)]
print("\n双振荡分解（n=100, p=3——stationary phase 检验）：")
I2a, _ = quad(lambda t: -np.sin(t*log(p)+2*n*np.arctan(1/(2*t)))*g(t), z[0], T, limit=2000)
I2b, _ = quad(lambda t: -np.sin(t*log(p)-2*n*np.arctan(1/(2*t)))*g(t), z[0], T, limit=2000)
print(f"  I2 = {I2a+I2b:+.6f}（sin(t log p+2nθ₁): {I2a:+.6f}——sin(t log p−2nθ₁): {I2b:+.6f}）")
# stationary phase 点：φ' = log p ∓ n/t² = 0——t* = √(n/log p)
for p in [2, 3, 5]:
    t_star = np.sqrt(n/log(p))
    print(f"  p={p}: t* = √(n/log p) = {t_star:.2f}（区间 [{z[0]:.1f}, {T:.0f}]——{'在内' if z[0]<t_star<T else '在外'}）")

# Σ_p 1/(p^{3/2}·log⁴p) 收敛
def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

ps_all = primes_upto(200000)
logp = np.log(ps_all)
S = np.sum(1.0/(ps_all**1.5 * logp**4))
print(f"\nΣ_p 1/(p^1.5·log⁴p) = {S:.6f}（收敛——< ∞）")

del z
gc.collect()
print("内存已释放")
