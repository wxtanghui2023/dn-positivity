#!/usr/bin/env python3
"""
E_j 核 vs q^n 核：高离线零点的可见性——死亡测试的核心
E_j ~ Σ(ρ-1)^{-j}（衰减核——低通——）
λ_n ~ Σ q^n——q = 1-1/ρ（|q|>1 离线——高通——增长核——）

问题：
1. 高离线零点（γ_off 大——）在 E_j 里可见吗？（相对低零点——）
2. 在 q^n 核里呢？（n 多大才见——）
3. 是否存在有限阶、γ-independent 的不变量？（死亡测试——）
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 40

def main():
    print("="*70)
    print("E_j 核 vs q^n 核——高离线可见性")
    print("="*70)
    
    # 1. E_j 核：高离线零点 vs 低在线零点的相对贡献
    print("\n1. E_j = Σ(ρ-1)^{-j}——高离线贡献相对低零点:")
    # 第一零点（在线——γ=14.13）vs 一个高离线（γ=1000, β=0.6——）
    rho1 = 0.5 + 1j*14.1347
    rho_off = 0.6 + 1j*1000
    z1 = 1/(rho1-1)
    zoff = 1/(rho_off-1)
    print(f"   |z₁| = |1/(ρ₁-1)| = {float(abs(z1)):.6f}")
    print(f"   |z_off| = |1/(ρ_off-1)| = {float(abs(zoff)):.6f}")
    print(f"   相对比 (|z_off|/|z₁|)^j:")
    ratio = abs(zoff/z1)
    for j in [10, 50, 100, 500]:
        print(f"   j={j:>4}: (|z_off|/|z₁|)^j = {ratio**j:.2e}——高离线被淹没程度")
    
    # 2. q^n 核：同一离线零点
    print("\n2. λ_n 核 q^n——同一高离线零点:")
    q1 = 1 - 1/rho1
    qoff = 1 - 1/rho_off
    print(f"   |q₁| = {float(abs(q1)):.10f}（在线=1——）")
    print(f"   |q_off| = {float(abs(qoff)):.10f}（β=0.6>½——|q|<1？——β>½ 时 q 定义——）")
    # 注意：β>1/2 时 |q|=|1-1/ρ|——之前算过 β=0.6: |q|=0.999967<1——衰减！
    # 爆炸在 β<1/2（|q|>1——）——经 FE 伙伴 1-ρ̄（β'=0.4——）爆炸
    print(f"   注意：β=0.6 的 |q|<1（衰减——）——爆炸在 FE 伙伴 β=0.4（|q|>1——）")
    rho_off2 = 0.4 + 1j*1000  # FE 伙伴（β<1/2——）
    qoff2 = 1 - 1/rho_off2
    print(f"   FE 伙伴 β=0.4: |q| = {float(abs(qoff2)):.10f}")
    m = abs(qoff2)
    print(f"   |q|^n 增长：n* ~ 1/(|q|-1) = {1/(m-1):.0f}")
    print(f"   验证：n=1e6: |q|^n = {m**1000000:.3e}")
    
    # 3. 有限阶不变量（死亡测试——）
    print("\n3. 死亡测试：有限阶不变量 I(E_0..E_k)——能见高离线吗？")
    print("   E_j 的前 k 项由低零点主导（|z₁|>|z_off|——）")
    print("   高离线贡献 ~ (|z_off|/|z₁|)^j——指数小——")
    print("   ⟹ 任何用 E_0..E_k（k 固定——）的不变量看不到高离线")
    print("   ⟹ 需 j ~ log(信号)/log(|z_off|/|z₁|)——随 γ_off 增长——非 γ-independent")
    
    # 4. q^n 的不变量——λ_n 的前几项能看到高离线吗？
    print("\n4. λ_n 的前几项（n 小——）能看到高离线吗？")
    for n in [10, 100, 1000]:
        # 低零点 q^n vs 高离线 q^n（FE 伙伴——）
        c1 = q1**n
        coff = qoff2**n
        print(f"   n={n:>6}: |q₁^n|={float(abs(c1)):.6f} vs |q_off^n|={float(abs(coff)):.3e}——比值 {float(abs(c1/coff)):.3e}")
    
    print("\n结论：E_j（低通——）看不到高离线——λ_n 的 q^n（高通——）")
    print("   但 q^n 检测需 n~γ²/δ——与 γ 相关——非 γ-independent——")
    print("   ⟹ 支持 NO-GO：无有限阶 γ-independent 不变量（需严格化——）")

if __name__ == "__main__":
    main()
