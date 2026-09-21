# c380_53_knife3_proof.py -- verify the knife-3 chain exactly (sympy) + numerical sanity
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

e2, e3, t = sp.symbols('e2 e3 t')
e1 = sp.Integer(1)
p = {1: e1}
p[2] = sp.expand(e1*p[1] - 2*e2)
p[3] = sp.expand(e1*p[2] - e2*p[1] + 3*e3)
for k in range(4, 8):
    p[k] = sp.expand(e1*p[k-1] - e2*p[k-2] + e3*p[k-3])
e1B = p[1]; e2B = sp.simplify((p[1]**3 - p[3])/(3*p[1]))
q = {1: e1B, 2: sp.expand(e1B*e1B - 2*e2B)}
for k in range(3, 8):
    q[k] = sp.expand(e1B*q[k-1] - e2B*q[k-2])
E1 = sp.expand(p[5] - q[5]); E2 = sp.expand(p[7] - q[7])

print("=== step 1: factor the two conditions ===", flush=True)
print("   E1 =", sp.factor(E1), flush=True)
print("   E2 =", sp.factor(E2), flush=True)

print()
print("=== step 2: the e3 != 0 branch forces e2 = e3 ===", flush=True)
A1 = sp.factor(sp.simplify(E1 / e3))            # E1 = 5*e3*(...)
print("   E1 / e3 =", A1, flush=True)
E2_at_e2e3 = sp.factor(sp.simplify(E2.subs(e2, e3)))
print("   E2 with e2 = e3 :", E2_at_e2e3, "  (identically zero?)", E2_at_e2e3 == 0, flush=True)

print()
print("=== step 3: A-polynomial on that branch ===", flush=True)
PA = sp.expand(t**3 - e1*t**2 + e2*t - e3).subs({e2: t, e3: t})
print("   P_A(x) = x^3 - x^2 + t x - t  =", sp.factor(PA), flush=True)
print("   check (x-1)(x^2+t) =", sp.expand((t-1)*(t**2+t)), "-- symbolic:", sp.simplify(sp.expand(PA - (t-1)*(t**2+t))) == 0, flush=True)
disc = sp.factor(sp.discriminant(PA, t))
print("   discriminant of P_A in x:", sp.factor(sp.discriminant(sp.Poly(PA, t), t)), flush=True)
roots = sp.solve(sp.Eq(PA, 0), t)
print("   roots:", roots, flush=True)

print()
print("=== step 4: numerical confirmation that the cube has <=1 real root for t>0 ===", flush=True)
for tv in (0.05, 0.3, 1.0, 3.0, 7.0):
    rts = mp.polyroots([1, -1, tv, -tv], maxsteps=200, extraprec=200)
    real = [z for z in rts if abs(mp.im(z)) < mp.mpf('1e-25')]
    print("   t=%.2f : roots = %s ; #real = %d" % (tv, [mp.nstr(z, 8) for z in rts], len(real)), flush=True)
for tv in (-0.3, -1.0):
    rts = mp.polyroots([1, -1, tv, -tv], maxsteps=200, extraprec=200)
    real = [z for z in rts if abs(mp.im(z)) < mp.mpf('1e-25')]
    print("   t=%.2f : roots = %s ; #real = %d" % (tv, [mp.nstr(z, 8) for z in rts], len(real)), flush=True)
print()
print("NOTE: e3 = abc > 0 whenever a,b,c > 0, so t = e3 > 0 is forced in the regular layer.", flush=True)
print("DONE", flush=True)
