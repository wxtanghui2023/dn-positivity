# Audits

Five status classes are strictly separated throughout:
- **THEOREM** (strict proof): see docs/theorem-status-audit.md (T1-T10)
- **PROPOSITION** (proof framework, condition-dependent): P1-P3
- **NUMERICAL OBSERVATION**: N1-N6
- **CONJECTURE**: C1-C3
- **FAILED ROUTE**: F1-F11

## P5 series (framework independence audit)
- P5.1-P5.4: framework independence, axiom minimization, inverse problem
- P5.7: critical-tail audit (C0-C4 logical strength)
- P5.8: W_δ distortion test (15 constraints — no exclusion)
- P5.9: positive-definite/spectral-gap audit
- P5.9-R/S: Cauchy configuration, fixed-direction analysis
- P5.10: adversarial block sequences (all fail)
- P5.11: adversarial theorem (phase engineering fails)
- P5.12: difference-spectrum / additive-energy / margin decay

## Key audit documents (docs/)
- theorem-status-audit.md (five-class separation)
- p59-positivedefinite-audit.md, p59r-cauchy-strict.md, p59s-fixed-direction.md
- p510-block-adversarial.md, p510-attack-confirmed.md, p510-literature-bm.md
- p511-adversarial-theorem.md, p5112-discrepancy-attack.md
- p512-additive-energy.md, p512c1-spectrum-counterexample.md, p512c2-margin-decay.md, p512-closure.md
- blind-spot-map.md, zero-prime-coupling-closure.md
