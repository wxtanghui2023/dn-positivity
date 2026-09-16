# V315 · **P3：$\texttt{P.lam}<1$ 的严格域定位** —— ⭐⭐⭐⭐⭐ **判词 P3-YES-A**：严格性在 `AssemblyQ` 中**立即被弱化为 $\le1$**（`hlam.le`），下游**全部**用 $\le1$；error-chain 引理（`tendsto_rpow_halflam_sub_one`／`isLittleO_sqrtX_Tl`）**皆用 $\le1$** ⟹ **严格性非本质**；⭐ **其真正用途在 $\varepsilon$-free 证书**（`CertFlat` 注释：**在 $\lambda=1$ 处严格**，再由 $\lambda\mapsto\kappa_1$ 的**连续性**下移到某 $\lambda\in[\frac12,1)$）⟹ 技术性、可由极限消除；⚠️ **三层标记必须分层**：$c_1^{*}=0.753296\ \to\ F_{\rm opt}(1)\ \to\ G_{\max}(1)=2-1/c_1^{*}=0.67250$

$$\boxed{\textbf{消费者定位}：\texttt{ThmE/AssemblyQ.lean:270,420}\ \text{的定理陈述取}\ \texttt{hlam}:P.\texttt{lam}<1 ⟹ \textbf{第一行立即}\ \texttt{hlam1}:P.\texttt{lam}\le1:= \texttt{hlam.le}} ✓✓✓$$
$$\qquad \text{其后}\ \textbf{所有} \text{调用（}358/382/402/453/497\ \text{行）一律传}\ \texttt{hlam1}\ \text{或}\ \texttt{hlam0}\texttt{.le}\ ⟹ \textbf{未发现本质使用严格性的位置} ✓✓$$
$$\boxed{\textbf{严格性的真实用途（V310 §1 的 `CertFlat` 注释逐字）}：\text{"SOME}\ \lambda\in[\frac12,1)\ \text{… beat the decimals STRICTLY（proof: exact rational value … \textbf{strict at}\ \lambda=1;\ then \textbf{continuity} of}\ \lambda\mapsto\kappa_1(\lambda,v)\ \text{on}\ [\frac12,1]\text{"}} ✓✓✓$$
$$\boxed{\textbf{判词 P3-YES-A}：\lambda<1\ \textbf{仅为技术性域限制，可由极限／连续性消除}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 14:17：**打 P3，但目标不是"证明 $\lambda<1$"，而是定位该严格不等式在 producer 中的逻辑作用**；只查三件事：**1** 找出 `P.lam < 1` 的**全部消费者**，定位**第一处真正使用严格性的位置**（不接受"看起来是为了误差项"）；**2 严格二分** —— **情况 A**（严格性只用于有限-$T$ 误差项 ⟹ 可整理为 $\forall\lambda\in[\frac12,1):G_{\max}(\lambda)\le c^{*}_\lambda$，再由 `cStar_continuousOn` 得 $\sup_{\lambda<1}\le\lim_{\lambda\to1^-}c^{*}_\lambda=c_1^{*}$；**但不得直接写 $G_{\max}(1)\le c_1^{*}$，除非另有 $\lambda=1$ 的 theorem**）／**情况 B**（严格性进入本质不等式、不能被极限消掉 ⟹ 最终陈述就是 $\sup_{\lambda<1}$）；**3** 检查 0.67250 究竟是哪个对象，保持 $c_1^{*}\to F_{\rm opt}(1)\to G_{\max}(1)$ **逐层标记**（不得因 $c_1^{*}$ 闭合就把 0.67250 也宣布闭合）✓✓✓；判词 **P3-YES-A／P3-YES-B／P3-GAP**；**尤其不得把"$c^{*}_\lambda$ 在 $[0,1]$ 连续"自动当成 P3 已解决** ✓✓✓
> 第一手依据（**本档直读源码**）✓ `ThmE/AssemblyQ.lean`（92/98/185/196/270/282/353/358/382/402/420/434/453/497 行）｜`XiPrime/Statement.lean §4`（`CertFlat` 注释，V310 §1 已录）｜`ThmD/Functional.lean`（`cStar_continuousOn`／`cStar_lipschitzOn`）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V315`（先领号 ✓）

---

## §1 **消费者定位（第一处使用严格性的位置）**

$$\texttt{AssemblyQ.lean:270}：\texttt{(P : Params) (hP : P.Valid) (hlam : P.lam < 1)} ⟹ \texttt{:282}\ \texttt{have hlam1 : P.lam ≤ 1 := hlam.le} ✓✓$$
$$\texttt{AssemblyQ.lean:420}：\text{同型（另一条定理）} ⟹ \texttt{:434}\ \text{同}\ \texttt{hlam.le} ⟹ \texttt{:453}\ \texttt{tendsto\_rpow\_halflam\_sub\_one}\ P\ \boxed{\texttt{hlam1}} ✓$$
$$\qquad \text{其余使用处（}358／382／402／497\text{）一律传}\ \texttt{hlam1}\ \text{或}\ \texttt{hlam0.le} ⟹ \textbf{全部是}\ \le1 ✓✓$$
$$\Longrightarrow \boxed{\text{严格性的第一处（也是唯一可见的）用途 ＝ 产生}\ \le1;\ \textbf{未发现被本质消费}} ✓✓✓$$
$$\qquad \text{error-chain 关键引理皆取}\ \le1：\ \texttt{isLittleO\_sqrtX\_Tl}\ (\le1)\ \text{给出}\ \sqrt X\ll Tl\（X=T^{\lambda},\lambda\le1）;\ \texttt{tendsto\_rpow\_halflam\_sub\_one}\ (\le1)\ \text{给出}\ T^{\lambda/2-1}\to0\（\lambda\le1\Rightarrow\lambda/2-1\le-\frac12）✓✓$$

---

## §2 **严格性的真实用途（= 情况下 A 的机制）**

$$\texttt{CertFlat}\ \text{注释（V310 §1 已录）逐字：\text{"SOME}\ \lambda\in[\frac12,1)\ \text{… already beat the decimals STRICTLY}\ (proof: exact rational value of}\ \kappa\ \text{with}\ \texttt{D1trunc}\ K,K\ge9,\ \textbf{at}\ \lambda=1;\ \texttt{D1}\le\texttt{D1trunc}\,K+\varepsilon_K;\ \boxed{\text{strict at}\ \lambda=1};\ \text{then}\ \boxed{\text{continuity}}\ \text{of}\ \lambda\mapsto\kappa_1(\lambda,v)\ \text{on}\ [\frac12,1]\text{)"}} ✓✓✓$$
$$\Longrightarrow \text{严格性的作用} ＝ \textbf{消 }\varepsilon\ \text{的技术装置};\ \textbf{数值源头在}\ \lambda=1\（\text{有理界在}\ \lambda=1\ \text{处算出}）⟹ \textbf{端点即真值} ✓✓✓$$
$$\qquad \text{故}\ \lambda<1\ \text{不是数学障碍，而是"用连续性把}\ \lambda=1\ \text{处的严格不等式下移"的表述技巧} ✓✓$$

---

## §3 **判词：P3-YES-A ＋ 推荐陈述形式**

$$\boxed{\textbf{P3-YES-A}：\lambda<1\ \text{仅为技术性域限制，可由极限／连续性消除}} ✓✓✓$$
$$\qquad \text{并且}\ \textbf{同意你的谨慎}：\text{连续性}\ \textbf{只} \text{解决右端极限，}\textbf{不能} \text{自动制造}\ \lambda=1\ \text{的有限-}T\ \text{定理} ✓✓$$
$$\text{推荐（不强改源码域）}：\forall\lambda\in[\tfrac12,1):\ G_{\max}(\lambda)\le c^{*}_\lambda\ \Longrightarrow\ \sup_{\lambda<1}G_{\max}(\lambda)\le\lim_{\lambda\to1^-}c^{*}_\lambda=c_1^{*} ✓✓$$
$$\qquad ⚠️\ \textbf{不得} \text{写成}\ G_{\max}(1)\le c_1^{*}\（\text{除非补}\ \lambda=1\ \text{的定理}）✓✓$$

---

## §4 **三层标记（你的第 3 项）**

$$\boxed{c_1^{*}=\frac{\sqrt2\sin(1/\sqrt2)}{\cos(1/\sqrt2)+(1/\sqrt2)\sin(1/\sqrt2)}=0.753296\ldots}\ \xrightarrow{\ F_{\rm opt}(1)=c_1^{*}\ }\ \boxed{G_{\max}(1)=2-\frac1{c_1^{*}}=0.672501\ldots} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{三层分别标记}：\text{① }c_1^{*}\ \text{（V313：}\sup c_{\rm Fun}=c^{*}_\lambda\ \text{，已闭合模形式化）};\ \text{② }F_{\rm opt}(1)\ \text{（V312 字典：}F=c_\lambda\text{）};\ \text{③ }G_{\max}(1)=2-1/F ✓$$
$$\qquad \qquad ⚠️\ \textbf{不得} \text{因①闭合而宣布③闭合};\ \text{但}\ ②\ \text{是源内逐字字典（V307 §5）⟹ ③ 的闭合度}\ \textbf{与①同步但分层记录} ✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

```
① ⚠️ §1 依据 grep（`lam < 1`／`lam_lt_one`）在 `Zeta23/` 全树的命中；**可能遗漏变形写法**（如 `1 > lam`、`lam_lt_one'` 等）⚠️
② ⚠️ §2 的 `CertFlat` 注释为**转述**（V310 §1 所录），本档未再直读 ⚠️
③ **不声称** P3 全域已封闭（仅"第一处使用已定位且非本质"）✓
④ **不声称** 0.67250 已是 Lean theorem ✓
⑤ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐⭐ **P3-YES-A**：`P.lam<1` 的第一处使用 ＝ `hlam.le`（→`≤1`），下游**全部**用 $\le1$；error-chain 引理（`isLittleO_sqrtX_Tl`／`tendsto_rpow_halflam_sub_one`）皆 $\le1$ ⟹ **严格性非本质** ✓✓✓
② ⭐⭐⭐⭐ **严格性的真实用途**：$\varepsilon$-free 证书的表述技巧（`CertFlat`：**$\lambda=1$ 处严格** → 连续性下移）⟹ **数值源头即 $\lambda=1$** ✓✓✓
③ ⭐⭐⭐ **推荐陈述**：$\sup_{\lambda<1}G_{\max}\le\lim_{\lambda\to1^-}c^{*}_\lambda=c_1^{*}$；**不得**直接写 $G_{\max}(1)\le c_1^{*}$ ✓✓
④ ⭐⭐⭐ **三层标记**：$c_1^{*}=0.753296\to F_{\rm opt}(1)\to G_{\max}(1)=0.672501$，逐层记录 ✓✓
【总结（本档给出的最终状态）】
  $$\text{P1-YES}+\text{P2-YES}+\text{P3-YES-A}+\text{V309 全变分最优性}\ \Longrightarrow\ \boxed{\text{数学链已闭合};\ \textbf{仅剩 V307–V309 的 Lean 形式化}}$$
  但仍须并列两项**登记**：① V313 §1 的"（E）库内缺失"结论**可能遗漏同名定理**；② V314 未跑构建 ✓
  下一步建议：**把 V307（E–L 闭式 $\kappa=w\cot w+w^{2}$、$C=\lambda/\kappa=c^{*}_\lambda$）与 V309（$H_\lambda\ge\frac12I$ 严格凸 ⟹ 唯一全局极小）形式化** ⟹ 这是把 0.67250 从"数学链闭合"升为"Lean theorem"的唯一剩余工作 ✓
