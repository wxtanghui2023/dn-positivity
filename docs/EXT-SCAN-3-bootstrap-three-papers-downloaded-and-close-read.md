已查地图（**先查后写**）：`EXT-SCAN-2`（bootstrap 方法论精读 ＋ ζ-bootstrap 可行性审计：三条结论）、`CEILING-AUDIT-3`（对偶证书）、`V316`／`V185`（67.2%／0.6818）、`V188` §2、`V247`／`V248`、`POS1`、`C-122` 链 A。**本档新增输入**：三份 PDF **已下载并归档**于 `external_refs/`（`bootstrap-2501.18711-tricritical-Ising-CFT.pdf` 1.89 MB／`bootstrap-0807.0004-RRTV2008-4D-CFT-bounds.pdf` 1.56 MB／`bootstrap-1502.02033-SDPB-solver.pdf` 386 KB），并用 `pypdf` 抽取**前 14–26 页**关键段 ✓。关键词回查：`间隙假设`＝0、`oracle 不对称`＝0、`参数无关正性`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 22:59「先下载论文仔细阅读」⟹ **三份全文下载 ＋ 靶向抽取后，得三条比 `EXT-SCAN-2` 更精确的结论** ✓✓：**(甲) ⭐⭐ bootstrap 的严格性需要一个\ \textbf{参数无关的正性公理}**（unitarity：对所有谱、所有 `\Delta` 皆成立）——**这才是它能"一次验证、多次排除"的原因**；**而 ζ 没有这样的公理**（候选只有系数正性（仅 `\sigma>1`）与 Weil 正性（RH 强度）），且 `V248` 独立预测其必落 RH 强度 ⟹ **移植失败点是\ \textbf{公理级}，不是技术级** ✓✓；**(乙) ⭐ 其被测对象是\ \textbf{"间隙假设（gap assumption）"}**（逐字：`\text{"To use a different lower limit }\Delta_*\ \text{of this interval is called imposing a gap assumption"}`）⟹ **我们的"固定 `\delta` 无零区"在其语言里正是一个 gap assumption** ⟹ 两边**问的是同一类问题** ✓✓；**(丙) ⭐ 其输出结构是\ \textbf{单向的（Oracle 不对称）}**（逐字：`p\in P\Rightarrow\{\text{find }\alpha\Rightarrow\textbf{ruled out};\ \text{no }\alpha\Rightarrow\textbf{maybe}\}`）⟹ **"找不到"不是证明**，且**单向严谨结果在文献里是被承认的正式产物**（`\text{bootstrap 的"rigorous intervals"/islands 即如此}`）✓✓

FREEZE-ACK: 本档即冻结期内的外部论文精读与可行性审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **三份 bootstrap 论文的全文下载＋靶向精读**（三条更精确结论：公理级失败点／间隙假设同一性／Oracle 不对称） —— 关系 = 外部精读与移植审计，非新机制
D1: 0

# EXT-SCAN-3 · **bootstrap 三份论文全文精读（下载版）**

> **时间**：2026-09-18 22:59 唐先生：**「先下载论文仔细阅读」** ⟹ 下载 ＋ 靶向精读 ✓

---

## §0 结论（先行）

$$\textbf{(甲)}\ ⭐⭐\ \text{bootstrap 的严格性需要}\ \textbf{参数无关的正性公理};\ \zeta\ \text{没有} \Longrightarrow \textbf{失败点在公理级}✓✓$$
$$\textbf{(乙)}\ ⭐\ \text{其被测对象＝}\textbf{间隙假设};\ \text{我们的"固定}\ \delta\ \text{无零区"}\ \textbf{正是} \text{一个 gap assumption}✓✓$$
$$\textbf{(丙)}\ ⭐\ \text{输出结构}\ \textbf{单向}：\text{find}\ \alpha\Rightarrow\textbf{ruled out};\ \text{no}\ \alpha\Rightarrow\textbf{maybe} \Longrightarrow \textbf{"找不到"不是证明}✓✓$$

---

## §1 三份论文的**逐字**细节（抽取所得）

### 1.1 `2501.18711`（tricritical Ising CFT，62 页）

$$\text{排除逻辑（逐字）}：\text{"If we can find a functional that is }\textbf{positive on all intervals}\text{, equation (3.2) }\textbf{cannot be satisfied}\text{ and the theory with spectrum}\ S_Q\subset D_Q\ \text{is }\textbf{ruled out}\text{"}✓✓$$
$$\textbf{单位性下界（逐字）}：D^{\mathrm{unitarity}}_Q=[\Delta_{\mathrm{u.b.}},\infty),\quad \Delta_{\mathrm{u.b.}}=\begin{cases}(d-2)/2,&\ell=0\\ (d-2+\ell),&\ell>0\end{cases}✓$$
$$\qquad ⭐\ \text{"To use a }\textbf{different lower limit}\ \Delta_*\ \text{of this interval is called imposing a }\boxed{\text{gap assumption}}\text{"}✓✓$$
$$\textbf{Oracle 模式（逐字）}：p\in\mathscr P \Longrightarrow\ \begin{cases}\text{find }\vec\alpha &\Rightarrow\textbf{ruled out}\\ \text{no }\vec\alpha &\Rightarrow\textbf{maybe}\end{cases}✓✓$$
$$\qquad \text{"By testing a grid of points ... this divides the parameter space in allowed and rule-out regions, }\textbf{up to some resolution}\text{"}✓$$
$$\textbf{输出（逐字）}：\text{"scaling dimensions }\textbf{rigorously confined to the intervals}\text{"};\quad \Delta_\phi=0.375405(145)\ (d=2.75)✓$$
$$\textbf{可调杠杆（逐字，两处）}：\text{"the }\textbf{derivative-order}\text{, or consider }\textbf{scanning over more observables/parameters}\text{"}✓✓$$

### 1.2 `1502.02033`（SDPB，34 页）

$$\text{"we compute a new }\textbf{rigorous high-precision bound}\text{ on operator dimensions in the 3d Ising CFT,}\ \Delta_\sigma=0.518151(6),\ \Delta_\epsilon=1.41264(6)\text{"}✓✓$$
$$\textbf{结构}：\text{Polynomial Matrix Programs（PMP）};\ \text{primal／dual 可行性};\ \text{duality gap};\ \textbf{Slater 条件};\ \text{内点法}✓$$
$$\qquad \Longrightarrow \textbf{严格性＝对偶可行性／最优性证书} \Longrightarrow \text{与}\ \text{`CEILING-AUDIT-3`}\ \text{的"对偶证书"}\ \textbf{同名同物}✓✓$$

### 1.3 `0807.0004`（RRTV 2008，49 页）

$$\text{首个"}\Delta_{\min}\le\Delta_c\text{"型界};\ \textbf{逐字}：\text{"Otherwise such a CFT will be }\textbf{ruled out}\ \text{by the same argument as a CFT without any scalars in the OPE}\text{"}✓$$
$$\qquad \text{（本档仅抽前 26 页；该档核心推导在后续页，标`[部分读]`）}✓✓$$

## §2 ⭐ (甲) 失败点在**公理级**（本档最重要的结论）

$$\text{bootstrap 的排除为何能"一次验证、多次排除"}：\text{正性}\ \lambda_Q^T\vec\alpha[\vec V_Q]\lambda_Q\ge0\ \text{来自}\ \textbf{unitarity}✓$$
$$\qquad \Longrightarrow \text{该正性}\ \textbf{不依赖于被检验的参数}\ p \Longrightarrow \text{对}\ \textbf{所有谱、所有}\ \Delta\ \text{皆成立}✓✓$$
$$\text{ζ 侧的对应物}：\text{需要一个}\ \textbf{同样"参数无关"的正性公理};\ \text{候选只有}：$$
$$\qquad \text{(i)}\ \text{系数正性（}\Lambda(n)\ge0\text{）} \Longrightarrow \textbf{只在}\ \sigma>1 \Longrightarrow \text{给}\ \sigma=1\ \text{级信息}（\text{`C-122` 链 A}）✗$$
$$\qquad \text{(ii)}\ \text{Weil 正性} \Longrightarrow \textbf{RH 强度}（\text{`POS1`}）✗$$
$$\Longrightarrow \text{且按}\ \textbf{`V248`}（判别锥必自对偶 ⟹ 单二次型 ⟹ 角 I） \Longrightarrow \textbf{bootstrap 式正性对 ζ 必落 RH 强度}✓✓$$
$$\Longrightarrow \boxed{\text{移植失败点是}\ \textbf{公理级}（缺参数无关正性），\ \textbf{不是技术级}}✓✓$$
$$\qquad \text{（即：无限族方程、线性泛函、SDP、对偶证书——}\textbf{机器全都在}）✓$$

## §3 ⭐ (乙) 被测对象＝"间隙假设"，与我们**同类**

$$\text{bootstrap 检验的是}：\text{"存在一个}\ \textbf{谱间隙}\ \ge\Delta_*\ \text{的自洽理论吗"}✓$$
$$\text{我们要检验的是}：\text{"存在一个}\ \textbf{零点间隙}\ \text{（无零点于}\ \beta>\tfrac12+\delta\text{）的自洽配置吗"}✓✓$$
$$\Longrightarrow \textbf{同类问题}：\text{都是"}\textbf{给一致性条件 ＋ 正性，问某间隙假设是否可行}\text{"}✓✓$$
$$\qquad \Longrightarrow ⭐\ \text{这把我们的目标从"证明 RH"重述为}\ \textbf{一个可行性／排除问题}✓✓$$

## §4 ⭐ (丙) Oracle 不对称：**单向结果是正式产物**

$$\text{逐字}：\text{find}\ \alpha\Rightarrow\textbf{ruled out};\quad \text{no}\ \alpha\Rightarrow\textbf{maybe}✓✓$$
$$\Longrightarrow \text{"找不到"}\ \textbf{不是证明}\ \text{——但}\ \textbf{单向的严格排除是文献承认的正式结果}（\text{rigorous intervals／islands}）✓✓$$
$$\qquad \Longrightarrow \text{对我方的意义}：\text{我们的}\ 0.6818\ \text{天花板、}\ 67.2\%\ \text{下界}\ \textbf{同属这一类} \Longrightarrow \textbf{不必为"单向"自卑}✓$$
$$\qquad ⚠️\ \text{但须与}\ \text{`C-116`}\ \text{一致}：\text{单向}\ \textbf{严谨排除} \text{（有证书）}\ \neq\ \text{归纳式"找不到"（无证书）}✓✓$$

## §5 可操作提案（由精读直接得出）

$$\textbf{P1（oracle 模式重述）}：\text{把我方问题写成}：\text{"给定}\ \text{显式公式 ＋ 泛函方程（一致性）＋ }\ \textbf{某正性代理} \text{，}\ \text{问"}\beta>\tfrac12+\delta\ \text{是否可行"}\text{"}✓$$
$$\qquad \text{我方已有}\ \textbf{正性代理}＝\text{`V316` 的 rank–trace／惯性不等式} \Longrightarrow \text{这正是}\ \textbf{一个 relaxation}✓✓$$
$$\qquad \Longrightarrow \textbf{0.6818}\ \text{＝该 relaxation 的值};\ \text{要抬它，}\ \text{按 bootstrap 的两条杠杆}：$$
$$\qquad \qquad \text{(i)}\ \Lambda\uparrow（\text{更高阶项}）;\quad \text{(ii)}\ \text{更多 observables（更多一致性方程）}✓✓$$
$$\qquad \Longrightarrow \text{我方对应：}\text{(i)＝测试函数的高阶项；}\text{(ii)＝更多独立性条件} \Longrightarrow \textbf{前者受 bandwidth 限，后者受}\ \text{`V188` §2 饱和限}✓✓$$
$$\textbf{P2（gap assumption 记法）}：\text{今后写"固定}\ \delta\ \text{无零区"时}\ \textbf{并列写"gap assumption}\ \Delta_*"\ \text{（便于与文献对表）}✓$$

## §6 边界与回查

- ⚠️ 三份 PDF **已下载并归档**（`external_refs/`）；抽取仅**前 14–26 页**，且为**自动抽取**（可能有字符噪声）⟹ 标 `[部分读·抽取级]`；`0807.0004` 核心推导在后续页，未读 ✓
- ⚠️ §2／§3／§5 为**本档判断**（非定理）✓
- ⚠️ **不声称** bootstrap 不可移植；仅**定位失败点为公理级** ✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:0x）`[纪律]`（先跑后写）

```
技术词 间隙假设       命中文件数=0  ⟹ 本档新增
技术词 oracle 不对称   命中文件数=0  ⟹ 本档新增
技术词 参数无关正性     命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
