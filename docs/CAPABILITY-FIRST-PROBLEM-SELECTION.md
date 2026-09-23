已查地图：命中（`ASSET-PROBLEM-REVERSE-AUDIT-table`／`P-a-GATE-VERDICT-CLOSED-and-C-executed`／`RH-LINE-ASSET-VALUE-INVENTORY`／`PROTOCOL-pre-work-map-check`）⟹ **引用，不开新案** ✓
D0: 本档对象 = 承认**审计偏差**（RH 锚定）＋ 改为 **capability-first／winnability-first** 的筛选轴 ＋ 四个非 RH 问题类 ＋ 纪律变更
D1: 0 （`[REVIEW]` 轮次：方法论纠正与提名，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **Capability-first：把"资产能接什么问题"换成"我们能赢什么问题"**

## §1 ⚠️ **先承认偏差（本档第一件事）**

```
【您的质问】 "你的问题是否**永远围绕 RH 相关问题在审计**？而不是围绕**我们可能解决的问题方向**？" ✓✓
【诚实回答：是】 本会话我做的每一张表／每一次 gate／每一个候选，**锚点都是"我们为 RH 造出来的资产"** ⟹ 即 **`asset-driven` ＝ RH 派生** ⟹ 于是筛选出来的自然是"RH 邻近问题"（临界线零点比例／`\xi'` 局部几何／Off-axis 密度）✓✓
【⟹ 这是**结构性偏差**，不是措辞问题】 `asset-driven` 搜索**必然**产生：**(i)** 重发现（资产是既有词汇的重述）；**(ii)** prior-art 撞车（RH 邻近问题被研究了 150 年）✓✓ —— 池内**三次重发现**（`Gabor/STP`、`T1/T2 vs 超分辨`、`r_q = rank of apparition`）正是这个偏差的直接后果 ✓
【⟹ 结论】 $$\boxed{\text{审计轴错了：应为 problem-first ＋ capability-first，而非 asset-driven}}$$ ✓✓
```

## §2 **两种"价值"必须分开（不美化、也不自我贬低）**

```
【解决问题价值】 当前 ≈ `0` ✓（您说得对：**没有解决任何问题** ⟹ 作为**数学价值**就是 0）✓
【流程/档案价值】 有（负结果地图／证据纪律／防错觉判据）✓ —— ⛔ **但它不能算作数学价值**，只能算**降低未来成本** ✓
【⟹ 诚实的合取】 $$\text{研究价值}=\text{解决的问题}\quad(\text{其余皆为辅助})$$ ✓
```

## §3 ⭐ **正确的筛选轴（本档核心）**

```
【错误问法】 $$\text{我们的资产}\ \to\ \text{它能接哪个未解问题？}$$ ⟹ 三次重发现 ⟹ 杠杆 = 0 ✓
【正确问法】 $$\boxed{\text{我们能赢哪一类问题？}\ \to\ \text{它需要什么工具？}\ \to\ \text{缺的工具我们能不能造？}}$$ ✓✓
【关键区别】 起点是**我们真实的工作能力**（可算/可验/可闭），**不是**我们已有的数学资产 ✓
```

## §4 **我们真实具备的能力（工作能力清单，非数学资产）**

```
**(C1) 机器可复核的区间证书链**：区间下界 ＋ 独立校验器 ＋ 铺砌/体积审计（`k=4` 那套：118,068 boxes、0 residual、独立复核、`2^{96}` 体积核算）✓✓ —— **这套是本项目最硬的能力**
**(C2) 大规模穷举与精确整数判定**（`D(-3)` 的 148 边／76 三角／`#K4=0`；EDS 的 `B_n` 表）✓
**(C3) 形式化基础设施**：Lean 工具链可用；**已补过 Mathlib 缺口**（von Neumann 迹不等式／Sylvester 惯性）✓✓
**(C4) 文献核查与证据纪律**（逐字引用、档级标注、三层 collision 模板）✓
**(C5) 任意精度符号计算**（`mpmath`／`sympy`／`zstandard` 管线）✓
**(C6) 可追溯档案**（提交纪律、回查脚本、pre-commit 门）✓
```

## §5 ⭐⭐ **由此导出的四个问题类（全部非 RH 锚定，且 certificate-friendly）**

```
**【K-1】显式常数的改进＋证书**：已知定理中的常数未优化处 ⟹ 目标＝把常数从 `X` 压到 `Y`（一个数字）＋给**机器可复核证书** ✓（形式：旧界 `X` → 新界 `Y`）
**【K-2】穷举分类的**边界扩展**：某类对象的枚举/分类已证到 `N`，但可推进 ⟹ 目标＝把 `N` 推到 `N'`，**带完整性证书**（无遗漏证明＋独立校验）✓（我们 `k=4` 的证书链正好是模板）✓
**【K-3】Mathlib 缺口的形式化贡献**：把标准但缺失的引理**补进库**（已有先例 ✓）⟹ 目标＝可编译的 `sorry`-free 引理 ＋ 通过 CI ✓（`C3` 原生）
**【K-4】已发表**计算主张的复核/纠错**：重算文献里的数值/常数；错则给反例，对则给独立证书 ⟹ 目标＝可复核结论 ✓（`C1`＋`C5` 原生）
【共同特征】 全部**目标含一个数字**、**证书型**、**规模对我们可算（天级）**、**不依赖 RH** ✓✓
```

## §6 **选择四条件（winnability）＋ 纪律变更（本档最重要产出）**

```
【四条件】 **(1)** 目标含**一个数字**（常数/范围/计数）｜**(2)** **证书型**（可被独立机器复核）｜**(3)** 规模**对四类能力可算**（天级）｜**(4)** 非 RH ＋ 仍须过 novelty/map gate ✓
【⛔ 纪律变更（立此存照）】 $$\boxed{\text{禁止 asset-driven 搜索}}$$（它产生 3 次重发现与 prior-art 撞车）⟹ 改为 **problem-first ＋ capability-first**；**第一条产出必须是"带数字的证书"，不是"漂亮的资产"** ✓✓
【⛔ 另一条】 不再用"资产价值"语言自我评估；只用 **"这个具体问题是否被推进（数字是否变了）"** ✓
【边界】 ⚠️ 四个问题类为**方法论提名**（尚未选具体问题、未核 novelty）；§1 偏差承认、§3 筛选轴、§6 纪律变更为**本档自行推导** ✓；⛔ 未制造候选／未启动搜索／未改状态 ✓
```

## §7 【技术词回查】（逐字粘贴 ✓）

```
技术词 capability-first 命中文件数=1    :: ./CAPABILITY-FIRST-PROBLEM-SELECTION.md 
技术词 winnability      命中文件数=1    :: ./CAPABILITY-FIRST-PROBLEM-SELECTION.md 
技术词 证书链        命中文件数=5    :: ./C320-directed-recheck-C273-v5-design-family-CLOSED-M5-question-OPEN.md ./C354-branch-completeness-as-core-audit-quantity-and-discovery-certificate-coverage-separation.md ./C355-four-execution-locks-param-endpoints-singular-stratum-uniqueness-vs-coverage-quantified-certificate.md 
```
【三分类】 **本档新增**：审计偏差承认、两种价值分离、capability-first 筛选轴、`C1`–`C6` 能力清单、`K-1`–`K-4` 问题类、纪律变更 ✓；**档案已有（引用）**：见上逐字；**通用词（不计）**：`winnability` ✓
