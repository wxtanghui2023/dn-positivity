已查地图：命中（`CAPMIX1A-3-three-layer-none75-and-orbit-uniformity`）⟹ 执行其 §6 之 (1)，**并自纠其 §2/§5 的 8 例解读**，不开新案
D0: 本档对象 = **radical 版全 204 例实测**（五项输出）＋ ⛔**自纠**（`case4=8` 不是"重根"，是**退化根**）＋ **分叉判定 = B**
D1: 1 （延续新自由度；本档给出**廉价增益耗尽**的定量判定与**根类型四分**）
[RESEARCH]

# **`CAP-MIX-1A(4)`：radical 版 → 判 `B`（廉价增益已吃完）**

## §1 五项输出（照您指定）

```
$$\textbf{STATS}:\quad \boxed{\text{PASS\_rad}=3},\quad \text{PASS\_alg}=3,\quad \boxed{\text{新增}=0},\quad \boxed{\text{FP\_rad}=0},\quad \text{FP\_alg}=0$$ ✓✓
$$\text{cap}\to\text{rad PASS}=3,\qquad \boxed{\text{noncap}\to\text{rad PASS}=0},\qquad \text{rad}X{-}1\ \text{计数}=8\ (\text{分布于那 3 例的多重 }j),\qquad \text{none\_after\_rad}=75$$
$$\boxed{\delta_j=\deg h_j-\deg\mathrm{rad}(h_j)=0\ \ \text{全部实例}},\qquad \text{delta\_max}=0,\qquad \text{delta\_pos\_cases}=0$$ ✓✓
**【⟹ 第 5 项：8 个 `(X-1)^k` 是否恢复？】** $$\textbf{否 —— 且原因与我上档说法不同（见 §2）}$$ ⚠️
```

## §2 ⛔ 自纠：`case4=8` **不是重根，是退化根**

```
**【上档错误说法】** "8 例为 `(X-1)^k` 重根结构，radical 可修好" ✗
**【实测反驳】** $$\delta_j\equiv0\ \text{（所有 }h_j\ \textbf{无重因子，全部 square-free）}\ \Longrightarrow\ \mathrm{rad}(h_j)=h_j\ \Longrightarrow\ \text{radical 版\textbf{不可能}带来任何增益}$$ ✓✓
**【⟹ 真正解释】** 三档实验中 `case4` 的定义是 `\deg g_*>1,\ N_{\rm true}=0,\ N_{\rm false}=0` ⟹ 额外根既非真 AP、亦非伪根 ⟹ 只可能是**被我分类逻辑排除的"退化根"**：
$$y=1\ (\iff x=-2)\qquad\text{或}\qquad y=x\ (\iff 2x=-1)$$ ✓✓（**这两种 `x` 给不出相异三元组，故既不计 `N_{\rm true}` 也不计 `N_{\rm false}`**）
**【⟹ 更正后的图景（根类型四分）】**
$$\begin{array}{c|c|c}
\text{根类型}&\text{条件}&\text{意义}\\
\hline
\text{平凡}&x=1&\text{始终存在}\\
\text{退化}&x=-2\ \text{或}\ 2x=-1&\textbf{新识别一类（上档漏计）}\\
\text{真根}&-1-x\in G\ (\text{相异})&\text{真 AP}\iff\text{非 cap}\\
\text{伪根}&-1-x\notin G&\text{共同伪根墙}\\
\end{array}$$ ✓✓
```

## §3 分叉判定 = **B**（照您预设）

```
$$\boxed{\text{B}:\ \mathrm{rad}\ \text{只 }3\to3\ (\text{零增益})}\ \Longrightarrow\ \boxed{\textbf{一阶 Frobenius 机制的全部廉价增益已经吃完}}$$ ✓✓
**【⟹ 纪律（照您指示）】** **不再折腾 `\mathrm{rad}^2`、高阶 gcd 等\textbf{同族变体}** ✓✓ **直接进入 24 例伪根墙** ✓
**【同时确认的两条硬结论】**
$$(i)\ \text{可靠性维持}:\ \text{FP}=0\ \text{（rad 与 alg 皆零）};\qquad (ii)\ \text{所有 }h_j\ \text{平方自由}:\ \delta_j\equiv0$$ ✓✓
```

## §4 更新后的三层图景（含自纠）

```
【`none=75` 的真实组成（修正版）】
$$\underbrace{43}_{\text{真根}\iff\text{非 cap}}\ +\ \underbrace{24}_{\text{伪根墙＝机制边界}}\ +\ \underbrace{8}_{\textbf{退化根（非重根）}}$$ ✓✓
【`blind=126`】由已验证引理（`458/458`）解释：`r_j` 全为 `p`-幂 ⟹ `Q_j\equiv0` ✓✓ 不再投入 ✓
```

## §5 下一步（单点，照您裁定）

```
**(1)** **24 例伪根墙**做**结构刻画**：伪根是否落在**少数固定轨道型**（如 `x` 满足低次多项式）⟹ 形成 **"伪根字典"** ✓✓
**(2)** 顺带核对 8 例**退化根**是否**恒为** `x=-2` 与/或 `2x=-1`（若是 ⟹ 完全解释，且 `case4` 永不再出现）✓✓
**(3)** **之后**才做 `CAP-MIX-1B`（char 2 四项）✓
【⛔ 纪律】 计算仅本实验；`U_{2,3}` 暂停；`T-1` 仍为 calibration ✓
【数据】 `out/capmix1H_radical.txt`；脚本 `scripts/capmix1h_radical.py` ✓
【边界】 本档为**实测＋自纠**；`\delta_j\equiv0`、`PASS_{\rm rad}=3`、`FP=0` 均逐字来自 `STATS` ✓

## §附 【技术词回查】（补录）
```
技术词 square-free      命中文件数=6    :: ./kloosterman_fractions.pdf ./V2-35-PQ-are-gcds-not-free-splitting.md ./ref-bc-ar5iv-plaintext.txt 
技术词 degenerate root  命中文件数=0    :: 
```
