已查地图：命中（`TOPIC-ASSET-MATRIX-v1-and-framework-reset`／`P1-3-unresolved-finite-problem-pool`／`F2-three-point-confirmation`）⟹ 引用其七字段制与三点确认，不开新案
D0: 本档对象 = **外部检索 R1**（`P2` 优先）＋ **三名七字段候选**（`C-1` 领先）＋ 裁定栏 ＋ 下一步核验单
D1: 0 （[REVIEW] 轮次：检索与筛选，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **检索 R1：七字段候选（`P2` 优先）**

## §C-1 ⭐ 领先候选：`z_L(5,5)` 的精确值（limited augmented Zarankiewicz）

```
$$P:\ \text{确定 }z_L(5,5)\ \text{的精确值}$$ ✓
$$X:\ 5\times5\ \text{上"limited augmented"}\ C_4\text{-free 图}\ \text{及其 2-edges 三/四元组}$$ ✓
$$K:\ \text{已知 }z_L\ \text{在 }6\times4,\ 5\times3,\ 5\times4\ \text{有精确值；}5\times5\ \text{已给\textbf{下界 }15}$$ ✓（**逐字**）
$$G:\ \textbf{explicit open gap}\ ——\ \text{原文逐字：}"A complete determination of the exact value would require an exhaustive search over all possible triples and quadruples of 2-edges for all extremal $C_4$-free graphs on $5\times5$. **Such a search is beyond the scope of this paper.** The exact value of $z_L(5,5)$ **remains open**; here a lower bound of 15 was established." ✓✓✓
$$A:\ \textbf{D（exact 枚举 ＋ 证书）为直接对口};\ \text{辅以 }A\ (\text{有限配置/对撞})\ \text{与 }G\ (\text{最小反例})$$ ✓✓ —— **作者自己把缺口描述成"\textbf{穷举}}"\ \Longrightarrow 与 `D` 资产\ \textbf{天然适配（Gate 2 强映射）** ✓✓
$$N:\ \text{一个精确整数}（z_L(5,5)=15\ \text{或}\ \ge16）\ \text{或"上界 }16\ \text{不可达"的完备证书}$$ ✓（**新量 = 精确值从"未知"变为"已知"** ✓）
$$O:\ \text{Zarankiewicz 型 extremal 问题族、limited/regular 变体、其它小参数格子}$$ ✓
	
【裁定（初）】**`C-1` = 首攻候选**（`Gate 1` ✓ 独立；`Gate 2` ✓✓ 强映射；`Gate 3` ✓ 新量明确；`Gate 4` ✓✓ 缺口逐字）✓✓
【待做（三点确认）】 **(i)** 该结论是否**至今仍为 open**（该文发表后是否有人已定 `z_L(5,5)`）；**(ii)** `z_L` 的**精确定义**须逐字核（"limited augmented" 的确切约束）；**(iii)** 缺口规模是否**有限可控**（作者称"all possible triples and quadruples of 2-edges **for all extremal** `C_4`-free graphs on `5\times5`"⟹ **须核 extremal `C_4`-free 图的个数是否已完备枚举**）✓✓
```

## §C-2 `\pm`-rank of `(0,\pm1)`-matrices（`P3` 型，秩）

```
$$P:\ \pm\text{-rank 的结构性界与分类}$$ ✓
$$X:\ (0,\pm1)\text{-矩阵},\ \text{尤其 alternating sign matrices}$$ ✓
$$K:\ \text{已建立若干不等式，联系 } \pm\text{-rank、binary rank、term rank、实秩}$$ ✓（来源：`ILAS 2026` 会议贡献摘要——**档级**）
$$G:\ \text{具体 open gap }\ \textbf{未锁定}$$ ⚠️
$$A:\ E\ (\text{秩})＋D$$ ✓（但**仅主题相邻**，非强映射）⚠️
$$N:\ \textbf{待具体化}$$ ⚠️\quad $$O:\ \text{矩阵组合/符号模式}$$
【裁定（初）】**暂缓** —— `G` 与 `N` 均未锁定 ⟹ **不满足七字段硬规** ✓
```

## §C-3 `11/8`-猜想（spin 4-流形：`b_2\ge\frac{11}8|\sigma|`）

```
$$P:\ \text{spin 闭定向光滑 4-流形是否满足 }b_2(M)\ge\frac{11}8|\sigma(M)|$$ ✓（来源：`ProofAtlas` #224 —— **档级**）
$$X:\ \text{交形式（rank 与 signature）}$$ ✓
$$K:\ \text{已知较弱常数（Furuta 型）}$$ ✓
$$G:\ \textbf{著名公开猜想}$$ ✓
$$A:\ E\ (\text{秩/签名/惯性})\ \text{仅\textbf{主题相邻}}$$ ⚠️ —— **无 exact/有限接口** ⟹ `Gate 2` **失败** ✓
【裁定（初）】**REJECT**（`Gate 2`：无强映射；属深层拓扑，非 `D`/`A`/`G` 可动）✓
```

## §汇总

```
$$\begin{array}{c|c|c|c|c|c|c|c|c}
\text{候选}&G1&G2&G3&G4&\text{七字段完备}&\text{裁定}\\
\hline
C\text{-}1\ z_L(5,5)&\checkmark&\checkmark\checkmark&\checkmark&\checkmark\checkmark&\checkmark&\textbf{首攻候选}\\
C\text{-}2\ \pm\text{-rank}&\checkmark&\triangle&\text{待}&\text{未锁定}&\times&\text{暂缓}\\
C\text{-}3\ 11/8&\checkmark&\times&-&\checkmark&\checkmark&\textbf{REJECT}\\
\end{array}$$ ✓
【下一轮（单点）】**对 `C-1` 做三点确认**：**(1)** 是否仍 open（查 2026 后续）；**(2)** `z_L` 定义逐字；**(3)** 缺口规模（extremal `C_4`-free `5\times5` 图是否已完备枚举，穷举规模量级）⟹ **过则进入 `(P,X,K,G)` 锁定与攻击方案；不过则回池** ✓✓
【⛔ 纪律】 **本轮未计算、未实现**；**未制造候选以外的对象**；`U_{2,3}` 维持暂停 ✓
【边界】 三个候选的来源均为**检索片段（档级）**，`K` 栏未做全文逐字核；`C-1` 的逐字引用来自 `MDPI\ Symmetry\ 18(7)\ 1076` 片段 ✓

## §附 【技术词回查】（补录）
```
技术词 limited augmented 命中文件数=1    :: ./TOPIC-SEARCH-R1-candidates-seven-field.md 
技术词 exact value      命中文件数=1    :: ./TOPIC-SEARCH-R1-candidates-seven-field.md 
```
