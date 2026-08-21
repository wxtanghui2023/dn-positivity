#!/usr/bin/env python3
"""
Final edge-case check for the alternating-half-wave bound |J| <= 2g(pi):
J = int_{pi}^{phi_max} sin(phi) g(phi) dphi, g decreasing positive.

Standard result: if g is positive decreasing, then
  |int_a^b sin(x) g(x) dx| <= 2 g(a)   [for any b > a, even partial waves]
Proof: split [a,b] into half-waves [m*pi,(m+1)*pi]. On each full half-wave,
  int sin g = ±(positive) with |int| <= 2 g(m*pi) (g decreasing => max at left).
  The signed contributions form an alternating sequence with decreasing magnitudes,
  so the total is bounded by the first term: <= 2 g(a). Partial last wave also <= 2g.
This is the classic Dirichlet/Abel test for ∫ sin(x)g(x)dx. VERIFY numerically for
partial waves and various b.
"""
import numpy as np, math

def g(phi, n):
    A = n/(2*math.pi)
    return np.log(A/np.maximum(phi,1e-12))/np.maximum(phi,1e-12)

print("=== |J| <= 2g(pi) 对任意 b（含不完整半波）===")
ok_all = True
for n in [1000, 5000, 10000]:
    phi_max = 0.070718*(n+0.5)
    # 测试多个 b：完整半波末端、不完整、中间
    bs = [math.pi*3, math.pi*4, math.pi*5.3, math.pi*7.7, phi_max]
    for b in bs:
        if b <= math.pi: continue
        phis = np.linspace(math.pi, b, 500000)
        J = np.trapz(np.sin(phis)*g(phis,n), phis)
        ok = abs(J) <= 2*g(math.pi,n)
        ok_all &= ok
        if not ok: print(f"  FAIL n={n} b={b:.2f}: |J|={abs(J):.4f} > 2g(pi)={2*g(math.pi,n):.4f}")
print(f"全部通过: {ok_all}")
print()
print("=== 更紧的界? |J| <= g(pi) 也成立? ===")
for n in [1000, 10000]:
    phi_max = 0.070718*(n+0.5)
    phis = np.linspace(math.pi, phi_max, 500000)
    J = np.trapz(np.sin(phis)*g(phis,n), phis)
    print(f"n={n}: |J|={abs(J):.4f}, g(pi)={g(math.pi,n):.4f}, 2g(pi)={2*g(math.pi,n):.4f}, |J|<=g(pi)? {abs(J)<=g(math.pi,n)}")
