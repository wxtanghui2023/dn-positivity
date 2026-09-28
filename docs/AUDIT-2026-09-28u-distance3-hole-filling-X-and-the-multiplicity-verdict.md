# AUDIT-2026-09-28u — **距离-3 补洞链之 $X$：精确算出，但 $\mathrm{mult}(x)$ **不是** $a(x)$ 之函数 ⟹ 不能压回 $E$**

> **性质**：**实验/审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:50 ✓
> **唐先生令**：推 $G_c$ 之外一层（距离 3 补洞）；**精确算 incidence multiplicity** ✓

**已查地图**：接续 `AUDIT-t`（局部状态 STOP）／C-532·C-533（**中点参数化**）✓

D0: 本档对象 ＝ **档案已有**（$S_c$／triple 补洞／**中点结构**——无新数学对象 ✓）
D1: 0（产出＝**$X$ 精确值 ＋ 一处必要条件修正 ＋ 否定判定** ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{① 唐先生 §1 必要条件\ \textbf{成立}（$0$ 违例）\ \textbf{但须补 }y_{ij}\in C\ \text{项（}220\ \text{例）}}ⓘ}$$
$$\boxed{\text{② ★ }X=\sum_x\delta(x)\,\mathrm{mult}(x)=\mathbf{908}\ \text{（精确）}}$$
$$\boxed{\text{③ ✗ \textbf{但} }\mathrm{mult}(x)\ \textbf{不是 }a(x)\ \text{之函数} \Longrightarrow X\ \textbf{不能}压回 }E\ \text{（唐先生 §10 之希望\ \textbf{落空）}}$$

## §1 §1 必要条件之核验与修正（$120$-code ✓）

$$\text{原式}:\ i,j\notin S_c\Longrightarrow\exists k\notin\{i,j\}:c\oplus e_i\oplus e_j\oplus e_k\in C$$
$$\textbf{实测}:\ \text{含 }y_{ij}\in C\ \text{之修正版\ \textbf{违例数}=0}\ ✓✓;\quad \textbf{但}\ y_{ij}=c\oplus e_i\oplus e_j\in C\ \text{之情形有}\ \mathbf{220}\ \text{例}\ ⚠️$$
$$\therefore\ \text{原式若省略 }[y_{ij}\in C]\ \text{项} \Longrightarrow 220\ \text{个反例}\ ✗;\quad \textbf{正确版}:\ i,j\notin S_c\Rightarrow[y_{ij}\in C]\vee[\exists k:\cdots]\ ✓$$
$$（\text{注}:y_{ij}\in C\iff\{i,j\}\in G_c\ \text{—— 正是唐先生前一档之 }t(c)\ \text{图}\ ✓\text{）}$$

## §2 ★ $X$ 之精确值（**本档主结果 ✓✓**）

$$\mathrm{mult}(x):=\#\{c\in C:\ d(c,x){=}2\ \wedge\ \text{中点}(c,x)\cap C=\varnothing\}\qquad\big(\text{中点}=x\oplus e_i,\ x\oplus e_j\big)$$
$$\boxed{X=\sum_{c\in C}\sum_{\{i,j\}\subseteq S_c^{c}}\delta(y_{ij})\ \overset{\textbf{实测}}{=}\ \sum_x\delta(x)\,\mathrm{mult}(x)=\mathbf{908}}\ ✓$$

$$\mathrm{mult}\ \text{之分布（仅 }\delta\ge1\ \text{之点}）:\ \{0{:}25,\ 1{:}29,\ 2{:}3,\ 3{:}35,\ 4{:}73,\ 5{:}50,\ 6{:}2,\ 7{:}6\}$$

## §3 ★★ 关键判定：$\mathrm{mult}(x)$ **不是** $a(x)$ 之函数（**否定 ✓**）

| $a(x)$ | 实测 $\mathrm{mult}$ 取值集合 |
|---|---|
| $2$ | $\{0,1,2,3,4,5,6,7\}$ |
| $3$ | $\{0,1,2,3,4,5\}$ |
| $4$ | $\{0,2,6\}$ |
| $5$ | $\{4\}$ |

$$\therefore\ \boxed{a(x)\ \text{相同而 }\mathrm{mult}(x)\ \text{可差 }7\ \text{倍} \Longrightarrow \mathrm{mult}\ \textbf{严格细于 }a(x)}$$
$$\Longrightarrow\ X\ \text{不能写成 }F(E)\ \text{或 }F(\{a(x)\})\ \text{之形式} \Longrightarrow \textbf{唐先生 §10 之压缩\ 落空}\ ✗$$

## §4 三本账对照

$$\sum_x\delta(x)\cdot a(x)=E+\textstyle\sum_x\delta^2=\mathbf{796}=4(N_1+N_2)\quad\text{（档案恒等式 ✓）}$$
$$\sum_x\delta(x)\cdot\mathrm{mult}(x)=\mathbf{908}\quad\text{（本档新账）};\qquad \sum_x\delta(x)\cdot\nu_2(x)=\mathbf{1270}\quad(\nu_2=\text{距离 }2\ \text{之码字数})$$
$$\Longrightarrow\ 796\ <\ 908\ <\ 1270\ \text{—— 三本账互不重合};\ \text{但 }X\ \text{无独立上界（}\mathrm{mult}\le\nu_2\ \text{仅给 }X\le1270\text{）}$$

## §5 ⚠️ 与档案之重叠（**必录 ✓**）

$$\mathrm{mult}(x)\ \text{之定义含\ \textbf{中点}(c,x)\cap C=\varnothing} \Longrightarrow \text{此即档案}\ \texttt{C-532}\text{·}\texttt{C-533}\ \text{之\ \textbf{中点参数化} 对象}\ ⚠️$$
$$\text{（}\texttt{C-532}:\ C_{ij}=\{I_i\oplus 1_S:S\in\binom D2\}\ \text{六中点};\ \texttt{C-533}:\ \text{额外 owner 参数化}\ \forall\ \text{全对}）$$
$$\therefore\ \boxed{\text{本档之 }X\ \text{部分退入已归档之\ \textbf{中点结构层}} \Longrightarrow \text{与 }119\text{-线旧档\ \textbf{同层}}\ ⚠️$$

## §6 判定（**照唐先生之判据 ✓**）

$$\text{唐先生}:\ \text{"若 }X\ \text{能压回 }E,\ \text{才有 }E{=}142\ \text{不可能之机会"}\ ✓$$
$$\textbf{实测}:\ \mathrm{mult}\ \text{非 }a(x)\ \text{之函数} \Longrightarrow X\ \textbf{压不回 }E \Longrightarrow \textbf{本层未得新界}\ ✗$$
$$\therefore\ \boxed{\text{未得到 }E\ge153/154;\ \text{本链给出\ \textbf{一本新账（}X{=}908\text{）}而\ \textbf{不闭合}}\ ⚠️}$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "incidence重数" "中点结构重叠" "压缩希望落空"
技术词 incidence重数   命中文件数=0    ::
技术词 中点结构重叠   命中文件数=0    ::
技术词 压缩希望落空   命中文件数=0    ::
```

## §8 边界（硬 ✓）

- 有限核验（$120$ 码全体 $(c,i,j)$）＋ 既有档引证（含中点结构重叠声明）✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**不主张** 119/106 之不可能 ✗（V290）
- §3 之判定**只**针对"$\mathrm{mult}$ 是否为 $a(x)$ 之函数"；**不主张**本链无价值 ⚠️
