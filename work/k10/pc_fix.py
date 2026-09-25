import random, sys, itertools
from collections import Counter
sys.argv=['x','5','none']
exec(open('exact_pack.py').read().split('def main()')[0])
def mu_ordered(Cs):
    order=sorted(range(len(Cs)), key=lambda i: len(Cs[i]))
    best=[0,None]
    def rec(t,assign):
        if len(assign)+(len(Cs)-t)<=best[0]: return
        if t==len(Cs):
            if len(assign)>best[0]: best[0],best[1]=len(assign),dict(assign)
            return
        i=order[t]
        for q in Cs[i]:
            if all((q^assign[j]).bit_count()>=3 for j in assign):
                assign[i]=q; rec(t+1,assign); del assign[i]
        rec(t+1,assign)
    rec(0,{})
    return best[0], best[1]
random.seed(9090)
diag_ok=0; off_ok=0; tot=0
diag_hist=Counter(); offmin_hist=Counter()
for _ in range(500):
    D=tuple(sorted(random.sample(range(120),4)))
    Xw=[WORDS[i] for i in D]; U=U_of(D)
    if U==0: continue
    pts=[v for v in range(1024) if (U>>v)&1]
    Cs=[[q for q in pts if (q^x).bit_count()<=1] for x in Xw]
    m,w=mu_ordered(Cs)
    if m<4 or w is None: continue
    tot+=1
    R=[[(w[i]^Xw[j]).bit_count() for j in range(4)] for i in range(4)]
    dg=[R[i][i] for i in range(4)]
    off=min(R[i][j] for i in range(4) for j in range(4) if i!=j)
    diag_hist[max(dg)]+=1; offmin_hist[off]+=1
    if all(d<=1 for d in dg): diag_ok+=1
    if off>=2: off_ok+=1
print(f"样本(有4-见证) {tot} 例")
print(f"① 对角 max d(q_i,x_i) 分布 = {dict(sorted(diag_hist.items()))}  ⟹ **对角≤1 成立 {diag_ok}/{tot}**")
print(f"② 非对角 min d(q_i,x_j) (i≠j) 分布 = {dict(sorted(offmin_hist.items()))}  ⟹ **≥2 成立 {off_ok}/{tot}**")
