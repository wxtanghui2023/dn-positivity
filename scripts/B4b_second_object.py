"""
Candidate second objects for 'Artin profile -> A' dual scale', screened against verified material.
One new verified computation: the tensor square rho (x) rho -- the canonical self-dual companion.
NO 1/2, NO recursion, NO artificial weights, NO audit.  L2 untouched.
"""
from fractions import Fraction as F
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
FILT=[gen([sig,tau]),gen([sig,tau]),gen([sig]),gen([sig]),gen([mul(sig,sig)])]*1
FILT=[gen([sig,tau]),gen([sig,tau]),gen([sig]),gen([sig]),gen([mul(sig,sig)]),gen([mul(sig,sig)]),gen([mul(sig,sig)]),gen([mul(sig,sig)]),gen([])]
G=FILT[0]; g0=len(G)
R=[[0,-1],[1,0]]; S=[[1,0],[0,-1]]
def mm(A,B): return [[sum(A[i][t]*B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mmk(A,k):
    n=len(A); M=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k): M=mm(M,A)
    return M
def rho(g):
    i,j=g
    M=mmk(R,i)
    return mm(M,mmk(S,j)) if j else M
def fixeddim(rep,dim,Gi):
    n=len(Gi)
    P=[[F(0)]*dim for _ in range(dim)]
    for g in Gi:
        M=rep(g)
        for a in range(dim):
            for b in range(dim): P[a][b]+=F(M[a][b],n)
    # rank of P (= dim of fixed space), exact
    A=[row[:] for row in P]; rank=0
    for c in range(dim):
        piv=None
        for r in range(rank,dim):
            if A[r][c]!=0: piv=r; break
        if piv is None: continue
        A[rank],A[piv]=A[piv],A[rank]
        pv=A[rank][c]
        for r in range(dim):
            if r!=rank and A[r][c]!=0:
                f=A[r][c]/pv
                for j in range(c,dim): A[r][j]-=f*A[rank][j]
        rank+=1
    return rank
# tensor square rep
def rho_tensor(g):
    M=rho(g)
    return [[M[a][c]*M[b][d] for c in range(2) for d in range(2)] for a in range(2) for b in range(2)]
phi=[F(0)]
for i in range(1,9): phi.append(F(sum(len(FILT[j]) for j in range(1,i+1)), g0))
intervals=[(-F(1),F(0),0)]+[(phi[i-1],phi[i],i) for i in range(1,9)]
def profile(rep,dim):
    out=[]
    for lo,hi,i in intervals:
        if hi==lo: continue
        c=dim-fixeddim(rep,dim,FILT[i])
        out.append((lo,hi,i,c))
    return out
print("="*82); print("profile of rho  vs  profile of the tensor square rho(x)rho"); print("="*82)
for name,rep,dim in (("rho",rho,2),("rho(x)rho",rho_tensor,4)):
    pr=profile(rep,dim)
    area=sum((hi-lo)*c for lo,hi,i,c in pr)
    print(f"\n  {name} (dim {dim}):")
    for lo,hi,i,c in pr:
        print(f"    ({lo},{hi}]  G_{i}  codim = {c}   (length {hi-lo})")
    print(f"    ==> integral = {area}")
print()
print("="*82); print("structural facts about rho(x)rho (verified)"); print("="*82)
# character of rho(x)rho and its decomposition into irreps of D4
def chi_r(g): return rho(g)[0][0]+rho(g)[1][1]
def linchar(g,ab):
    a,b=ab; i,j=g
    return ((-1)**a)**i*((-1)**b)**j
def ip(f1,f2): return F(sum(f1(g)*f2(g) for g in E), len(E))
print("  <chi_{rho(x)rho}, chi_1>   =", ip(lambda g: chi_r(g)**2, lambda g: 1))
for ab in [(0,1),(1,0),(1,1)]:
    print(f"  <chi_(rho x rho), chi_{ab}> = ", ip(lambda g: chi_r(g)**2, lambda g: linchar(g,ab)))
print("  <chi_(rho x rho), chi_rho>  =", ip(lambda g: chi_r(g)**2, chi_r))
print("  => rho(x)rho = 1 + chi_(0,1) + chi_(1,0) + chi_(1,1)   (all four constituents 1-dimensional)")
print(f"  a(rho)      = 8,   a(rho(x)rho) = a(1)+a(0,1)+a(1,0)+a(1,1) = 0+2+3+3 = {0+2+3+3}")
print("  => the two profiles give the SAME conductor 8 but are DIFFERENT:  rho -> (2,2,2),  rho(x)rho -> (3,2,0)")
print()
print("="*82); print("screening of candidate 'second objects'"); print("="*82)
print("""  (a) local reciprocity / unit filtration U^v (Herbrand psi = phi^{-1})
        -> pairs with the ABELIAN part only; gives the same information as the quadratic characters;
           on our example that pairing is DEGENERATE (B2: rank 1)  => does not give a nondegenerate two-scale
  (b) Kummer classes with the Hilbert pairing
        -> verified degenerate on the layer space (radical = span{[2]})                 => same obstruction as (a)
  (c) the Kummer 2-cover K -> K' = K(sqrt(sqrt2)) (built and verified earlier)
        -> a genuine SECOND arithmetic object attached to the same ramification data  => live candidate
  (d) the tensor square rho (x) rho  (canonical self-dual companion of the central layer)
        -> SAME conductor 8, DIFFERENT profile (3,2,0) vs (2,2,2);  it is the natural object in which the
           central (non-abelian) information meets all three abelian characters                  => live candidate
  => (c) and (d) are the two natural second objects; (a)/(b) are excluded on this example by the B2 degeneracy.""")
