# 猎-5（$\mathfrak F$-1）— **$\mathfrak F^{\rm uncond}$ 的已知点扫描 ＋ 一个关键障碍：范围局部性**

> 唐先生 2026-09-16 20:05 拍板：**𝔽-2 已闭合**（原文 §3.4 直接验证）；**转 𝔽-1**。
> 唐先生给定的等价措辞（采纳）：
> $$\boxed{\mathfrak F_A\cap\mathfrak F_{\rm application}\ \text{的排除由 §3.4}\ \textbf{显式验证} \Longrightarrow \mathfrak F=\mathfrak F_{\rm estimate}\ \text{有直接原文支撑}}✓$$
> $$\boxed{\mathfrak F_{\rm error}\ \textbf{已被消去为}\ \theta\ \text{的允许上界，}\ \textbf{而非}\ (r,t)\ \text{的独立可达条件}}\ ✓$$
> $$\qquad\text{干净分离}：\ (r,t)\in\mathfrak F_{\rm estimate}\Longrightarrow\theta<\Theta(r,t),\quad \Theta(r,t)=\frac{1+2t}{1+2r+4t}\ ✓$$
> **搜索纪律（唐先生）**：$\textbf{不} \text{搜"谁发表过更好的}\ \theta\text{"}；\ \textbf{而} \text{搜}\ \boxed{\text{所有 unconditional (1.3)-型估计}\to(r,t)\to L(r,t)=17r+t}✓$

---

## 1. 登记的目标函数与判据
$$\text{目标函数}：\ L(r,t)：＝17r+t；\ \text{已知}\ L\left(\tfrac9{20},\tfrac7{20}\right)=8（\text{恰在边界}），\ L\left(\tfrac{23}{48},\tfrac12\right)=\tfrac{415}{48}\approx8.646✓$$
$$\text{唯一问题}：\ \boxed{\exists\,(r,t)\in\mathfrak F^{\rm uncond}\ \text{使}\ L(r,t)<8\ ?}$$
$$\text{由上闭性（猎-4 §3）}：\ \text{一经找到严格带内点}\ (r_0,t_0) \Longrightarrow \operatorname{Up}(\{(r_0,t_0)\})\subset\mathfrak F \Longrightarrow \textbf{17/33 被严格突破}✓$$

## 2. 扫描结果（外部来源，**仅作数据**；本档未读全文）
$$\text{(a) }\textbf{已映射的两点}：\ \text{DFI}\ (\tfrac{23}{48},\tfrac12)\ (\text{双线性},\ 1997\ \text{Inventiones})；\ \text{Bettin--Chandee}\ (\tfrac9{20},\tfrac7{20})\ (\text{三线性},\ 2018\ \text{Adv.\ Math})✓$$
$$\text{(b) }\textbf{post-BC 改进确实存在}：$$
$$\qquad\text{-- "Bounds of trilinear sums with Kloosterman fractions"：}\text{在}\ \textbf{部分参数范围} \text{改进 BC}✓$$
$$\qquad\text{-- "On sums of Kloosterman and Gauss sums"：}\text{同样}\ \textbf{在部分范围} \text{改进 BC 的三线性界}✓$$
$$\qquad\text{-- "Trilinear Kloosterman fractions II: subdyadic intervals and nearly balanced convolutions"}\ (\text{2026-08}）：$$
$$\qquad\qquad\text{原文：}\text{"}\textbf{sharpen Bettin and Chandee's famous result}\ \text{in the case where some of the sums are over}\ \textbf{subdyadic intervals}\text{"}$$
$$\qquad\qquad\text{应用}：\text{Fouvry--Radziwiłł 近平衡卷积的}\ \delta<\tfrac{1}{68}\ (\text{原}\ \tfrac1{112})✓$$
$$\Longrightarrow\ \boxed{\text{改进}\ \textbf{均为"范围局部型"}（\text{部分范围／subdyadic}),\ \textbf{而非} \text{一致型}}✓$$

## 3. ⭐ 关键障碍（本档新识别）：**范围局部性 ≠ $(r,t)$ 点**
$$\text{(1.3) 的}\ (r,t)\ \text{是}\ \textbf{一致指数}：\ \text{界}\ \|\alpha\|\|\beta\|\|\nu\|(M+N)^{\frac12+r+\varepsilon}A^{t}\ \text{须对整个参数族}\ (bM,LN)\ \text{成立}✓$$
$$\qquad\text{而 §2(b) 的改进}\ \textbf{只在特定配置}（\text{subdyadic／部分范围）成立}✓$$
$$\Longrightarrow\ \boxed{\text{范围局部改进}\ \textbf{不自动} \Longrightarrow (r,t)\ \text{点；}\ \text{须先验证其}\ \textbf{形式与范围} \text{是否覆盖 (1.3) 模板的需求}}✓$$
$$\qquad\textbf{这与猎-2C §3 的"形式相容性"问题}\ \textbf{同源}：\ \text{对象是切片}\ne\text{估计可经模板分解}✓$$
$$\Longrightarrow\ \boxed{\mathfrak F^{\rm uncond}\ \textbf{可能远小于} \text{"各改进范围的并集"}}✓$$

## 4. 判定（本档落点）
$$\textbf{未发现} \text{任何}\ (r,t)\in\mathfrak F^{\rm uncond}\ \text{使}\ L(r,t)<8✓$$
$$\qquad\Longrightarrow\ \text{按唐先生二分}：\ \text{下一刀转为}\ \boxed{\text{为什么}\ 17r+t\ge8\ \text{会成为所有已知 unconditional 估计的共同边界？}}✓$$
$$\qquad\text{且}\ \textbf{唯一已映射的边界点} \text{＝BC 的}\ (\tfrac9{20},\tfrac7{20})；\ \text{另一点 DFI 在带外}✓$$
$$\textbf{同时确认（唐先生）}：\ \text{BCR 自述 Conjecture 1}\Longrightarrow\theta\ \text{任意}\ <1\Longrightarrow\text{Lindelöf} \Longrightarrow \textbf{17/33 不是 BCR 应用架构的理论终点，而是目前无条件估计的输入点}✓$$

## 5. 由此得到的两条下一刀（互斥）
$$\textbf{(𝔽-1a) 形式核验}：\ \text{逐篇核验 §2(b) 的改进是否能}\ \textbf{无损} \text{转成}\ (r,t)\ \text{点}（\text{须核其配置是否覆盖}\ A=\tfrac{N_1N_2}{d}T^{\frac12-\varepsilon}\ \text{型需求）}✓$$
$$\qquad\text{若某篇可无损转换}\ \Longrightarrow \text{直接得}\ (r,t)\ \text{点}\ \Longrightarrow\ \text{检查}\ L<8\ ?✓$$
$$\textbf{(𝔽-1b) 边界原因}：\ \text{若全部不可无损转换} \Longrightarrow \text{转而研究}\ \boxed{\text{为何}\ L\ge8\ \text{是所有已知 unconditional 估计的共同边界}}✓$$
$$\qquad\text{（\text{这可能是一个}\ \textbf{结构现象}：}\text{可用范围}\ \text{与}\ \text{指数}\ \text{之间存在}\ \textbf{刚性权衡}）✓$$

## 6. 残余（不得省略）
$$\text{残余 1：§2 的 post-BC 论文}\ \textbf{仅由检索片段得知}，\ \textbf{未读全文} \Longrightarrow \text{其确切指数}\ (r,t)\ \text{未知}✓$$
$$\text{残余 2：}\ \mathfrak F^{\rm uncond}\ \text{完整形状仍未知（仅两点已映射}）；\ \text{残余 3：本档未做任何}\ (r,t)\ \text{数值反演}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 检索结果为}\ \textbf{外部来源，仅作数据}，\ \text{未读全文；}\quad\text{② 遵守搜索纪律（}\textbf{不} \text{搜"更好的}\ \theta\text{"，}\textbf{只} \text{搜}\ (r,t)\to L）；$$
$$\text{③ }\textbf{未用 RH}；零数值（\text{仅}\ L\ \text{值演算}）；\ \text{未跑 Lean}✓$$

## 8. 净产出
$$\text{(i) 𝔽-2 闭合（§3.4 显式验证）＋ 措辞升级（}\mathfrak F=\mathfrak F_{\rm estimate}\ \text{有原文支撑）＋ }\mathfrak F_{\rm error}\ \text{措辞修正}；$$
$$\text{(ii) 目标函数}\ L=17r+t\ \text{与判据}\ \exists L<8\ \text{登记；}$$
$$\text{(iii) 扫描：post-BC 改进存在，但}\ \textbf{全部为范围局部型}；$$
$$\text{(iv) ⭐ }\textbf{新识别障碍}：\ \text{范围局部改进}\ \textbf{不自动} \text{给出}\ (r,t)\ \text{点} \Longrightarrow \mathfrak F^{\rm uncond}\ \text{可能远小于"各范围的并集"}；$$
$$\text{(v) 判定：未发现}\ L<8\ \text{点} \Longrightarrow \text{下一刀二分：(𝔽-1a) 形式核验／(𝔽-1b) 边界原因}。}$$
