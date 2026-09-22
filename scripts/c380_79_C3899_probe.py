# c380_79_C3899_probe.py -- C-3899 phase A: five-node active-set rebuild + z-census at known candidates
# model (ground truth from c380_61/62): phi in (0,pi/2)^5 ; x = cos^2 phi ; u = 2x-1 = cos 2phi
#   even layer: F_{4q}(c) = sum_j cos(4q phi_j) = sum_j T_{2q}(u_j) <= 1/2 , q = 1..12
#   odd layer : F_{2r+1}(c) = sum_j sigma_j cos((2r+1) phi_j) , r = 0..12
import numpy as np
HALF = np.pi/2
def Fe(phi, q): return float(np.sum(np.cos(4*q*phi)))            # = F_{4q} in c-coords = sum T_{2q}(u)
def Fo(phi, s, r): return float(np.sum(s*np.cos((2*r+1)*phi)))   # = F_{2r+1} (signed nodes)

def report(phi, s, tag):
    u = np.cos(2*phi); x = np.cos(phi)**2; z = u**2
    ev = np.array([Fe(phi,q) for q in range(1,13)])
    marg = 0.5 - ev
    ov = np.array([Fo(phi,s,r) for r in range(13)])
    t = np.abs(ov).max()
    print("--- %s ---" % tag, flush=True)
    print("  phi/pi   = %s" % np.round(phi/np.pi, 10), flush=True)
    print("  x        = %s" % np.round(x, 12), flush=True)
    print("  u=cos2phi= %s" % np.round(u, 12), flush=True)
    print("  z=u^2    = %s" % np.round(z, 12), flush=True)
    zs = np.sort(z)
    # distinct count with relative tolerance sweep
    for tol in (1e-6, 1e-9, 1e-12):
        d = []
        for v in zs:
            if not d or abs(v-d[-1]) > tol*max(1.0, abs(v)): d.append(v)
        print("  k(tol=%.0e) = %d   distinct z = %s" % (tol, len(d), np.round(np.array(d), 9)), flush=True)
    print("  u<0 index? %s ; x in (0,1)? %s" % (list(np.where(u < 0)[0]), bool(((x>0)&(x<1)).all())), flush=True)
    print("  pairwise |u_i +- u_j| min = %.3e" % min(min(abs(u[i]-u[j]), abs(u[i]+u[j])) for i in range(5) for j in range(i+1,5)), flush=True)
    for tol in (1e-7, 1e-9, 1e-11):
        A = [q for q in range(1,13) if abs(marg[q-1]) <= tol]
        I = [r for r in range(13) if abs(abs(ov[r]) - t) <= tol]
        print("  tol=%.0e : active even A=%s ; tied odd I=%s (|I|=%d)" % (tol, A, I, len(I)), flush=True)
    print("  even margins (0.5-F_4q): %s" % np.round(marg, 8), flush=True)
    print("  odd values F_{2r+1}: %s" % np.round(ov, 8), flush=True)
    print("  min inactive margin = %.3e ; t = %.12f" % (min(marg[q-1] for q in range(1,13) if q not in [3,4,7,9]), t), flush=True)
    return u, z

S_WIN = np.array([-1.,1.,1.,-1.,1.])
cands = {
 'C-3861/C-3862 KKT winner': (np.array([0.80093022,0.5611432,0.70245716,0.6261014,0.86884389]), S_WIN),
 'C-3850 seed':              (np.array([0.801874,0.561119,0.703473,0.627211,0.869546]), S_WIN),
 'C-3855 seed':              (np.array([0.702989,0.873806,0.797976,0.551115,0.628434]), S_WIN),
}
print("=== PHASE A: five-node active-set rebuild + z-census at the archive candidates ===", flush=True)
for tag,(xs,s) in cands.items():
    report(np.arccos(np.sqrt(xs)), s, tag)

print("\n=== PHASE A2: probe the four-node two-level point (m,a)=(-1/8, 3sqrt3/8) ===", flush=True)
m = -1.0/8.0; a = 3*np.sqrt(3)/8.0
u4 = np.array([m+a, m+a, m-a, m-a])
print("  u = %s ; z = %s ; k = %d" % (np.round(u4,10), np.round(u4**2,10), len(set(np.round(u4**2,12)))), flush=True)
def Tm(k, u): return np.cos(k*np.arccos(np.clip(u,-1,1)))
for lab, uu in (('4-node two-level (m+-a)x2', u4),):
    F = [float(np.sum([Tm(2*q, v) for v in uu])) for q in range(1,13)]
    print("  %s : sum T_2q (q=1..12) = %s" % (lab, np.round(F,6)), flush=True)
    F4 = [float(np.sum([Tm(4*q, v) for v in uu])) for q in range(1,13)]
    print("  %s : sum T_4q (q=1..12) = %s" % (lab, np.round(F4,6)), flush=True)
print("\nDONE-PHASE-A", flush=True)
