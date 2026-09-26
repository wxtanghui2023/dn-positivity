#!/usr/bin/env python3
"""P1.4: 二层影子碰撞表
先纠: |B1(u)∩B1(v)| = 2 (d=1) 与 2 (d=2) —— 都是 2, 不是 1/2
Δ_x = 新第二中心集合 = {x+e_i+e_j : i<j ∈ I_x}, |I_x|=4(B型)/3(A型)"""
import itertools
from collections import Counter, defaultdict
n=8   # 足够容纳 d<=4 的局部构型
N=1<<n
def ball(x): 
    s={x}
    for i in range(n): s.add(x^(1<<i))
    return s
print("="*60); print("① 球交事实（纠正）"); print("="*60)
for d in (1,2,3):
    x=0; y=(1<<d)-1
    print(f"  d(x,y)={d}: |B1∩B1| = {len(ball(x)&ball(y))}")
print("  ⟹ d=1 与 d=2 均为 **2** ✓（不是 1/2 ✗）")
print("\n"+"="*60); print("② σ(x) 与 |Δ_x|（纠正）"); print("="*60)
def star_set(x, I, typ):
    if typ=='A': return frozenset([x]+[x^(1<<i) for i in I])
    return frozenset([x^(1<<i) for i in I])
def sigma_and_delta(x,I,typ):
    S=star_set(x,I,typ); sig=0; delta=set()
    for u,v in itertools.combinations(sorted(S),2):
        cc=ball(u)&ball(v)
        sig+=len(cc)-1
        for c in cc:
            if c!=x: delta.add(c)
    return sig,delta
for typ,I in (('A',(0,1,2)),('B',(0,1,2,3))):
    sig,dl=sigma_and_delta(0,set(I),typ)
    print(f"  {typ} 型 (I={sorted(I)}): **σ={sig}** |Δ_x|={len(dl)} ⟹ 影子={sorted(format(p,'0%db'%n) for p in dl)}")
print("  ⟹ 纠正: σ(x)=**6**（两型皆然 ✓），而 |Δ_x| = 3(A)/6(B) ✓")
print("\n"+"="*60); print("③ 二层碰撞表 |Δ_x ∩ Δ_y| （x=0, y 为 δ-子集, 枚举 I_x,I_y）"); print("="*60)
rows=defaultdict(set); Srows=defaultdict(set)
for Tx in ('A','B'):
    nx=3 if Tx=='A' else 4
    for Ty in ('A','B'):
        ny=3 if Ty=='A' else 4
        for dxy in (1,2,3,4):
            vals=Counter(); svals=Counter()
            for Ix in itertools.combinations(range(n),nx):
                Sx=star_set(0,set(Ix),Tx)
                # y = 一个 δ-子集；为覆盖所有相对位置，枚举 y 的不同"形状"
                for supp in itertools.combinations(range(n),dxy):
                    y=sum(1<<i for i in supp)
                    Sy=set()
                    for Iy in itertools.combinations(range(n),ny):
                        Sy=star_set(y,set(Iy),Ty)
                        # 只取满足孤立条件的? 先全记
                        _,dx=sigma_and_delta(0,set(Ix),Tx)
                        _,dy=sigma_and_delta(y,set(Iy),Ty)
                        vals[len(dx&dy)]+=1
                        svals[len(Sx&Sy)]+=1
                    break   # 每个 Ix 只取一个 y（其余靠坐标置换等价）
            rows[(Tx,Ty,dxy)]=(min(vals),max(vals),sorted(vals))
            Srows[(Tx,Ty,dxy)]=(min(svals),max(svals))
    # 打印
print(f"{'(Tx,Ty)':10} {'δ':>2} {'|Δx∩Δy| 范围':>16} {'取值':>22} {'|Sx∩Sy|范围':>12}")
for Tx in ('A','B'):
    for Ty in ('A','B'):
        for dxy in (1,2,3,4):
            lo,hi,v=rows[(Tx,Ty,dxy)]; slo,shi=Srows[(Tx,Ty,dxy)]
            print(f"  ({Tx},{Ty}) {dxy:>2} {f'{lo}..{hi}':>16} {str(v):>22} {f'{slo}..{shi}':>12}")
print("\n 注: δ≥5 时 Δx∩Δy=∅（影子距 x 为 2）")
