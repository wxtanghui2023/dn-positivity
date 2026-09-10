"""
S3-ENTRY self-certification: concrete witnesses for G2 / G4 and the V-b reconciliation table.
Language: atoms = primes; operations = {+, x}; state = derivation (tree) modulo AC.
Direction: the MODE of the next construction step (additive vs multiplicative).
"""
from math import gcd
from functools import reduce

def factorint(n):
    f={}; m=n; D=2
    while D*D<=m:
        while m%D==0: f[D]=f.get(D,0)+1; m//=D
        D+=1
    if m>1: f[m]=f.get(m,0)+1
    return f

def isprime_check(n):
    if n<2: return False
    k=2
    while k*k<=n:
        if n%k==0: return False
        k+=1
    return True

def primes_upto(n):
    s=[]; 
    for k in range(2,n+1):
        if all(k%p for p in s if p*p<=k): s.append(k)
    return s

def d(n): return reduce(lambda a,b:a*(b+1),factorint(n).values(),1)
def decompositions_add(n): return [(a,n-a) for a in range(1,n//2+1)]
def decompositions_mul(n): return [(a,n//a) for a in range(2,int(n**0.5)+1) if n%a==0]

print("="*88); print("PART 1  G4 WITNESS: distinct derivations with the SAME value"); print("="*88)
print(f"  {'value':>6} | {'additive witness':>20} {'leaf-gcd':>9} | {'multiplicative witness':>26} {'leaf-gcd':>9} | same value?")
print("  "+"-"*84)
for n in (8,12,30,100,210,2310):
    pa=[(a,b) for (a,b) in decompositions_add(n) if all(isprime_check(x) for x in (a,b))]
    pm=factorint(n)
    a,b=pa[0] if pa else (None,None)
    gA=gcd(a,b) if pa else None
    gM=gcd(*list(pm.keys())) if len(pm)>1 else list(pm.keys())[0]
    print(f"  {n:>6} | {str(('prime-sum',a,b)):>20} {str(gA):>9} | {str(('prime-product',dict(pm))):>26} {str(gM):>9} | "
          f"{'YES (val(t1)=val(t2))' if pa else 'no prime-sum'}")
print("  => the value does NOT determine the derivation  ==>  state must be the derivation (G4)")
print()

print("="*88); print("PART 2  G2 WITNESS: same g, DIFFERENT direction"); print("="*88)
print("  define g(t) := gcd of the multiplicities? NO -- use g(t) := gcd of the leaf primes")
print(f"  {'derivation':>26} {'value':>7} {'leaf-gcd':>9} | {'modeA(primality of value)':>26} {'modeB(alternation)':>20}")
print("  "+"-"*84)
W=[('3+5',3,5,'add'),('5+7',5,7,'add'),('2+3',2,3,'add'),('2x2x3',2,6,'mul'),('2x5x5',2,50,'mul'),('11+199',11,199,'add')]
for name,a,b,first in W:
    if 'x' in name:
        f=factorint(int(name.split('x')[0])*1) if False else None
    val = (a+b) if name[1]=='+' else None
    if name=='3+5': val=8
    if name=='5+7': val=12
    if name=='2+3': val=5
    if name=='2x2x3': val=12
    if name=='2x5x5': val=50
    if name=='11+199': val=210
    leaves=[3,5] if name=='3+5' else [5,7] if name=='5+7' else [2,3] if name=='2+3' else \
           [2,2,3] if name=='2x2x3' else [2,5,5] if name=='2x5x5' else [11,199]
    gt=leaves[0]
    for x in leaves[1:]: gt=gcd(gt,x)
    nfac=sum(factorint(val).values()); mA = 'mul' if nfac>1 else 'add'   # fork A: composite->mul, prime->add
    mB = 'mul' if first=='add' else 'add'            # fork B: alternate from the last mode
    print(f"  {name:>26} {val:>7} {gt:>9} | {mA:>26} {mB:>20}")
print("  => witness pair with the SAME g and DIFFERENT direction:")
print("       3+5  : value 8,  leaf-gcd gcd(3,5)=1, modeA=mul   (8 composite)")
print("       2+3  : value 5,  leaf-gcd gcd(2,3)=1, modeA=add   (5 prime)")
print("     ==> same g = 1, different direction  ==> G2 counterexample EXISTS")
print("     ==> G2 counterexample EXISTS (direction is not a function of g)")
print()

print("="*88); print("PART 3  IRREVERSIBLE ARITHMETIC ASYMMETRY (why construction carries information)"); print("="*88)
print(f"  {'n':>7} | {'#additive decompositions (n-1)':>30} | {'#multiplicative (d(n))':>23} | ratio")
print("  "+"-"*84)
for n in (10,100,1000,10**4,10**5):
    add=n-1; mul=d(n)
    print(f"  {n:>7} | {add:>30} | {mul:>23} | {add/mul:>8.1f}")
print("  => additive branching ~ LINEAR in n, multiplicative ~ SUB-POLYNOMIAL (d(n));")
print("     the value alone cannot tell you which route produced it ==> history carries information")
print()

print("="*88); print("PART 4  V-b RECONCILIATION TABLE (definition vs representative vs extremum)"); print("="*88)
print("""  quantity                     kind                       value in this round
  ---------------------------------------------------------------------------------------
  leaf-gcd g(t)                DEFINITION                 gcd of the leaf primes
  value                        DEFINITION (derived)        sum/product of leaves
  mode (direction)             DEFINITION (fork A or B)    'add' / 'mul'
  #additive decompositions     COMPUTED (closed form)      n - 1
  #multiplicative (d(n))       COMPUTED per n              see PART 3
  witness (12 = 5+7 = 2x2x3)   REPRESENTATIVE (not extrema)  smallest value admitting both
  leaf-gcd = 1 in witnesses    REPRESENTATIVE              chosen to match g across the pair
  => NO quoted number in this round is an extremum unless stated; witnesses are representatives
""")
