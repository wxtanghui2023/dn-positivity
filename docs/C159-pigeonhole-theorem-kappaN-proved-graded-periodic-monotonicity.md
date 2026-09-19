已查地图（**先查后写**）：`C-158`（`\kappa_N` 数列；覆盖引理；周期单调性引理——本档**统一并严格化**）、`C-157`（新增窗口段；阻尼）、`C-156`（单调性归约）、`E4-ENGINE-2`（引理 C）。关键词回查：`鸽笼定理`=0、`分级周期引理`=0、`lcm门槛`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:37 追问）**：**能否用覆盖引理直接处理极值配置 `(60^\circ,90^\circ)`（不要求公共周期）？**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \boxed{\textbf{鸽笼定理}：\forall\theta\in\mathbb R,\ \forall N\ge1:\quad \max_{1\le m\le N}\cos(m\theta)\ \ge\ \cos\frac{2\pi}{N+1}}\quad(\textbf{三行证明，且最佳})✓✓✓$$
$$\qquad \text{证明}：\text{取}\ N+1\ \text{个点}\ 0,\theta,2\theta,\dots,N\theta\ (\mathrm{mod}\ 2\pi) \Longrightarrow \text{鸽笼} \exists 1\le m\le N:\ \|m\theta/2\pi\|\le\tfrac1{N+1}✓✓$$
$$\qquad \text{取}\ \theta=\tfrac{2\pi}{N+1}\ \text{时}\ \max=\cos\tfrac{2\pi}{N+1}\ \textbf{恰好} \Longrightarrow \kappa_N=\cos\tfrac{2\pi}{N+1}\ \text{为}\ \textbf{定理}（\text{非推测}）✓✓$$
$$\qquad \Longrightarrow \textbf{统一}：\text{引理 C}＝N=5\ (\cos\tfrac{2\pi}6=\tfrac12)；\ \text{覆盖引理}＝N=3\ (\cos\tfrac{2\pi}4=0)✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{分级周期单调性引理（\text{以}\ N=\lfloor5(M+1)/P\rfloor\ \text{分级}）}：\text{旧}\ M\ \text{点共同周期}\ P \Longrightarrow$$
$$\qquad N\ge5\ (P\le M+1)：\max\ge M+\tfrac12；\quad N\ge3\ (P\le\tfrac{5(M+1)}3)：\max\ge M\ge m_M；$$
$$\qquad N\ge1\ (P\le5(M+1))\ \text{且}\ m_M\le M-1：\max\ge M-1\ge m_M✓✓$$
$$\textbf{(三)}\ ⭐⭐\ \textbf{极值配置}\ (60^\circ,90^\circ)\ \textbf{被覆盖}：P=\mathrm{lcm}(6,4)=12\le5(M+1)=15\ \text{取}\ N=1\ \text{级}✓✓$$
$$\qquad \text{数值核验}：\min_\psi\max_{k\le15}[\text{对}+\cos(k\psi)]=1.309017\ \ge\ \tfrac12=m_2✓✓$$
$$\textbf{(四)}\ \text{支撑引理}\ m_M\le M-1：M\ge12\ \text{由}\ \textbf{概率方法}（\text{三行}：\mathrm{Hoeffding}+ \text{并界}）；\ M\le11\ \text{由数值}✓✓$$

FREEZE-ACK: 本档即冻结期内的推导推进（依 `§8.1`；不产候选结论）

D0: 本档对象 = **鸽笼定理（`\kappa_N` 严格化并统一两引理）＋ 分级周期单调性引理 ＋ 极值配置覆盖 ＋ `m_M\le M-1` 的概率证明** —— 关系 = 推导推进，非新机制
D1: 0

# C-159 · ⭐⭐⭐ **鸽笼定理（`\kappa_N` 已证）＋ 分级周期引理 ＋ 极值配置被覆盖**

> **唐先生 2026-09-19 13:37**：能否放宽"公共周期"，用覆盖引理直接处理 `(60^\circ,90^\circ)`？✓

---

## §1 ⭐⭐ 鸽笼定理（`\kappa_N` 从推测升为**定理**）

$$\textbf{定理}：\forall\theta\in\mathbb R,\ \forall N\ge1:\qquad \max_{1\le m\le N}\ \cos(m\theta)\ \ge\ \cos\frac{2\pi}{N+1}✓✓$$
$$\textbf{证明}：\text{考虑}\ N+1\ \text{个数}\ \{0,\theta,2\theta,\dots,N\theta\}\pmod{2\pi}\subset[0,2\pi)✓$$
$$\qquad \text{由}\ \textbf{鸽笼原理}，\text{其中两个的距离}\ \le\tfrac{2\pi}{N+1}\ \text{（\text{抽屉长度}）}✓$$
$$\qquad \text{其差为}\ m\theta\ (1\le m\le N) \Longrightarrow \Big\|\tfrac{m\theta}{2\pi}\Big\|\le\tfrac1{N+1} \Longrightarrow m\theta\ \text{距}\ 2\pi\mathbb Z\ \le\ \tfrac{2\pi}{N+1}✓$$
$$\qquad \Longrightarrow\ \cos(m\theta)\ \ge\ \cos\tfrac{2\pi}{N+1}\qquad(\text{因}\ \tfrac{2\pi}{N+1}\le\pi\ \text{且}\ \cos\ \text{在}\ [0,\pi]\ \text{单减})✓\qquad\square$$
$$\textbf{最佳性}：\theta=\tfrac{2\pi}{N+1}\ \text{时}\ \max_m\cos\tfrac{2\pi m}{N+1}=\cos\tfrac{2\pi}{N+1}\ \textbf{恰好} \Longrightarrow \kappa_N=\cos\tfrac{2\pi}{N+1}✓✓$$
$$\textbf{统一}\ (\text{本档收获})：\begin{cases}N=5: &\cos\tfrac{2\pi}6=\tfrac12\quad(\textbf{引理 C})\\ N=3: &\cos\tfrac{2\pi}4=0\quad(\text{覆盖引理})\end{cases}✓✓$$
$$\qquad ⟹ \text{`C-158` 的两条引理＝同一定理的两特例}；\ \text{且}\ \text{均为}\ \textbf{初等鸽笼} \Longrightarrow \text{无文献风险}✓✓$$
$$\qquad (\text{唐先生所指 Fejér 方向：}\cos\tfrac{\pi}{n+1}\ \text{型常数家族}\ \textbf{同源}；\ \text{本档未找到逐字同陈述} \Longrightarrow \text{标}\ [\text{经典·结构}])✓$$

## §2 ⭐ 分级周期单调性引理

$$\text{设旧}\ M\ \text{点具共同周期}\ P（=\mathrm{lcm}\ \text{各点周期}），\ \text{窗口}\ [1,5(M+1)]\ \text{含}\ N=\lfloor\tfrac{5(M+1)}P\rfloor\ \text{个}\ P\ \text{的倍数}✓$$
$$\qquad \text{在这些}\ k=Pm\ \text{上：}\ \sum_{j\le M}\cos(k\varphi_j)=M \Longrightarrow \text{总和}=M+\cos(mP\psi)✓$$
$$\qquad \text{再用鸽笼定理（对}\ \theta=P\psi）：\ \max_{m\le N}\cos(mP\psi)\ \ge\ \cos\tfrac{2\pi}{N+1}✓✓$$
$$\begin{array}{c|c|l}
\text{级} & \text{条件} & \text{结论}\\\hline
N\ge5 & P\le M+1 & \max\ \ge\ M+\tfrac12\\
N\ge3 & P\le\tfrac{5(M+1)}3 & \max\ \ge\ M\ \ge\ m_M\ (\text{平凡界})\\
N\ge1 & P\le5(M+1) & \max\ \ge\ M-1\ \ge\ m_M\ \text{（需}\ m_M\le M-1\text{）}\\
\end{array}✓✓$$

## §3 ⭐⭐ 极值配置 `(60^\circ,90^\circ)` **被覆盖**（回答唐先生）

$$\varphi_1=60^\circ\ \text{周期}\ 6；\ \varphi_2=90^\circ\ \text{周期}\ 4 \Longrightarrow P=\mathrm{lcm}(6,4)=12✓$$
$$\qquad 12\le5(M+1)=15\ (M=2) \Longrightarrow \textbf{取}\ N=\lfloor15/12\rfloor=1\ \text{级}✓✓$$
$$\qquad \text{在}\ k=12：\text{对的贡献}=\cos(720^\circ)+\cos(1080^\circ)=1+1=2✓✓$$
$$\qquad \Longrightarrow \text{总和}=2+\cos(12\psi)\ \ge\ 1\ \ge\ \tfrac12=m_2✓✓$$
$$\text{数值核验}：\min_\psi\max_{k\le15}\big[\text{对}(k)+\cos(k\psi)\big]=1.309017\quad(\text{在}\ \psi=108^\circ)✓✓$$
$$\Longrightarrow \textbf{极值配置被弱形式（}N=1\ \text{级）覆盖}，\ \textbf{不需} \text{"}P\le\tfrac{5(M+1)}3\text{"}✓✓$$
$$\qquad (\text{唐先生"各点各自周期"的直觉}\ \textbf{正确}：\text{正确对象是}\ P=\mathrm{lcm}\ \text{（公共周期），\textbf{而非}最大周期})✓$$

## §4 支撑引理 `m_M\le M-1`（分级引理的唯一外部输入）

$$\textbf{概率方法（严格，三行）}：\text{取}\ \varphi_j\ \text{iid 均匀于}\ [0,\pi]；\ \mathbb E\cos(k\varphi_j)=0✓$$
$$\qquad \text{Hoeffding}：\mathbb P\Big(\big|\sum_j\cos(k\varphi_j)\big|\ge t\Big)\le2e^{-t^2/(2M)}；\ \text{并界}\ k\le5M：\ \le10Me^{-t^2/(2M)}✓$$
$$\qquad \text{取}\ t=\sqrt{2M\ln(10M)} \Longrightarrow \text{概率}<1 \Longrightarrow \exists\ \text{配置}：\max_k\big|\sum\big|\le t✓✓$$
$$\Longrightarrow\ \boxed{m_M\ \le\ \sqrt{2M\ln(10M)}}\qquad(\text{严格；}\ M\ge12\ \text{时}\ \le M-1)✓✓$$
$$\qquad M\le11：\text{用数值（}m_3=0.764,\dots,m_{11}=2.271\ \ll M-1）✓$$

## §5 仍未覆盖的部分（诚实）

$$\text{未覆盖}：P=\mathrm{lcm}>5(M+1)\ \text{的配置}（\textbf{无理配比} \text{／大分母有理配比}）✓$$
$$\qquad \text{此情形"倍数归位"不存在} \Longrightarrow \text{回到}\ \textbf{部分对齐} \text{问题}；\ \text{鸽笼定理对单点有效，对多点需新的联合论证}✓$$
$$\qquad ⚠️\ \text{故}\ \textbf{不能} \text{声称一般单调性}；\ \text{本档把}\ \text{"可覆盖类"} \text{从"小周期"扩到"}\mathrm{lcm}\le5(M+1)\text{"}✓✓$$

## §6 下一步

$$\text{①}\ \kappa_N\ \text{已证} \Longrightarrow \text{可考虑把"窗口}\ 5M\text{"换成}\ \text{"窗口}\ N\text{"的最优形式推广到多点}（\text{即}\ m_M\ \text{的下界问题}）✓$$
$$\text{②}\ \text{未覆盖类}：\text{或}\ \text{用概率方法}\ \text{给}\ \max\ \text{下界}（\text{多点}\ \text{Turán 型}）；\ \text{或}\ \text{Case A 型聚类归约}✓$$
$$\text{③}\ \text{文献：}\kappa_N\ \text{的逐字出处（Fejér／Chebyshev 型极值）；本档未找到}\ \Longrightarrow \text{标}\ [\text{经典·结构}]✓$$

## §7 边界与回查

- ⚠️ §1 的证明为**本档独立给出**（鸽笼，三行）；**最佳性**由 `\theta^*` 处取等核验 ✓
- ⚠️ §4 的概率方法为**严格**（Hoeffding＋并界），但**只给上界**（不涉及 `(RP_M)`）✓
- ⚠️ §3 数值为实算（网格 `400001`）✓；§5 边界明确 ✓
- ⚠️ **不声称**一般单调性；**不声称** `(\text{RP}_M)` 一般成立；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:5x）`[纪律]`（先跑后写）

```
技术词 鸽笼定理      命中文件数=0 ::  ⟹ 本档新增
技术词 分级周期引理   命中文件数=0 ::  ⟹ 本档新增
技术词 lcm门槛       命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
