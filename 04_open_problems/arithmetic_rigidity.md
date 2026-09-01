# Open Problem: Arithmetic Rigidity

**Status: OPEN**

## The question
What is the minimal sufficient condition for arithmetic-direction coercivity?
```
inf_{Λ∈R} inf_θ ∫_0^∞ e^{−cv}|S_Λ(v+θ)|²dv > 0
```
where S_Λ(v) = Σ e^{iγ_j v}/(c−iγ_j), over a natural regularity class R.

## Why this is the right question
- Pure harmonic analysis — independent of zeta
- density → difference-spectrum structure → uniform coercivity → exclusion (the middle arrow is the unknown)
- If R* ⟹ coercivity holds for a natural R*, then ask: do zeta zeros satisfy R*?

## Candidates for the sufficient condition
- Difference-spectrum non-concentration (maximal negative deviation < b₀)
- Lower Beurling density + regularity
- Quantitative non-arithmeticity / additive-energy bounds
- Sine-type / de Branges regularity

## Documents
- docs/p510-literature-bm.md (Beurling-Malliavin/Ingham/frame theory)
- docs/p512c2-margin-decay.md (margin decay — candidate theorem weakened)
- docs/arith-direction-adversarial.md (RvM-calibrated coercivity — numerical)
