# -*- coding: utf-8 -*-
# 仅用于离线数据分析（非研究结论）
import numpy as np, math, time
from sympy import primerange
t0=time.time()
N = 40_000_000                      # Λ 到 4e7
sv = bytearray([1])*(N+1); sv[0]=sv[1]=0
i=2
while i*i<=N:
    if sv[i]: sv[i*i::i]=bytearray(len(range(i*i,N+1,i)))
    i+=1
pr = np.array([j for j in range(2,N+1) if sv[j]], dtype=np.int64)
del sv
Lam = np.zeros(N+1, dtype=np.float64)
pows=[]
for p in pr:
    lp = math.log(p); pk = p
    while pk <= N:
        Lam[pk] = lp; pk *= p
print(f"N={N:,}  素数个数={len(pr):,}  用时{time.time()-t0:.1f}s")

# 奇异级数（von Mangoldt 对）: S(h)=prod_p (1-nu_p/p)/(1-1/p)^2, nu_p=1(p|h) else 2
C2 = 1.3203236316937381   # 2 * prod_{p>2}(1-1/(p-1)^2) = 2 * 孪生素数常数
def sing(h):
    s = C2
    for p in primerange(3, int(h**0.5)+2):
        if p>2 and h % p == 0:
            s *= (p-1)/(p-2)
    # 大素因子（p|h 且 p>sqrt(h) 只可能有 1 个）
    r = h
    for p in primerange(3, 100000):
        if p*p > r: break
        while r % p == 0: r//=p
    if r > 1 and r > 2: s *= (r-1)/(r-2)
    return s

print("\n[A] C(h)=Σ_{n≤X}Λ(n)Λ(n+h) 与 HL 预测 S(h)·X 的比值（X=C(h) 的求和上界）")
print("   h            S(h)      C(h)          S(h)*Xeff      C/(S*Xeff)")
for X in (10**6, 10**7):
    print(f"  --- X = {X:,} ---")
    for h in (2,6,30,100,1000,10**4,10**5, 5*10**5, 10**6, 3*10**6, 5*10**6):
        if h >= X: continue
        Xeff = X - h
        C = float(np.dot(Lam[2:Xeff+1], Lam[2+h:Xeff+1+h]))
        S = sing(h)
        print(f"   {h:9d}  {S:9.5f}  {C:14.1f}   {S*Xeff:14.1f}   {C/(S*Xeff):9.5f}")

print("\n[B] 比值检验（比值应≈ S(h1)/S(h2)，与 X 无关）")
X=10**7; hs=[2,4,6,12,30,60,210,1000,1024]
Cs={}
for h in hs:
    Xeff=X-h
    Cs[h]=float(np.dot(Lam[2:Xeff+1], Lam[2+h:Xeff+1+h]))
print("    h    C(h)实测    C(h)/C(2)      S(h)/S(2)      相对差")
for h in hs:
    a=Cs[h]/Cs[2]; b=sing(h)/sing(2)
    print(f"  {h:6d}  {Cs[h]:13.1f}   {a:11.6f}   {b:11.6f}   {a/b-1:+.4%}")
print(f"\n总用时 {time.time()-t0:.1f}s")
