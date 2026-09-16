# V302 · **(5a) §5/§6 主项恒等式审计：$c_1^{*}$ vs $3/4$** —— ⚠️ **V301 的变分结论撤回并重构**：常数是 $\boxed{c_\lambda(v;D)=\mathcal J_D(\lambda;v)/\lambda}$（**窗口 $v$ ＋ 权重 $D$ 的泛函**），**不是** $\lambda$ 的单元函数 ⟹ $\Delta_\phi=O(1)$（主项级）⟹ 但该类内**已被 MT／最优窗饱和**（$c_1^{*}=0.7532960$）⟹ 修正后：**$C_{\rm uncond}(\lambda\le1)=2-\frac1{c_1^{*}}=0.6725$**，故定量必要条件改为 $c>0.6725\Longrightarrow\lambda>1$

$$\boxed{\textbf{问题 2 答案}：\text{V301 的}\ c^{\rm geom}=\frac{\lambda}{1+\lambda^{2}/3}\ \textbf{不是精确主项};\ \text{漏掉了}\ D\text{-依赖} ⟹ \Delta_\phi=O(1)} ✓✓✓$$
$$\boxed{\textbf{正确结构（源码）}：c_\lambda(v;D)=\frac{\mathcal J_D(\lambda;v)}{\lambda},\qquad v\ \text{＝窗口},\ D\ \text{＝权重},\ 0<\lambda\le1} ✓✓✓$$
$$\boxed{\textbf{问题 1 答案}：0.7533>\tfrac34\ \text{因}\ \tfrac34\ \text{只是}\ \textbf{指示窗} \text{的值};\ \text{最优}\ (v,D)\ \text{给出}\ c_1^{*} ⟹ \textbf{窗口＋权重是主项级自由度}} ✓✓✓$$
$$\boxed{\textbf{问题 3 答案}：\Delta_\phi=O(1)\ (\text{主项级，泛函族});\qquad \lambda_1\ \text{vs}\ \lambda\ \text{之差}=O(1/l)\ (\text{渐近可忽略})} ✓✓$$
$$\boxed{\text{故按唐先生分叉：}\Delta_\phi=O(1)\ ⟹ \textbf{V301 变分结论撤回、}\ c_{\rm geom}\ \textbf{重构}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:32：**立即开 5a，不先做 5b/5c**；**这次不是普通再核对，而是恒等式级审计**，目标只有一个：$$\boxed{\text{论文的}\ F(\lambda_1)\ \stackrel{?}{=}\ \text{V301 推出的}\ c_{\rm geom}}$$ ✓；四个检查点 **A**（$a$ 是否唯一窗口依赖 —— 是否漏掉同阶 $\phi$-项）／**B**（$L^2/3$ 是否真固定 —— 变量替换是否含窗口）／**C**（$c_1^{*}=0.7532960$ 来自哪里 —— **本路线支点**）／**D**（"$a=1$"不能只作形式归一化 —— 须证 $\phi\in\mathcal A_\sigma\iff\phi/\sqrt a\in\mathcal A_\sigma$）✓✓✓；并命令：**"不要为了保住 V301 而补假设"**；分叉：$\Delta_\phi=o(1)$ ⟹ 锁死做 5b／$O(1/l)$ ⟹ 仍锁死渐近 $3/4$ 墙／**$O(1)$ ⟹ V301 变分结论撤回**／改变 $\lambda$ 定义 ⟹ 先重定义三元组 ✓✓✓
> 第一手依据（**本档现场读源码**）✓ `Zeta23/XiPrime/Window.lean`（**`cRatio_eq_cWin`／`vConv_nonneg`／`jWin_nonneg`／`cWin_pos`／`cWin_denom_pos`**）｜`XiPrime/Window/FlatAdm.lean`（**`admWindow_taper`／`av_taper`／`bv_taper`／`half_le_bv_taper`（"in fact 3/4 ≤ b"）**）｜`XiPrime/Window/Quartic.lean`（**`tendsto_cRatio_quartic`／`tendsto_cRatio_quartic_D1`**）｜`ChallengeDeps.lean`（`cMT` 闭式）｜`Defs.lean`（`a`／`b`／`ell1`）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值（除闭式）✓｜编号 ✓ `V302`（**今夜曾误发后释放；现按唐先生指定正式启用** ✓）

---

## §1 ⭐⭐⭐ 问题 2：V301 的公式**不精确**（漏掉 $D$-依赖）

$$\textbf{源码（`XiPrime/Window.lean` 逐字）}：\text{"the tree's ratio constant at}\ \mathcal J：＝\mathcal J_D(\lambda;v)/\lambda\ \textbf{IS}\ c_\lambda(v;D)"\ ⟹ \boxed{c_\lambda(v;D)=\frac{\mathcal J_D(\lambda;v)}{\lambda}} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{常数依赖}\ \textbf{三个} \text{对象}：\text{窗口}\ v;\ \text{权重}\ D;\ \text{带宽}\ \lambda\ ——\ \textbf{不是}\ \lambda\ \text{的单元函数} ✓✓✓$$
$$\qquad \textbf{伴随的约束（`cWin_pos`／`cWin_denom_pos`）}：c_\lambda(v;D)>0\ \text{当}\ 0<\lambda\le1,\ \int v\ne0,\ \int v^{2}>0,\ \mathcal J\ge0 ✓$$
$$\qquad \textbf{非负性（`jWin_nonneg`）}：\mathcal J_D(\lambda;v)\ge0\ \text{当}\ 0\le\lambda\le1,\ D\ge0\ \text{on}\ [0,1],\ v\ge0\ \text{on window} ✓$$
$$\Longrightarrow \boxed{\text{V301 的}\ c^{\rm geom}=\frac{a^{2}\lambda}{1+\lambda^{2}/3}\ \textbf{漏掉了}\ (v,D)\ \text{的泛函依赖} ⟹ \Delta_\phi=O(1)\ \textbf{（主项级）}} ✓✓✓$$

---

## §2 ⭐⭐⭐ 问题 1：$0.7533>\frac34$ 的原因

$$\frac34\ \text{是}\ \textbf{指示窗} \text{（}\psi\equiv1\text{）在}\ \lambda=1\ \text{时的}\ c_\lambda\ \text{值};\qquad c_1^{*}=0.7532960\ \text{是}\ \textbf{最优}\ (v,D)\ \text{在同带宽下的值} ✓✓$$
$$\qquad \Longrightarrow \textbf{窗口＋权重}\ \textbf{是主项级自由度}（\text{可改}\ 3/4\to0.7533\text{）};\ \text{量级}\ \Delta\approx0.0033\ ✓$$
$$\qquad \text{但（⚠️ 关键）}：\text{该类内}\ \textbf{已被 Theorem D 的}\ c_1^{*}\ \textbf{饱和} \text{（`CCLM17 Cor.14` 的最优性）} ⟹ \textbf{无进一步窗口增益} ✓✓✓$$
$$\qquad \text{读数}：2-\frac1{c_1^{*}}=0.67250\ldots\（\text{论文 Theorem D}）;\qquad 2-\frac1{3/4}=\frac23\（\text{指示窗}）✓$$

---

## §3 检查点 A／B／D（逐项）

$$\textbf{A（}a\ \text{是否唯一窗口依赖）}：\textbf{否} —— \text{常数含}\ D\text{-泛函与}\ v\ \text{形状依赖} ⟹ \text{V301 漏掉同阶项} ✓✓$$
$$\textbf{B（}L^{2}/3\ \text{是否真固定）}：\textbf{待定};\ \text{V301 归因}\ \frac13=\int_0^1x^{2}dx\ \text{为几何核};\ \text{但若变量替换含窗口（}`Quartic.lean`\ \text{的}\ vConv\ \text{结构暗示卷积型}\ v*v\ \text{参与}）\ \text{则"不可优化"}\ \textbf{不完全成立} ⚠️✓$$
$$\qquad （`vConv_nonneg`：\ (v*v)\ge0\ \text{on}\ [0,1]\ \text{当}\ v\ge0\ ——\ \textbf{卷积型窗口量}\ \text{确实出现}）✓✓$$
$$\textbf{D（}a=1\ \text{是否可设）}：\textbf{不可} \text{（唐先生正确）} —— \text{须证}\ \phi\in\mathcal A_\sigma\iff\phi/\sqrt a\in\mathcal A_\sigma;\ \text{而}\ \textbf{可容许类有额外约束}：$$
$$\qquad \text{`FlatAdm.lean` 逐字}：\text{taper}\ \phi=\varrho\big((L/2-|u|)/w\big)\ \text{为}\ \mathrm{AdmWindow};\qquad \textbf{"}1/2\le bv,\ \textbf{in fact}\ \frac34\le b\text{"} ✓✓$$
$$\qquad ⟹ \textbf{窗口的四阶矩}\ b\ \text{有下界}\ \frac34 ⟹ \text{可容许类}\ \textbf{非尺度不变} ⟹ \text{"}a=1\text{"不能无失一般性地施加} ✓✓✓$$
$$\qquad \Longrightarrow \text{V301 §2 的"尺度失败 ⟹ 必取}\ a=1\ ⟹\ \phi\text{-无关"}\ \textbf{推理链失效} ✗✓$$

---

## §4 $c_1^{*}$ 的来源（问题 1 的定位）与 $\lambda$ 层级（问题 3 的后半）

$$\text{来源（源码）}：`ChallengeDeps.lean`\ \text{逐字}：c^{*}_{\lambda}=\frac{\sqrt2\tan\vartheta}{1+\vartheta\tan\vartheta}\Big|_{\vartheta=\lambda/\sqrt2};\quad c_1^{*}=0.7532960\ldots;\quad \frac1{c_1^{*}}=\frac12+2^{-1/2}\cot\big(2^{-1/2}\big)\ ✓$$
$$\qquad \Longrightarrow \textbf{不是}\ \frac34+o(1),\ \textbf{也不是}\ \frac{a^{2}\lambda}{1+\lambda^{2}/3}\ \text{的同族};\ \text{而是}\ \textbf{Theorem D 的最优窗常数} ✓✓✓$$
$$\text{$\lambda$ 层级}：\lambda_1=\frac L{\ell_1}=\frac L{l+2\log2-1}=\lambda\Big(1-\frac{2\log2-1}{\ell_1}\Big)=\lambda\big(1+O(1/l)\big) ✓$$
$$\qquad ⟹ \lambda_1\ \text{vs}\ \lambda\ \text{之差}\ =O(1/l)\ \textbf{渐近可忽略} ⟹ \text{按分叉：}\textbf{仍锁死渐近墙}（\text{但墙的高度改为}\ c_1^{*}）✓✓$$

---

## §5 ⭐⭐⭐⭐ 结论与重构（按唐先生分叉行事）

$$\boxed{\textbf{分叉归属}：\Delta_\phi=O(1)\ \Longrightarrow\ \textbf{V301 的变分结论撤回，}\ c_{\rm geom}\ \textbf{重构}} ✓✓✓$$
$$\textbf{重构后（本档）}：$$
$$\qquad \boxed{\text{在}\ \lambda\le1：\quad C_{\rm uncond}(\lambda)=\sup_{v,D\ \text{可容许}}\frac{\mathcal J_D(\lambda;v)}{\lambda};\qquad C_{\rm uncond}(1)=c_1^{*}=0.7532960} ✓✓$$
$$\qquad \Longrightarrow \boxed{G=2-\frac1{c_1^{*}}=0.67250\（\text{最优窗}）};\qquad \text{指示窗}:\ G=\frac23 ✓✓$$
$$\qquad \Longrightarrow \boxed{\textbf{定量必要条件（修正版）}：c>0.6725\ \Longrightarrow\ \lambda>1} ✓✓✓$$
$$\qquad \qquad （\text{V301 原写}\ c>\frac34\Rightarrow\lambda>1\ —— \textbf{常数须更正为}\ 0.6725）✓$$
$$\textbf{必须撤回的 V301 结论}：$$
$$\qquad ✗\ c^{\rm geom}\ \text{与}\ \phi\ \text{无关};\quad ✗\ \text{"窗口非实质自由度"};\quad ✗\ \text{族内上界}\ \sqrt3/2=0.8660;\quad ✗\ \text{单变量 E–L 的约束最优}\ \frac34 ✓✓$$
$$\qquad \text{保留的 V301 结论}：\text{① }\ell_1=l+2\log2-1\ \text{为 T-确定（非自由度）};\ \text{② 主导杠杆仍是}\ \lambda;\ \text{③ 单向必要条件的形式（}\lambda>1\text{）} ✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V302 判词}：\text{① }c_1^{*}\ \text{来自 Theorem D（最优窗），非}\ \frac34+o(1);\ \text{② V301 公式漏}\ D\text{-依赖} ⟹ \Delta_\phi=O(1);\ \text{③ 窗口＋权重是主项级自由度但已被饱和（}0.7533\text{）};\ \text{④ 撤回 V301 变分结论并重构};\ \text{⑤ 修正必要条件}\ c>0.6725\Rightarrow\lambda>1} ✓✓✓$$

```
① ⚠️ §1–§3 依据 `XiPrime/Window*.lean` **语句级源码**（`cRatio_eq_cWin`、`cWin_pos`、`half_le_bv_taper` 等）；**未跑构建** ⚠️
② ⚠️ $c_\lambda(v;D)=\mathcal J_D(\lambda;v)/\lambda$ 为 `cRatio_eq_cWin` 的**逐字转述**；$\mathcal J_D$ 的**显式形式未展开**（仅知 $\ge0$ 与卷积结构 $v*v$）⚠️
③ ⚠️ $\frac13=\int_0^1x^2dx$ 的归属（检查点 B）**未定论** —— `vConv`（卷积型窗口量）暗示替换含窗口 ⚠️✓
④ ⚠️ "$C_{\rm uncond}(1)=c_1^{*}$" 依赖 `CCLM17 Cor.14` 的最优性（**引用，未复核**）⚠️
⑤ **不声称** $\lambda>1$ 足够（仅：$c>0.6725$ 需 $\lambda>1$）；**不声称** trace 路线整体 $c=1$ 不可达（撤回 V301 的族内上界）✓
⑥ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值（除闭式算术）✓
```

```
① ⭐⭐⭐ **问题 1**：$0.7533>\frac34$ 因 $\frac34$ 只是**指示窗**值；最优 $(v,D)$ 给 $c_1^{*}$ ⟹ **窗口＋权重是主项级自由度** ✓✓✓
② ⭐⭐⭐ **问题 2**：V301 公式**不精确**（漏 $D$-依赖）⟹ $\Delta_\phi=O(1)$ ⟹ **按分叉：撤回并重构** ✓✓✓
③ ⭐⭐ **问题 3**：$\Delta_\phi=O(1)$；$\lambda_1$ vs $\lambda$ 之差 $=O(1/l)$ ⟹ **渐近墙仍锁死，但墙高改为 $c_1^{*}$** ✓✓
④ ⭐⭐⭐ **重构**：$$C_{\rm uncond}(\lambda\le1)=\sup_{v,D}\frac{\mathcal J_D(\lambda;v)}{\lambda},\qquad C_{\rm uncond}(1)=c_1^{*}\Rightarrow G=0.6725$$ ⟹ **修正的定量必要条件 $c>0.6725\Rightarrow\lambda>1$** ✓✓✓
⑤ ⭐⭐ **撤回清单**（V301）：$\phi$-无关、窗口非自由度、族内上界 $\sqrt3/2$、单变量 E–L 的 $\frac34$；**保留**：$\ell_1$ 为 T-确定、$\lambda$ 仍是主导杠杆、必要条件形式 ✓✓
⑥ ⭐ **检查点 D 确认**：可容许类含 $b\ge\frac34$ 约束 ⟹ **非尺度不变** ⟹ V301 的"$a=1$"推理链失效 ✓✓
【下一步（严格按 5a 结果）】
  (5b) 在**重构后的**二元泛函问题下达 $\lambda\leftrightarrow\sigma$ 关系，把必要条件改写为 $$\boxed{c>0.6725\Longrightarrow\sigma>\sigma_{\rm uncond}}$$ ✓
  (5c) $\mathcal J_D$ 的**显式展开**（含 $v*v$ 卷积结构）—— 这是唯一能把"窗口已饱和"从引用升级为定理的入口 ✓
```
