## CAP-MIX-1B · B2: 伪 survivor 分类（orbit / order / subfield / y=x^{2^k}）
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    A={"case":0,"Vstar_tot":0,"P_tot":0,"z_zero":0,"orbit_full":0,"orbit_partial":0,
       "y_in_orbit_of_x":0,"deg_hist":{},"ordz_div_d":0,"ordz_subfield":0,"ordz_general":0,
       "kx_lt_n":0,"kx_eq_n":0,"Pmax":0}
    orblens={}
    out=open("out/capmix1B2_pseudo.txt","w")
    for n in range(2,13):
        q=2**n
        if q>4096: continue
        _,tomul=mk(2,n)
        els=[tuple((i//(2**k))%2 for k in range(n)) for i in range(q)]
        enc={e:i for i,e in enumerate(els)}
        one=enc[(1,)+(0,)*(n-1)];zero=enc[tuple([0]*n)]
        addi=lambda a,b: enc[tuple((x+y)%2 for x,y in zip(els[a],els[b]))]
        muli=lambda a,b: enc[tomul(els[a],els[b])]
        def powi(a,e):
            r=one;b=a
            while e:
                if e&1:r=muli(r,b)
                b=muli(b,b);e>>=1
            return r
        M=q-1;prs=[];t=2
        while t*t<=M:
            if M%t==0:
                prs.append(t)
                while M%t==0: M//=t
            t+=1
        if M>1: prs.append(M)
        gen=None
        for e in range(1,q):
            if all(powi(e,(q-1)//pr)!=one for pr in prs): gen=e;break
        def order_of(a):
            if a==zero: return 0
            o=q-1
            for pr in prs:
                while o%pr==0 and powi(a,o//pr)==one: o//=pr
            return o
        def frobdeg(a):   # 最小 k>=1 使 a^{2^k}=a （即 a 属于 F_{2^k}）
            for k in range(1,n+1):
                if powi(a,2**k)==a: return k
            return None
        def orbit_of(a):
            o=[];z=a
            for _ in range(n):
                if z in o: break
                o.append(z);z=muli(z,z)
            return o
        for d in divs(q-1):
            if d<3 or d>100: continue
            A["case"]+=1
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            Jin=sorted({pow(2,j,d) for j in range(1,(ordm(2,d) or d)+1) if pow(2,j,d)!=0 and not ispp(pow(2,j,d),2)})
            pairs=[(a,b) for a in G for b in G if a!=b and a!=one and b!=one]
            valid=set()
            for (a,b) in pairs:
                if addi(addi(one,a),b) in Sset: valid.add((a,b))
            V=set(pairs)
            for r in Jin:
                if not V: break
                bad=set()
                for (a,b) in V:
                    z=addi(addi(one,a),b)
                    if addi(addi(addi(powi(a,r),powi(b,r)),powi(z,r)),one)!=zero: bad.add((a,b))
                V-=bad
            P=V-valid
            A["Vstar_tot"]+=len(V); A["P_tot"]+=len(P)
            A["Pmax"]=max(A["Pmax"],len(P))
            # 检验 P 是否为完整 Frobenius 轨道之并
            Pf=set()
            for (a,b) in P:
                z=a
                for _ in range(n): Pf.add((z,b)); z=muli(z,z)
                z=b
                # 只对 x,y 同时做轨道会生成 (a,b) 整体轨道，这里用二维轨迹
            # 二维轨迹（同时迭代）
            seen=set();full=True
            for (a,b) in P:
                if (a,b) in seen: continue
                orb=[];pa,pb=a,b
                for _ in range(n+1):
                    if (pa,pb) in orb: break
                    orb.append((pa,pb));pa=muli(pa,pa);pb=muli(pb,pb)
                seen.update(orb)
                if not all(o in P for o in orb): full=False
                orblens[len(orb)]=orblens.get(len(orb),0)+1
            if P:
                if full: A["orbit_full"]+=1
                else: A["orbit_partial"]+=1
            for (a,b) in P:
                z=addi(addi(one,a),b)
                if z==zero: A["z_zero"]+=1
                else:
                    oz=order_of(z)
                    if oz and d%oz==0: A["ordz_div_d"]+=1
                    elif oz and any(oz%(2**k-1)==0 for k in range(1,n) if 2**k-1>0): A["ordz_subfield"]+=1
                    else: A["ordz_general"]+=1
                kx=frobdeg(a);ky=frobdeg(b)
                k=1
                while powi(a,2**k)!=a or powi(b,2**k)!=b: k+=1
                A["deg_hist"][k]=A["deg_hist"].get(k,0)+1
                if k<n: A["kx_lt_n"]+=1
                else: A["kx_eq_n"]+=1
                if b in orbit_of(a): A["y_in_orbit_of_x"]+=1
            out.write("n=%2d q=%5d d=%4d |pairs|=%5d |valid|=%5d |V*|=%5d |P|=%2d Jin=%s\n"%(
                n,q,d,len(pairs),len(valid),len(V),len(P),str(Jin[:5])))
    print("STATS:",A)
    print("轨道长度直方图:",orblens)
    out.write("STATS: "+str(A)+"\nORBLEN: "+str(orblens)+"\n");out.close()
main()
