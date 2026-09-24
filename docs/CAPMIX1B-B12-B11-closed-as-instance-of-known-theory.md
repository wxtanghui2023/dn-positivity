已查地图：命中（`CAPMIX1B-B11-3-E-half-falsified-and-proposition-refuted`）⟹ 执行其 §5 之 (A)（新性核查），不开新案
D0: 本档对象 = **`B12` 已知理论精确对照**：`\lambda=d^2/Q+O(\sqrt Q)\ (Q=p^{\mathrm{ord}_d(p)})` 的 439 例机器核验（**零超界、偏差顶到上限**）＋ **最小包含域引理（一行可证）** ＋ ⛔**自我纠正**（"模型乙失效"是我的方法错误）⟹ `B11` **收口为已知理论的实例化**
D1: 1 （新自由度：`B11` 定性收口（非新机制）＋ 保留资产与否定结果清单）
[RESEARCH]

# **`CAP-MIX-1B · B12`：`B11` 作为已知理论实例收口**

## §1 ⛔ 先纠正我自己的方法错误（两处）

```
**(错误一)** 我把 `\rho\approx1/m` 与 `\lambda\approx d^2/q` 当成**两个模型** —— 其实后者除以 `d` 就是前者： ✓
$$\frac{d^2/Q}{d}=\frac dQ=\frac1m\left(1-\frac1Q\right)\ \Longrightarrow\ \boxed{\text{模型乙}=\text{模型甲}/d}\quad(\text{您 §6 已指出})$$ ✓✓
**(错误二)** 我判 `(n{=}10,d{=}93)` 为"模型乙失效"，**没有把偏差与 `\sqrt Q` 比**： ✓
$$\text{主项}\ \frac{93^2}{1024}=8.45,\quad \lambda=32,\quad \text{偏差}=23.55<\sqrt{1024}=32\ \Longrightarrow\ \textbf{完全在 Weil 误差内，非失效}$$ ✓✓✓
$$\Longrightarrow\ \textbf{该诊断点不是"理论外的薄缝"，而是 }Q\ \text{小}、\sqrt Q\ \text{压过主项的典型区}$$ ✓
```

## §2 ⭐ 439 例机器核验（**零超界 + 偏差顶到上限**）

```
$$\textbf{STATS}:\ \text{cases}=439,\qquad \boxed{\texttt{dev}>\sqrt Q:\ 0\ \text{例}},\qquad \texttt{dev}>2\sqrt Q:\ 0\ \text{例}$$ ✓✓✓
$$\max\frac{\texttt{dev}}{\sqrt Q}=\boxed{0.9648}\quad(p{=}13,\ d{=}336,\ Q{=}28561,\ \lambda{=}167,\ \text{主项}{=}4.0,\ \text{dev}{=}163,\ \sqrt Q{=}169)$$ ✓✓
$$\text{均值}\ |\text{dev}|=11.07;\qquad \text{子域案例}\ (m{=}1):\ \text{dev}\approx0.016\!\sim\!0.25\ (\text{即}\ \lambda=d-1\ \textbf{精确})$$ ✓✓
$$\Longrightarrow\ \boxed{(i)\ \text{经典 Weil 型估计完整解释全部 439 例};\quad (ii)\ \textbf{偏差已顶到 }\sqrt Q\text{ 尺度}\Longrightarrow\textbf{不残留可见的加严空间}}$$ ✓✓✓
```

## §3 ⭐ 最小包含域引理（一行可证，本档定稿）

```
$$\text{设}\ Q=p^{\mathrm{ord}_d(p)}\ (\text{含 }G\ \text{的最小子域}),\ \text{则}\ x\in G\Rightarrow x\in\mathbb F_Q,\ \text{且}\ 1+x\in\mathbb F_Q$$ ✓
$$\text{判据}\ 1+x\in G\iff(1+x)^d=1\ \text{只依赖元素本身}\ \Longrightarrow\ \textbf{与外围大域 } \mathbb F_{p^n}\ \text{无关}$$ ✓✓
$$\Longrightarrow\ \boxed{\lambda(G,\mathbb F_{p^n})=\lambda(G,\mathbb F_Q)}$$ ✓✓✓（**证明了一行**）
$$\text{解释}:\ d{=}21\ \text{时}\ Q=2^6=64,\ \text{故}\ n{=}6\ \text{与}\ n{=}12\ \text{皆}\ \lambda=8$$ ✓✓
```

## §4 已知理论对照（您提供的文献）

```
$$\text{对象等同}:\quad \lambda=|G\cap(G+1)|\ (\text{char 2}),\qquad |G\cap(G-1)|\ (\text{一般})\ =\ \textbf{“乘法子群加法平移的交集”}$$ ✓
$$\text{文献线}:\ \text{Shkredov–Vyugin（多平移）};\ \boxed{\text{Vyugin–Solodkova–Shkredov 2016《Intersections of Shifts of Multiplicative Subgroups》}}$$ ✓
$$\qquad\qquad \text{（Stepanov 方法；应用于乘法子群的 additive decomposability）};\ \text{Garcia–Voloch（}m{=}1\ \text{型）}$$ ✓
$$\text{机制等同}:\ 1_G=\frac1m\sum_{\chi\in X}\chi\ (\chi^m=1)\ \Longrightarrow\ \lambda=\frac1{m^2}\sum_{\chi,\psi}\sum_x\chi(x)\psi(1+x)$$ ✓
$$\qquad \text{主项}\ \frac{Q-2}{m^2}=\frac{d^2}{Q}(1+O(Q^{-1}));\qquad \text{非平凡项}= \text{Jacobi 型},\ |\cdot|\le\sqrt Q\ (\text{Weil})$$ ✓✓
$$\Longrightarrow\ \boxed{\lambda=\frac{d^2}{Q}+O(\sqrt Q)}\quad(\text{已知机制，非新})$$ ✓✓
$$\textbf{子域情形}\ m=1:\ \frac{d^2}{Q}=\frac{(Q-1)^2}{Q}=Q-2+\frac1Q=d-1+\frac1Q\ \Longrightarrow\ \lambda=d-1\ (\text{与我们的证明一致})$$ ✓✓
$$\textbf{反例族解释}:\ m=2\Rightarrow\rho\to\frac12\ (\text{可超 }\frac12\ \text{因 }\sqrt Q\ \text{波动});\ m=3\Rightarrow\rho\to\frac13;\ \Longrightarrow\ \textbf{非"反常"，是密度主项}$$ ✓✓
```

## §5 `B11` 判定（照您 §9 表）

```
$$\boxed{\texttt{B11-CLOSED}\ \text{—— 作为已知理论（乘法子群平移交集）的实例化收口}}$$ ✓✓✓
$$\text{理由}:\ (i)\ \text{对象经典};\ (ii)\ \text{主项与误差机制经典};\ (iii)\ 439\ \text{例零超界且偏差顶上限}\ \Longrightarrow\ \textbf{无可见加严空间}$$ ✓✓
$$\textbf{不得宣称}:\ \text{"大容量唯一来自子域"作为新定理};\quad 8/21\ \text{为 sharp 常数};\quad E_{1/2},\ 3/8$$ ✓
```

## §6 保留资产（全部为**已知理论的实例/我们自己的小结果**）

```
**(A)** 最小包含域引理 `\lambda(G,\mathbb F_{p^n})=\lambda(G,\mathbb F_Q)`（**一行证明，本档定稿**）✓✓
**(B)** 子域精确值 `d=p^k-1\Rightarrow\lambda=d-1`（**我们的直接证明**）✓
**(C)** 否定结果清单：`E_{1/2}`（24 例）、`3/8`（`d=21`）、`AA\setminus\{1\}\subseteq A`（50 例）、`B5/B6` 两条 ✓
**(D)** `B9` 定理（`2^k\equiv-1\ \wedge\ 3\nmid d\Rightarrow\lambda=0`，`7/7`）—— **属本支线唯一自证定理** ✓✓
**(E)** 数据：`out/capmix1B12_lit.txt`（439 例含主项/偏差/比值）✓
```

## §7 剩余（若还要继续，须明确标注"已知理论之外"）

```
$$\textbf{唯一形态}:\quad \boxed{\text{char 2}+\text{单平移}+\text{最小包含域结构下，能否比通用 Weil/Stepanov 更尖锐？}}$$ ⚠️
$$\text{数据立场}:\ \max\frac{\texttt{dev}}{\sqrt Q}=0.965\ \Longrightarrow\ \textbf{尺度上已饱和}\ \Longrightarrow\ \text{若有加严，只能是\textbf{常数级}/\textbf{特定参数族}},\ \text{非尺度级}$$ ⚠️
$$\text{照您纪律}:\ \text{不宣称新机制};\ \text{如需继续，须先给出明确超出已知理论的命题形态}$$ ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**不回 RH**；**不拟合** ✓
【数据】 `out/capmix1B12_lit.txt`；脚本 `scripts/capmix1B12_lit_alignment.py` ✓
【边界】 §2 为机器实测（439 例）；§3/§4 为**推导**（一行引理 + 经典字符和机制）✓

## §附 【技术词回查】（补录）
```
技术词 shift            命中文件数=33   :: ./r3-death-sentence-2026-09-09.md ./PAPERA-v2-structure.md ./R_8v-transform-chain-audit.md 
技术词 character sum    命中文件数=4    :: ./C305-FSD-blind-spot-audit-program-four-classes-dual-ledger-five-rounds.md ./CAPMIX1B-B11-3-E-half-falsified-and-proposition-refuted.md ./V228-root-edge-barrier-audit-analytic-barrier-impossible.md 
```
