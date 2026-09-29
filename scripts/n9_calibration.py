#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""n=9 上界侧搜索校准（交接档 §5.4a / PLAN-119-DETAILED-V2 §U1）

判据：**从零**搜索得到覆盖 512/512 的 **62** 词码（真值 K(9,1)=62）
纪律：经 scripts/pyguard.sh 受控运行；纯 Python（无 numpy）；种子可复跑
产出：证书（码 + 覆盖核验 + 极小性）+ 读数
"""
import random, time, os, math

N = 9
Q = 1 << N                      # 512
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]    # 闭邻域，10 点
NBS = [frozenset(s) for s in NB]

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources",
                   "KERI-CD-K_9_1-the-optimal-9-62-binary-covering-code.txt")


def load_known(path):
    C = []
    for line in open(path):
        t = line.split()
        if len(t) != N:
            continue
        v = 0
        for i, b in enumerate(t):
            v |= (int(b) << i)
        C.append(v)
    return C


def counts(C):
    cnt = [0] * Q
    for v in C:
        for x in NB[v]:
            cnt[x] += 1
    return cnt


def report(C, tag=""):
    cnt = counts(C)
    unc = sum(1 for c in cnt if c == 0)
    red = []
    for v in C:
        if all(cnt[x] > 1 for x in NB[v]):
            red.append(v)
    E = sum(c - 1 for c in cnt if c >= 1)
    print(f"  {tag}|C|={len(C)} distinct={len(set(C))} 覆盖={Q-unc}/512 "
          f"未覆盖={unc} 可删词={len(red)} 过量E={E}")
    return Q - unc, unc, red, cnt


class State:
    __slots__ = ("inS", "cnt", "S", "U", "E")

    def __init__(self, S):
        self.inS = [False] * Q
        self.S = list(S)
        for v in self.S:
            self.inS[v] = True
        self.cnt = counts(self.S)
        self.U = sum(1 for c in self.cnt if c == 0)
        self.E = sum(c - 1 for c in self.cnt if c >= 1)

    def F(self):
        return self.U * 1000 + self.E

    def remove(self, v):
        self.S.remove(v)
        self.inS[v] = False
        for x in NB[v]:
            c = self.cnt[x]
            self.cnt[x] = c - 1
            if c == 1:
                self.U += 1
            else:
                self.E -= 1

    def add(self, v):
        self.S.append(v)
        self.inS[v] = True
        for x in NB[v]:
            c = self.cnt[x]
            self.cnt[x] = c + 1
            if c == 0:
                self.U -= 1
            else:
                self.E += 1

    def delta_swap(self, w, v):
        """当前态下 rem w -> add v 的 (dU, dE, dF)；重叠点净 Δ=0，故只走对称差"""
        Sw, Sv = NBS[w], NBS[v]
        du = de = 0
        for x in Sw:
            if x in Sv:
                continue
            c = self.cnt[x]
            if c == 1:
                du += 1
            else:                       # c>=2 -> c-1>=1
                de -= 1
        for x in Sv:
            if x in Sw:
                continue
            c = self.cnt[x]
            if c == 0:
                du -= 1
            else:                       # c>=1 -> c+1>=2
                de += 1
        return du, de, du * 1000 + de


def search(k, seed, iters=400000, t0=5.0, t1=0.02, tlimit=25.0, rep=50000, targ_p=0.5):
    """定基数的 1-for-1 退火搜索；返回 (State, 迭代数, 秒)"""
    rng = random.Random(seed)
    st = State(rng.sample(range(Q), k))
    T = t0
    t_start = time.time()
    it = 0
    for it in range(1, iters + 1):
        if it % rep == 0:
            print(f"      [it {it}] U={st.U} E={st.E} T={T:.4f} ({time.time()-t_start:.1f}s)", flush=True)
            T = max(t1, T * 0.4)
        if st.U > 0 and rng.random() < targ_p:
            x = rng.choice([z for z in range(Q) if st.cnt[z] == 0])
            cands = [u for u in NB[x] if not st.inS[u]]
            if not cands:
                continue
            v = rng.choice(cands)
            w = min(rng.sample(st.S, min(8, len(st.S))), key=lambda z: st.delta_swap(z, v)[2])
        else:
            w = rng.choice(st.S)
            v = rng.randrange(Q)
            if st.inS[v]:
                continue
        _, _, d = st.delta_swap(w, v)
        if d <= 0 or rng.random() < math.exp(-min(60.0, d / T)):
            st.remove(w)
            st.add(v)
        if st.U == 0:
            return st, it, time.time() - t_start
        if time.time() - t_start > tlimit:
            break
    return st, it, time.time() - t_start


def greedy_repair(st, rng, cap=120):
    """只加不删的贪心修复（用于算子检验）"""
    while st.U > 0 and len(st.S) < cap:
        x = rng.choice([z for z in range(Q) if st.cnt[z] == 0])
        best, bc = None, -1
        for v in NB[x]:
            if st.inS[v]:
                continue
            c = sum(1 for y in NB[v] if st.cnt[y] == 0)
            if c > bc:
                best, bc = v, c
        if best is None:
            break
        st.add(best)
    return st


def prune(st):
    """贪心删冗余词"""
    rng = random.Random(7)
    order = sorted(st.S, key=lambda v: sum(1 for x in NB[v] if st.cnt[x] == 1))
    for v in order:
        if v in st.inS and all(st.cnt[x] > 1 for x in NB[v]):
            st.remove(v)
    return st


def greedy_from_scratch(rng):
    unc = set(range(Q))
    S = []
    while unc:
        best, bc = None, -1
        for _ in range(500):
            v = rng.randrange(Q)
            c = len(NBS[v] & unc)
            if c > bc:
                best, bc = v, c
        S.append(best)
        unc -= NBS[best]
    return S


def main():
    t_all = time.time()
    print("=" * 74)
    print("§5.4a  n=9 上界侧搜索校准   |   判据：从零得 62 词覆盖（真值 62）")
    print("=" * 74)

    print("\n[0] 已知 62-码（锚点）核验")
    known = load_known(SRC)
    cov, unc, red, _ = report(known, "anchor: ")

    print("\n[1] 算子检验（方法①）：已知码删 3 词 ⟹ 贪心修复 ⟹ 剪冗余")
    for t in range(3):
        rng = random.Random(1000 + t)
        C = list(known)
        rng.shuffle(C)
        st = State(C[:-3])
        print(f"   删3后: U={st.U} |S|={len(st.S)}")
        greedy_repair(st, rng)
        if st.U == 0:
            prune(st)
            report(sorted(st.S), f" 试验{t+1} 修复后: ")
        else:
            print(f"   试验{t+1} 修复失败 U={st.U}")

    print("\n[2] 从零贪心读数（对照「现状 66」）")
    for sd in (1, 2, 3):
        g = greedy_from_scratch(random.Random(sd))
        report(g, f" greedy seed={sd}: ")

    print("\n[3] ★ 从零搜索：固定 k=62")
    found = None
    t0s = time.time()
    for seed in (11, 202, 3033, 40404, 555555, 6666666):
        if time.time() - t0s > 170:
            print("   [总预算用尽]")
            break
        print(f"   -- seed={seed} --", flush=True)
        st, it, dt = search(62, seed)
        print(f"      seed={seed}: U={st.U} E={st.E} iters={it} ({dt:.1f}s)", flush=True)
        if st.U == 0:
            found = (seed, sorted(st.S))
            break

    print("\n" + "=" * 74)
    if found:
        seed, S = found
        cov, unc, red, _ = report(S, "结果: ")
        common = len(set(S) & set(known))
        ok = (len(S) == 62 and unc == 0 and not red)
        print(f"★ 判据{'达成 ✓' if ok else '部分'}：|C|={len(S)} 覆盖={cov}/512 可删词={len(red)} "
              f"(seed={seed})；与锚点共同词数={common}/62")
        out = os.path.join(HERE, "..", "out")
        os.makedirs(out, exist_ok=True)
        p = os.path.join(out, "n9_62_search_certificate.txt")
        with open(p, "w") as f:
            f.write("# n=9 从零搜索所得 62 词覆盖证书\n")
            f.write(f"# seed={seed} |C|={len(S)} coverage={cov}/512 removable={len(red)} "
                    f"common_with_anchor={common}/62\n")
            for v in S:
                f.write(" ".join(str((v >> i) & 1) for i in range(N)) + "\n")
        print(f"  证书：{os.path.relpath(p)}")
    else:
        print("✗ 判据未达成（预算内未得 62 词覆盖）—— 读数为「搜索力不足」，非机制性结论")
    print(f"总耗时 {time.time()-t_all:.1f}s")


if __name__ == "__main__":
    main()
