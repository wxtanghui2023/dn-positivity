# c380_70_C3870_attainment.py -- C3870: 6x6 six-active primal system; rank + solvability + c*=1/L
import mpmath as mp
mp.mp.dps = 60
SIG=[mp.mpf(-1),mp.mpf(1),mp.mpf(1),mp.mpf(-1),mp.mpf(1)]; AEV=[3,4,7,9]
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
Occ=lambda p,k: mp.fsum([SIG[j]*mp.cos(k*p[j]) for j in range(5)])
Ev =lambda p,q: mp.fsum([mp.cos(4*q*p[j]) for j in range(5)])
dOcc=lambda p,k: [-k*SIG[j]*mp.sin(k*p[j]) for j in range(5)]
dEv =lambda p,q: [-4*q*mp.sin(4*q*p[j]) for j in range(5)]
def Fk(z):
    p=[z[j] for j in range(5)]; om=z[5]; lam=[z[6+q] for q in range(4)]
    v13=[-t for t in dOcc(p,13)]; v19=list(dOcc(p,19))
    out=[om*v13[j]+(1-om)*v19[j]+mp.fsum([lam[q]*dEv(p,AEV[q])[j] for q in range(4)]) for j in range(5)]
    return mp.matrix(out+[Ev(p,q)-mp.mpf(1)/2 for q in AEV]+[Occ(p,13)+Occ(p,19)])
Z=newton(Fk,PHI0+[mp.mpf('0.903717944'),mp.mpf('0.83791706'),mp.mpf('0.98971406'),mp.mpf('0.04185319'),mp.mpf('0.12728511')])
p=[Z[j] for j in range(5)]; om=[Z[5],1-Z[5]]; lam=[Z[6+q] for q in range(4)]; L=mp.fsum(lam)
print("KKT residual %s ; L = %s"%(mp.nstr(max(abs(t) for t in Fk(Z)),5), mp.nstr(L,30)), flush=True)

v13=[-t for t in dOcc(p,13)]; v19=list(dOcc(p,19)); W=[dEv(p,q) for q in AEV]
rows=[v13,v19]+W
# 6x6 matrix for unknowns (h,c): rows.h - e*c = rhs, e=(0,0,1,1,1,1)
Mt=mp.matrix(6,6)
for i in range(6):
    for j in range(5): Mt[i,j]=rows[i][j]
    Mt[i,5] = mp.mpf(0) if i<2 else mp.mpf(-1)
print("\n=== C3870 item 1: rank of the six-active system ===", flush=True)
print("   det(Mtilde) = %s" % mp.nstr(mp.det(Mt),20), flush=True)
print("   |det| nonzero ? %s"% (abs(mp.det(Mt))>0), flush=True)
print("   rank = %s" % mp.nstr(mp.mpf(len([s for s in mp.svd(Mt)[1] if abs(s)>mp.mpf('1e-40')])) ,4), flush=True)

print("\n=== C3870 item 2/3: solve and verify c* = 1/L ===", flush=True)
rhs=mp.matrix([mp.mpf(-1),mp.mpf(-1),0,0,0,0])
sol=mp.lu_solve(Mt,rhs)
h=[sol[j] for j in range(5)]; cstar=sol[5]
print("   h* = %s" % [mp.nstr(t,20) for t in h], flush=True)
print("   ||h*||_inf = %s (box inactive)" % mp.nstr(max(abs(t) for t in h),10), flush=True)
print("   c* = %s" % mp.nstr(cstar,30), flush=True)
print("   1/L = %s" % mp.nstr(1/L,30), flush=True)
print("   *** L*c* - 1 = %s ***" % mp.nstr(L*cstar-1,5), flush=True)
print("   residual of the six rows: v13h+1 = %s ; v19h+1 = %s ; max_q(w_qh - c*) = %s"
      %(mp.nstr(mp.fsum([v13[j]*h[j] for j in range(5)])+1,5),
        mp.nstr(mp.fsum([v19[j]*h[j] for j in range(5)])+1,5),
        mp.nstr(max(abs(mp.fsum([W[q][j]*h[j] for j in range(5)])-cstar) for q in range(4)),5)), flush=True)

print("\n=== the algebraic derivation (independent of numerics) ===", flush=True)
print("   multiply KKT by h*: omega13(v13 h*) + omega19(v19 h*) + sum_q lambda_q (w_q h*) = 0", flush=True)
print("   with v13 h* = -1, v19 h* = -1 and w_q h* = c* for all four q:", flush=True)
print("   -(omega13+omega19) + c* * sum_q lambda_q = 0  =>  c* L = 1  =>  c* = 1/L  (forced by KKT)", flush=True)
chk=-(om[0]+om[1])+cstar*L
print("   numeric check of that identity: -(1) + c*L = %s" % mp.nstr(chk,5), flush=True)
print("DONE", flush=True)
