#!/usr/bin/env python3
"""
E-G 候选 T1-T4 致命测试
T1: u=0 分支是否闭合？
T2: 分支上是否出现 |ζ'|≈0 临界点？
T3: 临界点处 v 方向是否翻转？
T4: 零点之间的 u=0 连通性（相邻零点同分支？——）

用高精度 ζ——追踪 u=0 分支
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 20

def zeta_uv(sig, t):
    z = mp.zeta(mp.mpc(sig, t))
    return float(z.real), float(z.imag)

def zeta_deriv(sig, t):
    """ζ'(σ+it)"""
    z = mp.zeta(mp.mpc(sig, t), derivative=1)
    return complex(float(z.real), float(z.imag))

def main():
    print("="*70)
    print("E-G 测试 T1-T4")
    print("="*70)
    
    # T2: ζ' 的零点位置（前几个——）
    print("\nT2: ζ'(s) 的零点（Speiser——在 σ<½ 区——）:")
    # ζ' 零点在临界带——找 σ∈[0.4,0.5] 的 ζ' 零点——粗扫
    # 简化：检查 u=0 分支附近是否有 |ζ'| 小
    print("   （先检查零点附近 |ζ'| 的行为——）")
    for gamma in [14.1347, 21.0220, 25.0109]:
        for sig in [0.5, 0.505, 0.51, 0.515]:
            # 找 u=0 在 gamma 附近的 t
            ts = np.linspace(gamma-2, gamma+2, 400)
            zeros = []
            prev = None
            for t in ts:
                u, v = zeta_uv(sig, t)
                if prev is not None and prev*u < 0:
                    zeros.append(t)
                prev = u
            for t0 in zeros:
                zp = zeta_deriv(sig, t0)
                print(f"   γ={gamma:.1f} σ={sig:.3f}: u=0 在 t={t0:.4f}——|ζ'|={abs(zp):.4f}")
    
    # T1: u=0 "环"是否是闭合的？——追踪完整分支
    print("\nT1: u=0 分支追踪（从零点出发——沿 u=0 走——看是否闭合——）:")
    # 用数值跟随 u=0 曲线（从零点 14.1347 出发——）
    # u=0 局部两支——追踪（σ 从 0.5 增——t 跟随——）
    print("   从零点 γ₁ 出发的 u=0 分支（σ 增方向——）:")
    sig = 0.500
    t = 14.1347
    prev_sig, prev_t = sig, t
    for _ in range(30):
        # 在当前 σ 找 u=0 的 t（靠近前一个——）
        ts = np.linspace(t-0.15, t+0.15, 200)
        best = None
        prev_u = None
        for tt in ts:
            u, v = zeta_uv(sig, tt)
            if prev_u is not None and prev_u*u < 0:
                best = tt
                break
            prev_u = u
        if best is None:
            # 扩展搜索
            ts = np.linspace(t-0.5, t+0.5, 400)
            prev_u = None
            for tt in ts:
                u, v = zeta_uv(sig, tt)
                if prev_u is not None and prev_u*u < 0:
                    best = tt
                    break
                prev_u = u
        if best is None:
            print(f"   σ={sig:.3f}: u=0 分支消失（t 从 {prev_t:.4f}——）")
            break
        u, v = zeta_uv(sig, best)
        zp = zeta_deriv(sig, best)
        print(f"   σ={sig:.3f}: u=0 在 t={best:.4f}——v={v:+.4f}——|ζ'|={abs(zp):.3f}")
        t = best
        sig += 0.002  # σ 步进
        if sig > 0.56:
            break

if __name__ == "__main__":
    main()
