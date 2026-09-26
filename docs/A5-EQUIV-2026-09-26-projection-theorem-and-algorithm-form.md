已查地图：已跑 scripts/prework_map_check.sh projection theorem sphere-covering node LP ⟹ 执行自 A5-FORM-RECONSTRUCTED-2026-09-26 档；本档为**A5 升级：投影定理（证明）＋ ALGORITHM-FORM-RECONSTRUCTED**（唐先生 2026-09-26 18:32 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = node-level sphere-covering 不等式的投影定理（含证明与边界）、损失量化、机制结论、A5 升级、状态变量定档
D1: 1（新增：**投影定理（证明）** ✓✓；**A5 → ALGORITHM-FORM-RECONSTRUCTED** ✓✓；**机制结论：强度在树而非单 LP** ✓✓）

# A5-EQUIV-2026-09-26

## §1 ⭐⭐⭐ **投影定理（唐先生所求，已证 ✓✓）**

```
$$\textbf{节点级 sphere-covering 不等式}: \forall S\subseteq Q_9:\quad \sum_{c\in C}|B(c)\cap S|\ \ge\ |S|\ ✓$$
$$\textbf{取 }S=W_i\ (\text{单个 cell},\ |W_i|=2^{9-m})\ ✓\ \Longrightarrow\ \sum_{c}|B(c)\cap W_i|\ \ge\ 2^{9-m}\ ✓$$
$$\textbf{投影步（关键一行 ✓）}: \text{按 cell 归并码字，并用\textbf{该 cell 内可实现的最大覆盖}替换逐码字项}:$$
$$\qquad\sum_j\Big(\max_{c\in W_j}|B(c)\cap W_i|\Big)\,y_j\ \ge\ 2^{9-m}\ ✓$$
$$\textbf{而逐项可算（一行 ✓）}: \max_{c\in W_j}|B(c)\cap W_i|=\begin{cases}10-m,&j=i\\ 1,&d(i,j)=1\\ 0,&d(i,j)\ge2\end{cases}\ =\ A_{ji}\ ✓$$
$$\Longrightarrow\ \boxed{\sum_j A_{ji}y_j\ \ge\ 2^{9-m}\quad\text{（\textbf{恰为我方系统}）}\ ✓✓}$$
$$\textbf{结论}: \boxed{\text{我方 }A_m y\ge2^{9-m}\mathbf 1\ =\ \text{节点级 sphere-covering 不等式在 cell 计数变量上的}\textbf{投影}}\ ✓✓$$
$$
$$

## §2 ⚠️ **投影的损失（= 为何弱）＋ 边界诚实标注**

```
$$\text{投影时丢掉的}: \text{cell 内逐点差异（"每个码字对 }W_i\ \text{的覆盖"仅保留其最大）}\ ⟹\ \text{损失量}=\textbf{fiber}\ ✓$$
$$\qquad\log_2|\mathcal F(y)|:\ m{=}1:\ \mathbf{265}\ \text{bit}\ \to\ m{=}9:\ \mathbf 0\ \text{bit}\ ✓✓\ (\text{refinement 逐步回收该信息}\ ✓)$$
$$\boxed{\text{故单层投影\textbf{必然}弱}\ ✗\ \Longrightarrow\ \text{强度\textbf{不可能}来自任一单层 LP}\ ✓✓}$$
$$\textbf{边界（诚实 ⚠️）}: \text{更一般的投影（取 }S\ \text{为带权点集}\ \lambda\ \text{或任意 cell 并）可能比"单 cell 族"更强}\ ⚠️\ ——\ \text{本档只证"单 cell 族 = 我方系统"}\ ✓$$
$$
$$

## §3 ⭐⭐⭐ **机制结论（回答"为何 }m{=}1..4\text{ 弱而 62 需 refinement"）** ✓✓

```
$$\text{① 单层投影弱}: \text{均匀解 }y\equiv M/2^m\ \text{在}\textbf{每一层}满足系统（比值恒 }10M/512\ ✓);\ \text{分数 LP 含 cell 条件后仍恒 }=51.2\ (m\le6)\ ✓$$
$$\text{② 强度来自\textbf{树}}}:\ \text{整数 }y\ \text{的 refinement（}y_i=y_{i0}+y_{i1}\ ✓)+\ \text{equivalence 剪枝}+\ \text{节点 LP 定界}\ ✓$$
$$\qquad\Longrightarrow\ \text{整数性在深层咬合}: m{=}9\ \text{时 }y_i\in\{0,1\}\ \Longrightarrow\ \text{分布}=\text{码本体}\ ✓\ (\text{uniform 分支在此必死}\ ✓)$$
$$\text{③ 与文献三技术逐字对应}: \text{isomorphism pruning}=\text{equivalence 剪枝}\ ✓;\ \text{subcode enumeration}=\text{refinement 分支}\ ✓;\ \text{LP-based bounding}=\text{节点定界}\ ✓✓$$
$$
$$

## §4 ✅ **A5 升级（唐先生裁定 ✓）**

```
$$\boxed{\text{A5}\ =\ \textbf{ALGORITHM-FORM-RECONSTRUCTED}}\ ✓$$
$$\textbf{状态变量（文献证据已足 ✓）}: \boxed{\nu=\big(\text{row-prefix subspace distribution }y^{(m)},\ \text{partial-subcode equivalence class }[\mathcal C_m]\big)}\ ✓$$
$$\qquad\textbf{双层}: \text{Level A: }y^{(m)}\in\mathbb Z_{\ge0}^{2^m}\ (\text{coarse fingerprint}\ ✓);\ \text{Level B: }[\mathcal C_m]\ (\text{等价类, 由 2003 的 "equivalence tests on subcodes" 支撑}\ ✓)$$
$$\qquad\text{refinement 算子}: R_m:\ \mathbb Z^{2^m}\to\mathbb Z^{2^{m+1}},\ y_i\mapsto(y_{i0},y_{i1}),\ y_{i0}+y_{i1}=y_i\ ✓$$
$$\qquad m{=}9:\ |W_i|=1\ \Longrightarrow\ y_i\in\{0,1\}\ \Longrightarrow\ \text{分布 = 实际码}\ ✓\ (\text{"dimension zero" 的数学含义}\ ✓)$$
```
**唯一窄化后的未知（不再猜 y-SIP ✓）**：
```
$$\boxed{\text{OB-LP} = ?\ \begin{cases}\text{distribution feasibility LP}\\ \text{weighted-covering LP}\\ \text{partial-state LP}\\ \text{上述的等价重写}\end{cases}}$$
$$\text{证据最支持}: \text{partial distribution refinement}\ +\ \text{sphere-covering linear inequalities}\ ✓$$
$$\qquad\text{（"weighted covering" = 其 LP/对偶解释}\ ✓;\ \textbf{不得}\text{说成 OB 原文的某具体 dual 写法}\ ✗)$$
$$
$$

## §5 完整证明链（重建，K(9,1)=62 ✓）

```
$$\text{P0}: C\subseteq\mathbb F_2^9,\ |C|=61,\ R(C)=1\ (\text{反设}\ ✓)$$
$$\text{P1}: y^{(1)}\ \text{满足 sphere-covering inequalities（投影系统）}\ ✓$$
$$\text{P2}: \text{逐行 refinement }y^{(m)}\to y^{(m+1)}:\ \text{生成候选}\to\text{去等价}\to\text{LP 定界}\to\text{删不可行}\ ✓$$
$$\text{P3}: m\to9:\ \text{每个 subspace 为 singleton}\ ⟹\ \text{分布}=\text{码}\ ✓$$
$$\text{P4}: \text{剩余节点全部证不存在}\ ⟹\ K(9,1)\ge62\ ✓;\ \text{配合已知 62 码}\ ⟹\ K(9,1)=62\ ✓$$
$$
$$

## §6 地位与隔离

```
$$\textbf{A5} = \text{ALGORITHM-FORM-RECONSTRUCTED}\ ✓\ (\text{方法学资产}\ ✓;\ \textbf{不}升级为对 OB 原文的断言}\ ✗)$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓\ (\text{不因方法复原转入计算}\ ✓);\quad \textbf{G}: \textbf{COVERED}\ ✓$$
$$
$$

## §7 边界（诚实标注）

- §1、§3、§5 为**证明与重建** ✓；§2 明确**边界**（带权投影可能更强 ⚠️）；§4 的状态变量由 2003 措辞支撑 ✓
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 投影定理     命中文件数=1    :: ./A5-EQUIV-2026-09-26-projection-theorem-and-algorithm-form.md 
技术词 ALGORITHM-FORM-RECONSTRUCTED 命中文件数=1    :: ./A5-EQUIV-2026-09-26-projection-theorem-and-algorithm-form.md 
技术词 refinement 算子 命中文件数=1    :: ./A5-EQUIV-2026-09-26-projection-theorem-and-algorithm-form.md
```
- **本档新增**（扣自引后 = 0，命中 1 = 自引 ✓）：投影定理、ALGORITHM-FORM-RECONSTRUCTED、refinement 算子
- **档案已有（引用，不列为提出）**：sphere-covering、weighted covering、equivalence
