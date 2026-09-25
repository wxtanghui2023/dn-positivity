已查地图：命中（`RESEARCH-CONSTITUTION` AMEND-26/27 ＋ `ASTRA-PERMANENT-critical-codimension-isomorphism-audit`）⟹ 空间 B 首版匹配表，不开新案
D0: 本档对象 = **机制清单（`M1`–`M12`）× 独立靶点 × 交付物 × 状态** 的**首版多域匹配表** ＋ 可立即入场项
D1: 0（登记型，零计算）
[REVIEW]

# **资产 → 数学问题 · 多域匹配表 v1（空间 B）**

## §0 机制清单（**实证过**的，非设想）

```
$$\begin{array}{c|l|l}
\text{编号}&\text{机制}&\text{本会话/档案实证出处}\\\hline
M1&\text{局部约束}\to\text{全局压缩}／\text{证书}&\text{C07};\ X1;\ \text{覆盖码/设计}\\
M2&\text{全局证书同时满足大量局部条件}&\text{Ramsey 式模板（Astra ⑨）；我方 universal-certificate 思路}\\
M3&\text{商／修复／闭包（quotient/repair/closure）}&\text{极值图论（Astra ⑩）；群论（Astra ③）}\\
M4&\text{余维／临界轨迹}\operatorname{codim}\operatorname{Crit}&\text{Bézout/resultant 资产（}\texttt{ZF-RPC-1}\text{）；Astra ⑤}\\
M5&\text{单位根消去交叉项}&\text{Astra ⑤ 装置；本线 resultant 型已撞同一 GAP}\\
M6&\text{预解／纯化（resolvent/purification）}&\text{Astra ⑥；我方谱/预解资产（25 档 Fredholm）}\\
M7&\text{凸包络／配分函数}&\text{Astra ⑧；我方 convexity 型负结果}\\
M8&\text{高维局部结构压缩}&\text{Astra ①／②；packing/coding}\\
M9&\boxed{\text{精确有限搜索 ＋ 独立验证器}}&\boxed{\text{最强：}C07\ \text{证书};\ X1\ \text{（重数剖面＋三层刚性＋CP-SAT）}}\\
M10&\text{形式化（Lean 可迁移骨架）}&\text{TLDC（公理自由、五闸）}\\
M11&\text{机械式同构／去包装判定}&\text{Astra 十项审计（}\texttt{NEW-INFO GATE}\text{）}\\
M12&\text{整性／整除／}p\text{-进障碍}&\text{BRC；EDS/RPC；diffset 存在性}\\
\end{array}$$ ✓✓
```

## §1 独立靶点匹配（空间 B；**不要求接 RH**）

```
$$\begin{array}{c|l|l|l|c}
\text{机制}&\text{独立领域}&\text{具体靶点（可验证）}&\text{交付物}&\text{状态}\\\hline
M9&\text{编码/覆盖}&\boxed{K(10,1)\le119}\ (\text{119-word 覆盖码})&\text{显式码＋秒级独立验证}&\boxed{\textbf{进行中}}\\
M9&\text{差集/设计}& \texttt{LJCR}\ \text{差集库中}\textbf{未知参数}\ (v,k,\lambda)\ \text{的最小开格}&\text{显式差集}\Rightarrow\text{秒级验证}&\boxed{\textbf{可立即入场}}\\
M9&\text{覆盖设计}& \texttt{LJCR Coverings}\ \text{中 best-known 与已证最优之间的格}&\text{双向证书（构造＋界）}&\boxed{\textbf{可入场（未审计）}}\\
M9&\text{Ramsey}&\boxed{R(3,10)\in\{40,41\}}:\ \text{40 顶点无三角、}\alpha\le9\ \text{图}&\text{显式图}\Rightarrow\text{秒级验证}&\text{可入场（谱系拥挤但未做出）}\\
M2&\text{饱和数}& \text{sat}(n,H)\ \text{小 }H\ \text{未闭合值}&\text{见证图＋穷举完备性证明}&\text{W}\ (\text{已被工业化流水线覆盖})\\
M4&\text{代数几何/复杂性}& \text{小尺度 determinant vs permanent 临界轨迹余维的实际计算}&\operatorname{codim}\ \text{计算＋证书}&\text{W（需先定可验证定义）}\\
M10&\text{形式化}& \text{把}\ \texttt{TLDC}\ \text{骨架推进到一个真实数论实例}&\text{Lean 编译通过＋无 sorry}&\text{需装 Mathlib（几 GB）}\\
M11&\text{外部成果审计}& \text{对任意 AI/论文"新机制"宣称做}\ \texttt{NEW-INFO GATE}\ \text{判定}&\text{判定表＋同构证明}&\boxed{\textbf{已试点（Astra）}}\\
\end{array}$$ ✓✓
```

## §2 可立即入场项（按"交付物最硬"排序）

```
$$\text{(1)}\ \underbrace{K(10,1)\le119}_{M9}\ ——\ \text{已在进行（}B1\text{-a no\_lp 长跑）}$$
$$\text{(2)}\ \underbrace{\text{差集最小开格}}_{M9+M12}\ ——\ \textbf{证书最便宜}:\ \text{显式集合}\Rightarrow\text{秒级验证};\ \text{无需大算力}$$
$$\text{(3)}\ \underbrace{\text{LJCR Coverings 表格}}_{M9}\ ——\ \text{双向证书};\ \text{须先做表龄核验（}E4\text{）}$$
$$\text{(4)}\ \underbrace{R(3,10)}_{M9}\ ——\ \text{证书同样秒级};\ \text{但计算量大、竞争密集}$$
【⛔ 纪律】 本表\textbf{不要求}任何项接 RH;\ \text{空间 }A\ \text{仍按 }AMEND\text{-25}\ \text{独立把关} ✓
【边界】 状态列中 "已工业化/W" 为检索级判断;\ \text{靶点可验证性均为秒级（显式见证）} ✓
