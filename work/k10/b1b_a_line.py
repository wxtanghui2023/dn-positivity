#!/usr/bin/env python3
"""
A 线：158 个 (d=3, τ=3) 近命中的完整结构分析（四层可证伪）
  L1 频率：全部极小 3-覆盖中每个字的出现次数（并拆分：重加/新字）
  L2 universal：∀D ∃A∋c ；并算 ∩_D ∪_{A∈S_D} A
  L3 forced：c ∈ ∩_{A∈S_D} A ；并算 ∩_D ∩_{A} A
  L4 为什么特殊：球的 U-交、是否为 orbit 代表（平移稳定子）
  L5 聚类：按 (|U_D|, owner-pattern, 覆盖型签名) 归并结构轨道
输出 JSON + 控制台摘要。
"""
import itertools, json
from collections import Counter, defaultdict

WORDS = sorted(set(int(t, 2) for t in open('kamenetsky120.txt').read().split()
                   if len(t) == 10 and set(t) <= {'0', '1'}))
CODE = set(WORDS)
N = 1024
BALL = {}
for w in range(N):
    m = 1 << w
    for b in range(10):
        m |= 1 << (w ^ (1 << b))
    BALL[w] = m

owners = [[] for _ in range(N)]
for i, w in enumerate(WORDS):
    owners[w].append(i)
    for b in range(10):
        owners[w ^ (1 << b)].append(i)
m_of = [len(o) for o in owners]
L1 = defaultdict(int)
for v in range(N):
    if len(owners[v]) == 1:
        L1[owners[v][0]] |= 1 << v


def pack_ge3(pts, cap):
    cnt, rem = 0, pts
    while rem and cnt <= cap:
        v = (rem & -rem).bit_length() - 1
        nxt = 0
        t = rem
        while t:
            u = (t & -t).bit_length() - 1
            t &= t - 1
            if (u ^ v).bit_count() > 2:
                nxt |= 1 << u
        rem &= nxt
        cnt += 1
    return cnt


def U_of(D):
    Ds = set(D)
    u = 0
    for v in range(N):
        S = owners[v]
        if S and set(S) <= Ds:
            u |= 1 << v
    return u


def covers_upto3(U, banned):
    """枚举所有 ≤3 字覆盖（完备，按最小未覆点分支）；banned = 不可用字集合"""
    out = set()

    def rec(unc, chosen):
        if unc == 0:
            out.add(tuple(sorted(chosen)))
            return
        if len(chosen) == 3:
            return
        v = (unc & -unc).bit_length() - 1
        for i in range(11):
            w = v ^ ((1 << (i - 1)) if i > 0 else 0)
            if w in banned or w in chosen:
                continue
            rec(unc & ~BALL[w], chosen + [w])
    rec(U, [])
    return sorted(out)


def main():
    # 1) 复现 158 个幸存 D（与引擎同判据：|∪L1| ≤ 22 且 packing ≤ 2）
    surv = []
    for D in itertools.combinations(range(120), 3):
        u1 = L1[D[0]] | L1[D[1]] | L1[D[2]]
        if u1.bit_count() > 22 or pack_ge3(u1, 2) > 2:
            continue
        U = U_of(D)
        if U == 0:
            continue
        surv.append((D, U))
    print(f"幸存 D = {len(surv)}", flush=True)

    allcovers_freq = Counter()      # 所有极小覆盖中（含重加）
    pure_freq = Counter()           # 仅"纯新字"覆盖中出现
    perD = []
    uni_union_all = None            # ∩_D ∪_A A
    forced_inter_all = None         # ∩_D ∩_A A
    pure_missing = 0
    for D, U in surv:
        Dwords = {WORDS[i] for i in D}
        banned = {w for i, w in enumerate(WORDS) if i not in D}   # C120 \ D
        Sv = covers_upto3(U, banned)
        Sv3 = [A for A in Sv if len(A) == 3]
        # 纯新（A ∩ C120 = ∅）
        banned_pure = banned | Dwords
        Svp = [A for A in covers_upto3(U, banned_pure) if len(A) == 3]
        if not Svp:
            pure_missing += 1
        for A in Sv3:
            allcovers_freq.update(A)
        for A in Svp:
            pure_freq.update(A)
        Uall = set().union(*[set(A) for A in Sv3]) if Sv3 else set()
        Aint = set(Sv3[0]).intersection(*[set(A) for A in Sv3]) if len(Sv3) > 1 else (set(Sv3[0]) if Sv3 else set())
        uni_union_all = Uall if uni_union_all is None else (uni_union_all & Uall)
        forced_inter_all = Aint if forced_inter_all is None else (forced_inter_all & Aint)
        perD.append({
            "D": list(D), "Dwords": sorted(Dwords), "U_size": U.bit_count(),
            "owner_sig": sorted(Counter(m_of[(U >> b & 1) and b or 0] for b in []) ) or None,
            "n_covers3": len(Sv3), "n_covers3_pure": len(Svp),
            "minsize": min(len(A) for A in Sv) if Sv else None,
            "readd_counts": sorted(Counter(len(set(A) & Dwords) for A in Sv3).items()),
            "new_counts": sorted(Counter(len(set(A) - CODE) for A in Sv3).items()),
            "cover_union_size": len(Uall), "cover_core_size": len(Aint),
        })
    print(f"纯新 3-覆盖缺失的 D 数 = {pure_missing}", flush=True)
    print("\n=== L1 频率：所有极小 3-覆盖（含重加）top20 ===")
    for w, c in allcovers_freq.most_common(20):
        print(f"  {w:4d}{'  (在码中, idx %s)' % WORDS.index(w) if w in CODE else '  (新字)'}  次数={c}")
    print(f"\n=== L1' 频率：仅纯新 3-覆盖 top20 ===")
    if pure_freq:
        for w, c in pure_freq.most_common(20):
            print(f"  {w:4d}{'  (新字)' if w not in CODE else '  (碼中)'}  次数={c}")
    else:
        print("  （无纯新 3-覆盖）")
    print(f"\n=== L2 universal：∩_D ∪_A A = {sorted(uni_union_all) if uni_union_all else '∅'}（大小 {len(uni_union_all) if uni_union_all else 0}）")
    print(f"=== L3 forced：∩_D ∩_A A = {sorted(forced_inter_all) if forced_inter_all else '∅'}（大小 {len(forced_inter_all) if forced_inter_all else 0}）")
    # L4 deep dive：对高频新字
    top_new = [w for w, _ in allcovers_freq.most_common(50) if w not in CODE][:6]
    print(f"\n=== L4 高频新字深挖 {top_new} ===")
    info = {}
    for w in top_new:
        hits = [p for p in perD if any(w == x for x in ())]  # placehold
        inter_sizes = []
        for D, U in surv:
            Dwords = {WORDS[i] for i in D}
            banned = {x for i, x in enumerate(WORDS) if i not in D}
            if w in banned:
                continue
            inter_sizes.append((BALL[w] & U).bit_count())
        info[w] = {"S_in_code": w in CODE, "n_cases_available": len(inter_sizes),
                   "inter_min": min(inter_sizes) if inter_sizes else None,
                   "inter_max": max(inter_sizes) if inter_sizes else None,
                   "inter_mean": round(sum(inter_sizes) / len(inter_sizes), 2) if inter_sizes else None}
        print(f"  {w}: {info[w]}")
    # L5 聚类
    sig = Counter((p["U_size"], p["minsize"], tuple(p["readd_counts"]), tuple(p["new_counts"])[:2]) for p in perD)
    print(f"\n=== L5 聚类：不同签名数 = {len(sig)} ===")
    for k, c in sig.most_common(10):
        print(f"  sig={k}  例数={c}")
    # 平移稳定子（orbit 判定工具）
    stab = [t for t in range(N) if {w ^ t for w in CODE} == CODE]
    print(f"\n=== 平移稳定子 |Stab| = {len(stab)} (含 0) ===")
    json.dump({"perD": perD, "freq_all": allcovers_freq.most_common(30),
               "freq_pure": pure_freq.most_common(30),
               "universal_union": sorted(uni_union_all) if uni_union_all else [],
               "forced_inter": sorted(forced_inter_all) if forced_inter_all else [],
               "deep": info, "stab": stab, "pure_missing": pure_missing},
              open('b1b_a_line.json', 'w'), indent=1)
    print("已写 b1b_a_line.json")


if __name__ == "__main__":
    main()
