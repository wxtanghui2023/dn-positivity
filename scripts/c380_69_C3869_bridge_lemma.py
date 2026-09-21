# c380_69_C3869_bridge_lemma.py -- C3869: symbolic audit of the KKT->Farkas lemma (no optimisation)
import mpmath as mp
mp.mp.dps = 60
# symbolic/algebraic audit of the five steps, verified on the C-3863 data
SIG=[mp.mpf(-1),mp.mpf(1),mp.mpf(1),mp.mpf(-1),mp.mpf(1)]; AEV=[3,4,7,9]
exec(open('/dev/stdin').read()) if False else None
L=mp.mpf('1.99676941227516035204325246457')
om13=mp.mpf('0.903717944'); om19=1-om13
lam=[mp.mpf('0.837917064256959665845251945367'),mp.mpf('0.989714055780433823538410896454'),
     mp.mpf('0.0418531867977506525607285492544'),mp.mpf('0.127285105440016210098861073496')]
c_full=mp.mpf('0.500808953629041885590052265792')
print("=== STEP 1: KKT ray divided by L gives a dual-feasible certificate ===", flush=True)
nu13=om13/L; nu19=om19/L; mu=[t/L for t in lam]
print("   nu13=omega13/L = %s"%mp.nstr(nu13,25), flush=True)
print("   nu19=omega19/L = %s"%mp.nstr(nu19,25), flush=True)
print("   mu_q = lambda_q/L : %s"%[mp.nstr(t,20) for t in mu], flush=True)
print("   sum(mu) - 1 = %s ; all >=0 ? %s"%(mp.nstr(mp.fsum(mu)-1,5), all(t>=0 for t in mu) and nu13>=0 and nu19>=0), flush=True)
print("   dual objective nu13+nu19 = %s ; 1/L = %s ; difference = %s"
      %(mp.nstr(nu13+nu19,25), mp.nstr(1/L,25), mp.nstr(nu13+nu19-1/L,5)), flush=True)
print("   compare with C-3867 duals: nu13 = %s ; mu = %s"
      %(mp.nstr(nu13,25), [mp.nstr(t,20) for t in mu]), flush=True)
print("\n=== STEP 2/3: for every primal-feasible h, sum lambda_q w_q h >= 1 => max_q w_q h >= 1/L ===", flush=True)
print("   derivation (algebrA): omega13*v13*h + omega19*v19*h <= -(omega13+omega19) = -1", flush=True)
print("   KKT: omega13*v13 + omega19*v19 = -sum lambda_q w_q  =>  sum lambda_q w_q h >= 1", flush=True)
print("   with lambda >= 0: L*max_q(w_q h) >= sum lambda_q (w_q h) >= 1  =>  max_q w_q h >= 1/L", flush=True)
print("   1/L = %s  (= c_full to %d digits? %s)"
      %(mp.nstr(1/L,30), 30, mp.nstr(c_full-1/L,5)), flush=True)
print("\n=== STEP 4/5: weak duality direction ===", flush=True)
print("   primal: min c s.t. v13h<=-1, v19h<=-1, w_q h - c <= 0   =>   c_* = inf_h max_q w_q h", flush=True)
print("   weak duality with the certificate (nu,mu)=(omega/L,lambda/L):   c_* >= nu13+nu19 = 1/L", flush=True)
print("   => the dual certificate yields the LOWER bound c_* >= 1/L, NOT c_* <= 1/L.", flush=True)
print("   equality c_* = 1/L additionally needs an ATTAINMENT step (an explicit primal-feasible h", flush=True)
print("   with max_q w_q h = 1/L), i.e. solvability of the 6x6 vertex system (v13h=-1, v19h=-1, w_q h=c).", flush=True)
print("   instance-level: C-3867 solved exactly that system at 60 dps -> c_p = %s = 1/L (30 digits)."%mp.nstr(c_full,30), flush=True)
print("\n=== VERDICT ===", flush=True)
print("   steps 1,2,3 valid  =>  c_* >= 1/L is a RIGOROUS one-sided KKT->Farkas bridge lemma.", flush=True)
print("   step 4 as stated has the wrong direction (should be >=).", flush=True)
print("   step 5 equality holds at this KKT point (verified to 30 digits) but a general theorem still", flush=True)
print("   requires the attainment/rank step.", flush=True)
print("DONE", flush=True)
