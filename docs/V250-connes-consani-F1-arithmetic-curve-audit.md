# V250 · **Connes–Consani「绝对 F₁-算术曲线」审计**（arXiv:2606.06604 全文精读）—— ⭐⭐⭐ **canonicity 有真进展**（模空间/泛性质实现 → 部分回应 `V242` Gate 2；且**Frobenius 以真正自同态形式存在**（在 F₁/单子侧）→ 回应 `V242`-A 的**字面**）；但 ⭐⭐⭐⭐⭐ **对 β 无路，且理由全部来自本项目已有定理**：(a) Thm 5 是**直积隔离**算术与几何 ⟹ `V239`-C／`V205` KILL-2 ＋ `ESC2` no common carrier；(b) 典范输出是**比值** $\tau=i\log p/2\pi$ ⟹ `V220`；(c) archimedean 类比 $\mathbb X_\infty=\mathbb P^1(\mathbb R)$ 是**圆** ⟹ `V227`-A／§4（模长轨迹）；(d) torsor 商链＝**canonical symmetry-breaking** ⟹ `V148`（无定向信息）；(e) 其自身下一步落在 `AOB3`／`V145`／`V243` **停点**

> 委托 ✓ 唐先生 2026-09-15 21:31：**"直接去抓取F1-几何论文，仔细读取"** ✓✓
> 来源 ✓ **直连 arXiv 成功**（curl 753 KB HTML ＋ 803 KB PDF；**非二手转述**）✓✓；论文＝**Alain Connes & Caterina Consani, "On the Absolute Geometry of $\operatorname{Spec}\mathbf Z$ and the Fargues–Fontaine curve", arXiv:2606.06604v1 [math.AG], 30 页, 2026-06-04**（arXiv 提交记录：From: Alain Connes）✓；MSC 14G40, 14G45, 06F05, 11R42, 11M55；CC BY 4.0；**尚未同行评审** ⚠️
> 纪律 ✓ 逐节精读（引言四定理 ＋ §3.8／§3.10 ＋ §4.2／§4.3 ＋ §5 全部读过原文）✓；**未用 RH 作推导** ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ **V250**

---

## §1 论文在做什么（原文提炼，非转述）

$$\textbf{起点（Scholze 启发）}：\text{对特征}\ p\ \text{的代数闭完备域}\ F,\ \textbf{untilts of }F\ \text{是}\ \operatorname{Spec}\mathbf Z\ \text{的}\ F\text{-值点的良好替代} ✓$$

$$\textbf{构造（本文核心）}：\text{把算术 site 的}\ \mathbf F_1\text{-结构层拉回到}\ \operatorname{Spec}\mathbf Z：$$
$$\qquad \operatorname{Pic}_*:=(\widehat{\mathbf N^\times_0},\ \mathcal O_{\mathbf F_1}),\qquad \mathcal O_{\mathbf F_1}:=\mathbf F_1[T];\qquad \operatorname{Frob}_k(T^n)=T^{nk},\ k\in\mathbf N_{\ge0} ✓$$
$$\qquad \text{Abel–Jacobi 映射}\ \theta:\operatorname{Spec}\mathbf Z\to\operatorname{Pic}(\operatorname{Spec}\mathbf Z),\ \theta(p)=\mathbf Z[1/p],\ \theta(\eta)=\mathbf Z ✓$$
$$\qquad \textbf{绝对 }\mathbf F_1\text{-算术曲线}：(\operatorname{Spec}\mathbf Z)_{\mathbf F_1}:=(\operatorname{Spec}\mathbf Z,\ \mathcal F),\qquad \mathcal F:=\Theta^{-1}(\mathcal O_{\mathbf F_1})\ ✓$$
$$\qquad \text{茎}：\mathcal F_\eta=\mathbf F_1;\qquad \boxed{\mathcal F_p=\mathbf F_1\big[T^{\mathbf Z[1/p]_+}\big]}\quad\text{且}\ x\mapsto x^p\ \text{在}\ \mathcal F_p\ \text{上是}\ \textbf{自同态}（\text{"perfection at }p\text{"}）✓✓$$

$$\textbf{五个定理（原文编号）}：$$
$$\qquad \text{(Thm 3.16)}\ \text{对特征}\ p\ \text{代数闭 perfectoid}\ F：\text{局部}\ F\text{-点 mod 茎的典范对称} \Longrightarrow \ell\ne p\ \text{处}\ \textbf{坍缩为单轨道};\ p\ \text{处}\ \textbf{典范双射于 untilts mod Frobenius}＝\text{FF 曲线的闭点} ✓$$
$$\qquad \text{(Thm 3.9)}\ \text{对任意 perfectoid}\ C\ (\text{剩余特征}\ p)：\ C\text{-点（}p\ \text{处）}\textbf{典范同于 tilt 中的开单位圆盘}\ 1+\mathfrak m_{C^\flat};\ \text{mod 对称}\Rightarrow\text{untilts/Frobenius};\ \ell\ne p\Rightarrow\text{单}\ \mathbf Q_\ell^\times\text{-轨道} ✓$$
$$\qquad \qquad ⭐\ \text{关键：}\textbf{不要求}\ C\ \text{特征}\ p\ \text{或代数闭} \Longrightarrow \textbf{特征无关}（\text{可对}\ \mathbb C\ \text{取值}）✓✓$$
$$\qquad \text{(Thm 3.17)}\ \textbf{"严格几何筛"}：\ell\ne p\ \text{处超度量错配迫使拓扑表现为离散}\Rightarrow\text{坍缩};\ p\ \text{处}\ \mathbf F_1\text{-茎＝}\textbf{普遍倾斜函子} ✓$$
$$\qquad \text{(Thm 3／Prop 4.1、4.4)}\ \text{在}\ \mathbb C\ \text{上、固定}\ p：\text{两个位}\ \Sigma_p=\{p,\infty\};\ \textbf{局部性条件把}\ \mathbf N^\times\ \text{的 Frobenius 作用典范延拓为局部 Weil 群}\ W_v\ \text{的连续作用};\ \textbf{非平凡局部点空间}\ \mathcal M_p^v\ \text{是}\ W_v\text{-}\textbf{主齐性空间（torsor）}＝\text{单轨道} ✓✓✓$$
$$\qquad \qquad \qquad W_\infty=\mathbf C^\times,\quad W_p=\mathbf Q_p^\times ✓$$
$$\qquad \text{(Thm 5／§4.3)}\ \textbf{Tate 曲线与矩形分解}：：E_p:=\mathcal M_p^\infty/p^{\mathbf Z}\cong\mathbf C^\times/p^{\mathbf Z}\（q=p^{-1}）;\ \text{实轨迹}\ E_p(\mathbf R)=\mathbf R^\times/p^{\mathbf Z}=(\mathbf R_+^\times/p^{\mathbf Z})\sqcup(\mathbf R_-^\times/p^{\mathbf Z}) ✓$$
$$\qquad \qquad \mathcal X_\infty:=\mathcal M_p^\infty/W_\infty^\sigma\cong\mathbb P^1(\mathbf R),\qquad \widetilde{\mathcal X}_\infty＝\text{典范非分歧双覆盖（deck}＝-1）✓$$
$$\qquad \qquad \boxed{E_p\ \cong\ C_p\times\widetilde{\mathcal X}_\infty},\qquad C_p=\mathbf R_+^\times/p^{\mathbf Z}\（\text{长度}\ \log p\）,\quad \widetilde{\mathcal X}_\infty\（\text{相圆，长度}\ 2\pi\）✓✓$$
$$\qquad \qquad \qquad\Longrightarrow \textbf{原文自述}：\text{"perfectly isolating the arithmetic from the geometric data"};\ \text{模参数}\ \boxed{\tau=i\frac{\log p}{2\pi}}=\text{两个典范实微分之比的积分} ✓✓✓$$

$$\textbf{§5 Outlook（其自身下一步）}：\text{scaling site}\ \mathscr S=([0,\infty)\rtimes\mathbf N^\times,\mathcal O);\ \text{Gauss 赋值}\ v_s\ (s＝\text{对数半径});\ v_\bullet(f)\ \textbf{凹、分段线性、整斜率}$$
$$\qquad \Longrightarrow \tau(f):=-v_\bullet(f)\ \textbf{凸、分段仿射、整斜率}＝\text{scaling site 结构层的全局截面} \Longrightarrow \textbf{特征 0 解析几何 → 幂等几何的典范函子} ✓$$
$$\qquad \text{下一步（留作 future work）}：\textbf{Frobenius 本征空间}\ B^{\varphi=p}\ \text{在向}\ C_p\ \text{的 descent 下的行为}，\text{及其与}\ \text{`CC3` 椭圆曲线几何的关系} ✓$$

## §2 与 `V242` 的关系（三道门逐条）—— **有真进展，但不是我们要的那一项**

$$\textbf{Gate 1（是否真新对象）}：\ △\ \text{新}\ \textbf{包装} \text{（拉回层}\ \mathcal F=\Theta^{-1}(\mathcal O_{\mathbf F_1})\text{＋局部点模空间）};\ \text{部件＝算术 site（`CC1`）＋Abel–Jacobi（`CC6`）＋FF 曲线（FF）＋tilts（Scholze）＋scaling site（`CC3`）} ✓$$
$$\textbf{Gate 2（是否由}\ \mathbb Z\ \text{经泛性质强制）}：\ ⭐\ \textbf{这一步有真进展} ✓✓✓$$
$$\qquad \text{原文}：\text{"the curve}\ (\operatorname{Spec}\mathbf Z)_{\mathbf F_1}\ \text{arises }\textbf{canonically as the moduli space of local}\ \mathbf F_1\text{-points modulo the intrinsic symmetries of the arithmetic site}\ \widehat{\mathbf N^\times_0}\text{"} ✓$$
$$\qquad ⟹ \textbf{模空间／泛性质式论证} \text{——正是 `V242` Gate 2 要求的形状}（\text{不是"选择"，而是"模空间的典范描述"}）✓✓$$
$$\textbf{Gate 3（是否给出新 polarization／定号性）}：\ ✗\ \textbf{无} \text{（详见 §3）}✓$$
$$\qquad ⚠️\ \text{注意：文中确有"polarization-like"物（椭圆曲线＋典范全纯 1-形式}\omega=d\log\lambda+i\,d\theta），\ \text{但它是}\ \textbf{曲线}\ E_p\ \text{的}，\ \textbf{与}\ \zeta\ \text{零点无关联} ✓$$
$$\textbf{⭐ 附带回应 `V242`-A（Frobenius 只是共轭类、不能复合）}：\text{本文的 Frobenius}\ \textbf{是真正的自同态} \text{——但住在}\ \textbf{单子／topos 侧}：$$
$$\qquad \operatorname{Frob}_k(T^n)=T^{nk}\ \text{作用于}\ \mathbf F_1[T];\qquad p\cdot\rho:=\rho(p\,\cdot)\ \text{作用于局部态射} ✓$$
$$\qquad ⟹ \textbf{精确回应}：\text{不是"Frobenius 不可能"，而是}\ \textbf{"Frobenius 自同态必须住在}\ \mathbf F_1\text{／单子层，其代价是它的轨道是 }\textbf{untilts（FF 曲线闭点）而非 }\zeta\ \text{零点"} ✓✓✓$$

## §3 ⭐⭐⭐⭐⭐ **为什么对 β 无路（五条，全部引用本项目已有定理）**

$$\textbf{(a)}\ \textbf{Thm 5 是直积隔离} \Longrightarrow \text{`V239`-C／`V205` KILL-2 ＋ `ESC2` no common carrier} $$
$$\qquad \text{原文逐字}：\text{"perfectly isolating the arithmetic from the geometric data"},\ E_p\cong C_p\times\widetilde{\mathcal X}_\infty ✓$$
$$\qquad \text{两个因子}\ \textbf{独立};\ \text{唯一"耦合"是}\ \textbf{复结构的选取}（\text{"矩形复结构"}＝格\ \langle1,iy\rangle\ \text{，纠缠靠乘}\ i\ \text{——一个}\textbf{常数}，\ \text{不是算术耦合}）✓$$
$$\qquad \text{本项目}：\text{`V239`-C：加／乘数据互相独立}\Rightarrow\text{联合态是直积}\Rightarrow\text{holonomy＝独立因子之积}\Rightarrow\text{落 `V205` KILL-2}\Rightarrow DEAD;\ \text{`ESC2`：正性在一侧、谱数据在另一侧}\Rightarrow\text{no common carrier} ✓✓✓$$
$$\qquad ⟹ \textbf{没有"通道"能让算术数据（}\log p\text{）去约束任何谱／实部量} ✓✓✓$$
$$\textbf{(b)}\ \textbf{典范输出是比值} \Longrightarrow \text{`V220`} $$
$$\qquad \tau_p=i\log p/(2\pi)＝\textbf{"两个典范实微分之比的积分"} \Longrightarrow \text{每个素数出一个}\ \textbf{由}\ \log p\ \text{决定的数}，\ \text{无零点依赖} ✓$$
$$\qquad \text{`V220`（指数→位置转换器：乘子障碍＋聚集障碍）：}\text{任何}\ \textbf{聚集／比值型} \text{算术量至多给}\ \textbf{abscissa／增长}，\ \text{不给零点位置};\ \text{一个比值}\ \textbf{编码一个数}，\ \text{不编码集合}\{\Re\rho\} ✓✓✓$$
$$\textbf{(c)}\ \textbf{archimedean 类比是圆} \Longrightarrow \text{`V227`-A／§4} $$
$$\qquad \mathcal X_\infty\cong\mathbb P^1(\mathbf R)\（\text{圆}）,\ \widetilde{\mathcal X}_\infty＝\text{其双覆盖（亦圆，长度}2\pi）,\ C_p=\mathbf R_+^\times/p^{\mathbf Z}\（\text{亦圆}）✓$$
$$\qquad \text{`V227`-A：}\sup_{z\in R}\Re z\ \textbf{不是}\ \{|z|\}\ \text{的函数};\ \text{`V227` §4：char-}p\ \text{临界轨迹＝}\textbf{圆（模长轨迹，极化够用）}，\ \text{char-}0＝\textbf{竖直线（非模长轨迹）}\Longrightarrow\textbf{移植结构性失败} ✓✓$$
$$\qquad ⟹ \textbf{本文的 archimedean 类比又是一族"模长型"对象（圆）} \text{——与 `V245` 七机制普查得到的模式完全一致} ✓✓✓$$
$$\textbf{(d)}\ \textbf{torsor 商链＝canonical symmetry-breaking} \Longrightarrow \text{`V148`} $$
$$\qquad \mathcal M_p^\infty\（W_\infty\text{-torsor}）\xrightarrow{\ \div p^{\mathbf Z}\ }E_p\xrightarrow{\ \div\,\mathbf R_+^\times\ }\widetilde{\mathcal X}_\infty\xrightarrow{\ \div(\pm1)\ }\mathcal X_\infty\cong\mathbb P^1(\mathbf R) ✓$$
$$\qquad \text{`V148`：canonical symmetry-breaking }\textbf{把 torsor 平凡化}\Rightarrow H^1\Rightarrow\text{二次}\Rightarrow\textbf{不产生定向信息} ✓✓$$
$$\qquad ⟹ \text{这条商链}\ \textbf{恰恰典范地丢掉了} \text{我们 `V148` 判定的"定向"那类数据} ✓✓✓$$
$$\textbf{(e)}\ \textbf{其自身下一步落在已登记停点} $$
$$\qquad \text{§5 下一步＝}\textbf{Frobenius 本征空间}\ B^{\varphi=p}\ \text{＋}\ \text{scaling site 的 tropicalization} ✓$$
$$\qquad \text{`AOB3`:47（Deninger 纲领停点＝无限维上同调＋正性）};\ \text{`V145`（canonical generator 有、polarization 缺）};\ \text{`V243` §3（强外部交叉结论：谱几何／scaling-site-Frobenius／算术拓扑-DW 三者都能造 global object，}\textbf{都不能产生 RH 所需 polarization}）✓✓✓$$

## §4 净增量（对我们**有用**的部分）

$$\text{(1)}\ ⭐\ \textbf{canonicity 论证模板}：\text{"}\textbf{模空间 of local }\mathbf F_1\text{-points modulo intrinsic symmetries of the arithmetic site}\text{"} \text{——这是}\ \textbf{以模空间描述实现"泛性质强制"} \text{的一种具体方式};\ \text{可移植为}\ \text{`V242` Gate 2 的}\ \textbf{判据设计模板} ✓✓$$
$$\text{(2)}\ ⭐\ \textbf{"geometric sieve"}：\ell\ne p\ \text{处超度量错配}\Rightarrow\textbf{坍缩为单轨道};\ p\ \text{处打开为开单位圆盘} \Longrightarrow \textbf{一个真典范的"选择"机制} \text{——}\textbf{但选出的是素数，不是零点} ✓✓$$
$$\qquad \text{对照本项目多次遇到的"无 canonical 选择"（`V233`-C 乘子可把零点移到任意}\sigma\text{等）}：\text{此处}\ \textbf{存在} \text{典范选择，}\textbf{但它不能选择零点} ✓$$
$$\text{(3)}\ ⭐\ \textbf{Frobenius 自同态的存在位置}：\text{在}\ \mathbf F_1\text{／单子／topos 层存在真自同态},\ \text{在 Galois 层只有共轭类} \Longrightarrow \textbf{把 `V242`-A 从"不可能"精确化为"必须换层"} ✓✓$$
$$\text{(4)}\ ⭐\ \textbf{新引用登记}：\text{[CC6]}\ \textbf{Connes–Consani：}\operatorname{Pic}(\operatorname{Spec}\mathbf Z)\ \text{（算术除子类单子）＝算术 site}\ \widehat{\mathbf N^\times}\ \text{的点单子};\ \text{Abel–Jacobi}\ \theta\ \text{（}\theta(p)=\mathbf Z[1/p],\ \theta(\eta)=\mathbf Z\text{）} ✓\ \text{——本项目档案似乎未登记 `CC6`} ⚠️$$
$$\text{(5)}\ \textbf{统一性宣称}：\text{"common geometric origin for}\ p\text{-adic Hodge theory, complex analytic geometry, and the adelic scaling site"} \text{——}\textbf{统一} \text{正是 char-}p\ \text{成功所依赖的东西（基域几何）};\ \text{但见 §3：(a)–(d) 说明统一发生在}\ \textbf{几何侧}，\ \textbf{没到正性侧} ✓$$

## §5 判词 ＋ 状态表 ＋ 边界

$$\boxed{\textbf{V250：Connes–Consani 绝对 }\mathbf F_1\text{-曲线＝}\textbf{canonicity 方向上的真进展}（模空间／泛性质；Frobenius 自同态存在于 }\mathbf F_1\text{ 侧）};\ \textbf{但对 }\beta\ \textbf{ 无路，且理由全部来自本项目已有定理（五条）} ✓✓✓$$

| 项 | 判定 | 依据 |
|:--|:--|:--|
| 构造是否典范 | ⭐ **是（模空间／泛性质）** | 原文自述 ＋ `V242` Gate 2 |
| `V242` Gate 1（新对象） | △ 新包装、旧部件 | 部件＝`CC1`／`CC6`／FF／Scholze／`CC3` |
| `V242` Gate 2（泛性质强制） | ⭐ **有真进展** | 模空间 of local $\mathbf F_1$-points mod intrinsic symmetries |
| `V242` Gate 3（新 polarization） | ✗ **无** | §3(a)(c) |
| `V242`-A（Frobenius 共轭类） | ⭐ **精确回应**：换层到 $\mathbf F_1$／单子侧即得真自同态 | $\operatorname{Frob}_k(T^n)=T^{nk}$；$p\cdot\rho$ |
| 是否携带 β | ✗ **否** | §3(a)(b)(c) |
| 是否给出 positivity | ✗ 几何侧的极化（$E_p$ 的 1-形式），与 ζ 无关 | §3(a)(c) |
| 其下一步 | 落 `AOB3`／`V145`／`V243` 停点 | §3(e) |
| 对 RH 的地位 | **不是关于 RH 的论文**（无 ζ 零点、无临界线、无 L-函数正性） | 全文 |

$$\textbf{边界（诚实）}：\text{本档为}\ \textbf{全文精读审计}（\text{引言四定理＋§3.8／§3.10＋§4.2／§4.3＋§5 均读原文，非转述}）✓;\ \text{论文}\ \textbf{尚未同行评审}、\text{arXiv-only、30 页、2026-06} ⚠️;\ \text{§3 五条为}\ \textbf{[结构性]} \text{（引用本项目已有定理，但"因此无路"是判断，不是定理）}✓;\ \text{本文}\ \textbf{确有可能存在} \text{我们未看到的用法，}\textbf{本档不写"不可能"} ✓;\ \text{未用 RH 作推导} ✓;\ \text{未跑 Lean} ✓;\ \textbf{零数值} ✓$$

```
⚠️ 委托（唐先生 21:31）"直接去抓取F1-几何论文，仔细读取"
⚠️ 来源：直连 arXiv 成功（curl 753KB HTML + 803KB PDF，非二手）；论文 = Alain Connes & Caterina Consani,
   "On the Absolute Geometry of Spec Z and the Fargues-Fontaine curve", arXiv:2606.06604v1 [math.AG], 30 页,
   2026-06-04；MSC 14G40/14G45/06F05/11R42/11M55；CC BY 4.0；尚未同行评审
⚠️ §1 论文内容（原文提炼）：Scholze 启发；算术 site Pic_* = (N̂_0^×, F1[T])，O_F1:=F1[T]，
   Frob_k(T^n)=T^{nk}；Abel-Jacobi θ: Spec Z → Pic(Spec Z)，θ(p)=Z[1/p]，θ(η)=Z；
   绝对 F1-算术曲线 (Spec Z)_F1 := (Spec Z, F:=Θ^{-1}(O_F1))；茎 F_η=F1，F_p=F1[T^{Z[1/p]_+}]，
   且 x↦x^p 在 F_p 上是自同态（"perfection at p"）
   五定理：Thm 3.16（特征 p 代数闭 perfectoid F：ℓ≠p 坍缩为单轨道；p 处典范双射于 untilts/Frobenius
   ＝FF 曲线闭点）；Thm 3.9（任意 perfectoid C：C-点在 p 处＝tilt 中开单位圆盘 1+m_{C^♭}，mod 对称
   ⟹ untilts/Frobenius；ℓ≠p ⟹ 单 Q_ℓ^×-轨道；特征无关，可对 C 取值）；Thm 3.17（严格几何筛：ℓ≠p 超度量
   错配 ⟹ 离散坍缩；p 处 F1-茎＝普遍倾斜函子）；Thm 3/Prop 4.1、4.4（C 上固定 p：Σ_p={p,∞}；局部性把
   N^× 的 Frobenius 作用典范延拓为 Weil 群 W_v 连续作用；非平凡局部点空间 M_p^v 是 W_v-主齐性空间
   （torsor）＝单轨道；W_∞=C^×，W_p=Q_p^×）；Thm 5/§4.3（Tate 曲线 E_p:=M_p^∞/p^Z ≅ C^×/p^Z，q=p^{-1}；
   实轨迹 E_p(R)=R^×/p^Z=(R_+^×/p^Z)⊔(R_-^×/p^Z)；X_∞:=M_p^∞/W_∞^σ ≅ P^1(R)，X̃_∞ 为典范非分歧双覆盖；
   E_p ≅ C_p × X̃_∞；原文自述"perfectly isolating the arithmetic from the geometric data"；模参数
   τ=i log p/2π＝两个典范实微分之比的积分）
   §5 Outlook：scaling site S=([0,∞)⋊N^×,O)；Gauss 赋值 v_s（s=对数半径），v_•(f) 凹、分段线性、整斜率
   ⟹ τ(f):=-v_•(f) 凸分段仿射整斜率＝scaling site 结构层全局截面 ⟹ 特征 0 解析几何 → 幂等几何的典范函子；
   下一步（future work）＝Frobenius 本征空间 B^{φ=p} 在向 C_p 的 descent 下的行为
⚠️ §2 与 V242 三道门：Gate 2 有真进展（"arises canonically as the moduli space of local F1-points modulo the
   intrinsic symmetries of the arithmetic site"＝模空间/泛性质式论证）；Gate 3 ✗ 无新 polarization；
   ⭐ 附带精确回应 V242-A：Frobenius 自同态存在于 F1/单子/topos 侧（Frob_k(T^n)=T^{nk}；p·ρ:=ρ(p·)），
   Galois 侧才是共轭类 ⟹ 从"不可能"精确化为"必须换层"，代价是轨道＝untilts 而非 ζ 零点
⚠️ §3 ⭐⭐⭐⭐⭐ 对 β 无路的五条（全部引用本项目已有定理，[结构性]）：
   (a) Thm 5 是直积隔离（原文"perfectly isolating the arithmetic from the geometric data"；唯一"耦合"
   ＝复结构选取，纠缠靠乘 i＝常数）⟹ V239-C（加/乘独立 ⟹ 联合态直积 ⟹ 落 V205 KILL-2）＋ ESC2
   （正性在一侧、谱数据在另一侧 ⟹ no common carrier）
   (b) 典范输出是比值 τ_p=i log p/2π（"两个典范实微分之比的积分"）⟹ V220（聚集/比值型算术量至多给
   abscissa/增长，不给零点位置；一个比值编码一个数，不编码集合 {Re ρ}）
   (c) archimedean 类比 X_∞ ≅ P^1(R) 是圆，X̃_∞ 亦圆，C_p 亦圆 ⟹ V227-A（sup Re z 不是 {|z|} 的函数）
   ＋ V227 §4（char-p 临界轨迹＝圆即模长轨迹；char-0＝竖直线非模长轨迹 ⟹ 移植结构性失败）
   ⟹ 与 V245 七机制普查的模式完全一致
   (d) torsor 商链 M_p^∞ →(÷p^Z) E_p →(÷R_+^×) X̃_∞ →(÷(±1)) P^1(R) ＝ canonical symmetry-breaking
   ⟹ V148（canonical symmetry-breaking 平凡化 torsor ⟹ H^1 ⟹ 二次 ⟹ 不产生定向信息）
   (e) §5 下一步（Frobenius 本征空间 B^{φ=p} ＋ scaling site tropicalization）落在 AOB3:47（Deninger 停点
   ＝无限维上同调＋正性）／V145（canonical generator 有、polarization 缺）／V243 §3（三外部框架都能造
   global object，都不能产生 RH 所需 polarization）
⚠️ §4 净增量：(1) canonicity 论证模板（模空间 of local F1-points mod intrinsic symmetries）可移植为
   V242 Gate 2 判据设计模板；(2) "geometric sieve"＝真典范选择机制，但选出的是素数不是零点（对照 V233-C
   "无 canonical 选择"）；(3) Frobenius 自同态的存在层问题（F1/单子层有、Galois 层无）⟹ V242-A 精确化；
   (4) 新引用登记 [CC6]（算术除子类单子 Pic(Spec Z)＝算术 site N̂^× 的点单子；Abel-Jacobi θ）；档案似未登记；
   (5) 统一性宣称（p-adic Hodge + 复解析几何 + adelic scaling site 的共同几何起源）发生在几何侧，没到正性侧
⚠️ §5 边界：全文精读审计（非转述）；论文尚未同行评审、arXiv-only、30 页、2026-06；§3 五条为 [结构性]；
   不写"不可能"；未用 RH；未跑 Lean；零数值
✅ 净产出：① 全文精读（引言四定理＋§3.8/3.10＋§4.2/4.3＋§5）② V242 Gate 2 有真进展（canonicity 以模空间
   描述实现）③ V242-A 精确回应（Frobenius 换层到 F1/单子侧即得真自同态）④ ⭐ 对 β 无路的五条结构性理由，
   全部引用本项目已有定理（V239-C/V205/ESC2/V220/V227-A/V148/AOB3/V145/V243）⑤ 登记 [CC6] 与几何筛
```
