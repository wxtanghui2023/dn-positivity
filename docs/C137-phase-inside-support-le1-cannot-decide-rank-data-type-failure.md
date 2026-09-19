已查地图（**先查后写**）：`C-136`（FRI 假设审计：分离被正性替代；缺口＝相位）、`C-133`（核维数判据；toy 侧相位替代品＝整数性＋总量）、`C-132`（F3 反例）、`C-124`（刀②阈值现象：需 R ≤ 253 才能让引理生效）、`C-125`／`C-126`（饱和／信息位于收敛边界）、`d7-boundary-audit`（**逐字**：`3. 但——恒等通道只产生等式（自适应）——不产生不等式`；`4. 等式编码"代价"（D≥0——来自正性）——不能编码"排除"（D≤0——需要不等式）`；`5. 任何"跨越两侧的量"要么是恒等式（自适应——无约束）——要么是独立的两侧量（无连接——无法比较）`）、`C-82`（值 vs 界）、`V188 §2`（线性层饱和）、`W6`（support>1 原子墙）。关键词回查：`数据类型层`=0、`相位替代品`=0、`等式不给排除`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 11:45「甲2，乙」）**：**攻新靶子**：support ≤ 1 内的相位，是否足以定秩？
**结论（先行）**：$$\textbf{(一)}\ \text{甲2 判定}＝\boxed{\textbf{NO}}，\ \text{且失败在}\ \textbf{【数据类型层】}，\ \textbf{不在窗口层}✓✓$$
$$\textbf{(二)}\ \text{ζ 侧相位}\ \textbf{只} \text{出现在}\ \textbf{显式公式};\ \text{而显式公式是}\ \textbf{恒等式} \Longrightarrow \text{逐字}：\text{"恒等通道只产生等式（自适应）——不产生不等式"} \Longrightarrow \text{相位}\ \textbf{无法产生排除}✓✓$$
$$\textbf{(三)}\ ⟹\ \text{精确缺口重写}：\textbf{不是"相位是否存在"}，\textbf{而是"能否把相位信息用于产生不等式"} ＝ \text{`C-82`}\ \text{值vs界}＋\text{F5 同址}✓✓$$
$$\textbf{(四)}\ \text{toy 侧}：\text{`B2-1`}\ \text{的证书}\ \textbf{也} \text{是模长型}（\text{钉}\ |\hat\mu|^2）;\ \text{其相位替代品}＝\textbf{整数性＋固定总量}✓✓$$
$$\textbf{(五)}\ ⟹\ \textbf{统一读数}：\text{两设定的数据}\ \textbf{都是模长型};\ \text{toy 有替代品}（\text{整数性}），\ \zeta\ \textbf{目前没有}（\text{需 support}>1／\text{`W6`}）✓✓$$

FREEZE-ACK: 本档即冻结期内的新靶子首攻与主图同步（依 `§8.1`；不产候选结论）

D0: 本档对象 = **"support ≤ 1 内相位定秩"的否定判定（数据类型层失败）＋ 缺口重写（相位≠不等式）＋ 统一读数** —— 关系 = 判定与重写，非新机制
D1: 0

# C-137 · **甲2：support ≤ 1 内的相位能否定秩？—— 不能（失败在数据类型层）**

> **唐先生 2026-09-19 11:45**：**「甲2，乙」** ✓

---

## §1 三种数据类型的严格区分（承重）

$$\begin{array}{c|c|c|c}
\text{类型} & \text{内容} & \text{含相位？} & \text{我方可得性}\\\hline
\textbf{复样本} & \hat\mu(j)\in\mathbb C & ✓ & \zeta：\textbf{仅显式公式}（恒等式）;\ \text{toy}：✗\\
\textbf{模长/幅频} & |\hat\mu(j)|^2 & ✗ & ✓✓\ (\text{toy 证书};\ \zeta\ \text{的 support}\le1\ \text{窗口})\\
\textbf{自相关} & \text{差集测度}\ \nu\ \text{的 Fourier} & ✗ & ✓\\
\end{array}✓✓$$

## §2 toy 侧：相位**够**，但有自指条件

$$\text{经典}\ \textbf{Prony／湮灭滤波器}：\text{复样本}\ \hat\mu(j)\ (j=0..W)\ \Longrightarrow\ \text{湮灭滤波器系数的}\ \textbf{线性方程组}✓$$
$$\qquad \Longrightarrow\ \text{解出}\ R\ \text{个根}\ \Longrightarrow\ \text{位置与质量}\ \textbf{全部确定}✓✓$$
$$\qquad ⚠️\ \text{必需样本数}\ \ge2R\ \Longrightarrow\ \textbf{自指要求}\ W\ge2R\ (\text{正是}\ \text{`C-124`}\ \text{刀②的阈值现象})✓✓$$
$$\qquad \text{且（}\text{`C-136`}\ \text{§1 逐字）}\textbf{正性可免分离} \Longrightarrow\ \text{toy 侧"相位＋正性}\Longrightarrow\text{免分离恢复}"✓✓$$
$$\qquad ⚠️\ \textbf{但 toy 的实际数据是模长}（\text{证书钉}\ |\hat\mu|^2）\ \Longrightarrow\ \text{相位不可得}\ \Longrightarrow\ \text{需}\ \textbf{整数性} \text{替代}✓✓$$

## §3 ζ 侧：support ≤ 1 给的是**模长**，不是相位

$$\text{Montgomery／BGSTB24 的无条件内容}＝\text{素数侧和的}\ \textbf{二阶矩／配对相关}（\text{自相关型}）\ \Longrightarrow\ \textbf{模长型}✓✓$$
$$\text{相位信息}\ \textbf{只} \text{出现在}\ \textbf{显式公式}（\text{复恒等式}）;\ \text{但——（}\text{`d7`}\ \text{逐字）}✓✓$$
$$\qquad \textbf{"恒等通道只产生等式（自适应）——不产生不等式"}✓✓$$
$$\qquad \textbf{"等式编码代价（}D\ge0\text{——来自正性）——不能编码排除（}D\le0\text{——需要不等式）"}✓✓$$
$$\qquad \textbf{"任何跨越两侧的量要么是恒等式（自适应——无约束）——要么是独立的两侧量（无连接——无法比较）"}✓✓$$
$$\Longrightarrow\ \boxed{\text{加不加 support}\le1\ \text{这个窗口，都}\ \textbf{不产生相位型数据};\ \text{窗口是}\ \textbf{错的杠杆}}✓✓$$

## §4 判定 ＋ 统一读数 ＋ 缺口重写

$$\boxed{\text{甲2 判定}：\textbf{NO};\ \text{失败在}\ \textbf{数据类型层}（\text{模长}\neq\text{相位}），\ \textbf{不在窗口层}}✓✓$$
$$\textbf{统一读数}：\text{两设定数据}\ \textbf{都是模长型};\ \text{替代品}：\text{toy}＝\textbf{整数性＋固定总量}（\text{`C-133`}）;\ \zeta＝\textbf{暂无}✓✓$$
$$\textbf{缺口重写}：\ \boxed{\text{不是"相位是否存在"，而是"能否把相位信息用于产生}\ \textbf{不等式}"}✓✓$$
$$\qquad ⟹\ \text{与}\ \text{`C-82`}\ \text{（值 vs 界）}、\ \text{F5 缺口}、\ \text{`V188` §2}\ \text{（线性层饱和）}\ \textbf{同址}✓✓$$
$$\qquad ⟹\ \text{这也是}\ \text{`C-125`／`C-126`}\ \text{"信息位于收敛边界"的}\ \textbf{数据类型版} \text{表述}✓$$

## §5 边界与回查

- ⚠️ §2 的 Prony 复原为**经典事实引用**（未逐字核原文）✓
- ⚠️ §3 的"support ≤ 1 给的是二阶矩型"为**结构判断**（依 Montgomery／BGSTB24 的内容类型）✓
- ⚠️ **不声称** 相位信息在算术侧绝对不可得（仅：在 support ≤ 1 窗口内不可得，且在显式公式处受"恒等式"限制）✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 11:4x）`[纪律]`（先跑后写）

```
技术词 数据类型层   命中文件数=0 ::  ⟹ 本档新增
技术词 相位替代品   命中文件数=0 ::  ⟹ 本档新增
技术词 等式不给排除  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
