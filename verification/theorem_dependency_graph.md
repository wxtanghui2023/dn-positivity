# Theorem Dependency Graph（v2.14）

## Main Theorem
```
Main Theorem (Q = Q'_RH ⟺ Re ρ = ½ for every nontrivial zero)
 |
 +-- Proposition A2 (absolute interchange: Σ|⟨K_ρ,H_0⟩| < ∞)
 |     └── Proposition A1 (single-zero kernel: M₀ = M₁ = 0, |M₂| ≤ C|δ|)
 |           └── scaled-profile bound sup_λ ∫y²|Q_λ|dy < ∞   [internal]
 |
 +-- Proposition B (distributional Weil compatibility)
 |     ├── pairing ⟨S,H_0⟩ := ⟨log|ξ|, H_0''⟩   [internal verification]
 |     ├── H_0'' ∈ L¹ (O(t⁻²))                  [internal verification]
 |     └── Weil explicit formula (tempered form) [EXTERNAL: Weil 1952 / Barner 1981]
 |           └── tempered distribution framework [EXTERNAL: Schwartz / Hörmander]
 |
 +-- Lemma C (spectral discrepancy positivity)
 |     ├── closed form Δ_H = w_H(γ,δ) − w_H(γ,0)   [internal, definition]
 |     ├── numerator N(x) strictly increasing       [internal, algebra]
 |     ├── |γ_ρ| ≥ γ₁ = 14.1347 (zero ordinate)     [unconditional]
 |     └── pointwise positivity (no uniform inf)    [internal]
 |
 +-- Zero projection definition (ρ* = ½ + iγ_ρ)
 |     └── reference spectrum, not an assertion     [internal, definition]
 |
 └── positive-term argument (ΣΔ_ρ = 0 ⟹ each Δ_ρ = 0)  [internal]
```

## Legend
- **[internal]** — proved/verified in this manuscript
- **[internal, definition]** — definitional, no proof needed
- **[internal, algebra]** — closed-form algebraic statement
- **[EXTERNAL]** — invoked theorem, not reproven
- **[unconditional]** — no RH assumption

## Answers to "who supplies what"
- **External theorem**: Weil explicit formula (tempered form), tempered distribution framework.
- **Original contribution**: single constructed H_0; rigid discrepancy identity; positivity structure; equality characterization.
- **Assumption**: the stated distributional framework; validity of the explicitly verified pairings.
- **No step assumes RH.** RH appears only as the equality condition.
