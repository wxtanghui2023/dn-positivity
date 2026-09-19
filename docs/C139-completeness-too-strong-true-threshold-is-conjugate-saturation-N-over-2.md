已查地图（**先查后写**）：`C-138`（窗口完备性判据：本档须**更正**其"⟺ 完备"）、`C-133`（核维数实测 `K(128)=1`、`K(126)=4` —— 数据早已显示阈值在 128，我当时未解读为**刚性阈值**）、`C-132`（F3 反例：加均匀测度）、`C-137`（数据类型层）、`C-124` 刀②（阈值现象）、`W6`（support>1）。关键词回查：`共轭饱和`=0、`周期梳`=0、`可准入核`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 11:51「甲4」）**：**攻双条件中的一条**（完备窗口／相位）。本档攻第一条，并**检验我上一刀是否过强**。
**结论（先行）**：$$\textbf{(一)}\ ⚠️\ \text{`C-138` 的"刚性}\iff\textbf{完备}"\ \textbf{过强} \Longrightarrow \text{更正为}\ \boxed{\text{刚性}\iff\textbf{共轭饱和}（W\ge N/2）}✓✓$$
$$\textbf{(二)}\ \text{toy 阈值}\ \textbf{恰为}\ W\ge N/2=128\ （\text{不是}\ 255=N-1）✓✓$$
$$\textbf{(三)}\ \text{机制}＝\textbf{周期梳}：w=(+1,-1,+1,-1,\dots)\ \text{的 DFT}\ \textbf{只支撑在}\ j=128 \Longrightarrow \text{对}\ W\le127\ \textbf{不可见}✓✓$$
$$\qquad \text{且可准入（}\pm1\ \text{取值、零和）} \Longrightarrow \text{对}\ W\le127\ \textbf{无刚性}✓✓$$
$$\textbf{(四)}\ \text{ζ 侧}：\text{共轭饱和在}\ \textbf{直线} \text{上}＝\text{覆盖整个半线}＝\text{全部频率}＝\text{support}>1＝\text{`W6`} \Longrightarrow \textbf{仍被挡}，\text{但要求的结构}\ \textbf{精确化}✓$$
$$\textbf{(五)}\ \text{方法论净产出}：\text{不可见性判据必须按}\ \textbf{【可准入核】}（\text{约束下的整数核}），\ \textbf{不能} \text{按【实核维数】}✓✓$$

FREEZE-ACK: 本档即冻结期内的判据更正与构造验证（依 `§8.1`；不产候选结论）

D0: 本档对象 = **C-138 判据更正（完备 → 共轭饱和）＋ 周期梳构造 ＋ 可准入核 vs 实核维数的方法论** —— 关系 = 更正与构造，非新机制
D1: 0

# C-139 · **甲4：完备性太强 —— 真正的阈值是「共轭饱和」（`W ≥ N/2`）**

> **唐先生 2026-09-19 11:51**：**「甲4」**（攻双条件之一）✓
> ⚠️ 本档先做一件事：**检验我上一刀（`C-138`）是否过强** —— 结果：**是**。

---

## §1 ⚠️ 更正（`C-138` §1）

$$\text{`C-138` 原判据}：\textbf{秩刚性}\iff\textbf{窗口完备}（K(\Omega)＝\text{常数},\ \Omega=\hat G\setminus\{0\},\ \text{即}\ W=N-1）✗\ (\textbf{过强})✓$$
$$\text{错因}：\text{该论证用}\ \dim K(\Omega)=\infty\ \text{作理由}，\ \textbf{忽略了结构约束}（\text{整数性／零和}）✓✓$$
$$\textbf{正确判据}：\ \boxed{\text{秩刚性}\iff\textbf{共轭饱和}：\ \Omega\ \text{覆盖每一对}\ \pm j\ \text{中的至少一个},\ \text{即}\ W\ge N/2}✓✓$$

## §2 机制：**周期梳**（直接构造 ＋ 数值已验证）

$$w:=(+1,-1,+1,-1,\dots)\ (\text{周期 2}) \Longrightarrow \hat w(j)\ne0\ \text{仅当}\ j\equiv0\ (\mathrm{mod}\ N/2)✓✓$$
$$\qquad \text{数值实测}：\text{DFT 非零频率}＝\{128\}\ \text{（仅此一个）}✓✓$$
$$\text{且}\ \sum_i w_i=0\ (\text{零和}✓),\ w_i\in\{-1,+1\}\ (\textbf{可准入}✓)✓✓$$
$$\Longrightarrow\ \text{对}\ W\le127：w\ \textbf{不可见} \Longrightarrow \textbf{无刚性}✓✓$$
$$\qquad ⚠️\ \text{对}\ W\ge128：w\ \text{在}\ j=128\ \text{处可见} \Longrightarrow \text{不能作扰动}✓$$

## §3 阈值表（**toy**）

$$\begin{array}{c|c|c|c}
W & \dim K(W) & \text{可准入不可见扰动} & \text{刚性}\\\hline
\le127 & N-2W\ \ge2 & \textbf{有}（\text{周期 2 梳}） & ✗\\
128 & 1 & \text{无}（\text{常数不可零和}） & ✓\\
130\text{–}255 & 1 & \text{无} & ✓\\
\end{array}✓✓$$
$$\qquad ⚠️\ \text{`C-133` 实测早已显示}\ K(128)=1、K(126)=4 \Longrightarrow \text{阈值在 128 的}\ \textbf{数据当时就在手里}，\text{我未解读为刚性阈值}✓✓$$

## §4 ζ 侧含义（**精确化后仍通 `W6`**）

$$\text{"共轭饱和"在}\ \textbf{直线} \text{上的对应物}：\text{因实值测度有}\ \hat w(-\xi)=\overline{\hat w(\xi)},\ \text{饱和}＝\text{覆盖}\ \xi\ge0\ \textbf{全部}✓$$
$$\qquad ⟹\ \text{对}\ \zeta：\text{要求}\ \textbf{全部频率}＝\text{support}>1＝\text{`W6`} \Longrightarrow \textbf{仍被挡}✓✓$$
$$\qquad ⚠️\ \text{但收获是}\ \textbf{结构性的}：\text{有限群上"一半"就够（因}\ \pm\ \text{配对是}\ \textbf{有限} \text{对称）；直线上"一半"＝}\textbf{无限} \Longrightarrow \text{缺口不可用同一招补齐}✓✓$$

## §5 ⭐ 方法论净产出（可复用）

$$\textbf{不可见性判据必须按【可准入核】算}：$$
$$\qquad \text{可准入核}：=\Big\{w\in\underbrace{\mathbb Z^N}_{\text{整数}}\cap\underbrace{\text{零和}}_{\text{质量}}\cap\underbrace{\text{marks 相容}}_{\text{正性/取值}}:\ \hat w|_\Omega=0\Big\}✓✓$$
$$\qquad \textbf{不能} \text{按【实核维数】}\dim_{\mathbb R}K(\Omega)\ \text{判定 —— `C-138` 的错正出在这里}✓✓$$
$$\qquad （\dim K\ \text{大}\ \not\Longrightarrow\ \text{有可准入向量};\ \dim K=1\ \text{时才可能真刚性}）✓$$

## §6 边界与回查

- ⚠️ 本档为**自我更正**（第 9 次同类）：改的是 `C-138` **判据的强度**，不改 `C-133` 的核维数实测，也不改 `C-132` 的反例 ✓
- ⚠️ §2 构造为**解析构造 ＋ 数值已验证**（DFT 支撑实测）✓
- ⚠️ §4 的"直线上饱和＝全部频率"为**结构判断**（未证"部分饱和 ⟹ 必无刚性"的完整陈述）✓
- ⚠️ `128` 在两个地方出现（此处＝`N/2`；`C-125` `A2` 的 `R\ge P\ge128` 来自 `\sum m=256,m\le2`）—— **机制不同，勿混** ✓
- **未用** RH；**未改**任何原档（仅追加更正指针）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 11:5x）`[纪律]`（先跑后写）

```
技术词 共轭饱和   命中文件数=0 ::  ⟹ 本档新增
技术词 周期梳    命中文件数=0 ::  ⟹ 本档新增
技术词 可准入核   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
