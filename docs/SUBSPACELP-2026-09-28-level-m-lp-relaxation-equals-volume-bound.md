# SUBSPACELP-2026-09-28 — **level-$m$ 系统 LP 松弛 ≡ 体积界（零增益）**：武器 B 的引擎定位

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-27 23:59 令 ✓）**：执行**工具组合能力测试**（Test C 的第一步：测 subspace-recursion ＋ conditional LP 的**每层增益**）；**不找新机制** ✓、不做路线决定 ✗、不额外筛选 ✗。
> **有计算**（小规模 LP，scipy/HiGHS ✓；经 `pyguard.sh` ✓，单线程 ✓，输出落盘 ✓）

**已查地图：命中（接续 MCOVER／C-429／PROVENANCE／OBREVERSE，非新案 ✓）**
`docs/MCOVER-2026-09-26-…`（**level-$m$ M-covering system 精确重建 ＋ 均匀解 ＋ 实测收紧律** ✓✓）｜`docs/C-429`（**$n=10$ 推广 $A_{ii}=n+1-m$** ✓✓）｜`docs/PROVENANCE-2026-09-26-…`（**2001 摘要逐字** ✓✓）｜`docs/OBREVERSE-2026-09-26-…`（**重建算法** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** level-$m$ M-covering system（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出"LP 松弛 ≡ 体积界（一切 $m$）"的等号定理 ＋ 零增益实测 ＋ 引擎定位诊断** ✓）
**[RESEARCH]**

---

## §0 结论（**等号定理 ✓✓｜零增益 ✓✓｜引擎定位 ✓✓**）

$$\boxed{\textbf{(1) ★等号定理（新 ✓✓）}:\ \text{对 binary }R=1,\ \text{任意 }n,\ \text{任意 }m\ (1\le m\le n):\quad L(m)\ =\ \frac{2^n}{n+1}\ \ \textbf{恰好等号}}$$
$$\qquad\textbf{两行证明}:\ \text{① 聚合 }t\ \text{个约束} \Longrightarrow (n+1)\sum_iy_i\ \ge\ t\cdot s=2^n \Longrightarrow L(m)\ge\frac{2^n}{n+1}✓;\qquad \text{② 均匀解 } y_i\equiv\frac{2^{n-m}}{n+1}\ \text{可行}✓$$
$$\qquad\qquad\big(\text{因每列和}\sum_iA_{ji}=|B_1(c)|=n+1✓;\ \text{且 } \frac{2^{n-m}}{n+1}\le s=2^{n-m}✓\big) \Longrightarrow L(m)\le\frac{2^n}{n+1}✓\ \Longrightarrow\ \textbf{等号}✓✓$$
$$\boxed{\textbf{(2) ★★零增益（实测 ✓✓）}:\ n=9:\ L(m)\equiv\mathbf{51.200000}\ (m{=}1{:}9✓);\qquad n=10:\ L(m)\equiv\mathbf{93.090909}\ (m{=}1{:}10✓)}$$
$$\qquad\Longrightarrow\ \textbf{层数 }m\ \text{从 1 到 }n\ \text{全部一样 ⟹ \textbf{refinement 增益 ＝ 0}}✗✓\ \big(\text{含 }m=n\ \text{即覆盖条件本体层 ✓}\big)$$
$$\boxed{\textbf{(3) ★★引擎定位（诊断 ✓✓）}:\ \text{Östergård--Blass 的引擎\ } \textbf{不是}\ \text{ LP ✗; 而是}\ \textbf{整性 ＋ 不等价分布分类 ＋ 递归}\ ✓✓}$$
$$\qquad\text{LP 在该方法中的真实角色 ＝ }\textbf{剪枝／校验}\ ✓\ \big(\text{因其松弛恰好只给体积界}\ ✓\big);\ \text{全部强度必来自}\ \textbf{整性约束 + 分支}\ ✓✓$$

---

## §1 系统与实现（**与档案一致 ✓**）

$$\text{分区}: \text{固定前 }m\ \text{坐标} \Longrightarrow t=2^m\ \text{cells，每 cell }s=2^{n-m}\ \text{词}✓;\ y_i=|C\cap\mathrm{cell}_i|✓\ \big(\text{MCOVER ✓}\big)$$
$$A_{ii}=n+1-m;\quad A_{ij}=\mathbf 1_{\{d(i,j)=1\}};\quad A_{ij}=0\ (d\ge2)\ ✓\ \big(n=9\Rightarrow 10-m✓\ \text{与档案一致}✓;\ n=10\Rightarrow 11-m✓\ \text{C-429}✓\big)$$
$$\textbf{系统}:\ \sum_jA_{ji}y_j\ \ge\ s\quad(\forall i);\qquad 0\le y_i\le s;\qquad \sum_iy_i=M\qquad\Longrightarrow\quad L(m):=\min\Big\{\sum_iy_i:\ A^{T}y\ge s\mathbf 1,\ 0\le y\le s\Big\}$$
$$\textbf{合法性 ✓}:\ \text{任一覆盖码 }C\ (|C|=M)\ \text{给出整可行 }y \Longrightarrow L(m)\le M \Longrightarrow \boxed{L(m)\ \text{是 }K(n,1)\ \text{的合法下界}}✓$$
$$\textbf{脚本 ✓}:\ \texttt{scripts/SUBSPACE\_LP\_2026-09-28\_level\_m\_bound.py}（`scipy.optimize.linprog`／HiGHS ✓；经 `~/.openclaw/workspace/scripts/pyguard.sh 800` ✓）$$

## §2 实测输出（**逐字 ✓**）

```
n = 9   volume/sphere bound 2^n/(n+1) = 51.200000
  m   t=2^m  s=2^(n-m)           L(m)     L(m)-vol  status
  1       2        256      51.200000     0.000000       0
  2       4        128      51.200000     0.000000       0
  3       8         64      51.200000     0.000000       0
  4      16         32      51.200000    -0.000000       0
  5      32         16      51.200000     0.000000       0
  6      64          8      51.200000     0.000000       0
  7     128          4      51.200000    -0.000000       0
  8     256          2      51.200000     0.000000       0
  9     512          1      51.200000     0.000000       0

n = 10   volume/sphere bound 2^n/(n+1) = 93.090909
  m   t=2^m  s=2^(n-m)           L(m)     L(m)-vol  status
  1       2        512      93.090909     0.000000       0
  ...  （m=2..10 全部 93.090909，$L(m)-$vol $=0.000000$ ✓）
 10    1024          1      93.090909     0.000000       0
```
（完整逐字见 `scripts/SUBSPACE_LP_2026-09-28_level_m_bound.txt` ✓）

## §3 诊断（**武器 B 的哪一层有/没有汁水 ✓✓**）

$$\textbf{武器 B ＝ subspace recursion ＋ conditional LP};\ \text{本档测的是其中的\ \textbf{LP 层}}✓$$
$$\qquad\textbf{结果}:\ \text{LP 层在**任何** }m\ \text{都只给 }2^n/(n+1)：n=9\ \text{给 }51.2\ (\text{而真值 }62✓);\ n=10\ \text{给 }93.09\ (\text{而目标 }107\text{–}120✓)$$
$$\Longrightarrow\ \boxed{\text{LP 层贡献 ＝ }0\ ✗;\ \text{故 OB 机制的全部强度必来自\ \textbf{整性 + 不等价分布的分支排除}✓✓}}$$
$$\textbf{（结构原因 ✓）}:\ \text{系统\ \textbf{双重平衡}（每列和 }=|B_1(c)|=n+1✓\ \text{、每行 }s\ \text{同值}✓\big) \Longrightarrow \text{均匀分数解总最优} ⟹ \text{松弛恒为体积界}✓✓$$
$$\textbf{（与既有基线对照 ✓）}:\ \text{Delsarte/Krawtchouk LP }=\mathbf{94.0198}>\mathbf{93.0909}✓ \Longrightarrow \text{本 cell-LP\ \textbf{严格弱于}关联方案 LP}✗✓\ \big(\text{后者才加 }0.93✓\big);\ \text{SDP }=105.2223✓$$
$$\textbf{（与档案旧测的关系 ✓）}:\ \text{MCOVER 的"实测收紧律 }1.21\to1.09\text{"是\ \textbf{真实码}的 cell 比值}✓,\ \text{非 LP 界}✗;\ \text{本档补上的正是那块空白（LP 从未跑过 ✓）}$$

## §4 **Test C 的下一步**（**真正的 branch factor 在哪 ✓✓，登记未跑 ⚠️**）

$$\text{既然 LP 层零增益，则应直接测\ \textbf{整层}：}\ \text{对给定 }m,M:\ \#\Big\{y\in\mathbb Z_{\ge0}^{2^m}:\ A^{T}y\ge s\mathbf 1,\ 0\le y\le s,\ \sum_iy_i=M\Big\}\Big/\text{（码等价群 }B_n\ \text{轨道}✓\Big)$$
$$\Longrightarrow\ \text{此即唐先生所要的 \textbf{branch factor} ✓✓}:\ \text{若 }N_0\to N_1\to\cdots\ \text{随 }m\ \text{坍缩 ⟹ 递归有效}✓;\ \text{若 }m\ \text{增大到 }n\ \text{仍无坍缩 ⟹ OB 机制在 }n=10\ \text{不够}✗✓$$
$$\qquad\textbf{（可执行性 ✓）}:\ m\le4\ (t\le16)\ \text{可直接枚举 }y\ (0\le y_i\le s✓)\ \text{＋ }\sum y_i=M\ \text{过滤}✓;\ m\ \text{更大需 DP/母函数 ⚠️};\ \text{登记未跑 ✗}$$
$$\textbf{（附加约束可挂 ✓ Test B）}:\ \text{① 自由坐标引理（无 free coordinate ✓ 顶层剪枝）};\ \text{② }(\alpha)(\alpha')✓;\ \text{③ C-419/C-430 折衷 ✓};\ \text{④ 120-cover 对称/切换模式对比 ✓}\ \big(\text{档案有有效 120-码 } \texttt{work/k10/kamenetsky120.txt}✓\big)$$

## §5 状态（**不替唐先生做决定 ✓**）

$$\text{本档产出}:\ \text{① 等号定理 ✓✓；② 零增益实测 ✓✓；③ 引擎定位（强度在整性/分支，非 LP）✓✓；④ Test C 下一步的具体形式 ✓}$$
$$\text{未做}:\ \text{整分布枚举 ✗};\ \text{SDP 归因 ✗};\ \text{未改门 ✗};\ \text{未做任何路线裁定 ✗}\ \big(\text{照唐先生 23:54 ✓}\big)$$

## §6 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "零增益" "等号定理" "整性引擎" "cell-LP"
技术词 零增益     命中文件数=10   :: ./NEGATIVE-RESULTS-2026-09-12-ROUND.md ./C320-directed-recheck-…-M5-question-OPEN.md ./V118-fourth-detection-mode.md …
技术词 等号定理   命中文件数=3    :: ./E-GATE-and-Lemma-R-R2-CLOSED.md ./LEMMA-R-P1-CLOSED-…md ./INDEPENDENT-PROBLEM-HUNT-round1.md
技术词 整性引擎   命中文件数=0    ::
技术词 cell-LP    命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间／属线未定（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 零增益 | 0（10 命中多在 `NEGATIVE-RESULTS-*`／`C320-*`／`V118-*` ⟹ **属线未定 ⟹ 不计** ✗） | 10 | 0（既有词 ✓） |
| 等号定理 | 0（3 命中属 `E-GATE`／`LEMMA-R-P1`／`HUNT-round1` ⟹ **属线未定 ⟹ 不计** ✗） | 3 | 0（既有词 ✓） |
| 整性引擎 | 0 | 0 | 0（本档自造标签 ✓） |
| cell-LP | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（`整性引擎`／`cell-LP` 两空间皆 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 系统 ＋ §2 实测 ＋ §3 等号定理与诊断 ＋ §4 下一步形式**（推导 ＋ 计算 ✓）

## §7 边界（硬 ✓）

- **有计算**（小 LP ✓，经 pyguard ✓，单线程 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§6 已分栏 ✓）
- **不作路线裁定** ✓（照唐先生 23:54 令 ✓）：本档只报"LP 层零增益 ＋ 强度在整性/分支"这一事实与推论 ✗
- 数值口径 ✓：$93.090909$＝体积界（与档案基线一致 ✓）；$94.0197982$＝Delsarte LP ✓；$105.2223$＝SDP ✓；$107$＝文献下界（BÖW 2004 ✓）；$120$＝文献上界 ✓
