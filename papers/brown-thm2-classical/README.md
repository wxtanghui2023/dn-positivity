# Paper draft: the classical case of Brown's theorem

**Status**: draft v1 (2026-09-11) — **not submitted**.
**Claims**: Theorem 1 (stronger than the statement in [Dr12] Conjecture 1.7.10, which restricts k ≤ 2T²logT).
**Honest gaps**: see §7 of `main.md` — the closed-form near bound, the explicit local count, and the paywalled
original.
**Verification**: every numerical claim in §5–§6 is produced by an archived script:

| claim | script | output |
|---|---|---|
| S₄ sharp after the boundary term | `scripts/BL7_S4_bothsigns_check.py` | `scripts/BL7_*.txt` |
| exact margin (2/3)\|b\|H^{−3} | `scripts/BL10_final_comparison.py` | `scripts/BL10_*.txt` |
| finite window 5 ≤ H < 40 | `scripts/BL11_closed_form_near.py` | `scripts/BL11_*.txt` |
| the λ-band via the sinh² identity | `scripts/BL14_band_sharp.py` | `scripts/BL14_*.txt` |
| constant C = 2+γ−log4π (for context) | `scripts/NB1_constant_verification.py` | `scripts/NB1_*.txt` |

Per `docs/PROTOCOL-CODE-ARCHIVE.md` (rules R1–R7), no result in this paper is supported by ephemeral code.
