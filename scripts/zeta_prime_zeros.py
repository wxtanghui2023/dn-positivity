#!/usr/bin/env python3
"""
E-G 核心测试：ζ' 零点位置 vs u=0 拱顶
如果 ζ' 零点（σ_ζ' > 拱顶 σ_max——）——u=0 拱上无 ζ' 零点——v 单调——每拱一零点
Speiser：RH ⟺ ζ' 在 σ<½ 无零点——ζ' 零点（无条件）多在 σ>½？
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 15

def zeta_deriv_abs(sig, t):
    z = mp.zeta(mp.mpc(sig, t), derivative=1)
    return abs(complex(float(z.real), float(z.imag)))

def main():
    print("="*70)
    print("ζ' 零点位置 vs u=0 拱顶")
    print("="*70)
    
    # 1. 找 ζ' 的零点（粗扫——σ∈[0.4,0.7]——t 到 40——）
    # ζ' 零点：找 |ζ'| 的局部极小 ≈ 0——用网格
    print("\n1. |ζ'| 的极小值扫描（找 ζ' 零点——）:")
    sigs = np.linspace(0.40, 0.70, 31)
    ts = np.linspace(2, 40, 191)
    minima = []
    for sig in sigs:
        prev = None
        prev_t = None
        for t in ts:
            val = zeta_deriv_abs(sig, t)
            if prev is not None and val < prev:
                # 可能局部极小——记录
                pass
            prev = val
        # 简化——找整条 t 线上的最小
        vals = [zeta_deriv_abs(sig, t) for t in ts]
        idx = np.argmin(vals)
        if vals[idx] < 5.0:  # 相对小
            minima.append((sig, ts[idx], vals[idx]))
    
    # 找真正小的（ζ' 零点附近——）
    print("   |ζ'| 全局小值（<2——）:")
    small = [(s,t,v) for s,t,v in minima if v < 2.0]
    for s,t,v in small:
        print(f"   σ={s:.2f} t={t:.2f}: |ζ'|={v:.4f}")
    
    # 2. 精确找几个 ζ' 零点（已知——ζ' 零点在 σ~0.5-0.6 附近——）
    # 用已知：ζ' 有零点在临界带——第一个在？
    print("\n2. ζ' 零点的精确搜索（粗——）:")
    # 在 σ∈[0.5,0.8] 找 |ζ'| 深极小
    found = []
    for t0 in np.linspace(5, 40, 36):
        # 对每个 t0 区间——扫 σ
        best = None
        for sig in np.linspace(0.5, 0.85, 36):
            val = zeta_deriv_abs(sig, t0)
            if best is None or val < best[1]:
                best = (sig, val)
        if best[1] < 1.0:
            found.append((t0, best[0], best[1]))
    print("   (t, σ_min, |ζ'|min)——|ζ'|<1 的:")
    for t0, sig, val in found:
        print(f"   t={t0:.1f}: σ 极小在 {sig:.2f}——|ζ'|={val:.3f}")
    
    # 3. 结论：ζ' 零点的 σ 位置 vs 零点拱顶（~0.516——）
    print("\n3. 对比：u=0 拱顶（零点1: ~0.516——）vs ζ' 零点 σ")
    print("   如果 ζ' 零点 σ > 拱顶——拱上无 ζ' 零点——")

if __name__ == "__main__":
    main()
