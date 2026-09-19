已查地图（**先查后写**）：`C-189`（乙-5：全 5 维单纯形签名 ＋ §9 严格上界）、`C-187`（乙三层审计，§3 需勘误）、`C-188`（fixed-λ NO-GO）、`C-152`/`C-154`（三件套模板）、`C-161`（单模单纯形签名）。关键词回查：`执行清单`=0、`正权重区间`=0、`非活跃隔离`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 22:07 指令）**：**落成 C-190 执行清单并开工**；顺序：先锁上界 → 再规范化 C-187 勘误与 ALIVE 状态 → 然后局部解析化 ✓
**本档性质**：**执行清单与状态规范化**（Step 0 已完成；Step 1-2 本轮开工）✓

FREEZE-ACK: 本档即冻结期内的执行清单与登记（依 `§8.1`；不产候选结论）

D0: 本档对象 = **C-190 执行清单（8 步）＋ 账本升级 ＋ C-187 §3 状态规范化** —— 关系 = 组织与状态更正，非新机制
D1: 0

# C-190 · 执行清单：阻尼 M=3 的局部单纯形解析化

---

## §1 执行顺序（唐先生指定）

| Step | 审计项 | 必须得到的东西 | 判定 |
|---|---|---|---|
| **0** | 上界归档 | 合法有理构型 ＋ 60 位区间算术 | ✅ **已完成**（`C-189` §9） |
| **1** | 候选精确化 | $x_\ast$、6 个 active $\nu$ 的区间隔离 | 本轮开工 |
| **2** | 六个正权重 | $\lambda_i\in[a_i,b_i]$，$a_i>0$（区间而非浮点） | **硬门槛** |
| **3** | 非活跃频率控制 | 对全部 $\nu\notin A$，邻域内 $S_\nu<\max_{\mu\in A}S_\mu$ | **硬门槛**（**必须早于 Step 4**） |
| **4** | 局部二阶控制 | active-set 的 Hessian／二阶余量严格下界 | **核心** |
| **5** | 重估 $R$ | 去掉粗界 $R\approx590$，给出可用局部半径 | **关键瓶颈** |
| **6** | 局部证书 | 严格的 $C_3\ \ge\ 0.3731108-\varepsilon$ 型下界 | 目标 |
| **7** | 远场覆盖 | 局部邻域外统一推出足够下界 | 最终闭合 |

$$\textbf{Step 3 必须早于 Step 4}：\text{只有先证邻域内参与}\ \max\ \text{的确实是那 6 个频率，才能合法写} F(x)=\max_{\nu\in A}S_\nu(x)✓$$

## §2 账本升级（正式）

$$\boxed{0.35\ \le\ C_3\ \le\ \mathbf{0.3731108480}}✓✓\qquad（\text{上界已为}\ \textbf{严格}：\text{合法精确有理构型 ＋ 区间算术}）✓$$
$$\qquad r_1=1,\quad r_2=\tfrac{79051}{10^5},\quad r_3=\tfrac{83021}{10^5},\quad \varphi_j/\pi\in\{10911,82066,46172\}/10^5✓$$
$$\qquad \text{附}：S_{14}\le0.0935\ \text{而 active envelope}\approx0.3731 \Longrightarrow \textbf{频率间隔}\ 0.2796✓\（\text{对 Step 3 极有利}）$$

## §3 C-187 §3 状态规范化（保留原档，仅追加指针）

$$\boxed{\text{C-187}\ §3：\ \textbf{REVOKED}}✓\qquad \boxed{\text{阻尼局部 simplex mechanism：}\ \textbf{ALIVE}（\text{数值层}）}✓$$
$$\text{限定（必须附）}：\text{ALIVE}\ \text{指}\ \textbf{五维全空间} \text{中的数值结构已满足项目既有 simplex-signature 判据；}\textbf{尚未等同于解析定理}✓$$
$$\qquad \text{原判定错误原因}：\text{在}\ \textbf{3 维}\ \varphi\ \text{子空间} \text{检验（活跃数 2 < 3+1）}✗$$
$$\qquad \textbf{纪律}：\text{保留}\ \text{C-187}\ \text{原文，}\textbf{只追加 correction pointer}，\textbf{不静默改历史判定}✓✓$$

## §4 三个硬门槛（C-190 的核心，不能被 $c=0.4379$ 带偏）

$$\textbf{① 正权重区间}：\text{不是}\ \lambda_i>0\（\text{浮点}）\text{，而是}\ \boxed{\lambda_i\in[a_i,b_i],\ a_i>0}✓\ \text{并给出}\ \lambda_{\min}=\min_i a_i✓$$
$$\textbf{② active／non-active 隔离}：\text{证存在邻域}\ U\ \text{使}\ \nu\notin A\Rightarrow S_\nu(x)<\max_{\mu\in A}S_\mu(x)\ (x\in U)✓$$
$$\qquad \text{否则"六面单纯形"只是}\ \textbf{候选点上的现象}✗$$
$$\textbf{③ }R\ \textbf{必须重新定义}：\text{当前}\ \rho_{\text{local}}\approx c/R\ \text{被}\ R\approx590\ \text{压到}\ 0.0426°✗$$
$$\qquad \text{必须明确}\ R\ \text{是}：\sup_{x\in U}\|\nabla^2S_\nu(x)\|\ ／\ \text{一阶 Lipschitz 常数}\ ／\ \text{三阶余量界}\ ／\ \text{active-envelope 的 Hessian 界}✓$$
$$\qquad \text{然后}\ \textbf{逐项找出}\ 590\ \text{来自哪里}✓\ ——\ \text{这很可能是 C-190 最有价值的技术工作}✓✓$$

## §5 本档边界

- ⚠️ 本档为**清单与状态规范化**；Step 1-2 的具体计算见本档后续小节（本轮追加）✓
- ⚠️ §3 的 ALIVE **仅指数值层**（不含解析定理）✓
- **未用** RH；**未改** C-187 正文（仅追加指针）✓
