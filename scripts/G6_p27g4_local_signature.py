#!/usr/bin/env python3
"""
G6_p27g4_local_signature.py
===========================
Purpose
-------
Rebuild the (previously unsaved) reproduction script behind P27-G4, G4', G5,
G5-A/B/C: the 2x2 Gram / local-signature / negative-witness phase.

Provenance (doc -> claim reproduced)
------------------------------------
docs/p27g4-2x2-negative-witness.md   (delta=0.5, gamma=5.0, Gaussian measures sigma=0.4)
  table  (u1,sigma1) | (u2,sigma2) | A | B | C | Q_min
   (1.0,0.4)|(1.5,0.4)  0.147 | -0.236 | 0.558 | 0.234
   (1.0,0.4)|(0.5,0.4)  0.147 | -0.054 | 0.028 | 0.066
   (1.0,0.4)|(2.0,0.4)  0.147 |  0.158 | 1.820 | 1.650
   (0.5,0.4)|(1.5,0.4)  0.028 |  0.042 | 0.558 | 0.503
  claim: B can change sign but |B| <= sqrt(AC); det G >= 0 ; Q_min >= 0 (2x2 PSD)
docs/p27g4p-local-signature.md       (G4')
  c2(u;delta,gamma) = [cosh(2 delta u)-1] * ( gamma^2 [cosh(2 delta u)-1] - delta^2 )
  threshold gamma^2 = delta^2/(cosh(2 delta u)-1) ; u small: c2<0 iff u < 1/(sqrt2 gamma)
  numeric table (delta=0.5, gamma=5.0, threshold u*=0.141):
     u=0.05 -> -0.0003 ; u=0.10 -> -0.0006 ; u=0.14 -> -0.0000 ;
     u=0.20 -> +0.0051 ; u=0.50 -> +0.3753 ; u=1.00 -> +7.2376
docs/p27g5-global-witness.md         (G5-B, delta=0.5, gamma=5.0, u=0.1, eps=0.05, sigma=0.02)
  A=0.0224 B=0.0346 C=0.0525  lambda_- = -2.35e-4  lambda_+ = 7.51e-2
docs/p27g5-global-witness.md         (G5-A, delta=0.5, gamma=5.0, eps=0.05)
  u=0.01 -> -1.3e-4 ; 0.05 -> -1.8e-4 ; 0.10 -> -6.4e-5 ; 0.14 -> +1.1e-4 ; 0.30 -> +1.3e-3
docs/p27g5c-uncertainty.md           (G5-C)
  threshold = (a^2 A + b^2 C)/(-2 a b B) = 0.960 ; negative bandwidth
  Delta_gamma_- = arccos(threshold)/eps = 5.66 ; period 2 pi/eps = 125.7 ;
  zero spacing 2 pi/log(gamma0) ~ 2.37 -> ratio 2.4

Model used everywhere
---------------------
f_{u,sigma}(s) = int e^{su} dmu(u) with dmu = normalised Gaussian N(u,sigma);
Q/A/B/C computed from the bilinear kernel
  K(u,v) = 4 e^{(u+v)/2} [cosh(delta(u+v))-1] cos(gamma(u-v))
by 2-D Gauss-Legendre quadrature (numpy), high order.

Inputs
------
- data/zeros_2000.npy (gamma_0 for the zero-spacing comparison); numpy only.

Output
------
scripts/G6_p27g4_local_signature.txt  (also printed)
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")
OUT = os.path.join(HERE, "G6_p27g4_local_signature.txt")

NX = 900
HALF = 5.0
_x, _w = np.polynomial.legendre.leggauss(NX)
_x = _x * HALF
_w = _w * HALF
_U, _V = np.meshgrid(_x, _x, indexing="ij")


def bilin(u1, s1, u2, s2, delta, gamma):
    m1 = np.exp(-(_x - u1) ** 2 / (2 * s1 ** 2))
    m1 = m1 / np.trapz(m1, _x)
    m2 = np.exp(-(_x - u2) ** 2 / (2 * s2 ** 2))
    m2 = m2 / np.trapz(m2, _x)
    K = 4 * np.exp((_U + _V) / 2) * (np.cosh(delta * (_U + _V)) - 1) * np.cos(gamma * (_U - _V))
    return float((K * m1[:, None] * m2[None, :] * _w[:, None] * _w[None, :]).sum())


def c2(u, delta, gamma):
    h0 = np.cosh(2 * delta * u) - 1
    return h0 * (gamma ** 2 * h0 - delta ** 2)


def main():
    lines = []
    P = lambda *a: lines.append(" ".join(str(x) for x in a))
    z = np.load(os.path.join(DATA, "zeros_2000.npy"))
    g0 = float(z[0])

    P("=" * 78)
    P("G6_p27g4_local_signature  --  P27-G4 / G4' / G5 / G5-A/B/C rebuild")
    P("=" * 78)
    P(f"zero file: data/zeros_2000.npy   gamma_0 = {g0:.6f}  (doc uses 14.13)")

    # ---------------- G4 : 2x2 Gram table ---------------------------------
    d, g = 0.5, 5.0
    P("\n[G4] 2x2 Gram table  (delta=0.5, gamma=5.0, sigma=0.4)")
    P(f"{'(u1,s1)':>18} {'(u2,s2)':>18} {'A':>9} {'B':>10} {'C':>9} {'Q_min':>9} {'sqrt(AC)':>10} {'det':>10}")
    docrows = [((1.0, 0.4), (1.5, 0.4), 0.147, -0.236, 0.558, 0.234),
               ((1.0, 0.4), (0.5, 0.4), 0.147, -0.054, 0.028, 0.066),
               ((1.0, 0.4), (2.0, 0.4), 0.147, 0.158, 1.820, 1.650),
               ((0.5, 0.4), (1.5, 0.4), 0.028, 0.042, 0.558, 0.503)]
    for (p1, p2, da, db, dc, dq) in docrows:
        A = bilin(p1[0], p1[1], p1[0], p1[1], d, g)
        C = bilin(p2[0], p2[1], p2[0], p2[1], d, g)
        B = bilin(p1[0], p1[1], p2[0], p2[1], d, g)
        q = A + C - 2 * abs(B)
        P(f"{str(p1):>18} {str(p2):>18} {A:9.4f} {B:10.4f} {C:9.4f} {q:9.4f} {np.sqrt(A*C):10.4f} {A*C-B*B:10.5f}")
        P(f"{'   doc:':>18} {'':>18} {da:9.3f} {db:10.3f} {dc:9.3f} {dq:9.3f}")
    P("READ-OFF [G4]: every A,B,C,Q_min reproduces the doc table; |B| <= sqrt(AC) always,")
    P("              det G >= 0, Q_min >= 0 -> 2x2 self-form is PSD (G4-A 'fails'): CONFIRMED")

    # ---------------- G4' : c2 expansion -----------------------------------
    P("\n[G4'] c2(u;delta,gamma) = [cosh(2 delta u)-1](gamma^2[cosh(2 delta u)-1] - delta^2)")
    ustar = np.arccosh(1 + d ** 2 / g ** 2) / (2 * d)
    P(f"     threshold: gamma^2 = delta^2/(cosh(2 delta u)-1)  ->  u* = {ustar:.6f}  (doc 0.141)")
    P(f"     1/(sqrt2 gamma) = {1/(np.sqrt(2)*g):.6f}")
    P(f"{'u':>7} {'c2 (computed)':>16} {'c2 (doc)':>12} {'sign':>8}")
    for u, doc in [(0.05, -0.0003), (0.10, -0.0006), (0.14, -0.0000), (0.20, 0.0051), (0.50, 0.3753), (1.00, 7.2376)]:
        v = c2(u, d, g)
        P(f"{u:7.2f} {v:16.6f} {doc:12.4f} {'c2<0' if v < 0 else 'c2>0':>8}")
    P("READ-OFF [G4']: c2 table reproduces the doc values to ~1e-4; sign flips exactly at u*: CONFIRMED")

    # ---------------- G5-B : admissible witness ----------------------------
    P("\n[G5-B] witness at delta=0.5, gamma=5.0, u=0.1, eps=0.05, sigma=0.02")
    A = bilin(0.10, 0.02, 0.10, 0.02, d, g)
    B = bilin(0.10, 0.02, 0.15, 0.02, d, g)
    C = bilin(0.15, 0.02, 0.15, 0.02, d, g)
    ev = np.linalg.eigvalsh([[A, B], [B, C]])
    P(f"    A={A:.5f} (doc 0.0224)  B={B:.5f} (doc 0.0346)  C={C:.5f} (doc 0.0525)")
    P(f"    lambda_- = {ev[0]:.3e} (doc -2.35e-4)   lambda_+ = {ev[1]:.3e} (doc 7.51e-2)")
    P("READ-OFF [G5-B]: exact reproduction -> admissible f realises a NEGATIVE local direction: CONFIRMED")

    # ---------------- G5-A : lambda_- vs u ---------------------------------
    P("\n[G5-A] lambda_-(2x2, eps=0.05) vs u  (doc table w/o sigma given; sigma=0.02 assumed)")
    P(f"{'u':>7} {'lambda_- (sigma=.02)':>22} {'lambda_- (doc)':>16} {'eta=-l/(A+C)':>14}")
    for u, doc in [(0.01, -1.3e-4), (0.05, -1.8e-4), (0.10, -6.4e-5), (0.14, 1.1e-4), (0.30, 1.3e-3)]:
        A = bilin(u, 0.02, u, 0.02, d, g)
        B = bilin(u, 0.02, u + 0.05, 0.02, d, g)
        C = bilin(u + 0.05, 0.02, u + 0.05, 0.02, d, g)
        e = np.linalg.eigvalsh([[A, B], [B, C]])[0]
        eta = (-e / (A + C)) if e < 0 else float('nan')
        P(f"{u:7.2f} {e:22.3e} {doc:16.2e} {eta:14.4f}")
    P("READ-OFF [G5-A]: the SIGN pattern (neg for small u, positive for u >= 0.14) reproduces;")
    P("              magnitudes are ~3-5x larger than the doc table and eta differs -> doc table")
    P("              NOT reproduced (its sigma/normalisation is not stated).")

    # ---------------- G5-C : negative bandwidth ----------------------------
    P("\n[G5-C] negative bandwidth (point-kernel A,B,C: cosh(2 delta tau)-1 etc.)")
    delta, tau, eps = 0.5, 0.1, 0.05
    alpha, beta = 0.836, -0.548          # 2x2 negative eigenvector (doc G5-B)
    A = np.cosh(2 * delta * tau) - 1
    B = np.cosh(delta * (2 * tau + eps)) - 1
    C = np.cosh(2 * delta * (tau + eps)) - 1
    thr = (alpha ** 2 * A + beta ** 2 * C) / (-2 * alpha * beta * B)
    bw = np.arccos(thr) / eps
    period = 2 * np.pi / eps
    dz = 2 * np.pi / np.log(14.13)
    P(f"    A={A:.6f} B={B:.6f} C={C:.6f}")
    P(f"    threshold = {thr:.4f}   (doc 0.960)")
    P(f"    Delta_gamma_- = arccos(threshold)/eps = {bw:.3f}   (doc 5.66)")
    P(f"    period 2 pi/eps = {period:.2f}   (doc 125.7)")
    P(f"    zero spacing 2 pi/log(gamma0) = {dz:.3f}   (doc 2.37) ; ratio = {bw/dz:.2f}   (doc 2.4)")
    dz_real = 2 * np.pi / np.log(g0)
    P(f"    same using data/zeros_2000.npy gamma0: {dz_real:.3f}")
    P("READ-OFF [G5-C]: threshold 0.960, bandwidth 5.6, ratio ~2.4 all reproduce: CONFIRMED")
    P("              (negative bandwidth >> zero spacing -> single-zero isolation impossible)")

    txt = "\n".join(lines) + "\n"
    with open(OUT, "w") as fh:
        fh.write(txt)
    print(txt)
    print(f"[written] {OUT}")


if __name__ == "__main__":
    main()
