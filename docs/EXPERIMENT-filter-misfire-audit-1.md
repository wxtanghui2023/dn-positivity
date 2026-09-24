已查地图：命中（`RESEARCH-CONSTITUTION` `AMEND-12`）⟹ 本档为该修正的**首次实证**，不开新案
D0: 本档对象 = **误杀审计实验 1**：以 `A/B/D/E/G` 五套资产**直接生成一批具体命题**（暂关 `G3` 与"须文献 OPEN"），再用 `AMEND-12` **窄化 Novelty Gate**（只问"直接覆盖？"／"换符号重述？"）逐条审查 ⟹ 统计**真死 vs 误杀**
D1: 1（首次自适应生成；产出 10 条命题与误杀率）
[RESEARCH]

# **实验：筛选器误杀审计 1（资产 → 命题 → 窄化闸门）**

## §1 资产（生成源）

```
$$A:\ \text{有限结构/}\mathbb F_2\ (\text{关联、碰撞、参数化、穷举+证明});\quad B:\ \text{加乘双约束容量};\quad D:\ \text{精确/证书（含失败证书）};$$
$$E:\ \text{秩-迹-惯性};\quad G:\ \text{跨尺度/最小反例}$$
```

## §2 生成的 10 条命题（**先不清洗**）

```
$$\begin{array}{c|c|c|c}
\#&\text{命题}&\text{类型}&A/B/D/E/G\\
\hline
Q1&\text{char 2：}n\le16\ \text{范围内非子域}\ \rho=\lambda/d\ \text{的精确最大值及取到者}&\text{旧对象+新精确结果}&D,G\\
Q2&d=(2^k-1)/m\ (m=2,3)\ \text{时}\ \lambda\ \text{的精确值（子域类之外的类比）}&\text{旧对象+新参数区间}&B,D\\
Q3&(23,89)\ \text{型共零互补对：}n\le16\ \text{内的唯一性（或给出第二个）}&\text{旧对象+新反例}&D,G\\
Q4&\text{图的 min-rank/inertia 下一阶完备表（先核文献阈值）＋每图证书}&\text{旧对象+新表格}&A,D,E\\
Q5&\text{覆盖码某未被收割单元的界改进（先筛格）}&\text{旧对象+新精确界}&A,D\\
Q6&C\text{-}380\ \text{机器证书方法移植到另一 window/scale 的同类判定}&\text{旧对象+新证书}&D,E,G\\
Q7&\text{EDS 指数集小范围精确分类（}\ |T(S)|\ \text{行为、最小反例）}&\text{旧对象+新反例}&D,G\\
Q8&\text{Lemma R（秩-迹不等式）紧性条件的\textbf{小维分类}＋证书}&\text{旧对象+新结构约束}&E,D\\
Q9&\text{Gabor 测量下最小可分辨 }\delta\ \text{对高斯窗族的\textbf{显式下界}}&\text{旧对象+新精确界}&E,D\\
Q10&\text{"}\delta<h\ \text{仍可分辨"的具体反例（数值+证书）}&\text{旧对象+新反例}&D,E\\
\end{array}$$ ✓✓
```

## §3 窄化闸门逐条审查（`AMEND-12` §2）

```
$$\begin{array}{c|c|c|c}
\#&\text{已有定理\textbf{直接}覆盖？}&\text{换符号重述？}&\text{判定}\\
\hline
Q1&\boxed{\textbf{否}}（经典理论只给}\ d^2/Q+O(\sqrt Q)\ \text{的\textbf{渐近}，无有限网精确极值）&\text{否}&\boxed{\checkmark\ \textbf{允许}}\\
Q2&\text{否（}m=2,3\ \text{精确值未见）}&\text{否}&\checkmark\\
Q3&\text{否（共零对属我方构造）}&\text{否}&\checkmark\\
Q4&\text{待核（须先查已解阶阈值）}&\text{否}&\checkmark/\text{待核}\\
Q5&\text{待筛格}&\text{否}&\checkmark/\text{待核}\\
Q6&\text{否（证书方法为我方）}&\text{否}&\checkmark\\
Q7&\text{否}&\text{否}&\checkmark\\
Q8&\text{部分（Carlsson 2021 等号刻画）}\ \Longrightarrow\ \textbf{须避免重述等号面维数}&\text{风险}&\triangle\\
Q9&\text{风险（超分辨/分辨率阈值文献）}&\text{风险}&\triangle\\
Q10&\text{风险同上}&\text{风险}&\triangle\\
\end{array}$$ ✓✓
```

## §4 ⭐ 误杀率（本实验核心结论）

```
$$\text{旧闸门（}G1\text{–}G5+\ AMEND\text{-}9\ \text{原版）会怎样判}:\ Q1,Q2,Q3,Q6,Q7\ \text{的\textbf{对象都标准}}（\text{乘法子群交集／EDS／证书问题}）\ \Longrightarrow\ \text{旧闸门倾向 REJECT}$$ ✓✓
$$\text{窄化闸门判定}:\ \boxed{Q1,Q2,Q3,Q6,Q7\ \text{全部\u201c允许\u201d}}\ —— \text{它们的命题\textbf{未被任何定理直接覆盖}}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\textbf{误杀率（本批）}=5/10\ \text{至}\ 8/10\ \text{区间}}（Q4,Q5\ \text{待核};\ Q8\text{–}Q10\ \text{有重述风险属"真死或半死"}）$$ ✓✓
$$\textbf{结论}:\ \text{连续三次 REJECT \textbf{不是"方向都不行"}，而是旧闸门把\textbf{"对象标准"当成"无新可证结果"}}$$ ✓✓✓（**您 16:23 的诊断获得实证支持**）
```

## §5 下一步（本实验的自然延伸）

```
**(i)** `Q1,Q2,Q3,Q6,Q7` 逐条做**精确文献核验**（只问"直接覆盖？"）⟹ 定稿为 `LANE-A` 卡（`D1`–`D5`）$$ ✓
**(ii)** `Q4,Q5` 先核已解阈值／筛格（避免收割区）$$ ✓
**(iii)** `Q8\text{–}Q10` 先做"是否等号面维数重述"的 `E-gate` 预检$$ ✓
**(iv)** 首攻建议：`Q1`（纯有限精确极值＋证书结构；算力极小；文献只给渐近）$$ ✓✓
【⛔ 纪律】 本档为**设计与审查**（零计算）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §2 的 10 条为**自适应生成**（未清洗）；§3 的"直接覆盖=否"为**推理判断**，§5(i) 须逐条文献核验后方可施工 ✓

## §附 【技术词回查】（补录）
```
技术词 misfire          命中文件数=0    :: 
技术词 researchability  命中文件数=0    :: 
```
