# V2-33 第三刀 — **平方 $\ell_1$ 的真实结构** ⟹ 判定收窄为**二分（α 振荡被杀／β 纯计数）**

> 唐先生 2026-09-16 22:06「继续第三刀」✓
> 任务（REVIEW-V2H §4）：$\boxed{\text{直接写出平方后的真实相位}\to C_{\rm comb}^{\rm exact}\to\#\{C_{\rm comb}=0\}\to\text{与 Weil 支同账}}$✓

---

## 1. ⭐⭐⭐ C--S 对 $\ell_1$ 的**精确效果**（逐步）
$$\text{原式：}\ \sum_{\ell_1}\underbrace{g(\ell_1)}_{\text{含}\ \ell_1\ \text{的全部依赖}} \qquad\text{C--S：}\ \Bigl|\sum_{\ell_1}g(\ell_1)\Bigr|^2\ \le\ \Bigl(\sum_{\ell_1\asymp L}1\Bigr)\sum_{\ell_1}|g(\ell_1)|^2\ \approx\ L\sum_{\ell_1}|g(\ell_1)|^2✓$$
$$\Longrightarrow\ \Bigl|\sum_{\ell_1}g(\ell_1)\Bigr|\ \le\ \boxed{L^{1/2}\cdot\Bigl(\sum_{\ell_1}|g(\ell_1)|^2\Bigr)^{1/2}}✓✓$$
$$\textbf{关键}：\ \ell_1\ \text{在相位中}\ \textbf{仅经}\ \overline{\tilde\ell_1\tilde\ell_1'}\ \text{等模逆元出现}（\text{V2-31 已定}）\Longrightarrow |e(\phi(\ell_1))|=1✓$$
$$\text{但}\ \ell_1\ \text{另有}\ \textbf{条件依赖}：\ \mathfrak p_1,\mathfrak q_1|(\ell_1,\ell_1')、\text{互素、区间}\Longrightarrow \sum_{\ell_1}|g(\ell_1)|^2\ =\ \boxed{\#\{\text{admissible}\ \ell_1\}}✓✓$$
$$\Longrightarrow\ \boxed{\text{C--S over}\ \ell_1\ \text{＝把}\ \ell_1\ \text{的}\ \textbf{振荡} \text{换成}\ \textbf{计数}}✓✓✓\quad(\text{即：}L^{1/2}\times(\#)^{1/2})✓$$

## 2. ⭐⭐⭐ 由此得到的**精确二分**（第三刀的核心）
$$\boxed{\textbf{(α)}\ \text{若}\ \ell_1\ \text{-求和的全部内容}\ \textbf{是振荡} \Longrightarrow \text{C--S 将其}\ \textbf{杀死}（|g|=1\Rightarrow\text{返回平凡界}\ L）\Longrightarrow \textbf{更差}（\mathrm{DEAD}）}✓✓$$
$$\boxed{\textbf{(β)}\ \text{若}\ \ell_1\ \text{-求和的内容}\ \textbf{是计数}（\text{经整除／互素条件}）\Longrightarrow \text{C--S 只是把计数换个写法}\Longrightarrow \textbf{中性}（\mathrm A，\text{净收益}=0）}✓✓$$
$$\qquad\Longrightarrow\ \text{第三刀的判定}\ \textbf{＝}\ \text{在}\ \alpha/\beta\ \text{之间确定一个}✓✓$$

## 3. ⭐⭐⭐ 用 BC 自身用法定位（倾向 β）
$$\text{(4.14) 逐字（}\mathscr V^*\ \text{支）}：\ \text{计数}\ \boxed{\frac{L^2}{(\mathfrak p_1+\mathfrak q_1)(\mathfrak p_2+\mathfrak q_2)}}\ \Longrightarrow\ \textbf{BC 对}\ \ell\ \text{-求和}\ \textbf{用的是计数＋除因子}，\ \text{非其振荡}✓✓$$
$$\text{且 Weil 节省的来源}：\ \text{V2-28B 已定}\ \boxed{\text{Weil 施于}\ n_2'}\ \text{——}\ \textbf{不来自任何}\ \ell\ \text{-振荡}✓✓$$
$$\Longrightarrow\ \boxed{\text{在 BC 的账本里，}\ \ell\ \text{-求和的内容}\ \textbf{是}\ (β)\ \text{计数} \Longrightarrow \text{C--S over}\ \ell_1\ \textbf{中性}}✓✓$$
$$\qquad\Longrightarrow\ \textbf{倾向：}\ \mathrm A，\ \textbf{净收益}=0\ （\text{即"收益恰被新增成本抵消"那一行}）✓✓$$

## 4. ⚠️ 但 $C_{\rm comb}$ 的**精确形式**仍不能定（残余 1 未消）
$$\text{因}\ C--S\ \text{over}\ \ell_1\ \text{会使}\ |g|^2\ \text{中的}\ \textbf{其余变量成对出现}（\ell_1',\ell_2,\ell_2',d,d',a,c,n\ \text{各得共轭副本}）✓✓$$
$$\qquad\Longrightarrow\ \text{第二副本的}\ n_2''\ \textbf{与}\ n_2'\ \text{不共享} \Longrightarrow \text{合并式}\ e(C_{\rm comb}\overline{\mathfrak q_2n_2'})\ \textbf{不成立}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{V2-32 第二层的"合并"结论}\ \textbf{须修正}：\ \text{两份副本}\ \textbf{各带自己的一份变量}，\ \text{故}\ C_{\rm comb}\ \text{的精确形式}\ \textbf{尚未定}}✓✓$$
$$\qquad\textbf{但}：\ \text{按 §3 的}\ (β)\ \text{定位，}\ \ell\ \text{-求和本就是}\ \textbf{计数} \Longrightarrow \text{此修正}\ \textbf{不改变}\ (β)\ \text{判定}✓$$

## 5. 判定（唐先生四格）
$$\boxed{\begin{array}{c|c}\text{结果}&\text{判定}\\\hline\text{净得}\ L^{-\delta}&\mathrm{ALIVE}\\ \boxed{\text{收益恰被抵消}}&\boxed{\mathrm A，\text{净收益}=0}\\\text{成本超过收益}&\mathrm{DEAD}（\text{仅此架构}）\\\text{无法确定}&\mathrm{OPEN}\end{array}}✓$$
$$\Longrightarrow\ \textbf{本档：倾向第 2 行}\ \boxed{\mathrm A，\ \text{净收益}=0}✓✓\quad(\text{依据}：\ell\ \text{-求和}\ =\ \text{计数}\ (β)⟹\mathrm{C\!-\!S}\ \text{中性})✓$$
$$\qquad\textbf{不排除第 3 行}（\text{若某支路中}\ \ell\ \text{-内容实为纯振荡}\Rightarrow\alpha）✓$$
$$\qquad\Longrightarrow\ \text{不宣布 DEAD；}\ \text{但}\ \textbf{ALIVE 已排除}（\text{无幂次收益}）✓✓$$

## 6. 残余（不得省略）
$$\text{残余 1（关键）：}C_{\rm comb}\ \text{精确形式未定（第二副本各带变量}\Rightarrow\text{合并式不成立）}✓✓$$
$$\text{残余 2：}\ \alpha/\beta\ \text{的}\ \textbf{全支路裁定} \text{未做（本档据 (4.14) 倾向}\ β）✓$$
$$\text{残余 3：退化支计数界与 Weil 支的同账比较未完成}✓\quad\text{残余 4：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只写 C--S over}\ \ell_1\ \text{的真实结构；}\quad\text{② }\textbf{不} \text{宣布 DEAD／ALIVE}；\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) ⭐⭐⭐ C--S over}\ \ell_1\ \text{的精确效果：}\ |\sum g|\le L^{1/2}(\#\{\text{admissible}\ \ell_1\})^{1/2} \Longrightarrow \boxed{\text{把}\ \ell_1\ \text{的振荡换成计数}}✓✓✓$$
$$\text{(ii) ⭐⭐⭐ 精确二分：}\ (α)\ \text{振荡}\Rightarrow\mathrm{C\!-\!S}\ \text{杀死}\Rightarrow\mathrm{DEAD}；\ (β)\ \text{计数}\Rightarrow\text{中性}\Rightarrow\mathrm A\ \text{净收益}=0✓✓$$
$$\text{(iii) ⭐⭐⭐ BC 用法定位：}\ (4.14)\ \text{的}\ L^2/(\cdot)\ \text{计数＋Weil 在}\ n_2'\ \Longrightarrow \boxed{\text{倾向}\ (β)} \Longrightarrow \boxed{\mathrm A，\text{净收益}=0}✓✓$$
$$\text{(iv) ⚠️ 修正 V2-32 第二层：两份副本}\ \textbf{各带自己的一份变量} \Longrightarrow \text{合并式不成立} \Longrightarrow C_{\rm comb}\ \text{精确形式未定}✓✓$$
$$\text{(v) ALIVE 已排除（无幂次收益）；DEAD 未宣布}✓$$
