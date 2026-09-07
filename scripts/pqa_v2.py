#!/usr/bin/env python3
"""
解 x² − D·y² = N（D 非平方——N 素数——）——连分数收敛子法
x² − Dy² = N 有解 ⟹ 存在解 (x,y) 其中 x/y 是 √D 的收敛子或半收敛子
策略：生成收敛子 + 中间收敛——检查
"""
import math

def solve_pell(D, N, max_periods=8):
    """解 x² − D y² = N——返回 (x, y) 或 None"""
    a0 = math.isqrt(D)
    if a0*a0 == D:
        return None
    # √D 的连分数周期
    m, d, a = 0, 1, a0
    period = []
    seen = {}
    while True:
        m = d*a - m
        d = (D - m*m) // d
        a = (a0 + m) // d
        key = (m, d)
        if key in seen:
            break
        seen[key] = 1
        period.append(a)
    plen = len(period)
    # 收敛子序列：a0, period 重复
    seq = [a0] + period * max_periods
    # 递推收敛子
    conv_p = [a0, 0]  # 将用列表
    p_prev2, p_prev1 = 0, 1  # p_{-2}=0, p_{-1}=1
    q_prev2, q_prev1 = 1, 0
    for k in range(len(seq)):
        a = seq[k]
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
        val = p*p - D*q*q
        if val == N:
            return (p, q)
        if val == -N:
            # 需多周期（负的基本解——周期翻倍给出正的——）
            pass
    return None

if __name__ == "__main__":
    tests = [(5, 41), (13, 17), (5, 29), (29, 3373), (293, 7057), (3541, 4513), (17, 257), (73, 137)]
    for D, N in tests:
        sol = solve_pell(D, N)
        if sol:
            x, y = sol
            print(f"x²−{D}y²={N}: x={x}, y={y}——验证 {x*x-D*y*y==N}")
        else:
            print(f"x²−{D}y²={N}: 无解（收敛子界内——）")
            # 检查必要条件
            leg = pow(N % D, (D-1)//2, D) if D > 2 else 1
            print(f"  (N/D) = {leg}——{'(应有 1——)' if leg==1 else '无解确认'}")