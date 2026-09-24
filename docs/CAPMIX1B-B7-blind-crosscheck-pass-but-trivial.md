已查地图：命中（`CAPMIX1B-B6-dual-scan-closed-by-one-sided-cases`）⟹ 执行其 §6 之 (3)，不开新案
D0: 本档对象 = **`B7` 盲类交叉检验**：`\lambda_{\rm raw}` vs `\lambda_{\rm valid}`（按 blind/non-blind 分表）＋ ⛔**两处口径纠正**（① char 2 下 `D(G)=\varnothing` 使该检验为**恒等**；② `1B` 的 cap 条件是**二维**，`1A` 的 `\lambda_{\rm valid}` **不可平移**）
D1: 1 （新自由度：确立 `1B` 的**正确对应量是 |\text{Valid}|** 而非 `\lambda`；盲类压缩问题被精确定位）
[RESEARCH]

# **`CAP-MIX-1B · B7`：盲类交叉检验（PASS，但为恒等）**

## §1 结果表（照您要求）

```
$$\begin{array}{c|c|c|c|c|c|c|c}
\text{类别}&n&\lambda_{\rm raw}=\lambda_{\rm valid}&\text{零性一致}&\Delta\ne0&\text{cap}&\text{noncap}&|\text{Valid}|>0\\
\hline
\text{blind}&17&17/17&17/17&0&6&11&11\\
\text{nonblind}&22&22/22&22/22&0&12&10&10\\
\text{total}&39&39/39&39/39&0&18&21&21\\
\end{array}$$ ✓✓
$$\Delta\ne0\ \text{列表}=\varnothing\ \Longrightarrow\ \textbf{按您预设 EXIT}:\ \boxed{\texttt{B7-PASS}}$$ ✓
```

## §2 ⛔ 口径纠正一：char 2 下该检验是**恒等**（非新信息）

```
$$\mathrm{char}\,2:\ -1=1\ \Longrightarrow\ \text{退化候选}=\{x=1\ (=-1/2\ \text{同一元素}),\ x=-2=0\}$$
$$x=1:\ \text{需}\ 1+1=0\in G\ \textbf{恒否}\ (G\subseteq\mathbb F_q^\times);\qquad x=0\notin G\ \textbf{恒否}\ \Longrightarrow\ \boxed{D(G)=\varnothing}$$ ✓✓
$$\Longrightarrow\ \lambda_{\rm raw}=\lambda_{\rm valid}\ \textbf{恒成立}\ (\text{与 blind 无关，与参数无关})$$ ✓
$$\textbf{这与 }B3\ \text{的 D 项同源};\ \Longrightarrow\ \textbf{本检验\textbf{不能}作为"全类精确"的证据}$$ ⚠️
```

## §3 ⛔⭐ 口径纠正二：`1B` 的 cap 条件是**二维**，`1A` 的 `\lambda` 机制**不可平移**

```
$$\text{1A（奇特征）}:\ a+b+c=0\ \Longrightarrow\ \text{归一后 } x+y=-1\ \Longrightarrow\ \textbf{一维};\quad \boxed{\lambda_{\rm valid}=0\iff\text{cap}}$$ ✓（`204/204`）✓
$$\text{1B（char 2）}:\ a+b+c+d=0\ \Longrightarrow\ x+y+z+1=0\ (z=1+x+y)\ \Longrightarrow\ \boxed{\textbf{二维}}$$ ✓✓
$$\text{故 }1B\ \text{的对应量是}\ \boxed{|\text{Valid}|}=\#\{(x,y)\in G^2:\text{有效四项关系}\},\qquad \boxed{|\text{Valid}|=0\iff\text{cap}}$$ ✓（**定义级，非压缩**）✓
$$\boxed{\lambda=0\ \textbf{不}蕴含\ 1B\ \text{的 CAP}}$$ ✓（`B4` 已实测反例：`(6,64,9)`：`\lambda=2>0` 且 cap）✓✓
$$\Longrightarrow\ \textbf{您 §EXIT 中"}\lambda_{\rm valid}\ \text{对盲类亦精确}\Longrightarrow\text{全类精确}"\ \textbf{在此不成立（形态不同）}$$ ⚠️
```

## §4 盲类的**真实**缺口（本档精确定位）

```
$$\text{blind}: J_{\rm info}=\varnothing\ \text{（所有 }2^j\bmod d\ \text{皆 }2\text{-幂）}\ \Longrightarrow\ V_\ast=\text{全部 pairs}\ \Longrightarrow\ \textbf{零压缩}$$ ✓
$$\text{实测盲类}:6\ \text{caps}\ (\text{其中 }|\text{Valid}|=0),\ 11\ \text{noncaps}\ (|\text{Valid}|>0)\ \Longrightarrow\ \textbf{盲类的 CAP 判定需另一压缩源}$$ ✓✓
$$\textbf{⟹ 正确的残留问题}:\ \boxed{\text{盲类能否不枚举 pairs 而判定 }|\text{Valid}|=0？}$$ ✓✓
```

## §5 校正后的 `CAP-MIX` 资产链

```
$$\boxed{B4\ \text{充分零判据}\ (\text{解释 }7/7\ \text{单侧零})}\ +\ \boxed{\text{非盲 78/39 的 }V_\ast\ \text{压缩}}\ +\ \boxed{1A\ \text{侧 }\lambda_{\rm valid}\ \text{一维精确}}$$ ✓✓
$$\text{未闭合}:\ (i)\ \text{盲类压缩源};\qquad (ii)\ \lambda>0\ \text{的大容量结构};\qquad (iii)\ (23,89)\ \text{孤立线索}$$ ✓
**【⟹ 不再把 }B7\ \text{当作"全类精确"的证据】** ⚠️
```

## §6 下一步（按您 §末与校正后顺序）

```
**(1)** **盲类压缩源**：`J_{\rm info}=\varnothing` 时，是否存在 `1B` 特有的第二压缩（候选：`\lambda_2` 型**二阶加法 incidence**、或 `F/T` 轨道型必要条件）✓✓
**(2)** `\lambda>0` 的**大容量**结构（`\Theta(d)` 型）✓
**(3)** `(23,89)` 单例 ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**不回 RH** ✓
【数据】 `out/capmix1B7_blind.txt`（39 行）；脚本 `scripts/capmix1B7_blind_crosscheck.py` ✓
【边界】 §1 为实测；§2/§3 为**定义级推导**（`D=\varnothing`、维度差异）；§4 为实测分类 ✓

## §附 【技术词回查】（补录）
```
技术词 validity filter  命中文件数=0    :: 
技术词 blind class      命中文件数=0    :: 
```
