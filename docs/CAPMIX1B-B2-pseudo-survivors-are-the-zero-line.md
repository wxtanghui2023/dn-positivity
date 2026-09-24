已查地图：命中（`CAPMIX1B-B1-char2-fourterm-survivor`）⟹ 执行其 §7 之 (ii)（`B2`），不开新案
D0: 本档对象 = **`B2` 伪 survivor 分类**：⭐**伪 survivor 全部落在直线 `z=0` 上**（`388/388`）⟹ **`B1`-D 单侧升级为双向** ＋ 三条假设的**实测判决**
D1: 1 （新自由度：`V_\ast=\text{Valid}\sqcup(\text{直线 }z=0)`，判定机制**精确化**）
[RESEARCH]

# **`CAP-MIX-1B · B2`：伪 survivor ＝ 零线**

## §1 ⭐⭐⭐ 主结果

```
$$\textbf{STATS}:\quad \text{case}=39,\quad |V_\ast|_{\rm tot}=15484,\quad \boxed{|P_\ast|_{\rm tot}=388},\quad \boxed{\texttt{z\_zero}=388}$$ ✓✓✓
$$\Longrightarrow\ \textbf{每一个伪 survivor 都满足}\ \boxed{z=1+x+y=0}\quad(\text{即}\ y=1+x)$$ ✓✓✓
$$\Longrightarrow\ \boxed{P_\ast\subseteq\{\,x+y=1\,\}\ (\text{直线})}\quad\text{且因 }0\notin G\ \text{自动非 VALID}$$ ✓
**【⟹ `B1`-D 升级为双向（本档核心）】** $$\boxed{(x,y)\in V_\ast\ \text{且}\ z=1+x+y\ne0\ \Longrightarrow\ (x,y)\ \text{是有效四项关系}}$$ ✓✓✓
$$\text{i.e.}\quad \boxed{V_\ast\setminus\{z=0\}=\text{Valid}}$$ ✓✓（等价式：`CAP ⟺ V_\ast\subseteq\{z=0\}`）✓✓✓
```

## §2 ⭐ 与 `1A` 的意外交汇

```
$$\text{直线 }\cap G^2=\{(x,1+x):\ x\in G,\ 1+x\in G\}=\text{1A 的加法像集}\ G\cap(1+G)$$ ✓✓
$$\Longrightarrow\ \textbf{1B 的残余对象正是 1A 的加法 incidence};\ \text{两分支在"平移}"处\textbf{对接}$$ ✓✓
**【结构意义】** `z=0` 时 `Q_j(x,1+x)=x^{r}+(1+x)^{r}+1`，而 `(x+y)^r=1` ⟹
$$\boxed{\text{直线条件}\iff\textbf{`r`-次幂映射的加法缺陷在该对 `(x,y)` 上消失}}$$ ✓✓（即 `x^{r}+y^{r}=(x+y)^{r}`）
```

## §3 三条假设的实测判决（照您 §3–§5）

```
$$\begin{array}{c|c|c}
\text{假设}&\text{实测}&\text{判决}\\
\hline
\text{伪 survivor 是完整 Frobenius 轨道之并?}&\text{orbit\_full}=30/30,\ \text{partial}=0&\textbf{成立}\ \checkmark\\
y=x^{2^k}\ (\text{`x,y` Frobenius 互换})?&y\_in\_orbit\_of\_x=76/388\ (\textbf{20\%})&\textbf{不是主机制}\ \times\\
\text{真子域 }x,y\in\mathbb F_{2^k},k<n?&k_x<n:\ 242/388\ (\textbf{62\%})&\textbf{部分成立}\ \triangle\\
\mathop{\mathrm{ord}}(z)\ \text{分层？}&z\equiv0\ \Longrightarrow\ \mathrm{ord}(z)\ \text{未定义}\ (388/388)&\textbf{提问失效（`z=0` 恒）}\ \times\\
\end{array}$$ ✓✓
$$\text{轨道长度直方图}:\ \{2{:}20,\ 3{:}20,\ 4{:}12,\ 5{:}18,\ 6{:}18,\ 8{:}3,\ 9{:}2\}\quad(\text{全为 }n\ \text{的因子})$$ ✓
$$\text{二维度分布 }k:\ \{2{:}40,3{:}60,4{:}48,5{:}90,6{:}108,8{:}24,9{:}18\}$$ ✓
```

## §4 ⛔ 自纠/边界

```
**【`\mathrm{ord}(z)` 分析失效】** 您的 §5 设想 `z\ne0`（需按 `\mathrm{ord}(z)\mid d`／子域／一般三类分层）；实测 **`z=0` 恒成立（`388/388`）** ⟹ 该分层**不适用**，改由"直线"解释 ✓（**又一次"结果异常先查自己"**）✓
**【`P_\ast` 的定义性说明】** `P_\ast:=V_\ast\setminus\text{Valid}` 是**定义** ⟹ `|V_\ast|=|\text{Valid}|+|P_\ast|` 为恒等；但"**全部 `P_\ast` 落在 `z=0`**"**不是恒等**，是**实质发现** ✓✓
**【`orbit_full`】** 30 = 有 `P_\ast\ne\varnothing` 的案例数 ⟹ 该 30 例**全部**为完整轨道之并 ✓
```

## §5 `B2` 判定：**UPGRADE**（照您的 EXIT 条件）

```
$$\boxed{P_\ast=\{\,x+y=1\,\}\cap G^2\cap\{Q_j=0\ \forall j\in J_{\rm info}\}\quad(\textbf{有限结构族：直线})}$$ ✓✓
$$\Longrightarrow\ \boxed{V_\ast=\text{Valid}\ \sqcup\ P_{\rm explicit}}\quad\textbf{已成立}$$ ✓✓✓
$$\Longrightarrow\ \textbf{`B1` 由"单侧 CAP 证书"升级为\textbf{精确判定机制}}:\quad CAP\iff V_\ast\subseteq\{z=0\}$$ ✓✓✓
```

## §6 下一步

```
**(1)** 把直线条件**代数化**：$$\{(x,1+x)\in G^2\}\cap\{x^{r}+(1+x)^{r}+1=0\ \forall r\in J_{\rm info}\}\ \text{的显式刻画}$$ ✓（下一步）
**(2)** 与 `1A` 对接：直线 `\cap G^2` 即 `1A` 的加法像集 ⟹ 试看两分支能否共用同一"平移"机制 ✓✓
**(3)** 盲类（`17/39`）仍暂放（照您指示）✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停 ✓
【数据】 `out/capmix1B2_pseudo.txt`（39 行）；脚本 `scripts/capmix1B2_pseudo_survivor.py` ✓
【边界】 §1 的 `388/388` 为实测；§2 的交汇为**结构推导＋集合等式** ✓

## §附 【技术词回查】（补录）
```
技术词 zero line        命中文件数=0    :: 
技术词 additive defect  命中文件数=1    :: ./CAPMIX1B-B1-char2-fourterm-survivor.md 
```
