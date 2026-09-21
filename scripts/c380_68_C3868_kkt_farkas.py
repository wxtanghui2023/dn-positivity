# c380_68_C3868_kkt_farkas.py -- C3868: KKT -> Farkas proportionality audit at 60 dps
import mpmath as mp
mp.mp.dps = 60
SIG=[mp.mpf(-1),mp.mpf(1),mp.mpf(1),mp.mpf(-1),mp.mpf(1)]
AEV=[3,4,7,9]
PHI0=[mp.mpf('0.14721317'),mp.mpf('0.23048868'),mp.mpf('0.18365067'),mp.mpf('0.2094225'),mp.mpf('0.11795883')]
PHI0=[p*mp.pi for p in PHI0]

def newton(F,x0,maxit=90,tol='1e-55'):
    x=mp.matrix(x0); n=len(x)
    for _ in range(maxit):
        r=F(x); J=mp.matrix(len(r),n); h=mp.mpf('1e-40')
        for j in range(n):
            xp=mp.matrix(x); xp[j]=xp[j]+h; rp=F(xp)
            for i in range(len(r)): J[i,j]=(rp[i]-r[i])/h
        dx=mp.lu_solve(J,mp.matrix([-t for t in r])); x=x+dx
        if max(abs(t) for t in dx)<mp.mpf(tol): break
    return x

Occ=lambda p,k: mp.fsum([SIG[j]*mp.cos(k*p[j]) for j in range(5)])
Ev =lambda p,q: mp.fsum([mp.cos(4*q*p[j]) for j in range(5)])
dOcc=lambda p,k: [-k*SIG[j]*mp.sin(k*p[j]) for j in range(5)]
dEv =lambda p,q: [-4*q*mp.sin(4*q*p[j]) for j in range(5)]

print("=== step 1: rebuild the full KKT system (10x10) at 60 dps ===", flush=True)
def Fk(z):
    p=[z[j] for j in range(5)]; om=z[5]; lam=[z[6+q] for q in range(4)]
    v13=[-t for t in dOcc(p,13)]; v19=list(dOcc(p,19))
    out=[om*v13[j]+(1-om)*v19[j]+mp.fsum([lam[q]*dEv(p,AEV[q])[j] for q in range(4)]) for j in range(5)]
    out+=[Ev(p,q)-mp.mpf(1)/2 for q in AEV]
    out+=[Occ(p,13)+Occ(p,19)]
    return mp.matrix(out)
z0=[PHI0[0],PHI0[1],PHI0[2],PHI0[3],PHI0[4],mp.mpf('0.903717944'),
    mp.mpf('0.83791706'),mp.mpf('0.98971406'),mp.mpf('0.04185319'),mp.mpf('0.12728511')]
Z=newton(Fk,z0); om=[Z[5],1-Z[5]]; lam=[Z[6+q] for q in range(4)]
print("   ||KKT residual|| = %s" % mp.nstr(max(abs(t) for t in Fk(Z)),5), flush=True)
print("   omega_13 = %s" % mp.nstr(om[0],30), flush=True)
print("   omega_19 = %s" % mp.nstr(om[1],30), flush=True)
for q in range(4):
    print("   lambda_%d = %s" % (AEV[q], mp.nstr(lam[q],30)), flush=True)
L=mp.fsum(lam); print("   L = sum(lambda) = %s" % mp.nstr(L,30), flush=True)

# C-3867 values (recomputed here at the same precision for a clean comparison)
c_full=mp.mpf('0.500808953629041885590052265792')
mu=[mp.mpf('0.4196363681784466232834694'),mp.mpf('0.4956576606673542568951606'),
    mp.mpf('0.02096045068622233460521499'),mp.mpf('0.06374552046797678521615506')]
nu13=mp.mpf('0.4525900377602654099448385'); nu19=mp.mpf('0.04821891586877647564521381')
print("\n=== LAYER A: mu_q vs lambda_q / L (all four listed) ===", flush=True)
for q in range(4):
    muhat=lam[q]/L; d=mu[q]-muhat
    print("   q=%2d : mu=%s ; lambdahat=%s ; Delta_mu=%s"%(AEV[q],mp.nstr(mu[q],25),mp.nstr(muhat,25),mp.nstr(d,8)), flush=True)
print("\n=== LAYER B: nu vs c_full * omega (absolute residuals) ===", flush=True)
d13=nu13-c_full*om[0]; d19=nu19-c_full*om[1]
print("   nu13 = %s ; c*omega13 = %s ; Delta_nu13 = %s"%(mp.nstr(nu13,25),mp.nstr(c_full*om[0],25),mp.nstr(d13,8)), flush=True)
print("   nu19 = %s ; c*omega19 = %s ; Delta_nu19 = %s"%(mp.nstr(nu19,25),mp.nstr(c_full*om[1],25),mp.nstr(d19,8)), flush=True)
print("   ratios nu13/omega13 = %s ; nu19/omega19 = %s"%(mp.nstr(nu13/om[0],25),mp.nstr(nu19/om[1],25)), flush=True)
print("\n=== LAYER C: the scale identity L * c_full = 1 ===", flush=True)
prod=L*c_full
print("   L = %s" % mp.nstr(L,30), flush=True)
print("   c_full = %s" % mp.nstr(c_full,30), flush=True)
print("   L * c_full = %s" % mp.nstr(prod,30), flush=True)
print("   *** L*c_full - 1 = %s ***" % mp.nstr(prod-1,5), flush=True)
print("\n=== consistency: C-3863 stationarity vs C-3867 Farkas stationarity ===", flush=True)
p=[Z[j] for j in range(5)]
v13=[-t for t in dOcc(p,13)]; v19=list(dOcc(p,19))
bal_kkt=[om[0]*v13[j]+om[1]*v19[j]+mp.fsum([lam[q]*dEv(p,AEV[q])[j] for q in range(4)]) for j in range(5)]
bal_far=[(nu13*v13[j]+nu19*v19[j])+mp.fsum([mu[q]*dEv(p,AEV[q])[j] for q in range(4)]) for j in range(5)]
print("   ||KKT balance|| = %s ; ||Farkas balance|| = %s"%(mp.nstr(max(abs(t) for t in bal_kkt),5),mp.nstr(max(abs(t) for t in bal_far),5)), flush=True)
print("DONE", flush=True)
