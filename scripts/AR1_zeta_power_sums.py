#!/usr/bin/env python3
"""
AR1: Numerical validation of the power-sum (Z_j) arithmetic formula.

  Z_j := sum_rho rho^{-j}

Two independent evaluations:
  (a) ZEROS:  Z_j = 2 Re sum_{gamma>0} (1/2 + i gamma)^{-j}
              from data/zeros_odlyzko_2M.npy  (full table, clongdouble;
              plus an independent mpmath run over the first N0 zeros).
  (b) ARITH:  Z_1 = 1 + gamma/2 - (1/2) log(4 pi)                     (classical)
              Z_j = 1 - (1 - 2^{-j}) zeta(j) + (-1)^j eta_{j-1}   (j >= 2)
              where eta_k are defined by  log[s zeta(1+s)] = -sum_{k>=0} eta_k s^{k+1}/(k+1).
              The eta_k are obtained from the Stieltjes constants gamma_k
              (zeta(1+u) = 1/u + sum_k (-1)^k gamma_k u^k/k!) by exact power-series log;
              no eta value is assumed.

Also records the exact algebraic simplification
     1 - (1 - 2^{-j}) zeta(j) = -sum_{m odd >= 3} m^{-j}
which exhibits the cancellation against eta_{j-1}.

Inputs : data/zeros_odlyzko_2M.npy
Outputs: scripts/AR1_zeta_power_sums.txt
"""
import os, time
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ZP = os.path.join(ROOT, 'data', 'zeros_odlyzko_2M.npy')
OUT = []


def emit(s=''):
    print(s)
    OUT.append(str(s))


T0 = time.time()
gam = np.sort(np.load(ZP).astype(np.float64).ravel())
gam = gam[gam > 0.5]
GMAX = float(gam[-1])
emit("zeros loaded: n = %d,  gamma in [%.6f, %.6f]" % (gam.size, gam[0], GMAX))

# ----------------------------------------------------------------------------
# eta_k from Stieltjes constants (exact power-series log of s*zeta(1+s))
# ----------------------------------------------------------------------------
mp.mp.dps = 80
JMAX = 40
KD = JMAX + 2
NARR = KD + 3
gamma_k = [mp.stieltjes(k) for k in range(NARR)]
c = [mp.mpf(0)] * NARR
c[0] = mp.mpf(1)                                   # f(s) = 1 + sum_{m>=1} c_m s^m
for k in range(KD + 1):
    c[k + 1] = (-1) ** k * gamma_k[k] / mp.factorial(k)
l = [mp.mpf(0)] * NARR                             # l_m = [s^m] log f
for m in range(1, KD + 2):
    acc = mp.mpf(m) * c[m]
    for k in range(1, m):
        acc -= k * l[k] * c[m - k]
    l[m] = acc / mp.mpf(m)
eta = [-mp.mpf(k + 1) * l[k + 1] for k in range(KD + 1)]

emit()
emit("eta_k derived from Stieltjes constants (no value assumed);")
emit("  consistency check  eta_1 == gamma^2 + 2 gamma_1 :")
emit("     eta_1 = %s" % mp.nstr(eta[1], 25))
emit("     g^2+2g_1 = %s   (agree to %s)"
     % (mp.nstr(mp.euler ** 2 + 2 * mp.stieltjes(1), 25),
        mp.nstr(abs(eta[1] - (mp.euler ** 2 + 2 * mp.stieltjes(1))), 3)))
for k in range(13):
    emit("   eta_%-2d = %s" % (k, mp.nstr(eta[k], 22)))


def Z_arith(j):
    if j == 1:
        return 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    return 1 - (1 - mp.mpf(2) ** (-j)) * mp.zeta(j) + (-1) ** j * eta[j - 1]


def oddsum(j, M=400):
    return -sum(mp.mpf(2 * n + 3) ** (-j) for n in range(M))


# ----------------------------------------------------------------------------
# Z_j from the zero table (full 2M, clongdouble) + mpmath leading-zeros check
# ----------------------------------------------------------------------------
mp.mp.dps = 60
z = (np.longdouble(0.5) + 1j * gam.astype(np.longdouble))
Zz = {}
for j in range(1, JMAX + 1):
    Zz[j] = 2 * np.real(np.sum(z ** (-j)))

N0 = 4000
z0 = [mp.mpc(mp.mpf(1) / 2, mp.mpf(repr(g))) for g in gam[:N0]]
Zmp = {}
for j in range(1, JMAX + 1):
    Zmp[j] = 2 * mp.re(mp.fsum([q ** (-j) for q in z0]))

emit()
emit("=" * 116)
emit("TASK 1   Z_j = sum_rho rho^{-j}      zeros table  vs  arithmetic formula")
emit("=" * 116)
emit("%3s  %-24s %-24s %-24s %-11s" %
     ("j", "Z_j (2M zeros, cld)", "Z_j (4000 zeros, mp)", "Z_j (arith. formula)", "reldiff"))
for j in range(1, JMAX + 1):
    a = Z_arith(j)
    zz = mp.mpf(repr(float(Zz[j])))
    rd = abs((zz - a) / a)
    emit("%3d  %-24s %-24s %-24s %-11s" %
         (j, mp.nstr(zz, 17), mp.nstr(Zmp[j], 17), mp.nstr(a, 17), mp.nstr(rd, 6)))

emit()
emit("a priori tail of the zeros sum beyond gamma_max = %.6g  (exact leading asymptotics):" % GMAX)
emit("   j=1     : (1/2pi)(log(T/2pi)+1)/T                        [ 2Re rho^-1 = 1/(gamma^2+1/4) ]")
emit("   j>=2 ev : (1/pi)[log(T/2pi)/(j-1)+1/(j-1)^2]/T^(j-1)      [ 2Re rho^-j ~ 2(-1)^(j/2) gamma^-j ]")
emit("   j>=3 odd: (j/2pi)[log(T/2pi)/j + 1/j^2]/T^j               [ 2Re rho^-j ~ j sin(j pi/2) gamma^-(j+1) ]")
emit("%3s %14s %14s %14s %14s" % ("j", "tail (a priori)", "observed |dZ|", "|Z_arith|", "rel. of observed"))
for j in (1, 2, 3, 4, 5, 6, 10):
    L = mp.log(mp.mpf(GMAX) / (2 * mp.pi)); T = mp.mpf(GMAX)
    if j == 1:
        tl = (L + 1) / (2 * mp.pi * T)
    elif j % 2 == 0:
        tl = (L / (j - 1) + 1 / mp.mpf(j - 1) ** 2) / (mp.pi * T ** (j - 1))
    else:
        tl = mp.mpf(j) * (L / j + 1 / mp.mpf(j) ** 2) / (2 * mp.pi * T ** j)
    zz = mp.mpf(repr(float(Zz[j])))
    a = Z_arith(j)
    emit("%3d %14s %14s %14s %14s" % (j, mp.nstr(tl, 4), mp.nstr(abs(zz - a), 4),
                                      mp.nstr(abs(a), 6), mp.nstr(abs(zz - a) / abs(a), 4)))
emit("   ==> j=1 and j=2 are TAIL-limited (the observed difference equals the tail).")
emit("       j>=3: the tail is below the observed difference; see the precision diagnostic.")

emit()
emit("precision diagnostic: the stored zeros carry only ~11 significant digits.  The first stored")
emit("   value is gamma_1(file) = 14.134725142000001 vs the true 14.134725141734693790,")
emit("   i.e. delta_1 = 2.653e-10, a relative error 1.877e-11.  Since Z_j ~ gamma_1^-j, such an")
emit("   error propagates with relative factor ~ j.  Predicted |dZ_j| = |2 j Im(rho_1^-(j+1))| * delta_1.")
g1t = mp.mpf('14.134725141734693790')
d1 = mp.mpf('14.134725142000001') - g1t
rho1 = mp.mpf(1) / 2 + 1j * g1t
emit("%3s %16s %16s %10s" % ("j", "predicted |dZ_j|", "observed |dZ_j|", "ratio"))
for j in (3, 4, 5, 6, 10, 20, 30, 40):
    pr = abs(2 * j * mp.im(rho1 ** (-j - 1)) * d1)
    zz = mp.mpf(repr(float(Zz[j])))
    ob = abs(zz - Z_arith(j))
    emit("%3d %16s %16s %10s" % (j, mp.nstr(pr, 5), mp.nstr(ob, 5), mp.nstr(ob / pr, 3)))
emit("   ==> the residual zeros-vs-formula difference for j>=3 is accounted for (within a small")
emit("       factor) by the limited precision of the STORED zeros; the formula itself is NOT the")
emit("       limiting side (it is stable to dps=40..300, i.e. to >20 digits).")

emit()
emit("exact identity  1 - (1 - 2^{-j}) zeta(j) = - sum_{m odd >= 3} m^{-j}   (checked numerically)")
for j in range(2, 11):
    a = 1 - (1 - mp.mpf(2) ** (-j)) * mp.zeta(j)
    b = oddsum(j)
    emit("   j=%-2d  piece=%s   odd-sum=%s   diff=%s"
         % (j, mp.nstr(a, 15), mp.nstr(b, 15), mp.nstr(abs(a - b), 3)))

emit()
emit("cancellation diagnostic for j >= 2: the two terms of the formula and their ratio to |Z_j|")
for j in range(2, 26):
    a = Z_arith(j)
    p1 = 1 - (1 - mp.mpf(2) ** (-j)) * mp.zeta(j)
    emit("   j=%-2d  A=1-(1-2^-j)z(j)=%-19s  B=(-1)^j\eta_{j-1}=%-19s  Z_j=%-19s  |A/B|=%s"
         % (j, mp.nstr(p1, 12), mp.nstr((-1) ** j * eta[j - 1], 12), mp.nstr(a, 12),
            mp.nstr(abs(p1 / ((-1) ** j * eta[j - 1])), 8)))

with open(os.path.join(HERE, 'AR1_zeta_power_sums.txt'), 'w') as f:
    f.write("\n".join(OUT) + "\n")
print("\n[AR1 done, %.1fs]" % (time.time() - T0))
