#!/usr/bin/env python3
"""M03 E-型审计 第二刀：Soules-1，仅搜递增 x（1=x1<=x2<=...<=x5），变体 A。
输出 max d1；若 >=0 则给出精确证书并逐项核验 d_i>=0 与单调性。
"""
from fractions import Fraction as F
import itertools
LAM=[F(1),F(12,25),F(12,25),F(-41,50),F(-41,50)]; N=5
def dvals(x):
    xs=[F(0)]+list(x); S2=sum(xs[j]**2 for j in range(1,N+1)); out=[]
    for i in range(1,N+1):
        t1=xs[i]**2*LAM[0]/S2; t2=F(0)
        for k in range(i+1,N+1):
            num=(xs[i]*xs[k])**2*LAM[N-k+2-1]
            pre=sum(xs[j]**2 for j in range(1,k)); cur=pre+xs[k]**2
            t2+=num/(pre*cur)
        pre_i=sum(xs[j]**2 for j in range(1,i)); cur_i=pre_i+xs[i]**2
        t3=(pre_i*LAM[N-i+2-1]/cur_i) if i>=2 else F(0)
        out.append(t1+t2+t3)
    return out
vals=[F(1),F(3,2),F(2),F(5,2),F(3),F(4),F(5),F(6),F(8),F(10),F(12),F(16),F(20),F(25),F(30),F(40),F(50),F(64),F(100)]
best=None; hits=[]
cnt=0
for r,s,u,v in itertools.combinations_with_replacement(vals,4):
    x=(F(1),r,s,u,v); cnt+=1
    d=dvals(x)
    if best is None or d[0]>best[0]: best=(d[0],x,d)
    if d[0]>=0:
        mono=all(d[i]<=d[i+1] for i in range(N-1))
        hits.append((x,d,mono))
print("组合数:",cnt)
print("max d1 =",best[0],"=",float(best[0]))
print("  at x =",[str(t) for t in best[1]])
print("  d 向量 =",[str(t) for t in best[2]], " 全>=0?", all(t>=0 for t in best[2]))
print("d1>=0 的命中数:",len(hits))
for x,d,m in hits[:6]: print("   HIT x=",[str(t) for t in x],"d=",[str(t) for t in d],"单调?",m)
