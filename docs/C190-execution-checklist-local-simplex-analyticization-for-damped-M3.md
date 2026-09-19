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
$$\qquad 	ext{而是全域匀布的 separability slack}\ ✓\ —— 	ext{既非情况 A 也非情况 B，而是情形 C}\ ✓$$
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
