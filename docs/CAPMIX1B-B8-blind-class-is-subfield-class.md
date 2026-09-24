已查地图：命中（`CAPMIX1B-B7-blind-crosscheck-pass-but-trivial`）⟹ 执行其 §6 之 (1)，不开新案
D0: 本档对象 = **`B8` 二阶加法 incidence**：`B8`-A **口径纠正**（`N(G)\ne|\text{Valid}|`）＋ ⭐⭐**盲类 ＝ 子域乘法群**（所有加法不变量**只依赖 `d`**）＋ `CAP\iff d\le3`（基数）＋ **EXIT = PASS-A（平凡判据＋结构解释）**
D1: 1 （新自由度：**盲类的完整结构刻画** —— 它由子域结构决定，而非缺压缩源）
[RESEARCH]

# **`CAP-MIX-1B · B8`：盲类 ＝ 子域类**

## §1 ⛔ 口径纠正（`B8`-A 未通过，原因已定）

```
$$\text{您设 }|\text{Valid}|=N(G)=\#\{(x,y)\in G^2:\ 1+x+y\in G\};\qquad \textbf{实测二者不等（39/39）}$$ ✗
$$\text{差异来源（三条退化族）}:\quad x=1\Rightarrow z=y\in G;\quad y=1\Rightarrow z=x\in G;\quad x=y\Rightarrow z=1\in G$$ ✓
$$\text{各贡献 }d\ \text{对};\qquad \text{实测退化差}\ \texttt{I3}-\text{Valid}\in\{7,13,19,25,\dots,277\}\ (\text{量级}\approx3d)$$ ✓✓
$$\Longrightarrow\ \boxed{\text{正确关系}:\ \text{Valid}=N(G)-\#\{\text{三条退化族}\}};\quad \textbf{CAP}\iff \text{Valid}=0\ (\text{非 }N(G)=0)$$ ✓✓
$$\text{注}:\ N(G)\ \textbf{恒}\ >0\ (\text{取 }x=1\ \text{即得})\ \Longrightarrow\ N(G)\ \text{永不指示 CAP}$$ ✓✓
```

## §2 ⭐⭐⭐ 主结果：盲类所有加法不变量**只依赖 `d`**

```
$$\text{实测（17 个 blind 案例）}:\quad (I_2,I_3,\text{Valid},E_2)\ \text{对固定 } d\ \textbf{完全恒定},\ \text{与 } n\ \text{无关}$$ ✓✓✓
$$\begin{array}{c|c|c|c|c|c}
d&I_2=\lambda&I_3=N(G)&\text{Valid}&E_2&\text{cap?}\\
\hline
3&2&7&0&21&\textbf{CAP}\\
7&6&43&24&301&noncap\\
15&14&211&168&3165&noncap\\
31&30&931&840&28861&noncap\\
63&62&3907&3720&246141&noncap\\
\end{array}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{盲类的 }(I_2,E_2)\ \text{不能分离 CAP}:\ I_2\in\{2,6,14,30,62\}\ \text{全}>0},\ \text{而 }6\ \text{例为 CAP}$$ ✓✓（**`I_2` 路线 CLOSED**）
```

## §3 ⭐⭐ 解释：盲类 ＝ **子域乘法群**

```
$$\text{实测 blind 的 }d\in\{3,7,15,31,63\}=\boxed{2^k-1\ (k=2,\dots,6)}$$ ✓✓（**Mersenne / 子域型**）
$$\text{理由}:\ 2^k-1\mid2^n-1\iff k\mid n\ \Longrightarrow\ G=\mathbb F_{2^k}^{\times}\ \text{（子域乘法群）};\ \text{其加法结构完全落在子域 }\mathbb F_{2^k}\ \text{内}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{所有加法 incidence 只依赖 }d=2^k-1\ (\text{即只依赖子域}\ \mathbb F_{2^k})}$$ ✓✓✓ —— **`§2` 的"`d`-only 依赖"由此解释** ✓
$$\text{反向（待证）}:\ \text{blind}\iff d=2^k-1\ (\text{轨道 }\{2^j\bmod d\}\subseteq\{1,2,4,\dots\})$$ ⚠️（本网格成立；一般情形未证）
```

## §4 ⭐ 盲类的 CAP 判据（平凡但完整）

```
$$\text{四点 }x,y,z,1\ \text{须两两相异且全在 }G\ \Longrightarrow\ \text{需}\ |G|\ge4$$ ✓
$$\Longrightarrow\ \boxed{\text{blind 类}:\ \text{CAP}\iff d\le3\iff d=3}\quad(\text{实测 }6\ \text{例 }d=3\ \text{全 CAP},\ d\ge7\ \text{全 noncap})$$ ✓✓
$$\text{即：盲类的 CAP 由\textbf{基数}决定，无需任何 incidence 计算}$$ ✓✓
```

## §5 `B8` 判定（照您 EXIT）

```
$$\boxed{\texttt{PASS-A}\ (\text{存在 }C(G):\ C=0\iff|\text{Valid}|=0)}:\quad C(G):=\ 1\!\!1[d\le3]\ (d=2^k-1\ \text{时})$$ ✓✓
$$\text{但须标注}:\ C\ \text{为\textbf{基数判据}（}d\le3\text{）},\ \textbf{非}深机制;\ \text{真正的结构内容是"盲类}=\text{子域类"}$$ ✓✓
$$\boxed{\text{盲类问题\textbf{闭合}}:\ \text{它不是缺压缩源，而是\textbf{结构退化}（子域）}}$$ ✓✓✓
```

## §6 `CAP-MIX` 收口状态与下一步

```
$$\begin{array}{c|c|c}
\text{项}&\text{结论}&\text{状态}\\
\hline
1A\ \text{奇特征}&R_\ast\ \text{压缩}+\lambda_{\rm valid}\ \text{一维精确（定盲区 126/204）}&CLOSED\\
1A\ \text{角色路线}&\text{重编码}&\text{CLOSED}\\
1B\ \text{非盲}&V_\ast\ \text{二维压缩}\le0.32;\ V_\ast=\text{Valid}\sqcup\text{直线 }z=0&CLOSED\\
1B\ \text{盲类}&\boxed{=\text{子域类};\ (I_2,I_3,\text{Valid},E_2)\ \text{只依赖 }d;\ \text{CAP}\iff d\le3}&CLOSED\\
B4&B4\ \text{充分零判据（解释 }7/7\ \text{单侧零）}&\text{存活资产}\\
(23,89)&\text{孤立线索}&\text{未解释单例}\\
\end{array}$$ ✓✓
$$\textbf{未闭合（真残余）}:\ (i)\ \lambda>0\ \text{的大容量}\ \Theta(d)\ \text{结构};\qquad (ii)\ (23,89)\ \text{单例};\qquad (iii)\ B4\ \text{的定理化}$$ ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**不回 RH** ✓
【数据】 `out/capmix1B8_second_order.txt`（39 行）；脚本 `scripts/capmix1B8_second_order.py` ✓
【边界】 §2–§4 为实测（39 例 / 17 blind）；§3 的"反向"为**待证**；§1 的退化族计数为推导＋实测 ✓

## §附 【技术词回查】（补录）
```
技术词 subfield         命中文件数=0    :: 
技术词 cardinality      命中文件数=5    :: ./V324-E3A-D-relation-depth-irreducible-generation-audit.md ./O5-wording-tightened-and-O2-correspondence-reduction.md ./RESEARCH-CONSTITUTION.md 
```
