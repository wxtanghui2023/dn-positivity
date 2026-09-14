# 死路地图（**按死因**分类的筛选表）

**用途**：唐先生 SEL1 §12 要求"一套能直接筛掉下一代候选的结构性判据"。本表把已累积的判死结果**按死因**重排，
使任何新候选可以逐行对号，一步看出它落在哪个箱子里。**按轮次**的索引见 `B-SERIES-INDEX.md`。
**建立**：2026-09-11｜**全局约束**：无 $1/2$ 输入｜无递推输入｜无人为权重/范数｜L2 冻结（VERIFIED）

---

## A. 十二个箱子（按死因）
| # | 死因（bin） | 机制签名 | 已落入的实例 | 来源轮次 |
|---|---|---|---|---|
| 1 | **character 箱** | 乘性/加性 character、bicharacter、有限群/torsor | Hilbert/Artin/norm-residue 符号；Rédei 三重符号；cyclotomic/Legendre；**有限阿贝尔 torsor（最小表示空间 N=5）**；Aff(ℤ) 的平移 defect | AOB1, AOB2, AOB5, REP1, B2 |
| 2 | **Euler 化箱** | 是 $(\mathbb N,\times)$ 的真作用 ⟹ $S_n=\prod_p S_{p^k}$（唯一分解推论）| prime-history composition；ABD；δ-ring；逐素数算子 + 局部—整体相容 ⟹ Hecke 化 | D1, AOB4 |
| 3 | **profinite / 全不连通箱** | 离散阶段的逆极限；congruence；Stone/$\beta\mathbb N\setminus\mathbb N$ | 信息损失的 canonical 极限（$\widehat{\mathbb Z}\times$ archimedean profile）；$\operatorname{Spec}(\mathcal G)=\beta\mathbb N\setminus\mathbb N$；**有限阶段永不逃逸**；离散阶段 ⟹ 极限零维（connected 1D 不可能）| E1, G1, AEB1, F1 |
| 4 | **L-值 / 显式公式 / Tate 对偶箱** | 局部—整体 obstruction；$\mathrm{Sha}$ 型核；Massey/高阶上同调 | Ш/类群/Brauer–Manin（其 anomaly 全由 L-值测度）；Iwasawa 塔传播（主猜想）；Massey | E2, AOB2 |
| 5 | **计数 / 熵 / 增长指数箱** | 轨道计数、Lyapunov、谱半径、transfer operator、dynamical zeta | Poincaré 指数 δ；Δ 的熵化；Euclid–Mullin 的增长率；dynamical zeta 类 | D2, AEB1, SEL1, E1 |
| 6 | **谱 / HP 箱（无算术来源）** | 算子本征值，但仍需由 ζ/零点反向定义 | HP；Hecke/$[n]$（canonical element 但代数【交换】⟹ character 谱）；Deninger/Connes（char 0 缺正性）| AOB1, AOB4, E4 |
| 7 | **算术格 / 自守 / modular 箱** | 秩-2 结构 ⟹ SL₂/四元数序 ⟹ 自守影子 | mutation（Markov/Apollonian）；模形式；Bianchi/thin | D2 |
| 8 | **二次型箱** | 二元二次型 / Gaussian 整数 / 类群 | **最小表示空间 $a^2+b^2$（N=5 的共轭对）** | REP1, D2 |
| 9 | **泛性质闭合箱** | completion / localization / free object | 各类 canonical 闭包 | E1, F1, SEL1 |
| 10 | **incidence / 加法组合箱** | 关联矩阵再加工；flag complex | AFAC；CRT 兼容复形（**两两 ⟺ 可解，4000/4000 核验**）；$K_3$；hyperbola | E1, AOB5 |
| 11 | **valuation / divisor / factor-lattice 箱** | 局部因子数据 | divisor-格；valuation 型尺度 | E1, D1 |
| 12 | **极化⟂元素性箱** | 正定（Hodge–Riemann；pure 极化 HS 半单）与"非平凡活动"互斥 | 存在性终审：char 0 无 canonical similitude | AOB4 |

## B. 未关闭者（**只有一处**，四种等价表述）
$$\boxed{\text{单一缺口} = \text{一个【算术特异 + 非 completion + 非 L-测量 + limit-seeing/finite-blind】的机制}}$$
| 表述 | 出处 |
|---|---|
| 需要"非 generic（依赖算术特异性）"的机制 | D3 §4 |
| 需要"第三种不变量"（非 congruence、非 archimedean） | E1 §5 |
| 需要"非分解决定的 $L$"（非计数/误差函数） | E2 §3 |
| 需要"第五个局部化系统"（canonical + limit-seeing/finite-blind + 核非 L-值可测） | E5 §6 |
| 需要"char 0 的 non-triviality 与 positivity 兼容"的来源 | AOB4 §4 |

## C. 本轮新增**结构性事实**（可直接用作筛选判据）
```
F-1【finite-blind ⟂ escape】：逃逸要求无限阶段 ⟹ 与 E4/E5 的 finite-blind 框架不可兼得        [AEB1]
F-2【离散阶段 ⟹ 极限全不连通】：connected 1D 只能是【非单射连续商】(Cantor→S¹)，
     而 canonical 粘合来源仅 character（✗）或 digit/CF（非 canonical ✗）                       [AEB1 附]
F-3【有限阶段永不逃逸】：有限非空集逆系统极限恒非空（FSIP）                                  [AEB1]
F-4【element vs conjugacy class】：char p 的 Frobenius 是【元素】⟹ 可取本征值；
     char 0 只是【共轭类】⟹ 只能取 character/trace ⟹ L-函数。
     ⟹ 全项目反复崩回 character 是【结构强制的】                                              [AOB3]
F-5【极化 ⟂（元素性+动力学+相位）】：E+D+Z 需非刚性；P 需正定                                [AOB4]
F-6【分配律归类而非消灭】：$[\mathrm{Mul}_m,\mathrm{Add}_a]$ = 平移 $a(1-m)$ ⟹ 阿贝尔/
     character 型 ⟹ $(+,\times,\mid)$ 历史边界【无新相位】                                     [AOB5]
F-7【有限盲的 canonical 商 = 无穷远芽】：但 $\mathcal G$ 无 canonical 极限泛函；
     其不变结构 = 环 + 移位；移位不动点 = congruence 数据                                       [G1]
F-8【canonical orientation 不足】：最小表示空间的运输是【有限阿贝尔 torsor】⟹ character 箱     [REP1]
```

## D. 使用方式（对任何新候选的四问）
```
Q1 它是否【非 Euler 化】？       否则 ⟹ 箱 2
Q2 它的不变量是否【非 character】？否则 ⟹ 箱 1（含有限群/torsor）
Q3 它的谱/相位是否来自【算术 canonical 算子】？否则 ⟹ 箱 5/6
Q4 它是否依赖【非 completion、非 L-值、非 generic】的机制？否则 ⟹ 箱 3/4/12
```

---

# E. **方法论校正**：为什么 NO-GO 的累积没有缩小范围（2026-09-11 12:06 唐先生指出）

## E.1 结构性原因（诚实诊断）
```
在【未被枚举的无限空间】上做否定，每次只删掉【一个点】⟹ 可行域大小不变 ⟹ 搜索【不收敛】
本期实况：约 25 轮 ⟹ 实际只建立约 12 个箱 ⟹ 后段大量轮次是【同一批箱的重复推导】
⟹ 唐先生的判断正确：继续加 NO-GO 既没有缩小范围，也没有给出方向
```

## E.2 能真正缩小范围的只有一类东西：**表征定理**
$$\boxed{\text{不是"候选 X 死"，而是"一切候选都属于这 }N\text{ 类"（并给出证明）}}$$
本期唯一具备该形状的对象 = ADC1 的**严格收缩来源分类**。⟹ 正确动作是**攻这张类表**，而不是再加候选。

## E.3 本轮把类表**由 4 类扩到 6 类**（按穷尽性收窄，而非再杀一个候选）
| 类 | 严格收缩从何而来 | 算术实例 | 落入 | 状态 |
|---|---|---|---|---|
| I 不变性/对称 | 须对某作用稳定 | Galois 稳定、congruence | 箱 1 | 关闭 |
| II archimedean/度量 | 须满足增长/大小界 | $M(x)=O(x^{1/2+\varepsilon})$ | 箱 3/5 | 关闭 |
| III 存在性结构 | 须存在 section/lift/极化 | $\mathrm{Sha}$/Brauer–Manin；Hodge 正性 | 箱 4/12 | 关闭 |
| **V 极值/禁止模式** | 须避开某全局模式 | 无平方因子/本原性（**局部** ⟹ 违反 P3）；pair-correlation（**统计** ⟹ 箱 5/β-wall） | 箱 5 或 P3 失败 | **关闭** |
| **VI 可定义性/正则性** | 须【不】可被某语言定义 | Presburger 可定义集 = 最终周期 ⟹ 非周期性条件回到 **congruence** | 箱 1 | **关闭** |
| IV 证明论/一致性强度 | 须由更强公理推出 | $\mathrm{Con(PA)}$ 型 | E4 第三家 | **OPEN（只给可证性）** |

## E.4 于是活的问题**只剩一个**（并且它是收敛的）
$$\boxed{\text{这张类表【是否完整】？即：是否存在一个类表之外的严格收缩来源？}}$$
```
· 找到 ⟹ 一个新方向（且是结构性的，不是候选式的）
· 找不到（且能论证完整性）⟹ 空间【真正关闭】，此时应改变目标而非继续搜索
```
**这才是"能缩小范围"的唯一动作。** 继续枚举候选机制不在此列。


---
---

# F. ⭐⭐⭐ **Fourth-Arrow 总入口（`V128`–`V137`，2026-09-14 归档 ✓）**

> **用途 ✓**：任何新候选若声称提供了**新的 $\sqrt{}$-正性、稳定性、或第四箭头** ⟹ **先走本节，不重走九轮** ✗
> **配套 ✓**：`ARCHIVE-V128-V140-fourth-arrow-and-cross-scale-closure-audit.md`（三条不可越界标签 ＋ 九轮清单 ✓）｜`MASTER` §0.1（J 裁定 ✓）

## F.1 总入口决策树（✓）

$$\boxed{\text{Fourth Arrow}\ \longrightarrow\ \begin{cases}\text{finite-window}&\to\ \text{`V133`}\ ✗\\[1pt]\text{limit program}&\to\ \text{`E104`}\ ✗\\[1pt]\text{trace／operator}&\to\ \text{E104 ②／`L1`／`N0`}\ ✗\\[1pt]\text{canonical object}&\to\ \text{`V135`}\ ✗\ (\text{canonical}\not\Rightarrow\text{stable})\\[1pt]\text{stability}&\to\ D_1\ ✗\\[1pt]\sqrt{\ }\text{-positivity}&\to\ \text{`V136`／G13}\ ✗\\[1pt]\text{O2／O3}^\star\text{／O5}&\to\ \text{`V130`–`V132`}\ ✗\end{cases}}$$
$$\textbf{最终节点统一指向 ✓}：\boxed{R_{\rm residual}=\text{未分类的 char-0 intrinsic polarization/purity mechanism}\ ⚠️}$$

## F.2 ⭐ 最高优先级查重规则（✓ 新候选的**第一问** ✓）

$$\boxed{\text{新候选若声称"新的平方根来源" ⟹ 第一问 ＝ }\textbf{"它的 }\sqrt{\ }\text{ 来自哪里？"}\ ✓（\text{而非"它能不能工作"✗）}}$$
$$\qquad\textbf{强制七箱 ✓}：\text{quadratic/polarization}\ \big|\ \text{finite purity}\ \big|\ \text{statistical}\ \big|\ \text{functional-equation}\ \big|\ \text{spectral}\ \big|\ \text{finite-window/limit}\ \big|\ \text{order/stability}$$
$$\qquad\Longrightarrow\ \text{能归类 ⟹ 直接按对应 route 处理 ✗（不必研究 ✓）};\qquad\boxed{\text{全部不能归类 ⟹ 才允许进入 }R_{\rm residual}\ ⚠️}$$

## F.3 三条不可越界标签（✓ 摘要；详见 ARCHIVE ✓）

$$\textbf{① 已证明 ✓}：\text{具体机制}\Longrightarrow\text{已有 CLOSED route（}V133\ \text{Theorem A ／ }V130\ \text{FE 湮灭 ／ }E104\text{ ② ／ }L1\text{／}N0\ \text{／ }L3\ \text{0/15 ／ }V123\ \text{／ }V135\ \text{三反例 ／ }V136\ \text{(i)–(iv)} ✓）}$$
$$\textbf{② 条件分类 ✓}：\text{canonical}\not\Rightarrow\text{stable}；\text{任何稳定性须支付带符号/序结构（成本落 }D_1\text{）}$$
$$\textbf{③ 未证明 ⚠️（必须保留 ✓）}：R_{\rm residual}\ne\varnothing\ \text{或}\ =\varnothing\ \textbf{均未证明}\ ✗\ \text{—— 不得把"搜索库空了"写成"数学上不存在" ✗}$$

## F.3b 附：**跨尺度兼容 ＋ 缺陷复合律**（`V138` 查图结果 ✓ —— 已独立注册，早于本节 ✓）

$$\text{提案形状 ✓}：\text{Arithmetic}\to\text{irreversible compatibility}\to\text{canonical polarization}\to\text{RH}\ ✓；\text{缺陷复合律 }\Delta_{m,k}=\Delta_{m,n}+\Phi^*\Delta_{n,k}+\mathcal C_{m,n,k}\ ✓$$
$$\textbf{已注册三处 ✓}：\text{`TWO-SCALE-compatibility-construction-material`（同形状 ＋ 同排除表 ＋ 同自警 ✓）；`R-CS-PRE1`（}X0\text{：}T\ne\text{group cocycle}\ \wedge\ T\ne\text{coboundary}\ \textbf{逐字相同 ✓}）；`SCALE-DYNAMICS`（}\Omega(X,Y,Z)=T_{Y,Z}T_{X,Y}-T_{X,Z}\text{ ＝ }\mathcal C\ ✓）}$$
$$\textbf{已测试一次 ✓}：\text{`addmul-defect-test-death`：加法–乘法 defect 谱测试 ⟹ }\lambda_{\min}\text{ 与 }\gamma\text{ 完全无关 ✗ —— 原因 ＝ 【定理 ✓】：}D=|D|U(\gamma)\text{ 酉共轭保谱 ⟹ 对角 }D\text{ 乘两边的构造其谱必与 }\gamma\text{ 无关 ✗✓}$$
$$\textbf{类级状态 ✓}：R_{B4}\ \text{inactive ✗（七项崩塌清单 ✓）；}R_{A\text{-}ind}\ \text{inactive（在本轮规定的 coarse-graining 类中 ✓）}\ ——\ \textbf{但档案自标"}\ne\text{ 所有可能 ✗"，并加粗保留 }\boxed{\textbf{SW6 尚未证明为空}}\ ✓$$
$$\textbf{【}V139\text{ 更新 ✓】材料 A ⟹ 已审 ✓ 退回箱 8；材料 B ⟹ 已审 ✓ 四层塌缩（第 0 层 }\sqrt{|D_K|}\text{ 按定义 ＝ trace pairing Gram 行列式平方根 ⟹ 定义性地 }D_1\text{；第 2 层 }\tfrac12\text{ 非来自维数（应为 }1/d\text{）而来自二次性 ⟹ 违反自身约束 C4 ✗；第 4 层 Brauer–Siegel 下界 ＝ GRH 强度 ⟹ 循环 ✗）⟹ \textbf{三处未执行项中两处已关闭 ✗}；第三处（修复方向）见下行**【}V140\text{ 已审 ✓ 判死】$$$$
$$\textbf{【}V140\text{ ✓】修复方向（固定基缺陷／非对角 transport）⟹ }\textbf{已审 ✗ 判死}：\text{① 相位来源【已穷举】（`AOB1` §2 四源：互反符号／holonomy／2-上闭链 ⟹ character／Fourier–Mellin／L-值 ✗；第四种 Frobenius 型 ＝ 唯一活口但 char-}p\text{ 专属 ✗）；② 本档二分定理：}T\text{ 含 }\gamma\text{ ⟹ 相位 ＝ 算术频率}\times\gamma\text{ ⟹ }\gamma\text{ 是【输入】✗（Mellin 参数型）；}T\text{ 不含 }\gamma\text{ ⟹ 与 }\gamma\text{ 无关 ✗，谱＝}\{\gamma_j\}\text{ 须 HP ⟹ }N0\text{ 循环 ✗ ⟹ "non-diagonal} \ne \text{intrinsically }\gamma\text{-sensitive" 得证 ✓；③ 档案"断裂双重"（}phase\text{-}source\text{-}search\text{）＝ Gate A（相位来源）＋ Gate B（权-1 宿主），Spec }\mathbb Z\text{ 两者皆缺、}\mathbb F_q\text{ 两者皆有且【同源】（similitude }\Phi^\dagger Q\Phi=qQ\text{）⟹ 原型里两门是一门 ✗ ⟹ }\textbf{V138 三处未执行项全部关闭 ✓}$$
$$\boxed{\textbf{三处未执行 ⛔}}（各附前置问 ✓）：\text{① 材料 A（不变因子双尺度：指数 }N\text{ 的子格／二次型／理想类）⟹ 前置问：是否退回箱 8／12？}\ \text{② 材料 B（数域余体积 }\sqrt{|D|}\text{ vs 类数 }h\text{）⟹ 前置问：} \sqrt{|D|}\text{ 是【推出】的还是【输入】的？}\ \text{③ 修复方向（固定基缺陷／非对角 transport）⟹ 前置问：能否用【纯算术】给出该相位而不用零点？}}$$

## F.3c 附：**Lorentzian 多项式 / ξ-Jensen / 双曲性路线**（`V141`–`V142` ✓）

$$\textbf{新闻 ✓（`V141`）}：\text{arXiv:}2609.05341\ \text{"Bounded ratios for Lorentzian polynomials"}\ ✓（\text{AI 协助 ✓；}\text{Huh 二次情形 ⟹ 任意次数，由离散凸性决定 ✓）$$
$$\textbf{本档审计结论 ✓（`V142`）}：\text{① 一元 Lorentzian}\iff\text{非负}\ \wedge\ \text{支撑区间}\ \wedge\ \text{Newton／超对数凹 ✓；② }\textbf{Lorentzian}\not\Rightarrow\textbf{hyperbolic}\ ✗（反例 }t^3+3t^2+3t+3\ ✓）⟹\ \text{弱于 RH ✓；③ ξ-Jensen 的超对数凹部分}\textbf{已被 GORZ 无条件蕴含} ✓✓；④ 剩余差距（Lorentzian ⟹ 双曲）＝ RH 所在 ✗；⑤ 整条双曲性路线}\textbf{已由 Farmer（}arXiv\text{:}2008.07206\text{）关闭} ✓✓\ \text{（档案 }`ALIGN-A2`\ ✓）}$$
$$\boxed{\text{故 Lorentzian 路线落 A2 已封格 ✗；不填补 }R_{\rm residual}\ ✓}\qquad\textbf{⭐ 附带 ✓}：T^2\ \text{律在此独立出现（}d\le T^2\ ✓\text{）⟹ }W3\ \text{独立确认 ✓✓}$$

## F.5 ⭐⭐⭐ **总收束节点：Fourth Arrow / Cross-scale ⟹ $R_{\rm residual}$**（`V138`–`V140` ✓）

$$\boxed{\text{Fourth Arrow / Cross-scale}\ \Longrightarrow\ R_{\rm residual}}$$
$$\qquad\textbf{四条支路 ✓}：\begin{array}{c}\text{二维 lattice／invariant-factor}\ \xrightarrow{\ V139\ }\ \text{quadratic／discriminant}\\[1mm]\text{number-field／ideal-class}\ \xrightarrow{\ V139\ }\ \text{Gram determinant／analytic class-number}\\[1mm]\text{fixed-basis non-diagonal transport}\ \xrightarrow{\ V140\ }\ \text{phase source}\end{array}$$
$$\qquad\textbf{最终全部落到 ✓}：\boxed{R_{\rm residual}=\underbrace{\text{char-0 Frobenius substitute}}_{\text{Gate A：相位来源}}+\underbrace{\text{weight-1 host}}_{\text{Gate B：}\beta=\frac12}}$$

### F.5b 最终双门图（✓ `V140` ✓）
$$\boxed{\begin{array}{ccc}\text{Spec }\mathbb Z\\[1mm]\downarrow\\[-1mm]\underbrace{\text{arithmetic}}_{\text{输入}}&\xrightarrow{\ \text{Gate A}\ }&\underbrace{\gamma}_{\text{phase}}\\[2mm]&&\downarrow\text{ Gate B}\\[1mm]&&\underbrace{\beta=\frac12}_{\text{weight}}\end{array}}$$
$$\textbf{函数域 ✓}：\Phi^\dagger Q\Phi=qQ\ \Longrightarrow\ |\alpha|=\sqrt q,\ \alpha=\sqrt q\,e^{i\theta}\ \Longrightarrow\ s=\frac12+\frac{i\theta}{\log q}\ \Longrightarrow\ \boxed{\text{模}\Rightarrow\frac12,\quad\text{辐角}\Rightarrow\gamma}$$
$$\qquad\text{—— 在函数域它们}\textbf{不是两个独立机制}，而是\textbf{同一个 Frobenius eigenvalue 的 modulus ＋ phase} ✓✓$$
$$\textbf{Spec }\mathbb Z\ ✓：\boxed{\text{weight-1 host}\ \textbf{缺}}\qquad\boxed{\text{arithmetic Frobenius}\ \textbf{缺}}\ \Longrightarrow\ \textbf{两个独立结构缺口} ✓$$

### F.5c 档案纪律（✓ 唐先生 2026-09-14 23:32 指示 ✓ **必守** ✓）
$$\boxed{R_{\rm residual}\ \text{是【当前审计体系下唯一未关闭的机制类别】}\ ✓}\qquad\textbf{而不是}\qquad\boxed{\text{"不存在其他机制"}\ ✗}$$
$$\qquad\text{理由 ✓}：\text{穷举的是}\textbf{当前定义的 phase-source taxonomy}，\textbf{不是数学宇宙} ✗✓$$

### F.5d ⭐ 下一阶段准入闸 **C1–C5**（✓ 唐先生 2026-09-14 23:34 ✓ **冻结基线** ✓）
$$\boxed{\text{唯一问题 ✓}：\textbf{C1–C5 在特征零是否存在非平凡实例？}}\ \Longrightarrow\ \text{不存在 ⟹ 更强结构性负结果 ✓；存在 ⟹ 才有资格问是否指向 RH ✓}$$
$$\boxed{\begin{aligned}\mathrm{C1}&:\ \text{char-0 canonical arithmetic action}\\[1mm]\mathrm{C2}&:\ \text{similitude}\ \Phi^\dagger Q\Phi=\lambda Q\\[1mm]\mathrm{C3}&:\ \text{weight-1 normalization}\ |\lambda_{\rm eig}|=\sqrt{\lambda}\\[1mm]\mathrm{C4}&:\ \text{phase}\ \arg(\lambda_{\rm eig})\ \text{内生且非零点输入}\\[1mm]\mathrm{C5}&:\ \text{C1–C4 来自}\textbf{同一个 canonical object}，\textbf{非事后拼接}\end{aligned}}$$
$$\qquad\textbf{映射 ✓}：\mathrm{C2}{+}\mathrm{C3}\ \text{＝ Gate B（模 ⟹ }\beta{=}\tfrac12\text{）};\quad\mathrm{C1}{+}\mathrm{C4}\ \text{＝ Gate A（辐角 ⟹ }\gamma\text{）};\quad\textbf{C5 ＝ 两门同一把钥匙} ✓$$
$$\qquad\textbf{禁用 ✗}：\text{再沿 cross-scale／fixed-basis／transport 线搜索（`V138`–`V140` 已关闭 ✓）；}\textbf{不再造路线地图} ✓$$
$$\boxed{\textbf{V128–V140：搜索边界已冻结} ✓\qquad \text{下一阶段 ＝ 新数学对象的构造 ＋ 逐条件审计} ✓}$$

### F.5e ⭐ NO-GO 总图再核查：**四方向**（`V143` ✓ 2026-09-14 23:39）

| 方向 | 判定 | 依据 |
|:--|:--|:--|
| **① char-0 Frobenius 影子** | **已封 ✗（结构性 ✓✓）** | `AOB3` §1：**element vs 共轭类**（char $p$ pro-cyclic 有 canonical 生成元 ⟹ 可取本征值，同时带模 $\sqrt q$ ＋ 辐角 $\theta$；char 0 的 Frobenius 只是**共轭类** ⟹ **无 canonical 取本征值方式** ✗）；`AOB4` §1：**E/D/Z ⟂ P**（非交换非刚性 vs 正定 ＝ Hodge–Riemann ＝ pure 极化 HS **半单**，char 0 中**互斥** ✗）；`E100` ③ ＋ `rct-four-layer-final` 逐字"purity 载体（Frobenius／HP／Weil——全封——）死" |
| **② Arakelov $\infty$-place operator** | **已封 ✗** | `ESC2` §1–§2：档案已自我更正（"正性只能住紧致部分"**错** ✗；Arakelov 已含 archimedean 位，Faltings–Hriljac 负定 ⟺ Néron–Tate 正定 ✓）；**真正障碍 ＝ no common carrier**（正性在**除子／几何侧**，谱数据在**谱侧** ⟹ 无可比性 ✗）；`MASTER` G9：Arakelov R6 **尺度失败** ⟹ 输出 height／log（非幂律 $\sqrt X$）✗ |
| **③ 新 weight-1 arithmetic cohomology** | **已封 ✗** | 箱 7（秩-2 ⟹ 自守影子 ✗）／箱 8（二次型 ✗）／箱 12（极化 ⟂ 元素性 ✗）；`ix-arithmetic-realization`：所需条件已登记 ＝ "arithmetic object $M$ ＋ **可独立证明**的 weight／degree law" ✓ —— 而"可独立证明"**正是 C2／C3 的难点** ✓ |
| **④ 模＋相位同源对象** | **＝ $R_{\rm residual}$ 正向侧 ⛔（已登记、未执行）** | `AOB3` §4 逐字"char 0 【没有】canonical arithmetic similitude"✗（两独立理由 $\alpha/\beta$）；**`AOB2` 登记项与 C1–C5 逐字同形** ✓✓：$(X_n,F_n,\Phi_n,J_n)$ with $\Phi_n^\dagger J_n\Phi_n=N_nJ_n$、$\operatorname{Spec}\subset\sqrt{N_n}S^1$、phase internally generated by same polarization、**non-$L$-function-ized** ✓；`AOB4` §0 已**规定正确形状**（prime ＝ 状态的 observable／事件，非独立算子；canonical element 属于**状态演化 $F$** ✓） |

$$\boxed{\text{四方向全部已在图中 ✓ —— ①②③ 已封 ✗；④ ＝ 我们刚冻结的 }R_{\rm residual}\ \text{正向侧（已登记 ⛔ 未执行）}\ \Longrightarrow\ \textbf{无新入口 ✗，但正向构造任务活着 ⛔}}$$
$$\qquad\text{四陷阱 ↔ 档案 ✓}：\text{(a) }\Phi_\infty\ne\text{拼接}\to AOB4\ \text{§0 ✓};\ \text{(b) }\infty\text{-Fr}\ne e^{it\log p}\text{／Mellin}\to AOB1\ \text{§2 ＋ }V140\ ✓;\ \text{(c) 不能先写 }\zeta(s)\to AOB1\ \text{§4 的 }A6'\ ✓;\ \text{(d) 塞 }L\text{-函数 ⟹ 违 C5}\to AOB3\ \text{§4 ✓}$$

### F.5f ⭐⭐⭐ **层诊断：motive 层 vs Archimedean 层**（`V144` ✓ 2026-09-14 23:47；档案原诊断 2026-09-02 ✓✓）

$$\boxed{\text{ζ 的局部 Frobenius 本征值}\ \alpha_p\equiv1\（\textbf{平凡 motive}）\ \Longrightarrow\ \textbf{相位通道在每个有限处为空}\ ✗\ \text{且}\ \textbf{局部 }q_v\equiv1\ \text{无 }\sqrt{}\text{-尺度}\ ✗}$$
$$\qquad\text{（逐字依据 ✓：`thought-experiment-generator-M`："ζ 的 Euler 积局部因子 }(1-p^{-s})^{-1}\ \text{的'Frobenius 特征值'}\ \alpha_p=1\（\text{平凡！}\text{）—— }\zeta\ \text{是平凡 motive —— Euler 积无临界带零点 —— 零点是解析延拓的产物"✓）}$$
$$\boxed{\text{函数域}\textbf{平凡 motive 的 }L\ \textbf{无零点}（\zeta_C(u)=\tfrac1{(1-u)(1-qu)}\ \text{纯极点}\ ✓）\ \text{而 char-0 的 }\zeta\ \text{有非平凡零点} \Longrightarrow\ \text{差异 ＝ }\textbf{Archimedean 结构}（\Gamma／\xi\ \text{整性}\ ✓）}$$
$$\boxed{\textbf{ζ 零点（和 RH）不在 motive 层 —— 在 Archimedean 层}\ ✓✓（`iteration-independent-wplane-archimedean` 方向 B ✓）}$$
$$\boxed{\textbf{元解释 ✓✓✓}：\text{为什么所有 Frobenius／几何类比失败 —— }\textbf{层错了}（\text{作用在 motive 层，零点在 Archimedean 层}）}$$
$$\qquad\Longrightarrow\ \textbf{C6（＝"延拓的算术替代物"，`thought-experiment-generator-M` 第 5 步逐字 ✓）的死因 ＝ 层结构} ✗：\text{motive 层}\textbf{不可能};\ \text{Archimedean 层}\textbf{已知仅自伴 ⟹ }HP\ \text{循环} ✗（`iteration-2-5`：}\textbf{机制真空} ✓）$$
$$\qquad\textbf{同时已封 ✓}：\text{Sato–Tate／Hecke 局部统计 ⟹ }\textbf{L3 死}（`dstar-ec-death` ✓；`RESEARCH-CONSTITUTION` N15 ✓）；\text{Gaussian／CM 同源模+相位 ⟹ }\textbf{箱 8} ✓$$

### F.5g ⭐ **Archimedean 边界对象：三关审计**（`V145` ✓ 2026-09-14 23:52）

$$\text{提案 ✓}：\text{找"Archimedean arithmetic boundary object"}\ \mathcal B_\infty\ \text{＋ 边界耦合}\ \mathcal E:\mathcal A_{\rm fin}\to\mathcal B_\infty\ ✓,\ \text{使}\ \Lambda(s)\sim\det_{\rm ren}(I-\mathcal E(s))\ ✓（\text{零点 ＝ compatibility failure}\ ✓）$$
$$\boxed{Gate\ 1\ \textbf{通过 ✓ 且经典 ✓}}：\pi^{-s/2}\Gamma(s/2)\ \text{可由}\ \theta(1/t)=\sqrt t\,\theta(t)\（\mathbb Z\ \text{泊松自对偶}\ ✓）\ \text{＋ Mellin ＋ Tate 局部积分生成}\ ✓\ \text{—— 形状由三事实决定（Gaussian 自对偶}\ \widehat{e^{-\pi x^2}}=e^{-\pi x^2}\ ✓;\ \mathbb Z\ \text{自对偶格}\ ✓;\ \text{局部 ζ 积分}\ ✓）,\ \textbf{不碰 }\zeta,\Lambda,\rho,\gamma\ ✓$$
$$\boxed{Gate\ 2\ \textbf{失败 ✗}}：\text{档案逐字（`iteration-2-5` 第 2 轮 ✓）：}\zeta\ \text{站在}\textbf{乘法离散}＋\textbf{加法离散} \text{之间；}\textbf{加法侧（}\theta\text{／泊松）通回 }\zeta \Longrightarrow \text{同一延拓对象 ⟹ 非独立 ⟹ 循环}\ ✗✓$$
$$\boxed{Gate\ 3\ \textbf{结构性失败 ✗}}：\text{FE 是}\textbf{对称性}（\rho\leftrightarrow1-\rho\ ✓）；\text{对称性}\textbf{不强制固定轨迹}、\text{允许离轴对}\ ✗（\text{M-公理表：FE／duality}\ \textbf{安全}\ ✓）$$
$$\boxed{\text{⭐ 关键命中 ✓}：\det_{\rm ren}(I-\mathcal E(s))\ \textbf{＝ Deninger 纲领};\ \text{档案（`V105` 第 6 行 ✓）判：有 canonical 生成元}\ ✓\ \text{但}\textbf{缺 canonical polarization（正定相交形式）}\ ✗\ +\ \textbf{局部 similitude 只看得见 }\sigma>1\ \text{的 Euler 窗口（算术断裂）⟹ 看不到零点}\ ✗;\ \text{命中箱 6／12；状态 }\textbf{CLOSED*};\ \text{配套 `connes-2026-full-audit`（}\text{未产生独立于 Weil 显式公式的 }\beta\text{-障碍}\ ✓\text{）}$$
$$\qquad\Longrightarrow\ \text{三关结论 ＝ }\textbf{有限／无限层断裂 ＋ 有完成函数机制但无 RH 强制力} \text{两者同时成立}\ ✓;\ \text{并核对：}J\text{-unitary}\not\Rightarrow|\lambda|=1\ ✗（\text{不定度量下 }\lambda=r,\lambda'=r^{-1}\ ✓），\text{与 `AOB4` §1 的 E/D/Z}\perp\text{P 同向}\ ✓$$

### F.5h ⭐ **Iterated Arithmetic Action（$F_N^2=N R_N$，$R_N^\dagger R_N=I$）**（`V146` ✓ 2026-09-14 23:58）—— **DEAD** ✗

$$\text{命题 ✓}：\text{用}\ F_N^2=N\,R_N\ \text{（迭代律）替代}\ F^\dagger JF=NJ\ \text{（二次型），以求}\ \sqrt N\ \text{不经 determinant／Gram／polarization ✓}$$
$$\textbf{① 形式区分真实 ✓}：F=\begin{pmatrix}0&N\\1&0\end{pmatrix}\ \text{满足}\ F^2=NI\ \text{但}\ F^\dagger F=\operatorname{diag}(1,N^2)\ne NI\ ✓;\ \text{且}\ F^2=NR\ \text{自动给}\ |\lambda|=\sqrt N\ ✓$$
$$\textbf{② 但包含方向相反 ✗}：F^\dagger F=NI\ \Longrightarrow\ F=\sqrt N\,U\ \Longrightarrow\ F^2=N\,U^2\（U^2\ \text{酉}\ ✓）\ \Longrightarrow\ \textbf{迭代条件是 similitude 的【推论】，严格更弱} ✗✓$$
$$\textbf{③ "}R_N\ \text{酉"}\ \Longleftrightarrow\ \text{存在正定形式}\ \Longrightarrow\ \text{困难被}\textbf{搬回} char-0 canonical polarization 缺口\ ✗✓（\text{箱 12；`AOB4` §1：E/D/Z}\perp\text{P}）$$
$$\textbf{④ ⭐⭐⭐ 档案命中 ✓}：`p41-g1-unitary-factorization`（2026-09-02）＝ 同类，\textbf{已判死} ✓✓：$$
$$\qquad\textbf{消零定理 ✓}：S(w)=\frac{\zeta(\frac12-w)}{\zeta(\frac12+w)}\xrightarrow{FE}\chi(\tfrac12-w)\ \Longrightarrow\ \textbf{ζ 零点在比值中完全消掉} ✗;\ \text{"比值型 unitary 不可能携带零点"} ✓$$
$$\qquad\textbf{反例 ✓}：S=\frac{w-a}{w+a}\（a\ \text{实}）：S(-w)=1/S(w)\ ✓,\ |S(it)|=1\ ✓\ \text{但}\ \textbf{极点在实轴非虚轴} ✗✓\ \text{—— 与"}\ J\text{-unitary}\not\Rightarrow\text{单位圆"构成【两方向对称】（酉不约束位置 ✓）}$$
$$\qquad\text{inner-outer 循环 ✓；Hardy 类障碍 ✓}\ \Longrightarrow\ \text{判词逐字："与 }\beta\text{-wall }\textbf{同深度};\ \text{global factorization rigidity 未出现"}\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{DEAD} ✓}\qquad\textbf{残余（与 `V145` 一致 ✓）}：\text{非交换跨 }N\ \text{兼容律 ＝ }\textbf{SW6}\ ⛔\ \text{（未证明为空 ✓）}\ +\ \text{char-0 canonical polarization ⛔}$$

## F.4 与 §E.4 的关系（✓）

$$\text{§E.4 的活问题 ✓}：\text{"类表（六类）【是否完整】？"}\qquad\text{本节的回答 ✓}：\text{在【第四箭头}／\sqrt{\ }\text{-正性}／\text{稳定性】这三条具体支线上已给出}\textbf{逐项封闭} ✓\ \text{与}\textbf{一个命名残量} ⚠️$$
$$\qquad\Longrightarrow\ \text{本节}\textbf{不} \text{回答 §E.4 的完整性问题 ✗ —— 二者是同一缺口的两个视角 ✓}$$
$$\boxed{\textbf{V137 ＝ SEARCH BRANCH CLOSED}\ ✓\qquad\ne\qquad\text{RH CLOSED}\ ✗}$$
