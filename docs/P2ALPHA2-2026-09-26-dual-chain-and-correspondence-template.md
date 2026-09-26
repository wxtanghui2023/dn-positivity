已查地图：已跑 scripts/prework_map_check.sh weighted covering LP 对偶 refinement ⟹ 执行自 P2ALPHA1-2026-09-26 档；本档为**乙线第一 commit：primal/dual 链 ＋ 对应表模板 ＋ 正文状态**（唐先生 2026-09-26 18:02 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 覆盖 LP 的 primal/dual 完整链、论文关键词口径、refinement→dual 的机制假设、对应表模板、正文获取状态、一个示范性 slice 约束
D1: 1（新增：**完整对偶链** ✓✓；**refinement→dual 机制假设** ⚠️；**示范 slice 约束 m≥25** ✓；**正文未获** ✗）

# P2ALPHA2-2026-09-26

## §0 论文口径（Aalto 官方关键词逐字 ✓✓）

```
$$\text{标题}: \text{"On the size of optimal binary codes of length 9 and covering radius 1"}\ ✓$$
$$\text{作者}: \text{P.R.J. Östergård, U. Blass}\ |\ \textbf{IEEE TIT 47(6) 2556--2557 (2001)}\ |\ \textbf{DOI 10.1109/18.945268}\ ✓$$
$$\textbf{关键词（Aalto 官方页面逐字 ✓✓）}: \text{code equivalence}\ |\ \text{covering code}\ |\ \textbf{linear programming}\ |\ \text{nonlinear code}\ |\ \textbf{weighted covering}\ ✓✓$$
$$\text{正文}: \text{仅 IEEE 付费入口}\ \texttt{iel5/18/20448/00945268.pdf}\ ✗\ (\text{未获}\ ✗)\ \Longrightarrow\ \textbf{待唐先生上传}\ ⚠️$$
$$
$$

## §1 ✅ **A＋B：完整对偶链（可自行导出 ✓✓）**

```
$$\textbf{Primal（分数覆盖）}: \min\sum_{c}x_c\ \ \text{s.t.}\ \sum_{c\in B_1(x)}x_c\ \ge1\ (\forall x\in Q_9),\ x_c\ge0\ ✓$$
$$\textbf{Dual（weighted covering）}: \max\sum_{x}w_x\ \ \text{s.t.}\ \sum_{x\in B_1(c)}w_x\ \le1\ (\forall c),\ w_x\ge0\ ✓✓$$
$$\Longrightarrow\ \boxed{K(9,1)\ \ge\ \sum_x w_x\quad\text{对任意可行 }w}\ ✓\ (\text{弱对偶}\ ✓)$$
$$\textbf{基准}: w\equiv\frac1{10}\ \text{可行}\ (10\times\frac1{10}=1\ ✓)\ \Longrightarrow\ \text{值}=512/10=\mathbf{51.2}\ ⟹\ K\ge52\ ✓\ (\text{= 体积界，即\textbf{平凡对偶}}\ ✗)$$
$$\textbf{关键}:\ \text{平凡对偶只给 }52\ ✗\ \Longrightarrow\ \text{强度必须来自\textbf{额外约束}}\ ✓\ (\text{即 subspace distribution}\ ✓)$$
$$
$$

## §2 ⚠️ **机制假设：refinement 如何在 dual 侧产生强度（待正文验证）**

```
$$\text{论文原文}: \text{"distributions of codewords in }\textbf{subspaces}\ \text{are refined until each subspace is of dimension zero"}\ ✓$$
$$\text{推论（我方假设}\ ⚠️)}: \text{primal 每加一条"某子空间内码字数 = k"型约束}\ ✓\ \Longrightarrow\ \text{dual 出现一条\textbf{子空间级权约束}}\ ✓✓$$
$$\Longrightarrow\ \text{权 }\ w\ \text{从"点权"升级为"}\textbf{refinement state 上的权"}\ ✓\ (\text{与关键词 "weighted covering" 吻合}\ ✓)$$
$$\text{强度来源}: \textbf{同时 refinement}（\text{单切会分叉、丢失刚性}\ ✗\ ——\ \text{已由 P2ALPHA1 证}\ ✓✓)$$
$$
$$

## §3 ✅ **对应表模板（待正文逐项填 ✓）**

```
$$\begin{array}{c|c|c}
\text{原论文对象} & \text{LP 对象} & \text{对偶对象}\\ \hline
\text{subspace distribution} & \text{primal 变量（分布计数）} & \text{dual 权（子空间级）}\\
\text{inequivalent distribution} & \text{变量压缩（symmetry）} & \text{权空间压缩（orbit）}\\
\text{refinement（细分）} & \text{约束生成} & \text{权生成}\\
\text{dimension 0} & \text{终止态} & \text{证书}\\
\text{LP infeasible} & \text{下界} & \ w\ \text{-certificate}\\
\end{array}\ ✓\ (\text{待正文确认各格内容}\ ⚠️)$$
$$
$$

## §4 ✅ **示范：refinement 约束长什么样（单切，我方自算 ✓）**

```
$$\text{取半空间 }H^0/H^1\ (\text{某坐标 }i):\ m_0=|C^0|,\ m_1=62-m_0\ ✓$$
$$\text{覆盖计数}: \sum_{x\in H^0}\big(b_{\rm same}(x)+b_{\rm cross}(x)\big)\ge 2^8=256\ ✓\ \text{且}\ \sum_{H^0}b_{\rm same}=9m_0\ ✓,\ \sum_{H^0}b_{\rm cross}=m_1\ ✓$$
$$\Longrightarrow\ 9m_0+(62-m_0)\ \ge\ 256\ \Longrightarrow\ 8m_0\ \ge\ 194\ \Longrightarrow\ \boxed{m_0\ \ge\ 25}\ ✓\ (\text{对称地 }m_1\ge25\ ✓)$$
$$\text{实测}: \text{两最优码均 }(m_0,m_1)=(30,32)\ ✓\ ——\ \text{远高于 25}\ ✗\ \Longrightarrow\ \textbf{单切约束弱}\ ✗\ (\text{与 P2ALPHA1 一致}\ ✓)$$
$$\textbf{意义}: \text{示范了"refinement 约束"的形式}\ ✓\ \text{但确认单层\textbf{不足以}给出 62}\ ✗\ \Longrightarrow\ \text{强度在多层的\textbf{同时}约束}\ ⚠️$$
$$
$$

## §5 本 commit 结论与等待项

```
$$\textbf{完成}: \text{① 完整对偶链}\ ✓✓;\quad \text{② 机制假设（子空间级权）}\ ⚠️;\quad \text{③ 对应表模板}\ ✓;\quad \text{④ 示范 slice 约束 }m\ge25\ ✓$$
$$\textbf{阻塞}: \text{正文未获}\ ✗\ (\text{IEEE 付费}\ ✗)\ \Longrightarrow\ \textbf{请唐先生上传 PDF}\ ⚠️\ \text{—— 拿到后按"变量→约束→refinement→LP→dual→62"逐行反演}\ ✓$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{未跑 solver/LP}\ ✓$$
$$

## §6 边界（诚实标注）

- §1、§4 为我方**自行导出/计算** ✓；§0 为**第三方逐字**（Aalto 页面 ✓）；§2、§3 为**假设与模板**（待正文验证 ⚠️）
- **未跑 solver/LP/SAT** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 对偶链        命中文件数=1    :: ./P2ALPHA2-2026-09-26-dual-chain-and-correspondence-template.md 
技术词 子空间级权  命中文件数=1    :: ./P2ALPHA2-2026-09-26-dual-chain-and-correspondence-template.md 
技术词 对应表模板  命中文件数=1    :: ./P2ALPHA2-2026-09-26-dual-chain-and-correspondence-template.md
```
- **本档新增**（扣自引后 = 0）：对偶链、子空间级权、对应表模板
- **档案已有（引用，不列为提出）**：weighted covering、primal/dual、refinement
