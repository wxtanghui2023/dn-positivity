# c380_46_probe2.py -- feasibility structure probe (K=5 binding constraint + non-pairing coords)
import math, random
import numpy as np

def Qall(X, K=6):
    q = []
    X = np.asarray(X, dtype=float)
    for k in range(1, K + 1):
        q.append(float(np.sum(np.cos(k * np.arccos(np.clip(X, -1, 1))))))
    return q

def structure(X):
    X = np.asarray(X, dtype=float)
    m = X.mean()
    Y = X - m
    S1 = X.sum(); S2 = float((X**2).sum()); S3 = float((X**3).sum())
    P2 = float((Y**2).sum()); P3 = float((Y**3).sum())
    e4 = float(np.prod(Y))
    D4 = P2*P2/16.0 - e4
    return dict(m=m, S1=S1, S2=S2, S3=S3, P2=P2, P3=P3, e4=e4, D4=D4)

N = 4000000
rng = np.random.default_rng(3)
X = rng.uniform(-1, 1, size=(N, 4))
Tk = []
for k in range(1, 7):
    Tk.append(np.cos(k * np.arccos(np.clip(X, -1, 1))).sum(1))
Q = Tk
for K in (5, 6):
    M = np.maximum.reduce([Q[k] + 0.5 for k in range(K)])
    i = int(M.argmin())
    print("K=%d grid best minmax=%.6f  X=%s" % (K, M[i], ["%.6f" % z for z in X[i]]))
    print("    Q=", ["%.6f" % z for z in Qall(X[i], 6)], structure(X[i]))
    print("    argmax_k =", int(np.argmax([Q[k][i] + 0.5 for k in range(K)])) + 1)

# refined local search from best grid points (adaptive coordinate descent)
def obj(X, K):
    q = Qall(X, K)
    return max(q[k] + 0.5 for k in range(K)), q

best = None
for K in (5, 6):
    M = np.maximum.reduce([Q[k] + 0.5 for k in range(K)])
    starts = [X[i] for i in np.argsort(M)[:40]]
    bv = 1e9; bx = None
    for s in starts:
        Xc = np.array(s, dtype=float); v, q = obj(Xc, K); step = 0.05
        for it in range(4000):
            i = it % 4
            old = Xc[i]
            Xc[i] = min(1.0, max(-1.0, old + step))
            nv, nq = obj(Xc, K)
            if nv < v: v, q = nv, nq
            else:
                Xc[i] = min(1.0, max(-1.0, old - step))
                nv, nq = obj(Xc, K)
                if nv < v: v, q = nv, nq
                else: Xc[i] = old
            if it % 200 == 199: step *= 0.6
    #
        if v < bv: bv, bx = v, Xc.copy()
    print("K=%d refined minmax=%.8f  X=%s" % (K, bv, ["%.8f" % z for z in bx]))
    print("    Q=", ["%.8f" % z for z in Qall(bx, 6)], structure(bx))
    print("    argmax_k =", int(np.argmax([Qall(bx, 6)[k] + 0.5 for k in range(K)])) + 1)

# affine LP relaxation at the K=5 best structure: solve Q3=-1/2, Q4=-1/2 in (P3,D4), read Q5
print("== affine LP relaxation at refined K=5 point ==")
