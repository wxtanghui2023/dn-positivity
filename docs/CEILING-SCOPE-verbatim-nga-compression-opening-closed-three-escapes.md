# 🎯 **核 `0.6818287` 的范围**：换压缩族**不开**（类级定理）—— 但定义**写出三条逃逸**，其一为新

> 依唐先生 14:24「继续」；承接 `64f71a2` §6(v)（未核项）✓
> **本档结果**：① 我的"换压缩族"开口 **CLOSED** ✗；② 天花板定义**逐字给出三条逃逸**，其中 **(c) 为新发现** ✓✓✓

---

## §1 ⭐⭐⭐ 逐字定义（`clean.txt` L1307--1311）
$$\text{"Call a}\ \textbf{bandwidth-one certificate}\ \text{any function}\ p\ \text{of a locally finite,}\ \rho\mapsto1-\bar\rho\text{-symmetric configuration that}$$
$$\qquad\textbf{(a)}\ \text{depends on the configuration}\ \textbf{only through its first two trace moments}\ \text{against test functions of}\ \textbf{Fourier support in}\ [-1,1]$$
$$\qquad\qquad\textbf{and the partition into on-line points and off-line pairs},\ \text{and}$$
$$\qquad\textbf{(b)}\ \text{satisfies}\ p\le N^s_0/N\ \text{configuration by configuration."}✓✓✓$$

## §2 天花板是**类级**的（Lean 核验）
$$\text{L70--71 逐字}：\text{"among windows}\ \psi\ \text{..., this is optimal}\ [\text{CCLM17, Cor. 14}].\ \text{The ceiling over the}\ \boxed{\textbf{broader class of all bandwidth-one certificates}}\ \text{is approximately}\ 0.682"✓✓$$
$$\text{L1329}：p_0\le0.6818287\ \text{（精确有理数，}\ \text{Lean 定理}\ \texttt{PairCeiling.ceiling\_law256}\ \text{＋}\ \texttt{EnclOK}\ \text{区间算术）}✓✓$$
$$\Longrightarrow \boxed{\text{我的"换压缩族"开口}\ \textbf{CLOSED}}✗✗\qquad(\text{因定义 (a) 只允许经}\ \textbf{两个矩＋划分} \text{依赖，}\ \text{与族的选择无关})✓✓$$

## §3 ⭐⭐⭐ 但定义 (a)(b) **逐字写出三条逃逸**
$$\textbf{逃逸 ①}\ \textbf{用多于两个矩} \Longrightarrow \S7.2(e)\ \text{逐字}：\text{"at}\ X\asymp T\ \text{this allows only}\ k=1.\ \text{Thus, unconditionally, higher moments add nothing"}\ ✗✓$$
$$\textbf{逃逸 ②}\ \textbf{Fourier support}>1 \Longrightarrow \text{需 prime pairs}\ \Longrightarrow \textbf{SUPPORT-1}\ ✗✓$$
$$\textbf{逃逸 ③}\ ⭐\ \textbf{依赖粒度超过"划分"本身}：\text{定义 (a) 只允许经}\ \boxed{\text{"the partition into on-line points and off-line pairs"}} \text{依赖}$$
$$\qquad \Longrightarrow \ \text{利用离线集的}\ \textbf{更细结构} \text{（而非仅其计数／划分）的证书，}\ \textbf{不在天花板范围内}✓✓✓$$
$$\qquad 📌\ \text{此前}\ \textbf{未注意到}\ \text{这一条；}\ \text{它是本次核验的}\ \textbf{新产出}✓✓$$

## §4 ⟹ 具体新目标（可命名）
$$\boxed{\textbf{目标 P-part}：\text{构造一个利用}\ \textbf{on-line/off-line 划分的更细结构} \text{（非仅计数）的证书}}✓✓✓$$
$$\qquad \text{要求同时}：\text{(i) 只经}\ \text{support}\le1\ \text{数据}；\ \text{(ii) 不增加矩阶（}\le2\text{）；}\ \text{(iii) 依赖粒度}\ >\ \text{"划分"}✓✓$$
$$\qquad \text{若存在且给出}\ >0.6818287 \Longrightarrow \textbf{前沿类级天花板被突破}✓✓✓$$
$$\qquad ⚠️\ \text{前沿自陈（L162 逐字）}：\boxed{\text{"the zeros are not shown to be off the line, merely not reached by the certificate"}}✓✓$$
$$\qquad\qquad \Longrightarrow \ \text{他们}\ \textbf{自己} \text{承认是}\ \textbf{证书的可达性} \text{问题，}\ \text{不是零点问题}✓✓$$

## §5 边界
$$\text{(i)}\ §1--§3\ \text{全部逐字（行号见}\ \texttt{zeta23\_2608.13637.clean.txt}）✓✓\quad\text{(ii)}\ §4\ \text{为目标提案，}\ \textbf{未证}✓$$
$$\text{(iii)}\ ⚠️\ \text{EnclOK 的区间算术}\ \textbf{未由 Lean kernel 检查}（\text{前沿自陈），}\ \text{故}\ 0.6818287\ \text{为}\ \text{条件性类级定理}✓✓$$
$$\text{(iv)}\ \textbf{未用 RH}；\ \textbf{零计算}✓$$
