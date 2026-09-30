#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Z_3 x Z_9 x Z_9 中 (243,121,60)-差集搜索（乘子约化 → 99 轨道；numpy 二次型）

c_z = y^T M_z y  (z 非零, 242 个)，M_z = 对称/2 + 对角。目标 Σ_z (c_z − 60)² = 0。
保持 |D| = 121 的移动：① 1 不动点 ↔ 1 不动点；② 1 个 3-轨道 ↔ 3 个不动点。
"""
import numpy as np, random, sys, time
from collections import defaultdict

G = [(a, b, c) for a in range(3) for b in range(9) for c in range(9)]
sig = lambda x: ((7 * x[0]) % 3, (7 * x[1]) % 9, (7 * x[2]) % 9)
seen = set(); orbits = []
for x in G:
    if x in seen: continue
    o = []; y = x
    while y not in seen:
        seen.add(y); o.append(y); y = sig(y)
    orbits.append(o)
NO = len(orbits)
sizes = np.array([len(o) for o in orbits])
fixed = [i for i in range(NO) if sizes[i] == 1]
tri = [i for i in range(NO) if sizes[i] == 3]
nz = [z for z in G if z != (0, 0, 0)]
nzidx = {z: t for t, z in enumerate(nz)}
print(f"轨道 {NO} 个（不动点 {len(fixed)}, 3-轨道 {len(tri)}）; 非零元 {len(nz)}", flush=True)

# 建 W[i][j] (i<=j) → 贡献向量（非零 z 计数）
W = np.zeros((NO, NO, len(nz)), dtype=np.int32)
diff = lambda u, v: ((u[0]-v[0]) % 3, (u[1]-v[1]) % 9, (u[2]-v[2]) % 9)
for i in range(NO):
    for j in range(i, NO):
        for u in orbits[i]:
            for v in orbits[j]:
                z = diff(u, v)
                if z != (0, 0, 0): W[i, j, nzidx[z]] += 1
                if i != j:
                    z2 = diff(v, u)
                    if z2 != (0, 0, 0): W[i, j, nzidx[z2]] += 1
print("W 建好", flush=True)

# 二次型: c = Σ_{i<j} y_i y_j W[i,j] + Σ_i y_i W[i,i]
#   令 A[i,j] = W[i,j] (i≠j, 对称), D[i] = W[i,i]
A = np.zeros((NO, NO, len(nz)), dtype=np.float32)
for i in range(NO):
    for j in range(i+1, NO):
        A[i, j] = W[i, j]; A[j, i] = W[i, j]
Diag = np.zeros((NO, len(nz)), dtype=np.float32)
for i in range(NO): Diag[i] = W[i, i]

def counts(y):
    # c = 0.5 y^T A y + y·Diag
    return 0.5 * np.einsum('i,ijz,j->z', y, A, y) + y @ Diag

def objective(c):
    d = c - 60.0
    return float(d @ d)

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
# 初始: 随机不动点 + 3-轨道，使 |D| = 121
def init():
    y = np.zeros(NO, dtype=np.float32)
    size = 0
    order = fixed[:]; rng.shuffle(order)
    for i in order:
        if size + 1 <= 121: y[i] = 1; size += 1
    order = tri[:]; rng.shuffle(order)
    for i in order:
        if size + 3 <= 121: y[i] = 1; size += 3
    return y, size

y, size = init()
c = counts(y); cur = objective(c); best = cur; besty = y.copy()
print(f"初始 |D| = {size}, obj = {cur:.0f}", flush=True)
t0 = time.time(); LIMIT = float(sys.argv[2]) if len(sys.argv) > 2 else 180.0
iters = 0; T = 200.0
while time.time() - t0 < LIMIT:
    iters += 1
    y2 = y.copy()
    if rng.random() < 0.5:
        a = rng.randrange(NO)
        if sizes[a] != 1: continue
        b = rng.randrange(NO)
        if sizes[b] != 1 or y2[b] == 1 or y2[a] == 0: continue
        y2[a] = 0; y2[b] = 1
    else:
        a = rng.randrange(NO)
        if sizes[a] != 3 or y2[a] == 0: continue
        fs = [f for f in fixed if y2[f] == 0]
        if len(fs) < 3: continue
        y2[a] = 0
        for f in rng.sample(fs, 3): y2[f] = 1
    c2 = counts(y2); nc = objective(c2)
    if nc <= cur or rng.random() < np.exp(-(nc-cur)/max(T, 1e-9)):
        y, c, cur = y2, c2, nc
        if cur < best:
            best = cur; besty = y2.copy()
            print(f"  [{time.time()-t0:.0f}s] obj={best:.0f} |D|={int(y2@sizes)}", flush=True)
            if best == 0:
                print("**找到 (243,121,60)-差集（σ-不变）** ✓✓✓", flush=True)
                print("D =", [e for i in range(NO) if besty[i] == 1 for e in orbits[i]], flush=True)
                break
    T *= 0.9997
print(f"结束: iters={iters}, best obj={best:.0f}, |D|={int(besty@np.array([len(o) for o in orbits]))}", flush=True)
