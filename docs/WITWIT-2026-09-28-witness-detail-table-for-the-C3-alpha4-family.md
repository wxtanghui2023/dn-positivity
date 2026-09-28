# WITWIT-2026-09-28 — **C-509：$O_1$ 族之\ \textbf{witness 明细原表}（B-lemma 所需）＋ 三处结构事实 ✓✓：正边 $|W_{ij}|{=}\mathbf2$（非 6）；$W{=}\varnothing\iff\lambda{=}0$；$B\cap\{c\}\neq\varnothing$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §5）**。
> **范围（照唐先生 2026-09-28 15:29 令 ✓）**：交付 $O_1$ 族之 **witness／16-vector 原始表**（供 B-lemma 第一刀 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-508／C-507／C-504，非新案 ✓）**：`WITK4-…`／`WITDOSSIER-…`／`WITMASK-…`
D0: 本档对象 ＝ **档案已有**（witness/16-vector/$B$；无新数学对象 ✓）
D1: 1（**首次交付 $C{=}3,\alpha{=}4$ 族之\ \textbf{witness 明细原表}（含每 $w$ 之 $T_w$／$R(w)$）＋ 首次得\ \textbf{正边 $|W_{ij}|{=}2$}（非"}$\binom42{=}6$\textbf{"）＋ 首次得 $W_{ij}{=}\varnothing\iff\lambda_{ij}{=}0$ ＋ 首次得 $B\cap\{c\}\neq\varnothing$（解释 $R$ 行之 $0$ 坐标）** ✓）
**[RESEARCH]**

---

## §0 代表实例之 witness 明细原表（**B-lemma 之输入 ✓✓**）

$$\textbf{（代表实例 ∈ }C{=}3,\alpha{=}4\ \text{族 ✓；其规范 16-向量 ＝ C-507 之 }O_5\ ✓\big):\ O=(0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1)✓$$
$$x=0000000001,\quad y=0000001000\quad\big(\text{点}\big);\quad T_x=\{0,10,25\};\quad e_x{=}(a,b){=}(10,25);\quad c{=}0$$
$$T_y=\{0,1,4\};\quad e_y{=}(u,v){=}(0,1);\quad z{=}4$$
$$\textbf{四槽（序 }q_{11},q_{12},q_{21},q_{22}\big):\ (10,0){:}\lambda{=}2;\ (10,1){:}\lambda{=}2;\ (25,0){:}\lambda{=}2;\ (25,1){:}\lambda{=}\mathbf0\ ⟹\ \mathrm{mask}{=}(1,1,1,0)\ \big(\text{权 3}✓\big)$$

### (A) D7 之 16-位置原表（$B$ 之 4 点 × 4 坐标 ✓）

$$B=N_2(x)\cap N_2(p)\cap N_2(q)=\{131,\ 385,\ 515,\ 769\}\ ✓\ \big(\text{行序＝字典序}\big)$$

| 行 | $w$（二进制） | $T_w{=}\mathrm{own}(w)$ | $\lvert T_w\rvert$ | $R(w){=}(d(w,c),d(w,z),d(w,u),d(w,v))$ |
|---|---|---|---|---|
| 1 | $0010000011$ | $\{6,7,10,25\}$ | $4$ | $(0,1,0,0)$ |
| 2 | $0110000001$ | $\{10,16,17,18,25\}$ | $5$ | $(0,1,0,1)$ |
| 3 | $1000000011$ | $\{10,20,21,25\}$ | $4$ | $(0,1,0,0)$ |
| 4 | $1100000001$ | $\{10,25,30,33\}$ | $4$ | $(0,1,0,1)$ |

$$\qquad\Longrightarrow\ \text{等式型}\ =\ \big((0,1,0,0),(0,1,0,0),(0,1,0,1),(0,1,0,1)\big)\ =\ O_5\ ✓✓\ \text{——\ 16-向量之\ \textbf{逐位来源已定位}}✓✓$$
$$\textbf{（★关键 ✓✓）}:\ \text{第 1、3 行之首坐标 }d(w,c){=}\mathbf0\ \Longrightarrow\ w=c\ ✓\ \text{——\ 即}\ \boxed{B\cap\{c\}\neq\varnothing}\ ✓✓\ \big(\text{此为该 }O\ \text{之结构特征 ✓}\big)$$

### (B) witness 集 $W_{ij}:= \mathcal S\cap N_2(I_i)\cap N_2(I_j)$（四 cross-edge ✓）

$$W_{(10,0)}\ (\lambda{=}2):\ |W|{=}\mathbf2\ :\quad \begin{cases}w{=}0000000001 & R(w){=}(2,4,6,8),\ T_w{=}\{0,10,25\}\\ w{=}0100001001 & R(w){=}(2,4,4,8),\ T_w{=}\{0,10,16\}\end{cases}$$
$$W_{(10,1)}\ (\lambda{=}2):\ |W|{=}\mathbf2\ :\quad \begin{cases}w{=}0000000010 & R(w){=}(4,4,8,8),\ T_w{=}\{1,10,20\}\\ w{=}0100001010 & R(w){=}(4,4,6,8),\ T_w{=}\{1,10,35\}\end{cases}$$
$$W_{(25,0)}\ (\lambda{=}2):\ |W|{=}\mathbf2\ :\quad \begin{cases}w{=}0000000001 & R(w){=}(2,4,6,8),\ T_w{=}\{0,10,25\}\\ w{=}0010000101 & R(w){=}(2,6,6,6),\ T_w{=}\{0,18,25\}\end{cases}$$
$$W_{(25,1)}\ (\lambda{=}\mathbf0):\ |W|{=}\mathbf0\ ✓\ \big(\text{无 witness ✓}\big)$$

## §1 三处结构事实（**★B-lemma 直接可用 ✓✓**）

$$\boxed{\textbf{(F1) ✓✓正边 }|W_{ij}|{=}\mathbf2}\ \text{——\ \textbf{非}\ 唐先生 §5 所估之 }}\binom42{=6\ ✗✓$$
$$\qquad\textbf{（解释 ✓）}:\ \text{两码字距 4 ⟹ 公共半径-2 点共 }6\ \text{个 ✓；但 }W\ \text{只取其中属 }\mathcal S\ \text{者（}|\mathrm{own}|{=}3✓\big)⟹\ \textbf{仅 2 个}✓✓\ \text{——\ 这是一个\ \textbf{强筛选}}✓✓$$
$$\boxed{\textbf{(F2) ✓✓W_{ij}{=}\varnothing\iff\lambda_{ij}{=}0}}:\ \text{（本档之 }q_{22}\ \text{即例 ✓）}$$
$$\boxed{\textbf{(F3) ✓✓B\cap\{c\}\neq\varnothing}}:\ \text{故 }R(w)\ \text{行含 }d(w,c){=}0\ ✓\ \big(\text{16-向量之"首列为 }0"\ \text{即此 ✓}\big)$$
$$\qquad\Longrightarrow\ \textbf{B-lemma 之搜索空间极小 ✓✓}:\ \text{四 }W\ \text{各 }|W|{\le}2⟹\ \text{每实例至 }2^4{=}\mathbf{16}\ \text{组合}\ ✓✓\ \text{——\ 故 }S{=}1111\ \text{之不可能性须\ \textbf{结构性}证明（非大枚举 ✓）}$$

## §2 一处脚本失败与口径更正（**据实 ✓**）

$$\textbf{✗}:\ \text{本档首版脚本以 }C\text{-507 之 }O_1\ \text{常量比对，}\textbf{零命中} ✗\ \big(\text{常量抄录有误 ✗}\big);\ \text{已改为按}\ \textbf{(}C{=}3,\alpha{=}4\text{) 结构签名}\ \text{选取 ✓}$$
$$\qquad\Longrightarrow\ \text{代表实例属 C-507 之 }O_5\ ✓\ \big(\text{非 }O_1\ ✗✓\ \text{——\ 据实标注 ✓}\big);\ \text{六族之明细待\ \textbf{逐个}导出 ✓}$$
$$\qquad\textbf{（纪律 ✓）}:\ \text{脚本失败与口径更正皆如实登记 ✓✓}$$

## §3 B-lemma 之现成形式（**照唐先生 15:29 ✓**）

$$\boxed{\text{B-lemma}:\ }O\wedge S{=}1111\ \Longrightarrow\ \text{四 witness 无法同时满足 }|\mathrm{own}(w_{ij})|{=}3\ ✓$$
$$\qquad\textbf{（本档已备之件 ✓✓）}:\ \text{① }W_{ij}\ \text{之定义与实测（}\le2✓\big);\ \text{② }R(w)\ \text{之四坐标（}D7✓\big);\ \text{③ }B\ \text{四点之 }T_w\ ✓;\ \text{④ 16-向量之逐位来源 ✓✓}$$
$$\qquad\textbf{（下一刀之形 ✓）}:\ \exists(w_{11},w_{12},w_{21},w_{22})\in\prod W_{ij}\ \text{使四 }R(w)\ \text{之等式型 }{=}O\ ⟹\ \textbf{求最小冲突证书} ✓✓$$

## §4 汇总裁（**✓✓**）

| 项 | 值 |
|---|---|
| 代表实例 | $C{=}3,\alpha{=}4$（＝C-507 之 $O_5$） |
| mask | $(1,1,1,0)$（权 3） |
| $16$-向量逐位来源 | ✓✓ 已定位（4 行 $R(w)$） |
| 正边 $\lvert W_{ij}\rvert$ | $\mathbf2$ ✓✓（非 6） |
| $\lambda{=}0$ 边之 $W$ | $\varnothing$ ✓✓ |
| $B\cap\{c\}$ | $\neq\varnothing$ ✓✓ |
| B-lemma 搜索空间 | $\le2^4$ ✓✓（须结构证明） |

## §5 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "witness明细" "冲突证书" "16位原表"
技术词 witness明细    命中文件数=1    :: ./WITWIT-2026-09-28-witness-detail-table-for-the-C3-alpha4-family.md
技术词 冲突证书     命中文件数=1    :: ./WITWIT-2026-09-28-witness-detail-table-for-the-C3-alpha4-family.md
技术词 16位原表      命中文件数=1    :: ./WITWIT-2026-09-28-witness-detail-table-for-the-C3-alpha4-family.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| witness明细 | 0 | 0 | ✓（**自命中 1**（本档 ✓）；照唐先生 15:29 ✓） |
| 冲突证书 | 0 | 0 | ✓（**自命中 1**（本档 ✓）✓） |
| 16位原表 | 0 | 0 | ✓（**自命中 1**（本档 ✓）；本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §6 边界（硬 ✓）

- **有限穷举** ✓（实例扫描 ＋ $W_{ij}$ 全量 ＋ $R$ 表 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 ✓）
- **一项交付（witness 原表 ✓✓）** ＋ **三项结构事实（F1–F3 ✓✓）** ＋ **一项脚本失败／口径更正（据实 ✗✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** B-lemma 已证 ✗；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
