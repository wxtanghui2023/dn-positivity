#!/usr/bin/env python3
"""
B-LJCR-1 batch check: apply the Chen-Xiang-Sehgal exponent bound
   (Schmidt, "Difference Sets: an Update", Theorem 4.4:
    G abelian p-group with p = 3 mod 4, |G| = p^m, exp(G) = p^s;
    if G admits a skew Paley-Hadamard difference set and s >= 2 then s <= (m+1)/4)
to every OPEN cell of the LJCR difference-set database whose parameters are of
skew-Paley-Hadamard type (v,k,lam) = (4n-1, 2n-1, n-1) and whose group is an
abelian p-group with p = 3 (mod 4).  Cells violating the bound are NO.
Output: cxs_resolved.json + summary.
"""
import json, re, sys, time

T0 = time.time()
LIM = 100000
# sieve of primes up to LIM
sieve = bytearray([1]) * (LIM + 1)
sieve[0:2] = b"\x00\x00"
for i in range(2, int(LIM ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
PRIMES = [i for i in range(2, LIM + 1) if sieve[i]]
print(f"[{time.time()-T0:.1f}s] 素数筛完成，共 {len(PRIMES)} 个", flush=True)


def factor(x):
    """return dict prime->exponent"""
    f = {}
    for p in PRIMES:
        if p * p > x:
            break
        while x % p == 0:
            f[p] = f.get(p, 0) + 1
            x //= p
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


print(f"[{time.time()-T0:.1f}s] 读取 ds.json ...", flush=True)
d = json.load(open('unz/difference-sets-main/ds.json'))
print(f"[{time.time()-T0:.1f}s] 条目 {len(d)}", flush=True)

pat = re.compile(r'DS\((\d+),(\d+),(\d+),\[([0-9,\s]*)\]\)')
tot_open = pgroup_open = 0
resolved = []
cache = {}
for name, val in d.items():
    if val.get('status') != 'Open':
        continue
    tot_open += 1
    m_ = pat.match(name)
    if not m_:
        continue
    v, k, lam = int(m_.group(1)), int(m_.group(2)), int(m_.group(3))
    if not (k == 2 * lam + 1 and v == 4 * lam + 3):      # skew Paley-Hadamard type
        continue
    G = [int(x) for x in m_.group(4).split(',')] if m_.group(4).strip() else []
    if not G:
        continue
    facs = {}
    for g in G:
        if g not in cache:
            cache[g] = factor(g)
        for p, e in cache[g].items():
            facs[p] = facs.get(p, 0) + e          # exponents add over the product
    if len(facs) != 1:                             # not a p-group
        continue
    p, m = next(iter(facs.items()))
    if p % 4 != 3:
        continue
    pgroup_open += 1
    s = max(cache[g].get(p, 0) for g in G)         # exp(G) = p^s, s = max exponent
    if s >= 2 and s > (m + 1) // 4:
        resolved.append((name, v, k, lam, tuple(G), p, m, s))

print(f"[{time.time()-T0:.1f}s] Open 总数 = {tot_open}")
print(f"其中 SHDS 型且为 p-群(p≡3 mod 4) 的 Open 格 = {pgroup_open}")
print(f"⭐ 被 CXS 指数界判为 No 的格 = {len(resolved)}")
print("\n前 30 个（按 v 升序）：")
for r in sorted(resolved, key=lambda x: (x[1], x[4]))[:30]:
    print(f"   v={r[1]:6d} k={r[2]:5d} λ={r[3]:5d} G={str(r[4]):24s} p={r[5]} m={r[6]} s={r[7]}   (m+1)/4={(r[6]+1)/4}")
json.dump([{"name": r[0], "v": r[1], "k": r[2], "lam": r[3], "G": list(r[4]), "p": r[5], "m": r[6], "s": r[7]}
           for r in resolved], open('cxs_resolved.json', 'w'), indent=1)
print(f"[{time.time()-T0:.1f}s] 已写 cxs_resolved.json")
