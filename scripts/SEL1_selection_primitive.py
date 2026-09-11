"""
SEL1: audit the selection primitive.
 (1) compute the Euclid-type process q(P) = min{prime q : q | N(P)+1}, state P -> P u {q}
 (2) decide precisely whether it CHANGES the allowed-action space (Tang S7's requirement)
Discipline: calibrate first; no 1/2 input; L2 untouched.
"""
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True

print("="*82); print("STEP 0 CALIBRATION"); print("="*82)
print(f"  isprime: 2={isprime(2)} 3={isprime(3)} 4={isprime(4)} 97={isprime(97)} 91={isprime(91)}")
print(f"  2*3*5 = {2*3*5}; N+1 = {2*3*5+1}; smallest prime factor = 31 (since 31*1... check: {2*3*5+1} = 31)")
assert isprime(2) and isprime(3) and not isprime(4) and isprime(97) and not isprime(91)
assert 2*3*5+1==31
print("  calibration OK")
print()

print("="*82); print("(1) the Euclid-type process: one deterministic orbit, no branching"); print("="*82)
P=[2]; print(f"  P_0 = {P}")
for step in range(1,8):   # capped: doubly-exponential growth
    N=1
    for p in P: N*=p
    m=N+1
    q=2
    while m%q!=0: q+=1
    P=P+[q]
    print(f"  step {step:>2}: N+1 = {m}   q = {q}   |P| = {len(P)}")
print()
print("  NOTE: capped at 8 steps.  Euclid-Mullin terms grow doubly-exponentially")
print("        (2,3,7,43,13,53,5,6221671,38709183810571,...), so deeper terms need")
print("        factoring of astronomically large N+1 -- not computable by trial division.")
print()
print("  OBSERVE: at every step the allowed next action is THE SAME action (append q),")
print("           and q is uniquely determined => the action space NEVER changes.")
print()

print("="*82); print("(2) Tang S7 requirement vs this example"); print("="*82)
print("""  Tang S7 requires:  (a,b,c) |-> A_{a,b,c}  = the set of ALLOWED next actions,
     and that this set CHANGES between steps.
  Euclid-type example: the allowed next action is always exactly one action, determined
     by a VALUE (the smallest prime factor of N+1).  So the action space is CONSTANT.
  => THE EUCLID EXAMPLE FAILS TANG'S OWN S7 REQUIREMENT.  It is an extremal SELECTOR,
     not a feasible-region-changing defect.""")
print()
print("="*82); print("(3) what a genuine S7-type dynamics would need, and why it is blocked"); print("="*82)
print("""  A feasible-region-changing dynamics must BRANCH: |A| > 1 at some steps, and the
     region must sometimes SHRINK (otherwise the process is monotone and has no boundary).
  Case i  : FINITE branching  -> Koenig (AEB1 Test D, 903/903) => every level realisable
            implies a global infinite thread => NO escape boundary exists.
  Case ii : INFINITE branching -> possible escape (AEB1 Test C: S_n={k>=n}), but any such
            escape requires non-compact stages, i.e. STAGES THAT ARE NOT DISCRETE.
            With discrete stages (finite or infinite), the limit is ZERO-DIMENSIONAL
            (AEB1 addendum): totally disconnected => NO connected 1-dimensional boundary.
  => In BOTH cases the SPECTRAL parameter cannot arise as a boundary coordinate.""")
print()
print("="*82); print("CONCLUSION"); print("="*82)
print("""  1. The selection half is REAL and the Euclid-type mechanism shows it: multiplicative
     state -> additive defect (+1) -> canonical extremal resolution (min) truly produces a
     canonical, element-level choice with no quotient/character/conjugacy.
  2. But that example does NOT change the allowed-action space: it is a deterministic
     selector, so it fails Tang S7 (and indeed his own S4 death audit: monotone growth,
     no spectral localisation).
  3. A genuine S7 dynamics must branch, and then AEB1 closes the spectral half:
     finite branching -> no escape; infinite branching -> escape possible but the limit is
     still totally disconnected, so no connected 1-D boundary.
     Hence: selection can be built; the SPECTRAL PARAMETER cannot be a boundary coordinate.
  4. This separates Tang's two problems cleanly and shows only the FIRST is (in principle)
     open.""")
