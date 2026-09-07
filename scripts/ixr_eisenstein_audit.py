#!/usr/bin/env python3
"""
IX-R 审计——Eisenstein 级数作为"算术族"候选
E(z,s) = y^s + φ(s)y^{1-s} + 非零 Fourier 项
φ(s) = √π Γ(s−½)ζ(2s−1)/(Γ(s)ζ(2s))——常数项含 ζ！

问题：E(z,s)（固定 z——）作为 s 的函数的零点——是否被常数项主导（读出——）？
检查：非零 Fourier 项（"非完整部分"——）的零点是否独立于 ζ？
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def constant_term(s, y):
    """E(z,s) 的常数项（非零模——y^s + φ(s)y^{1-s}——）"""
    phi = mp.sqrt(mp.pi)*mp.gamma(s-0.5)*mp.zeta(2*s-1)/(mp.gamma(s)*mp.zeta(2*s))
    return y**s + phi * y**(1-s)

def main():
    print("="*70)
    print("IX-R 审计——Eisenstein E(z,s) 零点结构")
    print("="*70)
    
    # 1. 常数项的结构（φ 含 ζ——）
    print("\n1. 常数项 φ(s) = √πΓ(s−½)ζ(2s−1)/(Γ(s)ζ(2s)):")
    print("   ζ(2s) 在分母——ζ 零点 ρ 使 ζ(2s)=0 当 2s=ρ——s=ρ/2——")
    print("   → 常数项在 s = ρ/2 有极点（ζ 零点的缩放——）")
    print("   → 读出风险直接可见（VIII 的 ρ/k 轨道——）")
    
    # 2. E*(z,s) = ζ*(2s)E(z,s)——完整化
    print("\n2. 完整化 E*(z,s) = ζ*(2s)E(z,s):")
    print("   E* 满足 E*(z,s) = E*(z,1−s)——FE——")
    print("   E* 的极点 = ζ(2s) 的零点——s = ρ/2——")
    print("   → E* 的极点直接编码 ζ 零点（通过常数项乘入——）——读出——")
    
    # 3. 数值：E(z,s) 零点的"常数项主导"检查
    print("\n3. 数值——常数项零点的位置 vs ζ:")
    # 常数项 y^s + φ(s)y^{1-s} = 0——对固定 y——解 s？
    # φ(s)y^{1-2s} = −1——y^{1-2s} = −1/φ(s)
    # 粗略扫：找常数项为零的 s——看是否 = ζ 零点位置
    y = 1.0
    print("   常数项零点（y=1——粗略扫 s = σ+it——σ∈[0,1], t∈[0,30]——）:")
    found = []
    for sigma in np.arange(0.1, 0.95, 0.05):
        for t in np.arange(0.5, 30, 0.5):
            s = complex(sigma, t)
            try:
                ct = constant_term(s, y)
                if abs(ct) < 5:  # 近零点
                    found.append((sigma, t, abs(ct)))
            except:
                pass
    # 找最小的一些
    found.sort(key=lambda x: x[2])
    print(f"   常数项近零点（|CT|<5——）{len(found)} 个——最小 5 个:")
    for f in found[:5]:
        print(f"     s=({f[0]:.2f}, {f[1]:.1f})——|CT|={f[2]:.3f}")
    print("   ζ 零点: (0.5, 14.13), (0.5, 21.02), (0.5, 25.01)...")
    print("   （若常数项近零点不在 (0.5, γ_n)——常数项不主导零点——）")

if __name__ == "__main__":
    main()
