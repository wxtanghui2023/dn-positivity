"""
DOOR2: does the Guinand / explicit-formula direction have an EXPLICIT quantitative pairing
       (numeric parameter <-> region controlled)?  Test: partial sums of the zero-side
       expression, truncated at T, for a fixed arithmetic point x = log 2.
  If |S(T)| stabilises => the tail dies => a "decay-type" localization exists (but with what RATE?).
  If it wanders at O(1) => no localization at all.
Calibration: first zero of Xi must come out at 14.134725.
"""
import math
import numpy as np
PI=math.pi
def Phi(u):
    s=0.0
    for n in range(1,20):
        a=2*PI*PI*n**4*math.exp(4.5*u) - 3*PI*n*n*math.exp(2.5*u)
        s+= a*math.exp(-PI*n*n*math.exp(2*u))
    return s
U=7.0; N=3000; h=U/N
uu=np.linspace(0,U,N+1); ww=np.ones(N+1); ww[1:-1:2]=4; ww[2:-1:2]=2; ww=ww*h/3
PHI=np.array([Phi(u) for u in uu])
def Xi(t): return 2*np.sum(ww*PHI*np.cos(uu*t))
print("="*80); print("CALIBRATION: first zero of Xi"); print("="*80)
lo,hi=10.0,20.0
for _ in range(60):
    mid=(lo+hi)/2
    if Xi(lo)*Xi(mid)<=0: hi=mid
    else: lo=mid
t1=(lo+hi)/2
print(f"  first zero = {t1:.9f}   (known 14.1347251417)  [{'OK' if abs(t1-14.1347251417)<1e-4 else 'FAIL'}]")
print()
print("="*80); print("ZEROS up to ~130 by sign change"); print("="*80)
ts=np.linspace(1.0,130.0,40000); vs=np.array([Xi(t) for t in ts])
zeros=[]
for i in range(len(ts)-1):
    if vs[i]*vs[i+1]<0:
        a,b=ts[i],ts[i+1]
        for _ in range(40):
            m=(a+b)/2
            if Xi(a)*Xi(m)<=0: b=m
            else: a=m
        zeros.append((a+b)/2)
print(f"  found {len(zeros)} zeros; first 5 = {[round(z,4) for z in zeros[:5]]}; last = {zeros[-1]:.4f}")
print()
print("="*80); print("PARTIAL SUMS of the zero-side term at x = log 2   S(T)=sum_{gamma<=T} 2Re[e^{i gamma x}/(1/2+i gamma)]"); print("="*80)
x=math.log(2.0)
print(f"  {'T':>7} | {'S(T)':>12} | {'|S(T)|':>10} | {'#zeros used':>11}")
for T in (20,30,40,50,60,80,100,110,zeros[-1]+1):
    S=0j; k=0
    for g in zeros:
        if g<=T:
            S+= 2*(np.exp(1j*g*x)/complex(0.5,g)).real; k+=1
    print(f"  {T:>7.0f} | {S.real:>12.6f} | {abs(S):>10.6f} | {k:>11}")
print()
print("="*80); print("TAIL SIZE: how much does the last chunk (T1,T2] change S ?"); print("="*80)
def S_upto(T):
    return sum(2*(np.exp(1j*g*x)/complex(0.5,g)).real for g in zeros if g<=T)
for T1,T2 in ((40,60),(60,80),(80,100),(100,zeros[-1]+1)):
    print(f"  chunk ({T1},{T2}] contributes {S_upto(T2)-S_upto(T1):+.6f}")
print()
print("="*80); print("READ-OFF"); print("="*80)
print("""  * If the chunks keep contributing O(0.1-1) all the way up with NO decreasing trend,
    then there is no usable localisation: the numeric value can never be attributed to a
    finite zero range, i.e. NO EXPLICIT PAIRING  => DOOR 2 HAS NO DOOR.
  * If the chunks shrink like a power of T, a decay-type pairing exists and one could
    convert 'zeros verified to T' into an arithmetic statement up to X(T).""")
