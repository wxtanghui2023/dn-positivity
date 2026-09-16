# 猎-6（$\mathfrak F$-1a）— **一篇形式核验 ⟹ 判定 C**

> 唐先生 2026-09-16 20:07 拍板：**只做一篇、一次性形式核验**；不扩展扫描。
> 核验标准（唐先生固定）：$$\boxed{\text{post-BC 估计}\Longrightarrow\text{能否直接产生统一的}\ (r,t)\ ?}$$
> 四检：(1) 是否同一三线性模板；(2) 参数范围是否覆盖 Theorem 2 所需**整个**参数族；(3) 指数能否提为**单一统一** $(r,t)$；(4) 若能，算 $L=17r+t$ 是否 $<8$。

---

## 1. 核验对象（外部来源，仅作数据；**仅凭摘要／片段，未读全文**）
$$\text{2026 论文 I}：\text{"Trilinear Kloosterman fractions I: }\textbf{partially fixed moduli}\text{ and }\dots\text{"}\ (\text{arXiv:2604.25177v2})$$
$$\qquad\text{原文}：\text{"we }\textbf{improve Bettin and Chandee's famous result}\ \text{on trilinear forms with Kloosterman fractions}\ \boxed{\text{in the case where}}\dots\text{"}$$
$$\text{2026 论文 II}：\text{"Trilinear Kloosterman fractions II: }\textbf{subdyadic intervals}\text{ and nearly balanced convolutions"}\ (\text{arXiv:2608.27732})$$
$$\qquad\text{原文}：\text{"}\textbf{To prove this, we sharpen Bettin and Chandee's famous result}\dots\ \boxed{\text{in the case where some of the sums are over subdyadic intervals}}\text{"}$$
$$\Longrightarrow\ \boxed{\text{两者的提升均以}\ \textbf{"in the case where"}\ \text{限定} \Longrightarrow \textbf{情形受限型}}✓✓\ (\textbf{直接命中 C 型证据})$$

## 2. 四检逐项
$$\textbf{检 1（同一模板）}：\ \text{对象同为三线性}\ \mathcal B(M,N,A)/S_{A,M,N}\ \Longrightarrow \textbf{对象层同一}✓\ \text{但}\ \textbf{陈述层受限}✓$$
$$\textbf{检 2（参数范围）}：\ \textbf{✗ 不覆盖} \text{——改进仅对}\ \textbf{subdyadic intervals／partially fixed moduli}\ \text{成立}，}\ \text{即}\ \textbf{子区域}，\ \text{非 Theorem 2 所需全参数族}✓$$
$$\textbf{检 3（能否提为统一}\ (r,t)\text{）}：\ \textbf{✗ 不能} \text{——}\ (r,t)\ \text{是}\ \textbf{一致指数}，\ \text{而改进是}\ \textbf{情形局部} \text{的} \Longrightarrow \text{不存在单一统一}\ (r,t)✓$$
$$\textbf{检 4（}L\ \text{计算）}：\ \textbf{不适用} \text{（检 3 已失败）}✓$$

## 3. ⭐ 判定：**C（不能转成统一 $(r,t)$）**
$$\boxed{\text{C}：\ \text{确认}\ \textbf{"局部改进}\ne\mathfrak F\ \text{点"}}\quad(\text{第一篇即落入 C，符合唐先生预期})✓$$
$$\textbf{且本档给出更锐的机制（新信息）}：$$
$$\qquad\text{(i) BC 自身的界}\ \textbf{本就是非一致的}\ \text{两顶结构（据 BC 原文 Theorem 1 片段）}：$$
$$\qquad\qquad \mathcal B(M,N,A)\ll\|\alpha\|\|\beta\|\|\nu\|\Bigl(1+\tfrac{|\vartheta|A}{MN}\Bigr)^{\frac12}\Bigl((AMN)^{\frac7{20}+\varepsilon}(M+N)^{\frac14}+(AMN)^{\frac38+\varepsilon}(AN+AM)^{\frac18}\Bigr)$$
$$\qquad\qquad\text{且其原文把节省表述为}\ \textbf{"in the important case}\ M\approx N,\ a\ll MN\text{"}\ \text{型}\ \textbf{条件陈述}✓$$
$$\qquad\text{(ii) 而 BCR 从这样的}\ \textbf{非一致} \text{界中}\ \textbf{制造出} \text{统一}\ (r,t)=(\tfrac9{20},\tfrac7{20}) \Longrightarrow (r,t)\ \text{的提取是}\ \textbf{应用侧针对特定配置的优化}✓✓$$
$$\Longrightarrow\ \boxed{\text{故"统一性"是}\ \textbf{应用制造的}，\ \textbf{而非} \text{估计给出的}} \Longrightarrow \text{改进估计的}\ \textbf{子情形} \text{未必改进}\ \textbf{被提取的}\ (r,t)✓✓$$

## 4. 由此获得进入 $\mathfrak F$-1b 的资格（唐先生预设条件）
$$\text{唐先生：}\text{"若第一篇就落入 C，那么我们有资格}\ \textbf{谨慎} \text{进入}\ \mathfrak F\text{-1b"}\ ✓$$
$$\boxed{\mathfrak F\text{-1b}：\ \text{为什么}\ \textbf{uniformity 本身} \text{会制造}\ 17r+t\ge8\ \text{的刚性？}}$$
$$\qquad\text{本档为其提供的入口形态（\textbf{未开}）}：$$
$$\qquad\text{(a) 从}\ \text{BC 的两顶非一致界} \to \text{BCR 的统一}\ (r,t)：\ \text{该优化的可行域}\ \text{是否必然受}\ L\ge8\ \text{约束}？$$
$$\qquad\text{(b) 从}\ \text{(1.3)}\ \text{的模板结构} \to \text{统一性}\ \text{要求：}\ \text{一致指数是否}\ \textbf{强迫} \text{在}\ (M,N,A)\ \text{全族上取最坏情形，}\ \text{而最坏情形恰在}\ L=8\ ?$$

## 5. 残余（不得省略）
$$\text{残余 1：\ 2026 论文 I／II 仅凭摘要与片段，}\textbf{未读全文} \Longrightarrow \text{subdyadic／partially fixed moduli 的}\ \textbf{精确定义未知}✓$$
$$\text{残余 2：}\ \textbf{未判定} \text{BCR 的配置（}A=\tfrac{N_1N_2}{d}T^{\frac12-\varepsilon}）\ \text{是否落入那些子情形} \Longrightarrow \text{若落入，理论上仍可能产生改进}（\text{但须重跑 BCR 应用，}\textbf{超出一次性形式核验})✓$$
$$\text{残余 3：}\ \text{BC Theorem 1 的两顶结构与}\ (9/20,7/20)\ \text{之间的提取过程}\ \textbf{未核}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① 仅凭检索摘要／片段，}\textbf{未读全文}；\quad\text{② 遵守"一篇、一次性"纪律，}\textbf{不扩展扫描}✓$$
$$\text{③ }\textbf{未用 RH}；零数值（\text{未做}\ L\ \text{计算，因检 3 已失败）}；\ \text{未跑 Lean}✓$$

## 7. 净产出
$$\text{(i) 核验对象：2026 论文 I（partially fixed moduli）／II（subdyadic intervals）——两者提升均以}\ \textbf{"in the case where"}\ \textbf{限定}✓$$
$$\text{(ii) 四检：检 1 对象同（但陈述受限）；}\textbf{检 2 ✗}；\ \textbf{检 3 ✗}；\ \text{检 4 不适用}；$$
$$\text{(iii) ⭐ 判定}\ \textbf{C}：\text{确认"局部改进}\ne\mathfrak F\ \text{点"；}\ \text{且给出机制：}\ (r,t)\ \text{的提取是}\ \textbf{应用侧优化}，\ \text{故子情形改进未必改进}\ (r,t)；$$
$$\text{(iv) 进入}\ \mathfrak F\text{-1b}\ \text{的资格成立（唐先生预设）＋}\ \mathfrak F\text{-1b}\ \text{的两个入口形态（\text{未开}）。}$$
