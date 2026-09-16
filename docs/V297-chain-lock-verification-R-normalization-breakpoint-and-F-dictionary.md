# V297 · **$G=1-R_{\rm off}$ 链条逐项锁死** —— ⚠️ **发现真断点（检查 A）：V296 的"$\|\widetilde G\|^2_{\rm HS}=(R+o(1))N$"不精确**；论文 §5 承载语句是**比值** $\dfrac{(\operatorname{tr}\widetilde G)^2}{\operatorname{tr}\widetilde G^2}=F(\lambda_1)N$ ⟹ **正确字典 $R=1/F(\lambda_1)$**，$\boxed{G=2-1/F(\lambda_1)=1-R_{\rm off}}$（$R_{\rm off}:=1/F-1$）**修正后仍存活**；⭐ **焊接成功（识别层面）：rank–trace 损失 $=\tfrac1F-1=R_{\rm off}$**；⚠️ **逻辑护栏已写入：不得推出"所有非局部核 $R_{\rm off}>0$"**

$$\boxed{\textbf{断点 1（本档）}：\text{V296 §1 写}\ \|\widetilde G\|^{2}_{\rm HS}=(R+o(1))N\ \textbf{不精确};\ \text{论文实际给}\ \frac{(\operatorname{tr}\widetilde G)^{2}}{\operatorname{tr}\widetilde G^{2}}=F(\lambda_1)N(T,2T)\big(1+O(\mathcal E_T)\big)} ✓✓✓$$
$$\boxed{\textbf{修正后}：R：＝\tfrac1{F(\lambda_1)};\quad \hat G：＝\tfrac{\widetilde G}{aL}\Longrightarrow \operatorname{tr}\hat G=N,\ \operatorname{tr}\hat G^{2}=\tfrac{N}{F(\lambda_1)} \Longrightarrow \underbrace{4\operatorname{tr}\hat G-2N-\operatorname{tr}\hat G^{2}}_{=\ (2-1/F)N}=G\cdot N} ✓✓✓$$
$$\boxed{\textbf{焊接}：\text{rank–trace 损失}\ ＝\ \frac1F-1\ ＝\ R_{\rm off}};\qquad F=\frac{(\operatorname{tr}\hat G)^{2}}{N\operatorname{tr}\hat G^{2}}=\frac{\textbf{有效秩}}{N}\le1\（\text{Cauchy–Schwarz}）✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:18：**第 1 步必须先于任何非 Toeplitz 构造**；但**不是简单核验 $R_{\rm diag}=1$／$R_{\rm off}=1/3$**，而是要核验 **$G=1-R_{\rm off}$ 是否为从 AF 证书到 RH 目标的"无损重参数化"**；四项硬检查 **A**（固定 $R$ 的定义，**不得凭经典读数**）／**B**（对角项独立计算，查重零）／**C**（离对角**不得**直接等同于 $F(\alpha)-1$，须做**精确** form-factor 转换与换元 $u=\frac{\log T}{2\pi}(\gamma-\gamma')$）／**D**（确认 $R_{\rm off}=1/3$ 的来源）；并命令：**"只要其中任何一个换元不是恒等式，就立即标出断点，不要为了保住 V296 而补假设"** ✓✓✓
> 第一手依据（**本档现场读源**）✓ `~/lean-repro/zeta23-local/Zeta23/PrimeSideTemp.lean`（**[thm:traces] 逐字 ＋ TracesBounds 结构 ＋ ThmTracesHyp 定义**）｜`Zeta23/PrimeSideB/Concrete.lean`（`trGtilde`／`trGtildeSq` 的识别）｜`Zeta23/LinAlg/RankTrace.lean`（Lemma R 精确形式）｜`ChallengeDeps.lean`（**`cMT` 闭式**）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V297`（`id_claim.sh` ✓）

---

## §1 第一手原文（本档抽取，非转述）

$$\textbf{[thm:traces]（论文 §5，Lean 注释逐字）}：\text{Let}\ 0<\lambda\le1,\ L=\lambda l,\ X=e^{L},\ 1\le w\le L/8：$$
$$\qquad \operatorname{tr}\widetilde G=aL\,N(T,2T)+O(L\sqrt X)=L\,N(T,2T)\big(1+O(\mathcal E_T)\big)\tag{eq:tr1}$$
$$\qquad \operatorname{tr}\widetilde G^{2}=2\pi bL\!\int_T^{2T}\!\!\mu^{2}+\frac T\pi\sum_{n\le X}\frac{\Lambda(n)^{2}}{n}g(\log n)+O\big(Ll\log l(l^{2}+X)\big)=\frac{TL}{2\pi}\Big(\ell_1^{2}+\frac{L^{2}}3\Big)\big(1+O(\mathcal E_T)\big)\tag{eq:tr2}$$
$$\qquad \boxed{\frac{(\operatorname{tr}\widetilde G)^{2}}{\operatorname{tr}\widetilde G^{2}}=F(\lambda_1)\,N(T,2T)\big(1+O(\mathcal E_T)\big),\qquad \lambda_1=\frac L{\ell_1}=\lambda\Big(1-\frac{2\log2-1}{\ell_1}\Big)}\tag{eq:ratio}$$
$$\qquad \text{其中}\ \mathcal E_T：＝\frac wL+\frac{(l^{2}+X)\log l}{Tl}+T^{\lambda/2-1};\qquad \widetilde G：＝G/L,\ G_{kl}=\int_{\mathbb R}\widehat\phi(\tau-\tau_k)\widehat\phi(\tau-\tau_l)\nu_X(\tau)d\tau ✓$$
$$\text{识别（`Concrete.lean`）}：\ \operatorname{tr}\widetilde G=P.\texttt{trGtilde},\ \operatorname{tr}\widetilde G^{2}=P.\texttt{trGtildeSq};\qquad \widetilde G\ \text{Hermitian} \Longrightarrow \|\widetilde G\|_F^{2}=\operatorname{tr}\widetilde G^{2} ✓✓$$
$$\text{常数闭式（`ChallengeDeps.lean`）}：\ c^{*}_{\lambda}=\frac{\sqrt2\tan\vartheta}{1+\vartheta\tan\vartheta}\Big|_{\vartheta=\lambda/\sqrt2};\quad c_1^{*}=0.7532960\ldots;\quad \frac1{c_1^{*}}=\frac12+2^{-1/2}\cot\big(2^{-1/2}\big)\ \text{（Montgomery–Taylor 常数）} ✓✓$$

---

## §2 ⚠️ **检查 A：固定 $R$ 的定义 —— 断点已定位并修正**

$$\text{V296 §1 的写法} ✗：\ \|\widetilde G\|^{2}_{\rm HS}=\big(R(\psi)+o(1)\big)N\ ⚠️\ \text{（隐含"}\widetilde G\ \text{已归一化使}\ \operatorname{tr}=N\text{"，且把}\ R\ \text{当成独立于}\ F\ \text{的窗口泛函）}$$
$$\text{论文实际给的是}\ \textbf{比值}\ \text{(eq:ratio)，其分母}\ \operatorname{tr}\widetilde G^{2}\ \text{还需除以}\ (aL)^{2}\ \text{才归一到}\ N ⟹ ⚠️\ \textbf{换元非恒等} ⟹ \textbf{断点 1} ✓✓✓$$
$$\textbf{修正（本档，不引入新假设）}：\text{设}\ \hat G：＝\widetilde G/(aL),\ a：＝\text{taper 常数}：$$
$$\qquad \text{(eq:tr1)} ⟹ \operatorname{tr}\hat G=N\big(1+O(\mathcal E_T)\big) ✓;\qquad \text{(eq:ratio)} ⟹ \operatorname{tr}\hat G^{2}=\frac{(\operatorname{tr}\hat G)^{2}}{F(\lambda_1)N}\big(1+O(\mathcal E_T)\big)=\frac{N}{F(\lambda_1)}\big(1+O(\mathcal E_T)\big) ✓✓$$
$$\qquad \Longrightarrow \text{单链}：4\operatorname{tr}\hat G-2N-\operatorname{tr}\hat G^{2}=\Big(4-2-\frac1{F(\lambda_1)}\Big)N\big(1+o(1)\big)=\boxed{\Big(2-\frac1{F(\lambda_1)}\Big)N} ✓✓✓$$
$$\boxed{\textbf{故}\ 2/3\ \text{的正确来源}\ ＝\ 2-\frac1{F(\lambda_1)};\qquad R：＝\frac1{F(\lambda_1)}} ✓✓✓$$
$$\qquad \text{读数}：\text{指示窗}\ F=\tfrac34\Longrightarrow R=\tfrac43\Longrightarrow \tfrac23 ✓;\qquad \text{MT 窗}\ F=c_1^{*}\Longrightarrow R=1.32750\Longrightarrow 0.67250 ✓✓$$
$$\Longrightarrow \boxed{\textbf{V296 的核心恒等式在修正后存活}：G=2-\frac1F=1-R_{\rm off},\quad R_{\rm off}：＝\frac1F-1} ✓✓✓$$

---

## §3 **检查 B：对角项独立计算（含重数）**

$$\text{(eq:tr1)}\ \text{带重数}：\operatorname{tr}\widetilde G=aL\,N(T,2T)\big(1+O(\mathcal E_T)\big),\quad N(T,2T)：＝\sum_{\rho}m_\rho ✓$$
$$\qquad ⚠️\ \text{查重零}：\text{trace 侧}\ \textbf{已含重数}（N\ \text{为带重数计数}）⟹ \textbf{无需简单零假设};\ \text{简单零}\ s_1／\text{多重}\ s_2／\text{离轴对}\ p\ \text{只出现在}\ \textbf{rank 侧} ✓✓$$
$$\boxed{\text{"}R_{\rm diag}=1\text{"}\ \textbf{不是经典读数，而是归一化恒等式}}：\text{归一化}\ \hat G=\widetilde G/(aL)\ \text{恰使}\ \operatorname{tr}\hat G=N ✓✓✓\ \text{（比 V296 的表述更强更干净）}$$
$$\text{且}\ F\ \text{的意义被确定}：F=\frac{(\operatorname{tr}\hat G)^{2}}{N\operatorname{tr}\hat G^{2}}\ \text{（}\textbf{有效秩}/N：\text{participation number}/N\text{）}✓$$
$$\qquad \text{Cauchy–Schwarz（核心）}：(\operatorname{tr}\hat G)^{2}=\Big(\sum_i\lambda_i\Big)^{2}\le \operatorname{rank}\cdot\sum_i\lambda_i^{2} ⟹ \boxed{F\le1\ \text{恒成立}} ✓✓✓$$
$$\qquad \qquad F=1\iff \text{谱在满秩上}\textbf{均匀}（\hat G\ \text{的最大秩、最平坦}）⟹ \textbf{"}G\to1\text{"}\iff F\to1\iff \textbf{有效秩}\to N ✓✓✓$$

---

## §4 **检查 C：离对角 $\leftrightarrow$ Montgomery form factor（精确换元）**

$$\text{(eq:tr2)}\ \text{的素数侧}：\frac T\pi\sum_{n\le X}\frac{\Lambda(n)^{2}}{n}g(\log n)\ \text{（＋}\ 2\pi bL\!\int\mu^{2}\ \text{＋余项）} ⟹ \textbf{求和侧} \text{＝带宽约束进入处} ✓✓$$
$$\qquad \text{其求值}＝\textbf{对角}（n=m）＋\textbf{离对角}（n\ne m）；\text{差集}\ \{\log(n/m)\}\subseteq[0,\log X]=[0,L] ✓$$
$$\qquad \text{换元（唐先生建议的形式）}：\alpha：＝\frac{\log(n/m)}{L}\in[0,\ \lambda_1]\subseteq[0,1]\qquad ⟹\ \textbf{恰落在 Montgomery 的无条件区}\ |\alpha|\le1 ✓✓✓$$
$$\qquad \text{（}\gamma\ \text{侧写法}：u=\frac{\log(T/2\pi)}{2\pi}(\gamma-\gamma')\ \text{与}\ \alpha\ \text{同域；本档采}\ \alpha\ \text{记法）}✓$$
$$\Longrightarrow \boxed{\textbf{检查 C 通过（结构性）}：\text{离对角}\ \leftrightarrow\ F(\alpha);\ \text{带宽一}\iff\text{无条件区};\ \lambda>1\Rightarrow\text{需 RH}} ✓✓✓$$
$$\qquad \text{与 `V296` §1"障碍型 B（离对角／算术相关性）"}\ \textbf{一致} ✓✓$$
$$\qquad ⚠️\ \textbf{仍未锁死点}：F(\lambda_1)\ \text{与}\ \int_0^1\big(F(\alpha)-1\big)\ \text{型量的}\ \textbf{定量等同} \text{未做（需论文 §5 求值细节）} ⚠️$$

---

## §5 ⭐ **检查 D：$R_{\rm off}$ 的来源 —— 焊接成功（识别层面）**

$$\text{目标（唐先生）}：\text{不把}\ 1/3\ \text{当结论，而确认}\ R_{\rm off}=\mathcal F[K;\{\gamma_\rho\}]\ \text{且}\ \psi_0\ \text{给}\ \tfrac13 ✓$$
$$\text{由 §2}：R_{\rm off}：＝\frac1F-1 ⟹ F=\tfrac34\iff R_{\rm off}=\tfrac13 ✓;\qquad F=c_1^{*}\iff R_{\rm off}=0.32750 ✓$$
$$\qquad \text{闭式核验}：\frac1{c_1^{*}}=\frac12+2^{-1/2}\cot(2^{-1/2})\ \text{（Montgomery–Taylor 常数，`ChallengeDeps.lean` 逐字）} ✓$$
$$\boxed{\textbf{焊接（识别层面）}：\text{rank--trace 损失}\ \equiv\ \frac1F-1\ \equiv\ R_{\rm off}} ✓✓✓$$
$$\qquad \Longrightarrow \text{V295 的"秩-迹／HS 损失"与 V296 的"离对角算术质量"}\ \textbf{被同一对象}\ F(\lambda_1)\ \text{承载} ✓✓✓$$
$$\qquad ⚠️\ \textbf{定量焊接仍未完成}：\text{把}\ F\ \text{显式写成}\ 1+c\cdot(\text{离对角质量})\ \text{需论文 §5 求值} ⚠️$$

---

## §6 ⚠️ **逻辑护栏（唐先生命令，必写入）**

$$\text{即使 A–D 全部通过，}\textbf{不得} \text{得出}：\forall\ \text{允许核}：R_{\rm off}>0\ ✗✓$$
$$\qquad \text{因 Montgomery 的}\ F(\alpha)=1\ (|\alpha|\le1)\ \textbf{只} \text{说明"在特定 Fourier-support 证书机制内无条件控制到哪里"} ✓✓$$
$$\boxed{\text{正确结论形式}：\text{AF／Toeplitz／带宽一证书}\ \Longrightarrow\ R_{\rm off}\ \text{具不可消除质量}} \qquad \textbf{而非}\qquad \text{所有非局部核}\Longrightarrow R_{\rm off}>c ✗✓✓$$

---

## §7 **接口审计（第 2 步提前登记）**

$$\text{目标}：\texttt{Ceiling.lean}\ \text{assumptions}\ \leftrightarrow\ \text{Toeplitz／support}\ \leftrightarrow\ \sigma_{\min};\ \text{尤其找}\ \texttt{Ceiling.lean}\ \textbf{中第一次出现}\ \{\log(n/m)\}\ \text{处} ✓$$
$$\qquad \text{若证明链可写成}：\text{Certificate}\Rightarrow\text{difference-set support}\Rightarrow|\alpha|\le1\Rightarrow R_{\rm off}\ge c ⟹ \text{可正式写入}\ \boxed{\textbf{Certificate ceiling theorem}} ✓✓$$
$$\qquad \text{届时逃逸空间严格定义为}：\boxed{\mathcal E：＝\{K:\ K\ \text{非证书型}\ \wedge\ \text{仍有可证明的无条件控制}\}} ✓✓✓$$

---

## §8 判词 ＋ 边界 ＋ 净产出

$$\boxed{\textbf{V297 判词}：\text{① 断点 1 已定位（V296 §1 表述不精确）并}\textbf{修正};\ \text{② 修正后}\ G=1-R_{\rm off}\ \textbf{存活}（R=1/F）;\ \text{③ 对角项＝归一化恒等式（非经典读数），trace 侧含重数};\ \text{④ 离对角}\leftrightarrow F(\alpha)\ \text{换元验证（}a\le1\text{）};\ \text{⑤ 焊接成功（识别层面）};\ \text{⑥ 护栏已立}} ✓✓✓$$

```
① ⚠️ **断点 1（T10 勘误）**：V296 §1 的 $\|\widetilde G\|^2_{\rm HS}=(R+o(1))N$ 不精确 ⟹ 已在 V296 原档追加勘误 ✓
② ⚠️ **未锁死点**：$F(\lambda_1)$ 与 $\int(F(\alpha)-1)$ 的**定量等同**未做（需论文 §5 求值）⚠️
③ ⚠️ §3 的"$F\le1$（Cauchy–Schwarz）"为本档推导（标准，但未在 Lean 中核对）⚠️
④ ⚠️ `Ceiling.lean` 仍未读全文；§7 为**登记**，未执行 ✓
⑤ **不声称**一般核有 $R_{\rm off}>0$（护栏 §6）✓；**不声称** AF 证明正误 ✓
⑥ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⚠️⚠️ **断点 1（最重要）**：V296 §1 写法不精确 ⟹ 论文承载语句是**比值** (eq:ratio)，$R=1/F(\lambda_1)$ ⟹ **修正后** $G=2-1/F=1-R_{\rm off}$ **存活** ✓✓✓
② ⭐⭐ **对角项＝归一化恒等式**（$R_{\rm diag}=1$ 不是经典读数）；**trace 侧含重数 ⟹ 无需简单零假设**；$F=$ 有效秩$/N\le1$ ✓✓✓
③ ⭐⭐ **离对角 ↔ $F(\alpha)$ 换元验证**：$\alpha=\log(n/m)/L\in[0,\lambda_1]\subseteq[0,1]$ ⟹ 恰落 Montgomery 无条件区 ✓✓✓
④ ⭐⭐⭐ **焊接成功（识别层面）**：rank–trace 损失 $\equiv\tfrac1F-1\equiv R_{\rm off}$；MT 常数闭式 $1/c_1^{*}=\tfrac12+2^{-1/2}\cot(2^{-1/2})$ 逐字核验 ✓✓✓
⑤ ⚠️ **逻辑护栏**：不得推出"所有非局部核 $R_{\rm off}>0$"；正确形式 ＝ "AF／Toeplitz／带宽一证书 ⟹ 不可消除质量" ✓✓
⑥ ⭐ **新增可得的结构性结论**：$G\to1\iff F\to1\iff$ **有效秩**（participation number）$\to N$ ⟹ "到 1"问题 ＝ **能否让有效秩饱和** ✓✓✓
【下一步（唐先生既定：第 2 步提前为接口审计）】
  (2a) 读 `Ceiling.lean` **全文**，找**第一次出现 $\{\log(n/m)\}$** 处，把 §7 的链写成 **Certificate ceiling theorem** ✓
  (2b) 补 §4／§5 的两个**未锁死点**（$F\leftrightarrow\int(F(\alpha)-1)$ 的定量等同）—— 需论文 §5 求值细节 ✓
```
