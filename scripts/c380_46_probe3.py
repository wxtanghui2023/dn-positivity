import math
# c380_46_probe3.py -- high-precision boundary probe for the general four-node problem
# Q_k = sum_j cos(k theta_j); constraint Q_k <= -1/2  (k = 1..6)
import mpmath as mp
mp.mp.dps = 60

def Qv(th, k):
    return sum(mp.cos(k * t) for t in th)

def Qs(th):
    return [Qv(th, k) for k in range(1, 7)]

def newton(th0, active, iters=80):
    th = [mp.mpf(x) for x in th0]
    h = mp.mpf('1e-30')
    for it in range(iters):
        F = [Qv(th, k) + mp.mpf(1) / 2 for k in active]
        if max(abs(f) for f in F) < mp.mpf('1e-50'):
            break
        J = mp.matrix(len(active), 4)
        for i, k in enumerate(active):
            for j in range(4):
                t2 = list(th); t2[j] += h
                J[i, j] = (Qv(t2, k) - Qv(th, k)) / h
        b = mp.matrix([-f for f in F])
        try:
            dx = mp.lu_solve(J, b)
        except Exception:
            return None
        for j in range(4):
            th[j] += dx[j]
    return th

sets = {
    'S1234': [1, 2, 3, 4],
    'S2345': [2, 3, 4, 5],
    'S3456': [3, 4, 5, 6],
    'S1256': [1, 2, 5, 6],
    'S1345': [1, 3, 4, 5],
    'S2456': [2, 4, 5, 6],
}
seeds = []
# seed A: the refined numeric boundary point (K=5), seed B: (K=6), plus random
seeds.append([mp.acos(mp.mpf('-0.99421486')), mp.acos(mp.mpf('0.40409614')), mp.acos(mp.mpf('-0.49999660')), mp.acos(mp.mpf('0.59012116'))])
seeds.append([mp.acos(mp.mpf('-0.50256607')), mp.acos(mp.mpf('-0.94009334')), mp.acos(mp.mpf('0.17031966')), mp.acos(mp.mpf('0.76462431'))])
seeds.append([mp.acos(mp.mpf('-0.502692')), mp.acos(mp.mpf('0.753567')), mp.acos(mp.mpf('-0.940939')), mp.acos(mp.mpf('0.165387'))])
import random
random.seed(5)
for _ in range(60):
    seeds.append([mp.mpf(str(random.uniform(0.1, math.pi - 0.1))) if False else mp.mpf(str(random.uniform(0.1, 3.04))) for _ in range(4)])

def verdict(th):
    q = Qs(th)
    m = max(q[k] + mp.mpf(1) / 2 for k in range(6))
    return q, m

best = None
for nm, act in sets.items():
    bb = None
    for s in seeds:
        th = newton(s, act)
        if th is None: continue
        q, m = verdict(th)
        if bb is None or m < bb[1]:
            bb = (q, m, th)
    if bb:
        print("active=%-6s  max(Q+1/2)=%s" % (nm, mp.nstr(bb[1], 12)))
        print("        Q =", [mp.nstr(z, 12) for z in bb[0]])
        if best is None or bb[1] < best[1]:
            best = bb
        if bb[1] <= 0:
            print("        *** FEASIBLE (all six <= -1/2) ***")
print()
print("BEST overall: max(Q+1/2) =", mp.nstr(best[1], 20))
print("  Q =", [mp.nstr(z, 20) for z in best[0]])
print("  theta =", [mp.nstr(z, 20) for z in best[2]])
print("  X = cos(theta) =", [mp.nstr(mp.cos(z), 20) for z in best[2]])
print("  FEASIBLE?", best[1] <= 0)
