# V313 · **(1) `Functional`／`Endgame` 最优性审计** —— ⭐⭐⭐⭐⭐ **结果：(A) 达到性在库内，(E) 最优性定理在库内【缺失】** （`Functional.lean` 只证 `cStar` 的初等性质；最优性归因于论文 **[thm:D]「Montgomery–Taylor optimal」**）；⭐⭐⭐⭐⭐ **但 (E) 可由我们自己的链补上**：V309 严格凸（$H_\lambda\ge\frac12I$）⟹ $\{\int v=1\}$ 上唯一全局极小 ⟹ $\sup c_{\rm Fun}=\lambda/\kappa=c^{*}_\lambda$ ⟹ **等式情形 ＝ 射线 $\{t\,v_\star\}$**（尺度不变性）⟹ **窄墙闭合**

$$\boxed{\textbf{审计结果}：\texttt{Functional.lean}\ \text{的定理}\ = \{\theta/c^{*}\ \text{的初等性质}\}\ \textbf{无最优性定理}} ✓✓✓$$
$$\boxed{\textbf{(A) 达到性}\ ✓\ \text{库内}：\text{MT 窗}\ c\to c^{*}_\lambda+O(w/L+1/l)\（\texttt{AssemblyD.lean:27}）} ✓✓$$
$$\boxed{\textbf{(E) 最优性}\ ✗\ \text{库内缺失} ⟹ \text{归因于论文}\ \texttt{[thm:D]}\ \text{"Montgomery–Taylor optimal"}（\texttt{Final.lean:7}）} ✓✓✓$$
$$\boxed{\textbf{补法（本档）}：\text{V309 严格凸}\ (H_\lambda\ge\tfrac12I)\ \Longrightarrow\ \sup_{\{\int v=1\}}c_{\rm Fun}=\frac\lambda\kappa=c^{*}_\lambda;\ \textbf{等式情形}=\{t\,v_\star\}} ✓✓✓$$
$$\boxed{\textbf{窄墙闭合}：\sup_{\mathcal A_{\rm ThmD}}c_{\rm Fun}=c^{*}_\lambda\ \textbf{（模 P2／P3 ＋「V309 为纸面证明」两项登记）}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 14:14：**(1) 先审 `Functional`／`Endgame` 的最优性证明**（而非先做 P2/P3）；**P1-YES 已闭合"候选属于 ThmD admissible class"，但要把 $F_{\rm opt}(1)=c_1^{*}$ 写成链内已证，必须区分** **(E)** $c_{\rm Fun}(\lambda,v)\le c^{*}_\lambda\ \forall v\in\mathcal A_{\rm var}$ 与 **(A)** $c_{\rm Fun}(\lambda,v^{*}_\lambda)=c^{*}_\lambda$ ✓✓；**只查四件事**：① 最优性 theorem 的精确 statement；② 其 hypothesis 是否正好覆盖当前变分域（even／$v>0$／$v\le1$／正则性／归一化／是否允许一般 $L^{2}$／$\lambda$ 精确范围）—— **防"子类极值 ≠ 全局极值"**；③ equality／uniqueness（是否明确由 $v\propto v_\star$ 刻画）；④ 最后拼三条链 $$\sup_{\mathcal A_{\rm var}}c_{\rm Fun}=c^{*}_\lambda\Rightarrow v^{*}_\lambda\in\mathcal A_{\rm ThmD}\Rightarrow\sup_{\mathcal A_{\rm ThmD}}\ge c^{*}_\lambda\ \text{＋}\ \mathcal A_{\rm ThmD}\subseteq\mathcal A_{\rm var}\Rightarrow\sup_{\mathcal A_{\rm ThmD}}=c^{*}_\lambda$$ ✓✓✓；并强调 **P1-YES ＋ 全变分最优性已足以解决"严格子集"问题，无需两 admissible class 相等** ✓✓✓
> 第一手依据（**本档直读源码**）✓ `ThmD/Functional.lean`（定义与定理清单）｜`ThmD/Final.lean`（7、13、49–50 行）｜`ThmD/AssemblyD.lean`（27、53–54 行）｜`ThmD/Endgame.lean`（15 行）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V313`（先领号 ✓）

---

## §1 **`Functional.lean` 定理清单（逐条）**

$$\text{定义}：\texttt{theta}（\vartheta=\lambda/\sqrt2）,\ \texttt{vStar},\ \texttt{cStar},\ \texttt{cFun},\ \texttt{aStar／bStar／jStar},\ \texttt{HD}（=2-1/c^{*}）✓$$
$$\text{定理（全部为**初等性质**）}：\texttt{theta\_nonneg／theta\_pos／theta\_le／sqrt\_two\_inv\_lt\_one／theta\_sq\_le／theta\_lt\_pi\_div\_two／}$$
$$\qquad \texttt{sin\_theta\_nonneg／sin\_theta\_pos／cos\_theta\_pos／cStar\_denom\_ge／cStar\_pos／cStar\_lipschitzOn／cStar\_continuousOn} ✓$$
$$\boxed{\text{其中}\ \textbf{没有} \ \forall v,\ c_{\rm Fun}(\lambda,v)\le\texttt{cStar}\,\lambda\ \text{形式的定理}} ✓✓✓$$
$$\qquad ⚠️\ \text{注意}\ \texttt{Functional.lean}\ \text{头部注释自述}：\text{"the scale-free variational objects of the paper §7.1 [subsec:MT]: [eq:cv] the functional, [eq:vstar] the optimal profile, …"} ⟹ \textbf{该文件定位为"定义＋初等性质"} ✓✓$$

---

## §2 **最优性归因：论文 [thm:D]（外部引用）**

$$\texttt{Final.lean:7}（逐字）：\text{"Zeta23/ThmD/Final.lean — \textbf{Theorem D} (the paper §8.1 [thm:D], the \textbf{Montgomery–Taylor optimal} …)"} ✓✓$$
$$\texttt{AssemblyD.lean:27}（逐字）：\text{"Flat top }(a=b=1,\ J=1/3)：c=F(\lambda_1);\ \textbf{Montgomery–Taylor window}:} c\to\texttt{cStar}\,\lambda+O(w/L+1/l)\text{"} ✓✓$$
$$\Longrightarrow \boxed{\text{(A) 达到性}\ ✓\ \text{库内（MT 窗的极限）};\qquad \text{(E) 全局上界}\ ✗\ \text{库内缺失（＝Theorem D 的最优性引用）}} ✓✓✓$$
$$\qquad ⚠️\ \text{故按你的判据}：\text{单看库内}，0.67250\ \text{是"链内已定义 ＋ 链内已证达到 ＋ }\textbf{最优性依赖外部引用}\text{"} ✓$$

---

## §3 ⭐⭐⭐⭐⭐ **(E) 的补法：用我们自己的 V307／V309**

$$\text{关键}：\text{最大化}\ c_{\rm Fun}=\frac{\lambda(\int v)^{2}}{Q_\lambda(v)}\ \textbf{尺度不变} ⟹ \text{归约为}\ \min\{Q_\lambda(v):\ \int v=1\} ✓$$
$$\qquad Q_\lambda(v)=\int v^{2}+\lambda^{2}\iint|s-s'|vv\（\texttt{cFun}\ \text{的分母，源码逐字一致}）✓$$
$$\qquad \textbf{V309 已证}：H_\lambda=I+\lambda^{2}K\ge\tfrac12I>0\（0<\lambda\le1）⟹ Q_\lambda\ \textbf{严格凸} ✓✓$$
$$\qquad \text{约束}\ \int v=1\ \text{是仿射超平面} ⟹ \textbf{严格凸函数在其中的极小点唯一且全局} ✓✓✓$$
$$\qquad \text{驻点}\ = \text{E–L}\ (I+\lambda^{2}K)v=\kappa\mathbf 1\ ⟹ \min Q=\kappa\（\text{V307}：\kappa=w\cot w+w^{2}）✓$$
$$\Longrightarrow \boxed{\sup_{\{\int v=1\}}c_{\rm Fun}=\frac{\lambda}{\kappa}=c^{*}_\lambda}\ \textbf{（V307 闭式，已于 }\lambda=1\ \text{核对 0.7532960）} ✓✓✓$$
$$\textbf{等式情形（你的第③项）}：\text{extremizer 满足}\ (I+\lambda^{2}K)v=\kappa\mathbf 1 ⟹ \text{解空间为}\ \textbf{仿射直线};\ \text{配合偶对称 ⟹ 唯一到尺度} ⟹ \boxed{\{v:\ c_{\rm Fun}=c^{*}_\lambda\}=\{t\,v_\star\}_{t\ne0}} ✓✓✓$$
$$\qquad ⚠️\ \text{无遗漏比例自由度：}\text{因}\ c_{\rm Fun}\ \text{尺度不变，}\{t\,v_\star\}\ \text{正是全部等号点} ✓$$

---

## §4 **三条链拼接（你的图，逐项对位）**

$$\text{①}\ \sup_{\mathcal A_{\rm var}}c_{\rm Fun}=c^{*}_\lambda\qquad（\text{\S3：V309 严格凸 ＋ V307 E–L}）✓$$
$$\text{②}\ v^{*}_\lambda\in\mathcal A_{\rm ThmD}\qquad（\text{P1-YES：源码注释逐字"the optimal window profile"；}\texttt{AdmWindow}\ \text{实例在}\ \texttt{BridgeD.lean:32}\ \text{库内已证}）✓$$
$$\text{③}\ \mathcal A_{\rm ThmD}\subseteq\mathcal A_{\rm var}\qquad（\text{V310：}\mathcal A_{\rm var}\ \text{更宽}）✓$$
$$\Longrightarrow \boxed{\sup_{\mathcal A_{\rm ThmD}}c_{\rm Fun}\ \le\ \sup_{\mathcal A_{\rm var}}c_{\rm Fun}=c^{*}_\lambda\ \ \wedge\ \ \sup_{\mathcal A_{\rm ThmD}}\ \ge\ c_{\rm Fun}(v^{*}_\lambda)=c^{*}_\lambda\ \Longrightarrow\ \sup_{\mathcal A_{\rm ThmD}}=c^{*}_\lambda} ✓✓✓$$
$$\qquad ⚠️\ \text{域限}：\lambda\le1\ \text{（V309 的界用}\ \lambda\le1）;\ \text{源码侧}\ \texttt{P.lam}<1 ⟹ \textbf{P3}\ \text{待办} ✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V313 判词}：\text{(A)}\ ✓\ \text{库内};\ \textbf{(E)}\ ✗\ \text{库内缺失（Theorem D 最优性＝外部引用）};\ \text{但 (E) 可由 V309＋V307 补出};\ \text{等式情形}\ =\ \{t\,v_\star\};\ \textbf{窄墙（模 P2／P3）闭合}} ✓✓✓$$

```
① ⚠️ §1 的"无最优性定理"结论基于 `grep "theorem|lemma|/--"` 的清单与 130–215 行的空结果 ⟹ **有可能遗漏**（同名/异形定理）⟹ 标**待复核** ⚠️✓
② ⚠️ §3 的 (E) 由**我们的** V307／V309 给出（纸面证明），**未入 Lean** ⟹ 0.67250 是"链内已证（模形式化）" ✓
③ ⚠️ §4 的域限 $\lambda\le1$（vs 源码 $\texttt{P.lam}<1$）未调和 ⟹ **P3 必须做** ✓
④ **不声称** 库内已有 (E)；**不声称** 0.67250 已是 Lean theorem ✓
⑤ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐⭐ **(A) ✓ 库内 / (E) ✗ 库内**：最优性归因于论文 `[thm:D]`"Montgomery–Taylor optimal"（`Final.lean:7`）；MT 窗极限在 `AssemblyD.lean:27` ✓✓✓
② ⭐⭐⭐⭐⭐ **(E) 由我们补**：V309 严格凸 ⟹ $\min\{Q:\int v=1\}$ 唯一全局 ⟹ $$\sup c_{\rm Fun}=\frac\lambda\kappa=c^{*}_\lambda$$ ✓✓✓
③ ⭐⭐⭐ **等式情形 ＝ 射线 $\{t\,v_\star\}$**（尺度不变性 ⟹ 无遗漏比例自由度）✓✓（你的第③项）
④ ⭐⭐⭐ **窄墙闭合**：$$\sup_{\mathcal A_{\rm ThmD}}c_{\rm Fun}=c^{*}_\lambda$$（模 P2／P3 ＋ V309 形式化）✓✓
⑤ ⭐ **无需两 admissible class 相等** —— 你的判断被完整证实 ✓✓
【下一步（按你既定序）】
  **P2**：`BridgeD:86` 的 $\tfrac12\le bv(\texttt{phiD})$（库内是否已成定理）
  **P3**：调和 $\lambda<1$（源码）与 $\lambda\le1$（V309）⟹ 定 $"ceiling"$ 陈述的正确域
  附：若求 Lean 级闭合 ⟹ 把 V307／V309 的推理**形式化**（凸性界 ＋ E–L 闭式）✓
