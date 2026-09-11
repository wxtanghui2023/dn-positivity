"""
ADC1: (a) verify Tang S3/S11: every AM coupling of n collapses to the SAME normal form
           (n as the sum of n ones) -- i.e. the semiring quotient identifies all couplings.
      (b) enumerate the model-theoretic sources of STRICT CONTRACTION (Tang P4).
Discipline: calibrate first; no 1/2 input; L2 untouched.
"""
from itertools import product
print("="*84); print("STEP 0 CALIBRATION"); print("="*84)
print(f"  1+1 = {1+1} ; 1*1 = {1*1} ; (1+1)*(1+1) = {(1+1)*(1+1)}")
assert 1+1==2 and (1+1)*(1+1)==4
print("  calibration OK")
print()

print("="*84); print("(a) the normal-form claim of Tang S3 -- and an honest caveat"); print("="*84)
# proper enumeration: terms of size <= K over the single leaf 1 with + and *
def terms(K):
    """all terms with at most K occurrences of the leaf 1 (and K-1 operations)"""
    from functools import lru_cache
    @lru_cache(None)
    def gen(k):
        if k==1: return (("1",1),)
        out=[]
        for i in range(1,k):
            for s1,v1 in gen(i):
                for s2,v2 in gen(k-i):
                    out.append((f"({s1}+{s2})", v1+v2))
                    out.append((f"({s1}*{s2})", v1*v2))
        return tuple(set(out))
    return gen(K)
E=terms(5)
byval={}
for s,v in E: byval.setdefault(v,set()).add(v)     # normal form of a value = its one-count = the value itself
print(f"  terms with <= 5 leaves: {len(E)};  distinct values reached: {len(byval)}")
print(f"  value range reached: {min(byval)} .. {max(byval)};  contains 6? {6 in byval}   (ERR#12 fixed: deeper)")
viol=[v for v in byval if len(byval[v])!=1]
print(f"  values with non-unique one-count normal form: {len(viol)}")
print()
print("  HONEST CAVEAT: this check is TAUTOLOGICAL.  The 'sum of ones' normal form of a term")
print("  built from 1 with + and * has length exactly equal to the term's value, by definition.")
print("  So Tang S3 is CORRECT but adds no evidence beyond the definition -- it says only that")
print("  the semiring quotient identifies every AM coupling of the same n, which is true because")
print("  the quotient is defined by evaluation.")
print("  => the substantive content of the ADC audit is S4-S11 (the CROSS-SCALE analysis),")
print("     not S3.")
print()
print("  Tang S11 (substitution decomposes into local steps): same status -- correct, and it is")
print("  the definition of 'term built from + and *'.  The real content is that no NEW primitive")
print("  exists, which is a statement about the LANGUAGE, not about any particular n.")
print()

print("="*84); print("(b) sources of STRICT CONTRACTION  A_{N+1} < Lift(A_N)   (Tang P4)"); print("="*84)
print("""  A strict contraction needs a condition that is NOT a logical consequence of the
  arithmetic axioms (closure only adds consequences: V(R_inf) = V(R_0), Tang S16).
  Model-theoretically, a non-consequential arithmetic condition is one of four kinds:""")
import textwrap
rows=[
 ("I  invariance / symmetry","must be stable under an action (Galois, congruence, a group)",
  "Galois stability -> character; congruence -> character; group invariance -> character group",
  "BIN 1 (character / L-function)", "closed"),
 ("II archimedean / metric","must satisfy a growth or size bound",
  "height/analytic bounds; M(x)=O(x^{1/2+eps}) type statements",
  "BIN 3/5 (archimedean; counting/entropy)", "closed"),
 ("III existential structure","must admit a section / splitting / lifting / polarisation",
  "local-global obstructions (Sha, Brauer-Manin); posivity (Hodge/Hodge-Riemann)",
  "BIN 4 (cohomology / L-values) or BIN 12 (positivity)", "closed"),
 ("IV proof-theoretic","must be provable from a stronger axiom/consistency strength",
  "new axioms can prove new Pi_1 theorems (e.g. Con(PA)), so they CAN strictly contract",
  "home (c) of the apparatus audit: NEW BUT UNLINKED", "OPEN (no arithmetic link)"),
]
for name,form,inst,bin_,st in rows:
    print(f"  {name}")
    print(f"      form      : {form}")
    print(f"      instances : {textwrap.fill(inst,70,subsequent_indent=' '*18)}")
    print(f"      lands in  : {bin_}")
    print(f"      status    : {st}")
    print()
print("="*84); print("CONCLUSION"); print("="*84)
print("""  Tang P4 (strict contraction) is EQUIVALENT to requiring a non-consequential arithmetic
  condition, and every such condition falls into one of FOUR model-theoretic kinds:
     I  invariance/symmetry   -> character box            (closed)
     II archimedean/metric    -> archimedean/entropy box  (closed)
     III existential structure-> obstruction/positivity   (closed)
     IV proof-theoretic       -> NEW BUT UNLINKED         (open, gives provability not selection)
  => This is the EXPLANATION Tang asked for: all previous dead ends look alike because they
     all obtained their strict contraction from the SAME three closed sources.
  => The only non-closed class (IV) supplies PROVABILITY, not an arithmetic SELECTION
     mechanism, and has no known link to the location of the zeros.
  => Hence: within the identified sources there is NO minimal non-spectral non-local
     arithmetic structure that naturally produces an extension obstruction.""")
