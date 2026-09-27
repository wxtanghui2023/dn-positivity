# P1-AVOID-2026-09-27 — **勘误（C-408 数值前提）** ＋ **avoidance 反证接口** ＋ 第一个 avoidance 几何推论

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:47 令 ✓）**：勘误 C-408；攻 "square/tetra avoidance ⟹ 451-budget violation" 接口；零程序计算 ✓；不碰 profile 极值优化 ✗（除勘误所涉 ✓）。

**已查地图：命中（接续 R4-P1／R7-LOCK／P1-TETRA，非新案 ✓）**
所查：`docs/P1-TETRA-2026-09-27-…`（**中点定理／可达反证／上界 842** ✓✓）｜`docs/R7-LOCK-2026-09-27-…`（**接口恒等式** ✓✓）｜`docs/R4-P1-2026-09-27-…`（**$p(c)=10-|S\cup V(H_c)|$／451** ✓✓）｜`docs/R6/R7-2026-09-27-…`｜`docs/C3-119-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** $K_4$ 亏空／占用预算对象的**勘误与反证接口**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出占用恒等式的显式形式（$451-\sum_{j\ge3}(j-2)n_j$）＋ avoidance 的第一个局部几何推论 ＋ 刀锋式等价重述** ✓）
**[RESEARCH]**

---

## §0 结论（**勘误 ✓｜方向性纠正 ✓｜一个新推论 ✓｜诚实 ✗**）

$$\boxed{\textbf{(1) 勘误（照唐先生 ✓）}:\ T_3\le28\binom{10}3+\binom53=3370\ \textbf{不是无条件};\ \text{它\textbf{依赖 profile-concentration 前提}}\ (E=285=28\cdot10+5)✓✓}$$
$$\qquad\Longrightarrow\ N_{\rm tetra}\le T_3/4\le\mathbf{842}\ \text{亦\textbf{带同一前提}}✓\ (\text{原 C-408 §4 未注明 ⟹ 本档勘误 ✓})$$
$$\boxed{\textbf{(2) 方向性纠正（重要 ✗✓）}:\ \text{占用量\textbf{不是自由预算，而是恒等式锁定}}:\ \sum_c\big|S(c)\cup V(H_c)\big|=1190-n_1=\boxed{451-\sum_{j\ge3}(j-2)n_j}\ \le\ \mathbf{451}\ \textbf{恒成立}}✓✓$$
$$\qquad\Longrightarrow\ \text{"avoidance}\Longrightarrow\sum|\cdot|>451\text{"}\ \textbf{不可能成立}✗\ (\text{因上界恒真});\ \textbf{可用方向是下界}:\ \text{avoidance}\Longrightarrow\sum|\cdot|\ge\mathbf{452}✓$$
$$\qquad\Longrightarrow\ \text{该陈述\textbf{等价于} P1\ \textbf{本身}}✗✓\ (\text{非减弱，是重述 ✓——诚实标注 ✓})$$
$$\boxed{\textbf{(3) avoidance 的第一个几何推论（新 ✓）}:\ i,j\in S(c)\Longrightarrow c{\oplus}e_i{\oplus}e_j\notin C\ \Longrightarrow\ \boxed{d_2(c)\le45-\binom{|S(c)|}2}\ ✓✓}$$
$$\boxed{\textbf{(4) 现状 ✗}:\ \text{接口\textbf{未证成}};\ \text{(3) 求和后\textbf{弱}（}N_2\le2671\ \text{劣于 }388\ ✗\text{）}\ \Longrightarrow\ \text{须更强推论 ⚠️}}$$

---

## §1 勘误（**C-408 §4 的数值前提 ✓**）

$$\text{C-408 §4 原文}:\ T_3\le28\binom{10}3+\binom53=28\cdot120+10=3370✓\ \text{—— \textbf{数值本身正确} ✓ 但\textbf{前提未注}✗}$$
$$\textbf{前提 ✓（照唐先生逐字）}:\ 28,10,5\ \text{来自 }28\times10+5=285\ \text{—— 即把总 excess }E=285\ \text{\textbf{集中}成 28 个 }\delta{=}10\ \text{与 1 个 }\delta{=}5✓$$
$$\qquad\Longrightarrow\ \text{这是 \textbf{profile-concentration}（}\delta\le10\ \text{下的\textbf{极端 profile}）\ \text{的产物}✓;\ \textbf{仅凭 }b\le11\ \text{得不到} ✗✓$$
$$\textbf{勘误后表述 ✓}:\ \boxed{\text{在既有 profile-concentration 框架下 }T_3\le3370,\ N_{\rm tetra}\le842\ (\mathbb Z\Rightarrow\le842)✓;\ \textbf{非无条件}✗}$$
$$\textbf{（结论不变 ✓）}:\ \text{该界为\textbf{上界}};\ \text{未产生 P1 lower bound};\ \text{不改变 STOP 结论}✓$$

## §2 **占用恒等式**（**本档核心之一 ✓✓**）

$$\text{由 R4-P1 §2 ✓}:\ p(c)=10-\big|S(c)\cup V(H_c)\big|✓;\qquad \sum_c p(c)=n_1✓\ \Longrightarrow\ \sum_c\big|S(c)\cup V(H_c)\big|=1190-n_1✓$$
$$\text{由 R4-P1 §1 ✓}:\ n_1=1024-285+\sum_{j\ge3}(j-2)n_j=739+\sum_{j\ge3}(j-2)n_j✓$$
$$\Longrightarrow\ \boxed{\sum_c\big|S(c)\cup V(H_c)\big|=451-\sum_{j\ge3}(j-2)n_j\ \le\ 451}\ ✓✓\ \text{（\textbf{恒等式}，非不等式猜测 ✓）}$$
$$\textbf{读法 ✓✓}:\ \text{① 上界 451 \textbf{恒真}} ⟹ \text{任何"突破上界"的反证形态\textbf{逻辑上不可能} ✗};\ \text{② 占用量的值与 }\sum_{j\ge3}(j-2)n_j\ \text{一一绑定（＝}\textbf{profile 量}✗）}$$
$$\qquad\Longrightarrow\ \textbf{⚠️ 重要（诚实）}:\ \text{占用预算\textbf{不是独立几何 handle};\ \text{它与 profile 同源}✗\ —— \text{与 R7 STOP 的同一形态 ✓}$$

## §3 avoidance 的**局部推论**（**新 ✓；但弱 ✗**）

$$\textbf{avoidance 定义 ✓}:\ N_{\rm square}=N_{\rm tetra}=0\iff \forall c:\ A(c)=0\ \wedge\ B(c)=0✓\ \big(A(c):=\#\{\{i,j\}\subseteq S(c):c{\oplus}e_i{\oplus}e_j\in C\}✓,\ B(c):=\#\{3\text{-子集}\{i,j,k\}:c{\oplus}e_i{\oplus}e_j,c{\oplus}e_i{\oplus}e_k,c{\oplus}e_j{\oplus}e_k\in C\}✓\big)$$
$$\textbf{(3) 的推导 ✓}:\ A(c)=0\ \text{且 }i,j\in S(c)\Longrightarrow c{\oplus}e_i{\oplus}e_j\notin C✓;\ \text{而 }c{\oplus}e_i{\oplus}e_j=c'{\oplus}e_j\ (c'{=}c{\oplus}e_i)✓$$
$$\qquad\Longrightarrow\ \text{距离-2 邻居的坐标对 }\{i,j\}\ \text{中\textbf{至多一个}属于 }S(c)\ \Longrightarrow\ d_2(c)\le\#\{\{i,j\}:|\{i,j\}\cap S(c)|\le1\}=45-\binom{|S(c)|}2✓✓$$
$$\textbf{求和 ✓}:\ 2N_2=\sum_c d_2(c)\le119\cdot45-\sum_c\binom{d_1(c)}2\ \underset{\text{凸性}}{\le}5355-119\binom{2N_1/119}2\ \approx 5355-13\Longrightarrow N_2\le2671\ ✗\ (\text{\textbf{弱于}既有 }N_2\le388\ ✗)$$
$$\textbf{故 ✓}:\ \text{单靠 (3) 不足以逼近刀锋 ⟹ 需\textbf{更强}的 avoidance 推论 ⚠️};\ \text{但 (3) 是\textbf{本线第一个由 avoidance 产生的真几何约束}✓✓\ (\text{非 profile 型 ✓})$$

## §4 **刀锋式重述**（**等价性 ✓；诚实 ✗**）

$$\text{由 §2}:\ \sum_c\big|S(c)\cup V(H_c)\big|\le451\ \text{恒真};\qquad \text{covering 平均}:\ \tfrac{451}{119}\approx\mathbf{3.7899}\ (\text{即每码字平均 }<4\ ✓)$$
$$\textbf{目标（照唐先生 ✓）}:\ \text{avoidance}\Longrightarrow\sum_c\big|S(c)\cup V(H_c)\big|\ge\mathbf{452}\ \Big(\iff\text{平均}\ge3.798\ ✗\ \text{—— 只差 }\mathbf 1\ \text{个单位 }\Big)✓$$
$$\textbf{⚠️ 等价性（必须一同引用 ✓）}:\ \text{由 §2 恒等式},\ \sum|\cdot|\ge452\iff\sum_{j\ge3}(j-2)n_j\le-1\ \textbf{不可能}✗;$$
$$\qquad\Longrightarrow\ \text{"avoidance}\Longrightarrow\sum|\cdot|\ge452\text{"}\ \textbf{等价于}「\text{avoiding cover 不存在}」\iff\textbf{P1 本身}✓$$
$$\qquad\Longrightarrow\ \text{(诚实 ✗)}:\ \text{本接口是 P1 的}\textbf{重述}，\textbf{不是减弱}\ ✗——\text{其价值在于给出"}\textbf{一个单位的定量缺口}"形态 ✓（可被局部计数攻 ✓）$$

## §5 下一步（**诚实建议 ✓**）

$$\text{① 须找\textbf{比 (3) 更强}的 avoidance 局部推论（例如涉及 }B(c)=0\ \text{对 }\sum|S\cup V|\ \text{的直接压制）⚠️}$$
$$\text{② 必须避免再落回 profile 量 ✗}:\ \text{§2 表明"占用预算"与 }\{n_j\}\ \text{同源 ⟹ 用它作 handle 会重演 R7 STOP ✓}$$
$$\text{③ 候选（登记未做 ✓）}:\ \text{把 }\delta\ge3\ \text{的点（}b\ge4\text{）与 avoidance 的}\textbf{局部形状禁令}\ \text{对撞};\ \text{或用 R4-P1 的 }|S\cup V|\ \text{逐 }c\ \text{分布（而非只和）✓}$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "占用恒等式"
技术词 占用恒等式      命中文件数=0    ::
$ bash scripts/tech_word_check.sh "禁避"
技术词 禁避            命中文件数=0    ::
$ bash scripts/tech_word_check.sh "刀刃"
技术词 刀刃            命中文件数=1    :: ./C380-S1-STEP0.md
$ bash scripts/tech_word_check.sh "避开"
技术词 避开            命中文件数=91   :: ./E177-E178-support-geometry-closure.md ./C222-B-interval-newton-KKT-strict-box-X0-existence-and-uniqueness.md ./V181-S-line-structural-closure-audit-and-mainline-handoff.md
```
- **本档新增**：**0** 个术语 ✓（`占用恒等式`／`禁避` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`刀刃`／`避开` 档案已有 ✓）
- **注 ✓**：本档实质＝**§1 勘误 ＋ §2 恒等式 ＋ §3 局部推论 ＋ §4 等价重述**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** P1 成立 ✗（V290）；**不声称** avoidance 必然不可能 ✗ —— 只给**恒等式**、**局部推论**与**等价性标注** ✓
- **§4 的等价性必须与"刀锋目标"同引** ✓（防把重述当减弱 ✗）
- **§2 的"占用量 ≢ 独立 handle"必须与 R7 STOP 同引** ✓（防重复踩坑 ✓）
