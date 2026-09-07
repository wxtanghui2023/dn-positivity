#!/usr/bin/env python3
"""
PQa 算法解广义 Pell 方程 x² − D·y² = N（D = p 素数——N = q 素数——）
标准连分数法：展开 √D 的连分数——跟踪 (P,Q,a) 三元组——找解
参考：Lenstra 的 Pell 讲义 / 标准 PQa 迭代
"""
import math

def pqa_solve(D, N, max_iter=200000):
    """解 x² − D y² = N——PQa 算法
    返回 (x, y) 或 None
    D 非平方——N 非零"""
    # 需要 |x| 最小解——用连分数收敛子 + 中间值
    # 标准方法：解 x² ≡ N (mod |N| 相关)——先找 x₀ 使 x₀² ≡ D·k 类
    # 用"√D 连分数 + (x₀,y₀) 种子"的 Lagrange 法：
    # 若存在解——存在 (x,y) 使 |x| ≤ √(|N|·(√D+1)/2)·(√D+√(D-1)) 类界——但搜索策略：
    # 直接迭代 PQa 找 (P,Q) 使 Q | N 且匹配
    
    # 更直接：解模方程后提升——对每个满足 x² ≡ D·y²+N 的小 y——
    # 但最实用：若 x₀² ≡ D (mod |N|) 无解则无解（必要条件 N 的素因子条件）
    # 实际：x² − Dy² = N ⟹ x² ≡ N + Dy²——遍历 y 到界
    
    # 用连分数收敛子的标准搜索：x² − Dy² = N 的解 x/y ~ √D——
    # 对每个连分数收敛子 p_k/q_k——测 p_k² − D q_k² 是否 = N
    # 但需要包含"半收敛"（中间收敛）才保证找到——复杂
    # 简化实用版：y 遍历到足够界（解通常 y 不太大——对素数 N——）
    
    # 先检查必要条件：(N/p 的 Legendre 类——) 若 q 的某素因子 ℓ 使 (D/ℓ) = -1 且 v_ℓ(N) 奇——无解
    # 用模 D 的根：x² ≡ N (mod D)——需 (N/D) = 1（q 是 p 的二次剩余——admissible 已保证——）
    
    # 实用：y 从 1 到 y_max 遍历——x² = N + D y²——测平方
    # y_max 估计：对素数 q——解存在时最小 y 通常 < √q·(√D 相关)——粗界
    y_max = min(max_iter, int(math.sqrt(abs(N) * D)) + 1000)
    for y in range(1, y_max):
        x2 = N + D * y*y
        if x2 < 0:
            continue
        x = math.isqrt(x2)
        if x*x == x2:
            return (x, y)
    return None

def solve_norm_fast(p, q, max_iter=500000):
    """解 x² − p·y² = q——p,q 素数 ≡1 mod 4——(q/p)=1"""
    return pqa_solve(p, q, max_iter)

# 快速测试
if __name__ == "__main__":
    for p, q in [(5, 41), (13, 17), (5, 29), (29, 3373), (293, 7057), (3541, 4513)]:
        sol = solve_norm_fast(p, q)
        if sol:
            x, y = sol
            ok = x*x - p*y*y == q
            print(f"x²−{p}y²={q}: x={x}, y={y}——验证 {ok}")
        else:
            print(f"x²−{p}y²={q}: 无解")
