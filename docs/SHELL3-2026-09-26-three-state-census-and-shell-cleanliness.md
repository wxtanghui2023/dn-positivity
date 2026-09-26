已查地图：已跑 scripts/prework_map_check.sh shell 三态 private 第二覆盖 L□ ⟹ 执行自 SHELLBUDGET-2026-09-26 档；本档为**shell 三态普查＋shell 洁净性＋L□ 候选不等式**（唐先生 2026-09-26 16:00 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 方阵 shell 的 private/码字/第二覆盖 三态普查、逐坐标容量、L□ 与候选不等式
D1: 1（新增：**(9,64) shell 全 private（L□=0）** ✓✓；**每方阵 ≥4 private shell 点（已证）** ✓✓；**候选 L□ ≤ I_nw + S** ⚠️）

# SHELL3-2026-09-26

## §1 ✅ **三态普查结果**

```
$$\begin{array}{c|c|c|c|c|c|c}
\text{实例} & S_q & N_1 & \text{shell 总数} & P(\text{private}) & C(\text{码字}) & M(\text{第二覆盖})\\
\hline
(9,64)\ \text{我方} & 16 & 448 & 16\cdot28=448 & \mathbf{100\%} & 0 & \mathbf{0}\\
(5,8)>K & 1 & 24 & 12 & 9 & 0 & 3\\
(4,6)>K & 1 & ? & 8 & 3 & 1 & 4\\
\end{array}$$
$$\textbf{关键}: (9,64)\ \text{每个方阵的 28 个 shell 点}\ \mathbf{全为 private}\ ✓✓ \Longrightarrow L_\square=0\ \✓✓\ (\text{唐先生猜的"完全 private-rich 饱和构造"}\ ✓✓)$$
$$\qquad\text{且 shell 总数 }16\cdot28=448=\mathbf{N_1}\ ✓✓ \Longrightarrow \textbf{16 个方阵的 shell 恰好分割全部私有点}\ ✓✓$$
$$

## §2 ✅ **每方阵 ≥4 private shell 点（已证 ✓✓）**

```
$$\text{极小码每个码字有私有点}\ ✓;\ \text{方阵顶点 }v\ \text{的私有点必在其自由邻居中}\ ✓\ (\text{引理 (a)}\ ✓✓);\ \text{而 }v\ \text{的自由邻居}\subseteq\text{shell}(v)\ ✓$$
$$\Longrightarrow\ \text{每方阵 4 顶点各需 }\ge1\ \text{shell 私有点}\ ✓;\ \text{4 个 shell}(v)\ \text{互不相交}\ ✓\ (\text{同方阵内}\ ✓)\ \Longrightarrow\ \boxed{\text{每方阵}\ \ge4\ \text{private shell 点}}\ ✓✓$$
$$\Longrightarrow\ L_\square(Q)\ \le\ 4(n-2)-4\ =\ 4(n-3)\ ✓\ (\text{n}=9:\ \le24\ ✓)$$
$$

## §3 ⚠️ 唐先生候选式的定性

```
$$\text{候选}: 4S_q\le N_1+L_\square\ ✓\ ——\ \textbf{但这是平凡的}\ ✗\ (\text{因 }4S_q\le N_1\ \text{已成立}\ ✓)$$
$$\text{真正有信息的方向（唐先生自陈）}: N_1\ \text{收缩}\ \Longrightarrow\ L_\square\ \text{增长}\ ✓\ ——\ \text{但需要 }M=62\ \text{的真实码才能测}\ ✗$$
$$\text{可测的替代}: \text{候选}\ \boxed{L_\square\ \le\ I_{\rm nw}+S}\ ⚠️\ (\text{3 实例通过}\ ✓,\ \text{样本极少}\ ✗)$$
$$\qquad (9,64):\ 0\le0+0\ ✓;\quad (5,8):\ 3\le0+12\ ✓;\quad (4,6):\ 5\le2+4=6\ ✓$$
$$

## §4 状态与下一刀

```
$$\textbf{未闭合}\ ✗;\ \text{关键开放问题}: M=62\ (\text{比 64 少 2 词})\ \text{时 shell 能否保持洁净}\ (L_\square=0)\ ⚠️$$
$$\text{若不能}: \text{某些 shell 被第二覆盖}\ \Longrightarrow\ \text{产生距离-2 incidence}\ \Longrightarrow\ I_{\rm nw}\ \text{或}\ S\ \text{增长}\ ✓\ ——\ \text{这就是唐先生要的 P1 障碍形态}\ ✓$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad (9,62)\ \text{全码}: \text{仍未获得}\ ✗\ (\text{锚定 SAT 运行中}\ ⏳)$$
$$

## §5 边界（诚实标注）

- §1 为**数值普查** ✓（n=4,5 全枚举 ✓、n=9 我方构造 ✓）；§2 为**我方证明** ✓
- §3 明确记录候选式的**平凡性** ✗ 与候选 L□ ≤ I_nw+S 的**样本不足** ⚠️（未夸大 ✓）
- **(9,62) 全码未获得** ✗；**未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：shell 三态普查、shell 洁净性、第二覆盖态
- **档案已有（引用，不列为提出）**：方阵、私有点、shell、excess
