#!/usr/bin/env python3
"""审前沿天花板 · 自己重算（骨架 + 已可执行部分）
目标：证书侧上确界  max_{c0,r} [ c0 + ∫0^1 r x dx ]  s.t. c0 + Σ_j s_j r(j/N) ≤ p  ∀ admissible(s,p)
权威定义来源：Zeta23/PairCeiling/{Defs,Grid,Bridge,NumericCert,RowCert,NearCUE,LawN256}.lean（已存 ../）
"""
from fractions import Fraction as F
import re, numpy as np
from scipy.optimize import linprog

LEAN = "../LawN256.lean"
N = 256
K = 2**140

def parse_encl(path=LEAN):
    src = open(path, encoding="utf-8").read()
    body = re.search(r"encl\s*:=\s*\[(.*?)\]\s*\n", src, re.S).group(1)
    pr = re.findall(r"\((\d+)\s*,\s*(\d+)\)", body)
    return [(int(a), int(b)) for a, b in pr]

def rows_report(encl):
    """近-CUE 行条件：|N·S(j) − j| ≤ τ  (0<j<N)。返回每行的真实 τ_j = |N·(lo/K) − j| 与 |N·(hi/K) − j|。"""
    out = []
    for j, (lo, hi) in enumerate(encl, start=1):
        if j >= N: break
        # N·S(j) − j  ∈ [ N·lo/K − j , N·hi/K − j ]
        dl = F(N*lo, K) - j
        dh = F(N*hi, K) - j
        out.append((j, dl, dh))
    return out

def box_worst_penalty(rvals, r_nodes, encl, N=N, K=K):
    """盒最坏惩罚 max_S Σ_j s_j r(j/N)，s_j=S(j)/N，S(j)∈[lo/K, hi/K]。
       取上界当 r≥0、下界当 r<0  ⇒ 这是对抗方在盒内的最坏选择。"""
    rj = np.interp(np.arange(1, N+1)/N, r_nodes, rvals)   # r(j/N)
    tot = 0.0
    for idx, (lo, hi) in enumerate(encl, start=1):
        if idx > N: break
        S = hi if rj[idx-1] >= 0 else lo
        tot += (S/K)/N * rj[idx-1]        # s_j = S/N ，乘 r
    return tot

if __name__ == "__main__":
    encl = parse_encl()
    print(f"封闭区间: {len(encl)} 组")
    rep = rows_report(encl)
    tau_max = max(max(abs(dl), abs(dh)) for _, dl, dh in rep)
    print(f"近-CUE 行条件实测: max |N·S(j)−j| ≤ {float(tau_max):.6e}   (前沿声称 τ=3e-40)")
    print(f"   ⟹ 行条件 {'成立' if tau_max <= F(3,10**40) else '不成立（或索引约定待核）'}")
    # 试探：r ≡ 1 的盒最坏惩罚（对应 c0 + Σ s_j ≤ p，即最简证书）
    r_nodes = np.array([0.0, 1.0]); r_vals = np.array([1.0, 1.0])
    pen = box_worst_penalty(r_vals, r_nodes, encl)
    print(f"\n[试探 r≡1] 盒最坏惩罚 Σ s_j r(j/N) = {pen:.8f}")
    print("   注：Σ_j s_j = T_N/N 对盒取上界 ⟹ 由 j=N 自由行主导（见审前沿天花板第6步）")
    print("\n[规格] max_{c0,r} c0 + ∫ r x dx  s.t. c0 + 盒最坏惩罚 ≤ p_min(对抗方)")
    print("   待补输入：① marks 几何（p 与 S 的关系）② 对抗方 p_min 的确定")
