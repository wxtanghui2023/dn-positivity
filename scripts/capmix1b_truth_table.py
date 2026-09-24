## CAP-MIX-1b: index-table version (fast). 仅用于研究。
import itertools
from math import gcd

def poly_mulmod(a,b,f,p):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    n=len(f)-1
    for i in range(len(r)-1,n-1,-1):
        c=r[i]
        if c:
            for j in range(n+1): r[i-n+j]=(r[i-n+j]-c*f[j])%p
    return tuple(r[:n])

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)

def divmod_p(a,b,p):
    a=trim(a); b=trim(b); inv=pow(b[-1],p-2,p); r=list(a); q=[0]*max(1,len(a)-len(b)+1)
    for i in range(len(a)-len(b),-1,-1):
        if len(r)-1<i: continue
        c=r[i+len(b)-1]*inv%p
        if c:
            q[i]=c
            for j in range(len(b)): r[i+j]=(r[i+j]-c*b[j])%p
    return trim(q),trim(r)

def gcd_p(a,b,p):
    a=trim(a); b=trim(b)
    while b!=(0,): a,b=b,divmod_p(a,b,p)[1]
    return a

def find_irred(p,n):
    for coef in itertools.product(range(p),repeat=n):
        f=tuple(list(coef)+[1]); ok=True
        for k in range(1,n//2+1):
            e=p**k; res=(1,); base=(0,1)
            while e:
                if e&1: res=poly_mulmod(res,base,f,p)
                base=poly_mulmod(base,base,f,p); e>>=1
            sub=list(res); sub[1]=(sub[1]-1)%p
            if len(gcd_p(f,tuple(sub),p))>1: ok=False;break
        if ok: return f
    raise RuntimeError

def primes(n):
    out=[];d=2
    while d*d<=n:
        while n%d==0: out.append(d);n//=d
        d+=1
    if n>1: out.append(n)
    return out

def build(p,n):
    f=find_irred(p,n); q=p**n
    els=[tuple((i//(p**k))%p for k in range(n)) for i in range(q)]
    idx={e:i for i,e in enumerate(els)}
    mul=[[0]*q for _ in range(q)]
    for i in range(q):
        for j in range(i,q): 
            v=idx[poly_mulmod(els[i],els[j],f,p)]; mul[i][j]=v; mul[j][i]=v
    add=[[0]*q for _ in range(q)]
    for i in range(q):
        for j in range(q): add[i][j]=idx[tuple((x+y)%p for x,y in zip(els[i],els[j]))]
    one=idx[(1,)+(0,)*(n-1)]; zero=idx[tuple([0]*n)]
    return q,els,idx,mul,add,one,zero

def order(q,mul,x,one):
    if x==0: return 0
    o=q-1
    for pr in primes(o):
        while o%pr==0 and powm(mul,x,o//pr,one)==one: o//=pr
    return o

def powm(mul,x,e,one):
    r=one; b=x
    while e:
        if e&1: r=mul[r][b]
        b=mul[b][b]; e>>=1
    return r

def divisors(n): return [d for d in range(1,n+1) if n%d==0]

def subgroup(q,mul,gen,d,one):
    step=(q-1)//d; g=powm(mul,gen,step,one)
    S=[];x=one
    for i in range(d): S.append(x); x=mul[x][g]
    return S

def is_cap(q,mul,add,neg_of,G):
    S=set(G); n=len(G)
    for i in range(n):
        a=G[i]
        for j in range(i+1,n):
            c=neg_of[add[G[i]][G[j]]]
            if c in S and c!=G[i] and c!=G[j]: return False,(G[i],G[j],c)
    return True,None

def main():
    out=open("out/capmix1_truth_table.txt","w")
    cases=[(2,3),(2,4),(2,5),(2,6),(2,8),(3,2),(3,3),(3,4),(3,5),(3,6),(5,2),(5,3),(7,2),(11,2),(13,2)]
    for (p,n) in cases:
        q,els,idx,mul,add,one,zero=build(p,n)
        neg_of=[0]*q
        for i in range(q): neg_of[i]=idx[tuple((-x)%p for x in els[i])]
        gen=None
        for e in range(1,q):
            if order(q,mul,e,one)==q-1: gen=e;break
        line="===== p=%d n=%d q=%d (gen=%d)"%(p,n,q,gen)
        print(line); out.write(line+"\n")
        for d in divisors(q-1):
            if d<3: continue
            if d>200 and (q>250): continue
            G=subgroup(q,mul,gen,d,one)
            cap,ap=is_cap(q,mul,add,neg_of,G)
            # completeness via Sum2
            comp=None
            if cap:
                S2=set()
                m=len(G)
                for i in range(m):
                    for j in range(i+1,m): S2.add(neg_of[add[G[i]][G[j]]])
                comp=all((z in S2) for z in range(q) if z!=zero and z not in set(G))
            # certificate
            cert=None
            if d<=200:
                r=1; S=set(G)
                for j in range(1,2*d+3):
                    r=r*p%d
                    if r==0: continue
                    sgn=-1 if (p**j+r)%2 else 1
                    bad=0
                    for x in G:
                        lhs=add[powm(mul,x,r,one)][one]
                        rhs=powm(mul,add[x][one],r,one)
                        if sgn<0: rhs=neg_of[rhs]
                        if lhs==rhs:
                            y=neg_of[add[x][one]]
                            if y in S and y!=x and x!=one and y!=one: bad+=1
                    if bad==0: cert=(j,r,sgn); break
            rec="q=%4d d=%4d |G|=%4d cap=%s complete=%-5s cert(j,r,sgn)=%s"%(q,d,len(G),"Y" if cap else "N",str(comp),str(cert))
            if not cap: rec+="  minAP="+str([idx_show(ap,els)])
            print(rec); out.write(rec+"\n")
    out.close()
def idx_show(t,els): return [els[i] for i in t]
main()
