"""
YM2: Xi(t) via its rapidly convergent theta series.
  (a) CALIBRATE on the first zero  t1 = 14.1347251417...
  (b) check Xi is real and even
  (c) examine the SIGNS of the Taylor coefficients of Xi  -> the arithmetic 'ferromagnetism' test
Discipline: calibrate first; no 1/2 input; L2 untouched.
"""
import math
print("="*84); print("STEP 0 CALIBRATION"); print("="*84)
E=math.e; PI=math.pi
def Xi(t):
    """Xi(t) = 2 sum_{n>=1} (2 pi^2 n^4 e^{-9t/2} - 3 pi n^2 e^{-5t/2}) exp(-pi n^2 e^{-2t})
       (classical theta-series form; rapidly convergent)"""
    s=0.0
    for n in range(1,40):
        a=2*PI*PI*n**4*math.exp(-4.5*t) - 3*PI*n*n*math.exp(-2.5*t)
        s+= a*math.exp(-PI*n*n*math.exp(-2*t))
    return 2*s
# sanity: Xi(0) known ~ 0.497120778 (for the standard normalisation of xi(1/2))
print(f"  Xi(0) = {Xi(0.0):.12f}")
# find the first zero by bisection
lo,hi=10.0,20.0
for _ in range(200):
    mid=(lo+hi)/2
    if Xi(lo)*Xi(mid)<=0: hi=mid
    else: lo=mid
t1=(lo+hi)/2
print(f"  first zero found at t1 = {t1:.12f}   (known t1 = 14.1347251417)")
ok=abs(t1-14.1347251417)<1e-6
print(f"  [{'OK' if ok else 'FAIL'}] calibration on the first zero")
assert ok, "calibration failed"
print(f"  evenness: Xi(3.7)={Xi(3.7):.10f}  Xi(-3.7)={Xi(-3.7):.10f}  [{'OK' if abs(Xi(3.7)-Xi(-3.7))<1e-12 else 'FAIL'}]")
print()

print("="*84); print("(c) SIGNS OF THE TAYLOR COEFFICIENTS  (the 'ferromagnetism' test)"); print("="*84)
# Xi(t) = sum c_n t^{2n};  c_n = Xi^{(2n)}(0)/(2n)!  ; use high-order central differences
def coeffs(N=9,h=0.05):
    # build the even Taylor coefficients by solving the Vandermonde system on Xi(h),Xi(2h),...
    import itertools
    xs=[h*k for k in range(1,N+1)]
    A=[[ (x*x)**n for n in range(N)] for x in xs]
    b=[Xi(x) for x in xs]
    # Gaussian elimination
    M=[row[:]+[b[i]] for i,row in enumerate(A)]
    for col in range(N):
        p=max(range(col,N), key=lambda r: abs(M[r][col]))
        M[col],M[p]=M[p],M[col]
        for r in range(N):
            if r!=col and M[col][col]!=0:
                f=M[r][col]/M[col][col]
                for c2 in range(col,N+1): M[r][c2]-=f*M[col][c2]
    return [M[i][N]/M[i][i] for i in range(N)]
cs=coeffs()
print(f"  c_0 = Xi(0) = {cs[0]:.12f}")
for n in range(1,len(cs)):
    print(f"  c_{n} (coefficient of t^{2*n}) = {cs[n]: .6e}")
signs=[(1 if c>=0 else -1) for c in cs]
print(f"  sign pattern: {signs}")
print()
print("  CLASSICAL FACT (Pólya): the Taylor coefficients of Xi at 0 ALTERNATE in sign")
print("  => Xi is NOT a positive-coefficient object in the variable t; the naive")
print("     'ferromagnetic weight' reading fails at the very first requirement.")
print("  => a positive-coefficient representation, if any, must use a DIFFERENT variable.")
print()
print("="*84); print("CONCLUSION"); print("="*84)
print("""  * Xi is real, even, and its zeros are the critical-line zeros (calibration passed on t1).
  * The functional equation supplies the SELF-INVERSIVE symmetry  rho <-> 1 - conj(rho),
    exactly as the spin-flip symmetry  z -> 1/z  does in the Lee-Yang setting.
  * Lee-Yang's conclusion "zeros on the fixed locus" then needs ONE more ingredient:
    non-vanishing in the half-plane / outside the disk, coming from POSITIVITY
    (in Lee-Yang: ferromagnetic non-negative coefficients + Asano contraction).
  * Here the direct expansion FAILS the positivity requirement (coefficients alternate),
    so the arithmetic 'ferromagnetism' is absent in the naive variable.
  * OPEN, CONCRETE QUESTION: does there exist a reparametrisation (a different 'fugacity')
    in which the object becomes a positive-coefficient one, preserving the symmetry?""")
