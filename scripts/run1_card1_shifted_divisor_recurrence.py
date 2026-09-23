#!/usr/bin/env python3
# run1_card1_shifted_divisor_recurrence.py —— RUN-1（预注册、单轮、不可漂移）
# 【冻结范围】X ∈ {1e6, 1e7}; 数据 0<=h<=44; 方程位置 h=0..40; J=1..4; 两尺度堆叠; 精确整数; 精确有理零空间
# 【判定】∃ c ∈ Z^{J+1}: M c = 0, c_J = 1  （⛔ 不仅报 dim ker > 0）
# 【不做】J>4 / X>1e7 / h>44 / 第三尺度 / 新统计量 / 参数优化 / 事后改 S4
import numpy as np
from sympy import Matrix, Rational, linsolve, symbols, nsimplify
import time

N2 = 10**7
HMAX = 44          # 数据范围（方案 A）
HROW = 40          # 方程位置 h=0..40
print("=== RUN-1 :: 卡 1 移位除数和递推判定 ==="); print(f"数据 h<= {HMAX}；方程 h=0..{HROW}；J=1..4；X=1e6,1e7")
t0 = time.time()
print("[1] 计算除数个数 d(n), n<=1e7+44（numpy 筛）...")
d = np.zeros(N2 + HMAX + 1, dtype=np.int32)
for i in range(1, N2 + HMAX + 1):
    d[i::i] += 1
print(f"    完成 d 表，用时 {time.time()-t0:.1f}s；抽查 d(1..8)={list(d[1:9])} d(1e7)={int(d[N2])}")

def Xvec(N):
    v = np.empty(HMAX + 1, dtype=np.int64)
    a = d[1:N+1].astype(np.int64)
    for h in range(HMAX + 1):
        b = d[1+h:N+1+h].astype(np.int64)
        v[h] = int(np.dot(a, b))
    return v

print("[2] 计算 X^{(1)}（N=1e6）与 X^{(2)}（N=1e7），h=0..44（精确整数）...")
X1 = Xvec(10**6); X2 = Xvec(N2)
print("    X^{(1)}[0..6] =", list(map(int, X1[:7])))
print("    X^{(2)}[0..6] =", list(map(int, X2[:7])))
print("    X^{(1)}[41..44] =", list(map(int, X1[41:])))
print("    X^{(2)}[41..44] =", list(map(int, X2[41:])))

print("\n[3] 逐 J 构造堆叠系统 M（82×(J+1)）并做精确有理零空间与首一整系数判定")
for J in range(1, 5):
    rows = []
    for h in range(HROW + 1):
        rows.append([int(X1[h + j]) for j in range(J + 1)] + [int(X2[h + j]) for j in range(J + 1)])
    # 列顺序：先尺度1的 J+1 列，再尺度2的 J+1 列 —— 需 c 同时作用于两尺度 ⟹ 列应为 c_j 共用：
    # 正确构造：[X1[h+j]] 与 [X2[h+j]] 共用同一 c ⟹ 行块堆叠
    M1 = Matrix([[int(X1[h + j]) for j in range(J + 1)] for h in range(HROW + 1)])
    M2 = Matrix([[int(X2[h + j]) for j in range(J + 1)] for h in range(HROW + 1)])
    M = M1.col_join(M2)
    r = M.rank(); k = (J + 1) - r
    print(f"  --- J={J} ---   M 尺寸={M.shape}  rank_Q(M)={r}  dim ker_Q={k}")
    # 首一条件：c_J = 1 ⟹ 增广一行 e_J
    eJ = [0] * (J + 1); eJ[J] = 1
    A = Matrix([list(row) for row in M.tolist()] + [eJ])
    b = [0] * M.rows + [1]
    sol = linsolve((A, Matrix(b)), symbols(f'c0:{J+1}'))
    sol = list(sol)
    if not sol:
        print(f"      ∃c (Mc=0, c_J=1) = **否**（增广系统无解 ⟹ 不存在首一整系数递推）")
    else:
        s = sol[0]
        free = [v for v in s if v.free_symbols]
        print(f"      增广系统有解；自由参数个数={len(set().union(*[v.free_symbols for v in s])) if any(v.free_symbols for v in s) else 0}")
        print(f"      解族 = {s}")
        if not free:
            ints = all(v.q == 1 for v in s)
            print(f"      唯一解，整性={ints} ⟹ ∃c∈Z^{J+1} = **{'是' if ints else '否'}**；c = {[int(v) for v in s] if ints else None}")
        else:
            # 自由参数存在：在 Z 上判定存在性（对自由参数取小整数做完备性受限的检验；并标注为待 HNF 严格判定）
            found = None
            import itertools
            fs = sorted(set().union(*[v.free_symbols for v in s])) if any(v.free_symbols for v in s) else []
            for vals in itertools.product(range(-3, 4), repeat=len(fs)):
                sub = dict(zip(fs, vals))
                cand = [v.subs(sub) for v in s]
                if all(v.q == 1 for v in cand):
                    found = [int(v) for v in cand]; break
            print(f"      自由参数 {fs}；小范围整数扫描 ⟹ 找到整解 = {found}（若 None：需 HNF 严格判定，本轮不扩参）")
print(f"\n总用时 {time.time()-t0:.1f}s")
