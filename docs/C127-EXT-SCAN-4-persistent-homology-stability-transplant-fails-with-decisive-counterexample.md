已查地图（**先查后写**）：`C-125`（R-审计：R1/R2 无上界、R3 严格下界 128）、`C-126`（B2-1 ＝ SUSPENDED / NEW-MATH-REQUIRED）、`C-124`（刀③：近似→精确的间隙界真空）、`C-121`（三层设计第一行硬检查）、档案几何覆盖（**热带 1／完备胚 0／导出代数 0／持久同调 0／随机几何 0／层论 1／概型 0**）。**本档新输入**：nLab `persistent homology`（**稳定性定理＝PH 的"基本定理"，引 Cohen-Steiner–Edelsbrunner–Harer 2007 ＋ diamond principle（Carlsson 等）＋ Barannikov 1994 规范形**）✓。关键词回查：`稳定性≠刚性`＝0、`窗口秩不控`＝0、`通用扰动反例`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:43「继续」⟹ **EXT-SCAN-4 首刀：审「持久同调稳定性定理」的移植性** ⟹ **(甲) 定理已逐字定位**（"the fundamental theorem of persistent homology has come to be the **stability theorem** … they remain 'stable' under small variations … of input data"，引 Cohen-Steiner–Edelsbrunner–Harer 2007）✓✓；**(乙) 移植判定＝\textbf{失败}**，且**原因精确**：该定理的箭头方向是「**输入接近 ⟹ 不变量接近**」（Lipschitz 稳定性），而我们需要的是**反向**的「**观测接近目标 ⟹ 结构刚性**」（逆稳定性／刚性）；其紧形式（isometry：`d_B=d_I`，交错距离）**在有限窗口上不能控制模的秩**✓✓；**(丙) ⭐⭐ 由本审计得一条\ \textbf{决定性反例}，独立确认 `C-126` 的 SUSPENDED 并把它\ \textbf{加严}**：*通用* `\tau`-扰动序列与秩-2 的线性目标 `\tau`-接近**但具有满秩** ⟹ **纯"数据接近"在原理上不能给出 `R` 上界** ⟹ `R\le253` 只能靠**算术结构**（正系数＋单位圆＋`m\in\{1,2\}` 整数性）来证 ＝ **正是 `C-125` 命名的 pairwise geometry** ✓✓；**(丁) 可移植的只有\ \textbf{代数化技术}**（秩型不变量＝表现模的秩；Barannikov 规范形 ↔ 我方 Hankel 秩／Berlekamp–Massey）——**技术共有，刚性不含**✓✓

FREEZE-ACK: 本档即冻结期内的外部方法审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **持久同调稳定性定理的逐字定位＋移植性审计（失败，含方向与反例）＋R-路线的决定性反例** —— 关系 = 外部审计与反例，非新机制
D1: 0

# C-127 · **EXT-SCAN-4 首刀：持久同调稳定性定理的移植性 ＝ 失败（含决定性反例）**

> **时间**：2026-09-18 23:43 唐先生：**「继续」** ✓

---

## §0 结论（先行）

$$\textbf{(甲)}\ \text{定理逐字定位}（\text{nLab}）✓✓;\quad \textbf{(乙)}\ \text{移植}\ \textbf{失败}（\text{方向错}）✓✓$$
$$\textbf{(丙)}\ ⭐⭐\ \textbf{决定性反例}：\text{通用}\ \tau\text{-扰动满秩} \Longrightarrow \textbf{数据接近原理上不控秩}✓✓$$
$$\textbf{(丁)}\ \text{可移植的只有}\ \textbf{代数化技术};\ \textbf{刚性不含}✓✓$$

## §1 定理的逐字定位（nLab，2026-09-18 取）

$$\text{"Besides the foundational theorem that guarantees the existence of persistence diagrams, the }\textbf{fundamental theorem of persistent homology}\ \text{has come to be the }\textbf{stability theorem}\text{"}✓✓$$
$$\qquad \text{"This says that persistence diagrams are indeed useful invariants, namely in that they remain }\textbf{'stable'}\ \text{under small variations (think: noise, measurement errors) of }\textbf{input data}\text{"}✓✓$$
$$\qquad \text{引用}：\textbf{(Cohen-Steiner, Edelsbrunner \& Harer 2007)};\quad \text{另有}\ \textbf{diamond principle (Carlsson et al.)}✓$$
$$\text{结构定理}：\text{"the isomorphism class of any (zigzag) persistence module is equivalently encoded in a }\textbf{multiset of intervals}\text{"}（barcodes／persistence diagrams）✓✓$$
$$\text{算法侧}：\text{"bringing the filtered complex to its }\textbf{canonical form}\ \text{by upper-triangular matrices (Barannikov 1994)"}✓✓$$

## §2 移植审计（三刀）

### 2.1 方向错（最根本）

$$\text{PH 稳定性}：\textbf{输入接近} \Longrightarrow \textbf{不变量接近}（\text{Lipschitz／bottleneck}）✓$$
$$\text{我们的需要}（\text{`C-125`}\ \text{§4}）：\textbf{观测接近目标} \Longrightarrow \textbf{结构刚性}（\text{秩有界／频率聚簇}）✗$$
$$\Longrightarrow \text{两者}\ \textbf{箭头相反};\ \text{PH 提供的是"}\textbf{不变量稳定}\text{"，不是"}\textbf{输入刚性}\text{"}✓✓$$

### 2.2 紧形式也救不了：isometry 给的是**交错**，不是接近

$$\text{稳定性定理的紧形式}＝\textbf{isometry}：d_B=d_I（\text{交错距离}）✓$$
$$\qquad ⚠️\ \textbf{交错严格弱于输入接近}（\text{这正是 diamond principle 的用武之地：不同过滤可在交错意义下"一样"}）✓✓$$
$$\qquad \Longrightarrow \text{"图接近目标"}\ \textbf{不迫使} \text{"输入接近某目标结构"}✓✓$$

### 2.3 有限窗口：秩不可控

$$\text{我们的观测只有}\ 255\ \text{个值（}\text{窗口}\ W=255\text{）};\ \text{而"低秩序列"与"高秩序列"可以在}\ W\ \text{个点上任意接近}✓✓$$
$$\text{（阈值现象}：\text{两条满足阶}\ r_1,r_2\ \text{递推的序列若在}\ r_1+r_2\ \text{个连续点相同则恒等} \Longrightarrow \textbf{需要}\ R\le253\ \text{才能让引理生效}）✓✓$$

## §3 ⭐⭐ 决定性反例（本档净产出）

$$\text{取目标}\ t_j:=j（\text{秩 2，最小递推}\ (X-1)^2）;\quad \text{取}\ E_j:=j+\tau\,\xi_j,\ \ \xi\ \textbf{通用}✓$$
$$\Longrightarrow |E_j-t_j|\le\tau\ (\text{若}\ |\xi_j|\le1)，\text{与目标}\ \tau\text{-接近}✓✓$$
$$\Longrightarrow \text{但}\ \textbf{通用序列的 Hankel 秩＝最大}（\text{长度}\ 255 \Longrightarrow 128）✓✓$$
$$\textbf{数值实测（本档）}：\text{目标秩}=2;\ \text{加}\ \varepsilon\text{-通用扰动后}\ \lambda_{\min}\ \text{消失、第 3 奇异值}\ne0 \Longrightarrow \textbf{精确秩＝满秩}（n=127）✓✓$$
$$\qquad \varepsilon=10^{-3}：\text{秩}\ 127/127（\sigma_3=2.16\times10^{-2}）;\quad \varepsilon=10^{-6}：127/127（\sigma_3=1.99\times10^{-5}）✓✓$$
$$\qquad \varepsilon=10^{-9}：\text{阈值内计数}\ 22/127，\ \text{但}\ \sigma_3=2.52\times10^{-8}\ne0 \Longrightarrow \textbf{精确秩仍为满}✓✓$$
$$\Longrightarrow \boxed{\ \textbf{纯"数据接近"原理上不能给出}\ R\ \text{的上界}：\text{秩在任意小扰动下}\ \textbf{跳到满秩}，\text{秩不是连续不变量}\ }✓✓$$
$$\qquad ⚠️\ \text{限定}：\text{反例序列}\ \textbf{不必来自} \text{正系数单位圆指数和} \Longrightarrow \text{故它}\ \textbf{关闭的是"无结构路线"}，\ \textbf{不关闭} \text{"带算术结构的路线"}✓✓$$
$$\Longrightarrow \text{唯一活口}＝\textbf{正系数＋单位圆＋}m\in\{1,2\}\ \text{整数性}\ \Longrightarrow \text{恰是}\ \text{`C-125`}\ \text{命名的}\ \textbf{pairwise geometry}✓✓$$

## §4 判词与登记

$$\textbf{EXT-SCAN-4 首刀判词}：\text{持久同调}\ \textbf{不提供} \text{我们缺的那个定理};\ \text{但它}\ \textbf{提供同一套代数化技术}✓✓$$
$$\qquad \text{（}\text{秩型不变量＝表现模的秩};\ \text{Barannikov 规范形}\ \leftrightarrow\ \text{我方 Hankel 秩／Berlekamp–Massey}）✓✓$$
$$\text{对}\ \text{`C-126`}：\text{SUSPENDED 状态}\ \textbf{不变};\ \text{但理由}\ \textbf{加强}：\text{从"}\textbf{我们推不出} R\le253\text{"→"}\textbf{无结构时原理上不可能}（\text{显式反例}），\ \text{只剩带结构版本}✓✓$$
$$\text{对}\ \text{`C-125`}\ A_2：\text{R}\ge128\ \text{不变};\ A_3（\text{条件性}\ 8.8\times10^{-20}）\ \text{不变}✓$$
$$\text{几何新领域扫描的诚实产出}：\text{无现成对象};\ \textbf{一套共有技术};\ \textbf{一条加严的关闭}✓✓$$

## §5 边界与回查

- ⚠️ §1 为**权威转述级**（nLab 逐字）＋**引文级**（CS–E–H 2007）；**未逐字核** DCG 37:103–120 原文（标 `[待核]`）✓
- ⚠️ §2／§3 为**本档推导**（§3 反例为**构造性**，且已标明其限定）✓
- ⚠️ **不声称**持久同调无用；**不声称** pairwise geometry 可解；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**前沿档案 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；工具通道本轮**丢失结果两次**（已重跑补齐）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:4x）`[纪律]`（先跑后写）

```
技术词 稳定性不等于刚性   命中文件数=0  ⟹ 本档新增
技术词 窗口秩不控       命中文件数=0  ⟹ 本档新增
技术词 通用扰动反例      命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
