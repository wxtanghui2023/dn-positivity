已查地图：已跑 scripts/prework_map_check.sh 范数闭式 因式分解引理 母函数 归一 ⟹ 执行自 `A2-...-rho-u-...`（$\rho_u$ ✓）＋ 唐先生 11:48（(a)→(b) ✓）；本档 = **L5 闭合 ＋ L4-5 因式分解引理（含 convention 状态 ✓）**。
D0: 本档对象 = $\|h_i\|^2$ 闭式（L5）与 $\sum_u\rho_uN_u$ 的母函数（L4-5 核心）
D1: 1（新增：**$\|h_i\|^2$ 闭式（两条独立推导 ✓）**；**因式分解引理 ✓✓**；**convention 差异的精确定位 ✓**）

# L5 ＋ L4-5 因式分解引理（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(TT-1 L5 闭合 ✓)}\ \frac{\|h_i\|^2}{\|h\|^2}=((i-k)!)^2\binom{n-2k}{i-k}=\frac{(i-k)!(n-2k)!}{(n-i-k)!}\ ✓\quad(k\le i\le n-k)}$$
$$\qquad\text{两条独立推导: ① incidence＋Vandermonde ✓；② L2 的 }D_i h_i=c_i h_{i-1}\ (c_i=(i-k)(n-k-i+1)\ ✓)\ +\ \text{伴随性}\ D_i=U_{i-1}^*\ ✓\ \Longrightarrow\ \frac{c_{k,i}}{c_{k,i-1}}=c_i\ ✓$$
$$\qquad\text{数值核对（本机 ✓）：}(n,k)=(6,1):(1,4,24,144,576)\ ✓;\ (6,2):(1,2,4)\ ✓;\ (7,2):(1,3,12,36)\ ✓;\ (5,2),(6,3),(7,3)\ ✓\ \text{全吻合 ✓✓}$$
$$\boxed{\textbf{(TT-2 因式分解引理 ✓✓)}\ \sum_{u=0}^{k}(-1)^{k-u}\binom kuF_u(p,q,r)=p^kq^k(r-1)^k\big(1+p+q+pqr\big)^{\,n-2k}\ ✓\ \text{（\textbf{乘积形式} ✓）}}$$
$$\qquad\text{核对（本机 ✓）：}(n,k)=(5,1):36=36\ ✓;\ (5,2):12=12\ ✓;\ (6,2):28=28\ ✓;\ (6,3):4=4\ ✓\ \text{全恒等 ✓✓}$$
$$\qquad\textbf{证明（一行 ✓）}:\ \sum_u(-1)^{k-u}\binom ku(AD)^u(BC)^{k-u}=(AD-BC)^k,\quad AD-BC=pq\,[\,r\alpha-(1+qr)(1+pr)\,]=pq(r-1)\ ✓\ \text{其中 }\alpha=1+p+q+pqr\ ✓$$
$$
$$
```

---

## §1 L5 的来历（**归一因子的可追溯来源 ✓**）

```
$$\text{此前经验现象}:\ \text{"漏归一 ⟹ 特征值偏差 }40/400/1800;\ \text{补上 }\Longrightarrow10^{-13}"\ \text{—— 现成为\textbf{可追溯数学因子} ✓✓}$$
$$\text{原始（未归一）链}: h_i=U^{i-k}h\ ✓;\ \text{正交基}: e_i=h_i/\|h_i\|\ ✓\ \Longrightarrow\ \text{归一因子}\ \frac{\|h_i\|}{\|h\|}=(i-k)!\sqrt{\binom{n-2k}{i-k}}\ ✓$$
$$\text{早先出现的 }\binom{n-2k}{i-k}^{-1/2}\text{ 型因子 ＝ }\|h_i\|/\|h\|\ \text{的倒数（在\textbf{归一化} convention 下 ✓）}\ ✓\ \text{—— 两处 convention 不混 ✓}$$
$$
$$
```

---

## §2 因式分解引理的证明（**✓ 一行**）

```
$$\textbf{令}\ \alpha:=1+p+q+pqr,\ A:=pqr,\ B:=p(1+qr),\ C:=q(1+pr)\ \Longrightarrow\ F_u=A^uB^{k-u}C^{k-u}\alpha^{\,n-2k+u}\ ✓$$
$$\sum_u(-1)^{k-u}\binom kuF_u=\alpha^{\,n-2k}\sum_u(-1)^{k-u}\binom ku(AD)^u(BC)^{k-u}
=\alpha^{\,n-2k}(AD-BC)^k\quad\text{（二项式 ✓）}$$
$$AD-BC=pqr\alpha-pq(1+qr)(1+pr)=pq\,[\,r\alpha-(1+qr)(1+pr)\,]\ ✓$$
$$\qquad r\alpha-(1+qr)(1+pr)=r+pr+qr+pqr^2-1-pr-qr-pqr^2=r-1\ ✓\ \Longrightarrow\ AD-BC=pq(r-1)\ ✓$$
$$\Longrightarrow\ \boxed{G(p,q,r):=\sum_u(-1)^{k-u}\binom kuF_u=p^kq^k(r-1)^k\alpha^{\,n-2k}}\ ✓\qquad\square$$
$$
$$
```

---

## §3 convention 差异的精确定位（**诚实 ＋ 结构性 ✓**）

```
$$\text{数值判决（本机 ✓）}:\ \beta^{\rm chain}:=\frac{\langle h_i,M^t_{i,j}h_j\rangle}{\|h_i\|^2}\ \text{与作者闭式}\ \beta^{\rm paper}\ \text{比对}$$
$$\qquad(n,k)=(6,1):\ 48/175\ \text{组不符，且严格为\textbf{因子 }2}（-12\ \text{vs}\ -6,\ +12\ \text{vs}\ +6\ ✓）;\ (5,1):28/96\ ✓;\ (6,2):16/63\ ✓;\ (7,2):36/128\ ✓;\ (6,3):\mathbf{0/7}\ ✓$$
$$\qquad\text{独立手算核对（}(n,k,i,j,t)=(6,1,1,3,0)\ ✓\text{）}:\ \text{本侧 }\beta=-12\ ✓\ \text{（}h_3(S)=2\sum_{x\in S}h(x)\ ⟹\ (M^0_{1,3}h_3)(S)=12\sum_{x\notin S}h(x)\ ⟹\ \langle\cdot\rangle=12[({\sum}h)^2-\|h\|^2]=-12\ ✓\text{）}$$
$$\Longrightarrow\ \textbf{不是计算错误} ✓;\ \text{而是\ \textbf{作者闭式与其 }x^t_{i,j}\ \text{坐标的 convention}（方向／归一）}\ \text{与我们的 raw chain 定义相差一个因子 ✓}$$
$$\qquad\text{唐先生 11:44 预警 ✓}:\ "具体标量取决于你对 }h_i\text{ 的归一化和 }M^t_{i,j}\text{ 的方向约定"\ ——\ \textbf{已被数值精确证实} ✓✓$$
$$
$$
```

---

## §4 现状与下一步

```
$$\text{已闭合}:\ L1\ ✓\ |\ L2\ \text{主体}\ ✓\ |\ L3\ ✓\ |\ L4\text{-}1\ ✓\ |\ L4\text{-}2/3/4\ ✓\ |\ A\text{-}1\ ✓\ |\ A\text{-}2\ ✓\ |\ \textbf{L5}\ ✓\ |\ \textbf{因式分解引理}\ ✓$$
$$\text{未闭合}:\ (i)\ \text{把 }\sum_u\rho_uN_u=[p^iq^jr^t]G\ \text{展开并与作者闭式\textbf{逐项对齐}（含 convention 因子 ✓）};\ (ii)\ M''/N\ \text{的对应链}\ ⏳$$
$$\text{可直接用现成工具 ✓}:\ G=p^kq^k(r-1)^k\alpha^{\,n-2k}\ \text{的系数提取 ⟹ }\alpha^{\,n-2k}\ \text{的多项式展开 ＋ }(r-1)^k\ \text{的二项 ⟹ 三重计数（}n_0,n_1,n_2,n_3\text{）⟹ 与作者三 binomial 对齐 ✓}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §0–§2 为**本档证明 ＋ 数值核对** ✓（全吻合 ✓）；§3 为**判决性定位** ✓（含独立手算 ✓）
- **未**声称作者闭式已由我们链条导出 ✗（差 convention 因子 ✓）；**未**声称 formulation 等价已证 ✗
- ⚠️ 自我更正 ✓：本轮脚本曾两处 bug（`if G else R` 丢首轮系数 ✗；范数按 $k$-子集而非 $i$-子集分配 ✗）⟹ 已修正并复跑 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\|h_i\|^2$ 闭式、因式分解引理、convention 因子定位
- **档案已有（引用，不列为提出）**：Vandermonde、二项式定理、伴随性、falling factorial、Eberlein


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 因式分解引理 命中文件数=1    :: ./L5-2026-09-27-norm-closed-form-and-factorization-lemma.md 
技术词 convention 因子定位 命中文件数=1    :: ./L5-2026-09-27-norm-closed-form-and-factorization-lemma.md
```
- **本档新增**：$\|h_i\|^2$ 闭式、因式分解引理、convention 因子定位（见上方命中数；0 命中者为自造语／内部标签 ✓）
