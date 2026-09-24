已查地图：命中（`CAPMIX1A-7-decision-table-75-cases`）⟹ 执行其 §6 之 (2)(b)，不开新案
D0: 本档对象 = **加法平移不变量 `\lambda_G` 全 204 对照实验**（`\lambda_{\rm raw}` vs `\lambda_{\rm valid}`）＋ **blind 区 100% 判定** ＋ **与 `R_*` 的交叉实验（同一 incidence locus）** ＋ **"低容量"预期的实测否定**
D1: 1 （延续新自由度；本档确立 **`\lambda_{\rm valid}=0\iff\text{cap}` 在 204 例上精确成立（含全部 126 blind）**）
[RESEARCH]

# **`CAP-MIX-1B`：加法像 `\lambda_G`**

## §1 ⭐⭐ 主结果（`mis_val = 0`）

```
$$\lambda_{\rm raw}=|\{x\in G:-1-x\in G\}|,\qquad \lambda_{\rm valid}=|\{x\in G:-1-x\in G,\ x\ne1,\ -1-x\ne1,\ -1-x\ne x\}|$$ ✓
$$\textbf{STATS}:\quad \text{case}=204,\qquad \boxed{\text{mis\_raw}=23},\qquad \boxed{\boxed{\text{mis\_valid}=0}}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\lambda_{\rm valid}=0\iff G\ \text{是 cap},\quad \textbf{204/204 精确（含全部 126 blind）}}$$ ✓✓✓
**【blind 区完全解决】** $$126=\underbrace{19}_{\text{cap},\ \lambda_{\rm valid}=0}+\underbrace{107}_{\text{noncap},\ \lambda_{\rm valid}\ge1}$$ ✓✓ ⟹ **`J=\varnothing` 的 62% 缺口被加法平移量\textbf{精确盖住}** ✓
**【`\lambda_{\rm raw}` 为何不足（`mis\_raw=23`）】** 退化点（`x=1`、`x=-1/2`）计入 `\lambda_{\rm raw}` 但不产生有效三元组 $$\Longrightarrow\ \textbf{必须按当前 cap 定义扣除退化项（照您提醒）}$$ ✓
```

## §2 ⭐⭐ 与 `R_*` 的交叉实验（**同一点集的两个投影**）

```
$$\textbf{STATS}:\quad \text{cross\_eq}=78,\qquad \boxed{\text{cross\_neq}=0}$$ ✓✓
$$\Longrightarrow\ \textbf{在全部 78 个非盲实例上}:\quad \#\{\text{有效端点在 }R_*\ \text{中}\}=\lambda_{\rm valid}\ \textbf{逐例相等}$$ ✓✓✓
**【⟹ 判定（您的第三问）】** `R_*` **不是**独立机制，而是 **同一 incidence locus 的 Frobenius 过近似**：
$$\text{有效端点}\subseteq R_*\ (\text{因 }x+y=-1\Rightarrow Q_j(x)=0\ \forall j),\qquad \text{且计数逐个相同}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{Frobenius 压缩与加法平移压缩}=\text{同一 AP 关联集的两个投影（非互补机制）}}$$ ✓✓
**【⟹ 二者区别只在\textbf{代价}，不在\textbf{对象}】** `R_*` 或到 `d` 大；`\lambda` 是计数 ✓
```

## §3 ⚠️ "低容量"预期的实测否定（**须记清**）

```
**【实测】** `blind` 的 `\lambda_{\rm raw}` 最大 **727**，`\lambda_{\rm raw}/d` 最大 **0.9875**（即接近整个 `G`）✓
$$\text{例}:\ (3,4,81,80):\ \lambda_{\rm raw}=79,\ \lambda_{\rm valid}=78,\ \lambda/d=0.9875$$ ✓
$$\Longrightarrow\ \boxed{\lambda\ \textbf{不是低容量计数}:\ \text{noncap 侧可有 }\lambda_{\rm valid}=\Theta(d)}$$ ✓✓
**【但要分开看】** $$\begin{cases}\text{cap 侧}:\ \lambda_{\rm valid}=0\ (\text{恒}),\ \lambda_{\rm raw}\ \text{仅由退化点贡献（很小）}\\ \text{noncap 侧}:\ \lambda_{\rm valid}\ \text{可 }\Theta(d)\end{cases}$$ ✓
**【⟹ 结论】** **`\lambda` 的价值是"精确指示器"，\textbf{不是}"压缩"**；若要求廉价求值，须走**角色和/Jacobi 路线**（您已指示**暂不做**）✓✓
```

## §4 二机制系统的真实图景（更新）

```
$$\begin{array}{c|c|c|c}
\text{区}&|\text{规模}&J\ne\varnothing\ \text{侧}&J=\varnothing\ \text{侧}\\
\hline
\text{非盲}&78&R_*\ \text{判定（精确，逐例可查）}&\text{同一对象，}\lambda\ \text{同值}\\
\text{盲}&126&Q_j\equiv0\ (\text{无信息})&\boxed{\lambda_{\rm valid}\ \text{精确判定}} \\
\end{array}$$ ✓✓
$$\Longrightarrow\ \textbf{全 204 例均有精确判定途径};\qquad \text{区别在于\textbf{是否需要 }O(d)\ \text{枚举}}$$ ✓✓
```

## §5 下一步（照您裁定顺序）

```
**(1)** 暂**不做 Jacobi**；先做 `\lambda_{\rm valid}\to\text{低容量版}` 的**最小问题**：$$|\lambda_{\rm valid}-\tfrac{d^2}{q}|\ \text{的界（随机模型基线）能否给出 }\lambda_{\rm valid}=0\ \text{的充分条件}$$ ✓✓
**(2)** 独立于 (1)：**退化点的算术刻画**（`x=1`、`x=-1/2`、`x=-2` 何时落在 `G`）—— 因 `\lambda_{\rm raw}` 的 23 处误判全由它们造成 ✓
**(3)** 之后才做 `CAP-MIX-1B` 的 char 2 四项版 ✓
【⛔ 纪律】 统一口径（`126+3+75` / `204=\text{blind}+\text{nonblind}`）；计算仅本实验；`U_{2,3}` 暂停 ✓
【数据】 `out/capmix1L_lambda.txt`（blind 126 行 ＋ nonblind 78 行，含 `\lambda_{\rm raw},\lambda_{\rm valid},\lambda/d,m,\mathrm{ord}_d(p),\gcd(d,p-1)`）；脚本 `scripts/capmix1L_lambda_additive.py` ✓
【边界】 §1 的精确性为**本批 204 例实测**；`\lambda_{\rm valid}=0\iff\text{cap}` 的**证明**仍未写出（等价式已在推导层）✓

## §附 【技术词回查】（补录）
```
技术词 translation      命中文件数=19   :: ./p141-bridge-obstruction.md ./O3-mechanism-audit-and-ontology.md ./C3-TL-verified-and-Zomega-structure.md 
技术词 autocorrelation  命中文件数=2    :: ./MATH-STATEMENT-A-offdiagonal-second-moment-beyond-support-1.md ./R-A8.2-precision-gap-audit.md 
```
