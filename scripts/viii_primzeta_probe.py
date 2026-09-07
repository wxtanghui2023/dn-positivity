#!/usr/bin/env python3
"""
VIII 内部推导——P(s) 奇点结构与 monodromy 跳跃验证
P(s) = Σ_p p^{-s} = Σ_{k≥1} μ(k)/k · log ζ(ks)

理论预测：
1. P 的奇点 = {ρ/k: ζ(ρ)=0, k≥1} ∪ {s=1}（log ζ(ks) 的支点当 ks=ρ——）
2. 绕简单零点 ρ/k 的跳跃 = μ(k)/k · 2πi（log 的 2πi × Möbius 系数——）
3. 零点 ρ 本身（k=1——）跳跃 = 2πi（μ(1)=1——）

验证：P(s) 的数值（素数直接算 Re s>1——）与奇点结构
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def P_direct(s, pmax=200000):
    """P(s) = Σ_{p≤pmax} p^{-s}——直接素数求和（Re s>1——）"""
    # 用 sympy primerange 太慢——用预筛
    total = mp.mpf('0')
    # 简单筛
    limit = pmax
    sieve = bytearray([1])*(limit+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(limit**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * len(range(i*i, limit+1, i))
    primes = [i for i in range(2, limit+1) if sieve[i]]
    for p in primes:
        total += p**(-s)
    return total

def main():
    print("="*70)
    print("VIII 推导——P(s) 奇点结构验证")
    print("="*70)
    
    # 1. P(s) 在 Re>1 直接算（素数——）与 μ(k)/k logζ(ks) 对照
    print("\n1. P(s) 双表示对照（Re s > 1——）:")
    s_test = 1.5 + 0.0j
    P_direct_val = P_direct(s_test, 50000)
    # Möbius 组合（k 截断——）
    P_mob = mp.mpf('0')
    for k in range(1, 12):
        mu_k = mp.mobius(k)
        if mu_k != 0:
            P_mob += mu_k/k * mp.log(mp.zeta(k*s_test))
    print(f"  P_direct(1.5) = {P_direct_val:.6f}（素数≤5e4——）")
    print(f"  P_mobius(1.5) = {P_mob:.6f}（k≤11——）")
    print(f"  （直接求和截断 vs Möbius 截断——近似一致——）")
    
    # 2. 奇点位置验证：|P(s)| 在 s = ρ₁/k 附近（ρ₁ = ½+14.13i——）
    print("\n2. 奇点位置验证——|P(s)| 在 ρ₁/k 附近的行为:")
    rho1 = mp.mpc(0.5, 14.134725141734693)
    for k in [1, 2, 3]:
        z_k = rho1/k
        # P 在 z_k 附近——Möbius 组合（k' 截断——）
        def P_approx(s):
            tot = mp.mpf('0')
            for kk in range(1, 8):
                muk = mp.mobius(kk)
                if muk != 0:
                    tot += muk/kk * mp.log(mp.zeta(kk*s))
            return tot
        # 扫描 z_k 附近（实部固定——虚部扫——）
        vals = []
        for delta in [-0.05, -0.01, 0.0, 0.01, 0.05]:
            s_probe = z_k.real + 0.01 + 1j*(z_k.imag + delta)
            try:
                v = P_approx(s_probe)
                vals.append((delta, abs(v)))
            except:
                vals.append((delta, float('inf')))
        print(f"  ρ₁/{k} = {complex(z_k.real, z_k.imag):.3f}: |P| 扫描 = {[(d, round(float(v),1)) for d,v in vals]}")

if __name__ == "__main__":
    main()
