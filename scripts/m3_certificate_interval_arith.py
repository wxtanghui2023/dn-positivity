#!/usr/bin/env python3
"""m3_certificate_interval_arith.py — M=3 的【区间算术】证书（闭合 SLACK 假设）

## 目标
严格证明  m_3 := min_{phi in [0,pi]^3} max_{1<=k<=15} sum_{j=1..3} cos(k phi_j) >= 1/2

## 与 C-163 参考实现的区别（本脚本的意义）
C-163 用【浮点】算每箱下界, 并以 SLACK=1e-12 作为"浮点误差不超过此值"的【假设】。
本脚本把每箱下界改为【真区间算术】:
  · 箱边界为【精确有理数】(Fraction)
  · 域取 [0,P]^3, P 为 pi 的【有理上界】(故 [0,pi]^3 含于其中, 更强)
  · k*a_j 为【精确有理数】(整数运算)
  · cos 用 mpmath.iv (pi 取区间) => cos 取区间 => 取下端
  · "区间是否含 pi 的奇数倍" 用 pi 的区间【严格判定】; 不确定时保守取 -1
=> 不依赖 SLACK, 也不依赖 libm 的浮点误差界

## 每箱下界的正确性（核心不等式）
对任意箱 B=[a_1,b_1]x[a_2,b_2]x[a_3,b_3] 与任意 k:
    min_{phi in B} sum_j cos(k phi_j) = sum_j min_{phi_j in [a_j,b_j]} cos(k phi_j)
=> 对任意 phi in B:  max_k sum_j cos(k phi_j)  >=  max_k sum_j min_{[a_j,b_j]} cos(k phi_j) =: LB(B)
=> min_{phi in B} max_k ... >= LB(B)
故 LB(B) >= 1/2 即认证该箱; 全部箱认证 => m_3 >= 1/2。

单区间 min 的算法: cos 的局部极小只在 pi 的奇数倍处出现
   => 若 [x1,x2] 含 pi 的奇数倍 => min = -1
   => 否则 min = min(cos x1, cos x2)   （端点取下端, 区间算术）

## 用法
    pip install mpmath
    python3 scripts/m3_certificate_interval_arith.py [预算] [最大深度]
输出: 评估箱数 / 未决箱数 / 是否全部认证。若未决>0 => 【不声称】证明。
"""
import sys, time
from fractions import Fraction
from mpmath import iv

# pi 的【有理】上下界（用于严格的有理性运算）；P 为域上界（>= pi）
PI_LO = Fraction(3141592653589793, 10**15)
PI_HI = Fraction(3141592653589794, 10**15)
P     = PI_HI                      # 域: [0,P]^3 ⊇ [0,pi]^3
assert PI_LO < PI_HI and PI_HI > Fraction(3141592653589793, 10**15)

iv.dps = 40                         # 区间精度（越高越慢）

def iv_cos_lower(x: Fraction):
    """cos(x) 的严格下界（x 为精确有理数）。"""
    v = iv.cos(iv.mpf(x.numerator) / iv.mpf(x.denominator))
    return v.a                      # 区间下端（mpf）

def min_cos_on_interval(x1: Fraction, x2: Fraction):
    """严格下界: min_{x in [x1,x2]} cos(x)。x1<=x2 为精确有理数。"""
    assert x1 <= x2
    # 是否含 pi 的奇数倍: 对候选 n 做严格判定; 不确定则保守取 -1
    n_lo = int((x1 / PI_HI).__floor__()) - 2
    n_hi = int((x2 / PI_LO).__ceil__()) + 2
    definite = False
    possible = False
    for n in range(n_lo, n_hi + 1):
        if n % 2 == 0:
            continue
        lo = n * PI_LO
        hi = n * PI_HI
        if lo >= x1 and hi <= x2:
            definite = True          # 确证含奇数倍
            break
        if not (hi < x1 or lo > x2):
            possible = True          # 不能排除
    if definite or possible:
        return iv.mpf(-1)            # 保守: 最小值取下界 -1
    return min(iv_cos_lower(x1), iv_cos_lower(x2))

def lb_box(a, b, M, K=None):
    if K is None: K = 5 * M
    """箱下界 LB(B) = max_{k<=K} sum_j min_{[a_j,b_j]} cos(k phi_j) 的严格下界。"""
    best = None
    for k in range(1, K + 1):
        s = iv.mpf(0)
        for j in range(M):
            s += min_cos_on_interval(Fraction(k) * a[j], Fraction(k) * b[j])
        v = s.a
        if best is None or v > best:
            best = v
    return best

def main():
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    maxdepth = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    M = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    # 目标阈值（可给分数形式，如 0.75）—— 用于收窄下界
    tgt = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
    target = iv.mpf(repr(tgt))
    t0 = time.time()
    stack = [([Fraction(0)] * M, [P] * M, 0)]
    neval = 0; unres = 0; min_margin = None; maxd = 0; unres_boxes = []
    while stack:
        a, b, d = stack.pop()
        if neval >= budget:
            unres += 1 + len(stack)
            break
        neval += 1
        maxd = max(maxd, d)
        lb = lb_box(a, b, M)
        if lb >= target:
            m = lb - target
            if min_margin is None or m < min_margin:
                min_margin = m
            continue
        if d >= maxdepth:
            unres += 1
            unres_boxes.append(([float(x) for x in a], [float(x) for x in b], d, float(mp.mpf(lb.a) if hasattr(lb,'a') else lb)))
            continue
        # 拆最宽维
        w = [b[j] - a[j] for j in range(M)]
        jm = max(range(M), key=lambda j: w[j])
        mid = (a[jm] + b[jm]) / 2
        a1 = list(a); b1 = list(b); b1[jm] = mid
        a2 = list(a); a2[jm] = mid; b2 = list(b)
        stack.append((a1, b1, d + 1)); stack.append((a2, b2, d + 1))
    dt = time.time() - t0
    print(f"评估箱数        = {neval}")
    print(f"未决箱数        = {unres}")
    print(f"最大深度        = {maxd}")
    print(f"认证最小余量    = {min_margin if min_margin is not None else 'n/a'}")
    print(f"耗时(秒)        = {dt:.1f}")
    print(f"全部认证?       = {unres == 0}")
    print()
    if unres == 0:
        print(f"⟹ 严格结论（区间算术, 无 SLACK、无浮点误差假设）:  m_{M} >= {tgt}")
    else:
        print(f"⟹ 【未完成】: 仍有未决箱 ⟹ 不能声称 m_{M} >= {tgt}（需提高预算/深度或改进判据）")
    if unres_boxes:
        import json as _json
        _json.dump(unres_boxes, open('/tmp/m3_iv_unresolved.json','w'))
        print(f"未决箱已写 /tmp/m3_iv_unresolved.json（{len(unres_boxes)} 个）")
        import numpy as _np
        cl = _json.load(open('/tmp/t13aeq_clusters.json'))['clusters']
        x0 = _np.array(cl[0]['x'])
        import itertools as _it
        PERMS3 = list(_it.permutations(range(3)))
        def dS3(u,v): return min(float(_np.linalg.norm(_np.asarray(u)[list(q)]-_np.asarray(v))) for q in PERMS3)
        ds = [dS3([(a0+b0)/2,(a1+b1)/2,(a2+b2)/2], x0) for (a_,b_,d_,l_) in unres_boxes for (a0,a1,a2) in [a_] for (b0,b1,b2) in [b_]]
        print(f"未决箱中心到 x0 的距离：min={min(ds):.3e} max={max(ds):.3e} median={_np.median(ds):.3e}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
