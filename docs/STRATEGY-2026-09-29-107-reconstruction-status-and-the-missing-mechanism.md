# STRATEGY（2026-09-29）—— **107 重建之现状：目标形式、机制天花板、缺失机制之定位**

> **性质**：**战略裁定 ＋ 实验**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 15:1x ✓
> **唐先生令**：总课题＝判断 $107$–$120$ 区间我方方法可推进到哪；先独立重现 $107$ ✓

**已查地图**：`DERIVE-107*`（$6E$ 形式）／`CALIBRATE-K9*`／`CALIBRATE-n*`✓

D0: 本档对象 ＝ **档案已有**（van Wee／球界／SDP／cell 系统—皆经典 ✓）
D1: 0（产出＝**目标形式 ＋ 天花板表 ＋ 缺失机制之定位 ＋ 一实验** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 目标形式}:\ K(10,1)\ge107\iff \boxed{6E+M\ge1024}\iff 67M\ge7168\ (E{=}11M{-}1024)}$$
$$\boxed{\text{② ⟹ 107 ＝ 把 van Wee 之系数 }9\ \textbf{改到 }6}$$
$$\boxed{\text{③ ✗ 实测（本轮）}:\ \text{cell 整性系统（}r{=}1..5\text{）对 }M{=}105/106/107\ \textbf{全部可行}\Longrightarrow \text{单元整性层不给 }107}$$
$$\boxed{\text{④ ✗ 深洞路线已饱和}:\ \sum_{\text{深洞}}E(B(x,1))/E=8.31\ (120\text{-code})\Longrightarrow\ \text{榨不出 }6}$$
$$\boxed{\text{⑤ ⟹ 缺失机制}:\ \text{一个\ \textbf{全局}整性论证（非松弛、非纤维/单元局部）}}$$

## §1 目标形式（**✓**）

$$E=11M-1024;\qquad 9E\ \ge\ 1024-M\ \Longrightarrow\ M\ge102.4\Rightarrow103\ (\text{van Wee})$$
$$6E+M\ \ge\ 1024\iff 67M\ \ge\ 7168=7\cdot2^{10}\iff M\ \ge\ 106.99\Rightarrow107✓$$
$$\therefore\ \boxed{\text{107 之内容 ＝ 充电系数由 }9\ \text{改进到 }6}\ (\text{等价：}\#\{\text{非码字}\}\le6E)$$

## §2 机制天花板（**✓ 全表**）

| 机制 | 界 | 类型 | 瓶颈 |
|---|---|---|---|
| 球界 | $94$ | 松弛 | — |
| van Wee／excess 深洞 | $103$ | 松弛/充电 | 系数 $9$，实测 $8.31$ **饱和** |
| 单条线性不等式（结合方案层） | $103$ | 松弛 | 层封闭 |
| Zhang 覆盖设计 | $105$ | **整性** | 设计计数到顶 |
| SDP-3（Gijswijt–Polak 2025） | $105.2223\Rightarrow106$ | 松弛 | **层次不可升**（作者自述） |
| **目标** | $\mathbf{107}$ | **须整性** | $107>105.2223$ |

$$\therefore\ \boxed{107>105.2223\ \Longrightarrow\ 107\ \textbf{不可能}来自任何松弛法\Longrightarrow\ \textbf{必须整性}}$$

## §3 本轮实验：单元整性系统（**✗ 不足**）

$$\text{固定 }r\ \text{坐标}\Rightarrow2^r\ \text{单元};\ N_u\ \text{为整数};\ \text{约束}\ (11-r)N_u+\sum_{v\sim u}N_v\ \ge\ 2^{10-r}$$
$$\text{（同单元一字覆盖 }1+(10-r)\ \text{点；相邻单元一字覆盖 }1\ \text{点）}$$
| $r$ | $2^{10-r}$ | $M{=}105$ LP/ILP | $M{=}106$ LP/ILP | $M{=}107$ LP/ILP |
|---|---|---|---|---|
| $1$–$5$ | $512,256,128,64,32$ | Y/Y | **Y/Y** | Y/Y |

$$\text{理论}:\ \sum_u\bigl[(11-r)N_u+\sum_{v\sim u}N_v\bigr]=11M\ \ge\ 2^r\cdot2^{10-r}=1024\ \Longrightarrow\ M\ge93.09\ (\text{球界})$$
$$\therefore\ \boxed{\text{LP 一切 }r\ \text{可行};\ \text{且\ \textbf{整数化亦可行}}（M{=}106）\Longrightarrow\ \text{单元整性层\ \textbf{不足}}}✗$$

## §4 缺失机制之定位（**✓ 本档核心**）

$$\boxed{\text{须一个\ \textbf{全局}整性论证}:\ \text{非}\{A_i\}\text{之函数（松弛，}\le105.2223\text{）};\ \text{非 unit/cell 单元层（}\le94\text{）}}$$
$$\text{已知此类机制之唯一样本}:\ \text{Zhang 覆盖设计计数（得 }105\text{）及其\ \textbf{强化}}（\text{得 }107）$$
$$\text{而强化之唯一实现}:\ \text{Bertolo–Östergård–Weakley 2004 之 general }R{=}1\text{ lower bound}\ ——\ \textbf{正文不可得}✗$$
$$\therefore\ \boxed{\text{我方现有机制\ \textbf{不能}产出 }107;\ \text{缺口 ＝ 全局整性论证}}$$

## §5 本项目状态表（**按唐先生框架**）

| 层级 | 目标 | 状态 |
|---|---|---|
| 总课题 | $107$–$120$ 可推进到哪 | 进行中 |
| 里程碑一 | 独立重现 $107$ | **未完成**（缺口已定位） |
| 里程碑二 | $107\Rightarrow108+$ | 未进入 |
| 最终 | 我方方法能否逼近 $120$ | 未知 |
| 副产品 | $K(5,1){=}7$；$K(6,1)\ge12$；$\mathrm{Def}$ 放大律；压缩 $190\times$ | **已严格**（但不接 $107$） |

## §6 建议（**供唐先生定**）

$$\textbf{A}:\ \text{继续攻"全局整性论证"——但须先有一个候选不等式；我方\ \textbf{暂无}}$$
$$\textbf{B}:\ \text{把现有负结果（机制天花板表 ＋ 缺口定位）归档为定论}✓$$
$$\textbf{C}:\ \text{改换总课题（承认 }107\ \text{重现超出可达范围）}$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "107目标即系数9到6" "单元整性不足以给107" "缺失机制定位"
技术词 107目标即系数9到6    命中文件数=0    ::
技术词 单元整性不足以给107  命中文件数=0    ::
技术词 缺失机制定位        命中文件数=0    ::
```

## §8 边界（硬 ✓）

- **ILP 实测（$r{=}1..5$，$M{=}105/106/107$）＋ 天花板交叉核对** ✓；**不占 C 号** ✓
- **不主张** $107$ 不可达 ✗（V290）；本档系**我方机制之边界陈述**✓

---

## §9 ⚠️ **勘误（2026-09-29 15:2x，自查）—— §1／§2 之"系数 9"陈述作废**

$$\textbf{错误}:\ \text{§1／§2 曾称}\ 107\iff 6E+M\ge1024\ \text{即"把 van Wee 系数 }9\ \text{改到 }6"\ ✗$$
$$\textbf{反证（自查）}:\ \text{若}\ 9E\ \ge\ 2^n-M\ \text{普遍成立，则}\ n{=}7\ \text{给}\ M\ \ge\ 17.53\ >\ 16=K(7,1)\ \ ✗\ \text{矛盾}$$
$$\therefore\ \boxed{9E\ge2^n-M\ \textbf{不普遍成立};\ \text{散点数值吻合（}n{=}10\text{）不等于定理}✗}$$
$$\textbf{正确版}:\ \text{van Wee 1988}\ K(n,1)\ge2^n/n\ \text{仅对\ \textbf{偶}\ }n\ \text{成立}$$
$$n{=}8{:}\ 32=K(8,1)\ \textbf{紧}✓;\quad n{=}6{:}\ 10.67\Rightarrow11<12✓;\quad n{=}10{:}\ 102.4\Rightarrow103✓$$
$$\boxed{\text{故}\ 107\ \text{之机制\ \textbf{不是}\ "系数 }9\to6"\ \text{型改进;}\ \text{正确技术族 ＝ k-tuple covering inequalities}}$$
$$\text{阶梯（精确）}:\ 94\to96\ (\text{Stanton--Kalbfleisch 1968})\to97\ (\text{Cohen--Lobstein--Sloane 1986})\to103\ (\text{van Wee 1988, }\varepsilon\text{-精化})\to105\ (\text{Zhang 1991, \textbf{pair} covering})\to107\ (\text{BÖW 2004, general }R{=}1)$$
$$\therefore\ \textbf{缺口定位修正}:\ \text{缺的不是"全局整性论证"（此说法过泛）}，\text{而是\ \textbf{k-tuple covering 不等式族之 }k\ \text{提升}（\text{pair}\to\text{triple}\to\text{general}}）✓$$
