# Paper A — can the CLASSICAL SECOND MOMENT of `S(t)` control the fluctuation term `Fluc(n)`?

**2026-09-12, subagent task.** Analysis only: this file + `scripts/PAPERA_second_moment_route.py` → `scripts/PAPERA_second_moment_route.txt`. Not committed. Every formula is printed with the numbers substituted; a clean negative counts as a result; non-rigorous steps say so.

**Conventions.** `theta(t)=2 arctan(1/(2t))`, `f=1-cos`, `S=N-main`, `main(t)=(t/2pi)log(t/(2 pi e))+7/8`, `Fluc(n)=int_0^{T0} f(n theta) dS`, `w_n=f'(n theta) n theta' = n sin(n theta) theta'`, `theta'=-4/(4t^2+1)`, `t=(1/2)cot(theta/2)`. Heights: `T0=1.132490658714e6` (= `gamma_max` of `data/zeros_odlyzko_2M.npy`, 2,001,052 zeros, `main(T0)=2001051.377`) and `T0=3.0001753328e12` (Platt–Trudgian, no table). `Allow(n)=main(T0)-n B_{T0}`, `B_{T0}=(log T0+1)/(4 pi T0)`.

## Task 1 — the second-moment result used, with its source

    int_0^T |S(t)|^2 dt = (T/(2 pi^2)) loglog T + O(T sqrt(loglog T)),   i.e.  c = 1/(2 pi^2).

**Source.** Selberg 1946, *Theorems 6 and 7*, quoted verbatim in **arXiv:2006.08503, eq. (1.4)**, retrieved by literature search 2026-09-12 (a *secondary* quotation — I did not open Selberg's original). **The constant is `1/(2 pi^2) = 0.050660`, NOT `1/pi^2`** — the two normalisations differ by 2, which is why the standard shape carries a symbolic constant. The same source (eq. (1.8)) records a further `+O(T)` term, of relative size `~1/loglog T`. Independent determination from the table (`int S^2 dt` by 5-point Boole on every zero-interval, cross-checked against a uniform grid 2.188071e5 vs 2.188146e5, i.e. 3e-5):

| `T` | `int_0^T S^2 dt` | `T loglog T` | ratio |
|---|---|---|---|
| 283,123 | 5.280468e+04 | 7.163033e+05 | 0.07372 |
| 566,245 | 1.075698e+05 | 1.463039e+06 | 0.07352 |
| 1,132,491 | 2.188071e+05 | 2.983838e+06 | **0.07333** |

So `c_emp = 0.07333 = 1.447 x (1/(2 pi^2))` while `1/loglog T0 = 0.380` — consistent with that documented secondary term. `c_emp` is an *effective, one-realisation* constant and **exceeds** `1/(2 pi^2)`, so using it makes the bound larger, i.e. *more generous* to the route; the verdict below is given for `c` in `[1/(2 pi^2), c_emp]` and is unchanged (the bound scales as `sqrt(c)`).

## Task 2 — Cauchy–Schwarz on `Fluc(n)`

Stieltjes by parts (`S` of bounded variation, `f(n theta) ∈ C^1` for `t>0`):

    Fluc(n) = [f(n theta(t)) S(t)]_0^{T0} - int_0^{T0} S(t) w_n(t) dt.

Boundary: `|f|<=2`, `|S(T0)|=0.623`, `S(0+)=-7/8` ⟹ `|boundary| <= 2(0.623)+2(7/8) = 3.00` (rigorously `O(log T0)`; negligible). So `Fluc` is an inner product of `S` against the oscillatory weight `w_n`.

**(i) weight** (closed form verified to 1.000000 for `n=1e3 … 1.283e12`): `int_0^{T0} w_n^2 dt = 4n^2 int_{theta(T0)}^{pi} sin^2(n th) sin^2(th/2) dth = pi n^2 (1-theta(T0)/pi)`, hence

    ||w_n||_2 = n sqrt(pi) (1 - theta(T0)/pi)^{1/2} = 1.7725 n   (  1 - 2.8e-7 ).

**(ii) second moment**: `||S||_2 = sqrt(c T0 loglog T0)`. At `T0=1.132490658714e6`, `loglog T0 = 2.6348`, `||S||_2 = 467.7682`, but **`sup|S| = 1.7994` only**, so `||S||_2/sup|S| = 260.0 = 0.244 sqrt(T0)` (`sqrt(T0)=1064.2`). This is the decisive structural fact: the `L^2` norm over the whole interval is inflated by `sqrt(T0)`, because it pays the *length* of the interval, whereas the pointwise bound pays only the *size* of `S`.

**(iii) the bound** `|Fluc(n)| <= ||S||_2 ||w_n||_2 + O(log T0) = n sqrt(pi c T0 loglog T0) + O(log T0)`, i.e.

    c = 1/(2 pi^2) = 0.050660 :  sqrt(pi*0.050660*1.13249066e6*2.6348) = sqrt(4.7490e5) = 6.8912e+02 n
    c = c_emp      = 0.073331 :                                                        = 8.2910e+02 n
    c = 1/pi^2     = 0.101321 :                                                        = 9.7457e+02 n

Elementary pointwise bound for comparison: `|S|<=sup|S|` and `int_0^{T0}|w_n|dt ~ 2n` give `3.599n` (empirical `sup|S|`), or `9.44n` with Trudgian's explicit `|S(T)|<=0.111 logT+0.275 loglogT+2.45 = 4.722` at `T0`. So `global C-S / pointwise = 689.12/3.599 = 191.5`. **Inserting a true theorem about `S^2` therefore makes the bound ~190x WORSE than the trivial `|S|<=sup|S|`**: the second moment is true but applied at the wrong scale — Cauchy–Schwarz discards exactly the phase information that distinguishes `int S w_n` from `||S||_2||w_n||_2`.

## Task 3 — ratio to the allowance, and the range delivered

    ratio(n) = n sqrt(pi c T0 loglog T0) / ( main(T0) - n B_{T0} ).

At `n=T0^2`, `Allow = main(T0) - T0(logT0+1)/(4 pi) = (T0/4pi)(logT0 - 2log(2pi) - 3) + 7/8`. Substituting:

    T0 = 1.132490658714e6 : T0^2 = 1.2825351e+12 ; B_{T0} = 1.0498e-06 ; main(T0) = 2.001051e+06
      n B_{T0} = 1.346398e+06  ⟹  Allow = 2.001051e+06 - 1.346398e+06 = 6.5465e+05
      c = 1/(2pi^2): 689.12 * 1.2825351e12 = 8.8394e+14  ⟹  ratio = 1.3501e+09
      c = c_emp    : 829.10 * 1.2825351e12 = 1.0633e+15  ⟹  ratio = 1.6243e+09
    T0 = 3.0001753328e12 : T0^2 = 9.0010520e+24 ; B_{T0} = 7.8856e-13 ; main(T0) = 1.236315e+13
      n B_{T0} = 7.097856e+12  ⟹  Allow = 1.236315e+13 - 7.097856e+12 = 5.2653e+12
      c = 1/(2pi^2): sqrt(pi*0.050660*3.0001753328e12*3.3579) = 1.2662e+06
                    1.2662e+06 * 9.0010520e24 = 1.1397e+31  ⟹  ratio = 2.1646e+18
      c = c_emp    : 1.5234e+06 * 9.0010520e24 = 1.3713e+31  ⟹  ratio = 2.6043e+18

**Largest `n` with `ratio<1`.** Since `n B_{T0} << main(T0)` here, `n_max = main(T0)/coef`, i.e. the closed form `n_max = sqrt(T0/(2 pi loglog T0)) * log(T0/(2 pi e))` for `c = 1/(2 pi^2)`:

    T0 = 1.132490658714e6 : n_max = 2.9038e+03 (closed form = direct division) ; n_max/T0 = 2.56e-03,
                            n_max/T0^2 = 2.26e-09
    T0 = 3.0001753328e12  : n_max = 9.7636e+06 ; n_max/T0 = 3.25e-06 ; n_max/T0^2 = 1.08e-18
    with c = c_emp        : n_max = 2.4135e+03 (T0=1.13e6) and 8.1153e+06 (T0=3.0e12)

**Range delivered: `n <~ 2.9e3` at `T0=1.13e6` (exactly `sqrt(T0/(2 pi loglog T0)) log(T0/(2 pi e))`), i.e. of order `sqrt(T0) logT0/sqrt(loglog T0)` — hence BELOW the linear range (`2.9e3` vs `1.13e6`) and `4.4e8` times below `T0^2` (`1.2825e12/2.9038e3 = 4.42e8`).**

## Task 4 — Cauchy–Schwarz PER PERIOD-BLOCK, then sum

Blocks `theta_k=(u_0+2 pi k)/n` with `u_0=n theta(T0)`, `K = n(pi-theta(T0))/(2 pi) ~ n/2` (`K=499,999` at `n=1e6`). Per block `||w||^2_{2,bl}=4n^2 int_bl sin^2(n th)sin^2(th/2)dth` (closed form) and `||S||^2_{2,bl}=int_{t_{k+1}}^{t_k} S^2 dt` (exact from the table). Summing (script §e):

| `n` | `K` | per-block sum | crude `sup*int` | TRUE `Abs Fluc(n)` | per-block/global C-S |
|---|---|---|---|---|---|
| 1e3 | 499 | 1.298894e+03 | 3.598732e+03 | 1.016534e+01 | 1.567e-03 |
| 1e4 | 4999 | 1.212178e+04 | 3.598732e+04 | 4.232295e+01 | 1.462e-03 |
| 1e5 | 49999 | 1.209206e+05 | 3.598732e+05 | 3.937911e+01 | 1.459e-03 |
| 1e6 | 499999 | 1.208890e+06 | 3.598732e+06 | 3.051667e+01 | 1.458e-03 |

So the per-block sum is `~1.209 n` (coefficient stable in `n`): it **removes the whole `sqrt(T0)` inflation** (`1.458e-3 = 1/686` of the global C-S) and beats the crude bound by `1.209/3.599 = 0.336` (factor 3). Where `1.209n` comes from (heuristic — the global theorem says nothing about a single block, so use the *local* second moment `||S||^2_{2,bl} ~ (1/(2pi^2)) loglog t * Delta t`, giving `sqrt(loglog t)` per block): `(n/2pi) int_{20}^{T0} sqrt(loglog t)/t^2 dt = (n/2pi)(0.0993) = 0.0158 n`; **plus** the region `t < gamma_1 = 14.13`, where there are **no zeros at all** and `S=-main` is smooth of size `<=0.432`: `0.4886 n` blocks `x 4 sup|S| = 1.728` ⟹ `0.8444 n`, with **no second-moment gain available**. Total `~0.860 n` (heuristic) vs `1.209 n` (measured): same order, same `n`-scaling.

**Range:** `n_max ~ main(T0)/1.209 = 1.655e+06 = 1.46 T0` (table height); the same coefficient gives `1.02e+13 = 3.41 T0` at `T0=3.0001753328e12`. The refinement is real (686x off the global C-S, 3x off the crude bound, and it *restores* the linear range) but it **buys no change of range**: still `n=O(T0)`, never `O(T0^2)`. The obstruction is locatable: the block sum is dominated by low `t`, where `S` is smooth and the second moment says nothing, while the genuinely fluctuating region contributes only `0.016n`. *(Further refinement — subtracting the block mean, legitimate since `int_bl w=0` — does not help: in the fluctuating region the block mean is the local value of `S`, so nothing is removed; in the low-`t` region it would help, but one must then pay the block's total variation `~t^2 logt/n` zeros, and summing that over blocks grows like `(log T0)^2`. Heuristic.)*

## Task 5 — honest verdict

**No — the second-moment input delivers `n=T0^2` in neither treatment.**

* **Global C-S:** `|Fluc(n)| <= n sqrt(pi c T0 loglog T0)`; at `n=T0^2` the ratio to the allowance is `1.35e+09` (`T0=1.13e6`) and `2.16e+18` (`T0=3.0e12`). Range delivered `n <~ 2.9e3` resp. `9.8e6` — *below* the linear range, by a factor `390` resp. `3.1e5`.
* **Per-block C-S:** `~1.209 n`; range `n <~ 1.46 T0` (table height) / `3.41 T0` (second height) — the linear range with a better constant, still astronomically short of `T0^2`.
* **Where the loss occurs** — precisely where C-S replaces a *signed, phase-correlated* quantity by a *positive, phase-blind* one: (1) **globally** `|int S w_n| <= ||S||_2||w_n||_2` pays the interval length, inflating the pointwise size of `S` by `0.244 sqrt(T0)` (measured 260 at `T0=1.13e6`) — hence the true theorem on `S^2` gives a bound `~190x worse` than the trivial `|S|<=sup|S|`; (2) **per block** the bound is exhausted by `t<=14`, where `S` is smooth and nothing fluctuates. What is needed is a statement about the *correlation* `int S(t) sin(n theta(t)) dt` at the single frequency `n`; a bound on `|S|` is frequency-blind, and the resonance analysis (`docs/PAPERA-delta-N-resonance.md`) puts that frequency inside `[0,T0]` for all `n <= T0^2 log T0`.
* **What the numerics add.** The TRUE `|Fluc(n)|` on the table is `10.2, 42.3, 39.4, 30.5` for `n=1e3,1e4,1e5,1e6` and `2.19e+02` at `n=T0^2`, against an allowance `6.5e+05`: **the obstruction is in the proof, not in the truth**; no *bound* of the form `|Fluc(n)|<Allow(n)` is available, and the second moment is the wrong instrument to produce one.

## 对本项目的意义

1. 二阶矩输入（Selberg 1946，经 arXiv:2006.08503 复述：`∫_0^T S² = (T/2π²)loglog T + …`）是**真定理**，但在本框架里**用错了地方**。
2. 全局 Cauchy–Schwarz 比初等逐点界**差约 190 倍**：L² 范数为区间长度付出 `√T₀`（实测 `‖S‖₂/sup|S| = 260 = 0.244√T₀`）。
3. 它交付的范围 `n ≲ √T₀·logT₀/√loglogT₀`（`T₀=1.13e6` 时 `≈2.9e3`）**低于线性范围**（`2.9e3` vs `1.13e6`），比 `T₀²` 低 `4.4e8` 倍——是「比不做还差」的反效果。
4. 周期块版消掉了 `√T₀` 膨胀（`1.209n`，比全局小 686 倍、比逐点界小 3 倍），**恢复线性范围** `n ≲ 1.46T₀`，但**仍非二次**（第二高度亦仅 `3.41T₀`）。
5. 失败位置已定位：块和被 `t ≤ 14` 的**无零点、`S` 光滑**区域耗尽（`0.844n`），真正涨落区只贡献 `0.016n`；二阶矩对**相位相关量** `∫S·sin(nθ)dt` 无能为力。
6. 这把 `docs/PAPERA-delta-N-resonance.md` §四 (甲)「更精细的素数侧输入」中「可能仍不够」的猜测，**量化成了否定**：两条路都差 `≥10⁵–10¹⁸` 倍。
7. 数值事实：`|Fluc(n)|` 实测 `O(1)–O(100)`，允许量 `6.5e5` —— **障碍在证明侧，不在事实侧**（与共振分析 §三、§四一致）。
8. 论文 A 的处置不变：二次范围**留作 Remark 路线图**，②③④ 作为已完成部件；本文件新增一条**已量化的负面结果**，说明「二阶矩」这条显然后路为何走不通。
9. 可复用资产：`scripts/PAPERA_second_moment_route.py`（由零点表**精确**算 `∫S²`、`Fluc(n)`、逐块 C-S 界与允差），并独立实测二阶矩常数 `c_emp = 0.0733 = 1.447×(1/2π²)`（与文献 `+O(T)` 次项一致）。
10. 待唐先生决策：本条（含「比逐点界差 190 倍」这一可检验结论）是写入论文 A 的 Remark，还是单列一条技术注记。
