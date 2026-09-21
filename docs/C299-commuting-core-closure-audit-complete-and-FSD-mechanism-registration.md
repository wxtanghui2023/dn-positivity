已查地图（**先查后写**）：`C-298`（q.Prime 闭合 ＋ Commuting 链 ✓）、`C-297`（Coset descent ✓）、`C-296`（逐层 ✓）、`C-295`（枚举 ✓）、`C-294`（架构 ＋ GRH 承重 ✓）。一手材料：`Commuting.lean`／`Completion.lean`／`Residue.lean`／`Extension.lean` raw 逐字（✓）。回查见 §5 ✓

D0: 本档对象 = **C-299：Commuting 核心闭环审计完成 ＋ FSD 机制登记（标签，非筛选框架）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① 核心闭环审计完成}✓✓：\text{七段链条逐段有原文依据 ✓（见 §1}✓）$$
$$\textbf{② 残余收窄}⚠️：\texttt{*\_nat}\ \text{深层引理（}\texttt{doubleDefect\_eq\_zero\_nat}／\texttt{defects\_equal\_nat}／\texttt{doubleReflection}／\texttt{upperBand}✓）＋ \texttt{oddCompletion}／\texttt{centralRepresentative}\ \text{构造}✓；\textbf{独立复现}✗；\textbf{provenance}✗$$
$$\textbf{③ 登记 FSD 机制}✓（\textbf{标签}✓，\textbf{非}筛选框架 ✗；\text{不新增判据} ✓）$$
$$\textbf{④ 下一刀＝我们的对应问句}✓（\textbf{不照搬} ✗，见 §4 ✓）$$

---

## §1 核心闭环（**逐段有据**✓✓）

**（a）`IntervalSigns` 四字段（逐字 ✓✓，`Completion.lean`）**
```
structure IntervalSigns (p : ℕ) (f : ℕ → ℤ) : Prop where
  sign  : ∀ n, 0 < n → n < 2*p → f n = 1 ∨ f n = -1
  two   : ∀ n, 0 < n → n < p   → f (2*n) = - f n
  three : ∀ n, 0 < n → 3*n < 2*p → f (3*n) = - f n
  noPP  : ∀ a b, 0 < a → 0 < b → a + b = 2*p → ¬ (f a = 1 ∧ f b = 1)
```
- **`noPP` 就是反设本身** ✓✓ —— 即"目标失败"被**显式写成一个结构字段** ✓（本路线的起点 ✓）
- `Main.lean` 的 `liouville_intervalSigns` 正是**从反设构造该结构** ✓（`refine ⟨?_, ?_, ?_, ?_⟩` ✓，末项由 `h` 直接给出 ✓）

**（b）非负性** ✓✓：`doubleDefect_nonneg (hp2) (0<n) (2n<p) : 0 ≤ doubleDefect p f n` ✓
- 证明分两路 ✓：若 `4n < p` 用 `doubleDefect_small` ✓（`A = 0` ✓）；否则用 `doubleDefect_wrap` ＋ **`H.doubleReflection`** ✓（反射引理 ⚠️ 未逐字读到）
- ⟹ **`A(n) >= 0`** ✓✓（唐先生链条的第二段 ✓）

**（c）交换方阵恒等式** ✓✓：`defect_commuting_square` ✓ —— `A(-3x)+B(x) = B(-2x)+A(x)` ✓
- 证明**只用到乘子交换性 ＋ `ring`** ✓✓；公理仅 `[propext, Quot.sound]` ✓（最干净 ✓）

**（d）`A = B`** ✓✓：`defects_equal [NeZero p] (hp2) (hp3) (x) : doubleDefect p f x = tripleDefect p f x` ✓
- 经 `centralRepresentative`（`x = n` 或 `x = -n`，`2n < p` ✓）归约到自然数情形 ✓，调用 `H.defects_equal_nat` ⚠️

**（e）`A = 0`** ✓✓：`doubleDefect_eq_zero [Fact p.Prime] (3<p) (hp2) (hp3) (x) : A(x) = 0` ✓
- 同样经 `centralRepresentative` 归约，调用 `H.doubleDefect_eq_zero_nat` ⚠️

**（f）⟹ `IsGood 2/3`** ✓✓：
- `completion_two_eq_three`：`G(2x) = G(3x)` ✓（由 `A = B` ✓）
- `commuting_completion_two`／`_three`：`G(2x) = -G(x)`、`G(3x) = -G(x)` ✓✓（由 `A = B` **且** `A = 0` ✓）
⟹ **`G(2·) = -G(·)`、`G(3·) = -G(·)` 成立** ✓✓（唐先生链条末段 ✓）

**（g）支撑定位（两条，均可手验 ✓）**
- `doubleDefect_small (0<n) (4n<p) : A = 0` ✓；`doubleDefect_upper (p<3n) (2n<p) : A = 0` ✓
- ⭐ `doubleDefect_wrap (p<4n) (2n<p) : A(n) = f(p - 2n) - f(n)` ✓✓（**自反/回绕恒等式** ✓）
- ⟹ `doubleDefect_support (0<A(n)) ⟹ p < 4n ∧ 3n < p` ✓✓ 即 `supp(A_+) ⊂ (p/4, p/3)` ✓
- `tripleDefect_small (6n<p) : B = 0` ✓

**（h）终局：二次互反** ✓✓（`Residue.lean`）
- `exists_prime_square_below_half` docstring 逐字 ✓：Every prime `p > 3` congruent to three modulo four has a prime quadratic residue strictly below its half interval. **Any prime divisor of `(p+1)/4` works, including the prime two.** ✓
- 实现用 **Mathlib 的二次互反** ✓（`exists_sq_eq_prime_iff_of_mod_four_eq_one/three` ✓；`ℓ = 2` 分支用 `exists_sq_eq_two_iff` ＋ `p % 8 = 7` ✓）；文件显式 `import Mathlib.NumberTheory.LegendreSymbol.QuadraticReciprocity` ✓✓
⟹ **与 PROOF.md §8 逐字对应** ✓（`Character.lean` 的 `no_square_character_agreement`／`no_multiplicative_agreement` ✓）

---

## §2 **FSD 机制登记**（✓，**标签**✓，非框架 ✗）

$$\boxed{\textbf{Failure} \to \textbf{Symmetry} \to \textbf{Descent}\quad(\text{FSD})}$$

**七步模板**（✓，本档只作**已出现机制的命名** ✓）：
```
独立算术问题
  → 假设目标失败
  → failure 产生局部约束
  → 寻找两个可交换的自然作用
  → defect compatibility
  → minimal bad object
  → strict descent
  → global algebraic rigidity
```

**与旧范式的四点对照**（✓，唐先生提炼 ✓）：
| 旧范式（我们过去的默认） | FSD（本路线） |
|---|---|
| 对象 → invariant → 刚性 → 接 β | 假设失败 → **失败本身**产生局部约束 → 对称性 |
| 找 **correlation**（是否相关） | 找 **compatibility**（代数强制关系 ✓，更强 ✓） |
| local ⟹ global（常撞墙 ✗） | 假设 global failure ⟹ **minimal obstruction** ⟹ strict descent ⟹ ⊥ ✓ |
| global structure ＝ 谱／连续参数 | global structure ＝ **离散代数闭包对象**（`H <= F_p^×` ✓） |
| invariant 是研究对象 | **failure set** 是研究对象 ✓ |
| 盯算术函数 λ／μ／d／E(A) | 盯**作用群** `<-1,2,3> ↷ F_p^×` ✓ |

**六个盲点**（压缩登记 ✓）：① 反例当**结构发生器** ✓；② correlation → compatibility ✓；③ 最小坏点下降 ✓；④ 全局对象可以**离散代数**而非谱 ✓；⑤ **failure set** 可作对象 ✓；⑥ 强对象可以是**作用群** ✓

**纪律**（✓✓）：**不得**把 FSD 做成新筛选框架 ✗；**不得**照搬（把 λ 换成某个 RH 对象再套一遍 ✓＝立即 repackaging ✗）；本登记**只**记录"已出现的机制命名" ✓

---

## §3 残余审计项（⚠️，清单）

- `*_nat` 深层引理 ⚠️：`doubleDefect_eq_zero_nat`／`defects_equal_nat`／`doubleReflection`／`upperBand` ✓
- `oddCompletion` 构造 与 `centralRepresentative` 语句 ⚠️（均已被引用 ✓ 未读正文 ✗）
- **独立复现**（自行 `lake build` ／ Comparator ✓）✗ 未做
- **provenance** ✗：仓库自证 Astra 关联 ✗；媒体归因属 provenance claim ✓ → 证据链仍只到 **公开 GitHub artifact** ✓

## §4 下一刀问句（**我们的 RH 侧**✓，唐先生提出 ✓）

$$\boxed{\text{在 RH 的独立算术对象里，哪里存在}\ \textbf{两种天然可交换的算术作用}\text{，使得}\ \textbf{目标失败}\ \text{能产生两个 defect，而 } \textbf{defect compatibility}\ \text{又诱发}\ \textbf{严格下降}✓？}$$
- 前置纪律 ✓：先问**问句是否成立**（存在性审计 ✓），**不**先设计对象 ✗；命中既有封口则引既有 ✓（不重开 ✗）
- 与本项目既有工作的关系 ✓：C-286-B 的 divisor／local→global 死墙 ✓ 与 FSD 的 descent **不是同一机制** ✓（可对照但不并入 ✗）

## §5 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：该证明已独立复现 ✗；已同行评审 ✗；是 Astra 官方成果 ✗；FSD 是"新判据"✗
- **本档新增词**：`FSD 机制`／`failure set 作对象`／`compatibility 范式`（0 命中 ✓）
