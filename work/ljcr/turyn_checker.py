#!/usr/bin/env python3
"""
独立复核 Turyn 指数界批量结果（第二套实现，算法与主实现有意不同）
  区别：
    · 素因子分解：改用试除至 10^6 的显式列表 + 剩余大因子判定（不经主脚本的缓存的同一路径）
    · exp(G)：用素指数向量取最大值合成 lcm（非直接 lcm 迭代）
    · 自共轭判定：改用"乘法阶 ord，再检验 p^{ord/2} ≡ -1 (mod m')"（等价形式）
    · 界比较：用分数形式 exp(P) * p^a <= |P| 避免指数比较
输出：与 turyn_resolved.json 的交集/差集。
"""
import json, re, math

D = json.load(open('unz/difference-sets-main/ds.json'))
pat = re.compile(r'DS\((\d+),(\d+),(\d+),\[([0-9,\s]*)\]\)')


def factorize(x):
    f = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def exp_of_group(G):
    """lcm(G) = 逐素取最大指数后合成"""
    maxe = {}
    for g in G:
        for p, e in factorize(g).items():
            if e > maxe.get(p, 0):
                maxe[p] = e
    v = 1
    for p, e in maxe.items():
        v *= p ** e
    return v


def is_selfconj(p, m):
    m2 = m
    while m2 % p == 0:
        m2 //= p
    if m2 == 1:
        return True
    # 乘法阶
    ordr = 1
    cur = p % m2
    if cur == 0:
        return False
    while cur != 1:
        cur = (cur * p) % m2
        ordr += 1
        if ordr > m2:
            return False
    if ordr % 2 != 0:
        return False
    # p^{ord/2} ≡ -1 ?
    h = pow(p, ordr // 2, m2)
    return h == m2 - 1


res = []
for name, val in D.items():
    if val.get('status') != 'Open':
        continue
    m = pat.match(name)
    if not m:
        continue
    v, k, lam = int(m.group(1)), int(m.group(2)), int(m.group(3))
    G = [int(t) for t in m.group(4).split(',')] if m.group(4).strip() else []
    n = k - lam
    if n <= 0 or not G:
        continue
    fv = factorize(v)
    expG = exp_of_group(G)
    fG = {}
    for g in G:
        for p, e in factorize(g).items():
            fG[p] = fG.get(p, 0) + e
    for p in fv:
        a = 0
        while n % (p ** (2 * (a + 1))) == 0:
            a += 1
        if a < 1 or p not in fG:
            continue
        if not is_selfconj(p, expG):
            continue
        # 界：exp(P) <= |P|/p^a  ⟺  exp(P) * p^a <= |P|
        expP = p ** max(factorize(g).get(p, 0) for g in G)
        Psize = p ** fG[p]
        if expP * (p ** a) > Psize:
            res.append(name)
            break

prev = [x['name'] for x in json.load(open('turyn_resolved.json'))]
s1, s2 = set(prev), set(res)
print(f"主实现: {len(s1)} 格   独立实现: {len(s2)} 格")
print(f"交集: {len(s1 & s2)}")
print(f"仅主实现有: {sorted(s1 - s2)[:5]}")
print(f"仅独立实现有: {sorted(s2 - s1)[:5]}")
print("一致" if s1 == s2 else "★ 不一致，需排查")
