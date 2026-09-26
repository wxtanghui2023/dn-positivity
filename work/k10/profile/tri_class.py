#!/usr/bin/env python3
"""三角形局部 Hamming 分类 + μ(τ)=|B1(u)∩B1(v)∩B1(w)|
(a) 分类 (mod 平移+坐标置换)  (b) 6 个极值码上逐三角形验证 μ"""
import itertools
from collections import Counter, defaultdict
N=6  # n=6 足够覆盖所有距离<=2 的三元型
def ball(x): 
    m=[x]
    for i in range(N): m.append(x^(1<<i))
    return set(m)
print("="*70); print("(a) 三角形局部分类 (mod 平移 + 坐标置换)"); print("="*70)
groups=defaultdict(list)
for v in range(1,1<<N):
    for w in range(v+1,1<<N):
        dv=bin(v).count('1'); dw=bin(w).count('1'); dvw=bin(v^w).count('1')
        if max(dv,dw,dvw)>2: continue
        key=tuple(sorted([dv,dw,dvw]))
        mu=len(ball(0)&ball(v)&ball(w))
        groups[key].append((v,w,mu))
print("\n可能的距离型 (d_uv,d_vw,d_uw) 及 μ 分布:")
for key,items in sorted(groups.items()):
    mus=Counter(m for _,_,m in items)
    print(f"  型 {key}: 共 {len(items)} 个三元组, μ 分布 = {dict(mus)}")
    if len(mus)>1:
        # 细分：找出 μ 不同的代表
        for mu_val in sorted(mus):
            ex=[(format(v,'06b'),format(w,'06b')) for v,w,m in items if m==mu_val][:1]
            print(f"      μ={mu_val}: 例 {ex}")
print("\n奇偶校验: d(u,v)+d(v,w) ≡ d(u,w) (mod 2)  (F₂ 三角不等式)")
for key in sorted(groups):
    a,b,c=key
    print(f"  型 {key}: {a}+{b}={a+b} vs {c} ⟹ {'✓ 合法' if (a+b)%2==c%2 else '✗ 不合法'}")
print("\n"+"="*70); print("(b) 6 个极值码上的逐三角形 μ 检验"); print("="*70)
def build(n):
    NN=1<<n; BALL=[0]*NN
    for x in range(NN):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return NN,BALL
def check(n,C,tag):
    NN,BALL=build(n); Cs=set(C); FULL=(1<<NN)-1
    cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return
    T3=0; tri=0; mu0=0; mu1=0; mu2p=0
    b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(NN)}
    T3=sum(v*(v-1)*(v-2)//6 for v in b.values())
    for u,v,w in itertools.combinations(C,3):
        duv=bin(u^v).count('1'); duw=bin(u^w).count('1'); dvw=bin(v^w).count('1')
        if max(duv,duw,dvw)<=2:
            tri+=1
            mu=bin(BALL[u]&BALL[v]&BALL[w]).count('1')
            if mu==0: mu0+=1
            elif mu==1: mu1+=1
            else: mu2p+=1
    print(f"[{tag}] T3={T3} #三角形={tri} | μ=0:{mu0} μ=1:{mu1} μ≥2:{mu2p} ⟹ {'✓✓ 双射(全 μ=1)' if mu0==0 and mu2p==0 else '✗'}")
n=4;NN,BALL=build(n);FULL=(1<<NN)-1
for C in itertools.combinations(range(NN),4):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: check(n,list(C),"(4,4)=K"); break
n=5;NN,BALL=build(n);FULL=(1<<NN)-1
for C in itertools.combinations(range(NN),7):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: check(n,list(C),"(5,7)=K"); break
c1=[int(x,2) for x in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011".split()]
c2=[int(x,2) for x in "000100 000010 000001 100111 010111 001111 011000 101000 110000 111011 111101 111110".split()]
check(6,c1,"(6,12)=K 类#1"); check(6,c2,"(6,12)=K 类#2")
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
for i,c in enumerate(load62(),1): check(9,c,f"(9,62)=K 码#{i}")
