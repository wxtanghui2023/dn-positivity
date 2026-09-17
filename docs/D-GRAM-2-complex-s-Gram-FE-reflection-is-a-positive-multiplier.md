# ⚔️ **D-GRAM-2 四刀审计**：复-$s$ Gram 的 $\Re s$-敏感 ✓、HS 整数能量 ✓ —— **但 FE 反射是"正乘子"而非符号** ⟹ (1,1) 仍拿不到

> 依唐先生 13:54：第三型＝复 $s$ 的 Dirichlet Gram；三项审计 $\;v_{1-\bar\rho}=J_xv_\rho\;$、$\;\tilde G=A^*J_xA\;$、$\;\|\tilde G\|^2_{HS}\ll\sum|A(mn)|^2|B(n/m)|^2$ ✓
> **本档结果**：③**成立** ✓✓（HS 侧第二类型确实存在）；②之后**仍 PSD** ✗✗；⟹ **(A)⊥(B) 被加强（非击穿）**，新墙正名 **GRAM-INDEFINITENESS** ✓✓✓

---

## §1 设定（逐字采纳唐先生）
$$\phi_n(\sigma,t)=n^{-\sigma-it},\qquad x=\sigma-\tfrac12,\qquad \Omega\subset\mathbb C,\qquad G_{mn}=\iint_\Omega w(\sigma,t)m^{-\sigma-it}n^{-\sigma+it}d\sigma dt✓$$
$$\qquad G_{mn}=\iint_\Omega w(\sigma,t)\,(mn)^{-\sigma}\Big(\frac nm\Big)^{it}d\sigma dt✓\qquad(\textbf{唐先生：}\ (mn)^{-\sigma}\ \text{出现}\Longrightarrow\Re s\text{-敏感})✓$$

## §2 反射与奇偶通道（逐字确认 ✓）
$$s\mapsto1-\bar s \iff (\sigma,t)\mapsto(1-\sigma,t) \iff \boxed{x\mapsto-x}✓\qquad \phi_n^\pm=\tfrac12\big(n^{-1/2-x-it}\pm n^{-1/2+x-it}\big)✓$$
$$\phi_n^+(0,t)=n^{-1/2-it},\quad \phi_n^-(0,t)=0✓\qquad \phi_n^\pm(-x,t)=\pm\phi_n^\pm(x,t)✓$$

## §3 ⭐⭐⭐ **决定性计算**：$J_x$ 在 monomial 基上是**正乘子**（不是符号）
$$\big(J_x\phi_n\big)(x,t):=\phi_n(-x,t)=n^{-1/2+x-it}=\boxed{n^{2x}\,\phi_n(x,t)},\qquad n^{2x}>0\ \ \forall n,x✓✓✓$$
$$\Longrightarrow J_x\ \text{在 monomial 基上}\ \textbf{对角、元素全正}；\ \text{等价地}：\text{反射把}\ n\mapsto1/n\ (\textbf{基对称})✓✓$$
$$\Longrightarrow \text{插入}\ J_x\ \text{只把权换为}\ w(1-\sigma,t)\ (\textbf{权修改})，\ \textbf{不引入符号}✓✓✓$$

## §4 三刀结果
$$\textbf{(I)}\ \Re s\text{-敏感}：\ \checkmark✓\qquad \textbf{(III)}\ \textbf{第三式成立}：\checkmark✓✓$$
$$\qquad \tilde G_{mn}=n^{-1}H\!\big(\log\tfrac mn\big),\qquad H(\zeta)=\iint_\Omega w(\sigma,t)e^{-\zeta(\sigma+it)}d\sigma dt \Longrightarrow \textbf{纯整数核}✓✓\ (\text{HS 在整数能量层})✓✓$$
$$\textbf{(V)}\ (1,1)\ \textbf{signature}：\ \boxed{\times}✗✗$$
$$\qquad a^*\tilde Ga=\iint_\Omega w(1-\sigma,t)\Big|\sum_n a_nn^{-\sigma-it}\Big|^2d\sigma dt\ \ge0 \Longrightarrow \boxed{\tilde G\succeq0}✓✓✓$$
$$\qquad(\text{因}\ J_x\ \text{只改权}\Rightarrow \text{仍是}\ \textbf{正测度 Gram}\Rightarrow \textbf{恒 PSD})✓✓$$

## §5 ⭐⭐⭐ 因此 **(A)⊥(B) 被加强，而不是被击穿**
$$\text{根因}\ \textbf{不是}\text{"实}\ t\ \text{单模"}，\ \text{而是}\ \boxed{\text{任何}\ \textbf{正测度 Gram}\ \Longrightarrow\ PSD}\ \（\text{任意}\ s\text{-区域、任意窗、任意反射}）✓✓✓$$
$$\Longrightarrow \boxed{\Re s\text{-敏感性}\ \textbf{与 signature 无关}}✓✓\qquad(\text{唐先生的第三型在 (V) 处失效，而 (I)(III) 成立})✓✓$$
$$\Longrightarrow \text{前档互斥定理的}\ \textbf{适用范围从"实}\ t\ \text{单模"扩到"一切正测度 Gram"}✓✓✓$$

## §6 ⭐⭐⭐ 由此得到正确的墙名
$$\boxed{(1,1)\ \text{块}\ \textbf{不是 Gram 性质}，\ \text{而是}\ \textbf{Weil 型（显式公式）性质}}✓✓✓$$
$$\qquad 📌\ \text{前沿的}\ \tilde G\ \textbf{不是 PSD}：\text{它是 Weil 型的有限压缩，}\text{其不定性来自显式公式}（\text{值面}）✓✓$$
$$\Longrightarrow \text{正确命名}：\boxed{\textbf{GRAM-INDEFINITENESS BARRIER}}\quad(\text{而}\ \textbf{不是}\ \text{"zero-evaluation embedding"})✓✓✓$$
$$\qquad ⭐\ \text{副产品}：\text{唐先生猜的 "zero-evaluation embedding"}\ \textbf{不需要} —— \text{失败在}\ \textbf{更早} \text{处（Gram 本身恒 PSD）}✓✓$$

## §7 保留资产
$$\text{①}\ \textbf{复-}s\ \text{Gram 的 HS ＝ 整数能量}：\tilde G_{mn}=n^{-1}H(\log\tfrac mn)\ \text{是}\ \textbf{第二种非-素侧 HS 实现}（\text{与 D-GRAM-1 的实-}t\ \text{版并列}）✓✓$$
$$\text{②}\ \textbf{加强的定理}：\text{正测度 Gram}\Rightarrow PSD\Rightarrow\text{无}\ (1,1)\（\text{范围全覆盖}）✓✓✓$$
$$\text{③}\ \textbf{新墙名}：\boxed{\textbf{GRAM-INDEFINITENESS}}✓✓$$
$$\text{④}\ \text{负面副产品}：\Re s\text{-敏感性}\ \textbf{不能} \text{救 signature}✓✓$$

## §8 边界
$$\text{(i)}\ §2\ \text{逐字采纳唐先生；}\ §3\ \text{的关键代数恒等式}\ J_x\phi_n=n^{2x}\phi_n\ \text{为}\ \textbf{逐行可核}✓✓$$
$$\text{(ii)}\ §4\ \text{的}\ \tilde G\ \text{核形式（}n^{-1}H(\log\tfrac mn)\text{）为本档推导}✓\quad\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零计算}✓$$
$$\text{(iv)}\ ⚠️\ \text{本档}\ \textbf{不} \text{声称"一切 Hermitian 型皆 PSD"（}\text{仅"正测度 Gram"}）✓$$
