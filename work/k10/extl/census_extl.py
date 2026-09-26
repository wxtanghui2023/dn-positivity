#!/usr/bin/env python3
"""EXT-L 普查: 全部极值实例的 L□/S/I_nw/E/Q2 表 + 逐顶点收费规则检验
口径: L□ = M + C (private 不计入) ✓"""
import itertools, json
from collections import Counter, defaultdict
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
def full_analysis(n,C,tag):
    N,BALL=build(n); Cs=set(C); fmt=lambda x:format(x,'0%db'%n)
    FULL=(1<<N)-1; cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return None
    b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)}
    E=sum(v-1 for v in b.values()); Q2=sum((v-1)*(v-2)//2 for v in b.values())
    I=sum((b[c]-1)*(b[c]-2)//2 for c in C)
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in Cs)
    dC={c:b[c]-1 for c in C}
    sqs={}
    for u in sorted(Cs):
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i);c2=u^(1<<j);ac=u^(1<<i)^(1<<j)
            if a in Cs and c2 in Cs and ac in Cs: sqs[frozenset([u,a,c2,ac])]=(u,i,j)
    dirs_of=defaultdict(list)
    for verts,(u,i,j) in sqs.items():
        for v in verts: dirs_of[v].append({i,j})
    V=set(dirs_of); Inw=I-len(V)
    # 去重口径三态 + 逐顶点
    P=M=Cn=0; Lv={}; sv={}; wit=Counter(); shared_pen=0
    for v in sorted(V):
        inter=set.intersection(*dirs_of[v])
        seen=set(); lv=0
        for k in range(n):
            if k in inter: continue
            y=v^(1<<k)
            if y in seen: continue
            seen.add(y)
            if y in Cs: Cn+=1; lv+=1
            elif b[y]==1: P+=1
            else:
                M+=1; lv+=1
                cov2=[c for c in C if (BALL[c]>>y)&1 and c!=v]
                wit[(y,frozenset([v,cov2[0]]))]+=1
                # v 的 S-见证计数
                sv[v]=sv.get(v,0)+1
        Lv[v]=lv
        if len(dirs_of[v])>1: shared_pen+=max(dC[v]-2,0)
    L=P and 0 or 0; L=M+Cn
    rep=sum(1 for c in wit.values() if c>1)
    # 逐顶点收费规则检验: L_v ≤ (d_C(v)-2)_+ + s_v
    viol=[]
    for v in sorted(V):
        rhs=max(dC[v]-2,0)+sv.get(v,0)
        if Lv[v]>rhs: viol.append((fmt(v),Lv[v],dC[v],sv.get(v,0),rhs))
    rsq=sum(max(len(dirs_of[v])-2,1) for v in V)  # Σ(r-2)_+
    res=dict(tag=tag,n=n,M=len(C),P=P,Mt=M,Ct=Cn,L=L,S=S,Inw=Inw,E=E,Q2=Q2,
             V=len(V),Sq=len(sqs),Ds=S+Inw-L,shared_pen=shared_pen,rep=rep,
             rsum=rsq,viol=len(viol))
    print(f"[{tag}] n={n} M={len(C)} | L□={L} (P={P},M={M},C={Cn}) | S={S} I_nw={Inw} | **D={res['Ds']:+d}** {'✓' if res['Ds']>=0 else '✗失败'}")
    print(f"      E={E} Q2={Q2} |V□|={len(V)} S_q={len(sqs)} Σ(r-2)+={rsq} Σ_shared(dC-2)={shared_pen} #重复见证={rep}")
    print(f"      逐顶点规则 L_v ≤ (dC-2)+ + s_v : 违反 {len(viol)} {'✓' if not viol else '✗ '+str(viol[:3])}")
    # 逐顶点明细（仅方阵顶点）
    for v in sorted(V):
        print(f"        {fmt(v)}: 方阵数={len(dirs_of[v])} dC={dC[v]} |U|={n-len(set.intersection(*dirs_of[v]))} L_v={Lv[v]} s_v={sv.get(v,0)} 收费上限={max(dC[v]-2,0)+sv.get(v,0)}")
    return res
def load62():
    codes=[];cur=[]
    for line in open('../c62/K_9_1_classif.txt'):
        s=line.split()
        if len(s)==9 and all(c in '01' for c in s): cur.append(int("".join(s),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
print("="*70); print("EXT-L 普查（极值层）"); print("="*70)
allres=[]
# n=4 M=4
n=4;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),4):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: allres.append(full_analysis(n,list(C),"(4,4)=K")); break
# n=5 M=7
n=5;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),7):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: allres.append(full_analysis(n,list(C),"(5,7)=K")); break
# n=6 M=12 两个已知类
n=6
c1=[int("000000",2),int("000001",2),int("000010",2),int("001111",2),int("010111",2),int("011100",2),int("100111",2),int("101100",2),int("110100",2),int("111001",2),int("111010",2),int("111011",2)]
c2=[int("000100",2),int("000010",2),int("000001",2),int("100111",2),int("010111",2),int("001111",2),int("011000",2),int("101000",2),int("110000",2),int("111011",2),int("111101",2),int("111110",2)]
for i,c in enumerate([c1,c2]): allres.append(full_analysis(n,c,f"(6,12)=K 类#{i+1}"))
for i,c in enumerate(load62()): allres.append(full_analysis(9,c,f"(9,62)=K 码#{i+1}"))
json.dump([{k:v for k,v in r.items() if k!='viol'} for r in allres if r], open('extl_census.json','w'), indent=1)
print("\n=== 汇总表 ===")
print(f"{'实例':16} {'L□':>4} {'S':>5} {'I_nw':>5} {'D':>5} {'E':>5} {'Q2':>4} {'|V□|':>5} {'S_q':>4} {'Σ(r-2)+':>7} {'Σsh(dC-2)':>9} {'#rep':>5}")
for r in allres:
    if not r: continue
    print(f"{r['tag']:16} {r['L']:>4} {r['S']:>5} {r['Inw']:>5} {r['Ds']:>+5} {r['E']:>5} {r['Q2']:>4} {r['V']:>5} {r['Sq']:>4} {r['rsum']:>7} {r['shared_pen']:>9} {r['rep']:>5}")
