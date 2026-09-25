#!/usr/bin/env python3
"""完整 Level B 检验：C_x = B₁(x)∩U_D 中存活候选数（真 Level B）+ 私有点存活对照。"""
import random, sys
from collections import Counter
sys.argv=['x','5','none']
exec(open('exact_pack.py').read().split('def main()')[0])
PRIV={i:[v for v in range(1024) if owners[v]==[i]] for i in range(120)}
def greedy_pack(pts,target,banned=0):
    rem=pts&~banned; got=[]
    while len(got)<target and rem:
        v=(rem&-rem).bit_length()-1; got.append(v)
        t=rem; nxt=0
        while t:
            u=(t&-t).bit_length()-1; t&=t-1
            if (u^v).bit_count()>=3: nxt|=1<<u
        rem=nxt
    return got
random.seed(555)
surv_all=Counter(); surv_priv=Counter(); fail=0; fail_priv=0; tot=0
for _ in range(400):
    D=tuple(sorted(random.sample(range(120),4)))
    Xw=[WORDS[i] for i in D]; U=U_of(D)
    if U==0: continue
    pts=[v for v in range(1024) if (U>>v)&1]
    for xi in range(4):
        x=Xw[xi]; wt=D[xi]
        B1x=(1<<x)|sum(1<<(x^(1<<j)) for j in range(10))
        P=greedy_pack(U,3,banned=B1x)
        if len(P)<3: continue
        Cx=[v for v in pts if (B1x>>v)&1]                    # 合法候选
        Sa=[v for v in Cx if not any((v^p).bit_count()<=2 for p in P)]
        pv=[v for v in PRIV[wt] if (B1x>>v)&1]
        Sp=[v for v in pv if not any((v^p).bit_count()<=2 for p in P)]
        tot+=1; surv_all[len(Sa)]+=1; surv_priv[len(Sp)]+=1
        if not Sa: fail+=1
        if not Sp: fail_priv+=1
print(f"样本 {tot}")
print(f"真 Level B（C_x 存活候选数）分布: {dict(sorted(surv_all.items()))}")
print(f"  ⟹ Level B 失败例数 = {fail}  （应为 0）")
print(f"私有点存活数分布: {dict(sorted(surv_priv.items()))}")
print(f"  ⟹ 私有点路线失败例数 = {fail_priv}")
