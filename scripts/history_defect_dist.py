#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 最小 history algebra: rewrite 距离 d(H1,H2)
# 项 = 算术表达式 (数字原子 + 二元 +,×)
# rewrite (可逆): 结合律 (+ 与 ×) 可选分配律
# 问: d(2×3, 3×2) 是否非平凡 (不可消除的历史差异)
from functools import lru_cache
from collections import deque

# 表达式表示为嵌套元组: ('+', a, b) ('*', a, b) 或 int
def norm(e):
    """结合规范形: 同一 op 的链右结合 (不交换!): x*(y*z) 为规范"""
    if isinstance(e, int):
        return e
    op, a, b = e
    a, b = norm(a), norm(b)
    # 若 a 是 (op, a1, a2) 则重排: (op,a1,a2) op b -> a1 op (a2 op b)
    while not isinstance(a, int) and a[0] == op:
        a1, a2 = a[1], a[2]
        a, b = a1, (op, a2, b)
    return (op, a, b)

def size(e):
    if isinstance(e, int):
        return 1
    return 1 + size(e[1]) + size(e[2])

def all_sub(e):
    """所有子表达式位置 (含自身)"""
    res = []
    def walk(t, path):
        res.append((path, t))
        if not isinstance(t, int):
            walk(t[1], path + (1,))
            walk(t[2], path + (2,))
    walk(e, ())
    return res

def replace(e, path, new):
    """在 path 处替换为 new"""
    if not path:
        return new
    op, a, b = e
    if path[0] == 1:
        return (op, replace(a, path[1:], new), b)
    return (op, a, replace(b, path[1:], new))

def expand_assoc(e):
    """结合律的所有一步展开: (x op y) op z <-> x op (y op z)"""
    if isinstance(e, int):
        return []
    res = []
    op, a, b = e
    # 在 a 或 b 中递归
    for sub_path, sub in all_sub(e):
        if not isinstance(sub, int) and sub[0] == op and not isinstance(sub[1], int) and sub[1][0] == op:
            # (x op y) op z -> x op (y op z)   (子树的顶层是 op 且左孩子也是 op)
            _, x, yz = sub
            _, x2, y = x  # x = (x2 op y)?? 不对, sub = (op, (op,x,y), z)
            # sub = (op, L, R) with L = (op, x, y): (x op y) op R -> x op (y op R)
            L, R = sub[1], sub[2]
            if L[0] == op:
                x, y = L[1], L[2]
                newsub = (op, x, (op, y, R))
                res.append(norm(replace(e, sub_path, newsub)))
        if not isinstance(sub, int) and sub[0] == op and not isinstance(sub[2], int) and sub[2][0] == op:
            # x op (y op z) -> (x op y) op z
            L, R = sub[1], sub[2]
            if R[0] == op:
                y, z = R[1], R[2]
                newsub = (op, (op, L, y), z)
                res.append(norm(replace(e, sub_path, newsub)))
    return res

def apply_distrib(e):
    """分配律: a×(b+c) -> a×b + a×c  (单向展开, 可逆时加反方向)"""
    if isinstance(e, int):
        return []
    res = []
    for sub_path, sub in all_sub(e):
        if not isinstance(sub, int) and sub[0] == '*':
            L, R = sub[1], sub[2]
            if not isinstance(R, int) and R[0] == '+':
                a, b, c = L, R[1], R[2]
                newsub = ('+', ('*', a, b), ('*', a, c))
                res.append(norm(replace(e, sub_path, newsub)))
            if not isinstance(L, int) and L[0] == '+':
                b, c, a = L[1], L[2], R
                newsub = ('+', ('*', b, a), ('*', c, a))
                res.append(norm(replace(e, sub_path, newsub)))
    return res

def apply_distrib_rev(e):
    """分配律反向: a×b + a×c -> a×(b+c)"""
    if isinstance(e, int):
        return []
    res = []
    for sub_path, sub in all_sub(e):
        if not isinstance(sub, int) and sub[0] == '+':
            L, R = sub[1], sub[2]
            if not isinstance(L, int) and not isinstance(R, int) and L[0] == '*' and R[0] == '*':
                a1, b1 = L[1], L[2]
                a2, c1 = R[1], R[2]
                if a1 == a2:
                    newsub = ('*', a1, ('+', b1, c1))
                    res.append(norm(replace(e, sub_path, newsub)))
                elif b1 == c1:  # a*b + c*b
                    newsub = ('*', ('+', a1, a2), b1)
                    res.append(norm(replace(e, sub_path, newsub)))
    return res

def neighbors(e, use_distrib=False):
    """所有一步 rewrite 邻接 (可逆): 在结合规范形上应用分配"""
    res = set()
    if use_distrib:
        for n in apply_distrib(e):
            res.add(norm(n))
        for n in apply_distrib_rev(e):
            res.add(norm(n))
    return res

def bfs_dist(start, target, use_distrib=False, maxnodes=200000):
    """最短可逆 rewrite 距离; 返回 None 表示不可达 (超限)"""
    if start == target:
        return 0
    seen = {start: 0}
    q = deque([start])
    while q:
        e = q.popleft()
        d = seen[e]
        if d > 12:
            continue
        for n in neighbors(e, use_distrib):
            if n not in seen:
                if n == target:
                    return d + 1
                seen[n] = d + 1
                if len(seen) > maxnodes:
                    return None  # 爆炸: 视为不可达/超限
                q.append(n)
    return None

def show(e):
    if isinstance(e, int):
        return str(e)
    op = '+' if e[0] == '+' else '*'
    if isinstance(e[1], tuple):
        a = show(e[1])
    else:
        a = str(e[1])
    if isinstance(e[2], tuple):
        b = show(e[2])
    else:
        b = str(e[2])
    return f"({a}{op}{b})"

if __name__ == "__main__":
    import sys
    tests = [
        ("2×3 vs 3×2", ('*', 2, 3), ('*', 3, 2)),
        ("2×3×5 vs 3×2×5", ('*', ('*', 2, 3), 5), ('*', ('*', 3, 2), 5)),
        ("2×3 vs 2×(1+2)", ('*', 2, 3), ('*', 2, ('+', 1, 2))),
    ]
    for name, a, b in tests:
        na, nb = norm(a), norm(b)
        # 只结合: 同结合类 <=> 同一规范形
        d0 = 0 if na == nb else None
        dd = bfs_dist(na, nb, use_distrib=True)
        print(f"{name}:")
        print(f"  项A = {show(na)}  项B = {show(nb)}")
        print(f"  只结合 rewrite: d = {d0}  ({'同结合类' if d0==0 else '不同结合类-不可达'})")
        print(f"  结合+分配 rewrite: d = {dd}")
        print()
