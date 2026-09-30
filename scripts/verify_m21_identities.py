import itertools
from collections import Counter
def C2(x): return x*(x-1)//2
r=8
edges=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(edges)}; ne=28
tri=list(itertools.combinations(range(r),3))
tmask=[]; tri_e=[]
for t in tri:
    m=0; el=[]
    for e in itertools.combinations(t,2):
        idx=ei[e]; m|=1<<idx; el.append(idx)
    tmask.append(m); tri_e.append(el)
bad=Counter(); spec=Counter(); cnt=0
for C in itertools.combinations(range(ne),7):
    Cm=0
    for i in C: Cm|=1<<i
    T=sum(1 for m in tmask if not (m & Cm))
    if T!=21: continue
    cnt+=1
    load=[0]*ne
    for ti,m in enumerate(tmask):
        if not (m & Cm):
            for idx in tri_e[ti]: load[idx]+=1
    h=sum(C2(v) for v in load)
    if h!=66: continue     # 只看达到 H_2 的 extremizer
    spec[tuple(sorted(Counter(load).items()))]+=1
    # 补图量
    a=[0]*r; adjF=[set() for _ in range(r)]
    for i in C:
        u,v=edges[i]; a[u]+=1; a[v]+=1; adjF[u].add(v); adjF[v].add(u)
    # 核验 t_uv = 6 - a_u - a_v + c_uv
    for i in range(ne):
        if i in C: continue      # uv 属于 G
        u,v=edges[i]
        c=len(adjF[u]&adjF[v])
        if load[i] != 6-a[u]-a[v]+c: bad['t=6-a-b+c']+=1
    # 核验 sum_{uv in E(G)}(a_u+a_v) = 70
    s=sum(a[u]+a[v] for i,(u,v) in enumerate(edges) if i not in C)
    if s!=70: bad['sum(a_u+a_v)=70']+=1
    c2=sum(C2(a[v]) for v in range(r))
    if c2!=7: bad['sum C(a_v,2)=7']+=1
print("h=66 之 extremizer 数:", cnt and sum(spec.values()), flush=True)
print("载荷谱分布:", dict(spec), flush=True)
print("违背计数:", dict(bad) if bad else "全零 ✓✓", flush=True)
print("预期谱 {2^3,3^15,4^3}:", spec.get(tuple(sorted({2:3,3:15,4:3}.items())),0), flush=True)
