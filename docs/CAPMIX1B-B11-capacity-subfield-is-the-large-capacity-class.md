已查地图：命中（`CAPMIX1B-B10-23-89-isolated-not-a-family`）⟹ 执行其 §6（`B11` 第一刀），不开新案
D0: 本档对象 = **`B11` 大容量结构第一刀**：`\lambda\le d` 审计 ＋ 分层表（`\rho=\lambda/d` vs `r,3\mid d,\text{subfield},\alpha`）⟹ ⭐**`\lambda=d-1\iff G\cup\{0\}` 是子域**（大容量 ⟺ 子域类）
D1: 1 （新自由度：**正向容量判别**（子域刻画）＋ 非子域上界观察 `\rho\le0.381`）
[RESEARCH]

# **`CAP-MIX-1B · B11`：大容量 ＝ 子域类**

## §1 `P1`：`\lambda\le d`（成立，且为**定义级**）

```
$$\lambda=\#\{x\in G:\ 1+x\in G\}\ \text{是 } G\ \text{的子集之基数}\ \Longrightarrow\ \boxed{\lambda\le d}\ \text{恒成立}$$ ✓✓
$$\text{实测违例}=0;\qquad \text{但须标注}:\ \textbf{该上界平凡，不含算术信息}$$ ⚠️
$$\Longrightarrow\ \text{真正的问题不是上界，而是}\ \boxed{\rho:=\lambda/d\ \text{何时为 }\Theta(1)}$$ ✓✓
```

## §2 ⭐⭐⭐ 主结果：`\rho\approx1` **充要于子域类**

```
$$\textbf{实测（}n\le14\text{，全部 }d\ge3\text{）}:$$
$$\begin{array}{c|c|c|c}
\text{分层}&n&\text{mean }\rho&\max\rho\\
\hline
\textbf{子域（Mersenne }d=2^k-1\text{）}&—&\approx1&0.9999\\
\textbf{非子域}&36&0.144&\boxed{0.381}\\
3\mid d&34&0.484&1.0\\
3\nmid d&28&0.422&1.0\\
r=n&44&0.37&1.0\\
r<n&18&0.666&0.992\\
\end{array}$$ ✓✓
$$\rho\ge0.9\ \text{的全部案例}:\ d=15,31,63,127,255,511,1023,2047,4095,8191,16383\ (\textbf{全部 }d=2^k-1)$$ ✓✓✓
$$\Longrightarrow\ \boxed{\text{大容量}\ \rho\approx1\ \Longleftrightarrow\ G\cup\{0\}\ \text{是子域}\ (d=2^k-1)}$$ ✓✓✓
```

## §3 证明（`\Longleftarrow` 方向已可证）

```
$$\text{设 }d=2^k-1\ \text{且}\ k\mid n\ \Longrightarrow\ G=\mathbb F_{2^k}^{\times};\quad \text{对 }x\in G:\quad 1+x\in G\iff 1+x\ne0\iff x\ne1$$ ✓✓
$$\Longrightarrow\ \boxed{\lambda=d-1}\ \text{（精确）};\quad \rho=\frac{d-1}{d}\to1$$ ✓✓
$$\text{实测吻合}:\ d=15\to\lambda=14;\ 63\to62;\ 255\to254;\ 1023\to1022;\ 4095\to4094;\ 8191\to8190;\ 16383\to16382$$ ✓✓
$$\text{几何意义}:\ G\cup\{0\}=\mathbb F_{2^k}\ \text{对整个加法结构封闭}\ \Longrightarrow\ \text{平移 }+1\ \text{几乎不离开 } G$$ ✓
```

## §4 ⭐ 非子域上界观察（本档新增，待证）

```
$$\textbf{实测}:\quad \text{非子域 } d\ \text{的 }\boxed{\max\rho=0.381}\ (\text{36 例}),\quad \text{mean }0.144$$ ✓
$$\Longrightarrow\ \text{猜想（待证）}:\quad d\ne2^k-1\ \Longrightarrow\ \rho\le c_0<1\ (\text{观察 }c_0\approx0.38\approx3/8)$$ ⚠️
$$\text{若成立}:\ \text{大容量现象\textbf{完全}由子域结构解释，}\textbf{无第二来源}$$ ✓✓
```

## §5 分层读数的两条警示（防误读）

```
**(i)** `r<n` 组 `mean ρ=0.666` **不是独立效应** —— Mersenne `d=2^k-1` 的 `r=k` 通常 `<n`，故该组被**子域污染** ⟹ 须**先剔除子域**再比较 `r` ✓
**(ii)** `3\mid d` 与 `3\nmid d` 的 `mean ρ`（0.484 vs 0.422）差异**同样被子域污染**（`d=15,63,255,1023,4095,16383` 皆 `3\mid d` 且皆子域）⟹ `B9` 的 `3\mid d` 边界对大容量**无独立作用**（在子域层之外须重算）✓
**(iii)** `\alpha=d/(q-1)` 与 `\rho` 的相关**尚未剥离**；但子域案例覆盖 `\alpha` 从 `1/(2^{n-k}+1)` 到 `\approx1` 的宽范围而 `\rho\approx1` ⟹ **非密度效应** ✓
```

## §6 `B11` 第一刀判定与下一步

```
$$\boxed{P1\ \text{成立（平凡）};\quad P2\ \text{找到线性容量族}:\ d=2^k-1\Rightarrow\rho=1-1/d\ (c\to1)}$$ ✓✓✓
$$\Longrightarrow\ \text{下一步（真问题）}:\quad \boxed{\text{非子域类能否有 }\rho=\Theta(1)\ (\text{即 }c_0>0\ \text{的线性下界})？}$$ ✓✓
**(1)** 剔除子域后重做 `\rho` vs `r,3\mid d,\alpha` 的分层（**去除污染**）✓✓
**(2)** 攻 §4 的 `c_0\approx0.38`：是否存在 `\rho\le1/2`（或 `3/8`）的**非子域**上界定理 ✓
**(3)** 若 (2) 成立 ⟹ **大容量结构定理**：`\rho=\Theta(1)\iff` 子域类 ⟹ `B11` 收口 ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**不回 RH** ✓
【数据】 `out/capmix1B11_capacity.txt`（全案例逐行）；脚本 `scripts/capmix1B11_capacity.py` ✓
【边界】 §2/§4 为实测（`n\le14`）；§3 为**已证**；§5 的污染警示为新发现 ✓

## §附 【技术词回查】（补录）
```
技术词 capacity         命中文件数=34   :: ./p51-m-tower-framework.md ./E-GATE-and-Lemma-R-R2-CLOSED.md ./p50a-r2-euler-l2-capacity.md 
技术词 subfield         命中文件数=3    :: ./CAPMIX1B-B8-blind-class-is-subfield-class.md ./CAPMIX1B-B11-capacity-subfield-is-the-large-capacity-class.md ./CAPMIX1B-B9-B4-theoremized-with-minimality-audit.md 
```
