import math
PI=math.pi
def PhiA(v):
    s=0.0
    for n in range(1,14):
        a=2*PI*PI*n**4*math.exp(4.5*v) - 3*PI*n*n*math.exp(2.5*v)
        s+= a*math.exp(-PI*n*n*math.exp(2*v))
    return s
def Phi(u):
    """ERR#14 fix: Phi is EVEN; evaluate the (convergent) form at -|u|."""
    return PhiA(-abs(u))
print("="*80); print("STEP 0 CALIBRATION after the evenness fix"); print("="*80)
print(f"  Phi(0)   = {Phi(0):.10e}     (earlier 4.466969e-01)")
print(f"  Phi(0.5) = {Phi(0.5):.10e}  Phi(-0.5) = {Phi(-0.5):.10e}")
print(f"  Phi(3)   = {Phi(3):.10e}  Phi(-3)   = {Phi(-3):.10e}   (evenness now exact)")
def Xi(t,U=7.0,N=2800):
    h=U/N; s=0.0
    for k in range(N+1):
        u=k*h; w=1.0 if k in (0,N) else (4.0 if k%2 else 2.0)
        s+= w*Phi(u)*math.cos(u*t)
    return 2*s*h/3
print(f"  Xi(0) = {Xi(0):.10f}   (standard 0.4971207782)")
lo,hi=10.0,20.0
for _ in range(60):
    mid=(lo+hi)/2
    if Xi(lo)*Xi(mid)<=0: hi=mid
    else: lo=mid
t1=(lo+hi)/2
print(f"  first zero = {t1:.9f}   (known 14.1347251417)  [{'OK' if abs(t1-14.1347251417)<1e-4 else 'FAIL'}]")
print()
print("="*80); print("TEST 1: sign-regularity of order 2 (with the CORRECTED kernel)"); print("="*80)
def D(u1,u2,v1,v2): return Phi(u1-v1)*Phi(u2-v2)-Phi(u1-v2)*Phi(u2-v1)
grid=[-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5]
pos=neg=0; ex=[]
for i in range(len(grid)):
    for j in range(i+1,len(grid)):
        for k in range(len(grid)):
            for l in range(k+1,len(grid)):
                d=D(grid[i],grid[j],grid[k],grid[l])
                if d>0: pos+=1
                elif d<0:
                    neg+=1
                    if len(ex)<4: ex.append((grid[i],grid[j],grid[k],grid[l],d))
print(f"  minors: {pos+neg}   positive: {pos}   negative: {neg}")
for e in ex: print(f"    negative example: u=({e[0]},{e[1]}) v=({e[2]},{e[3]})  D={e[4]: .6e}")
print(f"  => SR2 {'HOLDS' if neg==0 else 'FAILS'}")
print()
print("="*80); print("TEST 2: moments  2*int_0^inf Phi(u) u^k du"); print("="*80)
def mom(k,U=9.0,N=3600):
    h=U/N; s=0.0
    for i in range(N+1):
        u=i*h; w=1.0 if i in (0,N) else (4.0 if i%2 else 2.0)
        s+= w*Phi(u)*(u**k)
    return 2*s*h/3
for k in (0,2,4,6,8):
    print(f"  m_{k} = {mom(k): .6e}")
print("  (compare m_0 with 2*Xi(0) = above)")
print()
print("="*80); print("VERDICT (now on the corrected kernel)"); print("="*80)
print("""  Deterministic facts to read off:
    * is the kernel sign-regular of order 2?   -> see TEST 1
    * do the moments (Hamburger data) have a definite sign? -> see TEST 2
  A 'yes' to constant signs would open the classical Lee-Yang/total-positivity route;
  a 'no' pins the obstruction to the SIGN STRUCTURE of Phi, which is exactly the point
  where the gauge-side positivity hypothesis fails.""")
