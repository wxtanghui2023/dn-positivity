#!/usr/bin/env python3
"""
Ramanujan τ(n) 生成——用于 D* 的 (p,k) 场
τ 乘性 + Hecke：τ(p^{k+1}) = τ(p)τ(p^k) − p^{11}τ(p^{k−1})
用递推生成 τ(n) 对 n ≤ N（标准方法——）
"""
import numpy as np
from math import isqrt

def gen_tau(N):
    """生成 τ(n) 对 n ≤ N——用递推
    τ(1) = 1——τ(n) 乘性——τ(p) 用模形式系数（难直接——）
    替代：用已知公式 τ(n) 满足 Στ(n)n^{-s} 的乘积 + 递推——
    实际计算 τ(p) 需要专用算法——这里用查表/递推混合——
    对小的 p——τ(p) 可以用 Serre 的递推（模 p——）但复杂——
    简化：先只用已知的 τ(p) 表（前 ~50 个素数——从 OEIS/文献——）
    """
    # 用 sympy 的 ramanujan_tau（如果有——）
    try:
        from sympy import ramanujan_tau
        taus = {}
        return ramanujan_tau  # 返回函数
    except ImportError:
        print("sympy ramanujan_tau 不可用——")
        return None

def main():
    # 检查 sympy
    try:
        from sympy import ramanujan_tau
        # 验证
        for n in [1, 2, 3, 4, 5]:
            print(f"τ({n}) = {ramanujan_tau(n)}")
        # 生成素数表
        primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
        # τ(p) 对前 200 素数
        taus = {}
        for p in primes[:200]:
            taus[int(p)] = int(ramanujan_tau(int(p)))
        print(f"\nτ(p) 生成：{len(taus)} 个素数（到 {primes[199]}）")
        # 归一化 Satake：a_p = τ(p)/p^{11/2}
        print("\n归一化 a_p = τ(p)/p^{11/2} 示例：")
        for p in list(taus)[:5]:
            print(f"  p={p}: τ(p)={taus[p]}——a_p={taus[p]/p**5.5:.4f}")
        # 保存
        import json
        with open('/home/node/.openclaw/workspace/dn-project/data/tau_p_200.json', 'w') as f:
            json.dump({str(k): v for k, v in taus.items()}, f)
        print("\n已保存 data/tau_p_200.json")
    except ImportError as e:
        print(f"不可用: {e}")

if __name__ == "__main__":
    main()
