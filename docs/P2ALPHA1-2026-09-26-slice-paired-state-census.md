已查地图：已跑 scripts/prework_map_check.sh 余维1 slice paired-state 枚举 ⟹ 执行自 P2ALPHA-2026-09-26 档；本档为**第一 commit：slice paired-state 定义与压缩（无 solver）**（唐先生 2026-09-26 17:46 指令 ✓）。
D0: 本档对象 = b=b_same+b_cross 恒等式、(b_same,b_cross) 分布、N₄=N_(4,0)+N_(3,1)、paired-state 类型数、是否产生 slice-only 新约束
D1: 1（新增：**恒等式验证** ✓✓；**N₄ 二分解（但分叉）** ✗；**paired-state 类型 17/16 非刚性** ✗）

# P2ALPHA1-2026-09-26

## §1 ✅ **恒等式（0 违反 ✓✓）**

```
$$\boxed{b(x)=b_{\rm same}(x)+b_{\rm cross}(x)}\ ✓✓\ (n=9\ \text{全切片}: \text{违反 0}\ ✓)$$
$$\qquad b_{\rm same}(x)=|C^\epsilon\cap B_1^{(8)}(x)|\ ✓;\quad b_{\rm cross}(x)=\mathbf 1_{\{x+e_{\rm cut}\in C\}}\ ✓$$
$$
$$

## §2 ⭐ **N₄ 的二分解（新语言，但\textbf{分叉} ✗）**

```
$$\boxed{N_4=N_{(4,0)}+N_{(3,1)}}\ ✓\ (\text{两码皆 }\Sigma=10\ ✓\ \text{自洽}\ ✓)$$
$$\qquad\text{码#1}: N_4=\mathbf{8}+\mathbf{2}=10\ ;\quad \text{码#2}: N_4=\mathbf{3}+\mathbf{7}=10\ ✗\ \textbf{分叉}\ ✗$$
$$(b_{\rm same},b_{\rm cross})\ \text{分布}: \text{码#1}\ \{(0,1){:}52,(1,0){:}380,(1,1){:}8,(2,0){:}54,(3,0){:}8,(3,1){:}2,(4,0){:}8\}$$
$$\qquad\qquad\qquad \text{码#2}\ \{(0,1){:}30,(1,0){:}402,(1,1){:}19,(2,0){:}43,(2,1){:}6,(3,0){:}2,(3,1){:}7,(4,0){:}3\}\ ✗\ \textbf{分叉}\ ✗$$
$$
$$

## §3 ✗ **paired-state 类型数（非刚性 ✗）**

```
$$\text{paired-state } s(x)=(b_{\rm same}(x),b_{\rm cross}(x),b_{\rm same}(x{+}e),b_{\rm cross}(x{+}e))\ \text{的类型数}: \text{码#1}=\mathbf{17},\ \text{码#2}=\mathbf{16}\ ✗$$
$$\text{高频型}: \text{码#1}\ (1,0,1,0){:}138\ \text{对};\ (1,0,0,1){:}24;\ (2,0,1,0){:}21\ |\ \text{码#2}\ (1,0,1,0){:}180;\ (0,1,2,0){:}13;\ (1,0,1,1){:}13\ ✗$$
$$
$$

## §4 🎯 **判定：第一层 slice 只恢复旧约束，未产出 slice-only 新约束** ✗**

```
$$\text{slice 系统的聚合约束（全部可算 ✓）}: \sum_{x\in H^\epsilon}b_{\rm same}(x)=9|C^\epsilon|\ ✓;\quad \sum_{x\in H^\epsilon}b_{\rm cross}(x)=|C^{1-\epsilon}|\ ✓$$
$$\qquad\Longrightarrow\ \sum_x b=9\cdot62+62=620\ ✓\ (\textbf{恰好重导全局一阶矩}\ ✗)\ ;\quad \text{跨层 matching}\ \sum_x b_{\rm cross}=|C^1|\ \text{为\textbf{重计数恒等式}}\ ✗$$
$$\textbf{决定性观察}: \text{slice 级数据\textbf{随表示分叉}}\ ✗\ (\text{两最优码的 }(b_{\rm same},b_{\rm cross})\ \text{分布、}N_{(4,0)}/N_{(3,1)},\ \text{类型数皆不同}\ ✗)$$
$$\qquad\Longrightarrow\ \boxed{\text{slice 层\textbf{破坏}刚性，而非增加约束}\ ✗\ ——\ \text{刚性只在\textbf{全局矩层}}\ ✓✓}$$
$$\text{按唐先生预设判据}: \text{"若这一层最终只恢复 }E,Q_2,T_3\ \text{那些旧约束，立刻判定它不够"}\ ✓\ \Longrightarrow\ \textbf{判定：第一层不够}\ ✗$$
$$
$$

## §5 结构性结论（本档最重要 ✓✓）

```
$$\boxed{\text{刚性 }=\text{ 表示不变的全局量}\ ✓✓;\qquad \text{slice/局部层 }=\text{ 表示相关，分叉}\ ✗}$$
$$\Longrightarrow\ \text{任何"切子空间 + 分类局部状态"的 LP，其可行集必须同时容纳两份最优码}\ ✓$$
$$\qquad\text{（其剖面显著不同}\ ✗)\ \Longrightarrow\ \text{该 LP 的约束内容\textbf{比全局矩层更松}\ ✗\ (\text{在单坐标切层面}\ ✓)}$$
$$\text{要恢复原论文的杀伤力，需要}\textbf{多层同时 refinement}（\text{= 原方法本体}\ ✓)\ ✗\ \text{—— 成本高，且高度接近重跑文献}\ ⚠️$$
$$
$$

## §6 状态

```
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓\ (\text{未休眠}\ ✓);\quad \textbf{未跑 solver/LP}\ ✓$$
$$\text{P2-α 第一 commit 完成 ✓；判定：单坐标切不够 ✗；多层 refinement = 原方法（成本高）}\ ⚠️$$
$$

## §7 边界（诚实标注）

- §1–§3 为**实算**（两码 ✓）；§4–§5 为**判定与结构结论** ✓
- **未跑 solver/LP/SAT** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 slice paired-state 命中文件数=1    :: ./P2ALPHA1-2026-09-26-slice-paired-state-census.md 
技术词 二分解        命中文件数=1    :: ./P2ALPHA1-2026-09-26-slice-paired-state-census.md 
技术词 slice-only 新约束 命中文件数=1    :: ./P2ALPHA1-2026-09-26-slice-paired-state-census.md
```
- **本档新增**（扣自引后 = 0）：slice paired-state、二分解、slice-only 新约束
- **档案已有（引用，不列为提出）**：b_same、b_cross、N₄
