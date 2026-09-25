#!/usr/bin/env python3
"""B1-b 第一步：提取 120-码的 owner 结构与 multiplicity 分层。"""
import json, itertools, collections

words = []
for tok in open('kamenetsky120.txt').read().split():
    tok = tok.strip()
    if len(tok) == 10 and set(tok) <= {'0','1'}:
        words.append(int(tok, 2))
words = sorted(set(words))
N = 1024
assert len(words) == 120, len(words)
print(f"码字数 = {len(words)}；覆盖点数 = {N}")
# 覆盖检查
cov = [0]*N
for w in words:
    for i in range(10):
        cov[w ^ (1 << i)] += 1
    cov[w] += 1
assert min(cov) >= 1, "不是覆盖码"
# owner 集合
owners = [[] for _ in range(N)]
for idx, w in enumerate(words):
    for i in range(10+1):
        v = w ^ ((1 << (i-1)) if i > 0 else 0)
        owners[v].append(idx)
for v in range(N):
    owners[v].sort()
m = [len(o) for o in owners]
dist = collections.Counter(m)
print("multiplicity 分布:", dict(sorted(dist.items())))
print("max m =", max(m), "；m=1 点数 =", dist[1], "；Σm =", sum(m))
# 分层：L1/L2/L3...
layers = collections.defaultdict(list)
for v in range(N):
    layers[len(owners[v])].append(v)
for k in sorted(layers):
    print(f"  m={k}: {len(layers[k])} 点")
# 每字的私有点数 |P1(c)|
priv = collections.Counter()
for v in range(N):
    if len(owners[v]) == 1:
        priv[owners[v][0]] += 1
pv = sorted(priv.values())
print(f"|P1(c)| 分布: min={min(pv)} max={max(pv)} 中位={pv[len(pv)//2]}")
print(f"  私有数=0 的字: {sum(1 for c in range(120) if priv[c]==0)} / 120")
print(f"  私有数>=12 的字: {sum(1 for v in pv if v>=12)}")
# 分层掩码保存
def mask_of(vs):
    x = 0
    for v in vs: x |= (1 << v)
    return x
data = {
  "words": words,
  "owners": owners,
  "m": m,
  "L1": {str(c): mask_of([v for v in layers[1] if owners[v][0] == c]) for c in range(120)},
  "layers_count": {str(k): len(layers[k]) for k in sorted(layers)},
  "multiplicity": {str(k): dist[k] for k in sorted(dist)},
}
json.dump(data, open('b1b_layers.json','w'))
print("已写 b1b_layers.json")
