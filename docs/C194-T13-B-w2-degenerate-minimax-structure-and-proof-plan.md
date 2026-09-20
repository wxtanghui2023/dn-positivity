已查地图（**先查后写**）：查 `TARGETS` L132（T13）、`C-152`／`C-154`（M=2 三段拼装模板）、`C-162`（紧／松二分）、`C-193`（T13-B 首轮数值）。回查见 §5 ✓

D0: 本档对象 = **T13-B 的 w=2 分支**：候选极小点 $(π/3,π/2)$ 的**退化极小点结构** ＋ 三区覆盖 ＋ 精确恒等式 ＋ 证明计划 —— 关系 = 新构造 ＋ 结构定位
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 候选点上的完整局部数据（$w=2$，$S_k=2\cos(k\varphi_1)+\cos(k\varphi_2)$）

| $k$ | $S_k$ | $\partial/\partial\varphi_1$ | $\partial/\partial\varphi_2$ | |
|---|---|---|---|---|
| 1 | $1$ | $-1.7320508$ | $-1$ | ← 活跃 |
| 5 | $1$ | $+8.6602540$ | $-5$ | ← 活跃 |
| 6 | $1$ | $0$ | $0$ | ← 活跃，**梯度为零** |
| 7 | $1$ | $-12.1243557$ | $+7$ | ← 活跃 |
| 2,3,9,10 | $-2$ | — | — | |
| 4,8 | $0$ | — | — | |

$$\textbf{活跃集}\ A=\{1,5,6,7\}✓\qquad \mathbf{g_6=(0,0)}✓（\text{驻点}）\qquad 7g_5+5g_7=0✓\ （\text{又是}\ k+k'=12✓）$$
$$\textbf{covering 常数}\ c=\min_{|u|=1}\max_{k\in A}\langle g_k,u\rangle=\mathbf{0}✓\ （\text{数值}\ 7.3\times10^{-5}，\text{即离散误差}）⟹ \boxed{\textbf{退化极小点}}✗$$
$$\qquad \text{退化方向}\ u_0\propto(1,\sqrt3)（60^\circ）✓\qquad\Longrightarrow \textbf{一阶机制失效}✗ ⟹ \textbf{必须二阶}✓$$

## §2 ⭐ 精确恒等式（$S_6$ 的纯二阶结构）

$$S_6-1\ =\ 2\cos(6\delta_1)-\cos(6\delta_2)-1\ =\ 2\sin^2(3\delta_2)-4\sin^2(3\delta_1)✓✓$$
$$\Longrightarrow\ \boxed{\ S_6\ge1\iff|\sin 3\delta_2|\ \ge\ \sqrt2\,|\sin 3\delta_1|\ }✓✓\qquad（\text{数值一致率}\ 100.0000\%✓）$$
$$\qquad \text{沿退化方向}\ \delta_2=\sqrt3\delta_1：S_6-1=2\sin^2(3\sqrt3\delta_1)-4\sin^2(3\delta_1)\approx18\delta_1^2>0✓✓$$
$$\qquad\Longrightarrow \textbf{退化方向恰被}\ S_6\ \text{的纯二阶项救回}✓✓$$

## §3 ⭐ 三区覆盖（球 $r=0.10$ rad 内，1,130,905 点）

$$W:=\sqrt3\,\delta_1-\delta_2✓（\text{边界线}\ W=0\ \text{就是退化方向}✓）$$
$$\text{逐函数精确判据}：S_5\ge1\iff2\cos(5\delta_1+5\pi/3)\ge1+\sin(5\delta_2)✓；\ S_7\ge1\iff2\cos(7\delta_1+7\pi/3)\ge1-\sin(7\delta_2)✓（\text{均}\ 100\%\ \text{一致}）✓$$
$$\{S_5\ge1\}\cup\{S_6\ge1\}\ \text{仅}\ 69.55\%✗\qquad\boxed{\{S_5\ge1\}\cup\{S_6\ge1\}\cup\{S_7\ge1\}=100.00\%}✓✓$$
$$\qquad \text{缺口恰在}\ W\approx0\ \text{附近（那里}\ S_5/S_7\ \text{的一阶项同时消失✗），由}\ S_6\ \text{填满}✓✓$$

## §4 等号集与证明计划

$$\text{数值等号集}：\text{网格（}3000^2\text{，}π/3\ \text{与}\ π/2\ \text{恰为格点}✓）最小值=\mathbf{1.000000000}✓，\text{达成点}\ \textbf{恰 1 个}✓$$
$$\qquad \Longrightarrow \text{与无阻尼}\ M=2\ \text{同型：紧、孤立}✓（\texttt{C-162}\ \text{的紧／松二分}✓）$$

$$\textbf{证明计划（三段拼装，模板}= \texttt{C-152}／\texttt{C-154}\text{）}：$$
$$\qquad \textbf{① 局部解析}：\text{球}\ |\delta|\le R\ \text{内三区划分}（W\ \text{的符号 ＋ 修正项）✓，\text{各自用显式 Taylor 余项}✓$$
$$\qquad \qquad \text{预期形式}：\delta_2\le\sqrt3\delta_1-\alpha\delta_1^2⟹S_5\ge1✓；\delta_2\ge\sqrt3\delta_1+\beta\delta_1^2⟹S_7\ge1✓；\text{中间条带}⟹S_6\ge1✓$$
$$\qquad \textbf{② 环形证书}：r_0\le|\delta|\le R\ \text{用分离箱 B\&B（2 维，廉价）✓}$$
$$\qquad \qquad ⚠️\ \text{实测教训：含原点的箱【永远】无法被分离界认证}✗（因}\ \max_k\min_B S_k<1\text{）}⟹ \text{原点必须解析处理}✓✓$$
$$\qquad \textbf{③ 远场}：|\delta|>R\ \text{用网格＋Lipschitz}✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 退化极小点   命中文件数=0    ::
技术词 三区覆盖     命中文件数=1    ::  ./qlambda-lemma.md
```
$$\text{判定}：\text{「退化极小点」本档首次命名}✓；\text{「三区覆盖」为}\ \textbf{通用词}✗（\texttt{qlambda-lemma.md}\ \text{为不同语境}）⟹ \textbf{不计本档新增}✓$$

## §6 边界

- §1／§3／§4 的等号集均为**数值** ✓（多起点优化／网格抽样 ✓）⟹ 只作结构定位，未升级为定理 ✓
- §2 的恒等式是**精确**的（纯三角恒等 ✓）
- 本档**不**声称 $g_2(10)=1$ 已证 ✓（那是 ①+②+③ 完成后的结论 ✓）
- ⚠️ 局部证书试验脚本的 $r_0$ 过滤器有 bug ✗，该次试验**无效** ✓，但"含原点箱不可认证"这一结论对分离界是结构性的 ✓
- **未用** RH；**未改**他档 ✓
