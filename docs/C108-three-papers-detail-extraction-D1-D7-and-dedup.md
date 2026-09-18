已查地图（所查：`E18-NOGO-ALIGNMENT-2.md` #49（**`d7-boundary-audit.md`：素数↔零点通道＝`lossless, adaptive`；恒等通道只产等式不产不等式**）、`T3-0-charter-architecture-search.md`（**原损耗 `L^5=L_WL_{\ell_1}L_{\ell_2}L_u` ＋ `L_iL_j → 联合算术对象` 判据**）、`E44-ceiling-encl-audit.md`（**`certified` 包络**）、`CLOSED-ROUTES-MAP.md:2384`（**`C`／`P`／`U` 三分语义**）、`A3-barrier-opinion`／`A3-1`（`barrier` 62 档）、`C-78`（常数 vs 幂）、`W6`／`SUPPORT-1`）。**结论**：三篇论文**摘要逐字**取得并提取证明技术 ⟹ 除五个 primitive 外，再提取 **7 项新细节**（`D1`–`D7`）；查重结果：**6/7 落已覆盖**，其中 **`D1`／`D2` 档案已有精确条目**（`d7-boundary-audit`：通道**已无损**但**只产等式**；`T3-0`：**损失因子分解 `L^5` ＋ "联合算术对象"判据**）✓✓；**唯一结构性对照值得记录**：外部成功机制＝"把有损转换修成无损"，而我们**通道本来就无损** ⟹ **我们的障碍不是无损性，而是"等式 vs 不等式"** ✓✓ ⟹ **无新入口** ✓

# C-108 · **三篇论文细节提取（`D1`–`D7`）与查重：外部成功机制 vs 我们的障碍**

> **时间**：2026-09-18 16:06 唐先生：**搜索查看三篇论文的细节，看看是否有其它细节有启发** ✓
> **取法**：`arXiv` API（`export.arxiv.org/api/query`）取**摘要逐字**（`web_fetch` 成功；`curl` 直连不通）✓

---

## §0 结论（先行）

$$\textbf{(1)}\ \text{提取 7 项新细节}\ D1\text{–}D7 \Longrightarrow \textbf{6/7 落已覆盖}✓✓$$
$$\textbf{(2)}\ ⭐\ \text{两项档案已有}\ \textbf{精确条目}：$$
$$\qquad \text{`D1`（无损编码）} \Longrightarrow \text{`d7-boundary-audit.md`（`E18` #49）逐字}：\boxed{\text{"the prime}\leftrightarrow\text{zero channel is the }\textbf{lossless, adaptive}\text{ explicit formula"};\ \textbf{"identity channels produce equalities (cost) and never inequalities (exclusion)"}}✓✓$$
$$\qquad \text{`D2`（损失因子分解）} \Longrightarrow \text{`T3-0-charter` 逐字}：\boxed{L^5=L_WL_{\ell_1}L_{\ell_2}L_u};\ \text{新架构判据}：\boxed{L_iL_j\longrightarrow\textbf{联合算术对象}}✓✓$$
$$\textbf{(3)}\ ⭐\ \textbf{唯一值得记录的结构性对照}：\text{外部成功机制}＝\text{"把}\ \textbf{有损转换修成无损}\text{"};$$
$$\qquad \text{而}\ \textbf{我们的通道本来就无损} \Longrightarrow \boxed{\text{我们的障碍不是无损性，而是}\textbf{等式 vs 不等式}}✓✓$$
$$\textbf{(4)}\ \text{其余}：\text{`D3`}\ \text{certified} \Longrightarrow \text{已做（`E44` Lean 认证包络）};\ \text{`D4`}\ \text{两体/pair} \Longrightarrow \text{`W6` 墙};\ \text{`D5`}\ \text{局部 oracle ＋ 无全局对象} \Longrightarrow \text{严格落}\ \text{`C`／`P`／`U` 三分的 `C` 类} \Longrightarrow \textbf{cylinder} \Longrightarrow \beta\ \text{盲};\ \text{`D6` 效率工程};\ \text{`D7` 常数≠幂} \Longrightarrow \text{`C-78`}✓$$
$$\Longrightarrow\ \textbf{判词}：\text{三篇的剩余细节}\ \textbf{无新 RH 入口};\ \text{但}\ \textbf{独立外部模板确认了}\ \text{我们两条既有洞见}✓✓$$

---

## §1 三篇摘要逐字（关键句）

$$\text{【Matrix Spencer】}\ \text{arXiv:2609.15025}（\text{Zhao Song, Lichen Zhang};\ 2026\text{-}09\text{-}14）✓$$
$$\qquad \text{"…a signing of discrepancy below}\ \mathbf{8\sqrt n}\ \text{always exists…"}; \text{"…below}\ \mathbf{12\sqrt n}\ \text{with failure probability at most}\ p\ \text{using}\ n^{3+o(1)}\mathrm{polylog}(1/p)\ \text{arithmetic operations…"}✓$$
$$\qquad \text{"The existence proof is a partial-coloring argument with }\boxed{\text{one new estimate: a }\textbf{hereditary Gaussian small-ball}\text{ bound for the spectral body}}✓$$
$$\qquad \qquad \text{"…proved by }\textbf{interpolating a log-partition function}\text{ from a }\textbf{diagonal model}\text{ to the }\textbf{noncommutative one}\text{ under a }\textbf{matrix-weighted Poincaré inequality}"✓$$
$$\qquad ⭐\ \text{"}\textbf{Proving the conjecture and bringing the constant below 8 are different problems}\text{"} ✓✓$$
$$\qquad ⭐\ \text{"The partial-coloring argument loses a large factor}\ \textbf{twice}\text{…}\ (\text{i})\ \text{turning Gaussian measure into signs through a }\textbf{union bound}\ (\text{ii})\ \text{proving the small-ball estimate at a }\textbf{radius far larger than necessary};\ \text{they remove the first by a }\textbf{lossless coding of Gaussian measure into signs}\text{ and the second by }\textbf{smooth spectral barriers with certified coefficients}\text{"}✓✓$$
$$\qquad \text{"…project Gaussian points onto a smoothed version of the spectral body, whose derivatives are }\textbf{traces against one Gibbs matrix};\ \textbf{four successively cheaper ways}\ \text{of maintaining that matrix…"}✓$$
$$\text{【k-server】}\ \text{arXiv:2609.15979}（\text{Coester, Koutsoupias, Zbysiński};\ 2026\text{-}09\text{-}14）✓$$
$$\qquad \text{"…the work function algorithm satisfies it… a natural }\textbf{algebraic representation of the work function as a matrix}\text{, which encodes }\textbf{all feasible paths}✓$$
$$\qquad \qquad \text{"…the }\mathbf{min}\text{ and }\mathbf{addition}\text{ operations… correspond to }\textbf{addition and multiplication of formal expressions}\text{, and each work function value corresponds to the }\textbf{determinant of }k\text{ columns}✓$$
$$\qquad \qquad \text{"A request arrival updates the representation via a }\textbf{change of basis and row replacement}\text{…the amortized analysis is based on a potential function defined in terms of a }\textbf{larger matrix whose coordinates are pairs of coordinates}\text{ of the original matrix" }✓✓$$
$$\text{【Matroid Secretary】}\ \text{arXiv:2609.14555}（\text{Sahil Singla};\ 2026\text{-}09\text{-}13;\ 22\text{KB}）✓$$
$$\qquad \text{"…an online algorithm that accepts }\textbf{each element of the offline optimum with probability at least }1/4✓$$
$$\qquad \qquad \text{"…only needs the number of elements in advance and }\textbf{independence-oracle access to subsets of already-arrived elements};\ \textbf{it does not need to know the matroid upfront}\text{"}✓✓$$

## §2 新细节提取表（`D1`–`D7`）

| 编号 | 细节 | 出处 |
|:--|:--|:--|
| **`D1`** | **`lossless coding of Gaussian measure into signs`**（把"连续测度→离散符号"做成**无损**）| Matrix Spencer |
| **`D2`** | **损失因子化**：partial-coloring **丢因子两次**（union bound ／ 半径过大），**各自用专门装置消除** | Matrix Spencer |
| **`D3`** | **`smooth spectral barriers with certified coefficients`** | Matrix Spencer |
| **`D4`** | 势函数定义在**"坐标是原矩阵坐标对"的更大矩阵**上（pair-coordinate lift）| k-server |
| **`D5`** | **局部 independence-oracle（仅已到达子集）＋ 不需预先知道 matroid** ＋ **逐元素一致保证 ≥`1/4`** | Matroid Secretary |
| **`D6`** | 四种逐次更省的矩阵维护方式（效率分层）| Matrix Spencer |
| **`D7`** | **"证明猜想"与"把常数压到 8 以下"是两个不同问题** | Matrix Spencer |

## §3 查重（逐项）

| 细节 | 档案命中 | 判定 |
|:--|:--|:--|
| `D1` lossless | **`lossless`＝1 命中 ⟹ `d7-boundary-audit.md`（`E18` #49）："prime↔zero channel is the **lossless, adaptive** explicit formula… identity channels produce **equalities** and never **inequalities**"** | ⭐ **已有精确条目** |
| `D2` 损失因子化 | **`损耗`＝1 ⟹ `T3-0-charter`：`L^5=L_WL_{\ell_1}L_{\ell_2}L_u` ＋ 判据 `L_iL_j → 联合算术对象`** | ⭐ **已有精确条目** |
| `D3` certified | `certified`＝5 ⟹ `E44-ceiling-encl-audit`（**Lean 认证包络**）、`A3-1` | **已覆盖（我们已在做）** |
| `D4` pair-coordinate | `pair-coordinate`＝0；但 `两体`＝7 ⟹ `C-97`／`C-98`／`W6`／`SUPPORT-1` | **落 `W6` 墙（两体＝支撑>1）** |
| `D5` 局部 oracle | `oracle`＝8 ⟹ **`CLOSED-ROUTES-MAP:2384` `C`／`P`／`U` 三分**：`C` finite-data certificate ⟹ **cylinder ⟹ C0** | **落 `C` 类 ⟹ `β` 盲** |
| `D6` 效率分层 | —（工程）| **不涉 RH** |
| `D7` 常数≠幂 | `C-78`（常数房 ≤1.5× vs 幂级缺口）| **已登记** |
| 附：`log-partition` | **0 命中** | 新措辞（但＝`M2` 插值的内部步骤）|
| 附：`union bound`／`并集界` | **0 命中** | 新措辞 |
| 附：`局部独立性` | **0 命中** | 新措辞 |

## §4 ⭐ 两个结构性对照（本档核心产出）

$$\textbf{对照 A（无损性不是我们的障碍）}：$$
$$\qquad \text{外部}：\text{Gaussian 测度}\to\text{符号的转换}\ \textbf{本来有损}（\text{union bound 丢大因子}） \Longrightarrow \textbf{修成无损} \text{后才拿到存在性}✓$$
$$\qquad \text{我们}：\text{素数}\leftrightarrow\text{零点通道}\ \textbf{本来就无损}（\text{显式公式是恒等式}） \Longrightarrow \text{但它是}\ \textbf{等式通道} \Longrightarrow \textbf{只产代价，不产排除}✓✓$$
$$\qquad \Longrightarrow\ \boxed{\text{补"无损"对我们无用};\ \text{我们的缺口是}\ \textbf{从等式到不等式}}✓✓$$
$$\qquad \qquad ⚠️\ \text{这与}\ \text{`C-82`（值的性质 vs 界的性质）}\ \textbf{同向};\ \text{且与}\ \text{`d5-no-go-and-d6`（恒等通道只产等式不产不等式）}\ \textbf{同址}✓$$
$$\textbf{对照 B（损失因子化＝我们的 `T3-0` 判据）}：$$
$$\qquad \text{外部}：\text{把损失分成两块，各用专门装置消除}✓$$
$$\qquad \text{我们}：\text{`T3-0` 已给出更硬的判据}：\textbf{新架构须让}\ L_iL_j\ \textbf{耦合成联合算术对象};\ \text{理由}：\text{逐层绝对值化}\ \#\{\ell_2,\ell_2'\}=L^{2+o(1)} \Longrightarrow \textbf{不可能凭空制造固定幂次}✓✓$$
$$\qquad \Longrightarrow\ \text{外部模板}\ \textbf{确认} \text{我们的判据，但}\ \textbf{不提供新装置}✓$$

## §5 判词与边界

$$\boxed{\text{三篇论文的剩余细节}\ \textbf{无新 RH 入口}};\ \text{但}\ \textbf{独立外部模板确认了我们两条既有洞见}✓✓$$
$$\qquad \text{（\text{i}）}\ \textbf{无损性不是障碍，等式→不等式才是};\quad \text{（\text{ii}）}\ \textbf{损失必须耦合成联合对象，分别估计无效}✓$$
$$\qquad \Longrightarrow\ \text{与}\ \text{`C-104`–`C-107`}\ \text{结论}\ \textbf{一致}：\text{五 primitive 全部落地，无新入口}✓✓$$
- ⚠️ **边界**：三篇为**外部算法论文**（`cs.DS`），迁移至 RH 属**推测性类比**；本档仅做**细节提取＋查重**，**未**据此开任何新案 ✓
- **不声称**：任何外部技术对 RH 有效 ✗；`D1`–`D7` 可迁移 ✗（仅记录同址/新措辞）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓；外部内容按**不可信来源**处理 ✓（仅作论文事实引用）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 16:0x）`[纪律]`（先跑后写）

```
技术词 细节提取       命中文件数=1  :: ./C108-three-papers-detail-extraction-D1-D7-and-dedup.md
技术词 无损性不是障碍    命中文件数=1  :: ./C108-three-papers-detail-extraction-D1-D7-and-dedup.md
技术词 联合对象判据     命中文件数=1  :: ./C108-three-papers-detail-extraction-D1-D7-and-dedup.md
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

```
⚠️ 唐先生 16:06：搜索查看三篇论文的细节，看是否有其它细节有启发
✅ 取法: arXiv API(export.arxiv.org/api/query) 取摘要逐字成功（curl 直连不通, web_fetch 成功）
✅ 三篇事实（修正后）: Matrix Spencer = Zhao Song & Lichen Zhang(2026-09-14); k-server = Coester/Koutsoupias/Zbysiński(2026-09-14);
   Matroid Secretary = Sahil Singla(2026-09-13, 22KB)
✅ 提取 7 项新细节 D1–D7: D1 无损编码(Gaussian 测度→符号); D2 损失因子化(丢因子两次, 各自专门装置消除);
   D3 smooth spectral barriers with certified coefficients; D4 pair-coordinate 势矩阵; D5 局部 independence-oracle + 不知 matroid + 逐元素 ≥1/4;
   D6 四种逐次更省的维护方式; D7 证明猜想≠把常数压到 8 以下
✅ 查重: 6/7 落已覆盖 ——
   ⭐D1 ⟹ 档案已有精确条目 d7-boundary-audit.md(E18 #49): "prime↔zero channel is the lossless, adaptive explicit formula;
      identity channels produce equalities (cost) and never inequalities (exclusion)"
   ⭐D2 ⟹ 档案已有精确条目 T3-0-charter: 原损耗 L^5=L_W·L_ℓ1·L_ℓ2·L_u ＋ 判据 "L_iL_j → 联合算术对象"
   D3 ⟹ certified=5 命中(E44 Lean 认证包络 / A3-1) ⟹ 我们已在做
   D4 ⟹ pair-coordinate=0 但 两体=7 ⟹ 落 W6 墙(两体=支撑>1)
   D5 ⟹ oracle=8 ⟹ CLOSED-ROUTES-MAP:2384 的 C/P/U 三分; 局部 oracle ⟹ C 类(finite-data certificate) ⟹ cylinder ⟹ C0 ⟹ β 盲
   D6 ⟹ 工程, 不涉 RH; D7 ⟹ C-78(常数 vs 幂)已登记
   新措辞(0 命中): log-partition / union bound / 局部独立性
⭐ 核心产出（两个结构性对照）:
   对照 A: 外部成功靠"把有损转换修成无损"; 而**我们的素数↔零点通道本来就无损**(显式公式=恒等式) ⟹ **补"无损"对我们无用**;
     我们的缺口是"**从等式到不等式**"（与 C-82 值的性质 vs 界的性质、d5-no-go-and-d6 同址）
   对照 B: 外部"损失因子化" ⟹ 确认我们 T3-0 判据(**L_iL_j → 联合算术对象**), 但**不提供新装置**
⭐ 判词: 三篇剩余细节**无新 RH 入口**; 但独立外部模板确认我们两条既有洞见 ⟹ 与 C-104–C-107 一致（五 primitive 全部落地, 无新入口）
⚠️ 边界: 外部算法论文(cs.DS), 迁移属推测性类比; 本档仅细节提取+查重, **未据此开任何新案**; 外部内容按不可信来源处理
✅ 净产出: ①三篇摘要逐字（含证明技术细节）✓ ②D1–D7 提取表 ✓ ③逐项查重（含两条精确既有条目）✓ ④两个结构性对照 ✓ ⑤"无新入口"判定 ✓
```
