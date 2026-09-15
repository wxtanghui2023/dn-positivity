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
$$\qquad\Longrightarrow\ \textbf{C6（＝"延拓的算术替代物"，`thought-experiment-generator-M` 第 5 步逐字 ✓）的死因 ＝ 层结构} ✗：\text{motive 层}\textbf{不可能};\ \text{Archimedean 层}\textbf{已知仅自伴 ⟹ }HP\ \text{循环} ✗（`iteration-2-5`：\textbf{机制真空} ✓）$$
$$\qquad\textbf{同时已封 ✓}：\text{Sato–Tate／Hecke 局部统计 ⟹ }\textbf{L3 死}（`dstar-ec-death` ✓；`RESEARCH-CONSTITUTION` N15 ✓）；\text{Gaussian／CM 同源模+相位 ⟹ }\textbf{箱 8} ✓$$

### F.5g ⭐ **Archimedean 边界对象：三关审计**（`V145` ✓ 2026-09-14 23:52）

$$\text{提案 ✓}：\text{找"Archimedean arithmetic boundary object"}\ \mathcal B_\infty\ \text{＋ 边界耦合}\ \mathcal E:\mathcal A_{\rm fin}\to\mathcal B_\infty\ ✓,\ \text{使}\ \Lambda(s)\sim\det_{\rm ren}(I-\mathcal E(s))\ ✓（\text{零点 ＝ compatibility failure}\ ✓）$$
$$\boxed{Gate\ 1\ \textbf{通过 ✓ 且经典 ✓}}：\pi^{-s/2}\Gamma(s/2)\ \text{可由}\ \theta(1/t)=\sqrt t\,\theta(t)\（\mathbb Z\ \text{泊松自对偶}\ ✓）\ \text{＋ Mellin ＋ Tate 局部积分生成}\ ✓\ \text{—— 形状由三事实决定（Gaussian 自对偶}\ \widehat{e^{-\pi x^2}}=e^{-\pi x^2}\ ✓;\ \mathbb Z\ \text{自对偶格}\ ✓;\ \text{局部 ζ 积分}\ ✓）,\ \textbf{不碰 }\zeta,\Lambda,\rho,\gamma\ ✓$$
$$\boxed{Gate\ 2\ \textbf{失败 ✗}}：\text{档案逐字（`iteration-2-5` 第 2 轮 ✓）：}\zeta\ \text{站在}\textbf{乘法离散}＋\textbf{加法离散} \text{之间；}\textbf{加法侧（}\theta\text{／泊松）通回 }\zeta \Longrightarrow \text{同一延拓对象 ⟹ 非独立 ⟹ 循环}\ ✗✓$$
$$\boxed{Gate\ 3\ \textbf{结构性失败 ✗}}：\text{FE 是}\textbf{对称性}（\rho\leftrightarrow1-\rho\ ✓）；\text{对称性}\textbf{不强制固定轨迹}、\text{允许离轴对}\ ✗（\text{M-公理表：FE／duality}\ \textbf{安全}\ ✓）$$
$$\boxed{\text{⭐ 关键命中 ✓}：\det_{\rm ren}(I-\mathcal E(s))\ \textbf{＝ Deninger 纲领};\ \text{档案（`V105` 第 6 行 ✓）判：有 canonical 生成元}\ ✓\ \text{但}\textbf{缺 canonical polarization（正定相交形式）}\ ✗\ +\ \textbf{局部 similitude 只看得见 }\sigma>1\ \text{的 Euler 窗口（算术断裂）⟹ 看不到零点}\ ✗;\ \text{命中箱 6／12；状态 }\textbf{CLOSED*};\ \text{配套 `connes-2026-full-audit`（}\text{未产生独立于 Weil 显式公式的 }\beta\text{-障碍}\ ✓\text{）}}$$
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

### F.5i ⭐⭐ **Arithmetic One-Sidedness（序路线）**（`V147` ✓ 2026-09-15 00:02）—— **不存在** ✗

$$\text{提案 ✓}：\text{SW6 ＝ involution ＋ odd defect ＋ }\textbf{one-sided arithmetic law}（\text{非二次正定 ✓}）;\ \text{用 }\iota\text{-反转型序 ⟹ 不动点 ⟹ }\Re\rho=\tfrac12\ ✓$$
$$\boxed{\textbf{T1（本档 ✓）}\ \text{全预序 ＋ 保序}\ \iota\ \Longrightarrow\ x\sim\iota(x)\ \forall x\ \Longrightarrow\ \textbf{不存在严格单边律}\ ✗;\ \text{若为全}\textbf{序}\ \Longrightarrow\ \iota=\mathrm{id}\ \text{与非平凡性矛盾} ✗✓}$$
$$\qquad\text{（注 ✓：原论证需【保序】而非"反转"，且需【全序性】；修正后结论更强 ✓）}$$
$$\boxed{\textbf{T2（经典 ✓）}\ \text{与}\ +,\times\ \text{兼容的}\ \mathbb Z\ \text{序}\ \textbf{唯一 ＝ 标准序}（1\in P\Rightarrow n\in P;\ k<0\ \wedge\ k\in P\Rightarrow \pm k^2\in P\Rightarrow k^2=0\ ✗）\ \Longrightarrow\ \text{看不到零点} ✗✓}$$
$$\boxed{\textbf{类 VI（档案 ✓）}\ \text{Presburger 可定义集 ＝ 最终周期 ⟹ 回到 congruence ⟹ }\textbf{箱 1} ✗\ \text{（可定义型结构全封 ✓）}}$$
$$\qquad\textbf{配套 ✓}：\text{箱 11（valuation／divisor ✗）＋ 箱 10（incidence／加法组合 ✗）⟹ 您 §8 三分（Archimedean／valuation／divisibility）三支皆封 ✓}$$
$$\Longrightarrow\ \boxed{\text{SW6}\ \textbf{≠ 序型} ✓（\text{新增排除 ✓）};\ \text{SW6 形态压缩为"}\text{既非 involution-only ✗（}p41\text{ 消零定理）／非 unitary 分解 ✗／非 order／preorder ✗（T1）／非 }+,\times\text{-兼容序 ✗（T2）／非可定义型 ✗（类 VI）／非正定型 ✗（箱 12）"},\ \text{而该剩余}\textbf{仍未被证明非空} ⛔}$$

### F.5j ⭐⭐⭐ **Canonical Orientation-Torsor（select 范式）**（`V148` ✓ 2026-09-15 00:08）—— **三关全死** ✗

$$\textbf{G1 ✗}：\text{真的 }C_2\text{-torsor}\ \textbf{按定义} \in H^1(-,\mathbb Z/2)\ \text{（分类定理 ✓）} \Longrightarrow \text{orientation ＝ torsor ＝ }H^1\ \text{类} \Longrightarrow \text{quadratic／character} ✗（\text{箱 1／8}）$$
$$\qquad\textbf{高阶逃逸双封 ✓}：\text{(i) spin（}H^2\text{）／anomaly（}H^3\text{）⟹ 2-上闭链／Brauer ⟹ }\textbf{L-值} ✗（`AOB1` §2(3)）；\text{(ii) }\textbf{CRT 兼容复形 ＝ flag complex ⟹ 无三体/四体 obstruction} ✗（`AOB5` 4000/4000 ✓）$$
$$\textbf{G2 ✗（≡ G1）}：\text{"局部有定向但}\textbf{无全局截面}"\ \textbf{恰是非平凡 }H^1\ \text{类的定义} ✓ \Longrightarrow \text{无独立内容} ✓$$
$$\textbf{G3 ✗}：\text{"orientation"}\textbf{按定义} ＝ \text{结构群缩减（}O\to SO\text{）}＝\mathbb Z/2\text{-torsor} ⟹ \text{死} ✗$$
$$\boxed{\textbf{⭐⭐ 本档核心定理 ✓}：\text{RH}\iff\iota:\rho\mapsto1-\bar\rho\ \textbf{无自由轨道};\ \text{而 canonical symmetry-breaking ＝ 平凡化该 torsor} ⟹ H^1 ⟹ \text{quadratic} ⟹ }\textbf{select 范式与 RH 的陈述类型不匹配} ✓✓\（\text{RH ＝ "无自由轨道"（全局·缺席型）；select ＝ "在轨道中选一个"（局部·选择型）}）$$
$$\boxed{\textbf{⭐ 三形状皆闭 ✓}：\text{invariant ✗（只见 }\delta^2／|\delta|\text{，无方向）／select ✗（（本行））／size ✗（}T^2\text{／}\log\ \text{墙，W3／W4）}}$$
$$\textbf{档案决定性 ✓}：`AOB4` §2 逐字二分 —— char 0 中 canonical 对象：\text{① 交换谱化（Hecke／}[n]\text{）⟹ }L\text{-函数 ✗；② 不可全局极化（mixed：Galois／GT／MZV）⟹ 无 similitude ✗；③ pure＋polarizable ⟹ }\textbf{无 canonical element} ✗ ⟹ \textbf{存在性终审：不存在}；\ \textbf{差别不在 Frobenius，而在【非平凡性的来源】}（char $p$ 来自\textbf{元素}；char 0 只能来自\textbf{扩展}）✓✓$$
$$\qquad\textbf{配套 ✓}：`S9-strict` 第二支箭不成立（\theta=0\Rightarrow a=b ✗，反例 \theta=(a-b)g(a+b)）—— 与 `V147` §1 同型：forcing／selection 论证总需额外假设，而那些假设正是被封闭处 ✓$$

### F.5k ⭐⭐⭐ **证明形状审计（Fourth Proof-Shape Audit）**（`V149` ✓ 2026-09-15 00:14）

$$\text{三形状复核 ✓}：\textbf{(A) invariant} ⟹ \text{只见 }\delta^2／|\delta|\ ⟹ \textbf{无方向} ✗;\ \textbf{(B) selection} ⟹ \text{平凡化 }\mathbb Z/2\text{-torsor} ⟹ H^1 ⟹ \text{quadratic} ✗（`V148`）；\ \textbf{(C) size} ⟹ T^2／\log\ \text{墙} ✗（W3／W4／L3）$$
$$\qquad\textbf{映射 ✓}：\text{三形状} \cong §E.3\ \text{类表的 }\{I／II,\ III,\ II\}\ ✓\ \text{（III ＝ 存在性结构 ＝ selection，档内已标关闭 ✓）}$$
$$\boxed{\textbf{⚠️ "三形状穷尽" 为假 ✗}}：§E.3\ \text{类表为}\textbf{六类} —— \text{I／II／III／V／VI \textbf{关闭} ✗；}\textbf{IV 证明论／一致性强度 ＝ OPEN} ⚠️\ \text{（但"只给可证性 ⟹ 【不能】承载谱" ✗）}$$
$$\boxed{\textbf{⭐⭐ 且 §E.4 逐字就是同一问题} ✓✓}：\text{"于是活的问题【只剩一个】：这张类表【是否完整】？找到 ⟹ 新方向；找不到（且能论证完整性）⟹ 空间【真正关闭】，此时应}\textbf{改变目标而非继续搜索}\text{"}\ +\ \text{§E.2："能真正缩小范围的只有【表征定理】"}$$
$$\textbf{候选形状 (D) 形变／连续性型 ⚠️（闭环为循环）}：\text{de Bruijn–Newman：RH}\iff\Lambda\le0\ ✓,\ \Lambda\ge0\ \text{无条件（Rodgers–Tao）},\ \text{上界 }0.22\ \text{（Polymath 15）} ⟹ \text{要证 }\Lambda\le0\ \text{即证 RH ⟹ 循环} ✗;\ \text{char-}p\ \text{transfer ✗（}E100／F\text{-4}）；\ \text{热流 ✗（}p11／V123\text{）}$$
$$\textbf{候选形状 (E) 传播／级联型 ⚠️（铰链未封，但产出判据 ⟹ 已封 ✗）}：\neg\text{RH}\Rightarrow\text{稠密}\Rightarrow\text{矛盾}\ ✓;\ \textbf{E47 铰链"一个离轴零点是否迫使离轴谱稠密"＝ 未封} ⚠️✓;\ \text{但 (E) 把 RH 改写为"离轴集不稠密"（与 RH 等价 ⟹ 新判据）} ⟹ \text{落 }E106\ \text{（判据空间 ＝ 正性 ∪ 求和 ⟹ 封闭）✗};\ \textbf{诚实标注}：\text{(E)＋无条件"几乎全部在线上"}\Rightarrow\text{RH}，\text{但该输入未证（已知仅正比例：Selberg／Conrey }\ge2/5\text{）} ⟹ \text{(E) 单独不充分} ✗$$
$$\boxed{\text{闭合陈述 ✓}：\text{就"}\textbf{能承载零点谱}\text{"的形状而言，空间}\textbf{已闭合} ✓\ \text{（I／II／III／V／VI 五闭 ＋ (C)(D)(E) 闭）；两处缺口 ⚠️ ＝ 类 IV（元的，不承载谱）＋ §E.4 类表完整性（未证）}}$$

### F.5l ⭐⭐⭐ **Well-foundedness / Infinite-Descent（第七类候选）**（`V150` ✓ 2026-09-15 00:22）—— **不成立** ✗

$$\textbf{W1 ✗}：\textbf{WF}\subseteq\mathrm{II}\cup\mathrm{IV}\ ✓✓\ \text{—— Mostowski／rank 定理：}\text{良基}\iff\exists\ \text{秩} ⟹ \text{"无限下降"}\textbf{不是新逻辑原子};\ \text{秩值域二分}：$$
$$\qquad\text{(i) }\mathbb N\text{-型／度量型（标准序（}T2\ \text{唯一）／}\log|n|／\omega(n)／\text{height）}\ \Longrightarrow\ \textbf{归 II} ✗;\qquad\text{(ii) 超限序数型 ⟹ 强度 ＝ }\textbf{证明论序数}\ \Longrightarrow\ \textbf{归 IV} ✓✓\（\text{Gentzen：}\mathrm{Con(PA)}\iff\varepsilon_0\ \text{良基} ✓）$$
$$\textbf{W2 ✗}：\text{算术 rank 被 }\textbf{Π}_1\ \text{论证【整族】排除} ✓✓\ —— `E4` §2 逐字：\text{Robin 定理（RH}\iff\sigma(n)<e^\gamma n\log\log n\ \forall n>5040\text{，逐项可判定）}\Longrightarrow\text{RH 是 }\Pi_1\Longrightarrow\neg\text{RH}\ \text{有【有限见证】}n_0;$$
$$\qquad\text{算术完备的可观察系统 ⟹ 对 }B_R\ge n_0\ \text{的层有限层 obstruction 本应非零 ⟹ 与"每层严格平坦"矛盾} ⟹ \textbf{必须对 Robin 型见证盲目} ⟹ \text{anomaly 必须由}\textbf{解析／上同调} \text{定义} ✗✓;$$
$$\qquad\text{且候选 height 本身 ＝ 正定二次型 ⟹ 箱 8／12 ✗；Arakelov height ⟹ G9 }\textbf{尺度失败}（\text{height／}\log\ \text{非 }\sqrt X\text{）✗}$$
$$\textbf{W3 ✗}：\neg\text{RH}\ \text{给【有限见证（非无限）】};\ \text{下降需 canonical 单边映射 ⟹ }\textbf{V147 T1 已封} ✗;\ \text{FE 是 involution 非 descent，转 descent 即 selection ⟹ V148 已封} ✗$$
$$\boxed{\text{故}\textbf{无第七类} ✓\ \text{（WF 被 II}\cup\text{IV 吸收）};\ \textbf{但不证明类表完整} ✗\（\text{§E.4 仍开} ⚠️）}$$
$$\qquad\textbf{⭐ 本行收获 ✓}：\text{Π}_1\ \text{必要条件（对 Robin 型见证盲目 ⟹ 必须解析／上同调定义）是 }§E.4\ \text{类表的}\textbf{新增覆盖力证据} ✓（仍非完整性证明 ✗）$$

### F.5m ⭐⭐⭐⭐⭐ **§E.4 直接攻击（第一轮）：反例骨架生成器**（`V151` ✓ 2026-09-15 09:38）—— **未逃逸** ✗｜⭐ **§E.4 → (E4′) 精确化** ✓✓｜⭐ **六类表 ＝ big five 的影子** ✓✓

$$\textbf{方法论转向 ✓（回应 }V149\ \text{§2 的批评）}：\text{审计单位}\neq\text{对象形态};\ \text{审计单位}＝\textbf{推出矛盾所用的推理原则}\ \sigma\ ✓\ \Longrightarrow\ \text{写法定式}：\neg\mathrm{RH}\Rightarrow\exists\text{坏轨道}\Rightarrow_\sigma\bot$$
$$\textbf{四型骨架全试 ✓}：\text{A 算术枚举型（Robin）}\textbf{被吸收} ✗\（\text{有限阶段}⟹\mathrm V/\mathrm{III};\ \text{且 }V150\ \text{W2 的 }\Pi_1\ \text{必要条件在骨架层就排除}\ ✓✓\text{）};\ \text{B 动力系统型}\textbf{被吸收} ✗\（\text{证书}＝\text{秩}⟹\text{Mostowski}⟹\mathrm{II}\cup\mathrm{IV}\ ✓\ \text{或 有限特征}⟹_\text{König}\text{有限阶段见证}\ ✓\text{）};\ \text{C 选择/定向型}\textbf{已封} ✗\（V148\text{）};\ \text{D }\mathrm{zoo}\ \text{型}\textbf{被定位但判 }\beta\text{-盲} ✦$$
$$\textbf{⭐ §E.4 新形式 ✓✓}：\boxed{(\mathrm{E4}^{\prime})\quad\text{任何 }\neg\mathrm{RH}\Rightarrow\bot\ \text{的证书，必由 } RCA_0\cup WKL_0\cup ACA_0\cup ATR_0\cup\Pi^1_1\text{-}CA_0\ \text{之一认证}}$$
$$\qquad\Longrightarrow\ \text{有明确定义域（需固定骨架语言＋"}\beta\text{-排除证书"的形式定义）} ✓;\ \text{且有已知否定候选（}\mathrm{zoo}\text{）} ⟹ \textbf{可证／可否证} ✓\ \text{—— 满足"把 §E.4 变成可证明／可否证的命题"的要求} ✓✓$$
$$\textbf{⭐ 六类表 ＝ big five 的影子 ✓}：RCA_0\（\text{有限特征}）⟹\mathrm V/\mathrm{III};\ WKL_0\（\text{König/紧性}）⟹\text{有限阶段见证};\ ACA_0\（\text{算术量词/增长}）⟹\mathrm{II};\ ATR_0\（\text{超限递归/秩}）⟹\mathrm{IV};\ \Pi^1_1\text{-}CA_0\（\text{可定义性}）⟹\mathrm{VI};\ RCA_0\ \text{的等式型子形状}⟹\mathrm I$$
$$\qquad ⭐⭐\ \textbf{三项独立吻合}：\text{(a) }ATR_0\ \text{行}\equiv V150\ \text{W1（}\mathrm{WF}\subseteq\mathrm{II}\cup\mathrm{IV}\text{）} ✓✓;\ \text{(b) }WKL_0\ \text{行}\equiv V133\ \text{Theorem A（极限盲）} ✓✓;\ \text{(c) }\Pi^1_1\text{-}CA_0\ \text{行}\sim V134\ \text{（不可解码}⟹\text{不可认证}⟹\mathrm{IV}\text{）} ✓$$
$$\qquad ⚠️\ \textbf{诚实边界}：\text{映射为}\textbf{结构性 ⚠️ 非定理} ✗;\ \text{未证"每个 }\sigma\ \text{必落其中一层"} ✗$$
$$\textbf{唯一攻击面 ＝ 逆向数学 }\mathrm{zoo} ✦\（RT^2_2\text{／}COH\text{／}AMT\text{／}SADS\dots\ \text{严格超出 big five} ✓\text{）}\ ——\ \text{但判 }\beta\text{-盲}：\text{其输出 ＝ 齐次集／同构对象的存在}\⟹\ \text{对元素的算术位置不敏感}\⟹\ \textbf{结构性信息}\neq\beta\text{-排除所需的元素级信息}\⟹\textbf{类型不匹配}（与 }V148\ \text{同型} ✓\text{）};\ \text{双佐证}：V132\ \text{§② β-free 数据引理 ＋ }V150\ \text{W2 }\Pi_1\ \text{必要条件} ✓$$
$$\qquad\Longrightarrow\ \text{结论 ✓}：\text{反例骨架【未逃逸】✗}\ \text{—— 但 §E.4 第一次成为}\textbf{良置命题} ✓✓;\ \text{本档不证 }(\mathrm{E4}^{\prime})\ ✗\ \text{亦不证 zoo 逃逸} ✗$$
$$\qquad\textbf{下一步三选（待定 ✓）}：①\ \text{攻 }\mathrm{zoo}\（\text{先形式化"}\beta\text{-信息"再证 zoo 原理 }β\text{-信息}＝0\text{）};\ ②\ \text{攻 }ATR_0\ \text{行（}V150\ \text{W1 升为逆向数学定理）};\ ③\ \text{回 }P$$

$$\textbf{⚠️ ERRATUM（T10 · 唐先生 2026-09-15 09:48 ✓ 必守）}：\text{本行（}V151\text{）的 }(\mathrm{E4}^{\prime})\ \textbf{未良置} ✗✓\ \text{—— big five 是}\textbf{主要分层}，\textbf{无}\text{"任何证明的强度必等于某一级"之一般定理} ✗；\mathrm{zoo}\ \text{存在}\textbf{即其反例} ⟹ \text{降为}\ \textbf{(E4}^{\prime}\text{-cond)}（条件式）✓；\ \textbf{"zoo }\beta\text{-盲"}\textbf{作废} ✗\ \text{—— }\text{coloring }c:\mathbb N^2\to\{0,1\}\ \text{可编码}\textbf{任意}\text{算术谓词} ⟹ \textbf{Z 本身盲 ⇏ 所认证结构盲} ✓✓；\ \textbf{V148 类比不成立} ✗\（\mathrm{zoo}\ \text{无统一分类定理}）⟹ \text{正解见 }V152\ ✓$$

### F.5n ⭐⭐⭐⭐⭐ **β-Information Conservation / Zoo Neutrality（守恒命题为假）＋ Robin 二分**（`V152` ✓ 2026-09-15 09:52）—— **(BIC) 为假 ✗｜攻击面迁移 ✦**

$$\text{目标（唐先生 §五）}：\mathcal L_0\text{-}\beta\text{-free}\ +\ Z\text{-neutral}\Longrightarrow\mathrm{Cl}_Z(\mathcal L_0)\ \text{β-free};\ \mathcal L_0\ \textbf{不含}\ \rho/\beta/\gamma/\zeta(\rho)\ \text{及零点参数谓词（含}\sigma(n)\text{）} ✓$$
$$\textbf{⭐ 决定性反例 ＝ Robin} ✓✓：\mathrm{RH}\iff\forall n>5040:\sigma(n)<e^\gamma n\log\log n\（\gamma\ \text{＝ Euler–Mascheroni 常数，非零点虚部 ✓）}\Longrightarrow\neg\mathrm{RH}\iff\exists n>5040:\sigma(n)\ge e^\gamma n\log\log n$$
$$\qquad\Longrightarrow\ \text{该句}\textbf{完全落在 }\mathcal L_0\ \text{内} ✓✓\ \text{—— }\mathcal L_0\ \textbf{已在语义上完备于 RH} ⟹ \mathcal L_0\ \text{的语义 β-信息}\neq0\ ✗✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{二难} ✓✓}：\text{语法版 }I_\beta ⟹ (BIC)\ \textbf{可证但平凡且不承载 }§E.4 ✗;\ \textbf{语义版 }I_\beta ⟹ (BIC)\ \textbf{为假（Robin 反例）} ✗✗\ \text{—— 任何"强到正确"的语义定义都会把 RH 塞进定义} ✓✓$$
$$\textbf{⭐ 失败点定位} ✓✓：\textbf{finite → infinite 边界}\ \text{—— 有限阶段素数数据 β-盲（}E103\ \text{Lemma A ✓）而无界算术数据 β-可见（Robin ✓）} ⟹ \text{这}\textbf{正是 }V150\ \text{W2 的 Π}_1\ \text{论证} ⟹ \textbf{W2 的证明论根源 ＝ 算术虽 β-free 语法却经 Robin 承载 β} ✓✓$$
$$\textbf{⭐⭐ Theorem B（Robin 二分）}：(a)\ \textbf{Robin-seeing}（用无界除数和数据）⟹ \text{算术完备} ⟹ \text{会看到 }n_0 ⟹ \text{与"每层平坦"矛盾} ⟹ anomaly\ \text{必须解析／上同调} ⟹ \textbf{已封类} ✗；(b)\ \textbf{Robin-blind} ⟹ \text{不可能经算术路径得 β 信息} ⟹ \text{必须引入}\textbf{非算术 β-sensitive primitive} ⟹ \text{三来源：零点（循环 ✗）／L-函数（旧类 ✗）／}\boxed{\textbf{真正新的 arithmetic→Archimedean bridge（唯一剩余方向）}} ✓✓$$
$$\qquad ⭐\ \text{独立佐证}：\textbf{从证明论侧独立重推 }V144\ \text{层诊断}（(b)\ \text{逼出的"解析"侧 ＝ Archimedean 层 ✓✓）;\ \text{与 }V140\ \text{二分定理同向};\ \textbf{覆盖 }V133\ \text{Theorem A 的适用范围} ✓$$
$$\textbf{⭐ 反例搜索与攻击面迁移} ✦：\text{唯一发现的实例是"算术等价自身"（Robin），而}\text{算术}\in\ \text{big five}\（\text{非 zoo}）⟹ (BIC)\ \text{的反例}\textbf{不在 zoo 里} ⟹ \mathrm{zoo}\ \textbf{不再是自然攻击面};\ \text{攻击面迁移至}\ \boxed{\textbf{Robin 边界}}$$
$$\qquad\Longrightarrow\ §E.4\ \text{形态}\textbf{再次收窄} ✓：\text{不再是"big five 是否完整"（已判非正确形式 ✗），而是}\ \boxed{\textbf{Robin-blind 机制能否排除 β？}} ✓✓$$
$$\qquad\textbf{诚实边界 ⚠️}：\text{flatness 论证 [结构性] 非定理};\ \text{二分平凡穷尽、内容在两条后果};\ \text{"(b)⟹必须新 primitive" [结构性] 非定理}$$
$$\qquad\textbf{下一步三选 ✓}：①\ \text{攻 (b) 支（形式化"Robin-blind ⟹ 算术路径 β-信息＝0"，取代 }(BIC)\ \text{的表征定理靶）};\ ②\ \text{攻 flatness（把 }W2\ \text{补硬）};\ ③\ \text{回 }P（暂放）$$

### F.5o ⭐⭐⭐⭐⭐ **Robin-blind Arithmetic Path Theorem**（`V153` ✓ 2026-09-15 09:53）—— **(FAL) 成立 ✓✓｜⭐ Case B 空（定理级）✗✓｜⭐ ∃／λ 分裂 ✓✓｜残余 ＝ 打破 N29 ✦**

$$\text{规格（唐先生逐字）}：\mathscr A=\{A_N\},\ A_N=\{\text{所有 }n\le N\ \text{的素性／因子／}\sigma(n)\text{／}\Lambda(n)\};\ \textbf{任何有限 }N\ \text{不得使用 }n>N\ \text{的信息} ✓;\ A_1\subset A_2\subset\cdots,\ \bigcup A_N=A_\infty$$
$$\textbf{关键区分（本档纠正）}：\text{唐先生 §3 的反例 }f_N=0(N{<}n_0)/1(N{\ge}n_0)\ \textbf{并非逐点盲} ✗\ \text{—— 它在 }N\ge n_0\ \text{已可见异常} ⟹ \text{必须分开两种 regime}：\textbf{(R1) pointwise-blind}（O_n(Z_+){=}O_n(Z_-) \textbf{作为元素} \forall n，＝ V133 适用域）｜\textbf{(R2) eventually-separating}（\exists N: A_N(Z_+)\neq A_N(Z_-)，\textbf{Robin 属此类} ✓）$$
$$\textbf{⭐⭐ Theorem 1（非连续性无力定理）} ✓✓：\text{若 }A_N(Z_+)=A_N(Z_-)\ \forall N\ \textbf{作为元素}，\ \text{则}\textbf{任何} F=F((A_N)_N)\（\text{连续或不连续皆可}\）\ \text{满足 }F(Z_+)=F(Z_-)\ \text{（函数的定义，}\textbf{与连续性无关}）⟹ \boxed{\textbf{Case B 为空} ✗✓};\ \text{且 (R1)}⟹\textbf{global β-blindness}，\textbf{不需连续性假设}（强于目标 (FAL) ✓✓）$$
$$\qquad\Longrightarrow\ \textbf{六来源逐个审计} ✓✓：\text{Banach limit／ultrafilter(超积)／completion／boundary value／奇异测度选择（或落 selection ⟹ V148）／noncommuting limits}\ \text{—— }\textbf{全部落 B-空或 C-旧} ✗✓\（\text{皆为"数据族的函数"，等序列 ⟹ 等值}）；\ \textbf{唯一逃逸方式}：\text{构造}\textbf{不是}\text{数据族的函数} ⟹ \text{依赖"世界自身零点集"} ⟹ \textbf{偷渡 β ⟹ 循环}（V140 ✓）$$
$$\textbf{⭐⭐ 真正的障碍 ＝ ∃／λ 分裂} ✓✓：\text{(i) }\textbf{∃-信息}（\text{"存在 }n_0\ \text{违反 Robin"}\）\ \text{在 }N\ge n_0\ \textbf{有限阶段可得} ✓;\ \text{(ii) }\textbf{λ-信息}（\text{"哪一个／在哪"}\）⟹ E103\ \text{Lemma A 逐字"}\textbf{有限阶段}\text{素数数据}\textbf{不能定位任何零点}" ⟹ \textbf{算术不给 λ} ✗$$
$$\qquad\Longrightarrow\ \text{机制变证明只有两路}：(I)\ \text{用 ∃-信息排除一切 }n_0 ⟹ \text{须控制无界算术} ⟹ \text{手段正是 Robin 自己证明（}\psi(x)-x\ \text{／零自由区）} ⟹ \textbf{解析／上同调} ⟹ V152\ \text{(a) 旧类};\ (II)\ \text{直接供给 λ} ⟹ \text{算术不可得} ⟹ \textbf{非算术 primitive} ⟹ V152\ \text{(b)}$$
$$\qquad ⭐\ \text{附注 ✓}：\text{Robin 判据}\textbf{语法上 β-free}，\text{但"它与 RH 等价"}\textbf{本身经解析} ⟹ \mathcal L_0\to\beta\ \text{的通道}\textbf{就是解析的}（与 V152 \text{(a)} 一致）✓$$
$$\textbf{⭐ 三分法 ⟹ 二分法 ＋ 残余重述} ✓：\textbf{B 空} ⟹ A\ \text{（β-盲）}\cup\ C\ \text{（旧类）};\ \text{残余 ＝ λ-供给} ⟹ \text{新 primitive 的}\textbf{正确刻画}\text{不是"非连续极限"，而是}\ \boxed{\textbf{β-free、非选择、能输出位置（λ）的构造}} ⟹ \text{"输出位置"恰是 }\textbf{N29（位置盲，定理级）}\ \text{的否定} ⟹ \boxed{\textbf{残余 ＝ 必须打破 }N29} ⟦\text{落回已登记根墙}✗⟧$$
$$\qquad ⭐\ \textbf{三处收敛（结构性）}：N29\ \text{位置盲}（\text{定理级}）\ +\ V133\ \text{极限盲}\ +\ V144\ \text{层诊断（Archimedean 层）} ⟹ \text{同一约束的三个视角} ✓✓$$
$$\qquad\textbf{诚实边界 ⚠️}：\text{Theorem 1 的"任何 }F"\ \text{需先固定构造的范畴（本档取"数据族的函数"最广读法）};\ \text{§5 (I)(II) 归属与 §6 收敛为 [结构性]};\ \text{依赖 }E103\ \text{Lemma A（档案级} ✓\text{）}$$
$$\qquad\textbf{下一步三选 ✓}：①\ \text{正面攻 λ-供给}⟹\text{攻 }N29;\ ②\ \text{把 (I) 形式化（控制无界算术 ⟹ 必经解析）};\ ③\ \text{回 }P（\text{暂放}）$$

### F.5p ⭐⭐⭐⭐⭐ **Robin-无界排除的闭合（支 (I)）＋ 残余单点化 ＝ C6**（`V154` ✓ 2026-09-15 09:58）—— **支 (I) 闭掉 ✗✓｜C6 单点命名 ✓✓**

$$\text{规格}：R(n):=\sigma(n)-e^{\gamma_E}n\log\log n;\ \mathrm{RH}\iff R(n)<0\ \forall n>5040;\ \text{支 (I) 义务}＝(I)\ \forall n>5040:R(n)<0;\ \textbf{要点}＝\text{证明存在}\textbf{无界统一控制量}（\text{非逐个检查}）$$
$$\textbf{⭐ Theorem A} ✓✓：\text{显式公式 }\psi(x)-x=-\sum_\rho x^\rho/\rho+(\log\ \text{项})\ ⟹ \text{主项由 }\sup_\rho\Re\rho\ \text{支配};\ \text{结合三条}\textbf{经典等价}：\text{Robin 1984}(\mathrm{RH}\iff R<0)\ +\ \text{Schoenfeld 1976}(\mathrm{RH}\iff\psi(x)-x\le\frac{1}{8\pi}\sqrt x\log^2x)\ +\ \text{von Koch 1901}(\mathrm{RH}\iff\psi(x)=x+O(\sqrt x\log^2x))$$
$$\qquad\Longrightarrow\ \boxed{\text{达到临界精度的}\textbf{统一控制}\iff\mathrm{RH}} ⟹ \textbf{支 (I) 的有效内容}\equiv\mathrm{RH}\ \text{本身} ⟹ \textbf{不可能"内容上 β-free"} ✗✓\（\text{要么间接重引 }\lambda\text{（经 }\psi\text{-误差）}，\text{要么就是 RH}）$$
$$\qquad ⭐\ \text{与 }V152\ \text{二难接口}：\mathcal B\ \text{的}\textbf{语句}\text{可语法上 β-free（如 Robin 不等式）},\ \text{但}\textbf{语义／有效内容}\text{是 RH-等价的} ✓$$
$$\textbf{Theorem B（载体分类，[结构性] ⚠️）}：\text{无界 Robin 控制}\Longrightarrow\psi\text{-控制}\Longrightarrow\text{素数分布解析估计}\Longrightarrow \textbf{C（growth／sum-formula／explicit-formula 旧类）} ✗;\ \text{已达档载体}＝\{\text{零点自由区／显式公式／零点密度}\}$$
$$\textbf{⭐ 残余正式单一化} ✓✓：\text{B 空（}V153\text{）}＋\text{支 (I)}\in C＋\text{(C) 旧类（}V152\ \text{a}）⟹ \text{唯一余支}＝(II) ⟹ \text{须满足}\ \boxed{\beta\text{-free}+\text{non-circular}+\text{non-selection}+\lambda\text{-output}} ⟹ \boxed{\textbf{C6 ＝ β-free、非选择、非显式公式的 λ-供给机制}} \Longrightarrow \text{残余由"多张地图"压成}\textbf{单点} ✓✓\ \text{且立刻撞 }N29 ✗$$
$$\textbf{⭐ C6 定义漏洞审计（第一轮 ✓）}：\text{唯一逻辑缝隙}＝\lambda\text{-output 经}\textbf{关系／对应}\text{而非}\textbf{选择} ⟹ \textbf{已被登记}：\equiv \textbf{V131}（\text{"瓶颈不是非对称性而是}\textbf{箭头}"；\text{三箭头全封} ⟹ \text{需第四箭头} \equiv \text{类 VI／SW6}）⟹ \text{不构成未登记新缝，但"归约为箭头"}\textbf{待形式化} ⚠️;\ \text{第二缝：non-selection 是否过强（canonical 唯一化算不算选择）⟹ }V148\ \text{已判 torsor 平凡化} ⟹ H^1 ⟹ \text{quadratic} ⟹ \text{仍落 I/II} ✓$$
$$\qquad\textbf{诚实边界 ⚠️}：\text{Theorem A 依赖三条经典引用};\ \textbf{Theorem B 为 [结构性] 非定理}（\text{无"无直证"之形式化定理}）;\ \text{§6 归约待形式化}$$
$$\qquad\textbf{下一步} ✓（\text{唐先生已定}）：\text{审 C6 定义} —— ①\ \text{形式化"关系型 λ-供给 ⟹ 箭头问题"};\ ②\ \text{审 non-selection 强度} ✓$$

### F.5q ⭐⭐⭐⭐⭐ **C6 定义级审计（两刀落到底）＋ 九种箭头形态穷举审计**（`V155` ✓ 2026-09-15 10:00）—— **两刀皆成立 ✓✓｜九形态全落已知封闭，残余仍单点**

$$\textbf{第①刀 ✓✓（关系型 }\lambda\text{-供给}\Longrightarrow\text{箭头）}：\mathcal R\subseteq A\times Z;\ \text{三分}\textbf{逻辑穷尽}：\text{多值}\Longrightarrow\text{无位置输出}\ ✗;\ \text{空值}\Longrightarrow\text{无位置输出}\ ✗;\ \text{唯一值}\Longrightarrow\lambda=\Lambda(a)\ ✓ ⟹ \boxed{\text{关系型}\lambda\text{-供给}\Longrightarrow\text{唯一化关系}\Longrightarrow\textbf{箭头} A\to Z}\ ✓✓;\ \text{若唯一化非证明而得 ⟹ selection ⟹ 违反 C6};\ \textbf{V131 正式化}：\text{C6 须含}\textbf{非循环、β-free 的}\ \Lambda:A\to Z,\ \textbf{不得}\text{定义}\ \Lambda(a)=\Re\rho/\Im\rho\ \text{或等价零点参数编码}（\text{否则 }β\text{ 已作输入} ⟹ V140\ \text{循环}）✓$$
$$\textbf{第②刀 ✓✓（non-selection 过强）}：\textbf{选择对象}\neq\textbf{证明唯一存在};\ \text{若}\ \exists!\lambda\ R(a,\lambda)\ \text{则}\ \Lambda(a):=\text{the unique }\lambda\ \textbf{不构成}额外 selection,\ \text{仅为}\textbf{唯一性定理的函数化} ⟹ \text{原 non-selection}\textbf{确实过强} ✗✓;\ \text{改为}\ \boxed{\textbf{non-exogenous-selection}}：\lambda\ \text{不得由外部规则／任意代表元／选择公理／最小元规定挑出},\ \text{须由机制}\textbf{自证}\ \text{存在性＋唯一性＋与零谱的对应性};\ \text{形式上}\ \forall a:\exists!\lambda R(a,\lambda)\ \text{且}\ R(a,\lambda)\Longrightarrow\lambda\in Z_\zeta;\ ⚠️\ \textbf{关键限制}：Z_\zeta\ \textbf{不得}\text{偷定义为"ζ 的零点集合"}（\text{否则 C6.6 同义反复}）✓$$
$$\textbf{⭐ C6 严格版本}：\boxed{\text{C6.1 β-free input｜C6.2 non-circular｜C6.3 endogenous uniqueness｜C6.4 spectral-position output｜C6.5 non-analytic carrier｜C6.6 zero-spectrum correspondence}}\ \text{最硬两处}：\ \boxed{A\xrightarrow{\textbf{new primitive}}\lambda}\ \text{＋}\ \boxed{\text{该 }\lambda\ \text{须最终对应 }\zeta\ \text{谱位置}} ⟹ \textbf{V154 的"单点 C6"进一步压成具体缺口}：\text{不是"寻找新不变量"，而是寻找一个此前没有的}\ A\to\lambda\ \textbf{内生箭头} ✓✓$$
$$\text{三类最自然实现已被封}：\text{(i) 算术}\to L\text{-函数}\to\lambda ＝ \textbf{旧}（C／AOB3）;\ \text{(ii) 零点}\to\text{构造}\lambda ＝ \textbf{循环}（V140）;\ \text{(iii) 固定算子}\to\lambda ＝ \textbf{位置盲}（N29／E103 Lemma A）}$$
$$\textbf{⭐ 九种箭头形态穷举审计}：\text{①函数}（\text{β-free} ⟹ \text{不能定位}\（E103\ \text{Lemma A}）;\ \text{RH-等价} ⟹ \text{内容≡RH}\（V154\ \text{Thm A}））⟹ \textbf{N29} ✗;\ \text{②唯一关系} ⟹ \text{函数化退回①} ⟹ \textbf{N29};\ \text{③极值} ⟹ E146/E147\ \text{第一支（符号/正性）＋}V135\（\text{稳定 ⟺ 带符号不等式}）⟹ \textbf{II／D}_1 ✗;\ \text{④固定点} ⟹ \text{不动点由算术定义 ⟹ 输出算术 ⟹ β-free ⟹ 位置盲}（V119\ ①③;\ S9\ \text{对角线属 fixed locus}）⟹ \textbf{N29／箱 5} ✗;\ \text{⑤周期轨道} ⟹ V127\ \text{逐字：Connes 流存在但}\textbf{迹公式≡显式公式／Weil} ⟹ \textbf{C 旧类} ✗;\ \text{⑥因果响应} ⟹ \text{档案 }O3\ \textbf{class-closed}（\text{原生 action 皆态射型 ⟹ 模论层 ⟹ }N4+S10) ✗;\ \text{⑦}\textbf{对应／函子} ⟹ ⭐\textbf{自指回同一问题}（O2\ \text{瓶颈就是箭头};\ \text{函子型落 }N1/N2;\ \text{跨尺度缺陷已算出精确为零}\（V138\ D=|D|U(\gamma)\）;\ \text{三体版被 }AOB5\ \text{flag complex 排除}）⟹ \equiv \textbf{C6 自身} ⚠️;\ \text{⑧障碍类} ⟹ H^1/H^2/H^3 ⟹ quadratic／2-上闭链／Brauer ⟹ L-值（V148;\ AOB1 §2(3)）⟹ \textbf{箱 1／8} ✗;\ \text{⑨奇异点} ⟹ ζ\ \text{极点只在 }s=1;\ \text{"极点定位"}＝E146/E147\ \text{第三支（已封）};\ \text{唯一把零点变奇点者＝}-\zeta'/\zeta ＝ \textbf{显式公式} ⟹ \textbf{C 旧类} ✗$$
$$\qquad\Longrightarrow\ \boxed{\text{九形态}\textbf{全部落入已知封闭};\ \text{唯 #7 自指} ⟹ \textbf{残余仍单点}} ✓✓\ ⚠️\ \text{边界：本表为}\textbf{[结构性] 已归档实现分类},\ \textbf{非}"不存在第四箭头"之定理}$$
$$\qquad\textbf{下一步三选}：①\ \text{审 }\textbf{C6.6}（\text{零谱对应能否}\textbf{内生}\text{而不借显式公式}）＝\text{本档暴露的}\textbf{最硬单点};\ ②\ \text{审 }\textbf{C6.5}（\text{non-analytic carrier 与 }V144\ \text{层诊断}\textbf{直接冲突} ⚠️\ \text{值得单审};\ ③\ \text{把 #7（O2 对应 ⟹ 箭头）}\textbf{形式化} ✓$$

### F.5r ⭐⭐⭐⭐⭐ **C6.5 层诊断审计**（`V156` ✓ 2026-09-15 10:03）—— **不与 V144 矛盾 ✗✓，但被强烈夹逼 ⚠️；C6 收缩为"同一内部结构自产 $\sqrt N e^{i\theta}$"**

$$\text{C6 要有 }A\to\lambda\ \text{且最终得 }\zeta\ \text{零谱位置};\ \rho=\beta+i\gamma\Longrightarrow \text{载体至少需}\ \boxed{\text{模长/权重}\to\sqrt{\text{scale}}}\ +\ \boxed{\text{相位}\to\text{位置参数}}$$
$$\textbf{第一断裂（有限算术层）}：\zeta\ \text{局部因子}(1-p^{-s})^{-1},\ \text{有限素数处}\ \alpha_p\equiv1 ⟹ \text{无函数域型 }\alpha_p=\sqrt p e^{i\theta_p}\ \text{内部谱数据} ⟹ \boxed{\text{有限算术层}\not\Rightarrow(\sqrt{\text{scale}},\theta)}\ ✓✓\（\text{与 }AOB3\ \text{§1 element vs 共轭类同源}）$$
$$\text{非解析载体 }M\ \text{须内部产生 }\operatorname{Spec}(F_M)=\{\sqrt{N_j}e^{i\theta_j}\} ⟹ \text{须 }F_M^\dagger QF_M=NQ\（1\）⟹|\lambda_j|=\sqrt N;\ \textbf{但 (1) 只给模长},\ \text{相位还需 }F_M\ \text{的非实谱结构}（\text{canonical phase}）⟹ \text{C6.5 实际要求同时具}\ \textbf{polarization/similitude}\ +\ \textbf{canonical phase}\ \text{的 char-0 载体}$$
$$\textbf{双重断裂直接出现}：\text{权重侧（能自然产生 }|\lambda|=\sqrt N\ \text{者：二次型／Gram-polarization／rank-2／Hodge-Frobenius weight）}\Longrightarrow\textbf{旧箱 II／8／12}\（=V136\ \text{五来源枚举}）;\ \text{相位侧（能自然产生 }e^{i\theta}\ \text{者：character／reciprocity／holonomy／Artin-Hecke／cocycle-Brauer／L-value）}\Longrightarrow\textbf{character／L-函数类}\（=V140\ \text{相位二分}）⟹ \text{两通道}\textbf{各落旧类};\ \text{拼接}\Longrightarrow\textbf{不产生新 primitive} ✗✓$$
$$\qquad ⚠️\ \textbf{必须保留的逻辑缝}：\textbf{不得}\text{宣布"不存在任何 non-analytic carrier"}（V144 实为"}\textbf{在已审计的标准 char-0 算术结构中未找到}"\ \neq\ \text{"不存在"}）；真正需要的是两条\textbf{表示定理}：\ \boxed{R1_{wt}: F^\dagger QF=NQ\ \text{的纯算术 char-0 结构}\Rightarrow\text{polarization/Hodge/quadratic}}\ \text{＋}\ \boxed{R1_{ph}:\ \text{canonical phase 的全局 char-0 结构}\Rightarrow\text{character/holonomy/L}}\ ——\ \textbf{档案目前没有这两条}\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{C6.5 不与 }V144\ \text{矛盾，但被其强烈夹逼}};\ \text{C6 无逻辑不一致，只是被迫寻找}\ \boxed{\text{一种尚未被分类的 char-0 算术载体}}\ \text{同时自产 }\sqrt N+e^{i\theta}\ \text{且来自}\textbf{同一个内部结构}（\text{非两旧模块拼接}）$$
$$\qquad\Longrightarrow\ \boxed{\textbf{C6}\ =\ \text{char-0 intrinsic arithmetic object}\xrightarrow{\text{one mechanism}}\sqrt N e^{i\theta}\xrightarrow{\text{new correspondence}}\lambda_\zeta}\ \text{须避开：L-function／explicit formula／known polarization／selection／zero data}$$
$$\qquad\textbf{下一步 ✓（唐先生已定）}：\text{转 }\textbf{① C6.6} —— \text{即便找到这样的载体，}\textbf{仍没解释为何其谱就是 }\zeta\ \text{的零谱}，\textbf{这才是目前真正不可替代的第二个箭头} ✓✓$$
$$\qquad\textbf{诚实边界 ⚠️}：\text{本档 §6 C6 收缩为 [结构性]；}R1_{wt}／R1_{ph}\ \text{为}\textbf{待证表示定理} ✗$$

### F.5s ⭐⭐⭐⭐⭐ **C6.6 内生零谱对应审计**（`V157` ✓ 2026-09-15 10:36）—— **三分（A DEAD／B ⊂ C／C 真问题）｜C6 实为两箭头｜十条身份机制穷举 ⟹ 唯剩空槽**

$$\text{C6.5 给出 }M,\ \Lambda_M=\{\lambda_j\},\ \lambda_j=\sqrt{N_j}e^{i\theta_j};\ \text{C6.6 要求}\ \boxed{\Lambda_M\longleftrightarrow Z_\zeta}\ \text{（非"看起来相似"}）$$
$$\textbf{对应严格三分}：\text{A 定义型}\（Z_M:=Z_\zeta）\Longrightarrow \boxed{\text{DEAD}}\ ✗\（\text{循环}）;\ \text{B 公式型}\（F(\lambda){=}0\iff\zeta(\rho){=}0;\ \text{显式公式／Mellin／Hadamard／L-函数 FE}\）\Longrightarrow \boxed{\subset C}\ ✗\ \text{（C6 明确排除 B）};\ \text{C 结构型}＝\text{真问题（}M\ \text{自产}\lambda_j\ \text{＋ 独立算术结构定理证}\ \lambda_j\leftrightarrow\rho_j-\tfrac12\text{）}$$
$$\qquad\textbf{关键}：\boxed{\text{为什么是 }\zeta\text{，而不是另一个谱？}};\ \text{纯谱结构}\not\Rightarrow\zeta\ \text{零谱}（\text{CM/Hecke}\ \alpha_p=\sqrt p e^{i\theta_p}\ \text{及大量几何／表示论对象皆有纯权重谱}）;\ \text{统计／计数（}N_M(T)\sim N_\zeta(T)\text{／间距／矩／对称性）}\textbf{不足} ✗（\text{不同谱可共享 Weyl 主项}）$$
$$\qquad\text{最强非循环要求}：\text{需独立谱识别不变量}\ I_M(\lambda)=0\iff I_\zeta(\lambda)=0;\ \text{但若 }I_\zeta\ \text{由}\ \zeta(1/2+i\lambda)\ \text{定义} ⟹ \textbf{偷回零点} ⟹ \text{合法形式}\ \boxed{I_M(\lambda)=I_A(\lambda)}\（I_A\ \text{独立算术定义}\）\ \text{再证}\ I_A(\lambda)=0\iff\zeta(1/2+i\lambda)=0\ \text{—— 后者}\textbf{本身就是新的 ζ 身份定理}$$
$$\textbf{⭐ C6.6 拆成两箭头}：\boxed{M\xrightarrow{P}\Lambda_M}\ \text{（＝C6.5）};\ \boxed{\Lambda_M\xrightarrow{Q}Z_\zeta}\ \text{（Q 才是真难点）};\ \text{Q 七路线判决}：\text{经 }\zeta/\text{显式公式}⟹\textbf{循环／C};\ \text{经 L-function}⟹\textbf{C};\ \text{经 character/Hecke/Artin}⟹\textbf{C};\ \text{经已知 trace formula}⟹\textbf{C};\ \text{经统计／计数}⟹\textbf{不足以逐点};\ \text{经人为选择}⟹\textbf{selection};\ \text{经全新算术定理}⟹\textbf{真正的 C6 新内容} ⟹ \boxed{\textbf{第二箭头不能由第一箭头推出}}\ \text{（即便突破 }V144,\ \textbf{仍撞身份墙}）$$
$$\textbf{⭐ 非循环谱身份机制穷举（十条，本档新增）}：\text{①定义型}\to A\ \text{DEAD};\ \text{②公式型}\to\subset C;\ \text{③算子酉等价}\to \text{需不用零点定义的第二算子}⟹\text{循环或 C（HP）};\ \text{④迹公式相等}\to \text{就是显式公式}⟹C;\ \text{⑤矩／迹确定性}\to M\ \text{侧 β-free 可行，但 }\zeta\ \text{侧矩＝显式公式素数侧＋archimedean}⟹\textbf{此路线 ≡ 既有主线（Weil／Li 正性）}，已有 }T^2\ \text{律／预算交叉墙};\ \text{⑥FE＋增长刚性}\to ⭐\textbf{反例存在}：D1\ \text{逐字"Epstein }\zeta\ \text{有 FE 却有离轴零点（Potter–Titchmarsh）"}⟹ \text{FE 给临界线不给零点位置};\ \text{⑦统计／计数}\to \text{非逐点};\ \text{⑧L-函数分类定理（Selberg 类：degree 1}⟹\text{Dirichlet L；conductor 1}⟹ζ）\to ⭐\textbf{唯一"由公理识别身份"机制}，但分类证明用解析工具⟹C;\ \text{⑨Hadamard 分解比对}\to \text{公式型}⟹C;\ \text{⑩Lefschetz／正则化 det（Deninger）}\to V145\ \text{逐字：有 canonical 生成元但缺 canonical polarization；det 定义本身把 ζ 放入}⟹\text{定义型／C}$$
$$\qquad\Longrightarrow\ \boxed{\text{十条全落 A／C／不足／＝既有主线};\ \text{唯剩一个}\textbf{空槽}}\ ⟹ \text{C6.6 压成}\ \boxed{\textbf{非循环的谱身份定理是否可能存在？}} ✓✓$$
$$\qquad ⚠️\ \text{边界：本表为 [结构性] 已知机制分类，}\textbf{非}"不存在"之定理（与 }V144\ \text{"未找到"≠"不存在"同型）}$$
$$\qquad\textbf{下一步三选}：①\ \text{形式化空槽（给"谱身份定理"下定义：β-free 输入＋输出逐点相等＋不含零数据，看是否自相矛盾）};\ ②\ \text{审 #8（Selberg 类分类能否去解析化）};\ ③\ \text{审 #5 与既有主线的完全等价性（若 ≡ Weil 正性，则 C6.6 与 A1/A3 同墙）} ✓$$

### F.5t ⭐⭐⭐⭐⭐ **非循环谱身份定理形式化**（`V158` ✓ 2026-09-15 10:39）—— **相容性定理（不得语言判死）｜RH-equivalence ≠ spectral identity｜soundness ＋ completeness｜必经性审计**

$$\text{机制规格}：\mathfrak M=(A,M,P,Q),\ A=\text{β-free 算术输入},\ P:A\to\Lambda_M,\ Q:\Lambda_M\to\mathbb C;\ \text{C6.6-1 β-free}（\operatorname{Lang}(A,M,P,Q)\ \text{不得含}\ \rho,\beta,\gamma_\rho,\zeta(\rho),Z_\zeta\ \text{及可定义等价编码}）;\ \text{C6.6-2 内生谱};\ \text{C6.6-3 逐点身份}\ \lambda_j\in\Lambda_M\iff\zeta(\tfrac12+q(\lambda_j))=0$$
$$\qquad ⚠️\ \textbf{关键限定（必守）}：\zeta\ \textbf{只出现在待证明的结论中}，\textbf{不是}\text{机制的定义中} —— 否则"β-free"被}\textbf{错误强化}\text{成"证明中不能谈 ζ"} ✗$$
$$\textbf{⭐ 相容性定理（本档第①刀）}：\text{若 }P\ \text{β-free 算术命题且 }P\iff\mathrm{RH} ⟹ \text{可证 }P\Rightarrow\text{"所有 ζ 零点在临界线"} ⟹ \boxed{\text{β-free}+\text{推出 RH}\not\Rightarrow\text{逻辑矛盾}};\ \textbf{Robin 即显式模型}（\forall n>5040:\sigma(n)<e^{\gamma_E}n\log\log n\ \text{β-free 且}\iff\mathrm{RH}）⟹ \textbf{不能从语言层面判死 C6.6} ✗✓$$
$$\textbf{⭐ 更强结构结论}：\text{要禁的不是"β-free 命题推出 RH"，而是"β-free 机制}\textbf{如何}\text{产生逐点零谱身份"；Robin 只给}\ \boxed{\text{算术全称命题}\iff\mathrm{RH}}\ \textbf{不给}\ \boxed{n\mapsto\rho_n} ⟹ \boxed{\textbf{RH-equivalence}\neq\textbf{spectral identity}} ✓✓\ \text{（这正解释 C6.6 比 Robin 路线强）}$$
$$\textbf{⭐ C6.6 拆开}：\Lambda_M=Z_\zeta-\tfrac12\ \text{含两独立断言}\ \boxed{\Lambda_M\subseteq Z_\zeta-\tfrac12\ (\text{I soundness})}\ \text{＋}\ \boxed{Z_\zeta-\tfrac12\subseteq\Lambda_M\ (\text{II completeness})};\ \boxed{\text{soundness alone}\not\Rightarrow\mathrm{RH}}（\text{只产临界线上部分零点的谱也满足 soundness}）;\ \text{completeness 才迫使全谱进入载体} —— \text{比"证明 RH"强得多}$$
$$\text{硬墙}：\text{用 }\zeta'/\zeta／\text{Hadamard}／\text{explicit formula}／\text{Mellin}\to V157\text{-B}\to C;\ \text{用另一 L-函数 Euler 积／分类}\to C;\ \text{靠统计}\ N_M(T)=N_\zeta(T)+o(N(T))\ \text{只有计数一致}\to \text{不足};\ \text{人为配对}\to\text{selection}$$
$$\textbf{⭐ 必经性审计（本档新增）}：\text{(a) }\textbf{soundness}\ \text{要求对每个 }\lambda_j\ \text{建立}\ \zeta(\tfrac12+q(\lambda_j))=0;\ \text{该谓词是}\textbf{继续后对象}\text{的谓词}（\text{Euler 积只在}\operatorname{Re}s>1\ \text{收敛，而临界带不在其中}）⟹ \text{任何验证须触及 Archimedean／完成结构} ⟹ \text{与 }V144\ \text{层诊断一致}（\text{零点在 Archimedean 层；β-free 算术在有限层}）⟹ \boxed{\text{soundness}\ \textbf{必经 archimedean 桥}（V140\ \text{Gate A/B}）} \Longrightarrow ⚠️\ \textbf{该桥就是 C6 第一箭头本身} ⟹ \text{soundness}\textbf{不与 C6-gap 独立};\ \text{(b) }\textbf{completeness}\ \text{等价于}\ |\Lambda_M(T)|\ \text{与}\ N_\zeta(T)\ \text{全谱匹配} ⟹ \text{需 }N_\zeta(T)（\text{RvM}），\text{而已知唯一途径＝对 }\xi\ \text{用论证原理}\to\text{显式公式} ⟹ \boxed{\text{completeness}\ \textbf{必经解析计数}} ⟹ \textbf{至少 completeness 必然经过解析 ζ 结构}$$
$$\qquad\Longrightarrow\ \boxed{\text{C6.6 不可判 DEAD，但被压到两处必经性}：\text{soundness}\to\text{archimedean 桥（非独立墙）};\ \text{completeness}\to\text{解析计数}}\ \text{可闭合形式：}\text{若两条皆形式化}\Longrightarrow \text{C6.6 封死}$$
$$\qquad ⚠️\ \text{边界}：\text{(a) 为 [类型级]（Euler 积收敛域）＋[层诊断一致]};\ \text{(b) 的"唯一途径"为 [结构性] 非定理};\ \text{本档不证明 C6.6 封死}$$
$$\qquad\textbf{下一步三选}：①\ \text{形式化 (b)"completeness}\Longrightarrow\text{需 }N_\zeta(T)";\ ②\ \text{审 (a) 反面：能否造只用完成结构而不用显式公式的 soundness？};\ ③\ \text{若 (a)+(b) 成立} ⟹ \text{整条 C6 线}\textbf{并入既有主线}（\text{与 }A1/A3/V157\text{-}⑤\ \text{同墙}）$$

### F.5u ⭐⭐⭐⭐⭐ **C6.6 → A1/A3 的等价性审计（含 V158(b) 撤回）**（`V159` ✓ 2026-09-15 10:42）—— **撤回｜谱双射｜并轨骨架｜最终分叉**

$$\textbf{① 撤回 }V158\text{(b)} ✗✓：Z_\zeta-\tfrac12\subseteq\Lambda_M\ \textbf{不逻辑上必然要求先算}\ N_\zeta(T)\ \text{—— 可能存在}\textbf{结构定理}\ \Phi:\Lambda_M\xrightarrow{\sim}Z_\zeta-\tfrac12\ \text{直接证}\ \zeta(\tfrac12+\Phi(\lambda))=0\ \text{及反向存在性},\ \text{此为}\textbf{结构性双射证明}\ \text{未必先用 RvM} ⟹ \boxed{\text{completeness}\not\Rightarrow\text{必须用 }N_\zeta(T)};\ \text{故"需 }N_\zeta(T)\text{／唯一途径是论证原理"}\textbf{降级为结构性观察},\ \text{正确形式}\ \boxed{\text{计数路线}\subset C}$$
$$\textbf{② C6.6 压缩} ✓✓：\text{设}\Phi:\Lambda_M\to Z_\zeta-\tfrac12\ \text{内部双射};\ (S)\ \forall\lambda:\zeta(\tfrac12+\Phi(\lambda))=0;\ (C)\ \forall\rho\exists\lambda:\Phi(\lambda)=\rho-\tfrac12 ⟹ \boxed{\Lambda_M\xrightarrow{\Phi}\cong Z_\zeta-\tfrac12}\ \text{本身已是}\textbf{完整谱识别定理} ⟹ \boxed{\text{C6.6}＝\textbf{非解析、非循环谱双射}}$$
$$\textbf{③ 三层必须严格分开}：\text{层 1 逻辑}：\Lambda_M\subset i\mathbb R\ \text{时}\ C6.6+\text{C6.5 purity}\Rightarrow\mathrm{RH};\ \text{但}\ \mathrm{RH}\Rightarrow C6.6\ \textbf{不成立} ⟹ \textbf{C6.6 非逻辑等价于 RH};\ \text{层 2 载体}：\text{若 (*) 唯一有效工具＝trace}\to\text{explicit formula}\to\text{Li/Weil positivity}\ \text{则}\ C6.6\subseteq A1/A3\ \text{（}\textbf{仍需证明}）;\ \text{层 3 新情况}：\Phi\ \text{证明}\textbf{完全不用}\ \text{explicit formula／}\xi\ \text{论证原理／Mellin／L-function／Hadamard／Li-Weil positivity} ⟹ \textbf{真新类}$$
$$\textbf{⭐ ④ 并轨骨架（本档新增）}：\text{(i)–(vi) 范式}\（\text{trace/显式公式／}\xi\ \text{论证原理／Mellin／L-函数／Hadamard／Li-Weil positivity}\）\textbf{均作用于同一对象}\ \text{Weil 泛函族}\ W(f)=\sum_\rho\hat f(\rho)-(\text{archimedean})-(\text{prime}) ⟹ \text{任一经 (i)–(vi) 的 (*) 证明其}\textbf{有效内容}\text{＝对 }W\ \text{的正性／消失断言} ⟹ \boxed{W\ \text{正性}\equiv A3};\ \text{取 Li 检验族}\Rightarrow\boxed{\lambda_n\ \text{型}\equiv A1} ⟹ \text{须控制}\textbf{统一}\text{的 Weil 正性} ⟹ \text{已知无条件输入不足（}T^2\ \text{律／预算交叉／比例天花板 0.682）} ⟹ \boxed{\text{若 C6 谱双射载体属}\textbf{已知证明范式}\text{，则并入 }A1/A3}\ \text{（}\textbf{[结构性]} ⚠️,\ \text{需范式穷尽性}）$$
$$\textbf{⭐ ⑤ 最终分叉 ＋ §E.4 合法化}：\boxed{\text{谱双射依赖 ζ 解析结构}\Longrightarrow A1/A3/C\ \text{旧墙};\ \text{存在}\textbf{独立结构性双射}\Longrightarrow\textbf{真正的新 C6}} ⟹ \text{比 }V158\ \text{更严格，且}\textbf{避免}\text{把"没找到其他证明"误写成"没有其他证明"（同 }V136/V144\ \text{纪律）} ⟹ \text{完成后 }§E.4\ \text{可}\textbf{合法地}\text{问}\ \boxed{\textbf{C6 是否真的构成第七种证明类，还是只是 }A1/A3\ \text{的新表示？}}$$
$$\qquad ⚠️\ \text{边界}：§3 并轨骨架为 [结构性] 非定理（需范式穷尽性）；§4 分叉为 [结构性]；"合法化 §E.4 最后问题"为 [制度级]}$$
$$\qquad\textbf{下一步三选}：①\ \text{攻唯一开口：}\textbf{能否构造不用六大工具的结构性双射 }\Phi？\（\text{真正的第七类候选位}）;\ ②\ \text{把"已知范式穷尽性"形式化（并轨骨架}\to\text{定理）};\ ③\ \text{审 (i)–(vi)}\to W\ \text{归约是否有}\textbf{不经 }W\ \text{的例外} ✓$$

### F.5v ⭐⭐⭐⭐⭐ **六范式 → $W$ 归约审计**（`V160` ✓ 2026-09-15 10:46）—— **V159④ 强命题不成立｜$A1/A3\subsetneq C_{\rm analytic}$｜判死目标＝范式穷尽定理**

$$\text{待审强命题（V159④）}：\text{Proof of }\Phi\Longrightarrow\text{proof about }W;\ \text{更强：}\text{effective content}(\Phi)\subseteq\{\text{Weil positivity/vanishing}\} \Longrightarrow \textbf{不成立} ✗✓\ \text{（逐条如下）}$$
$$\textbf{① trace／显式公式}\to\textbf{归入 }W ✓：\sum_\rho\widehat f(\rho)=\text{archimedean}(f)+\text{prime}(f)+\cdots\ \text{即}\ W(f)=0;\ \text{若载体谱给出}\ W(f)=\sum_{\lambda\in\Lambda_M}\widehat f(\lambda)\ \text{则谱识别＝比较两个}\textbf{线性泛函} \subset W ✓$$
$$\textbf{② }\xi+\text{论证原理}\to\textbf{不必然 }W ✗：N_D=\tfrac{1}{2\pi i}\oint_{\partial D}\tfrac{\xi'}{\xi}ds\ \text{直接给}\boxed{\text{零点计数}}\textbf{而非}\text{Weil 正性};\ \text{只有再引测试函数 }f\ \text{并把 }\xi'/\xi\ \text{变换成显式公式才进入 }W ⟹ \boxed{\xi+\text{argument principle}\not\Rightarrow W}\ \text{（逻辑命题）} ⟹ \text{改记为}\boxed{\text{argument principle}\in C_{\rm analytic},\ \text{显式公式化后才进入 }W}\ \text{—— }\textbf{第一个不能直接并入 }A1/A3\ \text{的范式}$$
$$\textbf{③ Mellin}\to\textbf{不必然 }W ✗：\text{能产生}\ x^\rho=x^\beta e^{i\gamma\log x}\ \text{与完成 ζ 谱变量},\ \text{但 Mellin 本身只是变换}\ \widehat f(s)=\int_0^\infty f(x)x^{s-1}dx,\ \textbf{不自动}\text{产生 }W(f)=0\ \text{更}\textbf{不自动}\text{产生 }W(f)\ge0 ⟹ \boxed{\text{Mellin 是 analytic carrier，不是 Weil positivity 本身}}$$
$$\textbf{④ L-函数}\to\textbf{不必然 }W ✗：\Lambda_M=\{\lambda:L(\tfrac12+i\lambda,\pi)=0\}\ \text{＋}\ L(s,\pi)=\zeta(s)\ \text{分类定理}\Longrightarrow\Lambda_M=Z_\zeta-\tfrac12;\ \text{核心是}\ L\cong\zeta\ \textbf{而非}\ W(f)\ge0 ⟹ \boxed{\text{L-函数路线}\subset C\ \text{但不必落入 }A3}$$
$$\textbf{⑤ Hadamard}\to\textbf{不必然 }W ✗：\xi(s)=e^{A+Bs}\prod_\rho(1-\tfrac{s}{\rho})e^{s/\rho}\ \text{给}\boxed{\text{zero set}\leftrightarrow\text{entire factorization}}\ \textbf{而非}\text{Weil 正性};\ \text{两谱 canonical products 相同}\Longrightarrow\text{谱相等},\ \text{此证明甚至不需 }W(f)\ge0\ (\text{仍属 }C)$$
$$\textbf{⑥ Li／Weil 正性}\to\textbf{归入 }A1/A3 ✓：\lambda_n=\sum_\rho[1-(1-\tfrac1\rho)^n],\ \mathrm{RH}\iff\lambda_n\ge0\ \forall n\ \text{—— Weil 型正性泛函的离散化} \subset A1/A3$$
$$\qquad\Longrightarrow\ \text{后四个}\textbf{×}\ \textbf{并非}\text{新类},\ \text{只是说明}\ \boxed{A1/A3\subsetneq C_{\rm analytic}}\ \text{（证明形态意义上）};\ \text{⭐ 与 }E106\ \text{相容}（\text{判据空间＝正性}\cup\text{求和-公式}\Longrightarrow\text{封闭}）⟹ \textbf{并轨方向仍对（落旧类），但落点应由 }A1/A3\ \text{改为更大的 }C_{\rm analytic}$$
$$\textbf{⭐ C6 判死目标改写}：\text{真正要证的不是 }C6\subset A1/A3\ \text{而是}\ \boxed{C6\cap C_{\rm analytic}=\varnothing}（\text{几乎定义层}）\ \text{＋}\ \boxed{\text{所有能证 }\Phi\ \text{的机制}\in C_{\rm analytic}}\ \text{（＝}\textbf{范式穷尽定理}\text{，}\textbf{目前没有} ✗）$$
$$\textbf{⭐ 独立共同结构审计（本档新增）}：\text{若禁尽 explicit formula／Mellin／L-识别／Hadamard／argument principle／zero-counting／Li-Weil},\ \text{则最后箭头不能通过"计算 ζ 零点"实现} ⟹ \text{须存在}\textbf{独立于 ζ 零集定义的共同结构}\ \boxed{\mathfrak S(M)\cong\mathfrak S(\zeta)}\ \text{且该同构自动送 }\Lambda_M\to Z_\zeta-\tfrac12\ \text{（比 C6.6 更严一层）} ⟹ \text{要不用零点写出 }\mathfrak S(\zeta)\ \text{须一个}\boxed{\text{独立于零点的 ζ 结构刻画}};\ \text{档案唯一已知候选＝Selberg 类公理＋分类定理（degree 1}\Longrightarrow\text{Dirichlet }L;\ \text{conductor 1}\Longrightarrow\zeta\text{），但}\textbf{其证明用解析工具}\in C_{\rm analytic}\（V157\ \text{#8}）⟹ \boxed{\text{"进一步收缩"＝重述而非缩减}},\ \text{残余更新}\ \boxed{\textbf{是否存在非解析的 ζ-结构刻画？}}$$
$$\qquad ⚠️\ \text{边界}：本档不证明范式穷尽；§5"唯一已知候选"为 [结构性]；}C_{\rm analytic}\ \text{的界定依赖 }E106$$
$$\qquad\textbf{下一步 ＝ }V161 ✓：\boxed{\text{证明或否定：任何非解析的 }\Phi:\Lambda_M\xrightarrow{\sim}Z_\zeta-\tfrac12\ \text{都必须重新引入某一解析接口}}\ \text{（可证}\Longrightarrow\text{C6 封死于 }C_{\rm analytic}\text{，非 }A1/A3;\ \text{不可证且能构造反例}\Phi\Longrightarrow\textbf{C6＝真正第七类}）$$

### F.5w ⭐⭐⭐⭐⭐ **非解析谱双射的结构性穷尽审计（类 C 硬审计）**（`V161` ✓ 2026-09-15 10:52）—— **目标改造｜C6 ＝ 零点无关 ζ 本体刻画｜三分 A/B/C｜类 C 三障碍**

$$\text{目标改造} ✓✓：\textbf{不证}\text{"任何非解析 }\Phi\ \text{必须解析化"}（\text{过强／很可能不可证}），\ \text{改为}\textbf{反证审计};\ \text{禁止集}＝\{\text{explicit formula},\text{Mellin},L\text{-function},\text{Hadamard},\text{argument principle},\text{Li/Weil}\};\ \text{问}\ \boxed{\text{是否存在独立非解析定义的对象}\ \mathfrak S\ \text{同时有}\ M\to\mathfrak S\leftarrow\zeta\ \text{两种独立实现？}}$$
$$\textbf{第一刀（最关键重写）}：\text{不允许}\ \mathfrak S_\zeta:=Z_\zeta-\tfrac12\（\text{换名字}）／\mathfrak S_\zeta=\{\lambda:\zeta(\tfrac12+i\lambda)=0\}\（\text{＝C6.6 本身}）⟹ \text{须存在}\ \boxed{\textbf{零点无关谓词}\ P_\zeta(x)}\ \text{使}\ \boxed{P_\zeta(x)\iff\zeta(\tfrac12+ix)=0}\ (\text{V161.1}),\ \textbf{且}\ \text{证}\ P_\zeta\iff Z_\zeta\ \text{本身}\textbf{不得用六接口} ⟹ \boxed{\text{C6}\ \text{已不是"构造另一个谱"，而是找}\textbf{零点无关的 ζ 本体刻画}}$$
$$\textbf{第二刀（信息来源三分）}：\text{A 算术／Euler} ⟹ \textbf{撞 }V152\text{–}V154\ \text{的}\exists/\lambda\ \text{分裂}：\text{算术}\textbf{能}\text{表达 RH（Robin）},\ \text{但需}\textbf{逐点识别}\ x\leftrightarrow\rho ⟹ \boxed{\text{RH-equivalent arithmetic predicate}\not\Rightarrow\text{zero-position correspondence}};\ \text{若 }P_\zeta\ \text{真能逐点给零点须另携}\ x\ \text{的定位机制}（＝V153\ \text{的 }\lambda\text{-supply}）;\ \text{B 几何／代数}：\operatorname{Spec}(X_\zeta)=\{\pm i\gamma_n\}\ \text{须同时证}\ =Z_\zeta-\tfrac12,\ \text{若不经零点定义则是}\textbf{真新结构} ⟹ \textbf{不能提前判死};\ \text{硬条件}\ \boxed{X_\zeta\ \text{须同时解释"为什么是 ζ"与"为什么是这些 }\gamma_n"}\（\text{单纯漂亮}\ \sqrt N e^{i\theta}\ \text{不够}\ —— V144\ \text{已证 CM／Hecke 可做到却不识别 ζ}）;\ \text{C 组合／逻辑／范畴}：\text{构造}\ \mathcal C_\zeta\ \text{完全不用零点},\ \text{须}\operatorname{Aut}(\mathcal C_\zeta)\ \text{或}\operatorname{Spec}(\mathcal C_\zeta)\ \text{恰给}\ \gamma_n ⟹ \textbf{不能被 }V150/V151\ \text{直接杀死}（\text{不必是序／torsor／Frobenius／正性／trace／显式公式}）＝\textbf{真正残余}$$
$$\textbf{第三刀（精确分界）}：\mathcal P＝\{\text{不用六接口的构造}\},\ \mathcal Z＝\{P:P(x)\iff\zeta(\tfrac12+ix)=0\} ⟹ \text{C6 存在}\iff \boxed{\exists P\in\mathcal P:\ P\iff\text{零集}}\ (\text{V161.2})\ \text{＋}\ \boxed{\exists M:\Lambda_M=\{x:P(x)\}}\ (\text{V161.3}),\ \text{两条件缺一不可}$$
$$\textbf{第四刀（危险漏洞）}：\text{纯代数对象 }A_\zeta\cong A\ \text{但同构证明偷用}\ \xi,\xi'/\xi,L,\text{Mellin} ⟹ \text{只是}\ \boxed{\text{non-analytic definition ＋ analytic identification}}\ \text{不是 C6} ⟹ \boxed{\text{definition independence}\neq\text{proof independence}} ⟹ \text{V161 须}\textbf{同时}\text{要求定义与识别证明都不经 }C_{\rm analytic}\（\textbf{硬性准入}）$$
$$\textbf{第五刀（硬二分）}：\text{若存在 }S_\zeta\ \text{同时满足}\{\text{不用零点定义},\text{不用六接口},\operatorname{Spec}(S_\zeta)=Z_\zeta-\tfrac12\} ⟹ \textbf{真第七类候选};\ \text{否则}\ C6\subset C_{\rm analytic}$$
$$\textbf{⭐ 类 C 硬审计（本档新增，按唐先生指定第一目标）}：\text{把"离散结构}\to\text{连续谱"逐个推到底} —— \textbf{C-i 有限状态／组合动力学} ⟹ 其动力 ζ 函数（\textbf{Artin–Mazur}）\textbf{有理}, \text{而有理函数只有}\textbf{有限多个零点}，\zeta\ \text{有}\textbf{无限多零点} ⟹ \textbf{类型不匹配，整类排除} ✗✓;\ \textbf{C-ii 无穷状态＋需 Weyl 型离散谱} ⟹ 须紧预解算子（Weyl 律）⟹ 即须\textbf{算子谱理论}，落已关的 }L1（\text{非自伴谱刚性 NO-GO}）／\mathrm{II} ✗;\ \textbf{C-iii 选择性编码}\ \gamma_n ⟹ \text{已把零位置编入} ⟹ \textbf{偷渡 β／selection} ✗ ⟹ \boxed{\text{唯一}\textbf{未封闭形态}＝\text{一个}\textbf{无穷状态、非算子化、却能产生 Weyl 型离散谱}\text{的组合／范畴结构}}\ \text{（}\textbf{未被三障碍覆盖}，即唐先生要求"不要杀它"的那一类）}$$
$$\qquad ⚠️\ \text{边界}：C-i 依 Artin–Mazur（经典）；C-ii 依 Weyl 律＋L1 NO-GO（档案）；C-iii 依 C6.1／V148};\ \text{"唯一未封闭形态"为}\textbf{已削三块}的陈述，\textbf{不是}\text{"只剩这一块"的定理} ✗$$
$$\textbf{成功标准与纪律}：\textbf{不得}\text{把"找不到 }S_\zeta\text{"升成"不存在"（}V136/V144\ \text{纪律）};\ \textbf{DEAD}＝\text{证}\ \boxed{\text{任何零点无关的 ζ-结构刻画}\Rightarrow C_{\rm analytic}};\ \textbf{ALIVE}＝\text{给出具体 }S_\zeta\ \text{并实际推出}\ \boxed{\operatorname{Spec}(S_\zeta)=Z_\zeta-\tfrac12}（\text{而非只得 RH／计数／统计／RH-equivalent criterion}）$$
$$\qquad\textbf{下一步三选}：①\ \text{攻唯一未封闭形态（能否构造无穷状态、非算子化、产生 Weyl 型离散谱的组合／范畴结构？）};\ ②\ \text{审 C-i 边界（"有理 vs 无限零"能否加强为"零密度}\Longrightarrow\text{非有理"型定理）};\ ③\ \text{审 B 类硬条件} ✓$$

### F.5x ⭐⭐⭐⭐⭐ **C-i「有理性 → 零密度受限」升级审计 ＝ FSC 判据**（`V162` ✓ 2026-09-15 10:59）—— **纠正"零密度⇒非有理"｜FSC ＋ C-i⋆｜(W) 便宜、内生承重**

$$\textbf{① 纠正} ✗✓：\textbf{不写}\ \text{"零密度}\Rightarrow\text{非有理"}\ \text{（一般定理）};\ \text{完整形式}＝\boxed{\text{有理动力学}\Rightarrow\text{周期／代数型谱}\Rightarrow\text{零点计数增长受限}}\ \text{再证 ζ 违反上界};\ \text{反例}\ f(z)=\prod(1-z/2^n)\ \text{有无限零点却非有理} ⟹ \text{无限零点}\Rightarrow\text{非有理}\ \text{成立，但"零密度"（}N(T)\sim cT\text{）}\textbf{不是}\text{有理性的充分必要刻画} ⟹ \boxed{\text{non-rational}\not\Rightarrow\text{Weyl spectrum}}$$
$$\textbf{② FSC（有限状态谱容量定理）} ✓✓：\text{有限状态转移矩阵 }A：Z_A(z)=1/\det(I-zA)\ ✓;\ \operatorname{Spec}(A)=\{\lambda_1..\lambda_m\}\Longrightarrow Z_A(z)=\prod(1-\lambda_jz)^{-1} ⟹ N_{Z_A}(R)\le m\ \text{（有限 }z\text{-平面内只有有限基本零／极点）};\ \text{经固定解析参数化 }z=\chi(s)\ \text{的 }s\text{-零点只能来自有限个代数条件 }\chi(s)=\lambda_j^{-1} ⟹ \boxed{\dim(\text{state space})<\infty\Longrightarrow\text{independent spectral channels}<\infty};\ \text{链条}：\boxed{\text{finite-state}\Rightarrow\text{rational dynamical zeta}\Rightarrow\text{finite spectral channels}\Rightarrow\Phi\ \text{不可能完整识别 ζ 零谱}}$$
$$\textbf{③ 与 ζ 比较} ⟹ \textbf{C-i}^\star：N_\zeta(T)=\tfrac{T}{2\pi}\log\tfrac{T}{2\pi}-\tfrac{T}{2\pi}+O(\log T) ⟹ N_\zeta(T)/T\sim\tfrac1{2\pi}\log T\to\infty ⟹ \boxed{\text{finite-state combinatorial carrier}\not\cong Z_\zeta-\tfrac12}\ \text{（长期可引用排除式）}$$
$$\textbf{④ 三级结构（}C-ii\ \textbf{不能由 }C-i\ \text{推出）}：\text{有限状态}\Rightarrow\text{rational／有限谱通道}\Rightarrow\text{排除 ζ 完整谱};\qquad \textbf{无限状态}\not\Rightarrow\text{operator}\Rightarrow\textbf{仍开放}（\text{无限状态可有 }N(T)\asymp T\log T）⟹ N_\zeta(T)\sim T\log T\not\Rightarrow\text{operator}$$
$$\textbf{⭐ ⑤ 两项分解（本档新增）}：\text{(W)}\ N_\Lambda(T)\sim\tfrac{T}{2\pi}\log\tfrac{T}{2\pi}\ \textbf{单独不构成约束} ✓✓\ \text{—— 对任何给定递增计数函数 }N(T)\ \text{都存在递增序列实现它（取 }\lambda_n:=N^{-1}(n)\text{）} ⟹ \text{计数条件}\textbf{廉价可实现，不承重}; \text{三项要求}：\text{(1) 无限性（有限已被 C-i}^\star\ \text{杀）};\ \text{(2) Weyl 容量（须自然产生 }T\log T\ \text{而非 }T/T^\alpha/e^T\text{）};\ \text{(3) }\textbf{点定位}（\text{须产生}\textbf{每个 }\lambda_n,\ \text{而非只给 }N(T)\text{）} ⟹ \text{真正承重}\ \boxed{\text{内部机制产生 }\lambda_1,\lambda_2,\dots\ \text{而不可作为外部参数输入}};\ ⭐\ \text{附：}T\log T\ \text{的"非组合性"}\（\text{纯组合计数天然给出 }T^d\ \text{或}\ e^{cT}，\ T\log T\ \text{介于两者且恰是 1 维半经典密度律}\）⟹ \text{要}\textbf{自然}\text{产生它通常须}\ \boxed{\textbf{连续化}\text{步骤}} ⟹ \text{正是解析结构（[结构性] ⚠️）}$$
$$\textbf{⑥ 五条件压缩后残余}：\boxed{\textbf{无限状态}\ \downarrow\ \textbf{非算子化}\ \downarrow\ \textbf{内生地产生 }T\log T\ \textbf{离散谱}\ \downarrow\ \textbf{不输入 }\gamma_n\ \downarrow\ \Lambda_M=Z_\zeta-\tfrac12}（\text{五项须同时成立}）⟹ \text{若可证该形态}\textbf{必然退化}\text{为算子谱／解析谱／外部编码} ⟹ \textbf{C 类接近封口};\ \text{若找到满足五项的机制} ⟹ \textbf{第一个真正有资格叫 C6／第七类}\ \text{的东西}$$
$$\qquad ⚠️\ \text{与 }V153/V155\ \text{接口}：\text{承重项（内生＋逐点锁定）}＝V153\ \text{的 }\lambda\text{-supply}＝V155\ \text{的 }A\to\lambda\ \text{箭头} ⟹ \text{残余}\textbf{回到同一点}（\text{未产生新墙}）$$
$$\qquad ⚠️\ \text{边界}：\text{观察 1 为构造性} ✓;\ \text{观察 2 为归约} ⚠️;\ \text{观察 3（}T\log T\ \text{非组合性）为结构性} ⚠️\ \text{非定理};\ \text{FSC 依 Artin–Mazur／Ruelle（经典）}＋L1\ \text{NO-GO}$$
$$\qquad\textbf{下一步三选}：①\ \text{攻承重项（内生＋逐点锁定 ＝ V153 }\lambda\text{-supply／V155 箭头），但须}\textbf{新入口};\ ②\ \text{把 FSC 写成}\textbf{工具卡}（给定组合载体 }\Rightarrow\ \text{查 state space 有限性 }\Rightarrow\ \text{判 }\Phi\ \text{不可能）;\ ③\ \text{审能否把"}\ T\log T\Rightarrow\text{连续化"上升为定理} ✓$$

### F.5y ⭐⭐⭐⭐ **FSC 工具卡（基础设施，非突破口）**（`V163` ✓ 2026-09-15 11:06）

$$\text{最终判据}：\dim\mathcal S<\infty\ +\ Z_{\mathcal S}(z)=1/\det(I-zA)\Longrightarrow Z_{\mathcal S}\ \text{rational};\ A\in M_m(\mathbb C)\Longrightarrow\det(I-zA)=\prod(1-\lambda_jz)\Longrightarrow Z_{\mathcal S}=\prod(1-\lambda_jz)^{-1} ⟹ \text{基本零／极点通道}\le m$$
$$\qquad ⚠️\ \textbf{措辞修正（唐先生判定）}：\textbf{不得}\text{把 }N_{Z_A}(R)\le m\ \text{写成所有"零点计数"的统一表述 —— 周期覆盖 }z\mapsto e^s\ \text{下一个有限 }z\text{-平面奇点可对应 }s\text{-平面}\textbf{无限周期复制} ⟹ \text{真正不变量应叫}\ \boxed{\textbf{有限基本谱通道}}\ \text{而非" }s\text{-平面零点有限"}$$
$$\text{三步流程}：\text{FSC-1 状态有限性（}\exists\ \text{有限 }\mathcal S\ \text{使动力学由 }F:\mathcal S\to\mathcal S\ \text{或有限 }A\ \text{完整描述）}\Longrightarrow Z_M\ \text{rational};\ \text{FSC-2 谱通道有限（周期／代数映射产生的无限复制仍只算有限基本通道）};\ \text{FSC-3 目标是否要求 ζ 完整谱（需 }N_\zeta(T)\to\infty\ \text{且 }N_\zeta(T)/T\sim\tfrac1{2\pi}\log T\text{）}\Longrightarrow \boxed{\text{FSC}=DEAD}$$
$$\text{边界纪律}：\textbf{FSC 不判死}\ |\mathcal S|=\infty／Z_M\ \text{非有理}／N_M(T)\sim T\log T ⟹ \boxed{\textbf{FSC 只杀 finite-state，不杀 infinite-state}}$$
$$\text{复用筛选器}：\text{任何新提案先问}\ \boxed{\dim(\text{完整状态空间})<\infty\ ?}\ \text{若是}\Longrightarrow\text{FSC-DEAD 直接结束（不再讨论 Weyl law／谱统计／周期轨道／动力 ζ／"增加几个状态"／有限图／有限自动机／有限群作用）};\ \text{附声明表格式（FSC-1/2/3 三栏）—— 判据为声明式，故本卡为流程卡＋声明表，非脚本}$$
$$\qquad ⚠️\ ③（T\log T\Rightarrow\text{连续化}）\ \textbf{按唐先生指示放弃} ✓\ \text{（}N(T)\sim T\log T\ \text{几乎无承重能力；}\lambda_n:=N^{-1}(n)\ \text{可人为制造完全离散序列）}$$

### F.5z ⭐⭐⭐⭐⭐ **非算子化无限结构如何内生连续谱参数（机制本体）**（`V164` ✓ 2026-09-15 11:06）—— **三形态穷尽｜FSC 推广｜陈述类型分离｜四例元规律**

$$\text{五条硬条件}：\mathcal R(M,\lambda)=0\ \text{独立定义};\ \exists!\lambda;\ \lambda\in\mathbb R\ \text{非外部};\ \mathcal R\ \text{非解析接口};\ \mathcal R(M,\lambda)=0\iff\zeta(\tfrac12+i\lambda)=0\（\text{末行＝最硬 C6.6}）$$
$$\textbf{⭐ 三形态穷尽（本档核心）}：\text{(i) }\textbf{逼近型}（\text{Cauchy 模数／嵌套区间／受限展开／收敛级数}）⟹ \lambda\ \text{为}\textbf{可计算实数}，\text{代价＝}\textbf{收敛结构}（metric／topology／modulus）\ \text{隐含一个连续化接口};\ \text{(ii) }\textbf{选择型}（\text{非主超滤子／Banach 极限／filter 极限}）⟹ \lambda\ \text{是序列的函数}，\text{由 }V153\ \text{Theorem 1 相等的有限阶段数据}\Longrightarrow\text{相等输出}，\text{但}\textbf{与 ζ 的识别须另证};\ \text{(iii) }\textbf{隐式方程型}（\mathcal R(M,\cdot)=0\ \text{含不动点）}⟹ \text{若 }\mathcal R\ \text{只由有限数据定义则解集有限／代数型，若由无限数据定义则回到 (i)(ii)}$$
$$\qquad\Longrightarrow \boxed{\text{三形态穷尽}：\text{任何"离散无限结构}\Longrightarrow\text{连续内生参数"都须提供}\ \text{收敛结构／选择结构／无穷阶方程}\ \text{之一}}（\textbf{[结构性] ⚠️}）\ \text{且}\ \textbf{三形态都只解决"内生 }\lambda\text{"（条件 1–4），都不触碰"}\lambda\ \text{是 ζ 零点"（条件 5）}$$
$$\textbf{⭐ FSC 推广}：\text{若 }\mathcal R\ \text{由}\textbf{有限数据}\text{定义} ⟹ \text{(a) }\textbf{解析型条件}（有理／半代数／解析方程）⟹ \text{解集}\textbf{有限或代数型} ⟹ \text{不能承载 ζ 完整谱（元素超越且分布 }T\log T）；\ \text{(b) }\textbf{可定义型条件}（有限数据描述地定义任意集合）⟹ \text{落}\ \boxed{\textbf{类 VI（可定义性／正则性）}}\ ✗ ⟹ \boxed{\text{"有限数据"路线两条出口皆已封闭}}$$
$$\textbf{⭐ 陈述类型分离}：\text{条件 1–4}＝\textbf{局部生成命题}（\Sigma\text{-型}：存在且唯一）；\ \text{条件 5}＝\textbf{ζ 全局结构命题}（指定全局对象的整个零集）⟹ \boxed{\text{类型不同} ⟹ \text{1–4 对 5}\textbf{零贡献}}（\text{不是"还没做到"而是}\textbf{类型不匹配}）$$
$$\textbf{⭐⭐ 元规律：四例"陈述类型不匹配"}：V148（局部\textbf{选择} vs RH＝ι 无自由轨道／缺席型）; V152（\textbf{语法} β-free vs \textbf{语义} β-信息最大）; V153（\textbf{∃-信息} vs \textbf{λ-信息}）; V164（\textbf{局部生成} vs \textbf{全局同一}）⟹ \boxed{\text{四例同源}：\text{RH 及其相关命题是}\textbf{全局缺席型}，\text{而全部可行候选机制是}\textbf{局部存在／选择型}}（\textbf{[结构性]} 归纳，非定理）;\ \text{诊断用法：新提案先问"输出的是【局部存在】还是【全局缺席】？"}$$
$$\qquad\textbf{下一步三选}：①\ \text{攻条件 5 的}\textbf{类型}（\text{能否证"全局同一性}\Rightarrow\text{必经 ζ 全局结构"＝类型定理）};\ ②\ \text{把四例元规律写成}\textbf{诊断工具卡}（与 }V163\ \text{同层）};\ ③\ \text{审 §2 三形态穷尽能否形式化} ✓$$

$$\textbf{⚠️ ERRATUM（T10 · 唐先生 2026-09-15 11:10 ✓）}：\text{上节四例"陈述类型不匹配"的结论}\ \boxed{\text{RH 及相关命题是全局缺席型；全部可行候选机制是局部存在／选择型}}\ \textbf{不得作定理} ✗✓\ \text{—— 理由：存在}\textbf{全局结构命题}\ \forall x\,P(x)\ \text{其证明机制本身可以是}\textbf{真正的全局结构定理}，\textbf{不必}\text{先经局部存在}。\ \text{正式版本}\ \boxed{\textbf{诊断假设 H}：\text{当前已审计候选主要输出局部生成／选择信息，而 C6.6 要求全局谱同一性}\ \（\textbf{经验性},\ \textbf{非定理}）$$

### F.5aa ⭐⭐⭐⭐ **陈述类型不匹配诊断卡（工具卡，基础设施）**（`V165` ✓ 2026-09-15 11:10）

$$\text{核心筛子}：\boxed{\operatorname{Type}(P)=(\text{信息域},\text{量词结构},\text{对象范围},\text{输出对象})}\ \text{新候选先做四项审计}$$
$$\textbf{T1 局部／全局}：\text{机制只处理有限阶段／单个局部对象}\（M_n\to a_n）\ \text{而目标要求}\ \forall n\,P(a_n)\ \text{或整个 }X\ \text{满足 }P ⟹ \text{必须明确指出}\textbf{局部}\to\textbf{全局的桥梁};\ \text{无桥梁} ⟹ \boxed{\text{LOCAL}\not\Rightarrow\text{GLOBAL}}$$
$$\textbf{T2 存在／定位}：\exists a\,R(a)\ \text{只证"有东西"};\ \lambda=\Lambda(M)\ \text{须给}\textbf{身份／位置} ⟹ \boxed{\exists\text{-information}\not\Rightarrow\lambda\text{-information}}（=V153\ \text{核心筛子}）$$
$$\textbf{T3 生成／同一}：\Lambda_M=\{\lambda_n\}\ \text{vs}\ \Lambda_M=Z_\zeta-\tfrac12 ⟹ \boxed{\text{generation}\neq\text{identification}};\ \textbf{即使}\ N_{\Lambda_M}(T)=N_\zeta(T)\ \textbf{仍不足}\text{以得 }\Lambda_M=Z_\zeta-\tfrac12$$
$$\textbf{T4 语法／语义}：\boxed{\text{syntactic absence}\neq\text{semantic absence}}（\text{Robin 语法 β-free、语义最大}）⟹ \textbf{不得}\text{用"形式上没有 }\rho,\beta\text{"作为}\textbf{非循环性}\text{的证明}$$
$$\text{压缩筛子（4 维：范围 LOCAL/GLOBAL｜量词 }\exists/\forall\text{｜输出 GENERATION/IDENTIFICATION｜表述 SYNTACTIC/SEMANTIC）}；\ \text{三处断裂}\ \boxed{\text{LOCAL}\to\text{GLOBAL},\ \exists\to\text{LOCATION},\ \text{GENERATION}\to\text{IDENTIFICATION}}\ \Longrightarrow\ \text{必须提供}\textbf{额外定理},\ \text{否则}\ \boxed{\text{TYPE-MISMATCH / STOP}}（\text{而非继续堆计算}）$$
$$\text{今晚干净结论四行}：V161\ \text{有限组合}\Rightarrow\text{FSC-DEAD}｜V162\ \text{Weyl count 本身不承重}｜V164\ \text{内生连续参数仍不足以识别 ζ}｜V165\ \boxed{\text{generation}\not\Rightarrow\text{identification}}$$
$$\qquad\textbf{下一刀 ＝ ①}：\boxed{\text{"全局同一性是否必然需要 ζ 的全局结构？"}}\ \text{可证} ⟹ \textbf{C6 真正封口};\ \text{打不出} ⟹ \text{停止"收窄"，转而}\textbf{主动构造反例性全局结构}\ \mathfrak S_\zeta$$

### F.5ab ⭐⭐⭐⭐⭐ **C6.6 的 global identification 攻击 ＝ o-极小性障碍 ⟹ 终局 A（条件性封口）**（`V166` ✓ 2026-09-15 11:13）

$$\text{判据锁死}：\text{只允许终局 A（封口）或 B（活路）};\ \textbf{不允许终局 C}（\text{"又发现一个更深的 gap"}）$$
$$\textbf{第一刀}：P_M(\lambda):\iff\lambda\in\Lambda_M,\ P_\zeta(\lambda):\iff\zeta(\tfrac12+i\lambda)=0,\ \text{C6.6}\iff\boxed{P_M\iff P_\zeta};\ \text{⚠️ 不能说"这是 global 所以必须用 global structure"}（\text{把要证的当前提}）⟹ \text{等价式须对}\textbf{每个 }\lambda\ \text{成立} ⟹ \boxed{P_M\ \textbf{不只是生成谱}，而是新的零点独立的}\textbf{零点判定器}} ⟹ \text{C6.6 必须产生}\ \text{独立结构}\Longrightarrow\zeta\ \text{零点谓词}（\text{而非}\ \text{独立结构}\to\{\lambda_n\}＝V164）$$
$$\textbf{B1–B4}：\text{B1 }M\ \text{含 ζ 全局信息} ⟹ \boxed{\text{definition smuggling}}\ \mathrm{DEAD};\ \text{B2 等价证明用解析恒等式}\（\xi'/\xi,\zeta'/\zeta,\text{Mellin},\text{Hadamard},\text{EF}）⟹ C_{\rm analytic}（\text{⚠️ 不得声称"所有证明必如此"}）;\ \text{B3 只有统计／计数一致}\（N_M=N_\zeta\ \text{或}\ \sum f\ \text{一致}）⟹ \boxed{\text{GENERATION/COUNT}\not\Rightarrow\text{IDENTIFICATION}};\ \text{B4 }\textbf{结构同构＝唯一生存形态}：\Phi:M\to\mathfrak Z\ \text{自然同构},\ \operatorname{Spec}(M)=\operatorname{Spec}(\mathfrak Z),\ \textbf{并且}\ \text{另有独立于零点的定理}\ \operatorname{Spec}(\mathfrak Z)=Z_\zeta-\tfrac12\（\text{最后一步最难}）⟹ \text{这是}\textbf{对象识别问题}，\text{非 }V164\ \text{的"生成 }\lambda\text{"}$$
$$\textbf{⭐⭐ 本档新增 o-极小性障碍}：\text{(观察 1) }P_M\ \text{的外延是 ℝ 子集}\ \{\gamma_n\};\ \text{(引理 1, 经典) o-minimal 结构中可定义的 ℝ 子集必为}\ \boxed{\text{有限多个点与开区间的并}}\ ⟹ \textbf{不能}\text{定义任何}\ \boxed{\text{无限离散集}}\（\text{如 }\mathbb Z）;\ \text{(引理 2, 经典无条件) }Z_\zeta-\tfrac12\ \text{离散且无限多} ⟹ \text{是无限离散集} ⟹ \boxed{P_M\ \textbf{不可能}\text{在任何 o-minimal 语言中定义}}$$
$$\qquad\Longrightarrow\ \textbf{二分}：\text{(L1) }\mathcal L\ \text{o-minimal} ⟹ P_M\ \text{不存在} ⟹ \textbf{C6.6 不可能};\ \text{(L2) }\mathcal L\ \text{非 o-minimal} ⟹ \text{须含一个}\textbf{非 o-minimal 化装置},\ \text{而}\textbf{一切已知}\text{此类装置落于}\ \text{(i) 六接口族}\ \cup\ \text{(ii) }\textbf{类 VI}（\text{任意描述性定义}）$$
$$\qquad\Longrightarrow\ \boxed{\textbf{终局 A（条件性封口）}：\text{满足 C6.6 的 }P_M\ \text{必定义 ℝ 中无限离散集} \Longrightarrow \text{语言必非 o-minimal} \Longrightarrow \text{必含非 o-minimal 化装置} \Longrightarrow \text{已知此类装置全在}\ \textbf{六接口}\cup\textbf{类 VI}\ \Longrightarrow C6\subseteq C_{\rm analytic}}$$
$$\qquad\textbf{残余（不是"更深的 gap"，而是}\textbf{具体设备表}）②：\text{①非 o-minimal 化装置的}\textbf{穷尽性}：是否存在既不在六接口亦不落类 VI 者？\\text{候选表（可逐条审计）}：(a) \mathbb Z\ \text{在 ℝ 的统一定义}（\sin/\lfloor\cdot\rfloor/\text{exp 型}）;\ (b) \text{周期／拟周期}（\sin,\text{Jacobi},\text{模形式}）;\ (c) \text{完整解析对象};\ (d) \text{集合论／描述性任意定义};\ (e) \text{非标准模型}（\text{超积仅模型论容器，}V136\ \text{已判）} ⟹ \text{(a)(b)(c) 解析型}\to C_{\rm analytic};\ \text{(d)}\to\text{类 VI};\ \text{(e) 无信息};\ \text{②}\textbf{o-minimal 语言边界的界定}（\text{机制的定义语言是否总可规范为一阶 ℝ-结构？}）$$
$$\qquad ⚠️\ \text{边界}：\text{引理 1 为 o-minimality 定义级经典；引理 2 为经典无条件；"已知装置全落六接口}\cup\text{类 VI"为}\textbf{[结构性]} ⚠️\ \textbf{非穷尽性定理} ⟹ \text{本档为}\textbf{条件性封口}，}\textbf{不是}\text{无条件 DEAD}$$
$$\qquad\textbf{下一步（二选，不得有第三项）}：①\ \text{审计残余①的 (a)–(e)，看是否有既非六接口亦非类 VI 的非 o-minimal 化装置（一项即够 → 转终局 B 路线）};\ ②\ \text{界定"机制定义语言"能否规范为一阶 ℝ-结构} ✓$$

### F.5ac ⭐⭐⭐⭐⭐ **逐项审计 (a)–(e) ＋ 双义务结构**（`V167` ✓ 2026-09-15 11:16）—— **五项全部不构成 escape ✓✓｜但五项全死 ⟹ 更强的条件性封口（非无条件 DEAD）✓✓**

$$\text{审计标准}：D＝\{\text{装置能定义无限离散 }P_M\subset\mathbb R\}\ \text{＋五问}（\text{零点独立？非解析接口？非选择？逐点输出 }\lambda\text{？可能证 }P_M=P_\zeta\text{？}）$$
$$\textbf{(a) }\mathbb Z\ \text{统一定义}\（\sin(\pi x)=0,\lfloor x\rfloor=x）⟹ \boxed{\text{DEAD}}：\text{必须区分}\ \boxed{\text{"定义 }\mathbb Z"\neq\text{"定义 ζ 零点"}} ⟹ \text{即使 }P_M=\mathbb Z\ \text{仍无理由得 }P_M=Z_\zeta-\tfrac12;\ \text{若用解析 }F\ \text{使 }F(\lambda)=0\iff\zeta(\tfrac12+i\lambda)=0\ \text{则识别已进入解析接口 —— 死因不是"能定义 ℤ 所以没用"，而是}\ \boxed{\text{离散化能力}\not\Rightarrow\zeta\ \text{逐点识别能力}}$$
$$\textbf{(b) 周期／拟周期}\（\sin,\text{Jacobi/theta},\text{模形式}）⟹ \boxed{\text{DEAD}}：\text{周期性给 }P(x+T)=P(x)\ \text{或有限/可描述群作用不变性};\ \text{而 ζ 非平凡零点的 ordinates}\textbf{无已知固定周期结构};\ \text{即使拟周期仍须证}\ P(\lambda)=0\iff\zeta(\tfrac12+i\lambda)=0,\ \text{若由 theta/Mellin/模形式建立联系则仍进入既有解析接口 —— 死的是"周期性本身足以完成 identification"}$$
$$\textbf{(c) 完整解析对象＋延拓}\（F=\zeta\ \text{或同延拓/FE/增长}）⟹ P_M(\lambda)\iff F(\tfrac12+i\lambda)=0\ \textbf{当然可逐点识别}，但已把目标放进定义/证明载体}\ M\rightsquigarrow F\rightsquigarrow Z_\zeta ⟹ \boxed{\text{DEAD}}\ \text{属 B1/B2}$$
$$\textbf{(d) 集合论／描述性任意定义} ⟹ \boxed{\text{DEAD}}：\text{可直接取 }A=Z_\zeta-\tfrac12,\ \text{但}\textbf{正好违反 }V166\ \text{核心要求}\ \boxed{\text{零点独立性}} ⟹ \text{属 selection／definition smuggling／类 VI};\ ⚠️\ \text{"集合论能定义无限离散集"}\textbf{本身没问题}，\text{死的是用任意定义能力实现 ζ 零点识别}$$
$$\textbf{(e) 非标准模型／超积} ⟹ \boxed{\text{DEAD}}：\text{超积可产生}\ ^*\mathbb N,{}^*\mathbb R\ \text{把无限过程转成内部对象}，\text{但 }V136\ \text{关键限制}：\textbf{超积改变模型层，不自动产生新的 ζ 点位置信息};\ \text{形式上 }M=\prod_{\mathcal U}M_i\ \text{只提供 }\operatorname{Th}(M)\ \text{／内部结构} ⟹ \text{要得 }\operatorname{Spec}(M)=Z_\zeta-\tfrac12\ \text{仍须 identification theorem（用 ζ 解析性质}\Rightarrow C_{\rm analytic};\ \text{直接放零点序列}\Rightarrow\text{smuggling）}$$
$$\text{五行表}\（\text{能否产生无限离散集／能否独立产生 ζ 逐点集合／死因}）：\text{(a) ✓/✗/离散化≠identification};\ \text{(b) ✓/✗/周期结构≠ζ 零集};\ \text{(c) ✓/✓/}C_{\rm analytic}\text{／smuggling};\ \text{(d) ✓/表面 ✓/definition,selection（类 VI）};\ \text{(e) ✓/✗/不产生新位置} ⟹ \boxed{(a)\text{–}(e)\ \text{全部不构成 C6 escape}}$$
$$\textbf{⚠️ 纠正（本档必守）}：\boxed{\text{五项全死}\not\Rightarrow\text{无条件 }\mathrm{DEAD}}\ ——\ \text{最多证明"这五个装置不是逃逸口"} ⟹ \boxed{\text{五种已知非 o-minimal 装置}\not\Rightarrow\text{所有可能装置}};\ \textbf{终局 B 要求}\text{一个}\textbf{五项之外且确实满足 C6.1–C6.6 的具体构造} ⟹ \text{结论强度 ＝}\textbf{更强的条件性封口}（\text{与 }V136/V144/V165\ \text{同型纪律：不得把"全死"写成"不存在其它"}）$$
$$\textbf{⭐ 双义务结构（本档新增）}：\text{任何零点独立的无限离散生成器须同时通过两项}\textbf{独立}义务：\boxed{\textbf{L-义务}（语言层）：\text{定义 }P_M\ \text{的语言必须非 o-minimal}}\（V166\ \text{引理 1＋2}）\ \text{与}\ \boxed{\textbf{I-义务}（内容层）：\text{必须证明 }P_M=P_\zeta\（逐点同一性）}\（V165\ \text{T3／B3}）⟹\ ⭐\ \textbf{两义务独立}：\text{满足 L 不蕴含满足 I}（(a)(b) 有离散化能力却无识别）；\ \text{满足 I 不蕴含满足 L}（(c)(d) 有识别能力却把目标放进定义）⟹ \text{五项死因}\textbf{各不相同}却\textbf{恰好覆盖两处}：\text{(a)(b)(e) 死於 I-义务};\ \text{(c)(d) 死於 smuggling／类 VI（绕过 L 而非满足）} ⟹ \text{未来候选必须}\textbf{同时}\text{通过 L 与 I} ＝\textbf{双门筛子}（与 }V163\ \text{FSC 卡同层）$$
$$\qquad\textbf{更锋利的问题}：\boxed{\text{什么东西能产生无限离散实数集，却既非解析离散化、周期结构、任意集合编码，也非超积？}}\ \text{若存在须同时解决}\ \boxed{\text{discreteness}+\text{endogenous }\lambda+\text{pointwise identification}}\ \text{且不偷放 }\gamma_n$$
$$\qquad\textbf{V168 立项}：\text{不再审计"数学领域"，而审计}\ \boxed{\text{"离散实数生成机制"的逻辑分类}};\ \text{目标（表示定理）}\ \boxed{\text{任何零点独立的无限离散实数生成器}\Rightarrow\text{可归约为某类已审计装置}};\ \text{若证不出} ⟹ \textbf{立即反向构造}\text{一个五项之外的生成器}（\text{符合"定理封口或造出反例性结构"的二分）}$$

### F.5ad ⭐⭐⭐⭐⭐ **L-分类失败（第六类 $\mathrm I_{\rm sort}$）＋ 转向以 I 为不变量 ＋ I-分类第一刀 ＋ 构造尝试**（`V168` ✓ 2026-09-15 11:18）

$$\text{L-分类第一层}：P_M\ \text{无限离散}\subset\mathbb R\ \text{不可能由 o-minimal 结构定义} ⟹ \text{按"非-o-minimal 从哪进入语言"分类}：\{\text{内部振荡},\text{离散对象},\text{离散排序},\text{外加谓词},\text{非标准／外部极限}\};\ \text{第一类（内部振荡）}\mathrm I_{\rm osc}\subset(a,b)\（\mathrm L\checkmark,\mathrm I\times）;\ \text{第二类（离散对象直接映入 ℝ）}：\Lambda=f(\mathbb N)$$
$$\textbf{⭐ 第六类 }\mathrm I_{\rm sort}：\text{二排序结构}\ \mathcal M=(\mathbb R,\mathbb N,+,\times,<,f),\ f:\mathbb N\to\mathbb R;\ P_f(x)\iff\exists n:f(n)=x;\ \text{例 }f(n)=n^2\Longrightarrow\{0,1,4,9,\dots\}\ \text{无限离散};\ \textbf{不是}\sin／\textbf{不是}\text{周期}／\textbf{不是}\text{超积}／\textbf{不是}\text{任意集合指定}／\textbf{不要求}\text{在 ℝ 内定义 }\mathbb N ⟹ \boxed{\mathrm I_{\rm sort}\ \text{形式上独立于 }(a)\text{–}(e)}\ ⟹ \textbf{表示定理第一种形式失败} ✓✓$$
$$\qquad\textbf{但 I-义务检验}：\text{须构造}\ f(n)=\gamma_n\ \textbf{而不把 }\gamma_n\ \text{放进 }f\ \text{的定义} ⟹ \boxed{\mathrm L\ \checkmark,\ \mathrm I\ \times}\ \text{—— }\textbf{离散排序解决 L，完全未解决 I}（双门筛子的第一个真正压力测试）;\ \textbf{且}\ \mathrm I_{\rm sort}\neq(d)\（f(n)=n^2\ \text{绝非任意集合编码}）✓$$
$$\textbf{转向}：\textbf{不再分类 L}，\textbf{直接以 I 为分类不变量}（否则重入循环：新语言}\to\text{能产生离散集}\to\text{不能识别 ζ}\to\text{再换语言）;\ \text{候选给出 }f:D\to\mathbb R,\ \Lambda=f(D)=Z_\zeta-\tfrac12 ⟹ \text{对每个 }x\in\mathbb R：x\in f(D)\iff\zeta(\tfrac12+ix)=0\ (\text{168.2});\ \text{这不再是"生成 }\lambda_n\text{"，而是}\textbf{定义域到实数的谓词等价问题};\ \text{更硬的问题：若 }f,D\ \text{都零点独立，则信息"为什么恰好是 ζ 的零点"从哪进入？}$$
$$\qquad\text{三种可能}：\text{I-A 信息已在 }D\ \text{或 }f\ \text{中（}D=\{\text{ζ 零点编号}\},\ f(n)=\gamma_n）⟹ \text{smuggling／DEAD};\ \text{I-B 信息在证明中出现（需 }\zeta,\xi,\zeta'/\zeta,L,\text{Mellin},\text{Hadamard},\text{EF}）⟹ C_{\rm analytic};\ \text{I-C 两者皆非} ⟹ \textbf{C6-BREAKTHROUGH}$$
$$\textbf{⭐ I-分类第一刀 ＝ bridge 结构（本档新增）}：\text{任何 (168.2) 的证明是"证明两集合相等"（}A=f(D),\ B=Z_\zeta-\tfrac12）⟹ \text{必须给出一个}\ \boxed{\textbf{bridge}}\；\text{bridge 来源只有四类}：\text{(i) 定义性联系 ⟹ I-A／smuggling};\ \text{(ii) ζ 的零点／解析定理（FE／RvM／Hadamard／EF／论证原理）⟹ I-B／}C_{\rm analytic};\ \text{(iii) 选择 ⟹ selection};\ \text{(iv) }\boxed{\text{ζ 的}\textbf{非零点刻画}}\ \text{＝ I-C 的}\textbf{唯一可能载体} ⟹ \text{而 }V157\ \text{#8 已判：唯一已知此类刻画（Selberg 类＋分类定理）其}\textbf{证明是解析的} ⟹ C_{\rm analytic} ⟹ \boxed{\text{I-C 载体唯一化 ＝ "ζ 的非零点刻画"}\ ＝\ V160\ \S5\ \text{残余}\ \textbf{同一点}} ✓✓✓$$
$$\textbf{⭐ 构造尝试（五个真实实例，本档新增）}：\text{盘点已存在的零点独立结构}：\text{①Robin 判据};\ \text{②Farey 序列（Franel–Landau 型渐近）};\ \text{③Lagarias 判据}\（\sigma(n)\le H_n+e^{H_n}\log H_n）;\ \text{④Nyman–Beurling}\（1_{(0,1)}\in\overline{\mathrm{span}}\{\{\alpha/x\}\}\）;\ \text{⑤Weil 正性}\（W(f)\ge0）⟹ \boxed{\text{五者全部零点独立、全部等价 RH、}\textbf{无一}\text{给出逐点零集}} ⟹ \text{＝ }V152\ \text{§3"RH-equivalence}\neq\text{spectral identity"在真实数学中的}\textbf{实例确认}\（也＝V165 T3 的守门证据）;\ ⭐\ \text{其中 ④（＝本项目 }A4\ \text{方向）最接近：若被"实现"，其闭包／收缩算子结构}\textbf{立即把路线推入算子类} ⟹ \mathrm C\text{-ii／}L1$$
$$\qquad ⚠️\ \text{边界}：\text{§5 的"bridge 只有四类"为 [结构性] 非穷尽性定理；§6 是已存在结构的盘点，非穷尽；本档}\textbf{不}\text{证明 I-分类定理} ✗$$
$$\qquad\textbf{下一步}：①\ \text{攻 I-分类定理}\（\text{是否可证：任何零点独立 }f:D\to\mathbb R\ \text{若 }f(D)=Z_\zeta-\tfrac12\ \text{则识别信息必经定义／选择／解析接口}）;\ ②\ \text{若不能证} ⟹ \textbf{必须马上尝试构造}\text{具体 }(D,f)\（\text{不得再抽象分类}）$$

### F.5ae ⭐⭐⭐⭐⭐ **直接构造 $(D,f)$：三个真实构造全部撞 I 门 ＋ 具体化不变性**（`V169` ✓ 2026-09-15 11:28）

$$\text{目标}：D\ \text{零点独立},\ f:D\to\mathbb R\ \text{零点独立},\ f(D)=Z_\zeta-\tfrac12;\ \text{非解析／非选择／非零点定义};\ \textbf{硬规则}：\textbf{不能}\ f(n)=\gamma_n\ \text{或等价改写}\（\operatorname{Im}\rho_n／\text{第 }n\ \text{个零点}\Rightarrow\textbf{直接 DEAD}）$$
$$\textbf{最强非解析离散对象}：D\ \text{不应是 }\mathbb N\（\text{单纯 }\mathbb N\ \text{递推只能生成我们自己规定的数列}），\text{而应取有限素数结构／模空间／图／组合对象},\ \text{并要求}\ \boxed{\text{递推具有}\textbf{不可人为调整的刚性}}\ \text{否则退化为 (d)}$$
$$\textbf{候选一（最小违约尺度）}：f(d)=\inf\{X:E_d(X)\le\varepsilon_d\}\ (\text{169.1}) —— \text{无 }\sin／\text{无周期}／\text{无超积}／\text{无任意指定}／\text{无零点输入},\ \text{纯离散算术数据}\to\mathbb R;\ \text{须}\ \boxed{E_{d_n}(X)\le\varepsilon_n\iff\zeta(\tfrac12+iX)=0}\ (\text{169.2}) \Longrightarrow \text{这已不是生成机制问题，而}\textbf{直接成为"ζ 零点的非解析刻画"}\ ⟹ \boxed{\text{DEAD：缺失 (169.2)}}\ \text{—— }\textbf{没有被抽象分类杀死，而是在实际公式层撞到 I 门}$$
$$\textbf{候选二（整数递推极限）}：a_{n,k+1}=F(a_{n,k}),\ f(n)=\lim_k a_{n,k}\ (\text{169.3});\ \text{须证}\lim_k a_{n,k}=\gamma_n\ (\text{169.4}),\ \text{而这仍须说明极限为何满足 }\zeta(\tfrac12+i f(n))=0 ⟹ \boxed{\text{DEAD：递推生成}\neq\zeta\text{-identification}};\ ⚠️\ \textbf{不是}"\text{极限属于 }V164\ \text{就结束"},\ \text{而是}\textbf{真正写出候选 }f\ \text{并证明其最后一步必承担逐点识别义务}$$
$$\textbf{候选三（组合谱，不用算子）}：G_1\subset G_2\subset\cdots,\ \text{纯组合递推 }R_n（\textbf{不能}\text{变自伴算子，否则进 }L1）,\ f(n)=\lim_k\tfrac{A(G_k,n)}{B(G_k,n)}\ (\text{169.5}),\ A,B\ \text{整数计数};\ \text{须证}\lim\tfrac{A}{B}=\gamma_n ⟹ \text{问题：}\textbf{为什么这个组合极限恰是 ζ 第 }n\ \text{个零点？}\ \text{无独立结构恒等式则推不出} ⟹ \boxed{\text{当前构造失败，但失败坐标已精确}}：\boxed{\text{组合结构}\to\text{实数}\ \checkmark}\ \text{而}\ \boxed{\text{实数}\to\zeta\ \text{零点}\ \times}$$
$$\textbf{⭐ 具体化不变性（本档新增）}：\text{三次}\textbf{独立}\text{具体化（最小尺度／递推极限／组合极限）全部卡在同一位置，且每一个把 I-义务写成}\textbf{同一个方程形态}\ \boxed{\text{（零点独立定义的量）}=0\iff\zeta(\tfrac12+i\lambda)=0}\ \text{（169.2 型）} ⟹ \boxed{\textbf{具体化不变性}：把 I-义务具体化，它}\textbf{不消失}，\text{而是}\textbf{每次变成同一个方程}}\ \text{—— 三点意义：(i)}\textbf{残余是一个对象而非一个族}\（\text{经验证据}）;\ \text{(ii) 解释为何二十轮收缩总回同一句（}V160\ \S5／V168\ \S5）;\ \text{(iii) 把下一刀}\textbf{唯一化}\text{为"找那个方程"};\ \text{⚠️ 基于三次尝试的}\textbf{[归纳性证据]},\ \textbf{非定理}$$
$$\qquad\textbf{状态与纪律}：\boxed{\text{3 个真实构造尝试：全部撞 I；C6 仍 OPEN}}\ ——\ \textbf{只证了这三个具体构造失败} ✗,\ \textbf{未证}\text{"所有 }(D,f)\ \text{都失败"} ⟹ \textbf{不得升级};\ ✓\ \text{本轮没有"再抽象一层"（三次都是写出公式然后在其上失败）}$$
$$\qquad\textbf{防循环硬规则（新增候选必须通过）}：\text{(1) 不得 }f(n)=\gamma_n\ \text{或等价改写};\ \text{(2) 必须写出显式公式};\ \text{(3) 必须指出失败位置的精确坐标};\ \text{(4) 不得以"属于 }V164/V165\text{"代替失败定位};\ \text{(5) 只能产生 RH-equivalence 而无逐点谱同一性者 ⟹ 标 I-撞门，不得称"闭合"}$$
$$\qquad\textbf{V170 预登记}：\text{攻击}\ \boxed{\textbf{组合对象之间的自然同构／互反关系}}\（\textbf{不是}\text{再做极限、极值、计数、递推）;\ \text{若也只能产生 RH-equivalence 而无逐点谱同一性} ⟹ \text{开始把}\ \boxed{\text{"arithmetic relation}\to\text{pointwise spectral identity"}}\ \text{作为}\textbf{具体可证的障碍}\text{处理}$$

### F.5af ⭐⭐⭐⭐⭐ **Arithmetic relation → pointwise identity（R1–R4 ＋ 三互反实例 ＋ 两正交轴）**（`V170` ✓ 2026-09-15 11:30）

$$\text{规格}：A,B\ \text{零点独立},\ R\subseteq A\times B,\ \text{自然双射}\ \Phi:A\xrightarrow{\sim}B,\ f:A\to\mathbb R,\ g:B\to\mathbb R,\ f(a)=g(\Phi(a))\ (\text{170.1}),\ \text{终求}\ f(A)=Z_\zeta-\tfrac12\ (\text{170.2});\ \textbf{关键}：\textbf{(170.1) 只证两独立结构的对应，不自动证明它们对应 ζ};\ ⭐\ \textbf{新增硬规则}：\boxed{\text{关系本身必须独立于 }Z_\zeta,\ \text{同构必须逐点产生 }\lambda}$$
$$\textbf{R1–R4}：\text{R1 存在}\（\forall a\exists b\ R）\ \text{只给 }A\to B\ \text{无唯一对应} ⟹ \mathrm I\ \text{信息不足};\ \text{R2 唯一自然对应}\（\forall a\exists!b）⟹ \text{得自然函数}\ \Phi(a)=b,\ \text{但最终仍只有 }f(a)=g(\Phi(a))\ ⟹ \boxed{\text{RELATION}\to\text{IDENTIFICATION}\ \times};\ \text{R3 互反}\（R^{-1}\circ R=1_A,\ R\circ R^{-1}=1_B）⟹ \text{确实得自然同构},\ \text{但仍只是 }A\cong B ⟹ \boxed{A\cong B\not\Rightarrow A\cong Z_\zeta-\tfrac12};\ \text{R4 须第三零点独立对象}\ \mathfrak Z\ \text{与}\ A\xrightarrow{\Phi}\cong\mathfrak Z\xrightarrow{\Psi}\cong B\ \text{＋独立结构定理}\ \boxed{\mathfrak Z\cong Z_\zeta-\tfrac12}\ (\text{170.3})\ ——\ ⚠️\ \textbf{(170.3) 正是我们一直缺的东西} ⟹ \text{自然同构}\textbf{没有}\text{消除 I 门，而是把 I 门变成"为什么这个自然对象恰好是 ζ？"}$$
$$\textbf{三个具体互反实例}：\text{①加法—乘法互反}\（(A,+),(B,\times),\ \text{素因子分解／Dirichlet 卷积}）⟹ \text{最终产生 divisor data}\leftrightarrow\text{prime data}\ \textbf{而非}\ \gamma_n;\ \text{若送入 Fourier／Mellin／L-函数} ⟹ C_{\rm analytic} ⟹ R_{+\times}:\mathrm I\times;\ \text{②Farey}\leftrightarrow\text{divisor／连分数对偶}\（\text{自然参数 }q,a/q,\mu(n),\varphi(n)）⟹ \text{只得 arithmetic}\leftrightarrow\text{arithmetic},\ \text{仍缺 arithmetic}\to\gamma_n ⟹ R_{\rm Farey}:\mathrm I\times;\ \text{③Möbius}\leftrightarrow\text{显式谱侧（最危险）}⟹ \text{一旦谱侧真等于 ζ 零点就出现}\ \sum_n\Lambda(n)F(n)\leftrightarrow\sum_\rho\widehat F(\rho)\ ⟹ \text{这}\textbf{已经正是显式公式型桥梁} ⟹ \boxed{R_{\rm arithmetic\leftrightarrow spectral}\Rightarrow C_{\rm analytic}}\ \text{不是新 C6}$$
$$\qquad\Longrightarrow\ \text{硬结论}：\text{三种自然互反全部呈现}\ \boxed{A\leftrightarrow B\Longrightarrow A\cong B}\ \text{而 C6 要}\ \boxed{A\cong Z_\zeta-\tfrac12};\ \text{中间始终缺}\ \boxed{\text{natural relation}\longrightarrow\zeta\text{-specific pointwise identity}}\ (\text{170.4}) ⟹ \boxed{\textbf{自然同构可以消除 selection，但不能消除 identification}}$$
$$\textbf{⭐ 两正交轴（本档新增）}：\Phi:A\xrightarrow{\sim}B\ \text{拆为}\ \boxed{\textbf{canonicity}}（\text{由结构自身确定、无选择自由} ⟹ \text{消除 selection}，\text{处理多重性}）\ \text{与}\ \boxed{\textbf{reference}}（\text{指向特定外部对象（ζ 零集）} ⟹ \text{处理 identification}，\text{处理指称}） ⟹ ⭐\ \textbf{两轴正交}：内蕴同构}\ \Phi:A\to B\ \text{自动是 canonical，但关于 ζ 零参照} ⟹ \text{这解释了为何二十余轮"canonical 构造"从未触及残余：canonically 构造出的对象自动无参照，要加参照必须外部输入（解析桥或走私）} ⟹ \text{残余的正确定形：需要在"零点独立可构造对象"类内对目标的}\ \boxed{\text{刚性（rigidity）刻画}}\ \text{而非又一个 canonical 构造}$$
$$\textbf{⭐ 具体化不变性实例 3→6}：V169\ \text{三构造}＋\text{本档三关系} ⟹ \text{6 个独立实例全部卡在同一方程形态}\ \boxed{\text{（零点独立定义的量）}=0\iff\zeta(\tfrac12+i\lambda)=0}\（\text{归纳性证据，}\textbf{非定理}）$$
$$\textbf{⭐ 残余回到 §E.2 原话}：\text{由两正交轴，残余 ＝ 需要目标的}\ \boxed{\textbf{表征定理／刚性定理}};\ \text{而档案 §E.2}\ \textbf{逐字}\text{就是这一句}\ \boxed{\text{"能真正缩小范围的只有一类东西：表征定理"}} ⟹ \text{二十余轮之后回到 §E.2 原话，但已将其}\textbf{具体化}\text{为"ζ 零集的刚性刻画"}$$
$$\qquad\textbf{状态}：\boxed{\text{3 类具体互反关系：I-门全部未通过；C6 OPEN}}（\text{只证这三类不够，}\textbf{未}\text{证所有关系不够} ⟹ \text{不得升级}）$$
$$\qquad\textbf{V171 预登记}：\text{不能再找第四种"关系"；应}\textbf{直接攻击 (170.4)}：\boxed{\textbf{构造一个零点独立的算术对象}\ \mathfrak Z\ \text{并尝试证明}\ \mathfrak Z\cong Z_\zeta-\tfrac12};\ \text{若连这个最直接的对象构造都必须把 ζ 放回定义或解析接口} ⟹ \text{才真正接近}\ \textbf{条件性封口}$$

### F.5ag ⭐⭐⭐⭐⭐ **reference／rigidity 直接攻击 —— Selberg 类 ＋ Kaczorowski–Perelli 与 ⭐⭐ A $\perp$ D 互斥二分**（`V171` ✓ 2026-09-15 11:36）

$$\text{硬目标}：\boxed{\mathfrak Z\ \text{完全不使用 }\zeta,\rho,\gamma\ \text{且}\ \mathfrak Z\cong Z_\zeta-\tfrac12}；\ \text{四门}：\text{A 构造独立性}\（\text{禁 }\zeta,\xi,\rho,\gamma_n,\zeta'/\zeta,L(s),\text{零点计数}）;\ \text{B 对象强度}\（\textbf{不能}\text{只要 }N_{\mathfrak Z}=N_\zeta\ \text{或渐近；必须点集级}\ \Phi:\operatorname{Pts}(\mathfrak Z)\to\mathbb R\ \text{且}\ \Phi(\operatorname{Pts})=\{\gamma\}）;\ \text{C ζ-reference 不得藏在证明里};\ \text{D 刚性须排除同型不同对象}\（\text{若两非同构模型满足全部零点独立公理但点集不同则刚性失败}）$$
$$\textbf{⭐ 最强候选}：\text{Selberg 类公理}\（(i)\ \text{Dirichlet 级数};\ (ii)\ \textbf{Euler 积};\ (iii)\ \text{Ramanujan};\ (iv)\ \boxed{\Lambda(s)=\omega Q^s\prod\Gamma(\lambda_is+\mu_i)F(s)}\ \text{且}\ \Lambda(s)=\overline{\Lambda(1-\bar s)};\ (v)\ \text{解析延拓}）＋\ \text{Kaczorowski–Perelli 分类（经典：degree 1}\Longrightarrow\text{Dirichlet }L;\ \text{conductor 1}\Longrightarrow\zeta）⟹ \text{形状}\textbf{完全符合}\ \text{公理}\Longrightarrow\exists!\mathfrak Z\Longrightarrow\operatorname{Spec}(\mathfrak Z)=Z_\zeta-\tfrac12\ \text{（真实数学实例）}$$
$$\textbf{逐门审计}：\textbf{A ✗}\（\textbf{精确定位}：\text{公理 (iv) 出现}\ \boxed{\Gamma(\lambda_is+\mu_i)}\ \text{与}\ Q^s\ ＝\ \textbf{archimedean／完形化数据} ⟹ \text{公理系统}\textbf{不是}\text{零点独立}）;\ \textbf{B ✗}\（\text{公理刻画的是}\textbf{函数}\text{而非带 }\operatorname{Spec}\ \text{的对象；}\text{公理}\to\text{函数}\to\text{零点}\text{重新引入读零点 ⟹ 正是 I 门};\ \text{若改在"谱对象"类找刚性}\ ⟹\ \text{即 }Hilbert\text{–}P\acute olya\ \text{问题，}\textbf{无候选}）;\ \textbf{C ✗}\（\text{K-P 分类证明用解析工具（FE／Rankin–Selberg／Hecke–Tate）}\ ⟹ C_{\rm analytic}\ \text{，与 }V157\ \text{#8 一致}）;\ \textbf{D ⭐ 唯一性成立}\（\text{degree 1 ＋ conductor 1}\Longrightarrow\zeta\ \text{唯一}）但}\text{判别参数 (degree, conductor) 由函数方程的 archimedean 因子定义}\（\text{degree}=\sum2\lambda_i;\ \text{conductor 含 }Q,\mu_i）⟹ \text{回到 A 失败点};\ ⭐\ \text{第二子测：剔除 archimedean ⟹ 只剩级数＋Euler 积＋Ramanujan ⟹ 被}\textbf{无穷多对象}\text{满足（}\zeta,\text{Dirichlet }L,\text{Dedekind }\zeta,\text{自守 }L）⟹ \textbf{唯一性立刻崩塌}$$
$$\textbf{⭐⭐ 核心：A}\perp\textbf{D 互斥二分（本档新增）}：\boxed{\text{要 D 通过（唯一性）}\Longrightarrow\text{必须引入 archimedean}\Longrightarrow\text{A 失败}}\ \text{与}\ \boxed{\text{要保持 A 通过（零点独立）}\Longrightarrow\text{只剩 Euler 积＋级数公理}\Longrightarrow\text{唯一性崩塌}\Longrightarrow\text{D 失败}}\ \Longrightarrow\ \boxed{\textbf{A 与 D 不可同时通过}}\ \text{—— }\textbf{不是}"\text{又收窄一层"}\text{，而是}\textbf{类封口式二分}：\text{唯一性的}\textbf{来源}\text{与构造的}\textbf{独立性}\text{不可兼得}$$
$$\textbf{与 }V144\ \text{层诊断完全一致}：\text{零点与 RH 在 Archimedean 层} ⟹ \text{任何}\textbf{钉住零点}\text{的公理系统必然含 archimedean 数据} ⟹ \text{失败点必落}\ \boxed{\text{公理 (iv)}};\ \text{与 }V160\ \text{§5 残余的关系：V160 问"是否存在非解析 ζ-结构刻画"，V171}\textbf{把该问句定位到一个具体公理}⟹ \text{残余不再是"某处"而是"}\textbf{这一步}\text{"};\ ⚠️\ D1\ \text{教训：Epstein }\zeta\ \text{有 FE 却有离轴零点} ⟹ \text{FE 单独}\textbf{不足以}\text{钉住 ζ，钉住 ζ 的是}\textbf{Euler 积 ＋ FE 的联合}，\text{而 FE 正是 archimedean 入口}$$
$$\qquad ⚠️\ \text{边界}：\text{A}\perp\text{D 依赖 Selberg 类这一具体体系；"剔除 archimedean 唯一性崩塌"为实例观察，非穷尽性定理；本档}\textbf{不}\text{证明"不存在其他刚性体系"} ⟹ \text{条件性结论，但}\textbf{首次带精确坐标}$$
$$\qquad\textbf{下一步}：①\ \text{攻 A}\perp\text{D}\ \text{能否}\textbf{升为定理}（\text{把"唯一性必来自 archimedean"形式化）——\ \text{最接近封口的一刀};\ ②\ \text{审是否存在}\textbf{第七种体系}（\text{不用 Selberg 框架而用其它刚性来源}）$$

### F.5ah ⭐⭐⭐⭐⭐ **Rigidity Source Separation（F／A／S 三分）＋ `V171` (★) 撤回**（`V172` ✓ 2026-09-15 11:38）

$$\textbf{反例（击穿 }V171\ \text{(★)}）}：F(s)=\sum a_nn^{-s},\ a_1=1,\ a_{mn}=a_ma_n\ ((m,n)=1),\ \boxed{a_{p^k}=1}\ (k\ge1) \Longrightarrow a_n=1\ \forall n \Longrightarrow F=\zeta\ ——\ \text{完全不用}\ \Gamma,Q,\text{degree},\text{conductor},\ \textbf{甚至不用 Archimedean place} ⟹ \boxed{\text{finite-place rigidity}\not\Rightarrow\text{Archimedean rigidity}};\ \text{但该反例不能救 C6（它把 ζ 的 Euler local factors 写进去了）} ⟹ \text{死于}\ \boxed{\text{reference／identity smuggling}}\ \text{而非 A}$$
$$\textbf{教训（纪律级）}：\boxed{\text{不要把某一个框架的分类定理，误当成所有数学机制的分类定理}} ——\ \text{即使证 }D\Rightarrow A\ \text{也只得"在某形式化 Selberg-like 公理宇宙里"的结论，而 C6 需要}\ \boxed{\text{所有可能的零点独立刚性体系}}\ \text{（已是表示定理／元定理）}$$
$$\textbf{D 的拆分}：D_1\ \text{对象唯一性}\（\exists!M\,P(M)）;\ D_2\ \text{非平凡唯一性}\（P\cap\{\zeta\text{-specific local data}\}=\varnothing）;\ D_3\ \text{谱唯一性}\（\operatorname{Spec}(M)\ \text{内部产生，而非}:=Z_\zeta-\tfrac12）⟹ \boxed{\text{真 C6 要求 }D_1+D_2+D_3}$$
$$\textbf{F／A／S 三分}：\text{F 有限场唯一性（通过局部 Euler 数据钉住 ζ）}=\text{reference smuggling};\ \text{A Archimedean 唯一性（FE／degree／conductor）}=C_{\rm analytic};\ \boxed{S\ \text{真正新刚性（既不用 ζ-specific local data，也不用 Archimedean 数据）}=\text{真正的 C6 突破口}} ⟹ \text{目标改写：}\boxed{D_{\rm nontrivial}\Longrightarrow F\cup A\cup S};\ \text{S 六条要求（不用 Archimedean completion／不写 ζ local Euler factors／不用 zero set／不用 }L\text{-分类／却唯一产生 }M_\zeta／\operatorname{Spec}(M_\zeta)=Z_\zeta-\tfrac12）⟹ M\ \text{须具}\ \boxed{\text{自认证性（self-identifying rigidity）}}$$
$$\textbf{⭐ A-leak 扩张（本档新增）}：\text{一切关于 ℂ 上}\textbf{增长／全纯性／阶数／垂直带条件}\text{的公理都是 archimedean 层的（因 ℂ 上的 }|\cdot|\ \text{就是 archimedean 赋值）} ⟹ \boxed{\text{A-leak}\supseteq\{FE,\Gamma,Q,\text{degree},\text{conductor}\}\cup\{\text{增长／阶／全纯性／垂直带}\}}$$
$$\textbf{⭐ 局部灵活性论证（本档新增）}：\text{带 Euler 积的 Dirichlet 级数由其局部因子族}\ \{L_p\}\ \textbf{完全决定}；\ \text{而结构性公理（乘性、}a_1=1\text{、Euler 积存在、Ramanujan、有界性、甚至解析延拓）只约束局部因子的}\ \boxed{\text{形状}}\ \textbf{不约束其}\ \boxed{\text{值}} ⟹ \text{局部因子仍自由} ⟹ \textbf{结构性公理不可能是唯一性陈述} ⟹ \boxed{\text{uniqueness}\Longrightarrow\text{F-leak}\lor\text{某全局约束}};\ \text{而已知全局约束来源 ＝ FE（A-leak）或增长（}5a⟹\text{A-leak）} ⟹ \boxed{D_{\rm nontrivial}\Longrightarrow\text{F-leak}\lor\text{A-leak}}\ \text{的 [结构性] 论证，}\textbf{唯一缺口＝是否存在第三种全局约束}$$
$$\textbf{⭐ S 的两条障碍（本档新增）}：(6a)\ \text{结构唯一算术对象的本蕴谱是 prime-like 而非 zero-like}（\mathbb Z,\operatorname{Spec}\mathbb Z,\mathbb Q\ \text{的规范谱＝素数集／赋值集}）;\ (6b)\ \zeta\ \text{自身的平凡性阻塞 finite}\to\text{archimedean 内生转移}：\text{算术对象内蕴谱由局部 Frobenius 数据给出，而}\ \alpha_p\equiv1\（V144）⟹ \text{有限场不携带相位通道} ⟹ \text{无法内生 Archimedean 层零点位置} ⟹ \boxed{\text{ζ 的特殊性恰好使"结构唯一性"不可能来自有限场}} ⟹ \text{F ＝ 有限场唯一路径（smuggling）；A ＝ 唯一结构路径（}C_{\rm analytic}）；\ \text{S 需 finite}\to\text{archimedean 内生转移，而 ζ 自身平凡性阻塞它}$$
$$\qquad\textbf{V172 目标形式（Rigidity Source Separation）}：\text{定义允许的 ζ-independent axiom }P(M)；\ \textbf{精确禁止} F-leak（P 含 ζ 有限场 Euler 指纹）与 A-leak（P 含 Archimedean completion，含增长／全纯性）;\ \text{问}\ \boxed{P(M)\ \text{仍能否唯一确定 }M？};\ \text{若 NO 且可证"任何剩余唯一性信息}\Longrightarrow\text{F-leak}\lor\text{A-leak}" ⟹ \boxed{\text{nontrivial rigidity}\Longrightarrow\text{finite-place }\zeta\ \text{fingerprint}\lor\text{Archimedean analytic structure}}$$
$$\qquad\textbf{指导意义}：\text{若"非指纹、非 Archimedean 的刚性"也能被}\textbf{形式化排除} ⟹ \text{第一次接近类封口};\ \text{若排不掉} ⟹ \text{可能第一次得到}\textbf{真正未被前十几类 NO-GO 覆盖的突破口}$$
$$\qquad\textbf{下一步（V173 预登记）}：①\ \text{把局部灵活性论证}\textbf{形式化}（\text{S 排除的关键第一步，}\textbf{不依赖 Selberg 框架}）;\ ②\ \text{审是否存在第三种全局约束（既非 FE 亦非增长）}$$

### F.5ai ⭐⭐⭐⭐⭐ **Euler-local flexibility theorem（有适用域）＋ 全局耦合审计链＋⭐ 耦合≠选择**（`V173` ✓ 2026-09-15 11:41）

降级（唐先生）：标题＝ **Euler-local flexibility theorem**（**有明确适用域**），**不**写成"任意体系的框架无关元定理"；理由：若公理体系不要求 Euler factorization，"局部因子自由"连适用对象都没有。**纪律（新增）：不得把"很强但有明确适用域"的定理过早升级成全数学空间的 NO-GO。**

**引理 1**：$F(s)=\sum a_nn^{-s}=\prod_pF_p(p^{-s})$，全部有限场信息由局部因子族 $\{F_p\}_p$ 决定。若公理 $P$ 只施加**逐素数独立局部约束** $F_p\in\mathcal C_p$ ＋有限个统一增长／系数条件、**无跨素数全局约束**，则

$$P\ \text{一般不能唯一确定}\ F$$

证明：取素数 $q_1$、$\mathcal C_{q_1}$ 中 $F_{q_1}\neq G_{q_1}$，其余 $F_p=G_p$ ⟹ $F\neq G$，但不涉及 $q_1$ 的局部公理全同 ⟹ 局部独立约束 ⇏ 全局唯一性。

**local-swap 对称形式**：若公理集在**单点替换**下不变（任一素数允许类内替换仍成立），则任何模型都不唯一 ⟹

$$\text{唯一性}\iff\text{存在破坏单点替换对称性的跨素数约束}$$

⚠️ 适用条件：(i) $\mathcal C_q$ 非退化；(ii) **无**跨素数耦合；⚠️ 技术缺口：替换若破坏收敛／解析性质，出错的是**全局条件（A-leak）**。

**审计链**：Local flexibility ⟹ global coupling necessary ⟹ classify global couplings ⟹ {F-leak, A-leak, S residual}；⚠️ **纪律：若最后剩下一个真正的第三类 global coupling，这一次不要继续杀它。**

**十项全局约束审计**：①Hecke／系数递推 ＝ **同一素数内** ⟹ 仍局部；②⭐ **SMO** ＝ **真跨素数刚性且纯算术（不落 A）**，但把唯一性归约到局部数据的唯一性 ⟹ 仍需 F-leak；③Rankin–Selberg ⟹ A-side；④**无 $\Gamma$ 版 FE** ⟹ 跨素数，但经典 **Hamburger 定理（1921）**（$a_1=1$ ＋与 ζ 相同的函数方程 ⟹ $F=\zeta$）**用的正是 ζ 的 $\Gamma$-因子** ⟹ A-leak；"无 $\Gamma$ 版"是否存在 ⟹ **OPEN**；⑤positivity（$W(f)\ge0$）⟹ A-side；⑥automorphic axioms ⟹ A-side；⑦⭐ **Galois compatibility** ＝ **真跨素数耦合且纯算术**，但**不唯一选出 ζ**（无穷多 Galois 表示／Dirichlet 特征）⟹ 选择仍需 archimedean；⑧Artin 互反 ⑨局部-整体原则 ⑩"无限素数统一参数"（＝⑥⑦⑧ 的抽象形式）⟹ 同上。

⟹ **表结论**：跨素数耦合**确实存在，而且可以是纯算术的**（#2/#7/#8/#9/#10）⟹ **不落 A-leak**；但**都不能完成"选出 ζ"**；选择步骤在所有已知机制里退化为 F-leak（局部数据平凡性）或 A-leak（degree／conductor／$\Gamma$／FE）。

**⭐⭐ 本档核心：耦合 ≠ 选择。** 耦合 ＝ 把无限多个局部因子绑在一个对象上（**可纯算术**）；选择 ＝ 从众多对象中挑出 ζ（**不可纯算术**）。两条已知选择路径：**选择-A**（archimedean 选择器；经典实例 Hamburger 1921，**早于 Selberg 框架** ⟹ A 路线不依赖 Selberg 类）与 **选择-F**（局部数据平凡 $a_{p^k}=1\Rightarrow a_n=1$ ⟹ F-leak）。与 `V172` (6b) 衔接：$\alpha_p\equiv1$ ⟹ 选择不能来自局部数据的"内容"，只能来自"平凡性"本身（F）或 archimedean 选择器（A）。

**S 残余精确化**：S 须同时提供 **纯算术耦合（不落 A）＋ 纯算术选择（不落 F、不落 A）**。形式化目标：

$$\exists\ \text{纯算术跨素数耦合}\quad\text{s.t.}\quad \text{唯一选出}\ M_\zeta\ \text{且}\ \operatorname{Spec}(M_\zeta)=Z_\zeta-\tfrac12$$

⚠️ 边界：引理 1 有明确适用域（Euler–Dirichlet 型 ＋ 无跨素数耦合）；十项为**盘点**非穷尽；#4 标 **OPEN**；**不**声称"所有耦合都落 F／A"；**不**声称 S 已被排除（**S 仍 OPEN**）。

**下一步（V174 预登记）**：① 攻 #4 OPEN（无 $\Gamma$ 版 FE 唯一性）② 形式化「选择步骤 ⟹ F-leak ∨ A-leak」的条件性定理。

### F.5aj ⭐⭐⭐⭐⭐ **无 $\Gamma$ 版跨素数函数方程审计 —— 反射可内生、轴不可内生；形式级可算术、函数级必 archimedean**（`V174` ✓ 2026-09-15 11:46）

**硬定义（防伪 S）**：允许 $F(s)=\sum a_nn^{-s}=\prod_pF_p(p^{-s})$ 与纯算术跨素数关系 $\mathcal C(\{F_p\})=0$；**禁止任何等价 Archimedean 载体**：$\Gamma$、$Q^s$、$|\cdot|_\infty$、order／growth、vertical-strip bounds，以及用 Fourier／Mellin／Poisson 把上述数据**重新编码**。要求存在 $F(s)=\varepsilon\,\mathcal T(F)(1-s)$，$\mathcal T$ 须由有限素数／算术数据**内部**定义。

**三型区分**：**类型 A**（$\mathcal T=\mathcal T_{\rm arith}$ 完全由 Euler／系数／Galois／Hecke 构造）＝唯一 S 候选；**类型 B**（$\Gamma$ 被消去但信息仍在，如 $F(s)F(1-s)=H(s)$ 而 $H$ 携带增长／零点对称／无限位信息）＝**A-leak disguised**；**类型 C**（形式 $s\mapsto1-s$ 而无内生 involution）＝**公理写入**，无内容。

**⭐ 本档核心（一）：反射可内生，轴不可内生。**
观察 1：反射 $F(s)\mapsto F(k-s)$ 在**系数侧完全可实现** —— 只需两项系数侧操作：**算术平移** $T_k$（系数按 $n^{-k}$ 重标，$(T_kF)(s)=F(s+k)$）与**算术镜像** $R$（$RG(s):=G(-s)$，即指数符号翻转），于是 $R(T_kF)(s)=F(k-s)$。⟹ **反射不是 archimedean 独占的（正面发现，不得杀掉）**。
观察 2：但**平移量 $k$ 不唯一**（任意 $k\in\mathbb Z$ 甚至 $k\in\mathbb Q$ 都写得出来），固定点为 $k/2$；有限场数据（只给系数序列 $\{a_n\}$）对 $k$ 的任何取值都同样"配合" ⟹ **有限场数据不能规范选出 $k=1$** ⟺ **反射轴（中心 $k/2$）不被有限场数据确定**。**这就是"1 从哪里来"的直接回答：不从有限场数据来。**
观察 3：选 $k$ 需额外输入 —— **路径 F**（ζ 系数全为 1／ζ 是 Dirichlet 卷积的单位 ⟹ F-leak）或 **路径 A**（$\Gamma$ 与 $Q$ 钉住临界带宽 ⟹ A-leak）。

$$\boxed{\text{finite places can couple local data}\ \not\Rightarrow\ \text{finite places can}\ \textbf{locate the critical axis}}$$

**⭐ 本档核心（二）：形式级可算术，函数级必 archimedean。**
即使把 $k$ 供给出来，要把 $F(s)=\varepsilon F(k-s)$ 当作**复变量函数**的恒等式，就需要：① 带状域内两侧都有定义；② 解析延拓；③ 带状域上的增长控制 —— **三项全部 archimedean**（参 `V172` §5a 的 A-leak 扩张）。⟹ **形式 Dirichlet 级数层面反射可纯算术；复变量函数层面必引入 archimedean。** 这也给出**类型 B 的机制解释**：消去 $\Gamma$-因子并不消去**解析结构**（带状域存在／宽度／奇点位置／增长型仍携带 archimedean 信息）。⟹ **#4 之所以看似突破口却总落空：能给出零点／谱的必须是函数级对象，而函数级已经含 archimedean。**

**第二关（FE ≠ 选择器）**：$F\mapsto F\cdot F_0$ 可能保留对称结构 ⟹ 成功标准不是"发现无 $\Gamma$ FE"，而是"纯算术公理 ⟹ $\exists!F$ 且 $F=\zeta$"。**⭐ 第二实例**：**素性（primitive）纯算术** ✓，但把素性升级为**唯一选择器**仍需 **degree／conductor**（archimedean，`V171` §3-D）⟹ 与 SMO 同型（`V173`）的第二例。

**终止条件三选**：S-HIT（未达）／A-CLOSURE（**仅部分**：函数级确实必 archimedean，但形式级反射确实纯算术）／**OPEN（本档落此）** ⟹ 判定 ＝ **OPEN（半算术半 archimedean）**；按纪律**不强行杀掉**。

**下一步（V175 预登记）**：① 轴定位是否是**唯一的** archimedean 入口？（若是 ⟹ A-leak 可精确化为"轴定位输入"型）② 允许 $k\in\mathbb Q$ 后是否存在纯算术方式选出 $k=1$？③ 审"函数级"能否被"形式级＋有限组合"替代（若不可 ⟹ 层级二分可升为定理）

### F.5ak ⭐⭐⭐⭐⭐ **层级定理（局部因子刚性）：逐素数可分的"无 $\Gamma$"反射在 Euler 积类中只有平凡解**（`V175` ✓ 2026-09-15 11:49）

**目标（唐先生钉死）**：Prove or refute: finite arithmetic formal calculus $\not\Rightarrow$ cross-domain analytic reflection。

**三层分离**：形式对象 $\mathcal F=(a_n)$ —（有限次 $+$、$\times$、Dirichlet convolution、index rescaling、$T_k$、$R$）→ 形式级 $\mathcal G$；**函数级** $G(s)=\sum b_nn^{-s}$ 额外要求存在非空复域 $D$ 使 $G:D\to\mathbb C$ 解析且 $G(s)=\varepsilon G(k-s)$ 在 $D\cap(k-D)$ 成立。

**第一刀**：系数代数**不自动产生另一个解析域**（$\Re s>\sigma_0$ 经 $s\mapsto k-s$ 变为 $\Re s<k-\sigma_0$，两域仅特殊情况相交；连接它们**已不是系数有限组合**）。
**第二刀（纠错）**：**不能说"解析延拓 $=\Gamma$"**（不对，存在许多无显式 $\Gamma$ 的延拓机制）；真正缺的是 **boundary-to-boundary analytic identification**（跨域连接信息）；$\Gamma$ 只是经典实现之一。
**第三刀（恒等定理的正确用法）**：同一连通开域上一致 ⟹ 恒等定理 ⟹ 延拓唯一。**真正的问题不是"延拓是否唯一"，而是"从形式数据能否证明存在覆盖两侧的共同解析域"** ⟹ 目标变为存在性障碍：$\mathscr A(F)=\{$ 含初始收敛域的解析延拓 $\}$，$\#\mathscr A(F)\le1$，要证 **有限形式运算 $\not\Rightarrow$ $\mathscr A(F)\neq\varnothing$ 跨越反射轴**。

**⭐⭐ 局部因子刚性定理（本档新增，初等三行）**：设 $F(s)=\prod_pF_p(p^{-s})$，$F_p\in\mathbb C[[X]]$、$F_p(0)=1$，记 $X_p=p^{-s}$。方程 $F(s)=\varepsilon F(k-s)$ 逐素数展开为 $\prod_pF_p(X_p)=\varepsilon\prod_pF_p(p^{-k}X_p^{-1})$。
**(i)** 右端第 $p$ 因子只依赖 $X_p$ ⟹ 在 $\prod_p\mathbb C((X_p))$ 中逐分量比较得 $F_p(X)=\lambda_pF_p(p^{-k}X^{-1})$，$\prod_p\lambda_p=\varepsilon$。
**(ii)** 幂次支撑冲突：$F_p(X)$ 支撑 $\subseteq\mathbb Z_{\ge0}$；$F_p(p^{-k}X^{-1})$ 支撑 $\subseteq\mathbb Z_{\le0}$。
**(iii)** 相等 ⟹ 支撑 $\subseteq\{0\}$ ⟹ $F_p$ 常数；归一化 $F_p(0)=1$ ⟹ $F_p\equiv1\ \forall p$ ⟹ $F\equiv1$（**平凡对象，零谱为空**）。
⟹ $$\boxed{\text{逐素数可分的"无 }\Gamma\text{"反射在 Euler 积类中}\textbf{只有平凡解}}$$ ⚠️ 唯一假设＝**逐素数可分** ＋ 非退化归一化；**不需要任何解析延拓／增长／带状域论证**（障碍在**局部因子层**）。

**推论 1**：非平凡反射恒等式在 Euler 积类中**必然需要 archimedean 平衡项** ⟹ **`V174` 二分由经验观察升级为定理**（与"所有已知函数方程都带 $\Gamma$-因子"一致）。
**推论 2（更强）**：定理**不依赖 $\Gamma$ 的具体表达式**；它说明的是**局部参数倒置 $X_p\leftrightarrow X_p^{-1}$ 的幂次失配必须由某个"局部↔全局"平衡结构吸收**，$\Gamma$ 只是经典实现。
**推论 3（机制解释）**：`V174` 类型 B（$\Gamma$ 被消去但信息仍在）＝ **消去 $\Gamma$ 后若不引入"混合素数"结构，方程退化到只有平凡解**；一旦引入混合，archimedean 信息随该混合回流 ⟹ A-leak disguised。

**⭐ S 残余精确化（不杀）**：定理只覆盖逐素数可分反射 ⟹ S 切成两支：**S-i**（无 Euler 积的 Dirichlet 级数，经典属 Koshlyakov／Potter–Titchmarsh 型范围，**OPEN**）与 **S-ii**（**非逐素数可分的跨素数 involution**，本档新隔离的**主残余**）：须满足"**混合素数的对合 ＋ 纯算术构造 ＋ 唯一选出 ζ**"三者齐备（与 `V173` "耦合≠选择"直接衔接）。

**STOP 条件（唐先生）**：若找不到真反例／定理而只能说"通常需要解析延拓"，则只能 OPEN，不能封口；**不得**把"所有已知构造都需要解析延拓"升级为"任何可能构造都需要"。**本档定位**：给出的**不是**经验说法而是**初等定理**，其结论**弱于**"所有构造都需要"、**强于**"已知构造需要" ⟹ 满足 STOP 条件且未过度推广。

**下一步（V176 预登记）**：① 攻 **S-ii**（构造非逐素数可分的对合）② 攻 **S-i**（查无 Euler 积情形的经典结果）

### F.5al ⭐⭐⭐⭐⭐ **跨素数混合对合审计：锥定理 ＋ 加强定理 ＋ 平衡因子定理**（`V176` ✓ 2026-09-15 11:52）

**形式化**：$F(\mathbf X)=\sum_{\alpha\in\mathbb N^{(\mathcal P)}}c_\alpha\mathbf X^\alpha$（**不要求**逐素数可分）；单项式型跨素数对合 $\iota(\mathbf X)_p=c_p\prod_qX_q^{A_{pq}}$，$A^2=I$；模拟 $s\mapsto k-s$ 需含负方向，最直接 $A=-P$。

**① 锥定理（单项式，唐先生）**：$A\in GL(C)$ 整数、$A^2=I$、$A(C)=C$ ⟹ $A$ 矩阵元非负；$A^{-1}=A$ 亦非负；$AA^{-1}=I$ 要求非对角元严格抵消，而**两个非负整数矩阵不能通过正数相加产生零** ⟹ 每行每列恰一个 $1$ ⟹ $\boxed{A=P\ \text{（素置换）}}$ ⟹ **保持 Euler 正锥的单项式对合 ＝ 素数置换，无反演**（无法实现 $X_p\mapsto p^{-k}X_p^{-1}$）。二分：**S-ii(a)** 保持正锥 ⟹ 纯置换 ⟹ 死；**S-ii(b)** 真反演 ⟹ $A(C)\not\subseteq C$ ⟹ 锥冲突 ⟹ 交集平凡 ⟹ 回 `V175` 的 $F=1$。

**⭐ ② 加强定理（本档新增，严格强于 `V175`）**：设 $F(s)=\sum_{n\ge1}c_nn^{-s}$ 为**任一** Dirichlet 级数（**不假设** Euler 积、**不假设**逐素数可分）。若 $F(s)=\varepsilon F(k-s)$ 成立，则 $c_n=0\ (n>1)$，即 $F\equiv c_1$（常函数，零谱为空）。**证明（三行）**：$n^{-s}=\mathbf X^{\alpha(n)}$ ⟹ $F$ 支撑 $\subseteq C=\mathbb N^{(\mathcal P)}$；$n^{s-k}=n^{-k}\mathbf X^{-\alpha(n)}$ ⟹ $F(k-s)$ 支撑 $\subseteq -C$；而 $C\cap(-C)=\{0\}$ ⟹ 逐系数比较 ⟹ $c_\alpha=0\ (\alpha\neq0)$；$\alpha=0$ 对应 $n=1$ 且给 $\varepsilon=1$。∎ ⟹ **障碍由"局部因子层"升级为"支撑／锥层"**。

**⭐ ③ 平衡因子定理（本档新增，核心）**：裸反射是空方程 ⟹ 任何非平凡反射必须写成 $F(s)=\varepsilon\Phi(s)F(k-s)$，$\Phi\neq1$。**(i)** 对合条件 $\iota^2=\mathrm{id}$ ⟹ $\Phi(s)\Phi(k-s)=1$（**反自对偶**）。**(ii)** 锥条件：$\Phi(s)F(k-s)$ 支撑须回到正锥，而 $F(k-s)$ 支撑在负锥 ⟹ **$\Phi$ 的支撑必须混合正负指数**。**(iii)** 若 $\Phi$ **算术**，满足反自对偶且混合锥的最一般形态是 $\Phi=\Psi(s)/\Psi(k-s)$（由 $L:=\log\Phi$ 的形式解，**标 [结构性] 待严格化**）⟹ 代入得 $F\Psi=\varepsilon\,\mathrm{mirror}(F\Psi)$ ⟹ 由加强定理 $F\Psi\equiv$ const ⟹ $$\boxed{F=c/\Psi}$$ ⟹ **算术 $\Phi$ 使函数方程退化为对 $F$ 的【定义】而非【约束】** ⟹ **F-leak／走私**。**(iv)** 故要使文本成为真正约束，$\Phi$ **必须非算术** ⟹ 即 **archimedean 完成因子** ⟹ **解释了为什么所有已知函数方程都带 $\Gamma$-因子**（不是"必须写 $\Gamma$"，而是**只有非算术 $\Phi$ 才能使方程非空转**）。

**④ S-ii 判定**：单项式对合（保持正锥）⟹ 素置换 ⟹ 无作用；即使放弃 Euler 积与逐素数可分，裸反射仍只有常解；想救活须引 $\Phi$，而算术 $\Phi$ ⟹ 走私、非算术 $\Phi$ ⟹ archimedean ⟹ $$\boxed{\textbf{S-ii 在"单项式对合＋算术平衡因子"两种情形下均 DEAD}}$$ **残余（OPEN，不杀）**：**(1)** 非线性 substitution 且**不要求**指数单项式化（若要求 $\iota(\mathbf X^\alpha)$ 恰为单个单项式 ⟹ 反射在指数上即 $\alpha\mapsto-\alpha$ ⟹ 乘积的多个单项式无法等于单个 ⟹ 强制 $H_p$ 单项式 ⟹ 退回锥定理）；**(2)** 非 $\Psi/\mathrm{mirror}(\Psi)$ 型的反自对偶算术 $\Phi$。

**下一步（V177 预登记）**：① 攻残余 1（非线性对合且不要求指数单项式化 —— S 的最后一道门）② 攻残余 2（把 $\Phi=\Psi/\mathrm{mirror}(\Psi)$ 严格化，使"算术 $\Phi$ 走私"成为定理）

### F.5am ⭐⭐⭐⭐⭐ **$\Phi\Phi^\iota=1$ 的群上同调审计：$H^1(C_2,K_{\rm arith}^\times)=1$ ⟹ 算术 $\Phi$ 必为 coboundary**（`V177` ✓ 2026-09-15 11:56）

**① `V176`-② 勘误（降级为形式域版本）**：原表述"任一 Dirichlet 级数若 $F(s)=\varepsilon F(k-s)$ 则 $F=$ constant"**过强** —— $F$ 只在**右半平面**收敛、$F(k-s)$ 在**左半平面**，逐系数比较隐含"两边可在同一层面比较"，而 ζ 的 FE 之所以能联系两个方向**恰恰因为存在跨越两个收敛域的完成结构** ⟹ 原表述把该结构**偷渡成前提**。修正版本须含"**且该恒等式可在共同的 Dirichlet／Laurent 形式域中逐系数解释**" ⟹ 定理适用域 ＝ **形式域中可逐系数解释的恒等式**（该降级不影响 §4 链条，因那条链本就在 Laurent 形式域中运作）。

**② 群上同调形式化**：$\iota(s)=k-s$；$\Phi\Phi^\iota=1$ ⟹ $\Phi\in Z^1(C_2,K^\times)$；coboundary ＝ $\Psi/\iota\Psi$ ＝ $B^1$；$H^1=Z^1/B^1$。**若 $H^1=1$ 则 $\Phi\Phi^\iota=1\Rightarrow\Phi=\Psi/\Psi^\iota$** ⟹ 代入 $F=\varepsilon\Phi\,\iota F$ 得 $F\Psi=\varepsilon\,\iota(F\Psi)$ ⟹（修正版锥定理）⟹ $F\Psi=$ const ⟹ $F=c/\Psi$。

**③ ⭐ $K_{\rm arith}$ 严格定义与 $H^1$ 计算**：取 $$K_{\rm arith}:=\mathbb Q\bigl(X_p:\ p\in\mathcal P\bigr)$$（局部参数 $X_p=p^{-s}$ 的有理函数域；系数在 $\mathbb Q$ —— "纯算术"的最自然含义：只有素数 $p$ 与有理系数进入，**不含任何 archimedean 因子**）。反射在局部参数上作用为 $\iota:X_p\mapsto p^{-k}X_p^{-1}$：**(i)** 单项式替换（$p^{-k}\in\mathbb Q$）；**(ii)** $\iota^2(X_p)=p^{-k}(p^{-k}X_p^{-1})^{-1}=X_p$ ⟹ $\iota^2=\mathrm{id}$；**(iii)** 像生成整个域 ⟹ $\iota\in\operatorname{Aut}\mathbb Q(X_p)$，$\operatorname{ord}(\iota)=2$ ✓。记固定域 $L=K_{\rm arith}^\iota$：**Artin 定理** ⟹ $[K_{\rm arith}:L]=2$ ⟹ $K_{\rm arith}/L$ 为二次 Galois 扩张 ⟹ **Hilbert 90** ⟹ $$\boxed{H^1\bigl(C_2,K_{\rm arith}^\times\bigr)=1}$$ 即 $\{\Phi:\Phi\Phi^\iota=1\}=\{\Psi/\Psi^\iota\}$（Hilbert 90 的"范数 1"条件**逐字**就是反自对偶条件）。

**④ 结论 A（本档命中）：算术平衡因子 ＝ coboundary ＝ gauge 变换** ⟹ $F=c/\Psi$ ⟹ **F-leak／走私**（不再是"看起来像"，而是**严格定理**）—— **`V176`(iii) 正式闭合** ✓✓✓。**机制解释的最后一环**：$\Gamma(s/2)\notin\mathbb Q(X_p)$（因 $s=-\log X_p/\log p$，$\Gamma$ 是 $X_p$ 的**超越函数**，非有理函数）⟹ **不在定理作用域内** ⟹ 可合法充当"非 coboundary"平衡因子 ⟹ 与 `V176`(iv)"$\Phi$ 必须非算术"**完全一致** ✓✓。完整因果链：$$\text{算术}\Phi\Rightarrow\text{coboundary}\Rightarrow F=c/\Psi\Rightarrow\text{空转（走私）};\quad \text{非算术}\Phi\Rightarrow\text{archimedean 完成因子}$$

**⑤ 三选判定**：**A 命中**（$H^1=1$ ⟹ 算术 $\Phi$ 必为 coboundary ⟹ 走私）；**B 未出现**；**C 未出现**（S 未命中）。

**⑥ 残余（精确，OPEN，不杀）**：**(1)** $\Phi$ 在**单位环**而非**域**中 —— Hilbert 90 给出的 $\Psi$ **可能落在环外** ⟹ $F=c/\Psi$ 仍成立，但"$\Psi$ 是否算算术对象"需另议（本档新暴露的**唯一严格残余**）；**(2)** **非有理函数型的算术 $\Phi$**（如含算术指数的无穷乘积 $\prod_p(\dots)$ 型），超出 $\mathbb Q(X_p)$，Hilbert 90 不适用 ⟹ **未判**。

**下一步（V178 预登记）**：① 攻残余 1（单位环 vs 域：$\Psi$ 落在环外时 $F=c/\Psi$ 还算不算"算术定义"）② 攻残余 2（非有理函数型算术 $\Phi$）

### F.5an ⭐⭐⭐⭐⭐ **环级 Hilbert 90 审计：$H^1(C_2,R_\pm^\times)\neq1$（奇偶×符号）＋ 支撑闭合**（`V178` ✓ 2026-09-15 11:59）

**① 三层次判据化（唐先生）**：**Level 1** 域 coboundary $\Phi=\Psi/\iota\Psi$（$\Psi\in K^\times$；`V177` 已证 $H^1(K^\times)=1$）；**Level 2** 环 coboundary（$\Psi\in R^\times$ ⟹ $F=c/\Psi$ 完全留在允许类内 ⟹ **真正 F-leak**）；**Level 3** 可接受扩张 coboundary（$\Psi\in K^\times\setminus R^\times$ 但 $1/\Psi$ 仍属允许类 ⟹ 不能简单 DEAD）。**关键缺步**：$\Psi\in K^\times\not\Rightarrow\Psi$ 是允许的算术对象 ⟹ `V177` 只给**域层面** coboundary，**不自动**给允许类中的走私。

**② V178-A：定死环（第一行）**：$$R_\pm:=\mathbb Q[X_p^{\pm1}:p\in\mathcal P]=\mathbb Q[\mathbb Z^{(\mathcal P)}]$$（Laurent 多项式环／群环）；$R_+:=\mathbb Q[X_p]$。**单位群（经典）**：$R_+^\times=\mathbb Q^\times$；$$\boxed{R_\pm^\times=\{cX^\alpha:\ c\in\mathbb Q^\times,\ \alpha\in\mathbb Z^{(\mathcal P)}\ \text{有限支撑}\}}$$（无挠阿贝尔群上的群环，系数为域 ⟹ 单位只有系数单位 × 单式）。

**③ V178-B：环级 Hilbert 90 不成立**（本档核心计算）。设 $\Phi=cX^\alpha\in R_\pm^\times$：$\iota(X^\alpha)=(\prod_pp^{-k\alpha_p})X^{-\alpha}$ ⟹ $\Phi\iota(\Phi)=c^2(\prod_pp^{-k\alpha_p})$ ⟹ **cocycle 条件** $c^2=\prod_pp^{k\alpha_p}$；而取 $\Psi=dX^\beta$ 得 $$\frac{\Psi}{\iota\Psi}=\Bigl(\prod_pp^{k\beta_p}\Bigr)X^{2\beta}$$ ⟹ **环 coboundaries** $=\{(\prod_pp^{k\beta_p})X^{2\beta}\}$ ⟹ $\Phi=cX^\alpha$ 是环 coboundary **iff** $\alpha\in2\mathbb Z^{(\mathcal P)}$（**奇偶条件**）且 $c=\prod_pp^{k\alpha_p/2}$（**符号条件**，因 cocycle 只给 $c=\pm\prod_pp^{k\alpha_p/2}$）⟹ $$\boxed{H^1(C_2,R_\pm^\times)\neq1}\ \text{（障碍＝奇偶×符号）}$$ **具体反例**：$\Phi=-1$ 是 cocycle（$(-1)(-1)=1$）但**不是**环 coboundary（需 $\beta=0$ 且 $1=-1$）；⚠️ 而它在**域**层面**是** coboundary（$\Psi=X_p-p^{-k}X_p^{-1}\in K^\times$，$\iota(\Psi)=-\Psi$）—— 但 $\Psi\notin R_\pm^\times$ ⟹ **Level 1 与 Level 2 的差别在此具体化** ✓✓。

**④ ⭐ 支撑论证（本档第二个核心，杀尽非 coboundary 单项式）**：设 $\Phi=cX^\alpha$（任意）。方程 $F=\varepsilon\Phi\,\iota(F)$ 给 $$\operatorname{supp}(F)\subseteq C\cap(\alpha-C)=\{\delta:0\le\delta\le\alpha\ \text{（逐分量）}\}\ \textbf{有限}$$ ⟹ $F$ 是**有限 Dirichlet 多项式** ⟹ 零点集**有限** ⟹ $\operatorname{Spec}(F)$ **不可能** $=Z_\zeta-\tfrac12$ ⟹ $$\boxed{\text{单项式 }\Phi\ \text{（无论是否 coboundary）}\Longrightarrow\operatorname{Spec}(F)\ \text{有限}\Longrightarrow\textbf{非 S}}$$ 特别 $\Phi=-1$：$C\cap(-C)=\{0\}$ ⟹ $F\equiv$ const（零谱为空）。

**⑤ `V177` 结论 A 修正为析取式**：算术 $\Phi$ ⟹ **(I) 环 coboundary** ⟹ $F=c/\Psi$（方程退化为定义）；**或 (II) 环非 coboundary** ⟹ $\operatorname{supp}(F)$ 有限（零谱有限）⟹ $$\boxed{\text{两路皆不通向}\ \zeta}\ \text{—— }S\ \text{在 Laurent 多项式环层面闭合}$$ ⚠️ `V177` 的域级 $H^1=1$ 仍正确；本档补上"**域 coboundary $\neq$ 环 coboundary**"这一步，并把结论从"走私"改为"走私**或**零谱有限"（后者更强）。

**⑥ 残余（精确，OPEN，不杀）**：由 §4 单项式（＝ $R_\pm^\times$ **全部**元素）已被杀光 ⟹ 残余只能是**非单项式单位**，须在**扩张环**（如 Laurent 级数环 $\mathbb Q[[X_p]][X_p^{-1}]$，单位 $=\{X^\alpha u:u(0)\neq0\}$）中，并要求：算术／$\Phi\iota(\Phi)=1$／**非 coboundary**／**支撑可无限**／唯一选出 ζ 且不编码 ζ。⟹ **具体代数问题：在 Laurent 级数环中解无限方程组并检查非 coboundary 且无限支撑**。

**下一步（V179 预登记）**：① 攻残余（扩张环中的非单项式单位）② 把 §4 支撑论证升级为一般定理（"任何使 $F$ 支撑有限的平衡因子 ⟹ 非 S"）

### F.5ao ⭐⭐⭐⭐⭐ **有限支撑判据（FSC-Dirichlet 筛）＋ `V178` 勘误**（`V179` ✓ 2026-09-15 12:02）

**① `V178` 勘误（T10）**：`V178` §4 的推论"$\operatorname{Spec}(F)$ 有限"**必须撤回** —— **反例 $1+2^{-s}$** 有**无穷多**零点 $s=(2m+1)\pi i/\log2$ ⟹ **有限支撑不蕴含有限零点**（有限 Dirichlet 多项式沿垂直线可有无限多零点）；但 **支撑结论保留**（$\operatorname{supp}(F)\subseteq C\cap(\alpha-C)=\{\delta:0\le\delta\le\alpha\}$ 有限）✓；正确的杀法换为 **谱容量冲突** ✓✓。

**② 有限指数多项式的零点计数（经典）**：$P\not\equiv0$ 为有限指数多项式 $P(s)=\sum_{j=1}^mc_je^{\lambda_js}$ ⟹ 在 $|\operatorname{Im}s|\le T$ 内零点数 $$\boxed{N_P(T)=O(T)}$$ （常数取决于 $\{\lambda_j\}$ 的频率跨度）。**自检例证**：$1+2^{-s}$ 的频率跨度为 $\log2$，零点 $s=(2m+1)\pi i/\log2$ ⟹ $N(T)\approx T\log2/\pi=O(T)$ ✓ 与定理一致。

**③ ⭐ 谱容量冲突（本档核心）**：$N_\zeta(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)\asymp T\log T$，而有限支撑给 $N_F(T)=O(T)$ ⟹ $$\boxed{N_F(T)=O(T)\ \text{而}\ N_\zeta(T)\asymp T\log T}$$ ⟹ 若要求 $\operatorname{Spec}(F)=Z_\zeta-\tfrac12$ 则须 $N_F(T)=N_\zeta(T)\sim\frac{T}{2\pi}\log T$，**与 $O(T)$ 矛盾** ⟹ $$\boxed{\text{有限 Dirichlet 支撑}\Longrightarrow F\ \text{不可能承载}\ Z_\zeta}$$

**④ FSC-Dirichlet 筛（三步）**：**F1** $S$ 有限 ⟹ $F$ 是（广义）Dirichlet 多项式；**F2** $F\not\equiv0$ ⟹ $N_F(T)=O(T)$；**F3** 目标要求 $N_F(T)\asymp T\log T$ ⟹ **矛盾** ⟹ **FSC-DEAD**。

**⑤ ⭐ 可复用筛子（把"单项式杀法"彻底抽象掉）**：$$\boxed{\Phi\longrightarrow\operatorname{Supp}(F)\longrightarrow\text{有限？}\xrightarrow{\text{YES}}\textbf{FSC-DEAD}}$$ $V178$ 依赖具体有限盒 $C\cap(\alpha-C)=\{0\le\delta\le\alpha\}$；本档把"有限盒"**彻底抽象掉** —— **只要任何机制最终把支撑压进有限集合 ⟹ 立即 FSC-DEAD**，**无需**重新分析 $\Phi$ 的具体形式。**适用范围（"有限支撑"的常见来源，逐条可查）**：单项式平衡因子 $cX^\alpha$（`V178`）｜有限阶差分／微分型算子作用于 $F$｜有限秩扰动、有限个指数项线性组合｜任何把支撑限制在有限指数盒内的锥条件（$C\cap(\alpha-C)$ 型、多锥交成有限集）。

**⑥ 严格单向边界（唐先生）**：$$\boxed{\text{finite support}\Longrightarrow\text{DEAD};\qquad \text{infinite support}\not\Longrightarrow\text{ALIVE}}$$ 反例：$F(s)=\sum_{n\ge1}2^{-n}n^{-s}$ 支撑无限但毫无理由产生 ζ 零谱 ⟹ 本筛子**只杀不保**（**必要条件型**，排除法，**不是**充分条件判定器）。

**下一步（V179-① 开）**：在 Laurent 级数环 $\mathbb Q[[X_p]][X_p^{-1}]$ 中解 $\Phi\iota(\Phi)=1$，判定是否存在**非 coboundary 且支撑无限**的单位 —— 即**通过有限支撑筛的唯一剩余代数对象**。

### F.5ap ⭐⭐⭐⭐⭐ **principal-unit 反不变量审计：锥-支撑论证 ⟹ $h=0$ ⟹ Laurent 残余整块 DEAD**（`V180` ✓ 2026-09-15 12:04）

**① 三项分解（唐先生）**：$R=\mathbb Q[[X_p]][X_p^{-1}]$，$\Phi=X^\alpha u$（$\alpha\in\mathbb Z^{(\mathcal P)}$、$u(0)\neq0$），$u=c(1+h)$ ⟹ $$\boxed{R^\times=\mathbb Q^\times\cdot X^{\mathbb Z^{(\mathcal P)}}\cdot(1+\mathfrak m)}=\text{指数}\ +\ \text{常数}\ +\ \text{principal-unit}$$ **② ⚠️ §1 小修正**：$X^\alpha\iota(X^\alpha)=X^\alpha(\prod_pp^{-k\alpha_p})X^{-\alpha}=\prod_pp^{-k\alpha_p}\in\mathbb Q^\times$ ⟹ **单式部分精确相消**（$X^\alpha X^{-\alpha}=1$），**只留一个标量，不产生"$2\alpha=0$"型指数约束**；$\alpha$ 只通过**标量条件** $c^2\prod_pp^{-k\alpha_p}=1$ 与 $c$ 耦合。**③ 常数部分耦合**：$\Phi\iota(\Phi)=c^2(\prod_pp^{-k\alpha_p})(1+h)(1+\iota(h))$ ⟹ cocycle $\iff$ $$(1+h)(1+\iota(h))=\lambda:=1/(c^2\prod_pp^{-k\alpha_p})$$ **④ ⭐ 本档核心：principal-unit ⟹ $h=0$（锥-支撑论证）**：由 (3.1) 得 $\iota(h)=\lambda(1+h)^{-1}-1=(\lambda-1)-\lambda\frac{h}{1+h}$。**支撑比较**：左端 $\iota(h)$（$h\in\mathfrak m$ ⟹ $\iota(h)=\sum_{\alpha\in C\setminus\{0\}}h_\alpha(\prod_pp^{-k\alpha_p})X^{-\alpha}$）满足 $\operatorname{supp}\subseteq-C\setminus\{0\}$、**常数项 0**；右端除常数项 $(\lambda-1)$ 外各项来自 $h/(1+h)=h-h^2+\cdots$，而**正锥对乘法封闭** ⟹ 支撑 $\subseteq C\setminus\{0\}$。⟹ **(i)** 常数项比较：$0=\lambda-1$ ⟹ $$\boxed{\lambda=1}$$；**(ii)** 代入得 $$\boxed{\iota(h)=-\frac{h}{1+h}}$$ ⟹ 左端 $\subseteq-C$、右端 $\subseteq C$、两侧常数项均 0 ⟹ $\operatorname{supp}\subseteq C\cap(-C)=\{0\}$ ⟹ $$\boxed{h=0}$$ ⚠️ **本论证只比较"锥归属＋常数项"，不比较任何无穷系数和** ⟹ **无无穷和陷阱，严格** ✓✓✓。（取对数视角 $g=\log(1+h)$ ⟹ $g+\iota(g)=0$；但 $\iota$ **不保持** $\mathfrak m$（$\iota(X_p)=p^{-k}X_p^{-1}$ 是单位），故 $g$ 是否落在 $\mathfrak m\cap\iota(\mathfrak m)$ 本身即难点 —— 本档用锥论证**绕开**该难点。）**⑤ ⟹ 残余 DEAD**：$h=0$ ⟹ $\Phi=cX^\alpha$（**单式**）⟹ 有限支撑筛（`V179`）：$\operatorname{supp}(F)\subseteq C\cap(\alpha-C)=\{0\le\delta\le\alpha\}$ 有限 ⟹ **FSC-DEAD** ⟹ $$\boxed{\text{模型内 cocycle 只有单式 }\Phi=cX^\alpha\Longrightarrow\text{残余 DEAD}}$$ 顺带重现 `V178` 的两类障碍（奇偶／符号）；$\Phi=-1$ 现被**两条独立理由**判死（单式 ⟹ 有限支撑；$\alpha=0$ ⟹ $C\cap(-C)=\{0\}$ ⟹ $F\equiv$ const）。**⑥ 诚实边界（OPEN）**：分解对**逐变量 Laurent 环**成立，对**无限多变量完整 Laurent 级数环**需另行验证；未覆盖 (a) 非 $\mathbb Q$-系数（代数系数）(b) 非逐变量可分形式的无限乘积型单位 (c) 一般 $\prod_p(\dots)$ 型算术因子。

**下一步（V181 预登记）**：① 攻 (a) 代数系数 ② 攻 (b)/(c) 无限乘积型单位 ③ **撤销 S 线转回主线**（若三项残余经审均为死 ⟹ "$\Gamma$-free 纯算术平衡因子"整条线关闭，转回 A1／A3 同一堵墙）

### F.5aq ⭐⭐⭐⭐⭐ **⭐ S 线结构性关闭（`V171`→`V180`）＋ 主线交接**（`V181` ✓ 2026-09-15 12:11 —— **唐先生拍板：结构性关闭，非暂时搁置**）

**① 关闭链（完整登记）**：
$$\text{算术平衡因子}\ \Phi\ \text{（Laurent 形式环内 cocycle：}\Phi\iota(\Phi)=1\text{）}\ \downarrow\ \text{三项分解}\ R^\times=\mathbb Q^\times X^{\mathbb Z^{(\mathcal P)}}(1+\mathfrak m)$$
$$\text{指数部分}\Rightarrow\textbf{精确相消}（\text{只留标量}\prod_pp^{-k\alpha_p}）;\quad \text{常数部分}\Rightarrow\lambda=1;\quad \text{principal-unit}\ \Rightarrow\ \operatorname{supp}\iota(h)\subseteq-C,\ \operatorname{supp}\tfrac{h}{1+h}\subseteq C,\ C\cap(-C)=\{0\}\ \Longrightarrow\ \boxed{h=0}$$
$$\Longrightarrow\ \Phi=cX^\alpha\ \textbf{单式}\ \Longrightarrow\ \operatorname{supp}(F)\subseteq\{0\le\delta\le\alpha\}\ \textbf{有限}\ \Longrightarrow\ N_F(T)=O(T)\ \text{vs}\ N_\zeta(T)\asymp T\log T\ \Longrightarrow\ \boxed{\textbf{FSC-DEAD}}$$

**② 为什么是"解释性关闭"（层级区分）**：`V180` 的 principal-unit **锥-支撑论证**避开了最危险的漏洞（禁止对 $\sum h_\alpha X^\alpha$ 与 $\sum_\beta(\cdots)X^\beta$ 做无限系数求和比较），只用 $\operatorname{supp}(h)\subseteq C$、$\operatorname{supp}(\iota(h))\subseteq-C$、$C\cap(-C)=\{0\}$ ⟹ $\lambda=1,\ h=0$ 是**真正的支撑几何结论**（非形式级数技巧）⟹ S 线完成的**不是**"又排除若干构造"，而是**证明这一类因子没有足够的自由度** ⟹ 与"再得一条 NO-GO"**层级不同**（后者是清单增长，前者是机制解释）。

**③ 负结构定理（本档新增）**：$$\boxed{\text{Laurent（形式）环内算术因子}\ \overset{\text{cocycle}}{\longrightarrow}\ \text{单式}\ \overset{\text{FSC}}{\longrightarrow}\ \text{有限谱}}$$ 而 RH 所需是**相反性质**：$$\boxed{\text{算术数据}\longrightarrow\text{无限谱对象}\longrightarrow\text{临界线定位}}$$ ⟹ S 线暴露的不是"构造不够复杂"，而是 **纯算术乘法平衡本身无法提供所需的无限谱刚性** ⟹ 主线被推回 `V162` 承重墙。

**④ 类界（§11.2 纪律，必须写清）**：**被关闭**：Laurent 形式环 $R=\mathbb Q[[X_p]][X_p^{-1}]$ 内、逐变量分解成立的算术反自对偶平衡因子。**未覆盖（登记 Uninstantiated，非活跃候选）**：(a) 非 $\mathbb Q$-系数（数域／代数系数）(b) 非逐变量可分形式的无限乘积型单位 (c) 一般 $\prod_p(\cdots)$ 型算术因子。**模型边界**：三项分解对**逐变量 Laurent 环**成立（经典），对**无限多变量完整 Laurent 级数环**需另行验证。**结论精确形式**：**不**声称"全数学 DEAD"，只声称"上述类内 DEAD"。

**⑤ 为什么不攻 (a) 数域系数**：$$\boxed{\text{杀手是}\ C\cap(-C)=\{0\}}$$ 只要系数域嵌入**特征零有序／赋值结构**使 $\mathfrak m$ 保持相同支撑分离，则 $\iota(h)\in-C$ 与 $-\tfrac{h}{1+h}\in C$ 仍迫使 $h=0$ ⟹ 换数域**不触及真正的瓶颈**。

**⑥ 为什么不攻 (b)/(c) 无限乘积单位**：一旦允许任意不可分的无限乘积型单位，**必须先重新定义模型本身**（完备化？支撑良基？乘法逐项定义？$\iota$ 仍是同一自同构？恒等式是否合法？）⟹ 这是**换模型逃避 V180 的结论**，而非突破；除非有**独立理由**证明其具有 RH 所需谱自由度，否则不投入。

**⑦ 重开条件（明确登记）**：**(R1)** 给出**独立于本模型**的算术因子，同时满足：算术可构造／反自对偶／$\operatorname{supp}(F)$ **无限**／不与 $\Phi=c/\Psi$ 型走私等价，**且** $N_F(T)\asymp T\log T$；**(R2)** 证明无限乘积型单位存在**非等价于 V180 框架**的新谱自由度（须先给完备化与良基性）；**(R3)** 发现 $C\cap(-C)=\{0\}$ 在目标类中**不再成立**（即存在允许的"混合锥"算术因子）。⚠️ 三条均未满足 ⟹ 按纪律**不再投入**。

**⑧ 主线交接（A1／A3）**：**承重墙（`V162`）** $$\boxed{T\log T\ +\ \text{Weil 正性}};\qquad \text{核心缺口}：\boxed{\text{局部算术结构}\ \not\Longrightarrow\ \text{全球谱定位}}$$ 已知无条件输入不足：比例天花板 $0.682$｜第三矩／高相关需 support $>1$｜T² 律／预算越界（`V102`／`V162`）⟹ **唯一登记靶点：E102 §8 target1**。**V182 建议：形式化 N31**（char-0 无条件 $\sqrt{\cdot}$-正性 ⟹ origin 可归约到 finiteness）—— 理由：把三条**族级 NO-GO** 升级为**结构结论**（目前只在 known-candidate 级，覆盖性论证未证），杠杆最高。

### F.5ar ⭐⭐⭐⭐⭐ **N31 全证明审计：四箭逐个判定 ⟹ 判定 B＋C（箭 3 为假；两难；封口）**（`V182` ✓ 2026-09-15 12:13）

**硬目标（唐先生）**：char-0 无条件 $\sqrt{\cdot}$-正性 $\Longrightarrow$ origin reduction $\Longrightarrow$ finiteness；四箭必须独立闭合；**纪律：先不要证明"某已知候选满足 N31"，而要证"假设本身 ⟹ finiteness"**；三选 A／B／C（**C 也算实质结果**）。

**① 箭 1（钉死正性输入）**：必须钉死 (1a) 测试函数类范围｜(1b) 是否允许依赖 $T$｜(1c) 是否 PSD（决定能否用 Cauchy–Schwarz 产生 $\sqrt{\cdot}$ 型界 —— 这正是"$\sqrt{\cdot}$-正性"的来处）⟹ 无论怎么钉，都落入 §4 两难。

**② 箭 2（origin reduction）前提混入待证结论**：$\mathcal O(F)$（原点量）的存在要求对象有**局部（算术）模型** —— 正是 `V105`（L2 载体迁移）判 **0/14** 的东西 ⟹ 箭 2 的前提**正是族级 NO-GO 的内容**；若不要求局部模型，$\mathcal O(F)$ 只能是谱侧量 ⟹ 箭 2 退化为箭 3。

**③ ⭐ 箭 3 判为【假】（不是"未证"）**：**(3a) 反例类** —— 取 $H=\operatorname{diag}(\lambda_j)$ 自伴，$Q(f)=\langle Hf,f\rangle\ge0$，$\{\lambda_j\}$ **任意**（含 $\lambda_j\asymp j\log j$）⟹ 存在正半定、无条件、char-0 的二次形式，其谱恰为 $\{\lambda_j\}$ ⟹ $$\boxed{\text{正性}\ \not\Longrightarrow\ \text{任何计数界}}$$ **(3b) 加强到 trace-class 也只给 $O(T^2)$**：若 $\tau=\sum_j\frac1{1+\lambda_j^2}<\infty$，则 $|λ_j|\le T$ 时 $\frac1{1+λ_j^2}\ge\frac1{1+T^2}$ ⟹ $$\boxed{N_F(T)\le\tau(1+T^2)=O(T^2)}$$ 而 $O(T^2)$ 与 RvM 的 $T\log T$ **不矛盾** ⟹ **箭 4 无从产生矛盾**。⭐ 要得 $O(T)$ 必须要求**一阶可和** $\sum_j\frac1{1+|λ_j|}<\infty$，而这对 $\lambda_j\asymp j\log j$ **发散**（$\sum1/(j\log j)=\infty$）⟹ 一阶可和要求**排除 $T\log T$ 谱**。

**④ ⭐⭐ 两难（本档最强结论）**：**无条件读法**（全测试函数／全 $T$、PSD）⟹ 由 (3a) 与 $N\asymp T\log T$ 相容 ⟹ **不给界** ⟹ 箭 3 假；**强读法**（输入强到迫使 $N=O(T)$）⟹ 由 (3b) 等价于**一阶可和** ⟹ **排除** $\lambda\asymp j\log j$ ⟹ 已排除 ζ 零谱密度 ⟹ **该输入已蕴含 RH 强度** ⟹ **非无条件** ⟹ **循环**。⟹ $$\boxed{\text{无条件}\Longrightarrow\text{太弱（不给界）};\quad \text{给界}\Longrightarrow\text{太强（已是 RH）}}\ \Longrightarrow\ \boxed{\text{N31 的桥}\ \textbf{不存在}}$$

**⑤ 判定 ＝ B ＋ C**：**(B)** 失效在**箭 3**（且为假，有反例类），箭 2 亦混入待证结论；**(C-i)** 若把输入加强到"一阶可和"，对 ζ 无条件为**假**（RvM 给 $\sum1/|\gamma|$ 发散）⟹ N31 的假设对目标对象**空转** ⟹ 结论**真空**，不构成族级 NO-GO；**(C-ii)** 若把输入弱化为"ζ 可用"，则必须提供**线性 Weyl 律（1 维半经典密度）** —— 正是 `V162` 的 $$\boxed{T\log T+\text{Weil 正性}}$$ 墙本身。⟹ **N31 或空转，或 ≡ `V162` 墙** ⟹ 按纪律**立即封口，不包装成突破**。

**⑥ 一致性 ＋ 一条撤回**：与 `V162`（$T\log T$ 是 1 维半经典律，自然产生需 continuation）／`V179`（一阶可和才是 $O(T)$ 的正性侧充分形式，对 ζ 空转）／`V144`（零点在 Archimedean 层）一致。⚠️ **重要撤回**：此前（09-14 台账）把"形式化 N31"列为**最高杠杆**的升级路径 —— 本档判定该路径**不存在** ⟹ **三条族级 NO-GO（L1／L2／L3）保持 known-candidate 级，不升级**。

**下一步（V183 预登记）**：① 回主线承重墙攻**线性 Weyl 律的算术来源**（正性侧已证不可达 ⟹ 只剩几何／算术构造侧）② 审 §3(3b) 的**一阶可和门槛**可否反向用作新筛子（与 `V179` 有限支撑筛并列）

### F.5as ⭐⭐⭐⭐⭐ **线性 Weyl 律的算术来源审计 ⟹ DEAD（源-基数障碍 ＋ $S(T)$ 等价于 RH）**（`V183` ✓ 2026-09-15 12:16）

**硬目标（唐先生）**：$$\boxed{\text{什么算术结构，能够强制}\ N_F(T)=O(T)\ \text{或线性密度？}}$$ 第一原则：**先审计线性 Weyl 律本身**；判死标准：**若只能得 $\mathcal A(T)=O(T)$ 但无法控制纤维；或必须假设 $N_F(T)\ll T$；或所需条件等价于 RH／Weil 正性／已知线性律 ⟹ 立即封口**。② 一阶可和筛定位为**验尸工具／必要条件**，不单独开档。

**① 四类机制逐条 DEAD**：**(1) 离散长度谱**（每谱点 ↔ 整数／理想／素数事件）：此类事件**至多线性**（理想范数 $\le T$ 约 $cT$）⟹ 由 §2 不可能覆盖 $T\log T$ 零谱 ⟹ DEAD；**(2) 几何维数**（1 维／rank-1）：1 维 Weyl 给 $N(\lambda)\asymp\sqrt\lambda$ ⟹ 量级不符，且 $T\log T$ 真实来源是 $\Gamma$-相位（非几何）⟹ DEAD；**(3) 局部计数**（每高度区间 $O(1)$ 新自由度）：由 RvM，ζ 每单位高度新增 $\asymp\frac1{2\pi}\log T$ **不是 $O(1)$** ⟹ 该机制给出**过度稀疏**谱 ⟹ DEAD（此条最接近"算术可实现"，恰被 RvM 排除）；**(4) 算术唯一性**：即纤维条件 $\#\Phi^{-1}\le C$ —— **必要但非决定性**（见 §3）。

**② ⭐ 决定性障碍（本档核心，先行）：源-基数障碍**。RvM（**无条件**）：$$N_\zeta(T)\asymp T\log T$$ ⟹ 若源满足 $\#\mathcal A_{\le T}=O(T)$，则 $\#\Phi(\mathcal A_{\le T})\le O(T)$，要覆盖 $T\log T$ 个谱点须 $T\log T\le O(T)$，**矛盾** ⟹ $$\boxed{\text{线性计数源}\ \textbf{不可能}\text{覆盖}\ \zeta\ \text{零谱}}$$ ⚠️ **无条件**（只用 RvM，不依赖 RH／Weil／显式公式）⟹ 最干净的一层；与 `V179`（"有限支撑 ⟹ $O(T)$ ⟹ 冲突"，从 $F$ 结构出发）**互为镜像**。

**③ 纤维问题审计（唐先生危险点）**：$$\mathcal A_{\le T}\overset{\Phi}{\longrightarrow}\{\text{谱点}\ |\gamma|\le T\}$$ 的注入／有限纤维问题 —— **条件确实必要**（否则一个谱点可携带 $O(\log T)$ 内部自由度），但**不是本档瓶颈**：障碍在**更早**（源的基数本身只有 $O(T)$，即使纤维 $\equiv1$ 也不够）；且要救它只能**扩大源**到超线性 ⟹ 纯算术事件（素数／理想）**只有（次）线性计数**，能产生 $T\log T$ 计数的结构是 $\Gamma$-相位（archimedean）⟹ **回到层诊断**。

**④ $T\log T$ 的真实来源**：$N(T)=\frac{\theta(T)}{\pi}+1+S(T)$，$\theta(T)=\operatorname{Im}\log\Gamma(\frac14+\frac{iT}{2})-\frac T2\log\pi$，$\theta(T)\sim\frac T2\log\frac T{2\pi}-\frac T2-\cdots$ ⟹ $\frac{\theta(T)}{\pi}\asymp T\log T$ ⟹ $$\boxed{T\log T\ \text{的主项来自}\ \textbf{完成函数的相位增长（archimedean）}，\textbf{不是}\text{几何 Weyl 律}}$$ 与 `V144` 层诊断**完全一致**；且 $\theta$ 与 RvM 均**无条件** ⟹ **$T\log T$ 这一层不构成缺口**。

**⑤ 唯一剩下的计数问题 ＝ 涨落 $S(T)$ ⟹ DEAD**：无条件 $S(T)\ll\log T$（Littlewood）；$$\boxed{\text{RH}\Longleftrightarrow S(T)\ll\frac{\log T}{\log\log T}}$$（von Koch／Littlewood，经典）⟹ 控制 $S(T)$ 的算术来源 **≡ RH** ⟹ 按判死标准 ⟹ $$\boxed{\textbf{DEAD，封口}}$$ ⚠️ **目标改写**：要的不是 **Weyl 律**（密度／主项，无条件已知），而是 $$\boxed{\textbf{涨落（误差项）控制}}$$ —— 这是**抵消／相消**问题，**不是**计数问题。

**⑥ 与 `V162` 墙的对应**：$$\boxed{\text{主项}\ T\log T\ \text{（条件成立）};\qquad \text{缺口}\ =\ \text{Weil 正性}\ =\ \text{涨落相消}}$$ ⟹ `V162` 的"墙"**不是**产生 $T\log T$ 密度，而是**抵消其涨落** ⟹ 与 A1／A3 **完全一致**。

**下一步（V184 预登记）**：① **正面**：攻**涨落相消的算术来源**（＝ A1／A3 的算术实现；今晚唯一剩下的承重缺口）② **工具化**：把**源-基数障碍**做成新筛子（与 `V179` 有限支撑筛、`V182` 一阶可和门槛并列）

### F.5at ⭐⭐⭐⭐⭐ **外部输入分诊（不局限 RH）—— 【惯性／签名计数】新机制类型 ＋ 0.68185 天花板（＝我们的 0.682）**（`V184` ✓ 2026-09-15 12:24）

**委托（唐先生）**：搜索所有数学／物理模型相关研究（**不特定 RH**），找符合我们要求的"特别输入"。

**⭐ A（最重要）无条件对相关（带宽 ≤1）＋ Weil 形式 ＋ Sylvester 惯性** —— `More than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line`（署名 **Claude**；专家注 Alpöge–Furman；arXiv:2608.13637；2026-08；**Lean 形式化** anthropics/formal-math `zeta23/`，toolchain `lean4:v4.33.0-rc2` + Mathlib `v4.33.0-rc2`；Conrey／Goldston 复核）：**无条件** $N^*_0(T,2T)/N(T,2T)\ge2/3$，优化后 $0.6725$，$(5/6-o(1))N$ 互异。**三件输入**：(i) 零点平均密度（RvM）(ii) **Montgomery 对相关，测试函数 Fourier 支撑 $\subset(-1,1)$ —— 无条件**（Aryan 2022；**Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh** 2024, Acta Arith. 214）(iii) 重数整性。**⭐ 关键技术（RH 不进入）**：经典需 RH 把零点侧读成正和；他们改用 $$\boxed{\text{有限压缩的 Weil Hermitian 形式}\ +\ \textbf{Sylvester 惯性定律}}$$（离轴对 $\{\rho,1-\bar\rho\}$ 贡献一个 **block**）⟹ 用**符号计数**而非**正性** ⟹ **绕开 `V182` 的障碍**（V182 证"正性 ⟹ 无计数界"）⟹ **本项目 183 轮从未出现的机制类型** ✓✓✓。**⭐ 最优性 Remark 1.1**：只读带宽 $\le1$ 数据、逐配置成立的证书**无法超过 $\boxed{0.68185}$** ⟹ **带宽 $\le1$ 已封顶**；下一步必须 support $>1$ ⟹ **正是我们 `V162`／A3 的墙** ✓✓✓（"0.682"被独立证明为该类硬天花板）。**过程**：$\sim60$ subagents／2400 shell／31M tokens／**650 次失败**；Lean 作机械审计层；人类专家收口 ⟹ **工具链与本机已装 Lean 4.33.0 同版本 ⟹ 可本地复现** ✓✓。

**⭐ B Connes–Consani 线（archimedean 桥 ＋ 新正性机器）**：自述缺失构件 ＝ **arithmetic site 的平方上的 intersection theory ＋ Riemann–Roch**（char-1；已有 `Riemann–Roch for the ring ℤ`）；**Sonin 空间压缩 ⟹ archimedean place 的 Weil 正性**（Selecta 2021）；**prolate 算子自伴延拓的 UV 谱＝零点平方**（PNAS 2022，Connes–Moscovici），并可造**等谱 Dirac 族**；2026 `On the Jacobian of Spec ℤ`（JNCG）**自伴性由 Carathéodory–Fejér（Toeplitz 正性）推广保证** ⟹ **新正性来源**。⚠️ 需过我们的筛子：逐点＝全部零点？走私？等谱族 ⟹ 谱"族"而非"点"？**UV 匹配 ≠ 逐点同一**（与 `V165` T3 同型风险）。

**⭐ C 物理侧更强的正性机器**（ICTS 2025 讲义 arXiv:2603.28454）：正性三来源 ＝ ①Feynman 参数化 ⟹ **CM／Stieltjes** ②酉性＋解析性 ⟹ **色散关系＋正谱密度 ⟹ Stieltjes** ③**正几何 canonical form ⟹ 完全单调**。⟹ **CM／Stieltjes 比 PSD 强、自带定量内容**（Bernstein 表示；正测度＋矩条件）⟹ **正对症 `V182` 缺口**；开放问题：能否无条件把 ζ／Weil 放进 CM／Stieltjes／色散框架（⚠️ 风险：等价于已有正性 = 换语言）。

**D Guth–Maynard 2024**：大值估计 ⟹ $N(\sigma,T)\le T^{30(1-\sigma)/13+o(1)}$；**Ingham $0.6\to0.52$**；短区间素数 $x^{17/30}$；方法＝调和分析／多项式方法（外部技术注入）⟹ 真新无条件输入，但方向是"密度／排斥"，非涨落相消。
**E Dyatlov–Zworski**（已证 RH 型定理；microlocal ＋ anisotropic Sobolev）⟹ ⭐ **负载假设＝双曲扩张 ＋ 轨道指数增长** ⟹ 与函数域／Ihara 图 ζ 同侧；char-0 素数增长为多项式 ⟹ **机制不可移植**（分类学数据，与 `V144` 一致）。
**F 低可信度**：TechRxiv 2025 声称"Hermitian 算子谱＝零点虚部"（非同行评审）⟹ 登记为筛子测试样本。

**四个动作**：(1) **精读 arXiv:2608.13637**（§7.1 测试族优化／Remark 1.1 最优性／**Sylvester 惯性那一步**），把 **0.68185** 登记（对齐我们的 0.682）(2) **本地复现其 Lean 形式化**：装 Mathlib（`ghfast.top` 镜像）→ clone `anthropics/formal-math` `zeta23/` ⟹ **首次获得可机器验证的 ground truth** (3) 用我们的筛子审 **B／C** 两候选 (4) **工作流改造**：`sessions_spawn` 并行 subagent ＋ Lean 审计层 ＋ 数值验证 ＋ 外部专家收口 ⟹ 直接回应"低效"

### F.5au ⭐⭐⭐⭐⭐ **论文精读（arXiv:2608.13637）＋ V186 Inertia Mechanism Audit：终点退回 Weil 正性 ⟹ 关**（`V185`／`V186` ✓ 2026-09-15 12:50）

**论文（精读，`V185`）**：`More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line`（**署名 Claude**；专家注 Alpöge–Furman；arXiv:2608.13637v2，2026-08-24，21 页；**Lean 形式化，全部 Lean 代码由 Claude 撰写**；Comparator＋NanoDa 重放；Palomar 投稿）。**结果**：无条件 $N_0^s(T,2T)\ge(\frac23-o(1))N$、$N_d\ge(\frac56-o(1))N$；MT 窗 $0.67250$／$0.83625$（$c_{\rm MT}^{-1}=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}$）；对原初 Dirichlet $L(s,\chi)$ 同样成立。**机制（论文 §1.2 三步＋单链）**：取窗 $\psi$ 与 $\phi(u)=\chi(\frac L2+u)\chi(\frac L2-u)\psi(u/L)^{1/2}$，等间距调制 $\alpha_k=T+\frac{2\pi k}{L}$、$d=\lfloor LT/2\pi\rfloor=N(T,2T)+O(L)$，$v_\rho=(\widehat\phi(\gamma_\rho-\alpha_k))_k\in\mathbb C^d$，$\widetilde G=\frac1{aL^2}\sum_{\Re\gamma_\rho\in I'}m_\rho v_\rho v_\rho^{\mathsf T}$，$P=$ 在线部分，$Q=\widetilde G-P$。**(Z)** 零侧：在线点给 $P$ 非负 rank-one；**功能方程把离轴零点成对配 $\{\rho,1-\bar\rho\}$ ⟹ $Q$ 一个签名 $(1,1)$ 的 block** ⟹ $n_+(Q)\le p$、$N\ge s_1+2s_2+2p$、$\operatorname{tr}\widetilde G=(1+o(1))N$。**(P)** 素数侧：$\|\widetilde G\|_{\rm HS}^2=(R(\psi)+o(1))N$，$R(\psi_0)=\frac43$、$R(\psi_{\rm MT})=c_{\rm MT}^{-1}$ —— **Montgomery 无条件素数侧二阶矩（带宽 $\le1$）**（[Mon73],[Ary22],[BGSTB24]）。**(L)** **Lemma R**：$P\succeq0$、$\operatorname{rank}P\le r$、$n_+(Q)\le b$ ⟹ $\|P+Q\|_F^2\ge c\operatorname{tr}P-\frac{c^2}{4}r+2c\operatorname{tr}Q-c^2b$（取 $c=2$ 解出 $\operatorname{rank}P\ge2\operatorname{tr}P+4\operatorname{tr}Q-4b-\|P+Q\|_F^2$ ＝ 论文 (1.1)）；证明用 **von Neumann 迹不等式**；**且已形式化证明该不等式紧**（`ZeroSide/TightMult.lean`）。**单链**：$N_0^s+o(N)\ge\operatorname{rank}P_1\ge4\operatorname{tr}\widetilde G-2N-\|\widetilde G\|_{\rm HS}^2=(2-R(\psi)-o(1))N$。**解析输入**：Weil 显式公式｜RvM｜$N(t,t+1)\ll\log t$｜$\Gamma'/\Gamma$ Stirling｜Chebyshev–Mertens（$\sum\Lambda^2$）｜Montgomery–Vaughan —— **不用 mollifier／零点密度／零自由区**。**天花板**：Remark 1.1 ⟹ 带宽一类证书**无法超过 0.68185**（形式化 0.6818287＋唯一数值假设 `EnclOK`＝256 个整数包络）；**阶梯：达 0.70／0.80／0.90 需 Fourier 支撑到约 1.04／1.26／1.70（超出已知）**。

**V186（Inertia Mechanism Audit，七问拆解）**：**① $Q_T$** ＝ Weil 形式的 **Gabor 压缩**（非对角性来自相邻窗重叠，(2.11)）；**② rank** ⟸ Lemma R（**纠正**：不是平凡 C-S 界，是两矩阵不等式且紧）；**③ $\operatorname{tr}Q_T$** ⟸ **RvM**（预算总量 $\approx N$）；**④ $\operatorname{tr}(Q_T^2)$** ⟸ **素数侧二阶矩（带宽一，唯一真正算术杠杆）**；**⑤ $n_-(Q_T)$** ＝ **离轴对数**（$(1,1)$-block）——**用法与我们旧结论相反**（我们 V147／V148／V174 把功能方程当"对合 ⟹ 无单边律／选择难题"，此处当作**计数装置**）；**⑥⑦ 输入**：唯一算术输入＝素数侧二阶矩；其余为经典分析数论；**不用 mollifier／零点密度／零自由区**。

**⭐⭐ 关键一刀的答案（交换率 ＋ 终点退化）**：$$\frac{N_0^s}{N}\ \ge\ 2-R(\psi)$$（本档核算：$4/3\to\frac23$；$c_{\rm MT}^{-1}\approx1.3275\to0.6725$）⟹ **100% ⟺ $R(\psi)\le1$ ⟺ 需 support $>1$ 的输入**（与 `V162`／A3 墙精确对齐；阶梯 1.04／1.26／1.70）。**⭐⭐⭐ 终点退化定理（本档核心新增）**：$n_-(Q_T)$ **恰数离轴对** ⟹ $100\%\iff n_-(Q_T)=0$ 对全族 ⟹ $Q_T$ 半正定 ⟹ 取极限得 **Weil 形式非负** ⟹ [Wei52, Bom00] **Weil 正性 ⟺ RH** ⟹ $$\boxed{\text{inertia 路线不是 Weil 正性的替代};\ \text{它只在}\textbf{部分比例}\text{处有效，在"消灭离轴零点"处}\textbf{退回正性}}$$ ⟹ **按唐先生预定规则：关**。

**⭐⭐ 两项收获（留下）**：**(收1) 机制本身（新）**：indefinite form ⟹ inertia ⟹ rank ⟹ counting —— 不要求 PSD，故 `V182` 的"正性 ⟹ 无计数界"**不适用**；但限度是二阶矩的带宽可得性（上限 0.68185）。**(收2) 转移原理（工具，进筛子表）**：$$\boxed{\text{可算}\ \operatorname{tr}G\ \text{与}\ \|G\|_{\rm HS}^2\ \text{且可上界}\ n_+(G-P)\ \Longrightarrow\ \operatorname{rank}P\ \text{有下界}\ \Longrightarrow\ \text{零点计数下界}}$$ ＝ `V182` 的**对偶面**（V182：正性/一阶信息不足；本条：一阶＋二阶＋正惯性上界 ⟹ 计数下界）；形式化侧可复用（**von Neumann 迹不等式与 Sylvester 惯性定律双向此前不在 Mathlib，由该形式化贡献**）。

**下一步（V186 预登记，三选）**：① 把**转移原理**形式化进筛子表 ② 攻 **support $>1$** 的**已知进展**（BGSTB／Goldston–Lee–Schettler–Suriajaya "Alternative Hypothesis" 2025 等），看 1.04 档是否有人在推 ③ 接受部分比例路线封顶 0.682，转回涨落相消（但按 §3 逻辑仍回到 Weil 正性）

### F.5av ⭐⭐⭐⭐⭐ **Global Cancellation / Elimination Audit：⚡ 核心结构事实（离轴对三面性）＋ 三分分类 ⟹ 整族封闭**（`V187` ✓ 2026-09-15 12:53）

**原型（唐先生）**：$$\text{local DOF}\to\text{elimination}\to\text{effective coupling}\to\text{invariant preserved}$$ 与 Gaussian elimination／Schur complement／RG decimation／Morse cancellation／filtered Lefschetz cancellation 同族；反向原型 ＝ "先定义可消局部自由度，再证消元后 defect 不变"。**任务**：该原型能否产生**新的算术可消自由度**定义？

**⭐⭐⭐ 核心结构事实（证明级，直接来自 `V186` 的 $(1,1)$-block）**：功能方程把离轴零点配成 $\{\rho,1-\bar\rho\}$，压缩块签名 $(1,1)$ ⟹ **同一离轴对，对不同不变量表现完全不同**：

| 不变量类型 | 离轴对贡献 | 结论 |
|:--|:--|:--|
| signature $n_+-n_-$ | $0$（中性） | **盲** ⟹ 检测不到 |
| inertia $n_-$ | $+1$ | 可见，但需 $n_-=0$ ＝正性 |
| trace $\operatorname{tr}$ | $0$（block 无迹） | 中性 |
| $\operatorname{tr}(G^2)=\|G\|^2_{\rm HS}$ | $+\lambda^2$ | 可见（$R(\psi)$ 的来源之一） |
| $\det G$ | 带负特征值 | **可见** |

$$\Longrightarrow\ \boxed{\text{任何 index／signature／Euler 特征型的全局不变量，对离轴零点是}\textbf{结构盲}\text{的}}$$ **⟹ 可直接用作筛提案判据**：凡声称"用 defect／winding／null-sector 证无离轴零点"者，必在某处偷用 signature 之外的信息。

**⭐ 三分分类与归宿（整族封闭）**：**(i) index／signature 型 ⟹ 结构盲**（"把离轴贡献归入可消 null-sector"**不是可证的希望而是事实**：离轴对本来就是 signature-中性块，消掉与留着不变量相同 ⟹ **永远得不到 RH**）；**(ii) count／inertia 型 ⟹ 终点 $n_-=0$ ＝正性 ⟹ Weil 正性 ⟹ RH**（`V186`；只在部分比例处有效）；**(iii) det／regularized-det 型 ⟹ 对离轴对可见，但算术实现 ＝ Deninger 程序**（`V145`：有 canonical generator，缺 canonical polarization）或显式公式 ⟹ 旧墙。⟹ $$\boxed{\text{"global cancellation／elimination"整族落回既有三堵墙}}$$

**四候选逐个判定**：**(A) Bose–Fermi spectral conspiracy** ⟹ 结构上 ＝ "谱求和可由别的路径算出" ＝ **显式公式**；其引擎（涌现对称／large-N）在算术侧**无对应物** ⟹ 退化（A− → 降级）；其中真命题 **cancellation ≠ pairing** 留下（相消机制扩充为四类：逐项配对／迹级／指标级／尺度级）。**(C) supersymmetric spectral quotient／null-sector** ⟹ index 型 ⟹ **盲** ⟹ 封。**(D) index-space RG／Wiener RG** ⟹ 需消元映射**收缩性（谱隙）**，而算术情形的收缩性/谱隙**恰好等价于既有 RH 相邻陈述** ⟹ 退化（但 RG 语言正面用处：$\|\mathcal R^k(C)-C_*\| \le \rho^k\|\cdot\|$ ⟹ 若 $\rho<1$ 可证即得 **$S(T)$ 次线性界**，即缺口位置，也正是缺口无法无条件填的位置）。**(E) Lefschetz／Morse cancellation** ⟹ 需链复形＋同调不变量，而"Spec $\mathbb Z$ 的上同调/相交理论"正是前端**命名缺失构件**（arithmetic site 平方上的 intersection theory ＋ Riemann–Roch）⟹ **不是新路，是同墙新记法**；且 §2 暗示离轴对是 **collapsible**（signature-中性）⟹ 该机制"消元保不变量"恰恰**保证**它看不到它们。**(F) quasicrystal RG** ⟹ B（无 deterministic cancellation，留背景）。**(G) quantum optimal transport** ⟹ B+（提供"一对多耦合＋全局优化"的**框架**，非机制）。**(H) "arithmetic SUSY／p-adic string／emergent spacetime"** ⟹ **丢弃**（把"希望存在的相消"写进模型，无 arithmetic→spectral bridge）。

**唯一逃生口（OPEN，不杀但不投入）**：既非 index／count／det 的**第四类不变量**（非线性／范数型／多层）；但任何"能检测离轴零点"的不变量必须对 $(1,1)$ 块**非中性** ⟹ 必须用量级或符号 ⟹ 而 `V183` 已证量级/密度型信息受**源-基数**限制、且 $T\log T$ 主项无条件而缺口只在涨落 $S(T)$ ⟹ 第四类不变量若真工作，必须直接给 $S(T)$ 的界 ⟹ 即回到 **Weil／Li 正性** ⟹ **形式存在、实质封闭**。

**下一步（V188 预登记，三选）**：① 把**筛提案判据**（§2 表格＋§3 三分归宿）固化成工具卡（与 `V179`／`V182`／`V183`／`V186` 并列）② 攻第四类不变量（预计回到 Weil 正性）③ 接受外部机制普查到此为止：本晚已连关 **S 线（V181）／N31（V182）／线性 Weyl 律（V183）／inertia 终点（V186）／cancellation 族（V187）**，全线收敛到同一核心 ⟹ 转回 **A1／A3（Weil／Li 正性）**

### F.5aw ⭐⭐⭐⭐⭐ **Null-Relation / Spectral-Compensation Audit：⚡ 饱和定理（线性通道盲）＋ 四通道穷尽 ⟹ 封**（`V188` ✓ 2026-09-15 12:55）

**原型（唐先生）**：$$\text{local DOF}\to\text{global constraint}\to\text{compensation}\to\text{residual defect};\qquad \text{核心是}\ \sum_n w_na_n=C\ \text{或}\ \sum_jK_{ij}X_j=0\（\text{非逐项配对}\bigr)$$ 六条要求：$K$ 非局部／跨尺度／非人为 RH 等价／有 arithmetic origin／迫使局部涨落补偿／压制 $S(T)$。与 `V182`（$Q\succeq0$）、`V186`（$\operatorname{Inertia}Q$）构成三元组，本档为第三支 **$\ker K\neq0$**。

**⭐⭐⭐ 饱和定理（本档核心）**：零测度 $\mu=\sum_\rho m_\rho\delta_{\gamma_\rho}$ 的**全部线性统计量** $\sum_\rho m_\rho\widehat f(\gamma_\rho)$ **已由 Weil 显式公式（经典）与算术侧一并确定**（测试函数类稠密 ⟹ 线性泛函族确定 $\mu$）⟹ 任何**额外的线性（求和／矩／迹／null-relation）关系都是它的推论，不增加信息** ⟹ 该通道**已饱和**。⚠️ 而 **RH $\Longleftrightarrow \operatorname{supp}\mu\subset\mathbb R$** —— 这是**支撑性质**，**不是**线性统计性质（线性泛函只看见位置的加权和，看不见"某点是否离开了轴"）⟹ $$\boxed{\text{线性／全局求和／sum-rule／UV--IR／null-relation 通道对}\ \beta\ \textbf{结构性盲}}$$ 与 `V187` §2（signature／trace 中性）**完全一致**。⚠️ 诚实：饱和 ≠ 无用；把它**反演**成逐点位置需要**无界精度**，那一步正是 $S(T)$ 问题本身。

**六候选逐个判定**：**(1) Optical Hall sum rule／spectral compensation** ⟹ 频率矩恒等式 ⟹ **线性 ⟹ 盲**（留下形状：**矩恒等式强制跨尺度补偿**）。**(2) Spectral covariance sum rule／spectral rigidity** $\left(C(0)+\sum_{\ell\neq0}C(\ell)=0\right)$ ⟹ 对 ζ 的对应物**无条件存在**：**Selberg 中心极限定理** $S(t)/\sqrt{\frac12\log\log T}\Longrightarrow\mathcal N(0,1)$ ⟹ 无条件**典型**尺度 $\asymp\sqrt{\log\log T}$；⚠️ **但目标是最坏情形**，三层结构（经典）：**典型 $\sqrt{\log\log T}$（无条件）／无条件最坏 $O(\log T)$（Littlewood）／目标 $O(\log T/\log\log T)\Longleftrightarrow\text{RH}$（von Koch）** ⟹ **rigidity 型输入恰好只覆盖第 1 层，典型→逐点的过渡恰是 RH 等价陈述** ⟹ 退化。**(3) Interlacing／barrier（Bilu–Linial 改进）** ⟹ 形状"族＋夹逼 barrier"，但**已被 67.2% 证明用尽**（族＝窗／调制族，barrier＝临界线），其天花板**已被证明**（0.68185／形式化 0.6818287）⟹ 非新路。**(4) Index-space RG** ⟹ 需消元映射**收缩性（谱隙）**，算术情形**等价于既有 RH 相邻陈述**（`V187` §4(D)）；正面残留：$\rho<1$ 可证即得 $S(T)$ 次线性界 ＝ 第 3 层。**(5) UV–IR compensation／anomaly sum rules** ⟹ 对 ζ，UV–IR matching 的实例**就是显式公式**（素数＝UV，零点＝IR）⟹ 又是线性 ⟹ 盲。**(6) Spectral decoupling／local nullspace $\to$ global gap** ⟹ B+（正是缺的 local arithmetic → global spectral localization，但算术侧无对应 null-space 分解）。

**⭐⭐ 四（五）通道穷尽（结论表）**：

| 通道 | 典型外部机制 | 对离轴零点 | 归宿 |
|:--|:--|:--|:--|
| **线性**（加权和／矩／迹／和恒等式） | sum rule／UV–IR／null relation／covariance | **盲** | §2 饱和 ⟹ 封 |
| **二次型** | Weil 正性／Li 正性 | 可见 | RH 等价 ⟹ 旧墙 |
| **符号／惯性** | inertia／rank-迹（`V186`） | 可见（$n_-$） | 终点退回正性 ⟹ 封 |
| **逐点／时间型** | Selberg CLT／逐点 $S(T)$ | 可见 | 最坏情形 ⟺ RH ⟹ 旧墙 |
| **det／正则化行列式** | Deninger 程序 | 可见 | 缺 canonical polarization（`V145`）⟹ 封 |

⟹ $$\boxed{\text{四（五）通道全部落回既有墙}}\ \Longrightarrow\ \textbf{封}$$ ⚠️ 特别地：**同时满足六条要求的候选本档未发现** —— 因为**满足前五条者必属线性通道（从而盲），而能压制 $S(T)$ 者必然落到二次型／符号／逐点通道（从而＝旧墙）**。

**⭐ 与 `V187` 的收敛**：`V187`（机制族入口：index／inertia／RG／Lefschetz）与 `V188`（信息类型入口：线性／二次／符号／逐点／det）是**两条独立路径**，却收敛到**同一残余**：$$\boxed{\text{既非线性／index、非二次型、非符号-惯性、非逐点}\ =\ \text{`V187` §5 的"第四类不变量"}}$$ 标 OPEN，**不杀但不投入**（形式存在、实质封闭）⟹ 两个入口 → 一个残余，说明**地图在这两条线上趋于完备**。

**三条可复用筛（进工具箱）**：⭐ **饱和判据**（凡声称用全局和恒等式／sum rule／matching 约束零点者 ⟹ 线性通道 ⟹ 盲）；⭐ **涨落三层表**（典型／无条件最坏／目标⟺RH）；⭐ **四通道穷尽表**（任何未来提案的第一道分类器）。

**下一步（V189 预登记，三选）**：① 三件套固化成工具卡 ② 攻同一残余（第四类不变量）的严格定义 ③ 接受外部机制普查结束，转回 **A1／A3（Weil／Li 正性）** 本身。

### F.5ax 🧰 **工具卡：外部机制三筛 F1／F2／F3 ＋ 外部机制普查正式收束**（`V189` ✓ 2026-09-15 13:01）

**用法（固定顺序，30 秒预筛）**：$$\text{F3 通道分类}\to\text{F1 信息饱和}\to\text{F2 涨落层级}$$ 任一步判为"回归旧墙" ⟹ **立即停止，不进入推导（禁止先写数十页）**。

**🧰 F1 · 信息饱和判据**（措辞为唐先生 13:01 收紧版）：若候选**只**增加 $L_f(\mu)=\sum_\rho m_\rho f(\gamma_\rho)$ 及其有限／可控组合，而这些量**已被显式公式与算术侧确定**，则它**未产生新的独立信息**；必须**进一步**证明它能从统计量进入**支撑性质**，否则**关闭**。严格形式：$\mathcal L=\overline{\operatorname{span}}\{L_f\}$ 已饱和 ⟹ 额外线性关系是代数推论 ⟹ $\Delta I=0$ ⟹ $$\boxed{\text{线性统计量}\ \textbf{不能直接分辨}\ \text{支撑性质}}$$ ⚠️ **边界（须同时引用）**：若拥有**全部测试函数的完整无界精度数据**，$\mu$ 原则上可被恢复 ⟹ 支撑可被恢复；但那是**反演**而非**判别**，而反演所需的无界精度正是 $S(T)$ 问题本身 ⟹ F1 问的是"**是否携带新的独立信息**"，**不是**宣判"绝对不可能"。用法三步：① 列出候选增加了哪些量 ② 检查是否 ∈ $\mathcal L$ ③ 若 ∈ $\mathcal L$，要求给出**统计量 → 支撑性质**的过渡证明。

**🧰 F2 · 涨落层级判据**（候选必须自报控制哪一层）：**L1 典型** $S(T)\asymp\sqrt{\log\log T}$（**无条件**，Selberg CLT）｜**L2 无条件最坏** $S(T)=O(\log T)$（**无条件**，Littlewood 1924）｜**L3 目标最坏** $S(T)=O(\log T/\log\log T)$（**RH $\Longleftrightarrow$**，von Koch）。⟹ $$\boxed{\text{只达到 L1 或 L2 者，}\textbf{不能冒充}\ \text{RH 级控制}}$$（由 $\sqrt{\log\log T}$ 到 $\log T/\log\log T$ 的差距**不是常数因子**，是典型的"最坏情形"鸿沟）。

**🧰 F3 · 通道分类器**：$$\boxed{\text{linear}\ |\ \text{quadratic}\ |\ \text{signature/inertia}\ |\ \text{pointwise/dynamic}\ |\ \text{other}}$$ 立即检查 $\text{other}\stackrel{?}{\to}\text{linear／quadratic／pointwise}$。已知归宿：linear → **盲**（F1）｜quadratic → **Weil／Li 正性**｜signature/inertia → **终点退回正性**（`V186`）｜pointwise/dynamic → $S(T)$ **最坏**（F2）｜det → **Deninger（缺 polarization）**。

**外部机制普查正式收束（12:24–13:01）**：两条独立入口（**入口 A `V187`** 机制族：index／inertia／RG／Lefschetz／sum rule／null relation；**入口 B `V184`／`V188`** 信息类型：linear／quadratic／符号／逐点／det）**收敛**，产出**结构性地图**：$$\boxed{\text{线性统计}\to\text{信息饱和}}\quad\boxed{\text{二次／符号}\to\text{Weil／Li 正性}}\quad\boxed{\text{逐点／动态}\to S(T)\ \text{最坏}}$$（inertia 只是把第二列换成 signature 语言，**最终仍回到正性**）⟹ 真正留下的**不是**模糊的"第四类"，而是 $$\boxed{\textbf{必须找到一种既非线性统计、又非二次正性、又非逐点控制的独立信息载体}}$$

**⚠️⚠️ 严格警告（唐先生逐字，须随任何引用携带）**：$$\boxed{\text{"第四类存在"目前}\ \textbf{只是逻辑剩余类}，\ \textbf{绝不是}\ \text{候选机制}}$$ 否则易再陷循环：定义第四类 $\to$ 加足够强结构 $\to$ 结构隐含 Weil 正性 $\to$ 重新得到 RH。

**重开门槛（三条硬规则，唐先生逐字）**：**(R1)** 若新机制**不能回答"它携带的独立信息究竟是什么"**，则**不进入推导**；**(R2)** 禁止**先写数十页再判类型**（须先过 F3／F1／F2）；**(R3)** 禁止**把"第四类"当作目标对象**（只能作为判定的剩余）。

**下一步**：V189 ＝ ① → ③ 已完成（三筛固化 ＋ 普查收束）；**不再立即攻第四类**。

### F.5ay ⭐⭐⭐⭐⭐ **受约束外部搜索（F3／F1／F2 预筛）：发现 F3 之外的具名通道 S ＝ 稳定性／全正性 ⟹ ALIVE（不封）**（`V190` ✓ 2026-09-15 13:04）

**委托（唐先生）**：**"有了这些前提条件和约束后，再搜索一次所有的物理和数学模型，看看有没有适配我们研究的"** ⟹ 方法改为**用 `V189` 三筛预筛**（F3 归类 → F1 判断独立信息 → F2 判断层级），凡回归 linear／quadratic／pointwise 即停。

**① 找到并判定通道 S（ALIVE，不封）** —— **稳定性／全正性**（hyperbolicity／LP-class／TP-PF），**F3 "other" 的首个具名占位者**。**F1 通过**（见下）；**F2 不适用**（缺口按 $(d,n)$ 指标化，**不是** $T$ 的涨落尺度）。

**⭐ F1：独立信息 ＝ 支撑级（本档核心判断）**：**Bochner**（二次型通道）$f$ 正定 $\Longleftrightarrow$ $f$ 是 $\mathbb R$ 上**正测度的傅里叶变换** —— **对支撑无限制**；**Schoenberg**（本通道）$f$ 全正／Pólya 频率 $\Longleftrightarrow$ $f$ 是 $\mathbb R_{\ge0}$（**半直线**）上正测度的拉普拉斯变换 —— **支撑被限制在一侧**。⟹ $$\boxed{\text{该通道比二次型通道}\ \textbf{严格更强}：\text{它把}\ \textbf{支撑信息}\ \text{编码进去}}$$ 而支撑信息正是 F1 说"线性统计量**不能直接分辨**"的那一类 ⟹ **F1 通过** ✓✓✓（现代等价形式：变差缩减 variation diminishing／**全子式非负** —— 非有限阶、非二次型）。

**② 关键事实链与近期真进展**：**Pólya (1927)**：$(-1+4z^2)\Lambda(\frac12+z)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n}$，$J_\gamma^{d,n}(x)=\sum_{j=0}^{d}\binom dj\gamma(n+j)x^j$ ⟹ $$\boxed{\text{RH}\ \Longleftrightarrow\ \textbf{全部}\ J_\gamma^{d,n}\ \text{双曲（全实根）}}$$ **Griffin–Ono–Rolen–Zagier（PNAS 2019，arXiv:1902.07321，被引 180+）**：(i) 对**每个** $d\ge1$ 存在 $N(d)$ 使 $n\ge N(d)$ 时双曲 ✓（"高 $n$ 全成立"）(ii) 对 $1\le d\le8$ **全部** $n\ge0$ 双曲 ✓（此前最好 $d\le3$）(iii) 方法：重正化 Jensen 多项式 $\to$ **Hermite 多项式** $H_d$ ⟹ 大 $n$ 双曲 (iv) 数值：$d\le10^{20}$ 双曲 (v) 作者自述**未发明新技术**，只是**复活了 Jensen–Pólya 这条被认为已死的路线**。同通道经典：Csordas–Norfolk–Varga（Turán 不等式；解 Pólya 58 年问题，对应 $d=2$）｜Newman／Cardon（Fourier transforms with only real zeros）。

**③ ⭐⭐ 缺口结构与新轴**：RH ⟺ 所有 $(d,n)$ 无例外；已知**高 $n$ 全成立**（所有 $d$）＋**小 $d$ 全成立**（$d\le8$，全部 $n$）⟹ 缺口 ＝ **中等／大 $d$ 且小 $n$ 的例外集**；⚠️ **对每个 $d$ 只有有限多 $n$ 例外** ⟹ 缺口是"**每度有限的例外集族**"，**不是渐近墙** ⟹ F2 三层阶梯**不适用**，本通道有**自己的缺口几何（$d$ vs $n$）** ✓✓。

**④ 同通道现代工具与一刀**：**(a) Borcea–Brändén** 稳定性保持算子分类（用**算子 symbol** 判保稳定／保实根）⟹ 可用于构造或否定保持算子 ✓。**(b)** ⚠️ **Belton–Guillot–Khare–Putinar（2021/22）**：在无限全序集上（存在 TP$_2$ 核时）**TP 保持算子只有正齐次（positive homothety）** ⟹ **一刀**：若坚持**无限阶全正**保持算子，则保持类过窄（只有缩放）⟹ **该子通道不可用** ⟹ 要用的应是**稳定性（hyperbolicity）保持算子**（Borcea–Brändén，类很丰富），**而非**无限阶 TP 保持算子。

**⑤ 其余候选**：**2026 综述** arXiv:2602.04022（《The Riemann Hypothesis: Past, Present and a Letter to Riemann》）的原创贡献是**极值化 Weil 二次型**逼近零点 ⟹ **二次型通道 ⟹ 回归，关闭**（仅登记）。**Pólya–Schur–Lax（AIM 2007）** ⟹ 领域地图。**Newman／Cardon、Csordas–Norfolk–Varga** ⟹ 通道 S 工具。

**⑥ 三条风险（必须随本档携带）**：**(R-a)** Pólya 1927 是 **RH 等价改写** ⟹ 按 `V149` 教训，**等价改写不自动带来新输入**；**(R-b)** 正面判断（独立信息＝支撑级）**尚未证明能被无条件确立** —— **携带独立信息 ≠ 能被无条件确立**；**(R-c)** 缺口（中等 $d$、小 $n$）与**低零点／小高度**可能**同源** ⟹ 可能隐藏同一核心难点。

**⭐ R1 所要求的回答**：$$\boxed{\text{它携带的独立信息}\ =\ \textbf{支撑级信息}：\text{根集落在实轴上}\Longleftrightarrow\text{表示测度的支撑被限制在一侧／实轴}\ ——\ \text{严格强于"正定"}}$$

**下一步（V191 预登记，二选，均须先过 R1）**：① **结构性**：证明"中等 $d$、小 $n$ 例外集为空"需要**何量级输入**？（等价于低零点／Weil 正性 ⟹ 封；否则这是**第一个定位在 $(d,n)$ 轴上的新缺口**）② **构造性**：用 **Borcea–Brändén symbol 判据**构造**算术可实现**的稳定性保持算子，把"已知实根"起点推向 $\xi$（⚠️ 若把目标写进 symbol 即走私 ⟹ 按 `V188` 判据自检）。

### F.5az ⭐⭐⭐⭐⭐ ⚠️**勘误（`V193` ✓）**：本节所引 **MDPI Mathematics 14(11) 1884（Planat）存在实质性归一化错误**（其 $M_n=\int\Phi_1u^{2n}du$ 相对 GORZ 的 $\gamma(n)$ **漏掉一个随 $n$ 变化的 $n!$ 因子**）⟹ 其三条结论（$n\ge C_0^\infty d^4$／finite strip $\equiv$ RH／interlacing-lift vacuity）**一律作废、不得引用**；**S 通道封闭理由改用 `V191` 等价性**，**不依赖该文**。

### F.5az ⭐⭐⭐⭐⭐ **V191-① 的回答：NO（定理级）—— 剩余区域的双曲性不可能由严格弱于 RH 的命题推出；F1 升级为两问制**（`V191` ✓ 2026-09-15 13:08）

**委托（唐先生 13:08）**：把 S 通道升级为 ALIVE，但 V191-① 必须做且**比"需要什么量级输入"更严格**：**中/大 $d$、小 $n$ 的全部双曲性，是否能由一个明显弱于 RH 的有限算术命题推出？** 同时修正逻辑点（"每个 $d$ 有限例外"**不**蕴含统一 $(D,N)$，因 $N(d)$ 可随 $d$ 增长）并给出判死标准（若"剩余全双曲"$\Longrightarrow$ Weil/Li 正性 $\Longrightarrow$ **S channel DEAD**）；并指出真正该追的量是 **Hermite 稳定性到 finite-$n$ 的距离** $\|\widehat J-H_d\|<\operatorname{dist}(H_d,\partial\mathcal H_d)$。

**⭐ ① 答案 ＝ NO，且为定理级（零外部依赖）**：Pólya 1927：RH $\iff$ **全部** $J_\gamma^{d,n}$ 双曲；GORZ 2019（已证）：$\forall d\ \exists N(d):n\ge N(d)\Rightarrow$ 双曲，且 $1\le d\le8$ 对**全部** $n\ge0$ 双曲 ⟹ $$\boxed{\text{RH}\iff\bigl[\text{剩余区域}\{d\ge9,\ n<N(d)\}\ \text{全双曲}\bigr]}$$ ⟹ **剩余区域陈述强度恰等于 RH** ⟹ 若命题 $P$ **严格弱于** RH 却能推出它，则 $P\Rightarrow$ RH，**矛盾** ⟹ $$\boxed{\textbf{NO}}$$ ⚠️ 本论证**只用 Pólya ＋ GORZ**，不需任何关于剩余区内部结构的假设 ⟹ 强度极高。

**② 通道 S 重新定位**：不是"**弱输入载体**"，而是"**强度恰为 RH 的等价路线**"；其唯一可能的"新"在于**几何**（$(d,n)$ 轴 ＋ Hermite 极限机制），而**不在于更弱的输入**。

**③ 逻辑修正采纳 ＋ 机制**：$N(d)$ 可随 $d$ 增长 ⟹ 无统一 $(D,N)$ ✓；机制：$H_d$ 根间距 $\asymp\pi/\sqrt d$（根散布 $[-2\sqrt d,2\sqrt d]$）⟹ $\operatorname{dist}(H_d,\partial\mathcal H_d)\asymp d^{-1/2}$ **随 $d$ 衰减** ⟹ 一致推出双曲性需误差**一致地** $\ll d^{-1/2}$，$d$ 越大越难 ⟹ $$\boxed{N(d)\to\infty\ \text{是机制必然}}$$

**④ 定量判据与自证**：$\varepsilon_{d,n}:=\|\widehat J_\gamma^{d,n}-H_d\|<\delta_d:=\operatorname{dist}(H_d,\partial\mathcal H_d)\Longrightarrow$ 双曲 ✓；⚠️ **自证**：若对全部 $(d,n)\in\mathcal R$ 成立 ⟹ 由 §① 得 **RH** ⟹ 该不等式**不是弱输入**，而是 **RH 的充分判据**（"可攻"$\neq$"更弱"）。

**⑤ 外部证据（⚠️ 可信度中等，红旗待核）**：**MDPI Mathematics 14(11) 1884**（2026）《Asymptotic Hyperbolicity of Jensen Polynomials and the Finite-Strip Obstruction to the Riemann Hypothesis》取到片段给出：(i) **asymptotic regime $n\ge C_0^\infty d^4$**：$J_{d,n}^\gamma$ **双曲、无条件**（Theorem 3）✓；(ii) **finite strip $0\le n<C_0^\infty d^4,\ d\ge9$：等价于 RH**，且被称"**一切已知局部与归纳机制同时失效处**" ✓✓；(iii) **Theorem 9（interlacing-lift vacuity）**：该区域内 $J_{d-1,n+1}^\gamma$ **永不双曲**（$N_-\le1\ll d-1$）⟹ **归纳提升无立足点** ✓✓✓。⚠️ **红旗**：该文 Remark 3 称 $J_{2,n}^\gamma$"对每个 $n\ge0$ 都有非实根"，与 GORZ 已证 $d\le8$ 对全部 $n$ 双曲**表面冲突** ⟹ 可能归一化约定不同，亦可能有误 ⟹ **核对前不可作依据**。⭐ 三条与 §① 同向，但 §① **不依赖**该文。

**⑥ ⭐ F1 判据修订（本档最重要方法论产出）**：`V190` 给 F1 的回答（"通道 S 携带**支撑级信息**，严格强于 Bochner"）**在语义上正确**，但**不足以**支撑"弱输入"期望 ⟹ $$\boxed{\text{F1（修订版）＝两问}\：\text{① 语义问：是否携带}\ \textbf{新的独立信息}？\quad\text{② 强度问：该信息}\ \textbf{能否被无条件确立}\ \text{且}\ \textbf{严格弱于}\ \text{RH}？}$$ 两问都过才算"弱输入载体"；通道 S 过①、**过不了②**（§① 定理级）⟹ 降级为"**等价路线**"。⭐ 一句话：$$\boxed{\text{信息更多}\ \neq\ \text{更易证}}$$

**下一步（V192 预登记，三选）**：① **核**（低成本、必要）：核 MDPI 与 GORZ 原文，确认 $n\ge C_0^\infty d^4$ 的无条件性、finite strip 的等价性、interlacing-lift vacuity，并解 $d=2$ 红旗 —— 三条若成立 ⟹ 通道 S 的"路线价值"也被压低（**所有已知机制在该区域同时失效**）⟹ 可**封**；② 若①确认 ⟹ **封**，并把"**$d$ vs $n$ 轴**"登记为**已探明的第六类缺口形态**（与 $T$ 轴缺口并列）；③ 转回主线 **A1／A3（Weil／Li 正性）**。

### F.5ba ⭐⭐⭐⭐⭐ **Hedenmalm 审计 ＋ 纵坐标退化封印（谱实现族一次性封）＋ F4（Representation-Change Criterion）上线**（`V192` ✓ 2026-09-15 13:10）

**委托（唐先生）**：第三轮搜索（以"**独立信息载体**"为第一筛选条件）；提出 **F4 ＝ Representation-Change Criterion（六条）**；给出硬问题：**Hedenmalm 的 $\mathbf E=\prod_p\mathbf E^{\langle p\rangle}$ ＋ 补偿质量，能否在不假设 RH 下构造出同时依赖 $(\beta,\gamma)$ 的算术二元对象？若最终仍"只能看到 $\gamma$"，则干净封死。**

**⭐ ① 关键翻译（标准事实，本档核心）**：$\Xi(t):=\xi(\frac12+it)$，**RH $\iff$ $\Xi$ 全实根**（经典，即 `V190` 的 LP 表述）。设 $\Xi$ 零点 $t_0=x+iy$：$\xi(\frac12+i(x+iy))=\xi((\frac12-y)+ix)=0$ ⟹ $$\boxed{\Xi\ \text{的非实零点}\iff\xi\ \text{的离轴零点}\ (\beta=\tfrac12-y,\ \gamma=x)}$$ $\Xi$ 对实 $t$ 取实值 ⟹ 非实零点成共轭对 $x\pm iy$；⚠️ 一次**离轴对** $\{\rho,1-\bar\rho\}$ 给出 $\xi$ 的**两个**零点 $\beta=\frac12\mp y$，且 $$\boxed{\textbf{两者共享同一纵坐标}\ \gamma=x}$$ ⟹ 在"**纵坐标多重集**" $\{\gamma_\rho\}$ 语言里，**离轴对 ＝ 一个二重（退化）点，在线零点 ＝ 单点** ⟹ $$\boxed{\text{RH}\iff\text{纵坐标谱无"非本质退化"}}$$

**⭐ ② 硬问题的答案 ＝ 是的，只能看到 $\gamma$，且原因是结构性的**：Hedenmalm 把 $\Xi$ 的**实根**实现为边值问题特征值（$LDu+\alpha Lu=0$），而 $\Xi(x)=\int_0^\infty\Theta_{00}(it^2)t^{ix}\frac{dt}t$ 只涉及 $\Xi$ 本身 ⟹ 按 ①，"$\Xi$ 的**实**根"**只**对应 $\beta=\frac12$ 的零点；离轴对落在 $\Xi$ 的**非实**零点上 ⟹ **该构造取不到** ⟹ 它看到的是**只依赖 $\gamma$** 的对象，**结构上不可能**给出同时依赖 $(\beta,\gamma)$ 的算术二元对象 —— **与是否假设 RH 无关** ⟹ **这正是"干净封死"**（不是"还没做出来"，而是**对象类型不允许**）。

**⭐ ③ 谱实现族的封印（更一般；本档最重要结构性结论）**：设某"谱实现" $T$ 是**实谱**（自伴／Hilbert–Pólya 型），$\operatorname{Spec}(T)=\{\gamma_\rho\}$；⚠️ $\gamma_\rho=\operatorname{Im}\rho$ **本就为实**，故"谱为实"**对 $\beta$ 零约束** ⟹ **单纯构造自伴算子不触及 RH**；由 ①，$\beta$ 在该语言里**只能经"退化／重数"进入** ⟹ $$\boxed{\text{整个谱实现族的}\ \beta\text{-内容}\ =\ \textbf{退化计数}\ =\ \text{“简单零点／互异零点”问题}\ (N_0^s／N_d)}$$ ⭐ 而 $N_0^s／N_d$ **正是 `V184`／`V185` 审过的 Alpöge–Furman 2026 的主题**，其带宽一上限**已被证明**（0.6818287）⟹ $$\boxed{\text{谱实现族}\ \textbf{不是}\text{第四类};\ \text{它是同一堵墙的}\textbf{A 侧}}$$

**④ compensation 结构的 F1 判定（⚠️ 待核原文）**：$\Theta_{00}(it^2)=t^{1/2}\mathbf E h_{00}(t)$，$\mathbf E=\prod_p\mathbf E^{\langle p\rangle}$，$\mathbf E^{\langle p\rangle}f(t)=\sum_{k\ge0}f(p^kt)$ ⟹ **素数分解的膨胀算子是真正算术来源**（本晚候选中罕见）✓✓；但 "$h_{00}$ 零积分 ⟹ $\mathbf E h_{00}$ 在 $t\ne0$ 为正却须产生补偿性负点质量" ＝ **显式公式的 archimedean 补偿在算子语言中的形式**（素数侧求和 ↔ archimedean 补偿）⟹ 按 F1（`V188` 饱和定理）**不提供新的独立信息** ⚠️✓（判定基于转述，**须核原文**）。

**⑤ F4 采纳（六条）＋ 逐条打分**：$$\boxed{\mathcal R\ \text{须满足}：①\text{非线性}\ ②\text{非显式公式换坐标}\ ③\text{算术侧可独立构造}\ ④\text{对}\beta\text{敏感}\ ⑤\text{非}Q\succeq0\text{重编码}\ ⑥\text{定量 localization}}$$ 打分：**Hedenmalm** $\pm/\pm/\checkmark/\times/\pm/\checkmark$ ⟹ **死于④**（§②）｜**逆谱几何（Hayashi–Sakai）** $\checkmark/\checkmark/\times/\checkmark/\checkmark/\checkmark$ ⟹ **只缺③ arithmetic origin**｜sum rule／covariance（DEAD，`V188`）｜inertia（DEAD，`V186`）｜RG 收缩（DEAD）｜**RMT rigidity（Laguerre）＝统计型 ⟹ DEAD**（`V188`）｜self-adjoint／Hilbert–Pólya 类（**DEAD，§③ 封印**）。⭐ **四筛最终形态**：$$\text{F3 通道分类}\to\text{F1 两问（语义／强度）}\to\text{F2 涨落层级}\to\textbf{F4 表示变换}$$

**下一步（V193 预登记，三选）**：① **核** Hedenmalm 原文四句话（$\Theta_{00}$／$\mathbf E$／零积分／负点质量），确认 §④ 的 F1 判定（若其补偿结构与显式公式**不完全同构**，该资产值得单独立档）② **逆谱几何的③问**："能否把 $\mathcal R$（逆谱变换）的**输入**从零点测度换成素数侧数据？"——若不能 ⟹ 与一切几何侧候选同命（缺同一座桥）；若能 ⟹ **本晚第一个真正的新入口** ③ **收束**：本晚已连关 S 线／N31／线性 Weyl 律／inertia／cancellation／null-relation／通道 S（`V191`）／**谱实现族（`V192`）** ⟹ 转回 **A1／A3**

### F.5bb ⭐⭐⭐⭐⭐ **V193：Planat 剔除 ＋ 算术-逆谱几何审计（二分封闭）＋ 自查勘误 ＋ 第三次收敛**（`V193` ✓ 2026-09-15 13:14）

**① Planat／MDPI 归一化错误确认 ⟹ 三条结论剔除、我方引用作废**：GORZ 定义 $(-1+4z^2)\Lambda(\frac12+z)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n}$（级数中 $1/n!$ **显式**）；Planat 用 $M_n=\int_0^\infty\Phi_1(u)u^{2n}du$（**无** $n!$ 因子）⟹ 两族相差一个**随 $n$ 变化**的因子（量级 $n!/(2n)!$）⟹ **定义的 Jensen 族不同**；其 $d=2$ 的论证（$\Phi_1\ge0$ ＋ Cauchy–Schwarz $\Rightarrow M_{n+1}^2<M_nM_{n+2}\Rightarrow\Delta<0$，故永不双曲）与 GORZ 已证 $d\le8$ 全 $n$ 双曲**定义层面冲突** ⟹ 其 $n\ge Cd^4$／finite strip $\equiv$ RH／interlacing-lift vacuity **均不可采信**。⚠️ **纪律升级**：$$\boxed{\text{引用外部结果前，先做}\ \textbf{定义级核对}（归一化／因子／指标约定）}$$

**② S 通道 CLOSED，理由正确**：封闭理由**不是** "Planat 的 obstruction"，而是 `V191` 的等价性：$$\text{RH}\iff[\text{剩余区}\{d\ge9,n<N(d)\}\ \text{全双曲}]$$ ⟹ 该通道**强度恰等于 RH** ⟹ 不可能提供"弱于 RH 的输入"。⭐ 保留"**$d$ vs $n$ 二维缺口**"为**地图上的缺口形态**（与 $T$-轴缺口并列），**不作**独立机制。

**③ 算术-逆谱几何审计（V193-② 窄问题）**：$\mathcal R$ 链条 $$\boxed{\{\varepsilon_n\}\xrightarrow{\mathcal D}f\xrightarrow{\langle m|\cdot|n\rangle}F\xrightarrow{|m-n|=d}W_d\xrightarrow{\sum d^p}M_p}$$ 第一步是**谱 $\to$ 势**的**逆谱问题**，输入必须是**离散有序谱** ⟹ 素数侧自然对象 $\{\log p\}$ 虽也是离散有序序列，但 $$\boxed{\mathcal R(\{\log p\})\neq\mathcal R(\{\gamma_n\})}$$ ⟹ 须有算术 intertwiner $\mathcal A_{\mathbb P\to\zeta}$ ＝ **缺的桥** ⟹ **直接替换：NO**。唯一已知 intertwiner ＝ **显式公式**，但其内容已被 `V188` 饱和定理覆盖，且由 **F4 ②**：$$\boxed{\text{显式公式}+\mathcal R=\textbf{纯表示变换}}\Longrightarrow\text{杀}$$ ⟹ 旧工作（Wu–Sprung／Ramani 等）分别造出 $V_\zeta$ 与 $V_{\mathbb P}$ 但**未证明二者相同、无桥** ⟹ 判 **BRIDGE-ONLY / ALIVE BUT UNINSTANTIATED**。

**⭐⭐ ④ 二分封闭（本档核心）**：设 $\mathcal R_{\rm arith}$ 存在、产出 $\operatorname{Spec}(H_0+f)=\{\gamma_n\}$，问 $\beta$ 信息从何而来？**(i) 目标为自伴（实谱）实现**：由 `V192` 封印，$\beta$ **只能经退化／重数**进入 ⟹ 该支 $\beta$-内容 ＝ 简单／互异零点计数（$N_0^s／N_d$）⟹ 撞**已证上限 0.6818287** ⟹ **封**。**(ii) 目标为非自伴但声称实谱**：则"实性"本身 ＝ **RH 强度** ⟹ **无免费输入** ⟹ **封**。⟹ $$\boxed{\text{两支皆封};\ \text{唯一逃生 ＝ 第三支}}$$（算术对象，其 $\beta$-敏感性**既非重数、也非"实性声称"**）。

**⭐⭐⭐ ⑤ 第三次收敛**：`V187`（机制族入口）／`V188`（信息类型入口）／**本档（算术-逆谱几何入口）** 三路 ⟹ 同一残余：$$\boxed{\text{“}\beta\text{-敏感、但既非重数／指标、也非二次型、也非逐点}\text{的算术对象”}}$$ ⚠️ 标 **OPEN，不杀、不投入**（**不是**候选机制，只是判定的剩余）。

**⚠️⚠️ ⑥ 自查勘误（F1 措辞级）**：`V188`／`V192` 的"线性／求和／null-relation 通道对 $\beta$ **结构性盲**"**措辞过强** ✅ **正确表述**：线性通道**饱和**（不提供新的独立信息），但其**提取**需要**一致性／无界精度** ⟹ 障碍是**定量-一致性**，**不是盲**。根源：$\gamma_\rho=\frac{\rho-1/2}{i}=\gamma-i(\beta-\frac12)$ **为复数**，**显式公式的线性统计量确实编码 $\beta$**。⚠️ `V187` 的"signature／trace 中性"**仍成立**（那是**特定聚合泛函**的中性，≠ 泛函族盲）。⟹ **不影响任何结论**，只修正**理由的表述**；并印证 `V188` 原有 caveat（"饱和 $\neq$ 无用；反演需无界精度"）本就在 —— 是我压缩转述时丢了"**直接**"二字。

**下一步（V194 预登记，三选）**：① **收束**：本晚连关 9 项 ＋ 三入口收敛 ⟹ 转回 **A1／A3（Weil／Li 正性）** ② **工具卡收官**：F1 修订版（两问）＋F4＋二分封闭＋饱和判据＋涨落三层表＋四通道穷尽表 → **单页预筛卡** ③ 若攻第四类：按 R1 先给"第三支"**严格定义**并自检（预计回到二次型／重数通道）

### F.5bc 🧰 **V194：第四类机制预筛卡（总卡，取代 `V189`）＋ 二分封闭 Lemma ＋ 两条纪律升级**（`V194` ✓ 2026-09-15 13:19）

**委托（唐先生）**：同意 **② → ①**；**V194 不再扩展候选**，**"先把筛选器压缩成一张真正可执行的总卡，然后再回 A1／A3"**；理由：**"现在最有价值的不是再找一个名字，而是证明以后任何'第四类'候选都无法通过偷换信息类型逃过已建立的封闭条件。"**

**§0 用法（三步 $<2$ 分钟；任一步失败即停，禁止先写推导）**：$$\text{步 1 定性（F1 两问）}\to\text{步 2 结构（F4 六条）}\to\text{步 3 量化（三层涨落）}$$ 并对四通道表归类；凡引用外部结果者先过**定义级核对**（§7 六项）。

**I. F1 两问**：$$\boxed{\mathrm{F1a}:\ \text{是否携带显式公式／Weil 型信息}\textbf{之外}\text{的新信息}？\qquad \mathrm{F1b}:\ \text{能否以}\textbf{严格弱于 RH}\text{的输入}\textbf{无条件}\text{证明}？}$$ 2×2：**否／任意 ⟹ REPACKAGED**｜**是／否 ⟹ RH-EQUIVALENT / TOO STRONG**｜**否／是 ⟹ USEFUL BUT IRRELEVANT**｜$$\boxed{\textbf{是／是 ⟹ 真正候选}}$$

**II. F4 六条**：$$\boxed{\mathrm{F4.1}\ \text{非线性／非平凡变换};\ \mathrm{F4.2}\ \text{非显式公式换坐标};\ \mathrm{F4.3}\ \text{算术可直接构造};\ \mathrm{F4.4}\ \textbf{对}\ \beta-\tfrac12\ \textbf{有实质敏感性};\ \mathrm{F4.5}\ \text{非}\ Q\succeq0\ \text{等价};\ \mathrm{F4.6}\ \text{定量定位而非仅统计}}$$ ⭐ **F4.4 为本轮最重要升级**（因 $\gamma_\rho=\gamma-i(\beta-\tfrac12)$）⟹ $$\boxed{\text{information blindness}\ \neq\ \text{effective extractability}}$$ 正确障碍：线性信息**包含** $\beta$，但从**有限／可控输入**中**稳定提取** $\beta$ 困难。⚠️ **此后一律使用"可提取性"，不再使用"盲"**。

**III. 饱和判据**：若候选只产生 $L_f(\mu_\zeta)=\sum_\rho m_\rho f(\rho)$ 且 $L_f$ 已被显式公式完全确定 ⟹ **未增加新的信息通道**；⚠️ **不得**写成 "linear $\Rightarrow$ $\beta$-blind"；正确：$$\boxed{\text{linear}\Rightarrow\text{information-saturated}}$$ 唯一出路：进一步给出**稳定、有限复杂度、定量可逆的 support localization**。

**IV. 三层涨落**：$$\boxed{\text{typical}\ S(T)\sim\sqrt{\log\log T}\ \text{（无条件）}\ |\ \text{uncond. worst}\ O(\log T)\ \text{（无条件）}\ |\ \textbf{RH-level}\ O(\log T/\log\log T)\iff\text{RH}}$$ ⟹ RMT rigidity／pair correlation／variance／CLT 若只控 typical ⟹ 降级为 $$\boxed{\text{statistical improvement}}$$（**非** RH mechanism）。

**V. 四通道穷尽表 ＋ 第四类严格定义**：| 通道 | 能处理 | 状态 |｜Linear／trace｜全部显式公式线性信息｜**SATURATED**｜｜Quadratic／positivity｜Weil 型二次型、部分零点比例｜**A1／A3 主线**｜｜Signature／inertia｜正负惯性、部分在线比例｜**67.2% ceiling（0.6818287）**｜｜Pointwise／dynamic｜单点定位、最强局部信息｜**唯一真正未关闭**｜ ⟹ 收窄为 $$\boxed{\textbf{第四类}=\text{非二次型、非惯性、非纯线性，}\textbf{且能逐点／局部定位}\ \beta}$$ ⚠️ 并行携带 `V189` 警告：**"第四类存在"只是逻辑剩余类，绝不是候选机制**。

**VI. 二分封闭 Lemma**：设 $\mathcal A_{\mathbb P}\xrightarrow{\mathcal R}H$ 且声称 $\operatorname{Spec}(H)\subset\mathbb R$。**支 A（自伴）**：实谱自动成立（无信息）⟹ $\beta$ 只能经 $(\gamma,\text{multiplicity})$ 进入 ⟹ 落入零点比例／重数通道 ⟹ 撞 **0.6818287**。**支 B（非自伴但声称谱全实）**：实谱本身即极强谱定位命题；若足以推出全部零点实 ⟹ real spectrum $\Rightarrow$ RH ⟹ **无免费实谱**。⟹ $$\boxed{\text{自伴支}\cup\text{非自伴实谱支}=\textbf{全部封闭}}$$ 唯一剩余形态：$$\boxed{\mathcal A_{\mathbb P}\xrightarrow{\mathcal R}\mathcal X}$$ 其中 $\mathcal X$ **不是先验实谱对象**，却能从算术内部产生对 $\beta-\tfrac12$ 的**非退化敏感性**。

**VII. ⚠️ 纪律：Definition-level audit before theorem-level use**（六项，逐项记录）：$$\boxed{1.\text{对象定义一致}\ 2.\text{归一化一致}\ 3.\text{指标依赖因子一致}\ 4.\text{权重是否随指标变化}\ 5.\text{适用域一致}\ 6.\text{之后才谈定理结论}}$$ ⭐ Planat 事故为典型：**定理方向漂亮，但对象已不是 GORZ 的 Jensen polynomial**；本条为**实质性成果**，把"引用风险"从判断力问题变为**可执行清单**。

**VIII. 回 A1／A3 的唯一问题（V195 立项）**：主线压成 $$\boxed{\text{Weil positivity}\longleftrightarrow\text{Li positivity}}$$ 但**不再问**"能否找到另一个正性判据"；**新问题**：$$\boxed{\textbf{能否把 Weil／Li 正性从"全局无限族"降成一个可证明的}\textbf{局部结构条件}？}$$ 即求严格 $P_{\rm local}$：$$P_{\rm local}\Longrightarrow P_{\rm Weil}\iff\text{RH}\qquad\text{且}\ P_{\rm local}\ \text{可由}\ \textbf{严格弱于 RH 的算术事实}\ \text{推出}$$ 附加约束：$P_{\rm local}$ **不能只是 Weil 二次型的坐标表达**（否则 $\mathrm{F1a}=$ 否 ⟹ **REPACKAGED**）。

**V195 预登记（唯一方向）**：$$\textbf{Local Positivity Audit}：\text{攻}\ \boxed{\text{local arithmetic constraint}\Longrightarrow\text{global Weil／Li positivity}}$$ 第一步（按 R1 与 F1）：先给 $P_{\rm local}$ **严格定义**并自检两问；⚠️ 任一为否 ⟹ 按本卡**立即停**，不进入推导。

### F.5bd ⭐⭐⭐⭐⭐ **V195：搜索生成器重置（机制优先）—— 【第一轮禁用 F1–F4】＋ 三个刚性引擎**（`V195` ✓ 2026-09-15 13:22）

**委托（唐先生）**：**"我刚才虽然换了候选对象，但没有换搜索生成器"** —— 仍从"RH 已知障碍 → 分类 → 找绕开障碍的通道"出发 ⟹ 必然把新东西投影回四通道再宣布撞墙；**"这不是你要的'清空'"**。指示：$$\boxed{\text{不从 RH 出发找机制；先从数学／物理中找"异常强的机制"，再问它能否落到 RH}}$$ **第一轮只允许六类机制（A 一致性闭包／B 非线性吸引子／C 动力奇点／D 全球化障碍／E 约束传播／F 缺陷-拓扑荷）进入，且"暂时全部不允许套 F1–F4"**；**先不碰 RH**，先答纯数学问题"它为什么能产生全局刚性？"；三优先：**I 非线性算术吸引子／II 算术全球化障碍（排第一）／III 算术动力奇点**。

**§0 生成器重置**：旧生成器**停用**（四通道表是**障碍的投影**，当生成器用必投影回去 ⟹ "又撞墙"是**搜索结构的产物**）；新生成器：$$\boxed{\text{Physics／Math mechanism}\to\text{abstract mechanism}\to\text{arithmetic realization}\to\text{RH relevance}}$$ **本轮硬规则**：$$\boxed{\text{第一轮}\ \textbf{禁用 F1--F4}}$$ `V194` 卡**不作废但降级为后阶段过滤器**。

**§1 ⭐ 机制 II（全球化障碍，排第一）**：抽象：局部态 $\{x_i\}$ on $U_i$，重叠一致性 $x_i|_{U_i\cap U_j}=T_{ij}(x_j|_{U_i\cap U_j})$；三通道 $T_{AB}T_{BC}T_{CA}=\mathrm{id}$；⚠️ **关键限定**：不是"存在 compatible sequence"（**太弱**），而是 **transition cocycle／obstruction class**。**⭐ 纯数学引擎（它为什么产生全局刚性）**：**(i) 障碍类的离散性／量子化** —— $[T]\in H^1(\mathfrak U;\mathcal A)$（Čech）等，当取值于**离散群／格**时，"$[T]=0$"是**开条件** ⟹ **不可形变 ⟹ 刚性**；**(ii) 约束过定**（约束数 > 自由度 ⟹ 全局解集稀疏／唯一）。⟹ 机制 II 的独特处：刚性来自**量子化**，**不是**正性／实谱／逐点控制。**类型区别**：机制 II ＝ **discrete／quantized obstruction class**，**不落在任何已封通道的类型里**（类型层面观察，**≠** "通过了 F1–F4"）。**算术原材料（只列不判）**：$p$-局部因子｜功能方程对合 $s\leftrightarrow1-s$（离轴对正是其轨道）｜adelic 拼接｜经典 $\mathrm{Br}$／$\mathrm{Sha}$／非交换 $H^1$｜本项目 `V176`–`V180` 的 $H^1(C_2,K^\times)$ 触点。**⚠️ 缺的一环（诚实，不判死）**：$$\boxed{\text{transition map}\ T\ \text{在算术情形}\ \textbf{是什么} —— \text{目前}\ \textbf{没有候选}}$$ 三种待挖形态：(i) 沿 $s\leftrightarrow1-s$ 的过渡；(ii) 沿 $p$ 与 $\infty$ 的局部化过渡；(iii) 沿高度／尺度的过渡（archimedean 相关）；**若最终被证＝显式公式重述则退化，但按指示在算到最后前不杀**。

**§2 机制 I（非线性吸引子）**：抽象 $(\mathcal N f)(x)=\frac{\sum_pW_p(x)F_p[f](x)}{\sum_pW_p(x)}$，$f_{n+1}=\mathcal Nf_n$，目标唯一 $f_*$ ＋ $\|\mathcal N^nf-f_*\|\le Ce^{-cn}$。**⭐ 引擎 ＝ Birkhoff--Hopf 射影度量收缩**：$d_{\rm proj}(\mathcal Nf,\mathcal Ng)\le\kappa d_{\rm proj}(f,g)$，$\kappa<1$ ⟹ **唯一不变 profile ＋ 与初值无关 ＝ 刚性**；实现条件 ＝ **锥不变性 ＋ 有界畸变**（RPF 正统机制）。**⭐ 算术原材料：现成实例** $$\boxed{\text{Mayer／Gauss 转移算子的 Fredholm 行列式}\ =\ \zeta}$$（经典；具体形式待核）⟹ 在本实例中"profile"是函数，共振／零点＝ζ 的零点 ⟹ RH 问题变成**"共振位置"**。

**§3 机制 III（动力奇点）**：抽象：**零点 ≠ eigenvalue；零点 ＝ 动力学奇点**（Loschmidt 幅／累积相位的非解析点）。**⭐ 引擎**：单调／守恒量 ＋ **反射不变性** ⟹ 奇点轨迹落入**不动集**：若 $\mathcal E[X_s]=\mathcal E[X_{1-s}]$ 且 $\mathcal E$ 在轴外**严格分离** ⟹ $\Re\sigma=0$；**缺的输入 ＝ 一个反射不变、且在轴外严格分离的量**。⚠️ **风险（记录不判死）**：`V147` T1 曾证"全预序＋保序对合 ⟹ $x\sim\iota(x)$ ⟹ 无严格单边律"；但此处需**实值分离量**而非预序 ⟹ 不完全同型。

**§4 Backlog**：**D ＝ 机制 II**；**E 约束传播**（有限局部 ⟹ 无限刚性；紧性／König ⟹ 有限见证）；**F 缺陷／拓扑荷**（局部缺陷 ⟹ 全局不变量 ⟹ 禁忌扇区）；⚠️ E／F 与 II 的"量子化"引擎亲缘，建议并入 II。

**§5 Phase-1 纯数学答案表**：| 机制 | 刚性引擎 | 算术现成实例 |｜**II**｜**障碍类量子化**（＋过定）｜$\mathrm{Br}$／$\mathrm{Sha}$／非交换 $H^1$；本项目 $H^1(C_2,K^\times)$｜｜**I**｜**Birkhoff--Hopf 射影收缩**＋锥不变／有界畸变｜⭐ **Mayer／Gauss 转移算子，$\det=\zeta$**｜｜**III**｜**反射不变的严格分离量** ⟹ 奇点入不动集｜无现成（最薄）｜ ⭐ 机制 I 已有把 ζ 作为行列式的经典转移算子实例 ⟹ **不是无源之水**。

**§6 Phase-2 判据**：**成功** ＝ 机制能对**纯算术对象**（$p,\ p^k,\ \Lambda(n),\ \log p$）给出**局部定义**，并让全局化／不动点／奇点约束产生对 $\beta-\frac12$ 的**非平凡结论**；**失败** ＝ 该机制的过渡映射／收缩／守恒量**必然**退化为显式公式／字符 holonomy／有限逆极限。⚠️ 纪律：**在算到最后之前不能杀**；也不得**提前**宣布"可能又是延拓压力的重包装"。

**下一步（V196 预登记，唯一动作）**：**Mechanism II · Phase 1-b**：从零构造算术情形的 **transition maps／cocycle**，再算 **obstruction class**；三条待验形态（(i) 沿 $s\leftrightarrow1-s$；(ii) 沿 $p$ 与 $\infty$ 的局部化；(iii) 沿高度／尺度）；**唯一目标** ＝ 给出 $T$ 的**显式局部定义**并判断 $[T]$ 是否取值于**离散集合**（离散 ⟹ 刚性引擎可用）。

### F.5be ⭐⭐⭐⭐⭐ **V196：机制 II · Phase-1-b —— canonical transition structure 与 obstruction（五步已执行）**（`V196` ✓ 2026-09-15 13:25）

**委托（唐先生）**：**"V196 就攻 II，严格按 Phase-1-b，不碰 RH，不调用 F1–F4，不投影回旧四通道"**；**关键约束**：**"不能先假定 transition map 一定存在"** —— 第一步必须把**候选 transition structure 的来源空间也构造出来**，否则是"先写 $T$，再给 $T$ 找意义"（反向工程）。**禁令**（本档全程遵守）：**禁止出现 $\rho,\gamma,\beta,\Xi,\mathrm{RH},\text{Weil positivity},\text{Li criterion}$，甚至暂不问"这能否证明 RH"**；只允许 $$(p,p^k,\Lambda(p^k),\log p)\to A_v\to T_{vw}\to\text{cocycle}\to\text{obstruction}\to\text{是否离散}$$

**V196-1 底空间与局部对象**：$\mathscr X=\{v_p\}\cup\{v_\infty\}$；$A_p$ 只用 $p,p^k,\log p,\Lambda(p^k)$。候选 canonical 局部对象：$\mathbb Z_p^\times$｜$\mu_{p-1}\subset\mathbb Z_p^\times$（**局部挠**，Teichmüller，阶 $p-1$ **有限**）｜$v_p:\mathbb Q^\times\to\mathbb Z$（**取值离散**）｜$\log p\in\mathbb R_{>0}$（尺度）｜$\Lambda(p^k)=\log p$；$A_\infty=\mathbb R_{>0}$。

**V196-2 过渡映射存在性 ＋ canonical 性检验（第一个硬结果）**：**(A) $T_{p,q}:\mathbb Z_p^\times\to\mathbb Z_q^\times$ 直接映射 —— ✗ 不存在 canonical 定义**（挠阶 $p-1$ vs $q-1$ 不同、无自然 $p$-adic→$q$-adic 同态；任何此类映射都需**额外选择** ⟹ 那**不是** transition structure，只是**人为编码**）⟹ 按预定：$$\boxed{\text{素数之间没有这种 canonical gluing geometry}}$$ **转 B**。**⭐ 但发现 canonical 的替代道路 ＝ 公共对象（common object）**：不是点对点映射，而是各 $A_p$ **canonically 映入同一对象** ——(甲) 乘法侧 $p\mapsto p\in\hat{\mathbb Z}^\times$（**无需任何选择**）；(乙) 加法侧 $p\mapsto\log p\in\mathbb R_{>0}$；(丙) 局部挠侧 $\mu_{p-1}\hookrightarrow\mu_\infty=\bigcup_N\mu_N$ ⟹ **canonicity 在"共对象"层面成立**，过渡结构应写成**公共对象上的数据相容性**。**(C) 尺度支**：$A(r)=A_p$ 当 $r=\log p$ ⟹ canonical 性同 A 一样失败，**只能走公共对象道路**；尺度侧 canonical 结构 ＝ $\mathbb R_{>0}$ 上的伸缩作用，且 $\{\log p\}$ 在 $\mathbb Q$ 上**线性无关**。

**V196-3 cocycle（一阶／二阶由实际 gluing law 决定）**：**加法支（valuations／$\log p$）** ＝ **乘积公式** $\sum_pv_p(x)\log p-\log|x|_\infty=0$ ⟹ cocycle **恒为 0**（加法上闭链），且 $\{\log p\}$ $\mathbb Q$-线性无关（唯一分解；Baker 更强）⟹ **格自由** ⟹ $$\boxed{\text{obstruction}=0}$$ ⟹ 判据 ① **杀**。**乘法支（局部挠／符号）**：局部符号 $(a,b)_v$ 取值 $\mu_N$（**离散**）；gluing law ＝ **Hilbert 互反** $\prod_v(a,b)_v=1$ ⟹ obstruction 宿主 $$\bigoplus_v\mathrm{Br}(\mathbb Q_v)/\mathrm{Br}(\mathbb Q)\cong\mathbb Q/\mathbb Z$$ 其 $N$-挠部分 $\mathrm{Br}(\mathbb Q)[N]$ **有限**（逐 $N$ 离散），但整体 $\mathbb Q/\mathbb Z$ **非有限** ⟹ 判据 ③ **杀**。

**V196-4 离散值域来源（已定位）**：**(I) 局部挠 $\mu_{p-1}\subset\mathbb Z_p^\times$**（阶有限、canonical）；⭐ **结构事实**：$\hat{\mathbb Z}$ 的挠子群 $=\bigoplus_p\mu_{p-1}$（**直和**，因有限阶元只有限多分量非平凡）⟹ **它在 profinite 拓扑中是离散子群** ⟹ 这是"**连续群中的离散结构**"的现成实例 ⟹ **刚性引擎的前提在算术中真实存在**。**(II) 符号取值 $\mu_N$ 与 $\mathrm{Br}[N]$（逐 $N$ 有限）**。⚠️ 但 (I)(II) 的离散性**都来自"挠／单位根"，不来自任何"局部-全局张力"的新结构**。**(III)（本档新提）局部挠与全局挠的落差**：逐 $p$ 有 $\mu_{p-1}$（阶 $p-1$），而 $\mathbb Q$ 只有 $\mu_2$ ⟹ "局部离散数据不升为全局离散数据"这一**落差**本身是 canonical 现象，其障碍类落在 $\mu$-挠／$\mathrm{Br}$ 体系中。

**V196-5 刚性检验**：$T_\lambda$ 连续族、$[T_\lambda]\in D$ 离散 ⟹ $\lambda\mapsto[T_\lambda]$ **局部常值** ⟹ 一点为零则同支为零；⭐ **经典实例（局部符号／挠类）确有该性质**（对 $(a,b)$ 局部常值）⟹ $$\boxed{\text{机制 II 的刚性引擎在算术中确有实例};\ \text{但实例的类是}\textbf{经典类}}$$

**§6 判据对照（四条逐条）**：加法支 ＝ 0 ⟹ **① 杀**｜尺度支 ＝ 0 ⟹ **① 杀**｜$p\leftrightarrow q$ 直接映射 ＝ **canonical 性失败**（非 obstruction 型）｜$p\leftrightarrow\infty$ 公共对象 ＝ 可建但 gluing 是乘积公式 ⟹ **① 杀**｜乘法／符号支 ＝ $\mathrm{Br}$ 型 ⟹ **③ 杀**｜来源 (I)(II) 满足 ④ **形式条件但内容为经典挠类**。⟹ **四个候选支路全部落到 ① 或 ③**。⚠️ **但严格按纪律：本档不宣称"机制 II 死"，只宣称"canonical 分支的落点已被识别"**。

**§7 唯一残余与 V197 预登记（lead，不预判）**：唯一未被判据覆盖的形状 ＝ **离散、非平凡、且非已知挠／$\mathrm{Br}$ 类的 obstruction**；最接近的 lead（**仅登记**）＝ 经典 $K$-理论中 **Steinberg 型关系 $\{a,1-a\}=0$**（**配对形状 $a\leftrightarrow1-a$**），⚠️ 但其取值**可能仍落 $\mu_N／\mathrm{Br}$**（待算）。**V197 唯一动作**：判 Steinberg 型关系的 obstruction 是否仍落 $\mathrm{Br}[N]$ —— 若落 ⟹ 该 lead 亦属 ③；若否 ⟹ 这是**第一个不属于 ①②③ 的离散非平凡类**。

### F.5bf ⭐⭐⭐⭐⭐ **V197：Steinberg branch obstruction 值域审计 ＋ V196 §4 勘误（ℤ̂^× 挠结构）⟹ Mechanism II canonical branch 收口**（`V197` ✓ 2026-09-15 13:31）

**委托（唐先生）**：**"开 V197……不是先问 Steinberg relation 能不能产生离散类，而是把它作为候选 obstruction，完整算它的值域"**；**技术点核实**：**"$\hat{\mathbb Z}^\times$ 的 torsion $=\bigoplus_p\mu_{p-1}$ 这个表述涉及有限阶元素在 profinite 单位群中的具体分解；V197 不要沿用它作为未经证明的前提。先从标准结构分解逐项核。"**（并指出 V196 核心结论不依赖此表述）；**只允许链** $a\mapsto1-a\mapsto\{a,1-a\}\mapsto\partial_v\{a,1-a\}\mapsto\text{global obstruction}$；**禁令同 V196**。

**⚠️ ① 勘误（定义级核对）—— 唐先生提示正确**：标准分解 $\mathbb Z_p^\times\cong\mu_{p-1}\times(1+p\mathbb Z_p)$（$p$ 奇）、$\mathbb Z_2^\times\cong\mu_2\times\mathbb Z_2$ ⟹ $\hat{\mathbb Z}^\times=\prod_p\mathbb Z_p^\times$；挠元判据 ＝ **各分量挠且阶有界**（元组的阶 ＝ lcm 分量阶），⚠️ **不要求"只有限多分量非平凡"**（例 $x_p=-1\ \forall p$ 阶 2）⟹ $$\boxed{(\hat{\mathbb Z}^\times)[N]=\prod_p\mu_{\gcd(N,p-1)}}$$ **是积而非直和**，对 $N\ge2$ 为**无限积**；⚠️ $(\hat{\mathbb Z}^\times)[2]=\mu_2^\infty$ **不可数、Cantor 型、非离散** ⟹ 挠子群**不是离散子群** ✗ ⟹ **V196 §4 的"$\hat{\mathbb Z}$ 挠 $=\bigoplus_p\mu_{p-1}$ 且为离散子群 ⟹ 刚性前提存在"撤回** ✓；⭐ 但 **V196 核心结论（四支全落 ①／③）不依赖此表述，不受影响** ✓✓（唐先生已预判）。

**⭐ ② local boundary 全链实算**：tame symbol $\partial_v\{a,b\}=(-1)^{v(a)v(b)}a^{v(b)}b^{-v(a)}\in k(v)^\times$；关键输入 $a+(1-a)=1\Rightarrow v(1)=0\ge\min(v(a),v(1-a))$。**五情形穷尽**：(i) $v(a)=0,v(1-a)=n>0$ ⟹ $a\equiv1\bmod\mathfrak m$ ⟹ $\partial_v=a^n\mapsto1$；(ii) 对称情形 ⟹ $(1-a)^{-n}\mapsto1$；(iii) 两者皆 0 ⟹ $1$；(iv) $v(a)=v(1-a)=m<0$ ⟹ $u+u'=\pi^{-m}\in\mathfrak m^{|m|}$ ⟹ $\bar u'=-\bar u$ ⟹ $\partial_v=(-1)^{m^2}(u/u')^m=(-1)^m(-1)^m=1$；(v) $m>0$ **不可能**（否则 $v(1)\ge m>0$）。⟹ $$\boxed{\partial_v\{a,1-a\}=1\quad(\forall\ v)}$$ ⭐ **结构性原因**：$a+(1-a)=1$ 强制 $a$ 或 $1-a$ 为**主单位**（$\equiv1\bmod\mathfrak m$）⟹ 残数恒平凡；⭐ **逐层传播**：由 $a\in1+\mathfrak m$（或 $1-a\in1+\mathfrak m$），迭代边界同样平凡 ⟹ **Steinberg 对在所有边界层不可见**。

**③ localization 值域审计（逐类区分，不把 torsion 一律归 Brauer）**：对 **Steinberg 对**：由 ② 该链**无输出**（每分量为 1）⟹ "Steinberg $\to$ local data $\to$ global quotient" 的中间环节**为空** ⟹ quotient 无内容。对**一般符号** $\{a,b\}$（$b\ne1-a$）：局部数据非平凡；其离散不变量由 ⭐ **Merkurjev--Suslin** $K_2^M(F)/N\cong\mathrm{Br}(F)[N]$（**定理，非假设**）确定 ⟹ 从 $K_2$ 符号提取的离散不变量在 $N$-商上**恰是 Brauer 类** ⟹ **B 类**。其余逐项排除：$\mu_N$ ＝ $\mathrm{Br}[N]$ 的取值层，**不独立** ⟹ 归 B；$K_2$ **未商部分**／$K_2/\text{divisible}$：**非离散**（可除／无限秩）⟹ 不满足离散性要求 ⟹ **非候选** ⟹ **无第五类出现**。

**④ $a\leftrightarrow1-a$ 是否产生新 obstruction**：若 $\Omega(a)+\Omega(1-a)=0$ 或 $\Omega(a)\Omega(1-a)=1$，问其是否只是 Steinberg 的另一种表示；⚠️ 本档严格限于允许链（含 $\partial_v$ **边界型**构造）：由 ② 所有 tame 边界已平凡 ⟹ 任何**由边界构造**的 $\Omega$ **必为 0** ⟹ $$\boxed{\Omega=0}$$ ⟹ **A 类**。⚠️ 诚实边界：**非边界型**的 $a\mapsto1-a$ 构造不在本条链内（本档不涉及）。

**⑤ 三分判定**：$$\boxed{\text{A}\ \Omega=0\ \text{（trivial）}\ |\ \text{B}\ \Omega\in\mu_N\ \text{或}\ \mathrm{Br}[N]\ \text{（经典 torsion）}\ |\ \text{C}\ \Omega\in D_{\rm new}\ \text{（新 obstruction）}}$$ 本档落点：**Steinberg 支 $\Rightarrow$ A**；**一般符号支 $\Rightarrow$ B**；**C 未出现**。

**⑥ 判词：Mechanism II 的 canonical arithmetic branch 收口**：$$\text{transition}\to\text{cocycle}\to\text{localization}\to\text{obstruction}\ \Longrightarrow\ \text{落点}\ 0/\mu_N/\mathrm{Br}[N]$$ ⭐ 这不是**猜测性死亡**，而是经**实际计算**（V196 过渡/cocycle ＋ V197 边界/localization）后的**收口**；⚠️ 严格表述：收口范围 ＝ **"canonical 分支"**（公共对象道路 ＋ 边界型 obstruction），**不**声称机制 II 整类死亡。

**⑦ 残余**：唯一未被覆盖 ＝ **非 tame 边界、非 $\mathrm{Br}[N]$ 的离散不变量**；本轮**未见实例** ⟹ 登记 **UNINSTANTIATED**，**不给方向、不投入、不杀**。

### F.5bg 🚪 **V198：Mechanism II Closure Gate（V195–V197 收口入口；可执行重启判据）**（`V198` ✓ 2026-09-15 13:35）

**委托（唐先生）**：**「先写 V195–V197 的收口入口，而且要把『为什么不值得重启』写成可执行判据，而不是历史总结。」** ＋ **「这条线完成的事情不是证明 Mechanism II 不可能，而是把它的 canonical arithmetic realization space 实际压缩掉了。未来如果再回来，必须从『非 tame、非 Brauer、真正离散的新 obstruction』起步。」** ＋ **顺序：本门 → A1／A3**；下一轮不再从 Steinberg／$K_2$／局部符号横向挖。

**§1 已经计算掉的（结果导向，非叙事）**：| 分支 | 结果 |｜$p\leftrightarrow q$ canonical local map｜**不存在**（需额外选择 ⟹ 人为编码，`V196` §2.1）｜｜common additive object｜product formula $=0$（加法上闭链；$\log p$ $\mathbb Q$-线性无关，`V196` §3.1）｜｜multiplicative symbol｜$\mathrm{Br}[N]$／经典 torsion（`V196` §3.2）｜｜$a\leftrightarrow1-a$ ＋ tame boundary｜$0$（$\partial_v\{a,1-a\}=1\ \forall v$，`V197` §2）｜｜$K_2$ 的离散 $N$-商｜$\mathrm{Br}[N]$（Merkurjev–Suslin，`V197` §3）｜｜$\hat{\mathbb Z}^\times$ torsion｜**非离散**，不能充当离散 obstruction（`V197` §1）｜ ⟹ $$\boxed{\text{canonical arithmetic transition}\longrightarrow 0\ \text{or}\ \mathrm{Br}[N]/\text{classical torsion}}$$ ⚠️ 收口范围 ＝ **canonical 分支**，**不**声称机制 II 整类死亡。

**§2 重启必要条件（六条；逐条可检验；任一不满足 ⟹ 立即停）**：$$\boxed{(1)\ \text{明确 arithmetic transition/cocycle}\ (2)\ \Omega\ \text{值域离散}\ (3)\ \Omega\not\equiv0\ (4)\ \Omega\notin\mathrm{Br}[N]/\text{已知 torsion}\ (5)\ \text{非 explicit-formula 重编码}\ (6)\ \text{可证 deformation 下}\ \Omega\ \textbf{locally constant}\ (\text{真 rigidity})}$$ 检验口径：(1) 能否写出 $T_{vw}$ **显式局部定义且无需额外选择**；(2) 能否证明 $\Omega$ 取值于离散 $D$ **且 $D$ 在该拓扑下确实离散**（`V197` §1 已给反面范例：挠 $\neq$ 离散）；(4) 能否排除 Merkurjev–Suslin 型识别；(6) 是否存在连续族使 $[T_\lambda]\in D$ 离散 ⟹ $\lambda\mapsto[T_\lambda]$ 局部常值。

**§3 死禁令（写死）**：$$\boxed{\text{「发现一个新的}\ K\text{-theory／群论对象」}\neq\text{发现新的 obstruction mechanism}}$$ 必须先算**值域**与**局部化像**；「对象新」不构成理由。**§4 停止条件**：若自动掉进 $0$／$\mu_N$／$\mathrm{Br}[N]$ ⟹ **立即停止**，不得包装成「新机制」，须记入 §5 清单。**§5 不要重走清单（硬）**：prime$\leftrightarrow$prime canonical map｜product formula｜Hilbert 互反｜Steinberg／tame symbol｜$K_2$ 的 $N$-商｜$\hat{\mathbb Z}^\times$ torsion 当离散 obstruction —— 其 **canonical 版本已被实算排除**，重走须说明**为何不是同一分支**。**§6 残余**：非 tame 边界、非 $\mathrm{Br}[N]$ 的离散不变量 ⟹ 本轮未见实例 ⟹ **UNINSTANTIATED**，不给方向、不投入、不杀。**§7 勘误随行**：不得沿用 `V196` §4 的「$\hat{\mathbb Z}^\times$ 挠 $=\bigoplus_p\mu_{p-1}$ 且离散」；正确 $(\hat{\mathbb Z}^\times)[N]=\prod_p\mu_{\gcd(N,p-1)}$（积非直和），$(\hat{\mathbb Z}^\times)[2]=\mu_2^\infty$ 不可数非离散。**§8 下一站**：$$\boxed{\text{本门}\to\textbf{A1／A3}}$$ ⚠️ **不回** Mechanism II 变体；不再从 Steinberg／$K_2$／局部符号横向挖。

### F.5bh ⭐⭐⭐⭐⭐ **V199：A1／A3 主线（唯一主线）—— 中间正性机制的钉死 ＋ 正性锥三来源分类 ＋ 门的逻辑后果**（`V199` ✓ 2026-09-15 13:39）

**委托（唐先生）**：**「现在回 A1/A3，而且只回这一条主线」**；任务钉死为 $$\boxed{\text{寻找一个严格位于二者之间、可由算术侧独立验证的中间正性／耗散性机制}}$$ 核心审计对象 $$\text{prime-side}\longrightarrow\boxed{?}\longrightarrow\text{Li／Weil}\longrightarrow\mathrm{RH}$$ **「其中真正缺的是中间那个 ?，而不是再证明 RH ⟺ Li ⟺ Weil」**；**硬门（三条件）**：prime-side $\Longrightarrow P\Longrightarrow$ RH；$P\not\Rightarrow Q\succeq0$（仅靠定义等价包装）；$P$ **可在不假设 RH 下被证明** —— 否则立即归入旧等价类；**重检 A1／A3 区别**（A1：从 Li 系数本身找新结构性约束；A3：从 prime-side／explicit-formula 侧找**非显式公式重编码**的 Li 正性产生机制）；**第一问**：$$\boxed{\text{为什么一个本身不含零点位置的信息系统，会强制产生一个全局正性锥？}}$$

**§1 分层表（含实际内容）**：显式公式 ＝ $N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+S(T)$（主项无条件；RH $\iff S(T)=O(\log T/\log\log T)$）｜Weil ＝ $Q(f)=W(f\star f^*)=\sum_\rho|\hat f(\gamma_\rho)|^2$（零侧）／素数项＋archimedean（算术侧）｜Li ＝ $\lambda_n=\sum_\rho[1-(1-\frac1\rho)^n]=\frac{1}{(n-1)!}\frac{d^n}{ds^n}[s^{n-1}\log\xi(s)]|_{s=1}$｜RH ＝ $\beta=\frac12$。四层**在同一等价类内** ⟹ **不再证等价**。

**⭐ §2 关键观察（第一个核心）**：由 $(1-\frac1\rho)^n=\sum_j\binom nj(-1)^j\rho^{-j}$，$\lambda_n$ 是**幂和** $\{\sum_\rho\rho^{-j}\}_{j\le n}$ 的**有限组合**，而幂和由 $\xi'/\xi$ 的 Hadamard 展开在 $s=0$ 的 Taylor 系数给出 ⟹ 可由**显式公式的素数侧＋archimedean 侧**确定 ⟹ $$\boxed{\text{素数侧}\to\lambda_n\ \text{这条复合映射已经是显式的}}$$ ⟹ 中间那个 $?$ **不能是"信息通道"**，只能是**产生正性的结构**；⚠️ 这**排除**一整类候选（任何"再找一条素数→零点信息通道"的提案必然落入已有显式路径）。

**⭐⭐ §3 正性锥的三个来源（第二个核心）**：(a) **代数型＝平方和／二次型**：$Q(f)=\sum_\rho|\hat f(\gamma_\rho)|^2$；全 $\gamma_\rho$ 实时为平方和（自动非负）；离轴对给出两点取值和 $2\mathrm{Re}\,\hat f$，**不是平方和** ⟹ 破坏平方结构 ⟹ **SOS 型锥恰恰就是 RH 的断言** ⟹ 作为独立来源**等价于 RH**。(b) **分析型＝实根性／全正性（Newton–Turán 锥）**：实根 ＋ 正系数 ⟹ Newton 不等式；全正／Pólya 频率 $\iff$ 表示测度支撑半直线（Schoenberg）⟹ 即 `V190`／`V191` 通道，**强度等于 RH**（`V191` 已证不可能由严格更弱命题推出）。(c) **动力学型＝耗散性／熵产生**：双曲膨胀 ＋ 归一化 ⟹ 唯一不变态 ＋ 谱隙 ⟹ 符号确定的锥（RPF 型）；⚠️ 前提**需要指数级轨道增长**，而 char-0 素数增长是**多项式** ⟹ 该机制**不直接适用**（与层诊断一致）。

**§4 硬门逐条检验**：| 来源 | prime-side $\Rightarrow P$？ | $P\Rightarrow$ RH 且非包装？ | $P$ 可无条件证明？ |｜(a) SOS | 是 | **否（定义即 RH）** | 否｜｜(b) 实根性／PF | 是 | **否（强度＝RH）** | 否｜｜(c) 耗散／熵 | **否（需指数膨胀）** | 是（若能建立） | 否｜ ⟹ **三来源无一过门**，且**失败点各不相同**：(a) 失败于"非包装"；(b) 失败于"可无条件证明"；(c) 失败于"prime-side $\Rightarrow P$"。⚠️ 这是**按门对锥源做分类裁决**，**不是**再证等价。

**⭐ §5 门的逻辑后果（第三个核心）**：设 $P$ 过门 ⟹ prime-side（无条件已知事实）$\Longrightarrow P\Longrightarrow$ RH ⟹ **RH 可由无条件已知事实推出**；而**已知无条件事实（PNT／AP 中的 PNT／零自由区／二阶输入）不足以推出 RH** ⟹ $$\boxed{\text{过门的 }P\ \textbf{必然}\text{引入一个}\textbf{新的无条件输入}}$$ ⭐ 可执行判据：**若某提案不产生新的无条件输入，则它不可能过门**，无论包装多精巧；等价陈述：**过门 $\iff$ 存在新无条件输入** ⟹ 本主线的真任务 ＝ **寻找（或制造）该输入**。

**§6 第一问的回答**：**它不"强制"——除非锥来自 §3 三类之一**：(a) 若来自代数（平方和）则"不含零点位置"是**假象**（平方和的项本身含零点位置）；(b) 若来自分析（实根性／全正）则**它就是 RH 的等价形式**，"不含零点位置"只是**表述层面**；(c) 若来自动力学（耗散）则必须**外部**给出膨胀／双曲结构，而这在 char 0 中**缺失** ⟹ **所谓"零位置无关却强制锥"在任何已知机制下都不成立**。

**§7 残余与 V200 预登记**：唯一未被 §3 覆盖的锥源形状 ＝ **组合／单调型**（非代数、非分析、非动力学；候选形态：正关联／FKG 型、单调耦合、格上单调性、关联不等式）；⚠️ 按 §5，若欲过门**必须产生新的无条件输入**，否则立即判死。**V200 唯一动作**：审计组合／单调型锥源 —— 是否存在对 $(\Lambda(n),\log p,p^k)$ 的**单调关联结构**，其正性**不是** SOS／实根性／耗散的重新表述，且能产生新的无条件输入？若否 ⟹ **四类锥源全封、本主线收口**；若是 ⟹ 这是第一个合法 $P$。

### F.5bi ⭐⭐⭐⭐⭐ ⚠️**结论收紧（`V201`）**：本节的判词应读作「**现有 canonical 组合／单调构造未产生新的无条件输入**」，**不得**读作「任何组合／单调机制都不可能」—— 本档只穷尽**当前定义域内的候选构造**，非不存在性证明。

### F.5bi ⭐⭐⭐⭐⭐ **V200：跨素数正关联审计（单一预算）⟹ 组合／单调锥源 DEAD；四类锥源全封；A1／A3 主线收口**（`V200` ✓ 2026-09-15 13:43）

**委托（唐先生）**：**「开 V200。这一档要比前面更严格：不要先假定 FKG/正关联能产生 RH 所需的锥；先做『能否产生新无条件输入』的反向审计。」** 只检查 $$\text{prime-side}\overset{?}{\Longrightarrow}P_{\rm comb}\overset{?}{\Longrightarrow}\text{Li／Weil positivity}$$ **四项硬检验**：(1) 先定义对象，**不准使用零点**（只允许 $\Lambda,\psi,\theta,\log p,p^k$）；(2) **计算关联量，而非引用「正关联」**，并特别审计**独立乘法结构 vs 跨素数关联结构**（「若关联最后完全因子化，立即关闭」）；(3) **最关键：测新信息量**（若只是 $\psi(x)\le x+E(x)$／PNT／零自由区／BV／Selberg 型二次估计的变形 ⟹ **立即 DEAD**）；(4) 最后才问 RH 强度，**禁止** $P_{\rm comb}\equiv\text{total positivity}\equiv\text{Jensen hyperbolicity}\equiv\mathrm{RH}$。**预算＝一项**：跨素数正关联是否存在非平凡、可无条件证明、且产生新输入的 canonical 结构。

**§1 对象**：允许 $\Lambda,\psi,\theta,\log p,p^k$；两种 canonical 测度：$\mu_x$（$\{1,\dots,x\}$ 均匀）、$\mu_{\mathbb P}$（$\{p\le x\}$ 均匀）。

**⭐ §2 实测关联量（非引用）**：**(2.1)** $\mu_x$：$\mathbb E[F_pF_q]=\frac{\lfloor x/pq\rfloor}{x}$，$\mathbb E[F_p]=\frac{\lfloor x/p\rfloor}{x}$ ⟹ $$\boxed{\operatorname{Cov}_{\mu_x}(F_p,F_q)=\frac{\lfloor x/pq\rfloor}{x}-\frac{\lfloor x/p\rfloor\lfloor x/q\rfloor}{x^2}=O(1/x)}$$ ⚠️ **主项精确抵消**（$\frac1{pq}-\frac1p\frac1q=0$），剩余 $O(1/x)$ 的**符号由 $\{x/p\},\{x/q\}$ 决定 ⟹ 符号不定** ⟹ 按唐先生判据「关联完全因子化 ⟹ 立即关闭」✓✓。**(2.2)** $\mu_{\mathbb P}$：$p\ne q$ ⟹ $\mathbf 1_{p\mid N}\mathbf 1_{q\mid N}\equiv0$ ⟹ $\operatorname{Cov}=-\frac{1}{\pi(x)^2}<0$（**符号固定但为负**）⟹ 整除型变量在素数测度下**负关联**；正关联型结构只能来自**间隙（元组）**。**(2.3)** 高阶联合累积量 $\kappa_{\mu_x}=O(1/x)$ ⟹ **各阶均因子化** ⟹ 无高阶非平凡跨素数关联 ✓✓✓。

**⭐ §3 FKG 二难 ＋ 子格障碍（结构性）**：FKG $\iff$ log-supermodularity。**二难**：(i) 若 $F_p$ 独立 ⟹ 乘积测度满足 FKG **取等** ⟹ 不等式**平凡**、不含超出独立性的信息 ⟹ **检查 3 必败**；(ii) 若不独立 ⟹ 证 FKG 须证 log-supermodularity ＝ **正关联本身** ⟹ **循环**。**子格障碍**：窗口 $[1,x]$ 关于 $(\gcd,\mathrm{lcm})$ **不是子格**（lcm 可逃出窗口）⟹ canonical FKG 框架**不适用**；若改用有限素数集 $S$ 的除子格（Boole 格），乘积测度满足 FKG 且**取等** ⟹ 回到 (i)。⟹ 组合／单调型锥源在 FKG 框架内**二难闭合** ✓✓✓。

**⭐ §4 硬检验 3（判死点）**：唯一**非因子化**的跨素数结构 ＝ **素数元组／间隙相关** $\sum_{n\le x}\Lambda(n)\Lambda(n+h_1)\cdots\Lambda(n+h_{k-1})$ ⟹ 即 **Hardy–Littlewood 区域**；其**无条件**控制恰为 (a) **水平分布 $\theta=\frac12$（Bombieri–Vinogradov）**、(b) **二阶矩型估计（Selberg）**、(c) pair correlation **Fourier 支撑 $\le1$** ⟹ 越过须 **support $>1$** ⟹ 即 `V162` 承重墙 ⟹ $$\boxed{\text{任何无条件的}\ P_{\rm comb}\ \text{必为 (a)–(c) 的变体}}$$ ⟹ 按唐先生清单 ⟹ $$\boxed{\textbf{立即 DEAD}}$$ ⚠️ 不产生新无条件输入 ⟹ 由 `V199` §5 判据**不可能过门** ✓✓✓。

**§5 硬检验 4**：按协议**不进入**；且未使用被禁止的三项等价 ✓。

**§6 判词**：$$\boxed{\textbf{组合／单调锥源 DEAD}}$$（两条独立路径：协方差因子化；FKG 二难；非因子化残差＝已知墙）⟹ `V199` §3 **四类锥源全封**：(a) 代数／SOS ✓（＝RH 的断言）；(b) 分析／实根性-全正 ✓（强度＝RH）；(c) 动力学／耗散 ✓（需指数膨胀，char-0 缺失）；(d) 组合／单调 ✓（本档）⟹ $$\boxed{\textbf{A1／A3 主线收口}}$$（按 `V199` §5：四类锥源均不能产生新的无条件输入）✓✓✓。

**§7 残余（UNINSTANTIATED，不给方向）**：非 canonical、符号固定、跨素数、可无条件证明、且产生新数论不等式的关联结构；本轮**未见实例**；日后候选判据三条（缺一不可）：① 符号固定且跨素数；② 无条件可证；③ 给出**现有无条件理论没有的**不等式。

**备注**：审计线号段已由 V101–V199 扩至 **V101–V299**（`scripts/id_claim.sh` 注释已记）✓。

### F.5bj 🚪 **V201：A1／A3 Restart Gate（可重启协议；纯协议，不含研究内容）**（`V201` ✓ 2026-09-15 13:46）

**委托（唐先生）**：**「写成入口门。但这次不要再扩展研究内容，只做'可重启协议'，然后停。」** ＋ 「把'第五类'定义成**结构性**而非命名性的」＋ 「把 V200 的一个结论写得**稍微保守一点**」＋ **「写完这道门后，停在这里，不要自动开下一条路线。」**

**§1 重启条件（iff；五条缺一不可）**：$$\boxed{\ \text{重开 A1／A3}\iff\begin{cases}\text{(1)}\ \text{出现第五类正性生成机制且不属于四类旧范式};\ \textbf{或}\ \text{旧四类中出现此前不存在的 canonical arithmetic realization};\\ \text{(2)}\ \text{该机制产生}\textbf{新的无条件数论输入};\\ \text{(3)}\ \text{该输入不是 PNT／零自由区／Selberg／BV／pair-correlation 及其}\textbf{显式公式重写};\\ \text{(4)}\ \text{能够}\textbf{独立}\text{连接到 Li／Weil 正性，而非}\textbf{定义性等价}.\end{cases}\ }$$ 检验口径：(1) 写出正性箭头的**逻辑形式**并逐条过 §2 还原判据；(2) 能否指出**现有无条件理论没有**的不等式；(3) 对照清单逐项排除（尤须排除"显式公式重写"型伪装）；(4) 连接步骤是否只靠"定义即等价"。

**§2 ⭐ 「第五类」的**结构性**定义（命名不算）**：$$\boxed{\text{换一个术语、换一个范畴、换一个核}\neq\text{第五类}}$$ 必须**证明**其正性箭头不能还原为四类之一：**(i) SOS 型**（非负性可写成 $\sum$(非负项)／正定核积分）；**(ii) 实根／全正型**（等价于某族多项式双曲性或某核全正性／变差缩减）；**(iii) 谱隙／耗散型**（等价于某算子谱隙 $>0$ 或某量单调递减）；**(iv) 关联／单调型**（等价于某测度的 log-supermodularity／正关联）。⚠️ 还原判据须**逐条显式给出**；任一条命中 ⟹ 不是第五类。

**§3 ⚠️ V200 结论收紧（本轮生效）**：$$\boxed{\text{V200 结论（收紧后）}：\textbf{现有 canonical 组合／单调构造}\ \text{未产生新的无条件输入}}$$ ⚠️ **不得**写成"任何组合／单调机制都不可能"；理由：V200 使用**两种 canonical 测度**（$\mu_x,\mu_{\mathbb P}$）与 canonical 构造 ⟹ 穷尽的是**当前定义域内**的候选构造，**不是**数学上的不存在性证明 ⟹ §6 的"收口"须读作"**定义域内收口**"。

**§4 不要重走清单（换名清单）**：(i) 正相关→对数超模→单调耦合→格条件→关联不等式（同属 (iv)）；(ii) 耗散→熵产生→Lyapunov→谱隙→混合性（同属 (iii)）；(iii) 全正→变差缩减→Pólya 频率→实根性→Newton／Turán（同属 (ii)）；(iv) 平方和→正定核→Bochner→Weil 二次型（同属 (i)）。⚠️ 凡在清单内的改名，**一律按原类处理**，不构成新提案。

**§5 检查顺序（fail-fast）**：归类（四类之一 ⟹ 记录并停，除"旧四类出现此前不存在的 canonical arithmetic realization"例外）→ **新输入？**（否 ⟹ 停）→ **排除已知清单**（落入 ⟹ 停）→ **独立连接**（只靠定义等价 ⟹ 停）⟹ 全过才值得重启；任一步失败 ⟹ **立即停止，不进入推导**。

**§6 与 `V198` 门的关系 ＋ 当前状态**：**两道门并列** —— `V198`（Mechanism II 门：globalization obstruction）／`V201`（A1／A3 门：正性锥源）。**当前状态**：A1／A3 **定义域内收口**（依 `V200` ＋ §3 收紧表述），等**外部新输入**或**第五类**出现；⚠️ **不自动开新线**，不得以"换名"重启同一范式。

### F.5bk ⭐⭐⭐⭐⭐ **V202：Arithmetic Dual-Localization Audit（第一档只做定量不等式与复合律）⟹ canonical 算术对偶局域化 DEAD（$\Delta=0$）**（`V202` ✓ 2026-09-15 13:50）

**委托（唐先生）**：**「V200 的收口不是'研究结束'，而是说明 A1/A3 这条生成器已经耗尽；下一步必须重新找一个不同的数学/物理模型。」** 新模型 ＝ **Dual-localization defect amplification**（核心：**同一个对象不能同时在两个互补表示中过度局域化**；并带**放大机制** $r_{k_1+k_2}\le r_{k_1}r_{k_2}$ ⟹ **局部一个严格缺陷 ⟹ 跨尺度指数放大**）；**「我建议直接开 V201……第一步就算，不再做概念讨论：先求 additive/multiplicative 双局域化的精确定量不等式及其跨尺度复合律。」** ＋ **第一关**：若 $B_{\rm mult}$ 仅由 $\prod_{p\le y}(1-1/p)$ 控制（sieve density）⟹ 死；若加法侧只是 $|\operatorname{supp}f||\operatorname{supp}\hat f|\ge N$ ⟹ 死；要的是**加法尺度 × 乘法尺度 × 非因子化缺陷**；＋ **最终测试**：$\Delta_k>0$ 且 $\Delta_{k+\ell}\ge1-(1-\Delta_k)(1-\Delta_\ell)$ ⟹ $\Delta_{mk}\to1$；＋ **「如果第一阶段本身都做不出来，直接关闭，不碰 RH。」** ⚠️ 编号：`V201` 已被 A1／A3 Restart Gate 占用 ⟹ 本档 **V202**。

**§1 设置**：$B_{\rm add}(S)$（加法坐标可取值数）、$B_{\rm mult}(S)$（小素数模式数）；算子化 $T(N,Q)=P_{\Omega_Q}\mathcal F P_{I_N}$，$r=\|T\|$，$r^{\rm triv}=1$，$\Delta:=1-r$。

**§2 复合律的等价形式**：$\Delta_{k+\ell}\ge1-(1-\Delta_k)(1-\Delta_\ell)\iff$ $$\boxed{\rho_{k+\ell}\le\rho_k\rho_\ell,\quad \rho:=1-\Delta=r}$$ 即 **FUP 型次可乘性**；某项严格 $r_{k_0}<1$ ⟹ $r_{mk_0}\le r_{k_0}^m$ **指数趋零** ✓ ⚠️ **关键警告：次可乘性本身不产生放大** —— 若 $r\equiv1$，律**恒取等且空洞** ⟹ **第一要件＝某尺度存在严格缺陷** ✓✓✓

**⭐ §3 Canonical 对 I（加法 $=n\bmod M$；乘法 ＝ 小素数模式）：因子化 ⟹ $\Delta=0$**：取 $(M,\prod_{p\le y}p)=1$，$$\#\{n\le N:n\equiv r\bmod M,\ \mathbf 1_{p\mid n}=P\}\approx\frac NM\prod_{p\in P}\frac1p\prod_{q\notin P}\Bigl(1-\frac1q\Bigr)$$ **右端完全因子化**（加法因子 × 筛密度因子，**无交叉项**）⟹ 联合支撑 ＝ 直积 ⟹ $$\boxed{\Delta_{\rm I}=0}$$（仅平凡界 $B_{\rm add}B_{\rm mult}\ge|S|$）⟹ 按唐先生第一关：**只是筛密度＋平凡计数 ⟹ 杀** ✓✓

**⭐⭐ §4 Canonical 对 II（加法 ＝ 区间；乘法 ＝ 小分母频率／Farey）：相反区间 ⟹ 缺陷消失**：$\Omega_Q=\{a/q:q\le Q\}$，$|\Omega_Q|\asymp Q^2$；**大筛法**给出节省因子 $\frac{N}{N+Q^2}$ ⟹ **(i)** 大筛法**有内容** $\iff Q\gtrsim\sqrt N$，此时 $|\Omega_Q|\gtrsim N$（**频率集不再稀疏**）；**(ii)** FUP 型**严格节省需正余维** $|\Omega_Q|\ll N\iff Q\ll\sqrt N$ ⟹ $$\boxed{\text{两机制有效区间}\textbf{恰好相反}，\text{仅在}\ Q=\sqrt N\ \textbf{相切}}$$ 该点 $|\Omega_Q|\asymp N$（满维、临界）⟹ 节省 $\to0$、缺陷 $\to0$；且区间与 Farey 集在各自尺度上均**满维**，不满足 FUP 所需维数亏缺 ⟹ $$\boxed{\Delta_{\rm II}=0}$$ ✓✓✓

**§5 第三候选**：$|\operatorname{supp}f|+|\operatorname{supp}\hat f|\ge q+1$ 是 **additive-only**（不含乘法坐标）⟹ 不足以构成对偶；真正的对偶候选（同一 $f$ 上 additive DFT × 乘法特征变换）**确有已知结果** ⟹ 按 `V201` §1(2) **不产生新的无条件输入** ✓

**⭐ §6 FUP 复合律的四个结构前提（逐条对照）**：**(i) 嵌套族** —— 算术侧**满足** ✓；**(ii) 变换把两族互换** —— **不满足** ✗（区间 $\leftrightarrow$ 小分母频率在 DFT 下**不互换**）；**(iii) 乘积律** $T_{k+\ell}=T_kT_\ell$ —— **不满足** ✗；**(iv) 某尺度严格缺陷** —— **不满足** ✗（§3／§4 均得 $\Delta=0$）⟹ $$\boxed{\text{四前提中算术侧只满足 (i)};\ \text{放大引擎}\textbf{无法启动}}$$ ⚠️ 本结论**不**来自四类锥源、**不**来自 `V198` 门 —— 它是双局域化模型**内部**的**几何／临界性**型障碍 ✓✓✓

**§7 Granville–Soundararajan 的诚实定位**：真算术不确定性原理 ✓，但 **(a) 是已证定理** ⟹ 按 `V201` §1(2) **无新无条件输入**；**(b) 阈值仍在 $\sqrt N$（尺度不变）** ⟹ **不提供放大**；**(c)** 故正确位置是**已知语料**，仅"引用它"即被判死 ✓

**§8 判词**：$$\boxed{\textbf{Canonical 算术对偶局域化：DEAD（}\Delta=0\text{／无严格缺陷）}}$$ 两个独立原因：**(I)** 对 I **因子化**（CRT／筛独立）⟹ 只有平凡界；**(II)** 对 II **相反区间＋满维临界** ⟹ 节省与稀疏不可兼得。**第二阶段（$\to\zeta$／$L$-函数谱排除）按指示不进入** ✓✓✓；⚠️ 范围严格限定＝**canonical 对**，**不**声称"对偶局域化模型不可能" ✓

**§9 重开门（四条件，缺一不可）**：(1) **正余维**（两侧都稀疏）；(2) **嵌套**；(3) **存在变换 $\mathcal T$ 把两族互换**；(4) **乘积律** $T_{k+\ell}=T_kT_\ell$；且须产生**不是** G–S／大筛法／NTT 不确定性已给出的定量不等式；⚠️ 按 §4，条件 (1) 与"大筛法有内容"**互斥** ⟹ 若候选仍在大筛法框架内，**立即判死** ✓

### F.5bl ⭐⭐⭐⭐⭐ **V203：互换变换审计（窄窗口）⟹ 统一结论：「交换」与「乘积律」位于不相交的位；五条终止条件全中 ⟹ 关闭**（`V203` ✓ 2026-09-15 13:54）

**委托（唐先生）**：**「不要关闭。专门找'互换变换'，但只给它一个非常窄的 V203 审计窗口。」** 缺口形式化 $$\boxed{\exists\,\mathcal T:\mathcal T(\mathcal A_k)\approx\mathcal B_k,\ \mathcal T(\mathcal B_k)\approx\mathcal A_k}\ \text{＋}\ \boxed{T_{k+\ell}=T_kT_\ell}$$ **「不要从'寻找一个新变换'开始猜，直接从现有算术变换的完整候选空间做审计」**：(1) 有限 Fourier／加法特征；(2) Mellin／乘法特征；(3) Poisson／Voronoi 型；(4) Hankel／Bessel 型（Voronoi 的 dual summation）；(5) 有限域 Fourier／乘法 Fourier；(6) **adelic Fourier–Mellin（最值得优先）**；每候选**必须实际计算** $\mathcal T(P_{\mathcal A_k}f)\overset{?}{\subseteq}P_{\mathcal B_{k'}}\mathcal Tf$ **及反向**，**且**检查 $T_{k+\ell}\overset{?}{=}T_kT_\ell$ 或等价半群结构；**终止五条**；**「先审计 adelic F–M／Voronoi，再审计其他候选；不进入 RH，不做第二阶段。」**

**§1 判据**：(E1) 正向交换、(E2) 反向交换、(C) 复合律；三条件**同时**且须**逐点**（非平均）成立。

**§2 六候选逐一实算**：**(2.1) DFT**：交换**空间**不交换**族**（$1_{I_N}\mapsto$ Dirichlet 核、$1_{\Omega_Q}\mapsto$ Ramanujan 型和）✗ 命中 #1。**(2.2) Mellin**：确实交换**乘↔加**（$n^s=e^{s\log n}$）但把两族映到**不同空间**、对"区间／小分母"**无像**；其律是**卷积$\mapsto$乘积**（与 $T_{k+\ell}=T_kT_\ell$ **不同型**）✗；且 **Mellin 恰是显式公式的引擎** ⟹ 命中 **#5**。**(2.3) Poisson**：对 $\mathbb Z$ 与 $\mathbb Q\subset\mathbb A$ 均**自对偶** ⟹ 交换＝恒等 ✗ 命中 #1。**(2.4) ⭐ Voronoi／Bessel–Hankel（唯一真正带算术权重的候选）**：交换**确实存在** $$\boxed{N\leftrightarrow q^2/N}$$（**对合**，不动点 $N=q$），核为 Bessel／Kloosterman 型（**算术结构参与对偶**）✓；**但**核来自**函数方程的 $\Gamma$ 因子（archimedean）**，辐角含 $\sqrt{nx}/q$ ⟹ **对模数不乘性** ⟹ $$\boxed{T_{q_1q_2}\ne T_{q_1}T_{q_2}}$$ ⚠️ 虽 $e(a/q)$ 经 CRT **可乘性分解**，**但核不可** ⟹ 乘积律**在核层面失败** ⟹ 命中 **#2**；且交换只在"主项＋误差"意义成立（**非逐点**）⟹ 命中 **#3**；估计本身即**经典 Voronoi 估计** ⟹ 命中 **#4**；⭐ **决定性**：**Voronoi 求和由函数方程导出 ⟹ Voronoi $\equiv$ 函数方程** ⟹ **恰好命中唐先生预设的 #5** ✓✓✓。**(2.5) 有限域 Fourier／乘法 Fourier**：两变换住在**不同群**（$\mathbb F_q$ vs $\mathbb F_q^\times$）⟹ 无自映射交换 ✗；无跨 $q$ 复合 ✗；定量结果均为已证定理 ⟹ 命中 **#4**。**(2.6) ⭐ adelic Fourier–Mellin**：**有限位**：局部 Fourier **把球映为球** $$\boxed{\widehat{1_{\mathbb Z_p}}=1_{\mathbb Z_p},\qquad \widehat{1_{p^k\mathbb Z_p}}=p^{-k}1_{p^{-k}\mathbb Z_p}}$$ ⟹ **球族在 $\mathcal F_p$ 下闭合 ⟹ 族$\leftrightarrow$族是恒等 ⟹ 无交换可言**（命中 #1）✓✓✓；更一般 $\widehat{1_{\mathbb Z_p^\times}}=1_{\mathbb Z_p}-p^{-1}1_{p^{-1}\mathbb Z_p}$ —— **仍是球的组合** ⟹ 乘法群未引出第二个族 ✓；**阿基米德位**：唯一非平凡（$\widehat{1_{[0,1]}}=$ Dirichlet 核，非区间）⟹ **不交换** ✗ ⟹ 综合：**adelic F–M 在有限位自对偶、在 $\mathbb R$ 位不交换** ⟹ **无交换** ✓✓✓；且 $\mathbb R$ **是单个位** ⟹ 无模数乘性分裂 ⊂ 乘积律不可能来自此处。

**⭐⭐ §3 统一结论（核心）**：$$\boxed{\text{「交换」与「乘积律」在算术中位于}\textbf{不相交的位}：\text{交换生于}\ \mathbb R,\ \text{乘积律生于有限位}}$$ 一句话：**要交换就得去 $\mathbb R$，但 $\mathbb R$ 没有乘性；要乘性就得去有限位，但有限位没有交换** ✓✓✓

**§4 终止条件逐条命中**：| #1 不能真正交换 | ✓（2.1／2.3／2.5／2.6）|｜#2 无半群／乘积律 | ✓（2.2／2.4／2.6）|｜#3 只在平均意义 | ✓（2.4）|｜#4 只是已有大筛／G–S／Voronoi 估计 | ✓（2.4／2.5 ＋ `V202` §4）|｜#5 只是显式公式／函数方程重包装 | ✓（2.2 Mellin；2.4 Voronoi $\equiv$ FE）| ⟹ **五条全中** ⟹ 按预设规则 $$\boxed{\textbf{关闭}}$$；**不进入 V204**（唯一可进 V204 的组合「真交换＋乘积律＋新严格缺陷」**未出现**）✓✓✓

**§5 与 `V202` §4 的**同形观察**（模式，非定理）**：`V202` §4 ＝ 大筛法有效区间（$Q\gtrsim\sqrt N$）与 FUP 稀疏需求（$Q\ll\sqrt N$）**相反**；本档 §3 ＝ 交换生于 $\mathbb R$／乘积律生于有限位 **不相交** ⟹ 两档同形：**两个必要条件落在相反区域** ⟹ **层诊断（`V144`）第三次以不同面貌出现** ✓✓（**模式识别，非定理**）。

### F.5bm ⭐⭐⭐⭐⭐ **V204：Arithmetic Spectral-Flow／Index Audit（三步）⟹ 三步全 DEAD，第三步**自败**（对称给的是盲性）**（`V204` ✓ 2026-09-15 13:58）

**委托（唐先生）**：**「继续找'模型发动机'，而不是继续在已经关闭的路线里优化。」** 新候选 ＝ **同伦谱流／index transport**：$$\boxed{\text{局部连续变形}\to\text{谱流整数}\to\text{全局不可改变}}$$ **入口（更严）**：**第一阶段甚至不允许出现 $\zeta,\rho,\gamma,\beta$**；先答纯数学问题 $$\boxed{\text{素数局部数据能否产生一个非平凡、非 Brauer、非 explicit-formula 的}\ K_1／\text{index 类}？}$$ **「如果答案是 0、旧 torsion、Euler-characteristic 重写或 argument principle，立即死。」** 三步：**A** 纯算术 index；**B** 双参数闭环（$\operatorname{SF}(\Gamma)=\sum_{\rm local}\nu_i$，**不得**是已存在的 global explicit formula）；**C** 固定集（$\exists J,J^2=1$，$\nu(J\Gamma)=-\nu(\Gamma)$；若又 $J\Gamma\simeq\Gamma$ ⟹ $\nu=0$）。**致命风险（先写死）**：若 $\nu(\Gamma)=\frac{1}{2\pi i}\oint_\Gamma\frac{\zeta'(s)}{\zeta(s)}ds$ ⟹ **立即关闭**；若 $\nu=$ Li／Weil 正性 ⟹ 关闭。

**§1 引擎确认真实**：$\operatorname{SF}(A_t)\in\mathbb Z$；同伦不变；$K_1$ pairing；**可加记账律** $\operatorname{SF}(A_{t_0},A_{t_m})=\sum_j\operatorname{SF}(A_{t_j},A_{t_{j+1}})$；闭环 $A_0=A_1\Rightarrow\operatorname{SF}(\Gamma)=0$（除非不可去除谱奇点）⟹ 「整数加法守恒」代替 `V202` 的"乘法放大" ✓✓

**⭐ §2 V204-A（本阶段禁用 $\zeta,\rho,\gamma,\beta$）：DEAD** —— **候选 1（局部数据参数族）**：$\zeta$ 的局部因子为 $(1-p^{-s})^{-1}\Rightarrow$ $$\boxed{a_p\equiv1\ \forall p}$$ ⟹ 由 $\{a_p\}$ 构造的族**在 $p$ 方向是常族** ⟹ **无穿越** ⟹ $$\boxed{\operatorname{SF}=0}$$ ⭐ **失败点精确定位**：**不是"算术 index 不存在"，而是"$\zeta$ 的局部数据无变化 $\Rightarrow$ 任何由它构造的族是常族 $\Rightarrow$ index 平凡"** ✓✓✓；**候选 2（Euler-characteristic 型）**：加性、对自对偶复合体恒为 0 ⟹ 命中预设；**候选 3（Brauer／Galois／旧上闭链）**：$K$-类落在 $\mathrm{Br}[N]／H^1／H^2$ ⟹ 命中预设；**候选 4（Hecke／移位算子族 $K_1$）**：确有非平凡 index，**但对应其他 $L$-函数**，对 $a_p\equiv1$ 者**回到候选 1** ⟹ $\operatorname{SF}=0$。⟹ 四候选分别命中"零／Euler-characteristic／旧 torsion／回到零" ✓✓✓

**§3 V204-B：DEAD** —— 闭环的**闭合**必须由**全局算术**提供；canonical 闭合 ＝ 沿 $u=p$（局部／Euler）与 $v=\infty$（scale／archimedean）走一圈，其相消由**乘积公式**给出 ⟹ ⚠️ 而 **`V196` §3.1 已算出该 cocycle 恒为 0**（加法上闭链；$\{\log p\}$ $\mathbb Q$-线性无关 ⟹ 格自由）⟹ $$\boxed{\nu(\Gamma)=0}$$ ⚠️ 若改用**非平凡**全局闭合 ⟹ 那正是**显式公式** ⟹ 命中致命风险 ⟹ DEAD。⭐ 注：此处**复用** `V196` 的**实算结果**，**不回** `V198` 门（属跨线收敛）✓✓

**⭐ §4 V204-C：自败** —— 设 $J^2=1$（功能方程对合 $s\leftrightarrow1-s$ 即为其一）；取 $J$-对称回路（$J\Gamma\simeq\Gamma$）⟹ $\nu(J\Gamma)=-\nu(\Gamma)\Rightarrow\boxed{\nu(\Gamma)=0}$ ⚠️ **但这不是刚性，而是盲性**：对**任何** $J$-对称回路 $\nu=0$，**与配置无关** ⟹ index **对离轴配置完全盲** ⟹ **不可能**用它排除离轴配置；要产生内容必须把 $\nu$ 与配置连起来 ⟹ 唯一连接是 **argument principle**（$\zeta'/\zeta$）⟹ 命中预设致命风险 ⟹ DEAD ✓✓✓。**⭐⭐ 二分宣告（本档最强结论）**：$$\text{对称（}J^2=1\ \text{可用）}\Rightarrow\boxed{\text{盲}};\qquad \text{非对称}\Rightarrow\boxed{\text{失去唯一的算术对合}}\Rightarrow\text{无结构可用}$$ 两条路**互斥** ⟹ **"对称性＋拓扑守恒"作为发动机在算术中无法启动** ✓✓✓ ⭐ 与 `V187` §2 同形（"index／signature 型不变量对离轴对结构性盲"）—— 在**谱流语言中第二次独立复现** ✓✓

**§5 判词与前置问题答案**：$$\boxed{\textbf{V204：三步全 DEAD}}$$（A 常族／index 平凡；B 乘积公式闭合 ＝0；C 对称 ⟹ 盲）⟹ **前置问题（纯数学）答案 ＝ 不能（canonical 构造内）**，失败点 ＝ **"$\zeta$ 的局部数据无变化（$a_p\equiv1$）"**；⚠️ 范围 ＝ canonical 构造，**不**声称"算术 index 不存在"（其他 $L$-函数确有非平凡族）。**根因（模式）**：$\zeta$ 的**有限层无变化** ⟹ 既无变族（A）也无相位（`V144`）也无交换（`V203`）；**阿基米德层是单个位** ⟹ 无回路（B）也无乘性分裂（`V203`）⟹ **`V144` 层诊断第四次以不同面貌出现**（`V200` 组合／`V202` 双局域化／`V203` 交换／`V204` index）✓✓

**§6 重开三条件 ＋ 互斥宣告**：$$\boxed{(1)\ \text{局部数据必须有非平凡变化};\ (2)\ \text{闭环不得经过乘积公式／显式公式};\ (3)\ \text{index 不得在}\ J\text{-对称下恒为 0}}$$ ⚠️ ⭐ **互斥**：本档 §4 已证 (3) 与"使用算术对合 $J$"**逻辑互斥** —— 用 $J$ 对称化则 $\nu$ 必为 0；不用 $J$ 则**失去唯一的算术对合** ⟹ 重开须给出**新的算术对合**（非功能方程）或**非对合型守恒量**；⚠️ 若 $\nu$ 最终 ＝ $\zeta'/\zeta$／Li／Weil ⟹ **立即 DEAD**。

### F.5bn ⭐⭐⭐⭐⭐ **V205：一致性传播／延拓生存（最小模型实算）⟹ 核心发现「死亡需要边界，而算术约束在 $\mathbb N$ 上无边界」⟹ 无死亡、无刚性 ⟹ DEAD**（`V205` ✓ 2026-09-15 14:05）

**委托（唐先生）**：**「V204 不是又死一条路，而是把前三档发动机压缩成结构定理」** $$\boxed{\text{局部守恒量}+\text{全局闭合}+\text{算术对称}\Longrightarrow\text{要么 }0,\text{ 要么显式公式}}$$ 新候选 **V205：约束传播／一致性破缺**：核心 $$\boxed{\text{局部可满足}\ \not\Rightarrow\ \text{无限尺度可延拓}}$$ **「V205 故意没有守恒量：它允许局部状态死亡。」** 三步：**A** 构造最小非平凡算术传播系统（$\mathcal X_N,\pi,e_N,\tau_N$ 全部明确写出并计算）；**B** 是否为 Euler 直积（等号 ⟹ DEAD）；**C** 内生临界指数（不得假定 $1/2$；可调参数 ⟹ DEAD）；**预注册 KILL-1**（可压缩成有限状态 ⟹ DEAD）／**KILL-2**（状态空间只是 $\prod_p\mathcal S_p$ ⟹ DEAD）；**用户自设硬门**：「必须有 $\pi_{N+1,N}$ **不是满射**」（否则有限层非空 ⟹ 逆极限非空）；禁令：第一阶段不放 $\zeta,\rho,\beta$；**先禁止进入 operator／positivity 层**。

**§2 三最小模型实算**：**(2.1) 设计 1（可除边 $c(kp)=F_p(c(k))$）**：一致性（两种分解）⟹ $$\boxed{F_pF_q=F_qF_p}$$ ⟹ $c(n)$ 由 $c(1)$ 唯一决定 ⟹ $$\boxed{\mathcal X_N\cong\Sigma\ \text{（}N\text{-无关）}}$$ π ＝ identity ⟹ $e_N\equiv1$、$\tau_N\equiv\infty$、$\mathcal P_N=\mathcal X_N$ ⟹ **规则逐个素数作用 ＝ Euler 局部 ⟹ KILL-2**；**π 满射 ⟹ 违反自设硬门**；**无死亡 ⟹ 无刚性**；更尖锐：$$\text{整个传播系统退化为单个标签空间，除 }c(1)\text{ 外无算术内容}$$ **(2.2) 设计 2（加法＋乘法精确规则 $c(m+n)=\varphi(\cdot),c(mn)=\psi(\cdot)$）**：$\Sigma$ 得交换半环商结构 ⟹ 有限商分类（**待核**）＝ $\mathbb Z/M$ 的商 ⟹ $$\boxed{\mathbb Z/M\cong\prod_p\mathbb Z/p^{a_p}\ \text{（CRT）}}$$ ⟹ **KILL-1（有限）＋ KILL-2（素数直积）双杀**；且参数是 $M$（**可调**）⟹ 违反 C ⟹ $n\bmod M$ 正是"有限状态＋素数直积"的化身 ✓ **(2.3) 设计 3（无限字母表＋精确算术局部规则）**：经典刚性 ⟹ 解只有 $c(n)=\lambda n$ ⟹ **表示刚性**（解空间只有一条轨道，无法容纳要排除的配置）⟹ DEAD ✓✓✓

**⭐⭐⭐ §3 核心发现（统一根因）**：算术约束系统（$+,\times,\gcd,\mathrm{lcm},v_p$ 型）在 $\mathbb N$ 上是**平移不变＋无边界**的 ⟹ 任何**有限一致状态总能延拓**（用同一批规则继续作用）⟹ $$\boxed{e_N(x)>0\ \ \forall x}$$ ⟹ **无死亡** ⟹ $\mathcal P_N=\mathcal X_N$。**要"杀死"状态必须有边界／端点条件；而 $\mathbb N$ 型算术约束系统没有边界。** ⚠️ 用窗口 $W_N=[N,N+L_N]$（用户提案）：窗口**有**端点，但**平移不变的算术规则不读端点** ⟹ 仍 $e_N>0$；⚠️ 若强行让规则**显式依赖端点** ⟹ **人为植入边界条件** ⟹ 违反 **`V196` §2.1 的 canonical 性判据**（需额外选择）⟹ 非 canonical ⟹ $$\boxed{\text{死亡要么不发生，要么只能人为植入};\ \text{两条都不可接受}}$$

**§4 B／C 答案**：**B**：设计 1／2 均 $$\boxed{\mathcal X_N=\prod_{p\le N}\mathcal X_{N,p}}$$ **等号成立 ⟹ 按用户规则立即 DEAD**；**C**：设计 1 **无指数**（无死亡）、设计 2 的参数 $M$ **可调** ⟹ 按用户规则 DEAD；三设计均**未**内生给出 $\lambda_*=\frac12$，且设计 1／2 **根本没有"临界"概念**。

**§5 三难 ＋ 元结论**：**有限记忆** ⟹ 轨道终将周期 ⟹ **KILL-1**；**无限记忆** ⟹ 任意序列都能被某个约束系统编码 ⟹ **框架空洞（unfalsifiable）**；**精确算术局部** ⟹ 解平凡／状态退化 ⟹ **表示刚性** ⟹ $$\boxed{\text{三难}：\text{有限记忆死}／\text{无限记忆空}／\text{算术局部死}}$$ **⭐ 元结论（最重要）**：不加"**算术局部**"约束 ⟹ 框架**不可检验**；加上 ⟹ 按 §2／§3 死 ⟹ **该框架在可检验的形式下无可行最小模型**。

**§6 判词**：$$\boxed{\textbf{V205-A：DEAD}}$$（三设计全灭：KILL-2／KILL-1+KILL-2／表示刚性；且 π 满射违反自设硬门）；范围 ＝ **canonical 最小模型**；**不**声称"约束传播机制不可能"；⭐ 本档**不依赖** `V198`／`V200`／`V202`–`V204` 的任何判据 —— 死亡原因**内生**于本模型。

**§7 重开四条件 ＋ 相容性要求**：$$\boxed{(1)\ \pi\ \textbf{非满射};\quad(2)\ \text{状态空间无限且非素数直积};\quad(3)\ \textbf{无限记忆复杂度};\quad(4)\ \textbf{内生}\ \lambda_*=\tfrac12\ \text{而非可调}}$$ ⚠️ 须先说明 (1)+(3) 如何与 §3 的"无边界"相容 —— 即**边界从何而来而不人为植入**；⚠️ 若最终退化为 $n\bmod M$／Euler 直积／$\lambda n$ ⟹ **立即 DEAD**。

### F.5bo ⭐⭐⭐⭐⭐ **V206：Canonical Arithmetic Non-Commutativity 存在性审计 ⟹ 第 6 条**成立**（非交换**存在**），但缺陷**局部／无菌** ⟹ 不进入第二阶段**（`V206` ✓ 2026-09-15 14:13）

**委托（唐先生）**：**「V205 把'约束传播'整类模型的可行域边界找出来了」** $$\boxed{\text{canonical arithmetic on }\mathbb N\text{ is too homogeneous to generate an intrinsic killing boundary}}$$ **新发动机 V206：非交换累积** $$\boxed{\text{让"组合顺序"本身产生不可消去的信息}}$$ **不许**把素数变非交换元（人为破坏交换性）；**唯一合法来源 ＝ 算术对象是"从 $n$ 到 $m$ 的变换"**。**六条件**：(1) 对象由整数算术确定 (2) morphism 完全 canonical (3) composition 有定义 (4) 不依赖 $\zeta$／零点／显式公式 (5) 非 Galois／Brauer／$K_2$ 换包装 (6) $\exists f,g:fg\ne gf$。**若 (6) 不存在 ⟹ DEAD（canonical arithmetic relation remains commutative）**；若存在算 $K(f,g)=fgf^{-1}g^{-1}$；**"在这个结果出来之前，不进入 RH。"** **第二阶段门**：noncommutative defect $\to$ **canonical scalar threshold**（阈值不得人为指定；理想内生 $\rho=1$）。

**§1 三候选**：**(甲) $\mathrm{End}(\mathbb N)$／算术函数复合**：$\sigma(n)=n+1,\mu(n)=2n$ ⟹ $\sigma\mu\ne\mu\sigma$ ✓ 但**无算术特异性**（任意集合的 $\mathrm{End}$ 都非交换）⟹ 不合格；⭐ 本档补上隐含要求：范畴必须**算术刚性**。**(乙) 非交换 Galois／Brauer／$K_2$**：绝对 Galois 群**确实非交换**，但**被条件 (5) 排除**（该排除在起作用）。**(丙) ⭐ Dirichlet 卷积 vs 一元（unitary）卷积** —— **命中**：两种 canonical 可分性 $d\mid n$ 与 $d\parallel n$；算子 $D_fh=f*h$、$U_gh=g\times h$；**实算 $n=4$**：$$D_1U_1\delta_1(4)=\sum_{d\mid4}1=3;\qquad U_1D_1\delta_1(4)=\sum_{d\parallel4}1=2\ \Longrightarrow\ \boxed{[D_1,U_1]\delta_1\ne0}$$ 六条件 (1)–(6) **全过** ⟹ **预注册死门未触发** ⟹ 按指示计算 $K$ ✓✓✓

**⭐⭐ §2 $K$ 的显式值**：$$K(n)=[D_1,U_1]\delta_1(n)=d(n)-2^{\omega(n)}$$ (i) $K\ge0$，**等号 $\iff$ $n$ 平方自由** ⟹ **支撑恰为非平方自由整数**；(ii) $K(p^k)=(k+1)-2=\boxed{k-1}$；(iii) $K(n)=\prod_i(k_i+1)-\prod_i2$ ⟹ **只依赖指数型 $(k_i)$ 与 $\omega(n)$，不依赖哪个素数** ✓✓✓

**§3 判定：存在性 YES，但缺陷无菌**：由 (iii) 缺陷**只依赖指数型** ⟹ **不在尺度上累积**（无跨尺度耦合）⟹ $$\boxed{\textbf{无菌}：\text{非交换是真的，但不产生全局刚性}}$$ 且内容为**初等不等式** $d(n)\ge2^{\omega(n)}$（等号 ⟺ 平方自由）⟹ **不产生新的无条件输入** ✓✓✓

**§4 第二道门（§12）不通过**：本结构自然增长量为 $d(n)$ 的**平均阶 $=\log n$**（经典）⟹ **无幂律阈值、尤其无内生 $\tfrac12$**；人为引入 $\rho=1$ 则违反"阈值不得人为指定" ⟹ 按规则 DEAD ⟹ $$\boxed{\text{不进入第二阶段}}$$ ✓✓

**⭐⭐⭐ §5 整类刻画（最重要产出）**：canonical 非交换算术结构 ＝ **两种 canonical 可分性结构的交互**（Dirichlet／unitary／exponential／infinitary／nen 型）；任意两种的卷积算子对**都不交换**，**缺陷均为指数型局部函数** ⟹ $$\boxed{\text{整类 canonical 非交换算术结构都给局部缺陷}\Longrightarrow\text{整类关闭}}$$ ⚠️ 范围：**本档枚举的可分性交互类**；**不**声称"算术非交换不存在"（Galois 型存在，但被条件 (5) 排除）✓

**§6 判词 ＋ 与 `V205` 对照**：(i) 存在性 **YES**；(ii) $K=d(n)-2^{\omega(n)}$ 显式、**局部／初等** ⟹ **无菌**；(iii) 第二道门不通过（对数级、无内生 $\tfrac12$）；(iv) 整类关闭。**同形对照**：`V205` 算术**太均匀** ⟹ 无内生杀伤边界；`V206` 算术**确有非交换**但缺陷**局部化到指数型** ⟹ 无全局累积 ⟹ **两条同形：算术在局部／指数层提供的自由度不进尺度层** ✓✓

**§7 重开四条件**：$$\boxed{(1)\ \text{缺陷非局部};\ (2)\ \text{内生}\ \rho=1\ \text{或}\ \lambda_*=\tfrac12;\ (3)\ \text{跨尺度累积};\ (4)\ \text{非 Galois／Brauer／}K_2\ \text{换包装}}$$ ⚠️ 须先说明 (1) 与 `V205` 的"均匀／无边界"如何相容；⚠️ 若退化为 $d(n)-2^{\omega(n)}$ 型 ⟹ 立即 DEAD。

## F.4 与 §E.4 的关系（✓）

$$\text{§E.4 的活问题 ✓}：\text{"类表（六类）【是否完整】？"}\qquad\text{本节的回答 ✓}：\text{在【第四箭头}／\sqrt{\ }\text{-正性}／\text{稳定性】这三条具体支线上已给出}\textbf{逐项封闭} ✓\ \text{与}\textbf{一个命名残量} ⚠️$$
$$\qquad\Longrightarrow\ \text{本节}\textbf{不} \text{回答 §E.4 的完整性问题 ✗ —— 二者是同一缺口的两个视角 ✓}$$
$$\boxed{\textbf{V137 ＝ SEARCH BRANCH CLOSED}\ ✓\qquad\ne\qquad\text{RH CLOSED}\ ✗}$$
