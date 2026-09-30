#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""筛 LJCR 差集库：status == "Open" 之最小 v 参数（Survivor 第 0 步）"""
import json, collections, sys

f = open('/tmp/ds.json', 'r')
D = json.load(f)
f.close()

cnt = collections.Counter()
opens = []
for name, rec in D.items():
    st = rec.get('status')
    cnt[st] += 1
    if st == 'Open':
        try:
            parts = name.split(',')
            v = int(parts[0].split('(')[1]); k = int(parts[1]); lam = int(parts[2])
            G = parts[3].split('[')[1].split(']')[0]
        except Exception:
            v = k = lam = None; G = '?'
        opens.append((v, k, lam, G, name, rec.get('comment', '')[:60]))

print(f"总条目 = {len(D)}")
print(f"status 分布 = {dict(cnt)}")
print()
print(f"Open 条目数 = {len(opens)}")
opens.sort(key=lambda t: (t[0] if t[0] is not None else 10**9))
print()
print("=== Open 之最小 v 前 15 个 ===")
for v, k, lam, G, name, cm in opens[:15]:
    print(f"  v={v:<6} k={k:<6} λ={lam:<5} G={G:<12} | {cm}")
print()
# 按 v 阈值统计
for thr in (100, 200, 500, 1000, 2000, 5000):
    print(f"  v <= {thr:<5}: Open 数 = {sum(1 for t in opens if t[0] is not None and t[0] <= thr)}")
