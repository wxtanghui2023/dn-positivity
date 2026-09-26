#!/usr/bin/env python3
"""A23-D4 Step 2 (numpy): 全候选 blocker census + 三道门；无 solver"""
import re, itertools, time, sys
import numpy as np
from collections import Counter, defaultdict
t0=time.time()
P='/home/node/.openclaw/workspace/dn-project/work/k10/a23/a23.6.10.2969H.txt'
W=[]
for ln in open(P):
    s=ln.strip()
    if re.fullmatch(r'[0-9A-Fa-f]{5,8}', s): W.append(int(s,16))
W=np.array(sorted(set(W)), dtype=np.uint32)
print(f"C0 = {len(W)} 词 ✓  用时 {time.time()-t0:.1f}s", flush=True)
TBL=np.array([bin(i).count('1') for i in range(256)], dtype=np.uint8)
pc1=lambda x:int(TBL[x&0xFF])+int(TBL[(x>>8)&0xFF])+int(TBL[(x>>16)&0xFF])+int(TBL[(x>>24)&0xFF])
print("重量:",sorted({pc1(int(c)) for c in W}), "| 最小距离抽样:", min(pc1(int(W[i]^W[j])) for i in range(0,200) for j in range(i+1,200)), flush=True)
# 全部 C(23,10)
allw=[]
for comb in itertools.combinations(range(23),10):
    m=0
    for b in comb: m|=1<<b
    allw.append(m)
allw=np.array(sorted(allw),dtype=np.uint32)
print(f"C(23,10) = {len(allw)} ✓", flush=True)
cand=np.setdiff1d(allw,W)
print(f"候选（非 C0）= {len(cand)}  (论文: 1,141,097) {'✓✓' if len(cand)==1141097 else '✗'}", flush=True)
np.save('/tmp/a23_cand.npy', cand)
# 分块 blocker 计算
def popcnt(A): return (TBL[A & 0xFF]+TBL[(A>>8)&0xFF]+TBL[(A>>16)&0xFF]+TBL[(A>>24)&0xFF]).sum(axis=1)
CH=1000; cnts=np.zeros(len(cand),dtype=np.int16); small={}
hdr=0; tp=time.time()
for i in range(0,len(cand),CH):
    chs=cand[i:i+CH]
    A=(chs[:,None] & W[None,:])
    p=(TBL[A & 0xFF].astype(np.int16)+TBL[(A>>8)&0xFF]+TBL[(A>>16)&0xFF]+TBL[(A>>24)&0xFF])
    c=(p>=8).sum(axis=1); cnts[i:i+CH]=c
    sc=np.nonzero((c>0)&(c<=4))[0]
    for r in sc:
        idx=np.nonzero(p[int(r)]>=8)[0]
        small[int(chs[int(r)])]=tuple(int(x) for x in idx)
    if i % (CH*50)==0: print(f"  进度 {i}/{len(cand)}  {time.time()-tp:.0f}s", flush=True)
print(f"blocker 计算完成 {time.time()-tp:.0f}s ✓", flush=True)
D=Counter(int(x) for x in cnts)
print("|B(s)| 分布 (前 8):", dict(sorted(D.items())[:8]), flush=True)
print(f"零-blocker 数 = {D.get(0,0)}  (论文: 0) {'✓✓' if D.get(0,0)==0 else '✗'}", flush=True)
le2=sum(v for k,v in D.items() if 0<k<=2); le3=sum(v for k,v in D.items() if 0<k<=3); le4=sum(v for k,v in D.items() if 0<k<=4)
print(f"|B|≤2: {le2} (论文 1248) {'✓✓' if le2==1248 else '✗'} | |B|≤3: {le3} (论文 7751) {'✓✓' if le3==7751 else '✗'} | |B|≤4: {le4} (论文 30,247) {'✓✓' if le4==30247 else '✗'}", flush=True)
np.save('/tmp/a23_cnts.npy', cnts)
import pickle; pickle.dump(small, open('/tmp/a23_small.pkl','wb'))
print(f"小-blocker 候选数 = {len(small)} ✓", flush=True)
# 门 1
byD=defaultdict(list)
for s,bl in small.items(): byD[bl].append(s)
print(f"\n=== 门 1 ===  不同 |D|≤4 的 D 数 = {len(byD)}", flush=True)
for k in (1,2,3,4):
    print(f"   |D|={k}: {sum(1 for d in byD if len(d)==k)} 个", flush=True)
mx=max((len(v),k) for k,v in byD.items())
print(f"\n=== 门 2 === max |S(D)| = {mx[0]}  at D={mx[1]}", flush=True)
print("   |S(D)| 分布 =", dict(sorted(Counter(len(v) for v in byD.values()).items())), flush=True)
# 引理 C 校验 + 引理 D 窗口统计
viol=0; win=Counter()
for s,bl in small.items():
    for a,b in itertools.combinations(bl,2):
        if pc1(int(W[a]^W[b]))>8: viol+=1
    for s2 in ():
        pass
print(f"引理 C（B(s) 成团）: 违反 {viol} {'✓✓' if viol==0 else '✗'}", flush=True)
print(f"总用时 {time.time()-t0:.0f}s", flush=True)
