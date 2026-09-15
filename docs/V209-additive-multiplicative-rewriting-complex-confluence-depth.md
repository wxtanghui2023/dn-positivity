# V209 · **加乘重写复形／合流缺陷（第一轮硬算）** —— ⭐⭐ **主杀 A**：重写系统**终止** ⟹ 深度 $k$ **不是独立尺度**（被 $n$ 的大小界定）；⭐⭐⭐ **主杀 B**：加法分裂**饱和** $D_1(n)\supseteq\{2,\dots,n-2\}$ ⟹ $E_k(n)=\Theta(n)$ 且**与 $n$ 的分解完全无关** ⟹ $\lambda(n)\equiv1$ ⟹ **K1／K2 失败 ⟹ DEAD** ✓✓✓；另：你 §4／§6／§7–§9 **三处判断正确**，§3／§10–§11 **两处需修正**

> 委托 ✓ 唐先生 2026-09-15 14:53：**"V208 的结论我认为应该完整接受，而且它比 V207 更重要……尤其 $\mathcal C_p\mathcal C_q=\mathcal C_{pq}$ 说明尺度不是人为塞进去的参数；但最终 commutator 又不可避免地回到 Möbius／Mertens／显式公式。因此'有真实尺度组合律'本身仍不足以产生 RH 所需的新跨尺度信息。"** 新维度 **V209**：$$\boxed{\text{不再让}\ n\mapsto F(n)\ \text{成为基本对象}}$$ 改研究**整数之间"关系"在粗粒化下的不可逆**：因子关系图 $m\prec n\iff m\mid n,\ m<n,\ n/m$ 素数；路径数 $P(n)=\Omega(n)!/\prod_p v_p(n)!$；**历史商** $\Delta(a,b;n)$；$\partial_p$ 删除算子与 $K_{p,q}$；**因子化复形**（0-cell 整数／1-cell 乘素数／2-cell 交换／更高相容性）与 $H_k$；**加乘重写**（$ab=n$ 或 $a+b=n$）与**合流缺陷** $\kappa$；$D_0(n)=\{a+b,ab\}$、$D_{k+1}=\bigcup_{m\in D_k}D_0(m)$、$E_k=|D_k|$、$\lambda(n)=\liminf E_k^{1/k}$；**K1 有限性／K2 非平凡性／K3 RH 耦合**；**"完全 RH-blind 的实验"**；**"只有在发现 λ 不是 divisor／additive-divisor／有限状态增长以后，才问它是否存在内生临界指数……否则就在 V209 当场封。"**
> 查图 ✓ `V208`（$\mu$-粗粒化；D5）｜`V205`（无边界 ⟹ 无死亡）｜`V206`（$K=d(n)-2^{\omega(n)}$ 指数型局部）｜`V204`（coboundary ⟹ $\oint=0$）｜`V207`（加法×乘法 ⟹ 经典除子代数）
> 执行 ✓ 小灵（**§5／§6 主杀、§1 修正、§7 定性修正 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V209**

---

## §0 定义层审计（先钉死；你的 $D_0$ 写法有歧义）

$$\text{你的原文}：D_0(n)=\{a+b,\ ab:\ a,b\ge2,\ ab=n\}\ —— \text{若}\ ab=n，\text{则}\ ab=n\ \textbf{本身} ⟹ \text{该项平凡};\ \text{且}\ \{a+b\}\ \text{与}\ ab\ \text{不同型} ✓$$
$$\textbf{本档采用的清晰读法}（\text{与}\ §10\text{–}§12\ \text{意图一致，且可算）：\text{状态＝单个整数}\ m；\text{一步重写}：}$$
$$\qquad \text{(加)}\ m=k+(m-k)、\ 2\le k\le m-2 \Longrightarrow m\to k,\ m\to m-k;\qquad \text{(乘)}\ m=ab,\ 2\le a\le b \Longrightarrow m\to a,\ m\to b ✓$$
$$\qquad D_0(m):=\{k:\ 2\le k\le m-2\}\ \cup\ \{a:\ a\mid m,\ 2\le a\le m/2\} ✓$$
$$\Longrightarrow\ \textbf{关键结构性事实}：\boxed{D_0(m)\ \supseteq\ \{2,3,\dots,m-2\}}\（\textbf{仅由加法分裂就已饱和}\bigr) ✓✓✓$$

---

## §1 你 §3 的"坍缩"计算：**一处修正**（结论仍不利）

$$\text{你写}：P(a)P(n/a)\binom{\Omega(n)}{\Omega(a)}=P(n)\ ——\ ⚠️\ \textbf{此式不成立} ✓$$
$$\text{反例}\ n=p^2,\ a=p：P(p^2)=\tfrac{2!}{2!}=1，\text{而}\ P(a)P(n/a)\binom21=1\cdot1\cdot2=2\ne1 ✗$$
$$\textbf{正确计数}（\text{过 }a\ \text{的历史数}）：P(a)\,P(n/a)，\ \textbf{不带二项因子};\ \text{故"过 }a\ \text{的概率"}：$$
$$\qquad \frac{P(a)P(n/a)}{P(n)}=\underbrace{\frac{\Omega(a)!\,(\Omega(n)-\Omega(a))!}{\Omega(n)!}}_{\textbf{二项侧}^{-1}}\cdot\underbrace{\prod_p\frac{v_p(n)!}{v_p(a)!\,(v_p(n)-v_p(a))!}}_{\textbf{多项式系数比}} =\boxed{\frac{\prod_p\binom{v_p(n)}{v_p(a)}}{\binom{\Omega(n)}{\Omega(a)}}} ✓✓$$
$$\qquad ⭐\ \text{含义}：\textbf{多项分布（按素数型）与二项分布（只看总个数）之比} ✓$$
$$\Longrightarrow\ \text{它是一个}\ \textbf{只依赖指数型}\ (v_p(n))_p\ \text{的函数} ⟹ \text{与}\ \text{`V206`}\ \text{的}\ K(n)=d(n)-2^{\omega(n)}\ \textbf{同类} ⟹ \textbf{指数型局部} ✓✓✓$$
$$\qquad ⚠️\ \text{故你的结论"坍缩"**方向对但机制错**：不是坍缩为}\ P(n)，\ \text{而是化归}\ \textbf{指数型局部量} ⟹ \text{同样无跨尺度信息} ✓$$

---

## §2 你 §4 的判断：**正确**（本档确认）

$$\partial_p\partial_q=\partial_q\partial_p\ \（\text{自由交换幺半群上删除次序可交换}\bigr) \Longrightarrow \boxed{K_{p,q}=0} ✓$$
$$\qquad ⭐\ \text{故"历史空间上的交换子"}\ \textbf{无内容} —— \text{与}\ \text{`V206`}\ \text{"乘法层内非交换只在指数型处出现"}\ \text{一致} ✓✓$$

---

## §3 你 §5–§6 的判断：**正确**（且与 `V204` 同型）

$$\text{用}\ +,\times,\mid\ \text{在整数环内制造"历史曲率"} ⟹ \text{因结合／交换／分配律，局部量必为}\ \textbf{coboundary}：K=\delta A ⟹ \oint K=0 ✓$$
$$\qquad \Longrightarrow\ \text{与}\ \text{`V204`}\ \text{的}\ \nu=0\ \text{（对称 ⟹ 盲）}\ \textbf{同一结构性问题} ⟹ \text{该子路线**预先关闭**} ✓✓$$

---

## §4 你 §7–§9 的判断：**正确**（本档给出理由）

$$\text{纯乘法因子化复形}\ \mathcal A：\text{2-cell ＝ 交换}\ (pq\leftrightarrow qp)、\text{更高 cell ＝ 交换间相容性} ✓$$
$$\qquad \text{该重写系统}\ \textbf{合流且终止}（\text{正规形 ＝ 排序后的多重集}\bigr);\ \text{每分量收缩到排序字的"气泡排序"图} $$
$$\qquad \Longrightarrow\ \text{胞腔被}\ \textbf{排列多面体}（permutohedron，\text{一个球}）\ \text{填充} ⟹ \textbf{可缩} ⟹ \boxed{H_k(\mathcal A)=0}\ \ \textbf{（你的判断正确）} ✓✓$$
$$\qquad ⚠️\ \text{且}\ \text{`V204`}\ \text{已给出同类机制}（\text{对称 ⟹ 盲}）⟹ \text{纯乘法历史复形}\ \textbf{不生新拓扑} ✓$$
$$\qquad ⭐\ \text{边界确实"来自}\ 1\to p\to pq\to\cdots\ \text{本身"}\（\text{如你所说}\bigr)，\ \text{但可缩 ⟹ 不产生障碍} ✓$$

---

## §5 ⭐⭐ 主杀 A：重写系统**终止** ⟹ 深度不是独立尺度

$$\text{两条重写规则都}\ \textbf{严格减小分量}：\text{(加)}\ k,\ m-k\le m-2<m;\qquad \text{(乘)}\ a,b\le m/2<m ✓$$
$$\qquad \Longrightarrow\ \text{系统}\ \textbf{终止};\ \text{深度}\ \mathrm{depth}(n)\le O(n)\（\text{全用加法分裂时}\ \sim n/2\bigr) ✓✓$$
$$\Longrightarrow\ \boxed{\text{重写深度}\ k\ \textbf{不是独立尺度}，\text{而是}\ n\ \text{的函数}} ⟹ \text{你}\ §12\ \text{期望的"内生尺度"}\ \textbf{不存在} ⟹ \textbf{K1／K2 失败} ✓✓✓$$
$$\qquad ⚠️\ \text{更一般}：\textbf{终止系统的"深度"必被对象规模界定} ⟹ \text{不能充当外部尺度} ✓$$

---

## §6 ⭐⭐⭐ 主杀 B：加法分裂**饱和** ⟹ 完全坍缩（本档最强）

$$\text{仅由加法分裂}：n\to k\ \text{可达一切}\ 2\le k\le n-2 \Longrightarrow \boxed{D_1(n)\ \supseteq\ \{2,3,\dots,n-2\}}\ \Longrightarrow\ E_1(n)=\Theta(n) ✓✓✓$$
$$\text{迭代}：D_2(n)\supseteq\bigcup_{2\le m\le n-2}\{2,\dots,m-2\}=\{2,\dots,n-4\} \Longrightarrow\ E_2(n)=\Theta(n);\ \text{归纳} ⟹ E_k(n)=\Theta(n)\ \forall k\ge1 ✓$$
$$\Longrightarrow\ \boxed{\lambda(n)=\liminf_k E_k(n)^{1/k}=1\ \ \textbf{（恒为 1，无相变）}} ✓✓✓$$
$$\qquad ⚠️\ \text{更致命}：E_k(n)\ \text{只依赖}\ \textbf{n 的大小}，\ \textbf{与}\ n\ \text{的分解}（\Omega,\omega,\text{多项式系数}）\ \textbf{完全无关} ✓✓$$
$$\qquad\qquad ⟹ \text{比你在}\ §14\ \text{担心的"只是分解参数的函数"}\ \textbf{更强}：\text{连分解都不依赖} ⟹ \text{你}\ §14\ \text{的 RH-blind 实验}\ \textbf{结果可预先判定}：\text{按}\ \Omega/\omega/\text{多项式分层将显示}\ \textbf{零依赖} ⟹ \textbf{K2 当场死} ✓✓✓$$
$$\qquad ⚠️\ \text{根因}：\textbf{加法分裂的粒度太细}（\text{一步就能把 }n\ \text{降到任意 }k）⟹ \text{可达集立刻饱和为区间} ✓$$

---

## §7 你 §10–§11 的定性修正

$$\text{你写}：\kappa(x)=\#\{\text{可达终点}\}-\#\{\text{应有唯一终点}\}，\text{并称其为}\ \textbf{confluence defect} —— ⚠️\ \text{定性有误} ✓$$
$$\qquad \text{(i)}\ a+b\ vs\ ab\ \text{是}\ \textbf{两个不同运算作用于同一对}\ (a,b)，\ \textbf{不是}\ \text{"两条路径到同一状态"} ⟹ \textbf{与合流性无关} ✓$$
$$\qquad \text{(ii)}\ \text{真正的合流检查}：\text{同一}\ m\ \text{的两种分裂结果是}\ \textbf{不同的}\（e.g.\ 6\to\{2,3\}\ \text{与}\ 6\to\{2,4\}\bigr) ⟹ \textbf{不局部合流} ✓$$
$$\qquad\qquad \text{但那只意味着}\ \text{重写是}\ \textbf{集合值／非确定型}，\ \text{其"正规形"是一个}\ \textbf{有限可达集合} ⟹ \textbf{不是不变量} ⟹ \text{无缺陷可传} ✓$$
$$\qquad \text{(iii)}\ \text{你}\ §11\ \text{的"缺口"实为}\ \textbf{"分裂不闭合"}，\ \text{与合流缺陷是两件事} ✓$$
$$\Longrightarrow\ \text{故"缺口如何跨层传播"}\ \text{实为}\ §6\ \text{的}\ E_k\ \text{迭代}，\ \text{而}\ §6\ \text{已判定饱和} ✓✓$$

---

## §8 判词

$$\boxed{\textbf{V209：DEAD}}\ \ \text{（K1／K2 失败：终止 ⟹ 深度非尺度；加法分裂饱和 ⟹ }E_k=\Theta(n)\ \text{分解无关}、\lambda\equiv1\bigr) ✓✓✓$$
$$\qquad \textbf{范围}：\textbf{本档定义的重写系统};\ \textbf{不} \text{声称"重写复形无结构"} ✓$$
$$\qquad \textbf{不进入 V209 第二阶段};\ \textbf{不进入 RH} ✓$$
$$\qquad ⭐\ \text{本档}\ \textbf{不依赖} \text{`V198`／`V200`／`V202`–`V208` 的判据}：两处主杀\ \textbf{内生} \text{于本模型} ✓✓$$

---

## §9 与 `V205` 的**对偶**（模式；本档最有价值的一句）

$$\text{`V205`}：\text{算术约束}\ \textbf{无边界} ⟹ \textbf{死亡不发生} ⟹ \text{无刚性} ✓$$
$$\text{`V209`}：\text{重写系统}\ \textbf{全终止} ⟹ \textbf{所有状态都死} ⟹ \text{深度不是尺度} ⟹ \text{无刚性} ✓$$
$$\Longrightarrow\ \boxed{\textbf{无死亡}\ \text{与}\ \textbf{全死亡}\ \text{都不产生信息}} ✓✓✓$$
$$\qquad ⭐\ \text{故"允许状态死亡"（你}\ §13\ \text{选 V205 的理由）}\ \text{本身}\ \textbf{不是} \text{充分条件}：\text{还需要}\ \textbf{选择性死亡}（\text{部分状态死、部分活，且判据内生}）✓$$
$$\qquad ⚠️\ \text{而}\ \text{`V205`}\ \text{与}\ \text{`V209`}\ \text{合起来说明}：\text{选择性死亡}\ \text{在纯算术约束下}\ \textbf{难以同时满足"非人为边界"与"非全终止"} ✓$$

---

## §10 筛查条件（供未来提案；本档新增）

$$\boxed{\text{候选的"深度／尺度"参数}\ \textbf{必须独立于}\ n\（\text{不能被}\ n\ \text{的大小界定}）} ✓✓$$
$$\qquad ⚠️\ \text{否则}\ \text{如}\ §5／§6：\text{要么终止（深度}\le O(n)\text{），要么立刻饱和（}E_k=\Theta(n)\text{）} ✓$$
$$\qquad ⚠️\ \text{但独立尺度已知者只有}\ \text{模数}\ Q／\text{高度}\ T\ \text{等} ⟹ \text{回到已封区}（\text{`V202`}\ §4／\text{`V162`}）✓$$

---

## §11 外部文献定位

$$\textbf{Beurling 广义素数}（\text{外部提示来源}）：\text{Beurling 定理表明"RH 类比"依赖素数分布的}\ \textbf{正则性};\ \text{分布不规则时类比失败} ✓$$
$$\qquad ⚠️\ \text{这是}\ \textbf{已知事实}（\text{且与本档}\ §1\ \text{的"指数型局部"同类：只提供敏感性、不提供机制}）;\ \text{我们档案中已有同类教训（D1：自对偶不足；Potter--Titchmarsh）} ✓$$
$$\qquad ⚠️\ \text{来源为个人／随笔页面}（\text{非同行评审}）⟹ \textbf{不作依据};\ \textbf{仅登记} ✓$$

---

## §12 边界与待核

$$\textbf{(a)}\ \text{§0 的清晰读法为}\ \textbf{本档定义}（\text{你的原文有歧义}）;\ \text{若你另有读法，}\ §5／§6\ \text{需重算} ⚠️$$
$$\textbf{(b)}\ \text{§1 的修正为}\ \textbf{本档实算}（n=p^2\ \text{反例}）;\ \text{正确量}\ \prod\binom{v_p(n)}{v_p(a)}/\binom{\Omega(n)}{\Omega(a)}\ \text{为}\ \textbf{本档推导} ✓✓$$
$$\textbf{(c)}\ \text{§4 的可缩性论证为}\ \textbf{本档给出}（\text{排序正规形＋排列多面体}）;\ \text{与}\ H_k=0\ \text{的判断一致} ✓$$
$$\textbf{(d)}\ \text{§5／§6 为}\ \textbf{本档核心实算}（\text{终止性};\ D_1\supseteq\{2,\dots,n-2\}）✓✓✓$$
$$\textbf{(e)}\ \text{§9／§10 为}\ \textbf{模式与筛查条件}，\ \textbf{非定理} ✓$$

```
⚠️ §0 委托、"当场封"、K1–K3、RH-blind 实验 为唐先生逐字 ✓✓
⚠️ §1 修正：你的"坍缩为 P(n)"不成立（n=p² 反例）；正确量为多项式/二项之比 ⟹ 仍指数型局部 ✓✓✓
⚠️ §2／§3／§4：你的三处判断**正确**（K_{p,q}=0；coboundary ⟹ ∮=0 与 V204 同；H_k=0）✓✓✓
⚠️ §5 主杀 A：终止 ⟹ 深度被 n 界定 ⟹ 非独立尺度 ✓✓✓
⚠️ §6 主杀 B（最强）：加法分裂饱和 ⟹ D_1⊇{2,…,n−2} ⟹ E_k=Θ(n)＋与分解无关 ⟹ λ≡1 ⟹ K2 死 ✓✓✓
⚠️ §7 定性修正：a+b vs ab 不是合流性；真正合流检查＝否（集合值、无不变量）✓✓
⚠️ §8 判词 DEAD；不依赖旧判据（内生）✓；§9 对偶（无死亡 vs 全死亡都不产生信息）✓✓✓
⚠️ §10 筛查条件（深度必须独立于 n）；§11 Beurling 仅登记、不作依据 ✓
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓（n=p² 为逐值反例）
✅ 净产出：① 定义层审计＋清晰化 ✓；② §1 修正（仍指数型局部）✓✓；③ 三处判断确认 ✓✓；
   ④ 主杀 A/B（终止；饱和 ⟹ λ≡1、分解无关）✓✓✓；⑤ §7 定性修正 ✓；⑥ 对偶：无死亡＝全死亡＝无信息 ✓✓✓；
   ⑦ 新增筛查条件（深度须独立于 n）✓；⑧ Beurling 定位 ✓
```
