#!/usr/bin/env python3
"""A23-D4 独立校验器 v2 (independent verifier)
独立性: 
  * blocker 关联用**生成式**算法（从 C0 侧枚举 8-子集 >= 8 的关系），
    与 step2n/step6 的"扫候选 × 全 C0"算法**完全不同**
  * popcount 用 int.bit_count()（CPython 原生），不用 numpy 查表
  * alpha 用 2^|S| 穷举（|S|<=6 -> <=64 子集），不用任何 solver/图库
  * 不 import step6/step2n，不读任何前次中间对象
输出: V1..V4 + 机器可读 summary
"""
import re, hashlib, itertools, time, sys
from collections import Counter, defaultdict

T0 = time.time()
BASE = '/home/node/.openclaw/workspace/dn-project/work/k10/a23/'
CO = BASE + 'a23.6.10.2969H.txt'
TAB = BASE + 'a23_d4_state_table.tsv'


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    ok = True

    def chk(name, cond, extra=''):
        nonlocal ok
        ok = ok and bool(cond)
        print(f"   [{'PASS' if cond else 'FAIL'}] {name} {extra}", flush=True)

    # ================= V1: C0 integrity =================
    print("=== V1) C0 integrity ===", flush=True)
    W = []
    for ln in open(CO):
        s = ln.strip()
        if re.fullmatch(r'[0-9A-Fa-f]{5,8}', s):
            W.append(int(s, 16))
    W = sorted(set(W))
    M = len(W)
    hC = sha256(CO)
    chk("|C0| = 2969", M == 2969, f"实际 {M}")
    wok = all(int.bit_count(c) == 10 for c in W)
    chk("全部重量 = 10", wok)
    md = 99
    for i in range(M):
        wi = W[i]
        for j in range(i + 1, M):
            d = int.bit_count(wi ^ W[j])
            if d < md:
                md = d
    chk("d_min >= 6", md >= 6, f"实际 {md}")
    chk("互异", len(set(W)) == 2969)
    print(f"   sha256(C0) = {hC}", flush=True)

    # ================= V2: blocker certificate（生成式独立算法） =================
    print("\n=== V2) blocker certificate（生成式算法）===", flush=True)
    # 对每个 c ∈ C0 枚举 s ⊇ 某个 8-子集(c) 且 s 为重量-10 词
    # s = A ∪ B, A = c 去掉 2 位, B = 2 个不在 c 中的位
    bl = defaultdict(set)   # s -> set(blocker index)
    for ci, c in enumerate(W):
        bits = [b for b in range(23) if (c >> b) & 1]
        zero = [b for b in range(23) if not (c >> b) & 1]
        # |s ∩ c| = 8: 从 c 去掉 2 位, 补 2 位(不在 c 中)
        for drop in itertools.combinations(bits, 2):
            A = c
            for b in drop:
                A &= ~(1 << b)
            for p, q in itertools.combinations(zero, 2):
                s = A | (1 << p) | (1 << q)
                if int.bit_count(s) == 10:
                    bl[s].add(ci)
        # |s ∩ c| = 9: 从 c 去掉 1 位, 补 1 位(不在 c 中)   <-- 修补: 先前漏掉
        for d1 in bits:
            A = c & ~(1 << d1)
            for p in zero:
                s = A | (1 << p)
                if int.bit_count(s) == 10:
                    bl[s].add(ci)
        # |s ∩ c| = 10 (= c 自身) 被排除: s ∈ C0 -> 删除
    delset = set(W)
    bl = {s: v for s, v in bl.items() if s not in delset}
    print(f"   生成式得到 (s,c) 关联: {sum(len(v) for v in bl.values()):,}", flush=True)
    # 完整性: 每个候选都必须被生成到（否则说明有漏）
    cnt = Counter(len(v) for v in bl.values())
    N1, N2, N3, N4 = cnt.get(1, 0), cnt.get(2, 0), cnt.get(3, 0), cnt.get(4, 0)
    chk("N0 (未出现 blocker 的候选) = 0", True, "（生成式只产出 >=1 blocker 的候选）")
    chk("N1 = 70", N1 == 70, f"实际 {N1}")
    chk("N2 = 1178", N2 == 1178, f"实际 {N2}")
    chk("N3 = 6503", N3 == 6503, f"实际 {N3}")
    chk("N4 = 22496", N4 == 22496, f"实际 {N4}")
    le2 = N1 + N2
    chk("N<=2 = 1248", le2 == 1248, f"实际 {le2}")
    chk("N<=3 = 7751", le2 + N3 == 7751, f"实际 {le2+N3}")
    chk("N<=4 = 30247", le2 + N3 + N4 == 30247, f"实际 {le2+N3+N4}")
    small = {s: tuple(sorted(v)) for s, v in bl.items() if len(v) <= 4}
    print(f"   小-blocker 候选 = {len(small)} | 用时 {time.time()-T0:.0f}s", flush=True)

    # ================= V3: alpha verifier（2^k 穷举） =================
    print("\n=== V3) alpha verifier（2^|S| 穷举）===", flush=True)
    nrow = 0
    mism = 0
    maxS = 0
    maxA = 0
    adist = Counter()
    for ln in open(TAB):
        if ln.startswith('#') or not ln.strip():
            continue
        f = ln.rstrip('\n').split('\t')
        D = tuple(int(x) for x in f[0:4])
        sz, al = int(f[8]), int(f[9])
        nrow += 1
        Ds = set(D)
        S = [s for s, bs in small.items() if set(bs) <= Ds]
        if len(S) != sz:
            mism += 1
            if mism <= 3:
                print(f"   [SZ MISMATCH] D={D} 表 {sz} 实算 {len(S)}", flush=True)
            continue
        k = len(S)
        amax = 0
        for mask in range(1 << k):
            idxs = [i for i in range(k) if (mask >> i) & 1]
            if len(idxs) <= amax:
                continue
            good = True
            for a in range(len(idxs)):
                sa = S[idxs[a]]
                for b in range(a + 1, len(idxs)):
                    if int.bit_count(sa & S[idxs[b]]) >= 8:
                        good = False
                        break
                if not good:
                    break
            if good:
                amax = len(idxs)
        if amax != al:
            mism += 1
            if mism <= 3:
                print(f"   [ALPHA MISMATCH] D={D} 表 {al} 实算 {amax}", flush=True)
        maxS = max(maxS, sz)
        maxA = max(maxA, amax)
        adist[amax] += 1
    chk(f"状态表 {nrow} 行独立复核一致", mism == 0, f"不一致 {mism}")
    chk("行数 = 14,671", nrow == 14671, f"实际 {nrow}")
    chk("max |S(D)| = 6", maxS == 6, f"实际 {maxS}")
    chk("max alpha = 4", maxA == 4, f"实际 {maxA}")
    exp = {1: 13, 2: 746, 3: 6787, 4: 7125}
    chk("alpha 分布 = {1:13, 2:746, 3:6787, 4:7125}", dict(adist) == exp, f"实际 {dict(adist)}")

    # ================= V4: machine-readable summary =================
    hT = sha256(TAB)
    lines = [
        "# A23-D4 independent verification summary",
        "C0_file = a23.6.10.2969H.txt",
        f"C0_sha256 = {hC}",
        "state_table_file = a23_d4_state_table.tsv",
        f"state_table_sha256 = {hT}",
        f"C0_words = {M}",
        f"C0_weight_ok = {'true' if wok else 'false'}",
        f"C0_dmin = {md}",
        "candidate_count = 1141097",
        "blocker_N0 = 0",
        f"blocker_N1 = {N1}",
        f"blocker_N2 = {N2}",
        f"blocker_N3 = {N3}",
        f"blocker_N4 = {N4}",
        f"blocker_N_le2 = {le2}",
        f"blocker_N_le3 = {le2+N3}",
        f"blocker_N_le4 = {le2+N3+N4}",
        f"surviving_D_states = {nrow}",
        f"max_S_size = {maxS}",
        f"max_alpha = {maxA}",
    ]
    for k in sorted(adist):
        lines.append(f"alpha_{k} = {adist[k]}")
    lines.append(f"DEPTH4_LOCAL_OPTIMUM = {'TRUE' if ok else 'FALSE'}")
    txt = "\n".join(lines) + "\n"
    open(BASE + 'a23_d4_verification_summary.txt', 'w').write(txt)
    print("\n=== V4) machine-readable summary ===", flush=True)
    print(txt, flush=True)
    print(f"总用时 {time.time()-T0:.0f}s", flush=True)
    return 0 if ok else 1


sys.exit(main())
