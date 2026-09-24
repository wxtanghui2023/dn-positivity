已查地图：命中（`CAPMIX1B-B11-capacity-subfield-is-the-large-capacity-class`）⟹ 执行其 §6 之 (1)+(2)，不开新案
D0: 本档对象 = **非子域极值分析**：`\rho_{\max}` 与 top-20 ＋ **`E_{1/2}` 反例搜索（零反例）** ＋ **`3/8` 被击穿（极值 `8/21`）** ＋ 一条**自动闭合定理**（char 2）
D1: 1 （新自由度：非子域极值定位 ＋ `3/8` 常数否定 ＋ `A` 的自动闭合结构）
[RESEARCH]

# **`CAP-MIX-1B · B11.1/2`：非子域极值**

## §1 严格去污染后的 top-20（按 `\rho` 降序，共 36 例非子域）

```
$$\begin{array}{c|c|c|c|c|c|c}
n&d&r&\alpha&3\mid d&\lambda&\rho\\
\hline
6&21&6&0.333&\checkmark&8&\boxed{0.3810}\\
12&21&6&0.005&\checkmark&8&0.3810\\
10&341&10&0.333&\times&120&0.3519\\
10&93&10&0.091&\checkmark&32&0.3441\\
14&5461&14&0.333&\times&1848&0.3384\\
14&381&14&0.023&\checkmark&128&0.3360\\
12&1365&12&0.333&\checkmark&440&0.3223\\
12&45&12&0.011&\checkmark&14&0.3111\\
8&85&8&0.333&\times&24&0.2824\\
9&73&9&0.143&\times&18&0.2466\\
\end{array}$$ ✓✓（其后 10 例 `\rho` 从 0.237 降到 0.066）
```

## §2 ⭐ 极值与 `E_{1/2}` 判定

```
$$\boxed{\rho_{\max}=0.3810\quad(n=6,\ d=21,\ \lambda=8,\ r=6,\ 3\mid d)}$$ ✓✓
$$\boxed{\rho>1/2\ \text{的案例数}=0}\ \Longrightarrow\ \boxed{E_{1/2}\ \text{经验上成立（零反例）}}$$ ✓✓✓
$$\text{照您 EXIT}:\ \text{"无 }\rho>1/2\text{ 且极值远低于 }1/2\ \Longrightarrow\ \text{进入 }E_{1/2}\ \text{的代数证明"}$$ ✓
```

## §3 ⛔⭐ `3/8` 被击穿（重要否定）

```
$$\rho>3/8\ \text{的案例数}=2:\quad d=21\ \text{两次}\ (n=6,12),\ \lambda=8\ \Longrightarrow\ \rho=\frac8{21}=0.38095$$ ✓✓
$$\frac8{21}=0.38095>\frac38=0.375\ \Longrightarrow\ \boxed{\text{常数 }3/8\ \textbf{不成立}}$$ ✓✓✓
$$\Longrightarrow\ \text{若存在 sharp 常数},\ \text{它}\ \ge\frac8{21};\ \text{候选}: c_0=\frac8{21}\ (\text{本网格内 tight})$$ ⚠️
$$\text{照您纪律}:\ \textbf{不围绕 }3/8\ \text{拟合};\ \text{改以 }E_{1/2}\ \text{为攻击目标}$$ ✓
```

## §4 ⭐ 一条**自动闭合定理**（char 2，已可证）

```
$$\textbf{实测}:\ \text{top-10 全部 }|A\cap A^{-1}|=\lambda\ (\text{比值 }1.000)$$ ✓
$$\textbf{但这不是发现而是定理}:\quad x\in A\Rightarrow x,1+x\in G\Rightarrow (1+x)x^{-1}=1+x^{-1}\in G\ (\text{乘法封闭})\ \Rightarrow x^{-1}\in A$$ ✓✓
$$\Longrightarrow\ \boxed{A\subseteq A^{-1}\ (\text{自动})};\qquad \text{另由 char 2}:\ x\in A\Rightarrow 1+(1+x)=x\ \Rightarrow 1+x\in A\ \Longrightarrow\ \boxed{A+1=A}$$ ✓✓
$$\Longrightarrow\ \boxed{A\ \text{同时闭于 }x\mapsto1+x\ \text{与}\ x\mapsto x^{-1}}$$ ✓✓✓
$$\text{生成作用}:\ \langle x\mapsto1+x,\ x\mapsto1+x^{-1}\ (T,\ \text{阶 }3)\rangle\ \text{作用于 }A$$ ✓
$$\Longrightarrow\ \textbf{高容量的结构含义}:\ A\ \text{是一个同时"平移闭 + 取逆闭"的大子集}\ \Longrightarrow\ \text{其生成闭包可能被迫为子域}$$ ✓✓（**正是您 §2 设想的机制**）✓
```

## §5 判定与下一步

```
$$\boxed{(1)\ E_{1/2}\ \text{零反例（经验支持）};\quad (2)\ 3/8\ \text{否定};\quad (3)\ A\ \text{双闭合为定理}}$$ ✓✓✓
$$\textbf{下一步（照您 §5）}:\ \boxed{\text{攻 }E_{1/2}\ \text{的代数证明}:\ \rho>1/2\Rightarrow G\cup\{0\}\ \text{是子域}}$$ ✓✓
$$\text{可用的杠杆}:\ A\ \text{平移闭+取逆闭};\ |A|>d/2\ \text{时 }A\cdot A\ \text{必含大量交集（乘积集/和集下界）}\ \Longrightarrow\ \text{加法闭包}$$ ✓
$$\text{若 }E_{1/2}\ \text{得证}:\ \text{非子域}\Rightarrow\rho\le1/2\ \Longrightarrow\ "\rho\to1\ \text{唯来自子域}"\ \text{获严格定量版}$$ ✓✓
**【sharp 常数支线（单列）】** `c_0=8/21`（本网格 tight）—— **不与主体定理混算** ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**不回 RH** ✓
【数据】 `out/capmix1B11b_nonsub.txt`（36 例逐行）；脚本 `scripts/capmix1B11b_nonsubfield_extremal.py` ✓
【边界】 §1–§3 为实测（`n\le14`）；§4 为**已证**（char 2 自动性）✓

## §附 【技术词回查】（补录）
```
技术词 extremal         命中文件数=26   :: ./CROSS-0-additive-multiplicative-cross-invariant-MAP-CHECK.md ./CEILING-LP-RECOMPUTE-results.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md 
技术词 closure          命中文件数=149  :: ./B-SERIES-INDEX.md ./p3-uniform-decay-results.md ./E3-why-this-is-not-the-old-pit.md 
```
