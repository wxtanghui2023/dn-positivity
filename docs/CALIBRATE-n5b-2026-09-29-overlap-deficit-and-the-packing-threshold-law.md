# CALIBRATE-n5-b（2026-09-29）—— **overlap deficit 三条纠正；正确恒等式；$\mathrm{Def}{=}0\iff k\le A(m,3)$ 之\ \textbf{packing 阈值律}**

> **性质**：**机制提炼（A 之首刀）＋ 数值校准**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 15:5x ✓
> **唐先生令**：选 A；先完整提炼 $k{=}3$，再测 $\alpha(Q_5,k)$ ✓

**已查地图**：`CALIBRATE-n5`（defect 递归复现 7）✓

D0: 本档对象 ＝ **档案已有**（球交／容斥／packing 数——皆经典 ✓）
D1: 0（产出＝**三处纠正 ＋ 一恒等式 ＋ 一阈值律 ＋ 一局部律之转移效果** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ }|B_1(a)\cap B_1(b)|:\ d{=}2\ \textbf{亦为 }2\ (\text{你写 }0)\ ——\ \text{实测 }(1,2){:}80,\ (2,2){:}160,\ (3,0){:}160,\ (4,0){:}80}$$
$$\boxed{\text{② ✗ }\tau(A)\ne0:\ \text{三个两两距离 }2\ \text{之中心\ \textbf{有公共点}}（大小 }1）;\ \text{你写 }\tau{=}0}$$
$$\boxed{\text{③ ✗✗ 致命}:\ \alpha(Q_4,3)=\mathbf{0}\ ——\ Q_4\ \text{存在三点\ \textbf{两两距离 }2\ 且无任何距离-1 边}\Longrightarrow \text{亏损\ \textbf{不来自}被迫距离-1 边}}$$
$$\boxed{\text{④ ✓ 正确恒等式}:\ |N_1(A)|=(m{+}1)k-T(A),\quad T(A)=\sum_x\max(0,\mu(x)-1)\ (\text{重叠总数})}$$
$$\boxed{\text{⑤ ★ 阈值律}:\ \mathrm{Def}(m,k)=0\iff k\le A(m,3)\ (\textbf{packing 数});\ \text{首亏在 }k{=}A(m,3){+}1}$$

## §1 三处纠正（**✗✗ + ✗**）

$$(\text{i})\ |B_1(a)\cap B_1(b)|=2\ \text{当}\ d(a,b)\in\{1,\mathbf{2}\};\ =0\ \text{当}\ d\ge3✓\ (\text{你漏 }d{=}2)$$
$$(\text{ii})\ \text{三重交非空}:\ x{=}0,\ \text{中心 }e_1,e_2,e_3\ (d{\equiv}2)\Rightarrow 0\in\cap_3 B_1✓\Longrightarrow\tau\ne0$$
$$(\text{iii})\ \textbf{致命}:\ \text{实测 }\alpha(Q_4,3)=\min_{|A|=3}(\text{距离-1 边数})=\mathbf{0}$$
$$\qquad\text{（例：}0000,\ 0011,\ 1100\ \text{型之三点，两两距离 }2）\Longrightarrow\ e(A)\ge1\ \textbf{为假}$$
$$\therefore\ \text{亏损 }2\ \text{之源\ \textbf{不是}距离-1 边，而是\ \textbf{距离-2 对}}（与三重交修正）✓$$

## §2 ④ 正确恒等式（**✓ 全量核验**）

$$\textbf{用 multiplicity 表示最简单}:\quad \mu(x):=|C\cap\{x\}|\ \text{之邻域计数};\quad \sum_x\mu(x)=(m{+}1)k$$
$$\boxed{|N_1(A)|=(m{+}1)k-T(A)},\qquad T(A)=\sum_{x:\mu(x)\ge2}\bigl(\mu(x)-1\bigr)\ \ (\text{重叠总单位})✓$$
$$\text{核验}:\ m{=}4,k{=}3;\ m{=}5,k{=}3,4\ \text{各 4000 例，恒等式\ \textbf{全部成立}}✓$$
$$\text{而 }T\ \text{之解析表达才需 }\mathrm{P2}\ \text{与三重交}:\ |N_1|=3(m{+}1)-2\,\mathrm{P2}+\tau\ (\text{其中 }\mathrm{P2}=\#\{\text{对}:d\le2\})✓$$

## §3 ⑤ ★ 阈值律（**本档最重要**）

$$\textbf{实测 }Q_5\ (\text{容量 }6k):$$
| $k$ | $\max|N_1|$ | $6k$ | $\mathrm{Def}$ | $\min T$ |
|---|---|---|---|---|
| $1$–$4$ | $6,12,18,24$ | 同 | $\mathbf{0}$ | $0$ |
| $5$ | $26$ | $30$ | $\mathbf{4}$ | $4$ |
| $6$ | $30$ | $36$ | $\mathbf{6}$ | $6$ |

$$\therefore\ \boxed{\mathrm{Def}=0\iff k\le A(m,3)}\ (\text{可容 }k\ \text{个半径-1 球\ \textbf{互不相交}}\iff\text{中心两两距离}\ge3)✓$$
$$\text{实测}:\ A(4,3)=\mathbf{2}\ (\text{故 }k{=}3\Rightarrow\mathrm{Def}{=}2✓);\quad A(5,3)=\mathbf{4}\ (\text{故 }k{=}5\ \text{首亏}✓)$$
$$\therefore\ \text{可传递之局部律}:\quad \boxed{k>A(m,3)\ \Longrightarrow\ |N_1(A)|\le(m+1)k-\mathbf{1}}✓$$

## §4 该律对 $n{=}5$ 之效力（**✓ 有进步但仍差 1**）

$$\text{纤维界}:\ |B|\ge V-|N_1(A)|\ge16-5a+\mathrm{Def}(4,a);\quad M\ge16-4a+\mathrm{Def}(4,a)$$
- 仅容量（$\mathrm{Def}{\equiv}0$）：$M\ge\mathbf{4}$ ✗
- 加阈值律（$\mathrm{Def}(4,3){=}2$）：$M\ge\mathbf{6}$ ✓
- 真值：$K(5,1)=\mathbf{7}$ ⟹ **仍差 1** ✗（须再加"$B$ 覆盖 $V\setminus A$"之完整信息，即 fiber 对的精确条件 ✓）

## §5 下一步（**A 之续刀，供唐先生定**）

$$\textbf{A-1}:\ \text{求 }\mathrm{Def}(m,k)\ \text{在 }k>A(m,3)\ \text{处之\ \textbf{首个精确值}}（Q_5: k{=}5\Rightarrow4,\ k{=}6\Rightarrow6;\ \text{试定 }\mathrm{Def}=f(k-A(m,3))?）✓$$
$$\textbf{A-2}:\ \text{消元 }T\ \text{之二次项，把阈值律写成\ \textbf{中心点集之纯组合}条件（“}k\ \text{点必含一对距离}\le2\text{”）✓}$$
$$\textbf{A-3}:\ \text{问}:\ \text{packing 阈值律能否替代 }n{=}6\ \text{之 }2^{32}\ \text{枚举}✓\ (\text{即：能否只用 }A(m,3)\ \text{与 }\mathrm{Def}\ \text{给出 }K(6,1)\ge12)✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "overlap deficit" "packing threshold" "局部律转移"
技术词 overlap deficit   命中文件数=0    ::
技术词 packing threshold  命中文件数=0    ::
技术词 局部律转移        命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **全量实测（$Q_4$、$Q_5$ 各 $k$ 之 $\max|N_1|$、恒等式 4000 例核验、$\alpha$ 实测）** ✓；**不占 C 号** ✓；**未用 SAT/CP-SAT** ✓
- **不主张** $K(5,1)$ 之值有疑 ✗；本档为**局部律**之提炼 ✓
