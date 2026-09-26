#!/usr/bin/env python3
import itertools, random
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def stats(n,C):
    N,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    if any(v==0 for v in b.values()): return None
    E=sum(v-1 for v in b.values()); Q2=sum((v-1)*(v-2)//2 for v in b.values())
    I=sum((b[x]-1)*(b[x]-2)//2 for x in Cs)
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in Cs)
    h=sum(1 for x in C if b[x]-1>=3)
    A2=sum(1 for u,v in itertools.combinations(C,2) if bin(u^v).count('1')==2)
    return dict(E=E,Q2=Q2,I=I,S=S,h=h,A2=A2,twoA2=2*A2,bound=min(S,(E+Q2-S)/3) if (E+Q2-S)>=0 else S)
random.seed(7)
# 复用 seed: 两个已知 n=6 类 + 1986 文献码
seeds=[]
c1=[0b000000,0b000001,0b000010,0b001111,0b010111,0b011100,0b100111,0b101100,0b110100,0b111001,0b111010,0b111011]
seeds.append(c1)
lit=[0b000100,0b000010,0b000001,0b100111,0b010111,0b001111,0b011000,0b101000,0b110000,0b111011,0b111101,0b111110]
seeds.append(lit)
out=[]
for C in seeds:
    r=stats(6,C)
    if r: out.append(r)
print("=== n=6 M=12 精确值 ===")
for i,r in enumerate(out):
    print(f" seed{i}: E={r['E']} Q₂={r['Q2']} **I={r['I']} S={r['S']}** h={r['h']} A₂={r['A2']} 2A₂={r['twoA2']} h≤min{{S,(E+Q₂−S)/3}}={r['bound']:.2f} h≤I/3={r['I']/3:.2f}")
