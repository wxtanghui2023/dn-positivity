#!/usr/bin/env python3
"""
d=5 证书（SDR 版 · 断点续跑 · 低内存）
判据：对 D（|D|=5）若存在"每字一个私有点、两两距离>=3"的私有代表系(SDR)
      ⟹ 这些点都在 U_D 中 ⟹ α₂(U_D) >= 5 ⟹ ρ(D) >= 5 > d−1=4 ⟹ 该 D 无 119-补入
用法: python3 b1b_sdr_cert.py <d> <i1_lo> <i1_hi>
断点：每完成一个 D[0] 值，写入 state 文件；重启自动跳过。
"""
import itertools, json, os, sys, time

D_TARGET = int(sys.argv[1])
LO = int(sys.argv[2]); HI = int(sys.argv[3])
STATE = f'b1b_sdr_d{D_TARGET}_state_{LO}_{HI}.json'
OUT = f'b1b_sdr_d{D_TARGET}_{LO}_{HI}.json'

WORDS = sorted(set(int(t, 2) for t in open('kamenetsky120.txt').read().split()
                   if len(t) == 10 and set(t) <= {'0', '1'}))
N = 1024
owners = [[] for _ in range(N)]
for i, w in enumerate(WORDS):
    owners[w].append(i)
    for b in range(10):
        owners[w ^ (1 << b)].append(i)
P1 = {c: [v for v in range(N) if owners[v] == [c]] for c in range(120)}
# 预计算私有点两两距离（避免重复 xor）
P1D = {c: [[(a ^ b).bit_count() for b in P1[c]] for a in P1[c]] for c in range(120)}
print(f"[d={D_TARGET}] |P1| 范围 {min(len(x) for x in P1.values())}-{max(len(x) for x in P1.values())}", flush=True)

NODE_CAP = 4000


def sdr_ok(D, lists):
    """返回 True/False/None(超出节点预算)"""
    order = sorted(range(len(D)), key=lambda i: len(lists[i]))
    L = [lists[i] for i in order]
    nodes = [0]

    def rec(i, chosen):
        if i == len(L):
            return True
        nodes[0] += 1
        if nodes[0] > NODE_CAP:
            return None
        for v in L[i]:
            ok = True
            for x in chosen:
                if (v ^ x).bit_count() < 3:
                    ok = False
                    break
            if ok:
                r = rec(i + 1, chosen + [v])
                if r:
                    return r
        return False
    return rec(0, [])


done = set()
if os.path.exists(STATE):
    done = set(json.load(open(STATE)))
    print(f"  续跑：已完成 {len(done)} 个 i1 值", flush=True)

t0 = time.time()
tot = cert = fail = unknown = 0
fail_rows = []
fout = open(f'b1b_sdr_fail_d{D_TARGET}_{LO}_{HI}.jsonl', 'a')
for i1 in range(LO, HI + 1):
    if i1 in done:
        continue
    lists = [P1[c] for c in range(120)]
    for D in itertools.combinations(range(i1 + 1, 120), D_TARGET - 1):
        D = (i1,) + D
        tot += 1
        r = sdr_ok(D, lists)
        if r is True:
            cert += 1
        elif r is False:
            fail += 1
            fout.write(json.dumps({"D": list(D)}) + "\n")
        else:
            unknown += 1
            fout.write(json.dumps({"D": list(D), "unknown": True}) + "\n")
    done.add(i1)
    json.dump(sorted(done), open(STATE, 'w'))
    print(f"  i1={i1} 累计 tot={tot:,} cert={cert:,} fail={fail:,} unk={unknown:,} "
          f"{time.time()-t0:.0f}s", flush=True)

fout.close()
json.dump({"d": D_TARGET, "range": [LO, HI], "tot": tot, "cert": cert,
           "fail": fail, "unknown": unknown, "sec": round(time.time() - t0, 1)},
          open(OUT, 'w'), indent=1)
print(f"[d={D_TARGET} {LO}-{HI}] tot={tot:,} cert={cert:,} fail={fail:,} unk={unknown:,} "
      f"{time.time()-t0:.0f}s  ⟹ {OUT}", flush=True)
