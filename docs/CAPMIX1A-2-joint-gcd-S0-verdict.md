已查地图：命中（`CAPMIX1A-1-adversarial-FP-search-and-gcd-structure`）⟹ 执行其 §4 之 (1)(2)，不开新案
D0: 本档对象 = **联合 gcd 实验**（`m=1\to2\to3`）＋ **`\mu` 分类** ＋ **一条已验证引理** ＋ **`\textbf{S0}` 判定**
D1: 1 （延续新自由度；本档给出**第二阶机制的否定判定**与**退化引理的验证**）
[RESEARCH]

# **`CAP-MIX-1A(2)`：联合 gcd → `S0`**

## §1 ⭐ 已验证引理（**458/458 零反例**）

```
$$\boxed{r=p^{\,j}\bmod d\ \text{为 }p\text{-幂}\ \Longrightarrow\ Q_j\equiv0\ (\text{恒等退化})}$$ ✓✓
**【验证】** `QZERO_ok = 458`，`QZERO_bad = 0` ✓✓（**照您预期**）
**【证明（一行，已可得）】** `\mathrm{char}\,p` 下 `(x+1)^{p^i}=x^{p^i}+1=x^{r}+1`；且 `p` 奇时 `p^j+r` 为**偶**（`p` 奇、`r=p^i` 奇）⟹ 符号 `=+1` ⟹ `Q_j=x^r+1-(x^r+1)=0` ✓✓
$$\Longrightarrow\ \textbf{"全 }p\text{-幂轨道"情形下，}\{Q_j\}\ \textbf{整个一阶/二阶闭包为空}:\ \gcd(0,\dots,0,X^d-1)=X^d-1$$ ✓✓
```

## §2 ⭐⭐ 联合 gcd 结果（`m=1\to2\to3`，204 例）

```
$$\textbf{STATS}:\quad \mu=1:3,\qquad \boxed{\mu=2:0},\qquad \mu=3:0,\qquad \text{none}:75,\qquad \text{all-degen}:126$$
$$\qquad \text{jointPASS}=3,\qquad \text{cert\_cap}=3,\qquad \boxed{\text{FP}=0},\qquad \text{cap}=54$$
$$\Longrightarrow\ \textbf{联合 }\gcd\ \text{（}m=2,m=3\text{）}\ \textbf{新增 PASS = 0}$$ ✓✓
**【⟹ 判定】** $$\boxed{\textbf{S0}:\ \text{联合 }\gcd\ \text{没有任何新增 PASS}\ \Longrightarrow\ \textbf{一阶机制确实已经到头}}$$ ✓✓（照您预设的成功标准）
**【结构性解释（本档提出）】** 若"额外根"对**所有**信息型 `j` 共同存在，则 $$\gcd(g_j,g_k)=g_{\text{较小者}}\ (\text{无收缩})\ \Longrightarrow\ \text{相交运算天然无力}$$ ⚠️（**待下一步确诊**）
```

## §3 `\mu` 分类（新量，照您定义）

```
$$\boxed{\mu(p,n,d)=\min\{m:G_m=X-1\}}$$ ✓
$$\begin{array}{c|c|c}
\mu&\text{含义}&\text{本批计数}\\
\hline
1&\text{一阶 Frobenius 证书}&3\\
2&\text{二阶联合机制}&\mathbf{0}\\
3+&\text{更高阶}&0\\
\text{none}&\text{有信息型 }j\ \text{但全不认证}&75\\
\text{blind}&\text{全 }p\text{-幂} \Longrightarrow Q_j\equiv0\ (\text{机制族整体盲})&126\\
\end{array}$$ ✓✓
**【注】** `blind` 类占 **62%** ⟹ **主障碍已确认**：$$\boxed{\text{Frobenius-power orbit}\ \Longrightarrow\ \text{CAP-MIX-1A 整个机制族盲}}$$ ✓✓
```

## §4 反例保护（照您要求）

```
**【做法】** 每个联合 `PASS` 的实例，**独立**重新枚举寻找 AP witness ✓（不共用 truth label）✓
**【结果】** `FP=0` ⟹ **联合版亦零假阳性** ✓✓（作为**实现审计**通过；数学上由 `\gcd=X-1` 自动保证）✓
```

## §5 结论与下一步

```
**【本档净结论】** **(i)** 退化引理已验证（`458/458`）；**(ii)** 二阶联合机制**在这一形式下不成立**（`S0`）；**(iii)** 可靠性维持（`FP=0`）；**(iv)** 主障碍 = `blind` 的 62% ✓✓
**【下一步（诊断，非新计算）】** 确诊"额外根是否对所有 `j` 共同存在"：
$$(a)\ \text{对 "none" 类 75 例算}\ g_\ast=\gcd\{\,g_j\,\};\qquad (b)\ \text{取其 }G\ \text{内根集};\qquad (c)\ \text{检验是否有根 }x\ \text{满足}\ y=-1-x\in G\ (\text{即真 AP})$$ ✓✓
$$\Longrightarrow\ \text{若根为"伪根"（}y\notin G\text{）}\ \text{则机制是\textbf{不完备}而非错误};\ \text{若为真 AP 则这些实例本非 cap}\ (\text{那机制反而更完整})$$ ✓
**【更远一层（若诊断坐实"共同伪根"）】** 需**第三阶对象**（非单纯增加 `j`）：候选为 $$\text{元素级条件}\ y=-1-x\in G\ \text{的显式约束}\quad\text{或}\quad \text{子群内部二次结构}$$ ✓
【⛔ 纪律】 计算仅本实验；`U_{2,3}` 暂停；`T-1` 仍为 calibration ✓
【数据】 `out/capmix1F_joint.txt`；脚本 `scripts/capmix1f_joint_gcd.py` ✓
【边界】 `\mu=2` 的否定仅限**本批 204 例 × 本机制形式**；`blind` 引理已验证但未写成定理文本 ✓

## §附 【技术词回查】（补录）
```
技术词 joint closure    命中文件数=0    :: 
技术词 orbit            命中文件数=89   :: ./grh-goldbach-paper-draft-v2.md ./p39-g1-finite-orbit-moduli.md ./iteration-double-counting-round7.md 
```
