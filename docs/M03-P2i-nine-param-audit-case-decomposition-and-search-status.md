已查地图：命中（`M03-P2-first-cut-circulant-fails-structure-analysis`）⟹ `P2(i)` 参数审计＋三情形分解＋搜索状态，不开新案
D0: 本档对象 = ⭐**参数维度硬性修正（`10\to9`）** ＋ **`\mathbb Z_2` 分解与全部重构公式的精确核验** ＋ **三情形（`I/II/III`）判定**（`III` CLOSED；`I` 迹条件不杀）＋ **`Case II` 搜索状态（无穿透；搜索受限，非 FAIL）** ＋ ⭐**新必要条件 `y\le t`**（迹预算）
D1: 1（首次给出 `Z_2` 族的精确情形分解与 `Case II` 的迹预算必要条件）
[RESEARCH]

# **`P2(i)`：`9` 参数审计、情形分解、搜索状态**

## §1 参数维度硬性修正（采纳先生）

```
$$\textbf{一般 }(12)(34)\text{-不变实对称阵}:\ A=\begin{pmatrix}a&b&c&d&e\\ b&a&d&c&e\\ c&d&f&g&h\\ d&c&g&f&h\\ e&e&h&h&i\end{pmatrix},\quad a,b,c,d,e,f,g,h,i\ge0 \Longrightarrow \boxed{9\ \text{参数}}$$ ✓✓✓
$$\text{（sympy 计数 }=9;\ \textbf{原档记 }10\ \text{为误，已勘误修正）}$$ ✓
$$\text{正交基}: u_1=\tfrac{e_1-e_2}{\sqrt2},\ u_2=\tfrac{e_3-e_4}{\sqrt2};\quad v_1=\tfrac{e_1+e_2}{\sqrt2},\ v_2=\tfrac{e_3+e_4}{\sqrt2},\ v_3=e_5\quad (\textbf{逐对正交性已核验})$$ ✓✓
$$A\sim B_{\rm odd}\oplus Q_{\rm even};\quad B_{\rm odd}=\begin{pmatrix}a-b&c-d\\ c-d&f-g\end{pmatrix};\quad Q_{\rm even}=\begin{pmatrix}a+b&c+d&\sqrt2e\\ c+d&f+g&\sqrt2h\\ \sqrt2e&\sqrt2h&i\end{pmatrix}$$ ✓✓✓（与先生逐项一致）
$$\textbf{非负性}\iff Q_{11}\ge|B_{11}|,\ Q_{22}\ge|B_{22}|,\ Q_{12}\ge|B_{12}|,\ \text{且 }Q_{13},Q_{23},Q_{33}\ge0$$ ✓✓
$$\textbf{全部重构公式已逐一核验为恒等}:\ a=\tfrac{Q_{11}+\alpha}2,\ b=\tfrac{Q_{11}-\alpha}2,\ f=\tfrac{Q_{22}+\gamma}2,\ g=\tfrac{Q_{22}-\gamma}2,\ c=\tfrac{Q_{12}+\beta}2,\ d=\tfrac{Q_{12}-\beta}2,\ e=\tfrac{Q_{13}}{\sqrt2},\ h=\tfrac{Q_{23}}{\sqrt2},\ i=Q_{33}$$ ✓✓✓
```

## §2 三情形判定

```
$$\text{目标谱 }\{1,t,t,-s,-s\};\quad 2\times2\ \text{的 }B_{\rm odd}\ \text{必须吃掉两个二重位置} \Longrightarrow \text{仅三情形}$$ ✓
$$\textbf{Case III}:\ B_{\rm odd}=\{t,t\}\Rightarrow\alpha=\gamma=t;\ Q=\{1,-s,-s\}\Rightarrow\operatorname{tr}Q=1-2s;\ \text{而 }S\ \text{内 }s>\tfrac{1+t}2>\tfrac12\Rightarrow\operatorname{tr}Q<0$$ ✓
$$\qquad \text{与 }Q\ge0\ (\text{entrywise})\Rightarrow\operatorname{tr}Q\ge0\ \textbf{矛盾} \Longrightarrow \boxed{\text{Case III CLOSED on }S}$$ ✓✓✓（与先生一致）
$$\textbf{Case I}:\ B_{\rm odd}=-sI_2\Rightarrow\alpha=\gamma=-s;\ \text{支配}\Rightarrow a+b=Q_{11}\ge s,\ f+g=Q_{22}\ge s;\ \operatorname{tr}Q=1+2t\Rightarrow2s\le1+2t$$ ✓
$$\qquad \text{但 }S\ \text{内 }s>\tfrac{1+t}2,\ \text{而 }\tfrac{1+2t}2-\tfrac{1+t}2=\tfrac t2>0 \Longrightarrow \textbf{该条件不杀 Case I}$$ ✓✓✓（与先生一致）
$$\qquad \text{状态}:\ \text{Case I \textbf{未 CLOSED}（需另找约束或搜索）}$$
```

## §3 新必要条件（本档自推，来自迹预算）

```
$$\textbf{Case II 在 }Z_2\ \text{族内}:\ \alpha+\gamma=t-s,\quad Q_{11}+Q_{22}+Q_{33}=1+t-s\quad(\text{因 }Q\ \text{谱}=\{1,t,-s\})$$ ✓
$$\qquad \text{支配}\Rightarrow Q_{11}+Q_{22}\ge|\alpha|+|\gamma|\ge|\alpha+\gamma|=|t-s|\quad(\text{此处 }s>t\Rightarrow=t-s)$$ ✓
$$\Longrightarrow\ \boxed{Q_{33}=i\ \le\ \frac{1+t}{2}-\delta-\frac{1-t}{2}-\delta\ =\ t-2\delta}\quad\Longrightarrow\ \boxed{\delta\le\tfrac t2}\quad\text{即}\quad \boxed{y=2\delta\le t}$$ ✓✓✓
$$\textbf{在 }S\ \text{上核验}:\ y<4-8t\ \text{且}\ 4-8t\le t\iff t\ge\tfrac49\ (\text{恰为 }S\ \text{左端点}) \Longrightarrow \textbf{必要条件在 }S\ \text{上自动满足}$$ ✓✓
$$\qquad \text{（一致性检验通过；}\textbf{非}新排除，但为 }Z_2\text{-}Case\ II\ \text{的\textbf{结构性必要条件}）$$ ✓✓
```

## §4 `Case II` 搜索状态（严格分档）

```
$$\text{搜索(第一轮，}4\text{ 参数 }(\theta,\ \text{三个 Givens 角})\text{)}:\ S\ \text{内 }12\ \text{个 }(t,s)\ \text{点}\ \Longrightarrow\ \boxed{\Phi_{\min}>0\ \text{处处成立}};\ \text{值域 }5.9\times10^{-4}\sim7.3\times10^{-2}$$ ✓✓
$$\qquad \text{越靠近边界 }\eta\to0^+\ (\text{即 }\delta\to0^+),\ \Phi_{\min}\ \text{越小}\ (\approx0.4\eta)\ \Longrightarrow \textbf{优化器在边界附近可靠性不足}$$ ⚠️
$$\text{第二轮（特征向量参数化）因运行时间过长被中止} \Longrightarrow \text{未获得更精细数据}$$ ⚠️
$$\textbf{按先生验收标准分档}:\ \text{PASS}?(\Phi=0\ \text{精确点})\ \textbf{未达};\ \text{CONDITIONAL PASS}?\ \textbf{未达};\ \text{FAIL}?(\text{需解析下界 }\Phi\ge F>0)\ \textbf{未达}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{当前状态}=\textbf{未找到穿透；搜索受限；尚无解析下界}}$$ ✓✓
$$\textbf{不得写}:\ \text{"}Z_2\text{-Case II 不能穿透"}\ (\text{缺解析下界});\ \text{亦不得写"穿透成功"}$$ ✓✓
```

## §5 边界结构（为下一刀的一阶分析准备）

```
$$\text{边界 }\delta=0\ (y=0)\ \text{处}:\ \text{第 5 顶点孤立}\Rightarrow e=h=0\Rightarrow Q=\begin{pmatrix}Q_{11}&Q_{12}&0\\ Q_{12}&Q_{22}&0\\ 0&0&i\end{pmatrix}$$ ✓
$$\qquad \Longrightarrow Q\ \text{的谱}=\sigma(2\times2)\cup\{i\};\ \text{Case II 需 }\{1,t,-s\}\Rightarrow i\in\{1,t\}\ (\text{因 }i\ge0,\ -s<0)$$ ✓
$$\qquad \text{取值 }i=t:\ 2\times2\ \text{谱}\{1,-s\};\quad B_{\rm odd}\ \text{谱}\{t,-s\} \Longrightarrow \textbf{边界配置可解}（可约实现 ✓）$$ ✓✓
$$\text{奇块 vs 偶块（2×2 对 2×2）：}\ \text{偶块（谱}\{1,-s\}\text{）须\textbf{逐项支配}奇块（谱}\{t,-s\}\text{）的绝对值};\ \text{各由 1 个角度参数化};\ 3\ \text{条不等式}$$ ✓✓
$$\Longrightarrow\ \text{下一刀}=\textbf{以一阶展开求是否存在 }\delta>0\ \text{的可行方向}（\text{在显式边界配置的切空间内解线性系统}）$$ ✓✓✓
【⛔ 纪律】 本轮为**精确核验＋数值搜索**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 为 sympy 精确；§3 为本行自证必要条件；§4 的搜索为随机多起点＋局部优化（**非全域**），故结论限于"未找到" ✓

## §附 【技术词回查】（补录）
```
技术词 invariant family 命中文件数=0    :: 
技术词 penetration      命中文件数=2    :: ./INDEX-BY-DIRECTION.md ./C3861-B1alpha3FR-success-first-genuine-KKT-candidate.md 
```
