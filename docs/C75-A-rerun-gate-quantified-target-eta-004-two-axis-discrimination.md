已查地图 + **外搜**（所查档：`A3-break-682-attempt.md`（0.682 突破尝试，含前沿 §7.2(e)(f)、§1.4 逐字）、`A3-third-moment-barrier.md`（三阶矩障碍侦察 §Q1–Q2）、`V186` §5（下一步预登记三选）、`V185` §1–§3、`C74`（本会话前档）、`MATH-STATEMENT-A-offdiagonal-second-moment-beyond-support-1.md`（`Problem A`）／**外搜**：`arXiv:2501.14545`（`BGSTB25` v3 摘要，2026-09-18 取）、`arXiv:2503.15449`（`GLSS25`）、MPIM 报告页）。**结论**：修正后目标可**定量化为一个门槛** —— **无条件把 Montgomery 二阶矩范围从 `X≤T^{1−ε/2}` 推到 `X≤T^{1+η}`，`η≥0.04` 即破 `0.682`**；且新查证实 **`BGSTB25` 的 `b` 是水平侧（β 盒）参数，与 `support` 不同坐标** ⟹ **`1.04` 档未被走过** ✓

# C-75 · **A 重跑闸门**：修正后目标定量化（`η ≥ 0.04`）＋ 两轴判别 ＋ 三路线判定

> **时间**：2026-09-18 12:25 唐先生「继续」（承接 `C-74` 修正后的 A 目标）
> **性质**：闸门＋文献核对；**不新增数学** ✓；外搜内容标 `[外搜／未读全文]` ⚠️

---

## §0 结论（先行）

$$\boxed{\text{修正后 A 目标（定量）}：\text{无条件把 Montgomery 二阶矩从}\ X\le T^{1-\varepsilon/2}\ \text{推到}\ X\le T^{1+\eta};\ \eta\ge0.04\ \Longrightarrow\ 0.70>0.682}\ ✓✓$$
$$\text{即}\ \texttt{Problem A}\ \text{的}\ \eta^*>0\（\text{且}\ \eta^*\ge0.04\ \text{即够破天花板}）;\ \text{已知}\ \eta^*=0\（\text{无条件}），\ \eta^*>0\ \textbf{开放}✓$$
$$\text{新查证实（本档）}：\texttt{BGSTB25}\ \text{的}\ b=0.3185\ \text{是}\ \textbf{水平侧 β-盒} \text{参数}\ \ne\ \text{Fourier support}\ \Longrightarrow\ \textbf{1.04 档未被走过}✓✓$$

---

## §1 修正后目标的定量形式

$$\text{阶梯（`V185`／前沿 §7.3）}：\text{support}\ 1.04/1.26/1.70\ \Longrightarrow\ 0.70/0.80/0.90\（\textbf{超出已知}）✓$$
$$\text{泛函（同一两矩输入）}：\text{Christoffel}\quad 1-\Lambda_1(0)=\frac{m_1^2}{m_2}=\frac{(\sum\lambda)^2}{d\sum\lambda^2}\ \（\text{Cauchy--Schwarz，}E8\ \text{§3}）✓$$
$$\qquad 0.6725\to0.682\ \text{的}\ 0.01＝同一泛函＋同一两矩输入用 Christoffel 而非单一标量\ R(\psi)✓$$
$$\text{天花板机制}：\text{越}\ 0.682\ \textbf{需无条件三阶矩}（X\asymp T）——\text{而前沿 §7.2(e) 逐字}：$$
$$\qquad\text{"…available exactly in the Rudnick--Sarnak range}\ X^k\le T^{2-\varepsilon};\ \textbf{at}\ X\asymp T\ \textbf{this allows only}\ k=1.\ \textbf{Thus, unconditionally, higher moments add nothing.}"✓✓$$
$$\qquad\Longrightarrow\ k=3\ \text{的对角法只覆盖}\ X\le T^{2/3-\varepsilon};\ \text{推到}\ X\asymp T\ \text{需再进}\ T^{1/3}✓$$

## §2 文献读数（2026-09-18 检索；⚠️ 外搜内容，未读全文）

$$\textbf{(i)}\ \texttt{BGSTB25}\ \text{v3}\（\texttt{arXiv:2501.14545}，2026-09-01\）\textbf{摘要逐字}：$$
$$\qquad\text{"…we assume a more general condition, namely that}\ \textbf{all the zeros}\ \rho=\beta+i\gamma\ \text{with}\ T<\gamma\le2T\ \textbf{are in a narrow vertical box}\ \text{centered on the critical line with width}\ b/\log T.\ \text{We prove that under this assumption with}\ \mathbf{b=0.3185}\ \text{that at least}\ \mathbf{2/3}\ \text{of zeros are simple and on the critical line."}$$
$$\qquad ⭐\ \Longrightarrow\ \text{该"盒假设"是}\ \textbf{水平侧（β）} \text{条件}（\text{零点到临界线的距离}），\ \textbf{不是} \text{Fourier support} \Longrightarrow\ \textbf{与 ladder 的 }1.04\ \textbf{不同坐标}✓✓$$
$$\qquad ⚠️\ \text{且它}\ \textbf{不是} \text{RH：}b=0.3185\ \text{远窄于零自由区所给宽度} \Longrightarrow\ \text{属"弱于 RH 的假设"}✓$$
$$\textbf{(ii)}\ \text{两轴判别（本档新读）}：\text{垂直侧}（\text{pair-correlation／Fourier support}）\ \big|\ \ \text{水平侧}（\beta\ \text{盒}）$$
$$\qquad \texttt{BGSTB25}\ \text{走}\ \textbf{水平侧}; \quad \text{而}\ \texttt{arXiv:2608.13637}\ \text{的功绩＝把}\ \textbf{无条件垂直侧} \text{输入转成}\textbf{水平侧输出}（\text{摘要："for the first time…horizontal distribution"}）✓✓$$
$$\textbf{(iii)}\ \texttt{GLSS25}（\texttt{arXiv:2503.15449}）：\text{PCC}\ \Longrightarrow\ \text{渐近}\ \textbf{100\%} \text{零点既简单又在线上}（\textbf{猜想级}）✓$$
$$\textbf{(iv)}\ \text{MPIM 报告页}：\text{同组后续}（\text{Goldston–Schettler–Suriajaya}）\text{把}\ \text{AH}（\text{Alternative Hypothesis}）\ \text{纳入同一方法}✓$$
$$\textbf{(v)}\ \text{检索中}\ \textbf{无人声称} >0.682;\ \textbf{支撑}>1\ \text{的无条件扩展}\ \textbf{仍空}✓✓$$

## §3 三路线判定（修正后目标下）

| 路线 | 判定 | 依据 |
|:--|:--|:--|
| **1. `BGSTB`／`GLSS` 可扩带宽（→`Problem A` 的 `η*`）** | **开放，且未被走过** ✓ | §2：`BGSTB25` 的 `b` 是水平侧；k=3 无条件＝无（`A3` 侦察）；无人声称 >0.682 |
| **2. 大值／密度链** | **收束，无独立余地** ✗ | `TYPE-MATCH` ＋ `TODAY-ARC-CLOSURE-MAP`：第三通道存在但**上限＝输入**＝`SUPPORT-1` |
| **3. `Problem A` 的 `SQ3` 判别实验（`μ²` vs `Λ`）** | **未执行**；价值＝**诊断**（定位障碍在"素数提取"还是"双体双线性结构"）✓ | `C-66`／`MATH-STATEMENT-A` |

$$\Longrightarrow\ \boxed{\text{唯一值得投的是路线 1，且其判据已量化：}\eta\ge0.04\ (0.70)\ \text{或}\ \eta\ge0.26\ (0.80)\ \text{或}\ \eta\ge0.70\ (0.90)}✓✓$$

## §4 ⚠️ 一处待核（纯文献）

$$\texttt{BGSTB25}\ \text{v3（2026-09-01）}\ \text{与}\ \texttt{arXiv:2608.13637}\ \text{v2（2026-08-19/24）}\ \text{时间}\ \textbf{接近} ⟹ \ \text{须核后者是否已引用前者 v3}$$
$$\qquad \text{若已引用} \Longrightarrow \text{"无条件化"是}\ \textbf{明确改进};\ \text{若未引用} \Longrightarrow\ \text{两者独立、改进关系需自行判定}⚠️$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 12:3x）`[纪律]`

```
技术词 两轴判别     命中文件数=1    :: ./C75-A-rerun-gate-quantified-target-eta-004-two-axis-discrimination.md
技术词 水平侧       命中文件数=1    :: ./C75-A-rerun-gate-quantified-target-eta-004-two-axis-discrimination.md
技术词 门槛        命中文件数=93   :: ./E3-why-this-is-not-the-old-pit.md ./E152-double-reflection-axis-audit.md ./V186-inertia-mechanism-audit-endpoint-degenerates-to-positivity.md
技术词 可扩带宽     命中文件数=2    :: ./V186-inertia-mechanism-audit-endpoint-degenerates-to-positivity.md ./C75-A-rerun-gate-quantified-target-eta-004-two-axis-discrimination.md
```
**读数（按实测）**：`两轴判别`／`水平侧`＝**仅本档（1 档 ⟹ 本档新增）** ✓；⚠️ `门槛`＝**93 档 ⟹ 档案已有**（通用词）✗；⚠️ `可扩带宽`＝**2 档 ⟹ `V186` §5② 已用此术语** ⟹ 本档为**引用**，**不列为首次命名** ✗（⚠️ 即本档初稿的"首次命名"自述**已自行更正**）

## §6 边界

- `[逐字]` §1 梯阶／Christoffel／§7.2(e) 前沿原话（经 `A3` 两档，均标 `[原]`）✓；§2 为 `[外搜／未读全文]` ⚠️（仅摘要与转述，**不得**当已核定理使用）
- `[本档]` §0 定量化、§2(ii) 两轴判别、§3 三路线判定、§4 待核项 ✓
- **不声称**：`η*>0` 成立／不成立 ✗；不声称已破 0.682 ✗；不判 `Λ_1` 结局 ✓；不证 RH ✗；不修改原档 ✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓；未跑 Lean ✓

```
⚠️ 任务：A 三条路线在修正后目标下重跑闸门
⚠️ 结果：目标定量化 = 无条件把 Montgomery 二阶矩从 X≤T^{1−ε/2} 推到 X≤T^{1+η}；阈值 η≥0.04 ⟹ 0.70 > 0.682
   （阶梯：1.04→0.70；1.26→0.80；1.70→0.90）；天花板机制 = 越 0.682 需无条件三阶矩（X≍T，前沿 §7.2(e) 逐字
   "unconditionally, higher moments add nothing"）；Christoffel 泛函 1−Λ₁ = m₁²/m₂
⚠️ 新查证实（外搜，未读全文）：BGSTB25 v3 的 b=0.3185 是**水平侧 β-盒**假设（零点到临界线距离 b/logT），
   **不是** Fourier support ⟹ 与 ladder 不同坐标 ⟹ **1.04 档未被走过**；GLSS25 = PCC ⟹ 100%（猜想级）；
   检索中无人声称 >0.682；支撑>1 的无条件扩展仍空
⚠️ 两轴判别（本档新读）：垂直侧（pair-correlation/support） vs 水平侧（β 盒）；2608.13637 的功绩＝把无条件垂直侧输入
   转成水平侧输出（摘要 "for the first time…horizontal distribution"）
⚠️ 三路线判定：路线1 开放且未被走过（唯一值得投）；路线2 收束（上限=输入）；路线3 未执行（诊断价值）
⚠️ 待核：BGSTB25 v3 (2026-09-01) 与 2608.13637 v2 (2026-08-19/24) 时间接近 ⟹ 核后者是否引用前者 v3
✅ 净产出：①目标定量化（η≥0.04）✓；②两轴判别 ✓；③三路线判定 ✓；④文献卡点与待核项 ✓
```
