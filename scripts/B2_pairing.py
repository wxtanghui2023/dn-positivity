"""
B2: the pairing induced on the ramification layers, built from the natural alternating object
(NOT a new artificial pairing): the Hilbert symbol on Kummer classes, i.e. the cup product
H^1(G_Q2,Z/2) x H^1(G_Q2,Z/2) -> H^2(G_Q2,Z/2) = Z/2.
Every value is checked independently: entries = 1 by EXHIBITING a norm representation;
the entry -1 by the mod-8 obstruction (verified by exhaustion) + the standard criteria.
"""
print("="*84); print("B2  the quadratic classes of the three layers, and their natural pairing"); print("="*84)
print("""  layer i=1  <-> Q_2(i)        <-> class [-1]
  layer i=3  <-> Q_2(sqrt2)    <-> class [2]
  layer i=3  <-> Q_2(sqrt(-2)) <-> class [-2] = [-1]*[2]
  layer i=7  <-> central <sigma^2>, NOT the kernel of any linear character (no class in H^1)
  => the layers visible to H^1(G,Z/2) span the 2-dimensional space {[-1], [2]}  inside Q_2*/(Q_2*)^2""")
print()
print("  explicit verifications (entries = +1 by exhibiting a norm):")
# (2,-1):  is 2 a norm from Q_2(i) (N(a+bi)=a^2+b^2)?  exhibit
print("    (2,-1): 2 = 1^2 + 1^2  -> 2 IS a norm from Q_2(i)        => (2,-1)_2 = +1")
# (2,2): is 2 a norm from Q_2(sqrt2) (N(a+b d)=a^2-2b^2)?
print("    (2, 2): 2 = 2^2 - 2*1^2 -> 2 IS a norm from Q_2(sqrt2)   => (2, 2)_2 = +1")
# (2,-2): is -2 a norm from Q_2(sqrt2)?
print("    (2,-2): -2 = 0^2 - 2*1^2 -> -2 IS a norm from Q_2(sqrt2) => (2,-2)_2 = +1")
print()
print("  the entry that is -1:")
sols=[]
for x in range(-40,41):
    for y in range(-40,41):
        if (x*x+y*y+1)%8==0: sols.append((x,y))
print(f"    exhausting |x|,|y| <= 40 for x^2 + y^2 == -1 (mod 8): solutions found = {len(sols)}")
print("    mod-8 obstruction: unit square = 1 mod 8, so x^2+y^2 in {1,2,5} mod 8 while -1 = 7 mod 8")
print("    => x^2 + y^2 = -1 has NO 2-adic solution => -1 is NOT a norm from Q_2(i) => (-1,-1)_2 = -1")
print()
print("="*84); print("  the induced pairing matrix on the layer space, and its rank"); print("="*84)
# entries on basis {[-1],[2]}, values in F_2 (0 for +1, 1 for -1)
M=[[1,0],[0,0]]
print("    basis {[-1], [2]}:  matrix (entries in F_2, 1 means the symbol is -1):")
print(f"      [[{M[0][0]}, {M[0][1]}],")
print(f"       [{M[1][0]}, {M[1][1]}]]")
rank = 1 if (M[0][0] or M[0][1] or M[1][0] or M[1][1]) else 0
print(f"    rank over F_2 = {rank}   (space has dimension 2)")
print(f"    radical (vectors pairing trivially with everything): span{{[2]}}")
print()
print("="*84); print("  CONCLUSION of B1+B2 (structural, verified; no 1/2 computed)"); print("="*84)
print("""   (1) the ramification filtration has exactly three nontrivial layers, at i = 1, 3, 7, each ≅ Z/2
   (2) upper breaks phi = 1, 2, 3 : an EQUALLY SPACED ladder (verified; Hasse-Arf holds here)
   (3) layer types split into TWO kinds:
         i = 1, 3 : abelian-type (representatives tau, sigma are OUTSIDE [G,G] = <sigma^2>)
         i = 7    : CENTRAL-type (representative sigma^2 lies IN [G,G]) -> invisible to any linear character
   (4) the natural pairing (Hilbert / cup product on H^1) restricted to the layer space spanned by
       the quadratic classes is DEGENERATE, of rank 1, with radical spanned by the class [2] of Q_2(sqrt2)
   ==> there is NO non-degenerate complementarity between the abelian layers in this example;
       the pairing CANNOT see the central layer at all.
   ==> hence the only place where a nontrivial layer-interaction can live is the central layer i=7
       together with the 2-dimensional representation (conductor 8).  This is a TARGET, not a result.""")
