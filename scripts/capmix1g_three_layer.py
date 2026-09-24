## CAP-MIX-1A(3) 第⑤步：none=75 三层分离（共同真根/共同伪根/Frobenius 轨道）
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
    st={"none":0,"case1_Xm1":0,"case2_true":0,"case3_false":0,"case4_audit":0,
        "cap_with_true":0,"noncap_no_true":0,"orbit_all_out":0,"orbit_mixed":0,"skipped_deg":0,
        "sum_Ntrue":0,"sum_Nfalse":0}
    out=open("out/capmix1G_three_layer.txt","w")
    plan=[(3,range(2,8)),(5,range(2,5)),(7,range(2,5)),(11,range(2,4)),(13,range(2,4)),(17,range(2,3)),(19,range(2,3))]
    for p,nr in plan:
        for n in nr:
            q=p**n
            if q>4000: continue
            _,tomul=mk(p,n)
            els=[tuple((i//(p**k))%p for k in range(n)) for i in range(q)]
            enc={e:i for i,e in enumerate(els)}
            one=enc[(1,)+(0,)*(n-1)];zero=enc[tuple([0]*n)]
            scal=[enc[(c,)+(0,)*(n-1)] for c in range(p)]
            addi=lambda a,b: enc[tuple((x+y)%p for x,y in zip(els[a],els[b]))]
            negi=lambda a: enc[tuple((-x)%p for x in els[a])]
            muli=lambda a,b: enc[tomul(els[a],els[b])]
            def powi(a,e):
                r=one;b=a
                while e:
                    if e&1:r=muli(r,b)
                    b=muli(b,b);e>>=1
                return r
            def ev(poly,x):
                v=zero
                for c in reversed(poly):
                    v=muli(v,x)
                    if c%p: v=addi(v,scal[c%p])
                return v
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
                step=(q-1)//d;g=powi(gen,step)
                G=[];x=one
                for i in range(d): G.append(x);x=muli(x,g)
                S=set(G)
                cap=True
                for xx in G:
                    y=negi(addi(xx,one))
                    if y in S and y!=xx and xx!=one and y!=one: cap=False;break
                J=[];Xdm=Xd(d,p)
                for j in range(1,(ordm(p,d) or d)+1):
                    r=pow(p,j,d)
                    if r==0 or ispp(r,p): continue
                    sgn=-1 if (p**j+r)%2 else 1
                    J.append((j,r,pg:=None) if False else (j,r,gc(Qj(r,sgn,p),Xdm,p)))
                if not J: continue
                if any(isXm1(A[2],p) for A in J): continue    # 一阶/μ=1 不进本表
                st["none"]+=1
                gs=J[0][2]
                for A in J[1:]: gs=gc(gs,A[2],p)
                dgs=len(gs)-1
                if dgs>200: st["skipped_deg"]+=1; out.write("SKIP deg p=%d q=%d d=%d deg=%d\n"%(p,q,d,dgs)); continue
                R=[xx for xx in G if ev(gs,xx)==0]
                Nt=0;Nf=0
                for xx in R:
                    if xx==one: continue
                    y=negi(addi(xx,one))
                    if y==one or y==xx: continue
                    if y in S: Nt+=1
                    else: Nf+=1
                st["sum_Ntrue"]+=Nt; st["sum_Nfalse"]+=Nf
                if dgs==1 and isXm1(gs,p): st["case1_Xm1"]+=1
                elif Nt>0: st["case2_true"]+=1
                elif Nf>0: st["case3_false"]+=1
                else: st["case4_audit"]+=1
                if Nt>0 and cap: st["cap_with_true"]+=1
                if Nt==0 and not cap: st["noncap_no_true"]+=1
                # Frobenius 轨道
                seen=set();orbits=[]
                for xx in R:
                    if xx==one or xx in seen: continue
                    orb=[];z=xx
                    while z not in seen:
                        seen.add(z);orb.append(z);z=powi(z,p)
                    orbits.append(orb)
                for orb in orbits:
                    outs=[]
                    for xx in orb:
                        y=negi(addi(xx,one))
                        outs.append((y in S) and y!=one and y!=xx)
                    if any(outs) and any(not o for o in outs): st["orbit_mixed"]+=1
                    elif not any(outs): st["orbit_all_out"]+=1
                out.write("p=%2d q=%5d d=%5d cap=%-3s deg_gs=%4d |R|=%3d Ntrue=%3d Nfalse=%3d orb=%s\n"%(
                    p,q,d,"Y" if cap else "N",dgs,len(R),Nt,Nf,str([len(o) for o in orbits][:6])))
    print("STATS:",st); out.write("STATS: "+str(st)+"\n"); out.close()
main()
