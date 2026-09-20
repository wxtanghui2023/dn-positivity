#!/usr/bin/env python3
"""T13-A 甲：把 M=3 的最佳构型做区间算术上界认证（一个合法构型 = 上界证书）"""
import numpy as np, json
from scipy.optimize import minimize
import mpmath as mp
mp.iv.prec = 160
K=15; D=3
def F(x): return max(sum(np.cos(k*x[j]) for j in range(D)) for k in range(1,K+1))

x0=np.array([0.11584426,0.33188742,0.73557644])*np.pi
print("="*86); print("T13-A 甲：M=3 上界认证（区间算术，π 取区间）"); print("="*86)
print(f"起点（旧审计簇）: φ/π = {np.round(x0/np.pi,9)}   F = {F(x0):.12f}")

best=None
for s in range(40):
    rng=np.random.default_rng(1000+s)
    r=minimize(F, x0+rng.normal(scale=5e-7,size=3), method='Nelder-Mead',
               options={'xatol':1e-15,'fatol':1e-17,'maxiter':10000})
    if best is None or r.fun<best.fun: best=r
print(f"\n[1] 高精度精修: F = {best.fun:.15f}   φ/π = {np.round((best.x%np.pi)/np.pi,12)}")

# [2] 有理化到分母 D，并在格点上做局部搜索（±2）
for DEN in (10**8, 10**9, 10**10):
    base=[int(round(v/np.pi*DEN)) for v in (best.x%np.pi)]
    cur=(F(np.array([bb/DEN*np.pi for bb in base])), list(base))
    improved=True
    rounds=0
    while improved and rounds<12:
        improved=False; rounds+=1
        for j in range(D_:=3):
            for dlt in (-2,-1,1,2):
                cand=list(cur[1]); cand[j]+=dlt
                v=F(np.array([c/DEN*np.pi for c in cand]))
                if v<cur[0]-1e-16: cur=(v,cand); improved=True
    p=cur[1]
    print(f"\n[2] DEN={DEN}: 有理构型 p/DEN = {[pp/DEN for pp in p]}   浮点值 = {cur[0]:.15f}")
    # [3] 区间认证（上界）
    Pm=mp.mpf
    maxU=mp.mpf('-1e9'); kmax=None; details=[]
    for k in range(1,K+1):
        s=mp.iv.mpf(0)
        for pp in p:
            arg=(mp.iv.mpf(k*pp)/mp.iv.mpf(DEN))*mp.iv.pi
            s+=mp.iv.cos(arg)
        details.append((k,float(s.a),float(s.b)))
        if s.b>maxU: maxU=s.b; kmax=k
    width=max(d[2]-d[1] for d in details)
    print(f"[3] 区间认证: 逐 k 上界最大者 k={kmax}；max_k S_k 的上界 U = {mp.nstr(maxU,22)}")
    print(f"    区间宽度 ≲ {width:.3e}；最紧三项: "+", ".join(f"k={d[0]}:{d[2]:.12f}" for d in sorted(details,key=lambda t:-t[2])[:3]))
    U=mp.mpf(maxU)
    print(f"\n    ⟹ m_3 ≤ {mp.nstr(U,20)}")
    print(f"    对照旧上界 0.777171 ⟹ 收紧 {float(mp.mpf('0.777171')-U):.6e}")
    print(f"    新账本: 0.76 ≤ m_3 ≤ {mp.nstr(U,20)}   宽度 = {float(U)-0.76:.6e}")
json.dump(dict(DEN=DEN,p=p,U=str(U),kmax=kmax),open('/tmp/t13a_jia.json','w'),indent=2)
print("\n（已写 /tmp/t13a_jia.json）")
