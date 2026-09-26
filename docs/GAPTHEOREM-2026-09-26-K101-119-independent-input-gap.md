已查地图：已跑 scripts/prework_map_check.sh K(10,1) 缺口 十条机制 ⟹ 本档为**总账档**，逐条引用既有细档（`B2QUOTA`/`SUM-P1P4`/`GRAMSIGN`/`PACKB`/`ISOB3`/`STAR3`/`TCOLL`/`SCOL`/`HQ1`/`MIDSUP`/`K1AUDIT`/`L4AUDIT`/`ADJCOUP` ✓）。
D0: 本档对象 = 119 线（$K_2(10,1)=119$ 排除 $Q=1$）的**缺口定位**（既有对象）
D1: 0（产出为缺口陈述的严格化与机制清单冻结）

# GAPTHEOREM-2026-09-26 · 119 线的独立输入缺口（诊断性总账）

## §0 陈述（严格限定 ✓）

```
$$\boxed{\textbf{缺口陈述}:\ \text{在 }Q=1\ \text{分支下，下列机制族在该点的投影\textbf{均为恒等式／上界／弱界}，}\Rightarrow\ \text{均\textbf{未覆盖} P3 缺口}\ ✓}$$
$$\textbf{十族}:\ \text{线性局部求和}\ \to\ \text{二次符号}\ \to\ \text{双重计数}\ \to\ \text{packing 方向}\ \to\ \text{行闭合}\ \to\ \text{Haas×}Q_1\ \to\ \text{中点 load}\ \to\ \text{层限制}\ \to\ L_4\ \text{局部图}\ \to\ \text{相邻耦合}\ ✓$$
$$\textbf{被排除的陈述}:\ \boxed{\text{“上述十族在 }Q=1\text{ 点\textbf{不能}覆盖缺口”}}\ ✓;\qquad \textbf{未被排除}:\ \boxed{\text{“该缺口\textbf{不可能}被覆盖”}}\ ✗\ \text{（严禁外推 ✓）}$$
$$
$$
```

**一句话形式（唐先生指定 ✓）**：

```
$$\text{低阶局部计数}＋\text{中点 load}＋\text{incidence}＋\text{相邻耦合}＋\text{现有 SDP}\ \not\Rightarrow\ 119\ ✓$$
```

## §1 十族逐条（对象／为何不足／细档）

```
$$\textbf{(1) 线性局部求和}\ \text{AMEND-30 LOCAL-AVG-GATE}:\ \text{线性泛函}\ \sum_j c_jA_j(z)=M\sum_jc_jC(n,j)\ \text{恒为定值}\ ⟹\ \text{无码依赖信息}\ ✗\ (\rho=3/12.52)$$
$$\qquad\ \text{细档}:\ \texttt{SUM-P1P4-2026-09-26-...md}\ ✓$$
$$\textbf{(2) 二次符号}\ \text{GRAMSIGN}:\ \text{Gram-LIFT 族系数全非负}\ ⟹\ \text{只给下界，无上界方向}\ ✗;\ \text{区间}\ [143,213]\ \text{未收紧}$$
$$\textbf{(3) 双重计数}\ \text{ISOB3}:\ \text{局部 excess}\ \longleftrightarrow\ \text{距离-2 度}\ \text{映射为\ 2-对-1}\ ⟹\ \text{恒等式而非不等式}\ ✗$$
$$\textbf{(4) packing 方向}\ \text{TCOLL}:\ \text{服务名额约束}\ A_i+2B_i+C_i\le6\ \text{为上界}\ ⟹\ \text{方向相反（需下界）}\ ✗$$
$$\textbf{(5) 行闭合}\ \text{SCOL}:\ \text{行闭合引理严格}\ ✓\ \text{但强制点仅}\ O(1)\ (7/18/50/57)\ \ll\ 905\ ✗$$
$$\textbf{(6) Haas×}Q_1\ \text{HQ1}:\ \text{一阶层式恒等式}\ \sum\delta_i=C(10,i)E\ ⟹\ \text{代入后} A_1\ \text{依赖消失}\ ✗;\ \text{二阶含}P_1\ \text{但}\ \text{GRAMSIGN}\ \text{定符号}\ ✗$$
$$\textbf{(7) 中点 load}\ \text{MIDSUP}:\ \text{distinct support 钉死}\ ✓\ \text{但 load \textbf{逐点自动满足}}\ ⟹\ \text{无松弛可利用}\ ✗$$
$$\textbf{(8) 层限制}\ \text{K1AUDIT}:\ \text{“中点必落 }L_2/L_4\text{”}\ \textbf{数值否证}\ ✗\ (\text{中点层集可为}\ 0..10\ ✓)$$
$$\textbf{(9) }L_4\ \text{局部图}\ \text{L4AUDIT}:\ G_m\ \text{框架有效}\ (4\le r(m)\le9\ ✓)\ \text{但无矛盾}\ ✗$$
$$\textbf{(10) 相邻耦合}\ \text{ADJCOUP}:\ N_{G_{m'}}(k)=S(m)\ \textbf{正确但为恒等式}\ ⚠️;\ |S\cap S'|=0/1/2\ \text{三支均无矛盾}\ ✗$$
$$\textbf{(11 外部) 现有 SDP}\ \text{(L2AUDIT)}:\ (2,10,1)\ \text{格}=105.2223\Rightarrow K\ge106<107\ \text{仍远低 119}\ ✗$$
$$
$$
```

## §2 结构性诊断（本档结论 ✓）

```
$$\textbf{共同特征}:\ \text{十族\textbf{全部}只触及}\ \sum_xf(\delta(x))\ \text{或}\ \sum_xf(\delta_i(x))\ \text{型（\textbf{逐点函数之和}）}\ ✓$$
$$\qquad\Longrightarrow\ \text{而}\ Q=1\ \text{的指纹}\ (\sum\delta=285,\ \sum\binom{\delta}{2}=1,\ \delta\in\{0,1,2\})\ \textbf{恰把这些和钉到恰好}\ ✗\ \text{（既不太紧也无松弛）}$$
$$\textbf{缺口真正形态}:\ \text{需要一条依赖“\textbf{哪些点同时取哪个 }\delta\textbf{ 值}”的约束}\ ——\ \text{即\textbf{支撑型（support）约束}}\ ✓$$
$$\qquad\text{已尝试的支撑型入口（第 9/10 族）给出}\ O(1)\ \text{强制点}\ll\ 905\ \Longrightarrow\ \text{量级不足}\ ✗$$
$$\textbf{量级陈述（可复核 ✓）}:\ \text{任一可用机制的强制量}\ \lesssim57\ \text{点};\ \text{所需}\ \sim905\ \text{规模};\ \text{比}\ \approx16\times\ ✗$$
$$
$$
```

## §3 状态与用途（冻结 ✓）

```
$$\textbf{119 状态}:\ \textbf{UNKNOWN}（\text{未排除};\ \text{未构造}）\ ✓;\ \text{上界 120 已知（Östergård 构造）};\ \text{下界 107（BÖW 2004）};\ \text{新 SDP 106}\ ✓$$
$$\textbf{本档用途（消费规则 ✓）}:\ \text{今后任何复用 119 线者，须声明消费何者}:\ \text{① 十族“已试且不足”清单};\ \text{② 缺口 = 支撑型约束;\ ③ 量级门槛}\ \sim905$$
$$\textbf{禁止用法}:\ \text{把本档读成“119 不可达”或“低阶计数无用”}\ ✗;\ \text{把 }\sum\text{-型恒等式的新包装当作新机制}\ ✗$$
$$
$$
```

## §4 边界（诚实标注）

- §1 十族**逐条有细档** ✓（本档为汇总，不新造数学 ✓）
- §2 的"共同特征"为**本档归纳** ✓（基于十族各自的投影结果 ✓），**非**定理 ⟹ 标注为**结构性诊断** ✓
- §2 的量级"≈16×"为**点数量级比较** ✓（57 vs 905 ✓），**非**严格不可能性 ✓
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗、**未**主张方法穷尽 ✗
- **未跑**程序 ✓（仅汇总；个别细档含验证计算，已各自标注 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 独立输入缺口陈述 命中文件数=1    :: ./GAPTHEOREM-2026-09-26-K101-119-independent-input-gap.md 
技术词 十族汇总     命中文件数=1    :: ./GAPTHEOREM-2026-09-26-K101-119-independent-input-gap.md 
技术词 支撑型约束判定 命中文件数=1    :: ./GAPTHEOREM-2026-09-26-K101-119-independent-input-gap.md
```
- **本档新增**：独立输入缺口陈述、十族汇总、支撑型约束判定（见上方命中数）
- **档案已有（引用，不列为提出）**：AMEND-30、GRAMSIGN、ISOB3、TCOLL、SCOL、HQ1、MIDSUP、K1AUDIT、L4AUDIT、ADJCOUP、L2AUDIT
