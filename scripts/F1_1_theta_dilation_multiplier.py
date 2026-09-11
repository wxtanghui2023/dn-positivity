"""
F1-1: anchor the claim that char 0 DOES possess a canonical GLOBAL dilation with a
      non-trivial modulus -- namely the theta involution  t -> 1/t  with multiplier sqrt(t).
      This matters because it decides whether 'missing element with modulus' is the gap.
Discipline: calibrate; no 1/2 input; L2 untouched.
"""
import math
PI=math.pi
def theta(t, N=60):
    return 1.0 + 2.0*sum(math.exp(-PI*n*n*t) for n in range(1,N+1))
print("="*80); print("(1) theta involution   theta(1/t) = sqrt(t) * theta(t) ?"); print("="*80)
print(f"  {'t':>10} | {'theta(t)':>14} | {'theta(1/t)':>14} | {'ratio':>12} | {'sqrt(t)':>12}")
for t in (0.05,0.2,0.5,1.0,2.0,5.0,20.0):
    a=theta(t); b=theta(1.0/t)
    print(f"  {t:>10.2f} | {a:>14.8f} | {b:>14.8f} | {b/a:>12.8f} | {math.sqrt(t):>12.8f}")
print("  => the multiplier is EXACTLY sqrt(t).  This is the canonical GLOBAL dilation of char 0.")
print()
print("="*80); print("(2) how this multiplier becomes the functional equation"); print("="*80)
print("""  Lambda(s) = pi^{-s/2} Gamma(s/2) zeta(s) = (1/2) int_0^inf (theta(t)-1) t^{s/2-1} dt
  splitting the integral at t=1 and using theta(1/t) = sqrt(t) theta(t) gives directly
        Lambda(s) = Lambda(1-s).
  => the s <-> 1-s symmetry (and hence the '1/2') is MANUFACTURED by the sqrt(t) multiplier.
  So char 0 is NOT missing 'a canonical dilation with a modulus': it has one, canonically.""")
print()
print("="*80); print("(3) so is that enough?  the functional equation alone:"); print("="*80)
print("""  * is a REFLECTION symmetry (pairs s with 1-s) and therefore transports NO information
    about WHERE the zeros are -- it is satisfied by any zero configuration invariant under it;
  * has classical counterexamples with off-line zeros:  zeta functions of definite/indefinite
    binary quadratic forms (Epstein zeta functions) satisfy a functional equation yet have
    zeros off the critical line.   [CITED, not re-verified here]
  => a canonical dilation with modulus sqrt(t) EXISTS and is PROVABLY INSUFFICIENT.
  => therefore 'the gap is a missing canonical element/modulus' is FALSE.
     What is missing is POSITIVITY (of the quadratic form whose symmetry that involution is).""")
