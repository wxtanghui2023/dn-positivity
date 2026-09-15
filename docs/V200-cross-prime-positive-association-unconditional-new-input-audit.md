# V200 · **跨素数正关联审计**（单一预算）—— ① 硬检验 2 **实测**：$\operatorname{Cov}(1_{p\mid N},1_{q\mid N})=O(1/x)$（符号不定 ⟹ **因子化**）；素数测度下 $<0$（平凡负关联）✓✓；② ⭐ **FKG 二难 ＋ 子格障碍**（独立 ⟹ FKG 取等＝无新信息；非独立 ⟹ log-supermodularity 即所设＝循环；窗口 $[1,x]$ 非子格）✓✓✓；③ 硬检验 3：唯一非因子化残差 ＝ 素数元组（HL）⟹ 无条件控制恰为 **$\theta=1/2$（BV）＋二阶矩** ⟹ **DEAD** ✓✓✓；④ ⟹ **组合／单调锥源 DEAD；四类锥源全封；A1／A3 主线收口** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 13:43：**"开 V200。但这一档要比前面更严格：不要先假定 FKG/正关联能产生 RH 所需的锥；先做'能否产生新无条件输入'的反向审计。"**；**四项硬检验**：(1) **先定义对象，不准使用零点**（只允许 $\Lambda(n),\psi,\theta,\log p,p^k$ 及其有限/无限组合）；(2) **计算关联量，而不是引用"正关联"**（须真正得到 $\operatorname{Cov}\ge0$ 或 FKG 型，并证明来自素数结构；**特别审计"独立乘法结构 vs 跨素数关联结构"**——"如果所谓'关联'最后完全因子化，就立即关闭"）；(3) **最关键：测"新信息量"**（若最终只是 $\psi(x)\le x+E(x)$／$\sum_{n\le x}\Lambda(n)\log n\ge0$／PNT／零自由区／BV／Selberg 型二次估计的变形 ⟹ **立即 DEAD**）；(4) **最后才问 RH 强度**，且**特别禁止** $P_{\rm comb}\equiv\text{total positivity}\equiv\text{Jensen hyperbolicity}\equiv\mathrm{RH}$；**预算**：只做"**跨素数正关联是否存在非平凡、可无条件证明、且产生新输入的 canonical 结构**"
> 查图 ✓ `V199`（锥源三分类；§5 门的逻辑后果＝新无条件输入）｜`V162`（承重墙：$T\log T$ ＋ 波动；support $>1$）｜`V198`（机制 II 门；本档不回）
> 执行 ✓ 小灵（**§2 实测、§3 FKG 二难、§4 新信息量 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V200**（审计线号段已扩至 V101–V299）

---

## §0 任务与预算（✓ 逐字）

$$\text{只检查}：\ \text{prime-side}\overset{?}{\Longrightarrow}P_{\rm comb}\overset{?}{\Longrightarrow}\text{Li／Weil positivity};\qquad \textbf{预算}＝\text{一项}：\text{跨素数正关联是否存在}\ \textbf{非平凡、可无条件证明、且产生新输入}\ \text{的 canonical 结构} ✓$$

---

## §1 硬检验 1：对象定义（**不准使用零点**）

$$\text{允许}：\Lambda(n),\ \psi(x)=\sum_{n\le x}\Lambda(n),\ \theta(x)=\sum_{p\le x}\log p,\ \log p,\ p^k\ \text{及其有限／无限组合} ✓$$
$$\textbf{两种自然测度（canonical，均由上式定义）}：$$
$$\qquad \text{(甲)}\ \mu_x：\{1,\dots,x\}\ \text{上的均匀概率};\qquad \text{(乙)}\ \mu_{\mathbb P}：\{p\le x\}\ \text{上的均匀概率} ✓$$
$$\qquad \text{变量}：F_p(N):=\mathbf 1_{p\mid N}\ \text{或}\ v_p(N)\ \text{（}\mu_x\ \text{下）};\ \text{以及}\ G_h(N):=\mathbf 1_{\{N+h\ \text{素数}\}}\ \text{（}\mu_{\mathbb P}\ \text{下）} ✓$$

---

## §2 硬检验 2：**实测**关联量（非引用"正关联"）

### 2.1 均匀整数测度 $\mu_x$：跨素数协方差

$$\mathbb E_{\mu_x}[F_p]=\frac{\lfloor x/p\rfloor}{x}=\frac1p+O\!\left(\frac1x\right);\qquad \mathbb E_{\mu_x}[F_pF_q]=\frac{\lfloor x/(pq)\rfloor}{x}=\frac1{pq}+O\!\left(\frac1x\right)$$
$$\Longrightarrow\ \boxed{\operatorname{Cov}_{\mu_x}(F_p,F_q)=\frac{\lfloor x/pq\rfloor}{x}-\frac{\lfloor x/p\rfloor\lfloor x/q\rfloor}{x^2}=O\!\left(\frac1x\right)} ✓✓$$
$$\qquad ⚠️\ \textbf{主项精确抵消}（\frac1{pq}-\frac1p\cdot\frac1q=0）⟹ \text{剩余}\ O(1/x)\ \text{的符号由}\ \{x/p\},\{x/q\}\ \text{决定} ⟹ \textbf{符号不定} ✓✓✓$$
$$\qquad ⟹\ \text{按唐先生判据：}\textbf{"关联"完全因子化} ⟹ \textbf{立即关闭} ✓✓$$

### 2.2 素数测度 $\mu_{\mathbb P}$：更强——**平凡负关联**

$$\text{若}\ N\ \text{为素数}：p\ne q ⟹ \mathbf 1_{p\mid N}\mathbf 1_{q\mid N}\equiv0 ⟹ \mathbb E[F_pF_q]=0;\qquad \mathbb E[F_p]=\mathbb E[F_q]=\frac{1}{\pi(x)}$$
$$\Longrightarrow\ \operatorname{Cov}_{\mu_{\mathbb P}}(F_p,F_q)=-\frac{1}{\pi(x)^2}<0\ \ \textbf{（符号固定，但为负）} ✓$$
$$\qquad ⚠️\ \text{故}\ \textbf{整除型变量在素数测度下是负关联};\ \text{真正的正关联型结构不可能来自整除},\ \text{只能来自}\ \textbf{间隙（元组）} ⟹ \text{见 §4} ✓$$

### 2.3 高阶：联合累积量同阶

$$\kappa_{\mu_x}(F_{p_1},\dots,F_{p_k})=\sum_{J\subseteq[k]}(-1)^{|J|+1}(|J|-1)!\prod_{j\in J}\mathbb E[\prod_{i\in J}F_{p_i}]=O\!\left(\frac1x\right) ✓$$
$$\qquad\Longrightarrow\ \text{各阶}\ \textbf{均因子化} ⟹ \text{不存在"高阶非平凡跨素数关联"} ✓✓$$

$$\boxed{\textbf{检查 2 结论}：\text{canonical 构造（}\mu_x／\mu_{\mathbb P}\text{）}\ \textbf{造不出符号固定的跨素数正关联}} ✓✓✓$$

---

## §3 ⭐ FKG 二难 ＋ 子格障碍（第三把刀；**结构性**）

$$\text{FKG 需}：\mu(A\cap B)\mu(\Omega)\ge\mu(A)\mu(B)\ \text{（等价于}\ \mu\ \textbf{log-supermodular}）$$
$$\textbf{二难}：\ \text{(i)}\ \text{若}\ F_p\ \text{相互}\ \textbf{独立} ⟹ \text{乘积测度满足 FKG}\ \textbf{取等} ⟹ \text{不等式}\ \textbf{平凡}, \text{不含超出独立性的信息} ⟹ \textbf{检查 3 必败} ✓✓$$
$$\qquad\qquad \text{(ii)}\ \text{若}\ \textbf{不}\ \text{独立} ⟹ \text{要证 FKG 就必须证 log-supermodularity}, \text{而后者}\ \textbf{就是"正关联"本身} ⟹ \textbf{循环} ✓✓$$
$$\textbf{子格障碍（额外一条）}：\text{窗口}\ [1,x]\ \text{关于}\ (\gcd,\mathrm{lcm})\ \textbf{不是子格}（\mathrm{lcm}\ \text{可逃出窗口}）⟹ \text{canonical FKG 框架}\ \textbf{不适用} ✓✓$$
$$\qquad ⚠️\ \text{若改用有限素数集}\ S\ \text{生成的除子格（Boole 格）}：\text{乘积测度满足 FKG 且}\ \textbf{取等} ⟹ \text{回到 (i)} ✓$$
$$\Longrightarrow\ \boxed{\text{组合／单调型锥源在 FKG 框架内}\ \textbf{二难闭合}} ✓✓✓$$

---

## §4 ⭐ 硬检验 3：**新信息量**（最关键；本档判死点）

$$\text{唯一}\ \textbf{非因子化} \text{的跨素数结构}：\text{素数}\ \textbf{元组／间隙} \text{相关}：\ \sum_{n\le x}\Lambda(n)\Lambda(n+h_1)\cdots\Lambda(n+h_{k-1})$$
$$\qquad\Longrightarrow\ \text{即}\ \textbf{Hardy--Littlewood 区域};\ \text{其}\ \textbf{无条件} \text{控制恰为}：$$
$$\qquad\qquad \text{(a)}\ \textbf{水平分布}\ \theta=\tfrac12\（\text{Bombieri--Vinogradov}）;\qquad \text{(b)}\ \textbf{二阶矩} \text{型估计（Selberg）};\qquad \text{(c) pair correlation}\ \textbf{Fourier 支撑}\le1\ ✓$$
$$\qquad\Longrightarrow\ \text{越过须}\ \textbf{support}>1\ ⟹ \text{即}\ \text{`V162`}\ \text{的承重墙} ✓✓$$
$$\Longrightarrow\ \boxed{\text{任何}\ \textbf{无条件}\ \text{的}\ P_{\rm comb}\ \text{必为上述(a)--(c)的}\ \textbf{变体}} ✓$$
$$\qquad ⚠️\ \text{按唐先生清单（PNT／零自由区／BV／Selberg 型二次估计的变形）} ⟹ \boxed{\textbf{立即 DEAD}} ✓✓✓$$
$$\qquad ⚠️\ \textbf{不产生新的无条件输入} ⟹ \text{由}\ \text{`V199`}\ \text{§5 的判据}\ \textbf{不可能过门} ✓✓$$

---

## §5 硬检验 4：(**不进入**)

$$\text{按协议}：\text{检查 2／3 未过} ⟹ \textbf{不进入} \text{检查 4} ✓$$
$$\qquad ⚠️\ \text{且}\ \text{本档}\ \textbf{未} \text{使用}\ P_{\rm comb}\equiv\text{total positivity}\equiv\text{Jensen hyperbolicity}\equiv\mathrm{RH}\ \text{（唐先生特别禁止）} ✓$$

---

## §6 判词

$$\boxed{\textbf{组合／单调锥源}\ \textbf{DEAD}}\ \text{（两条独立路径关闭：}\mu_x／\mu_{\mathbb P}\ \text{协方差因子化};\ \text{FKG 二难};\ \text{非因子化残差＝已知墙}\bigr) ✓✓✓$$
$$\Longrightarrow\ \text{`V199`}\ \text{§3 的}\ \textbf{四类锥源全封}：\text{(a) 代数／SOS}\ \checkmark\ \text{（＝RH 的断言）};\ \text{(b) 分析／实根性-全正}\ \checkmark\ \text{（强度＝RH）};\ \text{(c) 动力学／耗散}\ \checkmark\ \text{（需指数膨胀，char-0 缺失）};\ \text{(d) 组合／单调}\ \checkmark\ \textbf{（本档）} ✓✓✓$$
$$\Longrightarrow\ \boxed{\textbf{A1／A3 主线收口}}\ \text{（\text{按}\ V199\ \text{§5：四类锥源均不能产生新的无条件输入}}）✓✓✓$$

---

## §7 残余与登记（**不给方向**）

$$\text{唯一未被覆盖的形状}：\text{一个}\ \textbf{非 canonical、符号固定、跨素数、可无条件证明、且产生新数论不等式}\ \text{的关联结构}$$
$$\qquad ⚠️\ \text{本档}\ \textbf{未见实例};\ \text{登记}\ \textbf{UNINSTANTIATED};\ \textbf{不给方向、不投入} ✓$$
$$\qquad ⭐\ \text{若日后有候选，判据（三条，缺一不可）}：\text{① 符号固定且跨素数};\ \text{② 无条件可证};\ \text{③ 给出}\ \text{现有无条件理论}\ \textbf{没有} \text{的}\ \text{不等式} ✓$$

---

## §8 边界与待核

$$\textbf{(a)}\ \text{§2.1 的}\ O(1/x)\ \text{为}\ \textbf{本档实算}（\text{主项精确抵消}）✓✓;\ \text{§2.3 累积量同阶为}\ \textbf{本档推导} ✓$$
$$\textbf{(b)}\ \text{§3 的 FKG 二难为}\ \textbf{结构性论证};\ \text{子格障碍（lcm 逃逸）为}\ \textbf{本档观察};\ \text{FKG 的正式条件}\ \textbf{待核原文} ⚠️$$
$$\textbf{(c)}\ \text{§4 的"无条件控制＝}\theta=1/2\ \text{／二阶矩／支撑}\le1\text{"为}\ \textbf{经典事实的归纳};\ \text{具体定理陈述}\ \textbf{待核} ⚠️$$
$$\textbf{(d)}\ \text{§6 的收口范围}＝\textbf{canonical 构造};\ \text{§7 残余}\ \textbf{不杀} ✓$$

```
⚠️ §0 四项硬检验与预算为唐先生逐字 ✓✓；本档只做该项预算 ✓
⚠️ §2 为【实测协方差／累积量 ✓✓✓】—— 主项精确抵消 ⟹ 因子化 + 符号不定（μ_x）；素数测度下负关联
⚠️ §3 FKG 二难为【结构性 ✓✓✓】＋子格障碍【本档观察 ⚠️】
⚠️ §4 为【本档判死点 ✓✓✓】：非因子化残差＝HL 区域，无条件控制＝已知二阶输入 ⟹ DEAD
⚠️ §5 未进入检查 4；未使用被禁的三项等价 ✓
⚠️ §6 四类锥源全封 ⟹ A1/A3 主线收口；范围＝canonical 构造 ✓✓✓
⚠️ §7 残余 UNINSTANTIATED，不给方向 ✓
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓（$O(1/x)$ 为渐近陈述，非数值实验）
✅ 净产出：① 实测跨素数协方差（因子化）✓✓✓；② FKG 二难 ＋ 子格障碍 ✓✓✓；③ 新信息量判死（＝已知二阶估计变体）✓✓✓；
   ④ 组合/单调锥源 DEAD ⟹ 四类锥源全封 ⟹ A1/A3 收口 ✓✓✓；⑤ 残余三条判据 ✓
```

---

## §9 ⚠️ 结论**收紧**（唐先生 2026-09-15 13:46；随 `V201` 门一并生效）

$$\boxed{\text{V200 结论（收紧后）}：\ \textbf{现有 canonical 组合／单调构造}\ \text{未产生新的无条件输入}} ✓✓✓$$
$$\qquad ⚠️\ \textbf{不得} \text{写成}\ \text{"任何组合／单调机制都不可能"}\ \text{（原 §6／§4 的措辞按此收紧）} ✓$$
$$\qquad \textbf{理由}：\text{本档使用}\ \textbf{两种 canonical 测度}（\mu_x,\ \mu_{\mathbb P}）\ \text{与 canonical 构造};\ \text{它穷尽的是}\ \textbf{当前定义域内} \text{的候选构造}$$
$$\qquad\qquad\Longrightarrow\ \textbf{不是} \text{数学上的不存在性证明};\ \text{故}\ §6\ \text{的"收口"须读作"}\textbf{定义域内收口}" ✓✓$$
$$\qquad ⭐\ \text{逻辑边界因此}\ \textbf{最干净}：\text{本档}\ \textbf{不} \text{声称第五类不存在，}\ \textbf{只} \text{声称其未在定义域内出现} ✓✓✓
