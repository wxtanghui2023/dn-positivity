D0: 本档对象 = 档案已有 `V248` §3 的「判别锥必自对偶」命题 —— 关系 = 严格化（把直观步骤变成定理 ＋ 前提明确的推论）
D1: 0

FREEZE-ACK: 本档即冻结期内的严格化产物（依 `§8.1`；为负结果笔记，不产候选）

# 锥判据与自对偶性：为什么非自对偶正性锥不能加锐成员判据

**A note on cone criteria and self-duality: non-self-dual positivity cones cannot sharpen a membership criterion**

> 作者：Hui Tang ｜ 草稿 v1 · 2026-09-18 ｜ **性质：负结果笔记（独立数学笔记，非 RH 论文）**
> **来源**：本项目 `dn-project` 内部审计 `V248`（锥分离）§3 命题的严格化；**本笔记逐条自足，不引用项目内部档**

---

## §0 目的与范围（先行声明）

$$\textbf{本笔记证明}：\text{在"判据＝锥成员性"这一框架内，}\textbf{"自对偶"} \text{与}\ \textbf{"可加锐"} \text{不可兼得}✓✓$$
$$\textbf{本笔记不证明}：\text{任何关于 RH 的命题};\ \text{也不声称}\ \textbf{非锥型} \text{判据不存在}✓$$
$$\text{读者须知}：\text{§6 的 RH 读数为}\ \textbf{框架层解读，附明确前提}，\ \textbf{不是定理}✓$$

## §1 设置与记号

$$\text{设}\ V\ \text{为有限维实内积空间}，\langle\cdot,\cdot\rangle\ \text{为内积}✓$$
$$\text{设}\ K\subseteq V\ \text{为}\ \textbf{闭凸锥};\ \text{对偶锥}\ K^*:=\{y\in V:\ \langle y,x\rangle\ge0\ \ \forall x\in K\}✓$$
$$\textbf{自对偶}：K^*=K\ \（\text{记号固定于上述内积 —— }\textbf{自对偶性依赖内积选择}）✓✓$$
$$\textbf{锥判据}：\text{给定集合}\ \Theta\ \text{与映射}\ A:\Theta\to V，\ \text{则}\ K\ \text{给出判据}\ \ \theta\in\Theta_K\iff A(\theta)\in K✓$$
$$\textbf{松／紧}：K\subseteq L \Longrightarrow \Theta_K\subseteq\Theta_L\ \（\text{即}\ L\ \text{判据更松}）✓$$

## §2 两个初等引理

$$\textbf{引理 1（对偶单调性）}：K\subseteq L\ \text{（闭凸）} \Longrightarrow L^*\subseteq K^*✓$$
$$\qquad \text{证明}：y\in L^* \Longrightarrow \langle y,x\rangle\ge0\ \forall x\in L \Longrightarrow \text{特别}\ \forall x\in K \Longrightarrow y\in K^*\quad\blacksquare✓$$

$$\textbf{引理 2（自对偶锥不可被严格包含）}：\text{设}\ K,L\ \text{闭凸}，\ K\ \text{自对偶}，\ K\subseteq L✓$$
$$\qquad \text{则}\ L^*\subseteq K^*=K\subseteq L;\ \ \text{若进一步}\ L\ \text{自对偶}，\ \text{则}\ L=L^*\subseteq K \Longrightarrow L=K✓✓$$
$$\textbf{推论 2′}：\text{若}\ K\ \text{自对偶且}\ K\subsetneq L\ \text{（闭凸）}，\ \text{则}\ L\ \textbf{不是} \text{自对偶}✓✓$$
$$\qquad \text{（即：}\textbf{自对偶锥不能被严格扩大} \text{——}\ \text{扩大的代价是}\ \textbf{失去自对偶性}）✓✓$$

## §3 定理 A：Choi 宿主中的松紧结构（自足陈述）

$$\textbf{引用（外部）}：\text{Choi 1975}（\text{完全正映射的 Choi 矩阵刻画}）：\ \phi\ \text{完全正}\iff C_\phi\ \text{半正定（PSD）}✓$$
$$\qquad \Longrightarrow\ \text{经 Choi 同一化，}\ CP_n\ \textbf{对应 PSD 锥} \Longrightarrow \boxed{CP_n\ \textbf{自对偶}}✓✓$$
$$\qquad \qquad \text{（PSD 锥自对偶为标准事实：}\ \operatorname{tr}(AB)\ge0\ \forall B\succeq0\iff A\succeq0）✓$$
$$\textbf{引用（外部）}：\text{Choi 1975}\ \text{又证}：n=2\ \text{时}\ Pos_2=CP_2;\quad n\ge3\ \text{时}\ \boxed{Pos_n\supsetneq CP_n}✓✓$$
$$\textbf{定理 A}：n\ge3\ \text{时}\ Pos_n\ \textbf{不是自对偶锥}，\ \text{且}\ Pos_n\ \text{判据}\ \textbf{严格松于}\ CP_n\ \text{判据}✓✓$$
$$\qquad \text{证明}：CP_n\subseteq Pos_n\ \text{且}\ CP_n\ \text{自对偶};\ \text{代入推论 2′}\ \Longrightarrow Pos_n\ \text{非自对偶}✓$$
$$\qquad \qquad \text{判据松紧由}\ \S1\ \text{的单调性即得}（CP_n\subsetneq Pos_n \Longrightarrow \Theta_{CP}\subsetneq\Theta_{Pos}）\quad\blacksquare✓$$
$$\qquad ⚠️\ \textbf{注意方向}：\text{非自对偶的那个锥}（Pos_n）\ \textbf{恰是更松的那个}✓✓$$
$$\qquad \qquad \text{即：}\textbf{离开自对偶} \text{的方向是}\ \textbf{松}，\ \textbf{不是紧}✓✓$$

## §4 定理 B：自对偶判据的唯一性

$$\text{设}\ S\subseteq V\ \text{为"真元素"集合}\（\text{例：对应性质成立的全部}\ A(\theta)）;\ \ \text{记}\ K:=\overline{\operatorname{cone}}(S)✓$$
$$\textbf{定理 B}：\text{若}\ K:=\overline{\operatorname{cone}}(S)\ \text{自对偶}，\ \text{则任何}\ \textbf{自对偶} \text{闭凸锥}\ L\ \text{满足}\ S\subseteq L\ \text{必有}\ \boxed{L=K}✓✓$$
$$\qquad \text{证明}：S\subseteq L \Longrightarrow \overline{\operatorname{cone}}(S)\subseteq L \Longrightarrow K\subseteq L;\ \text{由引理 2}\ \Longrightarrow L=K\quad\blacksquare✓$$
$$\textbf{解读}：\text{一旦"真集合"}\ S\ \text{的锥包}\ \textbf{自对偶}，\ \text{则}\ \textbf{含}\ S\ \text{的自对偶判据锥}\ \textbf{唯一}✓✓$$
$$\qquad \Longrightarrow \text{在该框架内，}\textbf{不存在"另一个自对偶判据"能把判据加锐或改换}✓✓$$

## §5 二分（本笔记的主结论）

$$\boxed{\text{(I)}\ \textbf{自对偶} \Longrightarrow \textbf{唯一}（\text{定理 B}）;\quad \text{自对偶锥不能被严格扩大}（\text{推论 2′}）✓✓}$$
$$\boxed{\text{(II)}\ \textbf{严格加锐} \Longrightarrow \textbf{必非自对偶}}（\text{推论 2′ 的逆否}）✓✓$$
$$\qquad \text{而非自对偶的代价：}\text{判据锥}\ K\ \text{与证书锥}\ K^*\ \text{不再相同}⟹ \textbf{对偶缺口}✓✓$$
$$\qquad \qquad \text{（}\text{即：}\text{若}\ A\notin K，\ \text{分离定理给}\ \ell\in K^*\ \text{使}\ \langle\ell,A\rangle<0;\ \text{但}\ \ell\ \text{一般}\ \textbf{不在}\ K\ \text{中} \Longrightarrow \text{"判据语言"与"见证语言"分离}）✓$$
$$\Longrightarrow \textbf{主结论}：\text{在锥判据框架内，}\boxed{\text{"自对偶（证书对称）"} \ \textbf{与}\ \text{"严格加锐"} \ \textbf{不可兼得}}✓✓✓$$

## §6 RH 读数（**框架层**，附明确前提；非定理）

$$\text{设某性质}\ P（\text{例：}\operatorname{Re}\rho=\tfrac12）\ \text{被提议写成锥成员性}\ P(\rho)\iff A_\rho\in K✓$$
$$\textbf{前提 (P1)}：\text{判据须为}\ \textbf{锥成员性};\quad \textbf{(P2)}：\text{"真集合"的锥包}\ \textbf{自对偶};\quad \textbf{(P3)}：\text{判据须}\ \textbf{证书对称}（\text{同一锥兼作判据与见证}）✓$$
$$\text{则在 (P1)–(P3) 下：}\text{由 §5(I)}\ \text{判据锥}\ \textbf{唯一} \Longrightarrow \textbf{不能改换};\ \text{由 §5(II)}\ \text{任何}\ \textbf{严格加锐} \text{必破坏 (P3)}✓✓$$
$$\qquad \Longrightarrow \text{若在 Choi 宿主中该唯一锥为}\ CP_n（\text{经 Choi}＝PSD）\ \text{则判据}\ \textbf{就是单个二次型（}\text{PSD}\ \text{条件）}✓✓$$
$$\qquad \qquad ⚠️\ \text{而在算术侧，}\text{PSD 型（正性）判据与 RH 的等价性}\ \textbf{是另一个独立事实}（\text{Weil／Li 正性} \iff \text{RH}）\ \text{—— }\textbf{本笔记不证明该等价性}✓$$
$$\Longrightarrow \textbf{故本笔记对 RH 路线的意义是负向的}：\text{锥分离路线}\ \textbf{无法} \text{产出"新的、加锐的、证书对称的"判据}✓✓$$

## §7 未排除什么（诚实范围）

$$\text{(a)}\ \textbf{非锥型} \text{判据（不写成}\ A\in K\ \text{者）—— \textbf{完全不涉及}}✓$$
$$\text{(b)}\ \textbf{自对偶但不同构于 PSD} \text{的锥（}\text{定理 B 允许}\ K=\overline{\operatorname{cone}}(S)\ \text{是别的自对偶锥}）✓$$
$$\text{(c)}\ \text{判据不作"成员性"读法、或}\ S\ \text{的锥包}\ \textbf{非自对偶} \text{的情形}✓$$
$$\text{(d)}\ \text{无限维／非闭凸／非凸情形（本笔记的引理要求闭凸；分离定理需闭性）}✓$$
$$\Longrightarrow \textbf{本笔记只排除}：\text{在 (P1)–(P3) 下的"}\textbf{新且加锐且证书对称} \text{"的锥判据}✓$$

## §8 依赖清单（外部）

| 编号 | 内容 | 用途 |
|:--|:--|:--|
| **[C75]** | Choi, *Completely positive linear maps on complex matrices*, LAA **10** (1975) 285–290：Choi 矩阵刻画；`n\ge3` 时 `Pos_n\supsetneq CP_n` | §3 的**全部外部输入** `[经典·本档未逐字核原文]` |
| **[标准]** | PSD 锥自对偶；闭凸锥对偶 `K^{**}=K`；分离定理 | §2／§5 |
| **[背景]** | 自对偶齐次锥分类（Koecher–Vinberg）| **仅背景**，本笔记**不使用**（`§7(b)` 提示该方向未被排除）|

## §9 边界

- ⚠️ §3 的两条 Choi 事实为**引用**，标 `[经典·本档未逐字核原文]` ⟹ **投稿前须逐字核**（含 `n=2` 的 `Pos_2=CP_2` 归属）✓
- ⚠️ §6 的 (P1)–(P3) 是**建模前提**，不是定理；**不得**省略前提引用✓
- ⚠️ 本笔记**不证明** RH 的任何一侧；**不声称**非锥型判据不存在✓
- ⚠️ 本笔记**不声称**"自对偶 ⟹ PSD"（见 §7(b)：自对偶锥不止 PSD 一族）✓
- **性质**：负结果笔记；**可独立于 RH 阅读**✓

## §10 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 19:5x）`[纪律]`

```
技术词 对偶缺口          命中文件数=0  :: （docs/ 口径）
技术词 证书对称          命中文件数=0  :: （docs/ 口径）
技术词 严格加锐          命中文件数=0  :: （docs/ 口径）
```
**读数（按实测）**：三项在 `docs/` 口径下均＝**0 档 ⟹ 本笔记措辞在内部档案中未出现（新）**；
⚠️ 说明：`tech_word_check.sh` 只扫 `docs/`，本笔记位于 `papers/` ⟹ **本档自称"新措辞"仅就 `docs/` 口径成立** ✓
