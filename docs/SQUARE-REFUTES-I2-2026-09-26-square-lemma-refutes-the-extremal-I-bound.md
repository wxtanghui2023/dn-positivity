已查地图：已跑 scripts/prework_map_check.sh 方阵 I≥4 Wille 62 码 ⟹ 执行自 GCOMP-2026-09-26 档；本档为**方阵 ⟹ I≥4 引理＋对 `M=K⟹I≤2` 的否证**（唐先生 2026-09-26 15:42 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 方阵蕴含 I≥4 的引理、Wille 62 码含方阵的文献证据、对 `I≤2` 靶心的否证
D1: 1（新增：**方阵 ⟹ I ≥ 4（已证 ✓✓）**；**`M=K ⟹ I≤2` 对 n=9 被否** ✗✓；**Kéri 论文给出 Wille 码 4 个真实码字** ✓✓）

# I2-REFUTED-2026-09-26

## §1 ✅ **新引理：方阵 ⟹ I ≥ 4**（我方证明 ✓✓，一行）

```
$$\text{设 }F=\{u,\ u+e_i,\ u+e_j,\ u+e_i+e_j\}\subseteq C\ (\text{初等方阵/2-面}\ ✓)\ ——\ \text{四点互异}\ ✓$$
$$\text{每个顶点 }v\in F\ \text{有\textbf{两个}方阵内码字邻居}\ (\text{两相邻面边}\ ✓)\ \Longrightarrow\ d_C(v)\ge2\ \Longrightarrow\ \binom{d_C(v)}2\ge1\ ✓$$
$$\Longrightarrow\ \boxed{I=\sum_{c\in C}\binom{d_C(c)}2\ \ge\ 4}\ ✓✓\ (\text{与极小性/极值性\textbf{无关}，纯几何}\ ✓)$$
$$

## §2 ⚠️ **文献证据：Wille 的 62 码含方阵**（Kéri 论文，[L] 二手但明确 ✓）

```
$$\text{Kéri (191 页匈牙利文博士论文, MTA REAL-d 免费}\ ✓)\ \text{原文}:$$
$$\quad\text{"Külön említést érdemel a Wille-féle konstrukciónak az a jellegzetessége, hogy a kódszavak között}$$
$$\quad\text{találhatók olyan 4-es csoportok, amelyek a bináris Hamming térben elemi négyzetet képeznek"}$$
$$\quad\text{（意为: Wille 构造的特征之一是码字中存在 4 元组构成 Hamming 空间中的初等方阵）}\ ✓$$
$$\quad\text{并\textbf{给出显式 4 词}}:\quad c_2=(000001010),\ c_7=(000101010),\ c_9=(001001010),\ c_{13}=(001101010)\ ✓✓$$
$$\quad\Longrightarrow\ \text{方阵跨坐标 }\{3,4\}\ ✓\ \text{（平移后即 }\{0,\ e_3,\ e_4,\ e_3{+}e_4\}\subseteq C\ ✓✓)$$
$$\text{另}: \text{论文记载 }K(9,1)=62\ \text{两已知构造 = Fagioli 1984 与 Wille 1996},\ \text{均\textbf{非平衡}、2-满射}\ ✓;\ \text{分类\textbf{未解决}（难题）}\ ✓$$
$$

## §3 ⛔ **因此 `M=K ⟹ I ≤ 2` 对 n=9 被否** ✗✓

```
$$\text{若 Wille 的 62 码含方阵}\ ✓\ \Longrightarrow\ I\ge4\ ✗\ \Longrightarrow\ \boxed{\text{靶心 }M=K\Rightarrow I\le2\ \textbf{在 }n=9\ \text{上为假}}\ ✗✓$$
$$\text{后果}: \text{“}h\le I/3\ \text{＋}\ I\le2\ \Rightarrow\ h=0\text{”\ 的\textbf{闭合路线在 }n=9\ \text{不可用}\ ✗✓}$$
$$\qquad\text{且 }I\ge4\ \Longrightarrow\ h\le\lfloor I/3\rfloor\ge1\ \text{—— 无法排 }h>0\ ✗$$
$$\text{同时}: \text{此前 }n=4,5,6\ \text{的 }I\in\{0,1,2\}\ \text{是\textbf{小 n 现象}}\ ✗\ (\text{不得外推}\ ✗✓)$$
$$

## §4 保留与修正

```
$$\text{保留（已证\ }✓✓): \text{方阵}\Rightarrow I\ge4\ ✓✓;\ 4S\le Q_2\ ✓✓;\ h\le I/3\ ✓;\ 2A_2=I+S\ ✓✓;\ I+S\le E+Q_2\ ✓$$
$$\text{修正}: \text{靶心由 “}M=K\Rightarrow I\le2\text{" 改为\textbf{直接控制 }h\ \text{或 }d_C\ \text{的极值上界}\ ✗✓\ (\text{不再绕 }I\ \text{常数界}\ ✗)$$
$$\text{实验价值变化}: \text{拿到 62 码仍有用（测 }I,S,Q_2\ \text{真值\ }✓)，但\textbf{不再是 }I\le2\ \text{的判据}\ ✗$$
$$

## §5 状态

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \text{靶心（原 }I\le2\text{）}\ \textbf{已否}\ ✗;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$\text{下一步建议}: \text{① 用方阵资产重设靶心（方阵数 }S\ \text{给出 }I\ \text{下界 }\Rightarrow\ \text{反推 }h\ \text{的上界结构）}\ ⚠️;\ \text{② 转文献取 Wille/Fagioli 全码}\ ✓$$
$$

## §6 边界（诚实标注）

- §1 为**我方证明** ✓（纯几何，与极值性无关 ✓）
- §2 为**二手文献** [L]（Kéri 论文原文 ✓，免费可得 ✓）—— **未读 Wille 1996 一手原文** ⚠️
- §3 的否证**依赖 §2 的文献陈述** ✓（若 Wille 码确含方阵则成立 ✓）
- **(9,62) 全码仍未获得** ✗；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：方阵下界引理、靶心否证、小 n 现象、极值上界直控
- **档案已有（引用，不列为提出）**：方阵、A≤2、minimality
