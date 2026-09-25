已查地图：已跑 scripts/prework_map_check.sh K(10,1) 下界 Haas van Wee Habsieger 同余 ⟹ 本档为**方向规划＋难点拆解＋文献定位**（执行自 EXCESS-2026-09-25 与 MAPPING-2026-09-25 两档）；不开新研究方向。
D0: 本档对象 = `K(10,1)` 格的下界方法族（文献标准对象；非新对象）
D1: 0（无新独立自由度；产出为路线图、难点分解与文献清单）

# PLAN-2026-09-25 · `K(10,1)` 下一轮：方向规划 / 难点拆解 / 文献定位

## §1 文献定位（本轮实测，Firecrawl REST；tavily 额度已尽 432 ✗）

```
$$n=10\ \text{的下界阶梯（实测）}:\quad \lceil 1024/11\rceil=94\ (\text{球覆盖}) \ <\ \lceil 2^{10}/10\rceil=103\ (\mathbf{van\ Wee\ 1988})\ <\ \mathbf{107}\ (\text{Bertolo–Östergård–Weakley 2004 混合码表}) \ \ll\ 120\ (\text{上界})$$
```

**关键文献（含可获取性）**

| # | 文献 | 作用 | 可获取性 |
|---|---|---|---|
| L1 | **Wu & Chen 2024**, *Improved lower bounds on the domination number of hypercubes and binary codes with covering radius one*, Discrete Math 347(2):113752 | 用 **Habsieger(1997) 同余性质**改进下界（**仅 n 为 6 的倍数** ⟹ n=10 不适用 ✗） | **arXiv:2203.16901 免费** ✓ |
| L2 | **van Wee 1988**, *Bounds on packings and coverings by spheres in q-ary and mixed spaces* | `γ(Q_n) ≥ 2^n/n`（excess counting 源头） | ScienceDirect（有 PDF 入口）⚠️ |
| L3 | **Haas 2002**, *Binary and ternary codes of covering radius one: some new lower bounds* | **子空间内码字数满足线性不等式系统** ← 本档所指"耦合变量" | ScienceDirect / ACM ⚠️ |
| L4 | **Haas 2013**, *On the general excess bound for binary codes with covering radius one* | 一般 excess 界；同余（**n≡−1 mod 3** 情形） | ScienceDirect ⚠️ |
| L5 | **Bertolo–Östergård–Weakley 2004**, *An updated table of binary/ternary mixed covering codes* | **107 的出处** | Wiley 免费 PDF 入口 ✓ |
| L6 | **Habsieger 1997**, congruence properties（Wu–Chen 的方法来源） | 同余机制 | 待定位 ⚠️ |
| L7 | **Honkala**, *A new lower bound on codes with covering radius one* | 下界族 | Semantic Scholar ⚠️ |
| L8 | **Quistorff & Schneider 2007**, *New results on integer programming for codes* | **整数规划用于码界** | Congressus Numerantium ⚠️ |
| L9 | **arXiv:2608.19872v3 (2026)**, *New upper and lower bounds on covering codes K_q(n,R)* | 覆盖面 `q^n=10^10` 的 IP 精确计数；58 条新下界（6≤q≤21） | **arXiv 免费** ✓ |
| L10 | Cohen–Honkala–Litsyn–Lobstein, *Covering Codes*（书, 1997） | "excess bounds" 与 "method of linear inequalities" 分章 | 书 ⚠️ |

> **重要**：L1 摘要明确 `n≥10` 且 `n≠2^k,2^k−1` **仍是开问题** ✓ ⟹ 我们的目标格合法存在 ✓；
> 但 L1 的同余改进**只覆盖 n≡0 (mod 6)**，L4 覆盖 **n≡−1 (mod 3)** ⟹ **n=10 恰好落在两个"好同余情形"之外** ✗（10 mod 6 = 4；10 ≡ 1 mod 3）✓（与唐先生判断一致 ✓）

## §2 难点拆解（为什么卡住，以及卡在哪里）

```
D-1 我们已严格封死的层次（不再重复）
  · Layer 0/1: 球总量 + m-面未加权计数 ⟹ 最强 94 ✓ CLOSED
  · Layer 2  : 层式不等式族（Haas 2013 局部形式）⟹ **LP 恰 = 1024/11** ✓ CLOSED
    根因（解析）: 均匀解 z_c=1/11 使全部 11,264 条约束同时取等（用 (11−i)C(10,i−1)=i·C(10,i)、(i+1)C(10,i+1)=(10−i)C(10,i)）
    ⟹ **只要新增约束仍容许均匀分数解，LP 界不可能改善** ✓（这是"为什么必然弱"的硬道理）

D-2 真正缺失的机制（文献有、我们无）
  ① **跨中心/跨子空间耦合变量**（Haas 2002 的线性不等式系统：固定 k-维子空间后，码字数的多变量线性耦合）✓
  ② **同余机制**（Habsieger 1997 / van Wee / Haas 2013）：δ 的模 p 约束 ✓
     ⚠️ 但 n=10 落在 6∤10 且 10≢−1 (mod 3) ⟹ 不能机械套用 ✗（需自有推导或新同余）
  ③ **混合码（binary/ternary）精细化** ⟹ 107 的实际来源（L5）✓
  ④ **整数规划的精确覆盖计数**（L8/L9）✓
```

**核心判断**：`Layer 2` 的失败不是"LP 松弛太松"这一个工程问题，而是**该族在结构上等价于球覆盖** ✓
⟹ 唯一有前途的两条：(i) **破坏均匀分数解**（引入耦合变量/子空间 incidence，而非再堆同型层约束 ✓）；(ii) **构造**（不需要下界机制 ✓）

## §3 路线图（含判定标准）

```
Step 1（明日，低成本）: 修复版层 ILP 重跑
  ① 单次建模（消除 bad_alloc） ② 平移对称破缺 z_0=1（严格 WLOG：C↦C⊕t 保持约束族 ✓，非空解可平移使 0∈C ✓）
  ③ 先 LP relaxation ④ 再 ILP，记录 root bound / incumbent / gap（不只看 SAT/UNSAT）
  判定: 若 ILP 最优 ≈94–100 ⟹ 该族瓶颈**不在整数性**而在缺耦合 ✓ ⟹ 直接进 Step 2/3
        若 ILP 最优 ≳107 ⟹ **整数性本身已产生提升** ✓ ⟹ 值得把该族加进更大的 IP 模型

Step 2（文献获取，唐先生下载）: L1(arXiv 免费 ✓) → L3/L4/L2 → L5(免费入口 ✓) → L6/L7
  目标: 拿到 Haas 线性不等式系统的**准确形式**与 Habsieger 同余的**准确陈述**

Step 3（耦合模型）: 建含子空间耦合变量的 IP
  纪律: **校准门** —— 必须先精确复现真实 120-码（|C|=120, E=296, δ 分布, 一/二/三阶恒等式, incidence）才允许代 c=119 ✓
  判定: 若 119 在此模型下获**正式 infeasible certificate** ⟹ 真下界提升 ✓（最高价值）
        若 119 可行 ⟹ 该层降级，进 Step 4

Step 4（构造线，与 Step 3 并行）: 不依赖下界机制
  ① 对称性约束搜索（固定自同构子群 / 轨道分解）② 递归构造（(u,u+v) 型、wedge 型；L9/L2 的构造侧）
  ③ **混合多电平构造**（107 的出处即混合码线 ⟹ 构造侧同源 ✓）
  判定: 得 119 ⟹ 上界改进（真 dent ✓）；结构化全线失败 ⟹ 记录"该格进入 AI 有限搜索边界" ✓
```

## §4 今晚收口状态（2026-09-25 23:2x）

```
· `Σz=119`（层族 ILP）：**UNKNOWN**（300s）⟹ 记录为"尚未判定"，**不得**转为不可行 ✗
· `min Σz`：崩溃（bad_alloc，脚本内二次建模）⟹ 已修复方向明确 ✓（并已记入 TOOLS.md `1e3ea12`）
· 崩溃伴生 1.8GB core dump：**已删** ✓
· 今日新增可复用资产：δ-场恒等式体系 ✓、局部守恒律（代数恒等式）✓、Layer 2 解析封口 ✓、下界阶梯定位 ✓
```

## §5 边界（诚实标注）

- 本文献结论基于 Firecrawl REST 检索＋三处原文抽取（arXiv abs 页 ×2、arXiv HTML ×1）；**L1 摘要为逐字引用** ✓，其余为条目级定位 ✓
- **未**逐篇精读 L3/L4/L6；**未**核验 L5 的 107 与 van Wee 界的推导关系（仅知阶梯顺序 ✓）
- 不主张 `K(10,1)` 的可判定性；不主张任何"存在/不存在"结论 ✓

---

## 【技术词回查】（定稿前 `scripts/tech_word_check.sh` 逐字输出）

```
技术词 δ-场           命中文件数=2    :: ./PLAN-2026-09-25-K10-1-next-direction-and-difficulty-breakdown.md ./EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md
技术词 局部守恒律  命中文件数=3    :: ./EXT-4CT-2026-method-transfer.md ./PLAN-2026-...md ./EXCESS-2026-...md
技术词 层式不等式族 命中文件数=2    :: ./PLAN-2026-...md ./EXCESS-2026-...md
技术词 下界阶梯     命中文件数=1    :: ./PLAN-2026-09-25-K10-1-next-direction-and-difficulty-breakdown.md
技术词 校准门        命中文件数=2    :: ./PLAN-2026-...md ./EXCESS-2026-...md
```

**三分类标注**

- **本档新增**（仅本组两档自命中，无更早来源）：`δ-场`、`层式不等式族`、`下界阶梯`、`校准门`
- **档案已有（引用，不列为提出）**：`局部守恒律`（早档 `EXT-4CT-2026-method-transfer.md` 已有 ✓）
- **通用词（不计）**：—
- **说明**：本档**不**主张任一技术词为本项目首创 ✓
