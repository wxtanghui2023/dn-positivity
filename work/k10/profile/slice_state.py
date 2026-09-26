#!/usr/bin/env python3
"""P2-α 第一刀: 余维1 slice 的 paired-state 枚举与压缩 (无 solver)"""
import itertools
from collections import Counter, defaultdict
n=9;N=512
BALL=[0]*N; BALL8=[0]*N
for x in range(N):
    m=1<<x
    for i in range(n): m|=1<<(x^(1<<i))
    BALL[x]=m
    m8=1<<x
    for i in range(n-1): m8|=1<<(x^(1<<i))   # 仅低 8 位坐标 (0..7)，第 8 位为切向
    BALL8[x]=m8
def load():
    codes=[];cur=[]
    for line in open('../c62/K_9_1_classif.txt'):
        a=line.split()
        if len(a)==9 and all(c in '01' for c in a): cur.append(int("".join(a),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
for idx,C in enumerate(load(),1):
    Cs=set(C)
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    print(f"=== 码#{idx} (|C|={len(C)}, N4={sum(1 for x in range(N) if bl[x]==4)}) ===")
    # 坐标切: 取第 8 位(最高位)作为切向 -> H^0: 第8位=0, H^1: 第8位=1
    cut=8
    H0=[x for x in range(N) if not (x>>cut)&1]
    H1=[x for x in range(N) if (x>>cut)&1]
    m0=sum(1 for x in H0 if x in Cs); m1=sum(1 for x in H1 if x in Cs)
    print(f"  切向=坐标{cut}: |C^0|={m0}, |C^1|={m1}")
    # 分解 b = b_same + b_cross
    pairs=Counter(); bd=Counter(); N4_state=Counter()
    for x in H0:
        y=x|(1<<cut)
        bs=sum(1 for c in C if (BALL8[c]>>x)&1 and ((c>>cut)&1)==0)
        bs8=sum(1 for c in C if (BALL8[c]>>x)&1 and ((c>>cut)&1)==0)
        bc=1 if (x|(1<<cut)) in Cs else 0
        bs3=sum(1 for c in C if (BALL8[c]>>x)&1 and ((c>>cut)&1)==0)
        # H1 侧
        bs1=sum(1 for c in C if (BALL8[c]>>y)&1 and ((c>>cut)&1)==1)
        bc1=1 if x in Cs else 0
        pairs[( (min(bs,bs1),bc+bc1) )]+=0
        pairs[(bs,bc,bs1,bc1)]+=1
        if bl[x]==4: N4_state[(bs,bc)]+=1
        if bl[y]==4: N4_state[(bs1,bc1)]+=1
    # 重新用正确公式统计
    N4_state=Counter(); dist=Counter()
    for x in H0:
        y=x|(1<<cut)
        for z,eps in ((x,0),(y,1)):
            bs=sum(1 for c in C if (BALL8[c]>>z)&1 and ((c>>cut)&1)==eps)
            other=(z^(1<<cut))
            bc=1 if other in Cs else 0
            dist[(bs,bc)]+=1
            if bl[z]==4: N4_state[(bs,bc)]+=1
    print(f"  (b_same,b_cross) 分布 = {dict(sorted(dist.items()))}")
    print(f"  b=4 的 (b_same,b_cross) 分解 = {dict(sorted(N4_state.items()))} (Σ={sum(N4_state.values())}=N4)")
    print(f"  ⟹ N4 = N_(4,0) + N_(3,1) = {N4_state.get((4,0),0)} + {N4_state.get((3,1),0)} = {N4_state.get((4,0),0)+N4_state.get((3,1),0)}")
    # 校验 b = b_same + b_cross
    bad=0
    for x in range(N):
        eps=(x>>cut)&1
        bs=sum(1 for c in C if (BALL8[c]>>x)&1 and ((c>>cut)&1)==eps)
        bc=1 if (x^(1<<cut)) in Cs else 0
        if bs+bc!=bl[x]: bad+=1
    print(f"  恒等式 b = b_same + b_cross: 违反 {bad} {'✓✓' if bad==0 else '✗'}")
    # 4 类 paired state 分布
    ps=Counter()
    for x in H0:
        y=x|(1<<cut)
        def st(z):
            eps=(z>>cut)&1
            bs=sum(1 for c in C if (BALL8[c]>>z)&1 and ((c>>cut)&1)==eps)
            bc=1 if (z^(1<<cut)) in Cs else 0
            return bs,bc
        a=st(x); b_=st(y)
        ps[(a[0],a[1],b_[0],b_[1])]+=1
    print(f"  paired-state 类型数 = {len(ps)} (共 {sum(ps.values())} 对=256)")
    for k,v in sorted(ps.items(), key=lambda kv:-kv[1])[:6]:
        print(f"     s={k}: {v} 对")
