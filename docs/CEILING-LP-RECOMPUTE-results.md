# 🎯 **CEILING-LP-RECOMPUTE** — 前沿「带宽一证书天花板 0.6818287」的独立重算尝试

> **任务来源** ✓：唐先生 2026-09-17 15:11 指派（Subagent）。**承接** CEILING-AUDIT 1–9 ✓
> （`CEILING-AUDIT-frontier-lean-chain…`／`-2-enclosures-verified…`／`-3-definitions…`／`-4-exact-CUE…`／
> `-5-erratum…`／`-6-resolution…`／`-7-FINAL-NearCUE…`／`-8-extremal-configuration…`／`-9-own-code-reproduces-frontier-d1…` ✓）
> **本档＝实跑结果 ＋ 判词**（脚本 `lean-frontier-audit/lp/ceiling_lp_recompute.py` ✓ 可跑）

---

## §0 🧭 **开工前地图检查**（PRE-WORK MAP CHECK，2026-09-17 唐先生立规 ✓）

$$\text{已查（关键词：}\texttt{0.6818287}\ \big|\ \texttt{bandwidth-one／带宽一}\ \big|\ \texttt{marks 几何}\ \big|\ \texttt{EnclOK}）✓$$
1. `CLOSED-ROUTES-MAP.md` ✓　2. `MASTER-STATUS-AND-CLOSURES.md` ✓　3. `MASTER-NOGO-AND-LIVE-PATHS.md` ✓
4. `ASSETS-REGISTRY.md` ✓　5. `INDEX-BY-DIRECTION.md`＋`ID-CLAIMS.tsv`（前档已核）✓

**命中并引用（⟹ 本条非新案，不新开方向）** ✓：
$$\text{(i)}\ \texttt{CLOSED-ROUTES-MAP} \text{ L2598}：\textbf{0.682 身份更正}＝\text{外部引用}（\text{arXiv:2608.13637 §7.2}），\text{非本项目自推}✓$$
$$\text{(ii)}\ \texttt{CLOSED-ROUTES-MAP} \text{ L2654}（\texttt{V296.3} \text{判死刀}）：\text{证书框架内成立}✓$$
$$\text{(iii)}\ ⭐\ \texttt{CLOSED-ROUTES-MAP} \text{ L2681}（\texttt{V296}\ \text{层 1}）：\texttt{ceiling\_of\_valid\_at}\ \text{假设}＝\{N>0;\ r\in C^2;\ |E|\le M;\ \textbf{单配置}\ c_0+\sum s_jr(j/N)\le p_1\}$$
$$\qquad\Longrightarrow\ \text{天花板}\ \textbf{不含}\ \text{bandwidth／Fourier 支撑／Toeplitz／正性／trace／rank／HS}✓✓$$
$$\text{(iv)}\ \texttt{E44-ceiling-encl-audit.md}：p_0=1-a_N\ \text{已登记}（0.681828687463831474\ldots，\text{余量}\ 1.2536\times10^{-8}）✓$$
$$\text{(v)}\ \texttt{E45-ceiling-law-construction.md}（2026-09-13）：\text{自建近-CUE 法}；\text{粗网格}\ p\ge0.7134／0.7073，\textbf{细网格}\ p\approx0.0231✓$$
$$\Longrightarrow\ \boxed{\text{本档＝对既有规格}\ \textbf{执行重算}\ \text{并把新结果登记为资产}\ \texttt{C-36}✓✓}$$

---

## §1 ⭐ **目标身份的精确确认**（本档新发现：目标值本身就在 Lean 文件里，是**输入**而非输出）

$$\texttt{LawN256.lean}\ \text{文件头逐字}：\text{「The law's simple-point fraction is}\ p_0=1-a_N=\frac{10909258999421303588095230195816054408197}{16000000000000000000000000000000000000000}\ \text{exactly}\ (=0.68182868746\ldots)\text{」}✓✓$$
$$\text{本档精确复核}：p_0=0.681828687463832\ldots✓\qquad p_0\le0.6818287\ \text{（余量}\ 1.254\times10^{-8}\text{）✓✓}\quad(\text{与 E44 一致}✓)$$
$$\text{「2/3 距其方法天花板}<0.016\text{」}\quad 0.6818287-\tfrac23=0.0151620<0.016✓✓$$
$$\Longrightarrow\ \boxed{\text{目标}\ 0.6818287\ \textbf{＝律自身的简单点比例}\ p_0\ \text{（四舍五入上取）};\ \text{它作为}\ \textbf{显示性输入}\ \text{进入 Lean}✓✓}$$
$$\qquad ⚠️\ \text{故「独立确认」}\iff\textbf{独立重算该律本身}（\text{或其 LP 最优值}）——\ \text{而不可能在证书侧再推一遍得到}✓✓$$

---

## §2 **数据侧复算**（全部精确有理数／整数，261 行输出见 `lp/lp_run_log.txt` ✓）

| 项目 | 本档实测 | 前沿声称 | 判定 |
|:--|:--|:--|:--|
| 行条件 $\max_{0<j<256}\max_{\text{端点}}\|256S(j)-j\|$ | $1.836710\times10^{-40}=1/2^{132}$ | $\tau=3\times10^{-40}$ | **成立 ✓（更紧 0.612×）** |
| $lo_j=j/256$ 恰成立的行数 | 131/255 | — | 端点交替 = 下界恰为 $j/256$ ✓ |
| 盒最坏 $\sum_js_j=T_N/N$ | 1.32395316071284 | — | — |
| 盒最坏 $D(1)=\sum s_j-\tfrac12$ | 0.82395316071284 | $d_1=0.82395317$ | **复现 ✓（差 $-9.3\times10^{-9}$）** |
| $S(256)$（盒上端） | 211.432009 | — | 自由行 ✓ |

---

## §3 ⭐ **唯一可硬算的刚性关系：网格对齐律被 Parseval 锁死**

$$\text{若所有}\ x_{c,i}\in\{0,\ldots,255\}\（\text{整数位置}\）\text{，记}\ M_k:=\sum_{i:x_i=k}m_{c,i}\in\{0,1,2\},\ \sum_kM_k=N：$$
$$\textbf{Parseval}\ \Longrightarrow\ \sum_{j=1}^{256}S(j)=\frac1{256}\sum_{j=0}^{255}|\widehat M(j)|^2=\sum_kM_k^2=N+2n_2=N(2-p)✓$$
$$\text{行条件与}\ S(0)=256\ \text{（恒真）一并代入}：\quad p=2-\frac{\sum_{j<N}S(j)+S(N)}{256}\ \text{（}\textbf{被锁死，无自由度}\text{）}✓$$
$$\text{数值}：S(N)=1\（\text{sine-kernel 端值}）\Rightarrow p=1.498046875;\quad S(N)=\text{盒上端}\ 211.432\Rightarrow p=0.676046839✓$$
$$\Longrightarrow\ \boxed{\text{两值皆}\ne p_0=0.681828687\ \text{且}\ne\tfrac23\ \Longrightarrow\ \textbf{最优律非网格对齐}✓✓}$$
$$\qquad\Longrightarrow\ \text{位置必为非整数有理数}（\text{与 docstring 逐字「rational positions}\ x_{c,i}\in[0,256)\text{」一致}✓✓）$$
$$\qquad\Longrightarrow\ \textbf{Parseval 不适用}\ \text{（DFT 只对整数位置构成周期群）}\ \Longrightarrow\ p\ \text{与}\ S\ \text{之间存在}\ \textbf{自由耦合}$$

### §3.1 ⭐ **追加：由公布包络**直接**排除整数位置（不依赖 Parseval 求和约定）**
$$\text{对}\ \textbf{任何}\ \text{位置}：\ \widehat\mu(0)=\sum_im_i=N\ \Longrightarrow\ S(0)=N^2/N=256\ \text{恒成立}✓$$
$$\text{而}\ x_i\in\mathbb Z\ \text{时}：\ e^{2\pi i\cdot256\,x_i/256}=e^{2\pi ix_i}=1\ \Longrightarrow\ |\widehat\mu(256)|^2=\Big(\sum_im_i\Big)^2=N^2\ \Longrightarrow\ \boxed{S(N)=256}✓✓$$
$$\text{公布包络}（j=256）：\ S(256)\in\big[211.432009\ldots,\ 211.432009\ldots+2^{-140}\big]\ \ne\ 256\quad(\text{差}\approx44.57)✓✓$$
$$\Longrightarrow\ \boxed{\text{最优律的原子位置}\ \textbf{必不为整数}（\text{mod}\ 256）\ \text{—— 仅由 Lean 公布数据即可判定}}✓✓✓$$
$$\qquad\text{故前 255 行与第 256 行不在同一 Parseval 周期内}\ \Longrightarrow\ p\ \text{不被行条件锁定，}\ p\ \text{与}\ S\ \text{的耦合（marks 几何）}\ \textbf{不可本地重建}✓✓$$
$$\qquad\qquad\boxed{\text{该耦合＝任务所称「marks 几何」——它}\ \textbf{不在 Lean 内，也不在本地任何档}✓✓}$$

---

## §4 🔬 **对偶侧 LP（盒松弛）**：$ \delta_{\rm box}=\max_r\big[\int_0^1rx\,dx-B_{\rm box}(r)\big]$

### §4.1 ⚠️ **第一发现（本档实跑）：任务所给 LP 规格**字面上**是**无界**的**
$$\text{规格}：\max_{c_0,r}\ \big(c_0+\int_0^1rx\,dx\big)\quad\text{s.t.}\quad c_0+\sum_j s_j\,r(j/N)\le p\ \ \forall\ \text{可取}(s,p)✓$$
$$\text{取}\ r\equiv-\lambda\ (\lambda>0)：\ \text{盒最坏}\ \sum_js_jr(j/N)=-\lambda\cdot1.32395316\ \Longrightarrow\ c_0\le p+1.32395316\,\lambda✓$$
$$\Longrightarrow\ v=c_0-\tfrac12\lambda\ \le\ p+\underbrace{(1.32395316-0.5)}_{=0.82395316}\lambda=p+d_1|r(1)|✓✓✓$$
$$\Longrightarrow\ \boxed{\text{证书值随}\ \lambda\to\infty\ \textbf{无界};\ \text{但沿该方向的增量}\ \textbf{恰等于前沿的}\ d_1|r(1)|\ \text{惩罚项}✓✓✓}$$
$$\qquad ⚠️\ \text{即：}\textbf{任务给的目标函数本身没有上界};\ \text{前沿的天花板是对}\ \textbf{「惩罚后净值」}\ \text{而言}✓\quad(\text{与}\ \texttt{V296}\ \text{层 1 的判断一致}✓)$$
$$\qquad\Longrightarrow\ \text{证书类必须取}\ \textbf{band-limited}（r(\pm1)=0）\ \text{—— 这正是前沿散文逐字：「For a band-limited window,}\ r(\pm1)=0\text{, which zeroes the}\ 0.824|r(1)|\ \text{term}」✓✓✓$$
$$\qquad\Longrightarrow\ \text{本档 LP 全部在}\ r(1)=0\ \text{下执行}✓$$

### §4.2 正则化口径（必须，否则无界）
$$\text{前沿口径：}\ |r'(1)|+\int_0^1|r''|\le B\（\text{散文：}B<8.2\ \text{时所得界}<0.6819\text{）}✓$$
$$B_{\rm box}(r)=\frac1N\sum_jh_j\,r(j/N)+\frac1{NK}\sum_j\max\!\big(0,-r(j/N)\big),\qquad h_j=hi_j/K✓$$
$$r\ \text{离散为}\ M\ \text{节点分段线性（}M=20,50,100\text{）};\ \int_0^1rx\,dx\ \text{用}\ \textbf{闭式 hat 权重}\ W\ \text{（}\sum W_i=\tfrac12\ \text{已核}✓\text{）}✓$$

### §4.3 结果（关键数字）

| 正则预算 $B$ | $\delta_{\rm box}$（$M=20/50/100$） | 最优 $r$ 形状 | 含义 |
|:--|:--|:--|:--|
| 8.2（前沿阈值） | $+2.085368\times10^{-5}$（三档一致 ✓） | 斜坡 $r=+8.2(1-x)$，$r(1)=0$，$|r'(1)|+\int|r''|=8.2$ | 盒松弛给 $p_{\min}+2.085\times10^{-5}$ |
| 1.0 | $+2.543132\times10^{-6}$（三档一致 ✓） | 斜坡 $r=+1\cdot(1-x)$ | $\delta=1/(6N^2)$ **完全一致** ⭐ |
| 自由 $r(1)$ | **无界**（HiGHS 报 Unbounded ✓） | $r\equiv-\lambda$ | 复现 $d_1|r(1)|$ 项 ✓（§4.1） |

$$\text{解析候选（独立核算，}r(1)=0\text{）}：\ \text{缺陷}\ =1\!-\!x^2:3.81{\times}10^{-6}\ \big|\ x(1-x):1.27{\times}10^{-6}\ \big|\ 1-x:2.54{\times}10^{-6}\ \big|\ 1-x^4:6.36{\times}10^{-6}✓$$
$$\Longrightarrow\ \boxed{\textbf{盒松弛紧到}\ \sim10^{-5}：\ \text{真实 LP 值}=p_{\min}+\delta_{\rm box}\ \text{且}\ \delta_{\rm box}=2.085\times10^{-5}\ (B=8.2)✓✓}$$
$$\qquad ⭐\ \text{当}\ B=1：\delta_{\rm box}=2.5431315\times10^{-6}=\frac1{6N^2}\ \text{—— 与前沿稳定性常数}\ M=\frac1{6N^2}+\frac{\tau}{2N}\ \textbf{同一数}✓✓$$

---

## §5 🧮 **(β) 反推**：命中 0.6818287 所需的 $p_{\min}$

$$\text{真实 LP 值}=p_{\min}+\delta_{\rm box}\ \Longrightarrow\ p_{\min}=0.6818287-\delta_{\rm box}✓$$
$$B=8.2：p_{\min}=0.6818078\ \（\text{与记录}\ p_0=0.681828687\ \text{差}\ -2.08\times10^{-5}\text{）}✓$$
$$B=1.0：p_{\min}=0.6818261\ \（\text{与}\ p_0\ \text{差}\ -2.54\times10^{-6}\text{）}✓$$
$$\text{与 §7.2(b) 极值}\ \tfrac23\ \text{对照}：\ 0.6818287-\tfrac23=0.0151620\ \gg\ \delta_{\rm box}\ (2\times10^{-5}\!\sim\!2.5\times10^{-6})✓✓$$
$$\boxed{\text{故目标}\ \textbf{不能} \text{写成「}\tfrac23+\text{证书缺陷」};\ \text{目标}\equiv p_{\min}\ \text{本身（记录值}\ p_0\ \text{落在反推值}\ 2\times10^{-5}\ \text{之内）}✓✓}$$

---

## §6 ⚠️ **与 E45（既有资产）的张力 —— 约束集不可本地重建的直接证据**

$$\texttt{E45}（2026-09-13）\text{已建立}：\text{在}\ N=4／N=6\ \text{网格上，}\textbf{全部带标构型空间}（266／8074\ \text{个}）\text{内：}$$
$$\qquad \text{精确斜坡}\ \tau=0\ \Longrightarrow\ p_{\min}=0.713388348／0.707336156>0.6818287\（\text{粗网格障碍}✓\text{，含干净闭式}✓\text{）}$$
$$\qquad\text{而}\ Q=16\ \text{细网格（}K=\mathbb Q(\zeta_{16})^+\text{）上}\ \textbf{存在已验证的精确斜坡法}\ p\in[0.023069251,\,0.023069251]\ \ll\ 0.6818287✓✓$$
$$\Longrightarrow\ \text{「行条件}\ {+}\ \text{标记构型结构」}\ \textbf{不足以} \text{把}\ p\ \text{钉在}\ 0.6818287：\text{同一约束族在细网格上给出}\ p\sim0.02✓✓$$
$$\Longrightarrow\ \boxed{\text{前沿的「有限程序」}\ \textbf{必然携带额外结构}（\text{超出：行条件＋marks∈\{1,2\}＋Σm=N}）✓✓}$$
$$\qquad\Longrightarrow\ \text{该额外结构}\ \textbf{只在外部 JSON}（\texttt{cert\_N256\_blk\_b128m.json},\ \text{sha256}\ \texttt{cc3de991\ldots 4eb8}）\ \text{内}✓$$
$$\qquad ⚠️\ \textbf{不声称前沿有错}✓\quad\text{只声称：}\textbf{其 LP 的约束集不是本档能从 Lean／论文散文重建的那一版}✓✓$$

---

## §7 ⚖️ **判词（三选一）**

$$\boxed{\text{(iii)}\ \textbf{未能求解}\ \text{—— 目标既未推翻也未被独立确认}✓✓}$$
$$\text{(a)}\ \textbf{未推翻}：\text{本档未构造出任何}\ p<0.6818287\ \text{的}\ \textbf{256-周期近-CUE 律}；\text{亦无对偶反例}✓$$
$$\text{(b)}\ \textbf{未确认}：\text{目标值}\ 0.6818287\ \text{是}\ \textbf{显示性输入}\（p_0=1-a_N\ \text{的舍入}）\text{，}\ \text{其}\ Primal\ LP\ \text{诸列}\ \textbf{不在} \text{本地}✓$$
$$\text{(c)}\ \textbf{卡点（精确）}：\text{证书侧}\ \textbf{退化} \text{—— 盒松弛已紧到}\ 2\times10^{-5}，\text{故}\ \text{对偶值}\equiv p_{\min}；\ p_{\min}\ \text{只由}\ \textbf{Primal} \text{决定}✓✓$$
$$\qquad\Longrightarrow\ \text{所需输入（二选一）}：\text{①}\ \texttt{cert\_N256\_blk\_b128m.json}（\text{sha256 已记录}）\ \big|\ \text{②}\ \text{前沿「有限程序」的}\ \textbf{约束集} \text{逐字定义}✓✓$$
$$\qquad ⚠️\ \text{在二者到手之前，}\textbf{不得} \text{声称}\ 0.6818287\ \text{已被独立复核（}\text{与 E44／E45／V296 既有边界一致}）✓$$

**本档的正面产出**（可引用）✓：
$$\text{①}\ \text{目标值}\ p_0\ \text{的精确有理数身份}\ \text{＋ 三项一致性命中}（\S1\text{--}\S2\text{）}✓✓$$
$$\text{②}\ \text{对偶值}\equiv p_{\min}+\delta_{\rm box}\ \text{且}\ \delta_{\rm box}=2.085\times10^{-5}\ (B=8.2)；=1/(6N^2)\ (B=1)✓✓$$
$$\text{③}\ \textbf{无界性定理}：\text{LP 沿}\ r\equiv-\lambda\ \text{方向的增量}\ \textbf{恰为}\ d_1|r(1)|\ \Longrightarrow\ \text{band-limited 要求}\ \textbf{由 LP 自身强迫}✓✓$$
$$\text{④}\ \text{网格对齐律被 Parseval 锁死}（p=0.6760／1.4980）\Longrightarrow\ \text{最优律必为非整数有理位置}✓✓$$
$$\text{⑤}\ \text{E45 细网格}\ p\approx0.023\ \Longrightarrow\ \text{约束集必含额外结构}（\S6\text{）}✓✓$$

---

## §8 🔧 **方法学勘误（本档自查，第 1 条）**

$$\text{(勘误 1)}\ \text{首版}\ W_i=\int_0^1\phi_i(x)x\,dx\ \text{用}\ \texttt{scipy.integrate.quad}\ \text{算} \Longrightarrow \sum_iW_i=0.50993\ne\tfrac12\ ✗$$
$$\qquad\Longrightarrow\ \text{伪造出}\ M\ \text{依赖的}\ \delta_{\rm box}\ (M=50:0.553;\ M=100:1.030;\ M=200:1.317;\ M=256:1.336)\ ✗\ \text{并伴随"振荡最优} r" ✗✓$$
$$\qquad\Longrightarrow\ \text{已改为}\ \textbf{闭式 hat 权重}（\sum_iW_i=0.500000000\ ✓;\ \text{斜坡积分}\ =-8.2/6\ \text{与解析一致}\ ✓）\ \Longrightarrow\ \delta_{\rm box}\ \textbf{与}\ M\ \text{无关}✓✓$$
$$\qquad 📌\ \text{教训（与 E45 §22 同一纪律）}：\textbf{LP 报出的数在独立核验前只能记为猜测}✓✓$$

---

## §9 边界（诚实）

$$\text{(i)}\ \text{本档}\ \textbf{未用 RH}✓\quad\text{(ii)}\ \textbf{未取 JSON}✓\quad\text{(iii)}\ \textbf{不声称前沿有错}✓$$
$$\text{(iv)}\ \text{"没找到"}\ne\text{"不存在"}\ \text{—— 本档只在}\ \textbf{盒松弛} \text{框架内计算，含}\ \delta_{\rm box}\ \text{的正则预算依赖}✓$$
$$\text{(v)}\ \text{可跑脚本}：\texttt{lean-frontier-audit/lp/ceiling\_lp\_recompute.py}✓\quad\text{输出}：\texttt{ceiling\_lp\_recompute\_out.json}＋\texttt{lp\_run\_log.txt}✓$$
$$\text{(vi)}\ \text{与既有档的关系：}\textbf{不改} \text{E44／E45 结论；}\textbf{不改} \text{V296；}\text{本档只补「对偶侧实测＋无界性＋目标身份」三项}✓✓$$

---
*建档：2026-09-17 15:2x（Subagent CEILING-LP-recompute）｜判词：未能求解（卡点＝对偶退化＋marks 几何缺失）｜引用：E44／E45／V296／CEILING-AUDIT 1–9*
