已查地图：命中（`S2-30-PASS-1-record-and-partial-subtypes` ＋ `AMEND-16`）⟹ 本档为 Pass-2 证据审计，不开新案
D0: 本档对象 = **`S2-30/Pass-2` 审计**：口径锁定 `C=3,P=17,U=10`（`N=30`）＋ `17P` 的 `P1–P4` 逐条证据 ＋ `10U` 的三分（`no-direct-theorem`／`spec-gap`／`search-incomplete`）＋ **指标** `Direct-cover rate` 与 `survival rate` ＋ ⚠️**一条升级建议（`Po02`）**
D1: 1（首次 S2 证据审计；产出分型证据、两项指标与一条口径变更建议）
[RESEARCH]

# **`S2-30 / Pass-2`：证据审计**

## §0 口径锁定（照先生 17:32）

```
$$\boxed{C=3\ (Gr05,Mt01,R03)},\qquad \boxed{P=17},\qquad \boxed{U=10},\qquad N=30$$ ✓✓
$$\textbf{指标}:\quad \boxed{\text{Direct-cover rate}=\tfrac{3}{30}=10\%};\qquad \boxed{\text{survival rate}=\tfrac{27}{30}=90\%}$$ ✓✓
$$\text{注}:\ 90\%\ \textbf{不等于}90\%\ \text{新颖} —— \text{仅表示"未找到直接覆盖"，故只能进入后续阶段}$$ ✓✓
```

## §1 `17P` 逐条证据（`P1` 已有界／`P2` 渐近或一般理论／`P3` 相邻参数／`P4` 部分枚举或数据库）

```
$$\begin{array}{c|c|c|c|c}
\text{ID}&P\ \text{类}&\text{直接文献／数据集（档级）}&\text{覆盖对象}&\text{未覆盖部分（关键列）}\\
\hline
Gr03&P1&\text{图谱最大重数上界（}M(G)\le n-3,\ n\ge4\text{）与一般构造}&\text{上界＋一般构造类}&\boxed{n=11\ \text{完整极值图分类}}\\
Gr04&P1,P3&\text{cubic 图 zero-forcing／maximum-nullity 结构结果}&\text{结构类的界与分类}&\boxed{n\le12\ \text{精确极值表}}\\
Gr07&P1&\text{maximum-nullity／rank defect 系列结果}&\text{一般界与族}&\boxed{\text{小阶极值与达到者}}\\
C01&P1,P4&\text{covering-code bounds／tables（SZTAKI 等）}&\text{bounds＋维护表}&\boxed{\text{具体未收割单元}}\\
C02&P1,P4&\text{covering-code 系统表／历史 bounds}&\text{表与界}&\boxed{n\in\{39,\dots,44\}\ \text{目标值／改进界}}\\
C03&P1,P4&\text{A}_q(n,d)\ \text{exact values＋bounds＋更新表}&\text{已列表格}&\boxed{\text{未列表格的精确值}}\\
D01&P1,P4&\text{La Jolla best-known 数据库}&\text{best-known（非 exact）}&\boxed{C(v,k,t)\ \text{全部 exact}}\\
D02&P3&\text{Steiner existence spectrum（大参数）＋小参数表}&\text{部分参数族}&\boxed{\text{目标 }(v,k)\ \text{缺口}}\\
D05&P3&\text{orthogonal arrays 专门研究与小参数表}&\text{部分参数}&\boxed{\text{小 }v\ \text{完整存在性表}}\\
Au01&P1&{\text{同步字长一般上界（Pin 型）＋小 }n\ \text{验证（边界待核）}}&{\text{上界＋部分 }n}&{\boxed{n\le10,k=2\ \text{精确表 ＋ }(n-1)^2\ \text{逐点验证}}}\\
L01&P3&\text{lattice packing 数据＋经典格密度}&\text{若干维／格族}&\boxed{\text{维 }9\text{–}11\ \text{特定格族精确最优性}}\\
L03&P1&\text{kissing bounds（含 2025 新 lower bounds）}&\text{bounds}&\boxed{\text{维 }10\text{–}11\ \text{精确值}}\\
FF02&P2&\text{五次分圆数理论（Katre–Rajwade／BEW 线）}&\text{一般理论}&\boxed{q=2^k\ \text{该族精确值}}\\
FF07&P2&\text{乘法子群∩加法平移一般理论（Shkredov–Vyugin 线）}&\text{一般界／渐近}&\boxed{\text{小 }q\ \text{完整分类}}\\
G04&P3,P4&\text{S}_n\ \text{子群分类与标准子群数据（GAP 库等）}&\text{分类与数据}&\boxed{n\le12\ \text{指定型共轭类计数表}}\\
FF03&P2&\text{给定 trace 的本原元理论（含 2026 显式枚举线）}&\text{一般结果}&\boxed{(n,t)\ \text{精确表＋偏差谱}}\\
R02&P1,P2&\text{递推 mod }m\ \text{周期理论（Pisano 型）}&\text{一般理论}&\boxed{\text{小 }m\ \text{周期精确分布}}\\
\end{array}$$ ✓✓
$$\textbf{审计规则（照先生）}:\ P1\text{–}P4\ \text{是"已有东西是什么"的分类，\textbf{不是}"距解决还有多远"的评价};\ \text{强上界}+\text{目标为 exact}\ \Longrightarrow\ \text{仍记 }P1,\ \textbf{不得升级为 }COVERED$$ ✓✓
```

## §2 `10U` 三分（**永久区分两种表述**）

```
$$\texttt{U}\to\begin{cases}\texttt{U}_{\rm no\text{-}direct\text{-}theorem}:\ \text{检索到一般理论／数据，但无逐字覆盖}\\
\texttt{U}_{\rm spec\text{-}gap}:\ \text{命题规格不足（现 }Au06\ \text{已补规格，转为待核）}\\
\texttt{U}_{\rm search\text{-}incomplete}:\ \text{本轮检索不完整}\end{cases}$$ ✓✓
$$\begin{array}{c|c|c}
\text{ID}&\text{三分}&\text{本轮最高相关证据／说明}\\
\hline
Gr01&U_{\rm ndt}&\text{图谱枚举文献有；无"n=8 inertia 集完备表"结论}\\
Gr02&U_{\rm ndt}&\text{minimum-rank 文献与部分小阶结果；无"n=9 精确分布"}\\
D08&U_{\rm ndt}&\text{AG(n,3) cap 一般上下界；}\textbf{文献层"n\ge7 未定"是背景，不构成覆盖}\\
Mt02&U_{\rm ndt}&\text{9-element catalogue 存在；无"最小不可表示拟阵"命题覆盖}\\
Po02&U_{\rm ndt}&{\text{见 §3 —— \textbf{本档建议升级为 }COVERED}}\\
Po06&U_{\rm ndt}&{\text{vanishing sums 理论存在（Lam–Leung 线）；有限重极小分类边界待核}}\\
FF06&U_{\rm ndt}&\text{一般 shift/intersection 理论；无"小 q 完整表"}\\
Au06&U_{\rm spec\text{-}gap}\to\text{待核}&\text{规格已补（}qx{+}1,\ x\le10^8\text{）}\Longrightarrow\text{可进入逐字核验}\\
M03&U_{\rm ndt}&{\text{文献明示 }n\ge5\ \text{开放；}\textbf{"开放"}\ne\text{"无覆盖"}\ \text{两者分开记录}}\\
M04&U_{\rm search\text{-}incomplete}&\text{(0,±1)-矩阵 rank 分布；本轮未穷尽检索}\\
\end{array}$$ ✓✓
$$\textbf{禁止表述}:\ \text{"目前没有人做过"};\qquad \textbf{允许表述}:\ \boxed{\text{"截至本轮检索，未取得直接覆盖证据"}}$$ ✓✓✓
```

## §3 ⚠️ 一条升级建议：`Po02` → `COVERED`（附覆盖声明）

```
$$\textbf{候选（逐字）}:\ \text{`xⁿ−1` 在 }\mathbb F_2\ \text{上按次数分解的\textbf{精确计数}（}n\le100\text{）}$$
$$\textbf{覆盖声明（档级，须定点核）}:\ \text{经典事实}:\ x^n-1\ \text{在}\ \mathbb F_q\ \text{上的不可约因子}\ \leftrightarrow\ \text{分圆陪集／}q\text{-项链};\quad \text{次数 }d\mid n\ \text{的因子个数由 Witt／项链计数公式给出}$$ ✓✓
$$\Longrightarrow\ \text{"按次数分解的精确计数"}\ \textbf{被经典公式逐字蕴含}\ \Longrightarrow\ \text{建议 }S2=\boxed{COVERED};\ \text{Decision}=\text{移出}$$ ✓✓
$$\textbf{若确认}:\ \text{口径变}\ \boxed{C=4,\ P=17,\ U=9}\ (\text{Direct-cover rate}=13.3\%);\ \text{否则维持 }3/17/10$$ ⚠️
$$\textbf{另附两条"待定点核"（不主张升级）}:\ \text{`Po06`（Conway–Jones 型有限重分类边界）；`Gr03`（若最大重数达到者分类为\textbf{全 }n}\ \text{的完整定理，则亦应升级 —— 须查其是否含全部构造）}$$ ⚠️
```

## §4 判词与顺序

```
$$\boxed{\text{顺序锁定}:\ (c)\ 3/17/10\ \to\ (a)\ 27\ \text{条证据审计（本档）}\ \to\ (b)\ \text{剩余 }70\ \text{条 }S2\ \to\ S3}$$ ✓✓
$$\boxed{\texttt{S3}\ \text{冻结}} —— \text{待 }100\ \text{条全部过 }S2\ \text{后，再看池子结构 }(C,P_1,\dots,P_4,U,SPEC)$$ ✓✓
$$\textbf{首条正式校准结论}:\ \boxed{\text{S2-30：}30\ \text{条中 }27\ \text{条保留};\ C=3,P=17,U=10;\ \text{survival }90\%}$$ ✓✓
【⛔ 纪律】 本档零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §1/§2 的文献列为**档级（未逐字核）**；§3 为**升级建议**，须定点核后方可改口径 ✓

## §附 【技术词回查】（补录）
```
技术词 audit            命中文件数=312  :: ./EXT-4CT-2026-method-transfer.md ./B-SERIES-INDEX.md ./C3880-standalone-paper-packaging-of-the-cone-separation-assets.md 
技术词 coverage         命中文件数=32   :: ./C3843-global-endpoint-coverage-to-level2-closure.md ./C3-source-hunt-status-three-pdfs-and-remaining-gap.md ./C97-prime-gap-memory-analysis-real-data-N2e7.md 
```
