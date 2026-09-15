# V176 · ⭐⭐⭐⭐⭐ **跨素数混合对合审计 —— ①锥定理（单项式）：保持 Euler 正锥的有限阶对合 ＝ 素数置换（无反演）✓；②⭐ **本档加强定理**：裸反射对所有 Dirichlet 级数只有**常解**（**不需要** Euler 积、**不需要**逐素数可分）✓✓；③⭐ **平衡因子定理**：任何非平凡反射必含 $\Phi\neq1$，且**算术的 $\Phi$ ⟹ 函数方程退化为"定义"而非"约束"（＝走私）** ✓✓**

> 委托 ✓ 唐先生 2026-09-15 11:52：**"开。V176 应该直接攻 S-ii，而且不要先'找一个看起来混合'的例子，而是把'混合素数对合'形式化到足以一击判死的程度"**；给出指数锥形式化、**单项式跨素数对合定理**（其证明）、二分（S-ii(a)/(b)）、以及**真正剩余的漏洞**（非线性 substitution）、并指定真正目标："**先攻正幂级数环的有限阶自同构分类，再看反演能否存活**"
> 查图 ✓ `V175`（局部因子刚性；逐素数可分）｜`V174`（反射可内生/轴不可内生）｜`V173`（引理 1）｜`V172`（A-leak 扩张）｜`V171`（Hamburger 1921）｜`V144`（α_p≡1）
> 执行 ✓ 小灵（**§3 加强定理、§4 平衡因子定理 为本档新增**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V176**

---

## §0 判定

**① 锥定理（单项式情形）成立 ✓✓**
$A\in GL$、$A^2=I$、$A(C)=C$（$C=\mathbb N^{(\mathcal P)}$）⟹ $A$ 必为**素数置换矩阵**，因而**不含反演**。见 §2（用户三行证明）。

**② ⭐ 加强定理（本档新增）：裸反射对所有 Dirichlet 级数只有常解 ✓✓**
$F(s)=\sum_{n\ge1}c_nn^{-s}$ 若满足 $F(s)=\varepsilon F(k-s)$，则 $c_n=0\ (n>1)$，即 $F\equiv c_1$。
**不需要 Euler 积，不需要逐素数可分** —— 严格强于 `V175`。见 §3。

**③ ⭐ 平衡因子定理（本档新增）：算术的平衡因子 ⟹ 走私 ✓✓**
任何非平凡反射必写成 $F(s)=\varepsilon\,\Phi(s)F(k-s)$ 且 $\Phi\neq1$；而若 $\Phi$ **算术**，则函数方程退化为"$F$ 的定义"（$F=c/\Psi$）而非对 $F$ 的约束 ⟹ **F-leak／走私**。见 §4。

---

## §1 形式化：混合对合与指数锥（✓ 按唐先生逐字）

把形式 Euler 对象写成不完全可分的形状：

$$F(\mathbf X)=\sum_{\alpha\in\mathbb N^{(\mathcal P)}}c_\alpha\mathbf X^\alpha,\qquad \mathbf X^\alpha=\prod_pX_p^{\alpha_p}$$

（**不要求** $F=\prod_pF_p(X_p)$ ⟹ 已真正离开 `V175` 的逐素数可分假设。）

最一般的**单项式型跨素数对合**：

$$\iota(\mathbf X)_p=c_p\prod_qX_q^{A_{pq}},\qquad A^2=I$$

为模拟 $s\mapsto k-s$，$A$ 中**至少含负方向**；最直接情形 $A=-P$（$P$ 素置换），例如交换 $p,q$：

$$X_p\mapsto q^{-k}X_q^{-1},\qquad X_q\mapsto p^{-k}X_p^{-1}$$

这**确实是真正的跨素数 involution**，不是 `V175` 的逐素数形式 ✓。

---

## §2 锥定理（单项式）：保持正锥的对合 ＝ 素置换（✓ 用户证明）

设 $A\in GL(C)$ 为整数单项式变换，$A^2=I$，且 $A(C)=C$。

- $A(C)\subseteq C$ ⟹ $A$ 的所有矩阵元**非负**；
- $A^{-1}=A$ 亦把 $C$ 映回 $C$ ⟹ $A^{-1}$ 的矩阵元**也非负**；
- $AA^{-1}=I$ 要求每个**非对角元严格抵消**，而**两个非负整数矩阵不可能通过正数相加产生零** ⟹ 每行每列恰有一个 $1$，其余为 $0$。

$$\boxed{A=P\ (\text{素置换})}\qquad\Longrightarrow\qquad \boxed{\text{保持 Euler 正锥的单项式对合}＝\text{素数置换}}$$

**而素数置换没有反演** ⟹ 无法实现 $X_p=p^{-s}\mapsto p^{-(k-s)}=p^{-k}X_p^{-1}$。

**二分（✓ 用户）**：
- **S-ii(a)** 保持正锥 ⟹ 只能是 $\alpha\mapsto P\alpha$（纯置换）⟹ **死**。
- **S-ii(b)** 真正实现反演 ⟹ $A(C)\not\subseteq C$ ⟹ 正指数支撑与反演后的负指数支撑发生**锥冲突**；若交集只有有限／平凡支撑，则回到 `V175` 的 $F=1$。

---

## §3 ⭐ 加强定理（本档新增）：裸反射只有常解（**无需** Euler 积）

**定理.** 设 $F(s)=\sum_{n\ge1}c_nn^{-s}$ 为任一 Dirichlet 级数（**不假设** Euler 积、**不假设**逐素数可分）。若

$$F(s)=\varepsilon\,F(k-s)$$

作为形式恒等式成立，则 $c_n=0$ 对所有 $n>1$，即 $F\equiv c_1$（**常函数**，零谱为空）。

**证明（支撑／锥论证，三行）.** 记 $X_p:=p^{-s}$，则 $n^{-s}=\mathbf X^{\alpha(n)}$，其中 $\alpha(n)\in\mathbb N^{(\mathcal P)}$ 是 $n$ 的素因子指数向量。于是

- $F$ 的支撑 $\subseteq C=\mathbb N^{(\mathcal P)}$（**非负锥**）；
- $n^{s-k}=n^{-k}\cdot n^{s}=n^{-k}\cdot\mathbf X^{-\alpha(n)}$ ⟹ $F(k-s)$ 的支撑 $\subseteq -C$（**非正锥**）。

两支撑的**交**为

$$C\cap(-C)=\{0\}$$

故逐系数比较得：$c_\alpha=0$ 对一切 $\alpha\neq0$；而 $\alpha=0$ 对应 $n=1$，且 $n=1$ 项自动给 $\varepsilon$ 归一化（$c_1=\varepsilon c_1$ ⟹ $\varepsilon=1$ 若 $c_1\neq0$）。∎

$$\boxed{\text{裸反射}\ F(s)=\varepsilon F(k-s)\ \text{在所有 Dirichlet 级数中只有常解}} ✓✓$$

⭐ **与 `V175` 的关系**：`V175` 的定理要求 **Euler 积 ＋ 逐素数可分**；本定理**两者都不要** ⟹ **严格更强**，且把"障碍在局部因子层"升级为"**障碍在支撑／锥层**"。

---

## §4 ⭐ 平衡因子定理（本档新增）：算术的 $\Phi$ ⟹ 走私

§3 说明：**裸反射是空方程**（只有常解）。故任何非平凡的反射恒等式**必须**写成

$$F(s)=\varepsilon\,\Phi(s)\,F(k-s),\qquad \Phi\neq1 \tag{176.1}$$

### (i) 对合条件

$\iota^2=\mathrm{id}$ ⟹

$$\Phi(s)\,\Phi(k-s)=1 \tag{176.2}$$

即 $\Phi$ 关于镜像 $s\mapsto k-s$ 是**反自对偶**的。

### (ii) 锥条件是关键

$\Phi(s)F(k-s)$ 的支撑必须**回到正锥**（否则与 $F$ 的支撑无法相交）。而 $F(k-s)$ 支撑在**负锥**，故

$$\boxed{\Phi\ \text{必须把负锥"抬回"正锥}\ \Longrightarrow\ \Phi\ \text{的支撑必须}\textbf{混合正负指数}}$$

### (iii) 算术 $\Phi$ 的情形（本档核心）

设 $\Phi$ **算术**（即 $\Phi$ 是 $\mathbf X$ 的形式 Laurent 级数，系数来自算术数据）。满足 (176.2) 且混合锥的算术 $\Phi$ 的**最一般形态**是**两个 Dirichlet 型对象的比**：

$$\Phi=\Psi(s)/\Psi(k-s)\qquad\text{（记 }\Psi\ \text{为某算术形式对象）}$$

（理由：$L:=\log\Phi$ 需满足 $L(s)-L(k-s)=\log\Phi(s)$，其形式解为 $\log\Psi(s)=\tfrac12\log\Phi(s)+$ 对称部分 ⟹ $\Phi=\Psi/\text{mirror}(\Psi)$，标 **[结构性] 待严格化**。）

代入 (176.1)：

$$F(s)=\varepsilon\,\frac{\Psi(s)}{\Psi(k-s)}F(k-s)\ \Longleftrightarrow\ \bigl(F\Psi\bigr)(s)=\varepsilon\,\bigl(F\Psi\bigr)(k-s)$$

由 §3（加强定理）：

$$F\Psi\equiv\text{const}\qquad\Longrightarrow\qquad F=\frac{c}{\Psi}$$

$$\boxed{\text{算术的}\ \Phi\ \Longrightarrow\ \text{函数方程退化为}\ F=c/\Psi\ ——\ \text{这不是对 }F\ \text{的}\textbf{约束},\ \text{而是对 }F\ \text{的}\textbf{定义}}$$

⟹ **算术平衡因子给出的"函数方程"是空转的**：它不含任何关于 $F$ 的新约束，只把 $F$ 重新表达为 $c/\Psi$ ⟹ 属 **F-leak／走私**（$\Psi$ 携带算术数据；若 $\Psi$ 用到了目标对象的局部数据，则直接是 `V172` §1 的反例型走私）。

### (iv) 反向结论

$$\boxed{\text{要使 }(176.1)\ \text{成为}\textbf{真正的约束},\ \Phi\ \text{必须}\textbf{非算术}}$$

而经典体系中唯一的非算术平衡因子就是 **archimedean 完成因子**（$\Gamma$、$Q^s$ 及其组合）。这**解释了为什么所有已知函数方程都带 $\Gamma$-因子** —— 不是因为"必须写 $\Gamma$"，而是因为**只有非算术 $\Phi$ 才能使方程非空转**。

⭐ **这比 `V175` 的推论 1 更精确**：`V175` 说"非平凡反射需要 archimedean 平衡项"；本档进一步说明**为什么**：**算术 $\Phi$ 使方程退化为定义**。

---

## §5 S-ii 判定与残余

**判定 ✓✓**：
- §2 锥定理 ⟹ **单项式**混合对合若保持正锥 ⟹ 只能是素置换 ⟹ **无作用**（死）；
- §3 加强定理 ⟹ 即使**放弃** Euler 积与逐素数可分，**裸反射仍只有常解**（死）；
- §4 平衡因子定理 ⟹ 想救活就必须引入 $\Phi$；而**算术 $\Phi$ ⟹ 走私**；**非算术 $\Phi$ ⟹ 就是 archimedean**（落 A）。

$$\boxed{\textbf{S-ii 在"单项式对合 ＋ 算术平衡因子"两种情形下均 DEAD}} ✓✓$$

**残余（精确，保留 OPEN，不杀 ✓）**：
1. **非线性 substitution**（$X_p\mapsto H_p(X_{q_1},\dots)$，$H_p$ 非单项式）：
   ⚠️ 若强制要求 $\iota(\mathbf X^\alpha)$ 恰为**单个单项式**（因为反射 $s\mapsto k-s$ 在指数上就是 $\alpha\mapsto-\alpha$），则**乘积的多个单项式无法等于单个单项式** ⟹ 强制 $H_p$ 为单项式 ⟹ **退回 §2** ✓✓。
   ⟹ 因此残余只剩：**不要求"指数级单项式化"、而以更弱方式实现反射的非线性对合**（标 **OPEN**，本档无法判死）。
2. **非 $\Psi/\text{mirror}(\Psi)$ 型的反自对偶算术 $\Phi$**（§4(iii) 的形式解需严格化；标 **[结构性] 待严格化**）。

---

## §6 判词与下一步

**V176 判词**：① 锥定理（单项式）成立 ✓✓；② ⭐ 加强定理：裸反射对所有 Dirichlet 级数只有常解（无 Euler 积、无逐素数可分）✓✓；③ ⭐ 平衡因子定理：算术 $\Phi$ ⟹ 方程退化为定义 ⟹ 走私 ✓✓；④ S-ii 在两种情形 DEAD，残余精确化为"非线性对合（不要求指数单项式化）"与"非 $\Psi/\text{mirror}$ 型 $\Phi$"✓。

**净收获**：
- 把 `V175` 的**局部因子层**障碍升级到**支撑／锥层**（适用范围大幅扩大）；
- 给出**为什么必须 archimedean** 的机制性理由（算术 $\Phi$ ⟹ 空转）；
- S 残余从"跨素数混合对合"**再收窄为两点**。

**下一步（V177 预登记，二选）**：
① 攻残余 1：**非线性对合且不要求指数单项式化** —— 构造候选或证明不可能（这是 S 的最后一道门）；
② 攻残余 2：**把 §4(iii) 的形式解 $\Phi=\Psi/\text{mirror}(\Psi)$ 严格化**（若严格化成功 ⟹ 算术 $\Phi$ 走私成为定理）。

```
⚠️ §1／§2 为唐先生逐字 ✓（指数锥形式化 ＋ 锥定理三行证明 ＋ 二分）
⚠️ §3 加强定理为【本档新增 ✓✓】—— 三行支撑/锥论证；结论严格强于 V175（不假设 Euler 积与逐素数可分）
⚠️ §4 平衡因子定理为【本档新增 ✓✓】—— 核心；其中 §4(iii) 的 Φ=Ψ/mirror(Ψ) 形式解标 [结构性] 待严格化
⚠️ §5 残余两点均标 OPEN／待严格化，按纪律不杀
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 锥定理（单项式）✓；② ⭐ 加强定理（裸反射只有常解，无需 Euler 积）✓✓；
   ③ ⭐ 平衡因子定理（算术 Φ ⟹ 定义而非约束）✓✓；④ S-ii 两情形 DEAD ＋ 残余收窄为两点 ✓
```

---

## §7 ⚠️ ERRATUM（T10 勘误 · 唐先生 2026-09-15 11:56 ✓✓）

**§3 "加强定理"的表述过强，须降级为【形式域版本】。**

$$\text{原表述（撤回）}：\text{任一 Dirichlet 级数}\ F=\sum c_nn^{-s}\ \text{若}\ F(s)=\varepsilon F(k-s)\ \text{则}\ F=\text{constant}\qquad ✗$$
$$\text{问题}：F(s)=\sum c_nn^{-s}\ \text{只在}\textbf{右半平面}\text{绝对收敛};\ F(k-s)\ \text{对应}\textbf{左半平面};\ \text{逐系数比较}\ n^{-s}\leftrightarrow n^{s-k}\ \text{隐含"两边可在同一层面比较"} ✗✓$$
$$\qquad\text{而 ζ 的函数方程之所以能联系两个方向，}\textbf{恰恰因为存在跨越两个收敛域的完成结构} ⟹ \text{原表述把该结构}\textbf{偷渡成了前提} ✗$$
$$\boxed{\text{修正后的严格版本} ✓✓：F(s)=\sum c_nn^{-s};\ F(s)=\varepsilon F(k-s);\ \textbf{且该恒等式可在共同的 Dirichlet／Laurent 形式域中逐系数解释}\ \Longrightarrow\ F=\text{constant}}$$
$$\qquad\Longrightarrow\ \text{定理的适用域 ＝}\boxed{\text{"形式域（共同 Laurent 形式域）中可逐系数解释的恒等式"}},\ \textbf{不是}\text{"任意 Dirichlet 级数的解析函数方程"} ✓✓$$
$$\qquad ⚠️\ \text{该降级}\textbf{不影响} §4\ \text{的逻辑链（那条链本来就在 Laurent 形式域中运作）} ✓;\ \text{但}\textbf{必须}\text{先写明，否则 coboundary 消去步骤会建立在未证的跨域比较上} ✓✓$$
$$\qquad\Longrightarrow\ \text{后续见 }V177\ \text{（}H^1(C_2,K_{\rm arith}^\times)=1\ \text{＋ 结论 A：算术 }\Phi\ \text{必为 coboundary）} ✓✓$$
