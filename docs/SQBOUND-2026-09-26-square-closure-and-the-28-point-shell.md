已查地图：已跑 scripts/prework_map_check.sh 方阵 闭合 壳层 I_nw ⟹ 执行自 SQUARE-REFUTES-I2-2026-09-26 档；本档为**方阵闭合引理＋壳层耦合界面＋I_nw 分解**（唐先生 2026-09-26 15:56 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 方阵闭合引理、方阵与外部耦合的唯一界面（壳层）、I = I□ + I_nw 分解的数据
D1: 1（新增：**方阵闭合引理（已证＋核验）** ✓✓；**壳层界面 4(n−2) 点** ✓；**I_nw 分解数据** ✓）

# SQBOUND-2026-09-26

## §0 记号

```
$$F=\\{u,\ u+e_i,\ u+e_j,\ u+e_i+e_j\\}\subseteq C\ ✓\ (\text{初等方阵/2-面}\ ✓);\quad V_\square:=\\text{落在至少一个方阵内的码字集}\ ✓$$
$$I_\square:=|V_\square|\ ✓;\quad I_{\rm nw}:=I-I_\square\ \ge0\ ✓\ \Longrightarrow\ \boxed{I=I_\square+I_{\rm nw}}\ ✓✓$$
$$

## §1 ⭐ **方阵闭合引理**（我方证明 ✓✓）

```
$$\textbf{断言}: \text{对 }x\notin F:\quad |N(x)\cap F|\ \le\ 1\ ✓\ (\text{外部点至多邻接方阵的一个顶点}\ ✓)$$
$$\textbf{证明}: \text{设 }v,w\in F\ \text{同为 }x\ \text{的邻居}\ ✓\ \Longrightarrow\ x\in N(v)\cap N(w)\ ✓$$
$$\qquad d(v,w)=1\ \Longrightarrow\ N(v)\cap N(w)=\{v,w\}\subseteq F\ ✓;\qquad d(v,w)=2\ \Longrightarrow\ N(v)\cap N(w)=\{\text{另两顶点}\}\subseteq F\ ✓$$
$$\qquad\Longrightarrow\ x\in F\ ✗\ \text{与 }x\notin F\ \text{矛盾}\ ✓✓$$
$$\textbf{数值核验}: (9,64)\ \text{的 16 个方阵全部闭合}\ ✓✓\ (\textbf{0 违反}\ ✓)$$
$$\textbf{推论}: \text{方阵内码字对 }\\{v,w\\}\ \text{的公共邻居全在 }F\ \text{内}\ ⟹\ \text{\textbf{无外部中心承载方阵对}}\ ✓✓$$
$$

## §2 ⭐ **唯一耦合界面 = 壳层（4(n−2) 点）**

```
$$\text{方阵顶点 }v\in F\ \text{的\textbf{外部}邻居}:\ (\text{以 }F=\{0,e_i,e_j,e_i{+}e_j\}\ \text{为例}\ ✓)$$
$$\qquad v=0:\ e_k\ (k\notin\{i,j\})\ ✓;\ v=e_i:\ e_i+e_k\ ✓;\ v=e_j:\ e_j+e_k\ ✓;\ v=e_i{+}e_j:\ e_i{+}e_j{+}e_k\ ✓$$
$$\Longrightarrow\ \boxed{|\text{壳层}|=4(n-2)}\ ✓\ (n=9:\ \mathbf{28}\ ✓)$$
$$\text{壳层码字 }s\in C\ \Longrightarrow\ s\ \text{邻接某个 }v\in F\ \Longrightarrow\ d_C(v)\ \text{增大}\ \Longrightarrow\ \textbf{I 增大}\ ✓;\quad S\ \text{仍}\ 0\ ✓;\quad Q_2\ \text{随 }b(v)\ \text{增大}\ ✓$$
$$\Longrightarrow\ \textbf{耦合通道}: \text{方阵通过\textbf{壳层}影响 }I\ \text{与 }Q_2,\ \textbf{不}影响 }S\ ✓✓\ (\text{唐先生 item 4 的精确定位}\ ✓)$$
$$

## §3 数据（M=K 与极值码）

```
$$\begin{array}{c|c|c|c|c|c}
(n,M)&I&|V_\square|&I_{\rm nw}&S&\text{类型}\\
\hline
(9,64)\ \text{我方} & 64 & 64 & 0 & 0 & \textbf{纯方阵型}（16 个方阵，全部闭合、壳层空 ✓）\\
(5,7)=K & 1 & 0 & 1 & 7 & \textbf{纯非方阵型}（无方阵 ✓）\\
(4,6)>K & 6 & 4 & 2 & 4 & \text{两机制共存}\ ✓\\
(4,4)=K & 0 & 0 & 0 & 0 & \text{平凡}\ ✓\\
\end{array}$$
$$(9,64)\ \text{顶点 }b\equiv3\ ✓\ \Longrightarrow\ \text{壳层内\textbf{无}码字}\ ✓\ (\text{方阵孤立}\ ✓);\quad I=4\cdot16=64\ \textbf{取等}\ ✓✓$$
$$

## §4 靶心更新

```
$$\textbf{旧靶心（已否）}: M=K\Rightarrow I\le2\ ✗\ (\text{Wille 码含方阵}\Rightarrow I\ge4\ ✓)$$
$$\textbf{新靶心}: \text{分解后分别研究}\ \boxed{I_{\rm nw}\ \text{与壳层耦合}}\ ✓\ ——\ \text{不再限制整个 }I\ ✓$$
$$\textbf{具体问题}: \text{① }I_{\rm nw}\ \text{是否被极小性限制}\ ⚠️;\ \text{② 壳层码字是否被迫（private-point 预算）}\ ⚠️$$
$$

## §5 状态

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \text{(9,62) 全码}: \text{仍未获得}\ ✗$$
$$\text{锚定 SAT（含 Wille 方阵）}: \text{运行中}\ ⏳;\quad \text{免费 SAT}: \text{950s 超时无解}\ ✗\ (\text{不得当 UNSAT 证据}\ ✓)$$
$$

## §6 边界（诚实标注）

- §1/§2 为**我方证明** ✓（§1 已数值核验 0 违反 ✓）；§3 为**数值实测** ✓
- **未读 Wille 1996 一手** ⚠️（方阵证据来自 Kéri 论文 ✓）；**(9,62) 全码未获得** ✗
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：方阵闭合引理、壳层界面、方阵驱动分解、壳层耦合
- **档案已有（引用，不列为提出）**：方阵、I、S、minimality
