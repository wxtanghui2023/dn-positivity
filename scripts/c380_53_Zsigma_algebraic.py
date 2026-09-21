# c380_53_Zsigma_algebraic.py -- C3853 knives 1-3: algebraic classification of Z_sigma (3+2 split)
# normalisation: e1 = a+b+c = 1 (homogeneity). Conditions p_k(A) = p_k(B), k=1,3,5,7.
import sympy as sp

e2, e3 = sp.symbols('e2 e3')
e1 = sp.Integer(1)
p = {}
p[1] = e1
p[2] = e1*p[1] - 2*e2
p[3] = e1*p[2] - e2*p[1] + 3*e3
for k in range(4, 8):
    p[k] = sp.expand(e1*p[k-1] - e2*p[k-2] + e3*p[k-3])
print("=== knife 2: Newton power sums of A (e1=1) ===", flush=True)
for k in (1, 3, 5, 7):
    print("   p_%d = %s" % (k, sp.factor(p[k])), flush=True)

# B: the pair determined by (p_1, p_3): e1B = p1, e2B = (p1^3 - p3)/(3 p1)
e1B = p[1]
e2B = sp.simplify((p[1]**3 - p[3]) / (3*p[1]))
q = {1: e1B, 2: sp.expand(e1B*e1B - 2*e2B)}
for k in range(3, 8):
    q[k] = sp.expand(e1B*q[k-1] - e2B*q[k-2])
print("\n=== B (pair): e1B = %s ; e2B = %s ===" % (e1B, sp.simplify(e2B)), flush=True)

E1 = sp.expand(p[5] - q[5])
E2 = sp.expand(p[7] - q[7])
print("\n=== knife 3: the two polynomial conditions ===", flush=True)
print("   E1 (degree %s in e2/e3) = %s" % (sp.degree(E1, e2), E1), flush=True)
print("   E2 (degree %s) = %s" % (sp.degree(E2, e2), E2), flush=True)

R = sp.factor(sp.resultant(sp.Poly(E1, e3), sp.Poly(E2, e3)))
print("\n=== resultant (eliminating e3) ===", flush=True)
print("   R(e2) =", R, flush=True)
print("   factor:", sp.factor(sp.simplify(R)), flush=True)
