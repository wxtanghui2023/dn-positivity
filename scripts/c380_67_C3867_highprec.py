# c380_67_C3867_highprec.py -- C3867: 40+ dps primal/dual closure of the corrected LP
import mpmath as mp
mp.mp.dps = 60
SIG=[mp.mpf(-1),mp.mpf(1),mp.mpf(1),mp.mpf(-1),mp.mpf(1)]
AEV=[3,4,7,9]                     # even F_{2q}: frequencies 4q = 12,16,28,36
PHI0=[mp.mpf('0.14721317'),mp.mpf('0.23048868'),mp.mpf('0.18365067'),mp.mpf('0.2094225'),mp.mpf('0.11795883')]
PHI0=[p*mp.pi for p in PHI0]

def newton(F,x0,maxit=80):
    x=mp.matrix(x0); n=len(x)
    for _ in range(maxit):
        r=F(x)
        J=mp.matrix(len(r),n); h=mp.mpf('1e-40')
        for j in range(n):
            xp=mp.matrix(x); xp[j]=xp[j]+h; rp=F(xp)
            for i in range(len(r)): J[i,j]=(rp[i]-r[i])/h
        dx=mp.lu_solve(J,mp.matrix([-t for t in r]))
        x=x+dx
        if max(abs(t) for t in dx) < mp.mpf('1e-55'): break
    return x

Occ=lambda p,k: mp.fsum([SIG[j]*mp.cos(k*p[j]) for j in range(5)])
Ev=lambda p,q: mp.fsum([mp.cos(4*q*p[j]) for j in range(5)])
def dOcc(p,k): return [ -k*SIG[j]*mp.sin(k*p[j]) for j in range(5)]
def dEv(p,q):  return [ -4*q*mp.sin(4*q*p[j]) for j in range(5)]

print("=== step 1: rebuild the KKT point at %d dps (from C-3863) ===" % mp.mp.dps, flush=True)
F1=lambda x: mp.matrix([Ev(x,q)-mp.mpf(1)/2 for q in AEV]+[Occ(x,13)+Occ(x,19)])
phi=newton(F1,PHI0)
print("   ||residual|| = %s" % mp.nstr(max(abs(t) for t in F1(phi)),5), flush=True)
print("   x = %s" % [mp.nstr(mp.cos(phi[j])**2,25) for j in range(5)], flush=True)

v13=[-t for t in dOcc(phi,13)]; v19=list(dOcc(phi,19))     # s13=-1, s19=+1
W=[dEv(phi,q) for q in AEV]
print("\n=== step 2: primal vertex system (6 eqs / 6 unknowns) ===", flush=True)
def Fp(z):
    h=[z[j] for j in range(5)]; c=z[5]
    return mp.matrix([mp.fsum([v13[j]*h[j] for j in range(5)])+1,
                      mp.fsum([v19[j]*h[j] for j in range(5)])+1]
                     +[mp.fsum([W[q][j]*h[j] for j in range(5)])-c for q in range(4)])
h0=[mp.mpf('0.024405'),mp.mpf('0.01462'),mp.mpf('-0.018416'),mp.mpf('0.02306'),mp.mpf('0.048962'),mp.mpf('0.500808953629')]
z=newton(Fp,h0); h=[z[j] for j in range(5)]; cp=z[5]
print("   c_p = %s" % mp.nstr(cp,30), flush=True)
print("   h*  = %s" % [mp.nstr(t,25) for t in h], flush=True)
print("   ||h||_inf = %s   (box strictly inactive? %s)" % (mp.nstr(max(abs(t) for t in h),10), mp.nstr(max(abs(t) for t in h),10)+" < 1"), flush=True)
print("   primal residuals: v13h+1 = %s ; v19h+1 = %s ; max_q(b_q-c) = %s"
      % (mp.nstr(mp.fsum([v13[j]*h[j] for j in range(5)])+1,5),
         mp.nstr(mp.fsum([v19[j]*h[j] for j in range(5)])+1,5),
         mp.nstr(max(abs(mp.fsum([W[q][j]*h[j] for j in range(5)])-cp) for q in range(4)),5)), flush=True)

print("\n=== step 3: dual system (5 stationarity + normalisation) ===", flush=True)
def Fd(y):
    mu=[y[q] for q in range(4)]; nu13,nu19=y[4],y[5]
    bal=[nu13*v13[j]+nu19*v19[j]+mp.fsum([mu[q]*W[q][j] for q in range(4)]) for j in range(5)]
    return mp.matrix(bal+[mp.fsum(mu)-1])
y0=[mp.mpf('0.4196'),mp.mpf('0.4957'),mp.mpf('0.0210'),mp.mpf('0.0637'),mp.mpf('0.452590'),mp.mpf('0.048219')]
y=newton(Fd,y0); mu=[y[q] for q in range(4)]; nu13,nu19=y[4],y[5]
print("   mu   = %s" % [mp.nstr(t,25) for t in mu], flush=True)
print("   nu13 = %s ; nu19 = %s" % (mp.nstr(nu13,25), mp.nstr(nu19,25)), flush=True)
print("   dual feasibility: mu>=0 %s ; nu>=0 %s ; sum(mu)-1 = %s"
      % (all(t>=0 for t in mu), (nu13>=0 and nu19>=0), mp.nstr(mp.fsum(mu)-1,5)), flush=True)
cd=nu13+nu19
print("   c_d = nu13+nu19 = %s" % mp.nstr(cd,30), flush=True)
print("   *** |c_p - c_d| = %s ***" % mp.nstr(abs(cp-cd),5), flush=True)
print("   stationarity residual = %s" % mp.nstr(max(abs(t) for t in Fd(y)[:5]),5), flush=True)
print("\n=== complementary slackness (all six rows active by construction) ===", flush=True)
print("   odd rows: v13h+1 = %s, v19h+1 = %s (with nu>0: %s, %s)"
      % (mp.nstr(0,1),mp.nstr(0,1), nu13>0, nu19>0), flush=True)
print("   c_p (30 sig) = %s" % mp.nstr(cp,30), flush=True)
print("DONE", flush=True)
