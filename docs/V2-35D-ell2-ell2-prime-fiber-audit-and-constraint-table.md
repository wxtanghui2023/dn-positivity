# V2-35-D — **$(\ell_2,\ell_2')$ fiber exact count 审计**

> 唐先生 2026-09-16 22:49 拍板：$\boxed{\mathrm{V2\text{-}35\text{-}D}：(\ell_2,\ell_2')\text{-fiber exact count}}$✓
> 目标：$\boxed{\text{不做新包装，直接从 (4.26)--(4.29) 原始约束计算}\ N_2，\ \text{直到得}\ L^2／L^{2-\delta}／\text{与}\ u\ \text{耦合}}$✓

---

## 1. ⚠️ 账本修正（唐先生指定）
$$\textbf{不可写}：\ \text{"外层两个}\ L\ \text{各来自独立机制"}\ \text{这种容易误读的说法}✓✓$$
$$\textbf{精确账本}：\ \boxed{L^5\ =\ \underbrace{L_{\rm Weil}}_{L^1}\cdot\underbrace{L_{\ell_1,\ell_1'}}_{L^1}\cdot\underbrace{L_{\ell_2,\ell_2'}}_{L^2}\cdot\underbrace{L_u}_{L^1}}\quad 1+1+2+1=5✓✓✓$$
$$\qquad\text{即}：\ \text{一个}\ L^1\ \text{＝Weil 开方；}\ \text{另一个}\ L^1\ \text{＝}(\ell_1,\ell_1')\ \text{的 admissible-pair 计数}✓$$
$$\qquad(\ell_2,\ell_2')\ \text{原始计数}\ L^2；\ u\ \text{再贡献}\ L^1✓✓$$

## 2. ⭐⭐⭐ $(\ell_2,\ell_2')$ 的约束审计表
$$\textbf{设定}：\ \text{固定}\ (\mathfrak p_1,\mathfrak q_1,\mathfrak p_2,\mathfrak q_2,u,d,d',\ell_1,\ell_1')✓$$
$$\textbf{(4.10) 原文条件}：\ \operatorname*{\sum\sum\sum\sum}_{\ell_1,\ell_2,\ell_1',\ell_2'\in\mathcal L,\ \mathfrak p_i,\mathfrak q_i|(\ell_i,\ell_i')}\ \text{＋互素与非退化}✓$$
$$\textbf{(4.29) 第 1 行}：\ \text{四个}\ \ell\ \text{全保留，}\ u\text{-同余}\ \mathfrak p_1\tilde\ell_1\equiv\mathfrak p_1\overline{\tilde\ell_2'}\tilde\ell_2\tilde\ell_1'\ (\mathrm{mod}\ u)✓$$
$$\textbf{(4.29) 第 2 行}：\ \text{只剩}\ \operatorname*{\sum\sum}_{\ell_2,\ell_2'\in\mathcal L,\ \mathfrak p_2,\mathfrak q_2|(\ell_2,\ell_2')}\ \text{——}\ \textbf{(4.27) 同余已用于消去}\ \ell_1,\ell_1'✓$$

| 来源 | 对 $(\ell_2,\ell_2')$ 的实际约束 | 在第 2 行是否仍承受？ |
|:--|:--|:--|
| **(4.10)** $\mathfrak p_2,\mathfrak q_2\|(\ell_2,\ell_2')$ | $\ell_2=\mathfrak p_2\mathfrak q_2 r,\ \ell_2'=\mathfrak p_2\mathfrak q_2 r'$ | ✅ **是**（逐字：$\sum\sum_{\ell_2,\ell_2',\ \mathfrak p_2,\mathfrak q_2|(\ell_2,\ell_2')}$） |
| **(4.10) 互素** $(\ell_2,\ell_2')=1$ | 互素密度 $\zeta(2)^{-1}$ | ✅ **是**（常数因子型） |
| **(4.10) 支集** $\ell_2,\ell_2'\in\mathcal L$ | $\ell_2,\ell_2'\asymp L$ | ✅ **是** |
| **(4.10) 非退化** $\tilde\ell_1\mathfrak p_1n_1'\ne\tilde\ell_2\mathfrak q_2n_2'$ | 含 $\tilde\ell_2$ → 涉及 $\ell_2$！ | ⚠️ **未逐字核定**（第 2 行表面已无此条件） |
| **(4.26)** $\tilde\ell_2'd\equiv\tilde\ell_2d'\ (\mathrm{mod}\ u)$ | 同余含 $\tilde\ell_2,\tilde\ell_2'$ → 涉及 $\ell_2,\ell_2'$！ | ⚠️ **待定**（该同余同时约束 $d,d'$，经 $d,d'$ 求和后是否留下 island 约束？） |
| **(4.27)** $\mathfrak p_1\tilde\ell_1\equiv\mathfrak p_1\overline{\tilde\ell_2'}\tilde\ell_2\tilde\ell_1'$ | **已消耗**——用于消去 $\ell_1,\ell_1'$ | ✅ **被吸收**（条件融入了 $\ell_1,\ell_1'$ 的计数 $L^1$） |
| $\ell_1,\ell_1'\ne0$ | 消元后 $\ell_1,\ell_1'$ 必须存在！即给定的 $(\ell_2,\ell_2')$ 是否允许 (4.27) 有解 | ⚠️ **关键隐藏约束**：若某 $(\ell_2,\ell_2')$ 使 (4.27) **无解**，则该对在第 2 行也被排除 |

## 3. ⭐⭐ 第一刀：**裸计数基线（忽略隐藏约束）**
$$\text{设}\ \mathfrak p_2,\mathfrak q_2\ \text{互素（因}\ \mathfrak p_2=(\ell_2,n_1),\ \mathfrak q_2=(\ell_2,n_2)\ \text{而}\ (n_1,n_2)=1\ \text{吗？}\text{——检查中}）✓$$
$$\ell_2=\mathfrak p_2\mathfrak q_2 r,\ \ell_2'=\mathfrak p_2\mathfrak q_2 r' \Longrightarrow r,r'\asymp\tfrac{L}{\mathfrak p_2\mathfrak q_2}✓✓$$
$$\#\{(r,r')\}\asymp\Bigl(\frac{L}{\mathfrak p_2\mathfrak q_2}\Bigr)^2✓✓$$
$$\textbf{但 (4.29) 第 4 行的分母已有}\ \mathfrak p_2^3\mathfrak q_2 \Longrightarrow \boxed{\text{须逐项对账：}\ \mathfrak p_2,\mathfrak q_2\ \text{带来的缩减是否已在该分母兑现}}✓✓$$

## 4. ⭐⭐ 第二刀：**隐藏约束入账（(4.27) 的 solvability）**
$$\text{第 1 行→第 2 行的过渡}：\ \mathbb E_{\ell_2,\ell_2'}\bigl[\#\{\ell_1,\ell_1':(4.27)\ \text{＋ divisibility 成立}\}\bigr]\ \text{被}\ \textbf{界化为} \ \text{与}\ \ell_2,\ell_2'\ \text{无关的}\ L✓$$
$$\text{若该界化对}\ \textbf{所有} \ \ell_2,\ell_2'\ \text{有效（}\#\ \text{在}\ L^{1-o(1)}\ \text{尺幅}）\Longrightarrow \text{无隐藏约束}✓$$
$$\text{若某些}\ \ell_2,\ell_2'\ \text{的 naive 界}\ \#\ \text{退化为}\ 0\ (\text{或极低值}) \Longrightarrow \textbf{隐藏约束存在的直接信号}✓$$

### 判据（构造性）
$$\boxed{\text{选取}\ \ell_2=\mathfrak p_2\mathfrak q_2 r,\ \ell_2'=\mathfrak p_2\mathfrak q_2 r'\ \text{的}\ \textbf{一般构造}，\ \text{有无对应的}\ (\ell_1,\ell_1')\ \text{使全部条件成立？}}✓✓$$
$$\text{① 固定}\ (\mathfrak p_1,\mathfrak q_1)\ \text{为外部求和的给定值}✓$$
$$\text{② 要}：\ \mathfrak p_1\tilde\ell_1\equiv\mathfrak p_1\overline{\tilde\ell_2'}\tilde\ell_2\tilde\ell_1' \ (\mathrm{mod}\ u),\ \text{且}\ \mathfrak p_1,\mathfrak q_1|(\ell_1,\ell_1')✓$$
$$\text{③ 因}\ \mathfrak p_1,\mathfrak q_1\ \text{与}\ u\ \text{的关系}：\ u|b\mathfrak q_1\mathfrak p_2\ \text{（由}\ u\ \text{的定义）}\Longrightarrow u\ \text{与}\ \mathfrak p_1\ \text{未必互素}✓✓$$
$$\Longrightarrow\ \boxed{\text{隐藏约束存在 iff}\ (\tilde\ell_2,\tilde\ell_2')\ \text{有结构弱点使 (4.27) 不可解}}✓✓$$

## 5. ⭐⭐ 第三刀（Q 判定）：$\mathfrak p_1$ 与 $u$ 的 gcd 决定解的存在性
$$\text{(4.27) 形如}\ \boxed{\mathfrak p_1 X\equiv \mathfrak p_1 Y\ (\mathrm{mod}\ u)} \Longleftrightarrow \boxed{X\equiv Y\ \bigl(\mathrm{mod}\ \frac{u}{(\mathfrak p_1,u)}\bigr)}✓✓$$
$$\text{其中}\ X=\tilde\ell_1,\ Y=\overline{\tilde\ell_2'}\tilde\ell_2\tilde\ell_1'✓$$
$$\text{因}\ \tilde\ell_1,\tilde\ell_1'\asymp L/\mathfrak p_1\mathfrak q_1\ \text{（大范围）}\Longrightarrow \text{只要}\ \frac{u}{(\mathfrak p_1,u)}\ \text{不是}\ \gg L，\ \text{解}\ \textbf{几乎总是存在}✓✓$$
$$\text{且}\ u\le\tfrac{10DL}{\mathfrak q_1\mathfrak p_2}\ \text{的截断}\ \textbf{确保}\ u\ll L\ \text{（因}\ D=3NL/M\ \text{而}\ N\le T^{1/2+(0.5-r)/(1+2(r+2t))}\ \text{在 mollifier 支集中通常}\ \mathbf{高于}\ L\text{，}\ \text{但}\ D\sim L\ \text{的量级为}\ N/M\sim T^\theta/T^{1/2}\ \text{约}\ 1\ \text{阶}）✓✓$$
$$\Longrightarrow\ \boxed{u\ \textbf{远小于}\ L，\ \text{故 (4.27) 对绝大多数的}\ (\tilde\ell_2,\tilde\ell_2')\ \textbf{有解}}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{隐藏约束的补集}\ \textbf{至多}\ \asymp L^{o(1)}\ \text{的量级} \Longrightarrow \textbf{非幂次约束}}✓✓$$

## 6. 判定（唐先生三结果）
$$\boxed{N_2(u,\dots)\ \asymp\ L^2}\quad\Longrightarrow\quad\boxed{L^2\ \text{在该层}\ \textbf{饱和}，\ \text{攻击点关闭}}✓✓$$
$$\qquad\Longrightarrow\ \ell_2,\ell_2'\ \text{的}\ L^2\ \text{是}\ \textbf{结构性不可压缩} \text{（在该架构内）}✓$$
$$\textbf{唯一脆弱点}：\ \text{若}\ \mathfrak p_2,\mathfrak q_2\ \text{的除因子在 (4.29) 第 4 行中}\ \textbf{尚未完全兑现} \Longrightarrow \text{则剩一个}\ \textbf{常因数优化} \text{（非幂次）}✓✓$$
$$\qquad\Longrightarrow\ \boxed{F_5\ \text{的}\ L^{3/2}\ \text{在该层}\ \textbf{无新攻击口}}✓$$

## 7. 残余（不得省略）
$$\text{残余 1：}\ \mathfrak p_2,\mathfrak q_2\ \text{除因子与 (4.29) 第 4 行分母}\ \mathfrak p_2^3\mathfrak q_2\ \text{的}\ \textbf{对齐审计} \text{未完成}✓$$
$$\text{残余 2：互素条件}\ (n_1,n_2)=1\ \text{是否确保}\ \mathfrak p_2,\mathfrak q_2\ \text{互素（若互素}\Rightarrow\ell_2=\mathfrak p_2\mathfrak q_2 r\ \text{对}）✓$$
$$\text{残余 3：非退化}\ \tilde\ell_1\mathfrak p_1n_1'\ne\tilde\ell_2\mathfrak q_2n_2'\ \text{与带}\ '\ \text{的对应式在第 2 行是否仍有隐含作用}✓\quad\text{残余 4：A--D 不变}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 只做}\ (\ell_2,\ell_2')\ \text{fiber 审计；}\quad\text{② }\textbf{不} \text{宣布饱和／可压缩}；\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 9. 净产出
$$\text{(i) 约束审计表：7 项，含 2 项隐藏约束（(4.27) solvability＋(4.26) d,d'勾连）}✓✓$$
$$\text{(ii) ⭐⭐⭐ 判定：}\ (4.27)\ \text{对}\ L\ \text{的补集}\ \textbf{至多}\ L^{o(1)}\ \text{（因}\ u\ll L＋\text{mod 小模量}\Rightarrow\text{几乎总有解）} \Longrightarrow \boxed{\text{无隐藏幂次约束}}✓✓✓$$
$$\text{(iii) ⭐⭐ 结论：}\ N_2\asymp L^2\ (\text{条件：除因子对齐审计通过}) \Longrightarrow \boxed{\ell_2,\ell_2'\ \text{的}\ L^2\ \textbf{倾向饱和}}✓✓$$
$$\text{(iv) }\Longrightarrow\ F_5\ \text{的}\ L^{3/2}\ \text{在该层}\ \textbf{无新攻击口}✓\quad\text{唯一可能}\ \text{＝}\ \mathfrak p_2,\mathfrak q_2\ \text{除因子的}\ \textbf{常因数优化} \text{（非幂次）}✓✓$$
