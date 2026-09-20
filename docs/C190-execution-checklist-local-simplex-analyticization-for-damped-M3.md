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

---

## §6 Step 1 结果：候选精确化（按唐先生措辞修正：**不要求六值重叠**）

$$\text{候选（精确有理）}：r_1=1,\ r_2=\tfrac{79051}{10^5},\ r_3=\tfrac{83021}{10^5},\ \varphi_j/\pi\in\{10911,82066,46172\}/10^5✓$$
$$\begin{array}{c|r|r}
\nu & S_\nu\ \text{下界} & S_\nu\ \text{上界}\\\hline
3 & 0.3731108480 & 0.3731108480\\
1 & 0.3730984171 & 0.3730984171\\
5 & 0.3730946288 & 0.3730946288\\
4 & 0.3730910595 & 0.3730910595\\
15 & 0.3730847305 & 0.3730847305\\
2 & 0.3730721881 & 0.3730721881\\\hline
14\ (\text{第 7 名}) & 0.0934752273 & 0.0934752273
\end{array}✓$$
$$\Longrightarrow \textbf{active band}：\text{六值全落}\ [0.3730722,\ 0.3731108]\ \text{（宽}\ 3.9\times10^{-5}）✓$$
$$\qquad \max_{\nu\notin A}S_\nu\le0.093475✓\qquad \textbf{separation gap}=0.279597✓✓$$
$$\qquad \textbf{注}：\text{本档}\ \textbf{不主张} \text{六值解析相等}✗\（\text{候选只是有理构型，非已证精确极小点}）✓$$

## §7 Step 2 结果：正权重证书（唐先生版，与 covering 分离）

$$\textbf{① non-degeneracy（有理 λ）}：\lambda=\big(\tfrac{2001}{10^4},\tfrac{1785}{10^4},\tfrac{1655}{10^4},\tfrac{1948}{10^4},\tfrac{1119}{10^4},\tfrac{1492}{10^4}\big)✓$$
$$\qquad \sum\lambda=1\ \textbf{精确}✓；\qquad \lambda_{\min}=\tfrac{1119}{10^4}=0.1119>0✓✓\qquad（\text{分母}\ 10^6\ \text{版}：\lambda_{\min}=0.111860）✓$$
$$\textbf{② 残差（区间算术承担）}：\Big\|\sum_i\lambda_i g_i(x_\ast)\Big\|\le1.087\times10^{-3}✓\（\text{分母}\ 10^6\ \text{版}：\le1.467\times10^{-5}✓）$$
$$\textbf{③ covering constant（与 λ 无关，精确法）}：$$
$$\qquad \boxed{c=\min_{|u|=1}\max_{i\in A}\langle g_i,u\rangle=\mathbf{0.302091535}}✓✓$$
$$\qquad \text{方法}：c=\text{以 0 为心的最大内切球半径}=\min_{\text{支撑超平面}} \mathrm{dist}(0,H)✓\ \text{（5 维中面由 5 顶点张成，枚举}\ \binom{6}{5}=6\ \text{个）}✓$$
$$\qquad \text{六个支撑面距离}：0.302092,\ 0.343468,\ 0.459114,\ 0.480749,\ 0.570978,\ 0.960696✓⟹c=0.302092✓$$
$$\textbf{④ 区间传递}：\Delta_G\ll10^{-50}✓；|c(G)-c(G')|\le\max_i\|g_i-g_i'\|✓ \Longrightarrow c_{\text{exact}}>0✓✓$$

### ⚠️ 勘误：C-189 §3 的 $c=0.437928$ **过估** ✗（本档第 2 条自我更正）

$$\text{C-189}\ §3\ \text{报}\ c=0.437928\（4\times10^5\ \text{随机方向}）✗\qquad \text{真值}\ c=0.302091535✓$$
$$\text{采样序列（均为上界，单调下降趋近真值）}：N=4\times10^5\to0.437928;\ N=1.5\times10^6\to0.402910;\ N=8\times10^6\to0.355901✓$$
$$\Longrightarrow \textbf{原因}：\text{5 维球面随机采样收敛慢，}\textbf{采样 min 只是上界}✗；\text{改用}\ \textbf{精确 facet 法}✓$$
$$\Longrightarrow \text{结构性结论}\ \textbf{不变}（c>0\ ⟹\ \text{单纯形 ALIVE}✓）；\text{仅}\ \textbf{数值} \text{需更正}✗$$
$$\Longrightarrow \textbf{已向 C-189 追加勘误指针}✓（\text{保留原文，不静默改}）✓$$

## §8 Step 3 结果：非活跃频率隔离（硬门槛 #2）

$$\text{候选点严格间隙}=0.279597✓\qquad L_A=\max_{\mu\in A}\sup\|\nabla S_\mu\|=15.086✓\qquad L_{\max}^{\text{非活跃}}=14.118✓$$
$$\Longrightarrow \text{充分条件}\ \text{gap}>(L_A+L_{\max})\rho \Longrightarrow \rho<0.009574\ \text{rad}=\mathbf{0.5485°}✓✓$$
$$\qquad \Longrightarrow \boxed{\text{存在邻域}\ U\（\text{半径}\ge0.5485°）：\ \nu\notin A\Rightarrow S_\nu(x)<\max_{\mu\in A}S_\mu(x)}✓✓$$

## §9 Step 5 结果：$R$ 的重估（分块）

$$\begin{array}{c|r|r|r|c}
\nu & |\varphi\varphi|_{\max} & |r\varphi|_{\max} & |rr|_{\max} & \|\nabla^2S_\nu\|_2\\\hline
1 & 0.94 & 0.99 & 0.00 & 1.044\\
2 & 3.10 & 2.86 & 1.94 & 3.122\\
5 & 7.31 & 9.79 & 9.36 & 11.947\\
10 & 95.93 & 17.48 & 10.93 & 95.932\\
11 & 97.84 & 4.62 & 19.98 & 97.844\\
15 & 93.65 & 6.92 & 18.19 & 93.652\\
\end{array}✓$$
$$\Longrightarrow R_{\text{new}}=\sup_\nu\|\nabla^2S_\nu\|_2=\mathbf{97.844}\（\nu^\ast=11）\qquad \text{原粗界}\ 589.7 \Longrightarrow \textbf{改善}\ 6.03\times✓✓$$
$$\qquad \textbf{589 的来源}：\text{(i) 三项都按}\ |\cos|\le1\ \text{估；}\text{(ii) 完全未用阻尼衰减}\ r^\nu✗✗$$
$$\qquad \text{正确结构}：\nu=15\ \text{时}\ \varphi_1^2\ \text{项}\ =-93.65\（\text{单位模点无衰减}\Longrightarrow\text{主导}）✓；\varphi_2^2\ \text{仅}\ -3.72\（\text{被}\ r_2^{15}\ \text{压低}）✓$$
$$\qquad \text{且}\ \|\nabla^2S_\nu\|\ \text{在}\ \nu=11\ \text{达峰}\（\text{而非}\ \nu=15\），\text{因}\ \nu^2 r^\nu\ \text{在}\ \nu\approx 1/\log(1/r)\ \text{处平衡}✓$$

## §10 可审计对照表（唐先生指定格式）

$$\begin{array}{l|l|l}
\textbf{对象} & \textbf{原粗界} & \textbf{新严格界}\\\hline
S_\nu\ \text{active band（6 个）} & \approx0.37309 & [0.3730722,\ 0.3731108]\\
S_\nu\ \text{non-active} & — & \le0.093475\\
\text{separation gap} & — & \ge0.279597\\
\lambda_{\min} & 0.11186（\text{浮点}） & \ge\tfrac{1119}{10^4}\（\text{精确}）\\
\text{covering }c & 0.4379（\text{数值，过估}✗） & \ge0.302092\（\text{精确 facet}）\\
R & 589.7 & 97.844\\
\text{局部半径} & 0.0426° & 0.1769°\\
\end{array}✓$$
$$\qquad \textbf{局部半径}：|\delta|\le c/R=0.1769°✓（\text{保守}）；|\delta|\le2c/R=0.3538°✓$$
$$\qquad \textbf{拼接检查}：\text{局部半径}\ 0.1769°<0.3538°<\text{隔离半径}\ 0.5485°✓ \Longrightarrow \textbf{局部区 ⊂ 隔离区}✓✓$$

## §11 本档边界与纪律

- ⚠️ **原则（唐先生指定）**：**不得**把任何浮点优化输出直接升级为定理 ✓；所有最终门槛由**有理候选 ＋ 区间包络**承担 ✓✓
- ⚠️ §6 的 active band **不主张**六值解析相等 ✗（只主张落于窄带 ＋ 与其余分离 ✓）
- ⚠️ §7③ 的 $c$ 为**精确 facet 法**（枚举 6 个 5-子集 ✓），但**未做区间算术**（依赖 $G$ 的 60 位精度 ✓；$\Delta_G\ll10^{-50}$ ✓）
- ⚠️ §8 的 $L$ 用 $\sup$ 界（$|\sin|,|\cos|\le1$）⟹ 半径可再放大 ✓
- ⚠️ §9 的 $R$ 为**本点**的 Hessian 范数；邻域内 sup 需再取上界（下一步）✓
- **两条自我更正**：① 修正 §5 的 Hessian 装配索引 ✗；② 更正 C-189 §3 的 $c$ 过估 ✗✓
- **技术词回查勘误**：本节前文（C-190 初稿）若曾把 `执行清单` 记为 0 命中 ⟹ **勘误为 6 命中【沿用】** ✓（实测：`./IMPL-1-...md` 等 6 档）✓
- **未用** RH；**未改**他档正文（C-187/C-189 均以**勘误指针**追加 ✓）；**纪律**：先跑后写 ✓

---

## §12 Step 4 结果：局部二阶不等式（**本地闭合**，不含全局主张）

### §12.1 框架（唐先生给定 ＋ 符号审计）

$$x=x_\ast+\delta,\quad \forall\nu\in A：\ S_\nu(x)=S_\nu(x_\ast)+\langle g_\nu,\delta\rangle+\tfrac12\delta^{\mathsf T}H_\nu(\xi)\delta✓$$
$$\|H_\nu(\xi)\|_2\le R \Longrightarrow S_\nu(x)\ \ge\ S_\nu(x_\ast)+\langle g_\nu,\delta\rangle-\tfrac12R\|\delta\|^2✓$$
$$\text{又}\ \max_{\nu\in A}\langle g_\nu,\delta\rangle\ \ge\ c\|\delta\|✓\qquad \rho:=\|\delta\|✓$$
$$\Longrightarrow \boxed{F(x)\ \ge\ S_\ast+c\rho-\tfrac12R\rho^2}✓\qquad \text{正性条件}\ c\rho-\tfrac12R\rho^2>0\iff\boxed{\rho<\tfrac{2c}{R}}✓✓$$

### §12.2 $R$ 的定义澄清（唐先生要求区分两本账）

$$\begin{array}{c|r|r}
\rho\ (\text{rad}) & R_A=\sup_{\nu\in A,\,x\in B_\rho}\|H_\nu\|_F & R_{\text{all}}=\sup_{1\le\nu\le15,\,x\in B_\rho}\|H_\nu\|_F\\\hline
0.0030 & 124.655 & 124.655\\
0.0060 & 150.113 & 150.113\\
0.0096 & 176.902 & 176.902\\
\end{array}✓$$
$$\Longrightarrow \textbf{本例两本账相等}（\text{峰值由}\ \nu=11\in A\ \text{达到}）✓；\text{但计算已分开记账}✓✓$$
$$\qquad \text{注}：\text{此处用}\ \textbf{Frobenius} \text{上界（逐项区间最大值）}，\text{保守于谱范数}✓；\text{且含邻域放大}✓$$

### §12.3 固定点求解（两版并存，唐先生指定）

$$\text{标准版（余项}\ \tfrac12R\rho^2）：\rho\le\tfrac{2c}{R_A(\rho)} \Longrightarrow \rho=0.004412\ \text{rad}=\mathbf{0.2528°}，R_A=136.956✓$$
$$\text{超保守版（余项}\ R\rho^2）：\rho\le\tfrac{c}{R_A(\rho)} \Longrightarrow \rho=0.002512\ \text{rad}=\mathbf{0.1439°}，R_A=120.277✓$$
$$\qquad \textbf{两版均}\ <\ \text{隔离半径}\ 0.5485°✓ \Longrightarrow \textbf{Step 3 不是瓶颈}✓✓$$
$$\qquad \text{保留两版的理由（唐先生）}：\text{若后续 Hessian 范数转换再损失常数，证明仍有余量}✓$$

### §12.4 局部结论（**不得**升级为全局）

$$\text{因}\ \rho\le\tfrac{2c}{R}\ \Longrightarrow\ c\rho'-\tfrac12R(\rho')^2\ \text{在}\ [0,\rho]\ \text{上单调不减} \Longrightarrow \text{最小在}\ \rho'=0✓$$
$$\Longrightarrow \boxed{\forall x\in B_\rho(x_\ast)：\ F(x)\ \ge\ S_\ast=\mathbf{0.3730721881}}✓✓\qquad（S_\ast=\text{active band 严格下界}）✓$$
$$\qquad \text{该局部下界}\ \textbf{严格高于} \text{现有全局证书}\ 0.35✓✓$$
$$\qquad ⚠️\ \textbf{本步只覆盖}\ B_\rho(x_\ast)✓；\textbf{不声称}\ C_3\ge0.3731✗（\text{属 Step 7}）✓$$

### §12.5 数值自检（抽样，非证明）

$$\text{在}\ B_\rho\ \text{内随机抽 40000 点（三档}\ \rho）：\text{最小}\ F\ \text{均}\ \ge S_\ast，\textbf{违反数}=0✓✓$$

### §12.6 边界

- ⚠️ $R$ 用 Frobenius 上界（保守）✓；邻域放大用区间包络 ✓
- ⚠️ 局部球 $B_\rho$ 是 $(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)$ 空间的欧氏球（与 Step 3 隔离半径同度量 ✓）
- ⚠️ 本步**不**证明 $x_\ast$ 是极小点（只证附近 $F\ge S_\ast$ ✓）
- ⚠️ 抽样自检**不构成证明** ✓
- **Step 4 状态**：✅ **本地闭合**（严格局部二阶不等式 ＋ 两个半径版本 ＋ 自检）✓
- **下一步**：Step 6（把局部证书形式化）→ Step 7（远场覆盖，方得全局）✓

---

## §13 Step 7 结果：failure-cell inventory ＋ **全局目标抬升到 0.3730721881** ✓✓

### §13.1 第一刀：旧 0.35 证书的 weak-cell 清单（唐先生指定）

$$\text{以}\ T_0=0.35\ \text{为认证目标（旧证书 ✓），记录所有}\ \mathrm{LB}\in[T_0,T_1)\ \text{的格}，T_1=0.3730721881✓$$
$$\text{结果（1.4 s 完成）}：\text{评估}\ 338{,}930\ \text{盒}；\text{认证}\ 169{,}465；\mathcal W\ \text{弱格}\ 14{,}317✓$$
$$\frac{|\mathcal W|}{N}=\frac{14317}{169465}=8.45\%✓$$
$$\text{距离}\ d(C,x_\ast)：\min0.0097\ |\ q_{50}\mathbf{1.9205}\ |\ q_{90}2.93\ |\ q_{99}3.32\ |\ \max3.82✓$$
$$\textbf{★ 触及}\ B_\rho(x_\ast)\ \text{的弱格}=0/14317=\mathbf{0.0\%}✓✓$$
$$(r_2,r_3)\ \text{投影}：r\ge0.9\ \text{约}\ 32\!-\!34\%；\textbf{两坐标均}\ge0.9\ \text{仅}\ 11.2\%；\ r\ge0.99\ \textbf{为}\ 0.0\%✓$$

$$\Longrightarrow \textbf{诊断结论}：\text{弱区}\ \textbf{既不在}\ x_\ast\ \text{附近}，\textbf{也不沿}\ r\approx1\ \text{成片}✗$$
$$\qquad \text{而是全域匀布的 separability slack}\ ✓\ —— \text{既非情况 A 也非情况 B，而是情形 C}\ ✓$$
$$\qquad \Longrightarrow \text{局部技巧（Step 6）}\ \textbf{不能} \text{修掉这些弱格}✗；\text{但}\ \textbf{纯细分可以}✓（\text{下界随盒收缩收敛到真值}）✓$$

### §13.2 第二刀：直接在 T₁ 上做全局证书 —— **成功** ✓✓

$$\text{取}\ T_0=T_1=0.3730721881，\text{三个不同初始网格}：$$
$$\begin{array}{c|r|r|r|c}
N_0 & \text{评估盒数} & \text{终端格} & \text{弱格} & \text{未认证残留}\\\hline
10 & 634{,}012 & 317{,}006 & 0 & \mathbf{0}✓\\
14 & 1{,}509{,}602 & 754{,}801 & 0 & \mathbf{0}✓\\
18 & 4{,}496{,}462 & 2{,}248{,}231 & 0 & \mathbf{0}✓\\
\end{array}✓$$
$$\Longrightarrow \boxed{\text{阻尼}\ M=3：\ F(x)\ \ge\ 0.3730721881\ \ \text{对全部合法构型}}✓✓✓$$
$$\qquad \textbf{与旧}\ 0.38\ \text{任务失败一致}✓（0.38>\text{真极小}\ 0.3731108，\text{不可能成功}）✓$$

### §13.3 账本升级（重大）

$$\text{旧}：0.35\ \le\ C_3\ \le\ 0.3731108480\（\text{宽}\ 0.023\）✓$$
$$\textbf{新}：\boxed{0.3730721881\ \le\ C_3\ \le\ 0.3731108480}\qquad（\text{宽}\ \mathbf{3.9\times10^{-5}}，\text{收窄}\ \mathbf{590\times}）✓✓✓$$
$$\qquad \text{下界}：\text{本档计算机辅助证书（三网格一致 ✓）}\qquad \text{上界}：\text{C-189 §9 有理构型 ＋ 区间算术}✓$$

### §13.4 与 Step 1-6 的关系（诚实说明）

$$\textbf{Step 6 的局部证书}\ \textbf{不是} \text{得到 §13.2 的必要条件}✗\ \text{—— 全局目标靠}\ \textbf{纯细分} \text{就拿到了}✓$$
$$\qquad \text{原因}：\text{真极小}\ 0.3731108\ \text{高于目标}\ 0.3730722\ \text{仅}\ 3.9\times10^{-5}✓，\text{而盒下界随细分收敛到真值}✓$$
$$\qquad \text{局部球附近的格子}\ \textbf{早已被强认证}（\text{弱格触及}\ B_\rho=0✓）✓$$
$$\qquad \Longrightarrow \text{Step 1-6 仍作为}\ \textbf{独立局部引理} \text{保留}✓（\text{结构价值 ＋ 备用路线}）✓$$

### §13.5 边界与纪律

- ⚠️ 证书依赖**保守浮点参数** SLACK $=10^{-12}$／TEST\_EPS $=10^{-9}$（与 C-163/C-164/C-177 同族 ✓）；**区间算术版未做** ✗
- ⚠️ **单实现**（未做第二实现逐位交叉验证 ✗）
- ⚠️ 三网格（$N_0=10,14,18$）结论一致 ⟹ **稳健性证据** ✓
- ⚠️ §13.2 的**不是**解析证明；属**计算机辅助证书** ✓
- ⚠️ 本次修复两个实现 bug（`mincos` 的 π-命中判据 ✗；`inside_ball` 的坐标清零 ✗）—— 均由"结果过好/过坏"触发 ✓
- **未用** RH；**未改**他档 ✓
- ⚠️ 更高目标的推进（0.37310／0.373108／0.373110）**仍在运行** ✓

---

## §14 【等级归档 · 唐先生 2026-09-19 22:32】CA-1 标记 ＋ 两条方法论结论

### §14.1 当前正式账本

$$\boxed{0.3730721881\ \le\ C_3\ \le\ 0.3731108480}✓\qquad \Delta C_3\ \le\ 3.866\times10^{-5}✓$$
$$\qquad \text{相对旧的}\ 0.023\ \text{区间}：\textbf{缩窄约}\ 590\ \text{倍}✓✓$$

### §14.2 ⚠️ 证明等级：**CA-1（computer-assisted lower-bound certificate）**，**不是**无条件数学定理

$$\text{准确表述}：\boxed{\textbf{computer-assisted lower-bound certificate}}\qquad\textbf{不得} \text{写作"已完成严格解析证明"}✗$$
$$\text{三个 rigor gate（均未闭合）}：$$
$$\qquad \textbf{①}\ \text{区间算术版}：⏳（\text{本轮启动}）\qquad\qquad \textbf{②}\ \text{第二独立实现}：⏳$$
$$\qquad \textbf{③}\ \text{当前仍用}\ \texttt{SLACK}=10^{-12}、\texttt{TEST\_EPS}=10^{-9}\ \text{浮点参数}✓$$
$$\text{三网格（}N_0=10,14,18\text{）一致}\ = \ \textbf{robustness evidence}✓，\ \textbf{不能} \text{替代 ①②}✗$$

### §14.3 ⭐ 方法论结论（一）：**Step 7 不依赖 Step 6 即可闭合**

$$\textbf{原先判断}：\text{Step 7 必须靠"局部（Step 6）＋远场"拼接}✗ \Longrightarrow \textbf{该判断被数据修正}✓✓$$
$$\text{实际发生的}：\boxed{\text{separable LB 虽松，但通过足够细分仍能达到}\ 0.3730721881}✓✓$$
$$\qquad \text{证据}：\text{终端盒}\ 317{,}006\（N_0=10\text{）}\sim 2{,}248{,}231\（N_0=18\text{）}，\textbf{0 未认证}✓$$

### §14.4 ⭐ 方法论结论（二）：weak-cell 的**负面**结论（两条假设均被否掉）

$$\text{原怀疑}：\mathcal W\subset B_\rho(x_\ast)\ \text{或} \text{集中于}\ r_2,r_3\approx1\ \Longrightarrow \textbf{均被数据否定}✗✗$$
$$\qquad \#(\mathcal W\cap B_\rho)=0✓；\ \frac{|\mathcal W|}{N}=8.45\%✓；\ q_{50}(d)=1.92，\ q_{99}(d)=3.32✓$$
$$\qquad r\ge0.99\ \text{占比}\ \mathbf{0.0\%}✓；\text{两坐标均}\ge0.9\ \text{仅}\ 11.2\%✓$$
$$\Longrightarrow \textbf{弱区是全域匀布的分可性松弛}✓\ \text{—— 既非情况 A 也非情况 B，而是}\ \textbf{情形 C}✓$$
$$\qquad \Longrightarrow \text{局部技巧}\ \textbf{修不掉} \text{它}✗；\textbf{细分可以}✓✓\ \text{—— 值得单独归档}✓$$

### §14.5 审计优先级（唐先生指定）

$$\boxed{\text{Interval arithmetic}\ \to\ \text{independent implementation}\ \to\ \text{再推}\ 0.37310\to0.37311}✓$$
$$\text{理由}：\text{上下界已只差}\ 3.87\times10^{-5}✓；\text{在浮点 B\&B 上继续抬}\ T\ \text{只得到}\ \textbf{同等级的更窄数值证书}✗$$
$$\qquad \text{而先把}\ 0.3730721881\ \text{做成}\ \textbf{interval-certified ＋ 独立重实现} \Longrightarrow \textbf{可信度质变}✓✓$$

### §14.6 状态表（按唐先生格式）

$$\begin{array}{l|c}
\text{项目} & \text{状态}\\\hline
\text{上界}\ 0.3731108480 & ✅\ \text{interval}\\
\text{下界}\ 0.3730721881 & ✅\ \text{computer-assisted}\\
\text{三种}\ N_0 & ✅\ \text{一致}\\
\text{Step 6 局部引理} & ✅\ \text{独立成立}\\
\text{Step 7 全局证书} & ✅\ \text{当前阈值闭合}\\
\text{Interval B\&B} & ⏳\ \text{本轮启动}\\
\text{第二独立实现} & ⏳\\
0.37310+\ \text{下界} & ⏳\\
C_3\ \text{精确值} & ❌\ \text{尚不能声称}\\
\end{array}✓$$

---

## §15 严格化进展（唐先生指定顺序：interval → 第二实现 → 再抬 T）

### §15.1 gate ① 区间算术（第一版，旧网格）—— **通过** ✓

$$\text{P2 逐盒区间验证：验证盒}\ 317{,}006\ |\ \textbf{违反}\ 0\ |\ \text{最小严格余量}=\mathbf{2.834741\times10^{-10}}>0✓✓$$
$$\qquad \text{方法}：\text{P1 浮点 B\&B 生成终端盒清单（仅作组织装置）} \to \text{P2 每盒用}\ \texttt{mpmath.iv}\ \text{算严格下界}✓$$
$$\qquad \Longrightarrow \text{终端验证}\ \textbf{不再依赖}\ \texttt{SLACK}✗✓\ \text{（浮点参数仅影响铺砌，不影响每盒下界}✓\text{）}$$

### §15.2 ⚠️ 自查发现的缺口：φ 上界薄片（已修）

$$\text{第一版网格用}\ \texttt{float}(\pi)\ (\approx\pi-1.2\times10^{-16}) \Longrightarrow \text{漏掉}\ [\texttt{float}(\pi),\pi]\ \text{薄片}\ ✗$$
$$\text{修正}：\varphi\ \text{网格上界改取}\ \pi\ \text{的下一个可表浮点上界}\ \texttt{PI\_UP}=\texttt{nextafter}(\pi,+\infty)>\pi✓$$
$$\qquad \Longrightarrow [0,\texttt{PI\_UP}]\supseteq[0,\pi]✓\ \text{无薄片遗漏}✓；\text{修正版运行中（终端盒}\ 371{,}447，\sim22\ \text{分钟）}⏳$$

### §15.3 gate ② 第二独立实现 —— **通过（浮点层）** ✓

$$\text{实现 B：纯 Python、无 numpy、独立逻辑分支}；\text{实现 A：numpy 向量化}✓$$
$$\text{抽样}\ 20{,}000\ \text{终端盒比对}：\text{最大绝对差}=\mathbf{0.000e{+}00}✓；\text{中位差}=0✓$$
$$\qquad \text{对}\ T\ \text{的判定完全一致}=\textbf{True}✓✓ \Longrightarrow \text{向量化路径无 bug}✓$$
$$\qquad ⚠️ \text{区间路径（P2）目前仍是单实现}✗\ —— \text{待补抽样交叉验证}⏳$$

### §15.4 等级状态（更新）

$$\begin{array}{l|c|l}
\text{gate} & \text{状态} & \text{说明}\\\hline
\text{① 区间算术} & ⏳ & \text{第一版通过；修正版（补 φ 薄片）运行中}\\
\text{② 第二独立实现} & ✅（\text{浮点层}） & \text{逐位一致；区间层待补}\\
\text{③ 浮点参数} & ✅\ \text{已被取代} & \text{终端验证改由区间算术承担}\\
\end{array}✓$$
$$\text{账本不变}：\boxed{0.3730721881\ \le\ C_3\ \le\ 0.3731108480}✓$$

---

## §16 审计链归档（唐先生 2026-09-19 23:14 指令）＋ v3 终版设计

### §16.1 原则：**域覆盖先于余量**（本档第 3 条自我更正的重要教训）

$$\text{v1 最小严格余量仅}\ 2.834741\times10^{-10}✓\qquad \text{端点缺口宽度约}\ 10^{-16}✗$$
$$\textbf{但绝不能用"薄片很薄"来忽略}✗✗\ —— \text{因认证裕量本身只有}\ 10^{-10}\ \text{量级}✓$$
$$\qquad \Longrightarrow \text{必须坚持}\ \boxed{\textbf{domain coverage precedes margin}}✓✓$$

### §16.2 审计链（两条记录**不得混同**）

$$\begin{array}{c|l|l}
\text{版本} & \text{结果} & \text{状态}\\\hline
\text{v1（旧 φ 网格}\ \texttt{float}(\pi)\text{）} & 317{,}006\ \text{盒}；\text{违反}\ 0；\text{余量}\ 2.83\times10^{-10} & \mathbf{PRELIMINARY／SUPERSEDED}✗\\
\text{v3（φ 上界}\ \texttt{PI\_UP}>\pi\text{）} & \text{运行中} & \text{待}\ \text{Gate 1A/1B/2}\\
\end{array}✓$$
$$\qquad \textbf{纪律}：\text{v1}\ \textbf{只能} \text{作 preliminary}，\textbf{不得} \text{与修正版结果混在一起}✓✓$$

### §16.3 v3 终版（一次到位，含 3 个 Gate）

$$\textbf{Gate 1A——domain completeness}：\text{确认}\ r_2,r_3\in[0,1]、\varphi\in[0,\pi]\ \text{全部覆盖}✓$$
$$\qquad \text{做法}：\varphi\ \text{网格上界}\ \texttt{PI\_UP}=\texttt{nextafter}(\pi,+\infty)>\pi✓；\text{端点}\ 0.0/1.0\ \text{精确}✓$$
$$\qquad ⭐\ \textbf{精确铺砌体积校验}（\text{坐标皆二进制有理} \Longrightarrow \text{用}\ \texttt{Fraction}\ \text{精确比较}）：\sum\text{vol}(C)\ \overset{?}{=}\ 1\cdot1\cdot\texttt{PI\_UP}^3✓✓$$
$$\textbf{Gate 1B——interval positivity ＋ 最危险格固定}：\text{记录}\ \min_C\mathrm{LB}_{\rm IV}(C)>0✓$$
$$\qquad \text{并}\ \textbf{固定最小余量格}：\text{cell id ＋ 五维区间（lo/hi）}✓\ —— \text{后续所有复核针对此格}✓✓$$
$$\textbf{Gate 2——区间层双实现}：\text{同一批终端盒（含最危险格）上算}\ \mathrm{LB}_A^{\rm IV}\ \text{与}\ \mathrm{LB}_B^{\rm IV}✓$$
$$\qquad A：\texttt{mpmath.iv}\ \text{区间模块}✓\qquad B：\texttt{mpf}\ +\ \textbf{显式外向误差}\ \text{EPS}=10^{-50}✓（\text{独立机件}）✓$$
$$\qquad \text{记录}\ \max|\mathrm{LB}_A^{\rm IV}-\mathrm{LB}_B^{\rm IV}|✓✓$$

### §16.4 抬 T 阶梯（Gate ① 关闭后才进行）

$$0.37310\ \to\ 0.373108\ \to\ 0.373110\qquad（\text{注意}\ 0.373110<0.3731108480✓）$$
$$\qquad \text{若严格认证到}\ 0.373110 \Longrightarrow \text{上下界缩到}\ 8.48\times10^{-7}✓$$
$$\qquad ⚠️\ \textbf{不得} \text{把}\ 0.3731108480\ \text{写成"真值"}✗\ —— \text{它只是}\ \textbf{上界构型的数值}✓$$

### §16.5 最终账本格式（唐先生保留）

$$\boxed{0.3730721881\ \le\ C_3\ \le\ 0.3731108480}✓$$
$$\qquad \text{下界}：\text{修正版 interval B\&B 完成后正式锁定}⏳\qquad \text{上界}：\text{C-189 §9 合法有理构型 ＋ 区间算术}✓$$
$$\qquad \text{精确值}：\textbf{未声称}✗\qquad \text{路线}：\textbf{封实现漏洞}\to\textbf{双实现交叉}\to\textbf{再抬阈值}✓（\text{不再引入新数学机制}）✓$$

---

## §17 v3 终版结果：**四个硬点全部通过** ✓✓（2026-09-19 23:40）

$$\textbf{① 铺砌（domain coverage）}：\sum_C\mathrm{vol}(C)=1\cdot1\cdot\texttt{PI\_UP}^3\ \textbf{精确相等}✓✓$$
$$\qquad \text{用}\ \texttt{Fraction}\ \text{精确比较（坐标皆二进制有理，无浮点近似）} \Longrightarrow \textbf{无 overlap／无 gap}✓$$
$$\qquad \text{铺砌 sha256[:32]} = \texttt{75947683279fa46ff761bc95b3b4b900}✓$$
$$\textbf{② 严格正性（interval positivity）}：\text{验证盒}\ 371{,}447\ |\ \textbf{违反}\ 0\ |\ \min_C\mathrm{LB}^{\rm IV}_C=\mathbf{2.834729\times10^{-10}}>0✓✓$$
$$\qquad ⭐\ \textbf{最危险格已固定}：id=368400✓$$
$$\qquad \qquad lo=(0.8302978515625,\ 0.7905761718750002,\ 0.3427680070530466,\ 1.4505705825443598,\ 2.578161510199397)✓$$
$$\qquad \qquad hi=(0.830322265625,\ 0.7906250000000001,\ 0.3428063565727437,\ 1.450608932064057,\ 2.5781998597190943)✓$$
$$\textbf{③ 区间层双实现（cross implementation）}：\text{抽样}\ 2001\ \text{盒（含最危险格）}✓$$
$$\qquad A：\texttt{mpmath.iv}✓\qquad B：\texttt{mpf}+外向误差\ 10^{-50}✓（\text{独立机件}）$$
$$\qquad \max|\mathrm{LB}_A^{\rm IV}-\mathrm{LB}_B^{\rm IV}|=\mathbf{2.220\times10^{-16}}✓（\text{中位}\ 5.55\times10^{-17}）；\text{T-判定一致}=\textbf{True}✓✓$$
$$\textbf{④ 边界覆盖（mathematical domain）}：\texttt{PI\_UP}>\pi\ \text{于 60 位精度成立}✓（\text{差}\ 3.216\times10^{-16}）$$
$$\qquad r\ \text{端点精确}\ 0.0／1.0✓ \Longrightarrow [0,\texttt{PI\_UP}]^3\supseteq[0,\pi]^3✓ \Longrightarrow \textbf{证明的是数学域}\ [0,1]^2\times[0,\pi]^3✓✓$$

### §17.1 ⭐ 内部一致性核对（强证据）

$$\text{最危险格中心}：r_2\approx0.8303,\ r_3\approx0.7906,\ \varphi\approx(0.3428,\ 1.4506,\ 2.5782)✓$$
$$\text{对照}\ x_\ast：r_2=0.79051,\ r_3=0.83021,\ \varphi=(0.3428,\ 2.5782,\ 1.4506)✓$$
$$\Longrightarrow \textbf{最危险格恰为}\ x_\ast\ \textbf{的镜像}（r_2\leftrightarrow r_3,\ \varphi_2\leftrightarrow\varphi_3）✓✓\ —— \text{与问题固有对称性完全一致}✓✓$$

### §17.2 等级升级

$$\text{旧}：\text{CA-1}\ \text{preliminary（多网格 ＋ 初版区间验证，含}\ \varphi\ \text{薄片缺口}）✗$$
$$\textbf{新}：\boxed{\text{域完整（精确铺砌）＋ 区间认证 ＋ 双实现交叉验证的计算机辅助下界}}✓✓$$
$$\boxed{C_3\ \ge\ 0.3730721881}\qquad（\text{下界正式锁定}）✓✓$$

### §17.3 账本（唐先生保留格式）

$$\boxed{0.3730721881\ \le\ C_3\ \le\ 0.3731108480}\qquad（\text{宽}\ 3.866\times10^{-5}）✓$$
$$\qquad \text{下界}：\text{v3 区间证书}✓\qquad \text{上界}：\text{C-189 §9 合法有理构型 ＋ 区间算术}✓\qquad \text{精确值}：\textbf{未声称}✗$$

### §17.4 下一步（按唐先生阶梯，且不再改审计结构）

$$0.37310\ \to\ 0.373108\ \to\ 0.373110✓$$
$$\qquad ⚠️\ \text{最危险格余量仅}\ 2.83\times10^{-10}✓ \Longrightarrow \text{抬}\ T\ \text{会很快变得更贵}✓；\text{若成本爆炸，}\textbf{Step 6 局部支撑件} \text{已备}✓✓$$
$$\qquad \textbf{Step 6 保留}（\text{独立局部结构事实，非当前全局下界的必要条件}）✓$$

---

## §18 【勘误 · C-190】目标抬升量算错 10 倍（唐先生 2026-09-19 23:42 指出）

$$\text{原述}✗：T=0.37310\ \text{时目标只比最危险格现在的位置低}\ \sim2.8\times10^{-6}✗$$
$$\text{正确}✓：\ 0.37310-0.3730721881=\mathbf{2.78119\times10^{-5}}\（\text{即}\ 2.78\times10^{-5}，\text{差}\ \mathbf{10\ \text{倍}}）✓$$
$$\text{后果}：\text{新目标整体抬高}\ 2.78\times10^{-5}✓ \Longrightarrow \text{下一刀 B\&B 成本}\ \textbf{明显增加}✓（\text{而非微增}）✗$$

### §18.1 收口确认（唐先生 23:42 判定）

$$\boxed{C_3\ \ge\ 0.3730721881}✓\qquad \text{证书链四门全过（见 §17）}✓✓$$
$$\text{等级}：\text{CA-1 已从"数值计算证据"升级为}\ \textbf{可审计的区间计算机辅助证明}✓✓$$
$$\boxed{0.3730721881\ \le\ C_3\ \le\ 0.3731108480}\qquad（\text{宽}\ 3.866\times10^{-5}）✓$$

### §18.2 下一刀纪律（唐先生指定）

$$\boxed{T_2=0.37310}\qquad \text{保持已通过审计的}\ \textbf{v3 框架不变}，\textbf{只改 target}✓$$
$$\qquad \text{每个新}\ T\ \text{都必须形成}\ \textbf{独立 target certificate}✓，\ \textbf{不得} \text{当作"继续跑程序"}✗$$
$$\qquad \text{四门照旧}：\text{exact tiling}\to\text{strict interval positivity}\to\text{dual interval check}\to\text{boundary coverage}✓$$
$$\qquad \text{后续}：0.373108\to0.373110✓$$
$$\qquad ⚠️\ \textbf{不动} \text{Step 6／局部证书（本刀只改靶）}✓$$

---

## §19 P1 先导诊断：**纯 B&B 的成本天花板 ≈ T=0.37309**（2026-09-19 23:5x）

$$\text{方法}：\text{固定 v3 框架与}\ N_0=10，\text{仅扫描}\ T\ \text{对终端盒数的影响}✓$$
$$\begin{array}{c|r|r|r}
T & \text{终端盒数} & \text{总评估} & \text{P2 区间验证预估}\\\hline
0.3730721881\ (\text{基线}) & 371{,}447 & 742{,}894 & \sim21.7\ \text{分钟}✓\\
0.3730800000 & 374{,}637 & 749{,}274 & \sim21.9\ \text{分钟}✓\\
0.3730900000 & 385{,}832 & 771{,}664 & \sim22.5\ \text{分钟}✓\\
\mathbf{0.3730950000} & \textbf{未收敛}✗ & \text{爆炸}✗ & \textbf{不可行}✗✗\\
\end{array}✓$$
$$\Longrightarrow \textbf{关键结论}：\text{从}\ 0.37309\ \text{到}\ 0.373095，\text{成本}\ \textbf{突然爆炸}✗✗$$
$$\qquad \text{实测}：T=0.373095\ \text{运行}\ 3.5\ \text{分钟时 RSS 已达}\ \mathbf{3.9\ GB}\ \text{且未收敛}✗（\text{宿主仅}\ 7.86\ GB）$$
$$\qquad \text{原因}：\text{目标逼近真极小}\ 0.3731108\ \text{时，极小点邻域需}\ \textbf{极深细分}✗；\text{边界堆指数增长}✗$$

### §19.1 战略含义（已验证唐先生的预判 ✓）

$$\boxed{\text{纯 B\&B 路线在}\ T\approx0.37309\ \text{处见顶}}✗\qquad \text{若要}\ 0.37310+ \Longrightarrow \textbf{必须换路线}✓$$
$$\qquad \textbf{路线}\ α：\text{更紧的盒界}（\text{非可分／mixed-}\lambda，\text{C-170 测得 gap 改善}\ 7\!-\!17\times✓）$$
$$\qquad \textbf{路线}\ β：\textbf{Step 6 局部证书}（B_\rho\ \text{内已有}\ F\ge0.3730722✓）\ +\ \text{远场在}\ B_\rho\ \text{补集上做高靶证书}✓✓$$
$$\qquad \Longrightarrow ⭐\ \text{这正是唐先生让}\ \textbf{保留 Step 6} \text{的用处所在}✓✓\ —— \text{预判正确}✓$$

### §19.2 可立即执行的（便宜且合法）

$$\text{阶梯前两档}\ \textbf{仍在纯 B\&B 能力内}：0.37308\ ⟹\ 0.37309✓（\text{各}\ \sim22\ \text{分钟}）✓$$
$$\qquad \Longrightarrow \text{可先把下界从}\ 0.3730721881\ \text{抬到}\ \mathbf{0.37309}✓（\text{四门照旧}）✓$$
$$\qquad \text{而}\ 0.37310／0.373108／0.373110\ \text{需要}\ α\ \text{或}\ β✓$$

---

## §20 第二档 target certificate：**T=0.37309 四门全过** ✓✓（2026-09-20 00:10 完成）

$$\text{纪律（§18.2）}：\text{框架}\ \textbf{完全不动}（\text{v3}／N_0=10），\textbf{只改 target}✓\qquad \text{日志}：\texttt{/tmp/t2iv.log}✓$$

$$\textbf{① 铺砌}：\sum_C\mathrm{vol}(C)\overset{?}{=}1\cdot1\cdot\texttt{PI\_UP}^3\ \text{精确相等}=\textbf{True}✓\qquad \text{sha256[:32]}=\texttt{6195e20e3d77e520998d65fe62597021}✓$$
$$\qquad \text{终端盒}\ 385{,}832\（\text{总评估}\ 771{,}664）✓\qquad \texttt{PI\_UP}>\pi✓$$

$$\textbf{② 严格正性}：\text{验证盒}\ 385{,}832\ |\ \textbf{违反}\ 0\ |\ \min_C\mathrm{LB}^{\rm IV}_C=\mathbf{3.774862\times10^{-10}}>0✓✓$$
$$\qquad ⭐\ \textbf{最危险格}：\text{id}=384{,}376✓$$
$$\qquad \qquad lo=(0.7905197143554689,\ 0.8302108764648438,\ 0.3427799912779519,\ 2.5781950660291324,\ 1.4505346298696438)✓$$
$$\qquad \qquad hi=(0.7905212402343751,\ 0.83021240234375,\ 0.342782388122933,\ 2.578196264451623,\ 1.4505370267146247)✓$$

$$\textbf{③ 区间层双实现}：\text{抽样}\ 2001\ \text{盒（含最危险格）}✓$$
$$\qquad \max|\mathrm{LB}_A^{\rm IV}-\mathrm{LB}_B^{\rm IV}|=\mathbf{4.441\times10^{-16}}✓（\text{中位}\ 5.551\times10^{-17}）\qquad \text{T-判定一致}=\textbf{True}✓✓$$

### §20.1 内部一致性核对（对称性检查 ✓）

$$\text{最危险格中心}：r_2\approx0.79052,\ r_3\approx0.83021,\ \varphi\approx(0.3428,\ 2.5782,\ 1.4506)✓$$
$$\Longrightarrow \textbf{本档最危险格即}\ x_\ast\ \textbf{本体}✓\qquad \text{而基线档（§17.1）的最危险格是}\ x_\ast\ \textbf{的镜像}✓✓$$
$$\Longrightarrow \text{两档在}\ x_\ast\ \text{的两个对称拷贝上轮流取最危险格，与问题固有对称性完全一致}✓✓$$

### §20.2 账本更新

$$\text{旧}：0.3730721881\ \le\ C_3\ \le\ 0.3731108480\qquad（\text{宽}\ 3.866\times10^{-5}）$$
$$\boxed{\textbf{新}：0.3730900000\ \le\ C_3\ \le\ 0.3731108480}\qquad（\text{宽}\ \mathbf{2.0848\times10^{-5}}）✓✓$$
$$\qquad \text{下界}：\text{本档 target certificate}✓\qquad \text{上界}：\text{C-189 §9 构型 ＋ 区间算术}✓\qquad \text{精确值}：\textbf{未声称}✗$$
$$\qquad \text{宽度相对旧档收窄}\ \mathbf{46\%}✓（3.866\times10^{-5}\to2.085\times10^{-5}）$$

### §20.3 ⚠️ 工程记录（须修）

$$\text{本轮}\ v3\ \text{脚本把结果写死为}\ \texttt{/tmp/t1iv3\_result.json}✗ \Longrightarrow \textbf{基线档 JSON 已被本档覆盖}✗（\text{基线数值仅存于}\ \texttt{/tmp/t1iv3.log}✓）$$
$$\Longrightarrow \text{纪律修正：}\textbf{输出文件名必须按}\ T\ \text{命名}✓（\text{如}\ \texttt{t1iv\_T0.3730721881.json}）\Longrightarrow \text{每档独立证书方可长期审计}✓$$

---

## §20 β-2 五项输出 ＋ ⭐⭐ 账本级发现：**x\* 不是极小点**（2026-09-20 09:2x）

### §20.1 ⭐⭐ 关键发现：真极小点在别处（距 x\* 仅 1.25e-5）

$$F(x_\ast)=0.373110848000✓\qquad F(x_{\ast\ast})=\mathbf{0.373092052937}\ \color{red}{<}\ F(x_\ast)✗✗\qquad \|x_{\ast\ast}-x_\ast\|=1.247\times10^{-5}✓$$
$$x_{\ast\ast}=(r_2,r_3,\varphi/\pi)=(0.7905132461,\ 0.8302071370,\ 0.1091101624,\ 0.8206636560,\ 0.4617193264)✓$$
$$\Longrightarrow \textbf{此前所有优化器（DE／NM）都停在}\ x_\ast\ \text{这个非极小点}✗；\text{真极小在其}\ 1.25\times10^{-5}\ \text{邻域}✓$$

### §20.2 β-2 五项（按唐先生指定格式）

$$\textbf{①}\ H_\nu(x_\ast)\ \text{（5×5）谱：}\ \|H_\nu\|_2=1.04,\ 3.12,\ 6.10,\ 8.51,\ 11.95,\ \mathbf{93.65}\（\nu=15\ \text{主导}）✓$$
$$\textbf{②}\ \text{统一二阶常数}\ R=\max_\nu\|H_\nu\|_2=\mathbf{93.65}✓$$
$$\textbf{③}\ \text{三阶余项}\ M_\nu=7.1,\ 48.6,\ 140.8,\ 287.9,\ 488.0,\ \mathbf{4914.9}\qquad M_{\max}=4914.9✓$$
$$\textbf{④}\ \text{二阶模型球内最小}：\text{锚}\ x_\ast：\mathbf{0.373093055}\（\|\delta\|=1.39\times10^{-5}）；\text{锚}\ x_{\ast\ast}：\mathbf{0.373094931}\（\|\delta\|=4.01\times10^{-6}）✓$$
$$\textbf{⑤}\ LB_{\rm local}-T：$$
$$\begin{array}{c|r|r|c}
T & \text{锚}\ x_\ast（\text{毛值}） & \text{锚}\ x_{\ast\ast}（\text{毛值}） & \text{判定}\\\hline
0.37310 & -6.945\times10^{-6} & -5.069\times10^{-6} & ✗\ \textbf{FAIL}\\
0.37309 & +3.055\times10^{-6} & +4.931\times10^{-6} & ✅\\
0.3730925 & +5.553\times10^{-7} & +2.431\times10^{-6} & ✅\\
\end{array}✓$$

### §20.3 对 β 的解释（**不是界太弱，而是事实**）

$$\text{二阶模型的球内最小}\ 0.3730931\ \text{与真实下陷}\ 0.3730921\ \text{仅差}\ \sim10^{-6}✓⟹ \textbf{模型是准的}✓✓$$
$$\qquad \Longrightarrow T=0.37310\ \text{的门}\ \textbf{本来就不可能过}✗\ —— \text{因}\ x_\ast\ \text{附近真的有}\ F<0.37310\ \text{的点}✓✓$$
$$\qquad \Longrightarrow \text{二阶／三阶机制}\ \textbf{有效}✓；\text{只是靶子（0.37310）设得高于真极小（0.3730921）}✗$$

### §20.4 账本改进（立即生效）

$$\text{新上界}（\text{有理点＋区间算术}）：C_3\ \le\ \mathbf{0.373092075762}✓\qquad（\text{旧}\ 0.3731108480 ⟹ \text{改善}\ 1.877\times10^{-5}）✓$$
$$\boxed{0.3730900000\ \le\ C_3\ \le\ 0.373092075762}✓\qquad \text{宽度}=\mathbf{2.076\times10^{-6}}✓（\text{旧}\ 2.0848\times10^{-5} ⟹ \textbf{收窄}\ 10.0\times）✓✓$$

### §20.5 ⚠️ 对 §19 的解释修正

$$\text{§19 原述}✗：\text{纯 B\&B 的成本天花板} \approx0.37309\（\text{算力问题}）✗$$
$$\text{正确}✓：T=0.373095\ \textbf{本就不可能}✗\ —— \text{因真极小}\ 0.3730921<0.373095✓$$
$$\qquad \Longrightarrow \text{那次"爆炸"}\ \textbf{不是算力天花板}✗，\text{而是}\ \textbf{目标超过了真极小}✓✓\（\text{无任何算力可认证}）$$
$$\qquad \text{同时}\ 0.37309\ \text{的成功}\ \textbf{仍然有效}✓（\text{它低于真极小}✓）；\text{阶梯应改为}\ 0.373090\to0.3730915\to0.373092（\text{上限}\approx0.3730921）✓$$

### §20.6 下一步（最短信息量最高）

$$\textbf{①}\ \text{把下界从}\ 0.373090\ \text{推到}\ 0.3730915／0.373092（\text{纯 B\&B，现已知真极小位置，成本可控}）✓$$
$$\textbf{②}\ \text{β 局部分析}\ \textbf{重新以}\ x_{\ast\ast}\ \text{为中心}（\text{锚点／梯度／Hessian 全部重算}）✓，\text{并同时对镜像}\ \sigma x_{\ast\ast}\ ✓$$
$$\textbf{③}\ \text{局部球在}\ T\lesssim0.3730925\ \text{上可过}✓（\text{§20.2⑤}）；\text{远场再做补集证书}✓$$

---

## §21 ⚠️ 措辞更正（唐先生 2026-09-20 09:18）＋ 方法论更正 ＋ 三分法 ＋ 可达前沿

### §21.1 更正：上界合法，但"上限≈真极小"是**越界表述** ✗

$$\text{账本}\ C_3\le0.373092075762\ \textbf{本身合法}✓\ —— \text{上界只需}\ \textbf{一个合法构型}✓，\text{不要求它是极小点}✓$$
$$\qquad ⚠️\ \text{但我 §20 行文把它当成"真极小"✗} \Longrightarrow \textbf{越界}✗✗$$
$$\qquad \text{已证}：\text{"}x_{\ast\ast}\ \text{是目前}\ \textbf{找到的} \text{最深点"}\ ✓；\ \textbf{未证} \text{"}x_{\ast\ast}\ \text{是全局最小点"}\ ✗$$
$$\qquad \text{按唐先生逻辑}：\text{刚被}\ x_{\ast\ast}\ \text{教训过一次} \Longrightarrow \text{此刻更须警惕第三次}✓✓$$

### §21.2 ⭐ 方法论更正：证"没有更深的点"要用**证明**，不是搜索

$$\text{原建议（粗网格＋Lipschitz）}\ \textbf{在本问题无效}✗✗\qquad \text{实测}\ 12^5\ \text{网格（248,832 点）最小}=0.5434 \Longrightarrow \textbf{看不到下陷}✗$$
$$\qquad \text{原因}：\text{下陷盆地极窄（}\sim1\times10^{-5}✓） \Longrightarrow \text{任何粗网格必然漏掉}✗✗$$
$$\textbf{正确工具}：\text{把 v3 证书 B\&B 设在}\ T\ \textbf{略低于当前最优} \Longrightarrow \text{0 residual} \Longrightarrow \textbf{严格证明}\ F\ge T\ \text{处处成立}✓✓$$
$$\qquad \Longrightarrow \textbf{不存在比}\ T\ \text{更深的点}✓✓（\text{这是证明，不是启发式}）✓$$

### §21.3 三分法（把两种"爆炸"分开）

$$\begin{array}{l|l|l}
\text{情形} & \text{含义} & \text{例}\\\hline
T>\text{真极小} & \textbf{逻辑上不可能}✗（\text{无算力可认证}） & 0.37310,\ 0.373095\\
0.3730919\le T<\text{真极小} & \textbf{实用上不可行}✗（\text{分辨率墙}） & 0.3730919（\text{峰值 6.09M}）\\
T\le0.3730918 & \textbf{可达}✓（\text{廉价}） & 0.373090／0.3730915／0.3730918\\
\end{array}✓$$
$$\text{实测稳（}N_0=10\text{）}：0.3730915\to396{,}446✓；0.3730916\to398{,}770✓；0.3730917\to402{,}133✓；\mathbf{0.3730918\to409{,}171✓}；0.3730919\to\textbf{爆炸}✗$$

### §21.4 本刀产出

$$\textbf{可达前沿}\ T^\ast=0.3730918✓（409{,}171\ \text{盒，四门运行中}）$$
$$\text{若通过} \Longrightarrow \boxed{0.3730918\ \le\ C_3\ \le\ 0.373092075762}\qquad \text{宽度}\ \mathbf{2.758\times10^{-7}}✓（\text{再收窄}\ 7.5\times）✓✓$$
$$\qquad \textbf{且同时证明}\ F\ge0.3730918\ \text{处处成立} \Longrightarrow \textbf{不存在低于}\ 0.3730918\ \text{的点}✓✓$$
$$\qquad ⚠️\ \text{仍}\ \textbf{不能} \text{断言}\ C_3\ \text{精确值}✗（\text{真极小可能严格位于区间内部}✓）$$

---

## §22 第三档 target certificate：**T=0.3730918 四门全过** ✓✓（2026-09-20 09:46 完成）

$$\text{纪律（§18.2）}：\text{框架}\ \textbf{完全不动}（\text{v3}／N_0=10），\textbf{只改 target}✓\qquad \text{日志}：\texttt{cert\_appendix/iv-gates/t3iv\_T0.3730918.log}✓$$

$$\textbf{① 铺砌}：\sum_C\mathrm{vol}(C)\overset{?}{=}1\cdot1\cdot\texttt{PI\_UP}^3\ \text{精确相等}=\textbf{True}✓\qquad \text{sha256[:32]}=\texttt{0d69780a7d3b6374d0ddb13c81e5b8a5}✓$$
$$\qquad \text{终端盒}\ \mathbf{409{,}171}（\text{总评估}\ 818{,}342）✓\qquad \texttt{PI\_UP}=3.1415926535897936>\pi✓\qquad \text{无 float 偷换端点}✓$$

$$\textbf{② 严格正性}：\text{验证盒}\ 409{,}171\ |\ \textbf{违反}\ 0\ |\ \min_C\mathrm{LB}^{\rm IV}_C=\mathbf{4.573824652354119\times10^{-11}}>0✓✓$$
$$\qquad ⭐\ \textbf{最危险格}：\text{id}=\mathbf{379{,}970}✓\qquad \mathrm{LB}^{\rm IV}=0.373091800046✓$$
$$\qquad \qquad lo=(0.83021240234375,\ 0.7905334472656251,\ 0.34277759443297084,\ 1.4505322330246626,\ 2.5781710975793213)✓$$
$$\qquad \qquad hi=(0.8302185058593751,\ 0.79053955078125,\ 0.34278718181289514,\ 1.4505418204045868,\ 2.5781806849592455)✓$$

$$\textbf{③ 区间层双实现}：\text{抽样}\ \mathbf{2001}\ \text{盒（含最危险格）}✓$$
$$\qquad \max|\mathrm{LB}_A^{\rm IV}-\mathrm{LB}_B^{\rm IV}|=\mathbf{4.441\times10^{-16}}✓（\text{中位}\ 5.551\times10^{-17}）\qquad \text{T-判定一致}=\textbf{True}✓✓$$

$$\textbf{④ 内部一致性}：\text{最危险格中心}\ r_2\approx0.79053,\ r_3\approx0.83021,\ \varphi\approx(0.34278,\ 2.57818,\ 1.45054)✓$$
$$\qquad \text{与}\ §20.1\ \text{的}\ x_\ast\ \text{镜像一致}✓⟹ \text{本档取}\ x_\ast\ \text{的另一对称拷贝（两档在镜像对上轮流取最危险格）}✓✓$$

### §22.1 账本更新

$$\text{旧}：0.3730900000\ \le\ C_3\ \le\ 0.373092075762\qquad（\text{宽}\ 2.076\times10^{-6}）$$
$$\boxed{\mathbf{0.3730918}\ \le\ C_3\ \le\ \mathbf{0.373092075762}}\qquad（\text{宽}\ \mathbf{2.758\times10^{-7}}）✓✓$$
$$\qquad \text{宽度收窄}\ \mathbf{7.5\times}✓（2.076\times10^{-6}\to2.758\times10^{-7}）\qquad \text{下界}：\text{本档 target certificate}✓\qquad \text{上界}：\text{§20.4 有理构型}✓$$
$$\Longrightarrow \textbf{同时证明}\ F\ge0.3730918\ \text{处处成立}✓ \Longrightarrow \textbf{不存在低于}\ 0.3730918\ \text{的点}✓✓$$

### §22.2 三点注记（须随结论一并引用）

$$\textbf{① 稳健性}：\text{最小余量}\ 4.57\times10^{-11}\ \text{远大于双实现差异}\ 4.44\times10^{-16}\（\text{约}\ 10^5\ \text{倍}）\Longrightarrow \text{非数值噪声}✓✓$$
$$\textbf{② 截断合法}：\text{门}\ 1A/1B\ \text{取}\ K=15\ \text{的逐}\ k\ \text{下界再取}\max✓；\ \max_{k\le15}\le\sup_{k\ge1}✓ \Longrightarrow \text{截断只让证书}\ \textbf{更保守}✓，\text{不产生缺口}✓$$
$$\textbf{③ 仍不能断言精确值}✗：\text{真极小可能严格位于区间内部}✓\（\text{下界}\ 0.3730918\ \text{与目前最深已知点}\ 0.373092052937\ \text{相距}\ \approx2.5\times10^{-7}✓）$$

### §22.3 证书归档（修正 §20.3 的命名缺陷）

$$\text{新目录}\ \texttt{cert\_appendix/iv-gates/}✓\qquad \text{文件}：$$
$$\qquad \texttt{t1iv\_T0.3730918.json}✓（\text{本档 JSON}）\qquad \texttt{t3iv\_T0.3730918.log}✓（\text{本档原始日志}）$$
$$\qquad \texttt{t2iv\_T0.37309.log}✓（\text{第二档日志补归档}✓——\ \text{该档 JSON 已被覆盖丢失}✗，\text{仅日志可溯}✓）$$
$$\qquad ⚠️ \text{脚本仍把输出写死为}\ \texttt{/tmp/t1iv3\_result.json}✗ \Longrightarrow \textbf{仍待修}✓（\text{按}\ T\ \text{命名，见}\ §20.3）$$

---

## §22 ⭐⭐ T=0.3730918 四门全过 → **C₃ 本阶段封版**（2026-09-20 09:50）

### §22.1 四门结果

$$\textbf{Gate 1A}：\text{终端盒总体积}\ \textbf{精确相等}✓（\texttt{Fraction}，无 overlap／无 gap）✓$$
$$\textbf{Gate 1B}：\text{验证盒}\ \mathbf{409{,}171}\ |\ \textbf{违反}\ 0\ |\ \min_C\mathrm{LB}^{\rm IV}_C=\mathbf{4.573825\times10^{-11}}>0✓✓$$
$$\qquad \text{最危险格 id=379970}✓\qquad lo=(0.83021240234375,\ 0.7905334472656251,\ 0.34277759443297084,\ 1.4505322330246626,\ 2.5781710975793213)✓$$
$$\qquad \qquad\qquad hi=(0.8302185058593751,\ 0.79053955078125,\ 0.34278718181289514,\ 1.4505418204045868,\ 2.5781806849592455)✓$$
$$\textbf{Gate 2}：\text{区间层双实现（2001 盒含最危险格）}\ \max|\mathrm{LB}_A^{\rm IV}-\mathrm{LB}_B^{\rm IV}|=\mathbf{4.441\times10^{-16}}✓✓\ \text{T-判定一致}✓$$

### §22.2 ⭐ 内部一致性核对（第二次遇到，且这次更强）

$$\text{最危险格中心}\approx(0.8302155,\ 0.7905365,\ 0.3427824,\ 1.4505370,\ 2.5781759)✓$$
$$\text{对照}\ x_{\ast\ast}=(r_2{=}0.7905132461,\ r_3{=}0.8302071370,\ \varphi/\pi{=}0.1091101624,\ 0.8206636560,\ 0.4617193264)✓$$
$$\Longrightarrow \text{最危险格}\ \textbf{恰为}\ \sigma x_{\ast\ast}\（\text{镜像：}r_2\leftrightarrow r_3,\ \varphi_2\leftrightarrow\varphi_3\text{）}✓✓$$
$$\qquad \Longrightarrow \text{证书最难的格子}\ \textbf{正好落在最深已知点的对称像上}✓✓\ —— \text{与问题固有对称性完全一致}✓$$

### §22.3 ⭐⭐ 封版：**certified bracket asset**

$$\boxed{0.3730918\ \le\ C_3\ \le\ 0.373092075762}✓\qquad \text{宽度}=\mathbf{2.75762\times10^{-7}}✓✓$$
$$\text{下界}：\text{v3 四门证书（域完整＋区间认证＋双实现交叉）}✓\qquad \text{上界}：x_{\ast\ast}\ \text{构型＋区间算术}✓$$
$$\textbf{且本档同时证明}\ F\ge0.3730918\ \text{处处成立} \Longrightarrow \boxed{\textbf{不存在低于}\ 0.3730918\ \text{的点}}✓✓\（\textbf{证明}，非搜索）✓$$
$$\qquad ⚠️\ \text{仍}\ \textbf{不} \text{断言}\ C_3\ \text{精确值}✗（\text{真极小可能严格位于区间内部}✓）$$

### §22.4 决策规则（唐先生 2026-09-20 09:49 预先锁定，与结果无关）

$$\textbf{若四门通过}（\text{本轮情形}✓） \Longrightarrow \boxed{\text{C}_3\ \text{本阶段封版}}\ ✓\ \ \textbf{不} \text{立即冲}\ 0.3730919✗$$
$$\qquad \text{随后做}\ \textbf{总产出盘点 ＋ 优先级重排}✓（\text{见 §23}）$$
$$\textbf{若四门失败} \Longrightarrow \text{先判定失败类型}：\text{真违反／覆盖错／实现错／发现新的更深候选}✓$$
$$\qquad \text{只有第四种会改变数学对象}✓$$

### §22.5 为什么"不硬冲 0.3730919"（结构理由，非精度理由）

$$\text{关键}：0.3730919<0.373092052937 \Longrightarrow T=0.3730919\ \textbf{并非数学上不可能}✗，\text{只是}\ \textbf{当前实现的困难区}✓$$
$$\qquad \text{但成本已陡增}：4.09\times10^5\ \text{盒}\ \longrightarrow\ 6.09\times10^6\ \text{盒峰值}✗（\text{仅差}\ 10^{-7}\ \text{量级的目标}）✗$$
$$\Longrightarrow \text{再缩区间}\ \textbf{必须换机制}✓，\text{四条候选}：$$
$$\qquad \text{① 利用 active-set／KKT 结构（非逐盒独立排除）}✓$$
$$\qquad \text{② 把}\ x_{\ast\ast}\ \text{及其对称点附近的窄盆地}\ \textbf{解析化}✓$$
$$\qquad \text{③ 局部二／三阶严格下界 ＋ 全球 B\&B 只管外部}✓$$
$$\qquad \text{④ 找到比 separability 更强的联合约束}✓$$
$$\qquad \Longrightarrow \boxed{\text{不是继续加算力，而是提高每个盒子的"证明密度"}}✓✓$$
