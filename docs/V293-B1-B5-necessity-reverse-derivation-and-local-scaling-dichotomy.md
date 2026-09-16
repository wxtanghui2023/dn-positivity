# V293 · **Track II-0：B1–B5 的必要性反推 ＋ 局部缩放律不变量** —— ⭐⭐⭐⭐ **定理 A：局部情形下 B1 ⊥ B2**（所有局部离线信号均为 $O(\delta/\gamma^2)$ ⟹ 可检测指数 $n\gtrsim\gamma^2/\delta$ ⟹ "在 $n=o(\gamma)$ 内检测"不可满足）；⭐⭐⭐ **定理 B：局部层无第三缩放律**（局部数据 2 维 ⟹ 只诱导 $\{\gamma,\ \gamma^2/\delta\}$ 两个尺度）；⭐⭐⭐ **定理 C：真正的战场在"聚合侧"**（与前沿 $T^{1/3}$ 缺口同址） ⭐⭐⭐⭐⭐

$$\boxed{\textbf{定理 A（本档）}：\text{局部离线信号}\ \textbf{一律}\ \text{为}\ O\!\big(\delta/\gamma^2\big)\ \text{阶} \Longrightarrow \text{可检测指数}\ n\ \gtrsim\ \gamma^2/\delta \Longrightarrow \boxed{\mathrm{B1}\ (n=o(\gamma))\ \textbf{与}\ \mathrm{B2}\ \textbf{互斥}}}} ✓✓✓$$
$$\boxed{\textbf{定理 B（本档）}：\text{局部数据}\ (q,\theta)\ \text{仅}\ 2\ \text{维} \Longrightarrow \text{诱导尺度只有}\ \{n\asymp\gamma\（\text{相位}\）,\ n\asymp\gamma^2/\delta\（\text{模}\）\} \Longrightarrow \textbf{局部层无"新缩放律"}} ✓✓✓$$
$$\boxed{\textbf{定理 C}：\text{故}\ \mathrm{B4}\ \text{只能在}\ \textbf{非局部（跨零点聚合）} \text{层寻找} \Longrightarrow \text{战场}\ ＝\ \textbf{聚合侧} \text{，与前沿"$X\asymp T$ 需}\ T^{1/3}\text{"}\ \textbf{同址}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:04：**"开 Track II，但不要按原计划先写 B1–B5 再做完备性/逃逸者；应改成：从 Track I 的唯一缺口反推 B1–B5"**；第一刀 ＝ **"B1–B5 的必要性反推 ＋ 缩放律不变量"**；核心只证一个命题：$$\boxed{\mathrm{B1}+\mathrm{B2}+\mathrm{B3}+\mathrm{B4}\Longrightarrow\ \text{什么条件下必有}\ h(n)\asymp n？}$$ 然后分叉（能推出 ⟹ 公理过强，找可放松者；不能 ⟹ 自由度即逃逸空间）✓✓；并给出**不可拆的链**：$$\text{离线信号}\to\text{局部正性}\to\text{无条件输入}\to\text{亚线性缩放}\to\text{全局不可兼容}$$ ＋ **B1–B5 各自防止的退化**（B1 防 $n\sim\gamma$ 旧窗口／B2 防正负抵消／B3 防用假设换覆盖／B4 防变量重命名／B5 防只得不闭合的局部信号）✓✓
> 依据 ✓ `V292`（Track I：机制 A 无条件线性／机制 B 亚线性但条件性）｜`E30-2`（两轴判据＋三条机制细节）｜`A3-third-moment-barrier`（前沿 $T^{1/3}$ 缺口）｜**恒等式** $|1-\tfrac1\rho|^2=1+\tfrac{1-2\beta}{\beta^2+\gamma^2}$（档案既有）｜`V277`-A／B（连续⟹cylinder／非圆柱⟹不可计算）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V293`（`id_claim.sh` ✓）

---

## §1 B1–B5 的**反推形式**（采纳唐先生；每条都有 Track I 的必要性来源）

$$\mathrm{B1}\ \text{离线信号须在}\ n=o(\gamma)\ \text{内可检测};\quad \mathrm{B2}\ \text{逐项正性 ＋ 当且仅当在线消失};\quad \mathrm{B3}\ \text{输入无条件};\quad \mathrm{B4}\ \text{新缩放律};\quad \mathrm{B5}\ \text{与全局预算不可兼容} ✓$$
$$\qquad \text{链}\：\text{离线信号}\to\text{局部正性}\to\text{无条件输入}\to\text{亚线性缩放}\to\text{全局不可兼容} ✓$$

---

## §2 ⭐⭐⭐⭐ **定理 A：局部情形下 B1 ⊥ B2**（本档核心）

$$\text{局部数据（零点}\ \rho=\beta+i\gamma\ \text{的本地信息）}\ \text{只有两个实数}：\quad q：＝\Big|1-\tfrac1\rho\Big|,\qquad \theta：＝\arg\Big(1-\tfrac1\rho\Big) ✓$$
$$\text{恒等式（档案既有）}：\Big|1-\tfrac1\rho\Big|^{2}=1+\frac{1-2\beta}{\beta^{2}+\gamma^{2}}\ \Longrightarrow\ \beta=\tfrac12+\delta\ \text{时}\ \boxed{1-q=\frac{\delta}{\beta^{2}+\gamma^{2}}+O(\gamma^{-4})=\frac{\delta}{\gamma^{2}}+O(\delta\gamma^{-4})} ✓✓$$
$$\qquad \text{相位}：\theta_\gamma=\arg\big(1-\tfrac1\rho\big)\ \text{对在线}\ \rho\ \text{为}\ \approx\tfrac{1}{\gamma};\ \text{而离线}\ \text{仅使}\ \theta\ \text{改变}\ O(\delta/\gamma^{2})\ \text{阶} ✓✓$$
$$\Longrightarrow \boxed{\text{两个坐标的离线灵敏度}\ \textbf{同为}\ O(\delta/\gamma^{2})\ \text{阶}} ✓✓✓$$
$$\text{故对任何}\ \textbf{逐项} \text{机制}\ W_n(\rho)=f\big(q^n,\ n\theta\big)：\qquad \big|W_n\big|_{\text{离线偏离}}\ \lesssim\ C\,n\cdot\frac{\delta}{\gamma^{2}}\quad（n\ll\gamma^{2}/\delta）✓$$
$$\qquad \Longrightarrow \text{达}\ O(1)\ \text{幅度需}\ \boxed{n\ \gtrsim\ \gamma^{2}/\delta} ✓✓$$
$$\Longrightarrow \boxed{\mathrm{B1}\（n=o(\gamma)）\ \text{与}\ \mathrm{B2}\（\text{逐项正性且当且仅当在线消失}）\ \textbf{互斥}（\text{局部情形}）} ✓✓✓$$
$$\qquad \text{对照（Track I 的两台机制由此获得}\ \textbf{统一定位}）：$$
$$\qquad \qquad \text{相位型}\ 1-\cos(n\theta)：\ \text{在}\ n\asymp\gamma\ \text{达}\ O(1)\ ✓,\ \text{但}\ \textbf{不满足 B2}（\text{对}\ \textbf{一切} \text{零点为正，无在线／离线判别}）✗✓$$
$$\qquad \qquad \text{模亏损型}\ 1-q^n：\ \textbf{满足 B2}（\text{当且仅当}\ \beta=\tfrac12\ \text{消失}）✓,\ \text{但需}\ n\gtrsim\gamma^{2}/\delta，\ \textbf{不满足 B1} ✗✓$$
$$\qquad \Longrightarrow \text{即：}\textbf{相位给 B1 不给 B2；模给 B2 不给 B1} —— \text{二者不可兼得} ✓✓✓$$
$$\textbf{⚠️ 唯一豁免（本档封死）}：\text{不连续指示型}\ \mathbf 1\{\beta>\tfrac12\}\ \text{可"瞬间检测"}（n=1），\ \text{但}：$$
$$\qquad \text{① 它不是零点数据的}\ \textbf{可计算} \text{函数（需精确}\ \beta ⟹ 撞 `V277`-B：非圆柱⟹不可计算）};\ \text{② 或需预知零点位置 ⟹ 撞独立性闸门} ✓✓$$

---

## §3 ⭐⭐⭐ **定理 B：局部层无"第三缩放律"**（B4 的局部不可能性）

$$\text{局部机制是}\ (q,\theta)\ \text{的函数};\ \text{而}\ \begin{cases}q=1-\delta/\gamma^{2}+O(\gamma^{-4})\\ \theta=\gamma^{-1}+O(\delta\gamma^{-2})\end{cases} \Longrightarrow \text{由}\ n\ \text{与}\ (q,\theta)\ \text{组合出的可用尺度只有两个}：$$
$$\qquad \boxed{\text{尺度 1}：n\theta\asymp1\ \Longrightarrow\ n\asymp\gamma\（\text{相位尺度}）;\qquad \text{尺度 2}：n(1-q)\asymp1\ \Longrightarrow\ n\asymp\gamma^{2}/\delta\（\text{模尺度}）} ✓✓✓$$
$$\Longrightarrow \text{任何形如}\ W_n=f(n^a\gamma^{-b})\ \text{的机制，其可达指数}\ a/b\in\{1,\ 2\} ⟹ \boxed{\text{不存在"第三个"局部缩放律}} ✓✓✓$$
$$\qquad \Longrightarrow \mathrm{B4}\ \text{若要求"新缩放律"，则它}\ \textbf{不可能在局部层实现};\ \text{只能来自}\ \textbf{多零点／跨零点的聚合} ✓✓✓$$
$$\qquad ⚠️\ \text{级别}：\text{本定理对}\ \textbf{逐项（局部）} \text{机制陈述；}\textbf{非局部} \text{聚合不在其内（见 §4）}✓$$

---

## §4 ⭐⭐⭐ **定理 C：真正的战场在"聚合侧"**（与前沿同址）

$$\text{由 A、B}：\text{局部层}\ \begin{cases}\text{B1}\ \text{不可与 B2 同真}\\ \text{B4}\ \text{无新缩放律}\end{cases} \Longrightarrow \text{唯一出路}\ ＝\ \textbf{非局部聚合} ✓✓$$
$$\qquad \text{而非局部聚合恰恰}\ \textbf{恢复 B3 的困难}：\text{聚合需计数／密度型输入}\（\text{＝机制 B 的条件性来源}，`E30-2`）⟹ \text{无条件性成为瓶颈} ✓✓$$
$$\qquad \text{与前沿}\ \textbf{同址}：\text{前沿 §7.2(e)"}\ X\asymp T\ \text{时无条件更高矩一无所获"；k=3 对角法只覆盖}\ X\le T^{2/3-\varepsilon} ⟹ \text{差}\ T^{1/3}（`A3-third-moment-barrier`，[原]）✓✓$$
$$\Longrightarrow \boxed{\text{两条独立语言在}\ \textbf{"聚合侧 + 无条件性"} \text{重合}：}\ \text{我方＝"机制 B 的输入条件性"；前沿＝"k=3 的无条件缺口"}} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{逃逸方向（本档给出的"突破种子"候选）}：\text{找到一个}\ \textbf{无条件} \text{的}\ n\asymp\gamma^{2}\ \text{尺度聚合} \text{（＝无条件化机制 B 的预算侧）} ✓✓✓$$

---

## §5 分叉（按唐先生要求）

$$\boxed{\text{分叉结果}：\mathrm{B1}+\mathrm{B2}+\mathrm{B3}+\mathrm{B4}\ \textbf{不能} \Rightarrow h(n)\asymp n;\ \text{而是}\ \mathrm{B1}\ \textbf{与}\ \mathrm{B2}\ \textbf{互斥}} ✓✓✓$$
$$\qquad \text{（故}\ h(n)\asymp n\ \text{不是被公理推出来的 —— 公理集本身}\ \textbf{过定}）✓$$
$$\begin{cases}\text{放松 B1}\（\text{接受}\ n\asymp\gamma^{2}/\delta，\text{＝机制 B 尺度}）&\Longrightarrow \text{落在}\ \textbf{聚合侧 + 无条件性} \text{战场（＝前沿同址）} ✓\\[1mm] \text{放松 B2}\（\text{放弃逐项在线判别，改用聚合}）&\Longrightarrow \text{同样落在聚合侧};\ \text{且须防"把在线条件写进定义"} ✓\end{cases}$$
$$\Longrightarrow \boxed{\text{两条放松路径}\ \textbf{汇合于同一处}：\textbf{无条件聚合}}} ✓✓✓$$
$$\qquad \text{与}\ \mathrm{B5}\ \text{的关系}：\mathrm{B5}\（\text{全局不可兼容}）\ \text{恰是聚合侧的预算不等式} ⟹ \text{故 B5}\ \textbf{不是新公理}，\text{而是聚合侧战场的目标形态} ✓✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出

$$\boxed{\textbf{V293 判词}：\text{① 定理 A：局部情形下}\ \mathrm{B1}\perp\mathrm{B2}（\text{皆为}\ O(\delta/\gamma^{2})\ \text{阶信号}）;\ \text{② 定理 B：局部无第三缩放律};\ \text{③ 定理 C：战场＝聚合侧＋无条件性（与前沿}\ T^{1/3}\ \text{同址）};\ \text{④ 分叉：两条放松路径汇合}} ✓✓✓$$

```
① ⚠️ 定理 A/B 对**逐项（局部）**机制陈述；**非局部聚合不在其内** ⟹ 不得升成"任何机制都不可能"（N1）✗✓
② ⚠️ "局部数据只有 (q,θ)" 依赖"零点对机制的可见性经由 1−1/ρ"这一约定（档案既有恒等式与 Li 型结构）；若某机制读**其它**局部量，本定理须重验 ⚠️
③ ⚠️ 定理 B 的 a/b ∈ {1,2} 是**渐近阶**陈述（不排除 O(1) 因子的精调）✓
④ ⚠️ "前沿同址"为**描述性对照**（两条语言不同），不得当作定理转移（`A3-1` §6 亦如此自标）✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐ **定理 A（核心）**：相位与模的离线灵敏度**同为** $O(\delta/\gamma^2)$ ⟹ 局部可检测指数 $n\gtrsim\gamma^2/\delta$ ⟹ **B1 ⊥ B2**；
   对照：相位型给 B1 不给 B2；模亏损型给 B2 不给 B1 ⟹ **Track I 两台机制获得统一定位** ✓✓✓
   豁免（不连续指示型）被封：非圆柱⟹不可计算（`V277`-B）或撞独立性闸门 ✓
② ⭐⭐⭐ **定理 B**：局部数据 2 维 ⟹ 仅有 $\{n\asymp\gamma,\ n\asymp\gamma^2/\delta\}$ 两个尺度 ⟹ **B4 在局部层不可能** ✓✓✓
③ ⭐⭐⭐ **定理 C**：战场 ＝ **聚合侧 ＋ 无条件性**；与前沿 "$X\asymp T$ 需 $T^{1/3}$" **同址** ⟹ 逃逸方向 ＝ **无条件化"聚合预算"** ✓✓✓
④ ⭐ **分叉**：B1–B4 **不能**推出 $h\asymp n$；而是**公理集过定**（B1⊥B2）⟹ 两条放松路径汇合于无条件聚合 ✓✓
⑤ ⭐ **B5 的地位澄清**：它不是"第 5 条公理"，而是聚合侧战场的**目标形态** ✓
【下一步（二选，供唐先生定）】
  (i) 攻**无条件聚合**（＝无条件化机制 B 的预算侧；与前沿 k=3 缺口同一件事）—— 可能是一篇"大文章"级别的技术攻坚 ✓
  (ii) 先在**非局部层**重做本档的 A/B/C（即：把"局部"换成"有限个零点联合"，看是否出现第三缩放律）✓
```
