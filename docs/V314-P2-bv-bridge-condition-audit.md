# V314 · **P2：$bv\ge\frac12$ 桥接条件审计** —— ⭐⭐⭐⭐⭐ **判词 P2-YES**：库内已有**已证定理** `lemma bv_phiD_ge_half`（非目标式）＋ `theorem admWindow_phiD`（12 字段全由具名引理填充）⟹ producer 的两个合取项**各由一条库内定理供给**；⭐ **$bv$ 不是 `AdmWindow` 的字段** ⟹ 它是**独立桥接条件**；⭐ **额外假设 $4\pi w\le L$**（$L\to\infty$ 时最终成立）；⭐ **该引理用 $\lambda\le1$（非严格）⟹ 不依赖 P3**

$$\boxed{\textbf{定义（`WindowCore` 逐字）}：\texttt{bv}\ v\ L：＝L^{-1}\!\int_{\mathbb R}v(u)^{4}du ⟹ \text{问题即}\ \tfrac1L\int\phi_D^4\ge\tfrac12} ✓✓✓$$
$$\boxed{\textbf{定理一（12 字段）}：\texttt{theorem admWindow\_phiD}\ (\texttt{TaperProfile}\ \varrho)\ (0<\lambda)\ (\lambda\le1)\ (1\le w)\ (8w\le L)：\texttt{AdmWindow}\ (\texttt{phiD}\ \varrho\ \lambda\ L\ w)\ L\ w\ (\texttt{cDT}\ \varrho\ \lambda)} ✓✓✓$$
$$\boxed{\textbf{定理二（$bv$ 下界，独立）}：\texttt{lemma bv\_phiD\_ge\_half}\ (\cdots)\ (4\pi w\le L)：\tfrac12\le\texttt{AdmWindow.bv}\ (\texttt{phiD}\ \varrho\ \lambda\ L\ w)\ L} ✓✓✓$$
$$\boxed{\textbf{判词 P2-YES}（含精确假设表）} ✓$$

> 委托 ✓ 唐先生 2026-09-16 14:15：**接 P2，作为纯桥接条件审计，不再碰变分最优性**；只需回答 $$\boxed{bv(\texttt{phiD}\ \varrho\ \lambda\ L\ w)=\tfrac1L\int\phi_D^4\ \stackrel?\ge\ \tfrac12}$$；**四点**：① `bv` 定义是否真为该归一化（查隐藏权重／$L$／$\varrho$ 归一化）；② `BridgeD:86` 是**已证定理**还是**目标式／局部 lemma**（区分 `have hBV` 与最终 `theorem`，并确认 `AdmWindow` 实例是否真消费它）；③ 下界是否对**完整参数域**成立（$\lambda\in[\frac12,1)$，并查 $L,w,\varrho$ 的量词，**不得以固定 $\lambda$ 数值实验代替全域证明**）；④ $bv\ge\frac12$ 是否依赖 **P3** ✓✓✓；判词三选一 **P2-YES／P2-GAP／P2-NO** ✓；并建议 P3 的**最干净做法**：不强改源码严格域，而用 $$\forall\lambda\in[\tfrac12,1):\ G_{\max}(\lambda)\le c^{*}_\lambda\quad\Longrightarrow\quad \sup_{\lambda<1}G_{\max}\le\lim_{\lambda\to1^-}c^{*}_\lambda=c_1^{*}$$ ✓✓✓
> 第一手依据（**本档直读源码**）✓ `ThmD/BridgeD.lean`（`admWindow_phiD` 第 31–45 行；`admWindow_params`；**`bv_phiD_ge_half` 第 85–95 行**；`localHypsCoreD_eventually`）｜`ThmD/WindowCore.lean`（`def bv`；`structure AdmWindow` 12 字段）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V314`（先领号 ✓）

---

## §1 **四点审计（逐项）**

$$\textbf{① }bv\ \textbf{定义}：\texttt{WindowCore}\ \text{逐字}\ \texttt{def bv : ℝ := L⁻¹ * ∫ u, v u ^ 4} ⟹ \textbf{无隐藏权重};\ \text{归一化即}\ L^{-1}\ \text{与}\ \varrho\ \text{无关} ✓✓$$
$$\qquad （\text{对照}：\texttt{av}：＝L^{-1}\!\int v^{2};\ \text{两者同型，皆}\ L^{-1}\ \text{归一化}）✓$$
$$\textbf{② 是已证定理}：\texttt{BridgeD.lean:85} \ \boxed{\texttt{lemma bv\_phiD\_ge\_half}}\ \text{（含完整证明：}\texttt{bD\_close}\to|b_D-b_\star|\le4w/L;\ \texttt{bStar\_ge};\ 4w/L\le1/\pi）✓✓✓$$
$$\qquad \text{且}\ \textbf{$bv$ 不是 `AdmWindow` 的字段}（12 字段列表见 `WindowCore`：`one_le_w,w8,four_le_c,even,nonneg,le_one,contDiff,support,l1_deriv,l1_deriv_sq,l1_deriv2,l1_deriv2_sq`）$$
$$\qquad \Longrightarrow \text{producer 的合取}\ \big(\texttt{AdmWindow}\ \wedge\ \tfrac12\le bv\big)\ \textbf{由两条独立库内定理各供一项} ✓✓✓$$
$$\qquad \text{并有 Params 级包装：}\texttt{admWindow\_params}\ \text{（}\texttt{AdmWindow}\ (P.\texttt{phiD}\ T)\ (P.L\ T)\ P.w\ (\texttt{cDT}\ P.\varrho\ P.\lambda)\text{）} ✓$$
$$\textbf{③ 完整参数域}：假设为\ \{\texttt{TaperProfile}\ \varrho,\ 0<\lambda,\ \lambda\le1,\ 1\le w,\ 8w\le L,\ \boxed{4\pi w\le L}\} ✓✓✓$$
$$\qquad \Longrightarrow \text{在}\ L=\lambda l\to\infty\ \text{的设定下，}\ 4\pi w\le L\ \text{最终成立} ⟹ \textbf{属"eventually"型条件}，\text{非固定}\ \lambda\ \text{数值} ✓✓$$
$$\qquad \text{且另有}\ \texttt{localHypsCoreD\_eventually}：\exists T_0,\forall T\ge T_0,\ \texttt{LocalHypsCore}\ (\texttt{cDT}\ P.\varrho\ P.\lambda)\ \dots\ \text{（桥到素数侧输入）} ✓$$
$$\textbf{④ 与 P3 的关系}：\text{该引理假设为}\ \boxed{\lambda\le1}\（\textbf{非严格}）⟹ \textbf{不依赖}\ \lambda<1 ⟹ \textbf{P2 与 P3 解耦} ✓✓✓$$
$$\qquad \text{严格}\ \texttt{P.lam}<1\ \text{出现在}\ \texttt{CoeffMoments}\ \text{producer 的假设表里（V310 §1）} ⟹ \text{归 P3 处理} ✓$$

---

## §2 **判词**

$$\boxed{\textbf{P2-YES}：\forall\lambda\in(0,1],\ \forall w\ge1,\ \forall L\ge\max(8w,4\pi w)：\ \tfrac12\le bv(\texttt{phiD}\ \varrho\ \lambda\ L\ w)\ \text{且证明已入库}} ✓✓✓$$
$$\qquad \text{连接方式}：\texttt{admWindow\_phiD}\ \text{（12 字段）} ＋\ \texttt{bv\_phiD\_ge\_half}\ \text{（桥接条件）} ⟹ \text{producer 的合取完备} ✓$$

---

## §3 边界 ＋ 净产出 ＋ 下一步

```
① ⚠️ §1② 的"证明已入库"依据：`lemma bv_phiD_ge_half` 有完整 `by` 块（已读）；**未跑构建** ⚠️
② ⚠️ `bD_close`／`bStar_ge` 的**内部证明未逐行读**（只读其用法）⚠️
③ ⚠️ Params 级是否**已有**`4πw ≤ L` 的 eventually 引理未逐字确认（仅由 L→∞ 推断）⚠️
④ **不声称** Lean 构建通过；**不声称** P3 已解 ✓
⑤ 未用 RH ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐⭐ **P2-YES**：`bv` 下界是**已证 lemma**（`bv_phiD_ge_half`），非目标式；`AdmWindow` 实例为**已证 theorem**（`admWindow_phiD`，12 字段全由具名引理填充）✓✓✓
② ⭐⭐ **$bv$ 与 `AdmWindow` 解耦**：$bv$ **不是** 12 字段之一 ⟹ producer 合并取两项，各由一条库内定理供给 ✓✓
③ ⭐⭐ **精确假设表**：$\{\texttt{TaperProfile}\,\varrho,\ 0<\lambda,\ \lambda\le1,\ 1\le w,\ 8w\le L,\ 4\pi w\le L\}$；末项为 eventually 型 ✓✓
④ ⭐⭐ **P2 不依赖 P3**（引理用 $\lambda\le1$ 非严格）；严格 $\texttt{P.lam}<1$ 在别处 ⟹ 归 P3 ✓✓
⑤ ⭐ **另有** `localHypsCoreD_eventually`（桥到素数侧输入，$T$ 最终成立）✓
【下一步 = P3（域统一）】
  **推荐做法（唐先生）**：**不强改源码严格域**，而写 $$\forall\lambda\in[\tfrac12,1):\ G_{\max}(\lambda)\le c^{*}_\lambda\ \Longrightarrow\ \sup_{\lambda<1}G_{\max}(\lambda)\le\lim_{\lambda\to1^-}c^{*}_\lambda=c_1^{*}$$（用 `cStar_continuousOn`／`cStar_lipschitzOn` 供货）✓✓✓
  待核：严格 $\texttt{P.lam}<1$ 在 producer 中**到底被哪一步用到**（若仅为误差项 ⟹ 可换 $\lambda\le1$ 或用 $\lambda\to1^-$ 极限表述）✓
