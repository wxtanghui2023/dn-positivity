## CAP-MIX-1A(4): radical 版 I*_rad 全 204 例。输出 PASS_rad / 新增 / FP / 按标签拆分 / 8 例恢复 + δ_j
import itertools
from math import gcd as igcd
def pt(a,p):
    a=list(a)
    while len(a)>1 and a[-1]%p==0: a.pop()
    return a
def mu2(a,b,p):
    if not a or not b: return [0]
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x%p:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    return pt(r,p)
def dv(a,b,p):
    a=pt(a[:],p);b=pt(b[:],p);inv=pow(b[-1],p-2,p);q=[0]*max(1,len(a)-len(b)+1);r=a[:]
    for i in range(len(a)-len(b),-1,-1):
        c=r[i+len(b)-1]*inv%p
        if c:
            q[i]=c
            for j in range(len(b)): r[i+j]=(r[i+j]-c*b[j])%p
    return pt(q,p),pt(r,p)
def gc(a,b,p):
    a=pt(a[:],p);b=pt(b[:],p)
    while not(len(b)==1 and b[0]==0): a,b=b,dv(a,b,p)[1]
    inv=pow(a[-1],p-2,p);return [(x*inv)%p for x in a]
def rad(f,p):
    f=pt(list(f),p)
    if len(f)<=1: return f
    d=[(i*f[i])%p for i in range(1,len(f))]; d=pt(d,p)
    if len(d)==1 and d[0]==0:
        h=pt([f[i] for i in range(0,len(f),p)],p)
        return rad(h,p)
    g=gc(f,d,p)
    q,_=dv(f,g,p)
    return pt(q,p)
def isXm1(g,p): return len(g)==2 and g[0]==(-1)%p and g[1]==1
def mulmod(base,e,f,p):
    res=[1];b=pt(base[:],p)
    while e:
        if e&1: res=dv(mu2(res,b,p),f,p)[1]
        b=dv(mu2(b,b,p),f,p)[1];e>>=1
    return res
def find_irred(p,n):
    for coef in itertools.product(range(p),repeat=n):
        f=pt(list(coef)+[1],p)
        if len(f)!=n+1: continue
        ok=True
        for k in range(1,n//2+1):
            h=mulmod([0,1],p**k,f,p);sub=[0]*max(len(h),2)
            for i,c in enumerate(h): sub[i]=c%p
            sub[1]=(sub[1]-1)%p
            if len(gc(f,sub,p))>1: ok=False;break
        if ok: return f
def Qj(r,sgn,p):
    A=[0]*(r+1);A[0]=1;A[r]=1;B=[1]
    for _ in range(r): B=mu2(B,[1,1],p)
    if sgn<0: B=[(-x)%p for x in B]
    n=max(len(A),len(B));A=A+[0]*(n-len(A));B=B+[0]*(n-len(B))
    return pt([(A[i]-B[i])%p for i in range(n)],p)
def Xd(d,p):
    v=[0]*(d+1);v[0]=(-1)%p;v[d]=1;return v
def divs(n): return [d for d in range(1,n+1) if n%d==0]
def ispp(r,p):
    while r%p==0 and r>1: r//=p
    return r==1
def ordm(p,d):
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
    st={"case":0,"cap":0,"PASS_alg":0,"PASS_rad":0,"FP_rad":0,"FP_alg":0,
        "cap_radPASS":0,"noncap_radPASS":0,"delta_pos_cases":0,"radXm1_cases":0,
        "new_only":0,"alldegen":0,"none_after_rad":0}
    newlist=[];deltas=[]
    out=open("out/capmix1H_radical.txt","w")
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
                J=[];Xdm=Xd(d,p)
                for j in range(1,(ordm(p,d) or d)+1):
                    r=pow(p,j,d)
                    if r==0 or ispp(r,p): continue
                    sgn=-1 if (p**j+r)%2 else 1
                    hj=gc(Qj(r,sgn,p),Xdm,p)
                    J.append((j,r,hj,rad(hj,p)))
                if not J:
                    st["alldegen"]+=1; continue
                pa=any(isXm1(A[2],p) for A in J)
                pr=any(isXm1(A[3],p) for A in J)
                if pa: st["PASS_alg"]+=1
                if pr:
                    st["PASS_rad"]+=1
                    if cap: st["cap_radPASS"]+=1
                    else: st["FP_rad"]+=1; out.write("FALSE POSITIVE rad p=%d q=%d d=%d\n"%(p,q,d))
                else:
                    st["none_after_rad"]+=1
                if pa and not cap: st["FP_alg"]+=1
                if pr and not pa:
                    st["new_only"]+=1; newlist.append((p,q,d,[(A[0],len(A[2])-1,len(A[3])-1) for A in J]))
                for A in J:
                    dj=len(A[2])-1; rj=len(A[3])-1
                    if dj>rj: st["delta_pos_cases"]+=1; deltas.append(dj-rj)
                    if isXm1(A[3],p): st["radXm1_cases"]+=1
                out.write("p=%2d q=%5d d=%5d cap=%-3s PASSalg=%-5s PASSrad=%-5s J=%s\n"%(
                    p,q,d,"Y" if cap else "N",str(pa),str(pr),
                    str([(A[0],len(A[2])-1,len(A[3])-1) for A in J][:5])))
    st["delta_max"]=max(deltas) if deltas else 0
    print("STATS:",st); print("NEW:",newlist[:12])
    out.write("STATS: "+str(st)+"\nNEW: "+str(newlist[:12])+"\n"); out.close()
main()
