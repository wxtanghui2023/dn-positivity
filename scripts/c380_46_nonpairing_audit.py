# c380_46_nonpairing_audit.py
# 目的：(1) 核验非配对模态的精确仿射分解；(2) 五/六约束可行性数值探针
# 仅用于回测研究/审计核验，不构成本结论的证据；纯数值
import math, random, sys

def T(k, x):
    if k == 0: return 1.0
    a, b = 1.0, x
    for _ in range(2, k + 1):
        a, b = b, 2 * x * b - a
    return b

def Qall(X, K=6):
    return [sum(T(k, x) for x in X) for k in range(1, K + 1)]

def twolevel_archive(m, a):
    s = m * m + a * a
    return [4 * m,
            8 * s - 4,
            4 * m * (12 * s - 8 * m * m - 3),
            4 * (-32 * m**4 + 32 * m * m * s + 8 * s * s - 8 * s + 1),
            4 * m * (-64 * m**4 + 40 * m * m + 80 * s * s - 60 * s + 5)]

def moments(X):
    S1 = sum(X); S2 = sum(x * x for x in X); S3 = sum(x**3 for x in X)
    m = S1 / 4.0
    P2 = S2 - 4 * m * m
    P3 = sum((x - m)**3 for x in X)
    e4 = 1.0
    for x in X: e4 *= (x - m)
    D4 = P2 * P2 / 16.0 - e4
    return m, P2, P3, D4

def affine_ref(m, P2, P3, D4):
    q3 = 16 * m**3 + 12 * m * P2 - 12 * m
    q4 = 32 * m**4 + 48 * m * m * P2 + 2 * P2 * P2 - 32 * m * m - 8 * P2 + 4
    q5 = 64 * m**5 + 160 * m**3 * P2 + 20 * m * P2 * P2 - 80 * m**3 - 60 * m * P2 + 20 * m
    return [q3 + 4 * P3,
            q4 + 32 * m * P3 + 32 * D4,
            q5 + (160 * m * m - 20 + (40.0 / 3.0) * P2) * P3 + 320 * m * D4]

print("== A. convention check: sum T_k(X_j) vs archive two-level formulas ==")
for (m, a) in [(-0.25, 0.5592), (-1.0/8.0, 3.0 * math.sqrt(3.0) / 8.0)]:
    X = [m + a, m + a, m - a, m - a]
    q = Qall(X, 5); qa = twolevel_archive(m, a)
    print("  m=%.6f a=%.6f  maxdiff=%.3e" % (m, a, max(abs(q[i] - qa[i]) for i in range(5))),
          " Q5=%.12f" % q[4], " 341/128=%.12f" % (341.0 / 128.0))

print("== B. affine decomposition residual (random tuples) ==")
random.seed(7)
mx = [0.0, 0.0, 0.0]
for _ in range(200000):
    X = [random.uniform(-1, 1) for _ in range(4)]
    m, P2, P3, D4 = moments(X)
    q = Qall(X, 6)
    r = affine_ref(m, P2, P3, D4)
    for i in range(3):
        mx[i] = max(mx[i], abs(q[2 + i] - r[i]))
print("  max residual Q3,Q4,Q5 = %.3e %.3e %.3e" % tuple(mx))

print("== C. family Y=(b,c,-c,-b), m=-1/8, P2=27/16 (P3=P5=0) ==")
m = -1.0 / 8.0
a2 = 27.0 / 64.0
for r in [1.0, 0.95, 0.9, 0.8]:
    b = math.sqrt(a2 * 2 * r / (1 + r)) 
    c = math.sqrt(2 * a2 - b * b)
    X = [m + b, m + c, m - c, m - b]
    q = Qall(X, 6)
    mm, P2, P3, D4 = moments(X)
    print("  b=%.6f c=%.6f  D4=%.6e  Q5=%.10f  pred(341/128+320*m*D4)=%.10f  err=%.2e  Q3=%.6f Q4=%.6f Q6=%.6f"
          % (b, c, D4, q[4], 341.0 / 128.0 + 320 * m * D4, abs(q[4] - (341.0 / 128.0 + 320 * m * D4)), q[2], q[3], q[5]))

print("== D. feasibility probe: min over samples of max_{k<=K}(Q_k+0.5) ==")
try:
    import numpy as np
    N = 3000000
    X = np.random.uniform(-1, 1, size=(N, 4))
    T1 = X; T2 = 2 * X**2 - 1; T3 = 4 * X**3 - 3 * X; T4 = 8 * X**4 - 8 * X**2 + 1
    T5 = 16 * X**5 - 20 * X**3 + 5 * X; T6 = 32 * X**6 - 48 * X**4 + 18 * X**2 - 1
    Q = [X.sum(1), T2.sum(1), T3.sum(1), T4.sum(1), T5.sum(1), T6.sum(1)]
    for K in (4, 5, 6):
        M = np.maximum.reduce([Q[k] + 0.5 for k in range(K)])
        print("  K=%d  min max = %.6f   feasible frac = %.3e" % (K, M.min(), float((M <= 0).mean())))
except Exception as e:
    print("  numpy unavailable:", e)

print("== E. hill-climb probe (min max_{k<=5}, k<=6) ==")
def obj(X, K):
    q = Qall(X, K)
    return max(q[k] + 0.5 for k in range(K)), q
best = {}
random.seed(11)
for K in (5, 6):
    bv = 1e9; bx = None
    for _ in range(400):
        X = [random.uniform(-1, 1) for _ in range(4)]
        v, q = obj(X, K); step = 0.5
        for _ in range(600):
            i = random.randrange(4)
            d = random.uniform(-step, step)
            X[i] = min(1.0, max(-1.0, X[i] + d))
            nv, nq = obj(X, K)
            if nv < v: v, q = nv, nq
            else: X[i] = min(1.0, max(-1.0, X[i] - d))
            step *= 0.996
        if v < bv: bv, bx = v, list(X)
    best[K] = (bv, bx)
    print("  K=%d  best min max = %.6f  X=%s" % (K, bv, ["%.6f" % z for z in bx]))
    print("        Q =", ["%.6f" % z for z in Qall(bx, 6)])
