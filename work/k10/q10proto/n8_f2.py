#!/usr/bin/env python3
"""n=8 证伪 v2：只用 k=2,3 切换（便宜 ✓），流式输出 ✓，结果即时落盘 ✓"""
import random, sys
from itertools import combinations
from collections import Counter
n,N,M = 8,256,32; E = M*(n+1)-N
BALL=[]
for v in range(N):
    m=1<<v
    for i in range(n): m|=1<<(v^(1<<i))
    BALL.append(m)
FULL=(1<<N)-1
def covmask(C):
    m=0
    for c in C: m|=BALL[c]
    return m
def stats(C):
    cnt=[0]*N
    for c in C:
        mm=BALL[c]
        while mm:
            low=mm&-mm; cnt[low.bit_length()-1]+=1; mm^=low
    A1=sum(1 for a,b in combinations(sorted(C),2) if (a^b).bit_count()==1)
    A2=sum(1 for a,b in combinations(sorted(C),2) if (a^b).bit_count()==2)
    return dict(Q=sum((bb-1)*(bb-2)//2 for bb in cnt), A1=A1, A2=A2, b=dict(sorted(Counter(cnt).items())))
H=[[1,1,1,0,1,0,0],[1,1,0,1,0,1,0],[1,0,1,1,0,0,1]]
H7=[x for x in range(128) if all(sum(H[r][i]*((x>>i)&1) for i in range(7))%2==0 for r in range(3))]
start=set([c<<1 for c in H7]+[(c<<1)|1 for c in H7])
random.seed(29); cur=set(start); found={frozenset(cur):stats(cur)}; acc=0; tries=0
print("起点:", found[frozenset(cur)], flush=True)
while acc < 200 and tries < 200000:
    tries+=1
    k=random.choice([2,3])
    rem=random.sample(sorted(cur),k); C2=cur-set(rem)
    holes=FULL^covmask(C2)
    if holes==0: continue
    cand=[w for w in range(N) if w not in C2 and w not in rem and (BALL[w]&holes)]
    hit=None
    if k==2:
        for i in range(len(cand)):
            b1=BALL[cand[i]]
            for j in range(i+1,len(cand)):
                if (b1|BALL[cand[j]])&holes==holes: hit=(cand[i],cand[j]); break
            if hit: break
    else:
        for i in range(len(cand)):
            h1=holes&~BALL[cand[i]]
            if h1==0: continue
            for j in range(i+1,len(cand)):
                h2=h1&~BALL[cand[j]]
                if h2==0: continue
                for l in range(j+1,len(cand)):
                    if BALL[cand[l]]&h2==h2: hit=(cand[i],cand[j],cand[l]); break
                if hit: break
            if hit: break
    if hit is None: continue
    newc=C2|set(hit)
    if len(newc)!=M or covmask(newc)!=FULL: continue
    cur=newc; acc+=1
    key=frozenset(cur)
    if key not in found:
        found[key]=stats(cur)
        print(f"[{acc}] 新码 #{len(found)}: Q={found[key]['Q']} A1={found[key]['A1']} A2={found[key]['A2']} b={found[key]['b']}", flush=True)
print(f"\n=== 汇总: 接受={acc} 尝试={tries} 不同码={len(found)}", flush=True)
qd=Counter(v['Q'] for v in found.values())
print(f"Q 分布 = {dict(sorted(qd.items()))}", flush=True)
print(f"(A1,A2) 分布 = {dict(sorted(Counter((v['A1'],v['A2']) for v in found.values()).items()))}", flush=True)
print(("⛔ 出现 Q!=0 ⟹ n=8 pinning 被反驳 ✗" if any(v['Q']!=0 for v in found.values()) else "全部 Q=0 ✓（证伪未成功 ⟹ pinning 存活 ✓）"), flush=True)
