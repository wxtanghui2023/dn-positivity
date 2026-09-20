#!/usr/bin/env python3
"""C-221 甲-A：区间局部刚性工具（Step 3）—— 精确可分区间求值（非粗糙 Lipschitz 界）
相切条件（delta_A=0）不在本档，属 B。
"""
import mpmath as mp, json
mp.mp.dps = 120
K=15; A=[1,5,11,13]; R=max(k*k for k in A)
PIV=mp.pi; TWOPI=2*PIV
d=json.load(open('/tmp/c212_cert.json')); q=int(d['q']); p=[int(t) for t in d['p']]
xc=[mp.mpf(pj)/mp.mpf(q)*PIV for pj in p]   # φ_j（弧度，含 π 因子！）

def cos_minmax(k,c,H):
    a=k*(c-H); b=k*(c+H)          # c,H 均为 φ（弧度）
    mn=min(mp.cos(a),mp.cos(b)); mx=max(mp.cos(a),mp.cos(b))
    j0=int(mp.floor(a/PIV)); j1=int(mp.ceil(b/PIV))
    for j in range(j0,j1+1):
        t=PIV*j
        if a<=t<=b and j%2!=0: mn=mp.mpf(-1)
    j0=int(mp.floor(a/TWOPI)); j1=int(mp.ceil(b/TWOPI))
    for j in range(j0,j1+1):
        t=TWOPI*j
        if a<=t<=b: mx=mp.mpf(1)
    return mn,mx
def sin_minmax(k,c,H):
    a=k*(c-H); b=k*(c+H); mn=min(mp.sin(a),mp.sin(b)); mx=max(mp.sin(a),mp.sin(b))
    HPIV=PIV/2
    j0=int(mp.floor((a-HPIV)/TWOPI)); j1=int(mp.ceil((b-HPIV)/TWOPI))
    for j in range(j0,j1+1):
        t=TWOPI*j+HPIV
        if a<=t<=b: mx=mp.mpf(1)
    j0=int(mp.floor((a-3*HPIV)/TWOPI)); j1=int(mp.ceil((b-3*HPIV)/TWOPI))
    for j in range(j0,j1+1):
        t=TWOPI*j+3*HPIV
        if a<=t<=b: mn=mp.mpf(-1)
    return mn,mx

def data(H):
    Smin={}; Smax={}
    for k in range(1,K+1):
        lo=mp.mpf(0); hi=mp.mpf(0)
        for c in xc:
            mn,mx=cos_minmax(k,c,H); lo+=mn; hi+=mx
        Smin[k]=lo; Smax[k]=hi
    nonA=[k for k in range(1,K+1) if k not in A]
    Delta=min(Smin[k] for k in A)-max(Smax[k] for k in nonA)
    Gm=[]; hw=[]
    for k in A:
        g=[]; h=[]
        for c in xc:
            mn,mx=sin_minmax(k,c,H)
            g.append(-mp.mpf(k)*(mn+mx)/2)      # 分量中点
            h.append(mp.mpf(k)*(mx-mn)/2)       # 分量半宽
        Gm.append(g); hw.append(mp.sqrt(sum(t*t for t in h)))
    eps=max(hw)
    dists=[]; inside=True
    for i in range(4):
        tri=[j for j in range(4) if j!=i]; apex=i
        v1,v2,v3=Gm[tri[0]],Gm[tri[1]],Gm[tri[2]]
        n=[(v2[1]-v1[1])*(v3[2]-v1[2])-(v2[2]-v1[2])*(v3[1]-v1[1]),
           (v2[2]-v1[2])*(v3[0]-v1[0])-(v2[0]-v1[0])*(v3[2]-v1[2]),
           (v2[0]-v1[0])*(v3[1]-v1[1])-(v2[1]-v1[1])*(v3[0]-v1[0])]
        nn=mp.sqrt(sum(t*t for t in n))
        if nn==0: continue
        s0=sum(n[t]*(-v1[t]) for t in range(3)); sa=sum(n[t]*(Gm[apex][t]-v1[t]) for t in range(3))
        if s0*sa<=0: inside=False
        dists.append(abs(s0)/nn)
    return Delta,(min(dists) if dists else mp.mpf(0)),eps,inside

L_non=max(mp.mpf(k)*mp.sqrt(3) for k in range(1,K+1) if k not in A)
L_act=max(mp.mpf(k)*mp.sqrt(3) for k in A)
print("="*108); print("C-221 甲-A：区间局部刚性工具（精确可分区间求值）"); print("="*108)
print(f"A={A}  R={R}  L_non={float(L_non):.4f}  L_act={float(L_act):.4f}")
print(f"\n  {'H':>9} {'Delta':>13} {'c_mid':>13} {'eps':>11} {'c_X':>15} {'0在内':>6} {'rho_iso':>10} {'rho_up':>10} {'H>=rho_up':>10}")
rows=[]
for H in (5e-3,4e-3,3e-3,2.2e-3,2e-3,1.5e-3,1e-3,1e-6):
    Delta,c_mid,eps,inside=data(H); rho_iso=Delta/(L_non+L_act); cX=c_mid-eps
    rho_up=min(rho_iso,cX/R) if cX>0 else mp.mpf(0)
    ok=H>=rho_up
    print(f"  {H:9.1e} {float(Delta):13.6f} {float(c_mid):13.9f} {float(eps):11.2e} {float(cX):15.9f} {str(inside):>6} {float(rho_iso):10.3e} {float(rho_up):10.3e} {str(ok):>10}")
    rows.append(dict(H=H,Delta=float(Delta),c_mid=float(c_mid),eps=float(eps),cX=float(cX),inside=bool(inside),rho_iso=float(rho_iso),rho_up=float(rho_up),selfcons=bool(ok)))
json.dump(rows,open('/tmp/c221_A.json','w'),indent=2)
good=[r for r in rows if r['selfcons'] and r['cX']>0 and r['Delta']>0]
if good:
    r=max(good,key=lambda t:t['rho_up'])
    print(f"\n★ 最佳【自洽】档：H={r['H']:.1e} ⟹ rho_up={r['rho_up']:.4e}, c_X={r['cX']:.9f}, Delta={r['Delta']:.6f}")
    print(f"   A 的结论（不含相切）：F(x+δ) ≥ min_(k∈A)S_k(x) + {r['cX']:.9f}‖δ‖ − (169/2)‖δ‖²，  ‖δ‖ ≤ {r['rho_up']:.3e}")
else:
    print("\n⚠️ 无自洽档 ⟹ 需更精细的 c/隔离处理")
