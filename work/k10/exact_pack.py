#!/usr/bin/env python3
"""
精确 packing 判定器：对失败例做 clique decision
  目标（d=4）：U_D 中是否存在 4 点两两 Hamming 距离 ≥ 3  ⟹ α₂(U_D) ≥ 4 ⟹ ρ(D) ≥ 4 > d−1=3
  目标（d=5）：是否存在 5 点  ⟹ α₂ ≥ 5 > 4
用法: python3 exact_pack.py <target> <fail.jsonl>
"""
import json, sys, time

WORDS = sorted(set(int(t, 2) for t in open('kamenetsky120.txt').read().split()
                   if len(t) == 10 and set(t) <= {'0', '1'}))
N = 1024
owners = [[] for _ in range(N)]
for i, w in enumerate(WORDS):
    owners[w].append(i)
    for b in range(10):
        owners[w ^ (1 << b)].append(i)
from collections import defaultdict
_L = {}
for v in range(N):
    k = frozenset(owners[v])
    _L[k] = _L.get(k, 0) | (1 << v)
IDXn = {w: i for i, w in enumerate(WORDS)}
Lv1, P2, P3, P4, P5 = (defaultdict(int) for _ in range(5))
for k, m in _L.items():
    ii = tuple(sorted(k))
    if len(ii) == 1: Lv1[ii[0]] |= m
    elif len(ii) == 2: P2[ii] |= m
    elif len(ii) == 3: P3[ii] |= m
    elif len(ii) == 4: P4[ii] |= m
    elif len(ii) == 5: P5[ii] |= m
import itertools


def U_of(D):
    u = 0
    for i in D:
        u |= Lv1[i]
    if len(D) >= 2:
        for pr in itertools.combinations(D, 2):
            u |= P2.get(pr, 0)
    if len(D) >= 3:
        for tr in itertools.combinations(D, 3):
            u |= P3.get(tr, 0)
    if len(D) >= 4:
        for qd in itertools.combinations(D, 4):
            u |= P4.get(qd, 0)
    if len(D) >= 5:
        for qn in itertools.combinations(D, 5):
            u |= P5.get(qn, 0)
    return u


def has_clique(pts, target):
    """pts 中是否存在 target 个点两两距离 >= 3（精确，bitset B&B）"""
    n = len(pts)
    if n < target:
        return False
    # 兼容邻接位掩码
    adj = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if (pts[i] ^ pts[j]).bit_count() >= 3:
                adj[i] |= 1 << j
                adj[j] |= 1 << i

    def rec(cand, need):
        if need == 0:
            return True
        if cand.bit_count() < need:
            return False
        # 选度数最小的候选点分支
        t = cand
        while t:
            v = (t & -t).bit_length() - 1
            t &= t - 1
            if rec(cand & adj[v], need - 1):
                return True
            cand &= ~(1 << v)          # 排除 v（已试过）
            if cand.bit_count() < need:
                return False
        return False
    return rec((1 << n) - 1, target)


def main():
    target = int(sys.argv[1])
    path = sys.argv[2]
    t0 = time.time()
    n = ok = bad = 0
    examples_bad = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            D = r["D"]
            n += 1
            U = U_of(D)
            pts = [v for v in range(N) if (U >> v) & 1]
            if has_clique(pts, target):
                ok += 1
            else:
                bad += 1
                if len(examples_bad) < 10:
                    examples_bad.append({"D": D, "U_size": len(pts)})
            if n % 2000 == 0:
                print(f"  已查 {n} 例  ok={ok} bad={bad}  {time.time()-t0:.0f}s", flush=True)
    print(f"目标 {target}-clique: 总 {n} 例  PASS={ok}  FAIL={bad}  {time.time()-t0:.0f}s")
    if examples_bad:
        print("FAIL 示例:", examples_bad[:5])
    json.dump({"target": target, "n": n, "pass": ok, "fail": bad, "bad_examples": examples_bad},
              open(path.replace('.jsonl', f'_exact{target}.json'), 'w'), indent=1)


if __name__ == "__main__":
    main()
