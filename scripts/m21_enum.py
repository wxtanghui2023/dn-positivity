import itertools, time
from collections import Counter, defaultdict
def C2(x): return x*(x-1)//2
r=8
edges=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(edges)}; ne=28
triples=list(itertools.combinations(range(r),3))
tmask=[]; tri_e=[]
for t in triples:
    m=0; el=[]
    for e in itertools.combinations(t,2):
        idx=ei[e]; m|=1<<idx; el.append(idx)
    tmask.append(m); tri_e.append(el)
# 预计算：每个三角形在其三条边上的索引
recs=[]; cnt=Counter(); t0=time.time()
for C in itertools.combinations(range(ne),7):
    Cm=0
    for i in C: Cm|=1<<i
    T=0
    for m in tmask:
        if not (m & Cm): T+=1
    if T!=21: continue
    cnt['found']+=1
    # G = complement of C: loads
    load=[0]*ne
    for ti,m in enumerate(tmask):
        if not (m & Cm):   # this triple is a triangle of G
            for idx in tri_e[ti]: load[idx]+=1
    h=sum(C2(v) for v in load)
    # 补图结构：度数序列、连通分支
    Cset=set(C)
    degC=[0]*r
    for i in C:
        a,b=edges[i]; degC[a]+=1; degC[b]+=1
    recs.append((h,tuple(sorted(degC)),len(set(Cset))))
    if cnt['found']%200==0: print(f"  已找到 {cnt['found']} 个 extremizer, 用时 {time.time()-t0:.0f}s",flush=True)
print("=== m=21, e=21 之 extremizers ===",flush=True)
print("总数:", cnt['found'], flush=True)
if recs:
    hs=sorted(set(x[0] for x in recs))
    print("h 取值集合:", hs, flush=True)
    print("h 最小值 H_2(21) =", min(x[0] for x in recs), flush=True)
    print("h 分布:", dict(Counter(x[0] for x in recs)), flush=True)
    print("补图度序列分布(前10):", Counter(x[1] for x in recs).most_common(10), flush=True)
print("DONE",flush=True)
