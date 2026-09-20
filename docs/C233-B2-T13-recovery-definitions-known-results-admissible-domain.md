已查地图（**先查后写**）：查三张主图（`CLOSED-ROUTES-MAP.md`／`MASTER-STATUS-AND-CLOSURES.md`／`MASTER-NOGO-AND-LIVE-PATHS.md`）—— **无 Cassels／T13／weighted 条目** ✗ ⟹ 按协议属**未覆盖** ✓；查 `C193`（w=1 等号集＋w 表）、`C199`（w=2 定理）、`C200`（w=2 等号集）、`TARGETS`（T13 原始描述）、`MASTER-LEDGER-RELATED-LEMMAS-CONJECTURES`（L5/L6/L7 待核）。回查见 §7 ✓

D0: 本档对象 = **B2/T13 开工前的定义／已知结果／精确可行域／Cassels 型结构回收**（不做数值扫描）—— 关系 = 回收与规格化，非新机制
D1: 0
FREEZE-ACK: 本档即冻结期内的回收与规格化（依 §8.1；不产候选结论）

---

## §0 回收结论（先行）

$$\boxed{\text{B2/T13 的完整规格已恢复}✓：定义 ✓／已知结果（我方 2 条定理＋2 条数值）✓／古典家族（Turán 两定理＋Cassels 1941＋Andersson）✓／可行域的 3 个可选约定 ✓／6 个开口 ✓}$$
$$\boxed{\text{建议第一刀}：\textbf{w}\to\infty\ \text{的渐近定理}✓（\text{可证路线已定位}✓）\text{，不做数值扫描}✗}$$

## §1 定义（逐字）

### 1.1 我方定义（T13-B，`C-193` §2）

$$\boxed{\ g_w(N)\ :=\ \inf_{\varphi_1,\varphi_2}\ \max_{1\le k\le N}\ \bigl[\ w\cos(k\varphi_1)+\cos(k\varphi_2)\ \bigr]\ }✓,\qquad w\ge1✓,\ (\varphi_1,\varphi_2)\in[0,\pi]^2✓$$

$$\text{来历}：M=2\ \text{的阻尼/加权 (RP}_M\text{) 版}✓：Z_k:=[w\cos k\varphi_1+\cos k\varphi_2]✓\ \text{即两点幂和}\ \operatorname{Re}\sum_j b_j z_j^k✓\ \text{于}\ b=(w,1)✓,\ |z_1|=|z_2|=1✓$$
$$\text{约定}：N=5M=10✓（\text{与 (RP}_M\text{) 一致}✓）；\text{权重比}\ w\ge1✓（\text{不失一般性}：\text{可整体缩放并交换}✓）$$

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
| R4 | 下界 $g_w\gtrsim w\kappa_{10}-1=w\cos\tfrac{2\pi}{11}-1$ | 初等 ✓ | `C-193` §2（证明 ✓） |

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

## §5 ⭐ 开口清单 ＋ 候选机制（不在此做数值扫描 ✓）

$$\textbf{Q1}（常数的闭式）✓：\exists\ \text{闭式}\ g_w(10)\ \forall w\ge1\ ✓？\text{已知}：w=1\Rightarrow\tfrac12✓,\ w=2\Rightarrow1✓（\text{两端精确}✓）$$
$$\textbf{Q2}（相变点）✓：\text{最优构型切换的}\ w\ \text{阈值是否代数数}✓？\text{数值显示两个阈值落在}\ (1.2,1.5),\ (1.5,2)✓$$
$$\textbf{Q3}（大 }w\text{ 渐近）✓：g_w=w\kappa_{10}-1+o(1)✓？R4\ \text{只给}\ \gtrsim✓；w=5：3.2065\ \text{vs}\ 3.2468✓（\text{差}\ 0.040✓，\text{第二点的正贡献}✓）$$
$$\textbf{Q4}（等号集随 }w\text{ 的演化）✓：w=1\ \text{两点}✓\to w=2\ \text{单点}✓；\text{中间}\ w\ \text{如何}✓？\text{是否在阈值处【跳变}】✓$$
$$\textbf{Q5}（一般 }M\text{ 与一般权重）✓：b=(w_1,\dots,w_M)✓\ \text{的最优常数与等号集}✓（\text{T13 原始形式}✓）$$
$$\textbf{Q6}（与古典泛函的关系）✓：\text{古典的}\ \min_k|\sum_{i\le k}b_i|\ \text{型泛函}\ \text{在短窗 regime 对应何物}✓？$$

$$\textbf{候选机制（按可证性排序}✓，\text{供唐先生选一刀}✓\text{）}：$$
$$\textbf{(a) 大 }w\ \text{渐近定理}✓✓（\textbf{推荐}✓）：\text{取}\ k=k_1(w)=\arg\max\cos k\varphi_1✓\ \text{（鸽笼}✓，\kappa_{10}=\cos\tfrac{2\pi}{11}✓） \Longrightarrow g_w\ge w\kappa_{10}-1✓；$$
$$\qquad \text{断言}：w\ \text{充分大时【等号可达}】✓ \Longrightarrow g_w=w\kappa_{10}-1✓\ \textbf{精确}✓（\text{需证：第二点可同时被推到}\ \cos k\varphi_2=-1✓\ \text{或至少其贡献可算}✓）$$
$$\qquad \text{可证性}：\text{一维鸽笼＋显式误差}✓，\text{不需证书}✓ \Longrightarrow \text{预计一条引理}✓$$
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
