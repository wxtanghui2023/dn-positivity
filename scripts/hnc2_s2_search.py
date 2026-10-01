#!/usr/bin/env python3
"""HN-C2 S2: 结构约束下的定向搜索（SA）找 40 块 (12,6,4) 覆盖设计
不变量：每点恰 20 次（swap 保持）｜目标：覆盖 495 个 4-子集 且 λ=10(特对内)/9(特对间)
"""
import itertools, random, math, time
V,K,T,M=12,6,4,40
B4={b:[s for s in itertools.combinations(b,T)] for b in itertools.combinations(range(V),K)}
B2={b:[p for p in itertools.combinations(b,2)] for b in itertools.combinations(range(V),K)}
subs=list(itertools.combinations(range(V),T)); SIDX={s:i for i,s in enumerate(subs)}
pairs=list(itertools.combinations(range(V),2)); PIDX={p:i for i,p in enumerate(pairs)}
TGT=[10 if p[0]//2==p[1]//2 else 9 for p in pairs]
def init(rng):
    for _ in range(5000):
        cap=[20]*V; blocks=[]; ok=True
        for _i in range(M):
            av=[v for v in range(V) if cap[v]>0]
            if len(av)<6: ok=False; break
            # 优先选容量大的，降低尾部卡死概率
            av.sort(key=lambda v:-cap[v]); pool=av[:min(len(av),9)]
            pick=rng.sample(pool,6) if len(pool)>=6 else None
            if pick is None: ok=False; break
            for v in pick: cap[v]-=1
            blocks.append(tuple(sorted(pick)))
        if ok and sum(cap)==0: return blocks
    # 兜底：轮转式构造（必然可行）
    blocks=[]; order=list(range(V))
    for i in range(M):
        pick=sorted(order[(i*6+k)%V] for k in range(6))
        if len(set(pick))<6:
            pick=sorted(set([(i+k)%V for k in range(12)])&set(order))[:6]
        blocks.append(tuple(sorted(pick)))
    return blocks
def evaluate(blocks):
    c4=[0]*len(subs); c2=[0]*len(pairs)
    for b in blocks:
        for s in B4[b]: c4[SIDX[s]]+=1
        for p in B2[b]: c2[PIDX[p]]+=1
    unc=sum(1 for x in c4 if x==0); lv=sum(abs(c2[i]-TGT[i]) for i in range(len(pairs)))
    return unc,lv,c4,c2
def run(seed,secs):
    rng=random.Random(seed); blocks=init(rng)
    unc,lv,c4,c2=evaluate(blocks); best=(1000*unc+400*lv,unc,lv,list(blocks)); it=0; t0=time.time()
    while time.time()-t0<secs:
        it+=1; frac=(time.time()-t0)/secs; Temp=3.0*(0.02/3.0)**frac
        i,j=rng.randrange(M),rng.randrange(M)
        if i==j: continue
        bi,bj=blocks[i],blocks[j]; p=rng.choice(bi); q=rng.choice(bj)
        if q in bi or p in bj: continue
        ni=tuple(sorted(set(bi)-{p}|{q})); nj=tuple(sorted(set(bj)-{q}|{p}))
        loc={}
        for s in B4[bi]: loc[s]=loc.get(s,0)-1
        for s in B4[bj]: loc[s]=loc.get(s,0)-1
        for s in B4[ni]: loc[s]=loc.get(s,0)+1
        for s in B4[nj]: loc[s]=loc.get(s,0)+1
        d_unc=0
        for s,dn in loc.items():
            k=SIDX[s]; old=c4[k]; new=old+dn
            d_unc+=(1 if new==0 else 0)-(1 if old==0 else 0)
        loc2={}
        for p2 in B2[bi]: loc2[p2]=loc2.get(p2,0)-1
        for p2 in B2[bj]: loc2[p2]=loc2.get(p2,0)-1
        for p2 in B2[ni]: loc2[p2]=loc2.get(p2,0)+1
        for p2 in B2[nj]: loc2[p2]=loc2.get(p2,0)+1
        d_lv=0
        for p2,dn in loc2.items():
            k=PIDX[p2]; old=c2[k]; d_lv+=abs(old+dn-TGT[k])-abs(old-TGT[k])
        d=1000*d_unc+400*d_lv
        if d<=0 or rng.random()<math.exp(-d/Temp):
            for s,dn in loc.items(): c4[SIDX[s]]+=dn
            for p2,dn in loc2.items(): c2[PIDX[p2]]+=dn
            blocks[i],blocks[j]=ni,nj
            unc_new=unc+d_unc; lv_new=lv+d_lv; unc,lv=unc_new,lv_new
            sc=1000*unc+400*lv
            if sc<best[0]: best=(sc,unc,lv,list(blocks))
            if unc==0 and lv==0: return best,it,True
    return best,it,False
tot=time.time()
for seed in [11,12,13,14]:
    t0=time.time(); (sc,unc,lv,bl),it,hit=run(seed,120)
    print(f"[seed {seed}] it={it} 未覆盖={unc} λ违例={lv} 用时={time.time()-t0:.0f}s {'★命中' if hit else ''}",flush=True)
    if hit:
        print("BLOCKS:",bl,flush=True); break
print(f"总用时 {time.time()-tot:.0f}s",flush=True)
