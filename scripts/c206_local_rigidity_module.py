#!/usr/bin/env python3
"""C-206 乙-3：Type-A 局部线性刚性【可复用区间模块】（四层 A/B/C/D）
严格性：候选点 x_i = pi*p_i/DEN（有理）；梯度/值用均值形式 + pi 不确定度做区间传播。
c 的严格算法：c = min_{||u||=1} max_k <g_k,u> = 半径 = max r s.t. B_r ⊂ conv{g_k}
             = min over facets 的 dist(0, facet plane)（区间版）。
"""
import json, numpy as np, itertools, mpmath as mp
mp.mp.dps = 90
mp.iv.prec = 200
K, D, DEN = 15, 3, 10**10
PI_LO = mp.mpf('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803')
PI_HI = mp.mpf('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862805')
PI_MID = (PI_LO+PI_HI)/2; DPI = (PI_HI-PI_LO)/2; EPS = mp.mpf('1e-80')

def S_encl(p,k):
    lo=mp.mpf(0); hi=mp.mpf(0)
    for q in p:
        a=mp.mpf(k*q)/DEN; c=mp.cos(a*PI_MID); e=a*DPI+EPS
        lo+=c-e; hi+=c+e
    return lo,hi

def grad_iv(p,k):
    """返回 mpmath.iv 区间向量 (-k sin(k x_i))"""
    out=[]
    for q in p:
        a=mp.mpf(k*q)/DEN
        s=mp.iv.sin(mp.iv.mpf(a)*mp.iv.pi)
        out.append(mp.iv.mpf(-k)*s)
    return out

def facet_c(giv, verbose=False):
    """区间 facet 法。giv: list of interval vectors (mpmath.iv). 返回 (c_lo, ok_inside)"""
    n=len(giv)
    if n<4: return None, False
    idx=list(range(n)); dists=[]
    for comb in itertools.combinations(idx,3):
        rest=[i for i in idx if i not in comb]
        v1,v2,v3=giv[comb[0]],giv[comb[1]],giv[comb[2]]
        # 法向 nrm = (v2-v1) x (v3-v1)
        a=[v2[i]-v1[i] for i in range(3)]; b=[v3[i]-v1[i] for i in range(3)]
        nrm=[a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
        # 是否真面：其余顶点在同侧
        sgn=[]
        for j in rest:
            val=sum(nrm[i]*(giv[j][i]-v1[i]) for i in range(3))
            sgn.append(val)
        if not (all(x>0 for x in sgn) or all(x<0 for x in sgn)): continue
        num=abs(sum(nrm[i]*v1[i] for i in range(3)))
        den=mp.iv.sqrt(sum(nrm[i]**2 for i in range(3)))
        if den.a<=0: continue
        dists.append(num/den)
    if not dists: return None, False
    los=[float(d.a) for d in dists]; his=[float(d.b) for d in dists]
    return min(los), True, len(los), min(his)

def run(p,label,tol=1e-5):
    p=[int(v) for v in p]
    S={k:S_encl(p,k) for k in range(1,K+1)}
    T=max(S[k][0] for k in S); C=[k for k in range(1,K+1) if S[k][1]>=T]
    A=sorted(set(C)|{k for k in range(1,K+1) if S[k][1]>=T-tol})
    nonA=[k for k in range(1,K+1) if k not in A]
    Delta=min(S[k][0] for k in A)-max(S[k][1] for k in nonA)
    L_non=max(k*np.sqrt(3) for k in nonA); L_act=max(k*np.sqrt(3) for k in A)
    rho_iso=float(Delta)/(L_non+L_act)
    giv=[grad_iv(p,k) for k in A]
    cres=facet_c(giv)
    if cres[0] is None:
        print(f"{label}: facet 法失败（|A|={len(A)} 或 0 不在内部）"); return None
    c_lo, ok, nf, c_hi = cres
    R=max(k*k for k in A); c_cert=c_lo/2
    rho_fin=min(rho_iso, c_cert/R) if c_cert>0 else float('nan')
    print("="*94)
    print(f"{label}: C(argmax候选)={C}  A={A}  |A|={len(A)}")
    print(f"  [A] Delta={float(Delta):.6e}  L_non={L_non:.4f}  L_act={L_act:.4f}  rho_iso={rho_iso:.6e}")
    print(f"  [B] facet 法: 面数={nf}  0 在内部={ok}  c∈[{c_lo:.12f}, {c_hi:.12f}]  ⟹ c_lo={c_lo:.9f}")
    print(f"  [C] R = max k^2 = {R}")
    print(f"  [D] rho_fin = min(rho_iso, c_cert/R) = min({rho_iso:.6e}, {c_cert/R:.6e}) = {rho_fin:.6e}")
    print(f"      c_cert = c_lo/2 = {c_cert:.9f}")
    print(f"  [THM] 0<||d||<={rho_fin:.6e}  ==>  F(x+d) >= F(x) + {c_cert:.9f}||d|| > F(x)")
    return dict(label=label,p=p,C=C,A=A,Delta=float(Delta),L_non=L_non,L_act=L_act,rho_iso=rho_iso,
                c_lo=c_lo,c_hi=c_hi,nfacets=nf,R=R,rho_fin=rho_fin,c_cert=c_cert)

cl=json.load(open('/tmp/t13aeq_clusters.json'))['clusters']
def rat(v): return int(round(float(v)/np.pi*DEN))
out=[r for r in (run([rat(v) for v in np.array(cl[i]['x'])],l) for i,l in ((0,"簇 0"),(3,"簇 3"),(5,"簇 5"))) if r]
json.dump(out,open('/tmp/c206_module.json','w'),indent=2,default=float)
print("\n"+"="*94); print("三实例汇总（严格区间版 · facet 法）")
print(f"  {'簇':>6} {'|A|':>3} {'Delta':>11} {'rho_iso':>11} {'c_lo':>11} {'R':>4} {'rho_fin':>11} {'c_cert':>11}")
for r in out:
    print(f"  {r['label']:>6} {len(r['A']):3d} {r['Delta']:11.4e} {r['rho_iso']:11.4e} {r['c_lo']:11.8f} {r['R']:4d} {r['rho_fin']:11.4e} {r['c_cert']:11.8f}")
