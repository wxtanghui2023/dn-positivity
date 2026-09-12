#!/usr/bin/env python3
"""
A3-break-682 attempt 3 (chunked) — provenance script.
Question: extend pair-correlation Fourier support 1 -> 1+delta; what proportion?
Reuses E8 framework: Christoffel bound 1 - Lambda_m(0) from moments m_1..m_{2m},
with 1 - Lambda_1(0) = m_1^2 / m_2 (Cauchy-Schwarz).

Frontier moment data (in-repo, docs/A3-third-moment-barrier.md, [原]):
  m_k(1) = 1, 4/3, 2, 13/4  (k = 1,2,3,4)
  Lambda_2(0;1) = 5/36
  HL*(4) => lim inf N0^s/N >= 13/18
  HL*(k0) for all k0 => proportion -> 1

This script ONLY recomputes the Christoffel hierarchy 1 - Lambda_m(0) from the
given moments (m = 1, 2). It does NOT reconstruct the frontier's dictionary
"Lambda_m(0) -> certified proportion" (that dictionary lives in unread Sec 7.2).

No RH is assumed anywhere. Numbers-only, R7.
"""
from fractions import Fraction

def christoffel(moms):
    # moms = [m0, m1, ..., m_{2m}]  (m0 = 1)
    # Lambda_m(0) = det H_m / det B_m, H_m = (m_{i+j})_{0<=i,j<=m}, B_m = (m_{i+j})_{1<=i,j<=m}
    m = (len(moms) - 1) // 2
    def det(M):
        n = len(M)
        if n == 1:
            return M[0][0]
        s = Fraction(0)
        for c in range(n):
            sub = [[M[i][j] for j in range(n) if j != c] for i in range(1, n)]
            s += ((-1) ** c) * M[0][c] * det(sub)
        return s
    H = [[moms[i + j] for j in range(m + 1)] for i in range(m + 1)]
    B = [[moms[i + j] for j in range(m + 1)] for i in range(m + 1)]  # same dims? no
    # B_m is (m_{i+j})_{1<=i,j<=m} -> indices i+j in {2..2m}
    B = [[moms[i + j] for j in range(1, m + 1)] for i in range(1, m + 1)]
    detH = det(H)
    detB = det(B)
    Lambda = detH / detB
    return Lambda, detH, detB

def main():
    m = [Fraction(1), Fraction(1), Fraction(4, 3), Fraction(2), Fraction(13, 4)]
    print("=" * 70)
    print("A3-break-682 attempt3 : Christoffel hierarchy from frontier moment data")
    print("=" * 70)
    print("moments m_k(1) = 1, 4/3, 2, 13/4  (k=1..4)  [原, in-repo]")
    print()

    # m = 1 : moments m0,m1,m2
    lam1, dH1, dB1 = christoffel([m[0], m[1], m[2]])
    m1sq_over_m2 = m[1] * m[1] / m[2]
    print(f"[m=1] Lambda_1(0) = det H1 / det B1 = {dH1} / {dB1} = {float(lam1):.8f}")
    print(f"      1 - Lambda_1(0) = {float(1 - lam1):.8f}")
    print(f"      m1^2/m2 (Cauchy-Schwarz) = {float(m1sq_over_m2):.8f}  (equal: {1 - lam1 == m1sq_over_m2})")
    print()

    # m = 2 : moments m0..m4
    lam2, dH2, dB2 = christoffel(m)
    print(f"[m=2] Lambda_2(0) = det H2 / det B2 = {dH2} / {dB2} = {float(lam2):.8f}   (= 5/36 = {float(Fraction(5,36)):.8f} check)")
    print(f"      1 - Lambda_2(0) = {float(1 - lam2):.8f}")
    print()
    print("Frontier-recorded [原]: Lambda_2(0;1)=5/36 ; HL*(4) => proportion >= 13/18")
    print(f"  13/18 = {float(Fraction(13,18)):.8f}")
    print()
    print("NOTE: 1 - Lambda_m(0) != 'certified proportion'. The dictionary")
    print("      Lambda_m(0) -> proportion lives in frontier Sec 7.2 (UNREAD in repo).")
    print("      E8 (docs/E8-ceiling-0682.md) states this dictionary is NOT")
    print("      reconstructible from in-repo material. So this hierarchy is the")
    print("      'moment-information' curve, not the 'proportion' curve.")
    print()
    print("Anchors established elsewhere (in-repo, [核验]):")
    print("  bandwidth-one ceiling (support 1, moments m1,m2) ~ 0.682")
    print("  Montgomery-Taylor window (support 1) = 0.6725")
    print("  pair-correlation conjecture (all support) => 100% simple")

if __name__ == "__main__":
    main()
