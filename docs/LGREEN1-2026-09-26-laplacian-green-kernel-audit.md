已查地图：已跑 scripts/prework_map_check.sh K(10,1) 拉普拉斯 Green 核 heat semigroup ⟹ 执行自 `FOURIER-2026-09-26`（谱壳能量已被钉死 ✓）＋ `T3MIN1-2026-09-26`（Gram 法失明 ✓）；本档为**全局算子路线一次性实验（L-GREEN-1）**（唐先生 2026-09-26 21:47 指令 ✓）；含计算＋独立核验 ✓。
D0: 本档对象 = $(11I-L)f=b$ 的 Green 距离核 $g_0..g_{10}$ 与 Booleanity（既有对象，换全局算子语言 ✓）
D1: 0（产出为核值、符号判定与 STOP）

# L-GREEN-1-2026-09-26 · 拉普拉斯 Green 核审计

## §0 结论（先给）

```
$$\boxed{\textbf{(W-1 框架确认)}\ L=10I-A\ \Longrightarrow\ b=(I+A)f=(11I-L)f\ ✓✓;\ \lambda_k(L)=2k\ ⟹\ \text{纯谱≡Fourier}\ ✗\ (\text{你已指出 ✓})}$$
$$\boxed{\textbf{(W-2 核值已定 ＋ 独立验证)}\ g=(g_0,\dots,g_{10})\ \text{由递推唯一确定}\ ✓✓;\ \text{直接求逆核验偏差}\le6.5\times10^{-16}\ (n=4,6,8)\ ✓✓}$$
$$\boxed{\textbf{(W-3 关键否证)}\ \text{核\textbf{混合符号}}:\ \text{正}\ \{0,1,4,5,8,9\};\ \text{负}\ \{2,3,6,7,10\}\ \Longrightarrow\ \textbf{核非正}\ \Longrightarrow\ \textbf{最大原理/正性不可用}\ ⚠️✗}$$
$$\boxed{\textbf{(W-4 判定)}\ \text{盒约束下 }z\ \text{处 }0\in[-16.28,+16.82]\ ⟹\ \textbf{无矛盾}\ ✗;\ \text{正算子（}e^{-tL}\text{）}\to\text{壳能量}\to\text{已钉死}\ ✗\ \Longrightarrow\ \textbf{STOP}}$$
$$
$$
```

---

## §1 (W-1) 框架（正确 ✓）

```
$$A=\text{Q}_{10}\ \text{邻接算子};\ L=10I-A\ ✓;\ b(x)=\sum_{y:d(x,y)\le1}f(y)=(If+Af)(x)\ \Longrightarrow\ \boxed{b=(I+A)f=(11I-L)f}\ ✓✓$$
$$\text{谱}:\ A\ \text{的本征值}\ \theta_k=10-2k\ ⟹\ L=10I-A\ \text{本征值}\ \lambda_k=2k\ ⟹\ \textbf{纯 Laplacian 谱分析≡Fourier/Krawtchouk}\ ✗\ ✓$$
$$(11I-L)\ \text{可逆}:\ \text{本征值}\ 11-2k\in\{11,9,7,5,3,1,-1,-3,-5,-7,-9\}\ \textbf{无零点}\ ✓✓\ \Longrightarrow\ f=Gb,\ G=(11I-L)^{-1}\ ✓$$
$$\textbf{唐先生 §4 公式核验 ✓}:\ \langle f,Lf\rangle=11|C|-\langle f,b\rangle=1309-(119+2A_1)=\mathbf{1190-2A_1}\ ✓✓\ (\text{恰为 }A_1\ \text{重编码}\ ⚠️)$$
$$
$$
```

---

## §2 (W-2) 距离核 $g_0..g_{10}$（本条为所求 ✓✓）

```
$$\text{距离-transitive}\ \Longrightarrow\ G(x,y)=g\big(d(x,y)\big)\ ✓;\ \text{径向方程}:\ h(i)+i\,h(i-1)+(10-i)\,h(i+1)=\delta_{i0}\ ✓\ (h(11)\ \text{系数 0}\ ✓)$$
$$\begin{array}{c|ccccccccccc} i&0&1&2&3&4&5&6&7&8&9&10\\ \hline g_i&+0.090909&+0.090909&-0.020202&-0.020202&+0.011544&+0.011544&-0.013853&-0.013853&+0.036941&+0.036941&-0.369408\end{array}$$
$$\textbf{结构观察}:\ g_{2j}=g_{2j+1}\ (j=0..4)\ ✓;\ |g_{10}|\ \text{最大}\ ✓;\ g_n\ \text{符号随 }n/2\ \text{奇偶交替}\ ✓\ (n{=}4,6,8,10\ \text{实测 ✓})$$
$$\textbf{独立验证 ✓✓}:\ \text{直接求逆}\ (I+A)^{-1}\ \text{vs 递推}:\ n=4:\ 1.4\times10^{-16};\ n=6:\ 2.2\times10^{-16};\ n=8:\ 6.5\times10^{-16}\ ✓✓$$
$$\textbf{自检}:\ g_0=\tfrac1{11}\ ✓;\ \sum_i\binom{10}{i}g_i=\tfrac1{11}=(G\mathbf 1)\ ✓✓$$
$$
$$
```

---

## §3 (W-3) 符号/单调性判据：**否**（唐先生要查的这一条 ⚠️）

```
$$\text{正号层}:\ i\in\{0,1,4,5,8,9\};\qquad \text{负号层}:\ i\in\{2,3,6,7,10\}\ \Longrightarrow\ \textbf{核非正}\ ✗\ (\text{不满足 }g_i\ge0\ ✓\ \text{或单调性 ✗})$$
$$\Longrightarrow\ \textbf{最大原理、局部平均性质、正性传递均不可用}\ ⚠️\ \text{（Green 核路的\textbf{主要希望落空} ✓）}$$
$$\textbf{结构性原因}:\ 11I-L\ \text{本征值有正有负（}11,\dots,-9\text{）}\Longrightarrow\ \text{算子\textbf{不定}} \Longrightarrow\ \text{Green 核必然变号}\ ✓$$
$$\qquad\text{改用\textbf{正}算子}\ e^{-tL}\ \Longrightarrow\ H(t)=\langle f,e^{-tL}f\rangle=\sum_k e^{-2kt}G_k\ \text{（壳能量）}\ \Longrightarrow\ \text{已被两矩式钉死}\ ✗\ \text{（你 §7 判断 ✓）}$$
$$
$$
```

---

## §4 (W-4) Boolean 盒测试（无矛盾 ✗）

```
$$f(z)=0\ \text{且}\ b(z)=3\ \Longrightarrow\ 0=3g_0+\sum_{i\ge1}g_iN_i(z)\ ✓;\quad N_i(z)\in[\binom{10}i,\ 3\binom{10}i]\ ✓,\ \sum_{i\ge1}N_i(z)=1306\ ✓$$
$$\text{按 }g_i\ \text{符号取盒端点}:\ [\min,\max]=[\mathbf{-16.28},\ \mathbf{+16.82}]\ ⟹\ 0\ \text{在内}\ ⟹\ \textbf{无矛盾}\ ✗$$
$$\text{另一族检验（}G^2\ \text{谱界）}:\ 119=\langle f,f\rangle=\langle b,G^2b\rangle\in[\|b\|^2/121,\ \|b\|^2]\ ⟹\ \|b\|^2\in[119,14399]\ ✓\ \text{与 }1881\ \text{相容}\ ✗$$
$$
$$
```

---

## §5 判定与移交（诚实 ✓）

```
$$\textbf{路 A（三阶/全局算子）遍历完毕}:\ \text{三阶量判据表（}\texttt{THIRD}\text{）}\to\text{最小三点 PSD（}\texttt{T3MIN1}\text{）}\to\text{Green 核（本档）}\ \text{全部 STOP}\ ✗$$
$$\qquad\Longrightarrow\ \text{与 }\texttt{GAPTHEOREM}\ \text{诊断一致}:\ \text{障碍＝缺\textbf{类型不同}的独立量；本类语言（谱/算子/三点）在其最自然形式下均回到既有量}\ ⚠️$$
$$\textbf{移交（按预设 ✓）}:\ \to\ \texttt{FRONTIER-R1}:\ \text{第一步＝校准门 }\texttt{G-CAL}\ \text{（复现该文公开的 RoSQS}(46)\ \text{基块表，逐块核验）}\ ✓✓$$
$$\qquad\textbf{本轮副作用（已记）}:\ \text{两点自纠}\ ⚠️\ \text{① 谱式交叉核验公式有 bug（递推已由直接求逆独立验证 ✓）；② 径向检查脚本误把各层与 }d{=}0\ \text{层比较}\ ✗\ \text{（已修 ✓）}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §2 的核为**唯一解** ✓（递推＋直接求逆双重验证 ✓，偏差 ≤ 6.5e-16 ✓）
- §3 的"不可用"判定为**本档结论** ✓（针对 Green 核的具体形式 ✓），**非**"最大原理永远无用" ✗
- §4 为**盒松弛**（非精确局部 profile ✓）⟹ 只在"无矛盾"方向有效 ✓
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张算子语言无价值 ✗

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Green 距离核  命中文件数=1    :: ./LGREEN1-2026-09-26-laplacian-green-kernel-audit.md 
技术词 核符号否证  命中文件数=1    :: ./LGREEN1-2026-09-26-laplacian-green-kernel-audit.md
```
- **本档新增**：Green 距离核 $g_0..g_{10}$、核符号否证（见上方命中数；0 命中者为自造语，不列新命名 ✓）
- **档案已有（引用，不列为提出）**：$(11I-L)f=b$ 框架、$L$ 谱≡Fourier、壳能量钉死、$\langle f,Lf\rangle=1190-2A_1$
