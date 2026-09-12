# E8 — the 0.682 ceiling: moments, the Christoffel function, and what lies beyond bandwidth one

**Labels:** 核验 = checked here/in-repo；引用 = quoted；推导 = derived here；猜想 = conjecture.
**Sources:** in-repo `docs/ALIGN-A3-weil-positivity-inertia.md` and
`docs/ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md`, recording §5 and §7.2(d)(e) of the frontier paper
arXiv:2608.13637v2 (the paper itself was **not** read here). **Numerics:** `scripts/E8_ceiling_check.py` →
`scripts/E8_ceiling_check.txt`. **Not claimed:** nothing below proves or disproves RH.

## 1. Framework: moments known to order 2m

A certificate produces a Hermitian form G̃ in dimension d with real eigenvalues λ₁,…,λ_d. Normalise the
spectral measure μ = (1/d)Σ_i δ_{λ_i}, so m₀ = ∫dμ = 1 and m_k = ∫x^k dμ = (1/d)·tr G̃^k for k ≥ 0.
Say the moments are *known* to order 2m, i.e. m₁,…,m_{2m} are available by unconditional evaluation. The
quantity to bound below is the on-line proportion, equal to 1 − μ({0}) once the dictionary
"eigenvalue 0 ↔ not counted on the line" is fixed (§5: this dictionary is not fully reconstructible here).

## 2. The Christoffel function, and why it bounds the deficit (推导)

Let p(x) = Σ_{k≤m} c_k x^k with p(0) = c₀ = 1. Since p² ≥ 0 and p(0)² = 1,

    μ({0}) ≤ ∫p² dμ = Σ_{i,j≤m} c_i c_j m_{i+j} = cᵀ H_m c ,   H_m = (m_{i+j})_{0≤i,j≤m} ,

which depends only on the known moments. Minimising subject to c₀ = 1 gives the Christoffel function at 0,

    Λ_m(0) := min_{p(0)=1, deg p≤m} ∫p² dμ = 1/(H_m⁻¹)_{00} = det H_m/det B_m ,  B_m = (m_{i+j})_{1≤i,j≤m} ,

so that μ({0}) ≤ Λ_m(0), and therefore **(on-line proportion) ≥ 1 − Λ_m(0)**. (†)
[核验] 1/(H_m⁻¹)_{00} = det H_m/det B_m was verified numerically for m = 1,2,3 (script §C). Sharpness of
(†) is exhibited on a four-point measure: Λ₁(0) = 0.416, Λ₂(0) = 0.312, **Λ₃(0) = 0.300 = the mass at 0
exactly**. The bound is sharp, so it measures the true information content of the moments.

## 3. The two-moment case m = 1 (推导 / 核验)

For m = 1, H₁ = [[1,m₁],[m₁,m₂]], and the formula above gives Λ₁(0) = 1 − m₁²/m₂, hence

    1 − Λ₁(0) = m₁²/m₂ = (Σλ)²/(d·Σλ²) ,

exactly the Cauchy–Schwarz bound #{λ≠0}/d ≥ (Σλ)²/(d·Σλ²) [核验, script §C]. Since Λ_m(0) decreases in m,
1 − Λ_m(0) increases: **more moments always help if they are available**. Availability, not usefulness,
is the binding constraint — that is the whole content of the ceiling.

## 4. The window functional R(ψ), and the two constants (推导 / 引用 / 核验)

For bandwidth-one certificates the unconditional analytic input is the prime-side second moment

    ‖G̃‖²_HS = (R(ψ) + o(1))·N ,   R(ψ) = [∫ψ² + ∬|u−v|ψ(u)ψ(v) dudv]/(∫ψ)² ,   (◆)

with ψ the (even) window; the certified proportion so obtained is 2 − R(ψ). [核验] with ∫ψ = 1 on a unit
interval: ψ₀ (indicator) has ∫ψ² = 1 and ∬|u−v|ψψ = 1/3, so R = 4/3 and **2 − R = 2/3** (Montgomery);
ψ_MT has R = c_MT⁻¹ = ½ + (1/√2)cot(1/√2) = 1.3274992963, so **2 − R = 0.6725007** [引用: 0.6725]. Both
constants are reproduced to seven decimals (script §A).

## 5. The ceiling ≈ 0.682 — what it is, and what it is not

[引用] The frontier records "the ceiling over the broader class of all bandwidth-one certificates is
approximately 0.682", and (§7.2(e)) that **unconditionally higher moments add nothing**, the diagonal
method being available only in the Rudnick–Sarnak range X^k ≤ T^{2−ε}, which at X ≍ T permits only k = 1.

[核验] Minimising (◆) numerically over the **whole** bandwidth-one class — non-negative windows (simplex
SLSQP, script §B1) and signed windows (exact KKT solve, script §B2, N up to 1600) — gives
**min R = 1.3274992…**, i.e. max over the class of (2 − R(ψ)) = 0.6725, attained by ψ_MT.
[推导] (a) The window functional is **saturated**: 2 − R(ψ) cannot pass 0.6725 by any window optimisation,
agreeing with the optimality of the Montgomery–Taylor window ([CCLM17, Cor. 14]). (b) Since 0.682 > 0.6725,
the ceiling is **not a window-optimisation value**; it is the gain from using the two known moments
sharply — through Λ₁(0) in (†) — rather than through the single scalar R(ψ), i.e. 0.682 = 1 − Λ₁(0) for
the optimal admissible two-moment data.
[边界] The dictionary turning Λ₁(0) into 0.682 is not reconstructible from in-repo material (frontier §7.2
unread). This note verifies the constants 2/3 and 0.6725 exactly, and establishes that 0.682 lies strictly
beyond window optimisation; it does not re-derive 0.682 from first principles.
**Scoped question Q1:** with the normalisation μ ↔ (on-line proportion) fixed, is 1 − Λ₁(0) = 0.682 an
equality for the frontier's optimal two-moment data?

## 6. What a certificate class other than bandwidth-one must satisfy (推导)

Let 𝒞 be a candidate certificate class with spectral measure μ_𝒞 (m₀ = 1). 𝒞 raises the certified proportion
to at least c for all large d only if (i) for each m it supplies **all** moments m₁,…,m_{2m} of μ_𝒞 as
unconditional evaluations at X ≍ T (HL*(k₀), §7.2(f), is the hypothesis-conditional version); and (ii) the
resulting Christoffel values satisfy 1 − Λ_m(0) ≥ c, i.e. Λ_m(0) ≤ 1 − c.
Since Λ_m(0) ↓ Λ_∞(0) = μ_𝒞({0}), the proportion tends to 1 precisely when the class can both (a) supply
every moment and (b) drive the mass at eigenvalue 0 to zero. **Concrete first step:** since 0.682 is
already the sharp bound from m₁, m₂ alone, any class beating 0.682 must evaluate a **third moment (k = 3)**
unconditionally at X ≍ T. That is the barrier — a statement about multiplicative relations among prime
powers, not about window choice.

## 7. Do the project's own objects belong to such a class? (核验, in-repo)

No — neither candidate, on the project's own records.
- **Kernel family.** `docs/EXPLORATION-POINTS-REGISTER.md` (E7) records that whether the project's kernel
  family is a bandwidth-one certificate is **unknown**. A class not shown to leave bandwidth one cannot be
  claimed to break the bandwidth-one ceiling.
- **Inertia computations.** n₋(K_ρ) = 1, n₋(K_off(N)) = N and the moving-edge results P28–P33 are
  **negative-index** statements, on the other side of the inertia bookkeeping (observation due to Bombieri
  [Bom00]; see `ALIGN-A3-weil-positivity-inertia.md` §3). They supply no positive moments and no
  second-moment evaluation; the project's audit (`p27p33-fourfold-audit.md`, verdict P-C) records the route
  as circular as constructed (K_N takes δ as input) and blocked by moving-edge non-transmission.
- The one positive asset, the variational theorem (T6/A17: on-line ordinates minimise S_proj), is
  positivity on the **configuration** side and supplies no moment of any spectral measure.
⇒ The project possesses no object supplying the missing higher moments; its negative results are consistent
with — and independently explain — why the negative-index side cannot reach the ceiling question at all.

## 8. Boundaries

[引用] only: R(ψ_MT) = c_MT⁻¹, the values 2/3 and 0.6725, the ceiling 0.682, §7.2(e), HL*(k₀).
[核验]: R(ψ₀) = 4/3 → 2/3; R(ψ_MT) = 1.3274993 → 0.6725; min R over bandwidth-one windows = c_MT⁻¹;
Λ_m(0) = det H_m/det B_m and 1 − Λ₁(0) = m₁²/m₂.
[推导]: the mass-at-0 ≤ Λ_m(0) argument; the §6 criterion. [未结] Q1 (§5).
**Unread:** frontier §7.2; [CCLM17]; [BGSTB24]. RH is not addressed.
