# C309R — 重读：artifact（Liouville 版 Goldbach）的**有限/无限**结构与审计现状

已查地图（**先跑后写** ✓）：`C291`（事件登记 ✓）、`C293`（Mangerel 条件定理核验 ✓）、`C294`（**证明架构 ＋ GRH 单点承重** ✓✓）、`C295`（仓库枚举／claim only ✓）、`C296`（**一手 artifact 语句级／公理级／路线级审计** ✓✓）、`C297`（Coset descent ✓）、`C298`（q.Prime 闭合 ＋ Commuting 链 ✓）、`C299`（**核心闭环审计完成 ＋ FSD 登记** ✓✓）
一手材料：GitHub `CaptainSude/Liouville-Goldbach` 的 `lean/PROOF.md`（**证明叙述全文** ✓✓）、`lean/LiouvilleGoldbach/{Main,Extension,Commuting,Coset,Completion,Descent,Reduction,Residue,Character}.lean`（**已下载至** `dn-project/external/liouville-goldbach/` ✓）、`paper/liouville-goldbach.tex|pdf`（**仓库自带论文** ✓）

D0: 本档对象 = **C-309R：对事件（Liouville 版 Goldbach artifact）的"有限/无限"结构重读审计**（档案已有对象 `C291–C299` 链的**重读关系**；非重命名、非新对象）
D1: 0
FREEZE-ACK: 本档即冻结审计（连续 D1=0 ＝ 35 ≥ 3；本档为**重读登记**，未引入新自由度）

---

## §0 结论（四条 ✓✓）

```
① 路线归属 ✓：**Liouville 版（Shusterman 命题）**，**不是**经典（二元）Goldbach ⟹ **经典 Goldbach 仍开放** ✗✓
② 强度 ✓✓：**全 N 均匀**（∀ 偶数 N > 2）；**无 GRH、无渐近阈值、无有限验证计算区间** ✓✓
③ ⭐ **有限/无限如何破局**：标准路线 = 渐近（分析／GRH）**＋** 有限验证（计算）；
   本 artifact = **反设 ⟹ 交换对称平方 ⟹ 下降（短代表元 → 整域）⟹ 二次互反矛盾** ⟹
   **阈值根本不产生**；有限残留仅 **{8,12,18}** ＋ 素数 **2,3** ✓✓（详见 §2）
④ 审计现状：语句级 ✓✓｜公理级 ✓✓（无 `sorryAx`）｜路线级 ✓✓｜
   **深层 `*_nat` 引理 ＋ 构造类（`oddCompletion`／`centralRepresentative`）内容待审** ⚠️｜
   **独立复现未做** ✗｜**provenance 未闭合**（非 Astra 官方）✗✓
```

## §1 证明四段（`PROOF.md` ↔ Lean 声明 **逐段对应** ✓✓）

```
【段 1 · 反设 ⟹ 局部不等式】 设 p>3 素；反设 **2p 无"正-正"对**（λ(a)=λ(b)=1）✗
   ⟹ 由"加倍后即得正-正对"知 **p 无"负-负"对** ✓；配合 λ(2n)=λ(3n)=−λ(n) 得
      f(p−n) ≥ −f(n)，f(p+n) ≤ f(n)（0<n<p）与 f(p−2n) ≥ f(n)（0<n<p/2）✓
   由 2p=4n+2u、3n=p+v、p=3u+2v 得闭链 −f(n) ≤ f(v) ≤ −f(u) ≤ −f(n) ⟹
      **f(n) = f(p−2n) = −f(3n−p)**（p/3<n<p/2）✓
   Lean ✓：`liouville_intervalSigns`（构造 `IntervalSigns p liouville` 四字段 sign／two／three／**noPP**）✓✓
      —— 注意 `noPP` **就是反设本身**（目标失败被显式写成结构字段 ✓）

【段 2 · 奇延拓 ＋ 交换平方】 G(0)=0，G(t)=sgn(t)f(|t|)（唯一代表 −p/2<t<p/2）✓
   缺陷 A(x)=G(−2x)−G(x)、B(x)=G(−3x)−G(x)（**皆奇**）✓
   区间形态表（4 段）：(0,p/6)→A=B=0；(p/6,p/4)→B≥0；Q=(p/4,p/3)→A≥0 且 **A=B**；(p/3,p/2)→A=B=0 ✓
   ⭐ **交换恒等式 (4)**：**A(−3x) + B(x) = B(−2x) + A(x)**（因 ×(−2) 与 ×(−3) **交换**）✓✓
   由 (4) ＋"p/6<n<p/4 时左端两项皆非负且和为 0"⟹ A=B 处处；再证 A≠0 不可能
      （取 n∈Q 使 A(n)>0 ⟹ 2n/3 的中央代表 m 亦 A(m)>0 且 m∈Q ⟹ 3m≡2n，0<3m−2n<p **矛盾**）✓
   ⟹ **A = B = 0** ⟹ ⟹ ⭐ **G(2x) = −G(x)，G(3x) = −G(x)**（两个**精确**对称）✓✓
   Lean ✓：`oddCompletion*`（构造与性质）＋ `Commuting.lean`（`defect_commuting_square`／
      `commuting_completion_two`／`_three`）

【段 3 · 下降（extension）—— 无限性在此承担】 H := {c : F(cx)=F(c)F(x) ∀x} 为子群 ✓
   q := **最小缺席正整数**（**必为素数**：否则因子分解会把它放进 H ✓）
   **短代表元**：每个 H-余商有正整数代表 **n < p/(2q)** ✓（Lean：`short_representative_of_invariance`）
      算术核心 = 两分支：a=2j（取最近的偶数）或 a=3j（取 3 | a∈{2q−1,2q+1}），均 j<q ⟹ a∈H ⟹ **更小代表元** ⟹ 矛盾 ✓
      Lean ✓：`extension_descent_certificate`（声明 `∃ a b j r, 0<j<q ∧ 0<r<n ∧ (a=2j∨a=3j) ∧ (b=1∨b=2) ∧ (a·n=p+b·r ∨ p=a·n+b·r)`）✓✓
   **扩展**：D(x) := F(qx)/(F(q)F(x)) 在余商上**常值** ⟹ 短代表元 + 短乘法性给 D(n)=1 ⟹ D≡1 ⟹ **q∈H 矛盾** ✓
   Lean ✓：`half_interval_extension_via_invariance`（**主承重**）＋ `extension_prime_step`＋ 强归纳 q-闭合

【段 4 · 小素数矛盾 ＋ 两素因子收尾】
   乘法性 ⟹ **G ≡ 1 于一切非零平方** ✓；而 G(−1)=−1 ⟹ −1 非平方 ⟹ **p ≡ 3 (mod 4)** ✓
   **小素数引理**：p≡3 (4) ⟹ 取 L=(p+1)/4 的素因子 ℓ ⟹ ℓ ≤ L < p/2 且 **ℓ 是 mod p 的平方** ✓
      （ℓ=2 时 p≡7 (8) ⟹ 2 是平方 ✓；ℓ 奇时 (ℓ/p)=(−p/ℓ)=(1/ℓ)=1 ✓）
   ⟹ **1 = G(ℓ) = λ(ℓ) = −1 矛盾** ✓✓（Lean：`no_multiplicative_agreement_of_odd`／`exists_prime_square_below_half`）
   ⟹ 每个素数 p>3 有 **2p = u+v，λ(u)=λ(v)=1** ✓
   收尾：N=2m；λ(m)=−1 用 **m+m**；否则 m=rsc（r,s 素，λ(c)=1）；r>3 时把 2r 的正-正对**乘 sc**（负号）✓；
      否则 2rs∈{8,12,18} 用显式恒等式 **8=3+5｜12=5+7｜18=7+11**（两端 λ=−1 ✓）乘 c ✓
   Lean ✓：`all_even_of_positivePrimePairs` ＋ `liouville_goldbach`（＝ Shusterman 命题逐字 ✓）
```

## §2 ⭐ 有限/无限如何破局（**本档核心** ✓✓）

```
(i) **阈值从不出现** ✓✓：不需要"N 充分大"；矛盾对**每个素数 p>3 单独成立** ⟹ 无 N_0 ✓
(ii) **无限性由"下降"承担** ✓✓：短乘法性（ab<p/2）⟹ **全域乘法性**——这不是渐近，而是
     对每个 p 的**精确有限下降**（每步严格缩小代表元 n）⟹ 逐 p 闭合 ✓
(iii) **有限残留极小** ✓✓：仅 **{8,12,18}**（两素因子皆在 {2,3}）＋ 素数 2,3 的乘法性 ✓
(iv) **算术入口 = 二次互反** ✓✓：不是解析输入，而是**初等二次互反**（取 (p+1)/4 的素因子）——
     这正是经典路线里交给 **GRH／零自由区** 的地方，此处改用**一次互反计算** ✓✓
⟹ **一句话**：本路线里"有限/无限"**不是被桥接，而是被消除**：
   **无渐近 ⟹ 无阈值 ⟹ 无有限验证区间** ✓✓
```

## §3 与两条标准路线对照（✓）

| 项 ✓ | Helfgott（弱 Goldbach，奇数） ✓ | Mangerel（Liouville 版，偶数） ✓ | **本 artifact** ✓ |
|---|---|---|---|
| 核心工具 ✓ | 圆法／主弧＋奇异级数 ✓ | 特征分解＋短素数区间**零自由区** ✓ | **交换平方 ＋ 下降 ＋ 二次互反** ✓✓ |
| 条件性 ✓ | 无条件（巨量计算） ✓ | **GRH（或弱零自由区）** ✓ | **无条件** ✓✓ |
| 阈值 ✓ | N ≥ N_0 ＋ 有限验证 ✓ | N 充分大 ✓ | **无阈值（∀ p>3）** ✓✓ |
| 有限部分 ✓ | Helfgott–Platt 巨量计算 ✓ | 未解决 ✓ | **{8,12,18} 三条恒等式** ✓✓ |
| 结论 ✓ | 奇数 = 三素数和 ✓ | λ 型存在性 ✓ | **∀ 偶数 N>2** ✓✓ |

## §4 审计现状与残余（含本刀新增核对 ✓）

```
【已审（前档）】 语句级 ✓✓（`Main.lean` 主定理逐字＝ Shusterman 命题；无额外假设；用 **Mathlib 的 liouville** ✓）｜
   公理级 ✓✓（12 项仅 `propext`／`Classical.choice`／`Quot.sound`；**无 `sorryAx`** ✓）｜
   路线级 ✓✓（九项新组件全在、七项替换组件全缺 ✓）｜`q.Prime` 义务闭合 ✓（强归纳＋素/合二分 ✓）｜
   Coset 四项清单 ✓（含 `2*(q*n) < p` 严格性由**奇偶性**保证 ✓）
【本刀新增核对 ✓】 `Main.lean` 与 `PROOF.md` **逐段对应** ✓；`extension_descent_certificate` 的**算术下降核心**
   与 `PROOF.md` §2 短代表元证明**逐字对应**（两分支 a=2j／a=3j，b∈{1,2}，r<n ✓✓）
【残余 ⚠️✗】
   ⚠️ 深层 `*_nat` 引理（`doubleDefect_eq_zero_nat`／`defects_equal_nat`／`doubleReflection`／`upperBand`）
   ⚠️ 构造类（`oddCompletion` 系列 `_zero/_one/_neg/_sign/_nat/_short_mul`；`centralRepresentative`）
   ✗ **独立复现未做**（未 `lake build`；未重跑 `check_axioms.py`）
   ✗ **provenance 未闭合**（公开身份 `CaptainSude`；**无** Astra／OpenAI 官方关联）
   ⚠️ 注记：`Classical.choice` 出现 ⟹ 结论是**存在性、非有效可计算**（与 Mangerel "effectively computable N_0" 对照 ✓）
```

## §5 关键风险点（本刀判断：最脆三处 ✓）

```
① `half_interval_extension_via_invariance`（**主承重**）——若其隐含"F(1)=1、取值 ±1"之外的假设 ⟹ 全链失效 ⚠️
② `oddCompletion` 的**忠实性**（G(n)=f(n)（0<n<p/2））——段 3 的"短乘法性"来源；构造出错则段 3 断 ⚠️
③ `no_multiplicative_agreement_of_odd`（**矛盾步**）——依赖"乘法性 ⟹ 平方上取 1"＋"G(−1)=−1"＋互反小素数引理 ⚠️
⟹ 这三处正是 `C296–C299` 标为"**内容待审**"的部分 ✓（自审路径一致 ✓）
```

## §6 边界（✗✓）

- **不**写成"Astra 官方成果"（provenance 未闭合 ✓）；**不**声称已独立复现／已同行评审 ✗
- **不**与经典（二元）Goldbach 混同：本结论为 **Liouville 版**；**经典 Goldbach 仍开放** ✓✓
- **照录**：**我们无能力自行完成该证明** ⟹ 本档只做**审计／理解**，**不**尝试补证 ✗✓
- 不接 M-TOWER／不建判据／不做 L-F-B-R 排序 ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓✓）

```
技术词 重读审计     命中文件数=0    :: 
技术词 有限无限结构 命中文件数=0    :: 
技术词 下降引擎     命中文件数=0    :: 
技术词 均匀性破局  命中文件数=0    :: 
⟹ 四项**均本档首次命名**（本轨新增）✓✓
```

## §8 下一步选项（只列不选，决策权在唐先生 ✓）

```
(甲) **独立复现**：Lean 4.32.0 ＋ mathlib ＋ lake（NAS 需镜像）⟹ 把状态从"artifact 待复现"推到
     **"已独立复现"** ✓✓（预计数小时；本档评估为**最高价值的一步** ✓）
(乙) **只审三处最脆点**（§5；纯纸面）✓
(丙) **归档并停**：维持现有状态判定 ✓
```
