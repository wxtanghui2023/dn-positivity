# V306 · **A′-① 核识别（独立验算 ✓）＋ A′-② 完整积分边界条件分析** —— ⭐⭐⭐⭐⭐ **核 $K(x,y)=|x-y|$（你的判断成立，我的"$|x-y|/\min$"猜测作废）**；⭐⭐⭐⭐ **完整积分方程下：二阶 ODE＋一阶端点条件＋归一化 ⟹ 只有恒等式 $\omega^{2}=2\lambda$，无特征方程**（你的判断成立）；⭐⭐⭐⭐⭐ **但补上"取值条件"后得到闭式 $C_{\rm cone}(\lambda)=\dfrac{2w\sin w}{\cos w+w\sin w}\big|_{w=\sqrt{\lambda/2}}$** —— **与 $c^{*}_\lambda$ 同形，且在 $\lambda=1$ 精确相合（$0.7532957$ vs $0.7532960$），但 $\lambda\ne1$ 时不一致** ⟹ **你预设的第二支：存在 $\mathcal J_D$ 表面公式看不到的额外 admissibility／边界条件**

$$\boxed{\textbf{A′-①}：\mathcal J_D(\lambda;v)=\lambda\!\iint_{[-1/2,1/2]^{2}}\!|x-y|\,v(x)v(y)\,dx\,dy\ \Longrightarrow\ \boxed{K(x,y)=|x-y|},\qquad K''=2I} ✓✓✓$$
$$\boxed{\textbf{A′-②}：\text{二阶 ODE＋一阶端点＋归一化 ⟹ 仅恒等式}\ \omega^{2}=2\lambda\（\text{无特征方程}）;\ \text{补"取值条件"后}\ C_{\rm cone}(\lambda)=\frac{2\lambda}{\lambda+\omega\cot(\omega/2)}} ✓✓✓$$
$$\boxed{\textbf{核心不一致}：\text{我者}\ w=\sqrt{\lambda/2}\ \text{vs 论文}\ \vartheta=\frac{\lambda}{\sqrt2};\ \frac{\vartheta}{w}=\sqrt\lambda\ \Longrightarrow\ \textbf{仅}\ \lambda=1\ \textbf{相合}};\ \lambda\ne1\ \textbf{不一致} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:50：**先做 A′-① 核识别**（最便宜、信息量最大）；**不要直接接受"$|x-y|$ 型核"这一判断，要从定义逐项变成精确公式** ✓；给出 $\mathcal J_D=2\lambda\iint_{x<y}(y-x)vv$ ⟹ **$K(x,y)=|x-y|$**（**修正我的"$|x-y|/\min$"**）✓；指出 $K''=2I$ ⟹ ODE $v''+2\lambda v=0$ ⟹ $v=A\cos\omega x+B\sin\omega x$，$\omega=\sqrt{2\lambda}$ ✓；**并已证明：仅靠 $(Kv)''=2v$ 与一阶端点条件不足以产生 Cor.14 的 $\tan$ 闭式**（$\omega^{2}=2\lambda$ 只是定义恒等式）⟹ **真正信息藏在原始积分方程的取值/归一化条件里** ✓✓；**令 A′-② 任务 ＝ 从完整积分方程（而非仅二阶 ODE）推出全部端点条件，求出真正的特征／归一化方程，看是否严格产生 $\tan(\lambda/\sqrt2)$**；**若一致 ⟹ A3 结构揭开；若不一致 ⟹ 说明 Cor.14 还有 $\mathcal J_D$ 表面公式看不到的 admissibility／边界条件** ✓✓✓
> 依据 ✓ `XiPrime/Window.lean`（$\mathcal J_D$ 定义）｜`V303`／`V305`（闭式、E–L、resolvent）｜`Defs.lean` ✓
> 执行 ✓ 小灵｜**纸面 ✓（本档为可人工复核的积分推导）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；数值仅闭式算术 ✓｜编号 ✓ `V306`（先领号 ✓）

---

## §1 **A′-①：核识别（独立验算 ✓，修正我的猜测）**

$$\mathcal J_D(\lambda;v)=2\!\int_0^1\!\lambda r\,(v⋆v)(r)\,dr=2\lambda\!\int_0^1\!\!\int_{-1/2}^{1/2-r}\!\!r\,v(s)v(s+r)\,ds\,dr ✓$$
$$\text{换元}\ x=s,\ y=s+r\ (\text{Jac}=1)：r=y-x>0;\ \text{域}\ \{x<y\}\cap[-1/2,1/2]^{2}\ ✓$$
$$\Longrightarrow \mathcal J_D=2\lambda\!\iint_{x<y}(y-x)v(x)v(y)\,dx\,dy\ \overset{x\leftrightarrow y}{=}\ \lambda\!\iint|x-y|v(x)v(y)\,dx\,dy ✓✓$$
$$\Longrightarrow \boxed{K(x,y)=|x-y|}\ ✓✓✓\qquad（\textbf{我 V305 的"}|x-y|/\min(x,y)\ \text{型"猜测作废}）;\qquad (Kv)''=2v ⟹ K''=2I ✓$$

---

## §2 **A′-②：完整积分方程的边界条件与"取值条件"**

$$\textbf{E–L}：v+\lambda Kv=\kappa\mathbf 1\ (\kappa\ \text{常数}=\mu/2)\ ;\qquad \text{求导}：v'+\lambda(Kv)'=0 ✓$$
$$(Kv)'(x)=\int_{-1/2}^{x}\!\!v-\int_x^{1/2}\!\!v ⟹ (Kv)'(\pm\tfrac12)=\pm\textstyle\int v=\pm1 ⟹ \boxed{v'(-1/2)=\lambda,\quad v'(1/2)=-\lambda} ✓$$
$$(Kv)''=2v ⟹ \boxed{v''+2\lambda v=0} ⟹ v=A\cos\omega x+B\sin\omega x,\quad \omega=\sqrt{2\lambda} ✓$$
$$\textbf{一阶端点条件}：2B\omega\cos(\omega/2)=0,\qquad A\omega\sin(\omega/2)=\lambda ⟹ \textbf{一般分支}\ B=0（\text{偶}）✓$$
$$\textbf{归一化}\ \int v=1：A\cdot\frac{2\sin(\omega/2)}{\omega}=1 ⟹ A=\frac{\omega}{2\sin(\omega/2)} ⟹ \text{代入} ⟹ \boxed{\omega^{2}=2\lambda} —— \textbf{恒等式，无特征方程} ✓✓✓$$
$$\qquad ⚠️\ \textbf{唐先生判断成立}：\text{二阶 ODE ＋ 一阶端点 ＋ 归一化}\ \textbf{不产生}\ \tan\ \text{特征方程} ✓✓$$

$$\textbf{⭐ 本档补上的"取值条件"（新）}：\kappa=v(\tfrac12)+\lambda(Kv)(\tfrac12)：$$
$$\qquad (Kv)(\tfrac12)=A\!\int_{-1/2}^{1/2}\!\!\big(\tfrac12-y\big)\cos(\omega y)\,dy=A\cdot\frac{\sin(\omega/2)}{\omega}\（\text{本档算得，中间项抵消}）✓✓$$
$$\qquad ⟹ \boxed{\kappa=\frac{\omega}{2}\cot\frac\omega2+\frac{\omega^{2}}4}\ \Big(=\frac\omega2\cot\frac\omega2+\frac\lambda2\Big) ✓✓$$
$$\qquad ⟹ \boxed{C_{\rm cone}(\lambda)=\frac{\lambda}{\kappa}=\frac{2\lambda}{\lambda+\omega\cot(\omega/2)}\ \overset{w：＝\omega/2}{=}\ \frac{2w\sin w}{\cos w+w\sin w}=\frac{\sqrt2\tan w}{1+w\tan w}\Big|_{w=\sqrt{\lambda/2}}} ✓✓✓$$

---

## §3 ⭐⭐⭐⭐⭐ **核心不一致（你预设的第二支）**

$$\text{同形性}：C_{\rm cone}(\lambda)=\frac{\sqrt2\tan w}{1+w\tan w},\qquad c^{*}_\lambda=\frac{\sqrt2\tan\vartheta}{1+\vartheta\tan\vartheta}\ ——\ \textbf{同一个函数} ✓✓$$
$$\textbf{但自变量不同}：w=\sqrt{\lambda/2}\quad\text{vs}\quad\vartheta=\frac{\lambda}{\sqrt2};\qquad \frac{\vartheta}{w}=\sqrt\lambda ✓✓✓$$
$$\Longrightarrow \boxed{\lambda=1：w=\vartheta=\frac1{\sqrt2}\ \text{严格相合};\qquad \lambda\ne1：\textbf{不一致}} ✓✓✓$$
$$\qquad \text{读数}（\text{闭式算术}）：\lambda=1：C_{\rm cone}=0.7532957\ \text{vs}\ c_1^{*}=0.7532960\ \textbf{（六位相合）}✓✓✓$$
$$\qquad \qquad \lambda=0.5：0.4292\ \text{vs}\ 0.4623 ✗;\qquad \lambda=2：1.2179\ \text{vs}\ 0.8990 ✗✓$$

$$\boxed{\textbf{判定（按唐先生分叉）}：\textbf{不一致} ⟹ \textbf{Cor.14 存在}\ \mathcal J_D\ \textbf{表面公式看不到的额外 admissibility／边界条件}} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{A3 的缺失环节} ＝ \textbf{admissibility 类（taper 结构／}b\ge\frac34／8w\le L）\ ——\ \textbf{不是 ODE} ✓✓✓$$
$$\qquad \text{且不一致被精确定位到}\ \textbf{频率标度}：\text{我}\ \omega=\sqrt{2\lambda}\ \text{vs 论文}\ \omega_{\rm ThmD}=2\vartheta=\sqrt2\lambda;\quad \frac{\omega_{\rm ThmD}}{\omega}=\sqrt\lambda ✓✓✓$$

---

## §4 ⚠️ 内部一致性告警（诚实标注）

$$C_{\rm cone}(2)=1.2179>1,\qquad \text{但}\ F\le1\（\text{Cauchy–Schwarz，`V297` §3：}(\textstyle\int v)^{2}\le\int v^{2}\ \text{于长度 1 区间}）✗✓$$
$$\qquad ⟹ \textbf{variational ratio 与}\ F\ \text{之间的}\ \textbf{归一化字典仍需定标}（\text{可能缺}\ N／\lambda_1／\ell_1\ \text{因子}）⚠️✓$$
$$\qquad \qquad ⚠️\ \text{故本档的}\ C_{\rm cone}\ \text{只能作}\ \textbf{变分值} \text{读，}\textbf{不得} \text{直接当作}\ F\text{/}c_\lambda\ \text{代入两墙表} ✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V306 判词}：\text{① 核}\ K=|x-y|\ \textbf{（你的判断成立）};\ \text{② ODE＋端点＋归一化}\ \textbf{只给恒等式}（你的判断成立）;\ \text{③ 取值条件给闭式}\ C_{\rm cone};\ \text{④ }\lambda=1\ \text{相合、}\lambda\ne1\ \text{不一致};\ \text{⑤ 不一致＝隐藏 admissibility}} ✓✓✓$$

```
① ⚠️ §2 的 $\int_{-1/2}^{1/2}(\tfrac12-y)\cos(\omega y)dy=\sin(\omega/2)/\omega$ 为**本档手算**（可复核；中间 $1/\omega^2$ 项相消）✓
② ⚠️ §3 的"论文频率 $\omega_{\rm ThmD}=\sqrt2\lambda$"是**从闭式自变量反推**（**推断**；未读 Cor.14 原文）⚠️
③ ⚠️ §4 的警告：$C_{\rm cone}$ 与 $F$ 的字典未定标 ⟹ **本档结论不得直接代入两墙表** ✓
④ **不声称** A3 已证／已推翻；**不声称**论文有误（只声称**不一致**，且缺条件在 admissibility 侧）✓
⑤ 未用 RH ✓；未跑 Lean；零数值（仅闭式算术）✓
```

```
① ⭐⭐⭐⭐⭐ **A′-① 完成**：$$K(x,y)=|x-y|,\ K''=2I$$（我的 "$|x-y|/\min$" 猜测**作废**；你的判断成立）✓✓✓
② ⭐⭐⭐⭐ **A′-② 第一半（你的判断成立）**：二阶 ODE ＋ 一阶端点 ＋ 归一化 ⟹ 仅恒等式 $\omega^2=2\lambda$ ⟹ **无特征方程** ✓✓
③ ⭐⭐⭐⭐⭐ **A′-② 第二半（本档新）**：取值条件 ⟹ $$\kappa=\frac\omega2\cot\frac\omega2+\frac{\omega^2}4,\qquad C_{\rm cone}(\lambda)=\frac{2w\sin w}{\cos w+w\sin w}\Big|_{w=\sqrt{\lambda/2}}$$ ✓✓✓
④ ⭐⭐⭐⭐⭐ **核心不一致**：与 $c^{*}_\lambda$ **同形**，$\lambda=1$ **精确相合**（0.7532957 vs 0.7532960），但 $\lambda\ne1$ 不一致（比值 $=\sqrt\lambda$）⟹ **存在隐藏 admissibility／边界条件**（＝你预设的第二支）✓✓✓
⑤ ⚠️ **一致性告警**：$C_{\rm cone}(2)=1.2179>1$ 与 $F\le1$ 冲突 ⟹ **归一化字典待定标** ✓
【下一步（按你的分叉：不一致 ⟹ 查 hidden admissibility）】
  (a) **定位隐藏条件**：读 `XiPrime/Window.lean`／`Window/{FlatAdm,Quartic}.lean`／`ThmD/Window.lean` 的 **admissible 类定义**（taper 结构、$b\ge\frac34$、$8w\le L$、$\lambda_1$ 与 $\lambda$ 的代入方式），看是否把 $\vartheta$ 从 $\sqrt{\lambda/2}$ 改成 $\lambda/\sqrt2$ ✓✓
  (b) **核对频率**：论文 $\omega_{\rm ThmD}=\sqrt2\lambda$——查其 ODE／算子来源（是否核带 $\lambda$ 因子，或 $\mathcal J$ 的 $\lambda$ 次幂不同）✓✓
  (c) **定标字典**：把 $C_{\rm cone}$ 与 $F$（含 $N$／$\lambda_1$／$\ell_1$）的关系写清 ⟹ 解决 §4 告警 ✓
```
