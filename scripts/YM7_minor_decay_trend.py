"""
YM7: the trend of the smallest k x k minor as k grows.
  If the minima decay fast, the TP-infinity (all orders) condition is MARGINAL:
  the failure mode would live at higher orders / in the exact statement.
"""
import math, itertools, random
PI=math.pi
def Phi(u):
    s=0.0
    for n in range(1,16):
        a=2*PI*PI*n**4*math.exp(4.5*u) - 3*PI*n*n*math.exp(2.5*u)
        s+= a*math.exp(-PI*n*n*math.exp(2*u))
    return s
def det(M):
    n=len(M)
    if n==1: return M[0][0]
    if n==2: return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    A=[row[:]+[1.0 if i==j else 0.0 for j in range(n)] for i,row in enumerate(M)]
    d=1.0
    for c in range(n):
        p=max(range(c,n),key=lambda r:abs(A[r][c]))
        if abs(A[p][c])<1e-300: return 0.0
        if p!=c: A[c],A[p]=A[p],A[c]; d=-d
        d*=A[c][c]
        for r in range(c+1,n):
            f=A[r][c]/A[c][c]
            if f:
                for k in range(c,n+1): A[r][k]-=f*A[c][k]
    return d
def minors(pts,order):
    out=[]
    for idx in itertools.combinations(range(len(pts)),order):
        M=[[Phi(abs(pts[a]-pts[b])) for b in idx] for a in idx]
        out.append(det(M))
    return out
print("="*84); print("TREND: min k x k minor vs k   (uniform grid, h=0.1, 11 points)"); print("="*84)
pts=[k*0.1 for k in range(0,11)]
prev=None
for order in range(2,7):
    ms=minors(pts,order)
    mn=min(ms); mx=max(ms); neg=sum(1 for d in ms if d<-1e-14)
    ratio = (mn/prev) if prev else float('nan')
    print(f"  k={order}  #minors={len(ms):<5} min={mn: .4e}  max={mx: .4e}  violations={neg}  min_ratio={ratio:.4f}")
    prev=mn
print()
print("="*84); print("SAME on random non-uniform point sets (the true TP test)"); print("="*84)
random.seed(7)
for order in range(2,7):
    mn=1e300; neg=0; cnt=0
    for trial in range(25):
        n=order+random.choice([0,1,2])
        p=sorted(random.uniform(0,1.2) for _ in range(n))
        for d in minors(p,order):
            cnt+=1
            if d<mn: mn=d
            if d<-1e-14: neg+=1
    print(f"  k={order}  minors={cnt:<6} min={mn: .4e}  violations={neg}")
print()
print("="*84); print("INTERPRETATION"); print("="*84)
print("""  * If min_k decays geometrically, then TP-infinity is MARGINAL: no single order fails,
    but the margins shrink, so the exact/uniform statement is where the content lives.
  * This is the SAME shape as every other wall in this project: finite levels fine,
    the uniform/exact statement is the difficulty.""")
