# V177 · ⭐⭐⭐⭐⭐ **$\Phi\Phi^\iota=1$ 的群上同调审计 —— ①⚠️ `V176`-② **勘误：降级为形式域版本** ✓✓；②**$K_{\rm arith}$ 严格定义 ＋ $H^1(C_2,K_{\rm arith}^\times)=1$**（Hilbert 90 ＋ Artin）✓✓；③**结论 A**：算术 $\Phi$ ⟹ coboundary ⟹ $F=c/\Psi$ ⟹ 走私 —— **`V176`(iii) 正式闭合** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 11:56：**"可以开 V177-②，但这里我建议先做一个比'严格化'更重要的动作：先给 V176 的核心命题补上适用域，否则②严格化时会把一个隐藏的逻辑缺口正式化"**；给出勘误（跨收敛域比较）、群上同调形式化（$Z^1$／$B^1$／$H^1$）、三种结论（A／B／C）；并**把目标改成"先算清楚 $H^1(C_2,K_{\rm arith}^\times)$"**
> 查图 ✓ `V176`（锥定理；加强定理；平衡因子定理）｜`V175`（局部因子刚性）｜`V174`（反射可内生/轴不可内生）｜`V173`（引理 1）｜**Hilbert 90（经典）**｜**Artin 定理（Galois 理论，经典）**
> 执行 ✓ 小灵（**§1 勘误、§3 H¹ 计算、§4 结论 A 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V177**

---

## §0 判定

**① `V176`-② 表述过强，须降级 ✓✓（勘误）**
"任意 Dirichlet 级数的解析函数方程 $\Rightarrow$ 常函数"**不能**成立 —— 因为一般 Dirichlet 级数只在**右半平面**收敛，而 $F(k-s)$ 在**左半平面**；把两者逐系数比较，等于**偷偷把"能跨收敛边界比较"这个最困难的东西当成前提**。严格版本必须把"可在共同体形式域中逐系数解释"写进假设。见 §1。

**② $H^1(C_2,K_{\rm arith}^\times)=1$ ✓✓（本档核心）**
在自然的算术域（$\iota$ 为其 2 阶自同构的 char-0 域）上，**Hilbert 90 ＋ Artin** 直接给出 $H^1=1$ ⟹ **每个反自对偶 $\Phi$ 都是 coboundary**。见 §3。

**③ 结论 A 成立：`V176`(iii) 正式闭合 ✓✓✓**
$\Phi=\Psi/\iota(\Psi)$ ⟹ $F\Psi=\varepsilon\,\iota(F\Psi)$ ⟹（修正后的锥定理）$F\Psi=$ const ⟹ **$F=c/\Psi$** ⟹ **算术平衡因子 ＝ coboundary ＝ gauge 变换** ⟹ F-leak／走私。见 §4。

---

## §1 ⚠️ `V176`-② 勘误（T10）：补上适用域

**原表述（过强，撤回）**：

$$\text{任一 Dirichlet 级数}\ F(s)=\sum c_nn^{-s}\ \text{若}\ F(s)=\varepsilon F(k-s)\Longrightarrow F=\text{constant} \qquad ✗$$

**问题**：$F(s)=\sum c_nn^{-s}$ 只在某**右半平面**绝对收敛；$F(k-s)$ 对应**左半平面**。逐系数比较 $n^{-s}\leftrightarrow n^{s-k}$ 隐含了"两边可在同一（形式或解析）层面比较"。而 ζ 的函数方程之所以能联系两个方向，**恰恰是因为存在跨越两个收敛域的完成结构** ⟹ 原表述把该结构**偷渡**成了前提。

**修正后的严格版本 ✓✓**：

$$\boxed{F(s)=\sum c_nn^{-s};\quad F(s)=\varepsilon F(k-s);\quad \textbf{且该恒等式可在共同的 Dirichlet／Laurent 形式域中逐系数解释}\ \Longrightarrow\ F=\text{constant}}$$

即：**定理的适用域是"形式域（共同 Laurent 形式域）中可逐系数解释的恒等式"**，而**不是**"任意 Dirichlet 级数的解析函数方程"。

⭐ 这一降级**不影响** `V176`-③ 的逻辑链（因为那条链**本来**就在形式域（Laurent 形式域）中运作）✓✓；但它**必须**先写明，否则 §4 的 coboundary 消去步骤会建立在未证的跨域比较上。

---

## §2 群上同调形式化（✓ 按唐先生逐字）

令 $\iota(s)=k-s$（对合），要求

$$\Phi(s)\,\Phi(\iota s)=1$$

⟹ $\Phi$ 是 $C_2$-对合下的**乘法 1-cocycle**：$\Phi\in Z^1(C_2,K^\times)$。

**coboundary** 是形如

$$\Phi=\frac{\Psi}{\iota\Psi}\qquad(\Psi\in K^\times)$$

的元素，记 $B^1(C_2,K^\times)$。真正的判据是商空间

$$H^1(C_2,K^\times)=Z^1\big/B^1$$

$$\boxed{\text{若}\ H^1=1\ \text{，则}\ \Phi\Phi^\iota=1\Longrightarrow\Phi=\Psi/\Psi^\iota\ \text{（coboundary）}}$$

⭐ 一旦是 coboundary，代入 $F=\varepsilon\Phi\,\iota F$ 立即得

$$F\Psi=\varepsilon\,\iota(F\Psi)$$

再结合**修正后的锥定理**（§1）⟹ $F\Psi=$ const ⟹ $F=c/\Psi$ ✓。

---

## §3 ⭐ $K_{\rm arith}$ 的严格定义与 $H^1$ 计算（本档核心）

### (3a) 取什么作为 $K_{\rm arith}$？

自然选择：**以局部参数 $X_p=p^{-s}$ 为变量的 char-0 有理函数域**

$$K_{\rm arith}:=\mathbb Q\bigl(X_p:\ p\in\mathcal P\bigr)$$

（系数在 $\mathbb Q$ —— 这是"**纯算术**"的最自然含义：只有素数 $p$ 与有理系数进入，**不含**任何 archimedean 因子。）

### (3b) $\iota$ 是 $K_{\rm arith}$ 的 2 阶自同构 ✓

反射 $s\mapsto k-s$ 在局部参数上的作用是

$$\iota:\ X_p\longmapsto p^{-k}X_p^{-1}$$

- 这是 $\mathbb Q(X_p)$ 的**单项式替换**（$p^{-k}\in\mathbb Q$）✓；
- $\iota^2(X_p)=p^{-k}\bigl(p^{-k}X_p^{-1}\bigr)^{-1}=p^{-k}p^{k}X_p=X_p$ ⟹ $\iota^2=\mathrm{id}$ ✓；
- 像生成整个域（每个 $X_p$ 可由 $\iota(X_p)$ 反解）⟹ $\iota\in\operatorname{Aut}\mathbb Q(X_p)$，且 $\operatorname{ord}(\iota)=2$ ✓✓。

⟹ $\iota$ 是 $K_{\rm arith}$ 的**2 阶自同构** ✓。

### (3c) $H^1=1$（Hilbert 90 ＋ Artin）✓✓

记固定域 $L:=K_{\rm arith}^{\iota}$。由 **Artin 定理**（有限自同构群 ⟹ 扩张次数等于群阶）：

$$[K_{\rm arith}:L]=|\{1,\iota\}|=2$$

⟹ $K_{\rm arith}/L$ 是**二次 Galois 扩张**，群 $C_2=\{1,\iota\}$ ✓。由 **Hilbert 90**（循环扩张的乘性 $H^1$ 消失）：

$$\boxed{H^1\bigl(C_2,\ K_{\rm arith}^\times\bigr)=1}\qquad\text{即}\qquad \{\Phi:\Phi\Phi^\iota=1\}=\Bigl\{\frac{\Psi}{\Psi^\iota}:\Psi\in K_{\rm arith}^\times\Bigr\} ✓✓$$

⭐ **逐字对应**：Hilbert 90 的"范数 1"条件就是我们的反自对偶条件（$N(\Phi)=\Phi\cdot\iota(\Phi)=1$），而"$\Psi/\iota(\Psi)$"就是 coboundary ✓✓。

---

## §4 ⭐ 结论 A：算术平衡因子 ＝ coboundary ＝ gauge 变换（`V176`(iii) 正式闭合）

链：

$$\Phi\in K_{\rm arith}^\times,\ \Phi\Phi^\iota=1\ \xrightarrow{\ \S3\text{c}\ }\ \Phi=\frac{\Psi}{\iota\Psi}\ \xrightarrow{\ \text{代入}\ }\ F\Psi=\varepsilon\,\iota(F\Psi)\ \xrightarrow{\ \S1\ \text{（修正版锥定理）}\ }\ F\Psi=\text{const}$$

$$\boxed{F=c/\Psi}$$

⟹

$$\boxed{\textbf{算术平衡因子}\ =\ \text{coboundary}\ =\ \textbf{gauge 变换}}$$

即：**算术的 $\Phi$ 不携带约束信息** —— 它把函数方程**吸收进 $F$ 的定义**（$F$ 由 $\Psi$ 决定，而非被约束）⟹ **F-leak／走私** ✓✓✓

⭐ 这**不再**是"看起来像走私"，而是**严格定理** ✓✓。

**为什么经典 $\Gamma$ 能行（机制解释的最后一环）✓✓**：

$$\Gamma(s/2)\ \notin\ \mathbb Q\bigl(X_p\bigr)$$

因为 $s=-\log X_p/\log p$，故 $\Gamma(s/2)=\Gamma\bigl(-\tfrac{\log X_p}{2\log p}\bigr)$ 是 $X_p$ 的**超越函数**，**不是有理函数** ⟹ **不在定理作用域内** ⟹ 它可以**合法地**作为"非 coboundary"的平衡因子 ⟹ 与 `V176`(iv)"$\Phi$ 必须非算术"**完全一致** ✓✓✓

⟹ 于是本档给出一条完整的因果链：

$$\text{算术}\Phi\ \Rightarrow\ \text{coboundary}\ \Rightarrow\ F=c/\Psi\ \Rightarrow\ \text{空转（走私）};\qquad \text{非算术}\Phi\ \Rightarrow\ \text{archimedean 完成因子}$$

---

## §5 结论 B／C 的判定（✓ 三选）

- **A（本档命中）✓✓**：在 $K_{\rm arith}=\mathbb Q(X_p)$（及更一般的 char-0 域）上 $H^1=1$ ⟹ 算术 $\Phi$ 必为 coboundary ⟹ 走私。
- **B（未命中）**：$H^1\neq1$ 但所有非平凡类不能与 Dirichlet 正锥兼容 —— 本档**未出现**此情形（因为 $H^1$ 已算为 1）。
- **C（未命中）**：存在非平凡类且保持正锥、非走私、唯一选 $\zeta$ ⟹ **S 命中** —— 本档**未出现**。

---

## §6 残余（精确；按纪律保留 OPEN，不杀）

尽管 $H^1(C_2,K_{\rm arith}^\times)=1$，仍有两处**$K_{\rm arith}$ 未覆盖**的算术 $\Phi$：

1. **$\Phi$ 在"单位环"而非"域"中**：若要求 $\Phi$ 属于**形式 Dirichlet 型级数的单位群**（而非其分式域），则 Hilbert 90 给出的 $\Psi$ **可能落在环外** ⟹ 结论"$F=c/\Psi$"仍成立，但"$\Psi$ 是否算算术对象"需另议。⟹ **这是本档新暴露的唯一严格残余** ✓。
2. **非有理函数型的算术 $\Phi$**：例如含"算术指数"的无穷乘积（$\prod_p(\dots)$ 型），已超出 $\mathbb Q(X_p)$ ⟹ Hilbert 90 不适用 ⟹ **未判**。

⚠️ 两者均按纪律标 **OPEN**，**不杀** ✓。

---

## §7 判词与下一步

**V177 判词**：① `V176`-② 已勘误（降级为形式域版本，补上"可共同逐系数解释"的适用域）✓✓；② $K_{\rm arith}$ 严格定义为 $\mathbb Q(X_p)$，$\iota$ 为其 2 阶自同构 ✓；③ **$H^1(C_2,K_{\rm arith}^\times)=1$**（Artin ＋ Hilbert 90）✓✓；④ **结论 A 成立**：算术 $\Phi$ ⟹ coboundary ⟹ $F=c/\Psi$ ⟹ 走私 —— **`V176`(iii) 正式闭合** ✓✓✓；⑤ $\Gamma\notin\mathbb Q(X_p)$ ⟹ 与"$\Phi$ 必须非算术"完全一致 ✓✓；⑥ 残余两点（单位环外 coboundary／非有理函数型 $\Phi$）✓。

**净收获**：
- 把 `V176`-③ 从"结构论证"升级为**上同调定理**（$H^1=1$）；
- 补上 `V176`-② 的适用域（避免把跨域比较偷渡）；
- 给出"为什么 $\Gamma$ 必须出现"的**完整机制链**。

**下一步（V178 预登记，二选）**：
① 攻**残余 1**：**单位环 vs 域** —— 若 $\Psi$ 落在环外，$F=c/\Psi$ 还算不算"算术定义"？（这是本档暴露的唯一严格缺口）
② 攻**残余 2**：**非有理函数型的算术 $\Phi$**（无穷乘积型）—— 构造候选或证明不可能。

```
⚠️ §1 勘误为唐先生逐字 ✓✓（跨收敛域比较必须写进假设）；本档同步给 V176 挂 T10 勘误
⚠️ §3 为【本档新增 ✓✓】：K_arith=ℚ(X_p) 的严格定义、ι 为 2 阶自同构（ι²=id 验证）、Artin ＋ Hilbert 90 ⟹ H¹=1
⚠️ §4 结论 A 为【本档新增 ✓✓】—— 依赖 §1 修正后的锥定理适用域
⚠️ §4 末"Γ ∉ ℚ(X_p)"为【本档新增 ✓】—— 机制解释的最后一环
⚠️ §5 中 B／C 均未出现（因 H¹ 已算为 1）
⚠️ §6 残余两点标 OPEN，按纪律不杀
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① V176-② 勘误（形式域版本）✓✓；② K_arith 严格定义 ＋ ι 阶数验证 ✓；
   ③ H¹(C₂,K_arith^×)=1（Artin＋Hilbert 90）✓✓；④ 结论 A：算术 Φ ⟹ coboundary ⟹ F=c/Ψ（V176(iii) 正式闭合）✓✓✓；
   ⑤ Γ ∉ ℚ(X_p) 与"必须非算术"一致 ✓✓；⑥ 残余两点 ✓
```

---

## §8 精化注记（`V178` 追问后补 · 2026-09-15 12:0x ✓）

$$\text{本档 §4}\ \textbf{结论 A}\ \text{成立，但它是}\textbf{域级}\text{结论（}K_{\rm arith}^\times\text{）；}\textbf{不等价于}\text{环级结论} ✗✓$$
$$\qquad\Longrightarrow\ \text{`V178` 已算：}H^1(C_2,R_\pm^\times)\neq1\ \text{（}R_\pm=\mathbb Q[X_p^{\pm1}]\text{；障碍＝奇偶×符号；}\Phi=-1\ \text{即反例）} ✓✓$$
$$\qquad\Longrightarrow\ \text{故 §4 的"走私"结论须}\textbf{改写为析取式} ✓✓：\text{算术 }\Phi\Longrightarrow\ (\text{环 coboundary}\Longrightarrow F=c/\Psi\ \text{＝定义})\ \textbf{或}\ (\text{环非 coboundary}\Longrightarrow\operatorname{supp}(F)\ \text{有限}\Longrightarrow\ \text{零谱有限})$$
$$\qquad ⚠️\ \text{本档 }H^1(K^\times)=1\ \text{仍正确};\ \text{只是}\ \textbf{域 coboundary}\not\Rightarrow\textbf{环 coboundary} ✓\ \text{（具体化于}\ \Psi=X_p-p^{-k}X_p^{-1}\notin R^\times）$$
