## CAP-MIX-1A(2): 联合 gcd(Q_j,Q_k,X^d-1) + μ(p,n,d) + 反例保护 + Frobenius 轨道结构
import itertools
from math import gcd as igcd
def ptrim2(a,p):
    a=list(a)
    while len(a)>1 and a[-1]%p==0: a.pop()
    return a
def pmul2(a,b,p):
    if not a or not b: return [0]
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x%p:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    return ptrim2(r,p)
def pdivmod2(a,b,p):
    a=ptrim2(a[:],p);b=ptrim2(b[:],p);inv=pow(b[-1],p-2,p)
    q=[0]*max(1,len(a)-len(b)+1);r=a[:]
    for i in range(len(a)-len(b),-1,-1):
        c=r[i+len(b)-1]*inv%p
        if c:
            q[i]=c
            for j in range(len(b)): r[i+j]=(r[i+j]-c*b[j])%p
    return ptrim2(q,p),ptrim2(r,p)
def pgcd2(a,b,p):
    a=ptrim2(a[:],p);b=ptrim2(b[:],p)
    while not(len(b)==1 and b[0]==0): a,b=b,pdivmod2(a,b,p)[1]
    inv=pow(a[-1],p-2,p);return [(x*inv)%p for x in a]
def isXm1(g,p): return len(g)==2 and g[0]==(-1)%p and g[1]==1
def pmulmod(base,e,f,p):
    res=[1];b=ptrim2(base[:],p)
    while e:
        if e&1: res=pdivmod2(pmul2(res,b,p),f,p)[1]
        b=pdivmod2(pmul2(b,b,p),f,p)[1];e>>=1
    return res
def find_irred(p,n):
    for coef in itertools.product(range(p),repeat=n):
        f=ptrim2(list(coef)+[1],p)
        if len(f)!=n+1: continue
        ok=True
        for k in range(1,n//2+1):
            h=pmulmod([0,1],p**k,f,p)
            sub=[0]*max(len(h),2)
            for i,c in enumerate(h): sub[i]=c%p
            sub[1]=(sub[1]-1)%p
            if len(pgcd2(f,sub,p))>1: ok=False;break
        if ok: return f
def Qj(r,sgn,p):
    A=[0]*(r+1);A[0]=1;A[r]=1
    B=[1]
    for _ in range(r): B=pmul2(B,[1,1],p)
    if sgn<0: B=[(-x)%p for x in B]
    n=max(len(A),len(B));A=A+[0]*(n-len(A));B=B+[0]*(n-len(B))
    return ptrim2([(A[i]-B[i])%p for i in range(n)],p)
def Xd(d,p):
    v=[0]*(d+1);v[0]=(-1)%p;v[d]=1;return v
def divs(n): return [d for d in range(1,n+1) if n%d==0]
def is_ppow(r,p):
    while r%p==0 and r>1: r//=p
    return r==1
def ord_mod(p,d):
    if igcd(p,d)!=1: return None
    o=1;x=p%d
    while x!=1: x=x*p%d;o+=1
    return o
def mk(p,n):
    f=find_irred(p,n);q=p**n
    def tomul(a,b):
        r=[0]*(2*n-1)
        for i in range(n):
            if a[i]:
                for j in range(n): r[i+j]=(r[i+j]+a[i]*b[j])%p
        for i in range(2*n-2,n-1,-1):
            c=r[i]
            if c:
                for j in range(n+1): r[i-n+j]=(r[i-n+j]-c*f[j])%p
        return tuple(r[:n])
    return q,tomul
def main():
    st={"case":0,"mu1":0,"mu2":0,"mu3":0,"none":0,"alldegen":0,"Qzero_ok":0,"Qzero_bad":0,
        "jointPASS":0,"FP":0,"cap":0,"cert_cap":0}
    mu2list=[];alldegen_bad=[]
    out=open("out/capmix1F_joint.txt","w")
    plan=[(3,range(2,8)),(5,range(2,5)),(7,range(2,5)),(11,range(2,4)),(13,range(2,4)),(17,range(2,3)),(19,range(2,3))]
    for p,nr in plan:
        for n in nr:
            q=p**n
            if q>4000: continue
            _,tomul=mk(p,n)
            els=[tuple((i//(p**k))%p for k in range(n)) for i in range(q)]
            enc={e:i for i,e in enumerate(els)}
            one=enc[(1,)+(0,)*(n-1)]
            addi=lambda a,b: enc[tuple((x+y)%p for x,y in zip(els[a],els[b]))]
            negi=lambda a: enc[tuple((-x)%p for x in els[a])]
            muli=lambda a,b: enc[tomul(els[a],els[b])]
            def powi(a,e):
                r=one;b=a
                while e:
                    if e&1:r=muli(r,b)
                    b=muli(b,b);e>>=1
                return r
            m=q-1;prs=[];t=2
            while t*t<=m:
                if m%t==0:
                    prs.append(t)
                    while m%t==0: m//=t
                t+=1
            if m>1: prs.append(m)
            gen=None
            for e in range(1,q):
                if all(powi(e,(q-1)//pr)!=one for pr in prs): gen=e;break
            for d in divs(q-1):
                if d<3 or d>1200: continue
                st["case"]+=1
                step=(q-1)//d;g=powi(gen,step)
                G=[];x=one
                for i in range(d): G.append(x);x=muli(x,g)
                S=set(G)
                cap=True
                for xx in G:
                    y=negi(addi(xx,one))
                    if y in S and y!=xx and xx!=one and y!=one: cap=False;break
                if cap: st["cap"]+=1
                # informative j's + g_j
                J=[];Xdm=Xd(d,p)
                for j in range(1,(ord_mod(p,d) or d)+1):
                    r=pow(p,j,d)
                    if r==0: continue
                    sgn=-1 if (p**j+r)%2 else 1
                    Q=Qj(r,sgn,p)
                    if is_ppow(r,p):
                        if all(c%p==0 for c in Q): st["Qzero_ok"]+=1
                        else: st["Qzero_bad"]+=1;alldegen_bad.append((p,n,d,j,r))
                        continue
                    J.append((j,r,sgn,pgcd2(Q,Xdm,p)))
                mu=None;witness=None
                for (j,r,sgn,gj) in J:
                    if isXm1(gj,p): mu=1;witness=(j,);break
                if mu is None and len(J)>=2:
                    for A,B in itertools.combinations(J,2):
                        if len(A[3])<=1 or len(B[3])<=1: continue
                        gjk=pgcd2(A[3],B[3],p)
                        if isXm1(gjk,p): mu=2;witness=(A[0],B[0]);break
                if mu is None and len(J)>=3:
                    for A,B,C in itertools.combinations(J,3):
                        g3=pgcd2(pgcd2(A[3],B[3],p),C[3],p)
                        if isXm1(g3,p): mu=3;witness=(A[0],B[0],C[0]);break
                if not J: st["alldegen"]+=1
                elif mu==1: st["mu1"]+=1
                elif mu==2: st["mu2"]+=1;mu2list.append((p,n,q,d,witness,[(A[0],len(A[3])-1) for A in J]))
                elif mu==3: st["mu3"]+=1
                else: st["none"]+=1
                if mu is not None:
                    st["jointPASS"]+=1
                    if cap: st["cert_cap"]+=1
                    else: st["FP"]+=1;out.write("FALSE POSITIVE %d %d %d mu=%s\n"%(p,n,d,mu))
                out.write("p=%2d q=%5d d=%5d cap=%-3s mu=%-4s J=%s witness=%s\n"%(
                    p,q,d,"Y" if cap else "N",str(mu),str([(A[0],A[1],len(A[3])-1) for A in J][:5]),str(witness)))
    print("STATS:",st)
    print("QZERO bad:",alldegen_bad[:5])
    print("mu=2 sample:",mu2list[:8])
    out.write("STATS: "+str(st)+"\n");out.close()
main()
