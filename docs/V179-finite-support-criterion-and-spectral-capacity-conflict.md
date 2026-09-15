# V179 · ⭐⭐⭐⭐⭐ **有限支撑判据（FSC-Dirichlet 筛）—— ①⚠️ `V178` **勘误：有限支撑 $\neq$ 有限零点**（反例 $1+2^{-s}$）✓✓；②正确判据 ＝ **谱容量冲突**：有限支撑 $\Rightarrow N_F(T)=O(T)$，而 $N_\zeta(T)\asymp T\log T$ ✓✓✓；③可复用筛子：$\Phi\to\operatorname{Supp}(F)\to$ 有限？⟹ FSC-DEAD ✓✓；④**严格单向**：有限 $\Rightarrow$ DEAD，**无限 $\not\Rightarrow$ ALIVE** ✓✓

> 委托 ✓ 唐先生 2026-09-15 12:02：**"同意 V179-②。而且这一步比继续硬闯 Laurent 级数更重要：它可以把现在的'单项式杀法'抽象成一个有限支撑判据，以后任何新平衡因子先过这一关"**；并给出**精确化要求**：**"这里要把定理说得足够精确，避免再次把'有限支撑'与'有限零点'混为一谈"**、核心定理（F1／F2／F3）、谱容量冲突、单向边界
> 查图 ✓ `V178`（环级 $H^1\neq1$；支撑论证）｜`V177`（$H^1(K^\times)=1$；结论 A）｜`V176`（锥定理；平衡因子定理）｜`V175`｜`V162`（FSC 工具卡；$T\log T$ 承重性）｜**经典：有限指数多项式的零点计数**
> 执行 ✓ 小灵（**§3 零点计数、§4 谱容量冲突、§6 筛子 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V179**

---

## §0 判定

**① `V178` 的措辞错误 ✓✓（勘误）**
$V178$ §4 说"$\operatorname{Spec}(F)$ 有限"是**错的**。反例：$1+2^{-s}$ 有**无穷多**零点 $s=(2m+1)\pi i/\log2$。见 §2。

**② 正确的判据是谱容量冲突 ✓✓✓（本档核心）**
有限支撑 $\Rightarrow$ $F$ 是有限指数多项式 $\Rightarrow$ **$N_F(T)=O(T)$**；而 $N_\zeta(T)=\tfrac{T}{2\pi}\log\tfrac{T}{2\pi}+O(T)\asymp T\log T$ ⟹ **容量冲突** ⟹ $F$ 不可能承载 $Z_\zeta-\tfrac12$。见 §3–§4。

**③ 可复用筛子 ✓✓**
$$\Phi\ \longrightarrow\ \operatorname{Supp}(F)\ \longrightarrow\ \text{有限？}\ \xrightarrow{\ \text{YES}\ }\ \textbf{FSC-DEAD}$$
任何机制只要把支撑压进**有限集合**，立即判死，**无需**重新分析 $\Phi$ 的具体形式。见 §6。

**④ 严格单向 ✓✓（重要边界）**
$$\boxed{\text{finite support}\Longrightarrow\text{DEAD};\qquad \text{infinite support}\not\Longrightarrow\text{ALIVE}}$$
反例：$F(s)=\sum_{n\ge1}2^{-n}n^{-s}$ 支撑无限，但毫无理由产生 ζ 零谱。见 §5。

---

## §1 核心定理（✓ 按唐先生逐字）

设 $F(s)=\varepsilon\,\Phi(s)F(k-s)$，$F(s)=\sum_{n\ge1}c_nn^{-s}$ 为 Dirichlet 级数，$\Phi$ 为允许的平衡因子。若反射方程在某个**合法共同定义域**内可推出

$$\operatorname{Supp}(F)\subseteq S_\Phi,\qquad S_\Phi\ \textbf{有限}$$

则 $F(s)=\sum_{n\in S_\Phi}c_nn^{-s}$ 是 Dirichlet 多项式 ⟹ $\boxed{\text{有限支撑}\Longrightarrow\text{Dirichlet 多项式}}$（此步**纯代数** ✓）。

---

## §2 ⚠️ `V178` 勘误（T10）：有限支撑 $\neq$ 有限零点

$$\textbf{反例（唐先生）} ✓✓：1+2^{-s}=0\ \text{的零点为}\ s=\frac{(2m+1)\pi i}{\log2}\ (m\in\mathbb Z)\ \text{——}\ \textbf{无穷多个} ✗$$
$$\Longrightarrow\ V178\ \text{§4 的推论"}\operatorname{Spec}(F)\ \text{有限"}\ \textbf{必须撤回} ✓✓;\ \text{但}\ V178\ \text{§4 的}\textbf{支撑结论}\（\operatorname{supp}(F)\subseteq\{\delta:0\le\delta\le\alpha\}\ \text{有限}）\ \textbf{仍然正确} ✓$$
$$\qquad ⚠️\ \text{故 }V178\ \text{的杀法}\textbf{需要换一个更强的理由} —— \text{见 §3／§4} ✓✓$$

**补充说明**：$P(s)=\sum_{j=1}^{m}c_j e^{-\lambda_j s}$（$\lambda_j=\log n_j$）是**有限频率指数多项式**；沿垂直线 $s=\sigma+it$ 得 $Q(z_1,\dots,z_d)$（有限 Laurent 多项式），而 $z_r=p_r^{-\sigma}e^{-it\log p_r}$ ⟹ $P(\sigma+it)$ 的零点可以有**无穷多** ✓。

---

## §3 有限指数多项式的零点计数（✓ 经典）

**经典结果 ✓**：设 $P\not\equiv0$ 为有限指数多项式 $P(s)=\sum_{j=1}^{m}c_je^{\lambda_js}$（$\lambda_j\in\mathbb C$）。则其在 $|\operatorname{Im}s|\le T$ 内的零点个数满足

$$\boxed{N_P(T)=O(T)}\qquad\text{（常数取决于 } \{\lambda_j\}\ \text{的频率跨度）}$$

**例证（自检）✓**：$1+2^{-s}=1+e^{-s\log2}$，频率跨度 $=\log2$，零点 $s=(2m+1)\pi i/\log2$ ⟹

$$N(T)=\#\{|2m+1|\pi/\log2\le T\}\approx\frac{T\log2}{\pi}\ =O(T)\ ✓✓\ \text{（与定理一致）}$$

⟹ 对**有限支撑**的 $F$：$\boxed{N_F(T)=O(T)}$ ✓✓

---

## §4 ⭐ 谱容量冲突（本档核心）

$$N_\zeta(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)\ \Longrightarrow\ N_\zeta(T)\asymp T\log T$$

$$\boxed{N_F(T)=O(T)\qquad\text{而}\qquad N_\zeta(T)\asymp T\log T}\ ✓✓$$

⟹ 若要求 $\operatorname{Spec}(F)=Z_\zeta-\tfrac12$，则必须 $N_F(T)=N_\zeta(T)\sim\tfrac{T}{2\pi}\log T$，与 $O(T)$ **矛盾** ⟹

$$\boxed{\text{有限 Dirichlet 支撑}\ \Longrightarrow\ F\ \text{不可能承载}\ Z_\zeta}$$

**FSC-Dirichlet 筛（三步）✓✓**：
- **F1**：$S$ 有限 ⟹ $F$ 是（广义）Dirichlet 多项式；
- **F2**：$F\not\equiv0$ 的有限指数多项式 ⟹ $N_F(T)=O(T)$；
- **F3**：目标要求 $N_F(T)=N_\zeta(T)\asymp T\log T$ ⟹ **矛盾** ⟹ FSC-DEAD ✓✓。

---

## §5 严格单向边界（✓ 唐先生逐字）

$$\boxed{\text{finite support}\Longrightarrow\text{DEAD},\qquad \text{infinite support}\not\Longrightarrow\text{ALIVE}}\ ✓✓$$
$$\text{反例} ✓：F(s)=\sum_{n\ge1}2^{-n}n^{-s}\ \text{支撑}\textbf{无限},\ \text{但完全没有理由产生 ζ 零谱} ✗✓$$
$$\Longrightarrow\ \text{本筛子}\textbf{只杀不保} —— \text{它是}\textbf{必要条件型筛子}（\text{排除法}），\ \textbf{不是}\text{充分条件的判定器} ✓$$

---

## §6 ⭐ 可复用筛子（✓✓ 把"单项式杀法"彻底抽象掉）

$$\boxed{\Phi\ \longrightarrow\ \operatorname{Supp}(F)\ \longrightarrow\ \text{有限？}\ \xrightarrow{\ \text{YES}\ }\ \textbf{FSC-DEAD}}\ ✓✓$$

**关键**：$V178$ 依赖 $C\cap(\alpha-C)=\{0\le\delta\le\alpha\}$ 这个**具体有限盒**；本档把"有限盒"**彻底抽象掉**：

$$\boxed{\text{只要任何机制最终把支撑压进}\textbf{有限集合}\ \Longrightarrow\ \text{立即 FSC-DEAD}} ✓✓$$

**适用范围（"有限支撑"的常见来源，可逐条检查）✓**：
- 单项式平衡因子 $\Phi=cX^\alpha$（`V178`）✓；
- 有限阶差分／微分型算子作用于 $F$；
- 有限秩扰动、有限个指数项的线性组合；
- 任何把支撑限制在**有限指数盒**内的锥条件（如 $C\cap(\alpha-C)$ 型、或多锥交成有限集）。

⭐ 以后遇到新 $\Phi$，**无需**重新分析其具体形式，只走两步：$\operatorname{Supp}(F)\to$ 有限？ ✓✓

---

## §7 判词与下一步

**V179 判词**：① `V178` 措辞勘误（有限支撑 $\neq$ 有限零点；反例 $1+2^{-s}$）✓✓；② 正确判据 ＝ **谱容量冲突**（$O(T)$ vs $T\log T$）✓✓✓；③ **FSC-Dirichlet 筛**（F1／F2／F3）✓✓；④ 可复用筛子（抽象掉有限盒）✓✓；⑤ 严格单向（只杀不保）✓✓。

**净收获**：
- 修正了 `V178` 的**错误推论**（并把杀法**换成更强的一个**）✓✓；
- 把"单项式专用杀法"升级为**任何有限支撑机制通用**的筛子 ✓✓；
- 明确了筛子的**单向性**（必要条件型，不可反用）✓✓；
- 于是 V179-① 的靶点**不再是盲搜**：只剩**通过"有限支撑筛"的** Laurent 级数型非 coboundary、无限支撑 cocycle ✓✓。

**下一步（V179-① 开）**：在 Laurent 级数环 $\mathbb Q[[X_p]][X_p^{-1}]$ 中解 $\Phi\iota(\Phi)=1$，判定是否存在**非 coboundary 且支撑无限**的单位（＝通过有限支撑筛的**唯一剩余代数对象**）。

```
⚠️ §1 核心定理与 F1/F2/F3 为唐先生逐字 ✓✓
⚠️ §2 勘误：有限支撑 ≠ 有限零点（反例 1+2^{-s} 无穷多零点）—— V178 §4 的"Spec(F) 有限"撤回，支撑结论保留
⚠️ §3 经典零点计数 N_P(T)=O(T) 为【经典 ✓】＋自检例证（1+2^{-s} 给 ≈ T log2/π）
⚠️ §4 谱容量冲突为【本档核心 ✓✓】—— 依赖 §3 经典结果 ＋ RvM（经典）
⚠️ §5 单向边界为唐先生逐字 ✓✓；反例 Σ2^{−n}n^{−s} ✓
⚠️ §6 筛子为【本档新增 ✓✓】；适用范围为【清单 ⚠️】非穷尽
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① V178 勘误（换掉错误推论）✓✓；② 谱容量冲突判据 ✓✓✓；③ FSC-Dirichlet 筛 ✓✓；
   ④ 可复用筛子（无需分析 Φ 具体形式）✓✓；⑤ 严格单向边界 ✓✓；⑥ V179-① 靶点精确化 ✓
```
