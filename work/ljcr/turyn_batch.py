#!/usr/bin/env python3
"""
S2 批量核查：Turyn 指数界（一般 (v,k,λ) 差集，abelian G）
   Theorem 9.11 (Trout 2017 MSc thesis, UDel; 原文 Turyn 1965 Pacific J. Math. 15:319-346):
     G abelian, D a (v,k,λ)-DS, p | v prime, P = Sylow p-subgroup of G.
     Suppose ∃a ∈ N with p^{2a} | n (n = k - λ), and U ≤ G with U ∩ P = {1}.
     If p is self-conjugate modulo exp(G/U), then  exp(P) <= |U||P| / p^a.
   取 U = {1} 得最强形式：exp(P) <= |P| / p^a。
   违反者 ⟹ 该群不存在该参数的差集 ⟹ No。
输出: turyn_resolved.json + 统计。
"""
import json, re, time

T0 = time.time()
LIM = 200000
sieve = bytearray([1]) * (LIM + 1)
sieve[0:2] = b"\x00\x00"
for i in range(2, int(LIM ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
PR = [i for i in range(2, LIM + 1) if sieve[i]]


def fac(x):
    f = {}
    for p in PR:
        if p * p > x:
            break
        while x % p == 0:
            f[p] = f.get(p, 0) + 1
            x //= p
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)


def selfconj(p, m):
    """p self-conjugate modulo m  ⟺  ∃j: p^j ≡ -1 (mod m'), m' = p-free part of m"""
    mm = m
    while mm % p == 0:
        mm //= p
    if mm <= 1:
        return True
    x = p % mm
    seen = set()
    while x not in seen:
        if (x + 1) % mm == 0:
            return True
        seen.add(x)
        x = (x * p) % mm
    return False


pat = re.compile(r'DS\((\d+),(\d+),(\d+),\[([0-9,\s]*)\]\)')
print(f"[{time.time()-T0:.1f}s] 读 ds.json ...", flush=True)
d = json.load(open('unz/difference-sets-main/ds.json'))
print(f"[{time.time()-T0:.1f}s] {len(d)} 条", flush=True)

tot = 0
hadamard_open = 0
applic = 0
viol = []
facs_cache = {}
for name, val in d.items():
    if val.get('status') != 'Open':
        continue
    m = pat.match(name)
    if not m:
        continue
    v, k, lam = int(m.group(1)), int(m.group(2)), int(m.group(3))
    G = [int(x) for x in m.group(4).split(',')] if m.group(4).strip() else []
    n = k - lam
    if n <= 0 or not G:
        continue
    tot += 1
    if k == 2 * lam + 1 and v == 4 * lam + 3:
        hadamard_open += 1
    for g in G:
        if g not in facs_cache:
            facs_cache[g] = fac(g)
    fv = fac(v)
    fG = {}
    for g in G:
        for q, e in facs_cache[g].items():
            fG[q] = fG.get(q, 0) + e
    expG = 1
    for g in G:
        expG = lcm(expG, g)                      # exp(G) = lcm of invariant factors  ✓
    for p in fv:
        a = 0
        while n % (p ** (2 * (a + 1))) == 0:
            a += 1
        if a < 1:
            continue                              # 需 p^{2a} | n, a >= 1
        if p not in fG:
            continue
        mp = fG[p]
        s = max(facs_cache[g].get(p, 0) for g in G)   # exp(P) = p^s
        if not selfconj(p, expG):
            continue
        applic += 1
        if s > mp - a:
            viol.append({"name": name, "v": v, "k": k, "lam": lam, "G": G,
                         "p": p, "a": a, "mp": mp, "s": s,
                         "bound_logp": mp - a, "expP_logp": s})
print(f"[{time.time()-T0:.1f}s]")
print(f"Open 可解析格 = {tot}；其中 Hadamard 型 = {hadamard_open}")
print(f"Turyn 界假设成立（p|v, p^(2a)|n, a>=1, p 自共轭 mod exp(G)）= {applic} 例")
print(f"⭐ 违反 ⟹ 判 No 的格 = {len(viol)}")
json.dump(viol, open('turyn_resolved.json', 'w'), indent=1)
print(f"[{time.time()-T0:.1f}s] 已写 turyn_resolved.json")
