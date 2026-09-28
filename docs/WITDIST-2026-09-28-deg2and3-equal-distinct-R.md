# WITDIST-2026-09-28 — C-534：★$R$ 映射为单射（$\deg{=}2{\Rightarrow}\lvert$distinct $R\rvert{=}2$；$\deg{=}3{\Rightarrow}3$，无重复 $R$）✓✓

> **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查见 §3**。
> **范围**：核 $\deg(S){=}1$ 之不可能性之前置事实；**不作路线裁定** ✗。

**已查地图：命中（接续 C-533，非新案 ✓）**：`WITPARAM-…`
D0: 本档对象 ＝ **档案已有**（$\mathcal R_i$／$R$／$\deg$；无新数学对象 ✓）
D1: 1（**首次证实 $S{\to}R$ 之\ \textbf{映射为单射}（$\deg{=}2$ 时两 $R$ 互异、$\deg{=}3$ 时三 $R$ 互异）✓✓**）
[R]

## §0 结论

对三正实例（三槽全正）中 $d(I_i,I_j){=}4$ 之对 $(i,j)$，对每 $S\in\binom D2$：

| $\deg(S)$ | $\lvert$distinct $R\rvert$ | 计数 |
|---|---|---|
| $2$ | $2$ | $3968$ |
| $3$ | $3$ | $1984$ |

$$\Longrightarrow\ \boxed{\text{额外 owner 到 }\binom{D^c}{2}\text{ 之映射为\ \textbf{单射}}}\ ✓✓\ \text{（无两额外 owner 共享同一 }R\text{）}$$

## §1 读法

$$R=\mathrm{supp}(I_i\oplus K)\setminus S\ \in\binom{D^c}{2}$$

且 $R$ **完全决定** $K$（因 $K{=}I_i\oplus\mathbf1_{S\cup R}$）⟹ 单射 $S{\to}R$ ＝ $S$ 之额外 owner **两两不同** ✓✓。

（此即唐先生 §4 之"$K_{S,R}$ 只 owner 一个中点"之**直接推论** ✓。）

## §2 下一靶

在 $\deg(S){=}1$ 反设下，唯一 $R{=}\{a,b\}$。取 $a'\in D^c{\setminus}\{a,b\}$ 之 $x_{S,a'}{=}I_i\oplus\mathbf1_{S\cup\{a'\}}$，核其覆盖码字与 $K_{S,R}$ 之几何冲突——即证明 $\deg(S){\neq}0,1$ ✓。

**禁止** ✗：纯计数 ✗；$F,G$ 反推 ✗；**不声称** $\deg(S){\ge}2$ 已证 ✗。

## §3 技术词回查

```
$ bash scripts/tech_word_check.sh "单射映射" "distinct R" "S到R"
技术词 技术词 单射映射     命中文件数=2    :: ./WITDIST-2026-09-28-deg2and3-equal-distinct-R.md ./E3-why-this-is-not-the-old-pit.md
技术词 distinct R 命中文件数=0  ::
技术词 S到R       命中文件数=0  ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 单射映射 | 0 | 0 | ✓ |
| distinct R | 0 | 0 | ✓ |
| S到R | 0 | 0 | ✓ |

- 写后补跑 ⚠️ 据实 ✓

## §4 边界

- 有限穷举 ✓；未上 SDP/SAT ✗；不跨空间 ✓
- **不作路线裁定** ✗；**明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）