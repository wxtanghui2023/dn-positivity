#!/usr/bin/env python3
"""B1-b packing 证书：对给定 d，验证 ∀D,|D|=d 有 α₂(U_D) ≥ d（贪心见证即可）。
用法: python3 b1b_pack_cert.py <d> [mod k nsh]"""
import itertools, json, sys, time
from collections import Counter, defaultdict
WORDS=sorted(set(int(t,2) for t in open('kamenetsky120.txt').read().split() if len(t)==10))
CODE=set(WORDS); N=1024
BALL=[0]*N
for w in range(N):
    m=1<<w
    for b in range(10): m|=1<<(w^(1<<b))
    BALL[w]=m
owners=[[] for _ in range(N)]
for i,w in enumerate(WORDS):
    owners[w].append(i)
    for b in range(10): owners[w^(1<<b)].append(i)
L1=defaultdict(int)
for v in range(N):
    if len(owners[v])==1: L1[owners[v][0]]|=1<<v
def greedy_pack(pts, target):
    """贪心找 target 个两两距离>=3 的点；成功返回列表，失败 None"""
    rem=pts; got=[]
    while len(got)<target and rem:
        v=(rem & -rem).bit_length()-1
        got.append(v)
        nxt=0; t=rem
        while t:
            u=(t & -t).bit_length()-1; t&=t-1
            if (u^v).bit_count()>2: nxt|=1<<u
        rem=nxt
    return got if len(got)>=target else None
def U_of(D):
    Ds=set(D); u=0
    for v in range(N):
        S=owners[v]
        if S and set(S)<=Ds: u|=1<<v
    return u
def main():
    d=int(sys.argv[1])
    mod=tuple(int(x) for x in sys.argv[2].split(':')) if len(sys.argv)>2 else None
    t0=time.time(); tested=0; cand=0; cert=0; fail=[]; uhist=Counter()
    for D in itertools.combinations(range(120),d):
        if mod and D[0]%mod[1]!=mod[0]: continue
        u1=0
        for i in D: u1|=L1[i]
        tested+=1
        if u1.bit_count()>11*(d-1): continue
        if not greedy_pack(u1,d-1) and u1: continue   # u1 已有 d 点见证
        cand+=1
        U=U_of(D)
        if not U: continue
        uhist[U.bit_count()]+=1
        if greedy_pack(U,d): cert+=1
        elif len(fail)<20: fail.append({"D":list(D),"U":U.bit_count()})
        if tested%2000000==0: print(f"  d={d} tested={tested:,} cand={cand} cert={cert} {time.time()-t0:.0f}s",flush=True)
    print(f"d={d}: tested={tested:,} 需查={cand:,} 见证成功={cert:,} 失败={len(fail)} {time.time()-t0:.0f}s")
    print("失败的 D:",fail[:5])
    print("|U| 分布(抽样):",dict(sorted(uhist.items())[:10]))
    json.dump({"d":d,"tested":tested,"cand":cand,"cert":cert,"fail":fail},
              open(f'b1b_packcert_d{d}{"_mod%s:%s"%mod if mod else ""}.json','w'),indent=1)
if __name__=="__main__": main()
