## CAP-MIX-1A(1) v2: 无表实现（内存安全）。对抗式假阳性搜索 + gcd(Q_j,X^d-1) 结构
import itertools
from math import gcd as igcd

# ---- F_p 多项式 ----
def ptrim(a,p):
    a=list(a)
    while len(a)>1 and a[-1]%p==0: a.pop()
    return a
def pmul(a,b,p):
    if not a or not b: return [0]
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x%p:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    return ptrim(r,p)
def pdivmod(a,b,p):
    a=ptrim(a[:],p); b=ptrim(b[:],p); inv=pow(b[-1],p-2,p)
    q=[0]*max(1,len(a)-len(b)+1); r=a[:]
    for i in range(len(a)-len(b),-1,-1):
        c=r[i+len(b)-1]*inv%p
        if c:
            q[i]=c
            for j in range(len(b)): r[i+j]=(r[i+j]-c*b[j])%p
    return ptrim(q,p),ptrim(r,p)
def pgcd(a,b,p):
    a=ptrim(a[:],p); b=ptrim(b[:],p)
    while not(len(b)==1 and b[0]==0): a,b=b,pdivmod(a,b,p)[1]
    inv=pow(a[-1],p-2,p); return [(x*inv)%p for x in a]
def ppowmod(base,e,f,p):
    res=[1]; b=ptrim(base[:],p)
    while e:
        if e&1: res=pdivmod(pmul(res,b,p),f,p)[1]
        b=pdivmod(pmul(b,b,p),f,p)[1]; e>>=1
    return res
def find_irred(p,n):
    for coef in itertools.product(range(p),repeat=n):
        if coef[0]==0 and n>1: pass
        f=ptrim(list(coef)+[1],p)
        if len(f)!=n+1: continue
        ok=True
        for k in range(1,n//2+1):
            h=ppowmod([0,1],p**k,f,p)
            sub=[0]*(max(len(h),2))
            for i,c in enumerate(h): sub[i]=c%p
            sub[1]=(sub[1]-1)%p
            if len(pgcd(f,sub,p))>1: ok=False;break
        if ok: return f
def Qpoly(r,sgn,p):
    A=[0]*(r+1); A[0]=1; A[r]=1
    B=[1]
    for _ in range(r): B=pmul(B,[1,1],p)
    if sgn<0: B=[(-x)%p for x in B]
    n=max(len(A),len(B)); A=A+[0]*(n-len(A)); B=B+[0]*(n-len(B))
    return ptrim([(A[i]-B[i])%p for i in range(n)],p)
def Xd(d,p):
    v=[0]*(d+1); v[0]=(-1)%p; v[d]=1; return v
def divs(n): return [d for d in range(1,n+1) if n%d==0]
def is_ppow(r,p):
    while r%p==0 and r>1: r//=p
    return r==1
def ord_mod(p,d):
    if igcd(p,d)!=1: return None
    o=1;x=p%d
    while x!=1: x=x*p%d;o+=1
    return o
# ---- GF(p^n)（元组表示，无表）----
def mkfield(p,n):
    f=find_irred(p,n); q=p**n
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
    return f,q,tomul
def main():
    stat={"N_case":0,"N_cap":0,"N_PASS":0,"N_FP":0,"N_cert_cap":0,"N_allegen":0,"N_nontrivgcd":0}
    fp=[]
    out=open("out/capmix1E_FP.txt","w")
    plan=[(3,range(2,8)),(5,range(2,5)),(7,range(2,5)),(11,range(2,4)),(13,range(2,4)),(17,range(2,3)),(19,range(2,3))]
    for p,nr in plan:
        for n in nr:
            q=p**n
            if q>4000: continue
            f,_,tomul=mkfield(p,n)
            els=[tuple((i//(p**k))%p for k in range(n)) for i in range(q)]
            enc={e:i for i,e in enumerate(els)}
            one=enc[(1,)+(0,)*(n-1)]
            def addi(a,b): return enc[tuple((x+y)%p for x,y in zip(els[a],els[b]))]
            def negi(a): return enc[tuple((-x)%p for x in els[a])]
            def muli(a,b): return enc[tomul(els[a],els[b])]
            def powi(a,e):
                r=one;b=a
                while e:
                    if e&1: r=muli(r,b)
                    b=muli(b,b);e>>=1
                return r
            prs=[]
            m=q-1
            d0=2
            while d0*d0<=m:
                if m%d0==0:
                    prs.append(d0)
                    while m%d0==0: m//=d0
                d0+=1
            if m>1: prs.append(m)
            gen=None
            for e in range(1,q):
                if all(powi(e,(q-1)//pr)!=one for pr in prs): gen=e;break
            for d in divs(q-1):
                if d<3 or d>1200: continue
                stat["N_case"]+=1
                step=(q-1)//d
                g=powi(gen,step)
                G=[];x=one
                for i in range(d): G.append(x); x=muli(x,g)
                S=set(G)
                # truth（独立 AP 搜索）
                cap=True
                for xx in G:
                    y=negi(addi(xx,one))
                    if y in S and y!=xx and xx!=one and y!=one: cap=False;break
                # 代数 PASS（先算）
                PASS=False;used=None;info=[]
                jmax=(ord_mod(p,d) or d)
                for j in range(1,jmax+1):
                    r=pow(p,j,d)
                    if r==0 or is_ppow(r,p): continue
                    sgn=-1 if (p**j+r)%2 else 1
                    gg=pgcd(Qpoly(r,sgn,p),Xd(d,p),p); dg=len(gg)-1
                    info.append((j,r,sgn,dg))
                    if dg==1 and gg==[(-1)%p,1]: PASS=True;used=(j,r,sgn);break
                if cap: stat["N_cap"]+=1
                if PASS:
                    stat["N_PASS"]+=1
                    if cap: stat["N_cert_cap"]+=1
                    else: stat["N_FP"]+=1; fp.append((p,n,q,d,used))
                else:
                    if not info: stat["N_allegen"]+=1
                    else: stat["N_nontrivgcd"]+=1
                out.write("p=%2d q=%5d d=%5d truth=%-3s PASS=%-2s used=%s deg_j1=%s\n"%(
                    p,q,d,"cap" if cap else "non","Y" if PASS else "N",str(used),
                    str([(i[3]) for i in info[:4]])))
    print("STATS:",stat); print("FP LIST:",fp[:20])
    out.write("STATS: "+str(stat)+"\nFP LIST: "+str(fp[:20])+"\n"); out.close()
main()
