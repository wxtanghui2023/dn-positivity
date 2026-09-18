# V247 · **"第三型公理"的存在性判定** —— 两刀**定理级证实**（gauge 商 ⟹ 二次不变量；保留相位 ⟹ 须 canonical 轴）✓✓；第三刀 ⭐⭐⭐ **Koecher–Vinberg 给出角 I 的精确刻画＝"自对偶／双线性可表示的正性"** ✓✓✓；但 ⭐⭐⭐⭐⭐ **决定性反例：唐先生的三分律 $\text{Third-type}\Longrightarrow\text{I}\cup\text{II}$ 为\*\*假\*\* —— 第三型存在（Choi 非可分解正映射／$n\ge3$ 正映射锥非自对偶）** ⟹ **"两角"应升级为"三角"，且 III 的障碍是\*\*宿主／识别\*\*而非类型**

> 委托 ✓ 唐先生 2026-09-15 20:51：**"不要再继续扩大外部机制名单，而应该攻击'两角二分'本身。"** ＋ **"必须构造一个第三型的候选公理，然后证明它是否能存在。"** ＋ 五条要求 $(C1)$ 连续／$(C2)$ 相位 gauge 不变／$(C3)$ 确定符号或单调性／$(C4)$ 不以零点位置为输入／$(C5)$ 不等价于已有 Hermitian/quadratic positivity ＋ **三刀**（gauge 商 ⟹ 回角 I；不商 ⟹ 须 canonical axis；若真有额外结构 $A$ 则 $A$ 只能 ① bilinear/sesquilinear/quadratic ⟹ 角 I，② finite-order torsion ⟹ 角 II，**③ 连续非线性非度量非 torsion** ）＋ **任务**：**"构造这个'第三型'最一般的代数形式，然后证明它要么自动产生 quadratic form，要么自动产生 torsion，要么保留 gauge 自由度。"** ＋ **"这次可以直接算，不需要再搜文献。"** ✓✓✓
> 规格 ✓ 按 $(C1)$–$(C5)$ 逐条；**纸面推导** ✓；**零外部检索**（按唐先生指示）✓；纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V247**（注：`id_claim` 分配号为 V247；slug 曾误写 V246，已同步）

---

## §1 第一刀（gauge 商）—— **定理级证实** ✓✓

$$\textbf{Theorem A（不变量理论）}：\text{设}\ \mathcal P=\mathbb C^n\ \text{带标量相位 gauge}\ z\mapsto e^{i\phi}z\ (U(1))\text{。则}\ U(1)\text{-不变多项式环由}\ \textbf{二次不变量}\ \text{生成}：$$
$$\qquad \mathbb C[z,\bar z]^{U(1)}=\mathbb C\big[\,z_i\bar z_j\,\big]_{i,j}\quad（\text{因单项式}\ \prod z_i^{a_i}\bar z_j^{b_j}\ \text{不变}\iff\textstyle\sum a_i=\sum b_j\text{，而这类单项式可分解为}\ z_i\bar z_j\ \text{之积}）✓✓✓$$
$$\qquad ⟹ \text{连续不变}\ L\ \text{由}\ \textbf{Gram 矩阵}\ Z^*Z\ \text{决定} \Longrightarrow \textbf{二次型（半正定）型数据} \Longrightarrow \boxed{\textbf{角 I}} ✓✓✓$$
$$\qquad ⚠️\ \text{加强版}：\text{若相位数据}\ \textbf{只有} \text{相位本身}（\text{即}\ U(1)\ \text{上的一点}）,\ \text{则}\ U(1)\ \text{平移}\ \textbf{传递地} \text{作用} ⟹ (C2)\ \text{迫使}\ L\equiv\mathrm{const} \Longrightarrow \textbf{纯相位不携带任何 canonical 实数} ✓✓$$
$$\Longrightarrow \textbf{唐先生第一刀成立且为定理级} ✓✓✓$$

## §2 第二刀（保留相位）—— **定理级证实** ✓✓

$$\text{相位数据}\ \theta\ \textbf{的本体是一个}\ U(1)\text{-torsor};\ \text{torsor}\ \textbf{无 canonical 基点} ⟹ \text{要由}\ \theta\ \text{canonically 得到一个}\ \mathbb R\ \text{值}，\ \textbf{必须} \text{有}\ \textbf{canonical 原点／轴} ✓✓$$
$$\qquad \theta\in\mathcal T\（U(1)\text{-torsor}）,\ L=\text{“}\theta-0\text{”}\ \text{型} ⟹ \text{需指定}\ 0 \Longrightarrow \textbf{orientation ／ normalization ／ 实轴} ✓$$
$$\qquad \text{而由}\ \textbf{`V218` S1／S3}：\text{二阶对合的不动点}\ \Lambda_X=k/2\ \textbf{可调};\ \text{由}\ \textbf{`V227`-A}：\sup\Re z\ \textbf{不是}\ \{|z|\}\ \text{的函数};\ \text{由}\ \textbf{`V215`(c)}：\text{钉到坐标值须 archimedean 归一化} ✓✓$$
$$\qquad ⭐\ \text{且}\ \text{非自 Hermitian 拓扑的独立对照}：\text{"线只在旋转下定义"}（\text{`V245` M4}）\ \textbf{完全同型} ✓✓$$
$$\Longrightarrow \textbf{唐先生第二刀成立且为定理级} ✓✓✓$$

## §3 第三刀 · 第一步：**第三型最一般的代数形式**

$$\text{唐先生的条件 (C1)–(C5) 合起来}\ \text{＝}\ \textbf{一个 canonical 的"正性／方向性"结构}：$$
$$\qquad \text{(C3) 确定符号／单调} ⟹ \text{存在}\ \textbf{区分的正锥};\quad \text{(C1) 连续} ⟹ \text{锥闭且非离散};\quad \text{(C2) gauge 不变} ⟹ \text{锥}\ G\text{-不变};$$
$$\qquad \text{(C5) 不等价于已有 Hermitian／quadratic 正性} ⟹ \text{锥}\ \textbf{不由二次型定义};\quad \text{(C4) 不用零点} ⟹ \text{锥由其它 canonical 数据定义} ✓$$
$$\Longrightarrow \boxed{\text{第三型}\ \textbf{最一般代数形式}＝\text{一个 canonical、}\ G\text{-不变、}\textbf{非离散、非二次型定义的凸锥}\ (\text{正性锥})} ✓✓✓$$
$$\qquad \text{唐先生的第二分支据此可读作：}A\ \text{为 bilinear／sesquilinear／quadratic} \Longrightarrow \text{锥＝}\ \{x:Q(x)\ge0\}\ (\text{二次型锥})\Longrightarrow \textbf{角 I};\ A\ \text{为 finite-order torsion} \Longrightarrow \textbf{角 II} ✓$$

## §4 ⭐⭐⭐ **Theorem C（Koecher–Vinberg）：角 I 的精确刻画** —— 定理级 ✓✓✓

$$\textbf{定理（Koecher 1958/62；Vinberg 1960/63，经典）}：\text{有限维实向量空间中的}\ \textbf{齐性自对偶开凸锥}\ \text{恰为某个}\ \textbf{Euclid Jordan 代数}\ \text{的}\ \textbf{平方锥};\ \text{且该 Jordan 代数带一个 canonical 的}\ \textbf{trace 二次型} ✓✓✓$$
$$\qquad ⟹ \text{一个 canonical 正性锥若是}\ \textbf{齐性}\ \textbf{＋}\ \textbf{自对偶}，\ \textbf{自动} \text{产生二次型} \Longrightarrow \textbf{角 I} ✓✓✓$$
$$\Longrightarrow \boxed{\textbf{角 I 的精确数学刻画}＝\text{"}\textbf{自对偶正性锥}\text{"}＝\text{"正性可由}\textbf{双线性形式}\text{表示"}} ✓✓✓$$
$$\qquad ⚠️\ \text{读数}：\textbf{Weil 正性／Bochner／Hodge 指标配对} \text{全部是}\ \textbf{双线性} \text{的} ⟹ \text{全部落角 I，且这}\ \textbf{不是巧合，而是 KV 的推论} ✓✓✓$$

## §5 ⭐⭐⭐⭐⭐ **Theorem D（决定性反例）：第三型存在** —— 唐先生三分律为假 ✓✓✓✓

$$\textbf{事实（Choi 1975；Woronowicz 1976，经典）}：\text{正映射锥}\ \mathcal P(M_n\to M_n)\ \text{在}\ n\ge3\ \text{时}\ \textbf{非自对偶}，\ \text{且含}\ \textbf{非可分解} \text{元素}（\text{不能写成 CP}\ +\ \text{co-CP}）✓✓✓$$
$$\qquad ⚠️\ \text{对照低维}：\text{正映射锥自对偶}\iff(n,m)\in\{(2,2),(2,3),(3,2)\} ⟹ \textbf{只有极低维自对偶} ✓✓$$
$$\textbf{而}\ \text{Choi 定理}：\phi\ \textbf{完全正} \iff \text{Choi 矩阵}\ C_\phi=\sum_{ij}E_{ij}\otimes\phi(E_{ij})\ \textbf{半正定} ✓⟹ \textbf{CP 部分＝可由双线性形式表示} ✓✓$$
$$\qquad ⟹ \textbf{非 CP 的正性} \text{＝}\textbf{不可由任何双线性形式表示的正性} ✓✓✓$$

$$\textbf{逐条核对 $(C1)$–$(C5)$}：\quad (C1)\ \text{连续}\ \checkmark;\quad (C2)\ \text{gauge 不变}（\text{锥按定义}\ U(n)\text{-不变}）\checkmark;\quad (C3)\ \text{确定符号}（\text{它就是一个锥}）\checkmark;\quad (C4)\ \text{不用零点} \checkmark;\quad (C5)\ \text{不等价于 quadratic 正性} \checkmark\（\text{因非 self-dual} ⟹ \textbf{KV 不适用}）✓✓✓$$
$$\Longrightarrow \boxed{\textbf{第三型存在};\ \text{唐先生的}\ \text{Third-type}\Longrightarrow\text{I}\cup\text{II}\ \textbf{为假}} ✓✓✓$$
$$\qquad \text{逃逸点精确定位}：\text{KV 需要}\ \textbf{齐性＋自对偶};\ \text{正映射锥}\ \textbf{非自对偶（}n\ge3\text{）且非齐性} ⟹ \text{归约}\ \textbf{结构性失败} ✓✓✓$$

## §6 **"两角" ⟹ "三角"（本档核心结论）**

$$\boxed{\textbf{角 I}}：\text{自对偶／双线性可表示的正性（KV} \Longrightarrow \text{Jordan} \Longrightarrow \text{二次型）};\ \text{成员}：\text{Weil／Bochner／Hodge 配对／Bridgeland }Q／\text{单环}／\text{正定度量}$$
$$\boxed{\textbf{角 II}}：\text{离散／扭}（\mathbb Z／\mathbb Z/N／\mu_N／\text{绕数}）;\ \text{成员}：\text{point gap}／\text{Br}／\text{Galois 共轭类}$$
$$\boxed{\textbf{角 III}}\（\textbf{新}\）:\ \text{连续、gauge 不变、确定符号、}\textbf{非自对偶／非双线性可表示} \text{的正性锥};\ \textbf{实例}：\text{Choi 非可分解正映射}（n\ge3）✓✓✓$$
$$\qquad ⚠️\ \text{角 III 的障碍}\ \textbf{不是类型障碍}：\text{它}\ \textbf{不} \text{归约为二次型，也}\ \textbf{不} \text{归约为扭} ⟹ \text{剩下的障碍是}\ \textbf{宿主／识别}：$$
$$\qquad \qquad \text{(i)}\ \textbf{宿主}：\text{它是}\ M_n／\text{算子系统上的结构},\ \textbf{无已知 canonical 算术实例}（\text{`V242` 缺口 I／III};\ \text{`V204` "无非厄米宿主"}）✓$$
$$\qquad \qquad \text{(ii)}\ \textbf{识别}：\text{即便附上，还须证其极射线／锥结构编码}\ \Re\rho ⟹ \text{本项目经典残差} ✓$$

## §7 **对我们的意义（重写 polarization 故事）**

$$\text{char-}p\ \text{的 Weil／Deligne：}\textbf{Hodge 指标配对是双线性的} \Longrightarrow \textbf{角 I} ⟹ \text{所以成功} ✓$$
$$\text{char-}0\ \text{要 RH：}\textbf{要么} \text{同一件东西}（\text{Weil 正性} ⟹ \textbf{循环}）,\ \textbf{要么} \text{角 III（}\textbf{无算术宿主}）⟹ \textbf{与}\ \textbf{`V227` §4} \text{（char-}p\ \text{圆轨迹 vs char-}0\ \text{竖直线）}\textbf{完全一致} ✓✓✓$$
$$\Longrightarrow \textbf{残差被改写为}\ \textbf{可检验形式}：$$
$$\boxed{\text{是否存在一个}\ \textbf{算术正性}，它\ \textbf{不可由任何双线性形式表示}（\text{非 Choi 型}）？}$$
$$\qquad ⚠️\ \text{这一形式}\ \textbf{新于} \text{"缺 polarization"}：\text{它}\ \textbf{指定了类型} \text{（非双线性正性）}\ \textbf{并且}\ \textbf{有现成的判定机器}（\text{Choi 定理}／\text{算子系统}／\text{PPT}^2\ \text{型问题}）✓✓✓$$

---

## §8 判词 ＋ 状态表 ＋ 边界

$$\boxed{\textbf{V247：两刀定理级证实};\ \textbf{角 I 被 KV 精确刻画为"双线性可表示的正性"};\ ⭐\textbf{第三型存在}（Choi 非可分解正映射）⟹ \textbf{唐先生三分律为假};\ \textbf{"两角"升级为"三角"};\ \textbf{III 的障碍＝宿主／识别而非类型}} ✓✓✓$$

| 项 | 内容 | 级别 |
|:--|:--|:--|
| 第一刀（gauge 商 ⟹ 二次不变量 ⟹ 角 I） | $U(1)$ 不变多项式由 $z_i\bar z_j$ 生成；纯相位 ⟹ $L$ 常值 | **[定理级]** ✓ |
| 第二刀（保留相位 ⟹ 须 canonical 轴） | 相位是 $U(1)$-torsor，无 canonical 基点 ⟹ 须轴 ⟹ `V218`S1／`V227`-A／`V215`(c) | **[定理级]** ✓ |
| 第三型最一般形式 | canonical、$G$-不变、非离散、非二次型定义的凸锥 | **[结构性]** ✓ |
| **角 I 的精确刻画** | **Koecher–Vinberg**：齐性＋自对偶 ⟹ Jordan ⟹ 二次型 ⟹ **双线性可表示** | **[定理级]**（经典）✓✓✓ |
| **第三型存在** | **Choi 非可分解正映射**；$n\ge3$ 正映射锥**非自对偶** ⟹ KV 不适用 ⟹ **逃出角 I**；连续、定号、非扭 ⟹ **逃出角 II** | **[定理级]**（经典）✓✓✓ |
| **三分律判定** | $\text{Third-type}\Longrightarrow\text{I}\cup\text{II}$ **为假** | **[定理级反例]** ✓✓✓ |
| 三角化 | 角 I／II／III；III 的障碍＝宿主／识别 | **[结构性]** ✓ |
| 残差改写 | "是否存在**非双线性可表示**的算术正性？" | **[结构性]** ✓ |

$$\textbf{边界（诚实）}：\text{§1／§2／§4／§5 依赖的经典结果（}U(1)\ \text{不变量理论、}U(1)\text{-torsor、Koecher–Vinberg、Choi 定理与非可分解正映射、正映射锥自对偶仅在}(2,2),(2,3),(3,2)\text{）}\ \textbf{均凭记忆引用，未逐条核对原文} ⚠️✓$$
$$\qquad \text{§3／§6／§7 为}\ \textbf{[结构性]};\ \text{§5 的"∃ 第三型"是}\ \textbf{数学事实}，\text{但"它能否服务 RH"}\ \textbf{完全未触及}（\text{宿主缺失}）⚠️$$
$$\qquad \text{未用 RH 作推导} ✓;\ \text{未跑 Lean} ✓;\ \textbf{零数值} ✓;\ \textbf{零外部检索}（按唐先生指示）✓$$

```
⚠️ 委托（唐先生 20:51 逐字）：不要再扩大外部机制名单，而应攻击"两角二分"本身；必须构造第三型候选公理并证明其是否存在；
  五条 (C1)–(C5)；三刀（gauge 商 ⟹ 回角 I；不商 ⟹ 须 canonical axis；额外结构 A 只能是 bilinear/sesquilinear/quadratic
  ⟹ 角 I，或 finite-order torsion ⟹ 角 II，或连续非线性非度量非 torsion）；任务＝构造第三型最一般代数形式并证明它
  要么自动产生 quadratic form / 要么自动产生 torsion / 要么保留 gauge 自由度；这次直接算、不搜文献
⚠️ §1 Theorem A（定理级）：C[z,z̄]^{U(1)} = C[z_i z̄_j] ⟹ 连续不变 L 由 Gram 矩阵决定 ⟹ 二次型型数据 ⟹ 角 I；
  加强版：纯 U(1) 相位上平移传递作用 ⟹ (C2) 迫使 L 常值 ⟹ 纯相位不带 canonical 实数
⚠️ §2（定理级）：相位本体是 U(1)-torsor，无 canonical 基点 ⟹ 须 canonical 原点/轴 ⟹ V218 S1/S3 + V227-A + V215(c)；
  非 Hermitian 拓扑"线只在旋转下定义"同型
⚠️ §3 第三型最一般代数形式（[结构性]）：canonical、G-不变、非离散、非二次型定义的凸锥（正性锥）
⚠️ §4 Theorem C（定理级，经典）：Koecher–Vinberg —— 有限维实向量空间中齐性自对偶开凸锥 = 某 Euclid Jordan 代数的
  平方锥，带 canonical trace 二次型 ⟹ **角 I 的精确刻画 = "自对偶 = 双线性可表示的正性"**；Weil/Bochner/Hodge 配对
  全部双线性 ⟹ 落角 I 不是巧合而是 KV 推论
⚠️ §5 Theorem D（定理级，经典；决定性反例）：Choi 1975/Woronowicz 1976 —— 正映射锥 P(M_n→M_n) 在 n≥3 时非自对偶且
  含非可分解元素；Choi 定理：φ 完全正 ⟺ Choi 矩阵半正定 ⟹ CP 部分＝双线性可表示；非 CP 的正性＝不可由任何双线性形式
  表示的正性。逐条核对 (C1)–(C5) 全部满足 ⟹ 第三型存在 ⟹ 唐先生三分律 Third-type ⟹ I∪II 为假。
  逃逸点：KV 需齐性+自对偶，而正映射锥非自对偶（n≥3）且非齐性
⚠️ §6 三角化（[结构性]）：角 I 自对偶/双线性正性；角 II 离散/扭；角 III 连续/gauge 不变/确定符号/非自对偶正性锥
  （实例：Choi 非可分解正映射）；III 的障碍不是类型障碍而是宿主/识别
⚠️ §7 重写 polarization 故事：char-p 的 Hodge 指标配对是双线性的 ⟹ 角 I ⟹ 成功；char-0 要么同一件（Weil 正性 ⟹ 循环）
  要么角 III（无算术宿主）⟹ 与 V227 §4 一致；残差改写为可检验形式："是否存在不可由任何双线性形式表示的算术正性？"
  并指出该形式新于"缺 polarization"：指定了类型（非双线性正性）且有现成判定机器（Choi 定理/算子系统/PPT² 型问题）
⚠️ §8 边界：经典结果凭记忆引用、未逐条核对原文；§3/§6/§7 为 [结构性]；"∃ 第三型"是数学事实但"能否服务 RH"完全未触及
  （宿主缺失）；未用 RH；未跑 Lean；零数值；零外部检索
✅ 净产出：① 两刀定理级证实（不变量理论；torsor 论证）② 角 I 由 Koecher–Vinberg 精确刻画为"双线性可表示的正性"
  ③ 第三型存在（Choi 非可分解正映射）⟹ 三分律被反例否证 ④ 两角升级为三角，III 的障碍是宿主/识别
  ⑤ 残差改写为可检验形式："非双线性可表示的算术正性？"
```


---

## 【型标注】（`NEG-REGISTER-1`，2026-09-18 20:1x）

$$\text{本档定级}：\textbf{T-III？待核}\ \text{（框架性重述（待核）：第二刀"须 canonical"是否为引理待核）}✓$$
$$\qquad \text{两刀}：\text{(i) gauge 商}\Longrightarrow\text{二次不变量};\ (ii)\ \text{保留相位}\Longrightarrow\text{须 canonical}✓$$
$$\qquad ⚠️\ \text{第 (ii) 刀}\ \textbf{是引理还是断言} \text{本档未核} \Longrightarrow \text{定级}\ \textbf{暂标 T-III？}✓✓$$
$$\qquad \Longrightarrow \text{若 (ii) 为引理}\ \Longrightarrow \text{可升 T-I/II};\ \text{若为断言}\ \Longrightarrow \text{确为 T-III}✓$$
$$\textbf{引用纪律（本档确立）}：\text{引用本档时必须}\ \textbf{随引其型};\ \textbf{不得} \text{去条件化引用}✓✓$$
