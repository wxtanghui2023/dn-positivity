#!/usr/bin/env python3
# 完整最小系统: 数字 = 1 的加链 (n <-> 1+1+...+1), 结合, 分配 (无交换)
# 问: 2×3 与 3×2 是否可达? d? 缺陷是否被展开+分配消除?
from collections import deque

def norm(e):
    """结合规范形 (右结合)"""
    if isinstance(e, int):
        return e
    op, a, b = e
    a, b = norm(a), norm(b)
    while not isinstance(a, int) and a[0] == op:
        a1, a2 = a[1], a[2]
        a, b = a1, (op, a2, b)
    return (op, a, b)

def all_sub(e):
    res = []
    def walk(t, path):
        res.append((path, t))
        if not isinstance(t, int):
            walk(t[1], path + (1,))
            walk(t[2], path + (2,))
    walk(e, ())
    return res

def replace(e, path, new):
    if not path:
        return new
    op, a, b = e
    if path[0] == 1:
        return (op, replace(a, path[1:], new), b)
    return (op, a, replace(b, path[1:], new))

def expand_num(e, NMAX=6):
    """数字 n <-> 1 的加链 (n = 1+(1+(...)))"""
    if isinstance(e, int):
        return []
    res = []
    for sub_path, sub in all_sub(e):
        if isinstance(sub, int) and 2 <= sub <= NMAX:
            # n -> 加链: n = 1+(n-1)
            chain = 1
            for _ in range(sub - 1):
                chain = ('+', 1, chain) if isinstance(chain, int) or chain[0] != '+' else chain
            # 直接构建 n 个 1 的右结合加链
            c = 1
            for _ in range(sub - 1):
                c = ('+', 1, c)
            res.append(norm(replace(e, sub_path, c)))
            # 加链 -> n (反向: 子树是纯 1 加链且长度 = sub)
    return res

def collapse_num(e):
    """纯 1 的加链 -> 数字 (n 个 1 -> n)"""
    if isinstance(e, int):
        return []
    res = []
    for sub_path, sub in all_sub(e):
        # 检查 sub 是否是纯 1 加链
        cnt = count_ones(sub)
        if cnt is not None and cnt >= 2 and not isinstance(sub, int):
            res.append(norm(replace(e, sub_path, cnt)))
    return res

def count_ones(e):
    """若 e 是纯 1 的 + 链返回长度, 否则 None"""
    if e == 1:
        return 1
    if isinstance(e, int):
        return None
    if e[0] == '+':
        a, b = count_ones(e[1]), count_ones(e[2])
        if a is not None and b is not None:
            return a + b
    return None

def apply_distrib(e):
    if isinstance(e, int):
        return []
    res = []
    for sub_path, sub in all_sub(e):
        if not isinstance(sub, int) and sub[0] == '*':
            L, R = sub[1], sub[2]
            if not isinstance(R, int) and R[0] == '+':
                a, b, c = L, R[1], R[2]
                res.append(norm(replace(e, sub_path, ('+', ('*', a, b), ('*', a, c)))))
            if not isinstance(L, int) and L[0] == '+':
                b, c, a = L[1], L[2], R
                res.append(norm(replace(e, sub_path, ('+', ('*', b, a), ('*', c, a)))))
    return res

def apply_distrib_rev(e):
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
                    res.append(norm(replace(e, sub_path, ('*', a1, ('+', b1, c1)))))
                elif b1 == c1:
                    res.append(norm(replace(e, sub_path, ('*', ('+', a1, a2), b1))))
    return res

def apply_unit(e):
    """单位规则: 1×x <-> x, x×1 <-> x  (乘法单位; 加法单位 0 不存在)"""
    if isinstance(e, int):
        return []
    res = []
    for sub_path, sub in all_sub(e):
        if not isinstance(sub, int) and sub[0] == '*':
            L, R = sub[1], sub[2]
            if L == 1:
                res.append(norm(replace(e, sub_path, R)))
            elif R == 1:
                res.append(norm(replace(e, sub_path, L)))
    return res

def neighbors(e):
    res = set()
    for n in expand_num(e):
        res.add(n)
    for n in collapse_num(e):
        res.add(n)
    for n in apply_distrib(e):
        res.add(n)
    for n in apply_distrib_rev(e):
        res.add(n)
    for n in apply_unit(e):
        res.add(n)
    return res

def bfs_dist(start, target, maxdepth=14, maxnodes=300000):
    if start == target:
        return 0
    seen = {start: 0}
    q = deque([start])
    while q:
        e = q.popleft()
        d = seen[e]
        if d >= maxdepth:
            continue
        for n in neighbors(e):
            if n not in seen:
                if n == target:
                    return d + 1
                seen[n] = d + 1
                if len(seen) > maxnodes:
                    return None
                q.append(n)
    return None

def show(e):
    if isinstance(e, int):
        return str(e)
    op = '+' if e[0] == '+' else '*'
    a = show(e[1]) if isinstance(e[1], tuple) else str(e[1])
    b = show(e[2]) if isinstance(e[2], tuple) else str(e[2])
    return f"({a}{op}{b})"

if __name__ == "__main__":
    tests = [
        ("2×3 vs 3×2 (T2T3 vs T3T2)", ('*', 2, 3), ('*', 3, 2)),
        ("2×3 vs 1×6 (不同历史同值)", ('*', 2, 3), 6),
        ("2×3 vs 2+2+2 (乘历史 vs 加历史)", ('*', 2, 3), ('+', ('+', 2, 2), 2)),
        ("(1+1)×3 vs 2×3", ('*', ('+', 1, 1), 3), ('*', 2, 3)),
    ]
    for name, a, b in tests:
        na, nb = norm(a), norm(b)
        print(f"{name}:")
        print(f"  A = {show(na)}   B = {show(nb)}")
        d = bfs_dist(na, nb)
        print(f"  d(A,B) = {d if d is not None else '∞/超限'}")
        # 反向也测 (B -> A)
        d2 = bfs_dist(nb, na)
        print(f"  d(B,A) = {d2 if d2 is not None else '∞/超限'}")
        print()
