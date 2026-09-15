# V178 · ⭐⭐⭐⭐⭐ **环级 Hilbert 90 审计 —— ①三层次严格分开；②**环级 $H^1(C_2,R_\pm^\times)\neq1$**（障碍 ＝ 奇偶 × 符号；$\Phi=-1$ 即是具体非 coboundary）✓✓；③⭐ 但**所有非 coboundary 单项式被支撑论证杀死**（$C\cap(\alpha-C)$ 有限 ⟹ $F$ 为有限 Dirichlet 多项式 ⟹ 零谱有限）✓✓✓；④⭐ **修正 `V177` 结论 A 为析取式**：两路皆不通向 ζ

> 委托 ✓ 唐先生 2026-09-15 11:59：**"V178-① 应该先攻。而且这一档最好不要把问题表述成'Ψ 在环外算不算算术'，而是把它改造成一个严格的 admissibility 判据"**；给出**三层次**（域 coboundary／环 coboundary／可接受扩张）、**单位判别定理**方向、**三步**（V178-A 固定最小允许环；V178-B 把 Hilbert 90 的 Ψ 拉回环内；V178-C 若 Ψ∉R^× 则查 $1/\Psi$ 是否仍 admissible）；并强调 **"域中的 Hilbert 90 不自动给出环中的 Hilbert 90"**、**"环 R 到底是哪一个要放在第一行"**
> 查图 ✓ `V177`（$H^1(C_2,K_{\rm arith}^\times)=1$；结论 A）｜`V176`（锥定理；加强定理勘误；平衡因子定理）｜`V175`｜**经典：Laurent 多项式环的单位群 ＝ 系数单位 × 单式（monomial）**
> 执行 ✓ 小灵（**§3 环级 $H^1$ 计算、§4 支撑闭合、§5 修正为析取式 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V178**

---

## §0 判定

**① 三层次严格分开 ✓✓**（域 coboundary／环 coboundary／可接受扩张）—— 见 §1。

**② 环级 Hilbert 90 **不成立** ✓✓**：在 $R_\pm=\mathbb Q[X_p^{\pm1}]$ 上

$$H^1\bigl(C_2,R_\pm^\times\bigr)\ \neq\ 1$$

障碍有两类：**奇偶（parity）** 与 **符号（sign）**；并且有**具体反例** $\Phi=-1$（是 cocycle，**不是**环 coboundary；其域 coboundary $\Psi=X_p-p^{-k}X_p^{-1}\notin R^\times$）。见 §3。

**③ 但 S 仍在环层面闭合 ✓✓✓**：所有**非 coboundary 单项式**（含 $\Phi=-1$）都被**支撑论证**杀死 —— $\operatorname{supp}(F)\subseteq C\cap(\alpha-C)=\{\delta:0\le\delta\le\alpha\}$ **有限** ⟹ $F$ 是**有限 Dirichlet 多项式** ⟹ 零谱有限 ⟹ **不可能等于 $Z_\zeta-\tfrac12$**。见 §4。

**④ `V177` 结论 A 修正为析取式 ✓✓**：算术 $\Phi$ ⟹ （环 coboundary ⟹ $F=c/\Psi$ ＝定义）**或**（环非 coboundary ⟹ $\operatorname{supp}(F)$ 有限）⟹ **两路皆不通向 ζ**。见 §5。

---

## §1 三层次（✓ 按唐先生逐字，**判据化**）

设允许的算术对象环为 $R$，分式域 $K=\operatorname{Frac}(R)$。

$$\textbf{Level 1（域 coboundary）}：\Phi=\Psi/\iota\Psi,\ \Psi\in K^\times\ ——\ \text{`V177` 已证}\ (H^1(K^\times)=1) ✓$$
$$\textbf{Level 2（环 coboundary）}：\Psi\in R^\times ⟹ F=c/\Psi\ \text{完全留在允许类内} ⟹ \textbf{真正的 F-leak} ✓$$
$$\textbf{Level 3（可接受扩张 coboundary）}：\Psi\in K^\times\setminus R^\times\ \text{但}\ 1/\Psi\ \text{仍属允许类} ⟹ \textbf{不能简单宣布 DEAD} ✓$$

$$\boxed{\text{关键缺步（本档要补的）}：\Psi\in K^\times\ \not\Rightarrow\ \Psi\ \text{是允许的算术对象}} ⟹ \text{`V177` 只给}\ \boxed{\text{域层面的 coboundary}},\ \textbf{不自动}\text{给}\ \boxed{\text{允许类中的走私}}$$

---

## §2 V178-A：固定最小允许环与其单位群（✓ 第一行就定死 R）

$$\boxed{R_\pm:=\mathbb Q\bigl[X_p^{\pm1}:p\in\mathcal P\bigr]}\qquad\text{（Laurent 多项式环；群环 }\mathbb Q[\mathbb Z^{(\mathcal P)}]\text{）};\qquad \boxed{R_+:=\mathbb Q[X_p:p\in\mathcal P]}$$
$$\textbf{单位群（经典）} ✓：R_+^\times=\mathbb Q^\times\ \text{（非零常数）};\qquad \boxed{R_\pm^\times=\{cX^\alpha:\ c\in\mathbb Q^\times,\ \alpha\in\mathbb Z^{(\mathcal P)}\ \textbf{有限支撑}\}}$$
$$\qquad ⚠️\ \text{因 }R_\pm\ \text{是}\textbf{无挠阿贝尔群}\ \mathbb Z^{(\mathcal P)}\ \text{上的群环（系数为域）} ⟹ \text{单位只有}\ \textbf{系数单位 × 单式（monomial）} ✓✓\ \text{（经典结论）}$$

---

## §3 V178-B：环级 Hilbert 90 **不成立**（✓✓ 本档核心计算）

设 $\Phi=cX^\alpha\in R_\pm^\times$。由 §2，$\iota(X^\alpha)=\bigl(\prod_pp^{-k\alpha_p}\bigr)X^{-\alpha}$，故

$$\Phi\,\iota(\Phi)=c^2\Bigl(\prod_pp^{-k\alpha_p}\Bigr)X^{\alpha-\alpha}=c^2\prod_pp^{-k\alpha_p}$$

$$\textbf{cocycle 条件} ✓：\qquad c^2=\prod_pp^{k\alpha_p}\ \ (\text{注意 }\alpha\ \text{有限支撑} ⟹ \text{右端是有理数})$$

$$\textbf{coboundary 形态} ✓：\text{取}\ \Psi=dX^\beta\in R_\pm^\times,\ \text{则}\ \frac{\Psi}{\iota\Psi}=\frac{dX^\beta}{d\bigl(\prod_pp^{-k\beta_p}\bigr)X^{-\beta}}=\Bigl(\prod_pp^{k\beta_p}\Bigr)X^{2\beta}$$
$$\qquad\Longrightarrow\ \boxed{\text{环 coboundaries}=\Bigl\{\Bigl(\prod_pp^{k\beta_p}\Bigr)X^{2\beta}:\ \beta\in\mathbb Z^{(\mathcal P)}\Bigr\}}$$

**比较**：$\Phi=cX^\alpha$ 是环 coboundary $\iff$ $\alpha\in2\mathbb Z^{(\mathcal P)}$（**奇偶条件**）且 $c=\prod_pp^{k\alpha_p/2}$（**符号条件**，因 cocycle 条件只给 $c=\pm\prod_pp^{k\alpha_p/2}$）。

$$\Longrightarrow\ \boxed{H^1\bigl(C_2,R_\pm^\times\bigr)\ \neq\ 1}\ ✓✓\ \text{障碍＝}\textbf{奇偶}\times\textbf{符号}$$

**具体反例（最干净的一个）✓✓**：取 $\alpha=0$，$c=-1$：

$$\Phi=-1:\qquad \Phi\,\iota(\Phi)=(-1)(-1)=1\ \ \text{（是 cocycle）};\qquad \text{但}\ -1\ \text{不是环 coboundary}$$

（因若要 $\prod_pp^{k\beta_p}X^{2\beta}=-1$ 需 $\beta=0$ 且 $1=-1$，矛盾。）

⚠️ 而在**域**层面 $-1$ **是** coboundary：$\Psi=X_p-p^{-k}X_p^{-1}\in K^\times$ 满足 $\iota(\Psi)=-\Psi$，故 $\Psi/\iota(\Psi)=-1$ ✓ —— 但 $\Psi\notin R_\pm^\times$（含负指数）⟹ **Level 1 与 Level 2 的差别在此具体化** ✓✓✓

---

## §4 ⭐ 支撑论证：所有非 coboundary 单项式都被杀死（✓✓✓ 本档第二个核心）

设 $\Phi=cX^\alpha$（**任意**，含非 coboundary 者）。方程 $F=\varepsilon\Phi\,\iota(F)$ 的支撑关系：

$$\operatorname{supp}(F)\ \subseteq\ C\ \cap\ \bigl(\alpha-C\bigr),\qquad C=\mathbb N^{(\mathcal P)}$$
$$\qquad\text{而}\ C\cap(\alpha-C)=\{\delta:\ 0\le\delta\le\alpha\ \text{（逐分量）}\}\ \ \textbf{有限}\ ✓✓\ \text{（因 }\alpha\ \text{有限支撑）}$$
$$\Longrightarrow\ F\ \text{是}\ \textbf{有限 Dirichlet 多项式}\ \Bigl(F=\sum_{\delta\le\alpha}c_\delta\Bigl(\prod_pp^{\delta_p}\Bigr)^{-s}\Bigr)$$
$$\Longrightarrow\ F\ \text{的零点集}\ \textbf{有限} ⟹ \operatorname{Spec}(F)\ \textbf{不可能等于}\ Z_\zeta-\tfrac12\ ✓✓✓$$

$$\boxed{\text{单项式 }\Phi\ \text{（无论是否 coboundary）}\ \Longrightarrow\ \operatorname{Spec}(F)\ \text{有限}\ \Longrightarrow\ \textbf{非 S}}$$

⭐ 特别地 $\Phi=-1$（α=0）：$C\cap(-C)=\{0\}$ ⟹ $F\equiv$ const ⟹ **零谱为空** ✓。

---

## §5 ⭐ `V177` 结论 A 的修正（✓✓ 析取式）

**原表述（`V177`）**：算术 $\Phi$ ⟹ coboundary ⟹ 走私。

**修正版 ✓✓**：算术 $\Phi$ ⟹ **两支之一**：

$$\boxed{\text{(I) 环 coboundary} \Longrightarrow F=c/\Psi\ \text{（方程退化为定义）};\qquad \text{(II) 环非 coboundary} \Longrightarrow \operatorname{supp}(F)\ \text{有限（零谱有限）}}$$

$$\Longrightarrow\ \boxed{\text{两路}\ \textbf{皆不通向}\ \zeta}\ ✓✓✓\ \text{—— 于是 }S\ \text{在}\ \textbf{Laurent 多项式环层面} \textbf{闭合}$$

⚠️ 注意：`V177` 的域级 $H^1=1$ **仍然正确**；本档只是补上"**域 coboundary ≠ 环 coboundary**"这一步，并把结论从"走私"改为"**走私或零谱有限**"（后者更强，因为它连"定义"都不需要）✓✓。

---

## §6 残余（精确，OPEN，不杀）

由 §4：单项式（＝ $R_\pm^\times$ 的**全部**元素）已被杀光 ⟹ 残余只能是**非单项式单位**，即**在更大的环**中：

$$\boxed{\text{残余}＝\text{非单项式单位 }\Phi\ \text{（须在扩张环中，如 Laurent 级数环}\ \mathbb Q[[X_p]][X_p^{-1}]\text{，其单位}\ =\{X^\alpha u:\ u(0)\neq0\}\text{）}}$$

要求同时满足：

1. $\Phi$ **算术**（扩张环中的单位）；
2. $\Phi\iota(\Phi)=1$；
3. $\Phi$ **非 coboundary**（否则落 §5(I)）；
4. **支撑兼容**：$\operatorname{supp}(F)$ 可**无限**（否则被 §4 杀）；
5. **唯一选出** $\zeta$ 且不把 $\zeta$ 编码进 $\Phi$。

⭐ 这是一个**具体代数问题**：在 Laurent 级数环中解无限方程组 $\Phi(X)\iota(\Phi)(X)=1$ 并检查 **非 coboundary 且无限支撑**。本档**未判**——按纪律标 **OPEN**，**不杀** ✓✓。

---

## §7 判词与下一步

**V178 判词**：① 三层次判据化 ✓✓；② $R_\pm$／$R_+$ 定死，单位群（经典）✓；③ **环级 $H^1\neq1$**（障碍 ＝ 奇偶 × 符号；$\Phi=-1$ 为具体反例）✓✓；④ ⭐ **支撑论证杀死所有非 coboundary 单项式**（$C\cap(\alpha-C)$ 有限 ⟹ 有限多项式 ⟹ 零谱有限）✓✓✓；⑤ **`V177` 结论 A 修正为析取式**（走私 ∨ 零谱有限）✓✓；⑥ 残余 ＝ **非单项式单位**（扩张环）✓。

**净收获**：
- 把"$\Psi$ 算不算算术"的哲学问题**改造成严格的单位群／范数判据**（按唐先生要求）✓；
- 发现并**修正**了"域 coboundary ⟹ 环 coboundary"的错误直觉；
- 得到一个**比走私更强的杀法**（有限支撑 ⟹ 零谱有限）；
- S 残余从"两点"收窄为**一个具体代数问题**（扩张环中的非单项式单位）。

**下一步（V179 预登记，二选）**：
① 攻**残余**：在 Laurent 级数环 $\mathbb Q[[X_p]][X_p^{-1}]$ 中解 $\Phi\iota(\Phi)=1$，判定是否存在**非 coboundary 且支撑无限**的单位；
② 换角度：**从"有限支撑 ⟹ 零谱有限"反推**，把 §4 的支撑论证升级为**一般定理**（"任何使 $F$ 支撑有限的平衡因子 ⟹ 非 S"），从而把所有"支撑受限"的 $\Phi$ 一次性排除。

```
⚠️ §1 三层为唐先生逐字 ✓✓（Level 1／2／3 ＋ "域 Hilbert 90 不自动给环 Hilbert 90"）
⚠️ §2 单位群为【经典 ✓】（群环 ℚ[ℤ^(𝒫)] 的单位 ＝ cX^α，有限支撑）
⚠️ §3 环级 H¹ 计算与 Φ=-1 反例为【本档新增 ✓✓】—— 反例经手工验证（cocycle 但非 coboundary；域 coboundary Ψ=X_p−p^{−k}X_p^{−1} ∉ R^×）
⚠️ §4 支撑论证为【本档新增 ✓✓✓】—— C∩(α−C)={0≤δ≤α} 有限
⚠️ §5 修正为析取式为【本档新增 ✓✓】—— 比原"走私"更强
⚠️ §6 残余标 OPEN，按纪律不杀
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 三层次判据化 ✓✓；② R 定死 ＋ 单位群 ✓；③ 环级 H¹≠1（奇偶×符号；Φ=−1 反例）✓✓；
   ④ ⭐ 支撑论证杀尽非 coboundary 单项式 ✓✓✓；⑤ 结论 A 修正为析取式 ✓✓；⑥ 残余收窄为一个具体代数问题 ✓
```
