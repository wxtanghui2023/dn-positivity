已查地图：命中（`Brouwer-A4-source-check`）⟹ 数据库型批 `A5`，不开新案
D0: 本档对象 = **`A5 La Jolla 差集库` 五闸输出** ＋ **`A=0`** ＋ **两条提取发现（库结构：差集部＝存在性型；coverings 部＝记录型）** ＋ **工具变更记录（tavily 配额耗尽 → `web_fetch`）** ＋ 交棒
D1: 0（source-level 抽取型，零计算）
[REVIEW]

# **`A5：La Jolla 差集库`（含 `E5` 前置闸）**

## §0 库本体（本轮原文抽取）

```
$$\text{库名}:\ \text{LJCR}\ (\text{La Jolla Combinatorics Repository})\ ——\ \text{Dan Gordon（CCR–La Jolla）}\textbf{维护 30 年};$$
$$\qquad \text{构成}:\ \boxed{\text{Coverings}}\ |\ \text{Difference Sets}\ |\ \text{Relative Difference Sets}\ |\ \text{Signed Difference Sets}\ |\ \text{Circulant Weighing Matrices};\ \text{站点}\ \mathbf{2026\text{-}09\text{-}03}\ \text{更新}$$
$$\qquad \text{形态演进}:\ \text{HTML}\to\text{MySQL}\to\boxed{\text{JSON＋python 脚本}}\ (\text{永久数据仓}:\ \text{Zenodo DOI}\ \texttt{10.5281/zenodo.10775931})$$
$$\textbf{差集部自述（逐字要点）}:\ \text{“A }(v,k,\lambda)\text{-difference set in a group }G\ldots\text{each nonzero element}\ldots\text{in exactly }\lambda\ \text{ways}”;$$
$$\qquad \boxed{\text{“gives information about possible parameters for difference sets in }\textbf{abelian groups}\ G”;}$$
$$\qquad \boxed{\text{“All parameters with }v<100000\ \textbf{passing basic tests}\ (\text{counting, Schützenberger, Bruck–Ryser–Chowla})\ \text{are listed}”;}$$
$$\qquad \boxed{\text{“an attempt has been made to include all known difference sets”};\quad \text{“Most known for large }v\ \text{are Paley}\ldots\text{so those are omitted for }v>1000”}$$
```

## `Gate 0` — identity lock（按**对象本体**去重）

```
$$\text{压缩机制（本库自带）}:\ \text{① }\boxed{\text{补集等价}}\ (v,k,\lambda)\leftrightarrow(v,v-k,v-2k+\lambda);\quad \text{② }\boxed{\text{Paley／分圆类族}}\ \text{一式覆盖无穷多 }v\ (\text{库已在 }v>1000\ \text{省略});$$
$$\qquad \text{③ }\boxed{\text{Hadamard／Menon 族}}\ \text{整族覆盖};\quad \text{④ }\textbf{参数行} \ne\ \textbf{对象}:\ \text{同一参数在多个群 }G\ \text{上各有一入口}\Longrightarrow\text{行数再乘一倍}$$
$$\Longrightarrow\ \boxed{\text{“参数缺口很多”}\ne\text{“候选很多”}}\ ——\ \text{此判断在本库得到}\textbf{结构级证实}（\text{与先生预判一致})$$ ✓✓
```

## `Gate 1` — 记录型入口筛选（**关键发现：本源主体非 }R_0/R_1\textbf{ 型**

```
$$\boxed{\text{差集部是}\textbf{存在性型}（\text{yes/no/known-unknown}）\ \textbf{而非数值记录型}（R_0<R_1）}$$
$$\qquad \text{库形态}:\ \text{按参数列“可能参数”＋“已知差集”};\ \text{“未解决”＝无存在构造且无不可能性证明}\Longrightarrow\ \text{属}\boxed{\text{普通 open problem}}\ \text{而非记录缺口}$$
$$\textbf{照先生口径}:\ \boxed{\text{不把普通 open problem 自动升级为候选}}\ \Longrightarrow\ \text{本闸即已滤除本源主体};\ \text{不进入 }A$$
$$\textbf{同库内的对照}:\ \text{LJCR 的}\ \boxed{\text{Coverings}}\ \text{部才是}\textbf{记录型}（\text{best-known 值＋“已证最优”标记}）\ ——\ \text{本轮按预登记只跑差集部};\ \text{该 Coverings 部}\textbf{登记为后续可能来源}（\text{不在本轮展开}）$$
```

## `Gate 2` — owner

```
$$\boxed{\text{有主，且为}\textbf{单人长期维护}}\ ——\ \text{Dan Gordon（CCR–La Jolla）30 年};\ \text{站点 2026-09-03 更新};\ \text{近期}\textbf{新增} \text{Relative／Signed Difference Sets}\ \text{两类};\ \text{数据有 Zenodo DOI 永久化}$$
$$\qquad \text{社区侧}:\ \text{乘子定理／分圆构造／BRC 障碍（Gordon 本人 }\texttt{papers/multipliers.pdf}\ \text{等）}\Longrightarrow\ \text{不存在“无主记录”}$$
```

## `Gate 3` — `E5` 前置问

```
$$\text{问}:\ \text{是否已有}\ \text{计算生成}\to\text{certificate}\to\text{独立复核}\to\text{库更新}\ \text{的流水线？}$$
$$\textbf{答}:\ \boxed{\text{YES（经典算法型）}}\ ——\ \text{① 参数侧由计数／Schützenberger／BRC 自动筛};\ \text{② 构造侧有分圆／乘子／Paley 等\ 算法化方法};\ \text{③ 库由 JSON＋python 脚本生成并有 Zenodo 版本化}\ (\text{更新路径存在});$$
$$\qquad \textbf{但}\ \boxed{\text{“AI/SAT 级工业化”未获证据}\ ——\ \text{与 }A3\ \text{的 SAT 流水线不同级别}}\ (\text{如实区分，不夸大})$$
$$\qquad \text{注}:\ \text{本轮因 tavily 配额耗尽，改用 }\texttt{web\_fetch};\ \textbf{未能做二次检索交叉核}\ (\text{边界})$$
```

## `Gate 4` — `AMEND-21`

```
$$\textbf{① 对象未覆盖}:\ \text{✗ 不成立（差集论自 1930s Paley、1949–50 BRC 起为经典领域）};\quad \textbf{② 参数化未覆盖}:\ \text{✗ 不成立（}(v,k,\lambda)+\text{abelian }G\ \text{为标准参数化）};$$
$$\qquad \textbf{③ 充要条件}:\ \text{缺（存在性一般无 characterization），但}\boxed{\text{攻击接口由经典路线覆盖}}:\ \text{计数／Schützenberger／BRC 障碍};\ \text{乘子定理};\ \text{分圆与 Paley 构造};\ \text{小阶群穷举}$$
$$\Longrightarrow\ \boxed{\text{AMEND-21} = \text{判除}};\quad \boxed{\text{A-count} = 0}$$ ✓✓
```

## §交棒与工具

```
$$\text{数据库型批进度}:\ A1\ A=0;\ A2\ A=0;\ A3\ A=0;\ A4\ A=0;\ \boxed{A5\ A=0}\ \Longrightarrow\ \textbf{批 }(a)\ \text{五源全灭}$$
$$\textbf{照预登记规则}:\ \text{不在本源内改参数救场};\ \text{不改写 }\ (a)\ \text{批的性价比判断（照先生令）}$$
$$\textbf{后续候选来源（登记，不展开）}:\ \text{LJCR}\ \boxed{\text{Coverings}}\ \text{部（记录型，与本轮差集部同库不同对象）};\ \text{其余未评来源}$$
【⛔ 纪律】 本轮\textbf{零计算};\ \text{未决策};\ \text{未制造候选};\ \text{未改 }\ (a)\ \text{批判断} ✓
【边界】 tavily 配额耗尽 ⟹ 单源}\ \texttt{web\_fetch}\ \text{抽取};\ \text{未做二次交叉核} ✓

## §附 【技术词回查】（补录）
```
技术词 identity lock    命中文件数=3    :: ./LJCR-A5-difference-sets-source-check.md ./Zarankiewicz-A3-source-check.md ./Brouwer-A4-source-check.md 
技术词 existence type   命中文件数=0    :: 
```
