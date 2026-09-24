## Q1 (LANE-A): n<=16, d|2^n-1, 非子域型: rho=lambda/d 的精确最大值 + 全部取到者
## 双算法: A=集合查表(1+x in G); B=阶检验((1+x)^d==1)
import sys
def pdeg(x): return x.bit_length()-1
def pmod(a,f):
    n=pdeg(f)
    while a and pdeg(a)>=n:
        a ^= f << (pdeg(a)-n)
    return a
def pmul(a,b,f):
    r=0
    while b:
        if b&1: r^=a
        a<<=1; b>>=1
    return pmod(r,f)
def ppow(a,e,f):
    r=1
    while e:
        if e&1: r=pmul(r,a,f)
        a=pmul(a,a,f); e>>=1
    return r
def pgcd(a,b):
    while b:
        a,b=b,pmod(a,b)
    return a
def irred(f,n):
    x=2
    if ppow(x,1<<n,f)!=pmod(x,f): return False
    for p in primes_of(n):
        h=ppow(x,1<<(n//p),f)
        g=pgcd(h^pmod(x,f),f)
        if pdeg(g)>0: return False
    return True
def primes_of(m):
    s=set();d=2
    while d*d<=m:
        while m%d==0: s.add(d);m//=d
        d+=1
    if m>1: s.add(m)
    return sorted(s)
def find_field(n):
    cand=0
    for low in range(1<<n):
        cand=(1<<n)|low
        if irred(cand,n): return cand
    raise RuntimeError
def divisors(m):
    ds=[];i=1
    while i*i<=m:
        if m%i==0:
            ds.append(i)
            if i!=m//i: ds.append(m//i)
        i+=1
    return sorted(ds)
def is_subfield_type(d):
    k=1
    while (1<<k)-1<=d:
        if (1<<k)-1==d: return True
        k+=1
    return False
def main():
    rows=[];bad=0
    out=open("out/q1_lane_a.txt","w")
    for n in range(2,17):
        q=1<<n; f=find_field(n); M=q-1
        prim=None
        for g in range(2,q):
            ok=True
            for p in primes_of(M):
                if ppow(g,M//p,f)==1: ok=False;break
            if ok: prim=g;break
        assert prim is not None
        divs=[d for d in divisors(M) if d>=3]
        for d in divs:
            sub=is_subfield_type(d)
            if sub: continue
            step=M//d; base=ppow(prim,step,f)
            G=[];x=1
            for i in range(d):
                G.append(x); x=pmul(x,base,f)
            S=set(G)
            lA=sum(1 for a in G if (a^1) in S and (a^1)!=0)
            lB=sum(1 for a in G if (a^1)!=0 and ppow(a^1,d,f)==1)
            if lA!=lB: bad+=1
            rows.append((n,d,q,lA,rho:=lA/d,sub,lB))
            out.write("n=%2d d=%6d q=%6d sub=False lA=%6d lB=%6d rho=%.6f\n"%(n,d,q,lA,lB,rho))
        print("n=%2d done (q=%d, 非子域 d 数=%d)"%(n,q,len([1 for d in divs if not is_subfield_type(d)])),flush=True)
    non=[r for r in rows if not r[5]]
    mx=max(r[4] for r in non)
    eqs=[r for r in non if abs(r[4]-mx)<1e-15]
    print("\n=== 非子域案例数: %d ; 双算法不一致: %d ==="%(len(non),bad))
    print("rho_max = %.10f = %s"%(mx, "8/21" if abs(mx-8/21)<1e-12 else "其他"))
    print("取到者 (%d 个):"%len(eqs))
    for r in eqs: print("   n=%2d d=%4d q=%6d lambda=%d rho=%.10f"%(r[0],r[1],r[2],r[3],r[4]))
    print("\ntop-15 非子域:")
    for r in sorted(non,key=lambda t:-t[4])[:15]:
        print("   n=%2d d=%6d lambda=%6d rho=%.6f"%(r[0],r[1],r[3],r[4]))
    out.write("ROWS=%d BAD=%d RHO_MAX=%.10f EQ=%s\n"%(len(non),bad,mx,[(r[0],r[1]) for r in eqs]))
    out.close()
main()
