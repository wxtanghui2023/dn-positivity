已查地图：已跑 scripts/prework_map_check.sh K(10,1) 中点 support 2-face square Sidon ⟹ 执行自 `docs/SCOL-2026-09-26-...md`（行闭合 ✓）＋ `docs/TCOLL-2026-09-26-...md`（中点对偶 ✓）＋ `docs/HQ1-2026-09-26-...md`（Haas STOP ✓）；本档为**纯推导**（唐先生 2026-09-26 20:13 指令「开 K-1，先钉死 2A₂−3 是否真的是 distinct support demand」✓）；**未跑程序** ✓。
D0: 本档对象 = `Q=1` 分支的中点 distinct support 需求（既有对象；非新对象）
D1: 0（产出为 distinct support 精确值、load 自动满足判定、一处自我否证与 STOP 结论）

# MIDSUP-2026-09-26 · K-1.1：中点 distinct support 的钉死

## §0 结论（先给）

```
$$\boxed{\textbf{(M-1 distinct support 已钉死)}\ M_2^{\rm dist}=\#\{x\notin C:b(x)\ge2\}=(283-2A_1)+1=\mathbf{284-2A_1}\ \ge\ \mathbf{166}\ ✓✓\ (\text{分支 A})}$$
$$\qquad(\text{且它就是}\ \{\text{b=2 非码字}\}\cup\{z\}\ ✓;\ \text{全为\emph{distinct}点}\ ✓\ \text{—— "distinct support demand" 成立}\ ✓)$$
$$\boxed{\textbf{(M-2 load 侧自动满足)}\ \text{每个中点的覆盖者\emph{恰是其定义对的 2 个端点}}\ ⟹ \textbf{无需第三方覆盖}\ ✗\ \Longrightarrow\ \text{load 计数闭合为恒等式}\ ✓✓}$$
$$\boxed{\textbf{(M-3 判定)}\ \text{按唐先生 STOP 条件（"只得 incidence 恒等式即停"）}\ ⟹\ \textbf{K-1.1 即 STOP}\ ✗✓}$$
$$\boxed{\textbf{(M-4 自我否证)}\ \text{我中途试图用 "Q=1 ⟹ C 无 2-面" 推 Sidon 界（}\le45\text{）}\ ✗\ \textbf{该主张错误，已弃}\ ✓✓}$$
$$
$$
```

---

## §1 (M-1) distinct support 的精确值（本档核心 ✓）

```
$$\textbf{中点定义的精确化}:\ \text{距-2 对}\ \{c,c'\}\ \text{的中点}\ =\ \{m:d(m,c)=d(m,c')=1\}\ \text{恰 2 个}\ ✓\ (\text{TCOLL (E-1)}\ ✓)$$
$$\textbf{计费对象}:\ \text{"需落在支撑上的 }L_2/L_4\text{-type 中点"}\ \text{—— 本档先不预设层限制（见 §3 修正）}\ ✓$$
$$\textbf{支撑集（branch A，}\ z\notin C\ ✓）:\ \text{距-2 对的全部中点}\ =\ \{x\notin C:\ b(x)\ge2\}=\underbrace{\{b=2\ \text{非码字}\}}_{283-2A_1}\cup\underbrace{\{z\}}_{b=3}\ ✓✓$$
$$\qquad(\text{每}\ x\notin C\ \text{满足}\ b(x)\ge2\ \text{必为某距-2 对的"中点"}\ ✓\ \text{因}\ \binom{b(x)}2\ge1\ \text{且覆盖者两两距 2}\ ✓)$$
$$\Longrightarrow\ \boxed{M_2^{\rm dist}=284-2A_1}\ ✓✓;\quad \text{由}\ A_1\le59\ \Longrightarrow\ M_2^{\rm dist}\ \ge\ \mathbf{166}\ ✓✓$$
$$\textbf{与 incidence 的关系}:\ \sum_{\text{距-2 对}}2=2A_2=\sum_{m}\#\{\text{该 }m\text{ 服务的对数}\}=(283-2A_1)\cdot1+3\ \Longrightarrow\ 2A_2=286-2A_1\ \Longrightarrow\ A_1+A_2=143\ ✓$$
$$\qquad\Longrightarrow\ \text{incidence 数}\ 2A_2-3=283-2A_1=M_2^{\rm dist}-1\ ✓\ (\text{与唐先生预期一致}\ ✓)$$
$$
$$
```

**⟹ (M-1) 成立**：$2A_2-3$ **确实**对应 distinct support（差一个 $z$ ✓），不是纯 incidence 虚数 ✓。

---

## §2 (M-2) load 侧为何自动满足（STOP 的直接原因 ✓）

```
$$\textbf{关键}:\ \text{设}\ m\ \text{是距-2 对}\ \{c,c'\}\ \text{的中点}\ ✓\ \Longrightarrow\ c,c'\in B_1(m)\ \Longrightarrow\ b(m)\ge2\ ✓\ \text{且其覆盖者恰为}\ c,c'\ ✓✓$$
$$\qquad\text{即}:\ \text{中点的"被覆盖需求"由\emph{定义对本身}\ 满足}\ ⟹\ \textbf{不产生对第三方码字的额外需求}\ ✗✓$$
$$\textbf{故}:\ \text{"required load"}=\text{"available load"}\ \text{逐点相等}\ \Longrightarrow\ \text{总量侧恒等式}\ ✓\ \text{（无松弛可挖）}\ ✗$$
$$\textbf{唯一例外}:\ z\ (b=3)\ \text{服务 3 对}\ ✓\ \text{—— 但这是唯一}\ b{=}3\ \text{点，已被 Q=1 吸收}\ ✓$$
$$
$$
```

**⟹ 按唐先生 STOP 条件**：得到的是恒等式 ⟹ **立即 STOP** ✓（不再推向全局 163 ✓）。

---

## §3 修正：中点的"层限制"不成立（K-1.2 前提不成立 ⚠️）

```
$$\textbf{#14 稿的框架}:\ \text{"中点须落在}\ L_2/L_4"\ ✓\ \text{—— 这只在}\ T\ \text{内部子族成立}\ ✗$$
$$\textbf{一般情形}:\ \text{距-2 对}\ \{c,c'\}\ \text{的中点}\ m_1=c\oplus e_i,\ m_2=c\oplus e_j\ (c'=c\oplus e_i\oplus e_j)\ \text{—— 与}\ z\ \text{的层位置无固定关系}\ ✗✓$$
$$\qquad\Longrightarrow\ \text{"available}\ L_2\ \text{capacity}\ 21-\rho"\ \text{不能用于全局中点需求}\ ✗\ \text{（该框架仅限 T-子族}\ ⚠️）$$
$$\textbf{层无关的替代}:\ \text{真正的"容量"是}\ \#\{x\notin C\}=\mathbf{905}\ \text{—— 而需求}\ 166\ll905\ ✗\ \text{（差 5.4 倍）}\ ✓$$
$$
$$
```

---

## §4 (M-4) 自我否证：中途的 Sidon 过度主张 ✗（必须记录 ✓）

```
$$\textbf{中途思路}:\ \text{由 "Q=1}\Longrightarrow\text{无}\ 2\text{-面}\Longrightarrow\text{无 4 点和为零}\Longrightarrow\text{Sidon}\Longrightarrow |C|\le45<119\ \Longrightarrow Q=1\ \text{不可能}"\ ✗✗$$
$$\textbf{错在第几步}:\ \text{"中点不能是码字"}\ \text{确实成立}\ ✓,\ \text{但它只排除}\ \textbf{单位向量张成的 2-面（字面正方形）}\ ✓,\ $$
$$\qquad\textbf{不}\ \text{排除一般 2-面}\ \{v,v\oplus p,v\oplus q,v\oplus p\oplus q\}\ \text{（}|p\oplus q|\ge3\ \text{时其对角线不贡献中点）}\ ✗✓$$
$$\textbf{反例（本档自给）}:\ \text{全体奇权点（}512\ \text{个}\ ✓）\ \text{不含任何字面正方形}\ ✓\ \text{（权奇偶性破坏正方形）}\ ✓\ \Longrightarrow\ \text{该条件近真空}\ ✗✓$$
$$\qquad\Longrightarrow\ \textbf{"Sidon 界}\le45"\ \text{无效，}\ \text{"Q=1 不可能"}\ \textbf{不得主张}\ ✗\ \text{（已撤回）}\ ✓✓$$
$$
$$
```

---

## §5 判定与链状态

```
$$\textbf{K-1.1}:\ \text{distinct support 成立（}284-2A_1\ge166\ ✓\text{）但 load 自动满足} \Longrightarrow \textbf{STOP}\ ✗✓$$
$$\textbf{副产物}:\ \text{① 中点覆盖者＝定义对端点（普适局部事实）}\ ✓\ \text{② 层限制框架仅限 T-子族}\ ⚠️\ \text{③ 一处自我否证记录}\ ✓$$
$$\textbf{累计}:\ \text{与 AMEND-30／GRAMSIGN／ISOB3／TCOLL／SCOL／HQ1 同向}\ \Longrightarrow\ \text{第 \textbf{7} 次汇合}\ ✓✓$$
$$
$$
```

**更新链**：

```
P0 119/Q=1 归约 ✓ ｜ P1 理论障碍 ★（未破）
 ├ 匹配 A₁≤59/60 ✓ ｜ A₂=143−A₁ ✓ ｜ Type III 排除 ✓ ｜ 50+7 强制 ✓ ｜ |C∩L₃|≤80 ✓
 ├ T-collision（上界）✗ ｜ SCOL 行闭合 ✓ ｜ HQ1 STOP ✗
 └ K-1.1 distinct support ✓ 但 load 自动满足 ⟹ STOP ✗
P3 collision ✗ ← 缺口不变
```

---

## §6 本档对缺口的最终刻画（第 7 次同向 ⟹ 应作结论）

```
$$\boxed{\text{缺口的唯一形态}:\ \text{一条\emph{不}能被"逐点 load 自动满足"吸收的支撑约束}\ ✓}$$
$$\qquad\text{已穷尽}:\ \text{线性求和（AMEND-30）｜二次符号（GRAMSIGN）｜双计数（ISOB3）｜packing 方向（TCOLL）｜行闭合（SCOL）｜Haas×Q1（HQ1）｜中点 load（MIDSUP）}$$
$$\qquad\text{共同特征}:\ \text{每一条在\emph{逐点}层面都\emph{自动满足}或\emph{方向相反}；}\ \text{能产新强制量的机制只给}\ O(1)\ \text{个点（7/18/50/57）}\ ⟹\ \text{与 905 量级差 16 倍}\ ✗$$
$$
$$
```

---

## §7 建议（需唐先生拍板 ✓）

```
$$\textbf{L-1}:\ \text{把 119 线记为\ "}\ \textbf{结构未闭合；七类机制均不足}\ "\ \text{并\textbf{结题归档}（写入 CLOSED-ROUTES-MAP 与总图）}\ ✓\ \text{—— 但不写"不可能"}\ ✓$$
$$\textbf{L-2}:\ \text{转\textbf{文献侧}：查 2024–2026 是否有把 }K(10,1)\ \text{推到 120 或 119+\ 的新结果（AMEND-20 family-literal）}\ ✓$$
$$\textbf{L-3}:\ \text{若唐先生认为值得，把本线全部资产（匹配定理／Type III 排除／行闭合／中点对偶／7 次汇合记录）打包为独立小论文或技术报告}\ ⚠️\ \text{（需先做新性审计）}$$
$$
$$
```

---

## §8 边界（诚实标注）

- §1 的 (M-1) 为**严格推导** ✓（用 $x\notin C,\ b(x)\ge2\Rightarrow$ 必为某距-2 对中点 ✓）
- §2 的 (M-2) 为**本档核心判定** ✓（中点覆盖者＝定义对端点 ✓ —— 这同时是对唐先生"第三方覆盖"假设的**否定** ✓）
- §3 的层限制修正为**框架撤回** ⚠️（仅 T-子族成立 ✓）
- §4 的自我否证为**本档自抓并撤回** ✓（不保留错误主张 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 中点 distinct support 钉死 命中文件数=1    :: ./MIDSUP-2026-09-26-midpoint-distinct-support.md 
技术词 中点 load 自动满足 命中文件数=1    :: ./MIDSUP-2026-09-26-midpoint-distinct-support.md 
技术词 字面正方形真空性 命中文件数=1    :: ./MIDSUP-2026-09-26-midpoint-distinct-support.md
```
- **本档新增**：中点 distinct support 钉死、中点 load 自动满足、字面正方形真空性（见上方命中数）
- **档案已有（引用，不列为提出）**：$2A_2=3+(283-2A_1)$、$B_1\cap B_1$ 基数、Sidon 概念
