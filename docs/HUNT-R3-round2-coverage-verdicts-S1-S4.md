已查地图：命中（`HUNT-R3-round1-supply-inventory`）⟹ 第二轮覆盖判定，不开新案
D0: 本档对象 = **`S1`–`S4` 的 `AMEND-20/21` 判定（四项全 CLOSED）** ＋ 逐项证据 ＋ **硬停止执行（离开 `S1`–`S4`，回 `L1/L3/L4`）** ＋ 本轮元发现（2026 新条目半衰期短／"接口已覆盖"是主杀手）
D1: 0（审计型，零计算）
[REVIEW]

# **`HUNT-R3` 第二轮：`S1`–`S4` 覆盖判定**

## §0 本轮唯一问题与判据

```
$$\text{唯一问题}:\ \boxed{\text{AMEND-20/21 后，是否存在真正未覆盖的对象？}}$$
$$\text{“未覆盖”须三项同时成立}:\ \boxed{\text{对象未覆盖}\ \wedge\ \text{参数化未覆盖}\ \wedge\ \text{充分/必要条件未覆盖}}$$
$$\qquad \textbf{不是}\ \text{“我没搜到这篇论文”};\quad \textbf{且}\ \boxed{\text{问题仍开放但现有方法已覆盖攻击接口}\Rightarrow\text{照样 CLOSED}}$$ ✓✓
$$\text{本轮}\ \textbf{零计算};\ \textbf{未提前讨论“哪个更值得做”}$$ ✓
```

## §1 判定表

```
$$\begin{array}{c|l|l|c}
\text{项}&\text{AMEND-20}\ (\text{族字面检索＋等价参数化})&\text{AMEND-21}\ (\text{三合一})&\text{结论}\\\hline
S1&\text{命中}:\ \texttt{arXiv:2608.24202}\ (\textbf{2026-08})\ \text{《Induced-saturated graphs exist for even cycles》};\ \texttt{arXiv:2505.24100}\ (2025)\ \text{《Halfway to induced saturation for even cycles》};\ \text{Oxford《Infinite induced-saturated graphs》(2025)};\ \texttt{arXiv:2609.21388}\ (2026\text{-}09)&\boxed{\text{对象未覆盖 ✗}}:\ \text{2026-08 已对一切偶环给出诱导饱和图构造（“for every integer }q\ge3\text{ construct }C_{2q+2}\text{-induced-saturated}”）&\boxed{\textbf{CLOSED}}\\
S2&\text{等价参数化命中}:\ p(m,n)\ \text{（Urrutia 等《Efficient Regular Polygon Dissections》）——\textbf{正 }m\text{ 边形}\to\text{正 }n\text{ 边形（含三角形目标）的最小块数框架}，\text{含 }\lceil n/3\rceil\ \text{glass-cut 下界与渐近界};\ s(n)/r(n)/q(n)\ \text{（Sloane 2023《On Dissecting Polygons into Rectangles》, Table 1）}&\boxed{\text{参数化未覆盖 ✗}}:\ \text{目标为三角形的情形落在已研究的 }p(m,3)\ \text{内};\ \text{下界方法仅对 glass-cut 类成立}\Longrightarrow\boxed{\text{攻击接口已覆盖}}&\boxed{\textbf{CLOSED}}\\
S3&\textbf{对象已冻结}:\ \texttt{A046057}\ =\ \text{moa}(n)\ =\ \boxed{\text{恰有 }n\ \text{个同构类有限群的\textbf{最小阶}}};\\&\qquad\qquad \text{文献}:\ \text{Conway–Dietrich–O'Brien 2008《Counting groups: gnus, moas}\ldots\text{》（命名并研究）;\ Horn《Numbers of isomorphism types…》表};\ \text{附猜想（Dennis：无 0）}&\boxed{\text{充要条件未覆盖 ✗}}:\ \text{moa 之定义／计算框架已建立；“无 0”猜想已登记};\ \text{剩余缺口为}\textbf{规模型}（依阶递推搜索）\Longrightarrow\ \text{且 LANE-A ④「非纯算力堆砌」不满足}&\boxed{\textbf{CLOSED}}\\
S4&\text{对象已冻结}:\ \text{Barbados 2026 问题 24（诱导子式封闭族是否“小”）};\ \text{等价}:\ \text{诱导子式封闭类的计数函数 vs 子式封闭类的 }n!\,c^n&\boxed{\text{覆盖＋2026 内推进 ✗}}:\ \texttt{arXiv:2607.12090}\ (2026,\ \text{Chudnovsky 等})\ \text{给出诱导子式封闭类的}\textbf{完整分类}（tree-independence 亚多项式／线性／平方根…）；2025 年 }\{K_{t,t},W_{t\times t}\}\ \text{结果}\Longrightarrow\ \text{结构接口已覆盖}&\boxed{\textbf{CLOSED}}\\
\end{array}$$ ✓✓
```

## §2 硬停止执行（照先生令）

```
$$\boxed{\text{四项全 CLOSED}\Longrightarrow\text{离开 }S1\text{–}S4,\ \text{回 }L1/L3/L4\ \text{重新抽取}}$$ ✓✓
$$\textbf{禁止}:\ \text{在 }S1\text{–}S4\ \text{内改参数硬救（\textsc{amend-22}）}$$ ✓
$$\textbf{尚未开采的 }L1/L3/L4\ \text{子池（下一轮输入）}:$$
$$\qquad L1:\ \text{Open Problem Garden（图论 227／代数 298 条目级抽取）};\ \texttt{erdosproblems.com}\ \text{未审条目};$$
$$\qquad L3:\ \text{组合 Gray 码综述 }\texttt{DS26}\ \text{所提问题集};\ \text{设计理论开放问题汇总（BIBD 块相交图等）};\ \text{Cooper 问题集};\ \text{ICM 2026 猜想};\ \text{MathWorld 未解表};$$
$$\qquad L4:\ \text{Joyner–Kim《Selected Unsolved Problems in Coding Theory》条目级抽取}.$$
$$\textbf{旗标仍然生效}:\ R1\ (\text{OEIS 子集已被 AI 攻击}\Rightarrow\text{逐条查});\ R2\ (\text{Green 100 问题＝高覆盖});\ R3\ (\text{著名条目降末位});\ R4\ (\text{当年度新表须核 2026 内新解})$$
```

## §3 本轮元发现（供未来抽取用）

```
$$\textbf{(1) 2026 新条目的半衰期很短}:\ S1\ \text{来自 2026 Barbados 表，}\textbf{同年 8 月即被解决};\ S4\ \text{同年 7 月已出“完整分类”}$$
$$\qquad \Longrightarrow\ \text{“当年度新表 + 未收割”组合}\textbf{并不安全};\ \text{须逐条核当年预印本（本轮 }R4\ \text{旗标被实证}$$ ✓✓
$$\textbf{(2) “接口已覆盖”是本轮主杀手}:\ S2\ (\text{参数化落入 }p(m,n))\ \text{与}\ S3\ (\text{框架已建、剩余为规模型})\ \text{皆因}\textbf{攻击接口被现有方法覆盖}\ \text{而 CLOSED}，\textbf{与“问题是否仍开放”无关}$$ ✓✓
$$\textbf{(3) 对未来抽取的校准}:\ \text{优先取}\boxed{\text{记录型（证书型）缺口}}\ \text{而非}\boxed{\text{证明型（下界型）缺口}};\ \text{因后者攻击接口通常已被下界方法覆盖，且非 LANE-A 可交付}$$ ✓✓
【⛔ 纪律】 本轮**零计算**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 判定证据为**检索抽取级**；`S2` 之 `A110000` 逐字条目**未取**（经 style-sheet 摘要确认对象）；不得据以宣称“该类问题不存在” ✓

## §附 【技术词回查】（补录）
```
技术词 coverage verdict 命中文件数=0    :: 
技术词 interface covered 命中文件数=0    :: 
```
