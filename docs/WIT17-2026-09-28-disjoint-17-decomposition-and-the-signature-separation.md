# WIT17-2026-09-28 — **C-493：disjoint-17 之精确分解 —— $(k_1,k_2)$ 四格 P₃-only／两格 E-only ✓✓；\textbf{完整 signature 228/229 类纯} ✓✓✓（仅 1 类混合 ✗）；$k_2{=}3\Rightarrow$ 必属 $E_x$ ✓✓**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓✓）**。
> **范围（照唐先生 2026-09-28 14:35 令 ✓）**：C-493 四表（$(k_1,k_2)$／$(k_1,k_2,j)$／完整 signature／17 之判据）；**先跑后写 ✓✓**；**不作路线裁定** ✗。
> **记账纪律（照唐先生之警示 ✓✓）**：**不得**把 C-488 之 $E_x$ 32 点之 $j$-分布与"17 条 disjoint 边"**直接相减** ✗ —— $X\leftrightarrow E(H_1)$ 虽为双射，但须保持 C-490 之对应关系 ✓。

**已查地图：命中（接续 C-492／C-491／C-490，非新案 ✓）**
`docs/WITJOINT-2026-09-28-…`（**joint spectrum／$A_3$ 闭包／$P_3$ 不可判别 ✓✓✗**）｜`docs/WITEDGE-2026-09-28-…`（**边缘级／对易 ✓✓✓**）｜`docs/WITCHOICE-2026-09-28-…`（**两候选／闭环 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓✓**，见 §5）
D0: 本档对象 ＝ **档案已有** $e_x$／$T_x$／$\lambda$；**新对象**：交叉型 $(k_1,k_2)$ ＋ 完整 signature（首次入档 ✓）
D1: 1（**首次给出 disjoint-17 之 $(k_1,k_2)$ 精确分布（含 4 格 P₃-only／2 格 E-only）＋ 首次给出 $(k_1,k_2,j)$ 之 9/13 纯判别格 ＋ 首次给出\ \textbf{完整 signature 之 228/229 纯类}（仅 1 类混合）** ✓）
**[RESEARCH]**

---

## §0 结论（**17 之分解基本完成 ✓✓✓，余一类模糊 ✗**）

$$\textbf{设定 ✓}:\ x\in\mathcal S;\ e_x{=}\{p,q\}\ (\text{其 }H_1\text{-边});\ T_x{=}\{p,q,c\},\ c{=}w(e_x);\ y\in\mathcal S,\ y\ne x;\ e_y{=}\{u,v\};\ z{=}w(e_y)✓$$
$$\qquad\text{只取\ \textbf{不相交}边（}e_x\cap e_y{=}\varnothing\big)✓\ \big(\text{与 }e_x\ \text{相交之 }1{+}14{=}\mathbf{15}\ \text{条已全在 }E_x✓\big)⟹\ \text{余 }145\ \text{条}\ =P_3(128)+E_{\rm disj}(\mathbf{17})✓✓$$
$$\qquad\Longrightarrow\ \boxed{32=\underbrace{15}_{e_y\cap e_x\ne\varnothing}+\underbrace{17}_{e_y\cap e_x=\varnothing,\ y\notin P_3(x)}}\ ✓✓\ \big(\text{＝唐先生之精确重写 ✓✓}\big)$$
$$\boxed{\textbf{(1) ✓✓(k_1,k_2) 分布（}k_i:=\#\{(a,b)\in e_x\times e_y:R(a,b)=i\}✓\big)}$$
| $(k_1,k_2)$ | $P_3$ | $E_{\rm disj}$ | 判定 |
|---|---|---|---|
| $(0,0)$ | $4320$ | $160$ | 混合 ✗ |
| $(0,1)$ | $2560$ | $640$ | 混合 ✗ |
| $(0,2)$ | $1600$ | $320$ | 混合 ✗ |
| $(0,3)$ | $\mathbf0$ | $640$ | ★**E-only** ✓✓ |
| $(1,0)$ | $3200$ | $\mathbf0$ | ★**P₃-only** ✓✓ |
| $(1,1)$ | $4480$ | $\mathbf0$ | ★**P₃-only** ✓✓ |
| $(1,2)$ | $1600$ | $320$ | 混合 ✗ |
| $(1,3)$ | $\mathbf0$ | $640$ | ★**E-only** ✓✓ |
| $(2,0)$ | $2080$ | $\mathbf0$ | ★**P₃-only** ✓✓ |
| $(2,1)$ | $640$ | $\mathbf0$ | ★**P₃-only** ✓✓ |
$$\qquad\Longrightarrow\ \boxed{k_2{=}3\ \Longrightarrow\ \text{必属 }E_x}\ ✓✓\ \big(\text{两格全 E，无例外 ✓✓}\big);\quad \boxed{k_1{\ge}1\ \wedge\ k_2{=}0\ \Longrightarrow\ \text{必属 }P_3}\ ✓✓$$
$$\qquad\textbf{（计数校验 ✓）}:\ E_{\rm disj}\ \text{总计}=160+640+320+640+320+640=2720=160\times\mathbf{17}✓✓$$
$$\boxed{\textbf{(2) ✓✓(k_1,k_2,j) 分布（}j{=}|T_y\cap T_x|✓\big):\ 13 格中\ \mathbf9\ \text{格纯判别}}✓✓$$
| $(k_1,k_2,j)$ | $P_3$ | $E$ | |
|---|---|---|---|
| $(0,0,0)$ | $4320$ | $160$ | 混合 ✗ |
| $(0,1,0)$ | $2560$ | $640$ | 混合 ✗ |
| $(0,2,0)$ | $1280$ | $\mathbf0$ | ★P₃-only ✓ |
| $(0,2,1)$ | $320$ | $320$ | 混合 ✗ |
| $(0,3,1)$ | $\mathbf0$ | $640$ | ★E-only ✓✓ |
| $(1,0,0)$ | $3200$ | $\mathbf0$ | ★P₃-only ✓✓ |
| $(1,1,0)$ | $4480$ | $\mathbf0$ | ★P₃-only ✓✓ |
| $(1,2,0)$ | $1280$ | $\mathbf0$ | ★P₃-only ✓ |
| $(1,2,1)$ | $320$ | $320$ | 混合 ✗ |
| $(1,3,1)$ | $\mathbf0$ | $640$ | ★E-only ✓✓ |
| $(2,0,0)$ | $1920$ | $\mathbf0$ | ★P₃-only ✓✓ |
| $(2,0,1)$ | $160$ | $\mathbf0$ | ★P₃-only ✓ |
| $(2,1,0)$ | $640$ | $\mathbf0$ | ★P₃-only ✓✓ |
$$\qquad\Longrightarrow\ \boxed{\text{9 格纯、4 格混合}}✓✓;\ \ j{=}2,3\ \text{出现于 }E\ \text{之样本中 ✓（而 }P_3\ \text{仅 }j\le1✓\big)$$
$$\boxed{\textbf{(3) ✓✓✓完整 signature（照唐先生 §第三刀）}:\ }\Sigma=\big(R(p,u),R(p,v),R(q,u),R(q,v);R(c,u),R(c,v);R(z,p),R(z,q);R(c,z)\big)✓$$
$$\qquad\Longrightarrow\ \textbf{种类 }\mathbf{229};\ \textbf{纯类 }\mathbf{228};\ \textbf{混合仅 }\mathbf1\ ✗✗\ \big(\text{即}\ 228/229=99.6\%\ \text{分离 ✓✓✓}\big)$$
$$\qquad\textbf{（唯一混合类 ✓）}:\ \Sigma_0=(0,0,0,0;\ 2,2;\ 2,2;\ 0)\ \text{含 }E{=}160\ \text{与}\ P_3{=}480✓\ \text{——\ 即 }160\ \text{个 }x\ \text{各贡献 3 个实例 ✓}$$
$$\qquad\Longrightarrow\ \text{结构解释}:\ \Sigma_0\ \text{表示 }c\ \text{与 }u,v\ \text{皆 }H_2\text{-邻（}R(c,u){=}R(c,v){=}2✓\big)\ \text{且 }z\ \text{与 }p,q\ \text{皆 }H_2\text{-邻（}2,2✓\big)\ \text{而 }c,z\ \text{不相邻（}R(c,z){=}0✓\big)$$
$$\qquad\qquad\text{且 }e_x\times e_y\ \text{四交叉对全为 }H_0\ ✓\ \text{——\ 此构型\ \textbf{同时出现于 }P_3\ \text{与 }E\ ✗\ \big(\text{唯一模糊处 ✓}\big)}$$
$$\boxed{\textbf{(4) ✓✓E_{\rm disj} 之 (k_1,k_2) 全貌（17 之分解）}:\ }(0,0){:}1,\ (0,1){:}4,\ (0,2){:}2,\ (0,3){:}4,\ (1,2){:}2,\ (1,3){:}4\ ✓\ \big(\text{每 }x\ \text{之 17 条 ✓}\big)$$
$$\qquad\Longrightarrow\ \boxed{17=1+4+2+4+2+4}\ ✓✓\ \text{——\ 17 已\ \textbf{完全拆成 6 个局部型}}✓✓\ \big(\text{唐先生之目标达成大半 ✓}\big)$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §"32=15+17"\ 之精确重写\ \textbf{完全正确}}✓✓✓\ \text{——\ 本档证实且 }17\ \text{之 }(k_1,k_2)\ \text{分解为 }1{+}4{+}2{+}4{+}2{+}4✓✓$$
$$\textbf{✓✓✓}:\ \text{其 §第一刀之\ \textbf{警示}（不得把 }E_x\ \text{之 32 点 }j\text{-分布与 17 边直接相减）\ \textbf{正确}}✓✓✓\ \text{——\ 本档严守 ✓；且实测自洽（}E_{\rm disj}=2720/160=17✓\big)$$
$$\textbf{✓✓✓}:\ \text{其 §第二刀（四交叉对 }(R(p,u),R(p,v),R(q,u),R(q,v))\big)\ \textbf{命中要害}}✓✓✓\ \text{——\ 单独即已给 4 格 P₃-only／2 格 E-only ✓✓$$
$$\textbf{✓✓✓}:\ \text{其 §第三刀（完整 signature 加 }c,z\big)⟹\ \textbf{228/229 分离}}✓✓✓\ \text{——\ 其"若完全分离即得有限局部判据"\ ⟹\ \textbf{几乎达成}（仅 1 类模糊 ✗）$$
$$\textbf{✓✓}:\ \text{其 §第四刀（}k_2 优先）\ \textbf{正确}}✓✓\ \text{——\ 实测 }k_2{=}3\ \text{即 E-only ✓✓（最干净的判据 ✓）$$
$$\textbf{✓✓}:\ \text{其 §第五刀（}j{=}2,3\ \text{为强排除信号）\ \textbf{成立}}✓✓\ \text{——\ }P_3\ \text{中 }j\le1✓\ \text{（}123{+}5✓\big);\ E\ \text{含 }j{=}2,3✓$$
$$\textbf{✗（余一格）}:\ \text{唯一混合 signature }\Sigma_0\ \text{表明：单凭 }H_0/H_1/H_2\ \text{之九元关系\ \textbf{不足以完全分离}}✗\ \text{——\ 须再加一量（疑为\ \textbf{距离-2 球三重交}／环境 }Q_{10}\ \text{量 ✓）}$$

## §2 常数汇总裁（**本档 ✓✓✓**）

| 量 | 值 |
|---|---|
| $E_x$ 之分解 | $32=15+17$ ✓✓ |
| $E_{\rm disj}$ 之 $(k_1,k_2)$ 型 | $1,4,2,4,2,4$（合 17）✓✓ |
| P₃-only 之 $(k_1,k_2)$ | $(1,0),(1,1),(2,0),(2,1)$ ✓✓ |
| E-only 之 $(k_1,k_2)$ | $(0,3),(1,3)$ ✓✓ |
| 完整 signature | 229 类，**228 纯** ✓✓✓ |
| 唯一混合类 $\Sigma_0$ | $E{:}160,\ P_3{:}480$ ✗ |

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓ 最优先）}:\ \text{拆 }E_{\rm disj}\ \text{之 6 型（}1{+}4{+}2{+}4{+}2{+}4\big):\ \text{其与 }x\ \text{之\ \textbf{几何关系}（}d(x,y)\ \text{／}T_y\ \text{之 owner 位置 ✓）是否给出更细型 ✓？}$$
$$\textbf{（靶 2 ✓✓）}:\ \text{唯一混合类 }\Sigma_0\ \text{之细分：加\ \textbf{距离-2 球三重交}（}|N_2(x)\cap N_2(p)\cap N_2(q)|✓\big)\ \text{或}\ \mathrm{Aut}\ \text{轨道 ✓}$$
$$\textbf{（靶 3 ✓）}:\ \text{若 17 之型全部确定 ⟹ 目标升级为 }128=145-17\ \text{之\ \textbf{P1 结构定理}}✓✓$$
$$\textbf{（并行 ⚠️）}:\ r{=}3\ \text{profile}✗;\ \text{非 Best 39-码}✗$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "交叉型" "边签名" "禁配判据" "判别表"
技术词 交叉型   命中文件数=1    :: ./E183-T2a-verdict-projection-rigidity.md
技术词 边签名   命中文件数=0    ::
技术词 禁配判据 命中文件数=0    ::
技术词 判别表   命中文件数=1    :: ./p28b2c-schur.md
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 交叉型 | 0 | **1**（`E183-*` 属**空间 A（RH 线，E-编号）** ⟹ 不计 ✗✓） | ✓（本线新增 ✓） |
| 边签名 | 0 | 0 | ✓（照唐先生 §第三刀 ✓） |
| 禁配判据 | 0 | 0 | ✓（自造标签 ✓） |
| 判别表 | 0 | **1**（`p28b2c-*` 属**空间 A** ⟹ 不计 ✗✓） | ✓（自造标签 ✓） |

- **（本条\ \textbf{确已先跑后写} ✓✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（160 实例 × 145 disjoint 边 ＋ 229 类 signature 全量 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项精确重写（$32{=}15{+}17$ ✓✓✓）** ＋ **一项近乎完全分离（228/229 ✓✓✓）** ＋ **一项余留模糊（$\Sigma_0$ ✗）** 已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** 17 已完全刻画 ✗（余 1 类 ⚠️）；**不声称** P1 成立/不成立 ✗（V290）
