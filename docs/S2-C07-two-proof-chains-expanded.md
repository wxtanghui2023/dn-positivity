已查地图：命中（`S2-C07-modern-closure-check-19-9-20-9` ＋ `AMEND-19`）⟹ 两条证明链展开，不开新案
D0: 本档对象 = **`t_2[19,9]` 与 `t_2[20,9]` 的完整证明链**（`P0`–`P5` 逐层状态）＋ **决定性归约到 length function** ＋ **可攻击缺口定位**
D1: 1（首次把 `C07` 两格写成证明链；产出决定性归约与障碍入口）
[RESEARCH]

# **`C07`：两条证明链展开**

## §0 统一框架（照 `AMEND-19`）

```
$$\text{链条}:\ \text{Definition}\to\text{Lower Bound}\to\text{Existence}\to\text{Optimality}\to\text{Classification}$$ ✓
$$\text{核心等价（`parity-check` 形式）}:\ R(C)\le R\iff \forall s\in\mathbb F_2^{\,n-k},\ \exists I,\ |I|\le R,\ s=\textstyle\sum_{i\in I}h_i$$ ✓✓
$$\text{亦即}:\ \mathbb F_2^{\,r}=\bigcup_{j\le R}\{h_{i_1}+\dots+h_{i_j}\}\ (\text{子集和},\ \text{不重复})$ ✓
$$\text{几何等价（术语待核）}:\ \text{列点集在 }\mathrm{PG}(r-1,2)\ \text{中满足"每点落在}\le R\ \text{个给定点的张成内"}$$ ⚠️
```

## §1 链 A：`t_2[19,9]`（`r=n-k=10`）

```
$$\textbf{历史锚}:\ 3\le t_2[19,9]\le4\ (\text{CKMS-1985 原表"3-4"})$$ ✓
$$P0\ \text{定义}:\ \boxed{\text{CLOSED}}\ ——\ \mathcal C=\{C\le\mathbb F_2^{19}:\dim C=9\};\ \text{目标量 }R(C);\ \textbf{值不需要等价关系（分类才需要）}$$ ✓
$$P1\ \text{下界}(\ge3):\ \boxed{\text{CLOSED}}\ ——\ \text{球覆盖界}:\ \sum_{i\le2}\binom{19}{i}=1{+}19{+}171=191<2^{10}=1024\ \Longrightarrow\ R\ge3$$ ✓✓
$$P1'\ \text{下界}(\ge4)\ \textbf{＝排除 }R{=}3:\ \boxed{\textbf{OPEN（真缺口）}}$$
$$\qquad \text{等价}:\ \nexists\ H\in\mathbb F_2^{10\times19}\ \text{with}\ \mathbb F_2^{10}=\{0\}\cup H\cup(H{+}H)\cup(H{+}H{+}H)$$
$$\qquad \textbf{计数张力}:\ \#\{\text{子集}\le3\}=1+19+171+969=\boxed{1160}\ \text{vs}\ \boxed{1024}\ \text{个 syndrome}\ \Longrightarrow\ \textbf{仅 136 松弛}$$ ✓✓✓
$$\qquad \Longrightarrow\ \text{若要 }R\le3,\ \text{则 1160 个子集和必须\textbf{几乎无碰撞}地铺满}1024\ \text{个 syndrome} \Longrightarrow \textbf{强碰撞约束＝障碍入口}$$ ✓✓✓
$$P2\ \text{上界}(\le4):\ \boxed{\text{CLOSED-ish}}\ ——\ \text{1991 表既有上界 4};\ \text{机制疑为 }GD\ \text{型水平延拓}:\ t[17,9]=3\ (\text{1985 表 exact})\Rightarrow t[19,9]\le4$$ ⚠️（**机制须核**）
$$P3\ \text{相撞}:\ \boxed{\textbf{未闭合}};\ \text{两端为 }3\ \text{与}\le4 \Longrightarrow\ \text{真命题二选一}:\ \boxed{t_2[19,9]=3}\ \text{或}\ \boxed{t_2[19,9]=4}$$ ✓✓
$$P4/P5:\ \text{达到者分类／非同构 census}\ ——\ \text{现阶段不进入}$$ ✓
```

## §2 链 B：`t_2[20,9]`（`r=n-k=11`）

```
$$\textbf{历史锚}:\ 4\le t_2[20,9]\le5\ (\text{CKMS-1985 原表"4-5"})$$ ✓
$$P0:\ \boxed{\text{CLOSED}}$$ ✓
$$P1\ \text{下界}(\ge4):\ \boxed{\text{CLOSED}}\ ——\ \text{球覆盖界}:\ \sum_{i\le3}\binom{20}{i}=1{+}20{+}190{+}1140=1351<2^{11}=2048\ \Longrightarrow\ R\ge4$$ ✓✓
$$P1'\ \text{下界}(\ge5)\ \textbf{＝排除 }R{=}4:\ \boxed{\textbf{OPEN}};\ \textbf{但计数无张力}:\ \#\{\text{子集}\le4\}=6196\gg2048\ \Longrightarrow\ \textbf{须结构性障碍（van Wee／对偶／线性约束）而非计数}$$ ✓✓
$$P2\ \text{上界}(\le5):\ \boxed{\text{CLOSED-ish}}\ (\text{1985 表上界 5})$$ ⚠️
$$P3:\ \boxed{\textbf{未闭合}};\quad \boxed{t_2[20,9]=4}\ \text{或}\ \boxed{t_2[20,9]=5}$$ ✓
```

## §3 ⭐ 决定性归约（本轮最重要的产出）

```
$$t_2[n,k]\le R\iff \ell_2(n-k,R)\le n\qquad(\ell_2(r,R):=\text{最小长度，二元线性、协维 }r\text{、覆盖半径 }R)$$ ✓✓（\text{常规约定；零列/无零列约定须核}）$$
$$\Longrightarrow\ \boxed{t_2[19,9]=3\iff \ell_2(10,3)\le19};\qquad \boxed{t_2[20,9]=4\iff \ell_2(11,4)\le20}$$ ✓✓✓
$$\textbf{含义}:\ \text{两格的生死各由}\ \textbf{一个整数}（\ell_2(10,3),\ \ell_2(11,4)\ \text{与门槛 }19,20\ \text{的比较）决定}$$
$$\Longrightarrow\ \textbf{现代闭合点检的精确形式}:\ \text{查 length-function 表是否已给出 }\ell_2(10,3),\ \ell_2(11,4)$$
$$\qquad \text{来源}:\ \text{Brualdi–Pless 1990 表};\ \text{Brualdi–Pless–Wilson 1989};\ \text{《Covering Codes》(1997)};\ \text{Davydov–Östergård 等 length-function 论文}$$ ✓✓
$$\text{若表给 }\ell_2(10,3)\le19 \Rightarrow t=3\ \text{（DROP 该格）};\ \ell_2(10,3)\ge20 \Rightarrow t=4\ \text{（DROP）};\ \text{未定型 }bound \Rightarrow \text{保留 frontier}$$ ✓✓
```

## §4 可攻击缺口（若 `(甲1)` 闭合点检仍为空）

```
$$\textbf{链 A 的障碍入口（唯一有数学内容的入口）}:\ \text{证明\ \textbf{任意 }19\ \text{列}\ H\subseteq\mathbb F_2^{10}\ \text{必有}}\ \#\{0\}\cup H\cup2H\cup3H\le1023$$
$$\qquad \text{其中 }2H=\{h_i{+}h_j\},\ 3H=\{h_i{+}h_j{+}h_\ell\};\ \text{松弛仅 136}\ \Longrightarrow\ \text{碰撞数 }\ge137\ \text{必须结构性地不可避免}$$ ✓✓✓
$$\textbf{已知工具（档级）}:\ \text{加性组合在 }\mathbb F_2^{r}\ \text{的三元和集界};\ \text{van Wee 下界};\ \text{偶权重/线性约束};\ \text{球覆盖的精细版}$$ ⚠️
$$\textbf{链 B 的障碍入口}:\ \text{计数失效} \Longrightarrow \text{必须用线性结构约束（如对偶距离、van Wee 型不等式）排除 }R{=}4$$ ✓
$$\Longrightarrow\ \boxed{\text{两链均有"具体数学对象"级入口} \Longrightarrow \text{按 }AMEND\text{-}19\ \text{可进入攻击}}$$ ✓✓
```
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §1/§2 的 `P2` 机制与 §3 的约定（零列）为**待核**；§1 的 1160/1024 为**实算算术**（可信）✓

## §附 【技术词回查】（补录）
```
技术词 proof chain      命中文件数=1    :: ./E14-bom03-variational-check.md 
技术词 saturating       命中文件数=12   :: ./TARGET-L9-source-fetch-report.md ./A5-CORRECTION-17-is-reduced-reps-not-orbits.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md 
```
