# V299 · **谱离散度 ↔ form factor 的定量焊接（四刀）** —— ⭐⭐⭐⭐ **判词 C：焊接在主项层面失败**（$(F_{\rm pair}-1)$ **不进主项**：$\operatorname{tr}\hat G^{2}$ 的主项是**经典窗矩常数**，由 $F\equiv1$ 的**理想**评估给出）；⭐⭐⭐⭐ **关键发现：理想 $F_{\rm pair}\equiv1$ 已给 $R_{\rm off}=\frac1{c_\lambda^{*}}-1\ge0.3275>0$** ⟹ **"$R_{\rm off}\to0\iff F_{\rm pair}\to1$" 为假**；⭐⭐⭐ **故逃逸空间须改写为 $\{$几何常数 $c_{\rm geom}\to1\}$ ⟺ 支撑 $>1$ 的无条件化**

$$\boxed{\textbf{判词 C（本档）}：R_{\rm off}\ \textbf{的主项不含}\ (F_{\rm pair}-1)\ ——\ \text{它是}\ \frac1{c^{\rm geom}_{\phi}}-1;\ \text{故}\ \text{"谱离散度}\leftrightarrow\text{form-factor 偏离"}\ \textbf{不成立}} ✓✓✓$$
$$\boxed{\textbf{核心反例（本档）}：\text{理想}\ F_{\rm pair}\equiv1（\text{Montgomery 无条件输入的最优形态}）\Longrightarrow F_{\rm eff}=c_1^{*}=0.7532960\Longrightarrow R_{\rm off}=0.3275>0} ✓✓✓$$
$$\boxed{\textbf{两正性严格分离}：R_{\rm off}\ge0\ ＝\ \textbf{谱方差正性}（\text{代数恒等式}）;\qquad F_{\rm pair}-1\ge0\ ＝\ \textbf{算术配对相关正性};\qquad \textbf{前者不得传给后者}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:24：继续打 (3b)，四件事：**① $W_\phi$（精确核函数／尺度／权重／归一化）② $F_{\rm eff}$ 与 $F_{\rm pair}$ 的关系 ③ 权重正性 ④ $\lambda\uparrow1$ 的误差**；命令：**不得把 $R_{\rm off}$ 与"form factor 偏离"当成同一量的不同叫法**；结论只允许 **A 焊死／B 单向／C 焊接失败** 三种；并**特别要求**把两个"正性"严格分开（**不得把谱方差正性传递给配对相关正性**）✓✓✓
> 依据 ✓ `V297`（链锁死：$R_{\rm off}=\frac1{F(\lambda_1)}-1+o(1)$；$F=\frac{(\operatorname{tr}\hat G)^2}{N\operatorname{tr}\hat G^2}$）｜`V298`（层 1–3；$\mathcal C_{\rm actual}$；$R_{\rm off}=$ 成对离散度）｜`PrimeSideTemp.lean`（**(eq:tr2) 第一／第二形式**、(eq:ratio)）｜`ChallengeDeps.lean`（$c^{*}_\lambda$ 闭式）｜**Montgomery–Taylor**／**CCLM17 Cor.14**（经典·引用）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V299`（`id_claim.sh` ✓）

---

## §1 已锁死部分（不重新论证）

$$R_{\rm off}=\frac{N\operatorname{tr}\hat G^{2}-(\operatorname{tr}\hat G)^{2}}{(\operatorname{tr}\hat G)^{2}}=\frac1{F(\lambda_1)}-1+o(1),\qquad F(\lambda_1)：＝\frac{(\operatorname{tr}\hat G)^{2}}{N\operatorname{tr}\hat G^{2}} ✓$$
$$\textbf{两正性（严格分离，唐先生要求）}：$$
$$\qquad \boxed{R_{\rm off}\ \ge\ 0}\quad ＝\ \textbf{谱方差正性}：\text{代数恒等式}\ N\!\sum\lambda_i^{2}-\Big(\sum\lambda_i\Big)^{2}=\tfrac12\sum_{i,j}(\lambda_i-\lambda_j)^{2}\ \text{（`V298` §3b）} ✓✓$$
$$\qquad \boxed{F_{\rm pair}(\alpha)-1\ \ge\ 0}\quad ＝\ \textbf{算术配对相关正性}：\text{完全不同的命题} ✓✓$$
$$\qquad ⚠️\ \textbf{前者}\ \textbf{不} \text{蕴含后者};\ \text{本档}\ \textbf{不} \text{使用后者，也不把前者传给它} ✓✓✓$$

---

## §2 **第一刀：$W_\phi$ 在哪里？—— 结论：$(F_{\rm pair}-1)$ 不在主项里**

$$\text{(eq:tr2) 第二形式（`PrimeSideTemp.lean` 逐字）}：\operatorname{tr}\widetilde G^{2}=\frac{TL}{2\pi}\Big(\ell_1^{2}+\frac{L^{2}}3\Big)\big(1+O(\mathcal E_T)\big) ✓$$
$$\qquad \text{主项}\ \frac{TL}{2\pi}(\ell_1^{2}+L^{2}/3)\ \textbf{只含窗矩}\ \ell_1\ \text{与}\ L^{2}/3\ ——\ \textbf{不含任何零／素数相关输入} ✓✓$$
$$\qquad \text{(eq:tr2) 第一形式}：\operatorname{tr}\widetilde G^{2}=2\pi bL\!\int_T^{2T}\!\!\mu^{2}+\frac T\pi\sum_{n\le X}\frac{\Lambda(n)^{2}}n g(\log n)+O(\cdot)$$
$$\qquad \qquad ⟹ \text{素数侧是}\ \textbf{单重和}（\text{对角型}）：\ \text{离对角（}F_{\rm pair}\ \text{所控制者}）\ \textbf{只能进} \text{误差项}\ O(\mathcal E_T)\ \text{或次阶} ✓✓$$
$$\textbf{（本档判读·[推断]）}：\text{主项}＝\text{对角}\ +\ \text{以}\ F\equiv1\ \text{（理想形态）评估的离对角}\ ⇒\ \textbf{一个只依赖窗口的经典常数} ✓$$
$$\qquad ⟹ \boxed{\text{所期望的焊接形式}\ R_{\rm off}=\int W_\phi(\alpha)\big(F_{\rm pair}(\alpha)-1\big)d\alpha+\text{err}\ \textbf{在主项层面失败}} ✓✓✓$$
$$\qquad \qquad \text{（}W_\phi\ \text{若有，只作用于}\ o(1)\ \text{部分；故}\ W_\phi\ \text{的显式形状}\ \textbf{不决定}\ R_{\rm off}\ \text{的主项}）✓$$

---

## §3 **第二刀：$F_{\rm eff}$ 与 $F_{\rm pair}$ 是两个对象**

$$F_{\rm eff}(\lambda_1)：＝\frac{(\operatorname{tr}\hat G)^{2}}{N\operatorname{tr}\hat G^{2}}\ ——\ \textbf{证书的有效秩}／N ✓;\qquad F_{\rm pair}(\alpha)\ ——\ \textbf{Montgomery form factor} ✓$$
$$\boxed{\text{正确关系（本档）}：F_{\rm eff}(\lambda_1)=c^{\rm geom}_{\phi}+o(1)}$$
$$\qquad \text{其中}\ c^{\rm geom}_{\phi}\ \text{＝以}\ F\equiv1\ \text{评估的经典常数};\qquad \text{读数}：\text{指示窗}\ c^{\rm geom}=0.75（\Rightarrow2-4/3=2/3）;\ \text{MT 最优窗}\ c^{\rm geom}=c_1^{*}=0.7532960 ✓✓$$
$$\qquad \text{而}\ F_{\rm pair}\ \text{只经}\ o(1)\ \text{项进入} ⟹ \boxed{F_{\rm eff}\ \ne\ F_{\rm pair}(\lambda)} ✓✓✓$$
$$\qquad \text{故论文 §5 若给出前者，则本档定理形式应为}：\ \boxed{R_{\rm off}=\frac1{c^{\rm geom}_{\phi}}-1+o(1)} ✓✓$$
$$\qquad \qquad —— \textbf{这才是真正的"谱—算术字典"：主项由}\ \textbf{证书几何（窗口）} \text{决定，算术配对相关只在误差层} ✓✓✓$$

---

## §4 ⭐⭐⭐⭐ **第三刀（判死点）：正性与"理想形态反例"**

$$\textbf{检验}：\text{若焊接成立且}\ W_\phi\ge0，\text{则}\ F_{\rm pair}\to1\Rightarrow R_{\rm off}\to0 ✓$$
$$\textbf{本档反例（决定性）}：\text{取}\ F_{\rm pair}\equiv1（\text{＝ Montgomery 无条件输入能达到的}\ \textbf{最优理想形态}，|\alpha|\le1）$$
$$\qquad ⟹ F_{\rm eff}=c_1^{*}=0.7532960 ⟹ \boxed{R_{\rm off}=\frac1{c_1^{*}}-1=0.327498\ldots>0} ✓✓✓$$
$$\Longrightarrow \boxed{\textbf{"}R_{\rm off}\to0\iff F_{\rm pair}\to1\text{"}\ \textbf{为假}}:\ \text{连}\ \textbf{理想} \text{配对相关都给}\ R_{\rm off}>0.327 ✓✓✓$$
$$\qquad \textbf{故判词}\ ＝\ \textbf{C（焊接失败）};\qquad \text{且失败}\ \textbf{有明确机制}：$$
$$\qquad \qquad \text{谱离散度有}\ \textbf{基线（几何）分量}\ \frac1{c^{\rm geom}}-1;\ \textbf{任何配对相关改进都消不掉它} ✓✓✓$$
$$\qquad ⚠️\ \text{权重变号的假设路径}\ \textbf{不必} \text{走}：\text{因主项根本不含}\ (F_{\rm pair}-1) ⟹ \text{连"变号"问题都不成立} ✓$$

---

## §5 **第四刀：极限次序与 $\lambda\uparrow1$ 的误差**

$$\text{论文所证（`PrimeSideTemp.lean`）}：\text{固定}\ 0<\lambda\le1,\ 1\le w\le L/8,\ T\ge T_0(\lambda);\ \text{误差}\ \mathcal E_T=\frac wL+\frac{(l^{2}+X)\log l}{Tl}+T^{\lambda/2-1} ✓$$
$$\qquad \lambda<1：T^{\lambda/2-1}\to0 ✓;\qquad \lambda=1：T^{-1/2}\to0 ✓;\qquad \lambda>2：T^{\lambda/2-1}\to\infty\ \textbf{爆炸} ✓✓✓$$
$$\qquad ⟹ \text{框架}\ \textbf{只在}\ \lambda\le1\（\text{及}\ \lambda\ \text{适度}>1）\ \text{有内容};\ \lambda\ \text{大时误差主导} ✓✓$$
$$\textbf{但 RH 需要的是}\ F_{\rm eff}\to1（\text{而非}\ \forall\lambda<1：F_{\rm eff}(\lambda)<1）⟹ \text{须}\ c^{\rm geom}_\phi\to1 ✓$$
$$\qquad \textbf{路线图（`V185` §4，论文 Remark 1.1）}：0.70／0.80／0.90\ \text{需 Fourier 支撑约}\ 1.04／1.26／1.70 ✓✓$$
$$\qquad \qquad ⟹ \textbf{几何常数}\ c^{\rm geom}\ \textbf{随带宽改善} —— \textbf{这是唯一的杠杆} ✓✓✓$$
$$\qquad ⟹ \lambda\uparrow1\ \text{还不够}（c_1^{*}=0.7533）；\text{要到}\ c^{\rm geom}\to1\ \text{须}\ \textbf{支撑}\to\infty ⟹ \textbf{无条件带宽}\ \text{是硬需求} ✓✓✓$$

---

## §6 结论 ＋ 逃逸空间改写（本档净产出）

$$\boxed{\textbf{三选一落在}\ \textbf{C}：\text{谱离散度}\ \textbf{不} \text{与 form-factor 偏离等价}} ✓✓✓$$
$$\qquad \text{但}\ \textbf{失败给出正面结构信息}：\text{障碍}\ \textbf{不在} \text{算术配对相关，而在}\ \textbf{证书几何常数} ✓✓✓$$
$$\boxed{\text{逃逸空间改写}：\mathcal E=\big\{K:\ c^{\rm geom}(K)\to1\big\}\ \text{（而非}\ F_{\rm pair}\to1\text{）}} ✓✓✓$$
$$\qquad \text{而}\ c^{\rm geom}\to1\iff\textbf{支撑}>1\ \text{的无条件化} ⟹ \textbf{三向统一在}\ \textbf{机制层} \text{被确认} ✓✓✓$$
$$\qquad \left(\text{即：}2/3\to1\iff\text{几何常数}\to1\iff\text{支撑}>1\ \text{无条件}\iff `V162`\ \text{墙}\iff\text{k=3 缺口}\right) ✓$$

---

## §7 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V299 判词}：\text{① }(F_{\rm pair}-1)\ \textbf{不进主项} ⟹ \textbf{判词 C};\ \text{② 理想}\ F\equiv1\ \text{已给}\ R_{\rm off}=0.3275>0 ⟹ \text{等价为假};\ \text{③ 两正性严格分离（未传递）};\ \text{④ 唯一杠杆＝几何常数} ⟺ \text{带宽}\to\text{支撑}>1} ✓✓✓$$

```
① ⚠️ §2／§3 的"主项不含配对相关偏离"为**本档判读[推断]**（依据 (eq:tr2) 两形式的**结构**——主项只含窗矩）
   ⟹ 与论文 §5 的求值细节**未逐行核对** ⚠️
② ⚠️ $c^{\rm geom}_{\phi}$ 在指示窗为 $0.75$、MT 窗为 $c_1^{*}$，取自 [thm:traces] 与 Theorem D 的读数（间接）⚠️
③ ⚠️ §4 的反例依赖"$F\equiv1$ 是 Montgomery 无条件区内的理想形态"（经典·引用，未复核原文）⚠️
④ ⚠️ $c_\lambda^{*}\le c_1^{*}$（$\lambda\le1$）取自 CCLM17 Cor.14 的**最优性**（引用，未复核）✓
⑤ **不声称** $W_\phi$ 不存在（只声称它不决定主项）；**不声称**任何非 Toeplitz 逃逸存在 ✓
⑥ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐ **判词 C**：$(F_{\rm pair}-1)$ **不进主项**（$\operatorname{tr}\hat G^2$ 主项 ＝ 经典窗矩 $\frac{TL}{2\pi}(\ell_1^2+\frac{L^2}3)$，不含零／素数输入）⟹ **焊接在主项层面失败** ✓✓✓
② ⭐⭐⭐ **$F_{\rm eff}=c^{\rm geom}_\phi+o(1)$**（不是 $F_{\rm pair}(\lambda)$）⟹ 正确的字典是 $$R_{\rm off}=\frac1{c^{\rm geom}_\phi}-1+o(1)$$ ✓✓
③ ⭐⭐⭐⭐ **决定性反例**：理想 $F_{\rm pair}\equiv1$ ⟹ $R_{\rm off}=1/c_1^{*}-1=0.3275>0$ ⟹ **"$R_{\rm off}\to0\iff F_{\rm pair}\to1$" 为假** ⟹ 谱离散度含**基线几何分量**，配对相关改进消不掉 ✓✓✓
④ ⭐⭐⭐ **两正性未传递**（谱方差正性 ⇏ 算术配对相关正性）✓✓
⑤ ⭐⭐⭐ **逃逸空间改写**：$$\mathcal E=\{K: c^{\rm geom}(K)\to1\}$$ ⟺ **支撑 $>1$ 的无条件化** ⟹ **三向统一在机制层确认** ✓✓✓
⑥ ⭐⭐ **误差次序**：$\lambda>2$ 时 $T^{\lambda/2-1}$ 爆炸 ⟹ 框架只在 $\lambda\lesssim1$ 有内容；而 $c^{\rm geom}\to1$ 需支撑 $\to\infty$ ⟹ **无条件带宽是硬需求** ✓✓
【下一步（唐先生既定；不先构造核）】
  (4a) **核验 §2／§3 的[推断]**：读论文 §5 的求值细节，确认"主项不含配对相关偏离"（这是本档全部结论的支点）✓
  (4b) 若 (4a) 确认 ⟹ 攻**几何常数 $c^{\rm geom}$ 的结构**：它作为窗口泛函的**最优化问题**（⊇ MT/CCLM 的问题；问 $\sup_\phi c^{\rm geom}(\phi)$ 在"有无条件控制"的约束下能否 $\to1$）✓✓
  (4c) 该最优化的**约束侧** ＝ 支撑：$\operatorname{supp}\widehat\psi\le\sigma$ 与 $c^{\rm geom}$ 的**定量关系**（路线图说 1.04/1.26/1.70 ⟹ 0.70/0.80/0.90 ⟹ 反解 $\sigma(c)$）✓✓✓
```
