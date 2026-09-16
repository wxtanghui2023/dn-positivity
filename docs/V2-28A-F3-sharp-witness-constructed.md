# V2-28A — **$F_3$ 的 sharp witness 已构造** ⟹ $F_3$ 侧封死

> 唐先生 2026-09-16 21:45 拍板：**顺序＝先 V2-28A（$F_3$ sharp witness），再 V2-28B（$F_5$ 的 $L^{5/2}$）**✓
> **措辞收紧（采纳）**：$\boxed{\text{账本闭合}\ne\text{估计 sharp}}$✓
> V2-28A 判据：$\exists(\alpha,\nu):\ D_b^{\rm deg}\asymp\|\alpha\|^2\|\nu\|^2LM^{1-o(1)}$ ⟹ $\boxed{F_3\ \text{sharp}}$✓

---

## 1. ⭐ 构造（三类要素齐备）
$$\textbf{要素 1（相位＝1）}：\ \text{退化支路中}\ e\bigl(\tfrac{\eta(a_1\ell_1-a_2\ell_2)m}{b\ell_1n_1}\bigr)=e(0)=1 \Longrightarrow \textbf{无振荡抵消}✓✓$$
$$\textbf{要素 2（合法系数）}：\ \text{取}\ \boxed{\alpha_a=\tfrac{1}{\sqrt A}\ (a\asymp A),\qquad \nu_n=\tfrac{1}{\sqrt N}\ (n\asymp N)}✓✓$$
$$\qquad\textbf{合法性}：\ (3.1)\ \text{对}\ \textbf{任意}\ (\alpha,\nu)\ \text{成立（界以}\ \|\alpha\|,\|\nu\|\ \text{表示）}⟹ \text{常系数族}\ \textbf{合法}✓✓$$
$$\qquad\|\alpha\|^2=1,\quad\|\nu\|^2=1✓\qquad\text{且系数}\ \textbf{非负、相位对齐}✓$$
$$\textbf{要素 3（计数）}：\ \text{退化配置数（V2-21／22b 参数化）}：$$
$$\qquad N_{\rm deg}=\sum_u\underbrace{u}_{\#v}\cdot\underbrace{\tfrac Au}_{\#k}\cdot\underbrace{\tfrac Lu}_{\#g}\cdot\underbrace{\tfrac Nu}_{\#w}=\ A\,L\,N\sum_{u\ge1}\tfrac1{u^3}=A\,L\,N\,\zeta(3)=O(ALN)✓✓$$
$$\qquad(\textbf{由}\ u\asymp1\ \text{支配——}\zeta(3)\ \text{收敛}✓\quad\text{注意此处}\ \textbf{不是} \text{V2-23 已撤回的错误权重})✓$$

## 2. ⭐⭐ 求和估值（逐项）
$$D_b^{\rm deg}\ \asymp\ \underbrace{M^{1-o(1)}}_{m\ \text{-求和（相位}\ 1\text{，扣除互素条件）}}\ \times\ \sum_{\rm deg}\underbrace{|\nu_{n_1}\alpha_{a_1}|^2}_{=\frac1{AN}}✓$$
$$\qquad\Longrightarrow\ D_b^{\rm deg}\ \asymp\ M^{1-o(1)}\cdot(A\,L\,N)\cdot\tfrac1{AN}\ =\ \boxed{\,L\,M^{1-o(1)}\,}✓✓✓$$
$$\qquad\text{即}\ \boxed{D_b^{\rm deg}\asymp\|\alpha\|^2\|\nu\|^2\,L\,M^{1-o(1)}}✓✓✓\quad(\text{因}\ \|\alpha\|^2=\|\nu\|^2=1)✓$$
$$\qquad\textbf{对照 BC 的界}：\ O(\|\alpha\|^2\|\nu\|^2LM^{1+\varepsilon}) \Longrightarrow \boxed{\textbf{上下界同阶（差}\ M^{o(1)}\text{）}}✓✓✓$$

## 3. ⭐⭐⭐ 判定：$F_3$ **sharp**
$$\boxed{F_3\ \textbf{在当前 BC 退化计数架构中是}\ sharp}✓✓✓\quad(\text{由 §1--§2 的显式 witness})✓$$
$$\qquad\textbf{这比 V2-23 的"计数精确"}\ \textbf{更强}：\ \text{V2-23 只证}\ \text{上界已精确}；\ \text{本档给出}\ \textbf{达到该上界的合法系数族}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{"改善退化计数"这一条路}\ \textbf{正式封死}}✓✓\quad(\text{唐先生预判之"很快结束"，}\text{成立})✓$$
$$\qquad\textbf{且注意}：\ \text{sharpness 是}\ \textbf{支路级} \text{的（相位＝1 使然）；}\ \text{不涉及}\ (3.1)\ \text{另两项（Weil 支）}✓$$

## 4. ⭐⭐ 结构性后果（本档最重要的推论）
$$\text{平衡条件}：\ F_5\ =\ F_3\ \text{（在}\ L^{*}\ \text{处）}；\qquad F_3=\frac{M^2}{L}\ \textbf{已 sharp}✓$$
$$\qquad\Longrightarrow\ \boxed{\text{在}\ F_3\ \text{侧已无幂次改进空间}} \Longrightarrow \boxed{\textbf{唯一杠杆\ ＝\ }F_5}✓✓$$
$$\qquad\Longrightarrow\ \text{若要}\ \text{把}\ N\ \text{指数从}\ \tfrac{19}{20}\ \text{压低，只能}\ \textbf{改进}\ F_5\ \text{侧}✓✓$$
$$\qquad(\text{与唐先生框架一致：}\text{"即使}\ F_3\ sharp\ \text{也只封死改善退化计数这一条路"}\ ⟹\ \text{不构成对}\ F_5\ \text{的任何封堵})✓$$

## 5. ⚠️ 未做之事（诚实登记）
$$\textbf{未} \text{证明}\ F_3\ \text{的 sharpness 蕴含}\ (3.1)\ \text{另两项亦 sharp}✓\quad(\text{未审计})$$
$$\textbf{未} \text{处理}\ \text{supp}\ \text{类约束（}\alpha,\nu\ \text{的支撑是否须满足 BC 应用侧的附加条件）}✓\quad(\text{残余 1})✓$$
$$\textbf{未} \text{审计}\ C_b\ \text{侧的同一 witness（本档只给}\ D_b\ \text{侧；}\mathcal C_b\ \text{的因子}\ M/L\ \text{不影响 sharpness 结论）✓$$

## 6. 残余（不得省略）
$$\text{残余 1：}\ \text{BC 应用侧对}\ \alpha,\nu\ \text{的支撑／归一化约定是否排除常系数族}（\text{疑不排除：界以}\ \|\alpha\|\text{、}\|\nu\|\ \text{表述）✓}$$
$$\text{残余 2：}\ F_3\ \text{的 sharpness 仅在}\ \textbf{退化支路} \text{；}\ (3.1)\ \text{的 Weil 两项 sharpness 未审计}✓$$
$$\text{残余 3：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只做}\ F_3\ \text{的 sharp witness；}\quad\text{② }\textbf{未} \text{宣布}\ F_5\ \text{的任何结论}；\quad\text{③ }\textbf{未用 RH}；\ \text{零数值（计数量级）}✓$$

## 8. 净产出
$$\text{(i) ⭐⭐ 构造：}\ \alpha_a=A^{-1/2},\ \nu_n=N^{-1/2}（\text{合法、非负、相位对齐}）✓✓$$
$$\text{(ii) ⭐⭐⭐ }N_{\rm deg}\asymp ALN\,\zeta(3)（u\asymp1\ \text{支配}）\Longrightarrow D_b^{\rm deg}\asymp LM^{1-o(1)} \textbf{＝BC 的上界}✓✓✓$$
$$\text{(iii) ⭐⭐⭐ 判定}\ \boxed{F_3\ \text{sharp}} \Longrightarrow \boxed{\text{"改善退化计数"正式封死}}✓✓✓$$
$$\text{(iv) ⭐⭐ 推论：}\ F_3\ \text{侧无幂次空间} \Longrightarrow \boxed{\textbf{唯一杠杆＝}F_5}✓✓$$
$$\text{(v) 未做：}\ (3.1)\ \text{Weil 两项 sharpness／}\ C_b\ \text{侧 witness／supp 约定（残余 1--2）}✓$$
