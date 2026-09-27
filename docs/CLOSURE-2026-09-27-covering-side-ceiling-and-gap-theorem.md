已查地图：已跑 scripts/prework_map_check.sh 覆盖侧 封顶 信息分层 gap D=A₁−A₂ ⟹ 执行自 `PHASE2-KEY-...-ball-collapse`／`PHASE2-Q0-...`（✓）＋ 唐先生 12:23（(iii) 升级版 ✓）；本档 = **覆盖侧封顶定理 ＋ 缺口定理（信息分层 I₁⊂I₂⊂I₃）** ✓。
D0: 本档对象 = 覆盖侧可观测量的信息上限与其缺口
D1: 1（新增：**二阶矩封顶定理 A ✓**；**witness 定理 B ✓**；**信息分层 ＋ β gate ✓**）

# 覆盖侧封顶定理 ＋ 缺口定理（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AX-1 定理 A · 二阶矩封顶 ✓)}\ \sum_xb(x)=M(n+1)\ ✓,\quad\sum_x\binom{b(x)}2=2(A_1+A_2)\ \Longrightarrow\ \sum_xb(x)^2=M(n+1)+4(A_1+A_2)\ ✓}$$
$$\qquad\Longrightarrow\ \text{\textbf{任何最终化成 }}\Phi\ \text{次数}\le2\ \text{的 }b\text{-矩／球对交叠的不变量，}\textbf{至多看到 }A_1+A_2,\ \text{永不区分 }A_1\ \text{与 }A_2\ ✓✓$$
$$\boxed{\textbf{(AX-2 定理 B · 封顶被达到 ✓)}\ n=9,K=62\ \text{两码}:\ \text{全部 }I_1/I_2\ \text{统计量\textbf{逐项相同}} ✓,\ \text{而}\ \boxed{D:=A_1-A_2=-59\ \text{vs}\ -21}\ (\Delta D=38)\ ✓✓}$$
$$\qquad\Longrightarrow\ \text{盲区\textbf{非空}——}\textbf{不是"我们没找到足够好的不变量"，而是该类观测\textbf{结构上无区分能力}} ✓✓$$
$$\boxed{\textbf{(AX-3 信息分层 ✓)}\ \mathcal I_1\ \text{(覆盖计数)}\subset\mathcal I_2\ \text{(球对交叠)}\subset\mathcal I_3\ \text{(support/incidence 几何)};\quad \mathcal I_1,\mathcal I_2\Longrightarrow A_1+A_2\ ✓\ \text{但}\ \not\Longrightarrow(A_1,A_2)\ ✗✓}$$
$$\boxed{\textbf{(AX-4 缺口定理 ✓)}\ \text{下一条路必须携带一个泛函 }J:\ J(C_0)\ne J(C_1)\ \text{且其依赖\textbf{不可由 }(A_1,A_2)\ \text{解释}\ ✓;\ \text{否则必然重复失败}}$$
$$\qquad\textbf{G-PROGRESS β gate（下一轮 ✓）}:\ \text{测试集 = 上述两 witness（}D=-59\ \text{vs}\ -21\ ✓\text{）};\ \text{不能区分者 ⟹ 仍在盲区 ✓}$$
$$\qquad\textbf{已排除（档案 ✓）}:\ I,S\ \text{自由分叉（无约束力 ✗）};\ \text{2-面量} =(n-1)A_1+A_2\ \text{区分但\textbf{是 }A_1\ \text{的仿射函数} ⚠️（FACE 档：无 P3 碰撞 ✗）}$$
$$
$$
```

---

## §1 定理 A 的证明（**两行 ✓**）

```
$$\sum_xb(x)=\sum_c|B_1(c)|=M(n+1)\ ✓;\qquad \sum_x\binom{b(x)}2=\sum_{\{c,c'\}}\big|B_1(c)\cap B_1(c')\big|=2(A_1+A_2)\ ✓$$
$$\Longrightarrow\ \sum_xb(x)^2=4(A_1+A_2)+\sum_xb(x)=M(n+1)+4(A_1+A_2)\ ✓\qquad\square$$
$$\textbf{本机核对 ✓}:\ n=9\ \text{两码均 }\sum b=620\ ✓,\ \sum b^2=912=M(n+1)+4\cdot73\ ✓✓$$
$$\textbf{推论（信息上限 ✓）}:\ \text{任何 }\sum_x\Phi(b(x))\ (\deg\Phi\le2)\ \text{或}\ \sum_{\{c,c'\}}\Psi(|B\cap B'|)\ \text{型量}\in\mathbb Q[M,\ A_1+A_2]\ ✗$$
$$
$$
```

---

## §2 定理 B（witness，**决定性 ✓**）

```
$$\begin{array}{c|c|c|c|c|c|c|c|c|c}
\text{码} & A_1 & A_2 & A_1{+}A_2 & \mathbf{D=A_1-A_2} & \text{2-面量} & I & S & \text{profile} & \sum b^2\\
\hline
\#0 & 7 & 66 & 73 & \mathbf{-59} & 122 & 6 & 126 & \{(1,432),(2,62),(3,8),(4,10)\} & 912\\
\#1 & 26 & 47 & 73 & \mathbf{-21} & 255 & 27 & 67 & \text{同上} & 912\\
\end{array}$$
$$\text{相同（}I_1/I_2\ ✓\text{）}:\ \text{profile}\ ✓,\ \sum b\ ✓,\ \sum b^2\ ✓,\ A\ ✓,\ T_3\ ✓,\ T_4\ ✓,\ S_2\ ✓,\ S_{2b}\ ✓,\ H_H\ ✓,\ P_2\ ✓\ \text{—— 逐项相同 ✓✓}$$
$$\text{不同（}I_3\ \text{层 ✓}）:\ D=-59\ \text{vs}\ -21\ ✓;\ (n-1)A_1+A_2=122\ \text{vs}\ 255\ ✓;\ (I,S)=(6,126)\ \text{vs}\ (27,67)\ ✓$$
$$\qquad\text{注意}:\ I+S=132=2A_2\ \text{与}\ 94=2A_2\ ✓\ \text{—— 故 }(I,S)\ \text{的信息}=A_2+\text{一自由度} ✓\ \text{（与档案"I/S 分叉"一致 ✓）}$$
$$
$$
```

---

## §3 信息分层与缺口定理（**✓ 数学化**）

```
$$\boxed{\begin{array}{c|c|c}
\text{层} & \text{可观测量} & \text{可决定之处}\\
\hline
\mathcal I_1 & M,\ \sum b,\ \text{profile}\ (N_j)\ldots & \text{一阶：}M(n+1)\ ✓\\
\mathcal I_2 & \sum\Phi(b)\ (\deg\le2),\ \sum_{\{c,c'\}}\Psi(|B\cap B'|) & \textbf{仅 }A_1+A_2\ ✓\ \text{（定理 A ✓）}\\
\mathcal I_3 & 2\text{-面 incidence、}\mathrm{Supp}\ \text{几何、}I/S & \text{可含 }A_1\ \text{仿射量} ⚠️\ \text{（但档案：无碰撞 ✗）}\\
\end{array}}$$
$$\Longrightarrow\ \mathcal I_1,\mathcal I_2\ \text{的像空间}\ \subseteq\ \mathbb Q\big[M,\ A_1+A_2\big]\ \subseteq\ \mathbb Q\big[M,A_1,A_2\big]\ \text{（真包含 ✓，因 }D\ \text{自由 ✓）}$$
$$\textbf{核}:\ A_1-A_2\ \text{整个方向落在投影 }\mathcal I_1\oplus\mathcal I_2\ \text{的\textbf{核}里} ✓\ \text{—— 故"加强覆盖计数"永远不可能看见它 ✓✓}$$
$$
$$
```

---

## §4 与 119 的关系（**状态不变，但定位精确 ✓**）

```
$$\text{覆盖侧三步链（已闭合 ✓）}:\ \boxed{\text{覆盖条件}\ (b\ge1)\ \to\ \text{球交叠}\ \to\ A_1+A_2\ \to\ \textbf{信息封顶}}$$
$$\text{本会话新增的"带定理的解释" ✓}:\ \text{excess／surfeit／}Q／\zeta／\text{profile 矩／}U_\zeta\ \text{全部封顶} ✓\ \text{（定理 A ＋ 塌缩定理 ✓）}$$
$$\text{下一个 P1/P2 唯一入口 ✓}:\ \textbf{构造对 }A_1-A_2\ \text{非退化的 support/局部 incidence 泛函} ✓$$
$$\qquad\text{已被判无力的候选（档案 ✓）}:\ I/S\ \text{（自由 ✗）、2-面量（}A_1\ \text{仿射 ✗）—— \textbf{必须携带\textbf{新耦合}，而非另一个 }A_1\ \text{的线性投影} ⚠️}$$
$$\text{119 状态}:\ \textbf{OPEN} ✓\ \text{（不变 ✓）；本档为\textbf{结构性封顶 ＋ 缺口定位} ✓，非否定存在 ✗}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§2 为**定理 ＋ 本机验证** ✓（定理 A 两码 ✓；witness 逐项 ✓）；§3 为**分层数学化** ✓；§4 为**状态定位** ✓
- **未**声称解决 119 ✗；**未**声称覆盖侧"不可能" ✗（只声称"该类观测无区分能力" ✓）；**未**改动 UNKNOWN ✓
- 本档价值 ✓：把"No-Go 集合"升级为**带定理的信息封顶 ＋ 明确的缺口坐标（}$D=A_1-A_2$**）✓ —— 下一轮知道**必须携带什么信息** ✓✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：二阶矩封顶定理、witness 定理、信息分层 $\mathcal I_1\subset\mathcal I_2\subset\mathcal I_3$、β gate
- **档案已有（引用，不列为提出）**：$b$、球交叠常数、$A_{\le2}$、$I/S$、FACE 档、G-PROGRESS


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 二阶矩封顶定理 命中文件数=1    :: ./CLOSURE-2026-09-27-covering-side-ceiling-and-gap-theorem.md 
技术词 信息分层     命中文件数=1    :: ./CLOSURE-2026-09-27-covering-side-ceiling-and-gap-theorem.md
```
- **本档新增**：二阶矩封顶定理、witness 定理、信息分层、β gate（见上方命中数；0 命中者为自造语／内部标签 ✓）
