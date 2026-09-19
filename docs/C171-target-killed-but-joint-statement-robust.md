已查地图（**先查后写**）：`C-170`（新鲜窗口机制；新靶子）、`C-169`（证书附录）、`C-159`（周期单调性引理；鸽笼定理）、`C-158`（`\kappa_N`）、`C-156`（单调性归约）。关键词回查：`算术原因`=1（通用词）、`扩展窗配平`=0（**新增**）、`联合判据`=0（**新增**）。
**本档任务（唐先生 2026-09-19 15:28 两条）**：**① `A(k)` 含义澄清 ② 先讲清 `M=1` 反例的具体机制，再决定是否硬冲一般命题。**
**结论（先行）**：$$\textbf{(一)}\ \text{澄清}：A(k):=\sum_{j\le M}\cos(k\varphi_j)（\text{旧}\ M\ \text{点在第}\ k\ \text{点的和}）✓；\ \text{判据}\ \max_{k\le5(M+1)}A(k)\ \text{取在}\ \textbf{整个扩展窗口}✓$$
$$\qquad \text{（虽实测最优点总落在新增段}\ [5M+1,5(M+1)]）✓$$
$$\textbf{(二)}\ ⚠️\ \textbf{新靶子被否掉}：\text{充分条件}\ \max_{k\le5(M+1)}A(k)\ge m_M+1\ \textbf{对一切配置不成立}✓✗$$
$$\qquad m'_M:=\min_\varphi\max_{k\le5(M+1)}A(k)：M=1\to0.841；2\to0.962；3\to0.841；4\to0.919\quad(\text{全}\ <\ m_M+1)✓✗$$
$$\qquad ⭐\ \text{且}\ m'_1=\cos\tfrac{2\pi}{11}=\kappa_{10}=0.841254 \Longrightarrow \text{恰是}\ \textbf{鸽笼定理的锐值}（\text{窗口}\ 10）✓✓$$
$$\qquad \text{原因}：\text{存在}\ \textbf{扩展窗配平} \text{的配置}（\text{非}\ m_M\ \text{的极小点）} \Longrightarrow A\ \text{在整窗上都被压低}✓$$
$$\textbf{(三)}\ ⭐⭐\ \textbf{但联合判据依然稳健}：\text{在那些配置上（}A\ \text{最弱处）}：$$
$$\qquad \min_\psi\max_{k\le5(M+1)}[A(k)+\cos(k\psi)]：M=2\to0.962（+0.462）；3\to0.994（+0.217）；4\to1.093（+0.282）\ ✓✓$$
$$\qquad \Longrightarrow \textbf{单调性推论在最弱点上仍成立}，\ \text{且}\ \textbf{联合值}\ \textbf{超过}\ \max A（0.99>0.84；1.09>0.92）⟹ \text{新点是在"加值"而非对抗}✓✓$$
$$\textbf{(四)}\ \Longrightarrow \text{靶子应重述为}\ \textbf{联合不等式} \text{本身（而非}\ A\ge m_M+1\ \text{这个过强的充分条件）}✓$$

FREEZE-ACK: 本档即冻结期内的检验与靶子修正（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`A(k)` 澄清 ＋ `M=1` 反例解剖（算术原因）＋ 新靶子的否证（`m'_M`）＋ 联合判据的稳健性** —— 关系 = 检验与靶子修正，非新机制
D1: 0

# C-171 · ⭐⭐ **靶子被否掉，但联合判据更稳健**

> **唐先生 2026-09-19 15:28**：① 澄清 `A(k)` ② 先解剖 `M=1`，再决定是否硬冲 ✓

---

## §1 `A(k)` 澄清与 `M=1` 解剖

$$A(k):=\sum_{j\le M}\cos(k\varphi_j)\quad(\text{旧}\ M\ \text{点在第}\ k\ \text{点的贡献和})✓$$
$$\qquad \text{判据}\ \max_{k\le5(M+1)}A(k)\ \text{取在}\ \textbf{整个扩展窗口}\ [1,5(M+1)]；\ \text{实测最优}\ k\ \text{总在新增段}✓$$

$$M=1：\text{唯一旧点配置}\ \varphi_1=60^\circ（m_1\ \text{的极小点，引理 C 取等}）✓$$
$$\qquad A(k)=\cos(60^\circ k),\ k=1..10：\ 0.5,\ -0.5,\ -1,\ -0.5,\ 0.5,\ \mathbf 1,\ 0.5,\ -0.5,\ -1,\ -0.5✓$$
$$\qquad \text{旧窗口}\ [1,5]\ \text{的}\ \max=0.5（=m_1，定义成立）；\ \text{扩展窗口}\ \max=1\ (k=6)；\ \text{靶子}\ 1.5 \Longrightarrow \textbf{不成立}✗$$
$$\textbf{真正的原因不是几何，是}\ \textbf{算术}：A(k)\le M\ \forall k \Longrightarrow \text{靶子}\ m_M+1\ \text{可达}\iff m_M\le M-1✓$$
$$\qquad M=1：m_1=0.5>0=M-1 \Longrightarrow \textbf{对任何}\ M=1\ \text{配置都不成立（恒不可达）}✓✓$$
$$\qquad M=2：m_2=0.5\le1=M-1 \Longrightarrow \textbf{可达}✓$$

## §2 ⚠️ 决定性检验：新靶子**被否掉**

$$m'_M:=\min_{\varphi\in[0,\pi]^M}\ \max_{k\le5(M+1)}\ A(k)\qquad(\text{与}\ m_M\ \text{同为极小极大，但窗口}\ 5(M+1))✓$$
$$\begin{array}{c|r|r|r|c}
M & m'_M & m_M+1 & \text{成立？} & \text{取到的配置（度）}\\\hline
1 & 0.841254 & 1.500000 & ✗ & \{163.636\}\\
2 & 0.961676 & 1.500000 & ✗ & \{22.864,\ 87.694\}\\
3 & 0.841141 & 1.776882 & ✗ & \{102.013,\ 85.029,\ 35.037\}\\
4 & 0.919016 & 1.810937 & ✗ & \{51.082,\ 149.534,\ 124.383,\ 13.220\}\\
\end{array}✓✗$$
$$\Longrightarrow \textbf{充分条件对一切}\ M\ \textbf{不成立}：\text{存在}\ \textbf{扩展窗配平} \text{的配置} \Longrightarrow A\ \text{在整窗上都被压低}✓$$
$$\qquad ⭐\ m'_1=\cos\tfrac{2\pi}{11}=0.841254=\kappa_{10}\ \Longrightarrow \text{恰是}\ \textbf{鸽笼定理在窗口}\ 10\ \text{的锐值}✓✓$$
$$\qquad \text{且}\ m'_M\ge m_M\ \text{（窗口更大，恒成立）}；\ \text{间隙}\ m'_M-m_M\approx0.06\text{–}0.11\ \mathbf\ll1 \Longrightarrow \text{这就是该路线失败的量}✓$$

## §3 ⭐⭐ 但联合判据依然稳健（本档主要正面发现）

$$\text{在}\ m'_M\ \text{的极小点上（即}\ A\ \text{最弱处）直接测单调性推论}：$$
$$\begin{array}{c|r|r|r|r}
M & \max_k A & \min_\psi\max_k[A+\cos(k\psi)] & m_M & \text{余量}\\\hline
2 & 0.962 & \mathbf{0.962} & 0.500 & +0.462\\
3 & 0.841 & \mathbf{0.994} & 0.777 & +0.217\\
4 & 0.919 & \mathbf{1.093} & 0.811 & +0.282\\
\end{array}✓✓$$
$$\Longrightarrow \text{① 单调性推论在这些"}\ A\ \text{最弱点"上}\ \textbf{仍成立}；\ \text{② 且}\ \textbf{联合值超过}\ \max A（0.99>0.84；1.09>0.92）✓✓$$
$$\qquad \Longrightarrow \text{新点}\ \psi\ \text{不是在对抗，而是在}\ \textbf{加值} \Longrightarrow \text{"最坏情形}\ \cos=-1\text{"}\ \text{的估计}\ (\text{充分条件})\ \textbf{过强}✓✓$$

## §4 靶子重述（本档产出）

$$\textbf{旧靶子（已否）}：\max_{k\le5(M+1)}A(k)\ \ge\ m_M+1\quad ✗$$
$$\textbf{新靶子（保留）}：\forall\varphi,\psi：\ \max_{k\le5(M+1)}\big[A(k)+\cos(k\psi)\big]\ \ge\ m_M✓$$
$$\qquad \text{实证：在最硬的两类配置（}\ m_M\ \text{极小点／}\ m'_M\ \text{极小点）上，余量}\ 0.22\text{–}1.10✓✓$$
$$\qquad \text{待证的核心}：\textbf{"新点不能在所有好}\ k\ \text{上同时反相"}✓$$

## §5 边界与回查

- ⚠️ §2／§3 全部为**实算**（`differential\_evolution`＋`Nelder–Mead`；`\psi` 网格 `20001`）✓
- ⚠️ `m'_M` 为**上界**（优化器可能未达全局）；`M\ge5` 未算 ⟹ **不声称**其值 ✓
- ⚠️ 新靶子**未证**；`M=1` 的失败原因已给出（**算术**：`m_1>M-1`）✓
- ⚠️ **不声称** `(\text{RP}_M)` 一般成立；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓ —— 本档正因先测而避免了在假命题上投入）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 15:3x）`[纪律]`（先跑后写）

```
技术词 算术原因   命中文件数=1 ::  ⟹ 通用词（不计）
技术词 扩展窗配平  命中文件数=0 ::  ⟹ 本档新增
技术词 联合判据   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：`算术原因`＝**通用词**；`扩展窗配平`／`联合判据`＝**本档新增** ✓
