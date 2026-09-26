#!/usr/bin/env python3
"""最终对照: 两个已知 (9,62) 码的完整不变量 + Wille 指纹检验"""
import itertools
from collections import Counter
def load2(fn):
    codes=[]; cur=[]
    for line in open(fn):
        s=line.split()
        if len(s)==9 and all(c in '01' for c in s): cur.append(int("".join(s),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
WILLE=[int("000001010",2),int("000101010",2),int("001001010",2),int("001101010",2)]
n=9;N=512
BALL=[0]*N
for x in range(N):
    m=1<<x
    for i in range(n): m|=1<<(x^(1<<i))
    BALL[x]=m
def audit(C):
    Cs=set(C)
    b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)}
    E=sum(v-1 for v in b.values()); Q2=sum((v-1)*(v-2)//2 for v in b.values())
    I=sum((b[c]-1)*(b[c]-2)//2 for c in C)
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in Cs)
    A1=A2=0
    for u,v in itertools.combinations(C,2):
        d=bin(u^v).count('1')
        if d==1:A1+=1
        elif d==2:A2+=1
    sqs=set()
    for u in C:
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i);c2=u^(1<<j);ac=u^(1<<i)^(1<<j)
            if a in Cs and c2 in Cs and ac in Cs: sqs.add(frozenset([u,a,c2,ac]))
    V=set()
    for s in sqs:V|=s
    return dict(E=E,Q2=Q2,I=I,S=S,A1=A1,A2=A2,Asum=A1+A2,Sq=len(sqs),V=len(V),
        Inw=I-len(V),dmax=max(b[c]-1 for c in C),prof=dict(sorted(Counter(b.values()).items())),
        N1=sum(1 for v in b.values() if v==1))
cs=load2('K_9_1_classif.txt')
rs=[audit(c) for c in cs]
print("=== 完整对照（两个已知最优 (9,62) 码）===")
keys=['E','Q2','Asum','dmax','N1','prof','A1','A2','I','S','Sq','V','Inw']
print(f"{'指标':6} | {'码#1 (K_9_1.txt)':>20} | {'码#2 (含方阵)':>18} | 判决")
for k in keys:
    a,b=rs[0][k],rs[1][k]
    same = (a==b)
    print(f"{k:6} | {str(a):>20} | {str(b):>18} | {'**钉住 ✓✓**' if same else '不钉 ✗'}")
print()
print("=== Wille 指纹检验（4 词）===")
for i,c in enumerate(cs):
    Cs=set(c)
    hit=[w for w in WILLE if w in Cs]
    print(f" 码#{i+1}: 直接命中 {len(hit)}/4 {[format(w,'09b') for w in hit]}")
# 检验: 码#2 是否 B_n-等价于含 Wille 四词的码（构造：把它的方阵映到 Wille 方阵）
print("\n=== B_n 等价性构造检验（码#2 的方阵 → Wille 方阵）===")
c2=set(cs[1])
sq=None
for u in sorted(c2):
    for i,j in itertools.combinations(range(n),2):
        a=u^(1<<i);c=u^(1<<j);ac=u^(1<<i)^(1<<j)
        if a in c2 and c in c2 and ac in c2: sq=(u,i,j);break
    if sq:break
u,i,j=sq
print(f" 码#2 的一个方阵: 基点={format(u,'09b')} 方向=({i},{j})")
# Wille 方阵差分: 基点 000001010, 两方向差 (3,4)→ 0-idx (2,3)
wb=int("000001010",2); wd=(2,3)
# 构造坐标置换把 {i,j}→{2,3}，其余任意（保持其余为恒等）
perm=list(range(n))
perm[i],perm[j]=wd[0],wd[1]
# 其余坐标填剩余位置
rest=[k for k in range(n) if k not in (wd[0],wd[1])]
others=[k for k in range(n) if k not in (i,j)]
for a,b in zip(others,rest): perm[a]=b
def apply_perm(x):
    y=0
    for a in range(n):
        if (x>>a)&1: y|=1<<perm[a]
    return y
# 平移: 把 u 映到 wb
shift = u ^ wb
img=set()
for x in c2:
    y=apply_perm(x) ^ shift
    img.add(y)
hitw=[w for w in WILLE if w in img]
print(f" 经过（坐标置换+平移）后: Wille 四词命中 {len(hitw)}/4 {[format(w,'09b') for w in hitw]}")
cov=0
for w in img: cov|=BALL[w]
print(f" 变换后仍为合法覆盖码: {cov==(1<<N)-1} ✓ | |img|={len(img)}")
