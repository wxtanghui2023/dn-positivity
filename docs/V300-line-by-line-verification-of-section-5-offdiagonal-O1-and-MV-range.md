# V300 · **(4a) §5 逐行核验：离对角 $\mathcal O_1$ 与 MV 适用域** —— ⭐⭐⭐⭐ **判为情形 A**（源码级确认）：离对角被**尺寸型**不等式（Montgomery–Vaughan ＋ Chebyshev）压进误差，**相对量级 $\asymp T^{\lambda-1}/L\to0$**（$\lambda\le1$）⟹ **主项确由证书几何决定，配对相关不进主项**；⭐⭐⭐ **附加发现：AF 常数是"最坏情形几何常数"，离对角**不使用**配对相关

$$\boxed{\textbf{情形 A（本档，源码级）}：\mathcal O_1\ \ll\ L^{2}X,\qquad \text{主项}\ \asymp\ TL^{3}\ \Longrightarrow\ \frac{\mathcal O_1}{\text{主项}}\asymp\frac{T^{\lambda-1}}{L}\ \to\ 0\ (\lambda\le1)} ✓✓✓$$
$$\boxed{\text{故}\ V299\ \text{的核心判词（}F_{\rm eff}=c^{\rm geom}_\phi+o(1)\text{）}\ \textbf{成立};\ \text{且强于原[推断]：离对角由}\ \textbf{尺寸型} \text{不等式压掉，}\textbf{不用配对相关}} ✓✓✓$$
$$\boxed{\textbf{附加发现}：AF\ \text{常数}\ ＝\ \textbf{最坏情形（universal）几何常数}，\text{非配对相关均值} \Longrightarrow \text{解释其鲁棒性}\ \&\ \textbf{不可由算术输入改进}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:26：**先打 (4a)，不能跳**；**唯一支点是** $\operatorname{tr}\widetilde G^{2}=\frac{TL}{2\pi}(\ell_1^{2}+\frac{L^{2}}3)(1+O(\mathcal E_T))$ 是否真意味着"主项完全由证书几何决定"；**必须读 §5 的求值过程，不能从最终两形式反推** ✓；**要找的是"第一次把 $n\ne m$ 消掉／吸收到误差项的地方"**；三情形 **A**（离对角真低阶）／**B**（离对角被某平均恒等式重编码）／**C**（某未显式输入已把配对相关假定掉 ⟹ V299 判词须回滚）✓✓✓
> 第一手依据（**本档现场读源码**）✓ `Zeta23/PrimeSideB/PPOffDiag.lean`（**全文 173 行**：[prop:PP] 𝒪₁ §5.4）｜`PrimeSideB/PPKernel.lean`（`sub_mul_Aminus_eq`／`abs_*_le`／`MV_real`／`MV_size_le`）｜`Zeta23/MV.lean`（**`MVHilbert_of_diag : 0 ≤ C → MVDiag C → MVHilbert (2*C)`**）｜`Zeta23/Hypotheses.lean`（`PaperInputs.MV : ∃ C > 0, MVHilbert C`）｜`Zeta23/Final.lean`（`PaperInputs.of_lit … (exists_MVHilbert_of_diag hMV) …`）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V300`（**编号带已扩至 V101–V399**，治理留痕 ✓）

---

## §1 逐行链条（把 $n=m$ 与 $n\ne m$ 的分离钉死）

$$\textbf{(i) 定义（[prop:PP] 𝒪}_1\text{，§5.4）}：\ \mathcal O_1：＝\sum_{n\ne m\le X}a_na_m\,A^{-}\!\big(\log n,\log m\big) ✓$$
$$\qquad \text{其中}\ A^{-}\:＝\ \mathcal M[\cos(\cdot y_n),\cos(\cdot y_m)]\ \text{的}\ \textbf{差频半部};\ \text{系数}\ a_k\:＝\ \text{（素数侧）}\ \Lambda\ \text{型权重} ✓$$
$$\textbf{(ii) 关键恒等式（`PPKernel.sub_mul_Aminus_eq`）}：\ \theta：＝y-y'\ (\ne0)：$$
$$\qquad \theta\cdot A^{-}(y,y')=\textbf{8 项显式组合}：\ \mathrm{trig}(\theta\cdot cT)\cdot M(y\ \text{or}\ y'),\quad \mathrm{trig}\in\{\sin,\cos\},\ c\in\{1,2\},\ M\in\{C_p,S_p,C_m,S_m\} ✓$$
$$\qquad \qquad （M\ ＝\ \Phi^{2}\ \text{的半线矩}）;\qquad \text{并有}\ |M(y)|\le\int_{\mathbb R}\Phi^{2}\：＝\ W ✓$$
$$\textbf{(iii) 除以}\ \theta：\text{因}\ n\ne m\Rightarrow\log n\ne\log m（\log\ \text{单射}）\Longrightarrow \text{可除} \Longrightarrow \textbf{8 个 MV 型求和}\ S_1,\dots,S_8 ✓$$
$$\textbf{(iv) 每个求和的界（`MV_real` ＋ `MV_size_le`）}：\ \Big|\sum_{n\ne m}u_nv_m\frac{\mathrm{trig}\big(c(y_n-y_m)\big)}{y_n-y_m}\Big|\le C\sqrt{\textstyle\sum 2n\,u_n^{2}}\sqrt{\textstyle\sum 2n\,v_n^{2}} ✓$$
$$\qquad \text{取}\ \{u,v\}=\{a,\,a\cdot w\},\ |w|\le W \Longrightarrow \le 2C\,W\,\textstyle\sum_{n\le X}\Lambda(n)^{2}\：＝\ 2C\,W\,\Lambda_2 ✓$$
$$\qquad \Longrightarrow \text{八项合计}：\ \boxed{|\mathcal O_1|\ \le\ 8\cdot 2C\,W\,\Lambda_2\ =\ 16\,C\,W\,\Lambda_2} ✓✓$$
$$\textbf{(v) 代入尺寸}（`PPOffDiag.lean` 文档头逐字）：\ \Lambda_2=\sum\Lambda(n)^{2}\ll X\log X=XL;\quad W=\int\Phi^{2}=2\pi bL\le2\pi L ✓$$
$$\qquad \Longrightarrow \boxed{\mathcal O_1\ \ll\ L^{2}X} ✓✓✓$$

---

## §2 ⭐⭐⭐⭐ 量级比较（本档）：判为**情形 A**

$$\text{主项（(eq:tr2) 第二形式）}：\frac{TL}{2\pi}\Big(\ell_1^{2}+\frac{L^{2}}3\Big);\qquad \ell_1=\frac L{\lambda_1}\asymp\frac L\lambda \Longrightarrow \text{主项}\ \asymp\ T\,L^{3}\ (\lambda\asymp1) ✓$$
$$\text{离对角}：\mathcal O_1\ \ll\ L^{2}X=L^{2}T^{\lambda}\ ✓$$
$$\Longrightarrow \frac{\mathcal O_1}{\text{主项}}\ \asymp\ \frac{L^{2}T^{\lambda}}{TL^{3}}\ =\ \boxed{\frac{T^{\lambda-1}}{L}}\ ✓$$
$$\qquad \lambda<1：T^{\lambda-1}\to0 ✓;\qquad \lambda=1：\frac1L\to0 ✓\qquad \Longrightarrow\ \boxed{\text{离对角}\ \textbf{确为低阶}}\ ✓✓✓$$
$$\Longrightarrow \boxed{\textbf{情形 A 成立}}：\text{主项由}\ \textbf{对角评估（证书几何）} \text{决定};\ F_{\rm eff}=c^{\rm geom}_\phi+o(1)\ \text{得到确认} ✓✓✓$$
$$\qquad \textbf{不是 B}（\text{未出现"离对角被平均恒等式重编码"的步骤 —— 它是被}\ \textbf{上界吸收} \text{的}）✓$$
$$\qquad \textbf{不是 C}（\text{无"某未显式输入已假定配对相关"之处} —— \text{见 §3}）✓✓$$

---

## §3 ⭐⭐⭐ 附加发现（本档，强于 `V299` 的 [推断]）

$$\textbf{关键}：\text{MV 型不等式}\ \textbf{只用}\ \ell^{2}\ \text{范数}（\sqrt{\sum 2n u_n^{2}}\ \text{型}）⟹ \textbf{不含任何配对相关内容} ✓✓✓$$
$$\qquad ⟹ \text{离对角不是"被配对相关评估后压进误差"，而是被}\ \textbf{尺寸型不等式}\ \text{直接压掉} ✓✓$$
$$\qquad \Longrightarrow \boxed{\text{AF 常数}\ ＝\ \textbf{最坏情形（universal）几何常数}，\text{而非配对相关的平均}} ✓✓✓$$
$$\qquad \qquad \text{推论（解释）}：\text{① 这解释了它的}\ \textbf{鲁棒性与无条件性};\ \text{② 也解释了它}\ \textbf{不可能} \text{由更好的算术输入（配对相关）改进} ⟹ \text{与}\ `V299`\ \text{§4 的反例}\ \textbf{互证} ✓✓✓$$
$$\qquad \qquad \text{（}\ `V299`\ \text{说"理想}\ F\equiv1\ \text{仍给}\ R_{\rm off}=0.3275>0\text{"};\ \text{本档说"离对角根本不用}\ F\text{"} ⟹ \text{两者}\ \textbf{同向且更强}）✓$$
$$\textbf{对 V299 §2 的两处细化}：$$
$$\qquad \text{(a) 误差层是}\ \textbf{界}（16C\,W\,\Lambda_2）,\ \textbf{不是} \text{配对相关的评估} ⟹ V299\ \text{"}F_{\rm pair}\ \text{只进误差层"应改为"}\textbf{根本不用}\ F_{\rm pair}" ✓✓$$
$$\qquad \text{(b) bandwidth}\ \text{条件}\ \textbf{不经} \text{配对相关进入，而经}\ \textbf{MV 的适用域} \text{进入（见 §4）} ✓✓$$

---

## §4 bandwidth 条件在哪一环进入？（[推断]，标注级别）

$$\text{链条}：\underbrace{\text{MVDiag}\ C}_{\text{文献形式 Montgomery–Vaughan，`PaperInputs.MV`}}\xrightarrow{\ \texttt{MVHilbert\_of\_diag}\ }\text{MVHilbert}(2C)\xrightarrow{\ \texttt{MV\_real}\ }\text{8 项界}\xrightarrow{\ \text{Chebyshev}\ }\mathcal O_1\ll L^{2}X ✓$$
$$\qquad ⚠️\ \text{MVDiag}\ \text{在形式化中是}\ \textbf{输入}（`PaperInputs.MV`），\text{即}\ \textbf{经典 MV 不等式 ＋ 其适用域} \text{未形式化} ⚠️$$
$$\qquad \text{本档判断（[推断]）}：\text{MV／二阶矩法的适用域}\ ＝\ \log X\le L\iff X\le T\iff\lambda\le1 ⟹ \textbf{bandwidth 条件在此进入} ✓✓$$
$$\qquad \qquad \text{依据}：\text{经典二阶矩法要求多项式的指数跨度}\ \le\ \text{区间长度};\ \text{论文取}\ L=\lambda l\ (\lambda\le1)\ \text{正与此对应} ✓$$
$$\qquad \text{且 MV 是}\ \textbf{纯调和分析} \text{不等式（无需 RH）} ⟹ \text{这解释了"无 mollifier／无密度／无零自由区"的输入减法} ✓✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V300 判词}：\text{① 情形 A（源码级确认）};\ \text{② 离对角由尺寸型不等式压掉，}\textbf{不用配对相关};\ \text{③ AF 常数 ＝ 最坏情形几何常数};\ \text{④ V299 核心判词成立，且两处细化}} ✓✓✓$$

```
① ⚠️ 本档依据 **Lean 源码文本**（`PPOffDiag.lean` 全文 ＋ `MV.lean`／`Hypotheses.lean`／`Final.lean` 语句级）；**未跑构建** ⚠️
② ⚠️ `MVDiag`／MV 适用域为**输入（PaperInputs）** ⟹ §4 的"bandwidth 经 MV 适用域进入"为 **[推断]**，未形式化核验 ⚠️
③ ⚠️ §2 的量级比较为本档计算（$\ell_1\asymp L/\lambda$、$\Lambda_2\ll XL$、$W\le2\pi L$ 皆取自源码注释／经典）⚠️
④ **不声称** 论文无其它隐含输入（只核验了 §5.4／[prop:PP] 这一环）✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐ **情形 A**：$\mathcal O_1\ll L^2X$ vs 主项 $\asymp TL^3$ ⟹ 相对 $\asymp T^{\lambda-1}/L\to0$ ⟹ **离对角确为低阶** ⟹ **V299 核心判词（主项由证书几何决定）源码级成立** ✓✓✓
② ⭐⭐⭐ **不是 B、不是 C**：无"平均恒等式重编码"步骤、无隐含配对相关假定 ✓✓
③ ⭐⭐⭐ **附加发现**：MV 只用 $\ell^2$ 范数 ⟹ **不用配对相关** ⟹ **AF 常数 ＝ 最坏情形几何常数** ⟹ 解释其鲁棒性 ＋ **不可由算术输入改进**（与 V299 §4 反例互证且更强）✓✓✓
④ ⭐⭐ **两处细化**：(a) 误差层是**界**而非配对相关评估；(b) bandwidth 经 **MV 适用域**（$\log X\le L\iff X\le T$）进入 ✓✓
⑤ ⭐ **输入减法被解释**：MV 是纯调和分析（无需 RH）⟹ 与 `V185` §3"无 mollifier／无密度／无零自由区"一致 ✓
【下一步（唐先生既定顺序：4b/4c 统一求 $c_{\rm geom}(\sigma)$，不先优化窗口）】
  (4b＋4c) 求 $$c_{\rm geom}(\sigma)=\sup_{\phi\in\mathcal A_\sigma}c_{\rm geom}(\phi)$$ 其中 $\mathcal A_\sigma$ **须含无条件性约束**（不只 $\operatorname{supp}\widehat\phi\subseteq[-\sigma,\sigma]$）；
        并做**反问题** $$c_{\rm geom}\ge1-\varepsilon\Longrightarrow\sigma\ge\sigma(\varepsilon)$$ ✓✓
  ⚠️ **必须防的陷阱（唐先生）**：$$\text{"更宽的}\ \phi\text{"}\ \not\Rightarrow\ \text{"更大的}\ c_{\rm geom}\text{"}$$ **除非先证优化泛函的单调性** ⟹ 不得把"support 越大越好"当定理 ✓✓✓
```
