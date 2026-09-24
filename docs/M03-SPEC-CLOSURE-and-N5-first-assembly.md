已查地图：命中（`S2-ZONEB-eight-U-research-5tuple-round1` ＋ `AMEND-19`）⟹ `M03` 规格闭合与 `\mathcal N_5` 首次整理，不开新案
D0: 本档对象 = **`M03` 规格闭合**（对象／等价／归一化／两层 A/B）＋ **`\mathcal N_5` 首次显式整理（含可自证的恒等式与推论）** ＋ **缺口结构设计与 `P1/P2` 形态** ＋ **有限切片设计的陷阱标注**
D1: 1（首次把 `M03` 从"SNIEP } n=5$$"细化到可证链条；产出两条自证恒等式）
[RESEARCH]

# **`M03` 规格闭合 ＋ `\mathcal N_5` 首次整理**

## §1 规格闭合（`P0`）

```
$$\textbf{对象}:\ \text{给定有序实谱 }\lambda=(\lambda_1\ge\lambda_2\ge\dots\ge\lambda_5),\ \text{问是否存在 }A=A^{\mathsf T}\in M_5(\mathbb R),\ A\ge0\ (\textbf{逐元素非负，非 }PSD),\ \operatorname{spec}(A)=\{\lambda_i\}$$ ✓✓
$$\textbf{等价关系}:\ \text{(a) 正尺度同伦 }A\mapsto cA\ (c>0)\Longrightarrow\lambda\mapsto c\lambda;\ \text{(b) 谱排序（下标顺序无意义）}$$ ✓✓
$$\textbf{归一化}:\ \lambda_1>0\ \text{时可固定}\ \boxed{\lambda_1=1};\ \lambda_1=0\Rightarrow\lambda=0\ (\text{零矩阵可实现};\ \text{平凡})$$ ✓✓
$$\Longrightarrow\ \textbf{真正对象}:\ T_5:=\{(\lambda_2,\lambda_3,\lambda_4,\lambda_5)\in\mathbb R^4:\ (1,\lambda_2,\dots,\lambda_5)\in\mathcal S_5\},\quad T_5\subseteq[-1,1]^4\ (\textbf{紧})$$ ✓✓✓
$$\textbf{两层}:\ \boxed{M03\text{-}A}=\mathcal S_5\ (\text{完整 }n=5);\qquad \boxed{M03\text{-}B}=\mathcal S_5^0=\{\lambda\in\mathcal S_5:\ \textstyle\sum_i\lambda_i=0\}$$ ✓✓
$$\textbf{⚠️ trace-zero 的地位（采纳先生）}:\ \text{它\textbf{不是}最小开放核心的既成结论};\ \text{只可作为\textbf{优先构造型子问题}$$ ✓✓
$$\text{（因 }\operatorname{tr}A=\sum_i\lambda_i=0\ \text{＋ }A_{ii}\ge0 \Longrightarrow \boxed{\text{全部 }A_{ii}=0}\ \text{，问题降为无环加权图的谱问题）}$$ ✓✓
```

## §2 `\mathcal N_5` 首次整理（已知必要条件的显式清单）

```
$$\textbf{(N1) Perron／排序}:\ \lambda_1\ge|\lambda_i|\ \forall i;\ \text{归一化后}\ \boxed{-1\le\lambda_i\le1}\ (\text{因 }\lambda_1=1)$$ ✓✓（标准）
$$\textbf{(N2) 迹非负}:\ s_1:=\sum_i\lambda_i=\operatorname{tr}A\ge0\ (\text{对角元非负})$$ ✓✓（标准）
$$\textbf{(N3) 幂和（JLL 型）}:\ s_k:=\sum_i\lambda_i^k=\operatorname{tr}(A^k)\ge0\ \text{对所有 }k\ge1\ (\text{因 }A\ge0\Rightarrow A^k\ge0)$$ ✓✓（标准；偶 }k$$ 自动）
$$\textbf{(N4) ⭐ 自证恒等式（本档新推）}:\ e_2(\lambda)=\sum_{i<j}\lambda_i\lambda_j=\sum_{i<j}\bigl(a_{ii}a_{jj}-a_{ij}^2\bigr)$$ ✓✓✓
$$\qquad \text{推导}:\ e_2=\tfrac12\bigl((\operatorname{tr}A)^2-\operatorname{tr}A^2\bigr);\ (\operatorname{tr}A)^2-\operatorname{tr}A^2=\sum_i a_{ii}^2+2\sum_{i<j}a_{ii}a_{jj}-\sum_i a_{ii}^2-2\sum_{i<j}a_{ij}^2=2\sum_{i<j}(a_{ii}a_{jj}-a_{ij}^2)$$ ✓✓
$$\qquad \textbf{推论}:\ \text{在 }M03\text{-}B\ (\text{对角全 }0)\ \text{下}\ e_2=-\sum_{i<j}a_{ij}^2\le0 \Longrightarrow \boxed{e_2(\lambda)\le0}\ (\text{与 }s_1=0\ \text{合起来等价于 }s_2\ge0)$$ ✓
$$\textbf{(N5) ⭐ trace-zero 的符号强制}:\ s_1=0\ \text{且}\ \lambda\ne0 \Longrightarrow s_2=\operatorname{tr}A^2>0 \Longrightarrow \boxed{\lambda_1>0>\lambda_5}\ (\text{正负必共存})$$ ✓✓（自证）
$$\qquad \text{等价}:\ s_1=0\Rightarrow\ e_2=-\tfrac12 s_2\le0\ (\text{同上});\ \text{且 }\lambda\ \text{不能全非负或全非正}$$ ✓
$$\textbf{(N6) 奇次幂和的图论读数}:\ \text{在 }M03\text{-}B\ \text{下 }s_3=\sum\lambda_i^3=6\sum_{i<j<k}a_{ij}a_{jk}a_{ki}\ (\text{加权三角形计数})\ge0$$ ✓✓（自证：闭合三步游走）
$$\qquad \textbf{推论}:\ s_3=0\iff\text{无加权三角形};\ \text{若图二部}\Rightarrow\text{谱关于 }0\ \text{对称}\Rightarrow s_{\text{奇}}=0$$ ✓✓
$$\textbf{(N7) 待文献补齐（档级，未逐字核）}:\ n=5\ \text{下更强的必要条件}\ (\text{含 }Loewy\text{／}Šmigoc\text{／}Laffey\text{／}Spector\ \text{系列与 }SNIEP\ \text{综述)}$$ ⚠️
$$\qquad \textbf{已知事实（档级）}:\ SNIEP\iff NIEP\ \text{对 }n\le4;\quad \boxed{SNIEP\ne NIEP\ \text{对 }n\ge5}\ (\text{具体例子须核})$$ ⚠️
```

## §3 缺口结构（本档核心）

```
$$\underbrace{\mathcal N_5}_{\text{必要条件（}(N1)\text{–}(N6)\text{＋文献强条件）}}\ \supseteq\ \underbrace{\mathcal S_5}_{\text{可实现}}\ \supseteq\ \underbrace{\text{已知可实现子族}}_{\text{文献给出}}$$ ✓✓
$$\textbf{⚠️ 由 (N7) 的关键后果}:\ \text{既然 }SNIEP\ne NIEP\ \text{对 }n\ge5\ \textbf{已知} \Longrightarrow \textbf{"找一个 }\mathcal N_5\setminus\mathcal S_5\ \text{的例子"可能已被文献完成}$$
$$\qquad \Longrightarrow\ \textbf{目标必须上调为}:\ \boxed{\text{给出\textbf{新的}、可\textbf{独立核验}的不可实现谱族（或收紧必要条件 }N_5\to N_5'\text{）}}$$ ✓✓✓
$$P2\ (\text{构造侧，明确存在}):\ \lambda\in\mathcal S_5\iff\exists A=A^{\mathsf T}\ge0,\ \boxed{\chi_A(x)=\prod_{i=1}^5(x-\lambda_i)}\ \text{（系数＝初等对称多项式，}\lambda\ \text{有理时可\textbf{精确复核}）}$$ ✓✓✓
$$\qquad \text{关键}:\ \text{证书形式 }=\ (\text{矩阵 }A,\ \text{精确算术核验 }A\ge0\ \text{且系数逐项相等})\ ——\ \text{不是数值拟合}$$ ✓✓
$$P1\ (\text{障碍侧，须设计}):\ \text{两条合法形态 ——}$$
$$\qquad \text{(a) }\boxed{\text{新必要条件}}\ (\text{从 }A\ge0\ \text{的结构推出、}e_2/s_3\ \text{型恒等式的加强});\quad \text{(b) }\boxed{\text{精确不可行证书}}\ (\text{方程 }e_i(\lambda)\ \text{固定}＋A\ge0\ \text{的半代数不可行性};\ \text{Positivstellensatz／}SOS\ \text{型证书})$$ ✓✓
$$\qquad \text{（(b) 与资产 }D\ \text{同型：可精确、可独立复核；难度高但形态合法）}$$ ✓
$$\textbf{禁}:\ \text{不得把"已知必要条件很弱"当 }P1;\ \text{不得把"某实例枚举不到"当不可行}$$ ✓✓
```

## §4 有限切片设计的陷阱（须先解）

```
$$\text{陷阱}:\ \text{归一化 }\lambda_1=1\ \text{后 }|\lambda_i|\le1;\ \text{若再要求 }\lambda_i\in\mathbb Z \Longrightarrow \lambda_i\in\{-1,0,1\}\ \text{有限小族} \Longrightarrow \textbf{退化（且大概率全已知）}$$ ⚠️⚠️
$$\Longrightarrow\ \text{切片必须让 }\lambda\ \text{取\textbf{有理非整}值};\ \text{候选规格（择一，待钉死）}:$$
$$\qquad \text{(S-a)}\ \lambda_1=1,\ s_1=0,\ \lambda_i\in\tfrac1d\mathbb Z\ (d\ \text{固定});\qquad \text{(S-b)}\ \lambda_1=1,\ \lambda_5=-1,\ \text{其余自由};\qquad \text{(S-c)}\ \lambda_1=1,\ \lambda\ \text{含三重零点等退化型}$$
$$\textbf{本轮不选};\ \text{须先看文献已知可实现域的形状，再取"贴着已知域边界"的切片（这样 }P1/P2\ \text{才互补）}$$ ✓✓
```

## §5 `AMEND-19` 卡片（更新）

```
$$\begin{array}{c|c}
\text{层}&\text{状态}\\
\hline
P0&\boxed{\textbf{闭合}}\ (n=5,\ \text{实谱},\ \text{对称逐元素非负},\ \lambda_1=1,\ \text{紧 }T_5)\\
\text{归一化}&\boxed{\textbf{可用}}\ (\lambda_1=1;\ \lambda_1=0\ \text{平凡})\\
\text{等价}&正尺度同伦 ＋ 谱排序\\
P1&\textbf{有方向，尚无不可行证书}\ (\text{须设计 (a) 或 (b)})\\
P2&\boxed{\textbf{明确存在}}\ (\text{精确矩阵构造＋系数核验})\\
P3&\text{未到}\\
P4/P5&\text{暂不做}\\
\end{array}$$ ✓✓
$$\Longrightarrow\ \boxed{M03\ \text{维持 }KEEP};\quad \textbf{本轮仍不进入计算}$$ ✓✓
```

## §6 下一刀（纯理论，零计算）

```
$$\boxed{\text{①}}\ \text{把 }(N7)\ \text{的文献强条件补齐，得到显式 }\mathcal N_5\ (\text{含 }n=5\ \text{专用条件})$$ ✓✓
$$\boxed{\text{②}}\ \text{同时把"已知可实现子族"（文献中的 }\mathcal K_5\subseteq\mathcal S_5\ \text{）抄成显式区域}$$ ✓✓
$$\boxed{\text{③}}\ \text{找 }K_5\ \text{与 }N_5\ \text{之间的\textbf{真正缝隙}（贴边切片）},\ \text{再定 (S-a)/(S-b)/(S-c)}$$ ✓✓
$$\boxed{\text{④}}\ \text{切片钉死后才写 }P1/P2;\ \text{再谈计算}$$ ✓✓
【⛔ 纪律】 本轮\textbf{零计算}（不枚举谱、不跑 }SAT$$、不做随机矩阵搜索）；`U_{2,3}` 暂停；**不回 RH**；`C07` 已封口 ✓
【边界】 §2 的 `(N1)`–`(N3)` 为标准事实（档级）；`(N4)`–`(N6)` 为\textbf{本档自证}；`(N7)` 为档级且\textbf{须逐字核} ✓

## §附 【技术词回查】（补录）
```
技术词 SNIEP            命中文件数=6    :: ./S2-HANDOFF-zone-members-and-count-fix.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./S2-ZONEB-eight-U-research-5tuple-round1.md 
技术词 power sum        命中文件数=2    :: ./C3822-E0-multi-moment-feasibility-pivot.md ./C184-M3-damped-certified-0.35-plus-literature-pointer-Littlewood-cosine-sum.md 
```
