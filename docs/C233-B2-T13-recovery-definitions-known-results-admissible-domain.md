已查地图（**先查后写**）：查三张主图（`CLOSED-ROUTES-MAP.md`／`MASTER-STATUS-AND-CLOSURES.md`／`MASTER-NOGO-AND-LIVE-PATHS.md`）—— **无 Cassels／T13／weighted 条目** ✗ ⟹ 按协议属**未覆盖** ✓；查 `C193`（w=1 等号集＋w 表）、`C199`（w=2 定理）、`C200`（w=2 等号集）、`TARGETS`（T13 原始描述）、`MASTER-LEDGER-RELATED-LEMMAS-CONJECTURES`（L5/L6/L7 待核）。回查见 §7 ✓

D0: 本档对象 = **B2/T13 开工前的定义／已知结果／精确可行域／Cassels 型结构回收**（不做数值扫描）—— 关系 = 回收与规格化，非新机制
D1: 0
FREEZE-ACK: 本档即冻结期内的回收与规格化（依 §8.1；不产候选结论）

---

## §0 回收结论（先行）

$$\boxed{\text{本档即【定义与文献边界锁定}】✓：\text{不做 }g_w\ \text{数值扫描}✗；\text{工作对象固定为 }g_w:=g_w(10)✓}$$
$$\boxed{\textbf{审计（唐先生 2026-09-20 18:49 指定）}✓✓：\text{不得把古典的权重结构与 }g_w\ \text{说成同一对象}✗}$$

## §1 定义（逐字）

### 1.1 我方定义（T13-B，`C-193` §2）

$$\boxed{\ g_w(N)\ :=\ \inf_{\varphi_1,\varphi_2}\ \max_{1\le k\le N}\ \bigl[\ w\cos(k\varphi_1)+\cos(k\varphi_2)\ \bigr]\ }✓,\qquad w\ge1✓,\ (\varphi_1,\varphi_2)\in[0,\pi]^2✓$$

$$\text{来历}：M=2\ \text{的阻尼/加权 (RP}_M\text{) 版}✓：Z_k:=[w\cos k\varphi_1+\cos k\varphi_2]✓\ \text{即两点幂和}\ \operatorname{Re}\sum_j b_j z_j^k✓\ \text{于}\ b=(w,1)✓,\ |z_1|=|z_2|=1✓$$

$$\boxed{\textbf{工作对象的固定}✓（唐先生 18:49）：g_w\ :=g_w(10)✓✓\ \text{（}N=5M=10\ \text{固定}✓）}$$
$$\qquad \textbf{理由}✓：\text{继承 }N=5M\ (M=2)✓\ \text{与已证的 }g_1(10)=\tfrac12✓,\ g_2(10)=1✓$$
$$\qquad \textbf{反面}✗：\text{若让 }N\ \text{随 }w\ \text{漂移}✓，\text{则最后不知在研【权重依赖】还是【窗口依赖}】✗$$
$$\qquad \Longrightarrow \textbf{第一阶段只问}：\text{固定 }N=10✓,\ w\mapsto g_w(10)\ \text{是否存在【可证明的结构}】✓$$

### 1.2 古典 Turán–Cassels 家族（**逐字**，外搜所得 ✓）

$$\textbf{Turán 第一主定理}✓（\text{Kerr 讲义}✓，[外搜·待逐字核原文]）：$$
$$\qquad \text{设}\ b_1,\dots,b_n,z_1,\dots,z_n\in\mathbb C✓,\ |z_i|\ge1✓,\ m\in\mathbb Z✓,\ \text{则}$$
$$\qquad \max_{m+1\le\ell\le m+n}\Bigl|\sum_{i=1}^n b_i z_i^{\ell}\Bigr|\ \ge\ \Bigl(\frac{n}{2e(m+n)}\Bigr)^{n}\ \Bigl|\sum_{i=1}^n b_i\Bigr|✓$$
$$\textbf{Turán 第二主定理}✓（\text{同上}✓）：\text{设}\ \max_i|z_i|=1✓,\ \text{则}$$
$$\qquad \max_{m+1\le\ell\le m+n}\Bigl|\sum_{i=1}^n b_i z_i^{\ell}\Bigr|\ \ge\ \Bigl(\frac{n}{8e(m+n)}\Bigr)^{n}\ \min_{k}\Bigl|\sum_{i=1}^k b_i\Bigr|✓$$
$$\textbf{Cassels 1941}✓：\text{J. W. S. Cassels, }\textit{On the sums of powers of complex numbers},\ \textbf{Acta Math.}✓（\text{定位可靠}✓；\text{具体陈述待读原文}⚠️）$$
$$\textbf{Andersson 精化}✓（\text{学位论文}✓，[外搜]）：|z_1|\ge\cdots\ge|z_n|✓\ \text{时}$$
$$\qquad \max_{m+1\le v\le m+n}\Bigl|\sum b_k z_k^v\Bigr|\ \ge\ 1.007\Bigl(\frac{n}{4e(m+n)}\Bigr)^{n}\ \min_{k}\Bigl|\sum_{i\le k}b_i\Bigr|✓\qquad（\text{常数}\ 1.007\ \text{与分母}\ 4e\ \text{双双优于 Turán}✓）$$
$$\textbf{Montgomery}✓（\text{Ten Lectures, Ch.5 Thm 11}✓）＋\textbf{Palojärvi}✓（\text{arXiv:1807.01506 Lemma 2.2 / Thm 4.1}✓）：|z_j|=1✓\ \text{时}\ \max_{1\le k\le5M}\operatorname{Re}\sum z_j^k\ge\tfrac1{20}✓$$

### 1.3 ⭐ 两族的**形状差异**（关键 ✓）

$$\textbf{古典}：\text{窗口}=n✓（\text{与点数同阶}✓），\text{常数}=\bigl(\tfrac{n}{2e(m+n)}\bigr)^n✓\ \textbf{指数小}✗；\text{权重}\ b\ \text{进入【泛函}】✓（|\sum b_i|\ \text{或}\ \min_k|\sum_{i\le k}b_i|✓）$$
$$\textbf{我方}：\text{窗口}=5M✓\ \textbf{线性}✓，\text{常数}=\tfrac12✓\ \textbf{多项式}✓；\text{权重}\ w\ \text{进入【被极值化的值本身}】✓$$
$$\Longrightarrow \text{两族在【窗口 regime ＋常数量级 ＋权重位置】三处都不同}✗（\text{与}\ \texttt{RP-M-LITERATURE-POSITIONING}\ \text{的窗口-谱系图一致}✓）$$

## §2 已知结果（我方）

| # | 结果 | 强度 | 出处 |
|---|---|---|---|
| R1 | $g_1(10)=\tfrac12$，等号集 $=\{\pi/3,\pi/2\}$（两点） | **定理** ✓✓ | `C-193`（§1，T13-A） |
| R2 | $g_2(10)=1$，等号集 $=\{(0,\pi/2)\}$ 中心（**单点**） | **定理** ✓✓ | `C-199` ＋ `C-200` |
| R3 | $w=1.2,1.5,2,3,5$ 的 $g_w(10)$ 数值 | 数值 ✗ | `C-193` §2（表） |

$$\textbf{R4}（\textbf{双边边界结果}✓✓，唐先生 18:49 指定为正式结论 ✓）：w\kappa_{10}-1\ \le\ g_w(10)\ \le\ w\kappa_{10}+1✓\ \Longrightarrow\ \boxed{\Bigl|\frac{g_w(10)}{w}-\kappa_{10}\Bigr|\le\frac1w}✓✓$$
$$\qquad \text{下界证}✓：\text{取 }k^*=\arg\max_k\cos k\varphi_1\ \text{（不依赖 }w✓） \Longrightarrow \max_k[\cdots]\ge w\max_k\cos k\varphi_1-1\ge w\kappa_{10}-1✓$$
$$\qquad \textbf{上界证}✓（本档新增 ✓）：\text{取 }\varphi_1=\theta_1^*\ \text{（单点最优}✓，\max_k\cos k\theta_1^*=\kappa_{10}✓）\text{与}\ \varphi_2=0✓ \Longrightarrow g_w\le w\kappa_{10}+1✓$$
$$\qquad \Longrightarrow \boxed{g_w(10)=w\kappa_{10}+O(1)}✓✓\qquad（w\to\infty✓）$$
$$\qquad \textbf{与数值的差别}✓：\text{实测 }w=5：3.2468\ \text{vs}\ w\kappa_{10}-1=3.2065✓（\text{差}0.040✓）；\text{但}\ \boxed{g_w\stackrel{?}{=}w\kappa_{10}-1+\cdots}\ \textbf{不得写成猜想-定理}✗✓$$
$$\qquad \textbf{真正该做}✓：\text{分析 leading-order active set}\ \{k_1,k_{10}\}\ \text{在 }w\to\infty\ \text{的控制下}✓，\text{第二相位能否在 active constraints 上产生【可精确计算的 }O(1)\ \text{修正}】✓✓$$

$$\textbf{R3 的关键读数}✓：g_w/w=0.500\to0.482\to0.417\to0.500\to0.600\to0.649✓（w=1,1.2,1.5,2,3,5✓）$$
$$\qquad \Longrightarrow \textbf{非单调}✗，w\approx1.5\ \text{处有极小}✓，\text{最优构型在}\ w\in(1.2,1.5)\ \text{与}\ (1.5,2)\ \text{之间切换}✓（\text{两个相变点}✓）$$
$$\qquad w=2\ \text{回到精确整数}\ 1.000000✓（\text{构型回到}\ (\pi/3,\pi/2)✓） \Longrightarrow \text{存在【整数/代数特值点}】✓$$

## §3 ⭐ 精确可行域（三个可选约定 —— 必须先定 ✓）

$$\text{定义}\ g_w(N)\ \text{有【一个自由约定}】\text{：窗口}\ N\ \text{与}\ w\ \text{的关系}✓$$

| 约定 | $N$ 的取法 | 特点 | 谁在用 |
|---|---|---|---|
| **甲** | $N=5M$ **固定**（$M=2\Rightarrow N=10$） | 与 (RP_M) 一致 ✓；$g_1(10)=\tfrac12$ 直接对接 R1 ✓ | 我方 `C-193`/`C-199` ✓ |
| 乙 | $N=N(w)$ 随 $w$ 优化 | 得 $w$-族的"最优点"✓；与古典族的 window-flexible 形式同型 ✓ | 古典 Turán 族 ✓ |
| 丙 | $N\to\infty$ 的极限 | 可能是 $w\kappa_\infty$ 型发散 ✓（$\kappa_N\to1$）✗ | — |

$$\Longrightarrow \textbf{建议锁定【甲】}✓（\text{与既有两条定理衔接}✓；\text{并显式声明}：\text{本约定下}\ N=10\ \text{固定}✓）$$
$$\text{其余可行域}：\varphi\in[0,\pi]^2✓（\cos\ \text{偶＋周期}\Longrightarrow\text{基本域}✓）；w\ge1✓；\text{无其它约束}✓$$

## §4 Cassels 型结构（我们这一支的准确形状）

$$\textbf{古典 Cassels 型的形状}✓：\text{权重}\ (b_i)\ \text{与}\ (z_i)\ \text{分离}✓：\text{结论}=F(b)\cdot G(n,m)✓,\ \text{其中}\ F(b)\ \text{是【权重的泛函}】✓\（|\sum b_i|✓,\ \min_k|\sum_{i\le k}b_i|✓）$$
$$\textbf{我方的形状}✗：\text{当}\ M=2✓\ \text{时}，b=(w,1)✓\ \text{且}\ |z_j|=1✓ \Longrightarrow \text{古典【第二主定理】的设定}✓（\max_i|z_i|=1✓）$$
$$\qquad \text{但窗口不是}\ n=2✗\ \text{而是}\ N=10✓ \Longrightarrow \text{古典界}\ \bigl(\tfrac{2}{8e(\cdot)}\bigr)^2✓\ \text{在此 regime 完全无用}✗（\text{量级}10^{-3}\ \text{级}✗）$$
$$\Longrightarrow \textbf{我方 = 古典家族在【短线性窗＋实部】下的【最优常数}】问题✓ —— 即：\text{古典给指数小下界}✓，\text{我方问同族的【sharp}】值✓$$

$$\boxed{\textbf{审计条款}✓✓（唐先生 18:49）：\text{Turán--Cassels 的 weighted coefficient functional}\ \neq\ \text{T13-B 的 weighted minimax value}✓✓}$$
$$\qquad \text{古典}：\max_{m+1\le v\le m+n}\Bigl|\sum_j b_jz_j^v\Bigr|\ \ge\ C(n,m)\,\mathcal B(b_1,\dots,b_n)✓\ \text{——}\ b_j\ \text{进入【右侧泛函}】✓$$
$$\qquad \text{我方}：w\cos(k\varphi_1)+\cos(k\varphi_2)=\operatorname{Re}\bigl(we^{ik\varphi_1}+e^{ik\varphi_2}\bigr)✓\ \text{——}\ w\ \text{直接进入【被取 max 的值}】✓$$
$$\qquad \Longrightarrow \textbf{准确定位}✓：\text{同属 weighted exponential-sum / power-sum 【家族}】✓，\text{但 【minimax functional 不同}】✗✓$$
$$\qquad \text{⚠️ 这也正是 B2/T13 值得继续切的地方}✓；\text{否则只是经典结果的重新参数化}✗$$

## §5 ⭐ 开口清单 ＋ 候选机制（不在此做数值扫描 ✓）

$$\textbf{Q1}（常数的闭式）✓：\exists\ \text{闭式}\ g_w(10)\ \forall w\ge1\ ✓？\text{已知}：w=1\Rightarrow\tfrac12✓,\ w=2\Rightarrow1✓（\text{两端精确}✓）$$
$$\textbf{Q2}（相变点）✓：\text{最优构型切换的}\ w\ \text{阈值是否代数数}✓？\text{数值显示两个阈值落在}\ (1.2,1.5),\ (1.5,2)✓$$
$$\textbf{Q3}（大 }w\text{ 渐近）✓：g_w=w\kappa_{10}-1+o(1)✓？R4\ \text{只给}\ \gtrsim✓；w=5：3.2065\ \text{vs}\ 3.2468✓（\text{差}\ 0.040✓，\text{第二点的正贡献}✓）$$
$$\textbf{Q4}（等号集随 }w\text{ 的演化）✓：w=1\ \text{两点}✓\to w=2\ \text{单点}✓；\text{中间}\ w\ \text{如何}✓？\text{是否在阈值处【跳变}】✓$$
$$\textbf{Q5}（一般 }M\text{ 与一般权重）✓：b=(w_1,\dots,w_M)✓\ \text{的最优常数与等号集}✓（\text{T13 原始形式}✓）$$
$$\textbf{Q6}（与古典泛函的关系）✓：\text{古典的}\ \min_k|\sum_{i\le k}b_i|\ \text{型泛函}\ \text{在短窗 regime 对应何物}✓？$$

$$\textbf{候选机制（按可证性排序}✓，\text{供唐先生选一刀}✓\text{）}：$$
$$\textbf{(a) 固定窗加权 minimax}✓\to\textbf{w 方向的 active-set 相变}✓\to\textbf{精确 }g_w(10)✓✓\ \textbf{（推荐，唐先生 18:49 锁定}✓）$$
$$\qquad \text{工作命名}：\textbf{B2-1}✓：\text{固定 }N=10✓，\text{建立 }g_w\ \text{的解析结构与三个 regime}✓$$
$$\qquad \text{已知锚点}：w=1\Rightarrow\tfrac12✓；w=2\Rightarrow1✓；w\to\infty\Rightarrow g_w=w\cos\tfrac{2\pi}{11}+O(1)✓$$
$$\qquad \text{待检假设}✓：\exists\ \text{有限个【active-set 相变点}】\ 1=w_0<w_1<\cdots<w_r<\infty✓\ \text{使 }g_w\ \text{在各区间由【不同有限约束系统】控制}✓$$
$$\qquad \text{若可证此 piecewise-KKT 结构并获得某非平凡区间的精确公式} \Longrightarrow \textbf{真正的 B2/T13 新内容}✓✓$$
$$\qquad \textbf{禁止}✗：\text{先跑 }w=1.01,1.02,\dots\ \text{的扫描}✗（\text{唐先生 18:49 明令}✓）$$
$$\textbf{(b) 相变点定位}✓：\text{把}\ g_w\ \text{写成关于}\ w\ \text{的分段函数}✓\ \text{并定位阈值}✓（\text{需一阶 KKT 参数化}✓）$$
$$\textbf{(c) 等号集演化}✓：\text{沿}\ w\ \text{追踪等号集}✓（\text{依赖 (b)}✓）$$
$$\textbf{(d) 一般 }M✓：\text{把 (a) 推广到}\ M\ \text{点}✓\ \text{与权重}\ (w_1,\dots,w_M)✓$$

## §6 边界

$$\textbf{① 古典陈述的状态}：\text{Turán 两定理／Andersson 精化均为【外搜所得}】⚠️，\text{尚未逐字核原文}✗（\text{依项目引用纪律标【待核}】✓）；\text{Cassels 1941 仅定位可靠}✓，\text{陈述待读}⚠️$$
$$\textbf{② 无 Cassels 原文}：\text{故本档不声称与 Cassels 逐字对应}✗，\text{一律用【Cassels 型}】✓$$
$$\textbf{③ 本档为回收与规格化}✓，\text{不含新数学}✓；\textbf{④ 未做数值扫描}✓（\text{表 R3 为既有存量}✓）$$
$$\textbf{⑤ 未用 RH}✓；\text{未改他档}✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 加权幂和短窗       命中文件数=1  ::  ./C233-B2-T13-recovery-definitions-known-results-admissible-domain.md
技术词 相变阈值定位       命中文件数=1  ::  ./C233-B2-T13-recovery-definitions-known-results-admissible-domain.md
技术词 大权重渐近定理     命中文件数=1  ::  ./C233-B2-T13-recovery-definitions-known-results-admissible-domain.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
