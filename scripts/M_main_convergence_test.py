#!/usr/bin/env python3
"""
决定性测试：固定 T——M_main 部分和收敛还是发散？
M_main(T) = -(1/π)Σ_p [1-cos(T log p)]/(p^{1/2} log²p)
Σw 发散（~√x/log³x）——但 (1-cos) 加权后？

测试：多个 T——部分和随截止的行为
- 如果部分和趋向有限值（稳定——）→ 收敛（可证——）
- 如果部分和持续漂移（发散——）→ M_main 无限和发散——真实 M(T) 需正则化
"""
import numpy as np

def load_primes():
    return np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')

def main():
    print("="*70)
    print("固定 T 的 M_main 部分和收敛性测试")
    print("="*70)
    
    primes = load_primes()
    logp = np.log(primes)
    w = 1.0/(np.sqrt(primes) * logp**2)
    # 预计算 (1-cos) 因子部分和需要 T——分 T 算
    cutoffs = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
    
    for T in [1.0, 10.0, 100.0, 1000.0, 10000.0]:
        print(f"\nT={T}:")
        cosv = np.cos(T * logp)
        one_minus_cos = 1 - cosv  # ∈[0,2]
        partial = np.cumsum(one_minus_cos * w)
        for X in cutoffs:
            mask = primes <= X
            val = -partial[mask][-1]/np.pi
            print(f"   p≤{X:>9.0e}: M_main 部分和 = {val:+.4f}")
        # 末段漂移
        m1 = primes <= 1e7
        m2 = primes <= 1e8
        drift = partial[m2][-1] - partial[m1][-1]
        print(f"   末 decade 漂移 = {drift:+.4f}（→0 则收敛——非 0 则发散——）")
    
    # 对照：Σw 的末段漂移（发散基准——）
    cw = np.cumsum(w)
    m1 = primes <= 1e7
    m2 = primes <= 1e8
    print(f"\n对照 Σw 末 decade 漂移 = {cw[m2][-1]-cw[m1][-1]:.4f}（发散基准——）")

if __name__ == "__main__":
    main()
