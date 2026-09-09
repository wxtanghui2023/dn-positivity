#!/usr/bin/env python3
"""三问审计——第三问：跨 d 的耦合生死测试——2026-09-09
问题：J（或 Φ₆——）是否强制 d₁≠d₂ 之间的算术关系？
① Φ₆(d₁)、Φ₆(d₂) 共享素因子（= 经典分圆？——模 p 阶 6——）
② J(d) 之间的跨 d 关系（递推/恒等——）
③ a|n 约束的 a-d 耦合（J 侧 a 消掉——）
"""
from math import gcd

def factorize(n):
    fac = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1: fac[n] = fac.get(n, 0) + 1
    return fac

def Phi6(d):
    return d*d - d + 1

# ① 共享素因子分析：p | Φ₆(d₁) 且 p | Φ₆(d₂)（d₁≠d₂——）
print('=== ① Φ₆ 的跨 d 共享素因子（经典分圆检查——）===')
# 对 p ≡ 1 mod 6——收集解 d (mod p) 使 Φ₆(d) ≡ 0
# Φ₆(d) = 0 mod p ⟺ d 的阶 = 6 mod p——解 = 2 个本原 6 次单位根
found_pairs = []
for p in [7, 13, 19, 31, 37, 43, 61, 67]:
    if p % 6 != 1: continue
    roots = [d for d in range(1, p) if Phi6(d) % p == 0]
    # 检查：同 p 的两个根的关系（互逆——）
    if len(roots) == 2:
        r1, r2 = roots
        # 检查 r1·r2 ≡ 1 mod p？或 r1 ≡ r2⁻¹
        rel = (r1*r2) % p == 1
        print(f'  p={p}: Φ₆ 根模 p = {roots}——互逆关系: {rel}')
    # 验证阶 = 6
    for r in roots:
        # 阶（r^k = 1 mod p 的最小 k——）
        k = 1; val = r % p
        while val != 1:
            val = (val*r) % p; k += 1
            if k > p: break
        if k != 6:
            print(f'    ⚠️ p={p} r={r} 阶={k}（非 6——）')

print()
print('=== ② J 的跨 d 关系（每 d 独立？——）===')
# 检查 J(d₁) 与 J(d₂) 的乘法独立（num/den 素因子——）
# 如果 J(d₁)、J(d₂) 共享"新"素因子（非分圆的——）
def J_num_den(d):
    return Phi6(d)**3, d*d*(d-1)**2

shared_new = 0
samples = {}
for d1 in range(2, 60):
    n1, den1 = J_num_den(d1)
    f1 = set(factorize(n1)) | set(factorize(den1))
    for d2 in range(d1+1, 60):
        n2, den2 = J_num_den(d2)
        f2 = set(factorize(n2)) | set(factorize(den2))
        common = f1 & f2
        if common:
            shared_new += 1
print(f'  d₁,d₂ ∈ [2,60]: J(d₁)、J(d₂) 素因子共享对数 = {shared_new}')
print('  （共享 = 平凡（小素数 2,3,5...——）还是结构性？——见下——）')

# ③ a|n 约束：J 侧 a 是否完全消失（无 a-d 耦合——）
print()
print('=== ③ a|n 的 a-d 耦合检查 ===')
# n = ad——J_n(a) = J(d)——a 消掉——但检查 S₃ 是否作用在 (a,d) 对
print('  J_n(a) = J(d)——a 完全消掉（只依赖商 d——）')
print('  A 作用（a → n−a——）: 破坏 a|n（n−a 一般非因子——）')
print('  ⟹ S₃ 在除数对 (a,d) 上无完整作用（A 破坏整除——）')
print('  ⟹ J 侧无 a-d 耦合——a 信息丢失——')
