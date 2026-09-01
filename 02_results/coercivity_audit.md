# Coercivity Audit

**Status: PROPOSITION + NUMERICAL OBSERVATION**

## Difference-spectrum analysis
For F(θ) = Σ_{j,k} a_j ā_k K_c(γ_j−γ_k)e^{i(γ_j−γ_k)θ}, a_j = 1/ρ_j:
- F(θ) = b₀ + Σ_{r≠0} b_r e^{irθ}
- inf_θ F ≥ b₀ − Σ|b_r| (triangle bound — coarse)
- Coercivity requires control of the **maximal negative deviation** (not total variation)

## Empirical findings
| Quantity | Value | Status |
|---|---|---|
| RvM margin inf F/b₀ | ~0.03-0.05 (J to 4000) | numerical |
| margin ~ 0.2/log J | decay fit | numerical fit, not theorem |
| E_Λ vs F anti-correlation | lattice E=5.3e6 ⟹ F=0.0097 | numerical |
| Adversarial constructions | all fail to destroy coercivity | numerical |

## Key conclusion
**Uniform coercivity is not controlled by density statistics alone** (section title in paper §8.5). R0-R2 insufficient; the actual candidate is uniform difference-spectrum rigidity (unidentified).

## Documents
- docs/p512c1-spectrum-counterexample.md, p512c2-margin-decay.md, p512-closure.md
- papers/structural-framework-detection-exclusion-EN.md §8.5
