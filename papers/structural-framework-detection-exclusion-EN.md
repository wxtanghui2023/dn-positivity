# A Structural Framework for Detection without Exclusion

**From Detection to Exclusion: Structural Boundaries in Riemann-Type Problems**

**Hui Tang** -- 2026-09-01 -- v1 (structural audit)

---

## Abstract

We present a structural audit of a unified framework for the Riemann Hypothesis (RH) and related conjectures (GRH, Goldbach, Twin Prime). The contribution is not a proof of RH, but a precise answer to the question: **why do a large class of RH-type structures stably produce critical-line signals (detection), yet fail to produce an exclusion mechanism?**

The paper is organized in four layers:

- **I. Unconditional structural layer.** $A_{min} \Rightarrow F_U$ (Euler product, explicit formula, prime statistics, orbit structure, positivity, variational principle -- RH does not enter the axioms).
- **II. Detection layer.** prime data $\Rightarrow$ beta-sensitive observables (amplitude, Mellin, $V(T)$, moment spectra) -- **beta can be detected** (but not forced).
- **III. Exclusion layer.** We define a *rigidity mechanism*: independent construction + beta-sensitive observable + uniform coercivity. Only the third ingredient upgrades detection into exclusion. The audit P5.9 lives here.
- **IV. Rigidity Gap.** **Detection $\not\Rightarrow$ Exclusion.** The missing bridge is not more data, not a prettier representation, but **independent rigidity / coercivity**.

**Frozen conclusions (three statements):**
1. **Detection is unconditional; exclusion requires additional rigidity.**
2. **The audited positive-kernel constructions do not yield uniform coercivity.**
3. **No independent coercive mechanism was identified within the audited framework.**

The positive-definite/spectral-gap audit (P5.9) confirms: Gram positivity does not imply uniform coercivity; available nontrivial positivity mechanisms lead to RH-level information. The paper does **not** prove that a third mechanism cannot exist in the mathematical universe -- only that none was found within the audited scope.

**Key epistemological asset:** a reusable method for recognizing mechanisms that *look like RH proofs but are only detection*.

---

## 1. Introduction: Detection versus Exclusion

### 1.1 The precise question

After systematic exploration of ~30 independent routes (positivity, spectral, trace, realizability, arithmetic geometry, positive-definite kernels, variational, energy, dynamics, statistics), one phenomenon recurs:

> Every model can **detect** off-critical-line zeros ($\beta \ne 1/2$ leaves a different signal), but no model can **exclude** them (prove $\beta \ne 1/2$ incompatible with unconditional structure).

This is not an accidental failure but a structural fact: the channel from unconditional arithmetic structure (Euler product / explicit formula / functional equation) to beta-sensitive observables is **lossless and self-adaptive** -- it encodes off-axis information (detection) but produces no exclusion (constraint).

### 1.2 What this paper is not

- Not a proof of RH (no claim that $\beta = 1/2$).
- Not a disproof of RH (no claim that off-axis zeros exist).
- Not "yet another RH-equivalent condition" ($D = \sum P_\gamma$ is explicitly labeled as an equivalent criterion -- new organization, not new mechanism).

### 1.3 What this paper is

A structural audit of the unified framework: establishing the unconditional skeleton, precisely characterizing the detection-exclusion separation, giving a logical-strength map, performing a framework distortion test, and proposing the *rigidity gap* as the structural obstacle every successful RH mechanism must cross.

---

## 2. Layer I: The Unconditional Skeleton $F_U$

### 2.1 Definition

$$F_U = (\mathcal A_U, \mathcal R_U, \mathcal O_U)$$

- **$\mathcal A_U$ (unconditional inputs):** $A_1$ prime point process; $A_2$ Euler product ($\sigma>1$); $A_3$ analytic continuation + uniqueness; $A_4$ Gamma properties + functional equation. **RH $\notin \mathcal A_U$.**
- **$\mathcal R_U$ (strict reasoning):** all unconditional theorems derivable from $\mathcal A_U$.
- **$\mathcal O_U$ (computable observables):** $\theta(t)$, $V(T)$, $V_p(T)$, Mellin observables, $P_\gamma$, $S(p)$, duality density -- computable from prime data or zero data.

### 2.2 Minimal generating set

$$A_{min} = \{A_1, A_2, A_3, A_4\}$$

(prime point process / Euler product / analytic continuation / Gamma). $A_{min}$ generates all of $\mathcal R_U$. **$A_{min}$ does not contain RH** -- the unconditional layer does not depend on any conjecture.

### 2.3 Status of the unconditional theorems

Following a formal audit (T1-T10), the unconditional layer contains:
- **New algebraic closed forms:** the paired positivity $P_\gamma(\delta) = \delta^2 M_2/(2U^2 D_+ D_-) \ge 0$ (orbit pairing + all-positive coefficients).
- **Self-contained estimates:** $\int f_n S g = O(1)$ (Titchmarsh truncation + van der Corput + stationary phase).
- **Reorganizations of classical results:** the $V(T)$ exponent map (L2 mean vs $\beta_{max}$ -- classical theme, Gallagher-type), phase locking (corollary of Guinand/Weil), duality conservation (elementary consequence of PNT + Riemann-von Mangoldt).

We do not claim classical results as new theorems; the framework's contribution is the organization and the logical-strength map, not the originality of every component.

---

## 3. Layer II: Detection -- beta can be detected

### 3.1 Formalization

- **Detect($O$, beta)**: observable $O$ is sensitive to beta -- there exists an off-axis configuration where $O$ differs from its on-line value.
- **Exclude($O$)**: there exists an unconditional theorem -- $O \in \mathcal C \Rightarrow \beta = 1/2$.

### 3.2 Main observation: Detect $\ne$ Exclude

All experiments (E1-E9) confirm: many observables satisfy Detect (e.g., $V(T)$ changes by a factor 13.6 at $\delta = 0.2$), but no known unconditional mechanism satisfies Exclude.

### 3.3 Why the separation (structural explanation)

The channel from $\mathcal A_U$ to beta-sensitive observables is lossless and self-adaptive (the explicit formula holds for any zero configuration; prime data and zero configurations are coupled only through the identity channel). An identity channel produces equalities (encoding the off-axis cost $D \ge 0$) but not inequalities (cannot encode the exclusion $D \le 0$). Any quantity crossing both sides is either an identity (self-adaptive) or independent (no connection).

---

## 4. Layer III: Logical-strength spectrum C0-C4 (strict version)

### 4.1 Definitions (precise meaning)

```
C0:   V < infinity            (full integral converges)
C1_a: V(T) = O(T^-a)          (fixed a in (0,1] -- L2 tail decay)
C2:   V(T) = O(T^-1+eps)      (all eps > 0 -- L2 tail, eps-relaxed)
C3:   V(T) = O(T^-1)          (L2 tail -- exact, no eps)
C4:   psi(x) - x = O(x^1/2+eps)   (pointwise, all eps > 0)
```

C0-C3 are in the **L2 tail** sense (integral); C4 is **pointwise**.

### 4.2 Preliminaries (Lemma 1-4)

- **Lemma 1 (L2 upper bound):** $\beta_{max} \le \beta \Rightarrow V(T) = O(T^{2\beta-2+\varepsilon})$ -- unconditional (explicit formula + Hadamard convergence + van der Corput + zero-spacing lower bound).
- **Lemma 2 (zero spacing):** $\gamma_{n+1} - \gamma_n \ge c/\log \gamma_n$ -- unconditional classical.
- **Lemma 3 (L2 lower bound):** audited -- see Sec. 4.3 (hostile audit: NOT ESTABLISHED).
- **Lemma 4 (functional equation bridge):** $\beta_{max} \le 1/2 \Leftrightarrow$ RH -- unconditional (functional equation).

### 4.3 The lower-bound obstruction (Lemma 3 hostile audit + P5.9)

**Proposition (Lower-bound obstruction).** The attempted lower-bound route reduces exclusion of off-critical-line zeros to a uniform coercivity estimate for an oscillatory quadratic form. Classical zero-density and spacing estimates, together with the elementary Gram positivity of the associated kernel, **do not by themselves provide** such a coercivity estimate.

Precise content:

- $V(T) = D(T) + X(T)$ -- diagonal quadratic form $D$ (off-axis contribution, correct scale $T^{2\beta-2}$) plus cross terms $X$.
- Uniform coercivity requires $X(T) \ge -(1-\eta)D(T)$, $\eta > 0$ independent of $T$.
- **Density control does not imply phase-correlation control.** Ingham-type estimates count zeros ($N(\sigma,T)$) but do not control the oscillatory quadratic form $\sum_{j\ne k} a_j a_k e^{i(\gamma_j-\gamma_k)\log T}$.
- The minimal-counterexample test (abstract exponential sums $F(u) = \sum_j a_j e^{(\beta+i\gamma_j)u}$) shows that partial cancellation is constructible within spacing/counting constraints; full cancellation (a counterexample to the weak lower bound) was not constructed but cannot be excluded.
- The Gram reformulation $V(T) = \langle a, K_T a\rangle$ gives unconditional (trivial) positivity $K_T \succeq 0$ -- a Hilbert-space geometry fact -- but not the coercivity $\langle K_T a, a\rangle \ge \eta\|a\|^2$ with $\eta > 0$ uniform in $T$. Gershgorin-type bounds fail (harmonic divergence of cross-term moduli); the required phase cancellation depends on the actual zero structure (potentially RH-level).

**Wording boundary (frozen):** not "no such coercivity exists", but "**do not by themselves provide**". Not "the intermediate layer does not exist", but "**No independent intermediate coercive mechanism was identified within the audited classes**".

### 4.4 Condition strength table (final -- no vague "~")

| Condition | Proved direction | Relation to RH | Meaning |
|---|---|---|---|
| C0 | unconditional (PNT) | strictly weaker (any beta_max < 1) | L2 |
| C1_a (a<1) | unconditional (iff beta_max <= (2-a)/2) | strictly weaker | L2 |
| C1_1 (a=1) | both directions | iff RH | L2 |
| C2 | RH => C2 strict; C2 => RH open (coercivity) | one direction strict; equivalence not established | L2 |
| C3 | C3 => C2 (strict); C3 => RH via C2 (obstruction) | RH => C3 requires separate proof | L2 |
| C4 | classical | iff RH | pointwise |

### 4.5 Logical implication graph (only proved arrows)

```
        C4 (pointwise)
       /  \
      /    \              ---- unconditional implication (proved)
     v      v             - - - open / needs extra technical condition
    C3     RH
     \      /
      v    v
    C2 (V(T)=O(T^-1+eps))
      |
      v
    C1_a (a<1) -- strictly weaker than RH
      |
      v
    C0 (V<infinity) -- unconditional -- too weak
```

**Proved:** C4=>C3 (pointwise=>L2), C4<=>RH (classical), C3=>C2, C2=>C1_a (a<1), C1_a=>C0, C1_1<=>RH, RH=>C2 (strict).
**Open:** C2=>RH (coercivity), RH=>C3 (cross-term log factor), C3=>RH (via C2 -- same obstruction).
**Non-existent reverses:** C0 not=> C1_a, C1_a not=> C2 (a<1), C3 not=> C4 (L2 not=> pointwise).

### 4.6 The meaning of the spectrum

The more one wants an observable to genuinely *exclude* off-axis zeros, the closer one gets to RH itself. C2 is an L2 version of the classical $\psi(x) = x + O(x^{1/2+\varepsilon})$ equivalence; the attempted proof of C2=>RH reduces to a uniform coercivity problem that classical tools do not resolve.

---

## 5. Layer IV: Rigidity Gap and the classification of exclusion mechanisms

### 5.1 Definition (conceptual quantity -- not a standard mathematical definition)

$$G = \text{beta-sensitive information} - \text{independent rigidity}$$

### 5.2 Rigidity mechanism (formal object of the exclusion layer)

A structure $M$ has **exclusion power** if it satisfies:

$$\text{independent construction} + \text{beta-sensitive observable} + \text{uniform coercivity (independent of zero positions)}$$

Only the third ingredient upgrades detection into exclusion.

### 5.3 Unified classification table (audited mechanisms)

| Mechanism | beta-sensitive | independent | coercive | exclusion |
|---|:--:|:--:|:--:|:--:|
| Euler/Mellin | yes | yes | no | no |
| explicit formula | yes | yes | no | no |
| scattering | yes | yes | no | no |
| Arakelov | indirect | yes | no | no |
| THH/TP | partial | yes | no | no |
| positive kernels | yes | partial | conditional | no |
| L2 tail (K_T) | yes | yes | **missing** | no |
| hypothetical HP | yes | if exists | yes | yes |

**Contribution of P5.9:** the "coercive" entry for the L2 tail route is upgraded from "not found" to "**missing (structural -- at the spectral-gap level)**".

### 5.4 Weil positivity: careful wording (avoid over-broad definitions)

- "Nontrivial positivity iff RH" refers specifically to the **positivity of the particular Weil quadratic form $W(f,f) \ge 0$** -- not a generic "nontrivial positivity is equivalent to RH".
- The Gram kernel $K_T \succeq 0$ is a Hilbert-space geometry fact (holds for any configuration).
- What is genuinely needed is coercivity: $\langle K_T a, a\rangle \ge \eta\|a\|^2$ with $\eta > 0$ uniform in $T$. **The two notions are kept strictly separate throughout.**

---

## 6. P5.8 Framework distortion test ($W_\delta$)

### 6.1 Construction

An RH-agnostic surrogate world $W_\delta$ satisfying all 15 unconditional constraints of $F_U$ (Euler-type multiplicativity, PNT-scale asymptotics, functional symmetry, prime correlations, $P_\gamma$-type positivity, $C_2$ structure, universal scaling laws) but with $\beta_{max} = 1/2 + \delta$. $W_\delta$ is an abstract self-consistent "other world" (not a forged off-axis zeta -- that would touch RH itself).

### 6.2 Result (precise wording)

**Within the abstract system of the 15 defined unconditional constraints, the constructed $W_\delta$ is excluded by none of them; the constraint system itself therefore provides no logical separation for RH.**

### 6.3 Honest boundary (self-critical)

**P5.8 does not establish the non-existence of a rigidity principle; it establishes only that no such principle was obtained within the audited framework.** A future rigidity principle must come from a new object (providing independent rigidity), not a new representation (observable).

---

## 7. Common arithmetic architecture of RH/GRH/Goldbach/Twin Prime

### 7.1 The $P_\gamma$ structure as common architecture

$$P_\gamma \longrightarrow \begin{cases} \text{RH channel} & (\beta = 1/2 \text{ boundary}) \\ \text{Goldbach channel} & (C_2 \text{ constant}) \\ \text{Twin-prime channel} & (C_2 \text{ constant}) \end{cases}$$

The three conjectures share the $P_\gamma$ skeleton (orbit pairing + algebraic positivity -- unconditional) and the $C_2$ constant (numerical: $C_2 = 0.661377 \approx 0.6601618$ known -- shared by the twin-prime asymptotic and the Goldbach singular series).

### 7.2 Explicit boundary

**common architecture $\ne$ common proof.** The $C_2$ numerical agreement is computational evidence / structural observation -- **not a theorem** (no strict derivation of the $C_2$ asymptotics). The "commonality" is same-source (different channels of the same $P_\gamma$ object), not "one theorem implying all three". The candidate "more fundamental realizability theorem" (existence + unique stable realization) remains open -- "unique stable realization" is unproved (it is the variational form of RH).

---

## 8. Methodology: recognizing "looks like an RH proof, actually only detection"

### 8.1 Criteria (reusable asset)

A mechanism is *detection* rather than *proof* if it satisfies any of:

1. **Equivalence:** its core condition is equivalent to RH (e.g., C2 -- L2 version of $\psi = x + O(x^{1/2+\varepsilon})$) -- circular.
2. **Self-adaptivity:** its positivity/identity holds for any zero configuration (Weil, explicit formula, orbit positivity $P_\gamma \ge 0$ -- penalty, not exclusion).
3. **Zero-dependence:** its positivity/spectral construction needs zero knowledge (de Branges, Hermite-Biehler, intertwining operators) -- circular.
4. **Numerical support:** its "evidence" is numerical ($\beta \approx 1/2$ -- five probes) -- detection, not constraint.
5. **Unconstructed:** it depends on an unconstructed object (Theta, dynamical attractor, characteristic polynomial) -- unauditable.

### 8.2 Application

These criteria screen any newly proposed "RH proof" candidate: does it provide independent rigidity, or is it a repackaged detection? **This is a rare and genuinely reusable research asset after such a broad search.**

---

## 8.5 Uniform coercivity is not controlled by density statistics alone

### 8.5.1 The precise question (difference-spectrum analysis)

For the arithmetic-direction functional
$$F_\Lambda(\theta) = \sum_{j,k} a_j \bar a_k K_c(\gamma_j - \gamma_k) e^{i(\gamma_j-\gamma_k)\theta}, \qquad a_j = 1/\rho_j,$$
write $F(\theta) = b_0 + \sum_{r\ne 0} b_r e^{ir\theta}$. Then
$$\inf_\theta F(\theta) \ge b_0 - \sum_{r\ne 0}|b_r|,$$
so coercivity requires control of the **maximal negative deviation** of the difference spectrum (not its total variation; positive deviations do not affect the infimum).

### 8.5.2 Rigidity ladder (R0-R4)
- R0: global density -- does not give coercivity (lattice counterexample).
- R1: separation -- insufficient.
- R2: local discrepancy -- numerical attacks weaken but do not destroy coercivity (min margin ~ 0.016).
- R3: difference-set / additive-energy control -- empirically correlated with coercivity (E large => F small), but not decisive (quadratic counterexample).
- R4: uniform difference-spectrum rigidity -- the actual candidate; unidentified.

### 8.5.3 Empirical findings
- RvM-calibrated configurations: margin $\inf_\theta F/b_0$ decays slowly with J (numerically consistent with ~ c/log J; treated as numerical fit, not a theorem).
- Adversarial constructions preserving R0-R2 with low additive energy all fail to destroy coercivity (margins 0.08-0.78).
- The only configuration with margin -> 0 (dense lattice) violates the strong additive-energy bound.

### 8.5.4 Honest status (five layers)
| Layer | Status |
|---|---|
| $F \ge 0$ (Gram positivity) | strict |
| $F > 0$ (pointwise) | holds per configuration; not automatically uniform |
| $\inf_\theta F \ge \eta > 0$ (uniform coercivity) | **core unknown** |
| R0+R1+R2 imply uniform coercivity | unproved |
| zeta zeros satisfy the required condition | unknown |
| implies RH | not established / untouched |

### 8.5.5 The most precise form of the Rigidity Gap
> **Density information controls how many frequencies there are; coercivity controls how their difference spectrum can interfere at its worst phase.** The gap between these two information layers is the most precise form of the Rigidity Gap established in this work.

The honest conclusion: current experiments support the need for a difference-spectrum condition stronger than R0-R2, but no such sufficient condition has been identified. This is a well-posed harmonic-analysis problem, independent of zeta.

## 9. Conclusion: the killer diagram -- Detection not=> Exclusion

```
UNCONDITIONAL MATHEMATICS
     |
     +------------------+------------------+
     |                                     |
     v                                     |
beta-sensitive                      structural
observables                        identities
     |                                     |
     +------------------+------------------+
                        |
                        v
                  DETECTION
                        |
                        |  missing bridge (Rigidity Gap)
                        v
        +-----------------------------------+
        |   INDEPENDENT RIGIDITY /           |
        |   COERCIVITY                        |
        +-----------------------------------+
                        |
                        v
                   EXCLUSION
                        |
                        v
                       RH
```

**The question mark (RH) is the problem itself** -- not "we still lack a pretty model". The five rounds P1-P5 check layer by layer whether this gap can be filled by existing structure. **The current answer: not found (not: does not exist).**

### Frozen conclusions (three statements)

1. **Detection is unconditional; exclusion requires additional rigidity.**
2. **The audited positive-kernel constructions do not yield uniform coercivity.**
3. **No independent coercive mechanism was identified within the audited framework.**

### Final positioning

This is not a paper about "we did not prove RH" -- it is a paper about **why a large class of RH-type structures stably produce critical-line signals yet cannot automatically produce an exclusion mechanism.** That is the most stable and most honest landing point.

---

## Appendix: Audited route inventory (C1-D7 + P1-P5 + K1-K2 + THH/Arakelov)

Positivity (Weil/orbit/Li/de Branges/HB) / spectral (HP/BK/Connes/scattering) / trace / realizability / arithmetic geometry / positive-definite kernels / variational / energy / dynamics / statistics -- all converge to the rigidity gap.
