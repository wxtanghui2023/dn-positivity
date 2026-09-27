已查地图：已跑 scripts/prework_map_check.sh incidence 覆盖矩阵 谱 ker A ⟹ 命中档案 **M-1（BQP-lift：CIRCULAR ✗ KILL）／M-2A（CLOSED，$\le1024/11$）／M-2A′（BLOCKED）／M-2B（DROP ✗）／Fourier audit（`ec8d20d`：「短步已耗尽；Booleanity 步 ⟺ 原问题（坐标变换而非松弛）」）**；本档 = **关系全表 ✓ ＋ 新定理（$n$ 偶 ⟹ $A$ 列满秩）✓ ＋ 对旧封口的解释 ✓**。
D0: 本档对象 = 覆盖矩阵 $A$ 及其派生物的完整关系与可松弛性判定
D1: 3（**关系全表 ✓（$A,A^TA,AA^T,b,\ker A$,Walsh ✓）**；**定理：$n$ 偶 ⟹ $A$ 列满秩 ⟹ $b$ 决定 $C$ ✓✓**；**推论：incidence/谱层\textbf{可证}不可松弛 ⟹ 解释 M-1/M-2/Fourier 封口 ✓**）

# Incidence 层：关系全表与可松弛性定理（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(JA-1 关系全表（纯推导 ✓）)}\ \text{球算子 }T:=I+\sum_{i=1}^n\sigma_i\ (=\text{半径-1 邻接})\ ✓;\ \text{列 }A_{(\cdot,c)}=\mathbf 1_{B_1(c)}=T\,e_c\ ✓ \Longrightarrow \boxed{A=T\,P_C},\ P_C=\text{选列算子 ✓}}$$
$$\qquad \mathbf 1_C\ \text{为码的指示向量 ⟹}\ \boxed{b=A\mathbf 1_M=T\,\mathbf 1_C}\ ✓\ (\text{即档案 }(I{+}A)Z^{1024}\ \text{形 ✓})$$
$$\qquad \boxed{A^{\mathsf T}A=(n+1)I+2\,\mathrm{Adj}(G_{\le2}(C))}\ ✓✓\ \text{（因 }|B_1(c)\cap B_1(c')|=2\ \text{对 }d\le2\ ✓、0\ \text{对 }d\ge3\ ✓）—— \textbf{只含码侧距离结构 ✓、不含 profile ✗}}$$
$$\qquad \boxed{(AA^{\mathsf T})_{x,y}=|B_1(x)\cap B_1(y)\cap C|}\ ✓\ \text{（\textbf{点侧 Gram，支撑敏感 ✓}）};\qquad \text{Walsh}:\ \widehat T(\chi)=n+1-2|\chi|\ ✓$$
$$\qquad \Longrightarrow\ \widehat b(\chi)=\bigl(n{+}1{-}2|\chi|\bigr)\widehat{\mathbf 1_C}(\chi)\ ✓;\ n=10:\ \{11,9,7,5,3,{\bf 1},-1,-3,-5,-7,-9\}\ \textbf{无零} \Longrightarrow T\ \textbf{可逆 ✓（档案已核 ✓）}$$
$$\boxed{\textbf{(JB-1 ⭐新定理（$n$ 偶 ⟹ 列满秩 ⟹ profile 决定码 ✓✓）)}\ \text{对任意 }C\subseteq\mathbb F_2^n:\ \boxed{0\in\sigma(A^{\mathsf T}A)\iff -\tfrac{n+1}{2}\in\sigma(\mathrm{Adj})}\ ✓}$$
$$\qquad\text{而 }\mathrm{Adj}\ \text{为整对称矩阵 ⟹ 其特征值皆\textbf{代数整数};\ \text{若 }\tfrac{n+1}{2}\ \text{为奇数（⟺ }n\ \text{偶 ✓）则 }-\tfrac{n+1}{2}\ \text{为有理非整数 ⟹ \textbf{非代数整数} ⟹ 不可能为特征值 ✗✓}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{定理}:\ n\ \text{偶}\ \Longrightarrow\ A\ \text{列满秩} =|C|\ \Longrightarrow\ \text{映射 }C\mapsto b=A\mathbf 1_M\ \textbf{单射（}b\ \text{唯一决定 }C\text{ ✓✓）}}\ \text{（}n{=}10\ ✓\text{适用 ✓）}$$
$$\qquad\textbf{对照（必要性 ✓）}:\ n\ \text{奇时可失败 —— }n{=}1,\ C{=}\mathbb F_2\ \text{给 }A^{\mathsf T}A=\begin{pmatrix}2&2\\2&2\end{pmatrix}\ \text{秩 1}<\mathbf 2\ ✗✓\ \text{（故"偶"不可去 ✓）}$$
$$\boxed{\textbf{(JC-1 ⭐对旧封口的解释（定理级 ✓）)}\ \text{因 }A\ \text{满列秩 ⟹ }\mathbf 1_C=(A^{\mathsf T}A)^{-1}A^{\mathsf T}b\ \text{为 }b\ \text{的\textbf{线性}函数 ⟹ 唯一非线性 = }\mathbf 1_C\ \text{的 Booleanity ✓}$$
$$\qquad\Longrightarrow\ \boxed{\text{任何只用 }b\ \text{的证书\textbf{自动}等价于原问题（\textbf{不可松弛} ✓）}}\ \Longrightarrow\ \textbf{这从定理上解释了档案 M-1（CIRCULAR）／M-2A（CLOSED）／Fourier audit（"坐标变换而非松弛"）三处封口 ✓✓}$$
$$
$$
```

## §1 判定（**✓**）

```
$$\textbf{对你的提案 ✓}:\ \text{"incidence-level certificate 且非径向、非 profile" —— 本档证明它在 }\mathbf 1_C\ \text{层面\textbf{不可能}脱离 profile（因 }A\ \text{满秩 ⟹ }b\leftrightarrow\mathbf 1_C\ \text{线性同构 ✓）} \Longrightarrow \textbf{该形状可证不可松弛 ✗（比第 17 次经验坍缩强 ✓：这是定理 ✓）}$$
$$\qquad\textbf{真正的难处被定位 ✓}:\ \text{不是"profile 看不见支撑" —— \textbf{恰相反：}profile \textbf{完全决定}支撑（JB-1 ✓）；难处在于\textbf{"哪些 }b\ \text{可实现"（Booleanity/可实现集）}} —— \text{这正是档案 }P1\text{-}B\ \text{（支撑大小下界）BLOCKED\ 之处 ✓}$$
$$
$$
```

## §2 状态（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{本档未得新障碍 ✗，但得定理级封口解释＋关系全表 ✓};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$\textbf{可留档 ✓}:\ \text{(1) 关系全表；(2) 定理（}n\ \text{偶 ⟹ }A\ \text{满秩 ⟹ }b\ \text{决定 }C\text{）；(3) 该定理对 M-1/M-2A/Fourier 三处封口的解释 ✓}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$A,A^{\mathsf T}A,AA^{\mathsf T},b,\ker A$,Walsh 关系全表；$n$ 偶 ⟹ $A$ 列满秩定理；该定理对旧封口的定理级解释
- **档案已有（引用，不列为提出）**：M-1（CIRCULAR）、M-2A（CLOSED $\le1024/11$）、M-2A′（BLOCKED）、M-2B（DROP）、Fourier audit（`ec8d20d`；$T$ 可逆、Booleanity ⟺ 原问题）、AMEND-35 SUPPORT-VISIBILITY GATE、P1-B


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 关系全表     命中文件数=1    :: ./INCIDENCE-2026-09-27-full-relations-and-the-injectivity-theorem.md 
技术词 列满秩        命中文件数=2    :: ./II-GABOR-BLIND-MEASURE-round1.md ./INCIDENCE-2026-09-27-full-relations-and-the-injectivity-theorem.md
```
- **本档新增**：$A,A^{\mathsf T}A,AA^{\mathsf T},b,\ker A$,Walsh 关系全表；$n$ 偶 ⟹ $A$ 列满秩定理；该定理对旧封口的定理级解释（见上方命中数；0 命中者为自造语／内部标签 ✓）
