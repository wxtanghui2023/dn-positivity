# c380_71_C3871_structure.py -- C3871: exact decomposition M=[G|-e_E]; R1 rank G=5 ; R2 e_E not in col(G)
import mpmath as mp, itertools
mp.mp.dps = 60
SIG=[mp.mpf(-1),mp.mpf(1),mp.mpf(1),mp.mpf(-1),mp.mpf(1)]
PHI0=[p*mp.pi for p in [mp.mpf('0.14721317'),mp.mpf('0.23048868'),mp.mpf('0.18365067'),mp.mpf('0.2094225'),mp.mpf('0.11795883')]]
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
Ev=lambda p,q: mp.fsum([mp.cos(4*q*p[j]) for j in range(5)])
Occ=lambda p,k: mp.fsum([SIG[j]*mp.cos(k*p[j]) for j in range(5)])
p=newton(lambda x: mp.matrix([Ev(x,q)-mp.mpf(1)/2 for q in [3,4,7,9]]+[Occ(x,13)+Occ(x,19)]), PHI0)
print("KKT point rebuilt (60 dps): x = %s"%[mp.nstr(mp.cos(p[j])**2,22) for j in range(5)], flush=True)

# rows: odd frequencies 13,19 (gamma = sigma) ; even frequencies 12,16,28,36 (gamma = 1)
odd_k=[13,19]; even_k=[12,16,28,36]
def Grow(k, odd):
    gam = SIG if odd else [mp.mpf(1)]*5
    return [ -k*gam[j]*mp.sin(k*p[j]) for j in range(5)]
rows=[Grow(k,True) for k in odd_k]+[Grow(k,False) for k in even_k]
G=mp.matrix(rows)
print("\n=== R1: rank of the 6x5 gradient matrix G ===", flush=True)
sv=mp.svd(G)[1]; print("   singular values: %s"%[mp.nstr(t,12) for t in sv], flush=True)
print("   rank = %d"%(len([t for t in sv if abs(t)>mp.mpf('1e-40')])), flush=True)
print("\n   the six 5x5 minors (drop one row each):", flush=True)
for drop in range(6):
    idx=[i for i in range(6) if i!=drop]
    sub=mp.matrix(5,5)
    for a,i in enumerate(idx):
        for j in range(5): sub[a,j]=G[i,j]
    d=mp.det(sub)
    print("     drop row %d (k=%s): det = %s"%(drop, (odd_k+even_k)[drop], mp.nstr(d,12)), flush=True)

print("\n=== Chebyshev reduction: G_k = -k * diag(gamma_j sin(phi_j)) * (U_{k-1}(z_j))_j ===", flush=True)
print("   => row dependence <=> dependence of the U-evaluation rows (sin(k phi)=sin(phi) U_{k-1}(cos phi))", flush=True)
maxerr=mp.mpf(0)
for i,k in enumerate(odd_k+even_k):
    for j in range(5):
        u=mp.sin((k-1)*mp.acos(mp.cos(p[j])))/mp.sin(mp.acos(mp.cos(p[j])))
        pred=-k*(SIG[j] if i<2 else mp.mpf(1))*mp.sin(p[j])*u
        maxerr=max(maxerr, abs(pred-G[i,j]))
print("   max |row entry - Chebyshev prediction| = %s" % mp.nstr(maxerr,5), flush=True)

print("\n=== R2: e_E in col(G) ? (e_E=(0,0,1,1,1,1)) ===", flush=True)
M=mp.matrix(6,6)
for i in range(6):
    for j in range(5): M[i,j]=G[i,j]
    M[i,5]= mp.mpf(0) if i<2 else mp.mpf(-1)
print("   rank[G] = 5 ; rank[M] = %d ; det(M) = %s"
      %(len([t for t in mp.svd(M)[1] if abs(t)>mp.mpf('1e-40')]), mp.nstr(mp.det(M),14)), flush=True)
print("   R2 holds (e_E not in col G) <=> rank[M] = 6 : %s"%(len([t for t in mp.svd(M)[1] if abs(t)>mp.mpf('1e-40')])==6), flush=True)
rhs=mp.matrix([mp.mpf(1)]*6)
try:
    h=mp.lu_solve(M,rhs); print("   (a solution of  Gh = e_E  would appear here if it existed)", flush=True)
except Exception as e:
    print("   Gh = e_E unsolvable: %s"%str(e)[:60], flush=True)
print("\n=== discipline note ===", flush=True)
print("   Chebyshev systems alone do NOT give R1: a combination of U_5,U_7,U_12,U_13,U_17,U_18 is a polynomial", flush=True)
print("   of degree <= 18 and can vanish at the five sampled z_j; hence R1 needs the specific sample structure.", flush=True)
print("DONE", flush=True)
