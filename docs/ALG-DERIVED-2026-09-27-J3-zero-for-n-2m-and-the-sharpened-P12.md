已查地图：已跑 scripts/prework_map_check.sh van Wee 等号 b≤2 d₁≤1 J₃=0 ⟹ 执行自 `ALG-2026-09-27-matching-conjecture`（✓）＋ 唐先生 12:51（转等号条件 ✓）；本档 = **推导链完成：b≤2 ⟹ d₁≤1 ⟹ J₃=0 ⟹ P1-2 锐化** ✓✓。
D0: 本档对象 = $n=2^m$ 时 $J_3=0$ 的推导及其对 P1-2 的锐化
D1: 2（**推导链 ✓✓**；**$A=A_1{+}A_2=M/2$ 对 $n=2^m$ 已证 ✓**；**P1-2 锐化为单一可判定命题 ✓**）

# 推导：$n=2^m$ 时 $J_3=0$（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BJ-1 ⭐推导链 ✓✓)}\ \underbrace{n=2^m,\ R=1,\ |C|=2^n/n}_{\text{van Wee 取等}}\ \Longrightarrow\ \text{nearly-perfect}\ \Longrightarrow\ \textbf{b(x)}\le2\ \forall x\ \text{（引理 ✓）}\ \Longrightarrow\ \forall c\in C:\ b(c)=1+d_1(c)\le2\ \Longrightarrow\ \boxed{d_1(c)\le1}\ ✓✓}$$
$$\qquad\Longrightarrow\ m\equiv0\ \Longrightarrow\ \boxed{J_3=J_6=0}\ ✓,\qquad \boxed{J_2=2A_1}\ ✓$$
$$\boxed{\textbf{(BJ-2 副产品：}A=A_1{+}A_2=M/2\ \text{已证 ✓)}\ b\in\{1,2\}\ \text{且双覆盖点数}=M\ \Longrightarrow\ \sum_x\binom{b}2=M\ \Longrightarrow\ 2A=M\ \Longrightarrow\ \boxed{A=\frac M2=\frac{2^{n-1}}{n}}\ ✓✓}$$
$$\qquad\text{核（}n=8\text{）}:\ M/2=16\ ✓✓\ \text{—— 两码皆 16 ✓（\textbf{证实我此前 }A{=}16\ \text{的判断，否证 }A{=}24\ ✗）}$$
$$\boxed{\textbf{(BJ-3 ⭐P1-2 锐化 ✓✓)}\ n=2^m\ \text{时 support-2 fingerprint 只剩两个自由分量}:\ \boxed{\mathbf J=(2A_1,\ 0,\ 0,\ 0,\ 0,\ J_7,\ \Sigma_ia_i^2)}\ ✓}$$
$$\qquad\Longrightarrow\ \textbf{P1-2 锐化为单一命题}:\ \text{在同一 }A_1\ \text{类内}（A_2\ \text{由 }M/2-A_1\ \text{定 ✓），\ \textbf{是否 }\Sigma_ia_i^2\ \text{与 }J_7=\Sigma q_{ij}^2\ \text{恒定？} ✓✓}$$
$$
$$
```

---

## §1 等号条件的 source-first 抽取（**✓ 逐字**）

```
$$\text{(1) van Wee 界（档案 CLOSE-2026-09-26 逐字引自 arXiv:2608.12595 式 (5) ✓）}:\ M\Big(\sum_{i=0}^{R}\binom ni-\frac{\binom nR}{\lceil\frac{n-R}{R+1}\rceil}\big(\lceil\tfrac{n+1}{R+1}\rceil-\tfrac{n+1}{R+1}\big)\Big)\ge2^n$$
$$\qquad n=8,R=1:\ 9-\frac84\cdot\tfrac12=8\ \Longrightarrow\ 8M\ge256\ \Longrightarrow\ M\ge32\ ✓;\ \text{偶数 }n:\ \text{修正项}=1\ \Longrightarrow\ \boxed{nM\ge2^n}\ ✓$$
$$\text{(2) nearly-perfect 定义（同源摘要逐字 ✓）}:\ \textit{"nearly-perfect covering codes, which are codes that attain the Van Wee bound with equality"} ✓$$
$$\text{(3) 关键引理（同源 Lemma 3.18 逐字 ✓）}:\ \textit{"If }C\text{ is an }(n,M,d)_R\ \text{nearly-perfect covering code, and }z\in\mathbb F_2^n\text{ is over-covered, then it is covered by exactly two codewords"}\ ✓$$
$$\qquad\Longrightarrow\ \text{覆盖 }\Rightarrow b\ge1\ ✓;\ \text{over-covered }\Rightarrow b=2\ ✓\ \Longrightarrow\ \boxed{b(x)\in\{1,2\}\ \forall x}\ ✓\ \text{（\textbf{这就是"哪一个等号条件"的答案} ✓✓）}$$
$$
$$
```

---

## §2 推导的实现（**两行 ✓，本机实证 ✓✓**）

```
$$\text{恒等式（本机 6/6 码全验 ✓✓）}:\ b(c)=1+d_1(c)\qquad\forall c\in C\ ✓\ \text{（}c\ \text{自身 ＋ 距离 1 的码字 ✓）}$$
$$\text{由 }b(c)\le2\ \Longrightarrow\ 1+d_1(c)\le2\ \Longrightarrow\ \boxed{d_1(c)\le1}\ ✓\ \Longrightarrow\ S(c)\cap S(c')=\cdots\Longrightarrow m\equiv0\ \Longrightarrow\ J_3=0,\ J_6=0\ ✓$$
$$\text{且 }d_1(c)\in\{0,1\}\ \Longrightarrow\ d_1(c)^2=d_1(c)\ \Longrightarrow\ J_2=\sum_cd_1(c)=2A_1\ ✓$$
$$
$$
```

---

## §3 数值实证（**✓ 本机，6 码 ✓**）

```
$$\begin{array}{c|c|c|c|c|c|c|c}
\text{码} & b\ \text{取值} & b_{\max} & d_1^{\max} & J_2 & 2A_1 & J_3 & \Sigma_ia_i^2\\
\hline
\text{Kéri }K\_8\_1\ (n=8) & \{1,2\} & 2 & \mathbf 1 & 16 & 16\ ✓ & \mathbf 0 & 64\\
H(7,4)\times\mathbb F_2\ (n=8) & \{1,2\} & 2 & \mathbf 1 & 32 & 32\ ✓ & \mathbf 0 & 256\\
K\_6\_1\ \#0 & \{1,2,3\} & 3 & 0 & 0 & 0\ ✓ & 0 & 0\\
K\_6\_1\ \#1 & \{1,2,3\} & 3 & \mathbf 2 & 12 & 8\ ✗ & \mathbf 4 & 8\\
K\_9\_1\ \#0 & \{1,2,3,4\} & 4 & \mathbf 3 & 26 & 14\ ✗ & \mathbf 6 & 13\\
K\_9\_1\ \#1 & \{1,2,3,4\} & 4 & \mathbf 3 & 106 & 52\ ✗ & \mathbf{117} & 150\\
\end{array}$$
$$\textbf{判读 ✓✓}:\ \text{恰好 }n=2^m\ \text{的两码 }b_{\max}=2\ \Longrightarrow\ d_1^{\max}=1\ \Longrightarrow\ J_3=0,\ J_2=2A_1\ ✓✓;\ \text{非 }2^m\ \text{的码 }b_{\max}\ge3\ \Longrightarrow\ d_1^{\max}\ge2\ \Longrightarrow\ J_3>0,\ J_2>2A_1\ ✓$$
$$\qquad\Longrightarrow\ \text{推导链与其\textbf{反面对照}同时成立 ✓（}b\le2\ \text{是 }n=2^m\ \text{的关键 ✓）}$$
$$
$$
```

---

## §4 对 P1-2 的意义（**⭐ 锐化 ✓✓**）

```
$$\text{原 P1-2}:\ \exists C\ne C':\ (A_1,A_2)\ \text{同}\ \wedge\ J\ne J'\ \text{（}\mathbf J\ \text{共 7 分量 ✓）}$$
$$\text{现 n=2^m}:\ (A_1,A_2)\ \text{同}\ \Longrightarrow\ A_2=M/2-A_1\ \text{自动同 ✓};\ \ J_3=J_6=0\ \text{自动 ✓};\ J_2=2A_1\ \text{自动 ✓}$$
$$\qquad\Longrightarrow\ \textbf{唯一可变的只有}\ \boxed{\Sigma_ia_i^2\ \text{与}\ J_7=\sum q_{ij}^2}\ ✓ \Longrightarrow\ \textbf{P1-2 归结为一个锐命题}:\ \boxed{\text{同一 }A_1\ \text{类内},\ \Sigma a_i^2\ \text{与}\ \Sigma q_{ij}^2\ \text{是否恒定}} ✓✓$$
$$\textbf{几何读法 ✓}:\ \Sigma_ia_i^2\ \text{度量 }A_1\ \text{个匹配边在 }n\ \text{个坐标方向上的\textbf{分布集中度}};\ \Sigma q_{ij}^2\ \text{度量 }A_2\ \text{个距离 2 对在 }\binom n2\ \text{个坐标对上的分布 ✓}$$
$$\qquad\Longrightarrow\ \text{若其余 9 类存在同 }A_1\ \text{而方向分布不同} \Longrightarrow \textbf{P1-2 PASS} ✓✓\ \text{（如 }A_1{=}8:\ a{=}(8,0,\ldots)\ ⟹ \Sigma a^2{=}64\ \text{vs}\ a{=}(2,2,2,2,0\ldots)\ ⟹ \Sigma a^2{=}16\ ✓）$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 为 **source-first 逐字抽取** ✓（van Wee 式 (5)、nearly-perfect 定义、Lemma 3.18 ✓）；§2 为**两行推导** ✓；§3 为**本机实证** ✓；§4 为**锐化** ✓
- ⚠️ 推导链**模一条外部引理**（$b\le2$ ← Lemma 3.18／Boruchovsky 等 Thm 3 ✓，非自证 ⚠️）—— 若需自足，须自行证明该引理 ✓（下一步候选 ✓）
- **未**声称 P1-2 成立或失败 ✗（锐化后仍未测 ✓）；**未**改动 119 UNKNOWN ✓；**未**碰 $n=10$ 计算 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$n=2^m$ 的 $J_3=0$ 推导链、$A=M/2$ 的证明、P1-2 锐化命题
- **档案已有（引用，不列为提出）**：van Wee 界、nearly-perfect、Lemma 3.18、$b$、$d_1$、$J_3$、matching 定理


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 推导链        命中文件数=22   :: ./C3896-exact-symbolic-T3PASS-certificate.md ./E158-arithmetic-identity-zero-transfer-equivalence-test.md ./V316-C-step4-weak-EL-minimal-hypotheses.md 
技术词 P1-2 锐化命题 命中文件数=1    :: ./ALG-DERIVED-2026-09-27-J3-zero-for-n-2m-and-the-sharpened-P12.md
```
- **本档新增**：$n=2^m$ 的 $J_3=0$ 推导链、$A=M/2$ 的证明、P1-2 锐化命题（见上方命中数；0 命中者为自造语／内部标签 ✓）
