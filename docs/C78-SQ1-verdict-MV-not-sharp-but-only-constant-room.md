已查地图 + **外取文献**（所查档案：`C-25`（`ASSETS-REGISTRY`：`§5 引擎＝Lemma 2.2 MV 双线性型`，`λ_r=log n`，`δ_n^{-1}≤2n`，**只用 ℓ² 权、不含配对相关内容**）、`C-29`（`W6-MAJORANT-1a`：卡点＝MV 步；对角支配 ⟺ `X ≪ TL`；推到 `X ≫ T` **须改进因子 ≍ `X/(TL³)`**）、`C-76`／`C-77`、`E4-ENGINE-*`（`加权 Hilbert 不等式 Lemma 2.2 ＝ [MV74, Thm 2]`；`O₁ 的全部依据是加权 Hilbert 不等式（**非猜想**）`）；**外取**：`arXiv:2608.12315`（**Brad Rodgers，2026-08-12，6 页**）、`arXiv:2203.14950`（PAMS Series B 10 (2023) 439–454）、`en.wikipedia.org/wiki/Hilbert's_inequality`、`mathoverflow.net/questions/415005`、`kskedlaya.org/ant/chap-largesieve.html`）。**结论**：**MV 的加权 Hilbert 不等式已知不 sharp**（`Preissmann` 把常数改进到 `(4/3)π`；**`Rodgers` 2026-08 证明最优常数严格 `> π`，否定了 MV 自己的提问**）✓；**但可用的改进是常数级**（最好 ≲1.5 倍），而我们的缺口是**幂级**（需 ≍ `X/(TL³)`）⟹ **`SQ1` 对我们的用途＝关闭**（不能过墙）✓✓

# C-78 · **`SQ1` 结果**：MV 不等式**不 sharp**（常数可改进），但**只有常数空间** ⟹ 不能过墙

> **时间**：2026-09-18 12:41 唐先生建议：**直接查"该不等式本身是否已知 sharp"**（若 sharp ⟹ `SQ1` 路死；若不 sharp ⟹ 可能有改进空间）
> **本档**：查到确定答案 ＋ 判定其对我们的可用性 ✓

---

## §0 结论（先行）

$$\textbf{(i)}\ \text{MV 加权 Hilbert 不等式}\ \textbf{不 sharp}✓\quad(\text{已证改进：Preissmann}\ C=\tfrac43\pi;\ \textbf{且最优常数}\ >\pi\ \text{于 2026-08 被证明})$$
$$\textbf{(ii)}\ ⚠️\ \text{但可用改进是}\ \textbf{常数级}：\text{MV}\ C=\tfrac32\pi\approx4.712;\ \text{Preissmann}\ \tfrac43\pi\approx4.189;\ \text{最优}\ \in(\pi,\tfrac43\pi]\ \Longrightarrow\ \text{总余量}\ \lesssim1.5\ \text{倍}✓$$
$$\textbf{(iii)}\ \text{我们的缺口是}\ \textbf{幂级}（`C-29` 逐字）：
$$\qquad \text{对角支配}\iff X\ll TL;\quad \text{推到}\ X\gg T\ \textbf{须改进因子}\ \asymp\frac{X}{TL^3}\approx\frac{T^{\eta}}{\log^3T}\ \Longrightarrow\ \textbf{常数改进无法弥补幂级缺口}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{SQ1 对我们的用途＝关闭}：\text{"MV 不 sharp"不产生可用的幂级余地}}✓✓$$

---

## §1 文献（逐字）

$$\textbf{①}\ \texttt{arXiv:2608.12315}\（\textbf{Brad Rodgers},\ 2026\text{-}08\text{-}12,\ 6\ \text{页},\ \texttt{math.CA}）\ \text{摘要}\ \textbf{逐字}：$$
$$\qquad\text{"We give a proof that}\ \boxed{\text{the optimal constant in the weighted Hilbert inequality is strictly greater than}\ \pi},\ \text{answering}\ \textbf{in the negative a question asked by Montgomery and Vaughan}.\ \text{The proof proceeds via an explicit limiting counterexample."}$$
$$\qquad\Longrightarrow\ \text{MV 自己问过"π 是否最优"};\ \textbf{答案是否定的（2026-08）}✓✓$$
$$\textbf{②}\ \text{谱系（`mathoverflow 415005` 转述）}：\text{MV}\ C=\tfrac32\pi\ \big|\ \text{Preissmann}\ C=\tfrac43\pi\（\text{仍次优}）\ \big|\ \text{猜想的}\ \pi\ \textbf{已证不可达}✓$$
$$\textbf{③}\ \texttt{arXiv:2203.14950}\（\text{PAMS Series B}\ \mathbf{10}\ (2023)\ 439\text{--}454）：\text{"On the Montgomery--Vaughan}\ \textbf{weighted generalization}\ \text{of Hilbert's inequality"}✓$$
$$\textbf{④}\ \text{MV 形式（Wikipedia 逐字）}：\Bigl|\sum_{r\ne s}u_r\bar u_s\csc\pi(x_r-x_s)\Bigr|\le\delta^{-1}\sum_r|u_r|^2\ \ \text{与}\ \ \sum_{r\ne s}\frac{u_r\bar u_s}{\lambda_r-\lambda_s}\ ✓$$
$$\textbf{⑤}\ \text{（`Selberg 3.2`）}：\text{`MO` 转述"最优值猜想为}\ \pi;\ \text{曾有未发表}\ C=3.2\ \text{的传闻，但据称未获证实"}✓$$

## §2 为什么常数改进补不上幂级缺口（`[本档]` 判读）

$$\text{对角支配条件}：|O_1|\ \ll\ D\ \text{其中}\ D\asymp\frac T\pi\cdot\frac{L^3}6,\ |O_1|\ll C\cdot L^2X\ \Longrightarrow\ X\ \ll\ \frac{TL}{6C}✓$$
$$\qquad \Longrightarrow\ C\ \text{的改进}\ \textbf{只把阈值乘以}\ \text{常数因子}\（\text{最好}\ \lesssim1.5\）；\ \text{而}\ X=T^{1+\eta}\ \text{要求}\ T^{\eta}/\log T\ \text{级的改进}✓$$
$$\qquad \Longrightarrow\ \boxed{\text{要过墙，需要的是}\ \textbf{幂级精化}，\ \text{不是常数精化}}✓✓$$
$$\qquad ⭐\ \text{而幂级精化必须}\ \textbf{利用频率集}\ \{\log n\}\ \text{的算术结构}（\text{不只间距}\ \delta_n^{-1}\le2n） \Longrightarrow\ \text{回到}\ \textbf{prime-pair}\ ✓✓$$

## §3 `SQ` 状态更新

| 子问题 | 状态 |
|:--|:--|
| **`SQ1`（MV 对该核是否 sharp）** | ✅ **有答案：不 sharp，但只剩常数空间** ⟹ **对本用途关闭**（`[本案]`）|
| **`SQ3`（`Λ` vs `μ²` 判别实验）** | ⚠️ **仍开**（定位障碍在"素数提取"还是"双体结构"）|
| **（新增）幂级精化问题** | ⚠️ 开，且＝`prime-pair`（同址，本会话第 7 次）|

## §4 对唐先生"整理成技术解剖笔记"提议的回应

$$\text{建议}\ \textbf{接受}：\text{把 `C-64`\text{–}`C-78` 这条链整理为一篇}\ \textbf{review note}：$$
$$\qquad\text{"}\textbf{The support-1 barrier: a technical anatomy}\text{"}（\text{非新结果；文献解剖＋精确门槛}）：$$
$$\qquad \text{①}\ \text{Montgomery}\ \alpha\ge1\ \text{"little information"}\（\text{原始形式}）;\ \text{②}\ \text{RS Lemma 3.2 的乘积界}\（\text{消失引理}）;\ \text{③}\ \text{RS Lemma 3.5 ＝ C--S＋Rankin--Selberg};$$
$$\qquad \text{④}\ \text{BGSTB24 的无条件范围}\ 0\le x\le T;\ \text{⑤}\ \text{MV／Hilbert 步及其}\ \textbf{常数谱系}（\tfrac32\pi\to\tfrac43\pi\to>\pi）;\ \text{⑥}\ \text{门槛}\ \eta\ge0.04\Longrightarrow0.70✓$$
$$\qquad ⚠️\ \text{但按我方纪律，}\textbf{不得} \text{把它记为"突破级"};\ \text{性质＝}\textbf{过程性/综述}✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 12:5x）`[纪律]`

```
技术词 幂级精化     命中文件数=1    :: ./C78-SQ1-verdict-MV-not-sharp-but-only-constant-room.md
技术词 技术解剖     命中文件数=1    :: ./C78-SQ1-verdict-MV-not-sharp-but-only-constant-room.md
技术词 constant room    命中文件数=0    ::
技术词 不 sharp        命中文件数=1    :: ./C78-SQ1-verdict-MV-not-sharp-but-only-constant-room.md
```
**读数（按实测，先跑后写）**：`幂级精化`／`技术解剖`／`不 sharp`＝**仅本档（1 档 ⟹ 本档新增）** ✓；`constant room`＝**0 档 ⟹ 本档新增（仅中英混用处）** ✓

## §6 边界

- `[逐字]` §1（Rodgers 摘要、Wikipedia、MO 转述、arXiv:编号）✓；MO 为**社区转述**，非一手 ⚠️
- `[本档]` §0 判定、§2 幂级/常数之辨、§3 状态更新、§4 提议 ✓
- **不声称**：`SQ3` 结论 ✗；不声称过墙可能／不可能 ✗；不证 RH ✗；不修改原档 ✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓

```
⚠️ 唐先生 12:41 建议：直接查"MV/Hilbert 不等式是否已知 sharp"（sharp ⟹ SQ1 路死）
✅ 查到确定答案：**不 sharp** —— 已证改进 Preissmann C=(4/3)π；**Rodgers arXiv:2608.12315（2026-08-12）证明最优常数严格 > π，
   否定 MV 自己的提问**（"explicit limiting counterexample"）；谱系：MV (3/2)π → Preissmann (4/3)π → 最优 ∈ (π, 4/3π]
⚠️ 但判定：可用改进是**常数级**（总余量 ≲1.5×），而 C-29 逐字给出我们的缺口是**幂级**（对角支配 X≪TL；推到 X≫T 须改进
   因子 ≍ X/(TL³) ≈ T^η/log³T）⟹ **常数改进无法补幂级缺口** ⟹ **SQ1 对本用途＝关闭**
⭐ 幂级精化必须利用频率集 {log n} 的**算术结构**（不只间距）⟹ 回到 prime-pair（本会话第 7 次同址）
⚠️ SQ 状态：SQ1 关闭（本案）；SQ3（Λ vs μ²）仍开；新增"幂级精化"问题
✅ 唐先生提议把这条链整理为 review note（"support-1 barrier 技术解剖"）—— 建议接受，性质＝过程性/综述，不得记为突破级
✅ 净产出：①MV 不 sharp 的确定答案（2026-08 最新）✓；②常数 vs 幂级之辨 ⟹ SQ1 关闭的理由 ✓；③SQ 状态更新 ✓；④综述提议回应 ✓
```
