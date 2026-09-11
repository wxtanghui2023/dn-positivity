"""
PIE1: test the HYPOTHESES of Pierson's Theorem 1 (Polya 1927, as he states it) against
      the classical kernel Phi(u) = 4 sum_{n>=1} phi_n(u),
      phi_n = (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) exp(-pi n^2 e^{2u}).
Hypotheses (as stated):  (i) K>0 on ALL of R;  (ii) K even;  (iii) (log K)''<=0 on u>=0;
                         (iv) K = O(exp(-|t|^(2+delta))).
Calibration: int_0^inf Phi = xi(1/2) = 0.4971207782  (Pierson's own convention).
"""
from mpmath import mp, mpf, exp, pi, quad, nstr
mp.dps=40
def phi_std(u):
    u=mpf(u); s=mpf(0)
    for n in range(1,18):
        a=2*pi**2*mpf(n)**4*exp(mpf('4.5')*u) - 3*pi*mpf(n)**2*exp(mpf('2.5')*u)
        s+= a*exp(-pi*mpf(n)**2*exp(2*u))
    return 4*s
print("="*84); print("CALIBRATION:  int_0^inf Phi(u) du  vs  xi(1/2) = 0.4971207782"); print("="*84)
I=quad(phi_std,[0,mpf('1')])
print(f"  int_0^inf Phi = {nstr(I,14)}   [{'OK' if abs(I-mpf('0.4971207782'))<1e-9 else 'CHECK'}]")
print()
print("="*84); print("HYPOTHESIS (i): is Phi > 0 for ALL u (including u<0) ?"); print("="*84)
for u in ('-3','-2','-1','-0.5','0','0.5','1','2','3'):
    v=phi_std(u)
    print(f"  Phi({u:>5}) = {nstr(v,10):>18}   {'POSITIVE' if v>0 else 'NEGATIVE'}")
print()
print("="*84); print("HYPOTHESIS (ii): is Phi EVEN,  Phi(-u) = Phi(u) ?"); print("="*84)
for u in ('0.5','1','2'):
    a=phi_std(u); b=phi_std('-'+u)
    print(f"  u={u:>4}: Phi(u) = {nstr(a,10):>14}   Phi(-u) = {nstr(b,10):>14}   equal? {'YES' if a==b else 'NO'}")
print()
print("="*84); print("HYPOTHESIS (iii): (log Phi)'' < 0 on [0,inf) ?  (spot check)"); print("="*84)
def Q(u):
    h=mpf('1e-8'); u=mpf(u)
    f=phi_std(u); f1=(phi_std(u+h)-phi_std(u-h))/(2*h); f2=(phi_std(u+h)-2*f+phi_std(u-h))/(h*h)
    return f2*f-f1*f1
for u in ('0.1','0.5','1.0','1.5','2.0'):
    print(f"  Q_Phi({u:>4}) = {nstr(Q(u),8):>16}   {'log-concave (Q<0)' if Q(u)<0 else 'NOT log-concave'}")
print()
print("="*84); print("THE DILEMMA"); print("="*84)
print("""  If Phi means the classical series above, then (i) and (ii) FAIL (Phi is negative for
  u<0 and is not even) => Polya's stated hypotheses are not met => the proof does not close.
  If instead one replaces Phi by its EVEN EXTENSION Phi_e(u):=Phi(|u|), then (i) and (ii)
  hold by construction, (iii) holds by the proved log-concavity, and (iv) holds by the
  double-exponential decay => ALL FOUR hypotheses hold => Pierson's Theorem 1 would give RH.
  Since RH is open, the stated sufficiency of Theorem 1 cannot be correct as formulated:
  the passage log-concavity => real zeros requires a hypothesis beyond those four.""")
