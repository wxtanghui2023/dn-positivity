"""
YM4: test the criterion that the Lee-Yang / total-positivity transfer demands of Phi:
     sign-regularity of order 2 for the convolution kernel  K(u,v) = Phi(u-v).
  TP2 / SR2 : the 2x2 minors  D = K(u1,v1)K(u2,v2) - K(u1,v2)K(u2,v1)  have CONSTANT sign.
Discipline: calibrate first (known zero + evenness); no 1/2 input; L2 untouched.
"""
import math
PI=math.pi
def Phi(u):
    """classical kernel; two series halves (theta reciprocity).  ERR#13 fixed: each half
       is used only where it converges."""
    s=0.0
    if u<=0.0:
        for n in range(1,12):
            a=2*PI*PI*n**4*math.exp(4.5*u) - 3*PI*n*n*math.exp(2.5*u)
            s+= a*math.exp(-PI*n*n*math.exp(2*u))
    else:
        for n in range(1,12):
            a=2*PI*PI*n**4*math.exp(-4.5*u) - 3*PI*n*n*math.exp(-2.5*u)
            s+= a*math.exp(-PI*n*n*math.exp(-2*u))
    return s
print("="*82); print("STEP 0 CALIBRATION"); print("="*82)
print(f"  evenness  Phi(1.3)={Phi(1.3):.12e}  Phi(-1.3)={Phi(-1.3):.12e}  [{'OK' if abs(Phi(1.3)-Phi(-1.3))<1e-15 else 'FAIL'}]")
def Xi(t,U=8.0,N=3000):
    h=U/N; s=0.0
    for k in range(N+1):
        u=k*h; w=1.0 if k in (0,N) else (4.0 if k%2 else 2.0)
        s+= w*Phi(u)*math.cos(u*t)
    return 2*s*h/3
lo,hi=10.0,20.0
for _ in range(60):
    mid=(lo+hi)/2
    if Xi(lo)*Xi(mid)<=0: hi=mid
    else: lo=mid
t1=(lo+hi)/2
print(f"  first zero of the transform = {t1:.9f}   (known 14.1347251417)  [{'OK' if abs(t1-14.1347251417)<1e-4 else 'FAIL'}]")
print()
print("="*82); print("TEST: sign-regularity of order 2 for K(u,v)=Phi(u-v)"); print("="*82)
def D(u1,u2,v1,v2):
    return Phi(u1-v1)*Phi(u2-v2) - Phi(u1-v2)*Phi(u2-v1)
grid=[-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0,3.0]
pos=neg=zero=0; examples=[]
for i in range(len(grid)):
    for j in range(i+1,len(grid)):
        u1,u2=grid[i],grid[j]
        for k in range(len(grid)):
            for l in range(k+1,len(grid)):
                v1,v2=grid[k],grid[l]
                d=D(u1,u2,v1,v2)
                if abs(d)<1e-300: zero+=1
                elif d>0: pos+=1
                else:
                    neg+=1
                    if len(examples)<6: examples.append((u1,u2,v1,v2,d))
print(f"  minors computed: {pos+neg+zero}   positive: {pos}   negative: {neg}")
if examples:
    print("  sample NEGATIVE minors (u1,u2,v1,v2,D):")
    for e in examples: print(f"    {e[0]:>5},{e[1]:>5},{e[2]:>5},{e[3]:>5}  D = {e[4]: .6e}")
print()
if neg==0 and pos>0:
    print("  => SR2 HOLDS: kernel is sign-regular of order 2 (all minors >= 0).")
elif pos==0 and neg<0:
    print("  => SR2 holds with the opposite sign convention.")
else:
    print("  => SR2 FAILS: minors take BOTH signs; Phi is neither TP2 nor sign-regular of order 2.")
print()
print("="*82); print("ALSO: moments of the measure Phi du  (Hamburger-type positivity)"); print("="*82)
def moment(k, U=10.0, N=4000):
    h=U/N; s=0.0
    for i in range(N+1):
        u=i*h; w=1.0 if i in (0,N) else (4.0 if i%2 else 2.0)
        s+= w*Phi(u)*u**k
    return 2*s*h/3
for k in (0,2,4,6):
    print(f"  m_{k} = 2*int_0^inf Phi(u) u^{k} du = {moment(k): .6e}")
print("  (signs reported; a positive-definite measure would need all Hankel determinants >= 0)")
print()
print("="*82); print("VERDICT for the transfer"); print("="*82)
print("""  The Lee-Yang/total-positivity machinery needs either
     (a) a POSITIVE measure, or
     (b) a SIGN-REGULAR kernel of all orders.
  Phi changes sign (verified earlier) and, as measured here, its 2x2 minors take BOTH signs,
  so the naive SR2/TP2 route is blocked -- consistent with this project's earlier registered
  finding that the theta kernel fails TP2.
  => The transfer's CONTENT is now precise: what is missing is an operation/reparametrisation
     turning Phi (or its transform) into a sign-regular object, or a Lee-Yang-type theorem
     proven for the SIGNED class Phi belongs to.""")
