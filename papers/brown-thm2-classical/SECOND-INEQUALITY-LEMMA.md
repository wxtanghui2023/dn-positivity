# Lemma (second inequality of Conjecture 3.2.7 is elementary)

已查地图（**先查后写**）：`docs/C67`（3.2.7 逐字）、`docs/C179`（本引理的推导档）、`papers/brown-thm2-classical/main.md`（第一条已证）。关键词回查：本引理与 `C-179` 同批。
FREEZE-ACK: 本档即冻结期内的引理注记（依 `§8.1`；不产候选结论）
D0: 本档对象 = **3.2.7 第二条的初等引理（可与论文 B 合并入附录）** —— 关系 = 初等引理注记，非新机制
D1: 0


**Draft note · 2026-09-19 · companion to `main.md` (Theorem 1)**

## Statement

Under Droll's parameter hypotheses (verbatim: `a, c, d > 0`, `3a + b > 0`,
`b⁺ = max{b,0}`, `1 ≤ τ < 2`, `H > e`), the second inequality of Conjecture 3.2.7,

```
2 (r_H(τ)^k + r_H(τ)^{−k} − 2) B1  ≤  (9/4) (r_H(τ)^k + r_H(τ)^{−k} − 2) B2
```

holds **unconditionally**, where

```
B1 = (1/3) a H log H + ((4a + 3b⁺) H)/9 + 2c log H + 2d + c/4
B2 = a H log H + b⁺ H + 2c log H + 2d
```

## Proof

The common factor `2(r^k + r^{−k} − 2) > 0` cancels; it suffices to show `B1 ≤ (9/8) B2`.
Compute `D := (9/8)B2 − B1` term by term (exact coefficients):

```
D = (19/24) aH log H + (19/24) b⁺H − (4/9) aH + (1/4) c log H + (1/4) d − (1/4) c
  = aH[(19/24) log H − 4/9] + (19/24) b⁺H + (c/4)(log H − 1) + d/4 .
```

Since `H > e` gives `log H > 1`, and `a, c, d > 0`, `b⁺ ≥ 0`:

```
(19/24) log H − 4/9 > 19/24 − 4/9 = 25/72 > 0 ,
(c/4)(log H − 1) > 0 ,   d/4 > 0 ,   (19/24) b⁺H ≥ 0
```

hence `D > 0`, i.e. `B1 < (9/8) B2`. ∎

Note: `3a + b > 0` is **not** used.

## Consequences

1. **Coverage.** `main.md` proves the *first* inequality at `τ = 1`, `b⁺ = 0`;
   this lemma gives the second for all `1 ≤ τ < 2` and all `b`. Hence
   **both inequalities of Conjecture 3.2.7 hold at `τ = 1`.**
2. **Location of content.** The whole content of Conjecture 3.2.7 is its *first*
   inequality; the second is an elementary consequence of the parameter hypotheses.
   (Suggested wording: "the second inequality is elementary; the substance is the first.")

## Verification

`scripts/second_inequality_check.py` — exact rational coefficients, sample sweep
(`(H,a,b⁺,c,d)` incl. the ζ-type `a ≈ 0.159`, `b⁺ = 0`); all samples give `D > 0`.

## Positioning (read before citing)

This is a **clarification, not a novel theorem**. The computation is ours, but the fact
is elementary and almost certainly implicit in Droll's setup (his hypotheses `a,c,d>0`,
`H>e`). Droll himself does not prove it — verbatim: *"We relegate the proof of variants
of Conjecture 3.2.7 to future work."* Its only value: it shows that the **substance of
Conjecture 3.2.7 is its first inequality** (which `main.md` proves at `τ = 1`), so the
paper may honestly state its coverage of the conjecture. Suggested wording: *"the second
inequality is an elementary consequence of the parameter hypotheses; the substance of the
conjecture is its first inequality."* Do **not** claim novelty for this step.
