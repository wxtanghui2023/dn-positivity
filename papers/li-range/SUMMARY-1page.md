# One-page summary

**Title.** An elementary explicit positivity range for the Li coefficients
**Author.** Hui Tang ｜ **Length.** 5 pages

## Result
If every non-trivial zero with 0 < γ ≤ T is rigorously known to lie on the critical line, then
**λ_n ≥ 0 for all integers 2 ≤ n ≤ 2T − O(1)**. With T = 3.000175·10¹² (Platt–Trudgian,
interval arithmetic) this is **n ≤ ≈ 6.00035·10¹²**, i.e. **≈ 6·10⁷ times** the direct
computational range n ≤ 10⁵ (Palojärvi; Coffey).

## Method (four elementary ingredients)
1. On-line zeros contribute 1 − cos(nθ_γ) ≥ 0, θ_γ = arg(1−1/ρ) = arctan(γ/(γ²−1/4)).
2. **Window bound:** for γ ∈ [n/2, min(2n,T)], nθ_γ ∈ [1/2 − 1/(96n²), 2] because
   θ_γ = 1/γ − 1/(12γ³) + 1/(80γ⁵) − … and θ_γ is strictly decreasing; hence each window term
   ≥ C₁(n) = 1 − cos(1/2 − 1/(96n²)) = 0.12241744… for n ≥ 10⁴.
3. **Counting:** the classical explicit Riemann–von Mangoldt bound (Trudgian) supplies
   N(T) − N(n/2).
4. **Off-line bound:** zeros above T contribute at worst −n·B_T, with
   B_T = ½Σ_{γ>T}γ^{-2} ≤ 3.4·10⁻⁶ (T = 1.13·10⁶) / ≤ 2.85·10⁻¹² (T = 3·10¹²), computed
   from six elementary integrals.
⟹ λ_n ≥ C₁(n)·#{γ ∈ [n/2, min(2n,T)]} − n·B_T.

## Numerical calibration
- λ_1 = 0.0230957089661210338 (exact) vs 0.0230938677 (computed) → **8·10⁻⁵**.
- Every n ≤ 20000 checked exhaustively; margin **2.2·10⁴**.
- Margin in the criterion: 2.7·10⁵ (n=10⁵) → 1.03 (endpoint).

## Scope
- **Subset result**, not a proof of RH. Unconditional given T.
- No information about zero locations above T is used — only a worst-case bound.
- The height-to-range conversion is not claimed as new (folklore); the contribution is its
  explicit, elementary and calibrated form.
