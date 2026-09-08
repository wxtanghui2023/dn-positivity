#!/usr/bin/env python3
# |χ(s)| 沿 σ（χ 的势——）——σ=1/2 是否极值？
import mpmath as mp
mp.mp.dps = 12

def chi(s):
    return 2**s * mp.pi**(s-1) * mp.sin(mp.pi*s/2) * mp.gamma(1-s)

print("=== |χ(σ+it)| 沿 σ（多 t——）——σ=1/2 极值性 ===")
for t in [8.0, 14.0, 21.0, 30.0]:
    print(f"t={t}:")
    vals = []
    for sg in [0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8]:
        m = abs(chi(mp.mpc(sg, t)))
        vals.append(m)
        print(f"  σ={sg:.2f}: |χ| = {float(m):.6f}")
    # 检查 σ=1/2 是否极小/极大
    m_half = abs(chi(mp.mpc(0.5, t)))
    m_lo = abs(chi(mp.mpc(0.4, t)))
    m_hi = abs(chi(mp.mpc(0.6, t)))
    print(f"  → |χ(0.5)|={float(m_half):.4f} vs |χ(0.4)|={float(m_lo):.4f} vs |χ(0.6)|={float(m_hi):.4f}")
    if m_half < m_lo and m_half < m_hi:
        print("  → σ=1/2 是局部极小！")
    elif m_half > m_lo and m_half > m_hi:
        print("  → σ=1/2 是局部极大！")
    else:
        print("  → σ=1/2 非极值（单调？——）")
    print()

print("=== log|χ| 沿 σ——更细（t=14——）===")
t = 14.0
prev = None
for sg in mp.arange(0.3, 0.7, 0.02):
    l = float(mp.log(abs(chi(mp.mpc(sg, t)))))
    print(f"  σ={float(sg):.2f}: log|χ| = {l:+.4f}")
