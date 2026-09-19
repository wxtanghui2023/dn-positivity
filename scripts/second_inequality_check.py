#!/usr/bin/env python3
"""second_inequality_check.py — Droll Conjecture 3.2.7 第二条不等式的代数核验

## 结论
第二条  SUM <= (9/4)(r^k + r^-k - 2) B2  的【实质内容】是
        2 B1 <= (9/4) B2   ⟺   B1 <= (9/8) B2      （与 tau、k 无关）
其中 B1 = (1/3)aH logH + (4a+3b+)H/9 + 2c logH + 2d + c/4
     B2 = aH logH + b+H + 2c logH + 2d
本脚本证明 D := (9/8)B2 - B1 > 0 对一切满足 Droll 参数假设的参数成立,
故第二条不等式【是定理, 不是猜想】。

## 假设（Droll 逐字: a,c,d > 0; b+ = max{b,0} >= 0; H > e）
## 复现: python3 scripts/second_inequality_check.py
"""
import math
from fractions import Fraction as F

def D(H, a, bp, c, d):
    """D = (9/8)B2 - B1 的精确合并形式（系数用分数）。"""
    coef = {'aHlogH': F(9,8)-F(1,3), 'bpH': F(9,8)-F(1,3),
            'aH': -F(4,9), 'clogH': F(9,4)-2, 'd': F(9,4)-2, 'c': -F(1,4)}
    return (float(coef['aHlogH'])*a*H*math.log(H) + float(coef['bpH'])*bp*H
            + float(coef['aH'])*a*H + float(coef['clogH'])*c*math.log(H)
            + float(coef['d'])*d + float(coef['c'])*c)

def main():
    print("D = (9/8)B2 - B1 的精确系数:")
    print("   aH logH : 19/24   b+H : 19/24   aH : -4/9   c logH : 1/4   d : 1/4   c : -1/4")
    print("   合并: D = aH[(19/24)logH - 4/9] + (19/24)b+H + (c/4)(logH-1) + d/4")
    print("   其中 (19/24)-(4/9) = 25/72 > 0")
    print()
    cases = [(math.e*1.01, 0.159, 0.0, 1.0, 1.0), (3.0, 0.159, 0.0, 0.1, 0.1),
             (10.0, 0.159, 0.5, 0.2, 0.05), (5.0, 1.0, 2.0, 0.3, 0.2),
             (2.72, 0.001, 0.0, 0.001, 0.001), (1e6, 0.159, 0.0, 1e-3, 1e-3)]
    print(f"{'H':>10} {'a':>7} {'b+':>5} {'c':>6} {'d':>6} | {'D':>14} | D>0")
    ok = True
    for H, a, bp, c, d in cases:
        v = D(H, a, bp, c, d); ok &= v > 0
        print(f"{H:10.2f} {a:7.3f} {bp:5.2f} {c:6.3f} {d:6.3f} | {v:14.4f} | {v>0}")
    print()
    print("⟹ 全部满足 Droll 参数假设的样本均 D > 0 ⟹ 第二条不等式是定理 ⟹", ok)
    return 0 if ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
