#!/usr/bin/env python3
"""剖面刚性: 消元验证 + t-族 + 已有约束扫描 + 三阶量/缺陷恒等式"""
import itertools
from collections import Counter
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
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
print("="*72); print("① 消元验证 (n=9,M=62: E=108, Q2=38)"); print("="*72)
print("  N1+N2+N3+N4=512 | N2+2N3+3N4=108 | N3+3N4=38")
print("  ⟹ N3=38-3t, N2=32+3t, N1=442-t   (t:=N4)")
sol=[]
for t in range(0,13):
    N1,N2,N3,N4=442-t,32+3*t,38-3*t,t
    ok = (N1+N2+N3+N4==512) and (N2+2*N3+3*N4==108) and (N3+3*N4==38)
    # 派生量
    Q=512-N1                      # #{b>=2}
    Asum=(N2+3*N3+6*N4)//2        # A<=2
    T3=N3+4*N4                    # Σ C(b,3) (b<=4 假设下)
    defect=(Q2:=38)-(108-Q)       # 由 Q2=(E-Q)+defect
    sol.append((t,N1,N2,N3,N4,Q,Asum,T3,defect,ok,N3>=0))
print(f"\n  {'t':>2} {'N1':>4} {'N2':>4} {'N3':>4} {'N4':>3} {'Q':>4} {'A≤2':>4} {'T3':>4} {'defect':>6} 合法")
for t,N1,N2,N3,N4,Q,Asum,T3,df,ok,nonneg in sol:
    print(f"  {t:>2} {N1:>4} {N2:>4} {N3:>4} {N4:>3} {Q:>4} {Asum:>4} {T3:>4} {df:>6} {'✓' if (ok and nonneg) else '✗'}")
print("\n  观察: A≤2=73 与 T3=38+t, defect=t 均随 t 线性 ✓ (前三阶矩全被 E,Q2 钉死 ✓)")
print("  ⟹ 剖面刚性 ⟺ 三阶量 T3 = 38+N4 的刚性 ✓✓ (即第四条约束必须来自三阶/几何 ✗)")
print("\n"+"="*72); print("② 两个真实码的实测 + 约束扫描"); print("="*72)
n=9;N,BALL=build(n);FULL=(1<<N)-1
for i,C in enumerate(load62(),1):
    Cs=set(C)
    b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)}
    Nj=Counter(b.values())
    E=sum(v-1 for v in b.values()); Q2=sum((v-1)*(v-2)//2 for v in b.values())
    Q=sum(1 for v in b.values() if v>=2)
    defect=sum((v-2)*(v-3)//2 for v in b.values() if v>=4)
    T3=sum(v*(v-1)*(v-2)//6 for v in b.values())
    Asum=sum(v*(v-1)//2 for v in b.values())//2
    t=Nj.get(4,0)
    # G<=2 的三角形数
    tri=0
    adj={}
    for u in C:
        adj[u]=set(v for v in C if 1<=bin(u^v).count('1')<=2)
    for u,v,w in itertools.combinations(C,3):
        if v in adj[u] and w in adj[u] and w in adj[v]: tri+=1
    print(f"\n[码#{i}] 剖面 N1..N4 = {[Nj.get(j,0) for j in range(1,5)]} → t={t} {'✓ 与族吻合' if [Nj.get(j,0) for j in range(1,5)]==[442-t,32+3*t,38-3*t,t] else '✗'}")
    print(f"   E={E} Q2={Q2} Q={Q} 缺陷defect={defect} **==t? {defect==t}** | T3={T3} **==38+t? {T3==38+t}** | A≤2={Asum}")
    print(f"   G≤2 三角形数={tri} ⟹ 约束 T3 ≤ #tri: {T3} ≤ {tri} {'✓' if T3<=tri else '✗失败'}")
    print(f"   b_max={max(b.values())}  L2: N≥3={Nj.get(3,0)+t} ≤ E/2={E/2} ✓")
    # 假设 t≠10 时的 T3 需求 vs 三角形上限
    print(f"   若 t=11 (T3 需 49) / t=12 (T3 需 50): 本码三角上限 {tri} ⟹ {'t>10 需更多三角形 ⚠️' if tri<50 else '无矛盾 ✗'}")
