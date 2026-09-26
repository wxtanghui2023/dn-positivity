已查地图：已跑 scripts/prework_map_check.sh P2-α LP 加权覆盖 对象匹配 ⟹ 执行自 PROVENANCE-2026-09-26 档；本档为**P2-α 三刀：frontier audit ＋ 对象匹配 ＋ LP 骨架（不跑 solver）**（唐先生 2026-09-26 17:45 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = Östergård–Blass 方法状态变量、参考文献口径、我们的覆盖矩阵对齐、N₄≤9 的可加性、LP 骨架
D1: 1（新增：**frontier audit 结论（不覆盖）** ✓✓；**对象对齐（b 是派生量）** ✓✓；**LP 骨架（含子空间扩展）** ✓✓）

# P2ALPHA-2026-09-26

## §1 ⭐⭐ **第一刀：frontier audit（结论：不覆盖 ✗）**

```
$$\text{源}: \text{Östergård \& Blass, IEEE TIT 47(6) 2556--2557 (2001)}\ ✓;\ \textbf{DOI} = 10.1109/18.945268\ ✓$$
$$\textbf{摘要逐字（完整 ✓）}: \text{"...}\textbf{which is computer-aided}\text{, possible distributions of codewords in subspaces are refined}$$
$$\qquad\text{until each subspace is of dimension zero (consists of only one word). Repeatedly, a }\textbf{linear programming problem}$$
$$\qquad\text{is solved considering only }\textbf{inequivalent distributions}\text{. A connection between this approach and}$$
$$\qquad\textbf{weighted coverings}\text{ is also presented; the computations give }\textbf{new results for such coverings}\text{ as a by-product."}$$
$$\textbf{文献表要点}: \text{① 《Covering Codes》专著（Cohen–Honkala–Litsyn–Lobstein 1997}\ ✓\ \text{= weighted covering 出处}\ ✓)$$
$$\qquad\text{② Kolev 1998 "A (9,56)}_{1}\ \text{binary code does not exist"}\ ✓\ (\text{即 }57\ \text{下界来源}\ ✓);\ \text{③ nauty（判不等价}\ ✓);\ \text{④ Östergård–Weakley 2000（分类}\ ✓)$$
$$\textbf{Audit 答案（三个具体问题）}:$$
$$\quad\text{(a) LP 的状态变量记录什么？}\ \Longrightarrow\ \textbf{子空间内的"码字分布"}（按不等价型）\ ✓\ ——\ \textbf{不是 }b(x)\ \text{型数据}\ ✗$$
$$\quad\text{(b) 是否记录 }b(x)\ \text{分布 / }b{=}3,4\ \text{频数？}\ \Longrightarrow\ \textbf{否}\ ✗\ ——\ b(x)\ \text{是\textbf{派生量}（由码字分布可算}\ ✓\ \text{但不进状态}\ ✗)$$
$$\quad\text{(c) weighted covering 的权函数定义在什么对象上？}\ \Longrightarrow\ \text{覆盖矩阵的对偶权（专著口径}\ ✓)\ ✗\ \text{非 }b\text{-profile}\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{未发现已覆盖 }N_4\ge10\ \text{的定理/推论}}\ ✗✓\ (\text{by-product 是"weighted coverings 的新结果"}\ ✓,\ \text{与 }b\text{-profile 无关}\ ✗)$$
$$\textbf{诚实边界}\ ⚠️: \text{检索配额耗尽（tavily 432}\ ✗);\ \textbf{未做穷尽文献核查}\ ✗\ ——\ \text{结论是"未发现"而非"不存在"}\ ✓$$
$$
$$

## §2 ⭐⭐ **第二刀：对象匹配（b(x) 是派生量，但可线性化 ✓）**

```
$$\text{覆盖矩阵}: A_{xc}=\mathbf 1_{\{d(x,c)\le1\}}\ ✓;\quad b(x)=\sum_{c\in C}A_{xc}\ ✓;\quad \sum_x b(x)=M(n+1)=\mathbf{620}\ ✓$$
$$\text{我们的刚性条件} = \text{对"列和/行和分布"的条件}\ ✓:\quad \sum_x b(x)=620\ \checkmark;\quad N_j=\#\{x:b(x)=j\}\ ✓$$
$$N_4\le9\iff \#\{x:\sum_c A_{xc}=4\}\le9\ ✓\ ——\ \textbf{基数约束（非线性）}\ ✗\ \Longrightarrow\ \text{需指示变量}\ \checkmark\ (\text{ILP 可线性化}\ ✓)$$
$$\text{已知 }M=62\ \text{后}: (N_1,N_2,N_3,N_4)=(442-t,\ 32+3t,\ 38-3t,\ t)\ ✓\ \Longrightarrow\ t=N_4\ \text{是唯一自由度}\ ✓$$
$$\qquad\Longrightarrow\ \text{把 }N_4\le9\ \text{译成 LP 语言} = \text{把 }t\ \text{限制在 }\{0,\dots,9\}\ \text{的分布族内}\ ✓\ (\text{正好是 distribution refinement 的语言}\ ✓✓)$$
$$
$$

## §3 ⭐⭐⭐ **第三刀：LP 骨架（不跑 solver ✓）**

```
$$\textbf{骨架 A（经典对偶 = 加权覆盖）}: \text{找 }\ w(x)\ge0\ \text{使}\ \sum_x w(x)\,b(x)\ \text{被双向限制}\ ✓$$
$$\qquad\text{下界侧}: \sum_x w(x)\,b(x)=\sum_c\Big(\sum_x w(x)A_{xc}\Big)\ \le\ \sum_c \kappa(c)\ ✓\ (\kappa(c):=\text{单码字局部容量}\ ✓)$$
$$\qquad\Longrightarrow\ \text{若 }\sum_x w(x)\ \text{大而 }\kappa\ \text{受限}\ \Longrightarrow\ M\ \text{下界}\ ✓\ (\text{即原论文机制}\ ✓)$$
$$\textbf{骨架 B（唐先生提议的子空间扩展 ✓✓）}: \text{对余维 1 子空间 }H:\ N_j(H)=|\{x\in H:b(x)=j\}|\ ✓$$
$$\qquad\text{全局只给 }\sum_H N_j(H)=N_j\ ✗;\ \text{但 }\textbf{不同 }H\ \text{间还有约束}\ ✓\ (\text{码字在 }H/H^c\ \text{的分布}\ ✓)$$
$$\qquad\Longrightarrow\ \text{把 }\ b\text{-profile}\ \textbf{按子空间切开} = \textbf{把全局矩升级为"条件子空间分布"}\ ✓✓\ (\text{与原论文机制同层}\ ✓✓)$$
$$\textbf{目标形式（待建）}: \text{状态}:=(\text{子空间型},\ b\text{-profile}|_H)\ \text{的不等价类}\ ✓;\ \text{加 }t\le9\ \text{为 forbidden state}\ ✓\ \Longrightarrow\ \text{问 LP/ILP 不可行}\ ⚠️$$
$$
$$

## §4 状态与下一步

```
$$\textbf{三刀结果}: \text{① audit: 不覆盖}\ ✓\ (\text{诚实标注未穷尽}\ ⚠️);\ \text{② 对象匹配: }b\ \text{可线性化、}t\ \text{单一自由度}\ ✓✓;\ \text{③ 骨架: 需子空间扩展}\ ✓✓\ (\text{未跑 solver}\ ✓)$$
$$\text{下一步（须唐先生批 ✓）}: \text{把骨架 B 写成一个}\textbf{有限状态 ILP}\ ✓\ \text{并做可行性判断}\ ⚠️\ ——\ \text{先估规模与内存（纪律}\ ✓)$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §5 边界（诚实标注）

- §1 为**第三方摘要/文献表逐字**（OpenAlex/Crossref ✓）；§2–§3 为**我方对齐与骨架设计** ✓（**未跑任何 solver/LP** ✓）
- **未做穷尽文献核查**（配额耗尽 ⚠️）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 frontier audit   命中文件数=1    :: ./P2ALPHA-2026-09-26-frontier-audit-and-object-match.md 
技术词 对象对齐     命中文件数=6    :: ./ALIGN-variable-object-phase-three-level-audit.md ./R-A8.3-s2-mechanism-audit.md ./RESEARCH-CONSTITUTION.md 
技术词 子空间扩展骨架 命中文件数=1    :: ./P2ALPHA-2026-09-26-frontier-audit-and-object-match.md
```
- **本档新增**（扣自引后 = 0）：frontier audit、对象对齐、子空间扩展骨架
- **档案已有（引用，不列为提出）**：weighted covering、LP、A_xc
