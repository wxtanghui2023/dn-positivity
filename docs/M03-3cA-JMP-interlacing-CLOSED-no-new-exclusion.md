已查地图：命中（`M03-3c-shift-family-and-trace-battery-negative-on-S`）⟹ `(3c-A)` JMP 交错工具箱专项，不开新案
D0: 本档对象 = **JMP 2017 交错方法链逐段抽取**（主子式 → 交错 → 优化 → `Thm 1`）＋ **判定：`Thm 1` 输出即 `u` 条件（已用），无新曲线** ＋ **`J-C-L` 三次条件在 `S` 上不咬（数值核验）** ＋ ⭐**结构收获：`y=a+2d-1` ⟹ `MN=line 4` ⟹ `S` 紧贴"可实行"边界** ＋ `P2` 方向建议
D1: 1（首次完整抽取 JMP 交错链并判定其在 `S` 无新排除；产出 `y=a+2d-1` 的同一性）
[RESEARCH]

# **`(3c-A)`：JMP 交错方法 —— `CLOSED / NO NEW EXCLUSION`**

## §1 原文方法链（JMP 2017, LAA 512, 129–135；已入档）

```
$$\textbf{对象}:\ \lambda=(1,a,a,-(a+d),-(a+d)),\quad 0<a,d;\quad a+d,\ 2d<1<a+2d$$ ✓（**恰为本族**：`a=t,\ a+d=q(t)+\varepsilon`）
$$\textbf{步骤 1（主子式）}:\ A_{(i)}=\text{删去第 }i\ \text{行/列的 }4\times4\ \text{主子式};\ \text{交错给出 }p_i\ge a\ge q_i\ge-(a+d)\ (p_i=\rho(A_{(i)}))$$ ✓
$$\textbf{步骤 2（Perron + 交错）}:\ \boxed{1\ge p_i\ge a+d};\qquad \text{Tr}(A_{(i)})\ge0\Rightarrow p_i+q_i-d\ge0;\qquad 1-2d>0$$ ✓
$$\textbf{步骤 3（对角元）}:\ a_{ii}=\operatorname{Tr}(A)-\operatorname{Tr}(A_{(i)})\ge0\Rightarrow\boxed{1-p_i-d-q_i\ge0}\Longrightarrow d-p_i\le q_i\le 1-p_i-d$$ ✓
$$\textbf{步骤 4（迹恒等式与三次不等式）}:\ 4\operatorname{Tr}A=\sum_i\operatorname{Tr}A_{(i)}\Rightarrow\boxed{4-3d=\sum p_i+\sum q_i};\quad 4\operatorname{Tr}(A^3)\ge\sum_i\operatorname{Tr}(A_{(i)}^3)\Rightarrow\boxed{4+3a^3-3(a+d)^3\ \ge\ \sum p_i^3+\sum q_i^3}$$ ✓✓
$$\textbf{步骤 5（优化）}:\ \text{在约束下\textbf{最小化} }\sum p_i^3+\sum q_i^3;\ \text{固定 }\sum p_i\ \text{时 }p\ \text{取平权最小};\ q\ \text{取极端分布最小};$$
$$\qquad \text{令 }p_i=a+d+t\Rightarrow\text{一元 }t\ \text{问题},\ \text{导数}>0\Rightarrow\text{最小在 }t=0\ \Longrightarrow\ \sum p_i^3+\sum q_i^3\ \ge\ 5(a+d)^3-a^3-4(a+2d-1)^3$$ ✓✓✓
$$\textbf{输出（原文 Thm 1）}:\ \text{若 }2(a+d)^3\ge 1+a^3+(a+2d-1)^3\ \textbf{则不可实现}\quad\Longleftarrow\ \textbf{恰为 }u\le0\ \text{条件}$$ ✓✓✓
```

## §2 判定（先生硬规则：只有产生 `S` 的非空真子集才算成功）

```
$$\boxed{\text{JMP 交错方法的\textbf{全部输出} = Thm 1 = }u\ \text{条件（我方已用，且 }u>0\ \text{on }S\text{）}} \Longrightarrow \textbf{无新曲线}$$ ✓✓✓
$$\textbf{附加曲线（原文 Fig.1 curve 2）}:\ 50(a+d)^3+(1-2d)^2-50a^3=25\ (\text{三次 }J-C-L\ \text{条件})$$ ✓
$$\qquad \text{原文自述}:\ \text{"Other }J\text{-}L\text{-}L\ \text{conditions were also investigated... all were \textbf{comfortably inside our excluded region}"}\ \Longrightarrow\ \textbf{不越出 }u\ \text{之外}$$ ✓✓
$$\qquad \text{数值核验（}S\ \text{内 12 样点）}:\ \text{curve 2 的排除量}\ c_2\in(-9.5,-4.6)<0\ \forall\ \text{样点}\Longrightarrow \textbf{不咬}$$ ✓✓
$$\Longrightarrow\ \boxed{(3c\text{-}A)=\textbf{CLOSED} / \textbf{NO NEW EXCLUSION}}（\text{按先生步骤 5，不继续在同一 interlacing 变体上堆条件}）$$ ✓✓✓
$$\textbf{不得写}:\ "S\ \text{内不存在任何必要条件"；正确表述}:\ \textbf{JMP 交错方法及其附加 }J\text{-}C\text{-}L\ \text{条件在 }S\ \text{上不产生新排除}$$ ✓✓
```

## §3 ⭐ 结构收获（本条最有价值）：`y=a+2d-1` ⟹ 三条边界的同一性

```
$$\boxed{y:=\lambda_3-s_1=a+2d-1}$$ ✓✓（本行验证：`y=4-8t+2\varepsilon`，`a+2d-1=t+2(q+\varepsilon-t)-1=4-8t+2\varepsilon` ✓）
$$\Longrightarrow\ \text{三处表述实为\textbf{同一条直线}}:\ \text{MN 条件}\ (1+a+2b\le0)\ \equiv\ y\ge0\ \equiv\ \text{JMP 的 }\textbf{line 4}\ (a+2d\le1)$$ ✓✓✓
$$\qquad \text{Loewy}:\ \text{"points on and above MN are realizable"};\qquad \text{JMP}:\ \text{"all points on and below line 4 are (trivially) symmetrically realizable"}$$ ✓✓
$$\textbf{可实行机制（原文）}:\ \text{分块 }\operatorname{diag}(B_4,\ a),\ B_4\ \text{实现 }(1,a,-(a+d),-(a+d)),\ \text{其迹条件恰为 }1-a-2d\ge0$$ ✓✓
$$\Longrightarrow\ \boxed{S\ \textbf{紧贴可实行边界}}:\ S\ \text{的下边缘 }\varepsilon=4t-2\ \text{即 }y=0\ \text{即 line 4/MN};\ S\ \text{位于其\textbf{严格上方}}（y>0,\ a+2d-1\in(0.02,0.13)\ \text{实测）}$$ ✓✓✓
$$\text{几何定位（与原文 Fig.1 对照）}:\ S\ \text{四条边界检验全部通过}:\ \text{Thm 1 排除？否};\ \text{curve 2 排除？否};\ \text{line 4 之上（非平凡可实现）};\ \text{line 3 同侧（sign }-0.85\sim-1.20\text{，与原文未决例 }Q=(1/2,7/24)\ \text{同侧）}$$
$$\Longrightarrow\ \boxed{S\ \subset\ \text{JMP 2017 所称"small, nearly triangular region of unresolved spectra"}}$$ ✓✓✓（**外部独立确认** `S` 确为未决区）
```

## §4 下一步：`P2` 的天然入口（本档建议）

```
$$\text{因 }S\ \text{紧贴可实行线，最自然的构造路线}:\ \text{从 }\varepsilon=4t-2\ (y=0)\ \text{的\textbf{可约实现} }\operatorname{diag}(B_4,a)\ \text{出发},$$
$$\qquad \text{作\textbf{不可约扰动}进入 }y>0\ (\varepsilon>4t-2)\Longrightarrow \text{若成功即 }S\ \text{内可实现点（对 }\Lambda\ \text{类可实现域是新信息）}$$ ✓✓✓
$$\text{或}:\ \text{继续找\textbf{非幂和、非交错}的排除机制}（\text{如支撑图／奇异结构型}）$$ ✓
【⛔ 纪律】 本轮为**原文逐段实读＋数值核验**（无搜索）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 为原文逐字方法链；§2 判定按先生硬规则；§3 的 `y=a+2d-1` 为本行自证（三处表述同一性）；§3 的"subset unresolved"由四条边界检验＋原文表述支持（非逐点全域证明）✓

## §附 【技术词回查】（补录）
```
技术词 interlacing      命中文件数=13   :: ./IP-1-CLOSURE-and-IP-2-ENTRY.md ./C113-where-is-beta-and-did-we-avoid-beta-blindness.md ./C85-wall-breaking-phase-consolidated-map-and-terminal-obstruction-statement.md 
技术词 block diagonal   命中文件数=0    :: 
```
