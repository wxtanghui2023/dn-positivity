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
> **配套 ✓**：`ARCHIVE-V128-V137-fourth-arrow-closure-audit.md`（三条不可越界标签 ＋ 九轮清单 ✓）｜`MASTER` §0.1（J 裁定 ✓）

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
$$\textbf{【}V139\text{ 更新 ✓】材料 A ⟹ 已审 ✓ 退回箱 8；材料 B ⟹ 已审 ✓ 四层塌缩（第 0 层 }\sqrt{|D_K|}\text{ 按定义 ＝ trace pairing Gram 行列式平方根 ⟹ 定义性地 }D_1\text{；第 2 层 }\tfrac12\text{ 非来自维数（应为 }1/d\text{）而来自二次性 ⟹ 违反自身约束 C4 ✗；第 4 层 Brauer–Siegel 下界 ＝ GRH 强度 ⟹ 循环 ✗）⟹ \textbf{三处未执行项中两处已关闭 ✗}，仅剩【修复方向（固定基缺陷）】⛔$$
$$\boxed{\textbf{三处未执行 ⛔}}（各附前置问 ✓）：\text{① 材料 A（不变因子双尺度：指数 }N\text{ 的子格／二次型／理想类）⟹ 前置问：是否退回箱 8／12？}\ \text{② 材料 B（数域余体积 }\sqrt{|D|}\text{ vs 类数 }h\text{）⟹ 前置问：} \sqrt{|D|}\text{ 是【推出】的还是【输入】的？}\ \text{③ 修复方向（固定基缺陷／非对角 transport）⟹ 前置问：能否用【纯算术】给出该相位而不用零点？}}$$

## F.4 与 §E.4 的关系（✓）

$$\text{§E.4 的活问题 ✓}：\text{"类表（六类）【是否完整】？"}\qquad\text{本节的回答 ✓}：\text{在【第四箭头}／\sqrt{\ }\text{-正性}／\text{稳定性】这三条具体支线上已给出}\textbf{逐项封闭} ✓\ \text{与}\textbf{一个命名残量} ⚠️$$
$$\qquad\Longrightarrow\ \text{本节}\textbf{不} \text{回答 §E.4 的完整性问题 ✗ —— 二者是同一缺口的两个视角 ✓}$$
$$\boxed{\textbf{V137 ＝ SEARCH BRANCH CLOSED}\ ✓\qquad\ne\qquad\text{RH CLOSED}\ ✗}$$
