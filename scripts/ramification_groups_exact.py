"""LAYER 2 direct verification: compute the ramification groups of L=Q(delta,i) exactly.
L = K'(i), K' = Q(delta), delta^4 = 2.  O_L = Z[delta] + i Z[delta] = Z[delta,i] (assumed maximal).
valuation: v_q(x) = v_2(|N_{L/Q}(x)|)   [since e=8, f=1, all sigma fix q]
ramification groups: G_i = { sigma : v_q(sigma(e) - e) >= i+1 for all e in a Z-basis }
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
def det4(M):
    d=0
    for p in itertools.permutations(range(4)):
        s=1
        for i in range(4):
            for j in range(i+1,4):
                if p[i]>p[j]: s=-s
        t=s
        for i in range(4): t*=M[i][p[i]]
        d+=t
    return d
def norm4(u):
    cols=[mul4(u,e) for e in ((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))]
    return det4([[cols[j][i] for j in range(4)] for i in range(4)])

def add4(u,v): return tuple(a+b for a,b in zip(u,v))
def sub4(u,v): return tuple(a-b for a,b in zip(u,v))

# --- L elements as pairs (u,v): x = u + v*i,  u,v in Z[delta] ---
def Lmul(x,y):
    u,v=x; u2,v2=y
    return (sub4(mul4(u,u2),mul4(v,v2)), add4(mul4(u,v2),mul4(v,u2)))
def Lnorm_Q(x):
    u,v=x
    nKp=add4(mul4(u,u),mul4(v,v))     # N_{L/K'}(u+vi) = u^2+v^2
    return norm4(nKp)
def vq(x):
    if x==((0,0,0,0),(0,0,0,0)): return 10**9
    n=Lnorm_Q(x); a=abs(n)
    if a==0: return 10**9
    k=0
    while a%2==0: a//=2; k+=1
    return k

# --- Galois action: sigma(delta)=i*delta (fix i), tau(i)=-i (fix delta) ---
one4=(1,0,0,0); zero4=(0,0,0,0)
def sigma(x):
    """sigma: delta -> i*delta, i -> i.
    x = u + v i,  u=(a0,a1,a2,a3), v=(b0,b1,b2,b3)
    sigma(u) = a0 - a2 d^2 + i(a1 d - a3 d^3)
    sigma(v) = b0 - b2 d^2 + i(b1 d - b3 d^3)
    sigma(x) = sigma(u) + sigma(v)*i
             = a0 - a2 d^2 - (b1 d - b3 d^3)  +  i[(a1 d - a3 d^3) + b0 - b2 d^2]
    """
    u,v=x
    a0,a1,a2,a3=u; b0,b1,b2,b3=v
    return ((a0,-b1,-a2,b3),(b0,a1,-b2,-a3))
def tau(x):
    u,v=x
    return (u, tuple(-y for y in v))
basis = [((1,0,0,0),zero4),((0,1,0,0),zero4),((0,0,1,0),zero4),((0,0,0,1),zero4),
         (zero4,(1,0,0,0)),(zero4,(0,1,0,0)),(zero4,(0,0,1,0)),(zero4,(0,0,0,1))]
G=['id']+[ 's'*k for k in (1,2,3) ]+[ 's'*k+'t' for k in (0,1,2,3) ]
G=list(dict.fromkeys(G))

def act(word,x):
    y=x
    # word is a string like 'sst' meaning tau then sigma then sigma (applied right to left)
    for ch in word:
        y = sigma(y) if ch=='s' else tau(y)
    return y

print("="*88); print("sanity: valuations in L (v_q(x) = v_2 |N_{L/Q}(x)|)"); print("="*88)
print(f"  v_q(2)      = {vq((tuple([2,0,0,0]),zero4))}   (expect 8 = e)")
print(f"  v_q(delta)  = {vq(((0,1,0,0),zero4))}   (expect 2, since delta^4=2 and e=8)")
print(f"  v_q(i+1)    = {vq(((1,0,0,0),(1,0,0,0)))}   (uniformizer of the local Q2(i) part)")
print()
print("="*88); print("ramification groups G_i = { sigma : v_q(sigma(e)-e) >= i+1 for all basis e }"); print("="*88)
m={}
for w in G:
    vals=[]
    for e in basis:
        d=sub4 if False else None
        diff=(sub4(act(w,e)[0],e[0]), sub4(act(w,e)[1],e[1]))
        vals.append(vq(diff))
    m[w]=min(vals)
print("  element -> min_i v_q(sigma(e_i) - e_i)  [10^9 = infinity]")
for w in sorted(m,key=lambda z:(m[z],z)):
    print(f"    {w if w else 'id':>5} : {m[w] if m[w]<10**8 else 'inf'}")
print()
filt=[]
for i in range(0,8):
    Gi=[w for w in G if m[w]>=i+1]
    filt.append(len(Gi))
print(f"  |G_i| for i=0..7 : {filt}")
d=sum(g-1 for g in filt if g>0)
print(f"  different exponent from the filtration:  sum_i (|G_i| - 1) = {d}     (independent value from the tower: 22)")
print(f"  MATCH: {d==22}")
print()
print("="*88); print("comparison with the pattern I had cited"); print("="*88)
print(f"  cited pattern [8,8,4,4,2,2,1] gives d = {7+7+3+3+1+1}")
print(f"  computed pattern gives d = {d}")
