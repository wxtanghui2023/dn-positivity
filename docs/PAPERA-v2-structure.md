# Paper A (`papers/li-range/`) — proposed v2 structure and ready-to-paste prose

**Prepared:** 2026-09-12 (subagent task). **Status:** proposal only.
This file does **not** edit `papers/li-range/li-range.tex`, does not touch any other file, and is **not committed**.

**Discipline.** Every quotation below is copied verbatim from a file in this repository
(`papers/li-range/li-range.tex`, `papers/li-range/SUMMARY-1page.md`,
`docs/P8-GROUP6-voros-oesterle-bucur.md`, `docs/P8b-oesterle-rigor-status.md`,
`docs/PAPERA-quadratic-roadmap.md`, `scripts/PAPERA_num_enrich.txt`,
`scripts/PAPERA_avgcase_probe.txt`, `scripts/PAPERA_uniform_scan.txt`,
`scripts/PAPERA_oscillation_attack.txt`). No citation, page number or quotation has been
invented. Claims the reconnaissance does **not** support are explicitly marked as not supported.
Nothing is asserted as proved that is not proved; the quadratic route appears **only** as a
remark/roadmap.

---

## 0. The three changes of 2026-09-12, and what each one forces

| # | Finding (source) | What it forces in the paper |
|---|---|---|
| 1 | **Prior art.** A *quadratic* range — non-negativity of $\lambda_n$ for $n\le T_0^2$ when RH is verified to height $T_0$ — is attributed to Oesterlé's **uncirculated** 2000 typescript (`prop. 2`), and is stated in Biane–Pitman–Yor 2001 (§2.3, p. 441: "…for $n\le 2.975\ldots\times10^{17}$"), in Voros 2020 (Exp. Math. 29(4) 452–469, eq. (13)) and in Voros arXiv:2204.01036 §2.2.2; Maślanka 2004 restates it heuristically. It is **not** published as a rigorous theorem. | The abstract's comparison with "*direct computation of $\lambda_n$*" must be **deleted** (that is a limit of computation, not of knowledge) and replaced by an honest comparison with the prior claim, against which our range is **smaller by a factor $\approx T/2$**. Scope section's "folklore / not claimed as new" sentence must go. |
| 2 | **Direct numerics.** $\lambda_n$ is now computed directly (as a lower bound) from 2,001,052 zeros: positive lower bounds across the informative range; deviation from the zero count $\approx1.1\times10^{-4}$ at $n=T_0^2$; margin $\approx1.69$ against the tail term there (with caveats, §2.3 and Appendix A). | New numerics subsection, with the saturation caveat and the tail caveat stated, not hidden. |
| 3 | **Quadratic route.** Four steps: ① fluctuation term $O(\log T_0)$ uniformly (free); ② boundary term killed exactly by truncating at a phase zero (legitimate: verification at $T_0$ implies verification below it; recorded relative cost $\le T_0^{-1/2}$); ③ tail classical; ④ interior oscillation **OPEN**, with a measured two-regime structure. | Appears **only** as a Remark explicitly labelled a **roadmap, not a theorem**, listing the four steps and their status. |

**Postscript (added after the roadmap, same day — `docs/PAPERA-two-regime-attempt.md`, committed as b62a3f4).** A later note in this repository reports that in the second (averaging) regime three standard oscillation estimates — first-derivative, second-derivative (van der Corput), and "oscillation alone" — all fail *quantitatively*, the root cause being that the phase $\varphi(t)=2n\arctan(1/2t)$ varies too slowly near the truncation ($\varphi'(T_0)\approx2$ at $n=T_0^2$). Its conclusion is that the interior term must be **evaluated, not bounded** — which is what the prior (Oesterlé/Voros) argument does, by change of variable to a closed form — so that step ④ reduces to the error term of that saddle-point evaluation, and the two-regime route **merges with the arithmetic route** ($\mathrm{Osc}(n)=\mathrm{Re}\sum_j\binom nj(-1)^jZ_j$ with $Z_j=\sum_\rho\rho^{-j}$). If that finding is kept, §2.4's step-④ sentence should be updated to say this, and the remark remains a roadmap (it is no closer to a theorem; it is a sharper statement of where the difficulty lies). The paste-ready text in §2.4 below is written to the roadmap state and does **not** yet include this.

---

## 1. Proposed structure, section by section

1. **Introduction** (rewritten) — Li's criterion, notation, and the crucial taxonomy: three *different* things have been called "the range of $\lambda_n$" — (a) the range of *direct computation* ($n\le10^5$), (b) the range obtained by *converting a verified height* (Oesterlé's quadratic claim, reported in the literature, not proved in print), (c) the range *we prove* (linear in $T$, elementary, explicit constants). Then the precise statement of what this note contributes.
2. **Relation to prior work** (new) — the Oesterlé/BPY/Voros/Maślanka material, with the quadratic range attributed to them and our linear-range theorem claimed only in its explicit elementary form. (Prose in §2.2.)
3. **The phase of an on-line zero** — unchanged: identity $|1-1/\rho|=1$ on the line, $\theta_\gamma=\arg(1-1/\rho)$, $c_\rho$ off the line.
4. **Lemma 1, the window bound** — unchanged: $n\theta_\gamma\in[\tfrac12-\tfrac1{96n^2},2]$ for $\gamma\in[n/2,\min(2n,T)]$, hence $1-\cos(n\theta_\gamma)\ge C_1(n)$.
5. **Lemma 2, counting** — unchanged: Trudgian's explicit Riemann–von Mangoldt bound.
6. **Lemma 3, the off-line contribution** — unchanged, but add one sentence making the summation convention for $\Sigma_{\gamma>T}$ explicit (see Appendix A, item A3).
7. **Lemma 4, the explicit tail constant** — unchanged: $B_T\le$ six elementary integrals; $\le3.4015\cdot10^{-6}$ at $T=1.13249\cdot10^{6}$, $\le2.8531\cdot10^{-12}$ at $T=3.000175\cdot10^{12}$.
8. **Main theorem** — statement unchanged; the closing sentence that invokes "the range $1\le n\le10^5$ supplied by the direct verifications" recast so it is not read as the prior mathematical range.
9. **Remark (optimality within the method)** — kept but softened and explicitly cross-referenced to §11: the ceiling $n\le2T$ is optimal *for the worst-case, pointwise-window method*, and a different mechanism (stated in §11) would be needed to go beyond it; the phrase "the off-line term is never the binding constraint" reworded precisely.
10. **Numerical verification** — (i)–(iv) as now, plus **(v) direct computation of the Li coefficients from two million zeros** (prose in §2.3).
11. **Remark (roadmap): a quadratic route, and what remains open** — new; four steps and status; two-regime measurements; **explicitly not a theorem** (prose in §2.4).
12. **What this paper does not claim** — new short section (prose in §2.5).
13. **Scope** — rewritten opening: the conversion is prior art (attributed), the linear-shape explicit elementary proof is what is offered here; subset statement, not a proof of RH.
14. **Bibliography** — add BPY 2001, Oesterlé typescript, Voros 2006, Voros 2020, Voros 2022, Maślanka 2004 (BibTeX in §2.6).
15. *(Optional)* **Appendix: numerical provenance** — the two scripts, the data file, and the exact inequalities tested, so a referee can rerun.

*Optional retitle:* "An elementary explicit **linear** positivity window for the Li coefficients, and a numerical study of the quadratic route". The present title ("An elementary explicit positivity range for the Li coefficients") is not false, but it invites the reader to expect a range-record paper.

---

## 2. Ready-to-paste prose

### 2.1 Revised ABSTRACT

> Let $T$ be a height to which the Riemann Hypothesis has been verified by interval arithmetic.
> We prove, by elementary means, that the Li coefficients satisfy $\lambda_n\ge0$ for every
> integer $n$ with $2\le n\le 2T-O(1)$. For the verified height
> $T=3.000175\cdot10^{12}$ (that is, $T=3\,000\,175\,332\,800$) this gives $n$ up to
> approximately $6.00035\cdot10^{12}$.
>
> Our range is **linear** in $T$, and is therefore smaller — by a factor of order $T/2$ — than
> the **quadratic** range $n\le T_0^{\,2}$ that has been attributed to Oesterlé's uncirculated
> 2000 typescript and reported in the literature (Biane–Pitman–Yor, *Bull. AMS* **38** (2001),
> §2.3, p. 441; Voros, *Exp. Math.* **29** (2020), eq. (13)). We make no claim to improve on that
> range. The passage from a verified height to a range for $\lambda_n$ is not new here; what is
> offered is an *elementary, fully explicit* proof of a *linear* window, each ingredient of which
> is a published theorem, together with a numerical study of the coefficients themselves.
>
> The proof uses no information about the location of zeros above $T$: only the non-negativity of
> the on-line terms, a window bound for the phases, the classical explicit zero-counting estimate,
> and an elementary bound on the worst-case off-line contribution. No unproved hypothesis about
> the zeros above $T$ is assumed.

*Note for the authors:* the reconnaissance supports "the quadratic range is prior art, attributed
to Oesterlé and reported by BPY/Voros", and it supports "no **published** rigorous proof of the
quadratic range was found". It does **not** support "the quadratic range is unproved" as a
mathematical statement — Voros 2006 writes that Oesterlé "had a proof … but he neither published
nor even posted his typescript", and reproduces the argument. Phrase it as an absence of a
published proof, never as an absence of a proof.

### 2.2 RELATED WORK (new section / paragraph)

> **Relation to prior work.** The idea of converting a verified height into a range of Li
> coefficients is due to J. Oesterlé and is older than any published treatment. Biane, Pitman and
> Yor state, in §2.3 (p. 441) of their survey: *"We learned from J. Oesterlé (private
> communication) that $\lambda_n\ge0$ if every zero $\rho$ of $\xi$ with $|\Im\rho|<\sqrt n$ has
> $\Re\rho=\frac12$. This is known to be true for $n\le2.975\ldots\times10^{17}$."* With
> $T_0=\sqrt n$ this is exactly the statement that verification of RH up to a height $T_0$ forces
> $\lambda_n\ge0$ for all $n\le T_0^{\,2}$ — a **quadratic** range. Voros reports the same result
> as *"In 2000 Oesterlé [26, prop. 2] proved (but left unpublished [6, § 2.3]) that
> $\operatorname{Re}\rho=\frac12$ for all zeros with $|\operatorname{Im}\rho|\le T_0$ implies
> $\lambda_n\ge0$ for all $n\le T_0^{\,2}$"*, the reference being *"J. Oesterlé, Régions sans zéros
> de la fonction zêta de Riemann, typescript (2000, revised 2001, uncirculated)"*; he restates it
> in arXiv:2204.01036, §2.2.2, as *"$\operatorname{Re}\rho=\frac12$ holds up to a height $T_0$
> implies $\lambda_n>0$ as long as $n<T_0^{\,2}$"*. Maślanka 2004 records it heuristically:
> *"Oesterlé observed recently (in an unpublished note, …) that if the first $n$ complex zeros of
> zeta are located on the critical line, then the Li positivity criterion should hold for about the
> first $n^2$ Li coefficients"*. Voros 2006 states that Oesterlé *"had a proof of the statement …
> but he neither published nor even posted his typescript"*, and reproduces the argument; that
> argument concludes by the Riemann–Lebesgue lemma, i.e. as an $n\to\infty$ statement, and drops
> the fluctuation of the zero count (*"neglecting $\delta N(T)$ and other $O(\theta^{-\alpha})$
> terms: the error is $o(1)$"*). To the best of our knowledge **no published paper contains a
> complete rigorous proof** of the finite-height quadratic statement; what is published is the
> attribution, with the asymptotic argument alongside it.
>
> We therefore do not claim the quadratic range, and we do not claim the conversion of a verified
> height into a range for $\lambda_n$. The range proved here, $n\le2T-O(1)$, is **linear** in the
> verified height and is consequently smaller than the quadratic claim by a factor of order
> $T/2$; for $T=3.000175\cdot10^{12}$ this is a factor of about $1.5\times10^{12}$. What is
> claimed is narrower and, we hope, more durable: a proof of a linear window in which every step
> is elementary and every constant is explicit and numerically calibrated, so that the result is
> reproducible line by line, and a numerical study (§10) of the coefficients themselves, which
> measures the averaging behaviour that underlies the quadratic range and isolates precisely what
> a proof of it would still need (§11).

### 2.3 NUMERICS: direct computation of the Li coefficients from two million zeros (new subsection 10(v))

> **(v) Direct computation of the Li coefficients.** The verification of Theorem 1 is a check of a
> *criterion*; the coefficients themselves can also be computed directly. All zeros on the critical
> line contribute to $\lambda_n$ the quantity $1-\cos(n\theta_\gamma)$, with
> $\theta_\gamma=\arctan(\gamma/(\gamma^2-\tfrac14))\in(0,\pi/2)$, which is non-negative. Using the
> $2\,001\,052$ tabulated zeros of \cite{Odlyzko} (largest ordinate $\gamma_{\max}=1.132\,490\,66
> \cdot10^{6}$) we computed the partial sums
> $$S_n=\sum_{\gamma\le\gamma_{\max}}\bigl(1-\cos(n\theta_\gamma)\bigr).$$
> Every $S_n$ is **positive**: $S_{10}=1.1396$, $S_{10^3}=1.1621\cdot10^{3}$,
> $S_{10^5}=2.2209\cdot10^{5}$, $S_{10^6}=1.9867\cdot10^{6}$, $S_{10^9}=2.0005\cdot10^{6}$.
> Two cautions must accompany this table, and we state them rather than let the reader infer them.
> First, **validity**: $S_n$ is a lower bound for $\lambda_n$ only after the contribution of the
> zeros above $\gamma_{\max}$ is bounded; those zeros are not known to lie on the critical line, so
> we use $\lambda_n\ge S_n-nB_{\gamma_{\max}}e^{\,n/(2\gamma_{\max}^2)}$ (Lemma 3). The phrase
> "positive partial sum" is *not* by itself a proof of positivity. Second, **informativeness**:
> for $n\gg\gamma_{\max}$ the phases $n\theta_\gamma\approx n/\gamma$ oscillate rapidly, each term
> averages to $1$, and $S_n$ saturates at the number of tabulated zeros ($\approx2.0\cdot10^6$);
> the rows at $n=10^{7},10^{8},10^{9}$ repeat that saturation and are *not* evidence of large
> $\lambda_n$. The informative range is $n\lesssim\gamma_{\max}$.
>
> The numerically interesting quantity is the deviation from the zero count,
> $D_n=S_n-N(\gamma_{\max})$, which is what a proof of the quadratic range would have to bound.
> Taking $T_0=\gamma_{\max}$ the endpoint $n=T_0^2=1.2825\cdot10^{12}$ is *inside* the range that
> the table can reach (the phases $n\theta_\gamma$ remain computable), so the following is a
> measurement, not an extrapolation:
> $$S_{T_0^2}=2.001269\cdot10^{6},\qquad D_{T_0^2}=+2.17\cdot10^{2},\qquad
> |D|/N=1.09\cdot10^{-4},$$
> i.e. a deviation from the count of about **one part in ten thousand** at the square of the
> height; against the tail term $nB_{T_0}$ with $B_{T_0}=9.2065\cdot10^{-7}$ this leaves a margin
> $S_n/(nB_{T_0})\approx1.69$. The relative deviation decays like a power of $T_0/n$ with fitted
> exponent $\alpha\approx0.54$ over four points ($R^2=0.845$); independently random phases would
> give $|D|/N\sim1/\sqrt N=7.1\cdot10^{-4}$ with no decay in $n$, so the observed decay is a
> structural effect. We stress the limitations: these are numbers for the actual zeros, not a
> bound valid for all configurations; the margin $1.69$ is computed with the asymptotic value of
> $B_{T_0}$, not with the explicit upper bound of Lemma 4 (which is larger by a factor $\approx3.2$
> and would leave a margin $\approx0.46$); and restoring the factor
> $e^{\,n/(2T_0^2)}\approx1.65$, legitimately discarded in Theorem 1 because $n\le2T$, would
> reduce it further. The honest reading is that the measurement supports the *shape* of the
> averaging behaviour, not the endpoint inequality with rigorous constants.

*Note for the authors:* the first table in the working script claims "the partial sum IS ALWAYS
$\le\lambda_n$. No restriction." **This justification is wrong** and must not be reproduced: the
omitted zeros above $T$ are not known to lie on the critical line, so the partial sum is a lower
bound only modulo the tail term. (The script also tabulates a tail column labelled $n^2B_T$ while
the probe script compares with $nB_T$; see Appendix A, items A1 and A2.)

### 2.4 REMARK (roadmap): the quadratic route

> **Remark (a quadratic route, and what remains open — a roadmap, not a theorem).** The prior
> quadratic statement $n\le T_0^{\,2}$ would follow from the argument of Oesterlé as reproduced by
> Voros, if the $o(1)$ produced there by the Riemann–Lebesgue lemma were made quantitative,
> *uniformly* for $n\lesssim T_0^{\,2}$. Nothing in this section is proved; we record the route and
> its status because it isolates a single explicit inequality.
> The starting point is the representation
> $\lambda_n=2\int_0^\infty[1-\cos n\theta(T)]\,dN(T)$ with $\theta(T)=2\arctan(1/2T)$ — the same
> phase as our $\theta_\gamma$, since $\tan\bigl(2\arctan(1/2T)\bigr)=T/(T^2-\tfrac14)$ — and one
> integration by parts. Splitting $\lambda_n$ into four pieces, the state of each is as follows.
> **(1) Fluctuation term,** $4\int_0^{T_0}\sin(n\theta(T))\,\delta N(T)/(4T^2+1)\,dT$ with
> $\delta N=N-\mathrm{main}$: using the classical bound $S(T)=O(\log T)$, this term is
> $O(\log T_0)$, *uniformly in $n$* — it is free, since the weight $1/(4T^2+1)$ makes the integral
> converge and no oscillation is needed. **(2) Boundary term:** the integration by parts produces
> $-\cos(n\theta(T_0))\,\mathrm{main}(T_0)$, of the same order as the signal; it can be made to
> vanish *exactly* by truncating at a height $T_0'$ with $\cos(n\theta(T_0'))=0$ instead of at
> $T_0$, which is legitimate because verification at height $T_0$ implies verification at every
> lower height; the cost is a shift $\delta\sim T_0^{\,2}/n$, i.e. a relative cost at most
> $T_0^{-1/2}$ over the range considered. **(3) Tail:** bounded classically by
> $nB_{T_0}e^{\,n/(2T_0^2)}$, and available from Lemma 3 of this paper. **(4) Interior
> oscillation,** $-2\int_0^{T_0'}\cos(n\theta(T))\,d\,\mathrm{main}(T)$: **open**. This is the only
> remaining step, and it is a single explicit inequality,
> $\bigl|\sum_{\gamma\le T_0}\cos(n\theta_\gamma)\bigr|<N(T_0)-nB_{T_0}$ for all
> $n\lesssim T_0^{\,2}$.
> Numerically this term has a **two-regime structure**. In the resonance regime — $n$ comparable
> to a zero ordinate, where the phase $n\theta_\gamma\approx n/\gamma$ aligns — spikes do occur:
> over a dense scan of $582$ values of $n$ (using $10^5$ zeros, largest ordinate $\approx7.49
> \cdot10^{4}$) the largest relative oscillation is $0.3791$, but there the allowance is still
> $\ge1.00\,N$, so the spikes are harmless. In the averaging regime there are no spikes (largest
> relative oscillation $0.0341$) — and this is exactly the regime in which the allowance
> $N-nB_{T_0}$ becomes tight. The requirement was tested pointwise at every scanned $n$ and held at
> $581$ of $582$; the single failure occurred where the allowance is already negative, i.e. beyond
> the quadratic endpoint, as expected. We do not claim that the required uniform bound is true, nor
> that the quadratic range follows; what we claim is that the four steps above reduce it to one
> inequality, and that the numerical evidence is consistent with it while the endpoint margin
> computed with rigorous constants is thin (see §10(v)).

### 2.5 WHAT THE PAPER DOES NOT CLAIM

> **What this paper does not claim.** (i) It does not prove the Riemann Hypothesis, nor any
> statement about the location of zeros above the verified height $T$; the result is a subset
> statement implied by RH. (ii) It does not claim the quadratic range $n\le T_0^{\,2}$, nor any
> improvement on it: that range is prior art, attributed to Oesterlé and reported by Biane–Pitman–Yor
> and by Voros, and our linear window is **smaller** by a factor of order $T/2$. (iii) It does not
> claim the conversion of a verified height into a range for $\lambda_n$ as new, nor as a
> "folklore" observation of ours; the attribution is to Oesterlé, with the published statements
> cited in §2. (iv) It does not claim that the quadratic statement has been proved false, or that
> no proof exists: what is absent from the literature, as far as we can determine, is a *published*
> proof, and Voros records that Oesterlé had one which he never circulated. (v) It does not claim
> that the numerical computation of §10(v) proves anything about the quadratic endpoint: those
> numbers describe the tabulated zeros, not all configurations, and with the explicit constants of
> Lemma 4 the margin at the endpoint is thin. (vi) The quadratic material in §11 is a roadmap: it
> contains no theorem, and the fourth of its four steps is open. (vii) Nothing here is claimed to be
> optimal beyond the sense made precise in Remark 9, namely optimality of $n\le2T$ *for the
> worst-case, pointwise-window method used in this paper*.

### 2.6 Bibliography additions (BibTeX)

```bibtex
@article{BPY2001,
  author  = {Biane, Philippe and Pitman, Jim and Yor, Marc},
  title   = {Probability laws related to the Jacobi theta and Riemann zeta functions,
             and Brownian excursions},
  journal = {Bulletin of the American Mathematical Society (N.S.)},
  volume  = {38}, number = {4}, pages = {435--465}, year = {2001},
  note    = {See \S2.3, p.~441}
}
@misc{Oesterle2000,
  author = {Oesterl{\'e}, Joseph},
  title  = {R{\'e}gions sans z{\'e}ros de la fonction z{\^e}ta de Riemann},
  howpublished = {typescript (2000, revised 2001, uncirculated)},
  note   = {Proposition 2; reported in \cite{BPY2001} and \cite{Voros2020,Voros2022};
            we have not seen the typescript}
}
@article{Voros2020,
  author = {Voros, Andr{\'e}},
  title  = {Discretized Keiper/Li approach to the Riemann Hypothesis},
  journal = {Experimental Mathematics}, volume = {29}, number = {4},
  pages = {452--469}, year = {2020}, note = {eq.~(13) and \S1.3.2}
}
@misc{Voros2022,
  author = {Voros, Andr{\'e}},
  title  = {From asymptotic to closed forms for the Keiper/Li approach to the
            Riemann Hypothesis}, year = {2022}, note = {arXiv:2204.01036; \S2.2.2},
  howpublished = {RIMS Kyoto workshop report, October 2021}
}
@article{Voros2006,
  author = {Voros, Andr{\'e}},
  title  = {<FILL IN FROM THE SOURCE -- not recorded in our reconnaissance>},
  journal = {Mathematical Physics, Analysis and Geometry}, volume = {9},
  pages = {53--63}, year = {2006}, note = {arXiv:math/0506326}
}
@article{Maslanka2004,
  author = {Ma{\'s}lanka, Krzysztof},
  title  = {Li's criterion for the Riemann hypothesis --- numerical approach},
  journal = {Opuscula Mathematica}, volume = {24}, number = {1},
  pages = {103--114}, year = {2004}
}
```

*Caveat on `Voros2006`:* the file `docs/P8b-oesterle-rigor-status.md` gives this paper's
bibliographic data as "Math. Phys. Anal. Geom. **9** (2006) 53–63 = arXiv:math/0506326" and
quotes it for the sentence "Oesterlé had a proof of the statement … but he neither published nor
even posted his typescript". The reconnaissance file does **not** record this paper's **title**, and
we do not supply one: fill it in from the arXiv record (arXiv:math/0506326) before pasting, or
cite it without a title as "A. Voros, arXiv:math/0506326 (2006)".

---

## 3. Every existing sentence that must change or be deleted

### 3.1 `papers/li-range/li-range.tex`

| # | Quoted sentence (verbatim, LaTeX) | Verdict | Reason |
|---|---|---|---|
| 1 | `about $6\cdot 10^{7}$ times the range reached by direct computation of $\lambda_n$ in the literature.` | **DELETE** | The comparison object is the range of *direct computation* ($n\le10^5$), which is a limit of computing power, not of knowledge. The honest comparison is with the prior *mathematical* claim $n\le T_0^{\,2}$, against which we are weaker by a factor $\approx T/2$. This is the single most damaging sentence in the paper. |
| 2 | `For the verified height $T=3.000175\cdot 10^{12}$ this gives $n$ up to approximately $6.00035\cdot 10^{12}$,` | keep, but must be **immediately followed** by the comparison with $T_0^{\,2}$ | As it stands it invites the reader to read the number as a record. |
| 3 | `No hypothesis is assumed.` | **REWRITE** to "No unproved hypothesis about the zeros above $T$ is assumed." | The theorem is conditional on (i) the verified-height hypothesis and (ii) the numerical criterion (the display labelled `eq:criterion` in the manuscript). "No hypothesis is assumed" is literally false for the general statement in Theorem 1. |
| 4 | `Direct numerical verification of $\lambda_n\ge0$ has been carried out up to $n\le10^{5}$ (see \cite{Palojarvi,Coffey} and the references therein).` | **REWRITE** | True as written, but it is the sentence that sets up the wrong comparison. It must be accompanied by the prior *conversion* result (Oesterlé, via BPY 2001 §2.3 p. 441 / Voros 2020 eq. (13)), otherwise the reader concludes the state of the art is $10^5$. |
| 5 | `The purpose of this note is to show that, using only a \emph{verified height} $T$ as input, one obtains an explicit range $n\le 2T-O(1)$ by elementary estimates, and that no information about the zeros above $T$ is needed beyond a bound on their worst-case contribution.` | **AMEND** | Add: the conversion itself is prior art (attributed to Oesterlé); what is offered here is the elementary explicit *linear* form. |
| 6 | `We do not claim novelty for the conversion of a verified height into a range for $\lambda_n$, which is a folklore consequence of $|1-1/\rho|=1$ on the line and $|1-1/\rho|>1$ off it; what is given here is an elementary, explicit, and numerically calibrated form of the resulting range.` | **REPLACE** | "Folklore" is the wrong attribution: the conversion is attributed to Oesterlé (uncirculated 2000 typescript), was first published in BPY 2001 §2.3 p. 441 with the quadratic bound $n\le2.975\ldots\times10^{17}$, and is reported in Voros 2020 eq. (13). Also, "explicit range $n\le2T-O(1)$" must be contrasted with "$n\le T_0^{\,2}$ is prior art and larger". |
| 7 | `Consequently, within this method the range is optimal in $T$, and it can be extended only by verifying the hypothesis to a greater height --- a different mechanism, not a sharper estimate, would be needed to go beyond it.` | **SOFTEN** | "Optimal" is claimed without qualification. The argument establishes optimality of $n\le2T$ for the *worst-case pointwise-window* method only; the quadratic literature shows that a different mechanism (averaging) escapes the ceiling, which the remark itself concedes in the next clause. Say "optimal for this method", and point to §11. |
| 8 | `Second, the two quantities being compared are both linear in $n$: the on-line count in the window is of order $(1.5\,n/2\pi)\log n$, while the off-line cost is at most $nB_T^{\rm exp}$. The criterion \eqref{eq:criterion} is therefore independent of $n$ up to a factor $\log n$, and the off-line term is never the binding constraint.` | **REWRITE** | Imprecise and internally in tension with the paper's own endpoint analysis (Lemma 4's $B_T^{\rm exp}$ sets the required count $\approx140$ at the endpoint, so it does enter the endpoint). Say instead: the ceiling $n\le2T$ is geometric (the window $[n/2,\min(2n,T)]$ must be non-empty and lie below $T$), and no improvement of $B_T$ can move it; $B_T$ only affects the $O(1)$ deficit. |
| 9 | `The companion note \cite{BT26} sharpens the treatment of the sum over distant zeros in a different direction, namely for the input inequality of the classical converse theorem, but for the reason just given it does not widen the range here.` | **REVIEW, probably DROP** | It cites an unpublished draft of the author's own. Unless the companion note is available to the referee, this weakens the paper; if kept, mark it as a draft not submitted. |
| 10 | `Consequently, with the range $1\le n\le10^{5}$ supplied by the direct verifications of \cite{Palojarvi,Coffey}, one has $\lambda_n\ge0$ for every integer $n$ with $1\le n\le N_{\max}(T)$,` | **AMEND** | "supplied by the direct verifications" must be labelled as *computational validation* and explicitly not as the prior mathematical range. |
| 11 | `We prove by elementary means that the Li coefficients satisfy $\lambda_n\ge 0$ for every integer $n$ with $2\le n\le 2T-O(1)$.` (Abstract) | keep | True; the theorem is what it is. Keep the word "linear" adjacent to it so the shape is visible at once. |
| 12 | Bibliography entries | **ADD** | BPY 2001; Oesterlé typescript; Voros 2006; Voros 2020; Voros arXiv:2204.01036; Maślanka 2004 (BibTeX in §2.6). Without these, the paper's comparison is indefensible. |

### 3.2 `papers/li-range/SUMMARY-1page.md`

| # | Quoted text (verbatim) | Verdict | Reason |
|---|---|---|---|
| 1 | `**λ_n ≥ 0 for all integers 2 ≤ n ≤ 2T − O(1)**. With T = 3.000175·10¹² (Platt–Trudgian, interval arithmetic) this is **n ≤ ≈ 6.00035·10¹²**, i.e. **≈ 6·10⁷ times** the direct computational range n ≤ 10⁵ (Palojärvi; Coffey).` | **DELETE the comparison clause** | As above: comparing with a computational limit. Replace with the comparison to $T_0^{\,2}$: our range is smaller by $\approx T/2 \approx 1.5\times10^{12}$. |
| 2 | `The height-to-range conversion is not claimed as new (folklore); the contribution is its explicit, elementary and calibrated form.` | **REPLACE** | Not folklore: attributed to Oesterlé (uncirculated), published in BPY 2001 §2.3 p. 441 (quadratic), restated by Voros 2020 eq. (13) and Maślanka 2004. The contribution is the *linear*, explicit, elementary, calibrated form — and, if §11 is included, the numerical study of the averaging structure. |
| 3 | `- **Subset result**, not a proof of RH. Unconditional given T.` | keep | Accurate. |
| 4 | `## Numerical calibration` block (λ₁ calibration, exhaustive $n\le20000$, margins, endpoint $1.03$) | keep, **extend** | Add the direct computation from the two million zeros (§2.3) with its caveats. |
| 5 | `- **Off-line bound:** zeros above T contribute at worst −n·B_T` | keep, **add** the factor $e^{n/(2T^2)}$ | The paper's Lemma 3 bound is $-nB_Te^{\,n/(2T^2)}$; the exponential is harmless for $n\le2T$ but must be written, because it is *not* harmless in the quadratic regime discussed in §11. |

### 3.3 Submission e-mails (`papers/li-range/EMAIL-endorsement-long.txt`, `…-short.txt`)

Both contain the same defective claim and must not be re-sent as they stand:

- long: `n ≤ ≈ 6.00035·10¹², roughly 6·10⁷ times the range reached by direct computation of λ_n (n ≤ 10⁵, Palojärvi; Coffey).`
- short: `For T = 3.000175·10¹² this gives n up to ≈ 6.00035·10¹², about 6·10⁷ times the range reached by direct computation of λ_n in the literature (n ≤ 10⁵).`

Verdict: **rewrite before any further use**; the honest one-line version is "a *linear* window
$n\le2T-O(1)$, proved elementarily with explicit constants; the quadratic window $n\le T_0^{\,2}$
reported by Biane–Pitman–Yor (2001) and Voros (2020) is prior art and larger".

### 3.4 Statements that are simply *wrong* (said plainly)

1. **"≈6·10⁷ times the range reached by direct computation"** framed as a comparison with the
   literature's knowledge: wrong. The correct comparison is $2T$ vs $T_0^{\,2}$; we are *smaller*
   by $\approx T/2$.
2. **"the conversion … is a folklore consequence"**: wrong attribution (see 3.1 #6).
3. **`PAPERA_num_enrich.txt`, line "VALIDITY: … so the partial sum IS ALWAYS ≤ λ_n. No
   restriction."**: **wrong**. The zeros above $T_0$ are not known to be on the critical line; the
   partial sum is a lower bound for $\lambda_n$ only after subtracting the worst-case tail
   $nB_Te^{\,n/(2T_0^2)}$. Positive partial sums do not by themselves prove $\lambda_n>0$.
4. **`PAPERA_num_enrich.txt`, tail column labelled $n^2B_T$**, versus `PAPERA_avgcase_probe.py`
   which compares with $nB_{T_0}$: the two files report different "ends of the informative range"
   ($\approx1.5\cdot10^6$ versus $\approx2T_0^2$). One convention must be fixed and stated (see
   Appendix A, A1–A2).
5. **"the off-line term is never the binding constraint"** (Remark 9): as written, misleading;
   see 3.1 #8.

---

## 4. Assessment: is the revised paper worth submitting?

Verdict: **yes, but only as an explicitly positioned methods/notes paper — and only if §2.2 and
§2.5 are in it, verbatim in substance.** The theorem is true and its proof is short, elementary
and reproducible, but its headline number is *weaker* than a claim that has been in the literature
since 2001; a referee will find this in minutes, and a paper that appears to hide it should be
rejected. Reframed, the honest selling points are: (a) a complete, elementary, explicit-constant
proof of a linear finite-height window, which the reconnaissance did not find stated in this form
anywhere — the novelty is the *proof and the constants*, not the range; (b) a numerical study of
the coefficients themselves from two million zeros, which measures the averaging that underlies the
quadratic claim ($|D|/N\approx1.1\cdot10^{-4}$ at $n=T_0^2$) and exhibits a two-regime structure
(spikes with a large allowance at small $n$; no spikes and a tight allowance in the averaging
regime) — a picture we could not find in the literature; (c) a precise localisation of what a proof
of the quadratic range still needs, i.e. one explicit inequality, presented as a roadmap and not as
a result — and, if the later note `docs/PAPERA-two-regime-attempt.md` is taken up, the *negative*
result that three standard oscillation estimates fail quantitatively in the averaging regime, which
is itself useful methodological content (why bounding the interior term cannot work, and that one
must evaluate it, as the prior argument does). Two warnings. First, expected value is low-to-moderate: the paper cannot claim a record,
and a referee may say "this is a special case of what Oesterlé already had". Second, the
reconnaissance in this repository (`docs/RETRACTION-A1-li-range-2026-09-11.md`) records a
non-peer-reviewed source asserting a machine-checked explicit assembly of the quadratic range; that
source has **not** been verified here, but before any claim of "first published explicit window" is
made, that must be checked, because it would remove even the priority argument. If a *range* claim
is what is wanted, the reconnaissance points to a genuinely empty spot not occupied by
Oesterlé/BPY/Voros: the *negativity* side — an explicit threshold $N(T)$ such that an off-line zero
with $|\Im\rho|\le T$ forces $\lambda_n<0$ for some $n\le N(T)$ — which is a different paper.

---

## Appendix A. Audit notes and open verification items (not for the paper)

**A1 — Tail convention, $nB_T$ vs $n^2B_T$.** `scripts/PAPERA_num_enrich.txt` §(1)–(2) tabulates a
tail column labelled $n^2B_T$ and concludes that the informative range ends near $n\approx1.5\cdot10^6$;
`scripts/PAPERA_avgcase_probe.py` states the criterion as $S_n>nB_{T_0}$ and locates the endpoint at
$n\approx2T_0^2$. Both are valid bounds (for $2\le n\le T_0^2$ one has $n^2B_T\ge nB_Te^{n/(2T_0^2)}$,
since $e^{n/(2T_0^2)}\le e^{1/2}\le n$ there), but they answer different questions. The paper must state which tail bound it uses
and why. Recommend: quote the sharp one, $nB_Te^{\,n/(2T^2)}$ (Lemma 3), and use $n^2B_T$ only if a
crude but elementary bound is wanted.

**A2 — Exponential factor at $n\sim T_0^2$.** Theorem 1 legitimately absorbs
$e^{\,n/(2T^2)}=1+O(1/T)$ because $n\le2T$. In the quadratic regime $n\sim T_0^2$ this factor is
$e^{1/2}\approx1.65$, of order one. Consequently the measured margin $1.69$ at $n=T_0^2$
(`PAPERA_avgcase_probe.txt`, "margin $S_n/(nB_{T_0})=1.6949$") is *not* the margin against the
bound the paper actually proves: using Lemma 4's explicit $B_T^{\exp}\le3.4015\cdot10^{-6}$ at
$T_0=1.13249\cdot10^6$ the margin becomes $\approx0.46$, and with the exponential factor restored
$\approx0.28$. The numerical support for the quadratic endpoint is therefore weaker than the
roadmap's headline suggests. This does **not** affect Theorem 1 (the linear window), which uses
$n\le2T$.

**A3 — Summation convention in Lemma 3.** Lemma 3 bounds the contribution of a *single* zero
$\rho=\beta+i\gamma$ with $\gamma>T$ by $-nc_\rho e^{nc_\rho}$, and the proof of Theorem 1 then
sums "$\Sigma_{\gamma>T}$" against $B_T=\tfrac12\Sigma_{\gamma>T}\gamma^{-2}$. Whether the
conjugate zero with ordinate $-\gamma$ is included in that sum should be stated explicitly; if each
zero of the pair is counted separately, the per-pair cost is $2\times$ the single-zero bound and
the constant in the theorem must be adjusted correspondingly (the numerical safety factor of
Lemma 4, $\approx3.2$–$3.7$ times the nominal value, would absorb it, but the statement should be
correct on its own). Worth ten minutes of checking.

**A4 — The relative-cost figure $T_0^{-1/2}$ for step (2).** `scripts/PAPERA_oscillation_attack.txt`
records the phase-zero truncation cost as $\delta\sim T_0^2/n$, i.e. relative error $T_0/n$, and
concludes "at most $T_0^{-0.5}$ for the whole range $n\le T_0^2$". Read literally, $T_0/n\le
T_0^{-1/2}$ requires $n\ge T_0^{3/2}$; at smaller $n$ in the range the relative cost is larger
(and for $n\ll T_0$ it exceeds $1$, so no phase zero is reachable below $T_0$). Since §11 only
needs $n\gg2T_0$, the claim is probably intended in that regime — but it should be stated with its
range of validity.

**A5 — Fit quality.** The power-law fit for the fluctuation decay rests on four points and a single
optimisation (exponent $\alpha=0.539$, $R^2=0.845$); the fit was recomputed after an $R^2$ sign
error was corrected in the script output. Report it as "indicative, four points", never as a law.

**A6 — Typography of $T$.** In the Introduction the verified height is written
`$T=3.000175\,332\,800$`, i.e. $3\,000\,175\,332\,800$ with thin-space thousand separators,
whereas the abstract and Theorem 1 write $T=3.000175\cdot10^{12}$. Both denote the same number, but
the juxtaposition invites a misreading (and would become a $10^{12}$-fold error if the exponent were
copied into the first form). Recommend writing the Introduction form as
`$T=3.0001753328\cdot10^{12}$` as well.

**A7 — Terminology.** The word "verified" is used in two senses: RH is verified *by interval
arithmetic* up to $T=3.000175\cdot10^{12}$ (Platt–Trudgian), whereas the numerics of §10(v) use a
zero table complete only up to $\gamma_{\max}=1.13249\cdot10^6$. The paper must never let the two
heights be conflated; the quadratic-endpoint measurement is at $n=T_0^2$ with $T_0=\gamma_{\max}$,
not with the Platt–Trudgian height.
