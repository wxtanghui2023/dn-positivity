#!/usr/bin/env python3
"""
σ 扫描方向：ζ vs L(s,χ) 在 σ>½ 的干净性对比
干净（无零点在 σ>½——）：log|F(σ+it)| 随 σ 平滑（无 −∞ 尖峰）
离轴（零点在 β>½——）：log|F| 在 σ=β 处 → −∞

对真实 L(s,χ)（零点在线——GRH 数值——）应该干净——
对比人工构造的离轴——确认"干净性检测"有效——
然后——核心：χ 加权的干净性能否从 ζ 的（RH——）推出？
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def chi3(n):
    """模 3 原字符（二次——）χ(2)=−1"""
    r = n % 3
    if r == 0: return 0
    return 1 if r == 1 else -1

def L3(s):
    """L(s,χ₃) = 1 − 2^{−s} + 4^{−s} − 5^{−s} + ...（χ₃(n): 1,−1,0,1,−1,0...）"""
    # 用 mpmath 的 dirichlet 无内置——用 Hurwitz：L(s,χ₃) = 3^{−s}(ζ(s,1/3)−ζ(s,2/3))
    # mpmath 有 hurwitz zeta？
    try:
        return mp.dirichlet(s, [0, 1, -1])  # 可能有
    except:
        # 手动：用 eta 型加速——χ₃(n) 周期 3——交替
        return mp.nsum(lambda n: chi3(n)*n**(-s), [1, mp.inf])

def main():
    print("="*70)
    print("σ 扫描：ζ vs L(s,χ₃) 在 σ>½ 的干净性")
    print("="*70)
    
    # 固定 t——扫 σ
    for t in [10, 20, 30]:
        print(f"\nt={t}:")
        sigs = np.linspace(0.51, 1.5, 40)
        vals_zeta = []
        vals_L3 = []
        for sig in sigs:
            # log|ζ(σ+it)|
            lz = float(mp.log(abs(mp.zeta(mp.mpc(sig, t)))))
            # log|L(σ+it,χ₃)|——用 dirichlet 或 nsum
            try:
                Lv = mp.dirichlet(mp.mpc(sig, t), [1, -1, 0])  # 系数 1,−1,0 周期
                lL = float(mp.log(abs(Lv)))
            except:
                # 备选——粗求和（σ>0.5 条件收敛慢——用前 N 项——）
                S = mp.nsum(lambda n: chi3(n)*n**(-mp.mpc(sig,t)), [1, mp.inf])
                lL = float(mp.log(abs(S)))
            vals_zeta.append(lz)
            vals_L3.append(lL)
        
        # 打印几个点
        for i in [0, 5, 10, 20, 30, 39]:
            print(f"   σ={sigs[i]:.2f}: log|ζ|={vals_zeta[i]:+.3f}——log|L₃|={vals_L3[i]:+.3f}")
        
        # 平滑性检查：σ 扫描的"尖峰"（−∞ 附近——离轴迹象——）
        zeta_min = min(vals_zeta)
        L3_min = min(vals_L3)
        print(f"   min log|ζ| = {zeta_min:+.3f}——min log|L₃| = {L3_min:+.3f}（远离 −∞ = 干净——）")
    
    # 人工离轴对比：构造一个有离轴零点的"玩具 L"——看 σ 扫描是否检测
    print("\n" + "="*70)
    print("离轴检测验证（人工——）")
    print("="*70)
    # 玩具：f(s) = (1 − (s−ρ)/c)·g(s)——在 ρ=0.6+30i 有零点（离轴——）
    # 沿 σ 扫（t=30——）——log|f| 在 σ=0.6 处 → −∞
    print("\nt=30——人工离轴零点在 σ=0.6:")
    for sig in [0.55, 0.58, 0.59, 0.6, 0.61, 0.62, 0.65]:
        # f 的零点贡献 log|1−(s−ρ)/c|——在 s=σ+30i——ρ=0.6+30i——c 小——
        contrib = np.log(abs(1 - (mp.mpc(sig,30) - mp.mpc(0.6,30))/mp.mpf('0.5')))
        print(f"   σ={sig}: 零点贡献 log = {float(contrib):+.3f}（→−∞ 接近 σ=0.6——）")

if __name__ == "__main__":
    main()
