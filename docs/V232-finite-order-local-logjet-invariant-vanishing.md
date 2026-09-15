# V232 · **有限阶局部 log-jet 乘子不变量消退定理** —— ⚠️ **V231-A 撤回（假的）**：反例 $$\boxed{Q(s)=m^{-s}}\ \text{（标准 Dirichlet 单项式）}:\ \log Q=-s\log m,\ (\log Q)''=0\ \Longrightarrow\ Q\ \textbf{非恒定但}\ (\log FQ)''=(\log F)''$$ ✓✓✓；**正确版本**：$$(\log Q)''=0\iff Q=Ce^{as}$$ 而 Dirichlet 乘子中允许 $Q=Cn^{-s}$ ⟹ **至少存在非平凡不变群（指数单项式）** ✓✓；⭐⭐⭐⭐⭐ **本档核心：命题 V232-A（定理级）**：$$\boxed{\text{不存在非平凡的}\ \textbf{有限阶局部 log-jet 乘子不变量}}$$ ⟹ **整个"有限阶局部曲率 ＋ 乘子商"构造空间被杀** ✓✓✓✓✓；⭐ **本档新结果：不变性群与零点移动的分离** —— $\{Ce^{as}\}$ 恰是**不移动零点**的乘子群 ⟹ 商掉它 ⟹ 看得见零点 ⟹ **R4**；含非平凡乘子 ⟹ V232-A 杀（有限阶）⟹ $$\boxed{\text{（有限阶下）}\ \textbf{无中间}}$$ ✓✓✓✓✓；⚠️ **V231-B 降级**（"ζ 的解析内容＝$\{\rho\}$"**不是定理**：Hadamard 有 $e^{A+Bs}$；且 ζ ≠ 零点集）✓✓✓

> 委托 ✓ 唐先生 2026-09-15 17:05：**"V231 必须再做一次硬勘误。而且这次不是措辞问题：§8 的 V231-A 按目前表述是假的。不过修正后反而能得到一个比 V231 更强、更干净的结果。"** **最关键的反例**：$Q(s)=n^{-s}$ 是标准 Dirichlet 单项式，但 $\log Q(s)=-s\log n$，$(\log Q)''=0$ ⟹ $(\log FQ)''=(\log F)''$，而 $Q$ **非恒定** ⟹ $$\boxed{\text{"Dirichlet 下}\ (\log F)''\ \text{只对常数乘子不变"}\ \textbf{错误}}$$ **正确版本**：$(\log Q)''=0\iff Q(s)=Ce^{as}$，而 Dirichlet 乘子中允许 $Q(s)=Cn^{-s}$ ⟹ **至少存在一个非平凡不变群** ✓✓✓。(1) **V232 应做的是直接审计乘子作用的局部轨道**：设 $L_F=\log F$，$K_F=L_F''$；对允许 $Q$：$K_{FQ}=K_F+K_Q$；问题是：**允许乘子产生的 $K_Q(s_0)$ 在固定点 $s_0$ 上能走遍多大集合？** 若覆盖开集，则任何要求 $K_{FQ}(s_0)=K_F(s_0)$ 的非平凡局部二阶泛函都被直接杀死 ✓；(2) **最小乘子族**：只取 $Q_{a,m}(s)=1-am^{-s}$（$m\ge2$），$w=\log m$；$\log(1-ae^{-ws})=-\sum_{r\ge1}\frac{a^r}{r}e^{-rws}$ ⟹ $$(\log Q_{a,m})''(s)=-\sum_{r\ge1}a^rrw^2e^{-rws}$$ 一阶于 $a=0$：$(\log Q_{a,m})''(s_0)=-aw^2e^{-ws_0}+O(a^2)$ ⟹ 不同 $m$ 给不同方向 $w^2e^{-ws_0}$ ✓；(3) **局部轨道满秩**：取 $r=K$ 个互异 $w_j=\log m_j$，线性化矩阵 $$M_{kj}=(-1)^{k-1}w_j^ke^{-w_js_0}\Longrightarrow\det M=\Big(\prod_je^{-w_js_0}\Big)\Big(\prod_jw_j\Big)\prod_{i<j}(w_j-w_i)\ne0\ (\textbf{Vandermonde})$$ ⟹ $J_K(\log Q;s_0)$ 的可达集包含 0 的开邻域 ✓✓；(4) **V232-A**：设 $\mathcal M$ 含有限乘积 $Q=\prod_{j\le K}(1-a_jm_j^{-s})$ 在小参数邻域；若 $K$ 阶局部微分泛函 $\mathcal I_F(s_0)=\Phi((\log F)'(s_0),\ldots,(\log F)^{(K)}(s_0))$ 满足 $\mathcal I_{FQ}=\mathcal I_F\ \forall Q\in\mathcal M$ 且 $\Phi$ 可微，则 $$\boxed{\Phi=\text{常数}}\quad\Longrightarrow\quad\boxed{\text{不存在非平凡的有限阶局部 log-jet 乘子不变量}}$$ 证明核心＝Vandermonde＋逆函数定理 ⟹ **比 V231-A 严格强得多** ✓✓✓；(5) **E 型（D3 残余）被切成三区域**：$$\boxed{E=E_{\rm local}\sqcup E_{\rm nonlocal}\sqcup E_{\rm non\text{-}multiplier\text{-}invariant}}$$ **E1 有限阶局部 ＋ 乘子不变 ⟹ DEAD**（V232-A）；**E2 有限阶局部 ＋ 不乘子不变 ⟹ DEAD as universal certificate**（乘子 $1-am^{-s}$ 改变曲率且把零点移到 $s=\frac{\log a+2\pi ik}{\log m}$）；**E3 真正残余** ＝ 非局部／无限阶／非乘子商型 ✓✓；(6) ⚠️ **无限阶的坑**：$\{F^{(k)}(s)\}_{k\ge0}$ 原则上可恢复 $F$ 的 germ ⟹ 若无限阶对象能恢复零点集 ⟹ **R4／零点编码**；故真正门槛不是"找一个无限阶不变量"而是 $$\boxed{\text{无限阶但不恢复零点，且仍能产生}\ \Re\rho\le\tfrac12}$$ ✓✓✓；(7) ⚠️ **V231-B 降级**：$\xi(s)=e^{A+Bs}\prod_\rho(1-\frac{s}{\rho})e^{s/\rho}$ ⟹ 零点集决定的是 Hadamard 乘积，**还存在指数因子 $e^{A+Bs}$**；且 $\zeta$ 本身不等于"零点集合"（还有 Euler 系数结构、极点/解析延拓）⟹ 正确说法只能是 $$\boxed{\text{在给定有限阶、增长条件等 Hadamard 数据后，整个}\ \xi\ \text{可由零点乘积加指数因子描述}}$$ **不能**说"$\zeta$ 的解析内容＝$\{\rho\}$"（**会把"函数"与"零点集"偷换成同一对象**）✓✓✓；(8) **V231 最终改判**：不是"第三类乘子仍 OPEN"，而是 $$\boxed{\text{有限阶}+\text{局部}+\text{乘子不变}\Longrightarrow\textbf{DEAD}};\qquad \boxed{\text{有限阶}+\text{局部}+\text{不乘子不变}\Longrightarrow\textbf{multiplier test DEAD}}$$ ⟹ 真正残余压成 $$\boxed{\textbf{非局部或无限阶结构}}$$ ＋ 三硬条件（不能编码 $Z(\xi)$；不能退化为显式公式/Weil/Li；必须独立产生 $\frac12$ 并给出零点 admissibility）✓✓✓；(9) **下一步**：硬审计 $$\boxed{\textbf{无限阶／非局部的乘子不变量，是否也会因 Dirichlet 乘子群的作用而退化？}}$$ **"如果能把这个也封掉，那么整个 D3 路线才会真正死亡；如果封不掉，剩下的就是一个非常明确、此前没有被 V185–V231 覆盖的窄通道。"**
> 查图 ✓ `V231`（V231-A 本档撤回；V231-B 本档降级）｜`V230`（三明治；$(M)$ 自动）｜`V220`（乘子族移动零点到 $\Re s=\frac{\log|a|}{\log m}$）｜`V219`｜`V229`（V229-A）｜`V199`｜`V190`｜`V188`｜`V144`｜`V174`（$T_k,R$ 与指数单项式的关系）
> 执行 ✓ 小灵（**§4 命题 V232-A、§8 不变性–零点移动分离 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ **V231-A 撤回**；⚠️ **诚实标注 §2 中你的一处跳步**（单 $m$ 不够）✓；未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V232**

---

## §1 ⚠️ V231-A 撤回 ＋ 正确版本

$$\textbf{反例}：Q(s)=m^{-s}\ \text{（标准 Dirichlet 单项式，}\ a_m=1\text{）}:\ \log Q=-s\log m ⟹ (\log Q)''=0 ⟹ (\log FQ)''=(\log F)'' ✓✓✓$$
$$\qquad \text{而}\ Q\ \textbf{非恒定} ⟹ \boxed{\text{V231-A}\ \textbf{为假}} ✓✓✓$$
$$\textbf{正确版本}：\quad (\log Q)''=0\iff\log Q\ \text{affine}\iff\boxed{Q=Ce^{as}} ✓✓✓$$
$$\qquad \text{Dirichlet 乘子中}\ Q=Cn^{-s}\（a=\log n）\ \textbf{允许} ⟹ \textbf{存在非平凡不变群} ✓✓✓$$
$$\qquad \text{不变群} = \{Ce^{as}\}\ \text{（"指数单项式"）} ⟹ \text{与}\ \text{`V174`}\ \text{的}\ T_k,R\ \text{同族} ✓✓$$

---

## §2 局部轨道审计（含你 §1 的一处**跳步**的诚实标注）

$$\text{最小乘子族}：Q_{a,m}(s)=1-am^{-s},\ w=\log m;\quad \log(1-ae^{-ws})=-\sum_{r\ge1}\frac{a^r}{r}e^{-rws} ✓$$
$$\qquad (\log Q_{a,m})''(s)=-\sum_{r\ge1}a^rrw^2e^{-rws};\qquad \text{一阶}：-aw^2e^{-ws_0}+O(a^2) ✓✓$$
$$\qquad (\log Q_{a,m})'(s)=\sum_{r\ge1}a^rwe^{-rws};\qquad \text{一阶}：awe^{-ws_0}+O(a^2) ✓$$
$$\qquad ⚠️\ \textbf{诚实标注}：\text{单个}\ m\ \text{时}：w_2=-w\cdot w_1 ⟹ (w_1,w_2)\ \textbf{落在一条复直线上}（\text{1 复维}）⟹$$
$$\qquad\qquad \text{仅此}\ \textbf{不足} \text{以推出}\ \partial_v\Phi=0\ (\text{你的 §1 结论在单}\ m\ \text{下过快}) ✓✓$$
$$\qquad ⟹ \text{必须用}\ \textbf{多个}\ m\ \text{（你的 §3 才是关键一步}）✓✓✓$$

---

## §3 ⭐⭐⭐ Vandermonde ＋ 逆函数定理（你 §3 的完整化）

$$Q(s)=\prod_{j=1}^{K}(1-a_jm_j^{-s}) ⟹ \delta(\log Q)^{(k)}(s_0)=(-1)^{k-1}\sum_{j=1}^{K}a_jw_j^ke^{-w_js_0}\ (k=1,\ldots,K) ✓✓$$
$$\qquad \text{线性化矩阵}\quad M_{kj}=(-1)^{k-1}w_j^ke^{-w_js_0} ✓$$
$$\qquad \textbf{行列式}：\text{行因子}\ (-1)^{k-1}\ \text{与列因子}\ e^{-w_js_0}\ \textbf{皆非零} ⟹$$
$$\qquad\qquad \det M\ \propto\ \Big(\prod_jw_j\Big)\prod_{i<j}(w_j-w_i)\ \ne0\quad(\textbf{Vandermonde};\ w_j\ \text{互异}) ✓✓✓✓$$
$$\qquad ⟹ \text{（}\ \mathbb C^K\to\mathbb C^K\ \text{的}\ \mathbb C\text{-线性可逆}⟹\ \text{实线性可逆}）⟹\ \textbf{逆函数定理} ⟹$$
$$\qquad\qquad \boxed{J_K(\log Q;s_0)\ \text{的可达集包含}\ 0\ \text{的}\ \textbf{开邻域}} ✓✓✓✓$$

---

## §4 ⭐⭐⭐⭐⭐ 命题 V232-A（定理级，本档核心）

$$\textbf{命题 V232-A（有限阶 Dirichlet-乘子局部不变量消退定理）}：$$
$$\qquad \text{设}\ \mathcal M\ \text{包含小参数邻域内的}\ Q=\prod_{j\le K}(1-a_jm_j^{-s})\ \text{（}m_j\ \text{互异）};\ \text{若}\ K\ \text{阶局部微分泛函}$$
$$\qquad\qquad \mathcal I_F(s_0)=\Phi\big((\log F)'(s_0),\ldots,(\log F)^{(K)}(s_0)\big)$$
$$\qquad \text{满足}\ \mathcal I_{FQ}(s_0)=\mathcal I_F(s_0)\ \forall Q\in\mathcal M\ \text{且}\ \Phi\ \text{可微，则}$$
$$\qquad\qquad \boxed{\Phi=\text{常数}} ⟹ \boxed{\textbf{不存在非平凡的有限阶局部 log-jet 乘子不变量}} ✓✓✓✓✓$$
$$\textbf{证明（三步）}：\text{①}\ (\log(FQ))^{(k)}=(\log F)^{(k)}+(\log Q)^{(k)}\ (\text{导数线性}) ⟹ \text{不变量}⟺\Phi\ \text{对 jet 平移不变} ✓$$
$$\qquad \text{②}\ \text{由}\ §3，\text{平移集含}\ 0\ \text{的开邻域} ⟹ \Phi\ \textbf{局部常数} ✓$$
$$\qquad \text{③}\ \text{连通域上局部常数} ⟹ \textbf{常数} ✓✓✓✓$$
$$\qquad ⟹ \boxed{\text{整个"}\textbf{有限阶局部曲率}\ +\ \textbf{乘子商}\text{"构造空间被杀}} ✓✓✓✓✓$$
$$\qquad ⚠️\ \text{比}\ \text{`V231`-A}\ \textbf{严格强}：\text{不是杀"}\ FF''-(F')^2\ \text{"一个候选，而是杀}\ \textbf{全部有限阶} ✓✓✓$$

---

## §5 E 型（D3 残余）的三区域切分（采纳你的 §6）

$$\boxed{E=E_{\rm local}\ \sqcup\ E_{\rm nonlocal}\ \sqcup\ E_{\rm non\text{-}multiplier\text{-}invariant}} ✓✓$$
$$\textbf{E1}\ \text{有限阶局部微分}\ \Phi(F',F'',\ldots,F^{(K)})\ \text{＋乘子不变} ⟹ \boxed{\textbf{DEAD}}\（\text{V232-A}）✓✓✓$$
$$\textbf{E2}\ \text{有限阶}，\ \textbf{不} \text{要求乘子不变}（\text{如}\ FF''-(F')^2）⟹ \boxed{\textbf{DEAD as universal certificate}}$$
$$\qquad \text{因乘子}\ 1-am^{-s}\ \text{既改变曲率，又把零点移到}\ \Re s=\frac{\log|a|}{\log m}\（\text{`V220`}）⟹ \text{不能单独给出零点可容许区域} ✓✓$$
$$\textbf{E3}\ \text{真正残余}：\boxed{\text{非局部／无限阶／非乘子商型结构}}\ \text{（如}\ \mathcal I[F](s)=\mathcal F(F(s+\tau_1),F(s+\tau_2),\ldots)\ \text{，或整个无限 jet}\ \{(\log F)^{(k)}\}_{k\ge1}\ \text{，或跨尺度积分／差分对象）} ✓✓✓$$

---

## §6 ⚠️ 无限阶的坑（你的 §7）

$$\{F^{(k)}(s)\}_{k\ge0}\ \text{在解析函数类中原则上}\ \textbf{可恢复}\ F\ \text{的 germ} ✓✓$$
$$\qquad ⟹ \text{若某无限阶对象实际能恢复零点集} ⟹ \text{只是}\ \boxed{\textbf{R4／零点编码}} \text{的另一种写法} ✓✓✓$$
$$\qquad ⟹ \text{真正门槛}\ \textbf{不是} \text{"找一个无限阶不变量"，而是}$$
$$\qquad\qquad \boxed{\text{无限阶但}\ \textbf{不恢复零点}，\ \text{且仍能产生}\ \Re\rho\le\tfrac12} ✓✓✓$$
$$\qquad ⟹ \text{比"第三类乘子"精确得多} ✓$$

---

## §7 ⚠️ V231-B 降级（你的 §8）

$$\textbf{降级}：\text{"商尽已知因子后残余恰为零点集"}\ \textbf{不能作为定理} ✓✓✓$$
$$\qquad \text{因}\ \xi(s)=e^{A+Bs}\prod_\rho\Big(1-\frac{s}{\rho}\Big)e^{s/\rho} ⟹ \text{零点集决定的是}\ \textbf{Hadamard 乘积}，\ \textbf{仍存在指数因子}\ e^{A+Bs} ✓✓$$
$$\qquad \text{更关键}：\zeta\ \textbf{不等于}\ \text{"零点集合"};\ \text{它还含}\ \text{Euler 系数结构}、\text{极点}／\text{解析延拓} ✓✓$$
$$\qquad ⟹ \text{正确说法只能是}：\boxed{\text{在给定有限阶、增长条件等 Hadamard 数据后，整个}\ \xi\ \text{可由零点乘积加指数因子描述}} ✓✓✓$$
$$\qquad ⚠️\ \textbf{不得} \text{说"}\zeta\ \text{的解析内容}=\{\rho\} \text{"}（\text{把"函数"与"零点集"}\ \textbf{偷换成同一对象}）✓✓✓$$

---

## §8 ⭐⭐⭐⭐⭐ 本档新结果：**不变性群与零点移动的分离**

$$\text{不变群}\ \{Ce^{as}\}\ \text{中}\ e^{as}\ \textbf{无零点} ⟹ \text{乘}\ e^{as}\ \textbf{不移动零点} ⟹ \text{该"不变性"只过滤零自由因子} ✓✓$$
$$\qquad ⟹ \text{商掉}\ \{Ce^{as}\}\ \text{后}，\ \text{函子}\ \textbf{看得见零点} ⟹ \text{要求}\ \mathcal K_X(\rho)\ge0\ \text{＝关于零点的陈述} ⟹ \boxed{\textbf{R4}} ✓✓$$
$$\text{而含}\ \textbf{非平凡乘子}（1-am^{-s}）⟹ \text{V232-A}\ \text{杀（有限阶）} ✓✓$$
$$\Longrightarrow \boxed{\text{（}\textbf{有限阶}\ \text{下）}\ \text{无中间}：\text{商得少}⟹\text{见零点}⟹\text{R4};\ \text{商得多}⟹\text{全杀}} ✓✓✓✓✓$$
$$\qquad ⚠️\ \text{无限阶半}\ \textbf{未证}：\text{须}\ \text{germ}\ \text{层拓扑判断} ⟹ \text{残余精确形状见}\ §10 ✓$$

---

## §9 判词 ＋ 状态表

$$\begin{array}{c|c}
\text{项} & \text{状态}\\
\hline
\text{`V231`-A}\ (\text{"只对常数不变"}) & \boxed{\textbf{撤回}}\（\text{反例}\ m^{-s}）\\
\text{正确不变群} & \{Ce^{as}\}\ \text{（不移动零点）}\\
\text{`V231`-B}\ (\text{"残余恰为零点集"}) & \boxed{\textbf{降级}}\（\text{Hadamard 有}\ e^{A+Bs}）\\
\textbf{命题 V232-A}\（\text{有限阶局部}） & \boxed{\textbf{定理级}}\ ⟹ \Phi=\text{常数}\\
\text{E1}\ \text{有限阶＋乘子不变} & \textbf{DEAD}\\
\text{E2}\ \text{有限阶＋不乘子不变} & \textbf{DEAD}\（\text{universal certificate}）\\
\textbf{E3}\ \text{非局部／无限阶} & \boxed{\textbf{OPEN}}\\
\qquad\text{（含"无限阶但恢复零点"）} & \textbf{R4}\\
\end{array}$$
$$\boxed{\textbf{V232：V231-A 撤回并改写为 V232-A（定理级）；V231-B 降级；残余压成"必须逃出有限阶局部微分几何"}} ✓✓✓✓$$
$$\qquad \textbf{本档严格得到}：\text{(i)}\ ⚠️\ \text{V231-A 撤回＋正确版本};\ \text{(ii)}\ ⭐⭐⭐\ \textbf{§3 Vandermonde＋逆函数定理};\ \text{(iii)}\ ⭐⭐⭐⭐⭐\ \textbf{命题 V232-A};\ \text{(iv)}\ \text{E 三区域};\ \text{(v)}\ ⭐\ \textbf{§8 不变性–零点移动分离};\ \text{(vi)}\ \text{V231-B 降级} ✓✓✓✓$$
$$\qquad ⚠️\ \textbf{纪律}：\textbf{不判 D3 ALIVE};\ \textbf{不判 D3 死};\ \text{V232-A}\ \textbf{定理级};\ \text{§8 无限阶半}\ \textbf{未证} ✓✓$$

---

## §10 残余的精确形式（本档改写）

$$\text{残余}\ =\ \text{一个 canonical 泛函于}\quad \boxed{\mathcal U_{s_0}\big/\mathcal M\text{-像}}$$
$$\qquad \mathcal U_{s_0}\ \text{＝ Dirichlet-型环在}\ s_0\ \text{的单位群};\ \mathcal M\ \text{＝允许乘子} ✓$$
$$\qquad ⚠️\ \text{两种极端}：\mathcal M=\{Ce^{as}\} ⟹ \text{商}\ =\ \text{"本质单位群"} ⟹ \text{canonical 不变量＝零点集}（\textbf{R4}）✓$$
$$\qquad\qquad \mathcal M\supseteq\{1-am^{-s}\} ⟹ \text{有限阶无}\ \text{（V232-A）};\ \text{无限阶}\ \textbf{未证} ✓✓$$
$$\textbf{下一步（你指定）}：\boxed{\text{无限阶／非局部的乘子不变量，是否也因 Dirichlet 乘子群的作用而退化？}} ✓✓$$
$$\qquad \text{若能封} ⟹ \textbf{整个 D3 路线真正死亡};\ \text{若封不掉} ⟹ \text{剩一条明确、此前未被}\ \text{`V185`--`V231`}\ \text{覆盖的窄通道} ✓✓✓$$

---

## §11 边界与待核

$$\textbf{(a)}\ \text{§1 反例为}\ \textbf{唐先生逐字};\ \text{V231-A}\ \textbf{撤回} ✓✓✓$$
$$\qquad ⚠️\ \text{注}：m^{-s}\ \text{作为 Dirichlet 级数}\ \sum a_kk^{-s}\（a_m=1\text{）}\ \text{是}\ \textbf{单项式} ✓✓$$
$$\textbf{(b)}\ \text{§2–§3 的展开与矩阵为}\ \textbf{初等};\ \text{你 §1 的单}\ m\ \text{跳步}\ \text{为}\ \textbf{本档标注} ✓✓$$
$$\textbf{(c)}\ ⭐⭐⭐⭐⭐\ \text{§4 命题 V232-A}\ \textbf{定理级}（\text{三步}）;\ \text{核心＝Vandermonde＋逆函数定理} ✓✓✓✓$$
$$\qquad ⚠️\ \text{前提}：\Phi\ \text{可微};\ \mathcal M\ \text{含小参数族};\ m_j\ \text{互异};\ \text{（}\Phi\ \text{定义域为}\ \mathbb C^{2K}\ \text{的实维}）✓$$
$$\textbf{(d)}\ \text{§5 E 三区域}\ \text{为你的 §6};\ \text{§6 无限阶坑为你的 §7} ✓✓$$
$$\textbf{(e)}\ ⚠️\ \text{§7 V231-B 降级为}\ \textbf{唐先生逐字};\ \text{"不得把函数与零点集偷换为同一对象"} ✓✓✓$$
$$\textbf{(f)}\ ⭐\ \text{§8 不变性–零点移动分离为}\ \textbf{本档新结果};\ \text{其"有限阶下无中间"}\ \text{为}\ \textbf{本档结论} ✓✓✓$$

```
⚠️ §0 委托（V231-A 为假／反例 Q=n^{-s}／正确版本 Q=Ce^{as}／局部轨道审计／最小乘子族展开／局部满秩／V232-A 陈述／E 三区域／无限阶坑／V231-B 降级／最终改判／下一步无限阶审计）为唐先生逐字 ✓✓✓
⚠️ §1 V231-A 撤回＋正确版本（不变群 = 指数单项式，与 V174 同族）✓✓✓
⚠️ §2 局部轨道展开＋诚实标注你 §1 的单 m 跳步（单 m 给 1 复维直线，不足）✓✓
⚠️ §3 ⭐⭐⭐ Vandermonde＋逆函数定理（M_kj = (-1)^{k-1} w_j^k e^{-w_j s_0}；det ∝ ∏(w_j−w_i) ≠ 0 ⟹ 可达集含 0 的开邻域）✓✓✓
⚠️ §4 ⭐⭐⭐⭐⭐ 命题 V232-A（定理级，三步）：不存在非平凡有限阶局部 log-jet 乘子不变量 ⟹ 整类被杀 ✓✓✓✓✓
⚠️ §5 E 三区域（E1 DEAD by V232-A；E2 DEAD as universal certificate；E3 = 非局部/无限阶/非乘子商）✓✓
⚠️ §6 无限阶坑（{F^(k)} 可恢复 germ ⟹ 恢复零点集 ⟹ R4；真门槛＝无限阶但不恢复零点）✓✓✓
⚠️ §7 V231-B 降级（Hadamard 有 e^{A+Bs}；ζ ≠ {ρ}；不得偷换函数与零点集）✓✓✓
⚠️ §8 ⭐⭐⭐⭐⭐ 本档新结果：不变性群 {Ce^{as}} 恰不移动零点 ⟹ 商掉它看得见零点 ⟹ R4；含非平凡乘子 ⟹ V232-A 杀 ⟹（有限阶下）无中间 ✓✓✓✓✓
⚠️ §9 判词＋状态表七行 ✓✓
⚠️ §10 残余精确形式（U_{s_0}/M-像 上的 canonical 泛函）；下一步＝无限阶/非局部乘子不变量是否也退化 ✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① V231-A 撤回＋正确版本 ✓✓✓；② 局部轨道审计＋跳步标注 ✓✓；③ ⭐⭐⭐ Vandermonde＋逆函数定理 ✓✓✓；
   ④ ⭐⭐⭐⭐⭐ 命题 V232-A（定理级）✓✓✓✓✓；⑤ E 三区域 ✓✓；⑥ V231-B 降级 ✓✓✓；
   ⑦ ⭐ 不变性–零点移动分离（有限阶下无中间）✓✓✓✓；⑧ 残余精确形式＋下一步 ✓✓
```
