已查地图（**先查后写**）：`C-132`（F3 显式反例：窗口隐形测度；引擎＝KILL-2）、`C-131`（F3＝支撑大小刚性）、`C-125`（pairwise geometry）、`C-122`／`C-123`（mixture essentiality）、`CLOSED-ROUTES-MAP:1092`（KILL-2 ＝ 素数直积因子化）、`NEG-REGISTER-1/3`（T-I～T-VI 分级标准：**T-I ＝ 干净小结果**，与 `V227-A`／`V253` 并列）。关键词回查：`核维数`=0、`隐形能力`=0、`逐点整数性`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 11:31）**：①采纳其收紧（缺的是**逐点整数性**，不只总量）；②按要求**先验检查**"隐形能力"与"约束空间"是否互斥，再决定是否开 (丙)；③反例登记为 **T-I**。
**结论（先行）**：$$\textbf{(一)}\ \text{收紧}\ \textbf{采纳}：\text{封死反例的是}\ \textbf{逐点整数性}（\text{单独即够}）✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{预检答案＝互斥}：\text{满窗口}\ W=255\ \text{的隐形空间}\ \textbf{核维数}＝1（\text{恰为常数}）✓✓$$
$$\qquad \text{而唯一隐形方向（均匀平移）}\ \textbf{必违反}\ m_i\in\{1,2\}\ \text{与}\ \sum m=256\ \text{两条}✓✓$$
$$\textbf{(三)}\ \text{新判据}：\textbf{隐形能力}\iff\text{核维数}>1\iff W<N/2;\ W\ge128\ \Longrightarrow\ \text{核坍缩为常数}✓✓$$
$$\textbf{(四)}\ \textbf{(丙) 判定＝不可行}（\text{预检即死，未投入建设性工作}）✓✓$$
$$\textbf{(五)}\ \text{反例按唐先生分级登记为}\ \boxed{\textbf{T-I}}（\text{与}\ \text{`V227-A`}／\text{`V253`}\ \text{并列}）✓✓$$

FREEZE-ACK: 本档即冻结期内的预检、收紧与分级登记（依 `§8.1`；不产候选结论）

D0: 本档对象 = **隐形能力/约束空间互斥性的预检（核维数判据）＋ 收紧采纳 ＋ T-I 分级登记** —— 关系 = 判定与登记，非新机制
D1: 0

# C-133 · **预检：隐形能力 ⟺ 核维数 > 1（满窗口与约束空间互斥）＋ 收紧采纳 ＋ T-I 登记**

> **唐先生 2026-09-19 11:31**：①收紧"为什么 B2-1 不塌"；②**先验检查**"隐形能力"与"约束空间"是否天然互斥；③反例登记为 **T-I** ✓

---

## §1 收紧（逐条采纳：**逐点整数性单独即封死**）

$$\text{均匀平移}：m_i\ \to\ m_i+\frac tN;\qquad \text{要落在}\ \{1,2\}\ \text{必须}\ \frac tN\in\{0,1\}✓$$
$$\qquad t=0\ \text{平凡};\quad t=N\ \Longrightarrow\ \text{marks}\ \{1,2\}\to\{2,3\}\ ✗✓$$
$$\text{数值}：t=1\Longrightarrow\sum m=385\ (\text{且}\ \text{marks}\notin\{1,2\})\ ✗;\quad t=256\Longrightarrow\sum m=640\ ✗✓$$
$$\Longrightarrow\ \boxed{\text{封死反例的是}\ \textbf{逐点整数性}（\text{单独即够}）；"\text{总量固定}"\ \text{只是第二条}}✓✓$$

## §2 ⭐ 预检（唐先生要求的先验检查）：**核维数实测**

$$K(W):=\dim_{\mathbb R}\Big\{w\in\mathbb R^N:\ \hat w(j)=0,\ 1\le j\le W\Big\}✓$$
$$\begin{array}{c|cccccc}
W & 100 & 120 & 126 & 128 & 200 & \mathbf{255}\ (\text{`B2-1` 实际})\\\hline
K(W) & 56 & 16 & 4 & 1 & 1 & \mathbf{1}\\
\end{array}$$
$$\text{判据}：K(W)=N-2W\ (W<N/2);\qquad W\ge N/2=128\ \Longrightarrow\ K(W)=1\ (\textbf{仅常数})✓✓$$
$$\text{原因}：W\ge N/2\ \text{时}\ j\ \text{与}\ -j\equiv N-j\ \text{的配对已把全部非零频率纳入约束}✓✓$$
$$\Longrightarrow\ \boxed{\text{满窗口下隐形空间}＝\{\text{常数}\};\ \text{而唯一隐形方向（均匀平移）}\ \textbf{必违反两条约束}}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{答案：互斥 —— 你的猜测成立}}✓✓$$

## §3 **(丙) 判定＝不可行**（预检省下投入）

$$\text{目标}：\text{用隐形技巧构造}\ p<p_0\ \text{的构型}✓$$
$$\text{(i)}\ \text{满窗口}：\text{隐形}＝\text{常数}\ \Longrightarrow\ \text{无法在保数据下移动配置}\ ✗✓$$
$$\text{(ii)}\ \text{短窗口}：\text{核虽非平凡}，\text{但}\ \text{①约束集更弱（LP 放松，非反例）};\ \text{②构造物仍须满足}\ \textbf{全部}\ 255\ \text{行}（\tau=3\times10^{-40}）$$
$$\qquad \text{而短窗口只对被保留的行隐形，对被省略的行}\ \textbf{不隐形}\ \Longrightarrow\ \text{无法满足全部行}\ ✗✓$$
$$\Longrightarrow\ \boxed{\text{(丙) 两条路都不通（预检即死）}}✓✓$$

## §4 **T-I 登记**（唐先生判定；按 `NEG-REGISTER` 分级标准）

$$\text{内容}：\text{F3（不带额外假设）}\ \textbf{为假};\ \text{缺的假设}＝\textbf{整数性＋固定总量};\ \text{形式}＝\textbf{minimal counterexample}✓✓$$
$$\text{分级}：\boxed{\textbf{T-I 干净小结果}}（\text{显式反例＋精确定位缺失假设，无需额外假设即可验证}）✓✓$$
$$\qquad \text{与}\ \text{`V227-A`}（sup Re z 非模长不变量）、\text{`V253`}（Erdős 和界 A/B）\ \text{并列}✓✓$$

## §5 边界与回查

- ⚠️ §2 核维数为**实测**（`np.linalg.matrix_rank`，`N=256`）✓
- ⚠️ **不声称** (丙) 在**所有**可能变体下不可能；仅判：**在 B2-1 相关的窗口范围内**，隐形技巧与约束空间互斥 ✓
- ⚠️ **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 11:3x）`[纪律]`（先跑后写）

```
技术词 核维数      命中文件数=0 ::  ⟹ 本档新增
技术词 隐形能力     命中文件数=0 ::  ⟹ 本档新增
技术词 逐点整数性   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
