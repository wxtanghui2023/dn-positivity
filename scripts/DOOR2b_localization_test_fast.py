"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
import math, numpy as np
PI=math.pi
U=7.0; N=3000
uu=np.linspace(0,U,N+1); ww=np.ones(N+1); ww[1:-1:2]=4; ww[2:-1:2]=2; ww=ww*(U/N)/3
def Phi_arr(u):
    s=np.zeros_like(u)
    for n in range(1,20):
        a=2*PI*PI*n**4*np.exp(4.5*u) - 3*PI*n*n*np.exp(2.5*u)
        s+= a*np.exp(-PI*n*n*np.exp(2*u))
    return s
W=ww*Phi_arr(uu)                      # weights * kernel
def Xi_vec(t):                        # vectorised, chunked to bound memory
    t=np.atleast_1d(np.asarray(t,dtype=float)); out=np.empty_like(t)
    step=1200
    for i in range(0,len(t),step):
        blk=t[i:i+step]
        M=np.cos(np.outer(uu,blk))    # (N+1) x len(blk)
        out[i:i+step]=2.0*(W@M)
    return out
print("="*80); print("CALIBRATION"); print("="*80)
lo,hi=10.0,20.0
for _ in range(60):
    mid=(lo+hi)/2
    if float(Xi_vec(lo))*float(Xi_vec(mid))<=0: hi=mid
    else: lo=mid
t1=(lo+hi)/2
print(f"  first zero = {t1:.9f}  (known 14.1347251417)  [{'OK' if abs(t1-14.1347251417)<1e-4 else 'FAIL'}]")
print()
print("="*80); print("ZEROS up to ~150 by sign change (vectorised)"); print("="*80)
ts=np.linspace(1.0,150.0,60000); vs=Xi_vec(ts)
idx=np.where(vs[:-1]*vs[1:]<0)[0]
zeros=[]
for i in idx:
    a,b=ts[i],ts[i+1]
    for _ in range(45):
        m=(a+b)/2
        if float(Xi_vec(a))*float(Xi_vec(m))<=0: b=m
        else: a=m
    zeros.append((a+b)/2)
print(f"  found {len(zeros)} zeros; first 5 = {[round(z,4) for z in zeros[:5]]}; last = {zeros[-1]:.4f}")
print()
print("="*80); print("PARTIAL SUMS  S(T)=sum_{gamma<=T} 2Re[2^{i gamma}/(1/2+i gamma)]"); print("="*80)
x=math.log(2.0)
zarr=np.array(zeros); term=2*np.real(np.exp(1j*zarr*x)/ (0.5+1j*zarr))
print(f"  {'T':>7} | {'S(T)':>12} | {'|S(T)|':>10} | {'#zeros':>7} | {'chunk contrib':>14}")
prevS=0.0
for T in (20,30,40,50,60,70,80,90,100,120,150):
    m=zarr<=T; S=float(term[m].sum())
    print(f"  {T:>7.0f} | {S:>12.6f} | {abs(S):>10.6f} | {int(m.sum()):>7} | {S-prevS:>+14.6f}")
    prevS=S
print()
print("="*80); print("READ-OFF"); print("="*80)
print("""  * Are the chunk contributions shrinking with T (=> a decay-type localisation exists,
    so a conversion is possible once a RATE is known), or do they stay O(0.1-1) with no trend
    (=> no localisation at all => DOOR 2 HAS NO DOOR ?)""")
