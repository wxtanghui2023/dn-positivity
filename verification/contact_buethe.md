# Contact Letter — Jan Büthe（C3 / Weil–Barner / distributional attack）

**Subject:** Adversarial check of a distributional pairing in a candidate criterion — C3 question

Dear Dr. Büthe,

I am writing to ask for an **adversarial mathematical check** of one
specific technical part of a candidate criterion equivalent to the
Riemann Hypothesis — not for an endorsement.

Because your work on the Weil–Barner explicit formula is directly
relevant, I would value your attack on the **distributional pairing
step (C3)** of the construction. The setting is:

- $H_0(t) = -\frac{1}{4\pi}\log(1+t^2) + \frac{1}{2\pi(1+t^2)}$, with
  $H_0''(t) = O(t^{-2}) \in L^1$ (note $H_0 \notin L^1$);
- pairings are defined **termwise** through $L^1$ Fourier products
  $\widehat K_\delta \widehat H_0 \in L^1$ (the naive global pairing
  $\langle \log|\xi|, H_0''\rangle$ diverges and is **not** used);
- the question is whether the Parseval/Fourier normalization, the
  $\delta = 0$ singular-kernel treatment, and the interchange of
  per-zero pairing with spectral summation are legitimate under the
  hypotheses of the Weil/Barner explicit formula as invoked.

**The question I would value most is:** Is the termwise distributional
pairing framework (C3.1–C3.5) valid as stated — i.e., can you find an
illegal Parseval use, a missing boundary term, a convention slip, or a
hypothesis of the Weil–Barner framework that $H_0$ fails to satisfy?

I am deliberately **not** providing the derivation history, previous
failed attempts, or internal assessments — only the definitions, the
formal checks, and the INVALID-first protocol.

The self-contained material (definitions O1–O5, checks C1–C5, theorem,
and an INVALID-first protocol) is available at:
- Zenodo: DOI 10.5281/zenodo.22044629 (latest release v3.0.0)
- GitHub: https://github.com/wxtanghui2023/dn-positivity

Any verdict — VALID, INVALID, or UNJUSTIFIED — on C3 would be genuinely
valuable. I am grateful for any time you can give this.

Sincerely,

Hui Tang
Independent Researcher
wxtanghui@gmail.com
ORCID 0009-0003-5745-4820
