#!/usr/bin/env python3
"""C2 区间层【并行版】：同一 float 分区（确定性 ✓）→ 落盘终端箱 → 3 进程区间复核 ✓
数学与判据完全同 C2（T_C=F(z*)+1e-9，丢弃半径 ρ_g−1e-9，min 聚合）✓"""
import math,numpy as np,json,itertools,os,sys
from multiprocessing import Pool
PI=math.pi;K=15
r2=0.79051323395036623846;r3=0.83020729481457293027
p1=0.34277969225757373739;p2=2.5781910808964293534;p3=1.4505341840121660277
z0=[r2,r3,p1,p2,p3];sig=[r3,r2,p1,p3,p2]
RHO_G=1.9782244e-3;DISC_R=RHO_G-1e-9
def cosr(k,lo,hi):
    a,b=k*lo,k*hi
    if a>b:a,b=b,a
    mn=min(math.cos(a),math.cos(b));mx=max(math.cos(a),math.cos(b))
    for j in range(int(math.floor(a/PI)),int(math.ceil(b/PI))+1):
        t=PI*j
        if a<=t<=b and j%2!=0:mn=-1.0
    for j in range(int(math.floor(a/(2*PI))),int(math.ceil(b/(2*PI)))+1):
        t=2*PI*j
        if a<=t<=b:mx=1.0
    return mn,mx
def LB(b):
    best=-1e18
    for k in range(1,K+1):
        c1=cosr(k,b[2][0],b[2][1]);c2=cosr(k,b[3][0],b[3][1]);c3=cosr(k,b[4][0],b[4][1])
        p2v=[b[0][0]**k*c2[0],b[0][0]**k*c2[1],b[0][1]**k*c2[0],b[0][1]**k*c2[1]]
        p3v=[b[1][0]**k*c3[0],b[1][0]**k*c3[1],b[1][1]**k*c3[0],b[1][1]**k*c3[1]]
        s=c1[0]+min(p2v)+min(p3v)
        if s>best:best=s
    return best
def supF(b):
    best=-1e18
    for k in range(1,K+1):
        c1=cosr(k,b[2][0],b[2][1]);c2=cosr(k,b[3][0],b[3][1]);c3=cosr(k,b[4][0],b[4][1])
        p2v=[b[0][0]**k*c2[0],b[0][0]**k*c2[1],b[0][1]**k*c2[0],b[0][1]**k*c2[1]]
        p3v=[b[1][0]**k*c3[0],b[1][0]**k*c3[1],b[1][1]**k*c3[0],b[1][1]**k*c3[1]]
        s=c1[1]+max(p2v)+max(p3v)
        if s>best:best=s
    return best
TBOX=[[v-1e-21,v+1e-21] for v in z0]
TC=supF(TBOX)+1e-9
if __name__=='__main__':
    print("="*100);print("C2 区间层【并行版】");print("="*100)
    print(f"T_C = {TC:.15f}  （F(z*)={max(math.cos(k*p1)+r2**k*math.cos(k*p2)+r3**k*math.cos(k*p3) for k in range(1,K+1)):.15f}）")
    N0=8;CAP=1_500_000;MINW=1e-7
    g=[(0.0,1.0),(0.0,1.0),(0.0,PI),(0.0,PI),(0.0,PI)]
    Bd=[[[g[j][0]+(g[j][1]-g[j][0])*i/N0,g[j][0]+(g[j][1]-g[j][0])*(i+1)/N0] for i in range(N0)] for j in range(5)]
    st=[[Bd[j][ix[j]] for j in range(5)] for ix in itertools.product(range(N0),repeat=5)]
    ne=0;ns=0;nu=0;nd=0;terms=[];minf=None;disc_far=0.0
    while st:
        b=st.pop();ne+=1
        if ne>CAP:nu+=len(st);break
        far=min(math.sqrt(sum(max(abs(b[j][0]-c[j]),abs(b[j][1]-c[j]))**2 for j in range(5))) for c in (z0,sig))
        if far<=DISC_R:nd+=1;disc_far=max(disc_far,far);continue
        lb=LB(b)
        if lb>=TC:
            terms.append(b)
            if minf is None or lb<minf:minf=lb
            continue
        w=max(b[j][1]-b[j][0] for j in range(5))
        if w<MINW:nu+=1;continue
        ns+=1
        j=int(np.argmax([b[t][1]-b[t][0] for t in range(5)]));mid=(b[j][0]+b[j][1])/2
        b1=[r[:] for r in b];b1[j][1]=mid
        b2=[r[:] for r in b];b2[j][0]=mid
        st.append(b1);st.append(b2)
    print(f"① float 分区：评估 {ne:,}  待区间复核 {len(terms):,}  丢弃 {nd:,}  分裂 {ns:,}  未决 {nu:,}")
    print(f"   丢弃箱最远角 max = {disc_far:.12f} ≤ DISC_R? {disc_far<=DISC_R} ✓")
    print(f"② 启动 3 进程区间复核（{len(terms):,} 箱）...",flush=True)
    with open('/tmp/dC2_terms.json','w') as f: json.dump(terms,f)
    import mpmath as mp
    def worker(chunk):
        mp.mp.dps=40
        D=mp.mpf
        class Iv:
            __slots__=('a','b')
            def __init__(s,a,b):s.a=min(a,b)-D('1e-30');s.b=max(a,b)+D('1e-30')
            @staticmethod
            def _v(o):return o if isinstance(o,Iv) else Iv(o,o)
            def __add__(s,o):o=Iv._v(o);return Iv(s.a+o.a,s.b+o.b)
            __radd__=__add__
            def __mul__(s,o):
                o=Iv._v(o);c=[s.a*o.a,s.a*o.b,s.b*o.a,s.b*o.b];return Iv(min(c),max(c))
            __rmul__=__mul__
        def civ(k,lo,hi):
            a=D(repr(k*lo));b=D(repr(k*hi))
            if a>b:a,b=b,a
            mn=min(mp.cos(a),mp.cos(b));mx=max(mp.cos(a),mp.cos(b))
            for j in range(int(mp.floor(a/mp.pi)),int(mp.ceil(b/mp.pi))+1):
                t=mp.pi*j
                if a<=t<=b and j%2!=0:mn=D(-1)
            for j in range(int(mp.floor(a/(2*mp.pi))),int(mp.ceil(b/(2*mp.pi)))+1):
                t=2*mp.pi*j
                if a<=t<=b:mx=D(1)
            return Iv(mn,mx)
        TCq=D(repr(TC));bad=0;mmin=None
        for b in chunk:
            best=None
            for k in range(1,K+1):
                c1=civ(k,b[2][0],b[2][1]);c2=civ(k,b[3][0],b[3][1]);c3=civ(k,b[4][0],b[4][1])
                r2i=Iv(D(repr(b[0][0]))**k,D(repr(b[0][1]))**k);r3i=Iv(D(repr(b[1][0]))**k,D(repr(b[1][1]))**k)
                s=c1+r2i*c2+r3i*c3
                if best is None or s.a>best:best=s.a
            if best>=TCq:
                m=float(best-TCq)
                if mmin is None or m<mmin:mmin=m
            else: bad+=1
        return (len(chunk),bad,mmin)
    nw=3
    chunks=[terms[i::nw] for i in range(nw)]
    with Pool(nw) as pool:
        res=pool.map(worker,chunks)
    tot=sum(r[0] for r in res);bad=sum(r[1] for r in res)
    mmin=min((r[2] for r in res if r[2] is not None),default=None)
    print(f"\n③ 区间复核：{tot:,} 箱  区间不过 = {bad}  {'✓' if bad==0 else '⚠️'}")
    print(f"   区间层最小余量 = {mmin:.6e}")
    ok = (bad==0 and nu==0 and disc_far<=DISC_R)
    print(f"\n{'⭐ D-C / C2 区间层 PASS ✓✓' if ok else '⚠️ 未达'}")
    json.dump(dict(TC=TC,ne=ne,n_term=tot,n_disc=nd,ns=ns,nu=nu,n_bad=bad,min_margin=mmin,
                   disc_far_max=disc_far,ok=ok),open('/tmp/dC2par.json','w'),indent=1)
