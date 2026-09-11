"""LIGAP: Farmer's counterexample-gap standard applied to the Li coefficient criterion."""
import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, nstr
mp.dps=30
C=mpf('6.6'); T_ver=mpf('3.000175e12'); N_ver=T_ver**2/C
DS=['0.05','0.10','0.25','0.50']
hdr="d="+DS[0]
head="  %10s | " % "N" + " | ".join(["d=%-6s"%d for d in DS]) + "  (gamma_max, exclusion)"
print("="*96)
print("LIGAP: Li criterion under the counterexample-gap standard")
print("="*96)
print("  verified height T = %s   =>  N(T) = T^2/6.6 = %s" % (nstr(T_ver,10), nstr(N_ver,4)))
print()
print("  (a) EXCLUSION POWER:  lambda_n >= 0 for n <= N  ==>  no off-line zero below gamma_max(N,d)")
print(head)
for N in ['1e12','1e18','1e24',nstr(N_ver,6)]:
    Nv=mpf(N); row=[]
    for d in DS:
        gm=msqrt(2*mpf(d)*Nv/C); row.append("%8s"%nstr(gm,3))
    print("  %10s | " % N + " | ".join(row))
print()
print("  (b) COUNTEREXAMPLE GAP:  a failure at height g first shows up only at n*(g,d)")
print("  %10s | " % "g" + " | ".join(["d=%-6s"%d for d in DS]) + "  (n*)")
for g in ['14','100','1e3','1e6','1e9','1e12']:
    gv=mpf(g); row=[]
    for d in DS:
        n=C*gv**2/(2*mpf(d)); row.append("%8s"%nstr(n,3))
    print("  %10s | " % g + " | ".join(row))
print()
print("  (c) THE GAP TEST: how wide is the gap for a failure at SMALL height?")
g=mpf('14.0')
for d in DS:
    n_need=C*g**2/(2*mpf(d))
    print("      d=%s : failure at g=14 needs n* = %s ; verified N = %s ; gap ratio = %s"
          % (d, nstr(n_need,3), nstr(N_ver,3), nstr(N_ver/n_need,3)))
print()
print("="*96); print("READ-OFF"); print("="*96)
print("""  * gamma_max at the verified N of order the verified height T  =>  Li's exclusion power is
    NOT vacuous: positivity up to n ~ T^2/6.6 really excludes off-line zeros up to a height
    comparable with T.
  * the gap ratio in (c) says how much room a hypothetical early failure would have.""")
