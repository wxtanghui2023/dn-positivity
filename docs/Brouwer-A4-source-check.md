已查地图：命中（`Zarankiewicz-A3-source-check`）⟹ 数据库型批 `A4`，不开新案
D0: 本档对象 = **`A4 Brouwer 表` 五闸输出（`Gate 0` identity lock → `Gate 1` 记录筛 → `Gate 2` owner → `Gate 3` **`E5` 前置问** → `Gate 4` `AMEND-21`）** ＋ **`A=0`** ＋ **校准 E4 再确认（表龄 ≠ 数学缺口）** ＋ 交棒 `A5`
D1: 0（source-level 抽取型，零计算）
[REVIEW]

# **`A4：Brouwer 表`（含 `E5` 前置闸）**

## `Gate 0` — identity lock（按**对象本体**去重）

```
$$\text{来源面}:\ \texttt{aeb.win.tue.nl/codes/}\ \text{（Brouwer）};\ \text{Grassl }\texttt{codetables.de};\ \text{Jaffe（binary linear）};\ \text{Agrell }\texttt{codes.se}\ (\textbf{已冻结});\ \text{Litsyn 1998 手册表};\ \text{BEST/旧表}$$
$$\textbf{重复来源（同一记录多表并存）}:\ \text{同一个 }A(n,d)\ \text{或 best-known code 记录，至少在}\ \boxed{4}\ \text{处并存，且}\textbf{表龄不同只（2017／2019／2026／已冻结）}$$
$$\qquad \texttt{binary-1.html}\ \text{最后改动}\ \mathbf{2019\text{-}04\text{-}25};\quad \texttt{ternary-1.html}/\texttt{quaternary-1.html}\ \mathbf{2017\text{-}09\text{-}07};\quad \texttt{cwc/}\ \mathbf{2026\text{-}08\text{-}02}$$
$$\textbf{去重规则（本闸确立）}:\ \text{① 按}\boxed{\text{码参数 }(q,n,d)\ \text{＋ 码类（unrestricted／linear／self-dual／cyclic…）}}\ \text{归并};\ \text{② 同一记录在 }k\ \text{张表中出现}\ \Rightarrow\ \text{计 }\mathbf{1}\ \text{个入口};\ \text{③ 设计／关联结构／图 的等价表述归并到同一入口}$$
$$\Longrightarrow\ \text{入口数}\ \ll\ \text{表格行数};\ \boxed{\text{“按行计数”在本源会系统性高估}}$$ ✓✓
```

## `Gate 1` — `R_0/R_1` 记录型筛选（**不把普通 open problem 计入**）

```
$$\textbf{真正的“未闭合值”格（示例，抽取级）}:\ \text{二元表 }n=17..24\ \text{区段的区间型记录（如 }2816\text{-}3276,\ 5632\text{-}6552\ \text{型）};\ \text{三元／四元表 similar（如 }A_3(9,4)\ \text{lub }937\ \text{vs llb }729）$$
$$\textbf{⚠️ 但本闸即暴露关键事实（校准 E4 再确认）}:\ \text{Brouwer 页}\textbf{自承}:\ \text{“Terwilliger 代数新上界进一步改进为 }A(25,6)\le47998\text{，但把 }A(26,10)\ \text{改差为 }886”⟹$$
$$\qquad \boxed{\text{表中数字}\ne\text{当前最优}};\ \text{即}\boxed{\text{“表内缺口”首先可能是}\textbf{表龄缺口}\ \text{而非数学缺口}}$$ ✓✓
$$\Longrightarrow\ \text{凡“表内缺口”，先判}\boxed{\text{是表没更新，还是数学没解决}};\ \text{前者}\Rightarrow\ \text{不构成 LANE-A（属重新计算已知记录，先生已列为排除项）}$$
```

## `Gate 2` — owner

```
$$\boxed{\text{有主}}\ ——\ \text{Brouwer（表主，部分页面停在 2017／2019）};\ \text{Grassl（活跃维护）};\ \text{Jaffe（binary linear）};\ \text{Schrijver（Terwilliger 上界）};\ \text{以及编码论分类群体（Kurz }\texttt{lincode}\text{／Östergård 等）}$$
$$\qquad \text{注}:\ \text{本源不存在“无主记录”}\Longrightarrow\ \text{不满足 LANE-A 的“可独立接管”前提}$$
```

## `Gate 3` — **`E5` 前置问**（本轮新设，照先生令）

```
$$\text{问}:\ \text{是否已存在}\ \boxed{\text{SAT/ILP/CP／枚举}\to\text{显式 certificate}\to\text{独立重解/复核}\to\text{表/库更新}}\ \text{的流水线？}$$
$$\boxed{\text{答: YES}}\ ——\ \text{① 代码分类软件（}\texttt{lincode}\text{／Q-Extension）已长期工业化};\ \text{② 上界一侧有 LP／Delsarte／Terwilliger 代数自动化改进};\ \text{③ 下表一侧由构造＋SAT/ILP 见证（存入表/库）};\ \text{④ 表本身由社区持续收录更新（}\texttt{cwc/}\ \text{页面 2026-08 仍更新}）$$
$$\Longrightarrow\ \text{该流水线}\textbf{已覆盖本源的主要记录型入口};\ \text{即使具体参数仍有缺口，也须}\textbf{直接进入 `AMEND-21`}$$ ✓✓
```

## `Gate 4` — `AMEND-21`

```
$$\textbf{① 对象未覆盖}:\ \text{✗ 不成立（编码论经典对象，逾半世纪文献）};\quad \textbf{② 参数化未覆盖}:\ \text{✗ 不成立（}\ (q,n,d)\ \text{＋码类为标准参数化）};\quad \textbf{③ 充要条件}:\ \text{缺，但}\boxed{\text{攻击接口已被上述流水线覆盖}}$$
$$\Longrightarrow\ \boxed{\text{AMEND-21} = \text{判除}};\quad \boxed{\text{A-count} = 0}$$ ✓✓
```

## §交棒

```
$$\text{数据库型批进度}:\ A1\ A=0;\ A2\ A=0;\ A3\ A=0;\ \boxed{A4\ A=0}$$
$$\Longrightarrow\ \textbf{照预登记规则}:\ \text{不在本表内改参数救场};\ \boxed{\text{直接进入 }A5\ (\text{La Jolla 差集库})}$$
$$\textbf{`A5` 前置}:\ \text{同 }A4\ \text{五闸};\ \text{并特别注意先生预判“许多问题已属经典差集/设计理论路线”}$$
【⛔ 纪律】 本轮\textbf{零计算};\ 未决策;\ 未制造候选;\ \textbf{未收阶段性小结}（照先生令） ✓
【边界】 全为检索抽取级;\ 未逐行清点 Brouwer 全表\（仅取结构＋示例＋表龄证据） ✓
