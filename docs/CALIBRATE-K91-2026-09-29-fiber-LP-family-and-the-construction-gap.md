# CALIBRATE-K9（2026-09-29）—— **$K(9,1)$：纤维-LP 族只给球界 $52$（决定性）；构造搜索仅到 $66$（能力缺口）**

> **性质**：**能力校准链（P1 ＋ P2 之首刀）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 14:2x ✓
> **唐先生令**：选 1；先拆 Östergård–Blass 之 $57\to62$ 机制；不开 SAT/CP-SAT ✓

**已查地图**：`DERIVE-107*`（九支线之关闭）／本会话全部 ✓

D0: 本档对象 ＝ **档案已有**（$K(n,1)$／球界／纤维分解——皆经典 ✓）
D1: 0（产出＝**一决定性机制结论 ＋ 一能力缺口之量化** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 决定性（P1）}:\ \text{纤维-分布 LP 族（}r{=}1\dots8\text{）\ \textbf{一律只给球界 }52\Longrightarrow\ 57\to62\ \textbf{不可能}来自任何 LP／不等式}}$$
$$\boxed{\text{② ⟹ 该跃升只能来自\ \textbf{整数枚举 ＋ LP 剪枝}（即文献之"细化至维数 }0\text{"）}}$$
$$\boxed{\text{③ ✗ 能力缺口（P2）}:\ \text{"移除-修复"局部搜索 }\mathbf{170s/20\ \text{万迭代}}\ \text{只到 }\mathbf{66}\ (\text{真值 }62)\Longrightarrow\ \text{差 }6.5\%}$$
$$\boxed{\text{④ ⟹ 校准答案}:\ \text{机制\ \textbf{可拆}}（且已证明 LP 非承重）;\ \text{但\ \textbf{枚举/构造不可复现}}}$$

## §1 ① 纤维-分布 LP（**✓✓ 决定性**）

$$\text{固定 }r\ \text{个坐标}\Longrightarrow 2^r\ \text{个纤维};\ N_u=\#\{c\in C: c|_r=u\};\ \text{覆盖 }\Longrightarrow$$
$$\boxed{(10-r)N_u+\sum_{v\sim u}N_v\ \ge\ 2^{\,n-r}}\qquad(\forall u,\ n{=}9)$$
$$\text{实测（}r=1..8\text{，}M=50..62\text{）}:\ \textbf{一律}\ M\ge52\ \text{可行},\ M\le51\ \text{不可行}$$
| $r$ | $M{=}50$ | $51$ | $52$ | $\dots$ | $62$ |
|---|---|---|---|---|---|
| $1$–$8$ | N | N | **Y** | Y | Y |

$$\textbf{理论（与 }r\ \text{无关）}:\ \sum_u\bigl[(10-r)N_u+\sum_{v\sim u}N_v\bigr]=(10-r)M+rM=10M\ \ge\ 2^r\cdot2^{9-r}=512$$
$$\therefore\ M\ge51.2\ \Longrightarrow\ \boxed{\text{LP 族恒等于球界 }52}\ ——\ \text{与 }r\ \text{无关}✓✓$$
$$\therefore\ \boxed{57\to62\ \text{之跃升\ \textbf{不可能}来自任何此类 LP／线性不等式}}✓$$

## §2 ② 机制之定位（**✓ 拆出来了**）

$$\text{文献描述}:\ \text{"subspace 中码字分布}\to\text{反复解 LP}\to\text{仅取不等价分布}\to\text{细化至维数 }0\text{"}$$
$$\text{与本档实测对照}:\ \text{LP 本身只给 }52;\ \text{故 LP 之作用\ \textbf{是剪枝（pruning），不是下界本身}}$$
$$\therefore\ \boxed{\text{承重者为\ \textbf{枚举之完全性} ＋ LP 之剪枝}\ (=\ \text{LP-pruned 分支限界})}✓$$
$$\therefore\ \text{历史链}\ 52\to54\to55\to56\to57\ \text{来自\ \textbf{更强组合不等式}};\ \ 57\to62\ \text{来自\ \textbf{枚举}}✓$$

## §3 ③ 能力缺口（**✗ 量化**）

$$\text{方法}:\ \text{贪心初值}\ (80)\ +\ \text{移除-修复局部搜索};\ \textbf{170s},\ 20.4\ \text{万迭代}$$
$$\textbf{结果}:\ \text{最佳 }\mathbf{66}\ (\text{覆盖已验证}\ ✓),\ \text{而真值 }K(9,1)=62\Longrightarrow\ \text{差 }\mathbf{6.5\%}$$
$$\therefore\ \text{已得之可复跑证书}:\ K(9,1)\le\mathbf{66}\ (\text{弱上界};\ \text{非 }62)✗$$
$$\text{（}n=10\ \text{之同类搜索此前达 }120\text{-码量级};\ \text{故我们之构造能力\ \textbf{不足以}重现 }62\text{ 之最优构造}✗）$$

## §4 ④ 校准答案（**对唐先生核心问题之回答**）

$$\textbf{问}:\ \text{我们能否从已有结果中"抽出机制并自行重建"？}$$
$$\textbf{答（分两层）}:\ \text{①}\ \textbf{机制层 ✓}:\ \text{可拆（且已判定 LP 非承重、枚举承重）};\ \text{②}\ \textbf{实现层 ✗}:\ \text{枚举与最优构造皆不可复现}$$
$$\therefore\ \boxed{\text{此前九支线之失败\ \textbf{不是"机制理解错误"},\ 而是\ \textbf{实现（枚举/构造）能力不足}}}✓$$
$$\therefore\ \text{对 }107\ \text{之推论}:\ \text{若要 }106\ \text{不可能之证，须\ \textbf{枚举型}证明};\ \text{而枚举能力恰为我方短板}\Longrightarrow\ \text{应\ \textbf{换手段}（增强枚举/剪枝）而非继续找不等式}}✓$$

## §5 下一步（**P2 之正路，候唐先生定**）

$$\textbf{路线 A}:\ \text{改进构造搜索（加入精确算法：}ILP／\text{置换群约化}）\ \text{以求 }62\ \text{之 certificate}✓$$
$$\textbf{路线 B}:\ \text{改进剪枝枚举（实现"纤维细化 ＋ LP 剪枝"之原型）\ \text{以求 }M\le61\ \text{之不可行性}✓$$
$$\textbf{路线 C}:\ \text{接受校准结论，归档九支线 ＋ 本档}✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "纤维LP族只给球界" "57到62非LP机制" "能力校准K91"
技术词 纤维LP族只给球界   命中文件数=0    ::
技术词 57到62非LP机制   命中文件数=0    ::
技术词 能力校准K91     命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **LP 族全量实测（$r{=}1..8$, $M{=}50..62$）＋ 求和论证 ＋ 构造搜索实测** ✓；**不占 C 号** ✓；**未用 SAT/CP-SAT** ✓（遵你令）
- **不主张** $K(9,1)$ 之值有疑 ✗（$=62$ 为已定值 ✓）；本档仅校准**我方能力**✓
