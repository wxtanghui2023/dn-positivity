已查地图：已跑 scripts/prework_map_check.sh Lasserre eta 闭式 母函数 约定 ⟹ 执行自 `B-L3B-1-...`（(B) ✓）＋ 唐先生 12:06（(C) ✓）；本档登记为 **C-L3B-1 — Lasserre $\eta$ coefficient closed form** ✓（**closure/reconstruction，非新资产** ✓）。
D0: 本档对象 = $\eta^{(i,j,t)}_{(i',j',t'),d}$ 的显式闭式与其约定对齐
D1: 0（闭式重建 ＋ 约定核对 ✓，不产生新数学命题 ✓）

# (C) Lasserre $\eta$ 闭式（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AC-1 组合结构 ✓)}\ \text{平移 }w\ \text{把原四类}\ (t,\,i{-}t,\,j{-}t,\,\mathrm{rest}=n{-}i{-}j{+}t)\ \text{按}\ w_x\ \text{值\textbf{互换}}:\ \text{both}\leftrightarrow\text{neither},\ \text{u-only}\leftrightarrow\text{v-only}\ ✓}$$
$$\boxed{\textbf{(AC-2 显式闭式 ✓)}\ \eta^{(i,j,t)}_{(i',j',t'),d}=\sum_{\substack{c,d'\\a:=i-t+b-(i'-t'),\ b\ \text{解出}}}\binom tc\binom{i-t}a\binom{j-t}b\binom{\mathrm{rest}}{d'}\ \text{（约束见 }\S2\ ✓）}$$
$$\boxed{\textbf{(AC-3 母函数 ✓✓)}\ G_\eta=(A+sD)^t(B+sC)^{i-t}(C+sB)^{j-t}(D+sA)^{n-i-j+t}\ ✓\ \text{（}A{=}B{=}C{=}D{=}1\ \Longrightarrow\ (1+s)^n\ ✓\text{）}}$$
$$\boxed{\textbf{(AC-4 三层核对 ✓)}\ \text{①符号/范围：}d=0..n,\ i'+j'-2t'=i+j-2t\ ✓;\ \text{②系数：暴力 vs 闭式 }29\ \text{组零不符 ✓，暴力 vs 母函数 }3\ \text{组恒等 ✓};\ \text{③矩阵：R1b 谱级 }1\times10^{-13}\ ✓}$$
$$\boxed{\textbf{(AC-5 约定 ⚠️)}\ \text{论文 Prop 2.4(iii) 钉死 }d=|w|\ ✓\ \text{（}N_{u,v}=-\beta M_{u,v}+\sum_{w\in S_\ell(0)}\lambda_\ell M'_{u-w,v-w}\ ✓\text{）；作者代码另用 }\texttt{dist}=d(v,w)\ \text{参数化 ⚠️ ⟹ 最终数值钉死须 R2 ⏳}}$$
$$
$$
```

---

## §1 C-1：定义固定（**先于化简 ✓**）

```
$$\eta^{(i,j,t)}_{(i',j',t'),d}:=\#\Big\{w\in\{0,1\}^n:\ |w|=d,\ \overline d(u\oplus w,v\oplus w)=(i',j',t')\Big\}\quad\text{（}\overline d(u,v)=(i,j,t)\ ✓\text{）}$$
$$\textbf{注意（唐先生 ✓）}:\ \text{① }d\ \text{是平移 }w\ \text{的 Hamming 权 ✓；② }(i',j',t')\ \text{是\textbf{平移后}的型 ✓；③ }(i,j,t)\ \text{是\textbf{原}型 ✓；④ \textbf{必有不变量} }i+j-2t=i'+j'-2t'\ ✓（交叠距离在平移下不变 ✓）}$$
$$\textbf{符号来源（唐先生问 ✓）}:\ \eta\ \textbf{本身非负、无符号} ✓;\ \text{符号只来自 }(\lambda,\beta)\ \text{侧}:\ \text{Lasserre 块的 }-\beta\ \text{项 ✓、以及 }\beta^t_{i,j,k}\ \text{内蕴的 }(r-1)^k\ \text{机制 ✓——\textbf{不在 }\eta\ \text{内部} ✓}$$
$$
$$
```

---

## §2 C-2/C-3：四区域结构与母函数（**✓ 推导 ＋ 核对**）

```
$$\text{四区域在 }w\ \text{下的行为}:\ (u_x,v_x):\ (1,1)\xrightarrow{w=1}(0,0)\ ✓;\ (1,0)\to(0,1)\ ✓;\ (0,1)\to(1,0)\ ✓;\ (0,0)\to(1,1)\ ✓$$
$$\text{记 }(c,a,b,d')=\text{四区域中 }w_x{=}1\ \text{的个数 ⟹ }|w|=a+b+c+d'\ ✓;\ \text{平移后型}:\ t'=t-c+d'\ ✓,\ i'-t'=(i-t)-a+b\ ✓,\ j'-t'=(j-t)-b+a\ ✓$$
$$\textbf{逐区域因子（引入 }A,B,C,D\ \text{记平移后四类、}s\ \text{记 }d\ ✓\text{）}:\ (A+sD)^t\ ✓;\ (B+sC)^{i-t}\ ✓;\ (C+sB)^{j-t}\ ✓;\ (D+sA)^{\mathrm{rest}}\ ✓$$
$$\Longrightarrow\ \textbf{AC-3}\ ✓;\ \text{自检 }A{=}B{=}C{=}D{=}1\Longrightarrow(1+s)^n\ \text{（对 }w\ \text{求和 ✓）}\ ✓$$
$$\textbf{C-3 三元分解（诚实校正 ✓）}:\ \eta=(\text{orbit multiplicity})\times 1\times 1\ \text{—— orbit multiplicity}=\text{四区域二项式积 ✓；}\textbf{harmonic 机制与符号都不在 }\eta\ \text{内} ✗\ \text{（它们出现在 }\beta^t_{i,j,k}\ \text{与 }-\beta\ \text{项 ✓）}$$
$$
$$
```

---

## §3 C-4：与 $N_k$ 的接口（**符号不合并 ✓**）

```
$$(N_k)_{ij}=\sum_t\beta^t_{i,j,k}\Big(\underbrace{\sum_d\sum_{i',j',t'}\lambda_d\,\eta^{(i,j,t)}_{(i',j',t'),d}\,x^{t'}_{i',j'}}_{\text{Lasserre 内层（非负权重 ✓）}}-\beta\,x^0_{i+j-2t,0}\Big)\ ✓$$
$$\textbf{纪律（唐先生 ✓）}:\ \boxed{\beta^t_{i,j,k}}\ (\text{harmonic block coefficient},\ \text{带 }(r-1)^k\ \text{符号 ✓})\ \ne\ \boxed{\beta}\ (\text{Lasserre 标量参数 ✓})\ \text{——\textbf{不得合并} ✗}$$
$$
$$
```

---

## §4 C-5：三层 audit（**✓**）

```
$$\text{① 符号/范围层}:\ d\ \text{遍历 }0..n\ ✓;\ \text{型约束 }i'+j'-2t'=i+j-2t\ ✓;\ \text{四区域计数非负 ✓（}\binom{\cdot}{\cdot}\ \text{自动处理越界 ✓）}$$
$$\text{② 系数层（本机 ✓✓）}:\ \text{暴力 }\eta\ \text{vs 闭式}:\ (n,i,j,t,d)\ \text{共 }29\ \text{组}\ \textbf{零不符} ✓;\ \text{暴力 vs }G_\eta:\ (6,3,3,1),(6,4,3,2),(7,4,4,2)\ \text{项数 }32{=}32,\ 32{=}32,\ 46{=}46\ \textbf{恒等} ✓✓$$
$$\text{③ 矩阵层}:\ \text{R1b 已证 }\mathrm{spec}(R(c,N))=\biguplus_km_k\mathrm{spec}(\text{Lasserre 块})\ ✓\ \text{（}3.2\times10^{-14},\ 5.7\times10^{-14},\ 1.1\times10^{-13},\ 3.7\times10^{-13}\ ✓\text{，两族}(\lambda,\beta)\ ✓）$$
$$\qquad\textbf{诚实标注 ⚠️}:\ \text{R1b 是\textbf{块结构与归一}的谱级审计（内部一致性 ✓），\textbf{不是}与论文数值的对外比对 ✗ —— 对外钉死须 R2（块式 SDP vs 已验 unreduced 锚点 ✓）}$$
$$
$$
```

---

## §5 约定对齐（**最后一步的关键 ⚠️**）

```
$$\textbf{论文侧（钉死 ✓）}:\ \text{Prop 2.4(iii)}\ N_{u,v}=-\beta M_{u,v}+\sum_{\ell}\lambda_\ell\sum_{w\in S_\ell(0)}M'_{u-w,v-w}\ ✓\ \Longrightarrow\ \lambda\ \text{按 }|w|\ \text{索引 ⟹ }\eta\ \text{下标 }d=|w|\ ✓$$
$$\qquad\text{且 Lemma 4.6 原文措辞亦为"words }w\ \text{of weight }d"\ ✓\ \text{——\textbf{两侧一致} ✓}$$
$$\textbf{作者代码侧（参数化差异 ⚠️）}:\ \texttt{MakeDistr}\ \text{中 }\texttt{dist}=a+d'+j-b-c=d(v,w)\ \text{（另一指标 ✓）};\ \text{但 }\texttt{dist}\ \text{与 }|w|\ \text{在其参数化下非同一量 ✓}$$
$$\Longrightarrow\ \text{二者必为\textbf{同一和的重参数化}（否则代码不会复现论文表格 ✓），但结构上\textbf{未逐项核完} ⚠️ ⟹ 最终钉死 = \textbf{R2}（修 bmat 拼装的块式 SDP ⟹ 与已验 unreduced 锚点 }11.5980553/16.0000000\ \text{比对 ✓）⏳}$$
$$
$$
```

---

## §6 登记与边界（**诚实 ✓**）

```
$$\boxed{\textbf{C-L3B-1 — Lasserre }\eta\ \text{coefficient closed form}:\ \text{由四区域结构 ＋ }\alpha\ \text{型母函数完整推出 ✓；与 }N_k\ \text{装配及 R1b 谱级审计一致 ✓；}\textbf{性质 = closure/reconstruction，非新数学资产} ✓}$$
$$\text{闭链}:\ \texttt{4e1a82d（L3B 最终合并）}\to\text{B-L3B-1（border 归一）}\to\text{C-L3B-1（}\eta\ \text{闭式）}\ ✓$$
$$\textbf{状态}:\ \text{Level 3B 三项待办中的 (A)(B)(C) 均已成文 ✓；}\textbf{唯余一项对外钉死}（}\eta/\lambda\ \text{指标约定 ⟹ R2 ⟹ 与锚点比对）⏳$$
$$\qquad\Longrightarrow\ \text{建议标签}:\ \textbf{Level 3B FINAL CLOSED modulo the }\eta/\lambda\ \text{index convention (R2 pinning pending)}$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1–§4 为**定义／推导／核对** ✓（三个数值核对全部零不符 ✓）；§5 为**约定对齐的现状** ⚠️（论文侧已钉死 ✓，代码侧参数化差异未逐项核完 ✓）
- **未**声称 $\eta$ 闭式已与论文数值对外比对 ✗（R2 ⏳）；**未**声称新资产 ✗；**未**声称 Level 3B 无余项 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\eta$ 四区域结构、$G_\eta$ 母函数、$\eta$ 闭式登记、约定对齐现状
- **档案已有（引用，不列为提出）**：Lemma 4.6、Prop 2.4(iii)、Prop 4.5、$\alpha$ 母函数、R1b、$\beta^{\rm paper}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 eta 四区域结构 命中文件数=0    :: 
技术词 G_eta 母函数  命中文件数=0    ::
```
- **本档新增**：$\eta$ 四区域结构、$G_\eta$ 母函数、$\eta$ 闭式登记、约定对齐现状（见上方命中数；0 命中者为自造语／内部标签 ✓）
