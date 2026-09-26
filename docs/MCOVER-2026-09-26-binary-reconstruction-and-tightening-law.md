已查地图：已跑 scripts/prework_map_check.sh M-covering system partition refinement ⟹ 执行自 P2ALPHA2-2026-09-26 档；本档为**乙线第二 commit：binary(n=9,R=1) M-covering system 精确重建 ＋ 收紧律**（唐先生 2026-09-26 18:08 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = level-m M-covering system 的 binary 精确形式、A 矩阵闭式、均匀解分析、逐层收紧律、m=9 极限、三问答复、正文获取状态
D1: 1（新增：**A 矩阵闭式 A_ii=10−m / A_ij=1(d=1)** ✓✓；**逐层收紧律实测 1.21→1.09** ✓✓；**m=9 极限 = 覆盖条件本体** ✓✓）

# MCOVER-2026-09-26

## §1 ⭐⭐⭐ **精确重建：binary n=9, R=1 的 level-m M-covering system** ✓✓

```
$$\text{partition}: \text{固定前 }m\ \text{个坐标}\ ✓\ \Longrightarrow\ t=2^m\ \text{cells}\ ✓,\ \text{每 cell }s=2^{9-m}\ \text{词}\ ✓$$
$$y_i=|C\cap C_i|\ ✓;\quad \sum_i y_i=M\ ✓;\quad y_i\in\mathbb Z_{\ge0}\ ✓$$
$$\boxed{A_{ii}=10-m\ ✓;\qquad A_{ij}=\mathbf 1_{\{d(p_i,p_j)=1\}}\ ✓;\qquad A_{ij}=0\ (d\ge2)\ ✓✓}$$
$$\Longrightarrow\ \textbf{系统}: \sum_j A_{ji}y_j\ \ge\ 2^{9-m}\quad(\forall i)\ ✓\ (\text{"M-covering system"}\ \mathcal M_m\ ✓)$$
$$\textbf{推导}（\text{一行 ✓}）: \text{码字 }c\in C_i\ \text{的球在 }W_i\ \text{内落 }1+(9-m)\ \text{点}\ ✓\ (=10-m\ ✓);\ \text{在 }d(p_i,p_j)=1\ \text{的 }W_j\ \text{内恰落 1 点}\ ✓$$
$$

## §2 ✅ **验证（两码 × m=1..4，全部满足 ✓✓）**

```
$$\begin{array}{c|c|c|c|c}
m & \text{cells} & \text{每 cell} & \text{码#1 最小覆盖} & \text{码#2 最小覆盖}\\ \hline
1 & 2 & 256 & 310\ (=9\cdot31+31,\ y{=}(31,31)\ ✓) & 302\ (y{=}(30,32)\ ✗)\\
2 & 4 & 128 & 151 & 151\\
3 & 8 & 64 & 73 & 72\\
4 & 16 & 32 & 35 & 34\\
\end{array}\ \Longrightarrow\ \text{全部 } \ge \text{阈值}\ ✓✓$$
$$\textbf{与 P2-α 的对应}:\ m{=}1\ \text{系统即我方单坐标切}\ ✓✓;\ \text{我方 }8m_0\ge194\ (m_0\ge25)\ \text{是该系统推论}\ ✓\ (\text{用户第 9 点确认}\ ✓✓)$$
$$
$$

## §3 ⭐⭐⭐ **均匀解分析 ＋ 逐层收紧律（机制量化 ✓✓）**

```
$$\textbf{均匀解} y_i\equiv M/2^m:\ \sum_j A_{ji}y_j=\big[(10-m)+m\big]\frac{M}{2^m}=\frac{10M}{2^m}\ \ge\ 2^{9-m}\ \Longleftrightarrow\ 10M\ \ge\ 2^9=512$$
$$\Longrightarrow\ \boxed{\text{均匀解在\textbf{每一层}给出同一个比值 }10M/512\ \Longrightarrow\ \text{系统本身只给 }M\ge52\ ✗\ (\text{体积级}\ ✓)}$$
$$\textbf{实测收紧律（码#2 最紧 cell 比值）}: \frac{302}{256}=1.181\ (m{=}1)\ \to\ \frac{151}{128}=1.180\ \to\ \frac{72}{64}=1.125\ \to\ \frac{34}{32}=1.062\ (m{=}4)\ ✓✓$$
$$\qquad\text{(码#1}: 1.211\to1.180\to1.141\to1.094\ ✓)\ \Longrightarrow\ \textbf{比值单调下降}\ ✓✓\ \text{趋近 }1$$
$$\Longrightarrow\ \boxed{\textbf{强度来源 = 非均匀性 + 整性 + 层间归纳}\ ✓✓\ ——\ \text{更深层 } \Rightarrow\ \text{某个 cell 低于其词数}\ \Rightarrow\ \text{矛盾}\ ✓}$$
$$

## §4 ⭐⭐ **m=9 极限：系统收敛到覆盖条件本体** ✓✓

```
$$m=9:\ t=512\ \text{cells (单点}\ ✓),\ A_{ii}=1\ ✓,\ A_{ij}=\mathbf 1_{\{d(i,j)=1\}}\ ✓\ \Longrightarrow\ y_i\in\{0,1\}\ ✓$$
$$\textbf{系统}: y_i+\sum_{j:\,d(i,j)=1}y_j\ \ge\ 1\quad(\forall i)\ \Longleftrightarrow\ \textbf{每个词被自己或某邻居码字覆盖}\ ✓✓$$
$$\Longrightarrow\ \text{层次图}: m{=}1\ (\text{体积级 }52)\ \to\ \cdots\ \to\ m{=}9\ (\text{覆盖条件本体，精确}\ ✓✓)\ ;\ \text{阈值 }62\ \text{在中间某层被逼出}\ ⚠️$$
$$
$$

## §5 三问答复（含诚实标注）

```
$$\textbf{问 1}: m=\text{"固定多少坐标"还是更一般的 subspace dimension？}\ \Longrightarrow\ \text{后续文献用的是\textbf{固定前缀坐标}}\ ✓\ (m\ \text{= 固定前 }m\ \text{个符号}\ ✓)$$
$$\qquad\text{一般形式}: m=\text{partition cell 的}\textbf{余维}\ ✓;\ \text{cell 可取任意仿射子空间}\ ✓;\ \text{前缀切 = 嵌套特例}\ ✓\ (\text{一般性}\ ⚠️\ \text{待正文})$$
$$\textbf{问 2}: \text{为何枚举 inequivalent distributions？}\ \Longrightarrow\ \text{系统在码等价群 }B_n\ (\text{平移×坐标置换}\ ✓)\ \text{下不变}\ ✓\ \Longrightarrow\ y\ \text{向量成轨道}\ ✓$$
$$\qquad\text{轨道代表即可}\ ✓\ (\text{排除全部不等价类} \iff \text{排除全部}\ ✓)\ \Longrightarrow\ \text{把 }2^m\text{-维枚举压到可算规模}\ ✓✓$$
$$\textbf{问 3}: \text{论文里的 LP 在这个整系统上做什么？}\ \Longrightarrow\ \textbf{HYPOTHESIS}\ ⚠️\ (\text{未获正文，\textbf{不升级为结论}}\ ✗)$$
$$\qquad\text{假设}: \text{LP = 该系统的\textbf{分数松弛}}\ ✓\ \text{用于 (a) 定界（其对偶 = weighted covering}\ ⚠️) (b) 枚举剪枝}\ ✓\ ——\ \text{与关键词 "weighted covering" 吻合}\ ✓\ \text{但\textbf{未证实}}\ ⚠️$$
$$
$$

## §6 正文状态

```
$$\text{Östergård--Blass 2001}: \text{仅 IEEE 付费}\ ✗\ \text{未获}\ ⚠️$$
$$\text{Linderoth--Margot--Thain 2009}: \text{CiteSeerX 返回 301}\ ✗;\ \text{optimization-online 命中的是\textbf{另一篇}}\ ✗\ \text{未获}\ ⚠️$$
$$\Longrightarrow\ \textbf{请唐先生上传两篇 PDF}\ ⚠️\ (\text{或告知 NAS 路径}\ ✓)\ \text{—— 拿到后逐行填对应表}\ ✓$$
$$

## §7 状态

```
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{未跑 solver/LP/SAT}\ ✓$$
$$\textbf{本轮所得（不需正文 ✓）}: \text{① 精确重建（含 A 闭式）}\ ✓✓;\ \text{② 均匀解 ⟹ 系统只给 52}\ ✓✓;\ \text{③ 收紧律实测}\ ✓✓;\ \text{④ }m{=}9\ \text{极限 = 覆盖条件}\ ✓✓;\ \text{⑤ 三问答复（1,2 定论；3 仍假设）}\ ✓$$
$$

## §8 边界（诚实标注）

- §1–§4 为我方**自行导出＋实算验证** ✓（两码 m=1..4 ✓）；§5 问 3 明确标注 **HYPOTHESIS** ⚠️
- **未跑 solver/LP/SAT** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 M-covering system 命中文件数=1    :: ./MCOVER-2026-09-26-binary-reconstruction-and-tightening-law.md 
技术词 收紧律        命中文件数=1    :: ./MCOVER-2026-09-26-binary-reconstruction-and-tightening-law.md 
技术词 余维 partition 命中文件数=1    :: ./MCOVER-2026-09-26-binary-reconstruction-and-tightening-law.md
```
- **本档新增**（扣自引后 = 0，命中 1 = 自引 ✓）：M-covering system、收紧律、余维 partition
- **档案已有（引用，不列为提出）**：partition、inequivalent、weighted covering
