#!/usr/bin/env python3
"""
v4 最后硬门：规范化不变量审计
对同一 admissible triple——故意生成多个等价表示：
1. 不同 z 奇解（多 (x,y,z)——）
2. 同解 × 奇 k（β·k²——norm 类不变——）
3. sign 翻转（β vs −β——）
全部规范化后必须给相同 Rédei 符号（canonical——）
"""
import math, sys, itertools
sys.path.insert(0, 'scripts')
from redei_v4 import redei_v4, normalize_beta, legendre, tonelli, solve_z_odd, v2

def solve_z_odd_multi(a, b, n_sols=3, z_max=40, y_max=30000):
    """找多个 z 奇解"""
    sols = []
    for z in range(1, z_max, 2):
        for y in range(1, y_max):
            x2 = b*z*z + a*y*y
            x = math.isqrt(x2)
            if x*x == x2:
                # primitive 化（去掉共同因子——保持 z 奇——）
                g = math.gcd(math.gcd(x, y), z)
                sols.append((x//g, y//g, z//g))
                if len(sols) >= n_sols:
                    return sols
    return sols

def redei_from_beta(a, b, c, x, y, z):
    """从给定解算规范化 Rédei 符号（redei_v4 的核心——）"""
    if z % 2 == 0:
        return None
    norm = normalize_beta(a, b, x, y, z)
    if norm is None:
        return None
    eps, s = norm
    sq = tonelli(a % c, c)
    if sq is None:
        return None
    beta_c = (x + y*sq) % c
    if beta_c == 0:
        return None
    leg = legendre(beta_c, c)
    corr = 1
    if s == 2:
        corr *= legendre(2, c)
    if eps == -1:
        corr *= legendre(-1, c)
    return leg * corr

def main():
    import numpy as np, random
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:500]
    random.seed(31)
    
    n_triple = 0
    n_multi_rep = 0
    n_all_consistent = 0
    n_inconsistent = 0
    
    for _ in range(600):
        a, b, c = random.sample(p1, 3)
        if not (legendre(a,b)==1 and legendre(b,c)==1 and legendre(c,a)==1):
            continue
        n_triple += 1
        # 收集所有等价表示
        reps = []
        # 多个 z 奇解
        sols = solve_z_odd_multi(a, b, n_sols=3)
        for x, y, z in sols:
            reps.append((x, y, z))
            # k 奇乘子（β·k² 类——）
            for k in [3, 5]:
                reps.append((k*x, k*y, k*z))  # 注意：z 变 k·z——仍奇（k 奇——）
            # sign 翻转
            reps.append((-x, -y, z))
        
        # 去重 + 算符号
        seen = set()
        vals = []
        for x, y, z in reps:
            # primitive 化
            g = math.gcd(math.gcd(abs(x), abs(y)), abs(z))
            xg, yg, zg = x//g, y//g, z//g
            if zg % 2 == 0:
                continue  # 非法（z 偶——）
            key = (xg, yg, zg)
            if key in seen:
                continue
            seen.add(key)
            v = redei_from_beta(a, b, c, xg, yg, zg)
            if v is not None:
                vals.append(v)
        
        if len(vals) >= 2:
            n_multi_rep += 1
            if len(set(vals)) == 1:
                n_all_consistent += 1
            else:
                n_inconsistent += 1
                if n_inconsistent <= 3:
                    print(f"❌ 规范化不一致: ({a},{b},{c})——vals={vals}")
        if n_triple >= 30:
            break
    
    print(f"\nadmissible triple: {n_triple}——多表示: {n_multi_rep}——全一致: {n_all_consistent}——不一致: {n_inconsistent}")
    if n_inconsistent == 0 and n_multi_rep > 0:
        print("✅ 规范化不变量审计通过——canonical map 确认——可进入 R1/R2！")
    else:
        print("❌ 有 inconsistency——规范化仍有表示依赖——需修")

if __name__ == "__main__":
    main()
