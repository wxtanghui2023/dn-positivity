已查地图（**先查后写**）：`C-133`（核维数判据：`K(W)=N−2W`；满窗口核＝常数；整数性＋总量封死均匀平移）、`C-137`（数据类型层：support ≤ 1 给模长／自相关，不给相位；缺口重写＝"相位→不等式"）、`C-132`（F3 反例；逃逸＝加均匀测度）、`C-124` 刀②（阈值现象：严格刚性需 `R≤253` ＋ 精确数据）、`C-125`／`C-126`（饱和／信息位于收敛边界）、`W6`（support>1 原子墙）。关键词回查：`窗口完备性`=0、`完备窗口`=0、`不可见补集`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 11:48「甲2」）**：**甲2 第二刀** —— 既然判定是"数据类型层失败"，追问：**为什么 toy 侧有刚性而 ζ 侧没有？** 答：差在**窗口完备性**。
**结论（先行）**：$$\textbf{(一)}\ \text{推广}\ \text{`C-133`}：\boxed{\textbf{秩刚性}\iff\textbf{窗口完备}（\text{核}＝\text{常数}）}✓✓$$
$$\textbf{(二)}\ \text{toy（}\text{`B2-1`}）\ \textbf{完备}：\text{窗口}\ j=1..255＝\mathbb Z/256\ \text{的全部非零频率} \Longrightarrow \text{核}＝\text{常数} \Longrightarrow \text{唯一逃逸＝均匀平移} \Longrightarrow \text{被}\ \textbf{整数性＋总量} \text{封死}✓✓$$
$$\textbf{(三)}\ \zeta\ \textbf{不完备}：\text{观测窗口}＝\text{support}\le1; \text{而频率总体}\ \textbf{无限} \Longrightarrow \text{核}＝\textbf{不可见补集}\ \textbf{无穷维} \Longrightarrow \textbf{无刚性}✓✓$$
$$\textbf{(四)}\ ⭐\ \zeta\ \text{在}\ \textbf{两轴同时失败}：\text{①}\textbf{数据类型}（\text{模长，无相位}；\text{`C-137`}）\text{②}\textbf{窗口不完备}（\text{部分频率；本档}）✓✓$$
$$\textbf{(五)}\ ⟹\ \text{ζ 侧路线需要}：\textbf{完备窗口}（＝\text{support}>1＝\text{`W6`}）＋\textbf{相位或其替代品} —— \text{两者目前均不可提供}✓✓$$

FREEZE-ACK: 本档即冻结期内的判据推广与两轴对质（依 `§8.1`；不产候选结论）

D0: 本档对象 = **窗口完备性判据 ＋ toy/ζ 两轴对质 ＋ "整数性技巧为何不能平移到 ζ"的解释** —— 关系 = 判据推广与对质，非新机制
D1: 0

# C-138 · **甲2 第二刀：窗口完备性判据 —— 刚性 ⟺ 窗口完备；ζ 在两条轴上同时失败**

> **唐先生 2026-09-19 11:48**：**「甲2」**（第二刀：为何 toy 有刚性而 ζ 没有）✓

---

## §1 判据（严格形式）

$$\text{设观测窗口}＝\text{频率集}\ \Omega\subseteq\hat G;\quad \text{不可见空间}\ K(\Omega):=\{w:\hat w|_\Omega=0\}✓$$
$$\textbf{定义}：\textbf{窗口完备}\iff K(\Omega)＝\text{常数}\quad(\text{即}\ \Omega=\hat G\setminus\{0\})✓✓$$
$$\textbf{判据}：\textbf{秩刚性}（\text{解集有限／秩有界}）\ \textbf{在窗口不完备时不可能}：$$
$$\qquad \dim K(\Omega)=\infty \Longrightarrow \text{可任意扰动支撑而}\ \textbf{不改观测}✓✓$$
$$\text{注}：\text{完备性在}\ \textbf{有限群} \ \text{上可实现}（\mathbb Z/N:\Omega=\{1..N-1\}\Longrightarrow K＝\text{常数},\ \text{`C-133`}\ \text{实测}\ \dim=1）;\ \text{在}\ \textbf{无限频率集} \ \text{上"完备"}\,\Longrightarrow\,\text{观测全部频率}✓$$

## §2 toy 侧：完备 ⟹ 刚性如何成立

$$\text{窗口完备}（\text{核}＝\text{常数}）\Longrightarrow \text{唯一逃逸}＝\textbf{均匀平移}✓$$
$$\text{均匀平移被两条约束封死}：\text{marks}\in\{1,2\}\ \text{与}\ \sum m=256\quad(\text{`C-133`}\ \text{逐字})✓✓$$
$$\Longrightarrow\ \text{toy 的"刚性"}＝\textbf{完备窗口}＋\textbf{整数性替代相位}\ \text{的}\ \textbf{合力}✓✓$$
$$\qquad ⚠️\ \text{但注意}\ \text{`C-124`}\ \text{刀②阈值现象}：\text{严格的秩刚性仍需}\ R\le253\ \text{＋精确数据} \Longrightarrow \text{toy 侧刚性}\ \textbf{仍是条件性}✓$$

## §3 ζ 侧：**两轴同时失败**（本档核心）

$$\text{轴一（数据类型）}：\text{support}\le1\ \text{给}\ \textbf{模长／自相关}（\text{`C-137`}）\ ✗✓$$
$$\text{轴二（完备性）}：\text{频率总体无限},\ \text{观测只覆盖一部分}（\text{support}\le1） \Longrightarrow K(\Omega)\ \textbf{无穷维} \Longrightarrow \text{可任意改变支撑而不改观测}\ ✗✓$$
$$\qquad ⚠️\ \text{但 ζ 侧的"质量约束"类比}\ \textbf{存在}：\sum_{n\le X}\Lambda(n)\approx X\ \text{固定};\ \text{支撑在离散集}\ \{\log n\}\ \text{上}✓$$
$$\qquad \textbf{然而它不能替代完备性}（\text{本档关键区分}）：$$
$$\qquad\qquad \text{toy 的逃逸是}\ \textbf{质量方向}（\text{加均匀质量}）\Longrightarrow \text{被质量约束封死}✓✓$$
$$\qquad\qquad \text{ζ 的逃逸是}\ \textbf{频率补集方向}（\text{补集上的任意扰动}）\Longrightarrow \text{质量约束}\ \textbf{无关}✓✓$$
$$\qquad ⟹\ \boxed{\text{这就是}\ \textbf{整数性技巧不能平移到 ζ} \text{的原因}}✓✓$$

## §4 判定表

$$\begin{array}{c|c|c|c}
\text{设定} & \text{数据类型} & \text{窗口完备性} & \text{刚性}\\\hline
\text{toy}（\mathbb Z/256） & \text{模长}\ ✗ & ✓\ \text{完备}（\text{核}＝\text{常数}） & \textbf{条件性可得}（\text{整数性封逃逸}）\\
\zeta（\text{support}\le1） & \text{模长}\ ✗ & ✗\ \textbf{不完备}（\text{核无穷维}） & \textbf{不可得}\\
\text{理想} & \text{复}（\text{含相位}） & \text{完备} & \text{可恢复}（\text{Prony}）\\
\end{array}✓✓$$

## §5 ζ 侧路线需要什么（精确化）

$$\text{需要}：\textbf{完备窗口}（\iff\text{观测全部频率}\iff\text{support}>1＝\text{`W6`}）\ ＋\ \textbf{相位（或其替代品）}✓✓$$
$$\qquad ⚠️\ \textbf{结构判断（非定理）}：\text{ζ 侧的"完备性"要求可能}\ \textbf{已等价于 RH 级输入}（\text{因"观测全部频率"＝知道全部对数相关信息}）✓$$
$$\qquad ⟹\ \text{与}\ \text{`C-125`／`C-126`}\ \text{的"信息位于收敛边界"}\ \textbf{同址}：\text{本判据给出其}\ \textbf{窗口语言版}✓✓$$

## §6 边界与回查

- ⚠️ §1 判据为**本档推广**（由 `C-133` 的实测核维数推广到一般窗口）；**非定理**（未证"不完备 ⟹ 刚性不可能"的完整形式）✓
- ⚠️ §4 表中 ζ 行的"不可得"为**结构判断**（依轴一＋轴二）✓
- ⚠️ §5 的"可能已等价于 RH 级输入"标**结构判断·非定理**✓
- ⚠️ **不声称** ζ 侧绝无任何刚性机制；只判：**在两轴均失败的现状下不可得** ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 11:5x）`[纪律]`（先跑后写）

```
技术词 窗口完备性   命中文件数=0 ::  ⟹ 本档新增
技术词 完备窗口    命中文件数=0 ::  ⟹ 本档新增
技术词 不可见补集   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓

---

## 【更正·`C-139`】（2026-09-19 11:55）

⚠️ §1 判据**过强**：正确的刚性阈值是**共轭饱和**（`W ≥ N/2`），不是窗口完备（`W = N−1`）。
机制：周期 2 梳 $(+1,-1,\dots)$ 的 DFT 只支撑在 $j=N/2$，故对 $W<N/2$ 它是**可准入**（$\pm1$、零和）的不可见扰动。
ζ 侧结论不变（直线上的饱和＝全部频率＝`W6`），但要求的结构被精确化。
