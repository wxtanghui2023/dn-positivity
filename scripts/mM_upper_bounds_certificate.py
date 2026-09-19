#!/usr/bin/env python3
"""mM_upper_bounds_certificate.py — m_M 严格上界的区间算术证书 (M=2..11)

## 用途
证明 m_M := min_phi max_{1<=k<=5M} sum_j cos(k phi_j) 满足 m_M <= M-1 (M=2..11)。
配 C-159 的概率方法结论 (m_M <= sqrt(2M ln 10M) <= M-1 对 M>=12) ⟹ 一切 M>=2 严格。
⟹ 使 C-172 的推论 (近似周期单调性引理 ⟹ 单调性步) 无条件成立。

## 方法（严格性来源）
角度以【3 位小数的度】给出 = 精确有理数 d/1000 (d 为整数)。
于是 k*phi_j = k*d*pi/180000 —— 其中 k*d/180000 是【精确有理数】,
唯一非精确对象是 pi ⟹ 用 mpmath.iv 的【区间】表示 pi、cos 与求和,
取每个 k 的【区间上端】, 再对 k 取最大 ⟹ 得到 m_M 的严格上界。

## 复现
    pip install mpmath    # 需 mpmath（区间算术）
    python3 scripts/mM_upper_bounds_certificate.py
输出: 每个 M 的认证上界 U_M 与配置; 校验 U_M <= M-1。

## 边界
· 证书依赖 mpmath.iv 的正确性（标准区间算术实现）。
· 配置为启发式搜索所得（随机重启 + Nelder-Mead），仅作【上界】用途。
· 不是 m_M 的精确值；也不是下界。
"""
import json, os, sys
import numpy as np
from mpmath import iv

HERE = os.path.dirname(os.path.abspath(__file__))
CONF = os.path.join(HERE, '..', 'data', 'mM_configs_millideg.json')

def certify(M, deg_millideg, dps=60):
    """区间算术: 返回 max_{k<=5M} sum_j cos(k phi_j) 的严格上界。"""
    iv.dps = dps
    ub = float('-inf')
    for k in range(1, 5*M + 1):
        s = iv.mpf(0)
        for d in deg_millideg:
            # k * d / 180000 为精确有理; pi 为区间
            s += iv.cos(iv.mpf(k * d) * iv.pi / iv.mpf(180000))
        ub = max(ub, float(iv.mpf(s.b)))   # 取区间上端
    return ub

def main():
    confs = json.load(open(CONF))
    print(f"{'M':>3} | {'认证上界 U_M':>13} | {'M-1':>4} | {'余量':>9} | OK")
    allok = True
    for M in range(2, 12):
        dg = confs[str(M)]
        ub = certify(M, dg)
        ok = ub <= M - 1
        allok &= ok
        print(f"{M:3d} | {ub:13.6f} | {M-1:4d} | {float(M-1)-ub:9.6f} | {ok}")
    print()
    print("⟹ m_M <= M-1 对 2<=M<=11 严格成立 ?", allok)
    print("⟹ 配 C-159 (M>=12): m_M <= M-1 对一切 M>=2 严格成立。")
    return 0 if allok else 1

if __name__ == '__main__':
    sys.exit(main())
