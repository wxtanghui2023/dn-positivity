## CAP-MIX-1A: 奇特征 3-term cap truth vs 信息型 Frobenius 判据 I(p,n,d)
## 仅用于研究。p odd only.
import itertools
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
    a=trim(a);b=trim(b);inv=pow(b[-1],p-2,p);r=list(a);q=[0]*max(1,len(a)-len(b)+1)
    for i in range(len(a)-len(b),-1,-1):
        if len(r)-1<i: continue
        c=r[i+len(b)-1]*inv%p
        if c:
            q[i]=c
            for j in range(len(b)): r[i+j]=(r[i+j]-c*b[j])%p
    return trim(q),trim(r)
def gcd_p(a,b,p):
    a=trim(a);b=trim(b)
    while b!=(0,): a,b=b,divmod_p(a,b,p)[1]
    return a
def find_irred(p,n):
    for coef in itertools.product(range(p),repeat=n):
        f=tuple(list(coef)+[1]);ok=True
        for k in range(1,n//2+1):
            e=p**k;res=(1,);base=(0,1)
            while e:
                if e&1: res=poly_mulmod(res,base,f,p)
                base=poly_mulmod(base,base,f,p);e>>=1
            sub=list(res);sub[1]=(sub[1]-1)%p
            if len(gcd_p(f,tuple(sub),p))>1: ok=False;break
        if ok: return f
def primes(n):
    o=[];d=2
    while d*d<=n:
        while n%d==0: o.append(d);n//=d
        d+=1
    if n>1: o.append(n)
    return o
def build(p,n):
    f=find_irred(p,n);q=p**n
    els=[tuple((i//(p**k))%p for k in range(n)) for i in range(q)]
    idx={e:i for i,e in enumerate(els)}
    mul=[[0]*q for _ in range(q)];add=[[0]*q for _ in range(q)]
    for i in range(q):
        for j in range(i,q):
            v=idx[poly_mulmod(els[i],els[j],f,p)];mul[i][j]=v;mul[j][i]=v
    for i in range(q):
        for j in range(q): add[i][j]=idx[tuple((x+y)%p for x,y in zip(els[i],els[j]))]
    one=idx[(1,)+(0,)*(n-1)];zero=idx[tuple([0]*n)]
    neg=[idx[tuple((-x)%p for x in els[i])] for i in range(q)]
    return q,els,idx,mul,add,one,zero,neg
def powm(mul,x,e,one):
    r=one;b=x
    while e:
        if e&1: r=mul[r][b]
        b=mul[b][b];e>>=1
    return r
def order(q,mul,x,one):
    o=q-1
    for pr in primes(o):
        while o%pr==0 and powm(mul,x,o//pr,one)==one: o//=pr
    return o
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def is_ppow(r,p):
    while r%p==0 and r>1: r//=p
    return r==1
out=open("out/capmix1A_I_vs_truth.txt","w")
cases=[(3,2),(3,3),(3,4),(3,5),(3,6),(5,2),(5,3),(7,2),(7,3),(11,2),(13,2)]
counts={"PASS_cap":0,"PASS_noncap":0,"FAIL_cap":0,"FAIL_noncap":0}
for (p,n) in cases:
    q,els,idx,mul,add,one,zero,neg=build(p,n)
    gen=None
    for e in range(1,q):
        if order(q,mul,e,one)==q-1: gen=e;break
    hdr="===== p=%d n=%d q=%d"%(p,n,q); print(hdr); out.write(hdr+"\n")
    for d in divisors(q-1):
        if d<3: continue
        if d>200 and q>250: continue
        step=(q-1)//d; g=powm(mul,gen,step,one)
        G=[];x=one
        for i in range(d): G.append(x); x=mul[x][g]
        S=set(G)
        # truth (3-term, distinct)
        cap=True;ap=None
        for i in range(len(G)):
            for j in range(i+1,len(G)):
                c=neg[add[G[i]][G[j]]]
                if c in S and c!=G[i] and c!=G[j]: cap=False;ap=(G[i],G[j],c);break
            if not cap: break
        # I: informative j with Q_j trivial-only
        PASS=False;used=None
        for j in range(1,min(d,80)+1):
            r=pow(p,j,d)
            if r==0 or is_ppow(r,p): continue
            sgn=-1 if (p**j+r)%2 else 1
            nontriv=0
            for xx in G:
                lhs=add[powm(mul,xx,r,one)][one]
                rhs=powm(mul,add[xx][one],r,one)
                if sgn<0: rhs=neg[rhs]
                if lhs==rhs:
                    y=neg[add[xx][one]]
                    if y in S and y!=xx and xx!=one and y!=one: nontriv+=1;break
            if nontriv==0: PASS=True;used=(j,r,sgn);break
        key=("PASS_" if PASS else "FAIL_")+("cap" if cap else "noncap"); counts[key]+=1
        rec="q=%4d d=%4d |G|=%4d truth=%-3s I=%-4s used=%s"%(q,d,len(G),"cap" if cap else "non","PASS" if PASS else "FAIL",str(used))
        print(rec); out.write(rec+"\n")
print("COUNTS:",counts); out.write("COUNTS: "+str(counts)+"\n"); out.close()
