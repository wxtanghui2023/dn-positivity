已查地图：命中（`X1-K10-1-infrastructure-and-first-runs`）⟹ `X1` 首攻计算（第 2 轮），不开新案
D0: 本档对象 = **`X1` 第二轮**：记录码独立复核 ＋ **结构剖面** ＋ **刚性事实** ＋ **`(2,1)` 邻域穷举否定** ＋ **全 120 种删法的 `(1,1)` 修复否定** ＋ 下一步
D1: 1（**实际计算**，产出一批可复核的结构事实与穷举否定）
[RESEARCH]

# **`X1 / K(10,1)`：第二轮实测结果**

## §1 已完成并可复核的六项

```
$$\begin{array}{c|l|l}
\#&\text{项目}&\text{结果}\\\hline
1&\textbf{基础设施自校验（对已知精确值）}&
\begin{array}{l}n=4:\ K=4\ \text{SAT}\ \checkmark;\ n=5:\ K=7\ \text{SAT}\ \checkmark / K=6\ \text{UNSAT}\ \checkmark;\\ n=6:\ K=12\ \text{SAT}\ \checkmark / K=11\ \text{UNSAT}\ \checkmark\end{array}\\
2&\textbf{记录码独立复核（Kamenetsky 120，取自 OEIS）}&\text{120 字、去重后 120；}\boxed{1024/1024\ \textbf{全覆盖}}\ \checkmark\\
3&\textbf{包含极小性}&\boxed{\text{冗余字}=0}\ \Longrightarrow\ \text{不存在“删 1 字得 119”}\ \checkmark\\
4&\textbf{覆盖重数剖面（新事实）}&\boxed{801}\ \text{个顶点恰被 1 字覆盖};\ \boxed{172}\ \text{个恰被 2 字覆盖}\ \Longrightarrow\ \textbf{极紧}\\
5&\textbf{刚性（新事实）}&108{,}480\ \text{个 (1,1)-交换候选中}\ \boxed{\text{仅 }2\ \text{个仍为覆盖码}};\ \text{两者亦包含极小}\\
6&\textbf{(2,1)-邻域穷举（删 2 补 1）}&7140\ \text{对}\times904\ \text{候选，}\textbf{全扫}\ \Longrightarrow\ \boxed{\text{无 119-码}}\\
\end{array}$$ ✓✓
```

## §2 全 120 种删法的 `(1,1)` 修复穷举

```
$$\text{对 120-码的每一种“删 1 字”得到的 119-集，逐一遍历 904 个候选补字并检验“删 1 补 1”}:$$
$$\qquad \boxed{\text{全部 120 种删法，}(1,1)\ \text{修复均无解}}$$ ✓✓
$$\text{删 1 字后未覆盖顶点数分布}:\ \boxed{\min=2},\ \text{中位}=6,\ \max=11;\ \ \text{未覆盖}=2\ \text{的删法恰有}\ \boxed{2}\ \text{种}$$
$$\text{（最优 warm start}:\ \text{删去 }0111111001\ (\text{私有覆盖}=2)\ \text{后，仅剩顶点 }\{473,507\}\ \text{未覆盖}）$$
```

## §3 自建搜索的差距（诚实）

```
$$\text{贪心＋冗余消除＋delete\&repair}:\ \boxed{132}\ (\text{记录 }120);\quad \text{定长 tabu（}k=119/120/121\text{）}:\ \text{未覆盖最低}\approx\boxed{92}$$
$$\Longrightarrow\ \boxed{\text{自建搜索远劣于记录};\ \text{记录码才是唯一好基底};\ \text{“从零构造 119” 目前不可行}}$$
```

## §4 尚未排除的邻域与下一步

```
$$\textbf{已排除}:\ (1,0)\ \text{（删 1）};\ (2,1)\ \text{（相对记录码，穷举）};\ \text{全 120 种删法的 }(1,1)\ \text{修复}$$
$$\textbf{未排除}:\ (3,2)/(4,3)\ \text{型相对邻域（组合爆炸，需定向剪枝）};\ \textbf{全局其他 119-集}（非记录码邻域）$$
$$\textbf{下一步（三选）}:\ \text{(甲) 长跑 tabu（}k=119\ \text{warm start，已在后台）};\ \text{(乙) 定向 }(3,2)\ \text{剪枝搜索};\ \text{(丙) ILP/CP-SAT 长预算}$$
$$\textbf{诚实预期}:\ \text{社区认为 }K(10,1)=120\ \text{（下界 }107\ \text{远低）；}\boxed{\text{119 若不存在，则严格证明属 UNSAT 级（难）}};\ \text{我方可能产出 = 独立性复核＋刚性事实＋（若有）反例}$$
【⛔ 纪律】 本轮为\textbf{实际计算};\ \text{已当场自查并修正 1 处实现 bug（未覆盖集合计数）} ✓
【边界】 记录值取自 OEIS（抽取级）；\ \text{我方数值均为本地实测＋独立验证器复核} ✓
