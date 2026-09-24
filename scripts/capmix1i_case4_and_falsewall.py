## CAP-MIX-1A(5): (2) case4=8 固定候选完备性 + 24 伪根墙不变量与 Frobenius 轨道
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
    A_rows=[];B_rows=[]
    out=open("out/capmix1I_case4_falsewall.txt","w")
    plan=[(3,range(2,8)),(5,range(2,5)),(7,range(2,5)),(11,range(2,4)),(13,range(2,4)),(17,range(2,3)),(19,range(2,3))]
    A={"n":0,"m2":0,"h2":0,"other":0,"all_two":0}
    B={"n":0,"F":0,"orb_counts":{},"one_orbit":0,"multi_orbit":0,"orb_sizes":[]}
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
            # 常量：-2 与 -1/2 的编码
            mtwo=negi(addi(one,one))
            half_inv=enc[tuple((pow(2,p-2,p)*c)%p for c in els[one])] if p!=2 else None
            mhalf=negi(half_inv) if half_inv is not None else None
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
                J=[];Xdm=Xd(d,p)
                for j in range(1,(ordm(p,d) or d)+1):
                    r=pow(p,j,d)
                    if r==0 or ispp(r,p): continue
                    sgn=-1 if (p**j+r)%2 else 1
                    J.append(gc(Qj(r,sgn,p),Xdm,p))
                if not J: continue
                if any(isXm1(h,p) for h in J): continue
                gs=J[0]
                for h in J[1:]: gs=gc(gs,h,p)
                dgs=len(gs)-1
                if dgs>200 or dgs<2: continue
                R=[xx for xx in G if ev(gs,xx)==0]
                T=0;F=0;degen=[]
                for xx in R:
                    if xx==one: continue
                    y=negi(addi(xx,one))
                    if y==one or y==xx: degen.append(xx)
                    elif y in S: T+=1
                    else: F+=1
                if T==0 and F==0:
                    A["n"]+=1
                    in2 = (mtwo in degen); inh = (mhalf in degen) if mhalf is not None else False
                    A["m2"]+= 1 if in2 else 0; A["h2"]+= 1 if inh else 0
                    other=[xx for xx in degen if xx!=mtwo and xx!=mhalf]
                    A["other"]+=len(other)
                    if all(xx==mtwo or xx==mhalf for xx in degen): A["all_two"]+=1
                    A_rows.append((p,q,d,len(R),len(degen),in2,inh,len(other)))
                elif T==0 and F>0:
                    B["n"]+=1;B["F"]+=F
                    # Frobenius orbits among false roots
                    fs=[xx for xx in R if ev(gs,xx)==0 and xx!=one and (negi(addi(xx,one)) not in S)]
                    seen=set();orbs=[]
                    for xx in fs:
                        if xx in seen: continue
                        orb=[];z=xx
                        while z not in seen:
                            seen.add(z);orb.append(z);z=powi(z,p)
                        orbs.append(len(orb))
                    B["orb_sizes"]+=orbs
                    if len(orbs)==1: B["one_orbit"]+=1
                    else: B["multi_orbit"]+=1
                    B_rows.append((p,q,d,len(R),F,len(orbs),orbs[:6],dgs))
    print("A(case4):",A)
    print("A_rows:",A_rows[:10])
    print("B(falsewall):",{k:v for k,v in B.items() if k!="orb_sizes"})
    print("B_orb_size_hist:",{s:B["orb_sizes"].count(s) for s in sorted(set(B["orb_sizes"]))})
    print("B_rows:",B_rows[:10])
    out.write("A:"+str(A)+"\n"+str(A_rows)+"\nB:"+str({k:v for k,v in B.items() if k!="orb_sizes"})+"\n"+str(B_rows)+"\n");out.close()
main()
