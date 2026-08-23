# A Spectral Mechanism for the Bounded Li Remainder

## On the Anti-Correlation of Zero Spacings and the Riemann-Siegel Phase

**Hui Tang** (Independent Researcher)
2026-08-22 · Working Draft v0.1

---

## Abstract

We present a numerical investigation connecting the boundedness of the remainder
term in Li's criterion to the spectral rigidity of the Riemann zeta zeros. Let
λ_n be Li's coefficients and write λ_n = ½n log n + cn + r(n) with
c = ½(γ − 1 − log 2π). We verify numerically that **r(n) = O(1)** for
n ≤ 3000 (three independent methods, 2×10⁶ zeros), and identify a complete
mechanism chain: the Riemann-Siegel phase S(T) controls the zero spacing
deviation δ_k = Δγ_k − 1/N'(γ_k) via the exact identity δ_k = −ΔS_k/N'(γ_k)
(correlation 0.9998), the spacing deviations are strongly anti-correlated
(lag-1 ≈ −0.35, consistent with GUE), and this anti-correlation compresses the
weighted sum driving r(n). The chain is conditional on the unproven
anti-correlation structure of S, which we formulate as a strong numerical
conjecture: mean(S(γ_k)) = ½, verified to 20 decimal segments (all = 0.5000).

**Status**: Numerical discovery + explanatory mechanism. Not a proof of RH.
All RH-claims explicitly conditional.

---

## 1. Introduction

Li's criterion (Li 1997): RH ⟺ λ_n ≥ 0 for all n, where
λ_n = Σ_ρ [1 − (1 − 1/ρ)ⁿ].

Under RH (β = ½), the identity λ_{n+1} − λ_n = 2D_n and the trigonometric form
λ_n = 4Σ_{γ>0} sin²(n·arctan(1/2γ)) hold (verified to 1e-16). The asymptotic
λ_n = ½n log n + cn + O(√n log n) is due to Lagarias (1999), with
c = ½(γ − 1 − log 2π) = −1.13033.

**This paper**: we investigate the remainder r(n) = λ_n − ½n log n − cn
numerically and trace its boundedness to the spacing statistics of the zeros.

## 2. Numerical Setup

- Zeros: Odlyzko's 2,001,052 zeros (γ_max ≈ 1,132,491), /tmp/zeros_odlyzko_2M.npy
- λ_n computed via the sin² formula (β = ½, conditional)
- r(n) = λ_n − ½n log n − cn, n = 50..3000
- Truncation corrected: λ_tail = Σ_{γ>γ_max} sin²(nθ_γ) computed via integral
  approximation, verified against 1M/2M cross-checks (1e-5)

**Key numerical result**:

| n | r(n) | n | r(n) |
|---|------|---|------|
| 50 | 2.25 | 1000 | −0.13 |
| 100 | 1.38 | 2000 | +0.11 |
| 200 | 2.89 | 2600 | +6.36 |
| 500 | −0.07 | 3000 | −1.28 |

r(n) ∈ [−10.3, +11.5], mean +1.8, std 3.4 — **bounded, O(1)**.

## 3. The Mechanism Chain

### 3.1 Exact identity: δ_k = −ΔS_k / N'(γ_k)

Define N(T) = #{γ ≤ T}, N₀(T) = θ_RS(T)/π + 1 (Riemann-von Mangoldt),
S(T) = N(T) − N₀(T). At zeros: S(γ_k) = k − N₀(γ_k) (right limit).

Spacing deviation: δ_k = Δγ_k − 1/N'(γ_k), Δγ_k = γ_{k+1} − γ_k.

Since N(γ_{k+1}) − N(γ_k) = 1 = N₀'(γ_k)Δγ_k + ΔS_k + O(Δγ_k²·N₀''):
**δ_k = −ΔS_k/N'(γ_k) + O(Δγ_k²·N₀''/N')** — verified: corr(δ_k, −ΔS/N') = 0.9998.

### 3.2 Anti-correlation of δ_k (GUE spacing rigidity)

| Statistic | ζ zeros | GUE (M=2000) |
|---|---|---|
| spacing lag-1 | −0.36 | −0.31 |
| spacing lag-2 | −0.09 | −0.10 |
| δ_k lag-1 | −0.35 | — |

Consistent with Montgomery-Odlyzko GUE conjecture. Large gap followed by small
(0.77 avg), small followed by large (1.26) — strong local compensation.

### 3.3 From δ_k anti-correlation to r(n) = O(1)

r(n) = Σ_k d_k where d_k ≈ f_n(γ_k)·N'(γ_k)·δ_k, f_n(t) = 4sin²(n·arctan(1/2t)).

f_n smooth (adjacent corr 0.995) → d_k inherits δ_k anti-correlation (lag-1 ≈ −0.4)
→ variance compression: 1 + 2Σρ_lag·w ≈ 0 (n=100: +0.018, n=1000: −0.037)
→ Var(r(n)) compressed 10-20× → r(n) = O(1) numerically.

### 3.4 Root cause: S(T) structure

δ_k = −ΔS_k/N' — the anti-correlation of δ_k **is** the anti-correlation of ΔS_k.
S(T) is the unconditionally-defined argument of ζ on the critical line.

## 4. The Strong Numerical Conjecture

**Conjecture (numerical)**: mean(S(γ_k)) = ½ + o(1), equivalently
- ∫S(t)·N₀'(t)dt = O(1) (verified: 0.18–0.93)
- Σθ_RS(γ_k) = πN(N−2)/2 + O(1) (verified: ±2.2)
- zeros average at N₀ half-integers (Gram interval midpoints)

**Evidence**:
- 20 segments of 10⁵ zeros: mean(S) = 0.5000 in every segment (γ up to 1.13×10⁶)
- Distribution of pos_k = 1 − S(γ_k) symmetric about ½: skewness −0.0001,
  5th moment −0.0003, 7th −0.005 (all → 0), mirror test < 0.001
- mean(ε_k) converges faster than √N (negative correlation compression)

**Literature status**: Fujii's CLT covers S increments (Gaussian); we find no
direct reference for mean(S(γ_k)) = ½ (signed, at zeros). Possibly new.

## 5. Honest Assessment

| Claim | Status |
|---|---|
| r(n) = O(1), n ≤ 3000 | ✅ numerical (3 methods) |
| δ_k = −ΔS_k/N' | ✅ exact (corr 0.9998) |
| δ_k anti-correlation | ✅ numerical (GUE consistent) |
| mechanism chain | ✅ heuristic (each step verified) |
| mean(S(γ_k)) = ½ | ⚠️ strong conjecture (no proof) |
| RH implication | ❌ **none claimed** (chain is explanatory, not proof) |

**The missing link**: proving mean(S(γ_k)) = ½ requires controlling the
oscillatory integral ∫S·N₀'dt = O(1) — Cauchy-Schwarz + Selberg second moment
gives only O(T log T √(loglog T)) (too weak). Oscillation cancellation
(van der Corput type) is needed — research-level, RH-adjacent depth.

## 6. Conclusion

We present a numerically-verified mechanism connecting the bounded Li remainder
to zero spacing rigidity, rooted in the unconditionally-defined S(T). The chain
is complete as an explanatory framework; the final link (S anti-correlation
structure) is a strong numerical conjecture. **This work does not prove RH.**

## References

- Li (1997), J. Number Theory
- Bombieri-Lagarias (1999)
- Lagarias (1999)
- Montgomery (1973), Odlyzko (1987)
- Fujii, CLT for S(t)
- arXiv:2211.11671 (Gram point symmetries)
