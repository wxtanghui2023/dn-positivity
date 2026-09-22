已查地图：未覆盖（关键词: 刚性理论|Laman|pebble|对称刚性|曲面刚性|轨道刚性矩阵）—— 可开档，首行须照抄本行
　补证：本档续 `C-alpha-rigidity-MAP-CHECK-and-13-gate-screen.md`（`0785f49`）；组合刚性在本 RH 地图**零覆盖** ✓

# **C-α 台账锁定（GAP-HOLD）＋ 文献级 novelty audit**

**唐先生令（2026-09-22 20:58）**：
① **C-α 不应 PROMOTE，正式定为 `GAP-HOLD`** ✓（四项理由照录：**地图新** ✓｜**2D 关闭**（Laman 计数＝目标刻画，属重述）✓｜
　**3D 有真正独立的局部信息**（(3,6)-稀疏仅必要；**双重香蕉阻断"计数 ⟹ 刚性"**）✓｜
　**C3/C4 结构性断裂**（纯计数框架内）⟹ **不是尚未努力够** ✓）；
② **下一刀不应再挖 2D/3D 纯计数**；**若继续，只允许做一次文献级 novelty audit**：专查
　「**对称刚性／表示论计数／曲面刚性**是否真的产生一个**此前未覆盖、且有独立问题价值**的新不变量」；
　**若只是已知 rigidity-matroid／representation-theoretic reformulation ⟹ 立即 `DEAD`** ✓✓；
③ ⭐ **措辞锁定（照录）**：本档案保持「**GAP，不是潜在证明路线；PROMOTE 需要换不变量且先完成已知性核验**」✓✓

D0: 本档对象 = **C-α 台账状态锁定 ＋ 一次文献级 novelty audit**（档案已有对象 `C-α 核验档` 的**状态变更＋已知性核验**；非重命名、非新对象）
D1: 0
FREEZE-ACK: **零计算／零 Lean／未写程序／未碰 RH／未调用 C-380／未放宽门槛** ✓

---

## §1 **预注册 protocol**（先写死，后执行 ✓；一轮预算 ✓）

```
【范围】 仅三方向：① 3D＋纯计数 ② 对称刚性／表示论计数 ③ 曲面（拓扑修正）刚性 ✓
【唯一问题】 三者是否**真的**产生「**此前未覆盖 ＋ 有独立问题价值**」的新不变量？✓
【否决判据（写死，触发即 DEAD）】
　(a) 该"新不变量"实为**已发表框架**的 reformulation ✗
　(b) 该方向的核心问题已是**主流已知开放问题**（⟹ 不构成"未覆盖接口"）✗
　(c) 我方机制的下降环**已被反例结构性排除**（双重香蕉）✗
【预算】 **一轮**文献核验（非计算 ✓）；**不做**完整全文精读（**证据等级 = 题录级** ⚠️）✓
【输出】 逐方向判定 ∈ {DEAD, GAP-HOLD}；**不**产出推广承诺 ✓
```

## §2 文献核验结果（**题录级 ⚠️**；带来源 ✓）

```
【① 3D＋纯计数】 ⛔ (b) + (c) 触发
　· 计数法**仅在 d ≤ 2 充分**；`d > 2` **两条件皆不足** —— 标准反例 **double banana**
　　（"generically flexible, though it satisfies the basic counts"）✓【Handbook of Discrete and Computational Geometry, ch.61 ✓】
　· ⭐ **明文开放**：「**There is no combinatorial characterization of generically 3-isostatic graphs**」✓
　　＋ 相关猜想：**3-D Replacement Conjecture**（`TW85`）｜**Graver's / Dress' Conjecture**｜
　　　**Maximal Conjecture**（3 维存在唯一极大抽象刚性拟阵且 `= G₃(n)`）✓【Servatius, *Combinatorics and the rigidity of frameworks* ✓】
　· 2025 综述逐字：「characterising graphs which are generically rigid or globally rigid in `R^d` **is open for all `d ≥ 3`**」✓
　　＋ 同期活跃成果（Cruickshank–Jackson–Tanigawa：**triangulated manifolds 全局刚性**（Adv. Math. 2024）／
　　　**symmetric simplicial complexes 刚性**（Forum Math Sigma 2025））✓【arXiv:2508.11636 综述 ✓】
　⟹ 判定：**DEAD**（(c) 我方"失败保持下降"已被 **double banana 结构性排除**；(b) 剩余问题是**主流已知开放问题**，
　　　不构成"未覆盖接口" ✓）
【② 对称刚性／表示论计数】 ⛔ (a) 触发
　· **轨道刚性矩阵**（`Schulze–Whiteley 2011`）：`ker O(G₀,ψ,p)` ≅ 全对称一阶挠；`rank O = d|V₀| − triv τ(Γ)` ⟹
　　**forced Γ-symmetric 一阶刚性**的判据 ✓【Handbook ch.62 Thm 62.1.2／62.1.3 ✓】
　· **群依赖 gain-sparsity 计数**已成文（例：3 维半转 `C₂`：`|E₀| = 3|V₀∖V′₀| + |V′₀| − triv C₂`）✓
　· **Fowler–Guest 特征公式**（表示论分块对角化／一般化计数规则）✓【SIAM 2010／Handbook ch.62 ✓】
　· 周期／对称框架：`Malestein–Theran '10/'13`、`Jordán–Kasinitzky–Tanigawa '13`（**主体仍在 2D** ⚠️）✓
　⟹ 判定：**DEAD**（"表示论计数"**已是已发表框架** ⟹ 我方提法＝**reformulation** ⟹ 触发 (a) ✓）
【③ 曲面（拓扑修正）刚性】 ⛔ (a) 触发
　· ⭐ **已发表 Laman 型定理**：框架限于二维光滑子流形 `M ⊂ R³`；**同心球面／平行平面／同心柱面**的
　　**充要组合条件**已得 ✓【Nixon–Owen–Power, SIAM J. Discrete Math. 26(4) 1733–1757, 2012；arXiv:1009.3772 ✓】
　· **曲面上旋转体的 Laman 定理**（2012/2013）｜**曲面上的对称强制刚性**（arXiv:1312.1480, 2013）｜
　　**曲面框架的应力矩阵与全局刚性**（Jackson–Nixon）✓
　⟹ 判定：**DEAD**（拓扑修正计数**已有定理** ⟹ 我方提法＝**reformulation** ⟹ 触发 (a) ✓）
```

## §3 ⭐ 最终判定与台账锁定

```
【novelty audit 判定】 **三方向全部 DEAD** ✓（① (b)+(c)；② (a)；③ (a)）⟹ 依令："若只是已知 reformulation ⟹ 立即 DEAD" ✓✓
【C-α 台账（最终）】
　**C-α：首轮 = GAP-HOLD ⟹ 经**一轮文献级 novelty audit** ⟹ **DEAD**（**不再继续** ✓，依令"不应再挖 2D/3D 纯计数" ✓）
【⚠️ 判定的准确含义（防误读，依 `入口纪律` ②✓）】
　✗ **不是**"刚性理论没有价值／该领域已死"（该领域**活跃**：2024–2025 仍有主流成果 ✓）
　✓ **是**：**本仓 C-α 候选**（纯计数 → 失败下降 → 更强定理）在三方向上**均未找到"未覆盖且有独立问题价值"的新不变量** ✓
　✓ 且：**我方机制的下降环已被反例结构性排除**（这是**数学结论**，非努力不足 ✓✓）
【措辞锁定（照录令）】 本档与 `0785f49`／`a9916a8` 保持：
　「**GAP，不是潜在证明路线；PROMOTE 需要换不变量且先完成已知性核验**」✓✓
```

## §4 边界与回查（✗✓）

```
✗ 零计算／未写程序／未碰 RH／未调用 C-380／未放宽门槛 ✓
✗ 未新增推广承诺；未把"三方向 DEAD"记为战绩 ✓；**未**断言领域本身无价值 ✓
⚠️ **证据等级 = 题录级**（检索标题/摘要/片段，**未**逐字全文精读）⟹ 若需升为**逐字全文级**，须另授权 ✓
【技术词回查（`scripts/tech_word_check.sh`，**先跑后写** ✓；逐字粘贴 ✓）】
　技术词 轨道刚性矩阵        命中文件数=0 ⟹ **本档新增** ✓
　技术词 双重香蕉            命中文件数=0 ⟹ **本档新增** ✓
　技术词 表示论计数          命中文件数=0 ⟹ **本档新增** ✓
　技术词 novelty audit       命中文件数=0 ⟹ **本档新增** ✓
　技术词 已知性核验          命中文件数=0 ⟹ **本档新增** ✓
【外部来源（**题录级**）】 `Handbook of Discrete and Computational Geometry` ch.61（rigidity & scene analysis）／ch.62（rigidity of symmetric frameworks）｜
　`Servatius`《Combinatorics and the rigidity of frameworks》｜`Cheng 2014`（3D 刚性拟阵秩估计）｜
　`Schulze–Whiteley 2011`（轨道刚性矩阵）｜`Fowler–Guest`（对称刚性）｜`Nixon–Owen–Power 2012`（曲面刚性 SIAM JDM 26(4)）｜
　`Nixon 2013`（arXiv:1312.1480 曲面上的对称强制刚性）｜`Malestein–Theran`／`Jordán–Kasinitzky–Tanigawa`｜
　`arXiv:2508.11636`（2025 综述）｜`Mihalyko` 学位论文 §7.6（开放问题集）✓
```
