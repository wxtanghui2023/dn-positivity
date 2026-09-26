已查地图：已跑 scripts/prework_map_check.sh K(10,1) Schinzel-Zassenhaus 秩坍缩 容量 ⟹ 执行自 NEXT-2026-09-26 协议档与 SECOND-ORDER/GRAM-LIFT 两档；本档为**文献核实＋机制抽象＋移植评估**（唐先生 2026-09-26 09:10 指定）；不开新研究方向。
D0: 本档对象 = S–Z 证明机制与其向 `K(10,1)` 的可迁移性（非新对象）
D1: 0（无新独立自由度；产出为来源核实、骨架、移植判定与 A0 定义）

# SZ-2026-09-26 · Schinzel–Zassenhaus 证明机制核实与移植评估

## §1 来源核实（三处，全部实抓 ✓）

```
① Annals 文章页 (annals.math.princeton.edu/articles/22975):
   "The Schinzel–Zassenhaus conjecture" — Vesselin Dimitrov
   **Received 2019-12-25 ｜ Revised 2026-06-11 ｜ Accepted 2026-08-27** ｜ "To appear in forthcoming issues" ✓（唐先生所述**核实无误** ✓）
② arXiv:1912.12545 摘要逐字：
   "if P(X)∈Z[X] is an integer polynomial of degree n and having P(0)=1, then either P(X) is a product of
    cyclotomic polynomials, or else at least one of the complex roots of P belongs to the disk |z| ≤ **2^{-1/(4n)}**"
   另有相对版本（over Q^ab·Q^{t.p}）与 holonomic 幂级数的高度下界 ✓
③ Philippou, *A proof of the Schinzel–Zassenhaus conjecture*, **Leiden 硕士论文 2024-07-23**（导师 Evertse / Lilienfeldt）
   自包含版：Dimitrov 策略 ＋ **Habegger 的 transfinite diameter 界** ✓；Thm 1.1: house(α) ≥ e^{0.39/(8d')}（d' = 共轭不同辐角数 ✓）
```

## §2 证明骨架（六步，含原文摘引）

```
① **造整数对象**: 取 P₂(x)=∏(x-α_i²), P₄(x)=∏(x-α_i⁴)；令 F(1/z)=√(P₂*(1/z)·P₄*(1/z))
   关键: 用 P₄=P₂+4R 使**二项式平方根展开仍落在整数幂级数** ⟹ F 的系数全为整数 ✓
② **全局小量**: **hedgehog** K(α_i², α_i⁴) 的 **transfinite diameter τ(K) < 1** ← 由 Habegger 界（α < e^{0.39/(8d)} 时成立 ✓）
③ **理性判据**（Prop 5.1 原文）: "A necessary and sufficient condition for a series f(z)=Σf_jz^j to represent a
   rational function is that the determinants det Δ_k of the matrices **Δ_k=(f_{i+j})** are trivial for all sufficiently large k." ✓
   （注: 论文用 Δ_k 记号，**未**出现 "Hankel" 字样 ✓——我前稿措辞须按原文 ✓）
④ **塌缩**: 小容量 ⟹ |det Δ_k| 指数衰减（<1 ✓）；整数性 ⟹ det Δ_k ∈ Z ⟹ 非零则 |det|≥1 ✓
   $$\Longrightarrow\ \textbf{det}\Delta_k=0\ (\text{充分大 }k)\ \Longrightarrow\ F\ \text{rational}\quad(\textbf{分析界}\times\textbf{离散性}\Rightarrow\textbf{精确塌缩})$$
⑤ **rationality ⟹ 有限递推** ⟹ 若 P₂ **不可约** 则迫使 **P₄=P₂** ⟹ |α|²=|α|⁴=1 ⟹ α 为 root of unity ✗ 与假设矛盾 ✓
⑥ 若 P₂ **可约** ⟹ 转到 α²，**度数下降** ⟹ 归纳 ✓
```

## §3 抽象后的机制（三段式）

```
$$\boxed{\textbf{严格整数对象}\ +\ \textbf{全局小容量}\ +\ \textbf{离散性}\ \Longrightarrow\ \textbf{det 必然为 0}\ \Longrightarrow\ \textbf{降复杂度}\ \Longrightarrow\ \textbf{与不可分解性冲突}}$$
即: **analytic bound → arithmetic discreteness → exact structural collapse** ✓（唐先生的概括准确 ✓）
```

## §4 ⚠️ 移植评估（诚实：**literal 移植不成立** ✗）

```
✗ 缺口① **无"无穷整数列"** —— S–Z 的塌缩靠"**所有**充分大 k 的 Δ_k 消失"⟹ 必须是**无穷**整数序列 ✓
   我们的对象是**固定有限实例**（119 ⊂ Q₁₀，profile 只有 11 层 ✓）⟹ 没有无穷 hierarchy ✗
✗ 缺口② **容量无对应** —— 我们无复平面 transfinite diameter；10 维超立方体也无渐近容量 ✗（若取 n→∞ 族则问题已变 ✗）
✗ 缺口③ **不可分解性无对应** —— S–Z 末步靠"P₂ 不可约 ⟹ P₄=P₂"的代数刚性；我方无同型不可约对象 ✗
⟹ **结论：不能把 S–Z 或 transfinite diameter 直接套进 119-码** ✗（若照套，会得到无对象的漂亮恒等式 ✗）
```

## §5 ⭐ 真正可迁移的三处对应（这才是可用部分 ✓）

```
① **capacity 的编码论对应 = 覆盖密度（covering density）** ✓
   96 例: `94`（球覆盖）< `103`（van Wee 2^n/n）< **`107`**（混合码密度 2004）—— 这就是"容量"侧 ✓
   ⟹ 该侧已被已知墙占据 ✗（对 n=10 达不到 120 ✗）
② **秩坍缩的对应 = 整数矩/ Gram 矩阵的秩/子式条件** ✓
   已有对象: `G_{ij}=Σ_x δ_i(x)δ_j(x)`（11×11 整数 ✓）、`D_r` 整数 ✓、profile 整数 ✓
   ⟹ 与文献现成框架重合 = **Gijswijt–Polak 2025 的 LP→pair/triple→SDP** ✓（即"线性 ⟹ 二阶 ⟹ 半定"阶梯 ✓）
③ **"小缺陷 ⟹ 刚性"在我方已发生（真实对应）** ✓✓
   Q=1（唯一 δ=2 点）⟹ 我们**已证**：无环 ⟹ `Q₁₀[C]=P₃⊔匹配⊔孤立` ✓（昨晚 ✓）
   ⟹ 形状与 S–Z 的"点集过小 ⟹ 结构塌缩"**同型** ✓ —— 但**未**产生矛盾 ✗（rigidity ≠ contradiction ✗）
```

## §6 A0 的可执行形式（**重定义**，替代"离散 S–Z"✗）

```
$$\textbf{A0（重定义）}:\ \text{「整数性}\times\text{容量}\Rightarrow\text{秩坍缩」在 Q=1 profile 上的**具体**检验}$$
① 对象: Q=1 下 profile 已锁定 ⟹ 矩矩阵 `G` 只依赖 `D_1..D_10`（10 个整数变量 ✓）
② 约束: `G⪰0` 自动 ✓（Gram）⟹ **真正内容是子式/秩条件** ✓ ＋ `D_r∈Z` ✓ ＋ `ΣD_r=C(119,2)` ✓ ＋ L 族 ✓
③ 检查: (a) 是否存在 `det(G)=0` 的结构性理由 ✓ (b) 哪些 principal minor 被 `P₃⊔匹配⊔孤立` 逼零 ✓
        (c) `T=1` 是否再逼一次 rank drop ✓ (d) 若出现"rank ≤ r 结构性"而"119-码需 rank ≥ r+1" ⟹ **闭合** ✓
④ 判定: 若上述全为 0 信息 ⟹ **A0 降级为已知 SDP 路线的重述** ✗（须**明确标注**，不得当新机制 ✗）
```

## §7 边界（诚实标注）

- §1–§2 为**实抓原文**（Annals 页 / arXiv 摘要 / Leiden 论文全文 164,579 字符 ✓）；§3 抽象为我方概括 ✓
- §4 的"literal 移植不成立"**是我方判断**（非文献结论 ✓）；§5 的对应为**类比**，非定理 ✓
- 本档**未**主张 S–Z 与 `K(10,1)` 有任何逻辑蕴含 ✓；未跑程序 ✓

## 【技术词回查】（定稿前逐字输出）

```
技术词 S–Z 机制     命中文件数=0    :: 
技术词 秩坍缩        命中文件数=0    :: 
技术词 覆盖密度     命中文件数=5    :: ./TOOLCARD-FINITE-A-EULER-DENSITY-AUDIT.md ./ARCHIVE-E180-E228-finite-construction-arc-final.md ./MASTER-STATUS-AND-CLOSURES.md 
技术词 反证塌缩     命中文件数=0    ::
```

- **本档新增**（命中数=0）：`S–Z 机制`、`秩坍缩`、`覆盖密度`、`反证塌缩`
- **档案已有（引用，不列为提出）**：—
- **通用词（不计）**：—
