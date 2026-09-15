# V181 · ⭐⭐⭐⭐⭐ **S 线结构性关闭审计（`V171`→`V180`）—— ①关闭链：cocycle $\to$ monomial $\to$ finite support $\to$ **FSC-DEAD**；②**负结构定理**（精确陈述）；③**类界 ＋ 重开条件**；④转回主线 **A1／A3**（`V162` 承重墙）

> 委托 ✓ 唐先生 2026-09-15 12:11：**"我拍板 ③：关闭 S 线，转回主线 A1/A3。而且这不是'暂时搁置'，而应当把它登记为一个结构性关闭"**；并给出关闭理由（**V180 解释了 S 线为什么会死**，与单纯又得一个 NO-GO 是不同层级的结果）、①／② 不值得攻的理由、以及转回 A1/A3 的落点
> 查图 ✓ `V180`（锥-支撑 ⟹ $h=0$）｜`V179`（有限支撑筛 FSC；谱容量冲突）｜`V178`（环级 $H^1$；奇偶×符号）｜`V177`（$H^1(K^\times)=1$；coboundary）｜`V176`（锥定理；平衡因子定理）｜`V175`（局部因子刚性）｜`V173`（local-swap）｜`V172`（F／A／S）｜**`V162`（承重墙：$T\log T$ ＋ Weil 正性；"局部算术 $\not\Longrightarrow$ 全球谱定位"）**
> 执行 ✓ 小灵（**§1 关闭链、§2 层级区分、§3 负结构定理、§4 类界、§7 重开条件、§8 主线交接**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V181**

---

## §0 判定

**① S 线 ＝ 结构性关闭（NO-GO，含类界）✓✓**
$$\boxed{\text{Laurent 形式环内的算术反自对偶平衡因子（cocycle）}\ \Longrightarrow\ \text{单式}\ \Longrightarrow\ \text{有限支撑}\ \Longrightarrow\ \textbf{FSC-DEAD}}$$
**不是"没找到好因子"，而是"这一类因子没有足够的自由度"** ✓✓ —— 这是**结构性关闭**，不是搁置。

**② 关闭是"解释性"的，与 NO-GO 不同层级 ✓✓**
`V180` 给出的不是又一条禁令，而是**机制解释**：**纯算术乘法平衡无法提供所需的无限谱刚性**（方向性不匹配，见 §3）✓✓。

**③ 两个子分支登记为 Uninstantiated（不作活跃候选）✓**
(a) 数域系数｜(b) 非逐变量可分的无限乘积型单位 —— **不构成当前主线候选**；**除非先证明它们产生新的、非等价的无限谱自由度，否则不再投入** ✓✓。

**④ 主线回归：A1／A3（`V162` 承重墙）✓✓**
$$T\log T\quad+\quad\text{Weil 正性};\qquad \text{核心缺口：局部算术}\ \not\Longrightarrow\ \text{全球谱定位} ✓$$

---

## §1 关闭链（✓ 完整登记）

$$\text{算术平衡因子}\ \Phi\ \text{（Laurent 形式环内，cocycle：}\Phi\iota(\Phi)=1\text{）}$$
$$\qquad\downarrow\ \text{三项分解（`V180`）}：R^\times=\mathbb Q^\times X^{\mathbb Z^{(\mathcal P)}}(1+\mathfrak m)$$
$$\text{指数部分}\ \Rightarrow\ \textbf{精确相消}（\text{只留标量}\ \textstyle\prod_pp^{-k\alpha_p}）;\qquad \text{常数部分}\ \Rightarrow\ \lambda=1$$
$$\qquad\downarrow\ \textbf{principal-unit 锥-支撑论证}：\operatorname{supp}\iota(h)\subseteq-C,\ \operatorname{supp}\frac{h}{1+h}\subseteq C,\ C\cap(-C)=\{0\}\ \Longrightarrow\ \boxed{h=0}$$
$$\qquad\downarrow\ \Phi=cX^\alpha\ \textbf{单式}$$
$$\qquad\downarrow\ \text{有限支撑筛（`V179`）}：\operatorname{supp}(F)\subseteq C\cap(\alpha-C)=\{0\le\delta\le\alpha\}\ \textbf{有限}\ \Longrightarrow\ N_F(T)=O(T)$$
$$\qquad\downarrow\ N_\zeta(T)\asymp T\log T\ \text{冲突}\ \Longrightarrow\ \boxed{\textbf{FSC-DEAD}}$$

---

## §2 为什么这次是"解释性关闭"（层级区分）✓✓

$$\text{`V180` 最重要的改进}：\text{principal-unit 锥-支撑论证}\ \textbf{避开了最危险的漏洞}\ ——\ \text{禁止对}\ \sum h_\alpha X^\alpha\ \text{与}\ \sum_\beta(\cdots)X^\beta\ \text{做无限系数求和比较}$$
$$\qquad\Longrightarrow\ \text{只用}\ \operatorname{supp}(h)\subseteq C,\ \operatorname{supp}(\iota(h))\subseteq-C,\ C\cap(-C)=\{0\}$$
$$\qquad\Longrightarrow\ \lambda=1,\ h=0\ \text{是}\textbf{真正的支撑几何结论}（\text{不是形式级数技巧}）✓✓$$
$$\text{故 }S\ \text{线完成的不是"又排除若干构造"，而是：}\boxed{\text{证明这一类因子}\textbf{没有足够的自由度}} ✓✓$$
$$\qquad\Longrightarrow\ \text{与"再得一条 NO-GO"}\ \textbf{层级不同}：\text{后者是清单增长};\ \text{前者是}\textbf{机制解释} ✓✓$$

---

## §3 负结构定理（精确陈述）✓✓

$$\boxed{\textbf{负结构定理（S 线）}：\text{Laurent（形式）环内的算术因子}\ \overset{\text{cocycle}}{\longrightarrow}\ \text{单式}\ \overset{\text{FSC}}{\longrightarrow}\ \text{有限谱}}$$
$$\text{而 RH 所需的是}\textbf{相反性质}：\boxed{\text{算术数据}\longrightarrow\text{无限谱对象}\longrightarrow\text{临界线定位}}$$
$$\qquad\Longrightarrow\ ⭐\ S\ \text{线真正暴露的不是"构造还不够复杂"，而是：}\boxed{\text{纯算术乘法平衡本身无法提供所需的无限谱刚性}} ✓✓$$
$$\qquad\Longrightarrow\ \text{并把主线推回 }V162\ \text{承重墙}：\boxed{T\log T\ +\ \text{Weil 正性}};\qquad \boxed{\text{局部算术结构}\ \not\Longrightarrow\ \text{全球谱定位}} ✓✓$$

---

## §4 关闭的类界（必须写清，参 §11.2 纪律）

$$\textbf{被关闭的类} ✓：\text{Laurent 形式环}\ R=\mathbb Q[[X_p]][X_p^{-1}]\ \text{内、逐变量分解成立的算术反自对偶平衡因子}$$
$$\textbf{未覆盖（登记为 Uninstantiated，非活跃候选）} ✓：
\text{(a) 非}\ \mathbb Q\text{-系数（数域／代数系数）};\quad \text{(b) 非逐变量可分形式的无限乘积型单位};\quad \text{(c) 一般}\ \prod_p(\cdots)\ \text{型算术因子}$$
$$\qquad ⚠️\ \text{模型边界}：\text{三项分解}\ R^\times=\mathbb Q^\times X^{\mathbb Z^{(\mathcal P)}}(1+\mathfrak m)\ \text{对}\ \textbf{逐变量 Laurent 环}\ \text{成立（经典）};\ \text{对}\ \textbf{无限多变量完整 Laurent 级数环}\ \text{需另行验证} ✓$$
$$\qquad ⚠️\ \text{结论精确形式}：\textbf{不}\text{声称"全数学 DEAD"};\ \text{只声称"上述类内 DEAD"} ✓✓$$

---

## §5 为什么不攻 ①（数域系数）✓✓

$$\text{把}\ \mathbb Q^\times\to K^\times\ \text{确实可重查 Hilbert 90};\ \text{但}\textbf{杀死 principal-unit 的不是"系数是有理数"} ✓$$
$$\qquad\boxed{\text{杀手是}\ C\cap(-C)=\{0\}} —— \text{只要系数域嵌入}\textbf{特征零有序／赋值结构}，使\ \mathfrak m=\{\text{正锥支撑、无常数项}\}\ \text{仍具相同支撑分离}，$$
$$\qquad\text{则}\ \iota(h)\in-C\ \text{与}\ -\frac{h}{1+h}\in C\ \text{仍然迫使}\ h=0 ✓✓$$
$$\qquad\Longrightarrow\ \text{把}\ \mathbb Q\ \text{换成数域}\ \textbf{并不触及真正的瓶颈};\ \text{登记为重开条件之一（见 §7），但}\textbf{当前不投入} ✓$$

---

## §6 为什么不攻 ②（无限乘积单位）✓✓

$$\text{表面最诱人（可能逃出}\ R^\times=\mathbb Q^\times X^\alpha(1+h)\text{）};\ \text{但}\textbf{一旦允许任意不可分的无限乘积型单位，就必须先重新定义模型本身} ✓$$
$$\qquad\text{待重新开放的问题}：\prod_p(1+u_pX^{\alpha_p})\ \text{属哪个完备化？支撑是否良基？乘法是否仍逐项定义？}\ \iota\ \text{是否仍是同一自同构？}\ \Phi\iota(\Phi)=1\ \text{是否仍是合法环内恒等式？}$$
$$\qquad\Longrightarrow\ ⚠️\ \text{若这些都重新开放，实际上是在}\boxed{\text{换模型逃避 }V180\ \text{的结论}}\ —— \text{而不是突破 }V180 ✓✓$$
$$\qquad\Longrightarrow\ \text{除非已有}\textbf{独立理由}\text{证明这种单位具有 RH 所需的谱自由度，否则}\textbf{不值得投入} ✓✓$$

---

## §7 重开条件（明确登记）✓✓

$$\text{S 线}\ \textbf{重开}，\text{当且仅当满足以下任一条} ✓：$$
$$\textbf{(R1)}\ \text{给出一个}\ \textbf{独立于本模型的}\ \text{算术因子，并证明它}\textbf{同时}\text{满足：算术可构造／反自对偶／}\operatorname{supp}(F)\ \textbf{无限}／\text{不与 }\Phi=c/\Psi\ \text{型走私等价};\ \textbf{且}\ N_F(T)\asymp T\log T ✓$$
$$\textbf{(R2)}\ \text{证明无限乘积型单位存在}\ \textbf{非等价于 }V180\ \text{框架}\ \text{的新谱自由度（须先给出完备化与良基性证明）} ✓$$
$$\textbf{(R3)}\ \text{发现}\ C\cap(-C)=\{0\}\ \text{在目标类中}\ \textbf{不再成立}（\text{即存在允许的"混合锥"算术因子})\ ✓✓$$
$$\qquad ⚠️\ \text{三条均未满足} ⟹ \text{按纪律}\textbf{不再投入};\ \text{资源转回 A1／A3} ✓✓$$

---

## §8 转回主线 A1／A3（✓ 交接）

$$\textbf{承重墙（`V162`）} ✓✓：\boxed{T\log T\quad+\quad\text{Weil 正性}};\qquad \textbf{核心缺口}：\boxed{\text{局部算术结构}\ \not\Longrightarrow\ \text{全球谱定位}}$$
$$\qquad\text{已知无条件输入不足}：\text{比例天花板 }0.682;\ \text{第三矩／高相关需要}\ \textbf{support}>1;\ \text{T² 律／预算越界（`V102`／`V162`）} ✓$$
$$\qquad\Longrightarrow\ \textbf{唯一登记靶点}：E102\ \text{§8 target1} ✓$$

$$\textbf{V182 建议}：\text{形式化}\ \textbf{N31}（\text{char-0 无条件 }\sqrt{\cdot}\text{-正性}\ \Longrightarrow\ \text{origin 可归约到 finiteness}）✓✓$$
$$\qquad\text{理由}：\text{它把三条}\ \textbf{族级 NO-GO}\ \text{升级为}\ \textbf{结构结论}（\text{目前只在 known-candidate 级，覆盖性论证未证}）;\ \text{杠杆最高} ✓✓$$
$$\qquad\text{备选}：E102\ \text{§8 target1 的直接攻击};\ \text{或}\ V103\ \text{遗留的三条勘误收尾} ✓$$

---

## §9 判词

**V181 判词**：① S 线**结构性关闭**（链：cocycle $\to$ 单式 $\to$ 有限支撑 $\to$ FSC-DEAD）✓✓；② 关闭是**解释性**的（机制：纯算术乘法平衡无足够无限谱刚性）✓✓；③ 类界写清（Laurent 形式环内；模型边界；不越界宣布全数学 DEAD）✓✓；④ 两个子分支登记为 **Uninstantiated**（不攻，理由：①杀手是 $C\cap(-C)=\{0\}$ 而非系数域；②需先重定义模型 ⟹ 换模型逃避）✓✓；⑤ **重开条件 R1／R2／R3** 明确 ✓✓；⑥ 资源转回 **A1／A3**（`V162` 承重墙），V182 建议形式化 **N31** ✓✓。

```
⚠️ §0 关闭请求为唐先生逐字 ✓✓（"结构性关闭"而非"暂时搁置"）
⚠️ §1 关闭链各环节出处：V180（三项分解／锥-支撑／h=0）、V179（FSC／容量冲突）、V177（H¹）、V176（锥定理）
⚠️ §3 负结构定理为【本档新增 ✓✓】—— 精确陈述 ＋ 与 RH 所需方向的对置
⚠️ §4 类界（含模型边界与"不越界"纪律）为【本档新增 ✓✓】
⚠️ §5／§6 为唐先生逐字 ✓✓；§7 重开条件 R1–R3 为【本档新增 ✓✓】
⚠️ §8 主线交接（T log T ＋ Weil 正性；局部算术 ⇏ 全球谱定位；E102 §8 target1；V182 建议 N31）为【交接 ✓】
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① S 线结构性关闭登记 ✓✓；② 负结构定理 ✓✓；③ 类界 ＋ 重开条件 ✓✓；
   ④ 两子分支 Uninstantiated ✓✓；⑤ 主线交接（A1／A3；V182＝N31）✓✓
```
