import numpy as np, os
N=10**8; CACHE='/tmp/g4_cache.npz'
M=2000; ug=np.linspace(np.log(1e3), np.log(float(N)), M)
if not os.path.exists(CACHE):
    print("sieve...",flush=True)
    s=np.ones(N+1,dtype=bool); s[:2]=False
    for i in range(2,int(N**0.5)+1):
        if s[i]: s[i*i::i]=False
    pr=np.nonzero(s)[0].astype(np.int64); del s
    chi=np.where(pr%4==1,1.0,-1.0); chi[pr==2]=0.0
    lp=np.log(pr.astype(np.float64))
    A=np.cumsum(chi/pr); B=np.cumsum(chi); C=np.cumsum(chi*lp)
    idx=np.clip(np.searchsorted(pr,np.exp(ug),side='right')-1,0,len(pr)-1)
    np.savez(CACHE,ug=ug,Ag=A[idx],Bg=B[idx],Cg=C[idx],Dinf=A[-1]); print("cached #primes",len(pr),flush=True)
d=np.load(CACHE); ug=d['ug']; Ag=d['Ag']; Bg=d['Bg']; Cg=d['Cg']; Dinf=float(d['Dinf'])
Rg=Dinf-Ag
print(f"D(N)={Dinf:+.6f}  D(X) 从 1e3 到 1e8 的变动 = {Ag[-1]-Ag[0]:+.6f}")

def env_exp(v,d_env=0.55,d_fit=1.10):
    av=np.abs(v); env=np.array([av[np.abs(ug-ug[i])<=d_env].max() for i in range(M)])
    le=np.full(M,np.nan)
    for i in range(M):
        m=np.abs(ug-ug[i])<=d_fit
        if m.sum()>10:
            le[i]=np.polyfit(ug[m],np.log(np.maximum(env[m],1e-300)),1)[0]
    return le
dec=[(3,4),(4,5),(5,6),(6,7)]
def med(le): return [np.nanmedian(le[(ug>=a*np.log(10))&(ug<=b*np.log(10))]) for a,b in dec]
print("\n== 真实通道 (包络窗 ±0.55 ≈1.05 周期, 拟合窗 ±1.10) ==")
out={}
for nm,sig,exp0 in [("A: R(X)",Rg,"beta-1"),("B: 素数竞赛",Bg,"beta"),("C: psi_chi",Cg,"beta")]:
    m=med(env_exp(sig)); out[nm]=m
    print(f"  {nm:<12} (期望 {exp0:>6}): " + "  ".join(f"1e{a}-1e{b}:{v:+.4f}" for (a,b),v in zip(dec,m)))
print("\n  [跨通道一致性]  A+1 vs B vs C :")
for k,(a,b) in enumerate(dec):
    print(f"    1e{a}-1e{b}: A+1={out['A: R(X)'][k]+1:+.4f}   B={out['B: 素数竞赛'][k]:+.4f}   C={out['C: psi_chi'][k]:+.4f}")

print("\n== 人工 beta 对照 (标度辨识能力) ==")
g=6.0209
print(f"  区间内振荡周期数 ≈ {g*(ug[-1]-ug[0])/(2*np.pi):.2f}")
for label,shift in [("A类比 X^{b-1}cos",-1.0),("B/C类比 X^{b}cos",0.0)]:
    print(f"  --- {label} (gamma={g}) ---")
    for beta in [0.50,0.55,0.60,0.65]:
        vv=[]
        for phi in np.linspace(0,2*np.pi,7,endpoint=False):
            sg=np.exp((beta+shift)*ug)*np.cos(g*ug+phi)
            vv.append(np.nanmedian(env_exp(sg)))
        vv=np.array(vv)
        print(f"    true beta={beta:.2f} -> est {vv.mean():+.4f} ± {vv.std():.4f}  (真值 {beta+shift:+.4f}, 偏差 {vv.mean()-(beta+shift):+.4f})")
print("\n== 多 zero 更忠实模型 (3 个振荡, A类比) ==")
gs=[6.0209,10.2436,14.1347]
for beta in [0.50,0.55,0.60]:
    vv=[]
    for phi in np.linspace(0,2*np.pi,5,endpoint=False):
        sg=sum(np.exp((beta-1)*ug)*np.cos(gi*ug+phi)/gi for gi in gs)
        vv.append(np.nanmedian(env_exp(sg)))
    print(f"    true beta={beta:.2f} -> est {np.mean(vv):+.4f} ± {np.std(vv):.4f}  (真值 {beta-1:+.4f})")
