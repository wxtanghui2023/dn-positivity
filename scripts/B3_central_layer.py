"""
B3, steps 1-2-3: the central layer V_7 = G_7/G_8 = <sigma^2> inside the 2-dim irrep of D4,
the Schur scalar action, and the PRECISE correspondence with the conductor a(rho) = 8.
NO presupposition of 1/2, no r->(r-1)/2, no square root, no critical exponent.  L2 untouched.
"""
from fractions import Fraction as F
import itertools
# ---------------- D4 elements as (i,j) = sigma^i tau^j ----------------
def mul(a,b):
    i,j=a; k,l=b
    kk = k if j==0 else (-k)%4
    return ((i+kk)%4,(j+l)%2)
E=[(i,j) for i in range(4) for j in range(2)]
def gen(s):
    S={(0,0)}; fr=[(0,0)]
    while fr:
        x=fr.pop()
        for g in s:
            y=mul(x,g)
            if y not in S: S.add(y); fr.append(y)
    return frozenset(S)
sig=(1,0); tau=(0,1)
G=gen([sig,tau]); C4=gen([sig]); C2=gen([mul(sig,sig)]); ONE=gen([])
FILT=[G,G,C4,C4,C2,C2,C2,C2,ONE]
# ---------------- the 2-dimensional irrep ----------------
R=[[0,-1],[1,0]]; S=[[1,0],[0,-1]]
def mm(A,B): return [[sum(A[i][t]*B[t][j] for t in range(2)) for j in range(2)] for i in range(2)]
def pw(A,k):
    M=[[1,0],[0,1]]
    for _ in range(k): M=mm(M,A)
    return M
def rho(g):
    i,j=g
    M=pw(R,i)
    return mm(M,pw(S,j)) if j else M
print("="*84); print("STEP 1  explicit matrices of the 2-dim irrep"); print("="*84)
print(f"  rho(sigma) = {R}")
print(f"  rho(tau)   = {S}")
# self-check the D4 relations
ok1 = mm(mm(S,R),S)==pw(R,3)
ok2 = pw(R,4)==[[1,0],[0,1]]
ok3 = mm(S,S)==[[1,0],[0,1]]
print(f"  self-check: S R S = R^-1 ? {ok1}   R^4 = I ? {ok2}   S^2 = I ? {ok3}")
print()
print("  the central element sigma^2 acts as:")
print(f"    rho(sigma^2) = R^2 = {pw(R,2)}  = -I_2 ? {pw(R,2)==[[-1,0],[0,-1]]}")
print(f"    rho(sigma^3) = R^3 = {pw(R,3)}")
print()
print("="*84); print("STEP 2  Schur: is sigma^2 -> -I_2 NECESSARY for the 2-dim irrep?"); print("="*84)
# center of D4
Z=set(g for g in E if all(mul(g,h)==mul(h,g) for h in E))
print(f"  center Z(D4) = {sorted(Z)}   (sigma^2 = {(2,0)} is central: {(2,0) in Z})")
# character table of D4: compute chi_rho and inner product with itself
def chi(g): return rho(g)[0][0]+rho(g)[1][1]
print(f"  chi_rho(1) = {chi((0,0))}")
ip=F(0)
for g in E: ip += F(chi(g)*chi(g), len(E))
print(f"  <chi_rho, chi_rho> = {ip}   -> irreducible iff 1 ✓")
# the kernel of rho
ker=[g for g in E if rho(g)==[[1,0],[0,1]]]
print(f"  ker rho = {sorted(ker)}  = <sigma^2> ? {set(ker)==set(C2)}")
# argument: any irrep with sigma^2 in the kernel factors through D4/<sigma^2> = (Z/2)^2, whose irreps are ALL 1-dim
quot=set(g for g in E)
print("  argument: if sigma^2 acted as +I, then rho would factor through D4/<sigma^2>, which is (Z/2)^2")
print("            all irreducible representations of (Z/2)^2 have dimension 1")
print("            => rho would be reducible, contradicting <chi,chi> = 1 with dim 2")
print("  => lambda = -1 is FORCED:  rho(sigma^2) = -I_2 necessarily.")
print()
print("="*84); print("STEP 3  precise correspondence: central layer -> conductor a(rho)"); print("="*84)
print("""  Artin conductor (discrete form):   a(rho) = sum_{i>=0} (1/[G_0:G_i]) * codim V^{G_i}
  group the indices into LEVELS (blocks of constant G_i):""")
levels=[("G_0 = G_1 = D4", [0,1], G), ("G_2 = G_3 = <sigma>", [2,3], C4), ("G_4..G_7 = <sigma^2>", [4,5,6,7], C2)]
tot=F(0)
for name,idxs,Gi in levels:
    # fixed space of Gi inside V via the averaging projector
    n=len(Gi); P=[[F(0)]*2 for _ in range(2)]
    for g in Gi:
        M=rho(g)
        for i in range(2):
            for j in range(2): P[i][j]+=F(M[i][j],n)
    # fixed dim = dim ker(P - I)
    A=[[P[i][j]-(1 if i==j else 0) for j in range(2)] for i in range(2)]
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    fdim = 2 if (A[0][0]==0 and A[0][1]==0 and A[1][0]==0 and A[1][1]==0) else (1 if det==0 else 0)
    codim=2-fdim
    wsum=sum(F(1, len(G)//len(Gi)) for _ in idxs)
    contrib=wsum*codim
    tot+=contrib
    print(f"    level {name:>22}: indices {idxs}, weight-sum {wsum}, codim {codim}  -> contribution {contrib}")
print(f"  ==> a(rho) = {tot}   (expected 8)   MATCH: {tot==8}")
print()
print("  ⭐ the PRECISE (structural, not numerical) correspondence:")
print("""    codim V^{G_i} = dim V = 2 at EVERY level, and the reason at the central level is exactly
    rho(sigma^2) = -I_2 :  a fixed vector would be an eigenvector of rho(sigma^2) with eigenvalue +1,
    and -I_2 has no such eigenvector.   Hence the central level's contribution is
        (weight-sum 1) x (codim = dim rho = 2) = 2
    i.e. the central layer contributes EXACTLY dim(rho), and dim(rho) = 2 is itself forced by
    sigma^2 -> -I_2 through irreducibility.""")
print()
print("  per-level contributions:  4 (D4 level) + 2 (<sigma> level) + 2 (central <sigma^2> level) = 8")
print("  the 'weight-sum' of each of the last two levels equals 1, matching the upper-break interval")
print("  lengths: upper breaks are 1,2,3, so intervals [0,1),[1,2),[2,3) each have length 1 (verified in B1).")
