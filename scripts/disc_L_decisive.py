"""DECISIVE: compute disc(Z[delta,i]) exactly (8x8 trace form) to settle d(L/Q) = 30 or 50.
L = Q(delta,i): x = u + v i, u,v in Z[delta]; multiplication (u,v)(u',v') = (uu'-vv', uv'+vu').
disc(order) = det(Tr(e_i e_j)) ;  D_L = disc(order)/[O_L:order]^2.
"""
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
def Ltr(x):
    s=0
    for j in range(8):
        e=((1,0,0,0),0) if False else None
        # basis vectors
        if j<4:
            b=[0,0,0,0]; b[j]=1; e=(tuple(b),(0,0,0,0))
        else:
            b=[0,0,0,0]; b[j-4]=1; e=((0,0,0,0),tuple(b))
        col=Lmul(x,e)
        s += col[0][j] if j<4 else col[1][j-4]
    return s
basis=[]
for j in range(8):
    if j<4:
        b=[0,0,0,0]; b[j]=1; basis.append((tuple(b),(0,0,0,0)))
    else:
        b=[0,0,0,0]; b[j-4]=1; basis.append(((0,0,0,0),tuple(b)))
print("trace checks:")
print(f"  Tr(1)    = {Ltr(basis[0])}  (expect 8)")
print(f"  Tr(delta)= {Ltr(basis[1])}  (expect 0)")
print(f"  Tr(i)    = {Ltr(basis[4])}  (expect 0)")
print(f"  Tr(delta^2)= {Ltr(basis[2])}  (expect 8)   [delta^2=sqrt2 has 4 embeddings -> value, 4 -> -value]")
T=[[Ltr(Lmul(basis[i],basis[j])) for j in range(8)] for i in range(8)]
# Bareiss determinant (exact)
def det_bareiss(M):
    M=[row[:] for row in M]; n=len(M); sign=1; prev=1
    for k in range(n-1):
        if M[k][k]==0:
            for i in range(k+1,n):
                if M[i][k]!=0: M[i],M[k]=M[k],M[i]; sign=-sign; break
            else: return 0
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*M[k][k]-M[i][k]*M[k][j])//prev
            M[i][k]=0
        prev=M[k][k]
    return sign*M[n-1][n-1]
D=det_bareiss(T)
a=abs(D); k=0
while a%2==0: a//=2; k+=1
print()
print(f"disc(Z[delta,i]) = {D}")
print(f"  |disc| = 2^{k} * {a}    (2-adic valuation = {k})")
print()
print("comparison:")
print("  tower route gave d = 30  (2*11 + 8, with the relative different exponent 8)")
print("  ramification-group route gave d = 50  (truncated sum was 48, full sum 50)")
print(f"  disc gives 2^{k} (times an odd factor {a})")
print()
print("=> the ORDER here is Z[delta,i]; if it equals O_L then |D_L| = |disc| and the truth is 2^%d" % k)
