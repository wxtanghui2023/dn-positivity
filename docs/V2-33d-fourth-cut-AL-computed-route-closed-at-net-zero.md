# V2-33 第四刀（收口刀）— **$\mathcal A_L=L^{o(1)}$ 算出** ⟹ 本路线**封成"净收益 $=0$"**

> 唐先生 2026-09-16 22:22「继续」✓
> 任务（REVIEW-V2I §5）：$\boxed{\text{把平方后的全部 admissibility 条件固定下来，计算}\ \mathcal A_L}$✓

---

## 1. ⭐⭐⭐ 关键结构事实：$|g(\ell_1)|^2$ 中 $\ell_1$ 的**相位相消**
$$\text{C--S 后的对象}：\ \sum_{\ell_1}\bigl|g(\ell_1)\bigr|^2 \qquad (\text{同一指标}\ \ell_1\ \text{出现在两个因子里，}\ \textbf{非} \text{两份独立副本})✓✓$$
$$\qquad g(\ell_1)\ \text{的}\ \ell_1\ \text{-依赖}\ \textbf{全部在相位中}（\text{经}\ \overline{\tilde\ell_1\tilde\ell_1'}\ \text{等模逆元}）\Longrightarrow \bigl|g(\ell_1)\bigr|^2\ \text{中}\ \textbf{相位与其共轭相消}✓✓✓$$
$$\Longrightarrow\ \boxed{\bigl|g(\ell_1)\bigr|^2\ \text{的}\ \ell_1\ \text{-依赖}\ \textbf{仅剩条件}：\ \mathfrak p_1,\mathfrak q_1|(\ell_1,\ell_1')、\text{互素}、\ell_1\in\mathcal L\ \text{等}}✓✓$$
$$\Longrightarrow\ \boxed{\#\{\ell_1:\ \text{平方后全部约束成立}\}\ =\ \#\{\ell_1:\ \textbf{原约束} \text{成立}\}}✓✓✓$$
$$\qquad(\textbf{即无新约束}：\ell_1\ \text{在同一指标下出现，其相位相消}\Longrightarrow \text{不引入关于}\ \ell_1\ \text{的新同余／新条件})✓✓$$

## 2. ⭐⭐⭐ $\mathcal A_L$ 的计算
$$\text{原约束下的计数}：\ \text{(4.14) 逐字}\ \frac{L^2}{(\mathfrak p_1+\mathfrak q_1)(\mathfrak p_2+\mathfrak q_2)}\ \text{（两个}\ \ell）\Longrightarrow \text{单个}\ \ell\ \text{约}\ \frac{L}{\mathfrak p+\mathfrak q}\ \asymp\ L^{1-o(1)}✓✓$$
$$\Longrightarrow\ \boxed{\mathcal A_L\ =\ \frac{\#\{\text{平方后 admissible}\ \ell_1\}}{\#\{\text{原 admissible}\ \ell_1\}}\ =\ 1\ =\ L^{o(1)}}✓✓✓$$
$$\qquad(\text{严格地：}\ \mathcal A_L\ \text{为}\ L^{o(1)}\ \text{——除数因子}\ \mathfrak p+\mathfrak q\ \text{在两侧相同})✓$$

## 3. ⭐⭐⭐ 净收益（第四刀结论）
$$\boxed{\text{净幂次}\ =\ \underbrace{L^{-1}}_{\text{裸计数收益}}\times\underbrace{L}_{\text{C--S}}\times\underbrace{\mathcal A_L=L^{o(1)}}_{\text{新增稀疏度}}\ =\ L^{o(1)}\ =\ L^{0}}✓✓✓$$
$$\Longrightarrow\ \boxed{\text{净收益}\ =\ 0\quad（\text{即"收益恰被新增 C--S 成本抵消"，唐先生四格第 2 行）}}✓✓✓$$
$$\qquad\textbf{且这}\ \textbf{不使用} \text{任何新估计、}\textbf{不越界} \text{到}\ 17/33✓✓$$

## 4. ⚠️ 唯一的定性残余（不属幂次账）
$$\text{C--S 使其余变量}\ \textbf{成对出现}（n_2'\to(n_2',n_2'')\ \text{等}）\Longrightarrow \text{平方后的对象}\ \textbf{不再是}\ \text{单个}\ n_2'\ \text{-Kloosterman 和}✓✓$$
$$\qquad\Longrightarrow\ \text{须}\ \textbf{新估计}（\text{双变量}\ n\ \text{-和}）✓$$
$$\qquad\textbf{本刀结论的条件}：\ \text{若新估计}\ \textbf{至少与原来一样好} \Longrightarrow \text{净收益}=0✓；\ \text{若}\ \textbf{更差} \Longrightarrow \text{净为负（}\mathrm{DEAD}\ \text{此架构}）✓✓$$
$$\qquad\Longrightarrow\ \text{故}\ \boxed{\text{本路线在}\ \textbf{幂次账} \text{上封成"净收益}=0；但"平方后能否同样好地估计"}\ \text{为}\ \textbf{独立残余}}✓✓$$

## 5. ⭐ 封闭声明（按唐先生纪律）
$$\boxed{\text{本路线（单}\ \ell\ \text{反向 C--S）在}\ \textbf{幂次账} \text{上封成}\ \boxed{\text{净收益}=0}}✓✓$$
$$\qquad\textbf{无需} \text{再包装成更大的"17/33 硬墙"}✓✓\qquad\textbf{且}\ \text{该结论}\ \textbf{不} \text{声称"BC 的 C--S 几何全局最优"}✓$$
$$\qquad(\text{仅：}\ \text{"再平方一个}\ \ell\ \text{不能产生幂次改善"}\ \text{——}\ \text{一个}\ \textbf{局部、干净} \text{的结论})✓✓$$

## 6. 残余（不得省略）
$$\text{残余 1：平方后双变量}\ n\ \text{-和能否与原来同阶估计（定性；若更差}\Rightarrow\mathrm{DEAD}）✓$$
$$\text{残余 2：退化支（}C_{\rm comb}=0\text{）的计数界与 Weil 支同账比较未完成}✓$$
$$\text{残余 3：}\ \mathcal A_L=1\ \text{依据 (4.14) 的计数形式＋"同指标相位相消"；}\ \text{若某支路}\ \ell_1\ \text{以}\ \textbf{两个独立副本} \text{出现}\Rightarrow\mathcal A_L\ \text{需重算}✓$$
$$\text{残余 4：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只算}\ \mathcal A_L\ \text{与幂次账；}\quad\text{② }\textbf{不} \text{宣布 ALIVE／DEAD}；\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) ⭐⭐⭐ 关键事实：}\ |g(\ell_1)|^2\ \text{中}\ \ell_1\ \text{的相位}\ \textbf{相消}（同指标）\Longrightarrow \ell_1\ \text{-依赖仅剩条件}\Rightarrow \textbf{无新约束}✓✓✓$$
$$\text{(ii) ⭐⭐⭐ }\boxed{\mathcal A_L=1=L^{o(1)}}\ \text{（依据 (4.14) 计数形式＋除数因子两侧相同）}✓✓✓$$
$$\text{(iii) ⭐⭐⭐ 净收益＝}L^{-1}\times L\times L^{o(1)}=L^{0}\Longrightarrow \boxed{\text{净收益}=0}✓✓✓$$
$$\text{(iv) ⭐⭐ 封成结论：}\ \text{单}\ \ell\ \text{反向 C--S}\ \textbf{不能产生幂次改善}（\text{局部、干净；不包装成硬墙}）✓✓$$
$$\text{(v) ⚠️ 定性残余：平方后双变量}\ n\ \text{-和能否同阶估计（若更差}\Rightarrow\mathrm{DEAD}）✓$$
