#!/usr/bin/env python3
"""P1.5: h(z) 容量 + p2(z) 分叉验证 + code/non-code 分离预算"""
import itertools
from collections import Counter, defaultdict
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
def analyse(n,C,tag):
    N,BALL=build(n); Cs=set(C); FULL=(1<<N)-1
    cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    X4=[x for x in range(N) if bl[x]==4]
    Sx={x:frozenset(c for c in C if (BALL[x]>>c)&1) for x in X4}
    typ={x:('A' if x in Cs else 'B') for x in X4}
    # 孤立性: 与任何其他 b=4 中心星集不交
    iso=[x for x in X4 if all(not (Sx[x]&Sx[y]) for y in X4 if y!=x)]
    def delta(x):
        return set(v for v in C if (BALL[x]>>v)&1)  # placeholder
    # Δ_x = 新第二中心 = 距离2 pair 的中点（排除 x）
    def D(x):
        S=sorted(Sx[x]); out=set()
        for u,v in itertools.combinations(S,2):
            if bin(u^v).count('1')==2:
                m=BALL[u]&BALL[v]
                for c in [w for w in range(N) if (m>>w)&1]:
                    if c!=x: out.add(c)
        return out
    Dx={x:D(x) for x in X4}
    # p2(z) 验证
    bad_p2=0
    for z in range(N):
        pairs=[(u,v) for u,v in itertools.combinations(sorted(c for c in C if (BALL[z]>>c)&1),2) if bin(u^v).count('1')==2]
        pred=(bl[z]-1)*(bl[z]-2)//2 if z in Cs else bl[z]*(bl[z]-1)//2
        if len(pairs)!=pred: bad_p2+=1
    # h(z) 全中心 / 仅孤立
    h=Counter(); hi=Counter()
    for x in X4:
        for z in Dx[x]: h[z]+=1
    for x in iso:
        for z in Dx[x]: hi[z]+=1
    H=sum(h.values()); Hi=sum(hi.values())
    HC=sum(v for z,v in h.items() if z in Cs); HCb=sum(v for z,v in h.items() if z not in Cs)
    HCi=sum(v for z,v in hi.items() if z in Cs); HCbi=sum(v for z,v in hi.items() if z not in Cs)
    # 容量
    cap_all=sum(bl[z]*(bl[z]-1)//2 for z in range(N))
    capC=sum((bl[z]-1)*(bl[z]-2)//2 for z in range(N) if z in Cs)
    capCb=sum(bl[z]*(bl[z]-1)//2 for z in range(N) if z not in Cs)
    # h ≤ C(b,2) 检查 + 紧性
    viol=sum(1 for z,v in h.items() if v>bl[z]*(bl[z]-1)//2)
    tight=sum(1 for z,v in h.items() if v==bl[z]*(bl[z]-1)//2 and v>0)
    nA=sum(1 for x in X4 if typ[x]=='A'); nB=len(X4)-nA
    isoA=sum(1 for x in iso if typ[x]=='A'); isoB=len(iso)-isoA
    print(f"[{tag}] N4={len(X4)} (A{nA}/B{nB}) | 孤立={len(iso)} (A{isoA}/B{isoB})")
    print(f"   p2(z) 分叉公式验证: 违反 {bad_p2} {'✓✓' if bad_p2==0 else '✗'}")
    print(f"   Σ|Δx| 全={H} (=3·{nA}+6·{nB}={(3*nA+6*nB)}) | **孤立Σ={Hi} (=3·{isoA}+6·{isoB}={3*isoA+6*isoB})**")
    print(f"   H_C={HC} H_C̄={HCb} | 孤立: H_C={HCi} H_C̄={HCbi}")
    print(f"   **max h(z)={max(h.values()) if h else 0}** (全中心) | r 分布={dict(sorted(Counter(h.values()).items()))}")
    print(f"   **max h_iso(z)={max(hi.values()) if hi else 0}** | 分布={dict(sorted(Counter(hi.values()).items()))}")
    print(f"   h≤C(b,2) 违反={viol} {'✓✓' if viol==0 else '✗'} | 取等点数={tight}")
    print(f"   容量: ΣC(b,2)=146(={cap_all}) | Σ_C q(z)={capC} | Σ_C̄ C(b,2)={capCb}")
    print(f"   Δmass ≤ 容量: 全 {H}≤{cap_all} ✓ | 孤立 {Hi}≤{cap_all} ✓")
    return dict(Hi=Hi,maxh=max(h.values()) if h else 0,maxhi=max(hi.values()) if hi else 0)
def load62():
    codes=[];cur=[]
    for line in open('../c62/K_9_1_classif.txt'):
        a=line.split()
        if len(a)==9 and all(c in '01' for c in a): cur.append(int("".join(a),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
for i,c in enumerate(load62(),1): analyse(9,c,f"(9,62)=K 码#{i}")
for s in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011","000100 000010 000001 100111 010111 001111 011000 101000 110000 111011 111101 111110":
    analyse(6,[int(x,2) for x in s.split()],"(6,12)=K")
