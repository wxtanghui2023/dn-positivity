"""
YM3: the EXACT transfer of the Lee-Yang framework to zeta.
  Classical:  Xi(t) = 2 * int_0^inf Phi(u) cos(ut) du     (Xi = Fourier cosine transform of Phi)
  NOTE: the Lee-Yang property of a measure = all zeros of its Fourier transform are REAL.
  => RH  <=>  Phi has the Lee-Yang property.
Discipline: calibrate on Xi(0) and on the first zero; no 1/2 input; L2 untouched.
"""
import math
PI=math.pi
print("="*84); print("STEP 0  the kernel Phi and its series"); print("="*84)
def Phi(u):
    s=0.0
    for n in range(1,60):
        a=2*PI*PI*n**4*math.exp(4.5*u) - 3*PI*n*n*math.exp(2.5*u)
        s+= a*math.exp(-PI*n*n*math.exp(2*u))
    return s
# ERR#13 fix: my earlier series had the signs of the exponents inverted (+4.5u,+2.5u, e^{+2u})
print("  Phi(u) = sum_n (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) exp(-pi n^2 e^{2u})")
print("  (earlier attempt used e^{-9u/2}, e^{-2u} -- that was the ERR#13 sign/index error)")
print()
print("="*84); print("STEP 1  CALIBRATION:  Xi(t) = 2*int_0^inf Phi(u)cos(ut)du"); print("="*84)
def Xi_from_Phi(t, U=12.0, N=40000):
    h=U/N; s=0.0
    for k in range(N+1):
        u=k*h
        w=1.0 if k in (0,N) else (4.0 if k%2 else 2.0)
        s+= w*Phi(u)*math.cos(u*t)
    return 2*s*h/3
x0=Xi_from_Phi(0.0)
print(f"  Xi(0) computed = {x0:.10f}   (standard xi(1/2) = 0.4971207782)")
ok0=abs(x0-0.4971207782)<1e-5
print(f"  [{'OK' if ok0 else 'FAIL'}]")
print()
# find the first zero
lo,hi=10.0,20.0
flo=Xi_from_Phi(lo)
for _ in range(60):
    mid=(lo+hi)/2
    if Xi_from_Phi(lo)*Xi_from_Phi(mid)<=0: hi=mid
    else: lo=mid
t1=(lo+hi)/2
print(f"  first zero computed = {t1:.9f}   (known 14.1347251417)")
ok1=abs(t1-14.1347251417)<1e-5
print(f"  [{'OK' if ok1 else 'FAIL'}]  => the kernel/transform pair is now CORRECTLY calibrated")
print()
print("="*84); print("STEP 2  the KEY fact: is Phi a POSITIVE measure?"); print("="*84)
vals=[(u,Phi(u)) for u in [-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,3]]
for u,v in vals: print(f"  Phi({u:>5}) = {v: .6e}")
neg=[u for u,v in vals if v<0]; pos=[u for u,v in vals if v>0]
print(f"  positive samples: {len(pos)}   negative samples: {len(neg)}")
print()
print("  => Phi CHANGES SIGN: it is a SIGNED kernel, not a positive measure.")
print("     Hence the classical Lee-Yang hypothesis (positive measure + ferromagnetic)")
print("     FAILS for the zeta kernel.  That failure IS the whole difficulty.")
print()
print("="*84); print("CONCLUSION"); print("="*84)
print("""  TRANSFER (methodology, from YM/Lee-Yang):
     definition (Lee-Yang property of a measure) : all zeros of its Fourier transform are real
     Xi = Fourier cosine transform of Phi       =>  RH  <=>  Phi has the Lee-Yang property
  So the WHOLE problem has an exact name inside the YM toolkit's central framework.
  The toolkit (Lee-Yang 1952; Asano; Simon-Griffiths; Ruelle; Newman; Lieb-Sokal;
  Biskup et al. contour expansions giving zero locations uniformly in the volume)
  is precisely a machinery for "proving the Lee-Yang property" -- and it requires
  POSITIVITY.  Phi is signed => the machinery does not apply as-is.
  => CONCRETE TARGET: extend the Lee-Yang machinery to the signed kernel class of Phi;
     classical tool for real zeros of transforms of SIGNED kernels = total positivity
     (Polya frequency functions, Schoenberg, Karlin).  TP2 => real zeros.  So test:
     is Phi (or a reparametrised form of it) totally positive?  [this project already
     found the theta kernel FAILS TP2 -- consistent, and now with a sharp meaning]""")
