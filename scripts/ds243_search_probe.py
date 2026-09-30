#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Z_3 x Z_9 x Z_9 中 (243,121,60)-差集之搜索探针（乘子约化到 σ-不变集，99 轨道）

σ: x ↦ 7x (逐分量), σ³=id；27 个不动点 + 72 个 3-轨道 = 99 轨道。
D 可取为 σ-不变（乘子定理 61）；|D| = 121；目标：每非零 z 恰 60 次。
局部搜索最小化 Σ_z (c_z − 60)²。
"""
import random, itertools, sys, time
from collections import defaultdict

G = [(a, b, c) for a in range(3) for b in range(9) for c in range(9)]
idx = {e: i for i, e in enumerate(G)}
M = 243
sig = lambda x: ((7 * x[0]) % 3, (7 * x[1]) % 9, (7 * x[2]) % 9)

# 轨道
seen = set(); orbits = []
for x in G:
    if x in seen: continue
    orb = []; y = x
    while y not in seen:
        seen.add(y); orb.append(y); y = sig(y)
    orbits.append(orb)
print(f"轨道数 = {len(orbits)}; 大小分布 = {sorted(set(len(o) for o in orbits))}", flush=True)

# 轨道内元素索引列表
orbidx = [[idx[e] for e in o] for o in orbits]
fixed = [i for i, o in enumerate(orbits) if len(o) == 1]
tri = [i for i, o in enumerate(orbits) if len(o) == 3]
print(f"不动点轨道 = {len(fixed)}; 3-轨道 = {len(tri)}; |D| 需 = 121", flush=True)

# 预计算: 每个 3-轨道内元素之差分布 + 轨道对之差贡献向量
# diffvec[O][O'] = dict z->count (z != 0)  其中 z = d - d'
def diff(u, v):
    return ((u[0] - v[0]) % 3, (u[1] - v[1]) % 9, (u[2] - v[2]) % 9)

# 对每个轨道对预计算 (unord) 贡献
paircontrib = {}
for i in range(len(orbits)):
    for j in range(i, len(orbits)):
        dv = defaultdict(int)
        for u in [G[idx[e]] for e in orbidx[i]]:
            for v in [G[idx[e]] for e in orbidx[j]]:
                z = diff(u, v)
                if z != (0, 0, 0):
                    dv[z] += 1
                if i != j:
                    z2 = diff(v, u)
                    if z2 != (0, 0, 0):
                        dv[z2] += 1
        paircontrib[(i, j)] = dv
print("轨道对贡献表已建", flush=True)

nz = [z for z in G if z != (0, 0, 0)]
nzidx = {z: t for t, z in enumerate(nz)}
# 贡献向量化
PC = {}
for (i, j), dv in paircontrib.items():
    vec = [0] * len(nz)
    for z, c in dv.items():
        vec[nzidx[z]] += c
    PC[(i, j)] = vec
print("向量化完成", flush=True)

# 初始解: 随机选轨道使 |D| ≈ 121
def rand_sel(rng):
    sel = set()
    size = 0
    order = fixed[:] + tri[:]
    rng.shuffle(order)
    for i in order:
        L = len(orbits[i])
        if size + L <= 121:
            sel.add(i); size += L
    return sel, size

def obj_contrib(sel):
    vec = [0] * len(nz)
    L = sorted(sel)
    for a in range(len(L)):
        i = L[a]
        vec_ii = PC[(i, i)]
        for t in range(len(nz)):
            vec[t] += vec_ii[t]
        for b in range(a + 1, len(L)):
            v = PC[(L[a], L[b])]
            for t in range(len(nz)):
                vec[t] += v[t]
    return vec

def objective(vec):
    return sum((c - 60) ** 2 for c in vec)

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
sel, size = rand_sel(rng)
print(f"初始 |D| = {size}", flush=True)
vec = obj_contrib(sel)
cur = objective(vec)
best = cur
best_sel = set(sel)
t0 = time.time()
LIMIT = 240.0
iters = 0
while time.time() - t0 < LIMIT:
    iters += 1
    # 随机移动: 交换 1 个不动点轨道 或 (1 个 3-轨道 vs 3 个不动点)
    move = rng.random()
    if move < 0.5 and fixed:
        add = rng.choice(fixed)
        if add in sel: continue
        # 需移除等量: 1 个不动点
        rem = rng.choice([f for f in fixed if f in sel] or [None])
        if rem is None: continue
        sel2 = (sel - {rem}) | {add}
    else:
        if not tri: continue
        a = rng.choice(tri)
        if a not in sel: continue
        rem = [f for f in fixed if f in sel]
        if len(rem) < 3: continue
        rs = rng.sample(rem, 3)
        sel2 = (sel - {a} - set(rs)) | set(rs[:0])
        added = False
        for f in fixed:
            if f not in sel2:
                sel2.add(f); added = True; break
        if len(sel2) != len(sel): pass
    nv = obj_contrib(sel2)
    nc = objective(nv)
    if nc <= cur or rng.random() < 0.02:
        sel, vec, cur = sel2, nv, nc
        if cur < best:
            best = cur; best_sel = set(sel)
            print(f"  [{time.time()-t0:.1f}s] 新最优 obj = {best}  (|D|={sum(len(orbits[i]) for i in best_sel)})", flush=True)
            if best == 0:
                print("  ⟹⟹ **找到差集 (obj=0)** ✓✓✓", flush=True)
                break
print(f"探针结束: iters={iters}, best obj={best}", flush=True)
print(f"best |D| = {sum(len(orbits[i]) for i in best_sel)}", flush=True)
