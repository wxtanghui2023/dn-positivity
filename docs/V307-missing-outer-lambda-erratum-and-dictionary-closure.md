# V307 · **漏掉外层 $\lambda$ 的修正：系数链闭合，三个异常统一** —— ⭐⭐⭐⭐⭐ **正确分母 $Q_\lambda=\int v^{2}+\lambda\,\mathcal J_D=\int v^{2}+\lambda^{2}\langle v,Kv\rangle$ ⟹ E–L $(I+\lambda^{2}K)v=\kappa\mathbf 1$ ⟹ $\omega=\sqrt2\lambda$ ⟹ $w=\omega/2=\lambda/\sqrt2$** ⟹ **$C_{\rm cone}(\lambda)=c^{*}_\lambda$ 代数上直接一致（非巧合）**；⭐⭐⭐⭐ **三异常同源**（$C(2)=1.2179$、$\lambda=1$ 才相合、$\sqrt{\lambda/2}$ vs $\lambda/\sqrt2$ ＝ 同一个漏 $\lambda$）；⚠️ **T10 勘误：撤回 V306 的"隐藏 admissibility"判断与该告警**；⭐⭐⭐ **（c）字典闭合：$F(\lambda_1)=c_\lambda(v;D)$（源 W2）⟹ 0.67250 墙是真 F-ceiling（条件下 Theorem D 最优性）**

$$\boxed{\textbf{修正链（7 步闭链）}：\mathcal J_D=\lambda\langle v,Kv\rangle\Rightarrow Q_\lambda=\int v^{2}+\lambda^{2}\langle v,Kv\rangle\Rightarrow (I+\lambda^{2}K)v=\kappa\mathbf 1\Rightarrow v''+2\lambda^{2}v=0\Rightarrow \omega=\sqrt2\lambda\Rightarrow w=\frac\omega2=\frac{\lambda}{\sqrt2}\Rightarrow \boxed{C_{\rm cone}(\lambda)=c^{*}_\lambda}} ✓✓✓$$
$$\boxed{\textbf{代数核验}：v(\tfrac12)=w\cot w,\quad (Kv)(\tfrac12)=\frac12\ (\textbf{与}\ \omega\ \textbf{无关}!) ⟹ \kappa=w\cot w+\frac{\lambda^{2}}2=w\cot w+w^{2}} ⟹ C=\frac{\lambda}{\kappa}=\frac{\sqrt2w}{w\cot w+w^{2}}=\frac{\sqrt2\tan w}{1+w\tan w} ✓✓✓$$
$$\boxed{\textbf{三异常同源}：\sqrt{\lambda/2}\ \text{vs}\ \lambda/\sqrt2;\quad C(2)>1;\quad \text{仅}\ \lambda=1\ \text{相合}\ =\ \textbf{同一个漏掉的外层}\ \lambda} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:54：**"（b）应该先做，而且现在已经可以在给出的公式内部把这个频率差精确闭合"** —— **关键不是隐藏的 admissibility，而是 A′-② 写 E–L 时漏掉了 $\mathcal J_D$ 前面的 $\lambda$** ✓✓；给出完整系数链与结论 **$C_{\rm cone}(\lambda)=c^{*}_\lambda$ 代数上直接一致（"不是六位巧合"）** ✓✓；指出 **$F\le1$ 告警"也不是新的 normalization contradiction"**，是同一漏 $\lambda$ 造成的**假异常**；**三个异常＝同一个系数错误的三个表现** ✓✓✓；并要求 **V306 的"存在隐藏 admissibility"判断（就频率而言）改正** ✓；**修订顺序：(b) ✓ → (c) 定标字典 → (a) admissibility 全审计** ✓✓
> 依据 ✓ `XiPrime/Window.lean`（(W2)：$\lambda_1(T)\to\lambda$、$a_T\to\int v$、$b_T\to\int v^2$、$J_T\to\mathcal J_D(\lambda;v)/\lambda$ ⟹ $\mathrm{cRatio}\to c_\lambda(v;D)$）｜`V303`／`V305`／`V306` ✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；数值仅闭式算术 ✓｜编号 ✓ `V307`（先领号 ✓）

---

## §1 系数链（逐项核验，含"漏 $\lambda$"处）

$$\textbf{① 源公式}：c_\lambda(v;D)=\frac{\lambda(\int v)^{2}}{\int v^{2}+\lambda\,\mathcal J_D(\lambda;v)} ✓$$
$$\textbf{② A′-① 结果}：\mathcal J_D(\lambda;v)=\lambda\langle v,Kv\rangle,\ K(x,y)=|x-y| ✓$$
$$\textbf{③ ⚠️ 我 V306 的漏项处}：\text{分母}：\int v^{2}+\lambda\,\underbrace{\mathcal J_D}_{=\lambda\langle v,Kv\rangle}=\boxed{\int v^{2}+\lambda^{2}\langle v,Kv\rangle} ⟹ \boxed{(I+\lambda^{2}K)v=\kappa\mathbf 1} ✓✓✓$$
$$\qquad \text{（V306 误写为}\ (I+\lambda K)v=\kappa\mathbf 1\text{）}$$
$$\textbf{④}：(Kv)''=2v ⟹ v''+2\lambda^{2}v=0 ⟹ \boxed{\omega=\sqrt2\,\lambda};\qquad \textbf{⑤}\ w：＝\frac\omega2=\boxed{\frac{\lambda}{\sqrt2}}\ ✓✓✓$$
$$\textbf{⑥ 归一化}：\int v=1 ⟹ A=\frac\omega{2\sin(\omega/2)}=\frac w{\sin w};\qquad v(\tfrac12)=A\cos w=\boxed{w\cot w} ✓$$
$$\textbf{⑦ 取值条件}：(Kv)(\tfrac12)=\int_{-1/2}^{1/2}\big(\tfrac12-y\big)v(y)dy=A\cdot\frac{\sin(\omega/2)}{\omega}=\boxed{\frac12}\ \textbf{（与}\ \omega\ \textbf{无关！）} ✓✓$$
$$\qquad \kappa=v(\tfrac12)+\lambda^{2}(Kv)(\tfrac12)=w\cot w+\frac{\lambda^{2}}2\ \overset{\lambda=\sqrt2w}{=}\ w\cot w+w^{2} ✓$$
$$\qquad C_{\rm cone}(\lambda)=\frac{\lambda}{\kappa}=\frac{\sqrt2w}{w\cot w+w^{2}}=\frac{\sqrt2}{w+\cot w}=\boxed{\frac{\sqrt2\tan w}{1+w\tan w}\Big|_{w=\lambda/\sqrt2}}=\ c^{*}_\lambda\ \textbf{（代数恒等）} ✓✓✓$$

---

## §2 三个异常的统一（同一个漏 $\lambda$）

$$\text{(i) 频率}：\sqrt{\lambda/2}\ \text{vs}\ \lambda/\sqrt2 ⟹ \text{修正后一致 ✓};\qquad \text{(ii)}\ C_{\rm cone}(2)：$$
$$\qquad \text{旧（错）}：w=\sqrt{\lambda/2}=\sqrt1=1 ⟹ C=1.2179>1\ ✗;\qquad \text{新（对）}：w=\frac2{\sqrt2}=\sqrt2：$$
$$\qquad \qquad C=\frac{\sqrt2\tan\sqrt2}{1+\sqrt2\tan\sqrt2}=\frac{1.414214\times6.28505}{1+8.88959}=0.8990\ldots<1 ✓✓✓$$
$$\qquad \text{(iii) 仅}\ \lambda=1\ \text{相合}：\text{因}\ \sqrt{\lambda/2}=\lambda/\sqrt2\iff\lambda=1 ⟹ \textbf{假巧合} ✓$$
$$\Longrightarrow \boxed{\text{三者＝同一个系数错误的三个表现（唐先生判断成立）}} ✓✓✓$$

---

## §3 ⚠️【勘误 T10】（撤回 V306 的相应判断）

$$\text{(a)}\ \textbf{撤回}：\text{"Cor.14 存在}\ \mathcal J_D\ \text{表面公式看不到的额外 admissibility／边界条件"}\ ——\ \textbf{就频率而言不成立} ✓✓$$
$$\qquad \text{正确诊断}：\text{漏掉外层}\ \lambda\ (\text{我 V306 §2 误用}\ (I+\lambda K));\ \text{已按 §1 修正} ✓$$
$$\text{(b)}\ \textbf{撤回}：\text{"}F\le1\ \text{告警／normalization 字典冲突"}\ ——\ \text{假异常（修正后}\ C(2)=0.899<1\ ✓）✓✓$$
$$\text{(c)}\ \textbf{保留（V306 仍有效部分）}：\text{① 核}\ K=|x-y|\ \text{（独立验算）};\ \text{② "二阶 ODE＋一阶端点＋归一化只给恒等式"（修正后为}\ \omega^{2}=2\lambda^{2}，仍是恒等式 ✓）；\ \text{③ 取值条件确定}\ \kappa ✓$$

---

## §4 A3 状态更新（实质变化）

$$\textbf{原状态}：\text{"存在未解释的 admissibility／边界缺口"}\ ✗ ⟹ \textbf{新状态}：\text{"变分核与闭式之间的}\ \textbf{频率标度已解释}"\ ✓✓$$
$$\boxed{\text{但仍}\ \textbf{不能说 A3 全证}};\ \text{剩余五项审计}：$$
$$\qquad \text{(i) }\mathcal A\ \text{的准确 admissibility 定义};\quad \text{(ii) 极值解是否}\ v\ge0\（\text{锥}）;\quad \text{(iii) 偶对称化是否保持 admissibility};$$
$$\qquad \text{(iv) E–L 解是}\ \textbf{全局} \text{极值而非仅驻点};\quad \text{(v) `CCLM17 Cor.14` 与该变分问题的}\ \textbf{精确对应} ✓✓$$

---

## §5 ⭐⭐⭐ **（c）字典闭合（初步，源支持）**

$$\text{(W2)（`XiPrime/Window.lean` docstring 逐字）}：\lambda_1(T)\to\lambda,\ a_T\to\textstyle\int v,\ b_T\to\textstyle\int v^{2},\ J_T\to\mathcal J_D(\lambda;v)/\lambda ⟹ \mathrm{cRatio}(\cdots)\to c_\lambda(v;D) ✓$$
$$\qquad ⟹ \boxed{F(\lambda_1)=c_\lambda(v;D)}\ \textbf{（不是倒数，也不差额外的}\ N／\ell_1／L\ \text{因子 —— 那些已在}\ c_\lambda\ \text{内部）} ✓✓$$

$$\qquad \Longrightarrow \boxed{G=2-\frac1{F_{(\text{最优窗})}},\qquad F_{\rm opt}(1)=c_1^{*}=0.7532960 ⟹ G_{\max}(1)=0.67250} ✓✓$$
$$\qquad \qquad ⟹ \boxed{\textbf{0.67250 墙是真 F-ceiling}}\（\textbf{条件}：\S4\ \text{的 (i)–(iv) 成立}）✓✓✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V307 判词}：\text{① 漏外层}\ \lambda\ \text{已修正};\ \text{② }C_{\rm cone}=c^{*}_\lambda\ \text{代数恒等};\ \text{③ 三异常同源};\ \text{④ V306 判断撤回（T10）};\ \text{⑤ (c) 字典闭合} ⟹ \text{墙为真 F-ceiling}} ✓✓✓$$

```
① ⚠️ 本档全部为**纸面推导**（可人工复核）；未跑 Lean ✓
② ⚠️ §5 的"F = c_λ"依赖 (W2) 的**转述**（我读的是 docstring，未逐行核对 CoeffMoments 的形式化）⚠️
③ ⚠️ §5 的"F_opt(1)=c₁*"仍是 **Theorem D 的最优性claim**（＝§4 (i)–(iv) 的内容）⟹ **条件性** ✓
④ **不声称** A3 全证；**不声称** CCLM17 已内生；**不声称** 论文有误（前一条错误是我的）✓
⑤ 未用 RH ✓；零数值（仅闭式算术）✓
```

```
① ⭐⭐⭐⭐⭐ **修正链闭合**：$$\lambda\ \text{漏项} ⟹ (I+\lambda^2K)v=\kappa\mathbf1 ⟹ \omega=\sqrt2\lambda ⟹ w=\lambda/\sqrt2 ⟹ C_{\rm cone}=\frac{\sqrt2\tan w}{1+w\tan w}=c^{*}_\lambda$$ **代数恒等（非巧合）** ✓✓✓
② ⭐⭐⭐ **关键简化**：$$(Kv)(\tfrac12)=\tfrac12\ \textbf{与}\ \omega\ \textbf{无关}$$ ⟹ 使 $\kappa$ 与 $C$ 的闭式一步即得 ✓✓
③ ⭐⭐⭐⭐ **三异常统一**（频率／$C(2)>1$／仅 $\lambda=1$ 相合）⟹ 同一漏 $\lambda$ ✓✓✓
④ ⚠️ **T10 撤回**：V306 的"隐藏 admissibility（频率部分）"＋"$F\le1$ 告警"**均撤回**；保留核识别与"恒等式"结论 ✓✓
⑤ ⭐⭐⭐ **(c) 字典闭合**：$F(\lambda_1)=c_\lambda(v;D)$（源 W2）⟹ **0.67250 墙为真 F-ceiling**（条件下 (i)–(iv)）✓✓
⑥ ⭐⭐ **A3 剩余清单**：$\mathcal A$ 定义／$v\ge0$ 锥／偶对称化保持性／**全局性**／CCLM17 精确对应 ✓
【下一步（按修订顺序）】
  (c′) **加固字典**：核对 `CoeffMoments`／`ThmD/Limit.lean` 的形式化，把 (W2) 从转述升为逐行 ✓
  (a′) **admissibility 全审计**：读 `Window/{FlatAdm,Quartic}.lean` ＋ `Statement.lean §4`（`WindowProfile vFlat/vQuartic`），逐项验 §4 (i)–(iv) ⟹ 这才是 A3 的真正剩余 ✓✓
```
