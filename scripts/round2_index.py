"""(a) round-2 index determination:  [O_L : Z[delta,i]] ,  L = Q(delta,i), delta^4 = 2.
Index is a power of 2 since disc(Z[delta,i]) = 2^30.  Integrality test = characteristic
polynomial of the regular representation has integer coefficients."""
from fractions import Fraction as F
import itertools
def mul4(u,v):
    raw=[0]*7
    for i,a in enumerate(u):
        for j,b in enumerate(v): raw[i+j]+=a*b
    for k in range(6,3,-1):
        c=raw[k]
        if c: raw[k]-=c; raw[k-4]+=2*c
    return tuple(raw[:4])
def add4(u,v): return tuple(a+b for a,b in zip(u,v))
def sub4(u,v): return tuple(a-b for a,b in zip(u,v))
def Lmul(x,y):
    u,v=x; u2,v2=y
    return (sub4(mul4(u,u2),mul4(v,v2)), add4(mul4(u,v2),mul4(v,u2)))
BAS=[]
for j in range(8):
    b=[0]*4
    b[j%4]=1
    BAS.append((tuple(b),(0,0,0,0)) if j<4 else ((0,0,0,0),tuple(b)))
def coords(x): return tuple(x[0])+tuple(x[1])
def vec2el(v): return (tuple(v[0:4]), tuple(v[4:8]))
def mult_matrix(v):
    x=vec2el(v); cols=[coords(Lmul(x,BAS[j])) for j in range(8)]
    return [[cols[j][i] for j in range(8)] for i in range(8)]
def mm(A,B):
    n=len(A); return [[sum(A[i][t]*B[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
def charpoly_ints(v):
    M=mult_matrix(v); n=8
    P=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    p=[]
    for k in range(1,n+1):
        P=mm(P,M); p.append(sum(P[i][i] for i in range(n)))
    e=[]
    for k in range(1,n+1):
        acc=F(0)
        for j in range(1,k+1):
            ej = F(1) if (k-j)==0 else e[k-j-1]
            acc += ((-1)**(j-1))*ej*p[j-1]
        e.append(acc/k)
    c=[F(1)]+[((-1)**k)*e[k-1] for k in range(1,n+1)]
    return all(x.denominator==1 for x in c)
def det8(M):
    n=8; s=F(0)
    for p in itertools.permutations(range(n)):
        sg=1
        for i in range(n):
            for j in range(i+1,n):
                if p[i]>p[j]: sg=-sg
        t=F(sg)
        for i in range(n): t*=F(M[i][p[i]])
        s+=t
    return s
def pick_basis(rows):
    """choose 8 rows forming a rank-8 set; return (index=|det|, chosen rows)"""
    cur=[]
    for r in rows:
        trial=cur+[r]
        if rank_q(trial)==8:
            cur=trial
            if len(cur)==8: break
    if len(cur)<8: return None,None
    M=[[cur[j][i] for j in range(8)] for i in range(8)]
    d=det8(M)
    return abs(d), cur
def rank_q(rows):
    M=[[F(x) for x in r] for r in rows]
    n=len(M[0]); r=0
    for c in range(n):
        piv=None
        for i in range(r,len(M)):
            if M[i][c]!=0: piv=i; break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                q=M[i][c]/M[r][c]
                for j in range(n): M[i][j]-=q*M[r][j]
        r+=1
    return r
def rowHNF_index(rows):
    """rows: list of integer 8-vectors generating a lattice L' <= Z^8.
       returns (index [Z^8 : L'], basis rows)  -- interior HNF on the row matrix"""
    M=[list(map(int,r)) for r in rows]
    n=len(M[0]); R=len(M); r=0
    for c in range(n):
        while True:
            piv=None
            for i in range(r,R):
                if M[i][c]!=0: piv=i; break
            if piv is None: break
            M[r],M[piv]=M[piv],M[r]
            for i in range(R):
                if i!=r and M[i][c]!=0:
                    q=M[i][c]//M[r][c]
                    if q:
                        for j in range(n): M[i][j]-=q*M[r][j]
            # reduce further if any |M[i][c]| >= |M[r][c]| remains
            done=True
            for i in range(R):
                if i!=r and M[i][c]!=0 and abs(M[i][c])>=abs(M[r][c]): done=False
            if done: break
        if r<R: r+=1
    diag=[abs(M[i][i]) for i in range(min(R,n))]
    idx=1
    for d in diag: idx*=d
    # count rank
    rank=sum(1 for i in range(min(R,n)) if diag[i]!=0)
    return (idx if rank==n else None), M[:n]
print("="*84); print("(a) round-2 index  [O_L : Z[delta,i]]"); print("="*84)
print("  disc(Z[delta,i]) = 2^30  =>  index is a power of 2  =>  only p = 2 matters")
basis=[list(coords(b)) for b in BAS]     # current order's basis (8 vectors of length 8)
covol=1
for rnd in range(1,12):
    found=[]
    for mask in range(1,256):
        v=[F(0)]*8
        for j in range(8):
            if (mask>>j)&1:
                for i in range(8): v[i]+=F(1,2)*F(basis[j][i])
        if all(x.denominator==1 for x in v): continue
        if charpoly_ints(v): found.append([x for x in v])
    if not found:
        print(f"  round {rnd}: no new integral half-elements -> ORDER IS STABLE at this prime"); break
    # work in the doubled lattice: multiply everything by 2 so coordinates are integers
    rows=[[2*F(x) for x in basis[j]] for j in range(8)]+[[2*F(x) for x in f] for f in found]
    idx,newb=pick_basis(rows)
    newb=[[F(x,2) for x in r] for r in newb] if newb else None
    print(f"  round {rnd}: {len(found):>3} new integral half-elements;  [new : current] = {idx}")
    if idx is None or idx==1:
        print("     (no genuine enlargement) -> ORDER STABLE at this prime"); break
    covol*= idx//2 if idx%2==0 else idx     # index in the original scaling: doubled lattice index / 2^8*... 
    basis=newb
print()
print(f"  ==>  index [O_L : Z[delta,i]] = {covol}")
print(f"  ==>  |D_L| = 2^30 / index^2 = ", end="")
k=0; t=covol
while t%2==0: t//=2; k+=1
print(f"2^{30-2*k}" if t==1 else f"2^30/{covol**2} (not a power of 2 — check!)")
print(f"  ==>  d(L/Q_2) = 30 - 2*{k} = {30-2*k}" if t==1 else "")
