已查地图 + **外取原文**（所查：`A3-break-682-attempt.md`／`A3-third-moment-barrier.md`／`A3-second-moment`（`Montgomery 1973：Fejér 核二阶矩 可无条件求值（对角项＋Montgomery–Vaughan）`）、`V185` §3、`C-25`（`ASSETS-REGISTRY`，前沿 §7.2(a)／§5 逐字）、`C-29`（`W6-MAJORANT-1a`：卡点＝**MV（Lemma 2.2）步**，四个 `Σ_{n≠m}x_nz_m/(y_n−y_m)` 双线性形式；对角支配 ⟺ `X ≪ TL`）、`C-76`（本会话前档）；**外取**：`arXiv:2306.04799`（`BGSTB24` 全文 PDF，含 `Lemma 3` 与 `Proof of Theorem 1` 逐字）、`summit.sfu.ca/.../etd7113_ERinne.pdf`（**免费呈现 Montgomery 1973 原始论证**，第 2 章逐字）、`archive.mpim-bonn.mpg.de/5149/1/mpim-preprint_2024-34.pdf`（引 `MV` large sieve ＋ `Hilbert's inequality`））。**结论**：① 唐先生核出的 `Lemma 3.2` 逐字 ⟹ **二手源转录误差，原文无歧义**（我方"待核"标记正确并被这次核对证实）；② **分叉已解决**——`RS` 一般度数用 `C–S＋Rankin–Selberg`（唐先生核 ✓），而 **ζ（`m=1`）用的是 Montgomery 的无条件二阶矩，其逐字适用范围 `0 ≤ x ≤ T`**；③ **`SQ1` 问对了**（MV／Hilbert 双线性步正是该边界上的工具，且经 MPIM 独立佐证）；④ 且**两条路（MV sharpness／绝对收敛区扩展）在 ζ 上汇聚到同一个问题** ✓✓

# C-77 · **`Lemma 3.2` 勘误确认 ＋ 分叉解决 ＋ `SQ1` 定向判定**

> **时间**：2026-09-18 12:38 唐先生：① 核出 RS 原文 `Lemma 3.2`（我方 discrepancy 系二手源转录误差）；② 指出 RS 的 `Lemma 3.5` 用 `C–S＋Rankin–Selberg`（非 large sieve），质疑 `SQ1`（"MV 是否 sharp"）是否问偏；③ 要求找 Montgomery 1973 对应步骤
> **本档**：逐字呈上三条证据链 ＋ 判定 ✓

---

## §1 ✅ 勘误确认（`Lemma 3.2`，原文逐字，由唐先生核）

$$\textbf{Lemma 3.2（RS 原文，唐先生逐字核）}：\text{"Let}\ \Phi\ \text{as in (3.6) be supported in}\ \boxed{|\xi_1|+\cdots+|\xi_n|\le\frac{2-\delta}{m}}.\ \text{Then}\ A_{r,s}(n,T)=0\ \text{unless}\ |n_j|\ll T\ \text{and}\ n_1n_2\cdots n_{r+s}\ll T^{2-\delta}."$$
$$\Longrightarrow\ \text{原文用}\ \sum|\xi_j|（\text{绝对值之和}），\ \textbf{与 Theorem 1.1 的}\ \sum_j|\xi_j|<2/m\ \textbf{同记号};\ \text{二手源}\ (2002.00595)\ \text{写成}\ |\xi_1+\cdots+\xi_n|\ \textbf{系转录误差}✗$$
$$\textbf{结论}：\text{`C-76` §5／§6 的"待核"已闭合};\ \text{且这次核对}\ \textbf{抓到一处真实转录错误} \Longrightarrow \text{我方"二手源必须标注待核"的流程}\ \textbf{得到实证}✓✓$$
$$\text{另：唐先生核对}\ \text{Lemma 3.2 的证明纯由支撑条件代数推出}\（n_j\ll T^{m|\eta_j|}\ \text{相乘得}\ n_1\cdots n_{r+s}\ll T^{m\sum|\eta_j|}\le T^{2-\delta}）\ \textbf{与我方"identity-type"判断一致}✓✓$$

## §2 ⭐ 分叉解决：`RS` 一般度数 **vs** ζ（`m=1`）

$$\textbf{(甲) RS 一般度数（唐先生核）}：\text{Lemma 3.5}\ \sum_{m\le X}a_k(m)^2\ll X^{1+\varepsilon}\ \text{用}\ \textbf{Cauchy–Schwarz}\ \textbf{＋}\ \textbf{Rankin–Selberg 在}\ \operatorname{Re}s>1\ \textbf{绝对收敛}（RS1）✓✓$$
$$\qquad\Longrightarrow\ \text{不是 large sieve／MV};\ \text{瓶颈在}\ \textbf{绝对收敛区}✓$$
$$\textbf{(乙) ζ（}m=1\text{，即我们的机器所用）}：\text{`BGSTB24` 逐字（`arXiv:2306.04799` §2）}：$$
$$\qquad\textbf{Lemma 3}：F(x,T)=\frac2\pi\int_{-\infty}^{\infty}\Bigl|\sum_{\substack{\rho\\ 0<\gamma\le T}}\frac{x^{\rho-1/2}}{1-(\rho-(\frac12+it))^2}\Bigr|^2dt.$$
$$\qquad\textbf{Proof of Theorem 1 逐字}：\text{"R}(x,T)\ \text{does not depend on RH, and}\ \textbf{Montgomery [Mon73] proved unconditionally that}$$
$$\qquad\qquad R(x,T)=(1+o(1))Tx^{-2}\log^2T+T(\log x+O(1))+O(x\log x).\text{"}$$
$$\qquad\qquad \text{"From [GM87] this was improved, so that for}\ \boxed{0\le x\le T},\ R(x,T)=x^{-2}T\log T(\log T+O(1))+T(\log x+O(\sqrt{\log T})).\text{"}$$
$$\Longrightarrow\ \textbf{ζ 情形的无条件适用范围逐字＝}\ \boxed{0\le x\le T}\ \textbf{（＝support ≤ 1）}✓✓$$

## §3 ⭐⭐ Montgomery **原始**形式（免费文本逐字；SFU 论文第 2 章）

$$F(\alpha)=F(\alpha,T)=\Bigl(\tfrac T{2\pi}\log T\Bigr)^{-1}\sum_{0<\gamma,\gamma'\le T}T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma'),\qquad w(u)=\tfrac4{4+u^2}$$
$$\textbf{Theorem 2.1（Assume RH）}：F\ \text{real},\ F(\alpha)=F(-\alpha);\ F(\alpha)\ge-\varepsilon;\ \text{且对固定}\ 0\le\alpha<1：F(\alpha)=(1+o(1))T^{-2\alpha}\log T+\alpha+o(1)$$
$$\qquad \text{uniformly for}\ 0\le\alpha\le1-\varepsilon✓$$
$$\qquad ⭐\ \textbf{逐字}：\text{"Since this theorem gives little information for the case}\ \boldsymbol{\alpha\ge1},\ \text{attention here is restricted to kernels}\ \hat r\ \text{which}\ \textbf{vanish outside}\ [-1+\delta,\,1-\delta].\text{"}✓✓✓$$
$$\Longrightarrow\ \boxed{\text{support}\le1\ \text{墙的}\ \textbf{原始形式}＝\text{Montgomery 自己的}\ \alpha\ge1\ \text{"little information"}}\ ✓\（\text{而}\ 0\le\alpha<1\ \text{的求值＝他 1973 的无条件结果}）$$

## §4 判定：`SQ1` 问对了没有？

$$\textbf{(i)}\ \text{对 ζ（我们的机器）}：\text{边界}\ x=T\ \text{上的工具}\ \textbf{确实是 MV／Hilbert 型双线性估计}✓$$
$$\qquad \text{我方 `C-29` 逐字：卡点＝}\textbf{MV（Lemma 2.2）步}，\text{四个}\ \sum_{n\ne m}x_nz_m/(y_n-y_m)\ \text{型双线性形式};\ \text{对角支配}\iff X\ll TL✓$$
$$\qquad \text{独立佐证（本档）}：\text{MPIM preprint 2024-34 在同一语境}\ \textbf{同时引}\ \text{[MV] }\textit{The large sieve}\ \text{与}\ \text{[MV] }\textit{Hilbert's inequality}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{SQ1 问对了}}：\text{"MV 对该核是否 sharp"}\ \text{正是决定}\ x\le T\ \text{边界能否推进的问题}✓$$
$$\textbf{(ii)}\ \text{对一般度数（RS 语境）}：\text{唐先生的替代提法正确}——\ \text{应问"}\textbf{Rankin–Selberg 绝对收敛区能否扩展}\text{"}✓$$
$$\textbf{(iii)}\ ⭐\ \textbf{但两条路在 ζ 上汇聚（本档推导，}\text{[本档]}）：
$$\qquad \text{ζ 的"绝对收敛"类比＝}\ \sum_n\Lambda(n)^2n^{-2\sigma}\ \text{型级数};\ \text{其}\ \textbf{横坐标恰为}\ 1\ \Longrightarrow\ \text{把它推到}\ \operatorname{Re}s<1\ \text{即}\ \textbf{要求}\ \Lambda^2\text{-和的相消} \approx \textbf{prime-pair 信息}$$
$$\qquad\Longrightarrow\ \text{"MV sharpness" 与 "绝对收敛区扩展"}\ \textbf{是同一堵墙的两个面}✓✓$$

## §5 Montgomery 1973 原文：**未能取得** ⚠️（诚实报告）

$$\text{AMS}\ \textit{Proc. Symp. Pure Math.}\ 24,\ 181\text{--}193\ \text{为付费/无免费扫描};\ \text{检索仅得引用条目、百科、以及（免费）}\ \textbf{呈现其论证的二手文本}✓$$
$$\text{本档所用替代（可核）}：\text{①}\ \texttt{BGSTB24}\（\texttt{arXiv:2306.04799}，免费）\text{逐字复现 Montgomery 无条件求值与范围}\ 0\le x\le T;\ \text{② SFU 论文第 2 章逐字复现其}\ \alpha\ \text{参数化与}\ \alpha\ge1\ \text{"little information"}✓$$
$$\qquad ⚠️\ \text{但}\ \textbf{196}3\text{原文中"off-diagonal 用哪一条不等式"尚未取得逐字};\ \text{若要钉死，需 AMS 原文或教材（如 Iwaniec–Kowalski / Montgomery–Vaughan 书）对应章节}⚠️$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 12:5x）`[纪律]`

```
技术词 分叉解决     命中文件数=1    :: ./C77-lemma32-erratum-confirmed-fork-resolved-and-SQ1-verdict.md
技术词 两路汇聚     命中文件数=1    :: ./C77-lemma32-erratum-confirmed-fork-resolved-and-SQ1-verdict.md
技术词 little information 命中文件数=1    :: ./C77-lemma32-erratum-confirmed-fork-resolved-and-SQ1-verdict.md
技术词 绝对收敛区  命中文件数=1    :: ./C77-lemma32-erratum-confirmed-fork-resolved-and-SQ1-verdict.md
```
**读数（按实测，先跑后写）**：四项**均仅本档（1 档 ⟹ 本档新增）** ✓（`分叉解决`／`两路汇聚`／`little information`／`绝对收敛区`）

## §7 边界

- `[逐字]` §1（唐先生核）、§2（`BGSTB24`）、§3（SFU 论文）✓；§2／§3 均为**免费公开文本**，但 §3 为**二手呈现**（学位论文复现 Montgomery）⚠️
- `[本档]` §4 的判定与"两路汇聚"推导（`[本档]`，非逐字）✓
- **不声称**：Montegomery 1973 原文细节已核 ✗；`η*>0` 成立／不成立 ✗；不判 MV sharp 与否 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓

```
⚠️ 唐先生 12:38：① Lemma 3.2 已核（我方 discrepancy = 二手源转录误差，原文用 Σ|ξ_j|）；② RS 的 Lemma 3.5 用 C–S＋Rankin–Selberg（非 large sieve），质疑 SQ1 是否问偏；③ 找 Montgomery 1973 对应步骤
⚠️ 分叉解决：RS 一般度数 = C–S＋RS 绝对收敛（唐先生核 ✓）；ζ (m=1) = Montgomery 无条件二阶矩，BGSTB24 逐字适用范围 0 ≤ x ≤ T
   （R(x,T) = x^{-2}T logT(logT+O(1)) + T(log x + O(√logT))）⟹ 边界即 support ≤ 1
⭐ Montgomery 原始形式（免费二手文本逐字）：F(α)，Theorem 2.1（RH 下）F(α) = (1+o(1))T^{-2α}logT + α + o(1) 对 0≤α≤1−ε 一致；
   逐字 "gives little information for the case α ≥ 1, attention here is restricted to kernels vanishing outside [−1+δ, 1−δ]" ⟹ support≤1 墙的原始形式
✅ SQ1 问对了：ζ 边界 x=T 上的工具确实是 MV/Hilbert 型双线性估计（C-29 逐字：卡点=MV Lemma 2.2 步，四个 Σ x_n z_m/(y_n−y_m)）；
   独立佐证：MPIM 2024-34 同语境引 MV large sieve + Hilbert's inequality
⭐ 两路汇聚：[本档] ζ 的绝对收敛类比 = Σ Λ(n)² n^{-2σ}，横坐标恰为 1 ⟹ 推到 Re s<1 = 要求 Λ²-和相消 ≈ prime-pair ⟹
   "MV sharpness" 与 "绝对收敛区扩展" 是同一堵墙的两个面
⚠️ Montgomery 1973 原文未取得（AMS 付费/无免费扫描）；替代：BGSTB24（免费，逐字范围）+ SFU 论文第 2 章（免费，逐字 α 参数化）
   仍未取得：1973 原文中 off-diagonal 用哪条不等式的逐字
✅ 净产出：①Lemma 3.2 勘误闭合 ✓；②分叉解决（两对象两工具）✓；③Montgomery 原始 α≥1 逐字 ✓；④SQ1 定向判定=问对了 ✓；⑤两路汇聚推导 ✓
```
