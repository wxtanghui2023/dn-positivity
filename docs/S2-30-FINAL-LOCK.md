已查地图：命中（`S2-30-PASS-2-evidence-audit` ＋ `AMEND-16`）⟹ 本档为其**定点核收口（锁档）**，不开新案
D0: 本档对象 = **`S2-30 Final` 锁档**：三条定点核结论（`Po02` 升 `COVERED`；`Gr03` 守 `P1`；`Po06` 守 `U` ＋ 挂 `SPEC-REQUIRED`）⟹ 最终口径 **`C=4,P=17,U=9`**；并登记 `S2` 双向校准样本
D1: 1（首次完成定点核并锁死 S2 口径；产出两条 S2 边界样本）
[RESEARCH]

# **`S2-30 Final`（锁档）**

## §1 最终口径（正式）

```
$$\boxed{\mathbf{C=4,\quad P=17,\quad U=9,\quad N=30}}$$ ✓✓✓
$$\textbf{指标}:\quad \boxed{\text{Direct-cover rate}=\tfrac{4}{30}=13.33\%};\qquad \boxed{\text{survival}=\tfrac{26}{30}=86.67\%}$$ ✓✓
$$\texttt{COVERED}\ \text{四例}:\ Gr05,\ Mt01,\ R03,\ \boxed{Po02}; \qquad Po02\ \textbf{移出池}$$ ✓
```

## §2 `Po02` → `COVERED`（含先生补的技术点）

```
$$\textbf{候选}:\ \mathbb F_2\ \text{上}\ x^n-1\ \text{按不可约因子次数的精确计数}（n\le100）$$
$$\textbf{关键}:\ \text{不是"有没有 }n\le100\ \text{的表"，而是}\textbf{一般定理是否直接给出该 exact proposition};\quad \textbf{答案是是}$$ ✓✓
$$\textbf{特征 2 技术点（先生补）}:\ \text{写}\ n=2^a m\ (m\ \text{奇}),\ \text{则}\ \boxed{x^n-1=(x^m-1)^{2^a}}$$
$$\Longrightarrow\ \text{不同不可约因子集合由 }x^m-1\ \text{决定};\ \text{重数统一 }\times 2^a;\ m\ \text{奇}\ \Longrightarrow\ \text{对 }d\mid m,\ \Phi_d\ \text{的因子次数由}\ \mathrm{ord}_d(2)\ \text{控制};\ \text{数量}=\frac{\varphi(d)}{\mathrm{ord}_d(2)}$$
$$\textbf{按次数计数（不计重数）}:\quad \boxed{N_r(n)=\sum_{\substack{d\mid m\\ \mathrm{ord}_d(2)=r}}\frac{\varphi(d)}{r}};\qquad \text{若计入代数重数则再}\ \times 2^a$$ ✓✓
$$\Longrightarrow\ n\le100\ \text{只是该}\textbf{一般公式}的有限计算，\textbf{不留下独立数学命题}\ \Longrightarrow\ \boxed{COVERED}$$ ✓✓✓
$$\textbf{纪律样本}:\ \boxed{\text{计算工作}\ \ne\ \text{数学新命题}}$$ ✓
```

## §3 `Gr03` 守 `P1`（**不得升级**）

```
$$\textbf{候选}:\ n=11\ \text{图中，}\lambda_{\max}\ \text{的最大可能重数 ＋ 达到者完整极值图分类}$$
$$\textbf{已有（邻接且形式很强）}:\ n\text{-vertex connected graphs 中某特征值重数 }n-2\ \text{或}\ n-3\ \text{的完整分类}（n>6;\ \text{达到者含完全三部图与特定 }\Gamma\ \text{族）}$$ ✓
$$\textbf{但不构成覆盖}:\ \text{三个命题须逐项对应}:\ (i)\ \text{"存在某特征值重数 }n-3";\ (ii)\ \text{"}\lambda_{\max}\ \text{本身达到最大重数}";\ (iii)\ \text{"}n=11\ \text{全部极值图分类"}$$ ✓✓
$$\textbf{档案写法（照先生）}:\ \text{已有覆盖＝某特征值重数 }n-3\ \text{的一般完整分类};\ \textbf{未覆盖＝候选指定的 }n=11,\ \lambda_{\max}\ \text{最大重数及达到者完整图集之间的\textbf{逐字对应}尚未完成}$$ ✓✓
$$\textbf{纪律样本}:\ \boxed{\text{强邻接定理}\ \ne\ \text{exact target covered}}\ \Longrightarrow\ \text{仍记 }P1$$ ✓✓✓
```

## §4 `Po06` 守 `U` ＋ 挂 `SPEC-REQUIRED`

```
$$\textbf{已有}:\ \text{Mann（weight}\le7）;\ \text{Conway–Jones（}\le9）;\ \text{Poonen–Rubinstein（}\le12）;\ \text{现代工作以 Conway–Jones 为基础工具}$$ ✓
$$\textbf{不升级理由}:\ \text{原候选"}\textbf{minimum-weight}\ \text{有限权单位根消和分类"中 }\texttt{minimum-weight}\ \text{未定义}（\text{对固定阶 }N\ \text{的最小非平凡消和？给定约束族的最小支撑？系数受限下的最小 weight？已定义的 cancellation quantity？）$$ ⚠️
$$\Longrightarrow\ \text{仅有"邻接文献存在"，缺}\ \text{Po06 target}\subseteq\text{已分类 exact proposition}\ \text{的证据};\ \textbf{不得为凑 }C\ \text{数强行升级}$$ ✓✓
$$\textbf{依 }AMEND\text{-}16\ \S2:\ \text{该"规格不足"正属 }\boxed{\texttt{SPEC-REQUIRED}}\ \text{触发条件}\ \Longrightarrow\ \text{记为}\ \boxed{U+\texttt{SPEC-REQUIRED}};\ \text{补齐规格后\textbf{重新进入 }S2$$ ✓✓
```

## §5 双向校准样本（正式登记）

```
$$\begin{array}{c|c|c}
\text{样本}&\text{表面形态}&\text{判定}\\
\hline
\boxed{Po02}&\text{"自己做一张 }n\le100\ \text{exact 表"（看起来像可算的新工作）}&\text{一般理论已蕴含}\ \Longrightarrow\ \mathbf{COVERED}\ \text{（计算工作}\ne\text{新命题）}\\
\boxed{Gr03}&\text{已有极强的 }n-3\ \text{分类（看起来该杀）}&\text{未逐字对应}\ \Longrightarrow\ \mathbf{P1}\ \text{保留（强邻接}\ne\text{covered）}\\
\end{array}$$ ✓✓✓
$$\Longrightarrow\ \text{两个样本}\textbf{同时验证} S2\ \text{核心边界未漂移};\ \text{建议纳入 }S2\ \text{常规回归集}$$ ✓✓
```

## §6 状态与下一步

```
$$\boxed{\text{S2-30 Final 锁定}:\ C=4/P=17/U=9;\ Po02\ \text{移出};\ Po06,Gr03\ \text{保留}}$$ ✓✓✓
$$\textbf{本轮不进 (ii)}（照先生"这一轮不进入剩余 70 条"）;\quad \textbf{下一轮}\to (ii)\ \text{剩余 }70\ \text{条 }S2$$
$$\text{规则沿用（已校准）}:\ \text{八列表格};\ C/P_1\text{–}P_4/U\ \text{三态};\ \texttt{SPEC-REQUIRED}\ \text{正交标记};\ \text{不写"没人做过"};\ \textbf{S3 冻结}$$ ✓✓
【⛔ 纪律】 本档零数学计算；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §3/§4 的文献为**档级**（先生本轮引用）；§2 公式为先生所给 ✓

## §附 【技术词回查】（补录）
```
技术词 calibration      命中文件数=22   :: ./MAG1-magnitude-calibrated-and-forced-abscissa.md ./P5-Y3-SOURCE-CARD-and-AMEND9-gate-REJECT.md ./PAPERA-v2-structure.md 
技术词 final            命中文件数=68   :: ./round2-index-status.md ./E140-U1C-exhaustion-audit.md ./kloosterman_fractions.pdf 
```
