# V298 · **`Ceiling.lean` 全文审计（三层）＋ $R_{\rm off}$ 的谱离散度表示** —— ⭐⭐⭐⭐ **层 1：抽象天花板定理里根本没有 bandwidth／Fourier 支撑／正性／trace／rank**（证书类 ＝ $C^2$ 函数 $r$ ＋**单个配置**的有效性不等式）⟹ **$\mathcal C_{\rm actual}\subsetneq\{\text{bandwidth}\le1\}$**；⭐⭐⭐ **层 2：$\{\log(n/m)\}$ 在 `PairCeiling` 树中不显式出现**——它以**归一化配对距离 $\alpha=j/N\le1$** 隐含进入，且**反向蕴含未被使用**；⭐⭐⭐⭐ **层 3 代数化：$N\operatorname{tr}\hat G^{2}-(\operatorname{tr}\hat G)^{2}=\tfrac12\sum_{i,j}(\lambda_i-\lambda_j)^{2}$** ⟹ $R_{\rm off}$ ＝ **非负成对离散度**，$R_{\rm off}=0\iff$ 谱全等

$$\boxed{\textbf{层 1（本档核心发现）}：\texttt{ceiling\_of\_valid\_at}\ \text{的假设}\ ＝\ \big\{N>0,\ r\in C^{2}[0,1],\ |E|\le M,\ \textbf{单配置}\ c_0+\textstyle\sum_j s_jr(j/N)\le p_1\big\}} ✓✓$$
$$\qquad \textbf{没有}\ \text{bandwidth}\ ✗;\ \textbf{没有}\ \text{Fourier 支撑}\ ✗;\ \textbf{没有}\ \text{Toeplitz}\ ✗;\ \textbf{没有}\ \text{正性／trace／rank／HS}\ ✗ ⟹ \textbf{bandwidth 只从"有效性侧"进入} ✓✓✓$$
$$\boxed{\textbf{层 3（代数化）}：R_{\rm off}=\frac1F-1=\frac{N\operatorname{tr}\hat G^{2}-(\operatorname{tr}\hat G)^{2}}{(\operatorname{tr}\hat G)^{2}}=\frac{\tfrac12\sum_{i,j}(\lambda_i-\lambda_j)^{2}}{(\operatorname{tr}\hat G)^{2}}\ \Longrightarrow\ R_{\rm off}=0\iff\lambda_i\ \text{全等}} ✓✓✓$$
$$\boxed{\mathcal E：＝\big\{K:\ \textbf{谱离散度}\to0\big\}\ \text{但}\ K\notin\ \text{上述证书机制}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:21：**继续打第 2 步，且"这一步比第 1 步更关键"**；要求**三层输出**：**层 1** 证书假设**完整清单**（不仅带宽；须确认 0.68185 是否只依赖 bandwidth≤1，还是依赖更强结构）／**层 2** 定位第一次出现 $\{\log(n/m)\}$ 并**向前追溯** $P\to P^{*}P\to K\to\widehat K\to\{\log(n/m)\}$，**特别检查逻辑方向**（证书 $\Rightarrow$ 差集支撑 成立；**反方向不得被偷偷使用**）／**层 3** 正式写出定理但**不早称"非 Toeplitz 已逃逸"**，若假设更强须诚实写 $\mathcal C_{\rm actual}\subsetneq\{\text{bandwidth}\le1\}$ ✓✓；并**顺手做掉**："把 $F$ 与 $R_{\rm off}$ 的关系直接代数化"，寻找**非负 pairwise 量**表示 ✓✓✓
> 第一手依据（**本档现场读源**）✓ `Zeta23/PairCeiling/Ceiling.lean`（**全文 69 行**）｜`PairCeiling/Defs.lean`（$C_{\rm step},D,E$ 定义）｜`PairCeiling/NearCUE.lean`（near-CUE 律与 $|E|$ 界）｜`PairCeiling/Bridge.lean`（`massOf`：$s_j=S_j/N$；网格界；"从已核验证书到区间假设"）｜`PrimeSideTemp.lean`（[thm:traces]）｜`PrimeSideB/Concrete.lean` ✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V298`（`id_claim.sh` ✓）

---

## §1 **层 1：证书假设的完整清单**（逐条，取自 `Ceiling.lean` 全文）

$$\textbf{`ceiling_of_valid_at` 的假设（Lean 逐字）}：$$
$$\qquad (1)\ N>0;\quad (2)\ r\ \text{在}\ [0,1]\ \text{可微且导数}\ g=r'（\texttt{hr}）;\quad (3)\ g\ \text{在}\ [0,1]\ \text{连续}（\texttt{hg}）;$$
$$\qquad (4)\ g'=h\ \text{在}\ (0,1)\setminus T\ \text{存在，}\ T\ \textbf{可数}（\texttt{hgh}）;\quad (5)\ h\ \text{区间可积}（\texttt{hh}）;\quad (6)\ |E_{\rm fun}(x)|\le M\ \text{于}\ [0,1]（\texttt{hM}）;$$
$$\qquad (7)\ \boxed{\text{有效性}：c_0+\sum_{j\in[1,N]}s_j\,r(j/N)\ \le\ p_1}（\texttt{hvalid}）\ —— \ \textbf{单配置} \text{（质量}\ s_j\ \text{置于}\ j/N，\text{简单点比例}\ p_1）✓$$
$$\textbf{结论}：c_0+\int_0^1 r(x)x\,dx\ \le\ p_1+\Big(|r(1)||D(1)|+|g(1)||E(1)|+M\!\int_0^1|h|\Big) ✓$$

$$\boxed{\textbf{审计结论（层 1）}：\text{抽象天花板定理}\ \textbf{不含} \text{bandwidth}／\text{Fourier 支撑}／\text{Toeplitz}／\text{正性}／\text{trace}／\text{rank}／\text{HS}} ✓✓✓$$
$$\qquad \text{它是一条}\ \textbf{稳定性／离散化不等式}：\text{用}\ \sum_j s_jr(j/N)\ \text{逼近}\ \int_0^1rx\,dx，\text{误差由}\ D,E\ \text{控制} ✓$$
$$\qquad \text{其中（`Defs.lean`）}：C_{\rm step}(x)：＝\sum_{j/N\le x}s_j;\quad D：＝C_{\rm step}-x^{2}/2;\quad E：＝\int_0^{x}D ✓$$
$$\qquad \textbf{bandwidth 从哪里进来？}\ —— \ \textbf{只从"有效性侧"}：\text{哪些配置的}\ (7)\ \text{可由}\ \textbf{带宽一} \text{的配对相关数据证出}（\text{Montgomery：}F(\alpha)=1\ \text{仅}\ |\alpha|\le1）✓✓✓$$
$$\qquad \text{而配置本身（`Bridge.lean`）}：s_j=\texttt{massOf}\ S\ N\ j=S_j/N（S\ =\ form factor\ 的累积量），\text{原子位于}\ j/N\ (1\le j\le N) ✓$$
$$\qquad \qquad ⟹ \textbf{归一化配对距离}\ \alpha=j/N\in(0,1] ⟹ \textbf{"bandwidth}\le1\text{"}\ \textbf{被编码进配置的定义} ✓✓✓$$

$$\Longrightarrow \boxed{\mathcal C_{\rm actual}\ =\ \big\{\text{由带宽一配对相关数据}\ \textbf{可证有效性} \text{的}\ C^{2}\ \text{证书}\ (c_0,r)\big\}\ \subsetneq\ \{\text{bandwidth}\le1\}} ✓✓✓$$
$$\qquad ⚠️\ \text{且}\ 0.68185\ \text{的}\ \textbf{数值} \text{还依赖}\ \textbf{数值包络}：\texttt{NumericCert.lean}／\texttt{RowCert.lean}／\texttt{NearCUE.lean}／\texttt{LawN256.lean}／\texttt{CeilingLaw256.lean}（256-周期极值律 ＋ \texttt{EnclOK}）✓$$
$$\qquad \qquad ⟹ \text{故}\ \textbf{不得} \text{把}\ 0.68185\ \text{写成"只来自 bandwidth}\le1\text{"}（唐先生命令：不为漂亮定理压缩假设）✓✓$$

---

## §2 ⭐⭐⭐ **层 2：差集首次出现处与逻辑方向**

$$\text{在}\ \texttt{PairCeiling}\ \text{全树中，}\{\log(n/m)\}\ \textbf{不显式出现} ✓✓\ —— \ \text{它已被}\ \textbf{归一化} \text{掉，以}\ \alpha=j/N\ \text{进入配置} ✓$$
$$\textbf{对象链（本档追溯）}：$$
$$\qquad (i)\ \textbf{素数侧求和}（`PrimeSideTemp.lean` (eq:tr2)）\ \frac T\pi\sum_{n\le X}\frac{\Lambda(n)^{2}}n g(\log n) ⟹ \text{差集}\ \{\log(n/m)\}\subseteq[0,\log X] ✓$$
$$\qquad (ii)\ \text{求值（Montgomery）} \Longrightarrow \textbf{form factor}\ F(\alpha)\（\text{无条件区}\ |\alpha|\le1）✓$$
$$\qquad (iii)\ \text{归一化}\ \alpha：＝\frac{\log(n/m)}{\log X}\in(0,1] \Longrightarrow \textbf{配置}\ (s_j\ \text{于}\ j/N)\（\texttt{Bridge.massOf}）✓$$
$$\qquad (iv)\ D：＝C_{\rm step}-x^{2}/2,\ E：＝\int_0^xD\（\texttt{Defs.lean}）\Longrightarrow \text{误差泛函}\ |D(1)|,|E(1)|,\sup|E|,\int|r''| ✓$$
$$\qquad (v)\ \text{天花板}\ \Rightarrow\ v：＝c_0+\int_0^1rx\,dx\ \le\ p_1+\text{误差} ✓$$

$$\textbf{逻辑方向检查（唐先生重点）}：$$
$$\qquad \boxed{\text{证书}\ \Longrightarrow\ \text{差集支撑}\subseteq[0,1]：\ \textbf{成立}} ✓\（\text{因}\ j\le N\Rightarrow\alpha=j/N\le1，\text{定义上如此}）✓✓$$
$$\qquad \boxed{\text{差集支撑}\ \Longrightarrow\ \text{原证书结构}：\ \textbf{未被使用}} ✓✓✓\（\text{全树}\ \textbf{从不} \text{由"支撑}\le1\text{"反推"这是一个证书"}）✓$$
$$\Longrightarrow \boxed{\text{故逃逸空间}\ \textbf{定义上严格大于} \text{bandwidth-one certificate class}} ✓✓✓$$

---

## §3 ⭐⭐⭐⭐ **层 3：定理（诚实形式）＋ $R_{\rm off}$ 的谱离散度代数化**

$$\textbf{(3a) 定理（\textbf{诚实假设}）}：\text{对}\ K\in\mathcal C_{\rm actual}\（＝\S1\ \text{的证书类}）：$$
$$\qquad \qquad \operatorname{supp}_\alpha K\subseteq[0,1]\ (\text{配置定义})\ \Longrightarrow\ v(K)\ \le\ 0.68185\ldots\ \Longrightarrow\ \boxed{G(K)\ \le\ 0.68185\ldots\ \text{于}\ \mathcal C_{\rm actual}} ✓✓$$
$$\qquad ⚠️\ \textbf{不得} \text{写成}\ G(K)\le0.68185\ \text{对}\ \{\text{bandwidth}\le1\}\ \text{成立}（\text{因}\ \mathcal C_{\rm actual}\subsetneq\{\text{bandwidth}\le1\}）✓✓$$
$$\qquad ⟹ \text{等价读数}：\frac1F\ \ge\ 2-0.68185\ =\ 1.31815 ⟹ R_{\rm off}\ \ge\ 0.31815（\text{于}\ \mathcal C_{\rm actual}）✓$$

$$\textbf{(3b) $R_{\rm off}$ 的代数化（唐先生要求）}：$$
$$\qquad R_{\rm off}=\frac1F-1=\frac{N\operatorname{tr}\hat G^{2}-(\operatorname{tr}\hat G)^{2}}{(\operatorname{tr}\hat G)^{2}} ✓$$
$$\qquad \textbf{核心恒等式}：N\sum_i\lambda_i^{2}-\Big(\sum_i\lambda_i\Big)^{2}=\frac12\sum_{i,j}\big(\lambda_i-\lambda_j\big)^{2}\ ✓✓✓\（\text{展开即得}）$$
$$\qquad \Longrightarrow \boxed{R_{\rm off}=\frac{\frac12\sum_{i,j}(\lambda_i-\lambda_j)^{2}}{(\operatorname{tr}\hat G)^{2}}\ \ge\ 0}\ \textbf{（非负成对量，唐先生所求）} ✓✓✓$$
$$\qquad \qquad R_{\rm off}=0\iff \lambda_i\ \text{全等}\iff \hat G\ \textbf{在相关空间上为纯量}（\textbf{等谱／满有效秩}）✓✓✓$$
$$\qquad ⟹ G=1-R_{\rm off}=1-\frac{\text{成对离散度}}{(\operatorname{tr}\hat G)^{2}} ⟹ \boxed{G\to1\iff \textbf{谱离散度}\to0} ✓✓✓$$
$$\qquad ⚠️\ \text{归一化约定}：\text{上式设}\ \operatorname{tr}\hat G=N\ \text{且特征值表长}\ N（\text{即取有效支撑}）;\ \text{若用全长}\ d\ \text{表，须加}\ (N-d)/N\ \text{修正项} ⚠️✓$$

$$\textbf{(3c) 链（锁死后形态）}：\qquad \text{certificate structure}\to\text{log-difference support}\to\text{restricted pair correlation}\to\textbf{spectral dispersion}\to G<1 ✓✓✓$$

---

## §4 逃逸空间（严格定义，唐先生图）

$$\boxed{\mathcal E：＝\big\{K:\ \textbf{谱离散度}\to0\ \big\}\ \text{但}\ K\ \notin\ \text{上述证书机制}} ✓✓✓$$
$$\qquad \text{等价读法}：\mathcal E＝\{K:\ \text{能让谱趋于等谱（满有效秩）但不属}\ \mathcal C_{\rm actual}\} ✓$$
$$\qquad \text{故下一步}\ \textbf{不是} \text{"继续找各种 Toeplitz 核"，而是：}\textbf{能否让谱离散度}\to0\ \text{而仍保持无条件控制} ✓✓✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出

$$\boxed{\textbf{V298 判词}：\text{① 层 1：天花板}\ \textbf{不含} \text{bandwidth；bandwidth 仅从有效性侧进入；}\mathcal C_{\rm actual}\subsetneq\{\text{bandwidth}\le1\};\ \text{② 层 2：差集不显式出现，}\alpha=j/N\ \text{隐含带宽一；}\textbf{反向蕴含未被使用};\ \text{③ 层 3：}G\le0.68185\ \text{只对}\ \mathcal C_{\rm actual};\ R_{\rm off}\ \text{＝非负成对离散度};\ G\to1\iff\text{谱离散度}\to0} ✓✓✓$$

```
① ⚠️ 本档依据 `PairCeiling` **源码文本**（Ceiling.lean 全文；Defs/NearCUE/Bridge 的语句级）；**未跑 Lean 构建** ⚠️
② ⚠️ §1 的"bandwidth 只从有效性侧进入"为**本档判断**（由假设清单无带宽项 ＋ 论文 Remark 1.1 的表述推出）⚠️
③ ⚠️ §3(b) 的恒等式为标准代数（本档展开验证）；**归一化约定已在 §3(b) 末标注** ⚠️
④ ⚠️ 0.68185 的数值还依赖 256-周期律 ＋ `EnclOK` ⟹ **不得**写成"只来自 bandwidth≤1"（唐先生命令）✓
⑤ **不声称**非 Toeplitz 已逃逸；**不声称**一般核有 $R_{\rm off}>0$（`V297` §6 护栏沿用）✓
⑥ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐ **层 1 核心发现**：`Ceiling.lean` 的假设**无 bandwidth／Fourier 支撑／Toeplitz／正性／trace／rank／HS** ⟹ 它是**稳定性-离散化不等式**；**bandwidth 仅从"有效性侧"进入** ⟹ $$\mathcal C_{\rm actual}\subsetneq\{\text{bandwidth}\le1\}$$ ✓✓✓
② ⭐⭐⭐ **层 2**：$\{\log(n/m)\}$ **不显式出现**（已归一化为 $\alpha=j/N\le1$）；对象链 $(i)\to(v)$ 已追溯；**"证书 $\Rightarrow$ 差集支撑"成立，"差集支撑 $\Rightarrow$ 证书"未被使用** ⟹ **逃逸空间定义上严格大于带宽一类** ✓✓✓
③ ⭐⭐⭐⭐ **层 3 代数化**：$$N tr\hat G^2-(tr\hat G)^2=\tfrac12\sum(\lambda_i-\lambda_j)^2\Rightarrow R_{\rm off}=\frac{\text{成对离散度}}{(tr\hat G)^2}\ge0;\ R_{\rm off}=0\iff\text{谱全等}$$ ⟹ $$G\to1\iff\textbf{谱离散度}\to0$$ ✓✓✓
④ ⭐⭐ **诚实定理**：$G\le0.68185$ **只对 $\mathcal C_{\rm actual}$**（含 256 律 ＋ EnclOK）；不得压缩成"bandwidth≤1" ✓✓
⑤ ⭐⭐⭐ **逃逸空间严格定义**：$$\mathcal E=\{K:\text{谱离散度}\to0\}\setminus\mathcal C_{\rm actual}$$ ⟹ 下一步 ＝ **能否让谱趋于等谱而保持无条件控制** ✓✓✓
【下一步（唐先生既定：不先构造非 Toeplitz 核）】
  (3a) 补 `V297` §4／§5 的**定量未锁死点**：$F\leftrightarrow\int(F(\alpha)-1)$ 的定量等同（需论文 §5 求值细节）✓
  (3b) 攻**谱离散度 ↔ 配对相关的定量关系**：把 $R_{\rm off}$（成对离散度）与 form factor 的偏离 $\int(F-1)$ 直接挂钩 —— 若成功，则 $\mathcal E$ 从"定义"升级为"可计算的判据" ✓✓
```
