# RH 项目研究宪法（RESEARCH CONSTITUTION）
**四层地图 + 全部 NO-GO + 活路形式定义 + 入口协议**

**建立**：2026-09-10 ｜ 基点：`a0c411f` / `8516c69` ｜ 用途：**任何新想法先分类，再决定是否允许计算**

---
## 第 0 层：使用协议（最重要）

```
新想法出现时的固定动作（顺序不能颠倒）：
  ① 分类：它属于第一层（硬 NO-GO）吗？→ 查 §1 与 §5 禁止表，命中即停
  ② 过筛：是否通过 §3 的 18 条门槛？未过 → 停
  ③ 形式：是否属于 §4 的四种合法形态（L1–L4）之一？不属于 → 停
  ④ 自检：能否通过 §4 的最高级准入协议 A–H？不能 → 停
  ⑤ 纸面否决判据写死 + 一轮预算 → 此时才允许写代码
规则：结论必须标注证据等级；"未找到" ≠ "不存在"；撤回以勘误留档（不静默改写）
```

---
## 第 1 层：硬 NO-GO（有严格反例或已证结构 —— **永不再试**）

| 编号 | 名称 | 关闭强度与来源 |
|---|---|---|
| **N0** | Hilbert–Pólya 直接路线（含一切换名版） | 循环：把零点放进谱定义再证谱实 = RH 重编码 |
| **N10** | A–M 仿射半群 | **已证**：$M_pA_1=A_1^pM_p$ ⟹ $\sigma(p)=p$ ⟹ $G_N=\{1\}$（只需 $A_1$） |
| **N36** | 有限惯性不传输 | **已证**（P28–P33）：有限维负指标**不决定**无限维负指标（moving-edge indeterminacy） |
| **N26** | 形式事实冒充算术事实 | **逻辑严格**：只用半环公理可证的事实（Euclid/Mullin 型）⟹ 任何满足该公理的模型都成立 ⟹ 零模型可复现 |
| **N27** | 用输出熵排除短程序 | **逻辑严格**（AIT vs Shannon）：短程序可生成高复杂度输出 ⟹ "输出信息大"**不能**排除短机制 |
| **N45** | Integrability–Null Pincer | **结构严格**：任何不变量必落两腿之一 —— ①coboundary（可积 ⟹ holonomy 恒为 0）②依赖路径 ⟹ 轨迹的确定性函数 ⟹ 保轨迹的 null 可复现。**两腿皆死** |
| **N42** | CRT 局部–全局原理杀 frustration | **结构严格**：整除/同余型局部约束满足局部–全局原理 ⟹ 解空间可分解 ⟹ 无 frustration ⟹ 无跨尺度刚性 |
| **N20-A** | 边界幺正性 ⇏ 内部共振排除 | **严格反例**：Blaschke 乘积在边界模 1，内部可任意多极点/零点（**本项目唯一严格反例**） |

---
## 第 2 层：结构性关闭（"未找到"型，可被新证据推翻，但需正面反例）

### 2.1 表达式/判据类
```
N1  显式公式重包装（ψ/π/θ/Σx^ρ/ζ'/ζ）        ⟹ zero-side encoding
N2  Weil positivity 及其一切变体（Gram/kernel/trace/能量/test function 重选）
                                                ⟹ 判据，非独立机制
N7  静态算术曲率（A/M transport、radical/product）⟹ coboundary 或有限层局部因子
N8  非交换矩阵 / holonomy（K₂、path dependence、formal relation graph）
                                                ⟹ 随机权重也非零 ⟹ 无算术特异性
N17 AFE / Lagarias–Rains kernel deformation      ⟹ kernel geometry ≠ 新算术刚性
N43 恒等式吸收交互（双曲恒等式恒真）             ⟹ size/product 基底的交互内容被吸收
```

### 2.2 局部算术类
```
N3  Euler 化陷阱（F(nm)=F(n)F(m) / 逐素数叠加）  ⟹ 无跨尺度记忆
N4  加法卷积（含受约束/高阶/加权变体）            ⟹ circle method/singular series 类
N5  CRT / congruence / p-adic-only               ⟹ 局部正确 ≠ 全球谱定位
N6  Euclid / remainder / carry 动力学             ⟹ 算法历史，或历史硬编码
N9  Prime-table / compressed state               ⟹ 读取 ≠ 约束（description ≠ selection）
N46 Arithmetic Null Separation                   ⟹ 若 null 模型可复现 ⟹ 无信号资格
```

### 2.3 统计与数值类
```
N13 "出现 1/2" 即当机制                        ⟹ 观察值 ≠ 结构必然（typical ≠ pointwise）
N37 有限数据/低精度伪结构（stationary 假象、dps=40 伪零点、dps 缓存污染）
N21 L²→L∞ / GUE / 零点间距 / additive energy / 全阶非共振
                                               ⟹ 是 RH 的【精细后果】，【不是】RH 核心 engine
```

### 2.4 高阶与算术几何类
```
N14 Rédei / 三体符号（含 norm/twist/KL/L3/null 各变体）⟹ 高阶耦合 ≠ RH forcing
N15 D* / elliptic / Hecke recursion / Sato–Tate        ⟹ 已有自守统计 ≠ 反向约束 ζ
N19 Arakelov / δ-geometry（Buium）                     ⟹ 自然尺度是 height/log/p-adic，非 √X
N30 尺度族错配（1/4 族 vs 1/2 族；"升级指数"是错误抽象）⟹ 对象不同则典型尺度不同
N31 有限性来源的 √ 不可全局化（特征标正交/Gauss/有限域 Weil）⟹ 无条件 √-正性皆来自有限性
N33 引擎平凡化（Sym²(平凡)=平凡）                      ⟹ Kim–Sarnak 型引擎对 ζ 【无内容】
N34 无增益原理（GRH ⊇ ζ 的 RH）                        ⟹ 高阶陈述【包含】而非外部约束 GL(1)
N40 因子化后重新编码（ζ_K=∏L(s,χ)）                    ⟹ 由伴随因子反推 ζ = 换编码
```

### 2.5 流与载体类
```
N11 M-TOWER / inverse limit                      ⟹ 容器 ≠ 分支选择（detection ≠ selection）
N16 谱流 / C-flow / moving edge                  ⟹ 流隐喻 ≠ 动力学定理；终点即编码
N23 ⑰–⑳ 四步形成的边界                            ⟹ 现有散射 machinery ⟹ 无 RH locking
N28 对象混淆（Selberg zeta 零点 ≠ 散射共振 ≠ ζ 零点；GL(n) L ≠ ζ）
                                                 ⟹ 跨对象搬定理必须给映射
```

### 2.6 正性与对称类
```
N29 测试函数变量的正性【位置盲】（谱侧正性 = Parseval/L² 范数 ⟹ 不含 (Re ρ−1/2)²）
    子条：吸收谱/共振 ≠ 自伴谱（无实性定理可用）
N39 β 盲核 ⟺ 无条件 / β 敏感 ⟺ 条件性         （kernel 级筛选规则）
N41 三个 ½ 必须区分：代数中点 / 函数方程中心 / RH 刚性
N22 P-Lock 修正：不得要求 C=M=W（char 0 反例：PS/Selberg/Ramanujan）⟹ 用 Φ(C,M,W)=0
```

---
## 第 3 层：允许探索，但必须满足的边界

### 3.1 十八条门槛
```
P1″ 具体位置约束 ｜ P0′ 不读未来 prime label ｜ P-Info 三量分离（须申报信息预算）
P-Type 点式⇏聚合 ｜ P-Phase 须携带相位信息 ｜ P-Basis 申报基底(同余型淘汰)+误差家族
P-Exponent A/B/C/D（仅 C 可继续）｜ P-Dual 申报自对偶类别（(b)(c) 淘汰）
P-Scale 申报阳性尺度类型（height/log 淘汰）｜ P-Diag 申报对角尺度（须 X 级）
P-SqrtPos 正性须独立于零点 ｜ P-Lock* 申报 Φ(C,M,W) ｜
P-Basis-2 非同余基底须申报误差族（1/4 or 1/2）｜
A_min 四要素齐备（整性+对偶+独立阳性+共轭同步）
非循环性 ｜ 非 zero-encoding ｜ 非重包装（不得 ≡ 显式公式/迹公式/已知判据）
```

### 3.2 数值与流程纪律
```
数值卫生：中间量按工作精度缓存 → 每值附 dps 稳定性证书 → 接近底噪不算证据
           "区间内有零点" ≠ "第一个零点"；"数值建立" ≠ "无限维定理"
流程纪律：纸面否决判据先写死；一轮预算；触发即关闭；不得改换名字续命
留档纪律：撤回以【勘误】形式留在原文档（不静默改写）
对象纪律：跨对象结论必须给出显式映射，否则视为 N28
```

### 3.3 可复用资产
```
AFE 认证计算器：Ξ_w(t)=s(s−w)/(4w)Φ_w(s)，Φ_w=S₁+S₂+2/(s−w)−2/s（精确）
  w=1 五高度 ≤1e−43；与直接积分逐位一致；省 ~35 位；可达 t≈300–400
N_w(T) 计数框架 ｜ 一致性工具（rank 检验、telescoping 验证、pincer 检验）
```

---
## 第 4 层：什么正式算"活路"

### 4.1 最高级准入协议（A–H，全过才写代码）
```
A 独立载体   : 𝒳 在 ζ 零点未知时即可定义
B 内生动力学 : T_t: 𝒳→𝒳，来自 𝒳 自身结构（非人为定义后让谱"看起来像"ζ）
C 三重尺度锁 : Φ(C,M,W)=0，且必须解释 W ~ X^{1/2} 为何必然
D 独立正性   : 𝒫(𝒳) ≥ 0（非仅对称 s↔1−s）
E 参数作用   : 𝒫 必须直接约束谱/共振【位置】（不能只在测试函数变量上）
F 非循环     : ¬RH、¬零点位置、¬Weil、¬HP、¬zero encoding
G 非重包装   : ≢ 显式公式 / 迹公式 / 已知判据
H 选择性     : β≠1/2 必须被独立机制排除（description ≠ selection）
```

### 4.2 仅有的四种合法结构形态
```
L1 新型 char-0 三重锁载体
   𝒳_char0 使 C↔M↔W 锁定，且 ζ = 其自然 boundary/invariant（当前最干净主线）
L2 非自伴谱刚性（唯一纯数学残差）
   A≠A* 但 𝒫(A)≥0 ⟹ Re Spec_res(A) ⊂ {1/2}
   下一步=文献审计：numerical range / dissipativity / Krein-Pontryagin /
                    J-self-adjointness / resonance positivity
   唯一问题：是否存在【独立于自伴化】又能把共振锁到竖直线上的定理？无 ⟹ 一次性封死
L3 边界—内部锁定
   离散自伴扇区 ⟹ 散射/共振扇区（且不是迹公式/显式公式的重新编码）
L4 非标准 char-0 几何载体
   𝒳 ≠ Spec ℤ，甚至非传统算术簇；但必须同时具备
   算术意义 + 内生动力学 + 对偶结构 + 独立正性
```

### 4.3 禁止重复表（新想法 → 第一反应）
```
"谱就是零点的算子" ❌ N0 ｜"新的 quadratic form 正性" ❌ N2
"新的 kernel" ❌ N1/N2 ｜"新的 prime invariant" ❌ N3/N46
"高阶三体/四体符号" ❌ N14 ｜"noncommutative curvature" ❌ N8
"arithmetic flow" ❌ N11/N16 ｜"新的零点 phase statistic" ❌ N21
"数值接近 1/2" ❌ N13 ｜"p-adic / Frobenius lift" ❌ N19
"Arakelov height" ❌ N19 ｜"higher-rank automorphic" ❌ N15/N34
"scattering is unitary" ❌ N20-A ｜"functional equation gives symmetry" ❌ N41
"Parseval is positive" ❌ N29 ｜"trace formula gives positivity" ❌ N29
"make scattering self-adjoint" ❌ N0 ｜"compress prime table" ❌ N9
"只用半环公理可证的事实" ❌ N26 ｜"输出信息量大" ❌ N27
"跨对象搬定理（同形不同对象）" ❌ N28 ｜"用恒等式当约束" ❌ N43
```

---
## 附录：本次新增的 15 条 NO-GO（N25–N46，唐先生原表未列）

| 编号 | 名称 | 陈述（一句） | 来源 | 证据等级 |
|---|---|---|---|---|
| N25 | 恒真判据 | 判据若对**任意**输入成立则无判别力（C2 原版被唯一分解恒真化） | ⑯关前后 | 逻辑严格 |
| N26 | 形式事实冒充算术 | 仅由半环公理可证的事实不可承载算术刚性 | Euclid/Mullin 检验 | 逻辑严格 |
| N27 | 输出熵 ≠ 生成复杂度 | 短程序可生成高复杂度输出（AIT vs Shannon） | FPCA 撤回 | 逻辑严格 |
| N28 | 对象混淆 | Selberg zeta ≠ 散射共振 ≠ ζ；跨对象搬定理须给映射 | ⑲⑳关 | 方法学 |
| N29 | 测试函数变量的正性位置盲 | 谱侧正性 = Parseval/L² 范数 ⟹ 无 (Reρ−1/2)²；共振非自伴谱无实性定理 | ⑳关（第二次总封口） | 结构性 |
| N30 | 尺度族错配 | 不同对象典型尺度不同；"升级指数"是错误抽象 | Exponent-Bridge | 结构性 |
| N31 | 有限性来源的 √ | char 0 无条件 √-正性皆来自有限性，不可全局化 | G13 | 结构性 |
| N33 | 引擎平凡化 | Sym²(平凡)=平凡 ⟹ 该引擎对 ζ 无内容 | G17 | 结构严格 |
| N34 | 无增益原理 | 高阶族陈述【包含】ζ 的 RH ⟹ 非外部约束 | G18 | 结构性 |
| N36 | 有限惯性不传输 | 有限维负指标不决定无限维负指标（**已证**） | P28–P33 | **已证** |
| N37 | 有限数据/低精度伪结构 | stationary 假象、dps=40 伪零点、缓存污染 | 本阶段多次 | 经验严格 |
| N39 | β 盲 ⟺ 无条件 | β 盲核只能无条件；β 敏感必条件性 | Lamzouri 族 | 文献级 |
| N40 | 因子化后重编码 | ζ_K=∏L(s,χ)；由伴随因子反推 ζ = 换编码 | G18 | 结构性 |
| N41 | 三个 ½ | 代数中点 / 函数方程中心 / RH 刚性必须区分 | 早期 | 结构性 |
| N45 | Integrability–Null Pincer | 不变量必落 coboundary / 轨迹确定性函数两腿之一，皆死 | 本阶段 | 结构严格 |
| N46 | Arithmetic Null Separation | null 能复现 ⟹ 无信号资格（"非零/三体/非交换"永久失去资格） | T4 | 方法学门槛 |

---
## 一句话总结（全部关卡的压缩）

$$\boxed{\text{RH 需要 }1/2\text{ 的\textbf{选择性}（非尺度）；需要\textbf{独立}约束（非对偶对称）；}\\
\text{需要\textbf{全球}锁定（非局部算术）；需要载体\textbf{自身动力学}（非描述）；}\\
\text{需要作用于零点/共振参数\textbf{位置}的刚性（非测试函数正性）}}$$

$$\boxed{\text{char 0}\ \overset{?}{\longrightarrow}\ \underbrace{\text{三重尺度锁}}_{C,M,W}\
\overset{?}{\longrightarrow}\ \underbrace{\text{非自伴位置刚性}}_{\Re\rho=1/2}}$$

---
## 附加：宪法修正案 1 的两条最高原则（2026-09-10，唐先生）

$$\boxed{\textbf{没有通过 L3，不允许称为“RH 活路”；没有通过 L4，不允许称为“RH 证明路线”。}}$$

$$\boxed{\textbf{下一阶段的成功标准不是“更大胆”，而是：第一次有对象【通过】本宪法，而不是我们修宪法去容纳它。}}$$

（分级细节、META-NO-GO、L0–L4 阶梯、退出条件、决策树 → 见 `CONSTITUTION-AMENDMENT-1-grading.md`）

---
## 修正案 2（2026-09-10，宪法证伪测试产物）

### N29 范围修正（**重要**）
```
原文："测试函数变量的正性【位置盲】"——过宽，会连带否掉【比例/密度通道】
修正为双通道：
  ① 比例/密度通道：测试函数正性【无条件有效】（已知前沿：Lamzouri 2/3、
     零点在线比例纪录 67.25%、Kim–Sarnak 975/4096）
  ② 钉住通道（pinning）：位置盲，关闭
⟹ 缺口精确表述为"比例 → 全部"（proportion → all），而非"正性无用"
```

### 新增 Discovery Track（D0–D4）——**不是第五条活路，不得称 RH 活路**
```
D0 对象新颖性：𝒳 非已知 RH 对象重命名
D1 独立自由度：q_new ∉ closure(N0–N46)
D2 内生关系  ：R(q_new, C, M, W)=0
D3 位置接口  ：明确 q_new → B(λ) → Re λ（含糊不算；允许"尚未建立"）
D4 null 检验 ：换成 random/CRT/coboundary/形式半环/测试函数正性后仍成立 ⟹ 关闭
两轨：Discovery(D0–D4) ∥ Proof(A–H → L0–L4)；真活路须两轨皆过
```

### KPI 与冻结触发
```
① 每轮审计须报告"进入 Discovery 后新增的数学自由度数"
② 连续 3 轮产生 0 个 D0–D4 受理 ⟹ 不是候选变差，而是【搜索空间选错】⟹ 停止修剪，重设坐标系
```

### 登记候选（Discovery 级）
```
C-BC：Bost–Connes 系统 / KMS–Tomita–Takesaki 模结构载体
  状态：**Discovery 级，D3（位置接口）待审计**；预期为 β 墙的另一实例，但未审计不得假定
```

---
## §6 残差问题登记簿（R-Registry）—— 与 NO-GO 表【平级】

**设立理由**（2026-09-10）：掉坑的深层原因不是想法差，而是每次关闭**只记录"什么死了"，没记录"还剩下什么精确问题"**。
$$oxed{	ext{白区应随关闭而【单调收窄】，而不是反复原地立碑}}$$

### 规则（硬性）
$$oxed{	ext{每次关闭一条路线，必须同时产出或更新至少一条 R 问题；}\
	ext{没有产出 R 的关闭视为【不完整关闭】}}$$

### 登记表

| # | 残差问题 | 来源 | 攻击方式 |
|---|---|---|---|
| **R1** | 算术算子的 J-非负性是否可能 **β-盲**，或条件来源合法 | L2 × N39 | Krein/Langer 文献审计 + 尝试构造 |
| **R2** | 是否存在**非迹公式型**的边界–内部锁定定理 | L3 | 表述成精确数学问题存档，低频关注；不作为可探索空间 |
| **R3** | 什么装置能在 char-0 中产生 **√ 尺度正性** | LIVE-5 锐化 | 函数域链条逐步剥离已给出半张答案（缺 finite type 的 char-0 替身） |
| **R4** | β-敏感的**正性构造**是否存在（N39 的另一半） | N39 | 随 R1 一并审 |

### 附：L2/L1 的锐化表述（本轮定稿，替代此前的模糊表述）
```
R1（锐化）：是否存在算子 A，使
   (i) det(s−A) 型不变量给出 ζ（或 Ξ）；
   (ii) A−½ 是 J-自伴的；
   (iii) J-非负性可在【不引用零点、且不等价于 Weil 判据】的前提下被验证？
⟹ 咽喉是 (iii)：若其验证只作用于【测试函数变量】⟹ Weil 正性（N2/N29）
   按 N39 分类：β-盲 ⟹ 要么无条件可证（=大定理）要么可被反例击穿；β-敏感 ⟹ 必须申报条件来源
⟹ 即：L2 的全部内容 = 寻找 β-盲或条件来源合法的 J-非负结构
```
```
R3（锐化）：√X 是 X 与 1 的【几何中点】；任何把尺度 X 与其对偶尺度对合交换的结构，
   其不动点在对数尺度下为 0，即 X^{1/2}。而函数方程 s↔1−s 正是这样一个尺度对合
⟹ LIVE-5 重写为：寻找 char-0 对象 𝒳，自带【非循环的尺度对合】（Poisson 对合式，如 θ 变换 /
   Tate adelic 对偶），使 ζ 作为其行列式/特征不变量自然出现，且该对合不动点为 X^{1/2}
⟹ 搜索目标从"找 √X 机制"收窄为"找正确的尺度对合载体"
已知：对偶腿有真实内容（Tate / Deninger foliated spaces / 算术拓扑 Morishita）；
      正性腿全灭（N31：char-0 无条件 √-正性皆来自有限性）
⟹ L1 的生产性问题不是"选哪个纲领"，而是"什么数学装置能在 char-0 产生 √ 尺度正性"
```

### 状态定性（唐先生本轮确认）
```
L2 非自伴谱刚性  : ★ 唯一有【现成定理机制】可审的残差（Krein/Langer 家族存在真定理）
L1 char-0 三重锁 : 正确长期目标，但当前【无载体通过 P-Scale】——缺的是尚不存在的数学装置
L3 边界–内部锁定 : 是【目标】不是【领土】；已知边界–内部关系（Levinson、Birman–Krein、
                   Regge/复标定、Pavlov spectral singularities）全部是 trace/相移型 = N1/G 领土
L4 非标准载体    : = L1 + 额外语义风险 − 额外约束 ⟹ 不建议单独作为入口
```

### 执行顺序（已定，按序，不并行）
```
① 审计 A：de Branges 框架（协议见 PROTOCOL-R-A1-de-branges-audit.md）——1 轮，纸面
② 审计 B：Connes 谱实现（1998）——验证宪法对 N29 的【预言】，校准宪法
③ R1 文献扫描：Azizov–Iokhvidov 框架定理 + Znojil quasi-Hermitian 技术清单
   ⟹ 列出"J-非负性已被验证的所有具体算子"及其【验证输入形态】，
      再对照"是否存在算术可供给的输入形态"
```

### §6.1 R-Registry 更新（审计 A 后，2026-09-10）

**R4 更新（de Branges 收割）**：de Branges 三公理 = 已知的"空间正性 ⟹ 零点实性"**严格已发表机制**。
锐化后的问题：
> **能否用一个【独立于 Ξ】的算术对象实例化 de Branges 三公理？**
> 若能，RH 由结构定理自动成立；"三公理的算术可供给性"成为新的审计对象。

**R1 关联注记**：两个模板**互补**，R1 扫描时须并列表格对照：
```
de Branges 模板 : 正性在【空间公理】层（差商等距不变性）
Krein/Langer 模板: 正性在【算子不等式】层（J-非负性 [Hx,x]≥0）
```
**共同限制（须记录）**：de Branges 在 H(E) 中乘法算子**本身自伴**（典范系统理论要点）
⟹ **未打破自伴性墙**，只是把困难**搬迁**到空间构造 ⟹ 它给的是 **L2 的精确模板**，不是 L2 的解。

### §6.2 审计记录索引
```
审计 A : docs/R-A1-de-branges-audit.md —— 关闭（K2+K3 双触发）；K5 收割入 R4；校准【通过】
审计 B : 待执行（Connes 1998 谱实现；验证 N29 预言）
R1 扫描: 待执行（Azizov–Iokhvidov + Znojil；两模板并行对照表）
```

---
## §6.3 价值提取产物登记（V1–V4，2026-09-10，唐先生）

> **方法**：把语料从"墓碑清单"**逆变成"规格说明书"**——每条 NO-GO 杀掉缺某性质的对象族，
> 全部杀掉的**交集**就是活对象的**必要规格**；规格本身可成为一个新的数学对象定义。

### ⭐ 最重要单条提取：Levinson–Conrey = 唯一已知 β-敏感排除标本
```
性质：**β-敏感且位置作用**——断言"≥2/5 的零点在临界线上"（Conrey 1989，文献级）
      无条件定理，不假设 RH，直接**排除**一部分离线零点
      这是全部数学中唯一做到这一点的机制；其余一切正性（Weil/显式公式/Parseval）皆 β-盲
屏障：Levinson 方法要求 mollifier 长度 ≤ T^{1/2}
      原因不是技术性的——**mollifier 一旦超过 √T，它自己就开始探测它要排除的离线零点，方法自我击败**
```
$$oxed{	ext{宪法 LIVE-5 要求活对象内生解释 }W\sim\sqrt X;\ 	ext{而唯一成功的 β-敏感方法恰撞在 }\sqrt T	ext{ 墙上}}$$
$$oxed{	ext{⟹ }W\sim\sqrt X\ 	ext{不是本项目的特殊要求，而是 β-敏感排除机制在算术上自给时的【必然墙壁】}}$$
**两条独立推导收敛到同一尺度** ⟹ R3 获得一座桥（mollifier 屏障 ≡ 尺度对合不动点）。

### V1 活对象规格说明书（P-对象定义）
```
活对象 = β-敏感 ∩ 位置作用 ∩ √X 对角 ∩ char-0 供给 ∩ 非 coboundary ∩ 非局部 ∩ 非零编码
每项 = 一条 NO-GO 的逆 ⟹ 本 spec 本身是可引用的新数学定义（未来想法直接对表打分）
```

### V2 β-敏感无条件工具箱普查
```
已知 β-敏感且无条件的技术仅三样：
  ① Levinson–Conrey 型排除  ② zero-density 估计（Ingham–Jutila；Guth–Maynard 2024 有推进）
  ③（无）
⟹ 普查本身给出观察：任何新方法必落此三类的推广，否则即是新品
```

### V3 N39 升级为定理
```
"β-盲 ⟺ 无条件 / β-敏感 ⟺ 条件性" 目前是文献级观察
在核族上抽象形式化 ≈ 1–2 页可完成的真定理 ⟹ 值得做
价值：使宪法最锋利的一条过滤器变成【可引用的引理】
```

### V4 模型问题纲领（新 R5）
```
L2 的引擎不应先在 ζ 上试，而应在【同类但更便宜】的 char-0 谱刚性问题上试：
  · Selberg 特征值猜想 λ₁ ≥ 1/4（最好已知 1/4 − (7/64)²，纯 char-0、无有限型输入、未解决）
  · 算术双曲曲面的共振隙问题
⟹ 谁先在非 RH 问题上造出"无有限型输入的位置刚性"引擎，谁就拿到 L2 的钥匙；成败不赌在 RH 上
```

### 突破点排序（唐先生 commit）
$$\boxed{\text{构造第一个"β-敏感 + 位置作用 + √X 对角"的正性项——或证明它不存在}}$$
```
实入口（桥接）：Levinson √T 屏障 ← 当作对合不动点研究（V2 / R3）
                有文献、有已知失败模式、每次失败都精确标注缺哪条输入
虚入口（训练场）：Selberg 1/4（V4 / R5）——先造引擎，再上 ζ
审计 B（Connes）：**降级为低优先**（审计 A 已校准宪法，B 只是第二份确认；
                 而 V2 是第一次正向进攻，且纸面可做）
```

### §6.4 执行顺序（更新）
```
① V2：Levinson √T 屏障分析（协议：PROTOCOL-V2-levinson-barrier.md）——1 轮，纸面
② V4 / R5：Selberg 1/4 引擎（训练场，低频）
③ R1 扫描：Azizov–Iokhvidov + Znojil（两模板并列对照：空间公理层 vs 算子不等式层）
④ 审计 B：Connes 1998（低优先）
```

### §6.5 登记册内部不一致（必须追根，T3/N37）
```
本登记册另处记"零点在线比例纪录 67.25%"；而解析数论传统记录约在 5/12≈41.7% 量级
⟹ **两者不符，必须追根**；在追根完成前【禁止引用该数支撑任何判定】
```

---
# §7 价值提取层（Value-Extraction Layer）

**入宪日期**：2026-09-10 ｜ 提案：唐先生 ｜ **已按 R-A2 审计结果修正** ｜ 基线：`d18cde2`

### 提取原理
$$\boxed{\text{每条 NO-GO 杀掉一个缺某性质的物体族；全部杀掉的交集 = 活对象的必要规格}}$$
$$\boxed{\text{规则：每条 NO-GO 须登记其【逆命题】（规格项）；未登记逆的关闭视为【不完整关闭}}}$$
（与 §6 R-Registry 规则并立：R 登记"还剩什么问题"，§7 登记"活对象须具备什么性质"）

## §7.1 标本：β-敏感排除机制（**两条支线**，非一条）

> ⚠️ **修正（R-A2）**：原提案称"Levinson–Conrey 是唯一 β-敏感标本"——**已修正为两条支线**。

```
支线甲（mollifier / Levinson 谱系）
   Hardy 1914 → Selberg 1942 → Levinson 1974 (1/3) → Conrey 1989 (2/5)
   → Bui–Conrey–Young 2011 / Feng 2012 / PRZZ 2020
   ⟹ 记录 **5/12 ≈ 41.67%**（2020 起未再推进）
   屏（原以为）：mollifier 长度 ≤ T^{1/2}
   ⚠️ 已推翻：Conrey–Levinson 型可达 θ = 4/7 − ε（PRZZ 原文：θ 从 6/11 推至 4/7）；
      Kintali 2026-08 用 T^{29/50}；2025 年工作更证明【任意短】mollifier 亦给正比例
      （原文：opposite to "the common belief"）⟹ **θ=1/2 不是硬墙**

支线乙（pair-correlation 谱系，2026）★ 更强
   Montgomery 1973（RH 下 ≥2/3 单零点）→ 2026：把 pair-correlation 推论【无条件化】
   ⟹ 记录 **> 2/3 ≈ 67.2%**（计数为【互异】零点，非"单零点"）
   ⟹ 同机制亦证全部零点的 ≥ 5/6 互异
   **自我申报硬顶：0.68185**——由 **λ ≤ 1 的一次/二次矩信息**所致
   **量化梯度**：0.70/0.80/0.90 需 support ≈ 1.04/1.26/1.70 ⟹ 需【真正新的算术输入】
```

## §7.2 ⭐ 真正屏障（替换 √T）：support 边界 λ = 1
```
· 无条件可算：support λ < 1
· RH 强度：support λ ≥ 2（1-level density 经典门槛）
⟹ **λ = 1 恰是 [0, 2] 的中点**——本项目"½ 结构"以【support 中点】形式再现
⟹ "比例 → 全部"的缺口被【量化】：达 1 需 λ → ∞（= 完整零点侧输入）
```

## §7.3 规格说明书 V1（P-对象定义）
```
P-对象 ≔ β-敏感 ∩ 位置作用 ∩ √X 对角 ∩ char-0 供给 ∩ 非 coboundary ∩ 非局部 ∩ 非零编码
（每项 = 一条 NO-GO 的逆；用途：直接对表打分，替代逐条回忆 46 条 NO-GO）
```

## §7.4 工具箱普查 V2（**已修正**）
```
β-敏感且无条件的技术为【两类】：
  ① mollifier/Levinson 谱系（甲）——记录 5/12；θ 可 > 1/2
  ② pair-correlation 谱系（乙）——记录 2/3；硬顶 0.68185（λ ≤ 1 信息类）
  ③ zero-density 估计（Ingham–Jutila；Guth–Maynard 2024）——第三类，性质待厘清
⟹ 普查结论须改为：任何新方法必落此三类的推广，否则即新品
```

## §7.5 V3：N39 升级为定理
```
"β-盲 ⟺ 无条件 / β-敏感 ⟺ 条件性"现为文献级观察；
在核族上抽象形式化（约 1–2 页）⟹ 使宪法最锋利过滤器成为【可引用引理】。可直接立项。
```

## §7.6 V4 / R5：模型问题纲领（训练场）
```
Selberg 特征值猜想 λ₁ ≥ 1/4（已知 1/4 − (7/64)²；纯 char-0、无有限型输入、未解决）
算术双曲曲面共振隙问题
⟹ 谁先在非 RH 问题上造出"无有限型输入的位置刚性"引擎，谁即拿到 L2 钥匙；成败不赌在 RH
```

## §7.7 F1 几何收敛（推导，非偏好）
```
N10（G_N={1}）＋N42（CRT 杀 frustration）＋ Spec ℤ 的 étale 基本群平凡（Minkowski，经典）
⟹ 三条独立推出同一障碍：Spec ℤ 无覆叠/无单值化/无 Galois 式 holonomy
⟹ 活对象必须生活在这些障碍不成立的范畴；已知唯一候选 = 𝔽₁ 型几何
⟹ L1/L4 从"四种形态之一"升级为【消去法剩下的唯一范畴】
```

## §7.8 突破点排序（修正后）
$$\boxed{\text{构造第一个"β-敏感 + 位置作用 + √X 对角"的正性项——或证明它不存在}}$$
```
实入口（改锚后）：support λ = 1 → λ ≥ 2 的跨越（原"mollifier √T"锚点已失效）
虚入口（训练场）：Selberg 1/4（V4/R5）
审计 B（Connes）：低优先
```

---
## §8 Discovery 轮次登记（Discovery Rounds）

### §8.1 记账口径（**本轮固定，防止静默漂移**）
$$\boxed{\text{口径 = 连续 D1=0 轮数}；\ 连续 3 轮 D1=0 ⟹ 触发"冻结修剪 / 重设坐标系"}}$$
```
Round 1 : C-BC（Bost–Connes/KMS–模结构）—— D0–D2 ✓，D1 ✓（新自由度 = KMS 态空间 + 模结构），D3 ✗
          ⟹ 是"受理后逐层关闭"，**不计入 D1=0**
Round 2 : 双滤过算术耦合 —— **D1 = 0**（本轮）⟹ 计数 1/3，freeze = NO
```

### §8.2 Discovery Round 2 记录：双滤过算术耦合 ⟹ D1 = 0
```
命题：研究 P_A(Y)P_M(X)P_A(X) 型【跨尺度重构算子】，期望平衡律 Y²≍X 内生导出 √X

两条结构发现：
① 字面 σ-代数读法【退化】：𝒜_X = ℳ_X = 2^[1,X]（生成元含全部单点）
   ⟹ [P_A,P_M]=0，ℛ=identity ⟹ 内容不可能来自条件期望层，
      必须来自【受限计算类】（加法=区间/Fourier；乘法=除数/Dirichlet）
② 替换后的【自然形式化】滑入已关闭的经典对象：
   交替截断投影 = "截断 Dirichlet 级数在加法坐标求值" = **Dirichlet 双曲线对象**
   · 平衡尺度 Y = √X 已知（双曲线法，1849）⟹ **√X 是经典输入，不是内生平衡点**
   · 不对称缺陷 D(X,Y) = **除数问题误差 Δ(X)** ⟹ 猜 O(X^{1/4+ε}) = **1/4 族**
   ⟹ ℛ ∈ closure(N43 双曲恒等式 / N30 尺度族错配 / G7–G8 Exponent-Bridge 已关闭)

裁决：**D1 = 0**（不通过第一关）
   —— 不是"证明该方向为死"，而是"针对自然形式化，落入已关闭对象"
   —— 不算 N47；不使用 C-BC 残骸
```

### §8.3 ⭐ 本轮保留的【形式判据】（不是机制）
$$\boxed{\text{½ 应作为【平衡点/中点】出现——此形式与 V2 查到的已发表最锋利屏障一致}}$$
```
· 无条件范围 support λ < 1 ｜ RH 强度 λ ≥ 2 ⟹ **λ = 1 恰为 [0,2] 中点**
· 硬天花板 0.68185（仅用 λ ≤ 1 矩信息）
⟹ 提案【方向正确，实现被经典对象吸收】——这是本轮最重要的区分
⟹ 记为 §7.2 的【形式要求】：未来候选若声称"√X 是平衡点"，必须证明该平衡点
   【不是】双曲线/自对偶截断的引用（否则按本记录直接归入 D1=0）
```

### §8.4 Round 2 留下一扇门（须显式满足四条件才可重开）
```
① 不落入"截断 Dirichlet 级数在加法坐标求值"（= 双曲线/除数对象）
② 有【确定性】operator identity（非能量/相关/统计）
③ 平衡点 Y²=X 【由该 identity 导出】，而非引用经典双曲线
④ 有不可由对称性消除的方向性缺陷（否则 N41）
```

### §8.5 Discovery Round 3 记录：算术跨尺度演化的内生记忆 ⟹ **D1 = 0**（计数 2/3）

**本轮禁令已遵守**：未引入 RH / ζ / 零点 / 谱算子；**未预设 √X、未预设 1/2**。

**核心产出（概念性，非"又死一条"）**：
$$\boxed{\text{"未来不被过去决定"（ignorance）}\ \neq\ \text{"不可压缩的记忆"（memory）}}$$
```
Round 2 的教训：几何中点 ≠ 选择机制
Round 3 的教训：「过去不含未来信息」≠「不可压缩的记忆」
   —— 前者是问题的【原始困难本身】（素数分布）；后者才是新自由度
   —— 唐先生的判据天然会把前者误读成后者，本轮把这个混淆挡住
```

**三条结构性论证**：
```
① 算术【无内生动力学】：≤Y 的数据是给定的整数本身 ⟹ 𝒮(X)=F(X)
   ⟹ 中间经过哪些尺度对 X₂ 处数据无影响 ⟹ 路径依赖只能来自 observer 压缩
② 一旦有尺度作用（群作用），转移律【自动是 cocycle】：
     σ_{X₀→X₂} = σ_{X₁→X₂}∘σ_{X₀→X₁} ⟹ T = T(X,Y) 与路径无关 ⟹ 记忆为零
   破坏合成律只有两条路：①状态空间随尺度变化（⟹ 联络/和乐，已由 N7/N8 + pincer + carry 关闭）
                        ②转移律非群作用
③ 唐先生判据可被精确回答，并给出【信息边界】：
     n ≤ X² 的合数必有素因子 ≤ X ⟹ Y ≤ X² 时状态充分（同状态⟹同未来，Markovianity 平移成立）
     Y > X² 时状态不决定未来——但那是【无知】，不是【记忆】
   ⟹ **信息边界 Y = X²**
```

**判定表（唐先生杀灭清单）**：coboundary(N45-i) / 轨迹存储(N45-ii) / 有限高阶(N14,N43) /
convolution(N4) / CRT-local(N42) / divisor hyperbola(N43,N30) / 统计记忆(N13,N46) /
非平坦联络和乐(N7,N8,pincer，已关闭) / observer 压缩(N25,N1) / **ignorance（定义不符，不算 D1）**
$$\boxed{\text{⟹ 剩余可存活类别为空集 ⟹ D1 = 0}}$$

**必产 R**：
```
R7【新】：信息边界 Y = X²（"一步"的可判范围）与 R3 的对合不动点 √X
   是否为【同一个 involution 的两面】？即：平方 reach 与自对偶中点是否由同一条算术恒等式锁定？
   若"是" ⟹ R3 所缺 involution 可能从这里供给（须严格建立，不得类比）
   攻击方式：纯算术（+、×、|、≤）先建立 X ↦ X² reach 的 canonical 性，再看其与 x ↦ N/x 型
   对合固定点的关系；不得引入 ζ
```

**账本**：连续 D1=0 = **2/3**，freeze = NO。**再一轮 D1=0 ⟹ 触发冻结程序**
（宪法规定：届时问题从"哪个候选错了"升级为"为什么整个坐标系只能产生已知机制"）。

### §8.6 冻结审计（Freeze / Coordinate-System Audit）执行记录

**触发**：连续 D1=0 达阈值（Round 2、Round 3，本次冻结为第三次事件）｜ **规则**：R7 不作为候选；不产 Round 4 候选；不新增 N47

#### FZ-1 机制生成元审计：**46 条 NO-GO ⟹ 6 个机制 + 6 个筛子**
| 母机制 | 内容 | 代表 N 项 |
|---|---|---|
| M1 表示/编码 | 把 ζ 重写为另一对象 | N0, N1, N11, N16, N36, G17 |
| M2 对偶/自对称 | 对偶给中心不给选择 | N41, N22, G8, N30, N40 |
| M3 正性/能量 | 约束测试函数/能量，不约束位置 | N2, N29, N31, G13/G14, N39 |
| M4 局部算术 | 局部正确 ⇏ 全局耦合 | N5, N42, N6, N3, N46 |
| M5 经典耦合 | 双线性耦合 = 经典恒等式 | N4, N43, N14, N7, N8, N45 |
| M6 外部动力学 | 运动来自我们的坐标选择 | N16, Round 2, Round 3, N11 |

$$\boxed{\text{M1–M3 = 表示/对称化/界定（接触 ζ 的三方式）}；\ \text{M4–M6 = 局部/双线性/运动（构造的三方式）}}$$
$$\boxed{\text{语料 = 一个 } 2\times3=6\ \text{维坐标系的闭包}；\text{独立障碍数} = 6+6 = 12\ \text{（非 46）}}$$

#### FZ-2 未出现原语审计：**不提供逃生口**
```
唯一实质未覆盖：free probability / microstates / 非交换熵
   ⟹ 预判被同一吸收机制吞掉（邻接已审的 Connes 吸收谱 + 随机矩阵统计）
inverse problem  ⟹ 循环（N0 邻域）
definability    ⟹ 方法论边界，不产机制（§3 P-Type 已收）
nonstandard     ⟹ 无算术内容入口
（严格执行唐先生陷阱警告："未研究过" ≠ D1）
```

#### FZ-3 ⭐⭐ 核心发现：单一生 成机制 = **Canonical–Information Dichotomy**
$$\boxed{\text{canonical 可定义} \Longrightarrow \text{信息不足（β 盲）}；\quad \text{信息充分} \Longrightarrow \text{循环}}$$
```
① 可从算术 canonical 定义的结构（局部/双线性/对称/正性/群作用）⟹ 信息量有上界
   ⟹ 只能到聚合/比例/能量层 ⟹ 给不出位置选择（= N29/N39 的抽象形式）
② 携带零点位置信息的结构（显式公式/谱编码/缠绕 ζ）⟹ 立即循环（N1/N0）
⟹ **这就是 M1–M6 全部闭包的共同生成元** = 项目自第一日起撞的 β-墙（Rigidity Gap）的本质形式
⟹ 解释了唐先生的"经典吸附性"元现象：不是候选差，而是二分在起作用
```
**对本体论问题（"是否把真正的 arithmetic object 投影掉"）的裁决**：
```
不是坐标伪影，而是【信息量事实】：选择所需输入的信息量不低于零点位置本身，
而 canonical 可定义机制的 信息量 更少 ⟹ 无法选择
⟹ 推翻它须给出【canonical 且携带位置内容】的结构 —— 那才是真正的坐标系跃迁
```

#### FZ-4 R7 考古：**识别成立，但共同结构 = Dirichlet 双曲线 ⟹ R7 关闭**
```
Y = X²（因子分解完备性）与 x↦N/x（除数配对）确为【同一 involution 的两面】
   共同生成律 = 除数/卷积配对（n = d·e 限制在 [1,X]² ⟹ n ≤ X²；自对偶中点 = √(X²) = X）
⟹ 但该共同结构【正是 Dirichlet 双曲线对象】= N43（Round 2 已关闭）
⟹ 收益 = 已被关闭的 N43 ⟹ **R7 关闭**（按规则：证明不了即关闭；证明了却落入已知也关闭）
```

#### 冻结结论
$$\boxed{\text{不是"还没找到好模型"，而是坐标系的可允许结构被【二分】限定}}$$
$$\boxed{\text{真正的坐标系跃迁须提供【同时 canonical 且携带零点位置内容】的结构}}$$

### §8.7 FZ-5：Canonical Position-Bearing Audit 执行记录

**问题**：能否存在一个不编码零点、完全 canonical 的算术构造，其内部刚性能够区分复参数的实部位置？
**四门**：C1 canonical ｜ C2 non-encoding ｜ C3 independent rigidity ｜ C4 positional discrimination

#### ⭐ 三条修正（推翻 FZ-3 的隐含假设）

**修正 1：canonical 且位置承载的对象【存在】**
$$W_0:=\ x\mapsto \psi(x)-x=\sum_{n\le x}\Lambda(n)-x$$
```
canonical ✓（Λ 由素数/乘法结构定义）；位置承载 ✓（振荡由零点支配：ψ(x)−x ~ −Σ_ρ x^ρ/ρ）
⟹ **"canonical ⟹ 给不出位置信息"是错的**
真正的障碍是：canonical 对象的位置内容与 ζ 零点【互相定义】
⟹ 从 W_0 读出位置必经显式公式 ⟹ 读的就是零点本身，无独立杠杆
即：【位置承载不是问题，位置的独立来源才是问题】
```

**修正 2：判据不是 entropy，也不是 discrimination，而是【独立性】**
```
唐先生 W(x)=0 反例正确：低信息熵 ⇏ 低位置区分力
但对偶失效同样存在：位置内容"相同"⇏ 可用（等价 ⟹ 读的就是零点）
⟹ C2 必须从 non-encoding 强化为 **C2′ non-equivalent（不与显式公式互相定义）**
```

**修正 3：三层结构替换 FZ-3 的二分**
| 层 | 位置内容 | 实例 | 状态 |
|---|---|---|---|
| **L0** | 无（β 盲） | M1–M6 绝大多数 | 已关闭 |
| **L1** | **低于显式公式但仍能约束** | **Levinson（5/12）｜pair-correlation（2/3）** | ★ **非空 = 唯一有产出层** |
| **L2** | 完整（与目标互相定义） | ψ−x、显式公式 | 循环（N1） |

$$\boxed{\text{真实缺口 = L1 → L2，且已量化：support }\lambda\le1\ \Longrightarrow\ \text{比例}\le0.68185\text{；L2 强度需 }\lambda\ge2}$$

#### 四门裁决
```
C1 canonical ✓ ｜ C2 non-encoding ✓ ｜ C2′ non-equivalent ✓ ｜ C3 independent ✓
C4 positional discrimination：**比例层 ✓（确实排除部分离线零点）｜钉住层 ✗（受 λ ≤ 1 限制）**
⟹ **FZ-5 Outcome A 非空**：canonical ∧ non-encoding ∧ independent ∧ position-constraining 已存在
```

#### ⭐ FZ-3″（上修版，可证伪）
$$\boxed{\text{canonical 非等价构造的位置约束【只能通过矩/支撑信息】起作用；}\
\text{无条件素数侧只给 }\lambda\le1\text{，钉住需 }\lambda\ge2}$$
$$\boxed{\text{开放可证伪问题：}\lambda\le1\ \text{是【结构天花板】还是【当前方法的天花板】？}}$$
```
⟹ 这正是 V2 审计登记的 **R6** ⟹ R6 由候选问题升格为【唯一活跃的中心问题】
理由：① 不是 RH 本身，而是信息类陈述（可独立攻击）
     ② 有文献抓手（1-level density / support 理论 / λ≤1 与 λ≥2 经典门槛）
     ③ 可证伪：证明 λ≤1 为结构天花板 ⟹ FZ-3 升格为定理，且【那时才该做坐标系跃迁】
               证明 λ=1 可越 ⟹ **第一次出现 canonical ∧ 位置钉住 的入口**
```

#### 对"是否该做坐标系跃迁"的裁决
```
**现在还不该**：L1 非空 ⟹ 坐标系并未失效，只是当前产出停在比例层
跃迁的理由要等 λ ≤ 1 被证明为结构天花板之后
```

### §8.8 R6 升格为中心问题 + 协议就绪（FZ-5 出口）

$$\boxed{\text{R6：}\lambda=1\ \text{是【结构常数】还是【技术常数】？}}$$
```
来源：FZ-5 把"canonical 能否位置承载"（答案：能，在 L1 层）锐化为
      "L1 的天花板 λ ≤ 1 是否为结构性的"
协议：docs/PROTOCOL-R6-support-ceiling.md（§0 格式；1 轮纸面；不写代码/不做数值）
```

**协议结构（唐先生六关 + 我加两处）**：
```
Gate 1  定义干净化 —— **λ-字典**（我加）：1-level density 的 λ（基准）
        ｜mollifier 的 θ（**不同轴**，R-A2 已证 θ 可 >1/2）｜pair correlation support（待判定）
        ｜zero-free region（非 support 半径）｜zero proportion（下游输出量）
        ⟹ 不可比即直接输出 R6-D
Gate 2  λ ≤ 1 的真正来源：A 显式公式 / B positivity / C 算术独立性 / D 族平均
Gate 3  必须主动构造 λ = 1+ε 并**明确失败节点**（不可消除正项 B_λ ≥ c(λ)>0 才算"结构味"）
Gate 4  **信息需求 vs 证明技术**（核心）——障碍是 ⟦未算但可定义的量⟧ 还是 ⟦与目标的等价性⟧？
Gate 5  ★ 决定性：canonical L1 机制能否跨过 λ ≥ 2
Gate 6  写死：比例 ⇏ 钉住（proportion → zero exclusion 须独立步骤）

**判定程序（我加）**：
$$\boxed{\text{结构性天花板} = \text{存在定理：}C\in\mathscr C_{\rm L1}\ \text{且 support}>\lambda_0\Longrightarrow C\ \text{必含与零点互相定义的对象（或必为条件性）}}$$
⟹ 结构性 = 【在信息类内部证明】的界；技术性 = 障碍可归约为定义良好但尚未算出的量
```
**四种输出**：R6-A 真结构天花板（Λ*=1）→ **此时才该坐标系跃迁**｜R6-B 1<λ<2 独立机制｜
R6-C λ≥2 且过 C1/C2′/C3（最期待，L1→pinning 现实化）｜R6-D λ 不可比（FZ-3″ 统一坐标失效）
**硬禁令**：不得退化为"寻找更强的 1-level density 定理"；须审【所有】L1 位置约束机制
**先验锚点（文献级/待核实）**：unitary 无条件 λ<1；orth/symplectic 族可到 λ<2；
两者之差来自【移位矩展开中非对角项的存亡】；ζ 猜想为 unitary ⟹ 不能借用族结果
```

### §8.9 R6 第一轮（唐先生执行）与第二轮（小灵执行）记录

**第一轮裁决**：
$$\boxed{\textbf{R6-A 被否定}}\ \text{（已有 canonical/independent/non-equivalent L1 机制使 support 跨 1）}$$
$$\boxed{\textbf{R6-B 不可宣布}}\ \text{（λ>1 在【其他 L 函数族】实现，非 ζ 的 RH engine）}$$
$$\boxed{\textbf{R6-D'}:\ \lambda\ \text{作为跨机制统一坐标不可用；}\lambda_\zeta\ \text{须单独定义}}$$

**Gate 1 产物（λ-字典 + 不可比判定）**：
```
1-level density：λ = Fourier support 半径（基准）✓
mollifier：θ ≢ λ（R-A2 已证 θ 可 >1/2）｜pair correlation：同族非同一参数（不可直接比数值）
zero-free region：非 support 半径｜zero proportion：下游输出量
⟹ 首条正式 **R1**：λ 只能在同一统计机制、同归一化下比较
```
**Gate 2D 决定性反例**：固定权重素数 level holomorphic newforms 无条件 λ=1.5 → 1.866…；
Maass 族 15/8=1.875 ⟹ **λ=1 不是 one-level density 的数学结构上限**
**Gate 3**：失败节点 = "λ=1 后须计算被 diagonal approximation 隐藏的**非对角算术结构**"（非"数学禁止继续"）
**Gate 4**：障碍属**类型 I（未算但可定义）** ⟹ **技术型**，非信息论天花板
**Gate 5**：层 A 一般族可逼近 2 ✓｜层 B **ζ 本身未突破**（族结构不匹配，非技术未移植）
**留下来真活口**：为什么 orth/symplectic family 能跨 1，而 ζ 的 unitary 对象没有相同的独立结构？

**第二轮（小灵执行）**：
```
① 结构性差异：族靠迹公式【几何侧】（Kloosterman + Bessel）提供独立算术数据；
   ζ 无 family average，其"迹公式"= 显式公式，几何侧就是素数侧本身
   ⟹ 问题归结为"素数侧非对角和非条件可算吗"
② ⭐ 线索（待核实）：Montgomery 无条件 λ<1；**Goldston–Montgomery (1987) 无条件处理 α∈[1,2]**，
   其评估与【素数间隙方差/素数对相关】相联系
   ⟹ **λ_ζ>1 的 carrier 是【素数侧独立对象】**（与协议预注册的先验锚点相反）
   ⟹ 倾向：1 处天花板为【技术型】，缺失输入 = 素数对相关数据
③ 预注册可证伪判据：判读失败（⟹ R6-A）当且仅当可证"任何 λ>1 素数侧和的 canonical 求值，
   其正则化必须引入超越素数间隙统计的零点侧输入"
④ ⭐⭐ 与 V1 规格汇合：素数对（间隙）相关数据满足 V1 的 char-0 / 非编码 / 非局部 / β-敏感 四项
   ⟹ **R6 第二轮可能正好交出宪法一直要求的"新的独立算术输入"类别**
```
**裁决**：**不做坐标系跃迁**（第一轮已否定 R6-A ⟹ 坐标系未失效）；
下一动作 = 审计【素数对相关数据能否作为 λ_ζ>1 的独立输入】（三问：独立于零点？足以跨过 λ=2？非等价？）

**新登记 R**：
```
R6（收缩定义域）：改问 λ_ζ 的天花板是技术型还是结构型
R8【新】：素数对（间隙）相关数据能否作为 λ_ζ>1 的独立算术输入？（三问 + 与 V1 规格的四项匹配）
```

### §8.10 ⚠️ 勘误 + R8 协议就绪（Gate 0 强制）

**勘误（撤回，不静默改写）**：
```
被撤回：R-A6 第二轮 §2 判读——"λ_ζ>1 的 carrier 是【素数侧独立对象】"（依 GM87 无条件处理 α∈[1,2]）
撤回理由（唐先生核实）：GM87 的核心等价在【RH 下】成立；1987 年把 Montgomery 的 x ≤ T^{1−ε}
   推进到 x ≤ T 亦在 RH 框架下；Languasco–Perelli–Zaccagnini 明确描述 GM 定理为"在 RH 下"；
   Bui–Keating–Smith（Selberg class）明确指出其方法【从零点统计出发】，
   因为一般不存在可用的 Hardy–Littlewood 型算术自相关结果
失误性质：**未核实即用作判读依据**——正是预注册所要防止的失效模式
拦截：预注册可证伪判据 + 外部核实 ⟹ **成功拦截** ✓（§6 纪律的价值得到实证）
⟹ λ_ζ>1 的 carrier 性质 = **未定**
```

**R8 登记**：
$$\boxed{R8:\ \text{短区间素数方差 / 素数对相关，能否作为 }\lambda_\zeta>1\ \text{的【独立、非等价、无条件】算术输入？}}$$
**三问**：Q1 独立性（不用 RH/零点统计）｜Q2 跨越性（λ_ζ>1 乃至 ≥2）｜Q3 非等价性（非 pair correlation/RH 重述）

**Gate 0（本协议首位，强制）= RH Contamination Audit**：
```
逐项追踪 GM87 及后续中"素数方差 ⟷ 零点 pair correlation"的【方向】在哪一步用了 RH
每步六标记：① uncond/cond ② 用 RH？③ 用 zero statistics？④ 用 Hardy–Littlewood？
            ⑤ 仅等价转换？⑥ 真提供新 β-sensitive info？
核心理念：**"素数侧对象可以定义" ≠ "素数侧对象可以独立无条件算出"**（V1 要求后者）
航标（结构性判读）：无条件方向 = 零点侧→素数侧（= N1 编码方向）；
   "素数侧→约束"所需方向正是非无条件那一侧 ⟹ 预先倾向 R8-C，但必须核实不得先判
```
**具体靶点**：$V(X,H)=\frac1X\int_X^{2X}(\psi(x+H)-\psi(x)-H)^2dx$
$=\sum_{h\le H}(H-h)\sum_{n\sim X}\Lambda(n)\Lambda(n+h)$
箭 1（prime-pair → V）｜箭 2（V → λ>1）｜箭 3（λ>1 → λ≥2），每箭强六标记

**Gate 1（继承 R6 字典问题）**：必须先建立 H-范围 ↔ λ support ↔ 1-level density support 显式映射
（R6-D' 已确立 λ 非统一坐标）；结构要点：无条件结果通常覆盖较大 H，猜想覆盖较小 H（≤ X^{1−ε}）

**四输出**：R8-A 真无条件 prime-pair carrier（罕见，进 V1 主线）｜R8-B 载体存在但范围不足｜
**R8-C Gate-4 型杀灭**（载体存在但其达 λ>1 所需精度本身等价于目标零点信息）｜R8-D 字典不可建

**硬禁令**：不得把"素数对数据 = 独立输入"写入假设（本协议起因即该假设被违反）；不得以"可定义"充"可无条件获得"；不得以等价转换冒充新信息；不得以 Hardy–Littlewood 充当无条件结果

**预注册预期**：最可能 R8-C；最理想 R8-A；须避免把 BKS"从零点统计出发"当作算术独立性证据

### §8.11 R8 第一轮裁决 + H↔λ 字典 + R8.2 协议

**裁决**：$$\boxed{\textbf{R8-B（当前）｜R8-C 未证｜R8-A 未证｜R8-D 已排除}}$$

**Gate 0（RH contamination）**：
```
prime pairs --(代数)--> J --(显式公式)--> zero pair correlation
右端强等价【带 RH】（LPZ 明确"在 RH 下"；Chan：strong pair correlation ⟺ 短区间素数两个二阶矩，under RH）
HL 本身即强未解决算术输入，不是现成无条件 carrier
⟹ 未发现隐藏的"独立无条件 prime-pair → zeros"通道；R8-C 暂不能成立为定理
⚠️ 规范化警示：展开式 Σ_{h≤H}(H−|h|)Σ_nΛ(n)Λ(n+h) 结构成立但公式层须规范化（三角权/端点/连续平均）
```

**⭐ Gate 1 — H↔λ 字典（本轮核心产出）**：
$$\boxed{\lambda=\frac{1}{1-\eta},\quad H=X^\eta\quad\Longleftrightarrow\quad \eta=1-\frac1\lambda}$$
```
λ=1 ⟺ η=0（H=X^{o(1)} 边界）｜λ>1 ⟺ 0<η<1 ｜**λ=2 ⟺ H=X^{1/2}（自对偶长度）**
```
$$\boxed{\text{决定性问题改写为：能否【独立无条件】获得 }H\sim\sqrt X\text{ 尺度的正确二阶素数方差？}}$$
⚠️ 校正：不得把"无条件几乎处处一阶计数可达 $H\ge X^{1/6+o(1)}$"当作 λ>1 证据——**一阶 vs 二阶不可混淆**

**三箭**：箭1 prime-pair→J **PASS**（真实 carrier）｜箭2 J→λ>1 **FAIL（当前，精度不足）**｜箭3 λ>1→λ≥2 **FAIL（当前，更大缺口）**

**三问**：Q1 定义层 YES / 强渐近层"独立供给未知"｜Q2 均未实现（≠不可能）｜Q3 定义层 non-encoding YES；强渐近层可能进入与 zero statistics 等价层级（未证）

**新登记 R**：
$$\boxed{R_8^{(1)}:\ \lambda=\frac{1}{1-\eta},\ H=X^\eta;\quad \lambda>1\iff\eta>0;\quad \lambda=2\iff H=\sqrt X}$$
```
⟹ 把"prime-pair 能否推 support"变为明确尺度问题：
   能否在 H=X^η（η>0）正幂尺度上独立无条件得到正确二阶 prime variance？（RH 强度目标 H~√X）
```

**R8.2 协议就绪**（`PROTOCOL-R8.2-precision-gap.md`）—— 缺口六槽分解：
```
S1 对角项 ｜ S2 非对角项（**关键槽**）｜ S3 在 H 上的一致性/均匀性 ｜
S4 主项精度 ｜ S5 规范化/涌现项（新增）｜ S6 局部性筛查（新增，依 N42/N5 预淘汰同余型机制）
预注册判据：若 S2 求值必须借入 F(α)、α∈(1,2) 型信息 ⟹ **R8-C 成立（Gate-4 型杀灭）**
            若 S2 可由素数侧独立评估（含足够精度的上界/几乎处处）⟹ R8-A/B 方向
主要劳动：产出"无条件精度表"（行=η 分段；列=无条件一阶/二阶上界/二阶渐近 ｜ 猜想 ｜ RH 下 ｜ 所需）
```
**裁决**：不做坐标跃迁；不宣布 R8-C；下一轮只审 S1–S6 的缺口解剖

### §8.12 R8.2 裁决（唐先生）+ R8.3 协议（S2 Mechanism Audit）

**裁决**：$$\boxed{\textbf{R8-B（强化版）｜R8-C 未证｜R8-A 未证｜R8-D 已排除}}$$ **瓶颈已定位到 S2**

**六槽**：S1 ✓ ｜ **S2 非对角 = 核心缺口** ｜ S3 依赖 S2 的 uniformity 缺口 ｜
**S4 正确二阶主项缺口 ❌** ｜ S5 ✓ 技术性（**不得变成新机制**）｜ S6 🔒 局部性排除（奇异级数非全局选择器）

**⭐ S2 三级分离**：
```
S2-a 可定义 YES ｜ S2-b 无条件上界 ≠ 正确二阶渐近 ｜ S2-c 无条件正确主项 = R8 真正要求
```

**⭐ S4 关键**：主项 $V\sim HX\log(X/H)=HX(1-\eta)\log X$ ⟹ **support 参数经 $1-\eta=1/\lambda$ 进入方差**；
误差项与主项同阶则 support 信息丢失 ⟹ $H\ge X^{1/6+o(1)}$ 的**一阶** almost-all 结果 $\not\Rightarrow\lambda>1$

**S2 判据**：**R8-C 未触发**（已证"现有强理论落入等价类"，未证"任何未来求值必然落入"⟹ 缺必然性定理）

**⭐ 新登记**：
$$\boxed{R_{8.2}:\ \text{困难 = 获得正确的 }HX\log(X/H)\text{ 级二阶主项；而该主项携带 }1-\eta=1/\lambda}$$
$$\boxed{\text{support 信息}\ \longleftrightarrow\ \text{二阶方差主项的 }\eta\text{-依赖}}$$

**⚠️ 唐先生阻断**：**不得**因 $\sqrt X$ 漂亮就把 $H=\sqrt X$ 本身解释成 RH 机制；目前仅为 GM 字典的尺度对应；**Gate 6 仍有效**

**R8.3 协议就绪**（`PROTOCOL-R8.3-s2-mechanism-audit.md`）——
问题：η>0（尤其 η=1/2）时 S2 非对角项能否由**非 HL、非 zero pair correlation、非族平均、非 CRT/筛法**的 char-0 结构给出所需主项？
```
⭐ Gate 0（新增，首位强制）= 字典自洽性检验：
   Montgomery 无条件范围 λ<1 ⟺ H=X^{o(1)}；字典必须与之自洽
   任何"看似无条件的 λ≥2 结果"必须先假设【字典误用】，而非突破
   核验①归一化 ②主项 vs 上界 ③GM 对应在该 η 区间是否有效
⭐ 个体 h vs 平均 h：个体主项（如 h=2）⟹ twin-prime 强度 ⟹ 不可得；
   合法目标 = **加权平均主项**；从个体出发者直接判为 HL 强度
机制类预筛：纯筛法 ⟹ 奇偶性障碍预淘汰；族平均/zero statistics/HL ⟹ 排除
四输出：R8.3-A 新 carrier（R8-A 打开）｜R8.3-B 全部归约（方可开始 R8-C 结构论证）｜
        R8.3-C 字典误用（需修正对应）｜R8.3-D 平均主项被证为 twin-prime 强度
```

### §8.13 R8.3 执行（小灵）：S2 Mechanism Audit ⟹ **R8.3-B**（归约，非必然性定理）

**Gate 0（字典自洽性）通过**：
```
① 三项归一化统一（variance vs second moment／L² over x vs almost-all／F(α) 与 λ 的显式对齐）
   凡"无条件 λ≥2"⟹ 先判【归一化/方向错误】
② 与无条件 λ<1 事实自洽：λ<1 ⟺ η<0 ⟺ H=X^{o(1)}（亚多项式）✓；GM 猜想 H≤X^{1−ε} ⟺ λ≥1/ε 覆盖一切 λ>1 ✓
③ ⭐ 决定性内部一致性探针：若无条件得到 η>0 的正确二阶主项，应直接给出【无条件 λ>1】
   —— 而后者已知不成立 ⟹ **S2-c 的 η>0 主项不可得与 λ<1 无条件事实【同一条边界】**
⚠️ 必核项（Gate 0 产物）：Lavrik/Motohashi/Hooley 型【平均移位相关】的无条件 η-范围
   （唯一可能推翻 ③ 的入口；若覆盖 η>0 且真主项 ⟹ 二选一：字典约定有误（R8.3-C）／不能转译为 F(α) 信息）
```

**§1 机制类**：纯筛法（**奇偶性障碍**预淘汰）｜圆法/Type I–II（**仅至 η=0 边界**，待核实）｜
大筛/谱（S2-b 级）｜迹公式/族平均（排除）｜zero statistics（排除）｜HL（排除）｜**新 char-0 机制：未发现**

**§2 ⭐⭐ 核心恒等式**：
$$\boxed{\text{S2-c（S2 的无条件正确二阶主项）}\ \Longleftrightarrow\ \lambda>1\ \text{的跨越}}$$
```
⟹ S2-c 不是"另一个更难的坎"，它【就是】λ=1 的跨越
```

**§2 ⭐⭐ 三支线统一（结构性综合）**：
| 支线 | 参数 | 跨越点 |
|---|---|---|
| mollifier | θ | θ=1/2 |
| pair correlation | λ | λ=1 |
| **prime variance（本线）** | η | **η=0⁺** |
$$\boxed{\text{三支线的"墙"是【同一道】——无条件素数侧信息的边界}}$$
（结构性综合，非定理；但把 FZ-3″ 的信息边界提升为**跨支线一致现象**）

**§4 三问**：Q1 carrier 独立／平均主项无已知独立无来源｜Q2 未实现｜Q3 已知路线均经 HL/零点侧（无必然性定理）

**§5 裁决**：**R8.3-B**（所有【已知】S2 路线归约为 HL/zero-statistics/族平均/筛法奇偶障碍）
**⚠️ 严格限定**："已知路线"的归约 ≠ 必然性定理 ⟹ **R8-C 仍未证**，但"开始构造 R8-C 结构论证的必要条件"已满足

**必产 R**：R_{8.3} 必然性定理（任何 canonical 求值 S2 平均主项必与 zero-side 等价）｜
R_{8.2} 保留｜R_{8.3}-verify（Lavrik/Motohashi/Hooley 无条件 η-范围核实）

### §8.14 ⚠️ R8.3 勘误（唐先生纠正）+ R8.3-verify 协议（状态 → **R8.3-B′**）

**三处修正（留原档，不静默改写）**：
```
① "S2-c ⟺ λ>1"（写作等价）⟹ **降为单向**：仅"若 S2-c 在目标归一化下成立 ⟹ λ>1"可用
② "所有【已知】S2 路线只到 η=0 边界"⟹ **证据不足，撤回该表述**
   原因：**Hooley 已展示 prime-specific off-diagonal 可在某些平均问题中被无条件压到主项以下**
        （误差改善至 QN log N + O(QN) + O(N²(log N)^{−A})）
③ 三支线统一（θ=1/2 / λ=1 / η=0⁺ 同一道墙）⟹ **降级为待核**（按本项目自身 N28 对象混淆）：
   Lavrik=频率平均二阶量；Motohashi=arithmetic functions(除数族)在 AP 中的 variance；
   Hooley=素数 AP variance 的 off-diagonal 改进 —— 与 R8 的 fixed-X 短区间 prime-pair 主项【非同一对象】
   特别：**不得因同具 QN log N 量级就把它们放在同一 λ 坐标轴上**
```

**⭐ 唐先生指定登记（本轮最大正面收获）**：
$$\boxed{\text{Hooley 型 prime-specific off-diagonal cancellation = R8.3 必须排除的【真正反例模板】}}$$

**状态更正**：
$$\boxed{\textbf{R8.3-B'}:\ \text{已知路线未打开 S2-c，但"必然归约到 zero-side"【尚未证明】}}$$

**R8.3-verify 协议就绪**（`PROTOCOL-R8.3-verify.md`）—— 中心判别器（新增）：
$$\boxed{\text{候选结果主项是否携带【连续尺度自由度】}H/X\ (1-\eta)\text{，还是只含【离散参数】}}$$
```
（AP modulus q / Fourier cutoff / 另一坐标）—— 即"对象对齐检验"的具体化（回应 N28）
三问：V1 是否真含 H=X^η(η>0) 的 prime-pair 二阶主项｜V2 主项是否真出现 1−η｜
      V3 能否在不调用 RH/pair correlation 下转译为 F(α)(α>1)
三输出：R8.3-C′（V1+V2 成立 ⟹ 反查 λ↔η 坐标，**不得宣布突破**）｜
        R8.3-A（V1+V2+V3 不可转译 ⟹ 真正新 carrier）｜
        R8.3-B′（V1/V2 失败 **且证失败非技术缺口** ⟹ 方有资格开始 R8-C 必然性定理）
主要劳动：对象对齐表（变量空间／权函数／非对角展开／主项是否含 H/X／能否转译 F(α)）
```

### §8.15 R8.3-verify 执行（小灵）：Hooley 模板**不可移植**（平均坐标错配）

**中心判别器逐族结果**（对象对齐表）：
| 族 | 变量空间 | 主项含 $H/X$？ | 关键结构 |
|---|---|---|---|
| Lavrik 型频率平均 | 频率 θ | ✗ | 主项正比于频率区间长度 |
| Motohashi（除数族 AP／加法除数平均） | modulus q | ✗（含 q/N） | 成功来自**乘法/Dirichlet 结构 + 谱机器** |
| Hooley（素数 AP variance） | modulus q | ✗（含 q/N） | cancellation 沿 **modulus 平均**发生 |
| **R8 目标 S2-c** | fixed X、短区间 H=X^η | **必须含 1−η** | 唯一合法平均坐标 = 移位 h |

**V1 ✗（三族对象均非 prime-pair 短区间主项）｜V2 ✗（出现的是 q/N、β−α 等另一坐标的函数）｜V3 不适用**

**⭐ 关键结论**：
$$\boxed{\text{Hooley/Motohashi 的无条件成功依赖【modulus 平均】坐标（+ 谱机器），}\
\text{而 R8 的 fixed-X 短区间问题【不具备】该坐标 ⟹ 模板【不可移植】}}$$
⟹ **原因不是技术缺口，而是【平均坐标错配】** ⟹ 为 R8-C 提供第一块结构性论证材料（仍非必然性定理）

**⭐ 新增筛查项**：
$$\boxed{\text{averaging-coordinate mismatch（平均坐标错配）}}$$
任何以"某平均问题已无条件成功"为依据的路线，须先证明其**平均坐标**与目标问题一致；不一致者预淘汰。

**⭐ R_{8.3} 必然性定理的更锋利形式**：
$$\boxed{R_{8.3}^{\rm sharp}:\ \text{证明 S2-c 的 }(1-\eta)\text{ 项（作为【频率积分的端点/边界项】）}\
\text{无法在不调用 }F(\alpha)\ (\alpha\to1^+)\text{ 的情况下求值}}$$
```
端点结构来源：H log X − H log H = H log(X/H) = H(1−η)log X ⟹ −log H 来自【截断端点】
⟹ S2-c = 控制【频率范围均方在边界处的行为】，而该处正是非对角项进入之处
```

**输出**：**R8.3-B′（维持）**，且本轮给出结构性理由（平均坐标错配）；仍非必然性定理（R_{8.3}^{sharp} 为待证靶点）

**必产 R**：R_{8.3}^{sharp}（更新为锋利形式）｜R_avg-coord【新】｜R_8^{(v)}【新】：Lavrik 型频率平均量与 S2-c 端点项的精确关系（恒等／可逆／单向）

### §8.16 ⚠️ R8.3-verify 勘误（唐先生）+ AOC* 升级 + R_8^{(v)} 变换链协议

**勘误（留原档）**：我上一轮表中 Hooley 一行标"主项含 H/X ✗"——**错误**。
```
原文（Montgomery–Hooley 短区间定理，LPZ 版）：
  M(x,h,Q) = hQ log(xQ/h) + (x+h)Q log(1+h/x) − κhQ
  无条件范围：x^{7/12+ε} ≤ h ≤ x，Q ≤ h
⟹ Hooley/AP 方差族【确含】连续短区间尺度 h/x
```

**判别器升级（唐先生）**：
$$\boxed{\mathsf{AOC}^*:\ \text{该定理能否把【目标非对角变量本身】作为可控平均坐标？}}$$
```
R8 的目标平均坐标 = **shift h**；Hooley 中 h 只是 AP 误差项的区间长度，
真正产生 cancellation 的平均坐标仍是 (q,a) ⟹ H/X 出现 ⇏ R8 尺度自由度已被捕获
```

**必须改写的对比表述**：
```
· 已证：短区间二阶主项【可以】无条件存在（Hooley，H ≥ X^{7/12+ε}）
· 未证：shift-average 的 prime-pair S2-c 可无条件存在
⟹ 不得再写"char-0 中不存在这种二阶主项机制"（过强）
新增范围事实：Hooley 无条件范围【不覆盖】η ≤ 1/2，尤其不覆盖 H=√X
```

**⭐ 本轮发现的未对齐（列为 A4 靶点）**：
$$\boxed{\lambda=\frac1{1-\eta}\ (H=\sqrt X\mapsto\lambda=2)\quad\text{vs}\quad \alpha=1+\eta\ (H=\sqrt X\mapsto\alpha=1.5)}$$
```
两式不能同时作为映到同一 F 参数的映射 ⟹ 必有一方约定不同
⟹ A4 必须核实 LPZ / Montgomery–Soundararajan 的 α↔H 约定
⟹ 未解决前，R8 的"自对偶尺度 H=√X"陈述【悬空】
```

**R_8^{(v)} 协议就绪**（`PROTOCOL-R8v-transform-chain.md`）：目标链
$V(X,H)\leftrightarrow\sum_h w_H(h)\sum_n\Lambda(n)\Lambda(n+h)\leftrightarrow F(\alpha)$，
Fourier 形式 $C(X,H)\leftrightarrow\int|\widehat w_H(\alpha)|^2|S_X(\alpha)|^2d\alpha$，$|\alpha|\sim H^{-1}$
四箭：A1 (q,a)-平均→h-shift 平均｜A2 variance→shift correlation（恒等/单向/需额外信息）｜
A3 主项是否足以恢复 $1-\eta$｜**A4 $C\to F(\alpha)$ 是 exact/asymptotic/单向/RH+PC 下**
四输出：R8v-i 等价点精确定位｜R8v-ii 缺口位置明确｜R8v-iii 缺口在变换本身｜R8v-iv 坐标层未对齐

### §8.17 R_8^{(v)} 执行（小灵）：变换链审计 ⟹ **R8v-iv（坐标层）触发**

**§3 未对齐处理（本轮第一位）**：
```
一致性检验：若 λ=1/(1−η) 就是 F 支持映射，则 Hooley 的 η=7/12+ε ⟹ λ≈2.4>1
            ⟹ 应给【无条件 F 支持>1】——与 Montgomery 无条件 α≤1【矛盾】
但该检验【不闭合】：Hooley 的平均坐标是 (q,a)（AOC*），未必转译为 F 信息
⟹ **循环依赖**：判定字典需要 A1，而 A1 的判定又需要字典
```
**⭐ 可判定替代判据（本轮产出）**：
$$\boxed{\text{须用【非 AP-平均】的无条件短区间二阶结果（未平均 }V(X,H)\text{）来判定字典}}$$
```
两个必核项：① LPZ / Montgomery–Soundararajan 的 α↔H 确切约定
            ② 【未平均】V(X,H) 的无条件 η-范围（非 Hooley 的 AP 版）
```

**A1**：(q,a)→h 无已知无条件转换；且按 AOC* 不可用作 R8 carrier
**A2**（⭐结构性判读）：展开 + 三角权 (H−|h|) 的**二阶差分**即可回收 c(h)
$$
\boxed{\text{A2 疑为【可逆】}\ (\text{须扣 principal/diagonal/规范化项})}\ \Longrightarrow\ \text{困难不在变换，而在求值}}$$
**A3**：1−η 来自频率积分【端点项】⟹ **并入 A4**，不单独成立
**A4**：**判定【悬置】**（§3 未解 ⟹ α↔H 映射未定 ⟹ 四选项无法区分；不得强行选一）

**输出**：
$$\boxed{\textbf{R8v-iv}:\ \text{坐标层问题——}\alpha/\lambda/H\ \text{三者约定必须先统一}}$$
```
附带：A2 疑可逆 ⟹ 若成立则 R8v-iii（缺口在变换本身）被排除
      ⟹ §3 解决后最可能落 R8v-ii（缺口位置明确）；R8v-i 需 A4 双向，暂不可得
```

**必产 R**：**R_conv【新】**（α/λ/H 约定统一，输入=两个必核项；**A4 的前置**）｜
R_8^{(v)}【更新】（A2 可逆性须严格化）｜R_{8.3}^{sharp}、R_avg-coord【保留】

### §8.18 ⭐ R_conv 解出（唐先生核实）：坐标层闭合；**R8v-iv 撤回**

**解出结果**：
$$\boxed{\eta=1-\frac1\alpha\iff\alpha=\frac1{1-\eta}\qquad\text{且}\qquad \alpha=\lambda}$$
```
标准 Montgomery–Goldston：X=T^α、H=X/T ⟹ H=T^{α−1} ⟹ H=X^{1−1/α} ⟹ η=1−1/α
⟹ α=λ（同一 F(X,T) normalization 下的同一参数）
⟹ **H=√X ⟺ η=1/2 ⟺ α=λ=2**（R8 的"自对偶尺度"不再悬空，已被精确坐标化）
```
**⚠️ 取代登记**：上一轮登记的 $\alpha=1+\eta$ 为**坐标误用**，据其生成的"1.5 vs 2 未对齐"随之消解。
$$
\boxed{\text{真正缺口 = 【求值】——如何无条件求出 }V(X,H)\text{ 的正确非对角主项？}}$$

**M–S 主项验证该坐标**：$V\sim H\log(X/H)$，$H=X^\eta$ ⟹ 尺度系数 $(1-\eta)=1/\alpha=1/\lambda$

**第二个前置项（未平均 $V(X,H)$ 无条件范围）**：
```
未找到无条件 S2-c 渐近；2024 综述：该 asymptotics 无条件所知甚少
且记录 Goldston–Montgomery【在 RH 下】：V ~ H log X(1 − log H/log X) 对 1≤H≤X^{1−ε} 一致，
**并与 Strong Pair Correlation Conjecture 等价**
```
$$\boxed{\text{S2-c}\Longleftrightarrow_{\rm norm}\text{variance asymptotic}\Longleftrightarrow_{\rm RH}\text{Strong PC}}$$
**⚠️ 限定**：该等价在 **RH 框架内**建立；**不得**写成"无条件 RH-free 等价" ⟹ R8v-i 以**条件形式**达成

**A2（确认）**：$V(X,H)\sim\sum_{|h|<H}(H-|h|)C_X(h)+$ 修正项；三角核 $\Delta_H^2$ 产生离散 delta
$$\boxed{\text{A2：结构性可逆（精确公式尚需完整记账）}\ \Longrightarrow\ \text{R8v-iii 排除}}$$
三项 bookkeeping 必留：Λ(n)² diagonal｜主项 H² 及交叉项｜x-积分边界 O(H²)/endpoint

**A3/A4 坐标统一（A4 解除悬置）**：
$$\boxed{C(X,H)\leftrightarrow V(X,H)\leftrightarrow F(\alpha),\ \alpha=\frac1{1-\eta}}\quad(\text{不得写 }C\leftrightarrow F(1+\eta))$$
特别 $C(X,\sqrt X)\leftrightarrow V(X,\sqrt X)\leftrightarrow F(2)$

**状态**：$\boxed{\textbf{R8v-ii（强）}+\textbf{R8.3-B'}}$；**R8v-iv 撤回**
**下一刀**：① 严格化 A2（完整记账）⟹ S2-c ⟹ 目标 $F(\alpha),\alpha>1$；
② 是否存在**完全不经过 $F(\alpha)$**的方法直接给出 h-shift 非对角主项？
②若被堵死 ⟹ R8-C 才真正具有**结构性**

### §8.19 R8.4 执行（唐先生选 ②）：h-space Independent Carrier Audit ⟹ **R8.4-B** + 结构性理由

**唯一问题**：是否存在已知的、不经 $F(\alpha)$、不经 HL、不经 AP/族平均，
却能直接给出 $\sum_{h\le H}w_H(h)\sum_n\Lambda(n)\Lambda(n+h)\sim HX\log(X/H)$ 的 char-0 机制？

**分类表（按"产生 cancellation 的变量"）**：HL(h/prime pair，排除)｜Hooley(AP $(q,a)$，AOC* 不匹配)｜
族平均/迹公式（排除）｜zero statistics（目标侧）｜Fourier mean-square（需回到 h）｜纯筛法（奇偶性障碍）｜
大筛/zero-density（S2-b 级）｜Bombieri–Vinogradov（AOC* 不匹配）｜almost-all 一阶（非二阶）｜
**未知第三机制（h 本身）= 唯一活口——本轮未发现**

**⭐ 结构性发现（本轮核心）**：
```
唯一走出"平均二元关联"的先例 = 加法除数问题（Σ_n d(n)d(n+h) 在 h-平均下可无条件求解，
   Motohashi / Deshouillers–Iwaniec 一线），机制 = 谱方法（Kuznetsov 公式）
拆解：Kuznetsov 谱侧 = 离散谱（Maass 尖点形式）+ 连续谱（Eisenstein/ζ 相关）
 · 对除数函数：离散谱贡献【无条件可得】（自伴谱侧 ⟹ 谱参数实 ⟹ 门⑲"RH 自动"侧）
 · 对 Λ：对应谱输入正是 ζ 的零点/配对相关 F(α) ⟹ **条件侧/目标侧**
```
$$\boxed{\text{除数情形能无条件走出 h-平均，因为其谱引擎坐在【离散·自伴】侧；}\ \text{Λ 情形的同一引擎坐在【零点·散射】侧}}$$
⟹ **与门⑲/⑳完全同型**（"锁管离散侧；ζ 住散射侧"）⟹ **本项目内部强交叉一致性检验** ✓✓

**输出**：$\boxed{\textbf{R8.4-B}}$（已枚举机制均退化为 HL / zero statistics / AP-族机器）
**⚠️ 仍非必然性定理**（"已枚举"≠"全部"），但给出结构性理由

**R8-C\* 锐化**：
$$\boxed{\textbf{R8-C}^{*}:\ \text{任何 canonical、zero-blind、非-HL、h-space cancellation 若给 S2-c，必产生等价于 }F(\alpha)\ (\alpha>1)\text{ 的量}}$$
**更强等价表述（由 §2 得）**：
$$\boxed{\text{h-space cancellation 必须供给一个【谱输入】；而 Λ-关联可用的谱输入只有 zero-side（"谱输入二分"）}}$$

**保留任务 ①**（收口用）：严格化 A2（完整扣除三项 bookkeeping）⟹ 形式化链条 S2-c → V → Σ_h(H−|h|)C_X(h) → F(α)

### §8.20 R8.4-ERR-1（取代）+ R8-C† 登记 + 第一刀：**Voronoi vs 显式公式结构断点**

**⚠️ R8.4-ERR-1（取代）**：撤回"divisor case is unconditional because its spectrum is purely
discrete/self-adjoint"（Motohashi 谱分解并非只有离散谱，涉及 cusp forms 与 Kuznetsov/Kloosterman 耦合）
$$\boxed{\text{合法修正：divisor case possesses an }\textbf{unconditional automorphic spectral engine}}$$
**影响**：不修正则 R8-C\* 会建立在**假的"谱二分"**上。

**文献前提（I 层核验，唐先生）**：
```
Motohashi 1994：D(N;f)=Σ_{n≤N}d(n)d(n+f)，链 = Kloosterman → Kuznetsov → cusp-form Fourier coefficients
  **Theorem 1：对 shift f 的 uniform 结果（1<f<N^{1/2}）**
Motohashi–Ivić 1995：E(X;f) 关于 shift f 的均方（spectral large sieve + E(x;f) 的 explicit formula）
⟹ **h-space 本身可以承载真正的谱 cancellation（文献事实）**
```

**R8-C† 正式登记（Spectral Input Dichotomy）**：
$$\boxed{\text{canonical、zero-blind、非-HL 的 }h\text{-space cancellation 若给 }V\sim HX\log(X/H)\text{，则内部必有 spectral input 同时完成：}\text{①解析 }\Lambda\text{ 非对角}\\text{②对 h-shift 真 uniformity ③提取精确二阶主项}}$$
三子命题：C1 对象层（⟹ 真 Λ-shift spectral input，非仅 Fourier mean-square）｜
C2 主项层（$H\log(X/H)$ 不由 diagonal/size/density 自动产生；系数 $1-\eta=1/\alpha$ 须由跨尺度谱结构产生）｜
C3 zero-blindness 层（定义 zero-blind engine；问 C1+C2 是否迫使其失败）

**⭐ divisor 反例校准（写死）**：
$$\boxed{\text{h-space cancellation}\ \not\Rightarrow\ F(\alpha)}$$
⟹ R8-C\* 只能问：对 $\Lambda\times\Lambda$ 的 canonical correlation，产生正确二阶主项所需谱输入是否**只能**从 zero-side 获得？

**⭐ 第一刀结果（结构断点）**：
$$\boxed{\text{Voronoi 公式 = 相应 Dirichlet 级数【函数方程】的影子；要求系数来自"函数方程/Voronoi 类"}}$$
```
· d(n)：级数 = ζ(s)² ⟹ 有函数方程 ⟹ Voronoi ✓ ⟹ Kloosterman ⟹ Kuznetsov ✓
· Λ(n)：级数 = −ζ'/ζ ⟹ 无函数方程；Mellin/Perron 转移给出【零点和】（显式公式）
  ⟹ Voronoi 步骤被【显式公式】取代，其对偶对象【就是零点】
```
$$\boxed{\text{L1（引理候选）}：\text{Kuznetsov/Voronoi 引擎要求移位关联两因子来自函数方程类；}d(n)\text{ 在内}，\Lambda(n)\text{ 不在}}$$
L1 解释三件事：①divisor 能走出 h-平均 ②Λ 的 h-平均需 zero-side ③BKS 为何从 zero statistics 出发
**连接**：N1 + 门⑰（引擎平凡化）+ 门⑲⑳（离散/散射不对称）在 R8 世界的同一件事

**L1 可证伪条件（预注册）**：存在 Λ-侧 canonical、zero-blind、非-HL、non-Voronoi 谱引擎给出正确二阶主项
**可核实项**：是否存在"Λ 的 Voronoi 型公式"文献（若有且对偶非零点 ⟹ L1 削弱）

### §8.21 R8-C†-L1′：L1 撤回与取代（唐先生核实可证伪项）

**L1 撤回**：原命题"Kuznetsov/Voronoi 引擎要求两因子来自函数方程类；d 在内、Λ 不在"❌**过强**
```
理由：Λ 并非不属于任何函数方程相关结构；文献已有对 Λ 的 Voronoi-type treatment
     （Lou 2019 将 λ(n)=Λ(n) 放入 shifted-convolution 框架，大 H 区间获非平凡 cancellation）
```
$$\boxed{\text{L1}^{\prime}:\ \text{标准 Kuznetsov-compatible Voronoi 引擎要求系数具有一种能把 additive twist}\\text{转化为【另一个 arithmetic coefficient system】的函数方程结构}}$$
```
d(n): ζ² → automorphic 函数方程 → Kloosterman dual
Λ(n): −ζ'/ζ → logarithmic derivative → zero poles
⟹ Λ 缺的是"zero-free arithmetic dualization"，不是"任何 Voronoi formula"
```

**可证伪项三行结果**：①"Λ 完全没有 Voronoi 型公式"= **FALSE/过强**；
②"已有 Λ-type Voronoi machinery 是 zero-blind dual"= **未发现**；③"原始 Λ 的 Mellin dualization 暴露 zeros"= **成立**

**Mellin 机制精确化**：$\frac1{2\pi i}\int(-\zeta'/\zeta)\widehat W\,ds$ 左移 contour 必遇 $s=\rho$ ⟹
$$\boxed{\text{对原始 }\Lambda\text{，自然对偶谱不是 arithmetic Kloosterman side，而是 }\textbf{zero-residue side}}$$

**⭐ Chorge–Dixit 2024 数据**：新 Voronoi 公式（Liouville/Möbius/d²）**明确含 ζ 非平凡零点级数**
$$\boxed{\text{Voronoi-type formula}\ \not\Rightarrow\ \text{zero-blind}}$$
⟹ 新筛查项 **VZ**：若某函数 Voronoi 公式暴露零点级数，以其为 carrier 即重新引入 zero-side（N1）

**⭐ 机制细化（小灵）**：Bessel/Kloosterman 核来自函数方程【Γ 因子的乘性】；
对数导数破坏 Γ 乘性（引入 Γ'/Γ 型非乘性项）⟹ **同型 Bessel 核不存在**（结构性论证）

**C1′**：S2-c ⟹ Λ×Λ 的 genuine arithmetic dualization，且 dual spectrum **不含 ρ**（否则 = zero statistics in disguise）
**ZBV 条件**：$\mathcal V_\Lambda:\sum_n\Lambda(n)e(an/q)W(n/N)\mapsto\sum_m A_q(m)\widetilde W(m)$，
$A_q(m)$ 须由有限/离散 arithmetic data 构造且**不含** $\sum_\rho$，并能进 Kuznetsov 型机器给出正确二阶主项

**⭐ 核心问题压缩（当前唯一）**：
$$\boxed{\textbf{能否构造一个不经过 }\rho\textbf{ 的 }\Lambda\textbf{-arithmetic dualization？}}$$

**⭐ 元观察（结构性，非定理）**：同一障碍形状已三实例——
门⑲⑳（锁管离散侧/ζ 住散射侧）｜R8.4（divisor 有 automorphic engine，Λ 侧落 zero side）｜
本节（非-automorphic 乘法函数的 Voronoi 化暴露 zero 级数）
⟹ 形状一致："算术对象自身的对偶/谱引擎落在 zero 侧"（可作未来候选的快速筛查模板）

### §8.22 R8-C†-L1″：标准 Voronoi 范式内 zero-side 断点已锁定（唐先生完成"甲"）

**甲的结果**：Chorge–Dixit（2024/2026）覆盖 $\lambda$（**Liouville**）、$\mu$、$d^2$，**不覆盖** $\Lambda$（von Mangoldt）
$$\sum\lambda(n)n^{-s}=\frac{\zeta(2s)}{\zeta(s)}\qquad\text{vs}\qquad\sum\Lambda(n)n^{-s}=-\frac{\zeta'(s)}{\zeta(s)}$$
$$\boxed{\text{Chorge–Dixit}\not\Rightarrow\Lambda\text{-side VZ}}$$
**登记纪律**：$\lambda_{\rm Liouville}\neq\Lambda_{\rm von\,Mangoldt}$（禁止再混用）
**VZ → VZ-1**（降格为机制旁证）：$\lambda_{\rm Liou},\mu,d^2$ 的 Voronoï 公式中确实出现 $\rho$-series

**Λ 侧标准 Mellin dual 必含 $\rho$**：由 $\zeta(s)=\chi(s)\zeta(1-s)$ 微分得
$$-\frac{\zeta'}{\zeta}(s)=-\frac{\chi'}{\chi}(s)+\frac{\zeta'}{\zeta}(1-s)$$
右侧非新 Dirichlet series，而是 $\zeta'/\zeta(1-s)$ + archimedean 对数导数 ⟹ contour shift 必遇 $\operatorname{Res}_{s=\rho}=-\mathcal T(\rho)$

**⭐ 小灵补（显式结构）**：$\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)$ ⟹
$$-\chi'/\chi=\underbrace{\Gamma'/\Gamma\ \text{型项}}_{\text{非乘性 ⟹ Bessel 核不存在}}+\underbrace{\cot(\pi s/2)\ \text{型项}}_{\text{偶数处极点 = trivial zeros 来源}}$$

**L1″ 正式登记**：
$$\boxed{\textbf{L1}^{\prime\prime}:\ \text{在标准 Mellin/FE Voronoi 范式中，}-\zeta'/\zeta\text{ 对偶化时保持为 logarithmic derivative，}\\text{其非平凡谱贡献以 }\rho\text{-residue 出现，而不形成 zero-blind arithmetic coefficient system}}$$
$$\boxed{\text{L1}^{\prime\prime}\neq\text{"全体可能 ZBV 不存在"}}$$

**⭐⭐ 断点更准确位置**：
$$\boxed{\text{断点不是"有无函数方程"，而是【乘法层（积/比）】vs【导数层（对数导数）】}}$$
```
λ_Liouville：ζ(2s)/ζ(s) = 级数【之比】⟹ 可产生新系数系统 c(n) ⟹ 有 arithmetic dual ✓
Λ：−ζ'/ζ = Euler 积的【对数导数】⟹ 乘法局部因子 → 加法性 prime-power measure
小灵提炼：**可对偶性是乘法层的性质；导数层的对偶是极点/留数层**
```

**ZBV-Existence Audit 三分类**（只攻最后一格）：
```
① Mellin + ζ FE → ρ-residues（❌ N1）｜② automorphic Voronoi → 若存在对应 automorphic coefficient（? 待证）
③ 非-Mellin 新变换 → 未知 A_q(m)（**唯一活口**）⟹ 攻 Λ →? A_q(m) →? Kuznetsov
```
**⭐ 小灵提出的 ZBV 两难（审计框架；结构性）**：
```
① 满足 Z1–Z3 ⟹ 对偶系数须（本质）automorphic/FE 型 ⟹ 原对象须属乘法层或自守对象 ⟹ 与 Λ 的导数层性质冲突
② 放弃 Z3 ⟹ 失去产生二阶主项的谱机器（C2）⟹ 无法交付 S2-c
⟹ 两难即为"A_q(m) 必要结构条件"的可攻形式
附记（结构性）：对 −ζ'/ζ 对偶化实质要"积分回乘法层"（log ζ），而 log ζ 由零点支配（待严格化）
```

**状态表**：Chorge–Dixit 覆盖 Λ? NO ｜ λ 的 Voronoï 含 zero sums? YES(VZ-1) ｜
Λ 的标准 Mellin dual 含 ρ? YES ｜ Λ 的 zero-blind arithmetic dual? 未发现 ｜ ZBV 全称定理? NO

### §8.23 ZBV-Existence Audit 第一轮（小灵执行）：五门形式化 + **L3 → L3′**

**五门 ZBV = Z1∩Z2∩Z3∩Z4∩Z5**：
```
Z1 Non-reencoding + 压缩性（含 IDC：A_q 须独立于目标 C(X,H)，由 Λ 的算术律独立构造）
Z2 Reciprocal phase：e(an/q) → e(±ā m/q′)
Z3 Local/CRT compatibility：R_{q₁q₂} ≃ R_{q₁} ⊗ R_{q₂}
Z4 **Quadratic spectral closure (QSC)**：A_q×A_q → Kloosterman/trace 核 → **闭合谱展开**
Z5 Zero-blindness：不显式/隐式依赖 {ρ}
```
$$
\boxed{\text{若 ZBV 要成为 R8 carrier，必须具有二次谱闭合 QSC 且 }\operatorname{Spec}\cap\{\rho\text{-residue data}\}=\varnothing}$$
**Λ 状态表**：Z1 可要求 ✓ ｜ **Z2 未知** ｜ Z3 强约束未知 ｜ **Z4 未发现** ｜ **Z5 标准路线失败**
**标准 Mellin 分支已关闭**（ZBV-1 = NO）：$\sum_\rho\mathcal T(\rho)$ ⟹ 唯一活口 = 满足 Z2–Z5 的新 $A_q$

**L2（候选引理，近乎定义层可证）**：
$$\boxed{\text{zero-blind independent dualization }\Lambda\to A_q\text{ 且能产生 }\Lambda\times\Lambda\text{ 二阶主项}\Longrightarrow A_q\text{ 必满足 reciprocal}+\text{CRT}+\text{QSC}}$$
**L3 → L3′（本轮改写，小灵）**：
```
原 L3 用了"automorphic/Euler-FE 型"，但 **Kuznetsov 需要的是【谱可实现性/模性】，不是 Euler 乘性**
（Euler 乘性 ≠ 模性：存在有 FE 但无 Euler 积的对象，如 Epstein zeta/高阶格 theta 级数）
```
$$\boxed{\text{L3}^{\prime}:\ \text{reciprocity}+\text{CRT}+\text{QSC}+\text{Z5}\ \stackrel{?}{\Longrightarrow}\ \text{系数系统 modular/谱可实现？}}$$
⟹ 若准入门槛是**谱可实现性**而非乘性，则**潜在 ZBV 类比"自守 L 函数"更宽**

**⭐ 反例猎捕（主动）**：
| 候选类 | 判定 |
|---|---|
| (a) 非自守 Voronoi 函数（λ_Liou, μ, d²） | **Z5 ✗（公式显含 ρ 级数）** ⟹ 被吸收；且证明 **Voronoi ⇏ automorphic** |
| **(b) Epstein zeta / 高阶格 theta** | **真正威胁**：有 FE 无 Euler 积 ⟹ 待核实能否作 carrier |
| (c) 动力/几何谱展开（Ruelle、量子图、转移算子） | 缺算术 reciprocity/CRT ⟹ 被 Z2/Z3 吸收 |
| (d) Kloosterman zeta 函数 | **循环**（解析理论由 Kuznetsov/自守输入建立） |
| (e) Weil 表示 / theta | 谱理论 = theta = 自守 ⟹ 被吸收 |
$$\boxed{\text{【未发现】未被吸收的反例；但得到经验二分：算术 reciprocity+CRT 类中，Z5 仅在 automorphic/FE 类被观察到}}$$

**判定**：$\textbf{R8-C}^{\dagger}\to$ **L2 可形式化，L3′ 为真正生死线**
```
L3′ 成立 ⟹ A_q 须 modular/谱可实现 ⟹ Λ（导数层，连 FE 都无）不匹配 ⟹ ZBV 在 QSC 类内不存在
L3′ 不成立 ⟹ 得到明确新数学空间：non-Euler-multiplicative, zero-blind, quadratically closed
              arithmetic duality —— 可能才是 R8 真正活路
```
**下一刀（唯一）**：证或否证 L3′；**首选突破口 = 反例表 (b)**（Epstein/theta 类，同时触"有 FE 无 Euler 积"与"谱可实现性"两条线）

### §8.24 R8-C†-B1：Epstein/theta 反例审计（唐先生执行）——(b) 不是反例，而是 L3′ 的正面证据

**已确认**：$\text{FE}\not\Rightarrow\text{Euler product}$；$\text{zero-blind spectral duality}\not\Rightarrow\text{Euler multiplicativity}$
**Epstein FE 来源**：$\Theta_Q(t)\xrightarrow{\text{Poisson}}t^{-n/2}(\det Q)^{-1/2}\Theta_{Q^{-1}}(1/t)$ ⟹ lattice → Poisson → dual lattice → Mellin → FE
（适当条件下 $\Theta_Q$ 是 modular form，或 Weil 表示下的 vector-valued modular form）
**硬审计**：
$$\boxed{\text{Poisson reciprocity}\neq\text{Kloosterman reciprocal-phase reciprocity}}\quad\boxed{\text{Weil-locality}\neq\text{CRT-locality(Z3)}}$$
（Poisson kernel = $e^{2\pi i\langle x,\xi\rangle}$；Kuznetsov 几何侧需 $d\mapsto\bar d\bmod c$）
**Z4**：Epstein/theta 有 QSC 强版本，但**谱核是 theta/Weil 型，非 Kloosterman 型**

**四象限表**：
| 机制 | Z2 | Z3 | Z4 | Z5 | modular/spectral |
|---|:-:|:-:|:-:|:-:|---|
| Epstein/theta | △ | △ | ✓ | ✓ | ✓ |
| Kuznetsov | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ruelle/量子图 | × | × | ✓/△ | ✓ | 非算术 |
| Λ 标准 Mellin | × | × | × | × | zero residues |

**⟹ (b) 身份**：non-Euler but modular/Weil-spectral example（**非** non-modular zero-blind QSC 反例）

**L3′ → L3″**：QSC 至少两种实现（Type I Kuznetsov / Type II theta-Weil）⟹
$$\boxed{\textbf{L3}^{\prime\prime}:\ Z2+Z3+QSC+Z5\Longrightarrow\text{representation-theoretic spectral realization？}}$$
三支：Weil/theta ｜ automorphic/Kuznetsov ｜ **genuinely new**
$$\mathcal N=\{\text{zero-blind arithmetic QSC systems}\}\setminus\{\text{Weil/theta}\cup\text{automorphic}\}$$
**对 Λ 的意义**：没有 Euler 积**完全不是障碍**；关键是**是否存在独立的 representation-theoretic reciprocity engine**（Epstein 有 lattice duality/theta/Weil；**Λ 缺这一层次对象**）

**⭐ 小灵补三点**：
```
4.1 命名 Z2 的对偶类型：**inversion reciprocity（乘法群反转 d↦d̄）vs Fourier duality（加法群特征对偶）**
    Kloosterman 建在乘法群反转上；theta 建在加法群字符对偶上 ⟹ 第三类须提供第三种对偶类型
4.2 局部域对偶清单（结构性）：① 加法群 Pontryagin 自对偶 ② 乘法群特征论（反转→Kloosterman/Gauss）
    ③ 二者的综合 = Tate adelic 对偶（**其解析延拓产出 ζ 零点**）
    ⟹ 若 engine 必须由局部域结构装配，第三类须为【非对偶型】；已知非对偶候选 = 算术微分（Buium δ）
       —— **门⑩已因尺度关闭**
4.3 ⭐⭐ **QSC 的二次性 = GL₂-结构**：Kloosterman 来自 GL₂；Weil 表示是 GL₂ 的 metaplectic 表示
    ⟹ QSC 很可能正是"要求 GL₂-型表示论"；而对 GL(1) 对象 Sym²(平凡)=平凡 ⟹ 无 GL₂-二次结构
    ⟹ **R8 的 QSC 与门⑰（引擎平凡化）很可能是同一件事**（结构性论证，未形式化）
```

**下一刀**：证或否证 $Z2+Z3+Z4\Rightarrow$ 某有限 adelic/representation-theoretic kernel？
分类：$\text{finite reciprocity}\to\{$Kloosterman/automorphic ｜ Gauss/Weil/theta ｜ **genuinely new**$\}$
```
第三类存在 ⟹ R8 当前最值得追的活口
第三类不存在 ⟹ 有力度的受限 NO-GO：Z2+Z3+QSC+Z5 ⟹ Weil/automorphic representation-theoretic realization
   ⟹ 再查 Λ 能否进入该 envelope
小灵具体化：先判"第三类是否必须非对偶型"（若是 ⟹ = 已关闭的算术微分候选）；
            再判"QSC 是否即 GL₂-结构"（若是 ⟹ 用门⑰的 Sym² 平凡化直接给 Λ 的排除条件）
```

### §8.25 ⚠️ 撤回 4.2/4.3 + L3‴ + Finite-QSC Lemma（唐先生核实高秩 Voronoi/Weil/BK 框架）

**撤回 4.3**（小灵过强推断）：$\text{QSC}\Rightarrow GL_2$ **✗ 不成立**
```
反例：GL(N) balanced Voronoi 公式把 Fourier 系数与 **hyper-Kloosterman** 扭结连接，
并与 GL(2) Kuznetsov 配合产生谱 reciprocity ⟹ 底层表示论可为 GL₃、GL₄、…
更甚：QSC 也不唯一指向 GL(n) —— Epstein/theta 给第二类（quadratic lattice → Weil 表示 → Mp_{2r}）
⟹ 至少三类引擎：GL₂/Kuznetsov ｜ GL_n/Kloosterman–Voronoi ｜ Weil/theta/metaplectic
修正表述：QSC ⟹ **representation-theoretic spectral structure**（候选必要，非定理），
   底层群 ∈ {GL_n, Sp_{2n}, Mp_{2n}, SO_n, …}（与 Braverman–Kazhdan 一般 Fourier/γ-factor 框架一致）
⟹ **GL₂ 是 QSC 的一个实现，不是其定义**
```
**降级 4.2**（小灵过强推断）：「第三类必须 non-dual」**✗ 未证**
```
三清单完整性未证明；且 duality 非三个离散盒子：Fourier → Weil transform → ρ-Fourier →
  一般 reductive group 的 representation-dependent Fourier theory（BK：kernel 由 Langlands dual 表示决定）
⟹ "不是已有三种 duality" ⇏ "必须 non-dual"；可能出现新的 duality functor
```

**L3‴ 正式登记**：
$$\boxed{\textbf{L3}^{\prime\prime\prime}:\ Z2+Z3+Z4+Z5\ \stackrel{?}{\Longrightarrow}\ A_q\in\mathcal E_{\rm RT}}$$
$$\mathcal E_{\rm RT}\supset\{GL_2\text{-Kuznetsov}\}\cup\{GL_n\text{-Voronoi}\}\cup\{\text{Weil/theta}\}\qquad \boxed{\mathcal N=\text{QSC}\setminus\mathcal E_{\rm RT}}$$
**四层猎捕**：A Abelian Fourier（Z2/Z3 不够强）｜B Weil/theta（过 Z4+Z5，不自动过严格 Z2/Z3）｜
C Automorphic/reductive（目前最强已知 QSC 类）｜**D 真正未知（非 reductive 表示论）**

**⭐ 唐先生新观察**：Z2 含 $a\mapsto a^{-1}\bmod q$ ⟹ dual kernel 须同时看见 $(\mathbb Z/q,+)$ 与 $(\mathbb Z/q)^\times$
$$\boxed{\text{真问题}:\ \{\text{additive char}\otimes\text{multiplicative inversion}\otimes\text{CRT}\otimes\text{quadratic closure}\}\stackrel{?}{\Longrightarrow}\text{finite-group representation}}$$

**⭐⭐ 新硬目标 Finite-QSC Lemma**：$K_q(a,m)$ 满足 R1 reciprocal inversion｜R2 $K_{q_1q_2}\simeq K_{q_1}\otimes K_{q_2}$｜
R3 $K_qK_q^*$ 同类闭合｜R4 不由 $C(X,H)$ 反向定义。
$$\boxed{R1+R2+R3\ \Longrightarrow\ K_q\ \text{是否必来自某种有限群/代数表示？}}$$
若成立 ⟹ 第三类 = $\boxed{\text{non-representation-theoretic finite reciprocity kernel}}$

**⭐ 小灵补三点**：
```
7.1 候选证明策略（torus 识别）：R1（d↦d⁻¹）+ R2（CRT 张量）合起来把 kernel 逼向
    **环面指数和** Σ_{d∈(ℤ/qℤ)^×} e_q(ad+bd⁻¹)（Kloosterman 型）；已知其【谱闭合唯一途径】
    是 trace formula / automorphic / Weil 机器 ⟹ 未猎获者 = "torus 和 + 独立谱闭合"
7.2 Z1 升级 = 早前 **C_ar^finite 语法类**的同一动作（限制【构造文法】而非输出）；
    杀手反例：任意有限群表示造的 K_q(x,y)=Tr[ρ_q(x)ρ_q(y)⁻¹] 天然表示论闭合但可能是 re-encoding
    ⟹ IDC/生成性条件是唯一闸门（两处应合并为同节门槛纪律）
7.3 Z2 的实质 = **加法与乘法的耦合门** ⟹ 正是本项目最老主题（+ 与 × 的交互）以【门槛形式】重现
    （结构性呼应，非定理）
```

**判定**：Epstein/theta ✓ 正面证据 ｜ FE⇏Euler ✓ ｜ QSC⇒GL₂ ✗ 撤回 ｜ 第三类必须 non-dual ✗ 未证 ｜
Z2+Z3+QSC 仍可能强迫表示论结构 ｜ **真正活口 = non-representation-theoretic finite reciprocity kernel**
（本轮没回到任何已关闭路线：问的是 ZBV 五门本身是否已具备有限代数结构定理）

### §8.26 R8-C†-B2：QSC_F / QSC_G 分叉 + Global-QSC Lemma（唐先生本轮）

**⚠️ 小灵撤回 7.1**：$R1+R2\not\Rightarrow$ 标准 Kloosterman（一般核 = $\sum_{d\in(\mathbb Z/q)^\times}w_q(d)e_q(ad+bd^{-1})$，
$w_{q_1q_2}=w_{q_1}w_{q_2}$ ⟹ 仍满足 CRT 张量，$w_q\equiv1$ 只是最特殊情形）

**⚠️ Finite-QSC Lemma 改名**：→ **Finite-QSC Reduction Lemma**
```
若 QSC 只要求有限卷积闭合 ⟹ 固定 q 时进入 ℂ[G_q]≃⊕End(V_π) ⟹ 任何有限核分解为有限维不可约块
⟹ "finite closure ⟹ finite representation" 是【代数事实】
⟹ 原 Lemma 即使成立也【排除力弱】（价值 = 压缩候选空间，非杀候选）
```

**⭐⭐ Z4 少一层：QSC_F ≠ QSC_G**
| 级别 | 内容 | 性质 |
|---|---|---|
| **QSC_F** | finite closure（$A_qA_q^*\in\mathcal A_q$，dim<∞） | **近乎代数事实** |
| **QSC_G** | global spectral closure（统一谱空间 $\mathscr H$，含 finite $q$-算术侧 + archimedean transform + 同谱闭合所有 $q$） | **Kuznetsov 有、有限群表示没有** |

**L3 拆两级**：L3_F（Z2+Z3+QSC_F ⟹ finite rep envelope；大概率可证、排除力弱）｜
**L3_G**（$Z2+Z3+QSC_G+Z5\Longrightarrow\mathcal E_{\rm global}$?），$\mathcal E_{\rm global}\supset\mathcal E_{\rm theta}\cup\mathcal E_{\rm automorphic}\cup\mathcal E_{\rm other}$
$$\boxed{\mathcal N_G=\text{QSC-G}\setminus\mathcal E_{\rm global}}$$
**Epstein/theta = QSC-G 的合法实现**（确实通过 finite/local→global 关）

**⭐ 伪活路命名**：**finite-QSC impostor**——各 $q$ 的谱只是 $\mathscr H_q$（未形成 $\mathscr H_{\rm global}$），
无法把 $\Lambda\times\Lambda$ 二阶相关推进到统一谱参数。
**Z1 再加一层（唐先生）**：$\boxed{\text{Global independence}:\ A_q=\mathcal V_q(\Lambda)\ \text{须来自统一构造 }\mathcal V\ \text{与统一谱 }\mathscr H_{\mathcal V}}$

**R8 真正桥**：$\Lambda\overset{\mathcal V}{\to}\{A_q\}\overset{\text{finite reciprocity}}{\to}\{K_q\}\overset{\text{global closure}}{\to}\mathscr H$
（$\mathscr H$ 须承载：所有 $q$｜所有尺度｜additive twist｜archimedean transform｜二阶 $A\times A$ closure｜Z5 保证未偷放 $\rho$）

**⚠️ 不能用"有限表示"杀 R8**：$(R1+R2+R3)\Rightarrow\text{finite rep}\Rightarrow\text{R8 closed}$ **不成立**（差最关键一层）

**⭐ Global-QSC Lemma（新生死线）**：$A_q$ 满足 Z1+Z2+Z3+QSC_F+QSC_G+Z5 ⟹ 是否必然存在 global harmonic/rep-theoretic object？
且即使"是"也不能直接杀 Λ（Λ 可能对应尚未发现的 global object）
$$\boxed{\text{终点必须是}:\ \text{Global-QSC}+\Lambda\text{ 的结构约束}\Rightarrow\text{矛盾}}$$

**⭐ 小灵补两点**：
```
10.1 QSC-G ≈【系统满足一个 trace formula / Poisson 型全球恒等式】
     （Kuznetsov = GL₂ 迹公式；Epstein/theta = adelic Poisson + Weil 谱分解）
     已知这一切都【从群作用导出】⟹ 反例构造目标精确化为：
     **一个不借助群作用却仍具 global closure 的有限 reciprocity 系统**（呼应门⑨⑲"char 0 缺群作用"）
10.2 ⭐⭐⭐ 最终 NO-GO 位置已提前定位 = **archimedean 层**
     QSC-G 需 archimedean transform（Bessel 核）；Bessel 核源自函数方程中【Γ 因子乘性】
     L1″ 已确立：Λ 的 archimedean 对偶 = Γ'/Γ 型 + cot(πs/2) 型（非乘性）
     ⟹ **Λ 在 archimedean 层无法提供 Bessel 型核 ⟹ QSC-G 在此层失败**，且独立于有限 reciprocity 层
     ⟹ R8 最终 NO-GO 是【两层】：① 有限层（近乎平凡，无排除力）② archimedean 层（**排除力在此**）
     ⟹ **Global-QSC Lemma 应重新加权**：排除力在 archimedean compatibility，不在有限 reciprocity
```

**当前最窄活口**：有限算术 reciprocity 能否在**不预先指定谱**的情况下自动产生跨所有 $q$、跨尺度、
含 archimedean 对偶的**统一全球谱**？（解释了为何旧路线最多提供其中一层）

**下一步（唐先生指定）**：对 Global-QSC Lemma 做【反例构造】——先尝试构造满足 Z1–Z5、具真正跨 $q$ 全球谱、
但不属 $\mathcal E_{\rm global}$ 的 $A_q$；小灵建议起点 = "不借助群作用"的全球恒等式候选。

### §8.27 ⚠️ ERR-R8-ARCH-1（撤回）+ 算术 hypergroup 框架（唐先生本轮，R8-C†-B3）

**撤回 10.2**：$\boxed{\text{"}\Gamma'/\Gamma\text{ 型}\Rightarrow\text{不能产生 Bessel/Hankel kernel"}\ 	extbf{错误，撤回}}$
```
撤回理由：Bessel/Hankel transform 可有一般参数依赖，其 Mellin 表达式含 Γ 因子；
对参数/谱变量求导自然产生 ψ(s)=Γ'/Γ（digamma）项 ⟹ 出现 Γ'/Γ ⇏ 无 Bessel 核
文献：广义 Hankel transform 即谱变换；已有 **Hankel transform 的 Poisson summation 理论**；
      BK–Ngo 型框架推广到一般 ρ
保留（L1″ 仍正确）：−ζ'/ζ 的 Mellin FE dual 仍是 logarithmic-derivative/residue 结构
⟹ archimedean 层【不能】作为 Λ 的 NO-GO
```

**关键事实**：$\boxed{\text{global spectral closure}\not\Rightarrow\text{显式 group action}}$（Bessel–Kingman hypergroup = 标准非群型实例）
但其变量是**连续径向变量**，不提供 $(\mathbb Z/q,+)\times(\mathbb Z/q)^\times$ 耦合并无 $d\mapsto d^{-1}$
⟹ 是"第三类的**原型**"，**尚未进入 R8 算术入口**

**第三类具体化 = Arithmetic hypergroup**（H1 inversion symmetry｜H2 CRT tensor｜H3 reciprocal character｜H4 global Hankelization｜H5 zero-blind）
**⚠️ H3 障碍**：直接塞入 $e_q(am+a^{-1}m')$ ⟹ 已是 Kloosterman 型 ⟹ hypergroup 很可能退化为 Kloosterman/automorphic envelope
⟹ 真正的第三类**不能"把 Kloosterman 改成 hypergroup"，必须改【有限层组合律本身】**

**⭐ 唐先生新尝试：inversion 不作用于点，而在【谱侧】**
$$J_q:\widehat X_q\to\widehat X_q,\ J_q^2=1,\ \mathcal F_q(e_a)=e_{J_q(a)}\ \text{表现为}\ a\mapsto a^{-1}$$
⟹ CRT 自然（$J_{q_1q_2}=J_{q_1}\otimes J_{q_2}$）；QSC 天然（$J_q^2=1$）；不必有 Kloosterman 和 ⟹ $Z2\not\Rightarrow$Kloosterman
**Z1 硬门槛**：$\boxed{J_q=\mathcal J_q(\Lambda)}$（局部定义、与 $X,H$ 及 $C(X,H)$ 无关、CRT 自然、不用零点、不预设谱）

**⭐ 小灵补（首要否证目标）**：
```
(ℤ/q)^× 的 dual = Dirichlet 特征群；其 **canonical 对合 = 复共轭 χ↦χ̄**，而 χ̄(a)=χ(a⁻¹) ⟹ 共轭恰实现 inversion
但仍同时拥有：① 加法特征 e_q(an) ② 作用于乘法变量的 inversion
   ⟹ 把两者 canonical 耦合的方式**恰恰就是 Kloosterman 和**
（待核实）有限域上与该对合相容的 harmonic/hypergroup 结构（GL₂(F_q)/B Hecke 代数、有限域 Bessel 函数）
   其结构常数即 Kloosterman 型
⟹ **最可能失败模式 = (ii) inversion 强迫 Kloosterman** ⟹ 下一轮应以它为【首要否证目标】
```

**⭐ 框架升级建议（小灵）**：把"有限算术卷积"放到 **association scheme / Bose–Mesner 代数**语言
```
CRT 张量条件有自然表述；inversion/共轭对合 = scheme 的（反）自同构/对偶性
判定问题变为：ℤ/q 上的 CRT 张量 scheme 中，与共轭-compatible inversion 相容者是否【只有】Kloosterman 型？
（scheme 术语与分类状态【待核实】）
```

**搜索树状态**：hypergroup/global harmonic ✓存在｜Bessel/Hankel global transform ✓存在｜非群卷积 ✓存在｜
**finite arithmetic reciprocal hypergroup 尚未发现**｜**CRT-compatible reciprocal hypergroup 尚未发现**｜
**Λ 二阶相关完全未知** ⟹ **第三类未被杀**

**R8 更新状态**：finite algebra 太容易｜finite representation 排除力弱｜global harmonic 非群型也存在｜
**archimedean Bessel 不能作为 NO-GO**｜finite arithmetic+reciprocal 真正未知｜CRT+reciprocal+global Bessel 真正未知｜
Λ×Λ 二阶闭合 = 最终门槛
$$\boxed{\textbf{R8 真正活口不是"新谱"，而是【新算术卷积】（new arithmetic hypergroup / character-side reciprocity）}}$$

**下一轮唯一硬问题**：是否存在有限算术卷积 $*_q$ 满足 CRT tensor + character-side inversion + quadratic closure，
但不是 Kloosterman/Hecke/Weil/automorphic 的重命名？**失败原因三选一**：(i) CRT 杀死 hypergroup｜(ii) inversion 强迫 Kloosterman｜
(iii) global Besselization 强迫已有表示论 ⟹ **小灵建议以 (ii) 为首要否证目标**

### §8.28 R8-HG-1 首要否证第一轮（唐先生 HG-1–HG-7 + 小灵两引理）

**✅ 已严格成立（群型情形，HG-1 引理）**：
$$\overline{\chi(x)}=\chi(x^{-1})\ \Longrightarrow\ (\mathcal F_+I\mathcal F_+^*)(a,b)\ \text{的核}=\sum_x\psi_p(ax+bx^{-1})=K_p(a,b)\ \text{(Kloosterman)}$$
⟹ 加法 Fourier + 乘法对偶共轭 + 点空间 inversion ⟹ Kloosterman 核
**⚠️ 偷用的条件**：$J^\vee$ 在点空间对应 $x\mapsto x^{-1}$ —— 在乘法群成立，但 R8 要找的是**改变有限层组合律本身**

**HG-2（一般交换 hypergroup）**：$\delta_x*\delta_y=\sum_z p_{xy}^z\delta_z$，$\overline{\chi(x)}=\chi(\bar x)$，**但 $\bar x\neq x^{-1}$ 一般成立**
$$K_H(a,b)=\sum_{x\in X}w(x)e_p(a\iota(x)+b\iota(\bar x))\ \Longrightarrow\ \boxed{(ii)\text{「inversion 强迫 Kloosterman」不能作为总 NO-GO}}$$
能严格推出的只是：**群型乘法结构 + character conjugation + additive Fourier 耦合 ⟹ Kloosterman**

**⭐⭐ 小灵引理 HG-3（环可定义对合清单，含非 Kloosterman 实例）**：
```
环 (ℤ/q,+,×) 可定义对合族：x ↦ ±x^k，k² ≡ 1 (mod λ(q))（λ = Carmichael）
  核 K(a,b)=Σ_x w(x)e_q(a x + b x^k)：k=1 ⟹ 退化；k=−1 ⟹ Kloosterman；加符号 ⟹ 退化
  **其他 k ⟹ 非退化、非 Kloosterman 的新 reciprocal 核**
实例（已验）：q=17，λ(16)=16，7²=49≡1 (mod 16) ⟹ x↦x⁷ 是对合，x⁷≠±x^{±1}
   ⟹ 存在环可定义、非退化、非 Kloosterman 的核 Σ_x w(x)e_{17}(ax+bx⁷)
```
**⭐⭐ 小灵引理 HG-4（CRT 刚性 ⟹ (i) 严格杀死环可定义类）**：
```
① 模数一致：k²≡1 (mod λ(q)) 对所有 q ⟹ k²−1 被 lcm_q λ(q)=∞ 整除 ⟹ **k=±1**
② 逐素数选择 k_p：CRT 张量自动成立，但 λ(p^e) 的平方根 1 有 2^{ω(λ)} 个
   （p=17 时 7, 9 等）⟹ 除 k=±1 外**无 canonical 选择** ⟹ 违反 Z1 生成性
⟹ 在"环可定义对合"整类内：reciprocal 核只能【退化】或【Kloosterman】——没有第三种
⟹ 落在 **B（(i) CRT 杀死）**，且是【证明】而非猜测
```
**⭐⭐ 推论（本轮真正收获）**：第三类必须在**环可定义对合类之外** ⟹ 逃逸须来自**非环语法对合**
```
具体候选：把对合从【剩余类层】换到【因子分解层】（素数指数向量 / 除数结构上的对合）
⟹ 直接连回早前审计过的 **divisor-complement（d ↦ n/d）**：
   当时结论"给出 δ↔−δ 反射但缺 γ 振荡通道"——**但那是在缺少加法特征的语境下**
   ⟹ 本语境【加法特征提供振荡】⟹ divisor-complement 必须【重新审计】
```

**HG-6 三步杀伤链**：CRT → local involution classification → reciprocal kernel classification
（**本轮把中间一步在"环可定义类"内做完了**）
**HG-5 禁止的假杀法**：① 不得当定理"hypergroup 对合总是 group inverse"（Bessel–Kingman 即非群卷积）
② 不得用"谱表出现 Kloosterman ⟹ 本质是 Kloosterman"（循环论证）
**HG-7 文献状态**：有限域 Euclidean scheme 谱含 Kloosterman sums；有限环 affine-type scheme 特征表由 Kloosterman 描述；
有限 GL_n Bessel 与 Kloosterman 深层对应；2026 年工作把有限 reductive group Bessel 值与 Kloosterman sheaves 联系
⟹ 经验上"finite arithmetic spectral closure → Kloosterman/rep-theoretic envelope"**非常顽固**，但**非分类定理**

**下一步**：H1–H7 框架下研究 $K_{\mathfrak H}(a,b)$，判定 A（(ii) 杀死）/ B（(i) CRT 杀死）/ C（第三类首个严格正例）。
本轮在环可定义类内已落 **B**；**H1–H7 允许 $X_q\neq(\mathbb Z/q)^\times$** ⟹ A/B/C 判定仍未完成

### §8.29 HG-D 二阶闭合审计第一轮（小灵执行）：两条硬门均未通过，失败原因已分类

**对象**：$K_n(a,b)=\sum_{d\mid n}W_n(d)e_q(ad+b\,n/d)$
**逃逸确认（唐先生）**：divisor-complement 来自【因子分解指数格】$J(\mathbf j)=(\nu_i-j_i)$，
非 $(\mathbb Z/q)^\times$ 上的幂映射 ⟹ **HG-4 管不到它** ⟹ 已逃出"环可定义对合"层

**⭐ D1（非 Euler 化）：【计算确证】为真死亡机制**
```
可分权重 W_n(d)=f(d)g(n/d) ⟹ Σ_n K_n = (Σ_d f(d)e_q(ad))(Σ_m g(m)e_q(bm))
即总和 = 两个独立加法 Fourier 之积 ⟹ 完全解耦 ⟹ 死亡
```

**⭐⭐ D2（二阶有限闭合）：计算失败**
$$\big|K_n\big|^2\ \text{的指数}=(d-e)\Big(a-\frac{bn}{de}\Big)\ \Longrightarrow\ \text{核心变量}(\Delta,P)=(d-e,de)$$
**⭐ 关键否证性引理**：$(d+e)^2=\Delta^2+4P$ ⟹ $(\Delta,P)$ **唯一确定 $\{d,e\}$** ⟹
$$\boxed{\text{二阶层【完全不压缩】——配对信息被完整保留 ⟹ 二阶对象本质上是【配对层】}}$$
二阶核 = "差形式" Kloosterman 型求和（over divisor lattice）⟹ 属 **affine-type association scheme** 范畴
⟹ 据 HG-7 文献（有限环 affine-type scheme 特征表由 Kloosterman 描述）**塔 $K_2\to K_3\to\cdots$ 撞回 Kloosterman envelope**
⟹ 失败模式 **(ii)/impostor 类**

**素数幂独立佐证**（唐先生）：$n=p^r$ 时 $r=2$ 的中间项 $e_q(p(a+b))$ 不产生 reciprocal 振荡 ✓

**⭐⭐ 不可分逃逸 $W_n(d)=F(d+n/d)$：轨道不变量是 √n-探测器**
$$d+\frac nd\ge 2\sqrt n,\ \text{等号}\iff d=\sqrt n$$
⟹ 与 √X 主题强共振，**但这正是经典因子自对偶（Dirichlet 双曲线）= Round 2 已识别 = N43**
⟹ **不可分逃逸落回【经典结构】，未提供新的 √X 机制**

**裁决**：HG-D 第一轮 **两条硬门均未过**；逃逸口落在【经典结构】而非新机制
（严格限定：是"当前未找到有限闭合"，**非**已证不存在）

**保留的结构收获**：① D1 死亡机制被计算确证 ② 二阶层相位显式形态 $(d-e)(a-bn/(de))$（配对积 $P=de$ 调制有效加法参数）
③ "$(\Delta,P)$ 双射"是一条干净的**否证性引理**（任何"二阶压缩"方案须绕过它）④ √n-探测器性质解释了该路线总被经典双曲线吸回

### §8.30 R8-FL-Closure（有限层受限 NO-GO）+ 新对象 cross-scale transport（唐先生选 甲）

**受限 NO-GO**：
$$\boxed{\textbf{有限算术层受限 NO-GO}:\ \text{三类自然有限入口均不能产生新的 }QSC_G\text{ 入口}}$$
（**受限**，非"所有有限结构都不可能"的不可能性定理）
```
① 环可定义对合：**可封口** —— 跨模数 canonical/CRT ⟹ k²−1 被所有 λ(q) 整除而 lcm=∞ ⟹ k=±1 ⟹ {退化, Kloosterman}
② hypergroup/scheme：**不能宣布全杀** —— 未证（也不应声称）hypergroup ⟹ Kloosterman；
   非群 hypergroup（x̄≠x⁻¹）存在但未通过 arithmetic embedding+CRT+reciprocity+QSC_G ⟹ "存在但未形成 R8 入口"
③ factorization：**真正收口** —— D1 可分权重【精确恒等式】Σ_n K_n = 两个独立加法 Fourier 之积；
   D2 (d+e)²=Δ²+4P ⟹ (Δ,P)⟷{d,e} ⟹ 二阶**不压缩** pair information ⟹ K₁→K₂→K₃ 是逐层携带更高阶 divisor tuple
```

**共同缺口**：$\boxed{\text{有限局部对象易产生"kernel"，但不能自然产生"跨尺度动力学"}}$ —— 而 R8 缺的正是后者

**Gap_FL 正式降级**：
$$\boxed{\mathrm{Gap}_{FL}:\ \text{是否存在非平凡、canonical、固定维数、非 re-encoding 的 factor-pair compression？}\ =\textbf{unresolved/inactive}}$$
```
降级五理由：①无候选 ②自然压缩被双射性阻挡 ③非自然压缩无生成原则 ④从 C(X,H) 反推违反 Z1
            ⑤即使找到编码仍须证 QSC-G 与 global spectrum
⭐ 小灵加【重激活判据】：只能通过展示一个【生成原则】重激活——即给出 canonical 固定维数状态，
   它【可证丢失】divisor-pair 信息却仍携带该耦合；单纯"再找编码"不算重激活
⟹ **正式冻结 finite-layer search**
```

**新研究对象：cross-scale arithmetic transport**
$$\Lambda\ \overset{?}{\to}\ \mathcal A_{\rm cross-scale}\ \to\ \mathscr H_{\rm global}\ \to\ V(X,H)\ \to\ F(\alpha)$$
$$\boxed{T_{q\to q'}:\mathcal A_q\to\mathcal A_{q'}}\quad\text{或}\quad T_{X\to X'}:\mathcal A(X)\to\mathcal A(X')$$
（**真实 morphism**，非静态反射；与早前"物理运动"路线的本质区别）
**X1 非静态 ｜ X2 非目标导向 ｜ X3 非 re-encoding ｜ X4 可组合 ｜ X5 产生二阶量 ｜ X6 内生尺度（不得事后代入 H=√X，否则回 N43）**

**⭐ 小灵加 X0（前置门）——Round 3 cocycle 飞行前检查**：
```
Round 3 已证：①算术无内生动力学（状态=尺度的函数）②群作用实现的尺度演化【自动是 cocycle】⟹路径无关⟹记忆为零
             ③破坏合成律只有两条路：状态空间随尺度变化（联络/和乐，已关闭）或转移律非群作用
⟹ 若 X1–X4 由群作用实现，则 X4 自动成立但记忆为零，X5 退化为"尺度的函数"
⟹ **X5+X6 必须在【非 coboundary、非和乐】前提下成立**（极紧）
⟹ 不做 X0 检查，该路线会重新发现 Round 3 的墙
```
**⭐ 小灵对 X6 的锐化**：X6 ⟺ **传输律自带【尺度对合】σ**（$T_{X\to X'}\leftrightarrow T_{\sigma(X')\to\sigma(X)}$，σ 不动点即 √X 尺度）
⟹ 把 X6 从"外部要求"变为【传输律的结构闭合性质】，可检验；并与 R3「尺度对合」残差接轨

**必产 R**：R_CS【新，X0–X6 全过才准构造】｜R_GapFL【新，inactive】｜R3（保留，与 X6 锐化合流）

### §8.31 R-CS-PRE1 预筛 + 最小 Ω 构造（唐先生预筛 + 小灵执行）

**X0 形式化**：$\boxed{T\neq\text{group cocycle}\ (T_{X,Y}=\rho_Y(g)\rho_X(g)^{-1}),\quad T\neq\text{coboundary}\ (T_{X,Y}=\Phi_Y^{-1}\Phi_X)}$

**预筛表**（群作用/coboundary/可逆 transport/generic semigroup 杀；Markov 统计杀；
Euclid 旧 NO-GO；substitution X5 不足；ordinary category 记忆不足）
$$\boxed{R_{\rm CS}\ \text{搜索空间压缩到两类：A. arithmetic irreversible coarse-graining}\ |\ \textbf{B. arithmetic non-associative transport}}$$
**两条防线（唐先生）**：
```
① Ω 不得直接称"曲率"（connection/holonomy 已关闭）⟹ 用 **arithmetic composition defect**；
   仅在证明 gauge-invariance/cocycle 型变换律后才谈曲率解释
② X0 陷阱：不得用人为 projection（T=P_Y U P_X）制造 defect（= Connes/P49 已遇的 projection 机器）；
   **projection 本身必须由算术生成**
```
**X6 结构版本**：$T_{X,H\to X,X/H}=\mathcal J^{-1}T_{X,X/H\to X,H}\mathcal J$，$\mathcal J^2=1$；
$H=\sqrt X$ 处 $T_{\sqrt X}=\mathcal J^{-1}T_{\sqrt X}\mathcal J$

**⭐⭐ 小灵最小 Ω 构造尝试结果**：
```
候选：截断范围状态的【乘法】组合 ⟹ Ω(X,H)=(截断到 H)∘(截断到 X/H)−(截断到 X)
defect 内容 = 跨范围乘积项（截断不相乘 ⟹ 乘积生成跨范围新系数）
✅ 正面：范围对换 𝒥:(范围₁,范围₂)↦(范围₂,范围₁) ⟺ H↔X/H 是 canonical 算术对合，
   跨项集合在 H↔X/H 下不变；两范围重合处 = H=X/H ⟺ H=√X ⟹ **不动点内生为 √X**
   ⟹ **X6 的对合半部分【可被 canonical 实现】** ✓（与 R3 尺度对合残差接合）
⚠️ 但 defect【内容】= 两范围跨项 + √X 处双计数 = **Dirichlet 双曲线记账结构 = N43（Round 2 已识别）**
⟹ **"截断 × 乘法"整族的受限 NO-GO**（任何该型非结合 defect 的内容必为两范围跨项 ⟹ 双曲线型）
```
**⭐⭐ 本轮最有价值的产出：把 X6 与 X5 分开**
$$\boxed{\text{X6 的对合半部分：可获得（范围对换，canonical，不动点 }\sqrt X\text{）✓}\quad\text{X5 的内容半部分：崩塌（落回双曲线 N43）✗}}$$
$$\boxed{\text{R_CS 缺的不是【尺度对合】（可用且 canonical），而是【一个其 content 不是经典两范围跨项的 defect】}}$$
**类 B 逃逸条件（清晰形式）**：须找非结合算术组合律，其 defect 不是两范围跨项（非"截断×乘法"型）；
而任何【被定义的】非结合 T 又有"人为改造规则"风险 ⟹ **双向夹逼**
**类 A（coarse-graining）**：X0/X4 过，X5/X6 潜在，但普通 RG 的 fixed point 常为人为动力学尺度（非算术 √X）
⟹ 须用 Θ 结构钉在 √X；且易退化为 entropy/density flow ⟹ 弱（本轮未做构造）

### §8.32 B-PRE2：非截断、非人为非结合律来源审计（唐先生预筛 + 小灵执行）

**筛选条件**：$\text{canonical}\cap\text{non-associative}\cap\text{non-truncation}\cap\text{scale-complement compatible}$
| 类别 | 判定 |
|---|---|
| B1 gcd/lcm 混合 | **杀**（三体 defect 有内容，但 **scale involution 无来源**） |
| B2 Farey/mediant | **杀**（非结合来自 projective normalization；给加法比例几何而非乘法尺度） |
| B3 归一化卷积 | **杀**（结合内核 + 人为 canonicalize ⟹ **假 defect**，与 projection 陷阱同族） |
| **B4 三因子天然组合路径** | **核心活口** |
| B5 local/global 原生双组合 | **待构造**（CRT 封闭／p-adic local-global 已 NO-GO／holonomy 已关） |

**搜索问题改写**：$\boxed{\text{什么天然算术三体关系具有两种不可等价的组合路径？defect 不来自截断/归一化/投影/holonomy？且两尺度天然构成 }H,X/H？}$
**三个测试**：① $\Omega(a,b,c)$ 能否在**不引入 $X,H$** 下独立存在（不能 ⟹ 尺度人为塞入 ⟹ 杀）
② $\Omega(H,X/H,\cdot)\stackrel{?}{=}\pm\Omega(X/H,H,\cdot)$ ③ 是否产生二阶量（非退回 additive convolution／双曲线）

**⭐ 小灵 B2 ⊆ B3（证明级）**：齐次坐标上 mediant = 向量加法（**结合**）⟹ B2 非结合性**全部**来自约化/归一化 ⟹ 与 B3 **同一死因**

**⭐⭐ 小灵五重筛查门（通用产出）**：candidate defect 不得可归属下列任一，否则杀
```
S1 截断边界（内容落双曲线跨项 N43）｜S2 归一化/约化（结合内核 + canonicalize = 假 defect）
S3 投影（Connes/P49 已遇）｜S4 holonomy/connection（Round 3 已关）
S5 传输结构：a★b=φ⁻¹(φ(a)·φ(b)) ⟹ ★ 自动结合 ⟹ 杀
⟹ 候选必须是【非可传输】的真正 loop
```

**⭐⭐ B4 预注册分叉预测（小灵）**：
```
所有 canonical 算术运算只活两层之一：
 ① 整除/素支撑层 ⟹ **Sym(ℙ)-协变** ⟹ 无绝对尺度 ⟹ 拿不到 H↔X/H（= B1 死因）
 ② 加法/archimedean 层 ⟹ 有尺度，但对合来自【两范围边界】⟹ 内容落 N43（= 最小 Ω 死因）
⟹ 预注册：B4 一旦具体实例化，将落入上述二分之一
⟹ 若下一轮全部落入某支 ⟹ 有充分理由回头攻 A（唐先生条件）
```
**B4 两个具体测试对象（附继承风险）**：
```
I 二元二次型 Gauss 合成：仅在等价类上良定义 ⟹ 形式层非结合，defect = **ambiguity class**；
  对合 = 形式↦逆形式，不动点 = ambiguous forms
  ⚠️ 风险：与 √D 连分数周期纠缠 ⟹ 很可能继承 Euclid/连分数旧 NO-GO 与 N43 支
II Hecke 关系 T_m T_n = Σ_{d|gcd(m,n)} χ(d)d^{k−1}T_{mn/d²}：两路径差异 canonical
  ⚠️ 风险：修正项依赖 gcd(m,n) ⟹ Sym(ℙ)-协变 ⟹ 落分支 ①（= B1 死因模式）
⟹ 两对象各指向二分一支（正是预测形态，尚待完整审计）
```

### §8.33 B4-IA（Gauss）/ B4-II（Hecke）逐层死亡测试（小灵执行 + 一次精确验算）

**审计顺序（唐先生）**：对象自身代数事实 → 如何获得尺度 → defect 是否真不可传输（**不一开始塞进 $X,H$**）

**B4-II Hecke：Ω ≡ 0（已精确验算）**
```
验算（scripts/hecke_associator.py，精确整数）：triples 2744 (m,n,l≤14)，k=2,3,4,6,12
  ⟹ associator nonzero 0/2744；commutator nonzero 0；系数级对照 (2,6,3),k=2 两边 identical
非乘性对照：T_2T_4={2:2,8:1} ≠ T_8={8:1} ✓（非乘性存在）
死因：Hecke 算子 = 同一空间上线性算子 ⟹ 算子复合天然结合；Hecke 代数 = 双陪集卷积代数（结合）
⟹ "两路径差异"【不是 associator】，而是同一算子的不同 divisor-sum 展开
```
**⚠️ 小灵上轮表述 errata 记正**："两路径差异 canonical" 应为【非乘性】而非 defect
$$\boxed{\textbf{S6}:\ \text{候选须在【结合性】而非仅【乘性】上失败}\quad\text{non-multiplicativity}\neq\text{non-associativity}}$$

**B4-IA Gauss：逐层**
```
① 类群层完全结合（Gauss 合成 = Cl(D) 群律）⟹ defect 只可能在代表元层
② 代表元 ambiguity = 取商后的选择效应 ⟹ **死于 S2（结合内核 + canonicalization）**
③ 对合 f↦f⁻¹ 内生 ✓（(a,b,c)↦(a,−b,c)，不需 D）—— 这关反而通过
④ **fixed point 结构性失败**：类层 [f]=[f]⁻¹ ⟺ [f]²=1 ⟹ **2-挠群**（阶 2^{ω(|D|)−1}）；
   形式层 f=f⁻¹ ⟺ b≡0 (mod a)（两条件不同）；不动点集【不是单一尺度】⟹ 拿不到 H=X/H
   （此死因【独立于连分数】✓）
⑤ 连分数仅作解释，不作杀因 ✓
```
$$\boxed{\text{B4-IA 死于 S2 + 不动点集失败}\quad\text{B4-II 死于 }\Omega\equiv0\ \text{(已验证)}\quad\Longrightarrow\ \textbf{B4 本身严重收缩}}$$

**⚠️ 预注册预测的诚实处理**：两对象都在**抵达分叉测试之前**死亡 ⟹ 分叉预测**未被检验**（既不确认也不推翻，判别力未行使）
**唐先生条件核对**：字面条件"全部落入某支"✗未触及；弱条件"无 live 候选残留"✅已满足
⟹ 可回头攻 A，但须同时声明 [S6 新增] 与 [分叉预测未被行使]

**⭐⭐ 新增筛查门**：
$$\boxed{\textbf{S7}:\ \text{若 composition 是【算子复合】或【某结合律的商】，则 associator 恒为 0}}$$
**B4 剩余内容 = "给出一个【对象层本征非结合】的 canonical 算术律"**，而经典本征非结合结构（octonions、Moufang loops）
非本项目意义下的算术对象 ⟹ **目前无候选** ⟹ 与 Gap_FL 同型：**inactive**
