已查地图：命中（`M03-linear-layer-closed-and-boundary-family-verified`）⟹ `Soules-1` 在 `\Lambda_*` 上的 `E` 型审计，不开新案
D0: 本档对象 = **`E1`–`E6` 执行记录**：`(11)` 式解析定式（变体判别）＋ `x_1=1` 归一化合法性（齐次性）＋ 递增域搜索（**未命中**）＋ **`max d_1=-106/375` 与解析结构（有用失败）** ＋ 下一步分叉
D1: 1（首次实现 Soules-1 判据并给出其在 `\Lambda_*` 上的失败残迹与结构）
[RESEARCH]

# **`Soules-1` 审计：`\Lambda_*` 上未找到证书**

## §1 `E1`–`E3`：定式与归一化

```
$$E1:\ \Lambda_*=\bigl(1,\tfrac{12}{25},\tfrac{12}{25},-\tfrac{41}{50},-\tfrac{41}{50}\bigr)\ \text{固定}$$ ✓
$$E2:\ \text{定理 9\ (11) 式逐字}: \boxed{d_i=\frac{x_i^2\lambda_1}{\sum_{j=1}^n x_j^2}+\sum_{k=i+1}^{n}\frac{(x_ix_k)^2\lambda_{n-k+2}}{\bigl(\sum_{j=1}^{k-1}x_j^2\bigr)\bigl(\sum_{j=1}^{k}x_j^2\bigr)}+\frac{\bigl(\sum_{j=1}^{i-1}x_j^2\bigr)\lambda_{n-i+2}}{\sum_{j=1}^{i}x_j^2}}$$ ✓✓
$$\textbf{⚠️ 解析式曾有两读}（\text{中项分母}:\ \text{两和之积}\ vs\ \text{两和之比}）;\ \textbf{用定理自带单调性判别}:$$
$$\qquad \text{变体 A（两和之积）}:\ 0<x_1\le\dots\le x_5\Rightarrow d_1\le\dots\le d_5\ \textbf{成立 }300/300;\qquad \text{变体 B（两和之比）}:\ \textbf{0/300}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\text{变体 A 为正确定式}（\text{以定理断言为判别器，非猜测}）}$$ ✓✓
$$E3:\ \text{齐次性}:\ \text{三项分别为 }0,\,0,\,0\ \text{次齐次} \Longrightarrow d_i\ \textbf{尺度不变} \Longrightarrow \boxed{x_1=1\ \text{合法}}$$ ✓✓
$$\qquad \text{搜索域}:\ 1=x_1\le x_2\le x_3\le x_4\le x_5\ (\text{递增是单调性断言的前提，缺一不可})$$ ✓✓
```

## §2 `E5`：递增域搜索（**未命中**）

```
$$\text{第一刀}:\ \text{含递减点（}r<1\text{）之网格}\ \Longrightarrow\ \text{虽有 }18595\ \text{"}d_1\ge0\text{"命中},\ \textbf{但全部违反单调性前提}（x\ \text{递减}）\Longrightarrow \textbf{作废}$$ ⚠️（自纠）
$$\text{第二刀（合法）}:\ x=(1,r,s,u,v),\ 1\le r\le s\le u\le v,\ \text{取值 }\{1,\tfrac32,2,\tfrac52,3,4,5,6,8,10,12,16,20,25,30,40,50,64,100\},\ \textbf{组合 }7315$$ ✓
$$\boxed{\max d_1=-\tfrac{106}{375}\approx-0.2827}\quad \text{在 }x=(1,1,1,1,1);\qquad d\ \text{向量}=\bigl(-\tfrac{106}{375},-\tfrac{106}{375},-\tfrac{106}{375},\tfrac{73}{125},\tfrac{73}{125}\bigr)$$ ✓✓
$$\qquad \text{单调性在该点成立（}\checkmark\text{）但前三项为负};\qquad \boxed{d_1\ge0\ \text{命中数}=0}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{Soules-1 在已搜索参数族中未找到证书}}\ (\textbf{不得}写成"Soules-1 不可实现")$$ ✓✓
```

## §3 `E6`：有用失败（**解析结构**）

```
$$\text{将 }d_1\ \text{按项拆开（}x_1=1,\ \lambda_1=1,\ \lambda_2=\lambda_3=\tfrac{12}{25},\ \lambda_4=\lambda_5=-\tfrac{41}{50}\text{）}:$$
$$\qquad A=\frac{1}{\sum x_j^2}\le\tfrac15;\qquad B=\lambda_5\frac{x_2^2}{1+x_2^2}\le\lambda_5\cdot\tfrac12=-\tfrac{41}{100}\ (\text{因 }x_2\ge x_1=1);$$ ✓✓
$$\qquad C=\lambda_4\frac{x_3^2}{(1+x_2^2)(1+x_2^2+x_3^2)}<0\ (\text{存在 }\ge-\tfrac{41}{100}\text{ 的下界});\qquad D,E=\lambda_3,\lambda_2\ \text{小正项}\ (\le\tfrac{12}{25}\cdot\tfrac1{12},\ \tfrac{12}{25}\cdot\tfrac1{20})$$ ✓
$$\text{在 }x=(1,1,1,1,1):\ d_1=\tfrac15-\tfrac{41}{100}-\tfrac{41}{300}+\tfrac1{25}+\tfrac{3}{125}=-\tfrac{106}{375}$$ ✓✓（逐项与实算一致）
$$\textbf{结论}:\ \text{负项 }B+C\ \text{由 }x_2\ge1\ \text{被强制};\ \text{正项 }A+D+E\ \text{受分母增长压制} \Longrightarrow \textbf{强暗示 }d_1<0\ \forall x$$ ⚠️
$$\qquad \textbf{但尚未证};\ \text{欲证需联合优化（}A+D+E\ \text{的最大化与 }B+C\ \text{同时不能逼近），}\ \text{我方仅得粗糙界 }0.07>0 \Longrightarrow \textbf{留作独立子问题}$$ ⚠️
```

## §4 状态与下一步分叉

```
$$\boxed{\Lambda_*\ \text{可实现性\textbf{仍未决}（本轮仅排除"由 Soules-1 证书实现"这条路径）}}$$ ✓✓
$$\boxed{\text{分叉}}:\ (i)\ \textbf{Soules 2\ (Thm 10)}\ \text{审计} —— \text{含划分，自由度更大};\ (ii)\ \textbf{LS／Ellard–Šmigoc 递归分裂};\ (iii)\ \textbf{解析不可能性}:\ \text{证 }d_1<0\ \forall x\ (\text{子问题},\ 见 \S3)$$
$$\qquad (iv)\ \text{与 Johnson 的 }D(t)<0\ \text{合并},\ \text{寻找\textbf{新解析不可实现不等式}（\text{这才是扩张 }W\ \text{的正途}）}$$ ✓✓
【⛔ 纪律】 本轮计算\textbf{仅限 }E\ \text{型证书审计}（有界、有理算术、可复核）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 的定式由**定理断言判别**（非猜测）；§2 的 }7315$$ 组为**有界搜索**，失败如实登记为 residue ✓

## §附 【技术词回查】（补录）
```
技术词 witness          命中文件数=62   :: ./KERNEL-HUNT-1-two-minimization-problems.md ./V2-28B-L52-mechanism-identified-verdict-OPEN.md ./E4-2-falsifiable-conditions-spec-for-line-enforcing-localization.md 
技术词 residue          命中文件数=52   :: ./grh-goldbach-paper-draft-v2.md ./TARGET-L9-source-fetch-report.md ./E218-residue-compression-audit-counterexample.md 
```
