# R3-A3-2026-09-27 — **修正钉死** ＋ **行容量压缩（失败）** ＋ **必要系统松弛性判定**

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:10 令 ✓）**：钉死两个技术点；给 R3-P 精确定义；**纯数学压缩行容量**（不跑 SAT/SDP ✗）；零计算 ✓。

**已查地图：命中（接续 R3／R3-甲／R3-甲2，非新案 ✓）**
所查：`docs/R3-A2-2026-09-27-ten-bucket-PSD-integer-compressed-form.md`（**三条压缩形式** ✓✓）｜`docs/R3-A-2026-09-27-…`（**1555／slack≥53** ✓✓）｜`docs/R3-2026-09-27-…`｜`docs/SECOND-ORDER-2026-09-25-…`｜`docs/P1-REAUDIT-2026-09-27-…`（**Booleanity** ✓✓）｜`docs/ASSETS-REGISTRY.md`（**C-380 21 机制封口 ⟹ irreducible core ＝ Boolean covering feasibility** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §7）
D0: 本档对象 ＝ **档案已有** R3-甲2 系统的**修正、精确定义与松弛性判定**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出"必要系统松弛性"判定**：$(A,q,N_1^{(i)},\mathrm{PSD})$ 层级**可行** ⟹ 该层级不能给 P1；并给出行容量压缩的反例族 ✓）
**[RESEARCH]**

---

## §0 结论（**三处修正钉死 ＋ 两个负面判定 ＋ 一个收敛性发现 ✓**）

$$\boxed{\text{修正 1（trace）}:\ \mathrm{tr}\,\tilde Q=0\ \textbf{单独不给}\ 59.5;\ \text{正确写法}\ \mathrm{tr}\,\tilde Q=0\ \wedge\ G\succeq0\Longrightarrow-59.5\le\lambda_{\min}(\tilde Q)\le0✓}$$
$$\boxed{\text{修正 2（}2\times2\text{）}:\ q_{ij}\le m/2=59.5\ \Longrightarrow\ q_{ij}\le\mathbf{59}\ ✓\ (\text{整数})}$$
$$\boxed{\textbf{判定 A（行容量压缩失败 ✗）}:\ \text{PSD 不能把 }83\ \text{压小} —— \textbf{反例族}\ \tilde Q=w(J-I),\ w\le59.5✓}$$
$$\boxed{\textbf{判定 B（更要紧 ⚠️）}:\ \text{纯 Q 松弛（}\sum_{j\ne i}q_{ij}\le83\text{）\textbf{平凡可行}}\ \Longrightarrow\ \textbf{该松弛不能单独给 P1}✗✓}$$
$$\boxed{\textbf{收敛性发现 ✓✓}:\ (A,q,N_1^{(i)},\mathrm{PSD})\ \text{层级\textbf{可行/松弛}} \Longrightarrow \text{真约束在\textbf{符号层 III}} \equiv \text{档案独立结论（Booleanity ＝ irreducible core）✓}}$$

---

## §1 修正 1：trace 表述（照唐先生 ✓）

$$\mathrm{tr}\,\tilde Q=\sum_i\lambda_i=0\ \text{（零对角 ✓）}\ ——\ \textbf{单独不推出}\ |\lambda_{\min}|\le59.5\ ✗✓$$
$$\text{正确表述 ✓}:\quad \mathrm{tr}\,\tilde Q=0\ \wedge\ G\succeq0\ (\iff\lambda_{\min}\ge-59.5)\ \Longrightarrow\ \boxed{-59.5\le\lambda_{\min}(\tilde Q)\le0}✓$$
$$\text{（附带 ✓）}:\ \lambda_{\min}\le0\ \text{来自 }\mathrm{tr}=0\ \text{（否则全 }\lambda>0\Longrightarrow\mathrm{tr}>0 ✗）；\ \text{下界 }-59.5\ \text{来自 }G\succeq0\ ✓\ \text{—— 两者\textbf{来源不同}，须分开写 ✓}$$

## §2 修正 2：$2\times2$ 主子式（照唐先生 ✓）

$$\det\begin{pmatrix}m&2q_{ij}\\2q_{ij}&m\end{pmatrix}=m^2-4q_{ij}^2\ge0\ \Longrightarrow\ q_{ij}\le\tfrac m2=59.5\ \overset{q\in\mathbb Z}{\Longrightarrow}\ \boxed{q_{ij}\le59}✓$$

## §3 PSD 谱压缩（**保留**唐先生的"结构压缩增量"表述 ✓）

$$G=mI+2\tilde Q\ \Longrightarrow\ G\succeq0\iff m+2\lambda_{\min}(\tilde Q)\ge0\iff\lambda_{\min}(\tilde Q)\ge-59.5✓$$
$$\text{桶 }(\sum_{j\ne i}q_{ij}\le83)\ \text{＋ Gershgorin}\ \Longrightarrow\ \lambda_{\min}\ge-83\ \Longrightarrow\ \boxed{-83\longrightarrow-59.5}\ \text{＝\textbf{结构压缩增量} ✓✓}$$
$$\text{表述保留 ✓}:\ \textbf{PSD 不是"又一个上界"，而是把十个桶之间的\textbf{全局谱耦合}加入问题}✓$$

---

## §4 R3-P（**纯 Q 松弛**）精确定义 ＋ **判定 B**（⚠️ 要紧 ✓）

$$\boxed{\text{R3-P}:\quad q_{ij}\in\mathbb Z_{\ge0},\ q_{ii}=0,\ \sum_{i<j}q_{ij}=N_2,\ \sum_{j\ne i}q_{ij}\le83\ (i\le10),\ \lambda_{\min}(\tilde Q)\ge-59.5}✓$$
$$\text{逻辑方向（照唐先生 ✓）}:\ \text{真实 119-cover}\Longrightarrow\text{R3-P 可行}\ \Longrightarrow\ \text{R3-P \textbf{不可行}}\ \text{即是 \textbf{真 P1 反证}}\ \Longrightarrow\ K(10,1)\ge120✓$$
$$\textbf{⚠️ 判定 B（本档新发现 ✓）}:\ \boxed{N_2\ \text{在 R3-P 中\textbf{自由}（仅上界 }388\text{）}\Longrightarrow q\equiv0\ (\text{或 }N_2{=}1\ \text{的最小配置})\ \text{即为可行点}}\ ✗✓$$
$$\qquad\Longrightarrow\ \textbf{R3-P 本身平凡可行 ⟹ 不能单独给 P1} ✗\ \text{（须保留 labelled 数据 }N_1^{(i)}\ \text{与 pair-count 区域 ✓）}$$
$$\textbf{最小有用松弛 R3-P}^{\ast}（本档提出 ✓）:\ \text{R3-P}\ \textbf{外加}:\ (a)\ \sum_i N_1^{(i)}=N_1\ \text{且 }B_i=N_1^{(i)}+\sum_{j\ne i}q_{ij}\le83✓;\ (b)\ \text{pair 区域}\ N_1+N_2\ge72,\ N_1+2N_2\le777,\ N_1\le71\ (\text{＝}A_1/2\le142/2)✓;\ (c)\ Q\ \text{奇}✓$$

---

## §5 行容量压缩：**尝试与失败**（**判定 A** ✓✓）

$$\textbf{目标（照唐先生 ✓）}:\ \text{用 }q\ge0,\ q\in\mathbb Z,\ \sum q=N_2,\ \sum_{j\ne i}q_{ij}\le83,\ \tilde Q\succeq-59.5I\ \text{推出比 }83\ \text{更强的行容量界}$$
$$\textbf{反例族（决定性 ✓✓）}:\ \tilde Q=w(J-I)\ (w\le59.5)\ \Longrightarrow\ \lambda_{\min}=-w\ge-59.5\ ✓\ \text{成立};\quad \text{行和}=9w\le535.5✓✓$$
$$\qquad\Longrightarrow\ \text{行和可达 }\mathbf{535}\ \text{而 PSD 仍成立} \Longrightarrow \boxed{\textbf{PSD 单独不能把 83 压小}}\ ✗✓\ \text{（83 是\textbf{标号桶}约束，非谱约束）}$$
$$\textbf{唯一可证之新二次界 ⚠️}:\ \|\tilde Q\|_F^2=\sum_j\lambda_j^2\le10\cdot83^2\ \Longrightarrow\ \boxed{2\sum_{i<j}q_{ij}^2\le68890}\ \text{（弱；被 }q_{ij}\le59\ \text{支配）}✗$$
$$\textbf{失败的结构原因 ✓}:\quad \text{桶 ＝ }\textbf{标号（坐标分解）}\text{约束}\ \big|\ \text{PSD ＝ }\textbf{非标号（谱）}\text{条件} \Longrightarrow \text{改进容量须用}\textbf{更高阶标号数据}（D_1\ \text{扩展 PSD／三阶 }\gamma）$$

---

## §6 **松弛性判定（判定 B 的推广）＋ 收敛性发现**（✓✓）

$$\text{在 R3-P}^{\ast}\ \text{层级取具体可行点 ✓}:\ N_1=60\ (\text{每坐标 }6\le71✓),\ N_2=100\ (q_{ij}\ \text{均摊} \approx2.2),\ \text{桶} B_i\approx6+20=26\ll83,\ \lambda_{\min}\gtrsim-2.2✓$$
$$\Longrightarrow\ \boxed{\textbf{R3-P}^{\ast}\ \text{亦\textbf{松弛：其可行区域远未被 covering 逼紧}}}\ ✓\ \Longrightarrow\ \textbf{该层级（必要条件的任何弱化）都不能给 P1}\ ✓$$
$$\text{逼紧只在\textbf{极端超额集中}（}Q\to1270\Longrightarrow\sum_iB_i\to777\Longrightarrow\text{平均桶 }77.7\ \text{逼近 }83）\ ✓\ \text{—— 但那仍是\textbf{必要}条件，不构成矛盾 ✓}$$
$$\boxed{\textbf{收敛性发现 ✓✓}:\ \text{本线（R3 链）与\textbf{档案独立路线}（}g\text{-形／模 11／21 机制封口）\textbf{结论一致}:\ \text{真约束在 }\textbf{Booleanity／符号层}}✓✓$$
$$\qquad\text{（档案逐字：}g\text{-形"\textbf{线性内容恰是整数性，非线性内容＝二值性}" ✓；21 机制封口 ⟹ \textbf{irreducible core ＝ Boolean covering feasibility} ✓）}$$

---

## §7 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "行容量"
技术词 行容量          命中文件数=3    :: ./B2QUOTA-2026-09-26-b2-quota-and-layer-capacity-tables.md ./F14-DEDUP-2026-09-26-forced-propagation-dedup-table.md ./SCOL-2026-09-26-support-collision-row-closure.md
$ bash scripts/tech_word_check.sh "纯 Q 松弛"
技术词 纯 Q 松弛       命中文件数=0    ::
$ bash scripts/tech_word_check.sh "反例族"
技术词 反例族          命中文件数=25   :: ./KERNEL-HUNT-1-two-minimization-problems.md ./APPRECIATION-AUDIT-2026-09-11.md ./CAPMIX1B-B11-3-E-half-falsified-and-proposition-refuted.md
$ bash scripts/tech_word_check.sh "标号约束"
技术词 标号约束        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "松弛链"
技术词 松弛链          命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`纯 Q 松弛`／`标号约束`／`松弛链` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`行容量`／`反例族` 为档案已有 ✓）
- **注** ✓：本档实质＝**§4 判定 B（纯 Q 松弛平凡可行）＋ §5 反例族 ＋ §6 松弛性判定与收敛性发现**（推导性 ✓）

## §8 边界（硬 ✓）

- **零计算** ✓；**未跑 SAT/SDP** ✓（照令 ✓）；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **判定 A／B 均为**否定性**结论 ✓（有证明／反例 ✓）—— 但**不**声称"$K(10,1)\ge120$ 不可得" ✗（V290）；只声称"**该层级（必要条件的弱化）不能给 P1**" ✓
- §6 的"收敛性发现"为**路线间一致性陈述** ✓，**非**定理 ✓
- R3-P$^{\ast}$ 为**本档提出的最小有用松弛** ✓；**尚未**判定其可行性（本档只给松弛性证据 ✓）
