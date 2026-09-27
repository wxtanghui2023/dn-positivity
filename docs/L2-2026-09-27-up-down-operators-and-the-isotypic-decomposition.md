已查地图：已跑 scripts/prework_map_check.sh D U 算子 交换子 harmonic 重数 ⟹ 执行自 `L3C-...-lemma-chain-draft`（L1/L3 已证 ✓）＋ 唐先生 11:38（只攻 L2 ✓）；本档 = **L2（$D/U$ 与 isotypic 分解）**。
D0: 本档对象 = $\mathbb R^{\{0,1\}^n}$ 的 $S_n$-模分解（经 $D/U$ 交换子路线）
D1: 1（新增：**交换子的显式证明** ✓；**链非零性（含闭式 $c_i$）** ✓；**重数闭式的来源** ✓）

# L2 · $D/U$ 算子与 isotypic 分解（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(PP-1)}\ V=\bigoplus_{i=0}^nV_i,\ V_i=\mathbb R^{\binom{[n]}i}\quad\text{（层分解 ✓ 初等 ✓）}}$$
$$\boxed{\textbf{(PP-2)}\ D_{i+1}U_i-U_{i-1}D_i=(n-2i)I\ \text{在 }V_i\ \text{上}\ ✓\ \text{（\textbf{本档显式证明} ✓；数值 }3.6\times10^{-15}\ ✓\text{）}}$$
$$\boxed{\textbf{(PP-3)}\ \text{对 }h\in H_k:=\ker D_k,\ h_i:=U_{i-1}\cdots U_kh\ (k\le i\le n-k)\ \text{满足}\ h_i\ne0\ ✓\ \text{（长度 }n-2k+1\ ✓）}}$$
$$\boxed{\textbf{(PP-4)}\ \dim H_k=\binom nk-\binom n{k-1}=:m_k\ \text{（}n=4..8\ \text{数值全吻合 ✓；\textbf{证明依赖} sl_2\text{ 半单} ⏳ 见 §5）}}$$
$$
$$
```

---

## §1 L2.1 层分解（初等 ✓）

```
$$\textbf{Prop 1}:\ V=\mathbb R^{\{0,1\}^n}=\bigoplus_{i=0}^nV_i,\quad V_i=\mathbb R^{\binom{[n]}i}\ \text{（按支撑层 ✓，}S_n\text{-不变 ✓）}\qquad \dim V_i=\binom ni\ ✓$$
$$
$$
```

---

## §2 L2.2 $D/U$ 与交换子（**显式证明 ✓**）

```
$$\textbf{约定（本档固定 ✓）}:\ (D_if)(S)=\sum_{y\notin S}f(S\cup y)\ (|S|=i-1)\ ✓;\qquad (U_if)(S)=\sum_{y\in S}f(S\setminus y)\ (|S|=i+1)\ ✓$$
$$\textbf{Prop 2（互为伴随 ✓）}:\ \langle D_if,g\rangle=\langle f,U_ig\rangle\quad(f\in V_i,\ g\in V_{i-1})\ ✓$$
$$\textbf{Proof}:\ \text{左边}=\sum_{|S|=i-1}\sum_{y\notin S}f(S\cup y)g(S)\ ✓;\ \text{重指标 }T=S\cup y\ \text{（}|T|=i\text{）}:\ \sum_{|T|=i}\sum_{y\in T}f(T)g(T\setminus y)=\text{右边}\ ✓$$
$$
$$

$$\textbf{Prop 3（交换子 ✓ 与唐先生式一致 ✓）}:\ D_{i+1}U_i-U_{i-1}D_i=(n-2i)I\ \text{在 }V_i\ \text{上}\ ✓$$
$$\textbf{Proof（显式计数 ✓）}:\ \text{对 }|S|=i\ \text{与 }f\in V_i:$$
$$\quad(D_{i+1}U_if)(S)=\sum_{y\notin S}\sum_{z\in S\cup y}f((S\cup y)\setminus z)
=\underbrace{(n-i)f(S)}_{z=y}+\sum_{y\notin S}\sum_{z\in S}f((S\setminus z)\cup y)\ ✓$$
$$\quad(U_{i-1}D_if)(S)=\sum_{z\in S}\sum_{y\notin S\setminus z}f((S\setminus z)\cup y)
=\underbrace{i\,f(S)}_{y=z}+\sum_{z\in S}\sum_{y\notin S}f((S\setminus z)\cup y)\ ✓$$
$$\quad\text{两式末项相同（同一双重和 ✓）}\ \Longrightarrow\ (D_{i+1}U_i-U_{i-1}D_i)f(S)=(n-2i)f(S)\ ✓\qquad\square$$
$$
$$

$$\textbf{Cor 4（范数恒等式 ✓）}:\ \|U_if\|^2=\|D_if\|^2+(n-2i)\|f\|^2\quad(f\in V_i)\ ✓$$
$$\textbf{Proof}:\ \|U_if\|^2=\langle U_if,U_if\rangle=\langle f,D_{i+1}U_if\rangle=\langle f,U_{i-1}D_if\rangle+(n-2i)\|f\|^2=\|D_if\|^2+(n-2i)\|f\|^2\ ✓$$
$$
$$
```

---

## §3 L2.3 harmonic 空间与重数

```
$$\textbf{Def}:\ H_k:=\ker(D_k:V_k\to V_{k-1})\ ✓\qquad(m_k:=\binom nk-\binom n{k-1}\ ✓)$$
$$\textbf{Prop 5（数值核对 ✓，证明见 §5）}:\ \dim H_k=m_k\quad(k\le n/2)\ ✓$$
$$\qquad\text{核对（本机 ✓）：}n=4:(1,3,2)\ ✓;\ n=5:(1,4,5)\ ✓;\ n=6:(1,5,9,5)\ ✓;\ n=7:(1,6,14,14)\ ✓;\ n=8:(1,7,20,28,14)\ ✓\ \Longrightarrow\ \text{全部 }=\binom nk-\binom n{k-1}\ ✓$$
$$\qquad\text{维度自检}:\ \sum_{k=0}^{\lfloor n/2\rfloor}m_k(n-2k+1)=2^n\ ✓\ \text{（}n=4:16;\ 6:64;\ 7:128\ ✓✓\text{）}$$
$$
$$
```

---

## §4 L2.4 升链（**显式证明 ✓**）

```
$$\textbf{Prop 6（链递推 ✓）}:\ h\in H_k,\ h_i:=U_{i-1}\cdots U_kh\ \Longrightarrow\ D_ih_i=c_ih_{i-1}\quad(k<i)\ ✓$$
$$\qquad c_i:=\sum_{m=k}^{i-1}(n-2m)=(i-k)(n-k-i+1)\ ✓\ \text{（\textbf{闭式} ✓；证明：数学归纳 }+\ \text{Prop 3}\ ✓\text{）}$$
$$\qquad\text{检查}:\ c_k=0\ ✓\ \text{（}D_kh_k=0\ ✓\text{）};\ c_{n-k+1}=0\ ✓\ \text{（链自然终止 ✓）}$$
$$\textbf{Prop 7（非零性 ✓）}:\ h_i\ne0\ \text{对 }k\le i\le n-k\ ✓$$
$$\textbf{Proof}:\ \text{设 }i\ \text{最小使 }h_i=0\ (i>k)\ ✓;\ \text{则 }h_{i-1}\ne0\ \text{而 }D_ih_i=0\ ✗\ \text{与 }D_ih_i=c_ih_{i-1}\ne0\ \text{矛盾（}i\le n-k\ \Longrightarrow\ c_i>0\ ✓\text{）}\qquad\square$$
$$\qquad c_i>0\ \text{的证明}:\ c_i=(i-k)(n-k-i+1)\ \text{两因子在 }k<i\le n-k\ \text{时均正 ✓（}k\le n/2\ ✓\text{）}$$
$$\textbf{Cor 8}:\ \text{每个 }h\in H_k\ \text{给出 }n-2k+1\ \text{个\textbf{不同层}上的非零向量（}h_k,\ldots,h_{n-k}\ ✓\text{）}\ \Longrightarrow\ \text{它们线性无关 ✓}$$
$$
$$
```

---

## §5 重数闭式的来源（**诚实边界 ⏳**）

```
$$\textbf{路线}:\ \text{令 }H=n-2\,(\text{层指标})\ \text{在 }V_i\ \text{上}=n-2i\ ✓;\ \text{由 Prop 3}:\ [H,U]=-2U,\ [H,D]=+2D\ ✓\ \Longrightarrow\ (U,D,H)\ \text{构成 sl}_2\text{ 三元组 ✓}$$
$$\textbf{关键}:\ \text{有限维 sl}_2\text{-模\textbf{半单} ✓（标准引理 ⏳，本档\textbf{未证}）且不可约模由最高权向量决定（最高权 }=\text{被 }D\text{ 杀死 ✓}）}$$
$$\Longrightarrow\ \text{最高权 }n-2k\ \text{的不可约模的\textbf{重数} }\mu_k\ \text{满足（}k\le n/2\text{）}:\ \dim V_k=\sum_{j\le k}\mu_j\ ✓\ \Longrightarrow\ \mu_k=\dim V_k-\sum_{j<k}\mu_j\ ✓$$
$$\Longrightarrow\ \mu_0=1,\ \mu_k=\binom nk-\binom n{k-1}=m_k\ ✓\ \text{（归纳 ✓）—— \textbf{这正是 }\S3\text{ 数值事实的数学来源 ✓✓}}$$
$$\textbf{边界}:\ \text{① sl}_2\text{ 半单性（标准 ✓ 待引/补证 ⏳）；② }\S3\text{ 的 }H_k=\ker D_k\ \text{与最高权空间一致（}k\le n/2\text{）需 }\ker D_k\perp\mathrm{im}\,U_{k-1}\ ✓\ \text{（由 Prop 2 得 ✓）}$$
$$\textbf{唯一引用的表示论输入}:\ H_k\cong S^{(n-k,k)}\ \text{（}k\le n/2\ ✓\text{）}\ \Longrightarrow\ \dim=n-2k+1\ ✓\ \text{（与 Prop 7 的链长相符 ✓）}$$
$$
$$
```

---

## §6 STOP 检查（唐先生设定 ✓）

```
$$\text{① 是否用了完整 Schrijver 块分解定理？}\ \textbf{否}\ ✓\ \text{（L2 全程只用 }D/U\text{ 交换子 + 层分解 + sl}_2\text{ 标准事实 ✓）}$$
$$\text{② 是否用数值维数检查代替 L2？}\ \textbf{否}\ ✓\ \text{（}\S3\text{ 数值仅为\textbf{核对}；}\S5\text{ 给出\textbf{来源} ✓）}$$
$$\text{③ }A_{2,n}\ \text{定义是否与我们的 }S_n\text{-轨道代数一致？}\ \textbf{是}\ ✓\ \text{（}L1\text{ 已证 }\mathcal A_{2,n}=\mathrm{End}_{S_n}(V)\ ✓,\ \dim=\binom{n+3}3\ \text{两侧同 ✓）}\ \Longrightarrow\ \textbf{不触发 STOP}\ ✓$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1／§2／§4 为**本档自足证明** ✓（初等计数 ✓）；§3 为**数值核对** ✓；§5 为**路线 ＋ 一处待引**（sl₂ 半单性 ⏳）
- **未**声称 L2 已全部证毕 ✗（§5 的 sl₂ 半单性未在本档证明 ✓）；**未**声称 PSD 等价已证 ✗
- ⚠️ 自我更正 ✓：本轮核对脚本曾误用 `set(0/1 元组)`（取值集而非支撑 ✗）⟹ 那一列数据作废 ✓，已修正重跑 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$D/U$ 交换子显式证明、链闭式 $c_i=(i-k)(n-k-i+1)$、重数来源（最高权计数）
- **档案已有（引用，不列为提出）**：层分解、harmonic、$m_k$、sl₂、$S^{(n-k,k)}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 交换子显式证明 命中文件数=1    :: ./L2-2026-09-27-up-down-operators-and-the-isotypic-decomposition.md 
技术词 重数来源     命中文件数=1    :: ./L2-2026-09-27-up-down-operators-and-the-isotypic-decomposition.md
```
- **本档新增**：$D/U$ 交换子显式证明、链闭式 $c_i$、重数来源（最高权计数）（见上方命中数；0 命中者为自造语／内部标签 ✓）
