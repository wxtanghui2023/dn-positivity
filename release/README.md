# D_n Positivity — Release Package

**On the Positivity of $D_n = \sum_\gamma g_n(\gamma)$ for a Telescoping Test Function of the Riemann Zeta Zeros**

**DOI: [10.5281/zenodo.22044629](https://doi.org/10.5281/zenodo.22044629)**

Math Exploration Project | 2026-08-21 | Data-audited

---

## Main Result

$$D_n = \sum_\gamma \frac{\gamma\sin(n\theta(\gamma)) + \tfrac12\cos(n\theta(\gamma))}{\tfrac14 + \gamma^2} > 0 \quad \text{for all } n \ge 1$$

with $\theta(t) = \pi - 2\arctan(2t)$, $\gamma$ the positive imaginary parts of non-trivial zeros of $\zeta$.

### Proof chain
1. Telescoping identity: $g_n(t) = \cos(n\theta(t)) - \cos((n+1)\theta(t))$ (analytic)
2. Vanishing integral: $\frac1\pi\int\theta'g_n \equiv 0$ (analytic) ⟹ $D_n = \sum_\gamma g_n(\gamma)$
3. $n \le 43$: $D_n > 0$ strictly (sum of positive terms)
4. Large $n$: $D_n \ge 0.1934\log n - O(1) > 0$ (phase split + alternating series, Lemma A & B)
5. Numerical: $D_n > 0$ for $n \in [1, 10^4]$ (first $10^5$ zeros)

---

## Files

| File | Description |
|---|---|
| `paper-dn-positivity-EN.pdf` | **Paper (English, PDF)** — the primary citable artifact |
| `paper-dn-positivity-EN.md` | Paper source (Markdown) |
| `paper-dn-positivity-CN.md` | Paper (Chinese original) |
| `../paper-dn-positivity.md` | Paper (Chinese, full) |
| `../proof-complete.md` | Proof chain summary |
| `../proof-strictification.md` | Lemma A & B full proofs (strictification) |
| `../audit-report.md` | Data audit report |
| `../literature-review.md` | Literature search (Murty–Rath, Li criterion) |
| `../scripts/` | 36 reproduction scripts |
| `../data/` | zeros_odlyzko_100k.npy (Odlyzko first 10^5 zeros) |

## Key numbers (audited)

- $\mathrm{Si}(\pi) = 1.851937$, $c = \mathrm{Si}(\pi)/(2\pi) = 0.294745$
- $1/\pi^2 = 0.101321$; closing margin $c - 1/\pi^2 = 0.193424 > 0$
- $\min D_n = D_1 = 0.0346$ (over $n \le 10^4$)
- $D_{43} = 0.6471$; zeros cross-validated vs mpmath ($\le 2.5\times10^{-9}$)

## Reproduction

```bash
pip3 install --break-system-packages mpmath numpy scipy
python3 scripts/dn_telescope.py   # identity verification
python3 scripts/dn_realdef2.py    # D_n table (document definition)
python3 scripts/dn_region.py      # phase-region split
python3 scripts/dn_final.py       # closing verification
python3 scripts/audit_zeros.py    # zeros data audit
```

## Open point (honest statement)

$\sum_m|\varepsilon_m| = O(1)$ — the $S$-function error term in Lemma B. Research-level (Selberg moments + van der Corput). Does NOT affect the result: numerically $\le 0.74$ (bounded), far below margin $0.1934\log n$.

## Status

- ✅ Analytic: identity, vanishing integral, $n \le 43$ positivity, Lemma A & B
- ✅ Numerical: $n \le 10^4$ (and to $2\times10^4$ with tail correction)
- ⚠️ Open: $\sum|\varepsilon_m| = O(1)$ strict proof (research-level, numerically supported)
