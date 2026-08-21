#!/usr/bin/env python3
"""
PRECISE closing with CORRECT constants:
g(xi_1) = log((n+1/2)/(2pi·1.5pi))/(pi·1.5pi)  [first block, xi_1 in (pi, 2pi)]
|Leibniz main| <= g(xi_1)  [much smaller than log n/pi^2!]
|sum eps| <= |E| + |interior|/n <= 0.0389 + g(pi)/pi  [g(pi)=log((n+1/2)/(2pi^2))/pi]
Hmm wait — need to double check |interior|/n bound: it was g(pi)/pi = log(n/2pi^2)/pi^2? 
From dn_convert: |interior|/n = |J|/(2pi), |J| <= 2g(pi) => |interior|/n <= g(pi)/pi.
g(pi) = log((n+1/2)/(2pi·pi))/pi = log((n+1/2)/(2pi^2))/pi.
So |interior|/n <= log((n+1/2)/(2pi^2))/pi^2 ~ log n/pi^2 ~ 0.101 log n.  [this one IS ~ log n/pi^2]

And |E| <= 0.0389.

Main_pos = c log n + C_0 = 0.294745 log n - 0.456053 (+ O(1/n))

So D_n >= 0.294745 log n - 0.456 - [g(xi_1) + 0.0389 + log((n+1/2)/(2pi^2))/pi^2] - |Delta|
Let me compute the net coefficient and find n_0 EXACTLY.
"""
import numpy as np, math

def g_xi1(n):
    xi1 = 1.5*math.pi
    return math.log((n+0.5)/(2*math.pi*xi1))/(math.pi*xi1)

def g_pi(n):
    return math.log((n+0.5)/(2*math.pi**2))/(math.pi)

print("=== 精确闭合计算 ===")
print("n        D_n(真)  下界: 0.294745logn-0.456-g(xi1)-0.039-g(pi)/pi  裕量")
c = 0.294744936
C0 = -0.456053
for n in [43, 100, 500, 1000, 5000, 10000, 20000]:
    lb = c*math.log(n) + C0 - g_xi1(n) - 0.0389 - g_pi(n)/math.pi
    print(f"{n:7d} {'':>10} {lb:+.5f}   {'>0 ✓' if lb>0 else '<0 ✗'}")
print()
print("系数分解: c=0.2947, -g(xi1)~-0.03logn, -g(pi)/pi~-0.10logn")
print(f"  净系数 ≈ {c} - 0.034 - 0.101 = {c - 0.034 - 0.101:.4f}")

# 精确净系数（渐近）
# g(xi1) ~ log(n/(2pi·1.5pi))/(pi·1.5pi) = (logn - log(3pi^2))/(1.5pi^2) = logn/(1.5pi^2) - const
# 1/(1.5pi^2) = 0.0675
# g(pi)/pi ~ log(n/2pi^2)/pi^2 = logn/pi^2 - log(2pi^2)/pi^2 = 0.1013 logn - 0.294
coef = c - 1/(1.5*math.pi**2) - 1/math.pi**2
print(f"渐近净系数 = 0.2947 - 0.0675 - 0.1013 = {coef:.4f}")
