"""
VERIFICATION: reconcile the reported formula C=(2*floor(B/g)+1)^2 with the printed values 28/6/1.
Prints (1) the ACTUAL code definition used, (2) per-state outputs, (3) max/min over states by g,
(4) the formula, (5) monotonicity of the max.
"""
from math import gcd
B=3
print("="*84); print("(1) ACTUAL C DEFINITION AS USED IN abd1p.py (verbatim logic)"); print("="*84)
print("""    g = gcd(a,b)
    n = 0
    for p in range(-B, B+1):
        if p % g: continue
        for q in range(-B, B+1):
            if q % g: continue
            if a+p >= 1 and b+q >= 1: n += 1     # <<< BOUNDARY CLIPPING
    return n""")
print()
def C(a,b,B=B):
    g=gcd(a,b); n=0
    for p in range(-B,B+1):
        if p%g: continue
        for q in range(-B,B+1):
            if q%g: continue
            if a+p>=1 and b+q>=1: n+=1
    return n
print("="*84); print("(2) THE STATES I QUOTED (c=20)  -- these reproduce 28 / 6 / 1"); print("="*84)
for (a,b) in [(1,19),(2,18),(4,16),(5,15),(10,10),(7,13),(3,17),(9,11)]:
    g=gcd(a,b)
    print(f"   (a,b)=({a:>2},{b:>2})  c=20  g={g:>2}   C={C(a,b):>3}   multip-of-g pairs allowed = "
          f"{len([p for p in range(-B,B+1) if p%g==0])}x{len([q for q in range(-B,B+1) if q%g==0])}")
print()
print("="*84); print("(3) MAX / MIN OF C OVER ALL STATES WITH A GIVEN g     (the honest monotonicity test)"); print("="*84)
for c in (12,20,30):
    rows={}
    for a in range(1,c):
        b=c-a; g=gcd(a,b)
        rows.setdefault(g,[]).append(C(a,b))
    print(f"   c={c}:")
    for g in sorted(rows):
        vals=rows[g]
        print(f"      g={g:>2}   max C = {max(vals):>3}   min C = {min(vals):>3}   #states = {len(vals):>2}")
print()
print("="*84); print("(4) THE FORMULA vs THE MEASURED MAX"); print("="*84)
for g in (1,2,3,4,5,10):
    formula=(2*(B//g)+1)**2
    print(f"   g={g:>2}   formula (2*floor(B/g)+1)^2 = {formula:>3}")
print("   => the formula is the UNCLIPPED count, attained at INTERIOR states (a,b > B);")
print("      states near the boundary (e.g. a=1) are CLIPPED and give smaller values (28, not 49).")
print()
print("="*84); print("(5) MONOTONICITY OF max C(g)  over the g actually occurring"); print("="*84)
for c in (12,20,30,60):
    rows={}
    for a in range(1,c):
        b=c-a; g=gcd(a,b)
        rows.setdefault(g,[]).append(C(a,b))
    gs=sorted(rows); mx=[max(rows[g]) for g in gs]
    mono=all(mx[i]>=mx[i+1] for i in range(len(mx)-1))
    print(f"   c={c:>3}: g={gs}  maxC={mx}   monotone non-increasing: {mono}")
print()
print("="*84); print("VERIFICATION VERDICT"); print("="*84)
print("""  (i)   The reported numbers 28 / 6 / 1 are EXACT CODE OUTPUTS but for SPECIFIC states:
        (1,19) -> 28, (2,18) -> 6, (4,16) -> 1, (5,15) -> 1, (10,10) -> 1.
        They are BOUNDARY-CLIPPED values (the clipping a+p >= 1, b+q >= 1 bites when a or b <= B).
  (ii)  The formula (2*floor(B/g)+1)^2 is the UNCLIPPED count: g=1 -> 49, g=2 -> 9, g>=4 -> 1.
        It is NOT violated; it simply does not produce 28 / 6.  My earlier report wrongly presented
        clipped state-values as if they were the formula's values  ==> REPORT ERROR (now corrected).
  (iii) The MONOTONICITY CLAIM SURVIVES: taking max C over all states with a given g,
        the sequence is non-increasing in g and equals the formula at interior states.
  (iv)  The anti-alignment conclusion is therefore STRENGTHENED, not weakened:
        balanced state (c/2,c/2) has g=c/2, C=1 (the MINIMUM), while interior primitive states
        (g=1) have C=49 (the MAXIMUM).  Corrected comparison: 49 vs 1 (not 28 vs 1).
  (v)   Note: my own output A2 (40 counterexamples to 'C is a function of (g,c) alone') had ALREADY
        flagged boundary clipping; the earlier report failed to reconcile that with the g-table.
""")
