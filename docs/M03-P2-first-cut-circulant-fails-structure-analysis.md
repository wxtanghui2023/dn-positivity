已查地图：命中（`M03-3cA-JMP-interlacing-CLOSED-no-new-exclusion`）⟹ `P2` 第一刀（结构族构造），不开新案
D0: 本档对象 = ⭐**`P2` 第一刀**：循环（circulant）构造的精确解与判定（**FAIL，`c_2<0` 恒成立**）＋ **循环可实现边界解析式** ＋ ⭐**结构分析**（重数型 `1,2,2` 强制对称性 ⟹ 各自然族的重数谱）＋ 下一步选项
D1: 1（首次尝试 `S` 内的构造性实现；产出循环族精确解与结构障碍诊断）
[RESEARCH]

# **`P2` 第一刀：循环构造失败 ＋ 结构分析**

## §1 为什么先试循环族

```
$$\text{本族谱型}\ (1,t,t,-s,-s)\ \text{的重数结构}\ \boxed{1,2,2}\ \text{恰为}\ \textbf{循环矩阵}\ \text{的谱型}（\text{顶点传递};\ C_5\ \text{邻接谱}=(2,u,u,v,v)）$$ ✓✓
$$\text{对称非负循环}: \operatorname{circ}(c_0,c_1,c_2,c_2,c_1),\ c_i\ge0;\quad \mu_0=c_0+2c_1+2c_2,\ \mu_1=c_0+uc_1+vc_2,\ \mu_2=c_0+vc_1+uc_2$$
$$\qquad u=2\cos72^\circ=\tfrac{\sqrt5-1}2,\qquad v=2\cos144^\circ=-\tfrac{\sqrt5+1}2$$ ✓
$$\text{反解 }(c_0,c_1,c_2):\qquad c_0=\tfrac{-2\varepsilon+9t-4}{5};\quad c_1=\tfrac{(1+\sqrt5)\varepsilon}{10}-\tfrac{\sqrt5 t}{4}-\tfrac{9t}{20}+\tfrac{9+\sqrt5}{20};\quad c_2=\tfrac{(1-\sqrt5)\varepsilon}{10}+\tfrac{\sqrt5 t}{4}-\tfrac{9t}{20}+\tfrac{9-\sqrt5}{20}$$ ✓✓（sympy 精确）
```

## §2 判定：**FAIL**（`c_2<0` 恒成立）

```
$$\text{在 }S\ \text{内 12 样点}:\ c_0\in(0.064,0.092)>0,\quad c_1\in(0.493,0.517)>0,\quad \boxed{c_2\in(-0.054,-0.036)<0}\ \textbf{恒成立}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\text{循环构造在 }S\ \text{上\textbf{完全失效}}}（\text{不是逼近差一点，而是符号固定为负}）$$ ✓✓
$$\text{循环可实现边界}（c_2=0）:\ \text{解 }\varepsilon\ \text{得}\ \varepsilon_{\rm circ}(t)\approx-0.485\ (t=0.45)\ \Longrightarrow\ \textbf{远在条带下方}（S\ \text{内 }\varepsilon\in(-0.2,-0.1226)）$$ ✓✓
$$\qquad \Longrightarrow\ \text{循环族只实现"更深负谱"区};\ \text{与 JMP Fig.1 所述"circulant line = line 3，可实现区在其一侧"完全一致}$$ ✓✓（**两处独立吻合**）
$$\textbf{不得写}:\ \text{"}S\ \text{不可实现"};\ \text{正确}:\ \textbf{循环构造族在 }S\ \text{上失效}$$ ✓✓
```

## §3 ⭐ 结构分析（本档其余价值）：重数型 `1,2,2` 强制对称性

```
$$\text{要在 }S\ \text{内实现，矩阵必须保持}\ \lambda_2=\lambda_3,\ \lambda_4=\lambda_5\ (\text{两个二重特征值}) \Longrightarrow \text{结构受限};\ \text{各自然族的重数谱}:$$
$$\begin{array}{c|c|c}
\text{族} & \text{参数数} & \text{重数谱}\\
\hline
\text{循环（}D_5\text{ 不变）} & 3 & \boxed{1,2,2}\ \checkmark\ \text{但 }c_2<0\ \textbf{FAIL}\\
S_3\times S_2\text{ 不变} & 5 & 2,1,1,1\ ✗\\
S_4\text{（含固定点）不变} & 3 & 1,1,3\ ✗\\
\mathbb Z_2\text{ 对合 }(12)(34)\text{ 不变} & \textbf{9（勘误：原记 10，实为 9）} & 2+3\ \text{分解};\ \text{可经}\ \textbf{2 条条件}\ \text{逼出}\ 1,2,2\ \checkmark\ \text{待搜}\\
\text{块对角 }\operatorname{diag}(B_4,t) & — & 1,2,2\ \checkmark\ \text{但仅 }y=0\ (\text{可约})
\end{array}$$ ✓✓
$$\Longrightarrow\ \textbf{可用候选}:\ \mathbb Z_2\text{-不变族}（10\ \text{参数},\ 2\ \text{条件}:\ \text{奇部为标量}＋\text{偶部判别式}=0）\ \text{维数计数充足} \Longrightarrow \text{存在性可能，但需搜索}$$ ✓✓
$$\text{另注}:\ \text{块对角}\ \operatorname{diag}(B_4,t)\ \text{在 }y=0\ \text{处已具 }1,2,2\ \text{型};\ \textbf{向 }y>0\ \text{的扰动必须\textbf{保持重数}} \Longrightarrow \text{扰动不能破坏对称性}$$ ✓✓✓
```

## §4 下一步选项（按代价排序）

```
$$\boxed{\text{(i)}}\ \mathbb Z_2\text{-不变族的\textbf{有界搜索}}:\ 10\ \text{参数},\ \text{目标谱 }(1,t,t,-s,-s)\ \text{于 }S\ \text{内},\ \text{有理点优先}$$
$$\qquad \text{成功} \Longrightarrow \textbf{可实现新点}（P2\ \text{PASS}）;\ \text{失败} \Longrightarrow \text{登记该族 CLOSED}$$
$$\boxed{\text{(ii)}}\ \text{二阶扰动分析}:\ \text{以 }\operatorname{diag}(B_4,t)\ \text{为基},\ \text{在保持重数的切空间内求可行方向}$$ ✓
$$\boxed{\text{(iii)}}\ \text{若两路皆阻} \Longrightarrow \textbf{结构障碍候选}（\text{供 }(3d)\text{）}:\ \text{"}S\ \text{内实现需保持 }1,2,2\ \text{重数}＋\text{非负}\Longrightarrow \text{与已知族冲突"}}$$ ✓✓
【⛔ 纪律】 本轮为**解析计算＋结构分析**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1/§2 为 sympy 精确解＋12 样点核验；§3 的重数谱为结构计算（非定理）；**不得**由单一族失效推出 `S` 不可实现 ✓

## §附 【技术词回查】（补录）
```
技术词 circulant        命中文件数=5    :: ./C292-four-deep-audit-receipts-and-C290-errata.md ./C325-Barker-cross-object-mechanism-ontology-audit.md ./C324-C323-closure-Mahler-chain-archived-pivot-to-next-external-problem.md 
技术词 multiplicity     命中文件数=36   :: ./grh-goldbach-paper-draft-v2.md ./E20-E40-zero-density-2026-read.md ./p49-phase-diagram-summary.md 
```
