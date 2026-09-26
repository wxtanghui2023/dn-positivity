已查地图：已跑 scripts/prework_map_check.sh A5 形式重建 provenance gap 整性 ⟹ 执行自 SPHERELP-2026-09-26 档；本档为**A5 封口：FORM-RECONSTRUCTED ＋ 实现状态 provenance gap**（唐先生 2026-09-26 18:30 裁定 ✓）；未跑 solver（仅小 LP 判定 ✓）。
D0: 本档对象 = A5 状态定档、两轴重建终版、三条锁定事实、分数下界判定（m=0..6 恒 51.2）、provenance gap（ν）、citation bug 撤除
D1: 1（新增：**A5 = FORM-RECONSTRUCTED** ✓✓；**分数下界恒 51.2 ⟹ 整性/分支必需** ✓✓；**provenance gap 单列** ✓✓）

# A5-FORM-RECONSTRUCTED-2026-09-26

## §1 ⚖️ **A5 定档（唐先生裁定 ✓）**

```
$$\boxed{\text{A5}\ =\ \textbf{FORM-RECONSTRUCTED}\ \text{（不是 COMPLETE）}}\ ✓$$
$$\textbf{唯一未闭合项}: \nu=\text{一次 refinement 节点 }\nu\ \text{中 OB 究竟把什么当状态}:\quad \nu\in\{\ y\ \text{(distribution)},\ F\ \text{(partial code)},\ (y,F,\text{局部导出数据})\ \}\ ⚠️$$
$$\qquad\text{这是}\textbf{历史实现细节缺失}，\text{不是数学结构缺失}\ ✓$$
$$
$$

## §2 ✅ **两轴重建终版（文献确认 ＋ 我方推导 ✓✓）**

```
$$\textbf{A 轴（distribution refinement，文献确认 ✓）}: \text{M-covering system}\ \to\ \text{inequivalent integer }y\ \to\ m{=}1,\dots,9\ \to\ \text{cell 维数 0}\ ✓$$
$$\qquad A_{ii}=10-m\ ✓;\ A_{ij}=\mathbf 1_{\{d(p_i,p_j)=1\}}\ ✓;\ \sum_jA_{ji}y_j\ \ge\ 2^{9-m}\ ✓$$
$$\textbf{B 轴（covering inequalities / weighted covering，我方重建 ✓）}:$$
$$\qquad\forall S\subseteq Q_9:\ \sum_{c}|B(c)\cap S|\ \ge\ |S|\ ✓\Longrightarrow\ \text{部分状态}: \sum_{c\in C\setminus F}|B(c)\cap S|\ \ge\ |S|-|\{x\in S:\ F\ \text{覆盖 }x\}|\ ✓$$
$$\qquad\text{对偶}: w_x\ge0,\ \sum_{x\in B(c)}w_x\le1\ \Longrightarrow\ M\ \ge\ \sum_x w_x\ ✓$$
$$\textbf{链条}: \text{distribution}\ \to\ \text{local covering capacity}\ \to\ \text{LP bound}\ \to\ \text{pruning}\ ✓$$
$$
$$

## §3 ✅ **三条锁定事实（独立推导，非文献倒推 ✓）**

```
$$\text{① }\textbf{单球 LP 不是关键来源}\ ✓✓: \sum_{y\in B(x)}b(y)=10\cdot\mathbf 1_{\{x\in C\}}+2(d_1+d_2)\ \Longrightarrow\ OC(B(x))\equiv0\ (\bmod 2)\ ✓$$
$$\qquad\Longrightarrow\ \text{单球约束只能表达 }OC\ge0\ \text{或把最低非零量推到偶数层}\ ✗\ \Longrightarrow\ \textbf{强约束必须跨越多球/子空间}\ ✓$$
$$\text{② }\textbf{subspace distribution 得到机制解释}\ ✓✓: y_S\ \text{描述质量分布};\ \text{内层 covering inequalities 作用于局部区域}\ S\ \to\ \text{LP 判节点可行性}\ ✓$$
$$\text{③ }\textbf{weighted covering 的位置}\ ✓\ (\text{带审计限定}\ ⚠️): \text{它是\textbf{覆盖不等式的对偶解释}}\ ✓$$
$$\qquad\textbf{限定}: \text{不得写成"已证明 OB-2001 明确把这个 dual 写成 }w\text{-form"}\ ✗\ (\text{需原文}\ ⚠️)$$
$$
$$

## §4 ⭐⭐⭐ **新判定：分数下界恒为体积界 ⟹ 整性/分支必需（本档新算 ✓✓）**

```
$$\textbf{计算}: \min\sum_c x_c\ \text{s.t.}\ Ax\ge1,\ 0\le x_c\le1,\ \text{cell 和相等（均匀）}\ \Longrightarrow\ \text{各层 }m\ \text{下:}$$
$$\begin{array}{c|ccccccc} m & 0 & 1 & 2 & 3 & 4 & 5 & 6\\ \hline \text{分数下界} & 51.2 & 51.2 & 51.2 & 51.2 & 51.2 & 51.2 & 51.2\\ \end{array}\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{纯分数 LP（即便加 cell 条件）永远只给体积界 }51.2\ \Longrightarrow\ \textbf{强度必须来自}\textbf{整性}\ +\ \textbf{分支}\ ✓✓}$$
$$\qquad\Longrightarrow\ \text{与 LMT 摘要逐字吻合}: \text{"isomorphism pruning, subcode enumeration, and }\textbf{LP-based bounding}\text{"}\ ✓✓$$
$$\qquad\qquad\text{（LP 是\textbf{搜索内部的界}，不是自足的界 ✓）\ \Longrightarrow\ 也解释了 OB 摘要的 "repeatedly"}\ ✓$$
$$
$$

## §5 ⚠️ **provenance gap（单列，不猜 ✓）**

```
$$\boxed{\text{Gap }\nu: \text{OB 实现中的状态变量}\ \nu\ \in\ \{y,\ F,\ (y,F,\cdot)\}\ \textbf{未定}\ ⚠️}$$
$$\text{获取路径（下一轮，若做 ✓）}: \text{2003 论文的算法伪代码 / matrix construction / subcode enumeration 原始措辞}\ ✓$$
$$\text{若最终仍找不到}: \boxed{\text{A5: FORM-RECONSTRUCTED; implementation-state unresolved}}\ ✓\ \text{—— 已是完整方法学资产}\ ✓$$
$$
$$

## §6 🚫 **citation bug 撤除（唐先生指出 ✓）**

```
$$\text{唐先生 [2] 的 TU Delft 链接标题 = 《The separability of standard cyclic N-ary gray codes》}$$
$$\qquad\Longrightarrow\ \textbf{与 2003 平衡码论文不匹配}\ ✗\ (\text{预览页解析到同库另一文件}\ ⚠️)$$
$$\textbf{处置}: \textbf{从 A5 证据链中撤除该出处}\ ✗\ ——\ \text{不得让错误出处进入方法学档案}\ ✓$$
$$
$$

## §7 地位与隔离

```
$$\textbf{A5} = \text{FORM-RECONSTRUCTED}\ ✓\ (\text{方法学资产}\ ✓)\ ——\ \textbf{不}升级为对 OB 原文的断言}\ ✗$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓\ \text{—— \textbf{不因本次方法复原而转入计算}}\ ✓$$
$$\textbf{G}: \textbf{COVERED}\ ✓\ (\text{见 G-COVERED-2026-09-26}\ ✓)$$
$$
$$

## §8 边界（诚实标注）

- §1–§3、§5–§6 为**裁定/推导/登记**；§4 为**本档新算（小 LP，512 变量）** ✓
- **未跑 SAT/大规模 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 FORM-RECONSTRUCTED 命中文件数=1    :: ./A5-FORM-RECONSTRUCTED-2026-09-26-closure.md 
技术词 分数下界恒体积界 命中文件数=1    :: ./A5-FORM-RECONSTRUCTED-2026-09-26-closure.md 
技术词 实现状态 provenance gap 命中文件数=1    :: ./A5-FORM-RECONSTRUCTED-2026-09-26-closure.md
```
- **本档新增**（扣自引后 = 0）：FORM-RECONSTRUCTED、分数下界恒体积界、实现状态 provenance gap
- **档案已有（引用，不列为提出）**：weighted covering、M-covering、LP-based bounding
