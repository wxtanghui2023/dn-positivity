#!/usr/bin/env python3
"""
算术'能隙'候选检查 v2（快速版——30 个零点——验证趋势——）
"""
import numpy as np
import mpmath as mp
from mpmath import zetazero

mp.mp.dps = 15  # 低精度加速

def main():
    print("="*70)
    print("算术'能隙'候选——快速检查（30 个零点）")
    print("="*70)
    
    N = 30
    gammas = np.array([float(zetazero(k).imag) for k in range(1, N+1)])
    print(f"γ 范围: [{gammas[0]:.2f}, {gammas[-1]:.1f}]")
    
    # 候选 A：Re ζ'(ρ)
    re_zp = np.zeros(N)
    abs_zp = np.zeros(N)
    c_vals = np.zeros(N)
    for i, g in enumerate(gammas):
        rho = mp.mpc(0.5, g)
        zp = mp.zeta(rho, derivative=1)
        re_zp[i] = float(mp.re(zp))
        abs_zp[i] = float(mp.fabs(zp))
        z_prev = mp.zeta(rho - 1)
        c_vals[i] = -float(mp.re(z_prev/zp))
    
    print(f"\n【候选 A：Re ζ'(ρ)】")
    print(f"  全 > 0: {np.all(re_zp > 0)}——min = {re_zp.min():.6f} @ γ={gammas[np.argmin(re_zp)]:.1f}")
    
    print(f"\n【候选 B：|ζ'(ρ)|】")
    print(f"  min = {abs_zp.min():.4f}——max = {abs_zp.max():.2f}")
    slope = np.polyfit(np.log(gammas[10:]), np.log(abs_zp[10:]), 1)[0]
    print(f"  log|ζ'| vs logγ 斜率（尾部——）= {slope:.3f}")
    
    print(f"\n【候选 C：c(γ) = -Re[ζ(ρ-1)/ζ'(ρ)]】")
    print(f"  全 > 0: {np.all(c_vals > 0)}——min = {c_vals.min():.4f}")
    
    print(f"\n【候选 D：1/|ζ'(ρ)|²】——收敛性")
    inv2 = 1.0/abs_zp**2
    cum = np.cumsum(inv2)
    for m in [5, 10, 20, 30]:
        print(f"  前 {m}: {cum[m-1]:.4f}")
    
    print("""
结论（初步）：
  Re ζ'(ρ) > 0——数值（30 个全正——但随 γ 涨落——需更多样本确认趋势）
  c(γ) > 0——数值（30 个全正——运动学——）
  
但⚠️——关键：这些都在"零点上"（边缘量——）——不是"体能隙"
  SSH 的 gap 是体量（Bloch——连续——）——ζ 需要素数侧的恒正量
""")

if __name__ == "__main__":
    main()
