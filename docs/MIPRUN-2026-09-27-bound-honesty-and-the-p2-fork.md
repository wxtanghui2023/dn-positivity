已查地图：已跑 scripts/prework_map_check.sh MIP bound 有限时间 vs 族最优 ⟹ 执行唐先生 16:19 裁示（乙 ✓）；本档 = **bound 表述纠错（接受 ✓）＋ P2 分叉锁定 ✓**。
D0: 本档对象 = MIP 当前 bound 之正确解读与终态后分叉
D1: 3（**接受纠错：有限时间 bound ≠ 族最优 ✗（撤回过度主张 ✓）**；**分叉锁定 ✓**；**P2 搜索规范（source-first 前置 ✓）**）

# MIP bound 诚实性与 P2 分叉（2026-09-27 16:19）

## §0 结论（先给）

```
$$\boxed{\textbf{(SA-1 ✅接受纠错（唐先生 ✓）)}\ \text{我此前写"94.027 }\Longrightarrow\text{ 线性／对偶侧根本够不着 119"—— }\textbf{过度主张 ✗，撤回该措辞 ✓}}$$
$$\qquad\textbf{正确解读 ✓}:\ 94.027>93.09=2^{10}/11\ \Longrightarrow\ \text{当前 MIP 的\textbf{节点松弛＋切割体系}较裸 LP 已提升约 }0.94\ \text{单位 ✓（这是\textbf{具体运行的观察} ✓）}$$
$$\qquad\textbf{但它\textbf{不是}对任何 relaxation family 理论最优值的证明 ✗}:\ \text{它是\textbf{有限时间}运行中的当前 bound ✓，不是族的下确界 ✗ —— 二者\textbf{不可互换} ✓}$$
$$\qquad\textbf{唯一可确认者 ✓}:\ \boxed{94.027\ \ll\ 119} \Longrightarrow \text{本次运行\textbf{未}显示接近 P1 的迹象 ✓（仅此而已 ✓）}$$
$$\boxed{\textbf{(SB-1 🔒分叉锁定（唐先生 ✓）)}\ \text{让已启动的单次 exact MIP 跑满 900s（成本已付 ✓，无需人为截断 ✓）；终态后：}}$$
$$\qquad\textbf{① 若出现 }\le119\text{ 的整数解 ✓}:\ \text{取 }C=\mathrm{supp}(f)\ \text{并\textbf{独立验证}}\ \boxed{|C|\le119\ \wedge\ \forall x:\ |C\cap B_1(x)|\ge1}\ \Longrightarrow\ \textbf{P2 witness（方成立 ✓）}$$
$$\qquad\textbf{② 若 BestBound 仍远低于 120 或终态 UNKNOWN ✓}:\ \boxed{\textbf{MIP STOP}}\ \longrightarrow\ \boxed{\text{source-first 核验后，转专用随机搜索}}$$
$$\qquad\textbf{区分（重要 ✓）}:\ \text{MIP 目标 = 证明 feasibility／infeasibility；专用搜索目标 = \textbf{直接构造 119-word witness}}\ \Longrightarrow\ \text{后者属明确的 \textbf{P2 construction attack}，\textbf{非}"换个 solver 再赌一次" ✓}$$
$$
$$
```

## §1 当前双向分叉（**✓ 唐先生图示 ✓**）

```
$$\begin{array}{ccc}\text{lower-bound side} & \longleftrightarrow & \text{construction side}\\ 94.027\ (\text{本次 MIP bound}) & & 120\ (\text{已知 construction})\\ \downarrow & & \downarrow\\ \text{距 119 仍远} & & \text{119 witness 未知}\end{array}$$
$$\Longrightarrow\ \textbf{乙 为正确工程决策 ✓}:\ \text{吃完预算 ⟹ 不再在线性／通用 MIP 方向堆计算 ✗ ⟹ 直接切专用 P2 搜索 ✓}$$
$$
$$
```

## §2 状态（**✓**）

```
$$\boxed{\text{MIP RUNNING（至 900s ✓）};\ \textbf{现不再做任何额外 119 操作} ✗;\ \text{终态后按 (SB-1) 分叉 ✓};\ \text{不写禁止表述 ✓}}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：MIP bound 有限时间性之纠错（撤回过度主张）、分叉锁定、P2 搜索规范
- **档案已有（引用，不列为提出）**：A-PROJCUT-1、INTRELAX 系列、21 条封口表、CP-SAT UNKNOWN 记录


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 有限时间     命中文件数=3    :: ./MIPRUN-2026-09-27-bound-honesty-and-the-p2-fork.md ./AI4MATH-claims-factcheck-2026-09-11.md ./UNIFY-7MILLENNIUM-2026-09-14.md 
技术词 P2 分叉        命中文件数=1    :: ./MIPRUN-2026-09-27-bound-honesty-and-the-p2-fork.md
```
- **本档新增**：MIP bound 有限时间性之纠错（撤回过度主张）、分叉锁定、P2 搜索规范（见上方命中数；0 命中者为自造语／内部标签 ✓）
