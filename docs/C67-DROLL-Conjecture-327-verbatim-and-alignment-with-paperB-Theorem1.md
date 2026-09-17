已查地图：**未覆盖**（所查档：`P8-DROLL-verbatim-reading.md`、`N2-chain-confirmed.md`、`docs/Droll2012-thesis-Li-criterion-Selberg.pdf`（127 页，本地 ✓）、`papers/brown-thm2-classical/main.tex`、`ASSETS-REGISTRY.md` A-2 行；关键词：`Conjecture 3.2.7`（**本文首次给出其完整逐字陈述** ✓）、`Conjecture 1.7.10`（本文首次逐字 ✓）、`b⁺ = max{b,0}`（0 档 ⟹ 新）✓

# C-67 · **Droll Conjecture 3.2.7 的逐字陈述 ＋ 与论文 B `Theorem 1` 的逐项对齐**

> **时间**：2026-09-17 22:5x 唐先生：论文 B 的一切建立在"Theorem 1 即 Conjecture 3.2.7 经典情形"这一**身份断言**上，而他两次在线抓取 Droll 原文**恰在 §3.2 Lemma 3.2.3 之后被截断** ⟹ 要求贴出 Conjecture 3.2.7 的原始陈述以逐项对齐。
> **本档**：从**归档 PDF** 提取逐字（`docs/Droll2012-thesis-Li-criterion-Selberg.pdf`，PDF 第 100 页／idx 99）＋ 逐项对齐 ＋ **两处必须修正的表述** ✓

---

## §0 结论（先行）

$$\boxed{\text{身份断言（}\text{Theorem 1}=\text{Conjecture 3.2.7 的 }\tau=1\text{ 情形）}\ \textbf{成立}\ ✓✓}$$
$$\qquad\textbf{严丝合缝的条件}＝\boxed{b^{+}=\max\{b,0\}=0}\ \text{—— 对}\ \zeta\ \text{有}\ b=-\frac{1+\log 2\pi}{2\pi}<0\ ⟹\ b^{+}=0\ ✓✓\ \text{（Droll 猜想中唯一与我们写法不同的一项}：(4a+3b^{+})H/9\ \text{在}\ b^{+}=0\ \text{时}\ =\ 4aH/9\ ✓）$$
$$\textbf{⚠️ 但发现两处必须修正的表述}：\text{①}\ k\le2T^2\log T\ \textbf{属 Conjecture 1.7.10}（\text{我们逐字核到}），\ \text{Conjecture 3.2.7 本身}\ \textbf{对 }k\ \textbf{无上界};\ \text{② 猜想含}\ \textbf{两条} \text{不等式，我们只对应}\ \textbf{第一条} ✗$$

---

## §1 `Conjecture 3.2.7` 逐字（PDF idx 99，行 30–58）

> ⚠️ **字形层损坏声明**：该 PDF 的希腊字母／括号／求和号在文本层被替换为**内部字形名**（`/parenleft.alt1`、`/bracketleft.alt3`、`/summation.disp`、`/divides.alt0` 等）。下列**方括号内为按上下文重建**（与 `P8` 档已记录的同一坑一致 ✓）；拉丁字母部分为**逐字** ✓。

```
[逐字，行 30–32]
   "We will now state a conjecture which will be required for our proof of the main
    result of this chapter in the next section. This conjecture, combined with the
    previous lemma, provides a modified, generalized version of [3, Lemma 5]."

[逐字 + 重建，行 33–58]
   Conjecture 3.2.7  Let k be an integer greater than or equal to 2, and let τ and H
   be real numbers such that 1 ≤ τ < 2 and H > e. Define  r_H(τ) = (1 + τ/H²)^{1/2} .
   Let b be as in our hypothesis on N(T) in the previous section, and define b⁺ = max{b, 0}.
   Then, if for every zero ρ of F we write γ_ρ = I(ρ), we have

        Σ_{|I(ρ)| > H} [ (1 + τ/γ_ρ²)^{k/2} + (1 + τ/γ_ρ²)^{−k/2} − 2 ]

        ≤ 2 ( r_H(τ)^k + r_H(τ)^{−k} − 2 ) [ (1/3) a H log H + ((4a + 3b⁺) H)/9 + 2c log H + 2d + c/4 ]

        ≤ (9/4) ( r_H(τ)^k + r_H(τ)^{−k} − 2 ) [ a H log H + b⁺ H + 2c log H + 2d ] .

[逐字，行 59–60]
   "Remark: The necessity to adopt Conjecture 3.2.7 in the effort to generalize …"
```

## §2 逐项对齐（`Conjecture 3.2.7` @ `τ=1` vs 论文 B `Theorem 1`）

| 项 | Droll Conjecture 3.2.7 | 论文 B Theorem 1（@$\tau=1$） | 判定 |
|:--|:--|:--|:--:|
| 左端被加项 | $(1+\tau/\gamma_\rho^2)^{k/2}+(1+\tau/\gamma_\rho^2)^{-k/2}-2$ | $(1+1/\gamma_\rho^2)^{k/2}+(1+1/\gamma_\rho^2)^{-k/2}-2$ | **✓**（$\tau=1$）|
| 求和范围 | $\sum_{\vert I(\rho)\vert>H}$ | $\sum_{\vert\gamma_\rho\vert>H}$ | **✓**（同记号 $\gamma_\rho=I(\rho)$）|
| 右端因子 | $2\bigl(r_H(\tau)^k+r_H(\tau)^{-k}-2\bigr)$，$r_H(\tau)=(1+\tau/H^2)^{1/2}$ | $2\bigl(r_H^k+r_H^{-k}-2\bigr)$，$r_H=(1+H^{-2})^{1/2}$ | **✓**（$r_H(1)=r_H$）|
| 括号第一项 | $\tfrac13 aH\log H$ | $\tfrac a3 H\log H$ | **✓** |
| 括号第二项 | $\dfrac{(4a+3b^{+})H}{9}$ | $\dfrac{4a}{9}H$ | **✓ 当且仅当 $b^{+}=0$**（对 $\zeta$：$b<0\Rightarrow b^{+}=0$ ✓✓）|
| 括号其余 | $2c\log H+2d+c/4$ | $2c\log H+2d+c/4$ | **✓** |
| 参数域 | $k\ge2$ 整数、$1\le\tau<2$、$H>e$ | $k\ge2$、$\tau=1$、$H>e$ | **✓**（我们覆盖其中 $\tau=1$）|

$$\Longrightarrow\ \boxed{\text{在 }\tau=1\text{ 且 }b^{+}=0\ \text{（}\zeta\ \text{成立）时，Droll 猜想的}\ \textbf{第一条不等式}\ \textbf{与 Theorem 1 完全一致}}\ ✓✓$$

## §3 ⚠️ 两处必须修正的表述（对论文 B）

$$\textbf{① 范围归属错位}：\text{我们逐字核到}\ \textbf{Conjecture 1.7.10}（\text{PDF idx 48 行 2–9}）：$$
> "**Conjecture 1.7.10** Let $r>1$ and $T=\frac1{\sqrt{r^2-1}}$ … such that as long as $T>T_0$, we have that if all of the zeros of $\xi_B$ lie in the region $\mathcal C(r)$, then $\Re(\lambda_k(F,1))$ is non-negative for $\mathbf{1\le k\le 2T^2\log T}$."

$$\Longrightarrow\ \boxed{k\le2T^2\log T\ \textbf{属 Conjecture 1.7.10};\ \text{Conjecture 3.2.7 本身为}\ k\ge2\ \textbf{无上界}}\ ✗$$
$$\text{故论文中"it carries no restriction }k\le2H^2\log H\text{"若读作}\ \textbf{3.2.7 的} \text{限制}\ ⟹ \textbf{张冠李戴}\ ✗;$$
$$\qquad\text{正确表述}：\textbf{我们的不等式对全部 }k\ge2\ \textbf{成立}，\text{而}\ \textbf{1.7.10（原 Brown 逆命题）} \text{只断言}\ k\le2T^2\log T\ ⟹ \text{经典情形可由我们覆盖到}\ \textbf{全部阶} ✓$$
$$\textbf{② 猜想含两条不等式}：\text{Droll 的第二条}\ \le\frac94(\cdot)[aH\log H+b^{+}H+2c\log H+2d]\ \textbf{我们未涉及} ✗$$
$$\qquad\Longrightarrow\ \text{论文应（且只需）}\ \textbf{明确声明}\：\text{我们证的是}\ \textbf{第一条} \text{（即 Droll 修复 Lemma 5 所需的那条）} ✓\ \text{（建议措辞："the first inequality of Conjecture 3.2.7"）}$$

## §4 附带确认（加强可信度）

$$\textbf{Droll 猜想里}\ b^{+}=\max\{b,0\}\ \textbf{的构造}\ \Longleftrightarrow\ \text{论文 B 的}\ \textbf{"}b<0\ \text{是燃料}\text{"}\ \textbf{与}\ b\ge0/b<0\ \textbf{二分}\ ✓✓$$
$$\qquad\text{—— 即：猜想在 }b\ge0\ \text{时括号里多出}\ 3b^{+}H/9\ \text{项}，\ \text{而在 }b<0\ \text{时该项消失};\ \text{论文 B 的精确余量}\ \frac23\vert b\vert H^{-3}\ \text{正是这一支的产物}\ ✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-17 22:5x）`[纪律]`

```
技术词 范围归属错位  命中文件数=1    :: ./C67-DROLL-Conjecture-327-verbatim-and-alignment-with-paperB-Theorem1.md
技术词 逐项对齐     命中文件数=11   :: ./V308-admissible-class-audit-and-eigenfunction-gap.md ./APPRECIATION-AUDIT-2026-09-11.md ./PROTOCOL-R8.3-verify.md
技术词 身份断言     命中文件数=1    :: ./C67-DROLL-Conjecture-327-verbatim-and-alignment-with-paperB-Theorem1.md
技术词 Conjecture 3.2.7 命中文件数=23   :: ./A1-E3-status-and-large-k.md ./A1-PROOF-SKELETON-and-constants.md ./ASSETS-REGISTRY.md
```
**读数（按实测）**：`范围归属错位`（1 档＝**仅本档**）、`身份断言`（1 档＝**仅本档**）⟹ **本档新增** ✓；⚠️ `逐项对齐`＝**11 档 ⟹ 档案已有**（通用词）⟹ **不列为本档提出** ✗；`Conjecture 3.2.7`＝**23 档** ⟹ 此前仅以**引文片段**在档（如 `N2-chain-confirmed` ✓、`A1-E3-status-and-large-k` ✓），**完整逐字陈述本档首次给出** ✓（**注**：§1 的 `b⁺` 分析未单独回查（含特殊字符），已由 `范围归属错位` 项代表 ✓）

## §6 边界

- `[逐字]` §1 与 §3 的引文取自**本地归档 PDF**（`Droll2012-thesis`）✓；**含字形损坏的公式部分已显式标注为"按上下文重建"** ✓（严格遵 `P8` 的引用纪律）
- `[本档]` §2 对齐表、§3 两处修正、§4 附带确认 ✓
- **不修改** 论文 B 任何文件 ✓（修正为**建议**）；**不声称** Droll 的其他引理已复核（`N2` §3 限定 4 仍成立：其余引理为引用级 ⚠️）
- **纪律**：先查后判（R-1 ✓）；未用 RH ✓；零数值 ✓

```
⚠️ 委托：贴 Droll Conjecture 3.2.7 原始陈述，供与论文 B Theorem 1 逐项对齐
⚠️ 来源：本地归档 Droll2012-thesis-Li-criterion-Selberg.pdf（127 页）PDF 页 100／idx 99
⚠️ 身份断言：✓ 成立 —— 逐项严丝合缝，唯一差异项 (4a+3b⁺)H/9 在 τ=1 且 b⁺=0（ζ 的 b<0 ⟹ b⁺=0）时等于 4aH/9
⚠️ 两处修正：① k ≤ 2T²logT 属 Conjecture 1.7.10（已逐字核到），3.2.7 对 k 无上界 ⟹ 论文"no restriction"的归属需改；
   ② 3.2.7 含两条不等式，我们只对应第一条 ⟹ 论文需明确声明"the first inequality"
⚠️ 附带：b⁺=max{b,0} ↔ 论文"b<0 是燃料 / b≥0 vs b<0 二分" ✓（加强可信度）
✅ 净产出：①Conjecture 3.2.7 首次完整逐字（含损坏标注）✓；②逐项对齐表 ✓；③两处必改表述 ✓；④b⁺ 对应确认 ✓
```
