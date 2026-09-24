已查地图：命中（`M03-region-corrected-and-target-redefined`）⟹ `LS + ES/Soto` 的 `(3+,2-)` 特化与区域减法，不开新案
D0: 本档对象 = **2017 map 原文的确切判据清单**（已入档）＋ **判据的二分结构（线性型 vs 存在型）** ＋ **线性型在 `(1,a,b,-c,-d)` 下的显式特化** ＋ **对先生推导的两项核验与一处修正** ＋ **`③` 的形式纠正（点判定而非集合差）**
D1: 1（首次把 `n=5` 充分条件按"线性／存在"二分；产出显式特化区）
[RESEARCH]

# **`M03`：`LS + ES/Soto` 的 `(3+,2-)` 特化**

## §1 已入档原文（本轮）

```
$$\boxed{\text{map}}\ \Longrightarrow\ \texttt{sources/Marijuan-Pisonero-Soto-2017-map-of-sufficient-conditions-SNIEP.pdf}\ (20\ \text{页})$$ ✓✓
$$\qquad \text{题}:\ “A Map of Sufficient Conditions for SNIEP”\ (C.\ Marijuán,\ M.\ Pisonero,\ R.\ L.\ Soto)$$ ✓
$$\boxed{\text{rule}}\ \Longrightarrow\ \texttt{sources/Johnson-Marijuan-Pisonero-2017-ruling-out-5-spectra.pdf}\ (7\ \text{页},\ LAA\ 512(2017)\ 129\text{–}135)$$ ✓
```

## §2 ⭐ 结构性发现：判据分两类（本档核心）

```
$$\textbf{(L) 线性／有限划分型}（可写成有限条不等式）:\ \text{Suleimanova};\ \text{Perfect–Mirsky};\ \text{Ciarlet};\ \text{Kellogg};\ \text{Borobia}\ (\text{有限划分})$$ ✓✓
$$\textbf{(E) 存在型／递归型}（\textbf{不能}写成有限条不等式）:$$
$$\qquad \text{Soules 1}:\ \exists x=(x_1,\dots,x_n)>0\ \text{使 }d_i\ge0\ (i=1..n)\ \text{（含 }x\ \text{的有理函数式）};\quad \text{Soules 2}:\ \exists\ \text{两组划分};$$
$$\qquad \text{Laffey–Šmigoc}:\ \exists c\ \text{＋递归分裂为 }(\Lambda_1,\Lambda_2);\quad \text{Soto 2}:\ \exists\ \text{划分 ＋ 递推裕量 }MS_{p-1},\ NS_{p-1}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\text{"区域减法"只对 (L) 可直接执行};\ (E)\ \text{型的差集只能\textbf{逐点}处理}:\ \text{给 }x/\text{划分} \Rightarrow \text{可实现};\ \forall x\ \text{不可能} \Rightarrow \text{需证明}}$$ ✓✓✓
$$\text{注}:\ \text{Borobia 的划分在 }(3+,2-)\ \text{下只有 }2\ \text{种（}\{-c,-d\}\ \text{或}\ \{-c\},\{-d\}\text{）} \Longrightarrow \text{可穷举，归入 (L)}$$ ✓
```

## §3 若干确切判据（原文摘录）

```
$$\text{Perfect–Mirsky 1965}:\ \frac{\lambda_1}{n}+\frac{\lambda_2}{n(n-1)}+\dots+\frac{\lambda_n}{2\cdot1}\ge0 \Longrightarrow \text{对称可实现}$$ ✓✓
$$\text{Ciarlet 1968}:\ |\lambda_j|\le\frac{\lambda_0}{n}\ (\text{此处 }n=\text{元数}-1) \Longrightarrow \text{可实现}$$ ✓
$$\text{Kellogg 1971}:\ K=\{i\le\lfloor n/2\rfloor:\lambda_i\ge0,\ \lambda_i+\lambda_{n+1-i}<0\};\ \text{若 }\lambda_0+\sum_{i\in K,i<k}(\lambda_i+\lambda_{n+1-i})+\lambda_{n+1-k}\ge0\ \forall k\in K\ \text{（＋末条）} \Longrightarrow \text{可实现}$$ ✓
$$\text{Soules 1 1983}:\ \exists x>0,\ d_i(x)\ge0\ \text{（(11) 式）};\qquad \text{Soules 2 1983}:\ \exists\ \text{划分（(12) 前式）}$$ ✓
$$\text{Laffey–Šmigoc 2007\ (Thm 13)}:\ \Lambda_1\ \text{由带对角元 }c\ \text{的不可约对称非负矩阵实现},\ \Lambda_2\ \text{可实现} \Longrightarrow \text{合并可实现}$$ ✓✓
$$\textbf{包含关系（原文 Thm 15/16，逐字）}:\ \text{Ciarlet}\Rightarrow\text{Perfect–Mirsky}\ (\text{严格});\ \text{Perfect–Mirsky}\Rightarrow\text{Suleimanova}\ (\text{严格});\ \text{Soules 1}\Rightarrow\text{Suleimanova};$$
$$\qquad \text{Salzmann／Perfect 1 与 Perfect–Mirsky／Soules 1 \textbf{独立}}$$ ✓✓
```

## §4 线性型在 `(1,a,b,-c,-d)` 下的显式特化（零计算，纯代数）

```
$$\text{设定}:\ \lambda=(1,a,b,-c,-d),\quad 1\ge a\ge b>0,\ 0<c\le d\le1,\ S=1+a+b-c-d,\ 0<S<b,\ S<\tfrac12$$ ✓
$$\boxed{K_{\rm Ciarlet}}=R\cap\{a,b,c,d\le\tfrac14\}$$ ✓（与先生一致）
$$\boxed{K_{\rm PM}}=R\cap\Bigl\{\tfrac15+\tfrac{a}{20}+\tfrac{b}{12}-\tfrac{c}{6}-\tfrac{d}{2}\ge0\Bigr\}\ \overset{\times60}{=}\ R\cap\bigl\{\boxed{30d+10c\le12+3a+5b}\bigr\}$$ ✓✓（**本档新特化**）
$$\qquad \textbf{修正}:\ \text{由 Thm 15.1\ (逐字) }\text{Ciarlet}\Rightarrow\text{Perfect–Mirsky} \Longrightarrow \boxed{K_{\rm Ciarlet}\subset K_{\rm PM}} \Longrightarrow \textbf{Ciarlet 不必单列}$$ ✓✓
$$\qquad \text{（先生原述为"Ciarlet}\Rightarrow\text{Laffey–Šmigoc"；map 原文只给 Ciarlet}\Rightarrow\text{Perfect–Mirsky}\Rightarrow\text{Suleimanova};\ \text{该条}\textbf{待核}$$ ⚠️
$$K_{\rm Kellogg}=R\ (\text{先生推导；我复核其结构：}\lambda_1+\lambda_5=1-d\ge0\Rightarrow 1\notin K;\ \text{仅 }i{=}2\ \text{可触发};\ k{=}2\ \text{时条件为 }1-c\ge0\ \checkmark;\ \text{末条减弱为 }S\ge0\ \checkmark)$$ ✓（**末条完整式待逐字核**）
$$K_{\rm Borobia}:\ \text{两种划分各给一条 Kellogg 型条件};\ \text{待特化}$$ ✓
$$\textbf{一并记（一致性检查，代数）}:\ K_{\rm PM}\cap W\ \text{在 }a{=}b,\ c{=}d\ \text{线上会矛盾}（\text{须 }7.4b\ge4.4\ \text{与 }c\le0.3+0.2b,\ \text{同时 }S<b\Rightarrow c>\frac{1+b}{2}\text{）}\Longrightarrow \textbf{无冲突，两结果相容}$$ ✓✓
```

## §5 `③` 的形式纠正（关键）

```
$$\text{原写法}:\ U_{\rm live}=(R\setminus W)\setminus(K_{\rm LS}\cup K_{\rm ES/Soto})\ ——\ \textbf{对 (E) 型不可直接执行}$$ ✗
$$\boxed{\text{正确形式}}\ \text{分两层}:$$
$$\qquad \text{(i) }\textbf{线性层}:\ \text{先把 }(R\setminus W)\setminus(K_{\rm PM}\cup K_{\rm Kellogg}\cup K_{\rm Borobia})\ \text{算出（纯代数，有限条不等式）};\ \text{若为空}\Rightarrow M03\ \textbf{DROP}$$ ✓✓
$$\qquad \text{(ii) }\textbf{存在层}:\ \text{对该差集内的代表点},\ \text{逐点问 }(E)\ \text{型条件}:\ \exists x\ \text{（Soules）／}\exists c\ \text{＋分裂（LS）} \Longrightarrow \textbf{构造性、可精确复核}$$ ✓✓
$$\text{意义}:\ \text{不是"区域减法"，而是}\ \boxed{\textbf{边界点族 ＋ 逐点证书}};\ \text{这与 2026 }W\ \text{边界严格对齐}$$ ✓✓✓
```

## §6 下一刀（建议，仍零计算）

```
$$\boxed{\text{①}}\ \text{完成 }(R\setminus W)\setminus(K_{\rm PM}\cup K_{\rm Kellogg}\cup K_{\rm Borobia})\ \text{的显式代数消元};\ \text{空}\Rightarrow \textbf{DROP}$$ ✓✓
$$\boxed{\text{②}}\ \text{取 }W\ \text{边界 }4=9b-S\ \text{上的有理点族 }(a,b,c,d;\ \text{如取 }a{=}b,\ c{=}d\ \text{或 }d{=}c{+}t)\ \text{作候选}$$ ✓✓
$$\boxed{\text{③}}\ \text{对候选点尝试 (E) 型证书（显式 }x\ \text{或显式 LS 分裂}）\ \Longrightarrow\ \text{可实现}\Rightarrow R\setminus W\ne\emptyset\ \text{（新正结果，证 }W\ \text{边界紧）}$$ ✓✓
$$\boxed{\text{④}}\ \text{或证其不可实现（扩张 }W\text{）}\ ——\ \text{须与 2026"移位＋加权五环"机制竞争},\ \text{门槛高}$$ ⚠️
【⛔ 纪律】 本轮\textbf{零计算}（仅代数改写与文献摘录）；`U_{2,3}` 暂停；**不回 RH**；`C07` 已封口 ✓
【边界】 §3 为\textbf{原文逐字}（已入档）；§4 的 }K_{\rm PM}$$ 系数与 Ciarlet 尺度（`n`＝元数−1）已核；Kellogg 末条与 Borobia 待特化 ✓

## §附 【技术词回查】（补录）
```
技术词 sufficient condition 命中文件数=3    :: ./P8-CLASSIC-SOURCES-li1997-bombieriLagarias1999.md ./p511-adversarial-theorem.md ./E23-lee-yang-dqpt-report.md 
技术词 existential      命中文件数=0    :: 
```
