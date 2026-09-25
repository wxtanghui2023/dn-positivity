#!/usr/bin/env python3
"""
B1-b 引擎：以 120-码为中心，用 owner-set 结构做"删除—补入"结构化枚举。
目标：找 D（|D|=d）使 C' = (C120 \\ D) ∪ A 为 119-码，即 |A| = d-1 且 A 覆盖 U(D)。

关键结构（已由 b1b_layers.py 提取）：
  U(D) = { v : S(v) ⊆ D, S(v) ≠ ∅ }   ← 只有"全部 owner 都被删"的点才需新字覆盖
  对 v ∈ U(D)：覆盖 v 的 11 个候选字 (v 及其 10 个邻居) 全部 ∉ (C120 \\ D)  ✓（否则 v 不会被"全部删光"）
  必要性:  |U(D)| <= 11*(d-1)   （要降到 119 只有 d-1 个新字，每字最多覆盖 11 点）

输出：每个 d 的最优 |A| 统计；若存在 |A| <= d-1 ⟹ 发现 119-码（再由独立 verifier 复核）。
"""
import itertools, json, sys, time
from math import comb

WORDS = sorted(set(int(t, 2) for t in open('kamenetsky120.txt').read().split()
                   if len(t) == 10 and set(t) <= {'0', '1'}))
assert len(WORDS) == 120
CODE = set(WORDS)
N = 1024
FULL = (1 << N) - 1

# 每个字的半径-1 球（1024 点掩码）
BALL = []
for w in WORDS:
    m = 1 << w
    for i in range(10):
        m |= 1 << (w ^ (1 << i))
    BALL.append(m)

# owner 集合
owners = [[] for _ in range(N)]
for idx, w in enumerate(WORDS):
    owners[w].append(idx)
    for i in range(10):
        owners[w ^ (1 << i)].append(idx)

# 按 owner 集合精确分层
from collections import defaultdict
byowners = defaultdict(int)
for v in range(N):
    byowners[frozenset(owners[v])] |= (1 << v)
LAYER = [(k, mask) for k, mask in byowners.items()]
LAYER.sort(key=lambda t: len(t[0]))
print(f"层数 = {len(LAYER)}；最大 owner 基数 = {max(len(k) for k, _ in LAYER)}", flush=True)

# 索引查表：按 word-index 组合直接取掩码
IDX = {w: i for i, w in enumerate(WORDS)}
L1 = defaultdict(int); P2 = defaultdict(int); P3 = defaultdict(int); P4 = defaultdict(int); P5 = defaultdict(int)
for k, mask in LAYER:
    ii = tuple(sorted(k))   # k 已是 word-index 的集合
    if len(ii) == 1: L1[ii[0]] |= mask
    elif len(ii) == 2: P2[ii] |= mask
    elif len(ii) == 3: P3[ii] |= mask
    elif len(ii) == 4: P4[ii] |= mask
    elif len(ii) == 5: P5[ii] |= mask
    else: raise SystemExit("max owner 基数意外 >5")

ALLV = (1 << N) - 1


def U_of(D):
    """U(D)：按 word-index 组合查表，O(C(d,≤5)) 次 OR"""
    u = 0
    for i in D:
        u |= L1[i]
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


def U_of(D):
    """U(D) = 所有 owner 集 ⊆ D 的点"""
    Ds = set(D)
    u = 0
    for k, mask in LAYER:
        if k <= Ds:
            u |= mask
    return u


def dist_ge3_packing(pts, cap):
    """贪心给出 U 中两两距离>=3 的点数下界（>cap 即可剪枝）——用 K=3 packing 近似"""
    # 距离<=2 的点集：v 的 K=2 球
    cnt = 0
    remaining = pts
    while remaining and cnt <= cap:
        v = (remaining & -remaining).bit_length() - 1
        nxt = 0
        t = remaining
        while t:
            u = (t & -t).bit_length() - 1
            t &= t - 1
            if (u ^ v).bit_count() <= 2:
                continue
            nxt |= 1 << u
        remaining &= nxt
        cnt += 1
    return cnt


def min_cover(U, max_k, Dset):
    """精确求覆盖 U 所需最少新字数；>max_k 或不可达则返回 >max_k 的值。"""
    # 候选：所有不在 (C120 \\ D) 中的字；对 v ∈ U，其 11 个候选全部可用
    wordmask_remaining = 0
    for i, w in enumerate(WORDS):
        if i not in Dset:
            wordmask_remaining |= 1 << i

    def cands_for(v):
        out = []
        for i in range(10 + 1):
            w = v ^ ((1 << (i - 1)) if i > 0 else 0)
            if w in CODE_INDEX and (wordmask_remaining >> CODE_INDEX[w]) & 1:
                continue          # 该字仍在码中，不可能
            out.append(w)
        return out

    best = [max_k + 1]

    def dfs(unc, used):
        if unc == 0:
            best[0] = min(best[0], used)
            return
        if used >= best[0] or used >= max_k:
            return
        # 选候选最少的未覆点
        t = unc
        best_v, best_c = -1, None
        while t:
            v = (t & -t).bit_length() - 1
            t &= t - 1
            c = cands_for(v)
            if best_c is None or len(c) < len(best_c):
                best_v, best_c = v, c
                if len(c) <= 1:
                    break
        for w_ in best_c:
            bm = 1 << w_
            for i in range(10):
                bm |= 1 << (w_ ^ (1 << i))
            dfs(unc & ~bm, used + 1)
    dfs(U, 0)
    return best[0]


CODE_INDEX = {w: i for i, w in enumerate(WORDS)}


def run(d, limit=None, verbose=True, i1_lo=0, i1_hi=119):
    t0 = time.time()
    stats = {"d": d, "tested": 0, "pruned_size": 0, "pruned_pack": 0, "need_lower": 0,
             "best_defect": None, "found": []}
    cap = 11 * (d - 1)
    n = 0
    for D in itertools.combinations(range(120), d):
        if D[0] < i1_lo:
            continue
        if D[0] > i1_hi:
            break          # combinations 按字典序，D[0] 单调不减
        n += 1
        if limit and n > limit:
            break
        U = U_of(D)
        if U == 0:
            continue
        stats["tested"] += 1
        pc = U.bit_count()
        if pc > cap:
            stats["pruned_size"] += 1
            continue
        if dist_ge3_packing(U, d - 1) > d - 1:
            stats["pruned_pack"] += 1
            continue
        # 需要 |A| <= d-1 才得 119
        k = min_cover(U, d - 1, set(D))
        if k <= d - 1:
            stats["found"].append({"D": list(D), "A_size": k})
            print(f"  ★ d={d} 发现 119-码！D={D} |A|={k}", flush=True)
        else:
            stats["need_lower"] += 1
        if verbose and stats["tested"] % 200000 == 0:
            print(f"  d={d} 已测 {stats['tested']:,} （{time.time()-t0:.0f}s）", flush=True)
    stats["seconds"] = round(time.time() - t0, 1)
    print(f"d={d}: tested={stats['tested']:,} pruned_size={stats['pruned_size']:,} "
          f"pruned_pack={stats['pruned_pack']:,} surv={stats['need_lower']:,} "
          f"found={len(stats['found'])} {stats['seconds']}s", flush=True)
    return stats


if __name__ == "__main__":
    args = sys.argv[1:]
    shard = None
    if args and ':' in args[0]:
        d, lo, hi = (int(x) for x in args[0].split(':'))
        res = run(d, i1_lo=lo, i1_hi=hi)
        json.dump([res], open(f'b1b_result_d{d}_shard{lo}_{hi}.json', 'w'), indent=1)
        print("已写 shard json")
        sys.exit(0)
    ds = [int(x) for x in args] or [1, 2, 3, 4]
    out = []
    for d in ds:
        out.append(run(d))
    json.dump(out, open(f'b1b_result_{"".join(str(x) for x in ds)}.json', 'w'), indent=1)
    print("已写结果 json")
