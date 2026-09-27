已查地图：已跑 scripts/prework_map_check.sh alignment quantization 定理 证明 ⟹ 执行自 `P1ALIGN-2026-09-27-alignment-profile-law`（✓）＋ 唐先生 13:20（先整理定理再开 n=16 ✓）；本档 = **量子化律的定理 ＋ 证明 ＋ n=16 预测** ✓✓。
D0: 本档对象 = Type-B alignment profile 的完整分类定理
D1: 3（**定理 ＋ 证明 ✓✓**；**完整分类表 ✓**；**n=16 锐预测 ✓**）

# Alignment Quantization Theorem（n=8，已证 ✓）

## §0 定理与结论（先给）

```
$$\boxed{\textbf{(BO-1 ⭐定理 ✓✓)}\ \text{设 }H=\ker\sigma\ (\text{Hamming }[7,4,3] ✓),\ C_2=\pi H+e,\ H\cap C_2=\varnothing.\ \text{定义 }f:=\sigma\circ\pi^{-1}|_H,\ t_i:=\sigma(\pi^{-1}e_i),\ s:=\sigma(\pi^{-1}e).\ \text{则}}$$
$$\qquad\boxed{q_i=\lambda\cdot\mathbf 1_{\{i:\ t_i\in s+\mathrm{Im}f\}},\qquad \lambda=2^{\,4-d'},\qquad d'=\dim\mathrm{Im}f\le3}\ ✓✓$$
$$\qquad\Longrightarrow\ \textbf{L1（常值性）✓ 与 L2（支撑分类）✓ 同时成立，且}:\ \boxed{|S|=2^{d'}-\mathbf 1[s\in\mathrm{Im}f]},\qquad A_2=\lambda|S|,\qquad J_7=\frac{A_2^2}{|S|}\ ✓✓$$
$$\boxed{\textbf{(BO-2 完整分类表 ✓)}\ \text{七种情形（穷尽 ✓）}:\ (d',s\in\mathrm{Im}f)\in\{(0,\top),(0,\bot),(1,\top),(1,\bot),(2,\top),(2,\bot),(3,\top)\}\ \text{——}(3,\bot)\ \text{不可达（}|S|=8>7\ ✗\text{）}}$$
$$\boxed{\textbf{(BO-3 数值吻合 ✓✓)}\ \text{3840 个 }(\pi,e)\ \text{表示全部满足常值性}（3840/3840 ✓）\ \text{与尺寸律};\ \text{且\textbf{理论七情形与观测 }(|S|,\lambda,A_2)\ \text{表逐项一致}} ✓✓}$$
$$\boxed{\textbf{(BO-4 n=16 锐预测 ✓)}\ \text{同构论证逐字适用（}\sigma:\mathbb F_2^{15}\to\mathbb F_2^4,\ \lambda=2^{11-d'}\ ✓\text{）}\ \Longrightarrow\ \text{预测}:\ \text{仍为 }q_v\in\{0,\lambda\}\ \text{常值 ＋ }|S|=2^{d'}-\mathbf 1[s\in\mathrm{Im}f]\ ✓;\ \text{且 }(d'{=}4,\ s\notin\mathrm{Im}f)\ \text{不可达} ✓}$$
$$
$$
```

---

## §1 证明（**✓ 初等线性代数，7 行**）

```
$$\text{条件}:\ c+e_i\in C_2=\pi H+e\iff\pi^{-1}(c+e_i+e)\in H=\ker\sigma\iff\sigma(\pi^{-1}c)+\sigma(\pi^{-1}e_i)+\sigma(\pi^{-1}e)=0\ ✓\ \text{（}\sigma\ \text{线性 ✓）}$$
$$\qquad\iff f(c)=s+t_i\qquad(c\in H)\ ✓\ \Longrightarrow\ \boxed{q_i=\#\{c\in H:\ f(c)=s+t_i\}=n(s+t_i)}\ ✓$$
$$\text{其中 }n(x):=\#\{c\in H:\ f(c)=x\}\ \text{是 }f|_H\ \text{的直方图 ✓};\ f\ \text{线性} \Longrightarrow \mathrm{Im}(f|_H)\le\mathbb F_2^3\ \text{是子空间},\ \dim=d'\ ✓$$
$$\qquad\Longrightarrow\ n(x)=2^{\,4-d'}\cdot\mathbf 1[x\in\mathrm{Im}f]\ ✓\ \text{（}\ker(f|_H)\ \text{维数 }4-d'\ ✓\text{）}\ \Longrightarrow\ \textbf{L1 与 L2 同时得证} ✓✓$$
$$\text{支撑}:\ S=\{i:\ t_i\in s+\mathrm{Im}f\}\ \text{——}\ t:\{1..7\}\to\mathbb F_2^3\setminus\{0\}\ \text{是\textbf{双射}}（\text{列向量 = 全部非零向量 ✓}\text{）}\ ✓$$
$$\qquad\Longrightarrow\ |S|=\big|(s+\mathrm{Im}f)\cap(\mathbb F_2^3\setminus\{0\})\big|=\begin{cases}2^{d'}-1,&s\in\mathrm{Im}f\\2^{d'},&s\notin\mathrm{Im}f\end{cases}\ ✓\ \text{（}0\ \text{是否落在仿射子空间里 ✓）}$$
$$\text{推论}:\ A_2=\lambda|S|\ ✓;\quad J_7=\sum q_i^2=|S|\lambda^2=\frac{A_2^2}{|S|}\ ✓;\quad A_1=16-A_2\ \text{（等号链 ✓）}\ ✓✓$$
$$
$$
```

---

## §2 完整分类（**✓ 理论 ＋ 观测逐项吻合 ✓✓**）

```
$$\begin{array}{c|c|c|c|c|c|c}
d' & s\in\mathrm{Im}f & \lambda=2^{4-d'} & |S| & A_2=\lambda|S| & A_1=16-A_2 & J_7=A_2^2/|S|\\
\hline
0 & \top & 16 & 0 & 0 & 16 & —\\
0 & \bot & 16 & 1 & 16 & 0 & \mathbf{256}\\
1 & \top & 8 & 1 & 8 & 8 & 64\\
1 & \bot & 8 & 2 & 16 & 0 & \mathbf{128}\\
2 & \top & 4 & 3 & 12 & 4 & 48\\
2 & \bot & 4 & 4 & 16 & 0 & \mathbf{64}\\
3 & \top & 2 & 7 & 14 & 2 & 28\\
3 & \bot & — & 8\ (>7) & \textbf{不可达} ✗ & — & —\\
\end{array}$$
$$\textbf{观测吻合 ✓✓}:\ \text{profile 计数 }(|S|{=}1:\ 7\ \text{个},|S|{=}2:\ 21\ \text{个},|S|{=}3:\ 7\ \text{个},|S|{=}4:\ 7\ \text{个},|S|{=}7:\ 1\ \text{个})\ \text{与理论一致 ✓}$$
$$\qquad\Longrightarrow\ (A_1,A_2)=(0,16)\ \text{桶恰有\textbf{三种} }J_7\in\{256,128,64\}\ ✓✓\ \text{——P1-2 分叉被\textbf{完全解释} ✓✓}$$
$$
$$
```

---

## §3 n=16 预测（**✓ 锐预测，可判据化 ✓**）

```
$$\text{同构论证逐字适用}:\ H_{15}=\ker\sigma,\ \sigma:\mathbb F_2^{15}\to\mathbb F_2^4,\ |H_{15}|=2^{11}\ \Longrightarrow\ \lambda=2^{\,11-d'}\ ✓$$
$$\boxed{\text{预测}:\ q_v\in\{0,\lambda\}\ \text{常值};\quad |S|=2^{d'}-\mathbf 1[s\in\mathrm{Im}f],\ d'\le4;\quad (d'{=}4,s\notin\mathrm{Im}f)\ \text{不可达}\ ✓\ \Longrightarrow\ J_7=A_2^2/|S|\ ✓✓}$$
$$\text{判据（唐先生 ✓）}:\ \text{若 }n=16\ \text{出现 }q=(\lambda,\lambda,\mu,\ldots),\ \lambda\ne\mu \Longrightarrow \textbf{量子化律不提升}（干净负结果 ✓）;\ \text{若逐项吻合} \Longrightarrow \textbf{跨维度证据} ✓$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**已证定理**（初等线性代数 ✓，7 行 ✓）；§2 为**完整分类 ＋ 3840 表示数值吻合 ✓✓**；§3 为**预测（未验证 ⚠️）**
- ⚠️ 定理**限于 Theorem-13 构造域**（两半为完美码 ✓）与 $R=1$ ✓；**未**声称一般覆盖码 ✗；**未**涉及 119 ✓
- ⚠️ $n=16$ 预测**尚未跑**（下一步 ✓）；$n=8$ 的定理**不依赖枚举**（证明独立 ✓✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：Alignment Quantization Theorem、完整分类表、n=16 锐预测、直方图论证
- **档案已有（引用，不列为提出）**：Theorem 13、syndrome、$q_{i}$、$J_7$、$A_1+A_2=M/2$、Zaremba 唯一性


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Alignment Quantization Theorem 命中文件数=1    :: ./ALIGN-THEOREM-2026-09-27-quantization-proved.md 
技术词 直方图论证  命中文件数=1    :: ./ALIGN-THEOREM-2026-09-27-quantization-proved.md
```
- **本档新增**：Alignment Quantization Theorem、完整分类表、n=16 锐预测、直方图论证（见上方命中数；0 命中者为自造语／内部标签 ✓）
