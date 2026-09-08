#!/usr/bin/env python3
"""
零曲线几何深挖——u=0（Re ζ=0）与 v=0（Im ζ=0）曲线的拓扑结构
在 σ-t 平面找 u=0 和 v=0 的曲线——看它们怎么走——为什么 σ>½ 不相交
"""
import numpy as np
import mpmath as mp

def zeta_val(sig, t):
    """ζ(σ+it) 用 mpmath"""
    s = mp.mpc(sig, t)
    z = mp.zeta(s)
    return float(z.real), float(z.imag)

def main():
    print("="*70)
    print("u=0/v=0 曲线结构（σ-t 平面——）")
    print("="*70)
    
    # 扫描 σ∈[0.1, 0.9], t∈[0, 60]——找 u=0 和 v=0 的位置
    sigs = np.linspace(0.05, 0.95, 40)
    ts = np.linspace(0.5, 60, 3000)
    
    # 对每个 σ——找 u=0 的 t 和 v=0 的 t
    print("每 σ 的 u=0/v=0 位置（前几个——）:")
    print(f"{'σ':>5} | {'u=0 的 t':>30} | {'v=0 的 t':>30}")
    for sig in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
        # 采样找过零
        u_zeros = []
        v_zeros = []
        prev_u = None
        prev_v = None
        prev_t = None
        for t in ts:
            u, v = zeta_val(sig, t)
            if prev_u is not None:
                if prev_u * u < 0:
                    # 插值
                    t0 = prev_t + (t - prev_t) * abs(prev_u)/(abs(prev_u)+abs(u))
                    u_zeros.append(t0)
                if prev_v * v < 0:
                    t0 = prev_t + (t - prev_t) * abs(prev_v)/(abs(prev_v)+abs(v))
                    v_zeros.append(t0)
            prev_u, prev_v, prev_t = u, v, t
        
        us = np.array(u_zeros)
        vs = np.array(v_zeros)
        # 只显示前 8 个
        us_str = " ".join(f"{x:.1f}" for x in us[:8])
        vs_str = " ".join(f"{x:.1f}" for x in vs[:8])
        print(f"{sig:>5.2f} | {us_str:>30} | {vs_str:>30}")
        print(f"      （u=0 共 {len(us)} 个——v=0 共 {len(vs)} 个——）")
    
    # 关键：σ 从 0.5 到 0.6——u=0 数目的变化
    print("\nσ 扫描的 u=0 数目（t<60——）:")
    for sig in [0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80]:
        count_u = 0
        prev_u = None
        prev_t = None
        for t in ts:
            u, v = zeta_val(sig, t)
            if prev_u is not None and prev_u * u < 0:
                count_u += 1
            prev_u = u
        print(f"   σ={sig:.2f}: u=0 数目 = {count_u}")

if __name__ == "__main__":
    main()
