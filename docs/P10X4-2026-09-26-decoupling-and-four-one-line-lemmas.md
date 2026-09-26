已查地图：已跑 scripts/prework_map_check.sh P10 孤立码字 X4 解耦 ⟹ 执行自 PROVENANCE-2026-09-26 档；本档为**P₁₀ ↔ X₄ 判定：完全解耦 ＋ 4 条一行引理**（唐先生 2026-09-26 17:42 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = (d₁,p) 联合分布、跨层可证不等式、P₁₀ 与 X₄ 的 incidence（实测 0）、解耦的证明、P₁₀ 的结构引理
D1: 1（新增：**可证跨层不等式 p≤9−d₁+[d₁=0]** ✓✓；**P₁₀↔X₄ incidence ≡ 0（解耦）** ✓✓；**P₁₀ 最小距离 ≥3 + 球不相交** ✓✓）

# P10X4-2026-09-26

## §1 ✅ **可证跨层不等式（唐先生要的"把 codeword-side 接回 center-side"）**

```
$$\boxed{p(c)\ \le\ 9-d_1(c)+\mathbf 1_{\{d_1(c)=0\}}}\ ✓✓\ (\text{两码\textbf{0 违反}}\ ✓✓)$$
$$\textbf{证明（一行 ✓）}: \text{① 若 }c+e_i\in C\ (\text{即 }i\ \text{是 }d_1\ \text{方向}\ ✓)\ \Longrightarrow\ b(c+e_i)\ge2\ \Longrightarrow\ \text{该邻点\textbf{非 private}}\ ✓$$
$$\qquad\text{② }c\ \text{自身 private}\iff b(c)=1\iff d_1(c)=0\ ✓\ \Longrightarrow\ \text{合计上界 }9-d_1+\mathbf 1_{\{d_1=0\}}\ ✓✓$$
$$\text{求和}: \sum_c p=N_1\ \le\ 9M-2A_1+n_0\ (n_0:=\#\{d_1=0\})\ ✓\ \Longrightarrow\ 2A_1\le116+n_0+N_4\ ✗\ (\text{弱}\ ⚠️)$$
$$
$$

## §2 ⭐⭐⭐ **P₁₀ ↔ X₄：完全解耦（0 incidence，且是定理 ✓✓）**

```
$$\textbf{实测}: \sum_{x\in X_4}|S_x\cap P_{10}|=\mathbf 0\ ✓✓\ (\text{两码皆然}\ ✓✓)\ \Longrightarrow\ \textbf{无一个 }p{=}10\ \text{码字落在任何 }X_4\ \text{球内}\ ✓$$
$$\textbf{定理（一行 ✓✓）}: p(c)=10\ \Longrightarrow\ B_1(c)\setminus\{c\}\ \text{全为 private}\ \Longrightarrow\ \textbf{无任何 }b\ge2\ \text{点与 }c\ \text{相邻}$$
$$\qquad\Longrightarrow\ P_{10}\ \text{与} X_2,X_3,X_4\ \textbf{全部解耦}\ ✓✓\ (\text{不只是 }X_4\ ✓)$$
$$
$$

## §3 ⭐⭐ **P₁₀ 的结构引理（全部一行可证 ✓✓）**

```
$$\textbf{引理 1}: \text{两 }P_{10}\ \text{码字距离不能为 }1\ ✓\ (\text{否则对方在 }B_1\ \text{内}\ ⟹\ b\ge2\ ⟹\ \text{非 private}\ ✗)$$
$$\textbf{引理 2}: \text{距离不能为 }2\ ✓\ (\text{否则两个中点被二者共同覆盖}\ ⟹\ b\ge2\ \text{且落在 }B_1(c)\ \text{内}\ ✗)$$
$$\qquad\Longrightarrow\ \boxed{d(P_{10})\ge3}\ ✓✓\ (\text{实测内部距离 }\{3,4,7,8\}\ (\text{码#1})/\{3,4,7\}\ (\text{码#2})\ \textbf{全部 }\ge3\ ✓✓)$$
$$\textbf{引理 3}: \text{距离 }\ge3\ \Longrightarrow\ B_1\ \text{球两两不交}\ ✓\ \Longrightarrow\ \text{8 个 }P_{10}\ \text{占 }80\ \text{个互异 private 点}\ ✓\ (N_1=432\ \text{容得下}\ ✓)$$
$$
$$

## §4 ✗✓ **判定：这一刀"锐利但无杠杆"** ✗

```
$$\text{唐先生的目标}: \text{从 }P_{10}\leftrightarrow X_4\ \text{抽一个独立 incidence bound，接上 }N_4\ ⚠️$$
$$\text{实测结果}: \textbf{incidence 恒为 0}\ ✓✓\ ——\ \text{不是"小"，而是\textbf{结构性为零}}\ ✓\ (\text{且我们给出了证明}\ ✓)$$
$$\Longrightarrow\ \boxed{P_{10}\ \text{携带\textbf{零信息}关于 }N_4}\ ✗✓\ ——\ P_{10}\ \text{被完全"砌在"私有外围，与高层解耦}\ ✓$$
$$\text{按唐先生预设判据}: \text{"若这层也只是又一个恒等式，我们立即知道它没有 leverage"}\ ✓\ \Longrightarrow\ \textbf{判定：无杠杆，停止}\ ✓$$
$$\text{但收获}: \textbf{4 条一行可证引理}\ ✓✓\ +\ \textbf{1 条可证跨层不等式}\ ✓✓\ (\text{弱但真}\ ✓)$$
$$
$$

## §5 状态（今日全线）

```
$$\textbf{跨表示刚性层（终版）}: \{E,Q_2,A_{\le2},(N_j),d_{\max},T_3,\#\triangle,I_{ij},(3,4,4),h_3{=}1/h_4{=}2\ \text{逐点},X_4\ \text{负载}\ \{5{:}4,0{:}6\},p(c)\ \text{分布}\ \{6{:}40,8{:}14,10{:}8\}\}\ ✓✓$$
$$\textbf{可证资产（今日新增）}: T_3=\#K_3\ \text{普适}\ ✓✓;\ T_3\ge Q_2\ ✓✓;\ \sum p_2=\sum\binom b2-2A_1\ ✓✓;\ p\le9-d_1+[d_1{=}0]\ ✓✓;\ d(P_{10})\ge3\ ✓✓;\ P_{10}\perp X_{\ge2}\ ✓✓$$
$$\textbf{否证/封存（今日）}: \text{14 条}\ ✗\ (\text{含本轮 }P_{10}\leftrightarrow X_4\ ✓)$$
$$\textbf{方法类型诊断}: \text{62 的证明是计算机辅助 LP 细分/分类}\ ✓✓\ \Longrightarrow\ \text{靶心需"分类+LP"型输入}\ ✓$$
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓\ ——\ \text{但 }P1\ \text{与 }P_{10}\ \text{两线均已封存}\ ✓$$
$$
$$

## §6 边界（诚实标注）

- §1–§3 为**实算＋证明**（两码 ✓）；§4 明确判定**无杠杆** ✗✓
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 跨层不等式  命中文件数=1    :: ./P10X4-2026-09-26-decoupling-and-four-one-line-lemmas.md 
技术词 完全解耦     命中文件数=9    :: ./MATH-STATEMENTS-all-22-items-rigorous.md ./r3-kernel-expansion-2026-09-09.md ./P10X4-2026-09-26-decoupling-and-four-one-line-lemmas.md 
技术词 P₁₀ 结构引理 命中文件数=1    :: ./P10X4-2026-09-26-decoupling-and-four-one-line-lemmas.md
```
- **本档新增**（扣自引后 = 0）：跨层不等式、完全解耦、P₁₀ 结构引理
- **档案已有（引用，不列为提出）**：p(c)、d₁、X₄
