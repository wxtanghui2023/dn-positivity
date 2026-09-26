已查地图：已跑 scripts/prework_map_check.sh 同余 Haas Habsieger 分类 nearly-perfect ⟹ 执行自 PATHMAP-2026-09-26 档；本档为**同余压缩第一轮：一处撤销 ＋ 一处文献决定性命中**（唐先生 2026-09-26 11:58 指令）；纯推导，未动 solver ✓。
D0: 本档对象 = Haas/Habsieger 同余的适用条件核实，与 (8,32)_1 的 nearly-perfect 分类对接（非新对象）
D1: 1（新增独立文献接口：R=1 nearly-perfect 完全分类 ⟹ (8,32)_1 的 d≤2 ✓）

# CONGRUENCE-2026-09-26 · 撤销 ＋ nearly-perfect 命中

## §1 ⛔ **撤销**：PATHMAP §3 的"n=8 适用三进制同余"结论**错误** ✗

```
$$\text{我上档写}: n=8\equiv-1\ (\mathrm{mod}\ 3)\Longrightarrow\text{Haas 三进制同余适用}\ ✗\ \textbf{错}$$
$$\textbf{逐字依据}（\text{Wu--Chen, arXiv:2203.16901v6}\ ✓）:\ \text{Habsieger (1997) 定理}: \textbf{"When }n\text{ is a multiple of }6\text{"}\ ✓$$
$$\qquad \delta_{N[v]}(D)\equiv1\ (\mathrm{mod}\ 2)\ (v\notin D);\quad \delta_{N[v]}(D)\equiv0\ (\mathrm{mod}\ 2)\ (v\in D);\quad \delta_{N_1[v]}(D)+\delta_{N_2[v]}(D)\equiv\cdots\ (\mathrm{mod}\ 3)$$
$$\Longrightarrow\ \textbf{适用条件是 }6\mid n\ ✗\ ——\ n=8\ \text{不满足}\ ✗\ (\text{与 }n=10\ \text{同样不满足}\ ✓)$$
$$\textbf{教训}: \text{正是唐先生"不凭记忆、必须逐字核对"的价值}\ ✓✓\ （\text{我凭记忆的适用条件错了}\ ✗）$$
$$\text{（另: 我档案中对同一同余的出处记录互相矛盾（Haas 2013 / Habsieger 1997）}\ ⚠️\ \text{—— 本轮已澄清为 Habsieger 1997}\ ✓）$$
```

## §2 本轮**自证**结果：算术普查（无 solver ✓）

```
$$\text{剖面} = n_\delta\ (\delta=0..8)\ \text{非负整数};\quad \sum_\delta n_\delta=256,\quad \sum_\delta\delta\, n_\delta=32,\quad \sum_\delta\delta^2 n_\delta\equiv0\ (\mathrm{mod}\ 4)\ ✓$$
$$\text{枚举（32 的 }\le8\ \text{部分分割）}: \textbf{3319}\ \text{个剖面},\ \text{其中 }\textbf{1653}\ \text{个满足 mod 4 约束}\ ✓$$
$$\text{按 }Q=\sum\binom{\delta}{2}n_\delta\ \text{升序}: Q=0\ (\text{全 }\delta\le1\ ✓);\quad \boxed{Q=2:\ \delta=(2,2)\ \text{两点}}\ ⬅\ \textbf{最小违例}\ ✓$$
$$Q=4:\ \delta=(3,2)\ \text{或}\ (2,2,2,2);\quad Q=6:\ (4),\ (3,3),\ (3,2,2,2),\ (2,2,2,2,2,2)\ \cdots$$
$$\boxed{\text{纯算术（}E=32＋\mathrm{mod}\ 4\text{）}\textbf{不排除} Q>0\ ✗\ \Longrightarrow\ \text{必须有几何/结构输入才能杀}\ (2,2)\ \text{型违例}\ ✓}$$
```

## §3 ⭐⭐ **文献决定性命中**：R=1 nearly-perfect 完全分类 ⟹ `d ≤ 2`

```
$$\textbf{源}（\text{免费}\ ✓）: \text{G. Sac Himelfarb, M. Schwartz, \textit{On Nearly-Perfect Covering Codes Beyond Radius One}, arXiv:2608.12595v1\ (2026-08-12)}\ ✓$$
$$\text{定义}: \text{nearly-perfect} = \textbf{van Wee 界取等}\ ✓;\qquad \text{引文逐字}: \textbf{"These codes have been completely classified for covering radius }R=1\text{"}\ ✓$$
$$\text{该分类（Boruchovsky et al.\ (2025)，由上述论文转述 ✓）}:$$
$$\qquad \text{参数只能是 }(2^m,\ 2^{2^m-m},\ 2)_1\ \text{或}\ (2^m,\ 2^{2^m-m},\ 1)_1,\ \text{且两类都存在 nearly-perfect 码}\ ✓$$
$$\textbf{代入 } m=3:\ (n,M,d)=(8,32,\mathbf{2})\ \text{或}\ (8,32,\mathbf{1})\ ✓\ \Longrightarrow\ \boxed{\text{所有 }(8,32)_1\ \text{码满足 } d\le2}\ ✓✓$$
$$\text{且 } K(8,1)=32=2^8/8=\text{van Wee 界}\ ✓\ \Longrightarrow\ (8,32)_1\ \text{码\textbf{就是} nearly-perfect}\ ✓\ \text{故分类适用}\ ✓$$
```

## §4 由 `d ≤ 2` 能推出什么？（严格逐步 ✓）

```
$$\text{恒等式（我方已验证 ✓）}: 2(A_1+A_2)=E+Q=32+Q\ ✓;\qquad A_1=0\iff d\ge2\ ✓$$
$$\text{若 }d=2:\ A_1=0\ \Longrightarrow\ A_2=(32+Q)/2\ ✓;\qquad \text{若 }d=1:\ \text{存在距离 1 对}\ ✓$$
$$\text{关键观察}: d\le2\ \Longrightarrow\ \text{存在距离}\le2\ \text{的码字对}\ ✓\ \Longrightarrow\ \text{其闭球交于 2 点（double-covered}\ ✓\ \Longrightarrow\ \delta=1\ \text{不贡献 }Q\ ✓)$$
$$\boxed{\text{但 }d\le2\ \textbf{本身不足以}推出 b(x)\le2\ ✗\ (\text{需更多结构}\ ✗)\ }$$
$$\text{仍需}: \text{Boruchovsky et al.\ (2025) 的\textbf{结构}结论（而非仅参数）}\ ✓\ \text{—— 若无 } b\le2\ \text{或等价陈述，则应回到局部/几何路线}\ ✓$$
```

## §5 状态更新（三张表 ✓）

```
$$\textbf{CLOSED}: E=32;\ \sum_i\delta_i(x)=32\ \forall x;\ \sum\delta^2\equiv0\ (\mathrm{mod}\ 4);\ \text{单 }m{=}3/4/7/8\ \text{不可行};\ \text{WLOG 三式};(8,32)_1\ \text{的 }d\le2\ ✓$$
$$\textbf{EVIDENCE}: \text{CP-SAT }900\text{s}/18.5\text{M conflicts 无解};\ \text{案 A/B 对称破缺版}（\text{至 }12{:}00\ \text{仍在跑}\ ⏳);\ \text{doubled Hamming }Q=0\ ✓$$
$$\textbf{OPEN}: b\le2\ \text{的结构理由};A_1+A_2\le16\ \text{独立证明};private\text{-}point\ \text{lemma};\ \text{Boruchovsky 结构原文};\ \textbf{n=10, M=119}\ ✗$$
$$\textbf{RETRACTED}: \text{"n=8 适用三进制同余"}\ ✗\ (\text{适用条件实为 }6\mid n\ ✗)$$
```

## §6 下一刀（按"关闭哪个 OPEN" ✓）

```
$$\text{① 取 Boruchovsky et al.\ (2025) 原文}（\text{看结构结论是否直接给 } b\le2\ ✓）\text{——最高优先}\ ✓$$
$$\text{② 若其只有参数结论}: \text{回到局部/几何路线（PATHMAP 路线 A/E）}: \text{分析最小违例}\ \delta=(2,2)\ \text{型的局部几何}\ ✓$$
$$\text{③ 案 A/B}（\text{若 UNSAT} ⟹ M_2\ \text{级 certificate，须独立复核}\ ✓）$$
```

## §7 边界（诚实标注）

- §1 的撤销依据为**逐字引用** ✓（arXiv:2203.16901v6 ✓）；**我方旧结论已标 RETRACTED** ✓
- §2 为**自算** ✓（分割枚举 ✓）；§3 为**文献转述**（Boruchovsky 原文未取 ✗）
- §4 的"d≤2 不足"为**我方推导** ✓（明确标注不足 ✗）
- **未**排除任何 n ✗；**未**触碰 119 ✓

## 【技术词回查】（定稿前逐字输出）

```
技术词 撤销条目     命中文件数=0    :: 
技术词 算术普查     命中文件数=0    :: 
技术词 nearly-perfect 分类 命中文件数=0    :: 
技术词 最小违例构型 命中文件数=0    ::
```

- **本档新增**（命中数=0）：撤销条目、算术普查、最小违例构型
- **档案已有（引用，不列为提出）**：—
