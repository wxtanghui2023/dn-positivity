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
# 分层索引（按 word-index 组合直接取掩码）——比 O(330) 层扫描快 ~6x
_L = {}
for _i, _w in enumerate(WORDS):
    for _v in [ _w ] + [ _w ^ (1 << b) for b in range(10) ]:
        _L.setdefault(frozenset(owners[_v]), 0)
        _L[frozenset(owners[_v])] |= 1 << _v
IDX = {w: i for i, w in enumerate(WORDS)}
Lv1, P2, P3, P4, P5 = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
for _k, _m in _L.items():
    _ii = tuple(sorted(_k))
    if len(_ii) == 1: Lv1[_ii[0]] |= _m
    elif len(_ii) == 2: P2[_ii] |= _m
    elif len(_ii) == 3: P3[_ii] |= _m
    elif len(_ii) == 4: P4[_ii] |= _m
    elif len(_ii) == 5: P5[_ii] |= _m


def U_of(D):
    u = 0
    for i in D:
        u |= Lv1[i]
    if len(D) >= 2:
        for pr in itertools.combinations(D, 2):
            u |= P2.get(pr, 0)
    if len(D) >= 3:
        for tr in itertools.combinations(D, 3):
            u |= P3.get(tr, 0)
    if len(D) >= 4:
        for qd in itertools.combinations(D, 4):
            u |= P4.get(qd, 0)
    if len(D) >= 5:
        for qn in itertools.combinations(D, 5):
            u |= P5.get(qn, 0)
    return u
def main():
    d=int(sys.argv[1])
    mod=tuple(int(x) for x in sys.argv[2].split(':')) if len(sys.argv)>2 else None
    t0=time.time(); tested=0; cand=0; cert=0; fail=[]; uhist=Counter()
    tag0 = f"d{d}" + (f"_mod{mod[0]}of{mod[1]}" if mod else "")
    fh = open(f'b1b_packfail_{tag0}.jsonl','w'); failn=0
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
        else:
            failn += 1
            fh.write(json.dumps({"D":list(D),"U":U.bit_count()})+"\n")
        if tested%500000==0: print(f"  d={d} tested={tested:,} cand={cand} cert={cert} fail={failn} {time.time()-t0:.0f}s",flush=True)
    fh.close()
    print(f"d={d}: tested={tested:,} 需查={cand:,} 见证成功={cert:,} 失败={failn} {time.time()-t0:.0f}s",flush=True)
    print("失败已流式写入 jsonl:",failn)
    print("|U| 分布(抽样):",dict(sorted(uhist.items())[:10]))
    json.dump({"d":d,"tested":tested,"cand":cand,"cert":cert,"n_fail":failn},
              open(f'b1b_packcert_{tag0}.json','w'),indent=1)
    with open(f'b1b_packfail_{tag}.jsonl','w') as fh:
        for r in fail: fh.write(json.dumps(r)+"\n")
    print(f"失败已写 b1b_packfail_{tag}.jsonl（{len(fail)} 例）")
if __name__=="__main__": main()
