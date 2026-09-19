已查地图（**先查后写**）：`C-156`（单调性归约）、`C-157`（新增窗口段；阻尼；Lemma 2.2 逐字）、`E4-ENGINE-2`（引理 C 及其初等覆盖证明）、`C-152`–`C-154`（`M=2`）。关键词回查：`缩放引理`=0、`周期单调性`=0、`单点窗口数列`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:33「继续推导完成证明」）**：**把单调性归约往前推**。
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{新对象：单点窗口数列}\ \kappa_N:=\inf_{\theta}\max_{1\le m\le N}\cos(m\theta)✓✓$$
$$\qquad \text{实测闭式}\ \boxed{\kappa_N=\cos\frac{2\pi}{N+1}}（N\le20\ \text{全部吻合}）：\ -1,\ -\tfrac12,\ 0,\ +0.30902,\ +\tfrac12,\ +0.62349,\dots✓✓$$
$$\qquad (\theta^*\ \text{为}\ 2\pi/(N+1)\ \text{的整数倍} \Longrightarrow \textbf{正规}\ (N+1)\text{-边形极值}，\text{与 Turán 定理同族})✓$$
$$\textbf{(二)}\ ⭐\ \textbf{覆盖引理（本档已严格证明）}：\forall\theta,\ \exists m\in\{1,2,3\}:\ \cos(m\theta)\ge0（N=3\ \text{情形，}\kappa_3=0）✓✓$$
$$\textbf{(三)}\ ⭐⭐\ \textbf{周期单调性引理（本档已严格证明）}：$$
$$\qquad \text{若旧}\ M\ \text{点有共同周期}\ P\ \text{且}\ P\le\tfrac{5(M+1)}3，\ \text{则}\ \forall\psi\in[0,\pi]:\ \max_{1\le k\le5(M+1)}\Big[\sum_{j\le M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ M\ \ge\ m_M✓✓$$
$$\qquad \Longrightarrow \textbf{单调性在该类配置上成立}（\text{用平凡界}\ m_M\le M\ \text{即可，\textbf{无需}任何数值}）✓✓$$
$$\textbf{(四)}\ \text{加强版}：P\le M+1\ \text{时}\ \text{窗口含}\ \ge5\ \text{个}\ P\ \text{的倍数} \Longrightarrow \text{用引理 C} \Longrightarrow \max\ \ge\ M+\tfrac12✓✓$$

FREEZE-ACK: 本档即冻结期内的推导推进（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`\kappa_N` 数列（闭式 `\cos\frac{2\pi}{N+1}`）＋ 覆盖引理（已证）＋ 周期单调性引理（已证）** —— 关系 = 推导推进，非新机制
D1: 0

# C-158 · ⭐⭐ **`\kappa_N` 数列、覆盖引理、周期单调性引理**

> **唐先生 2026-09-19 13:33**：**「继续推导完成证明」** ✓

---

## §1 ⭐ 新对象：单点窗口数列

$$\kappa_N:=\inf_{\theta\in[0,\pi]}\ \max_{1\le m\le N}\ \cos(m\theta)\qquad(N\ge1)✓$$
$$\text{作用}：\text{它是}\ (\text{RP}_M)\ \text{的}\ \textbf{"单点"版本}（1\ \text{点，窗口}\ N）；\ \text{周期性归纳把它}\ \textbf{降到这里}✓✓$$
$$\begin{array}{c|r|l}
N & \kappa_N\ (\text{实测}) & \cos\frac{2\pi}{N+1}\\\hline
1 & -1.000000 & -1\\
2 & -0.500000 & -0.5\\
3 & +0.000000 & 0\\
4 & +0.309017 & \cos72^\circ=0.309017\\
5 & +0.500000 & \cos60^\circ=0.5\ (\textbf{即引理 C})\\
6 & +0.623490 & \cos\frac{2\pi}7\\
8 & +0.766045 & \cos40^\circ\\
10 & +0.841254 & \cos\frac{2\pi}{11}\\
12 & +0.885456 & \cos\frac{2\pi}{13}\\
16 & +0.932472 & \cos\frac{2\pi}{17}\\
20 & +0.955573 & \cos\frac{2\pi}{21}\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{闭式（数值}\ N\le20\ \text{全吻合）}：\boxed{\kappa_N=\cos\frac{2\pi}{N+1}}\qquad(\text{极值在}\ \theta^*=\tfrac{2\pi}{N+1}\ \text{的整数倍处})✓✓$$
$$\qquad \text{结构：极值配置＝}\textbf{正规}\ (N+1)\ \text{边形} \Longrightarrow \text{与 Turán 定理（等号＝正多边形顶点）\textbf{同族}}✓$$

## §2 ⭐ 覆盖引理（**本档已严格证明**）

$$\textbf{引理（}N=3\text{）}：\forall\theta\in\mathbb R,\ \exists m\in\{1,2,3\}:\ \cos(m\theta)\ \ge\ 0✓✓$$
$$\textbf{证明}（\text{区间覆盖}）：\text{记}\ S_m:=\{\theta:\cos(m\theta)\ge0\}=\bigcup_{j\in\mathbb Z}\Big[\tfrac{2\pi j-\pi/2}{m},\ \tfrac{2\pi j+\pi/2}{m}\Big]✓$$
$$\qquad S_1=[-\tfrac\pi2,\tfrac\pi2]\ \text{模}\ 2\pi;\quad S_2=[-\tfrac\pi4,\tfrac\pi4]\cup[\tfrac{3\pi}4,\tfrac{5\pi}4];\quad S_3=[-\tfrac\pi6,\tfrac\pi6]\cup[\tfrac\pi2,\tfrac{5\pi}6]\cup[\tfrac{7\pi}6,\tfrac{3\pi}2]✓$$
$$\qquad S_1\cup S_2\cup S_3\supseteq[0,\tfrac{5\pi}6]\cup[\tfrac{3\pi}4,\tfrac{5\pi}4]\cup[\tfrac{7\pi}6,2\pi)=[0,2\pi)✓✓$$
$$\qquad (\text{因}\ \tfrac{5\pi}6<\tfrac{5\pi}4\ \text{且}\ \tfrac{7\pi}6<\tfrac{5\pi}4 \Longrightarrow \text{无缝隙})✓\qquad\square$$
$$\qquad \text{数值核验}：\min_\theta\max_{m\le3}\cos(m\theta)=+0.00000000\ \ge0✓✓$$

## §3 ⭐⭐ 周期单调性引理（**本档已严格证明**）

$$\textbf{引理}：\text{设}\ \varphi_1,\dots,\varphi_M\in[0,\pi]\ \text{有共同周期}\ P（\text{即}\ P\varphi_j\in2\pi\mathbb Z\ \forall j），\text{且}\ P\le\tfrac{5(M+1)}3✓$$
$$\qquad \text{则}\ \forall\psi\in[0,\pi]:\quad \max_{1\le k\le5(M+1)}\Big[\sum_{j=1}^{M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ M\ \ge\ m_M✓✓$$
$$\textbf{证明}：\text{取}\ k=Pm,\ m\in\{1,2,3\}；\text{由}\ P\le5(M+1)/3\ \text{知}\ 3P\le5(M+1)\ \text{故三个}\ k\ \text{都在窗口内}✓$$
$$\qquad \text{①}\ \sum_{j\le M}\cos(Pm\varphi_j)=\sum_{j\le M}1=M\quad(\text{共同周期}\Longrightarrow\text{每一项都是}\ \cos(2\pi\cdot\mathbb Z)=1)✓✓$$
$$\qquad \text{②}\ \text{覆盖引理（§2）应用于}\ \theta=P\psi：\exists m^*\le3:\ \cos(m^*P\psi)\ge0✓$$
$$\qquad \Longrightarrow\ \max_k\ \ge\ M+\cos(m^*P\psi)\ \ge\ M✓✓$$
$$\qquad \text{③}\ m_M\le M\ \text{是}\ \textbf{平凡界}（\text{任一项}\ \le1）\Longrightarrow M\ge m_M✓✓\qquad\square$$
$$\Longrightarrow \textbf{该类配置上单调性成立，且}\ \textbf{不需要任何数值输入}✓✓$$

## §4 加强版（窗口含 ≥5 个倍数时）

$$\text{若}\ P\le M+1，\ \text{则}\ \lfloor5(M+1)/P\rfloor\ge5 \Longrightarrow \text{可用}\ \textbf{引理 C}（\kappa_5=\tfrac12，\text{已证}）✓$$
$$\qquad \Longrightarrow\ \max\ \ge\ M+\tfrac12\qquad(\text{更强，但适用范围更窄})✓$$

## §5 诚实的边界（本档覆盖了什么、没覆盖什么）

$$\text{覆盖}：\text{"}\textbf{小周期}" \text{类配置}（\text{共同周期}\ P\le5(M+1)/3）✓✓$$
$$\text{未覆盖}：\text{无小周期者}（\textbf{无理配比} \text{／大分母有理配比}）\Longrightarrow \text{该情形下"倍数技巧"不可用}✓$$
$$\qquad ⚠️\ \text{关键诚实}：\text{数值观察到的极小点}\ (\text{如}\ (60^\circ,90^\circ)，\text{周期}\ 12>5\cdot3/3=5)\ \textbf{不在本类内}✓$$
$$\qquad \Longrightarrow \textbf{本档引理不覆盖极值情形}，\ \text{故}\ \textbf{不能} \text{据此声称一般单调性}✓✓$$

## §6 下一步

$$\text{①}\ ⭐\ \text{把}\ \kappa_N=\cos\tfrac{2\pi}{N+1}\ \text{一般情形}\ \textbf{严格证明}（\text{疑似经典，与 Turán 正规多边形极值同族} \Longrightarrow \textbf{先做文献核查}）✓✓$$
$$\qquad \text{一旦有一般}\ \kappa_N，\text{周期单调性引理可放宽到}\ P\le\tfrac{5(M+1)}{3}\ \text{的}\ \textbf{最优形式}✓$$
$$\text{②}\ \text{补类：无小周期情形} \Longrightarrow \text{需 Turán 型定量输入}（\text{或 Case A 型聚类归约}）✓$$
$$\text{③}\ \text{注意}\ \kappa_N\ \text{与}\ (\text{RP}_M)\ \text{的关系}：\kappa_{5M}\ \text{是"1 点/窗口}\ 5M"；\ m_M\ \text{是"M 点/窗口}\ 5M"✓$$

## §7 边界与回查

- ⚠️ §1 的闭式为**数值吻合**（`N\le20`），**非本档定理**；§3 的证明只用到**已证**的 §2 ✓✓
- ⚠️ §2 的区间覆盖为**严格**（显式区间＋无缝）✓
- ⚠️ **不声称**一般单调性；**不声称**一般 `M`；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:5x）`[纪律]`（先跑后写）

```
技术词 缩放引理    命中文件数=0 ::  ⟹ 本档新增
技术词 周期单调性  命中文件数=0 ::  ⟹ 本档新增
技术词 单点窗口数列 命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
