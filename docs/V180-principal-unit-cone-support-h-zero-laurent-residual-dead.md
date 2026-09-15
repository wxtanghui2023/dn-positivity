# V180 · ⭐⭐⭐⭐⭐ **principal-unit 反不变量审计 —— ①三项分解执行；②⚠️ §1 小修正（单式部分只给**标量**，不给指数约束）；③⭐ **本档核心：cocycle ⟹ $h=0$**（**锥-支撑论证**，严格避开无穷和陷阱）✓✓✓；④⟹ **Laurent 残余整块 DEAD**（余下只剩单式 ⟹ 有限支撑筛杀死）

> 委托 ✓ 唐先生 2026-09-15 12:04：**"开。V180-① 应该直接开，而且这次可以先把'无限方程组'化成一个明确的代数分解问题，不需要一上来做截断"**；给出**三项分解**（指数／常数／principal-unit）、**取对数化简**（$g+\iota(g)=0$）、以及**最锋利判据**：$\mathfrak m\cap\iota(\mathfrak m)$ 是否存在非零反不变量；终判据树（交集为 0 ⟹ DEAD；非 0 ⟹ 产生 S 候选）
> 查图 ✓ `V179`（有限支撑筛；谱容量冲突）｜`V178`（环级 $H^1$；奇偶×符号）｜`V177`（$H^1(K^\times)=1$）｜`V176`（锥定理）｜`V175`｜`V174`
> 执行 ✓ 小灵（**§3 锥-支撑论证 为本档核心；§1 一处修正**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V180**

---

## §0 判定

**① 三项分解成立，但 §1 需要小修正 ✓**
单式部分给的是**标量**（不是指数约束）：$X^\alpha\iota(X^\alpha)=\prod_pp^{-k\alpha_p}\in\mathbb Q^\times$，**指数精确相消**。见 §1。

**② ⭐ 本档核心：principal-unit 部分被锥-支撑论证一次杀死 ✓✓✓**
由 cocycle 条件得 $\iota(h)=\lambda(1+h)^{-1}-1$；左端支撑 $\subseteq-C$、右端（除常数项外）支撑 $\subseteq C$ ⟹ 常数项比较给 $\lambda=1$ ⟹ $\iota(h)=-\dfrac{h}{1+h}$ ⟹ **$h=0$** ✓✓✓
⭐ 该论证**只用支撑（锥归属）**，**不需要**比较任何无穷和 ⟹ 严格 ✓✓

**③ ⟹ Laurent 残余整块 DEAD ✓✓✓**
$h=0$ ⟹ $\Phi=cX^\alpha$（**单式**）⟹ 有限支撑筛（`V179`）⟹ **FSC-DEAD** ⟹ 本模型下残余**全部封死**。

**④ 诚实边界（必标）✓**
结论成立**在模型** $R^\times=\mathbb Q^\times X^{\mathbb Z^{(\mathcal P)}}(1+\mathfrak m)$ **之内**；该分解对"逐变量 Laurent 环"成立，对**无限多变量的完整 Laurent 级数环**需另行验证 ⟹ 见 §5（标 **OPEN**，不越界宣布"全数学 DEAD"）。

---

## §1 三项分解（✓ 唐先生）+ 一处修正

$$R=\mathbb Q[[X_p]][X_p^{-1}],\qquad \Phi=X^\alpha u\ (\alpha\in\mathbb Z^{(\mathcal P)},\ u(0)\neq0),\qquad u=c(1+h)\ (c\in\mathbb Q^\times,\ h\in\mathfrak m)$$
$$\Longrightarrow\ \boxed{R^\times=\mathbb Q^\times\cdot X^{\mathbb Z^{(\mathcal P)}}\cdot(1+\mathfrak m)}:\quad \text{指数部分}\ +\ \text{常数部分}\ +\ \text{principal-unit 部分}$$

**⚠️ 修正在 §1 的单式计算**：
$$X^\alpha\iota(X^\alpha)=X^\alpha\Bigl(\prod_pp^{-k\alpha_p}\Bigr)X^{-\alpha}=\boxed{\prod_pp^{-k\alpha_p}\in\mathbb Q^\times}$$
$$\qquad\text{即：单式部分}\ \textbf{精确相消}\ \text{（}X^\alpha X^{-\alpha}=1\text{）},\ \textbf{只留下一个标量};\ \textbf{不产生}\ \text{"}2\alpha=0\text{"}\ \text{型的指数约束} ✓$$
$$\qquad ⚠️\ \text{故}\ \alpha\ \text{不被单独钉死};\ \alpha\ \text{最终只通过}\ \textbf{标量条件}\ c^2\prod_pp^{-k\alpha_p}=1\ \text{与}\ c\ \text{耦合}（\text{见 §3}）✓$$

---

## §2 常数部分（✓ 唐先生，修正后）

$$\Phi=cX^\alpha(1+h)\ \Longrightarrow\ \iota(\Phi)=c\Bigl(\prod_pp^{-k\alpha_p}\Bigr)X^{-\alpha}(1+\iota(h))$$
$$\Phi\,\iota(\Phi)=c^2\Bigl(\prod_pp^{-k\alpha_p}\Bigr)\cdot X^{\alpha}X^{-\alpha}\cdot(1+h)(1+\iota(h))=c^2\Bigl(\prod_pp^{-k\alpha_p}\Bigr)(1+h)(1+\iota(h))$$
$$\text{cocycle}:\ \Phi\iota(\Phi)=1\ \Longleftrightarrow\ \boxed{(1+h)\,(1+\iota(h))=\lambda}:=1\Big/\Bigl(c^2\prod_pp^{-k\alpha_p}\Bigr)\in\mathbb Q^\times \tag{V180.1}$$
$$\qquad\Longrightarrow\ \text{常数部分与 principal-unit 部分由}\ \lambda\ \text{耦合};\ \lambda\ \text{将由 §3 的常数项比较}\textbf{钉为 1} ✓✓$$

---

## §3 ⭐ 本档核心：principal-unit 部分 ⟹ $h=0$（锥-支撑论证）

### (3a) 把 (V180.1) 改写为 $\iota(h)$ 的表达式

$$1+\iota(h)=\frac{\lambda}{1+h}\ \Longrightarrow\ \iota(h)=\lambda(1+h)^{-1}-1=(\lambda-1)+\lambda\bigl[(1+h)^{-1}-1\bigr]$$
$$\qquad\text{而}\ (1+h)^{-1}=1-h+h^2-h^3+\cdots\ \text{（}\mathfrak m\text{-adic 合法）}\ \Longrightarrow\ (1+h)^{-1}-1=-\frac{h}{1+h}$$
$$\qquad\Longrightarrow\ \boxed{\iota(h)=(\lambda-1)-\lambda\cdot\frac{h}{1+h}} \tag{V180.2}$$

### (3b) 支撑（锥归属）比较 —— 关键一步

$$C:=\mathbb N^{(\mathcal P)}\ \text{（正锥）};\qquad -C\ \text{（负锥）};\qquad C\cap(-C)=\{0\}$$
- **左端 $\iota(h)$**：$h\in\mathfrak m$（正指数、无常数项）⟹ $\iota(h)=\sum_{\alpha\in C\setminus\{0\}}h_\alpha\bigl(\prod_pp^{-k\alpha_p}\bigr)X^{-\alpha}$ ⟹
  $$\operatorname{supp}\iota(h)\subseteq -C\setminus\{0\},\qquad\textbf{常数项}=0\ ✓$$
- **右端** $(\lambda-1)-\lambda\dfrac{h}{1+h}$：常数项 $=(\lambda-1)$；其余各项是 $h/(1+h)=h-h^2+h^3-\cdots$ 的项，而**正锥对乘法封闭** $\bigl(C+C\subseteq C\bigr)$ ⟹
  $$\operatorname{supp}\Bigl(\frac{h}{1+h}\Bigr)\subseteq C\setminus\{0\}\ ✓$$

### (3c) 结论

$$\textbf{(i) 常数项比较}：\text{左 }0=(\lambda-1)\ \Longrightarrow\ \boxed{\lambda=1}\ ✓✓$$
$$\textbf{(ii) 取}\ \lambda=1\ \text{后}：\text{(V180.2) 化为}\ \boxed{\iota(h)=-\frac{h}{1+h}}\ ✓;\ \text{左端}\ \subseteq-C,\ \text{右端}\ \subseteq C,\ \text{两侧常数项均为 }0$$
$$\qquad\Longrightarrow\ \operatorname{supp}\subseteq C\cap(-C)=\{0\}\ \text{且常数项 }0\ \Longrightarrow\ \frac{h}{1+h}=0\ \Longrightarrow\ \boxed{h=0}\ ✓✓✓$$
$$\qquad ⚠️\ \textbf{无无穷和陷阱}：\text{本论证}\textbf{只比较"锥归属 ＋ 常数项"}，\textbf{不}\text{比较任何无穷系数和} ⟹ \text{严格} ✓✓✓$$

### (3d) 取对数视角（✓ 唐先生；与本档论证的关系）

$$\text{设}\ g=\log(1+h)\ ⟹ \Phi\iota(\Phi)=1\iff\exp(g+\iota g)=1\iff \boxed{g+\iota(g)=0}\ ✓✓\ \text{（multiplicative cocycle}\iff\text{additive 反不变量）}$$
$$\qquad ⚠️\ \text{但}\ \iota\ \textbf{不保持}\ \mathfrak m\ \text{（}\iota(X_p)=p^{-k}X_p^{-1}\ \text{是单位，}\notin\mathfrak m\text{）};\ \text{故}g\ \text{是否落在}\ \mathfrak m\cap\iota(\mathfrak m)\ \text{本身即难点} ✓$$
$$\qquad ⭐\ \text{本档用 (3c) 的锥论证}\textbf{绕开}\text{该难点}：\text{不需要 }g\ \text{的反不变量存在性，只需 }h\ \text{的锥归属} ✓✓$$

---

## §4 ⟹ Laurent 残余整块 DEAD

$$h=0\ \Longrightarrow\ \Phi=cX^\alpha,\qquad \text{标量条件（§2 的 }\lambda=1\text{）给}\ c^2\prod_pp^{-k\alpha_p}=1$$
$$\Longrightarrow\ \Phi\ \text{是}\ \textbf{单式}\ ⟹ \text{有限支撑筛（`V179`）：}\operatorname{supp}(F)\subseteq C\cap(\alpha-C)=\{0\le\delta\le\alpha\}\ \textbf{有限}\ \Longrightarrow\ \textbf{FSC-DEAD}\ ✓✓✓$$
$$\boxed{\text{在模型 }R^\times=\mathbb Q^\times X^{\mathbb Z^{(\mathcal P)}}(1+\mathfrak m)\ \text{内：cocycle 只有 }\Phi=cX^\alpha\ (\text{单式})\ \Longrightarrow\ \textbf{残余 DEAD}}$$
$$\qquad ⭐\ \text{顺带重现}\ \text{`V178`}\ \text{的两类障碍}：\alpha\ \text{的奇偶性}（\text{单式 coboundary 需 }\alpha\in2\mathbb Z^{(\mathcal P)}\text{）与}\ c\ \text{的符号}（\Phi=-1\ \text{即 }c=-1,\alpha=0\text{）} ✓✓$$
$$\qquad ⭐\ \text{且}\ \text{`V178`}\ \text{的}\ \Phi=-1\ \text{现在被}\ \textbf{两条独立理由}\ \text{判死}：\text{(i) 单式 ⟹ 有限支撑};\ \text{(ii) }\alpha=0\ \Longrightarrow\ C\cap(-C)=\{0\}\ \Longrightarrow\ F\equiv\text{const} ✓✓$$

---

## §5 ⚠️ 诚实边界（模型边界；按纪律标 OPEN，不越界宣布）

$$\textbf{(i) 分解的适用范围} ✓：R^\times=\mathbb Q^\times X^{\mathbb Z^{(\mathcal P)}}(1+\mathfrak m)\ \text{对}\ \textbf{逐变量 Laurent 环}\ \text{成立（经典）};\ \text{对}\ \textbf{无限多变量的完整 Laurent 级数环}\（\text{允许一般指数向量、乘积为无穷和}\）\ \textbf{需另行验证} ⚠️$$
$$\textbf{(ii) 本档结论的精确形式} ✓：\text{不是"全数学 DEAD"}，而是\ \boxed{\text{"在 Laurent（形式）环模型内，算术反自对偶因子只能是单式"}}\ ✓✓$$
$$\textbf{(iii) 仍未覆盖} ⚠️：\text{(a) 非}\ \mathbb Q\text{-系数（如代数系数）；(b) 非逐变量可分形式的无限乘积型单位；(c) 一般的"无穷乘积 }\prod_p(\dots)\ \text{型"算术因子}}$$
$$\Longrightarrow\ \text{三项均标}\ \textbf{OPEN}，\ \textbf{不杀} ✓$$

---

## §6 判词与下一步

**V180 判词**：① 三项分解执行 ✓；② §1 修正（单式部分只给标量，指数相消）✓；③ ⭐ **principal-unit 部分被锥-支撑论证杀死（$h=0$）**，且**无无穷和陷阱** ✓✓✓；④ λ 由常数项比较钉为 1 ✓✓；⑤ ⟹ 模型内残余 DEAD（只剩单式 ⟹ 有限支撑 ⟹ FSC-DEAD）✓✓✓；⑥ 诚实边界（模型适用域；三项未覆盖）✓。

**净收获**：
- 把"无限方程组"**化成一个锥-支撑比较**（按唐先生要求先做代数分解）✓✓；
- **避开**了 $\mathfrak m\cap\iota(\mathfrak m)$ 的技术难点（不需要构造反不变量）✓✓；
- 一次性封死 Laurent 环残余，并**顺带给出** `V178` 符号障碍的**第二条独立理由** ✓✓。

**下一步（V181 预登记，三选）**：
① 攻 §5(iii)-(a)：**代数系数**（$K^\times$ 换成数域，验证 Hilbert 90 与锥论证是否仍成立）；
② 攻 §5(iii)-(b)/(c)：**非逐变量可分的无限乘积型单位**（本档证明不覆盖）；
③ **撤销 S 线，转回主线**：若三项残余经审均为死，则"$\Gamma$-free 纯算术平衡因子"整条线关闭，应转回 A1／A3（`V162` 已指出的同一堵墙）。

```
⚠️ §1 三项分解为唐先生逐字 ✓✓；§1 的单式计算修正为【本档新增 ✓】（单式部分只给标量 ∏p^{−kα_p}，指数精确相消，不产生 2α=0）
⚠️ §3 锥-支撑论证为【本档核心新增 ✓✓✓】—— 只用锥归属 ＋ 常数项比较，不比较无穷和
⚠️ §3(d) 取对数视角为唐先生逐字 ✓；本档指出 ι 不保持 𝔪 而绕开该难点
⚠️ §5 模型边界标 OPEN，不越界宣布"全数学 DEAD"
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 三项分解执行 ＋ §1 修正 ✓；② h=0（锥-支撑，无无穷和陷阱）✓✓✓；③ λ=1 ✓✓；
   ④ 模型内残余 DEAD（单式 ⟹ 有限支撑 ⟹ FSC-DEAD）✓✓✓；⑤ V178 符号障碍的第二条独立理由 ✓✓；⑥ 三项 OPEN 残余 ✓
```
