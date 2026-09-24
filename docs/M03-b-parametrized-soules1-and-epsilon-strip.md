已查地图：命中（`M03-iii-theorem-sup-d1-on-ordered-cone`）⟹ `(b)` 第一阶段（参数化）＋ 第二阶段（`\varepsilon` 条带），不开新案
D0: 本档对象 = ⭐**参数化定理**（四偏导分子全为 `(t-1)\times`正系数多项式 ⟹ 符号只依赖 `t<1`）＋ **`d_1(t,q,1^4)=\frac{2t+3-10q}{15}`，负值 `\iff q>\frac{2t+3}{10}`** ＋ **`\Lambda(t)` 全族排除** ＋ **`\varepsilon` 条带 `(4t-2,0)\subset R\setminus W` 的 Soules-1 解析排除**
D1: 1（首次把单点证书推广到整族，并首次给出**穿过 `\partial W` 进入 `R\setminus W`** 的解析条带）
[RESEARCH]

# **`(b)` 参数化证书 ＋ `\varepsilon` 条带**

## §1 阶段 1：参数化（保留 `t,q` 符号）

```
$$d_1(t,q,x)=\frac{1}{T_5}-q\frac{x_2^2}{T_2}-q\frac{x_3^2}{T_2T_3}+t\frac{x_4^2}{T_3T_4}+t\frac{x_5^2}{T_4T_5}$$ ✓✓（`\lambda=(1,t,t,-q,-q)` 型）
$$\frac{\partial d_1}{\partial x_5}=\frac{2x_5(t-1)}{T_5^2};\qquad \text{代 }x_5=x_4:\ \frac{\partial}{\partial x_4}=\frac{4x_4(t-1)}{(x_2^2+x_3^2+2x_4^2+1)^2}$$ ✓✓（**与 `q` 无关**）
$$\text{代 }x_5=x_4=x_3:\ \frac{\partial}{\partial x_3}\ \text{的分子系数}\ \textbf{全部为 }(\text{正数})\times(t-1):\ 11(t-1),\ 42(t-1),\ 22(t-1),\ 51(t-1),\ 42(t-1),\ 11(t-1)$$ ✓✓✓
$$\text{全相等时}\ \frac{\partial}{\partial x_2}\ \text{的分子系数}:\ 192(t-1),\ 112(t-1),\ 18(t-1)$$ ✓✓✓
$$\Longrightarrow\ \textbf{四方向偏导}<0\ \textbf{只取决于 }\boxed{t<1}\ (\text{与 }q\ \text{无关}) \Longrightarrow \text{下降链对\textbf{一切 }t<1\ \text{成立}}$$ ✓✓✓
$$\boxed{d_1(t,q,x)\le d_1(t,q,1,1,1,1)=\frac{2t+3-10q}{15}}\ \Longrightarrow\ \textbf{负值}\iff 10q>2t+3$$ ✓✓✓
$$\text{代入 }q=\frac{5-7t}{2}:\ d_1\le\frac{37t-22}{15}<0\iff t<\frac{22}{37}\approx0.5946;\quad \text{本族 }t<\tfrac12<\tfrac{22}{37}\ \Longrightarrow\ \textbf{全族排除}$$ ✓✓✓
$$\boxed{\Lambda(t)\notin\mathcal S_5^{\rm Soules\text{-}1}\ (\tfrac49<t<\tfrac12)}\qquad \textbf{不得升级为 }\Lambda(t)\notin\mathcal S_5$$ ✓✓
```

## §2 阶段 2：`\varepsilon` 扰动（`c=d=q(t)+\varepsilon`）

```
$$\lambda(t,\varepsilon)=\bigl(1,\ t,\ t,\ -(q(t)+\varepsilon),\ -(q(t)+\varepsilon)\bigr)$$ ✓
$$S=1+2t-2(q+\varepsilon)=9t-4-2\varepsilon;\qquad \boxed{9b-S=4+2\varepsilon}$$ ✓✓（`\varepsilon>0` 入 `W`；`\varepsilon<0` 入 `R\setminus W`）
$$\textbf{四偏导系数（含 }\varepsilon\textbf{）}:$$
$$\qquad \partial_{x_5}:2(t-1);\quad \partial_{x_4}:4(t-1)\ (\text{无 }\varepsilon);\quad \partial_{x_3}:\ -2\varepsilon+11t-11,\ 6(-2\varepsilon+7t-7),\ 2(-2\varepsilon+11t-11),\ 3(-6\varepsilon+17t-17),\dots$$
$$\qquad \partial_{x_2}:\ 64(-\varepsilon+3t-3),\ 16(-2\varepsilon+7t-7),\ 2(-2\varepsilon+9t-9)$$ ✓✓
$$\Longrightarrow\ \text{链条件}\ \varepsilon>5.5(t-1)\ (\text{由 }11t-11-2\varepsilon<0\ \text{主导})\ \text{与}\ \varepsilon>4.5(t-1)\ \text{均被更强条件吸收}$$ ✓
$$\text{全1点值}:\ d_1(t,\varepsilon,1^4)=\frac{37t-22}{15}-\frac23\varepsilon<0\iff \varepsilon>\frac{37t-22}{10}$$ ✓✓
$$\textbf{R 约束}:\ S=9t-4-2\varepsilon\in(0,\min\{t,\tfrac12\})\iff \varepsilon\in\Bigl(\max\bigl\{4t-2,\tfrac{9t-4.5}{2}\bigr\},\ \tfrac{9t-4}{2}\Bigr)$$ ✓✓
$$\qquad \textbf{比较}:\ 4t-2>\tfrac{9t-4.5}{2}\ \text{与}\ 4t-2>\tfrac{37t-22}{10}\ \text{与}\ 4t-2>5.5(t-1)\ \text{对一切 }t<\tfrac12\ \textbf{成立}$$ ✓✓✓
$$\Longrightarrow\ \textbf{合并下界即 }4t-2\ \text{本身}\ (\text{本档最干净的一步})$$
$$\boxed{\text{定理（阶段 2）}:\ \forall t\in(\tfrac49,\tfrac12),\ \forall\varepsilon\in(4t-2,\ 0):}$$
$$\qquad (\text{i})\ \lambda(t,\varepsilon)\in R;\qquad (\text{ii})\ 9b-S=4+2\varepsilon<4\ \text{即}\ \boxed{\lambda(t,\varepsilon)\notin W}\ (\textbf{严格在 }R\setminus W\ \text{内});$$
$$\qquad (\text{iii})\ \forall\,1\le x_2\le x_3\le x_4\le x_5:\ d_1(t,\varepsilon,x)\le\frac{37t-22}{15}-\frac23\varepsilon<0 \Longrightarrow \textbf{Soules-1 判据恒失败}$$ ✓✓✓
$$\text{条带宽度}:\ 2-4t\in(0,\tfrac29)\ \text{随 }t\to\tfrac12\ \text{收缩到 }0\ (\text{与边界贴合的几何一致})$$ ✓
```

## §3 读法（严格，两个方向都不夸大）

```
$$\textbf{负向读法（已确立）}:\ \text{在贴近 }\partial W\ \text{的条带 }\varepsilon\in(4t-2,0)\ \text{内},\ \textbf{Soules-1 无法给出 }P2\ \text{证书}$$ ✓✓
$$\textbf{正向读法（本档定位）}:\ \text{该条带 }=\ \textbf{2026 }W\ \text{未覆盖、且自然构造机制被解析排除的"未决前沿"}$$\Longrightarrow \text{真正的靶区不只在 }\partial W,\ \text{而在这一条带（宽 }2-4t\text{）}$$ ✓✓
$$\textbf{⚠️ 不得写}:\ W_{\rm new}\supsetneq W\ \text{已得};\ \ \text{理由}:\ \text{本条带证的是"Soules-1 不可实现"，}\textbf{不是}"不可实现"$$ ⚠️⚠️
$$\text{要真正扩张 }W,\ \text{须在此条带内给出\textbf{与机制无关}的不可行论证（如把 2026 的"移位＋加权五环"外推）}$$ ✓✓
```

## §4 下一步（阶段 3）

```
$$\boxed{\text{(3a)}}\ \text{查 2026 原文论证对 }S\ \text{的依赖是否\textbf{有余量}}: \text{其判据 }4\le 9b-S\ \text{是否为紧界};\ \text{若证明中用到的估计在 }S\ \text{略减时仍成立} \Longrightarrow \textbf{可外推} \varepsilon<0$$ ✓✓
$$\boxed{\text{(3b)}}\ \text{反向}:\ \text{在条带内尝试 }P2（\text{换机制}:\ Soules\text{-}2/LS/ES\ \text{或直接矩阵构造）$$ ✓
$$\boxed{\text{(3c)}}\ \text{把条带结果登记为\textbf{靶区资产}（不宣称 }W\ \text{扩张）}$$ ✓
【⛔ 纪律】 本轮为**解析推导**（无搜索）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 的 `t<1` 判据与 §2 的 `4t-2` 合并下界为本行自证（sympy 逐式核实）；§3 的"不得写"条目为强制措辞 ✓

## §附 【技术词回查】（补录）
```
技术词 strip            命中文件数=28   :: ./p49-g26-accessibility-formalization.md ./E20-E40-zero-density-2026-read.md ./arp2-framework.md 
技术词 perturbation     命中文件数=12   :: ./p49-g273r2c-r2-close-prime-mech.md ./A5-2-phase-locking-sharpness-check.md ./p49-g273p1r3-stability-scan.md 
```
