已查地图：已跑 scripts/prework_map_check.sh Young rule 两行 Kostka 无重分解 hook length ⟹ 执行自 `L3B-FINAL-...`（三项待办 ✓）＋ 唐先生 12:01（做 (A) ✓）；本档登记为 **A-L3B-2 — Classical representation-theoretic input** ✓（**非新数学资产** ✓）。
D0: 本档对象 = $V_k$ 的无重 $S_n$-分解（经典输入）
D1: 0（本档为**经典引用 ＋ 逐条核对** ✓，不产生新数学命题 ✓）

# (A) 经典表示论输入：$V_k$ 的两行分解（2026-09-27）

## §0 引理（可引用形式 ✓）

```
$$\boxed{\textbf{(AB-1 两行分解)}\ V_k=\mathbb C[\binom{[n]}k]\cong M^{(n-k,k)}\cong\bigoplus_{j=0}^{k}S^{(n-j,j)}\ ✓\ \text{（各不可约\textbf{恰一次} ✓，}k\le\lfloor n/2\rfloor\ ✓）}$$
$$\boxed{\textbf{(AB-2 维数和)}\ \dim V_k=\sum_{j=0}^{k}\dim S^{(n-j,j)}=\binom nk\ ✓}$$
$$\boxed{\textbf{(AB-3 新 summand)}\ H_k\simeq S^{(n-k,k)},\qquad \dim S^{(n-k,k)}=\binom nk-\binom{n}{k-1}=m_k\ ✓}$$
$$\textbf{来源标注 ✓}:\ \text{引用 \textbf{Young's rule}（两行 Kostka 数 ＝ 1 ✓）＋ hook-length formula ✓ —— \textbf{不重证 Young's rule} ✓（唐先生 12:01 ✓）}$$
$$
$$
```

---

## §1 Young's rule 推导（**✓**）

```
$$\text{把 }V_k\ \text{识别为 }k\text{-子集置换模 }M^{(n-k,k)}\ ✓\ \text{（}\mathbb C\ \text{上的置换表示 ✓，特征标由不动点计数给出 ✓）}$$
$$\text{Young's rule}:\ M^{(n-k,k)}=\bigoplus_{\lambda\vdash n}K_{\lambda,(n-k,k)}\,S^{\lambda}\ ✓\ \text{（}K=\text{Kostka 数 ✓）}$$
$$\text{dominance 条件}:\ K_{\lambda,\mu}\ne0\Longrightarrow\lambda\trianglerighteq\mu\ ✓;\ \mu=(n-k,k)\ \text{只有两行 ⟹ }\lambda=(\lambda_1,\lambda_2)\ \text{至多两行且 }\lambda_1\ge n-k,\ \lambda_2\le k\ ✓$$
$$\qquad\Longrightarrow\ \lambda=(n-j,j),\ 0\le j\le k\ \text{（唯一参数化 ✓）};\ \text{且两行情形 }K_{(n-j,j),(n-k,k)}=1\ ✓\ \text{（经典 ✓）}$$
$$\Longrightarrow\ V_k\cong S^{(n,0)}\oplus S^{(n-1,1)}\oplus\cdots\oplus S^{(n-k,k)}\ ✓\ \text{（\textbf{无重} ✓）}\qquad\square$$
$$
$$
```

---

## §2 维数：hook-length（**✓ 显式计算**）

```
$$\text{两行图 }(a,b):=(n-k,k)\ \text{的 hook 长}:\ \text{行 1 第 }i\ \text{格}:\ (a-i+1)+\mathbf 1[i\le b]\ ✓;\ \text{行 2 第 }i\ \text{格}:\ (b-i+1)\ ✓$$
$$\prod\text{hooks}=\underbrace{\frac{(a+1)!}{(a-b+1)!}}_{\text{行 1 前 }b\ \text{格}}\cdot\underbrace{(a-b)!}_{\text{行 1 后段}}\cdot\underbrace{b!}_{\text{行 2}}=\frac{(a+1)!\,b!}{a-b+1}=\frac{(n-k+1)!\,k!}{n-2k+1}\ ✓$$
$$\dim S^{(n-k,k)}=\frac{n!}{\prod\text{hooks}}=\frac{n!\,(n-2k+1)}{(n-k+1)!\,k!}\ ✓$$
$$\text{而}\ \binom nk-\binom{n}{k-1}=\frac{n!}{k!(n-k+1)!}\big[(n-k+1)-k\big]=\frac{n!\,(n-2k+1)}{k!(n-k+1)!}\ ✓\ \Longrightarrow\ \textbf{两者相同}\ ✓\ \Longrightarrow\ \textbf{AB-3}\ ✓$$
$$
$$
```

---

## §3 数值核对（**✓ 本机，$n=4..10$**）

```
$$\begin{array}{c|c|c}
n & \sum_{j\le k}\dim S^{(n-j,j)}\overset{?}{=}\binom nk & \dim S^{(n-k,k)}\overset{?}{=}m_k\\
\hline
4 & (1,4,6)\ ✓ & (1,3,2)\ ✓\\
5 & (1,5,10)\ ✓ & (1,4,5)\ ✓\\
6 & (1,6,15,20)\ ✓ & (1,5,9,5)\ ✓\\
7 & (1,7,21,35)\ ✓ & (1,6,14,14)\ ✓\\
8 & (1,8,28,56,70)\ ✓ & (1,7,20,28,14)\ ✓\\
9 & (1,9,36,84,126)\ ✓ & (1,8,27,48,42)\ ✓\\
10 & (1,10,45,120,210,252)\ ✓ & (1,9,35,75,90,42)\ ✓\\
\end{array}$$
$$\text{与 L2 的 }\dim\ker D_k\ \text{实算交叉核对 ✓}:\ n=6:(1,5,9,5)\ ✓;\ n=7:(1,6,14,14)\ ✓;\ n=8:(1,7,20,28,14)\ ✓\ \text{—— 全中 ✓✓}$$
$$
$$
```

---

## §4 在 Level 3B 中的角色（**明确划界 ✓**）

```
$$\boxed{V_k=\bigoplus_{j\le k}H_j\ \text{（作为 }S_n\text{-模 ✓）};\qquad H_k\simeq S^{(n-k,k)},\ \text{重数}=1\ ✓}$$
$$\textbf{承担}:\ \text{① 层分解的无重性；② }H_k\ \text{的不可约类型与维数；③ }\mathrm{mult}=1\ \text{（重数在 }V\ \text{中}=n-2k+1\ \text{的原因是链长 ✓）}$$
$$\textbf{不承担（唐先生 ✓）}:\ \textbf{PSD 等价} ✗ —— 那由\ \text{Maschke ＋ Schur ＋ 谱事实}\ \text{承担（L3B ✓）}$$
$$\text{新 summand 的定位（✓ 用已证结构）}:\ U:H_k\to V_{k+1}\ \text{＋链长 }n-2k+1\ \text{（L2 ✓）}\ \Longrightarrow\ H_k\ \text{取自该层中\textbf{不来自 }V_{k-1}\ \text{的那一个新不可约} ✓}$$
$$
$$
```

---

## §5 登记与边界（诚实标注 ✓）

```
$$\textbf{登记} ✓:\ \textbf{A-L3B-2 — Classical representation-theoretic input}（\textbf{非新数学资产} ✗ ✓；不应计入 N×L×G×D 的 D ✓）$$
$$\textbf{范围}:\ k\le\lfloor n/2\rfloor\ ✓\ \text{（}M^{(n-k,k)}\ \text{的两行条件 ✓；对 }k>n/2\ \text{用补层对称 ✓）}$$
$$\textbf{未做（且不需要 ✓）}:\ \text{不重证 Young's rule／Kostka 数／hook-length formula ✗（唐先生 12:01 ✓）}$$
$$\textbf{待办余项}:\ \text{(B) }M''\ \text{border 的 }D^{1/2}\ \text{归一化引理};\ \text{(C) }N\ \text{中 }\eta\ \text{的符号闭式 ⏳}$$
$$
$$
```

---

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：两行分解引理登记、hook-length 显式乘积、classical input 划界
- **档案已有（引用，不列为提出）**：Young's rule、Kostka 数、hook-length formula、$M^{(n-k,k)}$、$S^{(n-k,k)}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 两行分解引理 命中文件数=1    :: ./A-L3B-2-2026-09-27-classical-two-row-input.md 
技术词 classical input 划界 命中文件数=1    :: ./A-L3B-2-2026-09-27-classical-two-row-input.md
```
- **本档新增**：两行分解引理登记、hook-length 显式乘积、classical input 划界（见上方命中数；0 命中者为自造语／内部标签 ✓）
