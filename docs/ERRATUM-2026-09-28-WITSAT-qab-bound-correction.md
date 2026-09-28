# ERRATUM-2026-09-28 · **WITSAT §0(3) 勘误**：$\sum q_{ab}\ge|U^c|$ **不成立** ✗ → 应为 $\ge|X_L|$（＋ 两新结论）

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **性质 ✓**：**制度性勘误**（自查发现，当日发出 ✓）—— 按项目纪律「结果异常先怀疑自己的分支」✓ ＋「同源错误须定点重写」✓。
> **范围 ✓**：仅勘误 C-437 的一步 ＋ 补两条**由修正引出的新结论**；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-437／C-436／C-435，非新案 ✓）**
`docs/WITSAT-2026-09-28-…`（**被勘误档 ✓**）｜`docs/WITW2C-2026-09-28-…`（**双色条件／$X_L$ 定义 ✓✓**）｜`docs/WITFIB-2026-09-28-…`（**精确等价 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** $q_{ab}$／$X_L$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出该步勘误 ＋ $|X_L|\le72\min(|A|,|B|)$ ＋ 局部模型的\textbf{不可完成性证明}** ✓）
**[RESEARCH]**

---

## §0 勘误与新结论（**✗勘误 ✓✓｜新必要条件 ✓✓｜局部模型不可完成（证明）✓✓｜二择 ✓**）

$$\boxed{\textbf{✗ 勘误}:\ C-437\ §0(3)\ \text{所写的}\ \ \sum\nolimits_{a\in A,b\in B}q_{ab}\ \ge\ |U^c|\ \ge\ 450\ \ \textbf{不成立}\ ✗✓}$$
$$\qquad\textbf{出错点 ✓}:\ \text{该步需要"每个 }x\in U^c\ \text{都同时有 }A\text{-邻与 }B\text{-邻"}\ ✗;\ \textbf{实际只对无 }H\text{-邻的点成立}✓✓$$
$$\qquad\textbf{正确形式 ✓✓}:\ \boxed{\sum_{a\in A,\,b\in B}q_{ab}\ \ge\ \big|X_L\big|}\qquad \big(X_L:=U^c\cap D=\{\,x\notin U:\ N(x)\cap H=\varnothing\,\}\ ✓\big)$$
$$\qquad\textbf{（恒等式本身 ✓\ 不受影响）}:\ \sum_{a,b}q_{ab}=\sum_{x\in U^c}\big|N(x)\cap A\big|\cdot\big|N(x)\cap B\big|\ ✓\ \big(\text{纯计数 ✓，已逐项核 ✓}\big)$$
$$\boxed{\textbf{★ 新必要条件 1（✓✓）}:\ x\in X_L\Longrightarrow|N(x)\cap A|\ge1\ \wedge\ |N(x)\cap B|\ge1\ \big(\text{无 }H\text{-邻 + 双色要求}✓\big) \Longrightarrow 72\min(|A|,|B|)\ \ge\ \sum q_{ab}\ \ge\ |X_L|✓✓}$$
$$\qquad\Longrightarrow\ \boxed{\ |X_L|\ \le\ 72\min(|A|,|B|)\ }\ ✓✓\ \big(\text{因每个距离-2 对 }\le2\ \text{个 }X_L\text{-点}✓,\ \text{而 }A\text{-}B\text{ 距离-2 对}\le36\min(|A|,|B|)✓\big)$$
$$\boxed{\textbf{★ 新必要条件 2（✓✓ 沿用重容量）}:\ |X_L|\ \ge\ (512-s)-9|H|\ =\ \boxed{\max\big(0,\ 8s-559\big)}\ ✓✓}$$
$$\qquad\textbf{组合核对 ✓}:\ 8s-559\le36(2s-119)\iff 3725\le64s\iff s\ge58.2\ ✓\ \textbf{平凡}✗✓ \Longrightarrow \textbf{修正后链条无矛盾}（与 C-436 §9 一致 ✓）$$
$$\boxed{\textbf{★ 新结论 3（✓✓ 局部模型不可完成 —— 由 ⚠️ 升级为\textbf{定理}）}:\ C-437\ §5\ \text{的构型}\ (s=78,\ |A|=1,\ |B|=36,\ |U^c|=434) \Longrightarrow}$$
$$\qquad 9\big|C_0\big|=9\big(|H|+|A|\big)=9(41+1)=378\ <\ 434=|U^c| \Longrightarrow \text{违反 }U^c\subseteq N(C_0)✗✗ \Longrightarrow \textbf{该局部模型不可全局完成}✓✓$$
$$\boxed{\textbf{★ 二择（✓✓ 与 C-436 §6 一致）}:\ \text{① }U^c\subseteq N(H)\Longrightarrow s\le69\ \wedge\ \exists\,\ell\in L:\ N(\ell)\cap H=\varnothing\ \big(\text{否则 }H\ \text{成 cover}\Rightarrow|H|\ge62\Rightarrow s\le57\ \text{与 }s\ge62\ \text{矛盾}✗\big)；\quad \text{② 否则 }X_L\ne\varnothing✓}$$

---

## §1 勘误细节（**为什么 $\ge|U^c|$ 不成立 ✗✓**）

$$\text{取 }x\in U^c\ \textbf{且} N(x)\cap H\ne\varnothing\ (\text{存在，见 §3 的二择 ①}\ ✓):\quad \text{此时 }x\ \text{的两色要求可由\ \textbf{同一个 heavy 邻点}满足}\ ✓✓\ \big(h\in H\subseteq C_0\cap C_1✓\big)$$
$$\qquad\Longrightarrow\ x\ \text{可以}\ \textbf{完全没有 }A\text{-邻点或完全无 }B\text{-邻点}\ ✗ \Longrightarrow |N_A(x)|\cdot|N_B(x)|=0 \Longrightarrow \textbf{该点对 }q_{ab}\ \text{零贡献}✗✓$$
$$\Longrightarrow\ \sum q_{ab}\ \ge\ \big|\{x\in U^c:\ |N_A(x)|\ge1\ \wedge\ |N_B(x)|\ge1\}\big|\ =\ |X_L|\ ✓✓\ \big(\text{因 }x\in X_L\iff N(x)\cap C_0\subseteq A\ \wedge\ N(x)\cap C_1\subseteq B✓\big)$$
$$\textbf{（教训 ✓）}:\ \text{上一步把"存在 heavy 邻点"这一\ \textbf{替代路径}\ 漏掉 ✗；同型失误在本线已多次出现（"只考虑一条路径"）✓ \Longrightarrow \textbf{凡"每点 $\ge1$"型断言，须先列出该点的\ \textbf{全部} 满足路径 ✓✓}}$$

## §2 修正后的链条（**✓ 一致，无矛盾**）

```
119-cover  ==>  U^c ⊆ N(C_0) ∩ N(C_1)                    (C-437 §0(1) ✓ 不受影响)
             ==>  每点 x ∈ U^c: 有 heavy 邻  或  (A-邻 且 B-邻)     (✓ 二择)
             ==>  记 X_L := U^c ∩ {无 heavy 邻}
             ==>  Σq_ab  ≥ |X_L|  且  Σq_ab ≤ 72·min(|A|,|B|)      (✓✓ 新)
             ==>  |X_L| ≤ 72·min(|A|,|B|)  且  |X_L| ≥ max(0,8s-559) (✓✓)
             ==>  8s-559 ≤ 36(2s-119)  <=>  s ≥ 58.2  (平凡, 无矛盾) ✓
```

## §3 两新结论的证明（**✓✓**）

$$\textbf{结论 3 ✓✓}:\ \text{局部模型给 }|H|=41,\ |A|=1 \Longrightarrow |C_0|=42 \Longrightarrow |N(C_0)|\le9\cdot42=378✓;\ \text{但 }|U^c|=512-78=434>378✗ \Longrightarrow U^c\not\subseteq N(C_0)✗$$
$$\qquad\textbf{（意义 ✓✓）}:\ \text{C-437 §5 的构型只证明"局部禁配不存在"✓；现\ \textbf{已证} 它\ \textbf{不可能}\ 嵌入任何 119-cover ✓✓ \Longrightarrow \text{饱和事件的局部可构造性}\ \textbf{不蕴含} 全局可行性 ✓（\textbf{局部 vs 全局的真实缺口}被显式量化 ✓）}$$
$$\textbf{结论 2 ✓}:\ |X_L|=|U^c\setminus N(H)|\ \ge\ |U^c|-|N(H)|\ \ge\ (512-s)-9|H|=(512-s)-9(119-s)=8s-559✓✓$$
$$\textbf{（注 ✓）}:\ s\le69\ \text{时 }8s-559\le-7<0 \Longrightarrow \text{取 }\max(0,\cdot)✓;\ \text{即 }s\le69\ \text{时该界为空}✓\ \text{—— 与二择①相容}✓$$

## §4 状态（**不作路线裁定 ✗**）

$$\textbf{受影响 ✓}:\ C-437\ §0(3)\ \text{的}\ \ge|U^c|\ge450\ \text{一步 ✗（已在 registry C-438 标注 ✓）};\ \text{其余（精确条件／修正／饱和自足／局部模型）\ \textbf{不受影响}}✓$$
$$\textbf{新增 ✓}:\ |X_L|\le72\min(|A|,|B|)✓;\ |X_L|\ge\max(0,8s-559)✓;\ \textbf{局部模型不可完成（定理）}✓✓;\ \text{二择}✓$$
$$\textbf{不变 ✗}:\ C-437\ \text{的}\ n_2\ \text{无局部上界结论}\ \textbf{成立}✓\ \big(\text{该论证只用局部结构，未用被勘误的不等式}✓\big)$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "非可完成性" "逐点乘积" "制度性勘误"
技术词 非可完成性  命中文件数=0    ::
技术词 逐点乘积    命中文件数=0    ::
技术词 制度性勘误  命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 非可完成性 | 0 | 0 | 0（本档自造标签 ✓） |
| 逐点乘积 | 0 | 0 | 0（本档自造标签 ✓） |
| 制度性勘误 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词**两空间皆 0** ⟹ 自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 勘误定位 ＋ §0 三新结论 ＋ §3 证明**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **同引要求 ✓**：本档须与 C-437 同引（勘误关系 ✓）；C-437 §0(3) 的该步**作废** ✗，其余部分仍有效 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）
- **不声称** 119 已排除 ✗；**不声称** $\sum q_{ab}\ge|U^c|$（该式已被否证 ✗✓）；不声称 P1 成立 ✗（V290）
