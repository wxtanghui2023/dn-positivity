已查地图（**先查后写**）：`C-166`（对偶间隙诊断）、`C-169`（证书附录）、`C-159`（周期单调性引理；鸽笼定理）、`C-158`（`\kappa_N`）、`C-157`（新增窗口段）、`C-161`（单纯形签名）。关键词回查：`新鲜窗口机制`=0、`近似通约`=0、`最硬点直测`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 15:23 决定）**：**止损证书路线；转 `(c)` 单调性归约，攻"lcm 过大／无理配比"情形。**
**结论（先行）**：$$\textbf{(一)}\ (b)\ \text{实测有真实改进但不改指数}（\text{按唐先生判断}\ \textbf{止损}）✓$$
$$\qquad \text{混合}\ \lambda\ \text{（凸化）界}：\text{对偶间隙}\ \text{从}\ \textbf{线性}\to\textbf{近二次}：\text{改善}\ 7\text{–}17\times✓✓$$
$$\qquad （h=4^\circ：0.0790\to0.0110；h=0.25^\circ：0.0052\to0.0003）\ \text{但仍是}\ N_0^M\ \text{结构}✓$$
$$\textbf{(二)}\ ⚠️\ (c)\ \text{诊断 1}（\textbf{坏消息}）：\text{数值极小点}\ \textbf{不} \text{近似通约}（M\ge3）✓$$
$$\qquad M=2：q^*=12,\ \delta=\mathbf 0\（\textbf{精确通约}，\text{周期引理直接适用}）✓；M=3：q^*=19,\ \delta=0.0678✓$$
$$\qquad M=4：q^*=21,\ \delta=0.2596；M=5：q^*=27,\ \delta=0.2465；M=6：q^*=17,\ \delta=0.3167✓$$
$$\qquad \Longrightarrow \textbf{"四舍五入到小周期有理配置"的路线不覆盖最硬点}✓$$
$$\textbf{(三)}\ ⭐⭐\ (c)\ \text{诊断 2}（\textbf{好消息}）：\text{在最硬点上，单调性推论}\ \textbf{成立且余量很大}✓✓$$
$$\qquad \text{测}：\min_\psi\max_{k\le5(M+1)}[A(k)+\cos(k\psi)]\ \text{vs}\ m_M：M=2\ \text{余量}+0.809；M=3\ +1.104；M=4\ +0.861✓✓$$
$$\qquad ⭐\ \text{且}\ A\ \text{的最大值}\ \textbf{恰好落在新增窗口段}：M=2\ k=12>5M=10；M=3\ k=19>15；M=4\ k=21>20✓✓$$
$$\qquad \Longrightarrow \textbf{"新鲜窗口机制"被确认}：\text{旧配置在最优化窗口}\ [1,5M]\ \text{内被"配平"}，\ \text{而多出的}\ 5\ \text{个}\ k\ \textbf{不受约束}✓✓$$

FREEZE-ACK: 本档即冻结期内的诊断与路线评估（依 `§8.1`；不产候选结论）

D0: 本档对象 = **(b) 止损（混合 λ 界的实测改进）＋ (c) 两项诊断（近似通约失败；新鲜窗口机制确认）＋ 剩余缺口重述** —— 关系 = 诊断与路线评估，非新机制
D1: 0

# C-170 · ⭐⭐ **`(b)` 止损；`(c)` 两项诊断：新鲜窗口机制**

> **唐先生 2026-09-19 15:23**：止损证书；转 `(c)`，攻 lcm 过大／无理配比 ✓

---

## §1 `(b)` 收官（实测改进，但按判断止损）

$$\text{旧界（纯}\ k\text{）}：\min_\varphi\max_k\ \ge\ \max_k\min_\varphi S_k✓\qquad \text{新界（混合}\ \lambda\text{）}：\min_\varphi\max_k\ \ge\ \max_{\lambda\in\Delta}\min_\varphi\ \sum_k\lambda_k S_k✓✓$$
$$\qquad \text{机制}：\text{凸化后最优}\ \lambda\ \text{在极小极大点处}\ \sum_k\lambda_k g_k=0 \Longrightarrow \text{该点成为}\ \textbf{临界点} \Longrightarrow \text{箱内损失}\ O(h)\to O(h^2)✓✓$$
$$\begin{array}{c|rrrrr}
h\ (\text{度}) & 4 & 2 & 1 & 0.5 & 0.25\\\hline
\text{旧界间隙} & 0.0790 & 0.0412 & 0.0216 & 0.0106 & 0.0052\\
\text{新界间隙} & 0.0110 & 0.0044 & 0.0026 & 0.0010 & 0.0003\\
\text{改善} & 7.2\times & 9.4\times & 8.3\times & 10.6\times & 17.3\times\\
\end{array}✓✓$$
$$\Longrightarrow \text{① 是真的改进（}\text{线性}\to\text{近二次}）；\ \text{② 但}\ \textbf{不改指数} \Longrightarrow \text{按唐先生判断}\ \textbf{止损}✓✓$$

## §2 ⚠️ `(c)` 诊断 1：最硬点**不**近似通约

$$\text{定义}：\delta(q):=\max_j\mathrm{dist}\big(q\varphi_j/(2\pi),\mathbb Z\big)；\ q^*=\arg\min_{q\le5(M+1)}\delta(q)✓$$
$$\begin{array}{c|r|r|r}
M & \text{窗口上界}\ 5(M+1) & q^* & \delta(q^*)\\\hline
2 & 15 & 12 & \mathbf{0}\ (\text{精确通约})\\
3 & 20 & 19 & 0.0678\\
4 & 25 & 21 & 0.2596\\
5 & 30 & 27 & 0.2465\\
6 & 35 & 17 & 0.3167\\
\end{array}✓✓$$
$$\Longrightarrow M\ge3\ \text{的极小点}\ \textbf{不} \text{近似通约（}\delta\approx0.07\text{–}0.32，\text{即某些坐标差近}\ \tfrac14\ \text{圈）}✓$$
$$\qquad \Longrightarrow \textbf{"四舍五入到小周期有理配置 ＋ 周期引理"}\ \text{这条路线}\ \textbf{不覆盖最硬点}✓✗$$

## §3 ⭐⭐ `(c)` 诊断 2：新鲜窗口机制（本档主要正面发现）

$$\text{在数值极小点（最硬点）上直接测单调性推论}：$$
$$\begin{array}{c|r|r|r|r}
M & m_M & \min_\psi\max_{k\le5(M+1)}[A(k)+\cos(k\psi)] & \text{余量} & A\ \text{的最大}\ k\\\hline
2 & 0.5000 & 1.3090 & +0.809 & 12\ (>5M=10)\\
3 & 0.7769 & 1.8813 & +1.104 & 19\ (>15)\\
4 & 0.8109 & 1.6718 & +0.861 & 21\ (>20)\\
\end{array}✓✓$$
$$\qquad （A(k):=\text{旧}\ M\ \text{点在}\ k\ \text{处的和}）✓$$
$$\Longrightarrow \textbf{两个关键事实}：$$
$$\qquad \text{① 单调性推论在最硬点上}\ \textbf{成立，余量}\ 0.81\text{–}1.10 \Longrightarrow \text{比证书的}\ 10^{-6}\ \text{余量}\ \textbf{宽}\ 10^5\ \text{倍}✓✓$$
$$\qquad \text{②}\ A\ \text{的最大值}\ \textbf{总落在新增窗口段}\ [5M+1,5(M+1)]✓✓$$
$$\qquad \text{机制理解}：\text{旧配置是针对窗口}\ [1,5M]\ \text{优化/配平的} \Longrightarrow \text{多出的}\ 5\ \text{个}\ k\ \textbf{不受约束} \Longrightarrow \text{往往给出大值}✓✓$$

## §4 剩余缺口的**清洁重述**（`(c)` 的新靶子）

$$\textbf{充分条件}：\text{若}\ \max_{k\le5(M+1)}A(k)\ \ge\ m_M+1，\ \text{则}\ \forall\psi\ \text{（因新点项}\ \ge-1）：\max_k[A+\cos(k\psi)]\ \ge\ m_M+1-1=m_M✓✓$$
$$\text{实测}：\text{在极小点上}\ \max A=2.0/2.88/2.50\ \text{vs}\ m_M+1=1.5/1.78/1.81 \Longrightarrow \textbf{成立}✓✓$$
$$\qquad ⚠️\ \text{但}\ M=1\ \text{反例}：\max A=1<m_1+1=1.5 \Longrightarrow \text{该充分条件对}\ M=1\ \text{不成立（特例）}✓$$
$$\Longrightarrow \textbf{待证命题（新靶子）}：\forall M\ge2,\ \forall\varphi\in[0,\pi]^M：\ \max_{k\le5(M+1)}\ \sum_j\cos(k\varphi_j)\ \ge\ m_M+1✓$$
$$\qquad \text{等价说法}：\textbf{"多出的}\ 5\ \text{个}\ k\ \text{不能同时小"}✓✓$$
$$\qquad \text{（这就是}\ \text{`C-157`}\ \text{"新增窗口段"的}\ \textbf{定量版}：\text{当时只做到"最优点落在新增段"的现象观察}）✓✓$$

## §5 边界与回查

- ⚠️ §1 为**实算**（一维逐维网格 `4001` 点）；§2／§3 为**实算**（`\psi` 网格 `20001`；`q` 全枚举）✓
- ⚠️ §4 的命题为**新靶子**（未证）；`M=1` 反例已标 ✓
- ⚠️ **不声称** `(\text{RP}_M)` 的一般成立；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 15:2x）`[纪律]`（先跑后写）

```
技术词 新鲜窗口机制   命中文件数=0 ::  ⟹ 本档新增
技术词 近似通约      命中文件数=0 ::  ⟹ 本档新增
技术词 最硬点直测    命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
