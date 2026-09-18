# -*- coding: utf-8 -*-
# 仅用于离线数据分析（非研究结论）
import array, math
from collections import Counter
from sympy import primerange

N = 20_000_000
sv = bytearray([1])*(N+1); sv[0]=sv[1]=0
i=2
while i*i<=N:
    if sv[i]: sv[i*i::i]=bytearray(len(range(i*i,N+1,i)))
    i+=1
pr=(array.array('l',[j for j in range(2,N+1) if sv[j]]))
del sv
n=len(pr); gaps=array.array('l',(pr[k+1]-pr[k] for k in range(n-1))); m=len(gaps)

# 奇异级数 for pattern {0,h1,h2}
def nu(q,h1,h2):
    return len({0%q,h1%q,h2%q})
def sing(h1,h2,Q=20000):
    pr_=list(primerange(2,Q))
    s=1.0
    for q in pr_:
        v=nu(q,h1,h2)
        if v>=q: return 0.0
        s *= (1-v/q)/((1-1/q)**3)
    return s

pats=[(2,2),(2,4),(2,6),(2,8),(4,2),(4,4),(4,6),(4,10),(6,2),(6,4),(6,6),(6,8),(6,10),(12,12),(2,10),(4,8),(6,12),(8,4)]
obs={p:0 for p in pats}
for k in range(m-1):
    t=(gaps[k],gaps[k+1])
    if t in obs: obs[t]+=1
tot=sum(obs.values())
print(f"N={N:,}  素数={n:,}  间隙对总数(受限模式集)={tot:,}")
print(f"\n{'pattern':>12} {'S(h1,h2)':>12} {'HL 预测比':>12} {'实测比':>12} {'实测/预测':>10}  {'可容许'}")
pred_sum=sum(sing(g1,g1+g2) for g1,g2 in pats)
rows=[]
for g1,g2 in pats:
    S=sing(g1,g1+g2)
    pred=S/pred_sum
    o=obs[(g1,g2)]/tot
    ratio=(o/pred) if pred>0 else float('nan')
    rows.append((g1,g2,S,pred,o,ratio))
for g1,g2,S,pred,o,ratio in rows:
    admissible = '是' if S>0 else '否(奇异级数=0)'
    print(f"{str((g1,g2)):>12} {S:12.6f} {pred:12.6f} {o:12.6f} {ratio:10.4f}  {admissible}")
# 相关系数（对数尺度，排除不可容许）
import statistics as st
xs=[math.log(sing(g1,g1+g2)) for g1,g2,S,_,_,_ in rows if S>0]
ys=[math.log(o) for g1,g2,S,pred,o,_ in rows if S>0]
mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
num=sum((a-mx)*(b-my) for a,b in zip(xs,ys)); dx=math.sqrt(sum((a-mx)**2 for a in xs)); dy=math.sqrt(sum((b-my)**2 for b in ys))
print(f"\n可容许模式（{len(xs)} 个）上 log 奇异级数 vs log 实测频率的相关系数 = {num/(dx*dy):+.5f}")
