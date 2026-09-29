# DERIVE-107-e（2026-09-29）—— **owner incidence operator $A$ 与 $G=A^\top A$：四项数据 ＋ 独立性门\ \textbf{通过}**

> **性质**：**纯推导 ＋ 全量实测**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 13:3x ✓
> **唐先生令**：开 1；**不上谱半径/秩**，先做 $G=A^\top A$ 之四项审计 ＋ 独立性门 ✓

**已查地图**：`DERIVE-107-d`（③ 关闭；局部复用上限 $10$）／`DERIVE-107-c`✓

D0: 本档对象 ＝ **档案已有**（$A,G$ 由 $\mu{=}2$ 结构定义——无新数学对象 ✓）
D1: 0（产出＝**四项数据 ＋ 独立性门之判决** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 数据}:\ A\in\{0,1\}^{136\times120};\ \text{rank}(A)=\text{rank}(G)=\mathbf{90};\ \text{nullity}=\mathbf{30}}$$
$$\boxed{\text{② 谱}:\ 30\ \text{个零};\ \text{多重度 }\{18{:}2.0,\ 12{:}3.0,\ 11{:}2{\mp}\sqrt3,\ 5{:}4.0,\ 3{:}0.622,\ \dots\}\ ＋\ 24\ \text{个单重}}$$
$$\boxed{\text{③ 非对角}:\ \textbf{全部}落在距离 }2\ \text{之码字对上};\ \text{取值 }1\ (220\ \text{对})\ \text{或}\ 2\ (26\ \text{对})}$$
$$\boxed{\text{④ ★ 独立性门\ \textbf{通过}}:\ \text{支撑}\ \subsetneq\ \text{距离2对}\ (123/149;\ \textbf{26 对被排除});\ \text{对角}\ne\ \text{距离2度}}$$
$$\boxed{\text{⑤ ✗ 但}:\ G\ \text{不含 }E\ \text{之信息}\ (\text{只涉 }\mu{=}2);\ \text{我未能由其谱/核导出与 }E\ \text{挂钩之不等式}}$$

## §1 ① 构造与秩（**✓**）

$$A_{y,c}=1\iff c\ \text{为 }y\ \text{之 owner};\quad |Y_2|=136,\ M=120;\quad \text{行和}\equiv2✓$$
$$\boxed{\text{rank}(A)=\mathbf{90},\quad \text{rank}(G)=\mathbf{90},\quad \text{nullity}(G)=120-90=\mathbf{30}}$$
$$\text{trace}(G)=272=2|Y_2|✓\quad(\text{与 }\Sigma\lambda\ \text{一致}✓)$$

## §2 ② $G$ 之完整谱（**✓**）

$$\lambda=0\ (\times30)\ \big|\ 2.0\ (\times18)\ \big|\ 3.0\ (\times12)\ \big|\ 2\pm\sqrt3=0.2679/3.7321\ \text{类}\ \big|\ 4.0\ (\times5)$$
$$\textbf{代数值出现}:\ 2\pm\sqrt2\ (0.5858/3.4142),\ 2-\sqrt3\ (1.2679,\times11),\ 3+\sqrt3\ (4.7321,\times11)\ \Longrightarrow \textbf{有结构}✓$$
$$\text{另有 }24\ \text{个单重特征值}\ (0.0334,\dots,8.2749)\ \Longrightarrow\ \text{部分规则、部分"散"}$$

## §3 ③ 非对角元（**✓ 支撑被锁定**）

| $d(c_i,c_j)$ | $G_{ij}$ | 对数 |
|---|---|---|
| $2$ | $1$ | $220$ |
| $2$ | $2$ | $26$ |
| 其它 | $0$ | — |

$$\therefore\ \boxed{\text{supp}(G)\subseteq\{\text{距离 }2\ \text{之码字对}\}}✓\ (\text{几何: owner 对恒距 }2)$$
$$\text{对角}\ (\text{owner degree})\ \text{分布}:\ \{0{:}14,\ 1{:}18,\ 2{:}38,\ 3{:}23,\ 4{:}26,\ 5{:}1\}$$
$$\text{而码字之\ \textbf{距离2度}\ 分布}:\ \{0{:}13,\ 1{:}25,\ 2{:}27,\ 3{:}19,\ 4{:}21,\ 5{:}12,\ 6{:}3\}\ \Longrightarrow\ \textbf{二者不同}✓$$

## §4 ④ 独立性门之判决（**★ 通过**）

$$\text{距离2之码字对}:\ 149;\qquad \text{supp}(G)\ \text{之对数}:\ 123;\qquad \text{被排除者}:\ \mathbf{26}$$
$$\therefore\ \boxed{\text{supp}(G)\ \subsetneq\ \{\text{距离 }2\}\ \Longrightarrow G\ \textbf{不是}\ \text{距离-2 邻接矩阵}}✓\ (\text{且权重非齐一};\ \text{对角}\ne\text{度})$$
$$\therefore\ \text{依你之判据：}G\ \textbf{不完全由"码字距离2关系 ＋ 已有 degree 数据"决定}\ \Longrightarrow\ \textbf{是真独立对象}✓$$
$$\text{（对比}:G'\ \text{若统计\ \textbf{全部}\ 点之 owner 对，则其总和}=\Sigma_x\tbinom{\mu(x)}2=2(N_1{+}N_2)\ \text{属距离分布层}\ ✗\ ——\ \text{故 }G\ \text{之价值在于}\ \textbf{只取 }\mu{=}2\ \text{层}✓）$$

## §5 ⑤ 诚实之缺（**✗**）

$$\text{可算之线性泛函皆为旧账}:\ \text{行和}=\text{owner degree};\ \text{总和}=N_2;\ \Sigma\lambda=\text{trace}=2N_2✓$$
$$\text{而}\ E=\Sigma_x(\mu(x)-1)=n_2+2n_3+3n_4+\cdots\ \textbf{不是}\ G\ \text{之泛函}\ (\text{因 }G\ \text{只涉 }\mu{=}2)$$
$$\Longrightarrow\ \text{欲把 }G\ \text{之谱接到 }E,\ \text{须\ \textbf{分层}}:\ \text{对每个 }k\ \text{构造 }G^{(k)}\ (\mu{=}k\ \text{层之 owner-pair 算子}),\ \text{再由}\ E=\Sigma_k(k{-}1)\cdot|G^{(k)}|\ \text{组装}$$
$$\boxed{\text{本档未做到这一步};\ \text{亦未取出任何}\ \text{(i) 非平凡特征值约束／(ii) 秩-零化约束／(iii) 新 PSD 不等式}}✗$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "owner incidence operator" "G=A^T A谱" "独立性门通过"
技术词 owner incidence operator  命中文件数=0    ::
技术词 G=A^T A谱                  命中文件数=0    ::
技术词 独立性门通过                  命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code 全量实测（$A$、$G$ 谱、非对角分布、支撑对照）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张** $107$ 不可达 ✗（V290）；**未拟合**谱量与 $E$ ✓（遵你令）
