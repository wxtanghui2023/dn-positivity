"""
B1 (structural construction only, no 1/2 computation):
  V_i = G_i/G_{i+1}, breaks, Herbrand function, and the layer <-> quadratic-subfield <-> character dictionary.
Self-check: layer orders; break positions; phi at breaks integral; dictionary matches the conductor table.
"""
from fractions import Fraction as F
# ---- D4 ----
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
G=gen([sig,tau]); C4=gen([sig]); C2=gen([mul(sig,sig)])
FILT=[G,G,C4,C4,C2,C2,C2,C2,gen([])]
print("="*80); print("B1  layer structure of the filtration"); print("="*80)
print(f"  |G_i| (i=0..8) = {[len(g) for g in FILT]}")
# layer quotients: |V_i| = |G_i|/|G_{i+1}|
V=[len(FILT[i])//len(FILT[i+1]) for i in range(8)]
print("  |V_i| = |G_i| / |G_(i+1)| = " + str(V))
nontriv=[i for i in range(8) if V[i]>1]
print(f"  nontrivial layers (|V_i|>1): i = {nontriv}   (each of order {set(V[i] for i in nontriv)})")
# lower breaks: i where G_i strictly contains G_{i+1}
brk=[i for i in range(8) if FILT[i]!=FILT[i+1]]
print(f"  lower breaks (G_i > G_{{i+1}}): {brk}")
# Herbrand phi(i) = (1/|G_0|) * sum_{j=1..i} |G_j|
def phi(i):
    return F(sum(len(FILT[j]) for j in range(1,i+1)), len(FILT[0]))
print(f"  Herbrand phi: " + ", ".join(f"phi({i})={phi(i)}" for i in range(0,9)))
print(f"  upper breaks phi(lower breaks) = {[str(phi(i)) for i in brk]}   integral: {all(phi(i).denominator==1 for i in brk)}")
print(f"  layer contributions to d: |G_i|-1 for each i = {[len(FILT[i])-1 for i in range(8)]}  (sum {sum(len(FILT[i])-1 for i in range(8))})")
print()
print("="*80); print("B1'  layer <-> quadratic subfield <-> character dictionary"); print("="*80)
# action on L:  x = u + v i, coordinates (a0,a1,a2,a3 | b0,b1,b2,b3) in basis 1,delta,delta^2,delta^3
def sigma_act(v):
    a0,a1,a2,a3,b0,b1,b2,b3=v
    return [a0,-b1,-a2,b3, b0,a1,-b2,-a3]
def tau_act(v): return [v[0],v[1],v[2],v[3],-v[4],-v[5],-v[6],-v[7]]
def act(w,v):
    for ch in reversed(w):
        v = sigma_act(v) if ch=='s' else tau_act(v)
    return v
WORD={ '':(0,0) }
def g_of(w):
    x=(0,0)
    for ch in w: x=mul(x, sig if ch=='s' else tau)
    return x
WORD={w:g_of(w) for w in ['','s','ss','sss','t','st','sst','ssst']}
ELEM2WORD={v:k for k,v in WORD.items()}
def word_of(g): return ELEM2WORD[g]
# the three quadratic subfields, given by an element generating them over Q_2
subs={'Q_2(i)':[0,0,0,0,1,0,0,0],              # i
      'Q_2(sqrt2)':[0,0,1,0,0,0,0,0],          # delta^2 = sqrt2
      'Q_2(sqrt(-2))':[0,0,0,0,0,0,1,0]}       # i*delta^2
# note: i*delta^2 has coords (0,0,0,0 | 0,0,1,0)
subs['Q_2(sqrt(-2))']=[0,0,0,0,0,0,1,0]
def fixes(w,x): return act(w,x)==x
for name,x in subs.items():
    H=[g for g in E if fixes(word_of(g),x)]
    Hset=frozenset(H)
    # character with kernel H
    ker=[g for g in E if g in Hset]
    # find the linear character whose kernel is H (H must be index 2)
    assert len(Hset)==4
    chi={g:(1 if g in Hset else -1) for g in E}
    # Artin conductor of this character (1-dim):  a = sum_i (1/[G_0:G_i]) * codim
    tot=F(0)
    for i,Gi in enumerate(FILT):
        inv = all(chi[g]==1 for g in Gi)
        tot += F(0 if inv else 1, len(G)//len(Gi))
    print(f"  {name:>16}: Gal(L/F) = {sorted(Hset)} (|H|={len(Hset)}) -> quadratic character conductor a = {tot}")
print()
print("  parity of the layer type (linear vs central):")
Gprime=gen([mul(mul(sig,mul(sig,sig)),mul(sig,sig))])  # placeholder
# commutator subgroup of D4 is <sigma^2>
D=gen([mul(sig,sig)])
print(f"    commutator subgroup [G,G] = {sorted(D)}  (contains sigma^2)")
for i in nontriv:
    Vi=set()
    for g in FILT[i]: Vi.add(mul(g, (0,0)))
    # representative element of the layer: an element of G_i not in G_{i+1}
    rep=[g for g in FILT[i] if g not in FILT[i+1]][0]
    incomm = rep in D
    print(f"    layer i={i}: representative {rep}, in [G,G]? {incomm}  -> "
          f"{'NOT detected by linear characters (central-type)' if incomm else 'detected by a linear character'}")
