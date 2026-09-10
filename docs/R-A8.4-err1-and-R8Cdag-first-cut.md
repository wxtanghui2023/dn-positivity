# R8.4-ERR-1（取代登记）+ R8-C† 第一刀：Voronoi/显式公式结构断点

**日期**：2026-09-10 13:54+ ｜ 依据：唐先生核实 Motohashi 1994 原文 ｜ 预算：纸面，无代码

---

## 0. ⚠️ R8.4-ERR-1（取代，留原档，不静默改写）

```
被撤回（R8.4 §2 内）："divisor case is unconditional because its spectrum is
                     purely discrete/self-adjoint"
撤回理由：Motohashi 1994 的 spectral decomposition 并非"只有离散谱"；
         其分解涉及 automorphic spectral data 与 cusp forms，且与
         Kuznetsov / Kloosterman sums / Fourier coefficients 耦合
         ⟹ "纯离散/自伴 ⟹ RH 自动侧"为【过度简化】，未获文献核实
合法修正为：
```
$$\boxed{\text{divisor case possesses an }\textbf{unconditional automorphic spectral engine}}$$
**⚠️ 关键影响**：若不修正，R8-C\* 会建立在**假的"谱二分"**之上 ⟹ 本条取代必须先入档。

---

## 1. 文献前提（I 层第一轮核验结果，唐先生）

```
① Motohashi 1994《The binary additive divisor problem》(Ann. Sci. ENS) 研究
     D(N;f)=Σ_{n≤N} d(n)d(n+f)，目标是渐近式与误差项
② 历史链明确：Kloosterman sums → Kuznetsov trace formula → cusp-form Fourier coefficients
   （原文指出 Deshouillers–Iwaniec 用 Kuznetsov 改进误差项；Motohashi 建立更完整谱分解）
③ **Motohashi Theorem 1 给出对 shift f 的 uniform 结果**（范围 1 < f < N^{1/2}）
④ Motohashi–Ivić 1995：E(X;f) 关于 shift f 的均方，用 spectral large sieve + E(x;f) 的 explicit formula
```
$$\boxed{\text{h-space 本身【可以】承载真正的谱 cancellation（已非推测，文献事实）}}$$

---

## 2. R8-C† 正式登记（Spectral Input Dichotomy）

$$\boxed{\textbf{R8-C}^{\dagger}}:\ \text{对 canonical、zero-blind、非-HL 的 }h\text{-space cancellation，}\\
\text{若它能产生 }V(X,H)\sim HX\log(X/H)\text{，则其内部必须存在一个 spectral/arithmetic input，}\\
\text{同时完成：①解析 }\Lambda\text{ 的非对角 correlation ②对 }h\text{-shift 保持真 uniformity ③提取精确二阶主项 }H\log(X/H)$$
**三子命题（可审计）**：
```
C1（对象层）：S2-c ⟹ 真正的 Λ-shift spectral input（而非仅 Fourier mean-square）
C2（主项层）：H log(X/H) 不是由 diagonal/Kloosterman size/sieve density 自动产生；
             正确系数 1−η=1/α 本身必须由某种【跨尺度谱结构】产生
C3（zero-blindness 层）：定义 "zero-blind spectral engine"（输入不用 ζ zeros / pair correlation /
             explicit-formula zero sum，也不经等价变换隐式恢复 F(α)）
             ⟹ 问：C1+C2 是否迫使 C3 失败？
```
**⭐ 由 divisor 反例校准（必须写死）**：
$$\boxed{\text{h-space cancellation}\ \not\Rightarrow\ F(\alpha)}\quad(\text{被 }d(n)d(n+h)\text{ 的真 h-space 谱机器击穿})$$
⟹ **R8-C\* 不得**声称"任何 h-space spectral cancellation ⟹ F(α)"；只能问
$$\boxed{\text{对 }\Lambda\times\Lambda\text{ 的 canonical correlation，产生正确二阶主项所需的谱输入是否只能从 zero-side 获得？}}$$

---

## 3. ⭐⭐ 第一刀结果：结构断点 = 【Voronoi 对显式公式】

**拆 additive divisor 的 Kuznetsov 入口（逐项）**：
```
d(n)d(n+h) 的处理链：
  h-shift → 【Voronoi summation】把一个因子对偶化 → Bessel 核 + 对偶和
          → Kloosterman sums → Kuznetsov 迹公式 → automorphic spectral coefficients
```
**关键：Voronoi 求和公式的成立条件**：
$$\boxed{\text{Voronoi 公式 = 相应 Dirichlet 级数的【函数方程】的"影子"；}\\
\text{它要求被求和的系数来自一个具备函数方程的（自守/Voronoi 类）L 函数}}$$
```
· d(n)：Dirichlet 级数 = ζ(s)² ⟹ **有函数方程**（Γ 因子 + s↔1−s）⟹ Voronoi ✓
        且 ζ² 属"函数方程类"，乘法封闭 ⟹ Kuznetsov 兼容 ✓
· Λ(n)：Dirichlet 级数 = −ζ'/ζ ⟹ **没有函数方程**；
        其 Mellin/Perron 转移给出的是【零点和】（显式公式）
        ⟹ Vienna 步骤被【显式公式】取代，而对偶对象【就是零点】
```
$$\boxed{\textbf{结构断点}:\ d(n)\ \text{属"函数方程/Voronoi 类"（系数层）；}\\
\Lambda(n)\ \text{住在【对数导数】侧，其"对偶"恰是零点分布}}$$

**⟹ 候选引理 L1（R8-C† 的第一条引理候选）**：
$$\boxed{\text{L1}:\ \text{Kuznetsov/Voronoi 引擎要求移位关联的两个因子来自【函数方程类】；}\\
d(n)\ \text{在该类内（ζ²），}\Lambda(n)\ \text{不在（−ζ'/ζ 无函数方程，其 Mellin 对偶即零点和）}}$$
**L1 直接解释三件事**：
```
① 为何 divisor 情形能无条件走出 h-平均（两因子皆 Voronoi/Kuznetsov 兼容）
② 为何 Λ 情形的 h-平均需要 zero-side（Voronoi 步骤被显式公式取代）
③ 为何 BKS 明确"从 zero statistics 出发"（Λ 缺 HL 型算术自相关）
```
**与既有登记的连接**：这正是 N1（显式公式重编码）+ 门⑰（引擎平凡化：Sym²(平凡)=平凡）+ 门⑲⑳（离散/散射不对称）在 R8 世界的**同一件事**。

---

## 4. L1 的可证伪条件（预注册）
```
L1 被推翻（⟹ R8.4-A 方向打开）当且仅当存在：
  一个【Λ-侧】的 canonical、zero-blind、非-HL、non-Voronoi 的谱引擎，
  能对 Σ_h w_H(h)Σ_n Λ(n)Λ(n+h) 提取正确的二阶主项 H log(X/H)
  —— 例如：把 Λ 视为某类"广义系数"而存在对应的 Voronoi/对偶结构，
     且其对偶对象不是零点和
```
**可核实项**：是否存在"Λ 的 Voronoi 型公式"文献（若有且对偶非零点 ⟹ L1 立即被削弱）

## 5. 诚实边界
```
· §1 的 Motohashi 事实为唐先生核实（文献级）；§0 取代登记为自我更正
· §3 的"Voronoi = 函数方程的影子"为标准认识（文献级）；但
  "Λ 不在函数方程类"是【结构性论证】，须以文献核实（尤其是否存在 Λ 的 Voronoi 型公式）
· L1 为【引理候选】，非已证引理；§4 给出其可证伪条件
· 未写代码、未做数值；未引入 ζ 零点或谱算子（L1 陈述中"对偶即零点"为结构定位，非计算）
```

## 6. 提交链
```
bcfdcb9 R8.4 → 本篇（R8.4-ERR-1 + R8-C† 第一刀）
```
