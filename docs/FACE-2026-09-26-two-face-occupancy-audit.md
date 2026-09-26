已查地图：已跑 scripts/prework_map_check.sh K(10,1) 2-face square occupancy ⟹ **命中既有三档**：`EXCESS-2026-09-25`（面数 11520 ＋ m-面计数界，**已 CLOSED 为过弱** ✗）、`BUDGET-2026-09-26`（子立方预算引理 `Q_k⊆C ⟹ E≥k·2^k` ✓，**包含**本文 §2 的 q_F=4 情形 ✓）、`MIDSUP-2026-09-26`（字面正方形，**已自证否** ✗）⟹ 本档为**新增小部分＋判定**（唐先生 2026-09-26 21:35 稿 ✓）；未跑 solver ✓。
D0: 本档对象 = 2-面占据数 $q_F$ 与码字对-面多重度（既有对象之细化）
D1: 1（新增：**码字对-面多重度拆分 9 vs 1** ✓✓；**$q_F\le2$（分支 A）与恰 3 个例外面（分支 B）** ✓）

# FACE-2026-09-26 · 2-面占据审计

## §0 结论（先给）

```
$$\boxed{\textbf{(U-1 新)}\ \text{码字对-面多重度\textbf{依赖距离}:\ }d(c,c')=1\ \text{共}\ \mathbf 9\ \text{面};\ d(c,c')=2\ \text{共}\ \mathbf 1\ \text{面}\ ✓✓\ \text{（此前只用 }A_1+A_2\ \text{时未使用）}}$$
$$\boxed{\textbf{(U-2 新)}\ q_F\ \text{定理}:\ \text{分支 A}\ q_F\le\mathbf 2\ \forall F\ ✓;\ \text{分支 B}\ \text{恰}\ \mathbf 3\ \text{面有}\ q_F=3\ ✓;\ q_F=4\ \text{不可能}\ ✓}$$
$$\boxed{\textbf{(U-3 否)}\ \text{但全局量仍\textbf{逐项由 }A_1\ \text{决定}} \Longrightarrow \textbf{无 collision}\ ✗\ \text{（第 12 次同向汇合 ⚠️）}$$
$$\boxed{\textbf{(U-4 更正)}\ \#\{\text{2-面}\}=\mathbf{11520}\ ✓\ \text{（唐稿 46080 是\textbf{点-面关联数} ✗；档案 }\texttt{EXCESS}\ \text{早已记下 11520 ✓）}$$
$$
$$
```

---

## §1 (U-1) 多重度拆分（本档核心新增 ✓）

```
$$\text{2-面 }F(v;i,j)=\{v,\ v{+}e_i,\ v{+}e_j,\ v{+}e_i{+}e_j\}\ ✓;\ \text{含码字 }c\ \text{的面数}=C(10,2)=45\ ✓\Longrightarrow\#\text{码字-面关联}=119\cdot45=5355\ ✓$$
$$\textbf{含给定对的公共面数}:\ d(c,c')=1\ (c'=c{+}e_i):\ F(c;i,j)\ni c,c'\ \forall j\ne i\ \Longrightarrow\ \mathbf 9\ \text{面}\ ✓✓$$
$$\qquad d(c,c')=2\ (c'=c{+}e_i{+}e_j):\ \text{二者在该面内为\textbf{对角}，面被唯一确定}\ \Longrightarrow\ \mathbf 1\ \text{面}\ ✓✓$$
$$\Longrightarrow\ \sum_F\binom{q_F}{2}=9A_1+A_2\ ✓✓\ \text{（＝}8A_1+143\ \text{因 }A_1{+}A_2=143\ ⚠️\ \text{—— 故仍由 }A_1\ \text{决定}\ ✗）$$
$$
$$
```

---

## §2 (U-2) $q_F$ 定理（含分支 B 的例外面 ✓）

```
$$\textbf{引理}:\ \text{面内 3 个角（L 形）中，"中间"角与另两角均距 1}\ \Longrightarrow\ b(\text{中间角})\ge1+2=3\ ✓$$
$$\qquad\text{由 }Q=1\ (\text{唯一 }b\ge3\ \text{点为 }z)\ \Longrightarrow\ \text{中间角}=z\ ✓$$
$$\Longrightarrow\ \textbf{分支 A}\ (z\notin C):\ \text{任何 }q_F\ge3\ \text{都要求某角}=z\ \text{为码字}\ \Longrightarrow\ \textbf{不可能}\ \Longrightarrow\ \boxed{q_F\le2\ \forall F}\ ✓✓$$
$$\qquad\textbf{分支 B}\ (z\in C):\ q_F=3\ \text{仅当中间角}=z\ ⟹\ \text{该面由 }z\ \text{的两条邻边张成}\ ✓;\ \text{而 }b(z)=3\Rightarrow z\ \text{恰 3 个码邻}\ ✓\Longrightarrow\ \binom32=\mathbf 3\ \text{个例外面}\ ✓✓$$
$$\qquad q_F=4\ \text{不可能}:\ \text{四角两两距}\le2\ \Longrightarrow\ \text{每角有两个组内码邻}\ \Longrightarrow\ b\ge3\ \Longrightarrow\ \text{四角皆}=z\ \text{✗}\ ✓\ \text{（与 }\texttt{BUDGET}\ \text{引理 A 的 }k{=}2\ \text{同机制 ✓）}$$
$$
$$
```

---

## §3 (U-3) 全部面占据分布由 $A_1$ 决定（故无 collision ✗）

```
$$\#\{q_F=2\}=9A_1+A_2=8A_1+143\ ✓;\quad \#\{q_F=1\}=5355-2(8A_1+143)=5069-16A_1\ ✓$$
$$\qquad\#\{q_F=0\}=11520-(5069-16A_1)-(8A_1+143)=\mathbf{6308+8A_1}\ ✓$$
$$\textbf{必要性检查}:\ \#\{q_F=1\}\ge0\Rightarrow A_1\le316\ ✗\ (\text{远弱于 }A_1\le49);\ \text{各量随 }A_1\ \text{线性}\ \Longrightarrow\ \textbf{无可行域收缩}\ ✗$$
$$\qquad\textbf{判定}:\ \text{2-面语言给出的全部全局量都是 }A_1\ \text{的\textbf{仿射函数}} \Longrightarrow \textbf{无新约束}\ ✗$$
$$
$$
```

---

## §4 (U-4) 数量更正与地图核对

```
$$\#\{\text{2-面}\}=\frac{2^n\binom n2}{4}=\frac{1024\cdot45}{4}=\mathbf{11520}\ ✓✓;\qquad \text{点-面关联数}=2^n\binom n2=46080\ ✗\ (\text{唐稿误用})$$
$$\qquad\textbf{档案核对}:\ \texttt{EXCESS-2026-09-25}\ \text{已记"面数 11520"}\ ✓\ \text{（本档仅更正表述 ✓，\textbf{不列为新提出}）}$$
$$\qquad\textbf{并对表}:\ \text{该档 m-面计数最强仅 }c\ge57\ll94\ll107\ \Longrightarrow\ \text{**该线早已 CLOSED**} ✗\ \text{（本档不重开 ✓）}$$
$$
$$
```

---

## §5 判定与建议（诚实 ⚠️）

```
$$\textbf{本刀}:\ \text{① (U-1) 多重度拆分\textbf{确为新} ✓✓（干净、可复用：任意 }(n,R{=}1)\ \text{下 }d{=}1/d{=}2\ \text{对的面多重度}=n{-}1/1\ ✓）}$$
$$\qquad\text{② (U-2) }q_F\ \text{定理新} ✓\ \text{但 }q_F=4\ \text{情形被 }\texttt{BUDGET}\ \text{更强覆盖 ✓}; ③\ \text{全局量仍 }\propto A_1\ ✗$$
$$\Longrightarrow\ \textbf{第 12 次同向汇合}:\ \text{2-面语言＝又一种 }A_1\ \text{的仿射重写} \Longrightarrow\ \textbf{无 P3 collision}\ ✗$$
$$\textbf{建议}:\ \text{(a) 把 (U-1) 多重度拆分登记为可迁移小资产 ✓（“对-面多重度 = n−1 / 1”）};\ \text{(b) 若继续换语言，宜换到\textbf{非二次型}对象（face occupancy 属二阶，必被 }A_1\ \text{吸收 ⚠️）};\ \text{(c) 119 线维持 }\texttt{OPEN—structurally audited}\ ✓$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1 的多重度为**纯组合**（面由方向对确定 ✓）＋ 已核数 ✓；§2 为**纯局部分类** ✓（无计算 ✓）
- §3 的三个计数式为**本档推导** ✓；其"无收缩"判定为**本档结论** ✓
- §4 的 11520 与既有档案**一致** ✓（非新提出 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张 2-面语言无用 ✗（只主张其全局量被 $A_1$ 吸收 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 码字对-面多重度拆分 命中文件数=1    :: ./FACE-2026-09-26-two-face-occupancy-audit.md 
技术词 q_F 定理       命中文件数=0    ::
```
- **本档新增**：码字对-面多重度拆分（1 档 ✓）；`q_F 定理` **命中 0** ⚠️（本档写作 $q_F$ 定理，该检索词非档案形式 ⟹ **不列为新命名** ✓）
- **档案已有（引用，不列为提出）**：面数 11520（EXCESS）、子立方预算（BUDGET）、字面正方形否证（MIDSUP）、$A_1\le49$、$A_1+A_2=143$
