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
