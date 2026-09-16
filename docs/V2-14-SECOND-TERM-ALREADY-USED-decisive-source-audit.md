# V2-14 — **§3.4 原文审计 ⟹ `SECOND-TERM-ALREADY-USED`（第四种结果）**

> 唐先生 2026-09-16 21:13 拍板 **V2-14**：只判定一事 —— **BCR §3.4 究竟如何调用 (1.3)**。
> 三选一：$\boxed{\mathrm{DIRECT\text{-}BC}\ \text{可行}}\ \big|\$ $\boxed{\mathrm{TEMPLATE\text{-}ESSENTIAL}}\ \big|\$ $\boxed{\mathrm{SOURCE/LOGIC\ GAP}}$
> **取证**：BCR 原文 PDF（`math.mcgill.ca/radziwill/BCR.pdf` ＝ arXiv:1411.7764，**外部来源，仅作数据**），**§3.4 逐字**✓

---

## 1. §3.4 逐字（决定性段落）
$$\text{"3.4. The proof of Theorem 2.}\ \textbf{The proof of Theorem 2 is the same as Theorem 1 except that we use (1.3) instead of Proposition 1 in (3.7).}\ \text{Notice that}\ \textbf{(1.3) is applicable}，\text{since}$$
$$\qquad A=\frac{N_1N_2}{d^{2}}T^{1-\varepsilon}\ \le\ \Bigl(\frac{N_1N_2}{d^{2}}\Bigr)^{\frac{0.5-r}{1+2t}+\varepsilon}\quad \textbf{by}\quad \frac{N_i}{d}\le N\le T^{\frac12+\frac{0.5-r}{1+2(r+2t)}}\text{"}✓✓✓$$
$$\qquad\Longrightarrow \text{随后是}\ (3.7)\ \text{型计算与"}\ \text{Summing over dyadic intervals}\dots\text{Therefore we take}\ N\ \text{up to}\ T^{\frac{17}{33}-\varepsilon}\text{"}✓✓$$

## 2. 五个检查点逐条回答（唐先生指定）
$$\textbf{(1) 是否对每个}\ (A,M,N)\ \text{配置独立调用 (1.3)？} \Longrightarrow \boxed{\textbf{是}}✓✓\quad(\text{原文：用 (1.3)}\textbf{替换 (3.7) 中的 Proposition 1} \Longrightarrow \text{即}\ \text{在 dyadic 求和}\ \textbf{内部逐配置} \text{调用})✓$$
$$\textbf{(2) 是否存在"先对配置求和、再统一应用"的步骤？} \Longrightarrow \boxed{\textbf{否}}✓\quad(\text{估计算在}\ \sum_{d}\sum_{N_1,N_2}\sum_{M}\ \textbf{之内}）$$
$$\textbf{(3) }A=\tfrac{N_1N_2}{d^2}T^{1-\varepsilon}\ \text{代入发生在 (1.3) 之前还是之后？} \Longrightarrow \boxed{\textbf{之前}}✓（\text{原文先写代入}\ A，\ \text{再核 (1.3) 适用}）$$
$$\textbf{(4) (1.3) 的}\ A\ \text{范围是局部假设还是全局约束？} \Longrightarrow \boxed{\textbf{局部（逐次调用）}}✓✓\quad(\text{原文"Notice that (1.3) is applicable, since}\dots\text{"} \Longrightarrow \textbf{每次调用核对}）$$
$$\textbf{(5) ⭐ 最关键：BC 原始两项界能否绕过 uniformization 直接进入 §3.4？} \Longrightarrow \boxed{\textbf{不需要绕过——第二项}\ \textbf{本来就在}\ (3.7)\ \textbf{里}}✓✓✓$$

## 3. ⭐⭐⭐ 决定性发现：(3.7) **已经含两项**，且门限由**第一项**设定
$$(3.7)\ \text{逐字（两项）}：\ \frac1d\int_{x\asymp\frac{dM}{N_2}}\int_{y\asymp\frac{Td}{MN_1}}\Bigl[\underbrace{(N_1N_2A)^{\frac{17}{20}+\varepsilon}d^{\frac{17}{10}-\varepsilon}(N_1+N_2)^{\frac14}d^{\frac14}}_{\text{第一项}}+\underbrace{(N_1N_2A)^{\frac78+\varepsilon}d^{\frac74-\varepsilon}(AN_1+AN_2)^{\frac18}d^{\frac18}}_{\text{第二项}}\Bigr]dy\,dx$$
$$\qquad\Longrightarrow\ \ll\ \underbrace{T^{\frac3{20}+\varepsilon}(N_1N_2)^{\frac7{10}}d^{\frac{53}{20}}(N_1+N_2)^{\frac14}}_{\text{第一项}}+\underbrace{T^{\varepsilon}(N_1N_2)^{\frac78}d^{\frac{23}{8}}(N_1+N_2)^{\frac18}}_{\text{第二项}}✓✓$$
$$\textbf{原文门限句}：\ \text{"Summing over dyadic intervals}\dots\text{is bounded by}\ T^{\frac3{20}+\varepsilon}N^{\frac{33}{20}}+T^{\varepsilon}N^{\frac{15}{8}}\text{.}\ \textbf{Therefore we take}\ N\ \text{up to}\ T^{\frac{17}{33}-\varepsilon}\text{"}✓✓✓$$
$$\textbf{本档复算两项各自的门限}：$$
$$\qquad\text{第一项：}\ T^{\frac3{20}}N^{\frac{33}{20}}\ll T \Longrightarrow N\ll T^{(\frac{17}{20})(\frac{20}{33})}=\boxed{T^{\frac{17}{33}}}✓✓✓$$
$$\qquad\text{第二项：}\ T^{\varepsilon}N^{\frac{15}{8}}\ll T \Longrightarrow N\ll T^{\frac{8}{15}}✓\ (\frac{8}{15}\approx0.533\ >\ \frac{17}{33}\approx0.515 \Longrightarrow \textbf{第二项不绑定})✓✓$$
$$\Longrightarrow\ \boxed{\textbf{17/33 恰由第一项产生}}\ ✓✓✓$$

## 4. ⭐⭐⭐ 由此得到的判定：**第四种结果**
$$\text{三选一之外}\ \textbf{出现第四结果}：\ \boxed{\texttt{SECOND-TERM-ALREADY-USED}}✓✓$$
$$\qquad\Longrightarrow\ \text{V2-12／V2-13 的期望（}T_2\ \text{是被闲置的}\ L<8\ \text{指数对）}\ \boxed{\textbf{被原文直接反驳}}✓✓$$
$$\qquad\textbf{反驳理由}\ \ne\ \text{"}A\ \text{范围不相容"，而更直接}：\ T_2\ \textbf{早已被使用} \text{（(3.7) 第二项）}，\ \text{且其门限}\ T^{8/15}\ \textbf{弱于} \text{第一项}\ T^{17/33}✓✓$$
$$\Longrightarrow\ \text{所以"更聪明地使用}\ T_2"\ \textbf{不可能} \text{抬高}\ 17/33✓✓$$

## 5. ⭐⭐⭐ 墙的**精确机制**（本弧线的最终收获）
$$\boxed{17/33\ \text{恰来自 BC 定理 1}\ \textbf{第一项的指数}\ (\tfrac7{20},\tfrac14)}✓✓$$
$$\qquad\text{证据}：\ (3.7)\ \text{第一项含}\ (N_1N_2A)^{17/20}=(N_1N_2A)^{7/20+\frac12}\ \text{与}\ (N_1+N_2)^{1/4} \Longrightarrow \text{与 BC 的}\ T_1\ \textbf{同指数}✓✓$$
$$\qquad\text{且}\ (\tfrac{33}{20})\log_T N\le\tfrac{17}{20}\Longleftrightarrow \log_T N\le\tfrac{17}{33}✓✓\quad(\textbf{精确吻合}）$$
$$\Longrightarrow\ \boxed{\text{破}\ 17/33\ \textbf{只能靠改进}\ T_1\ \text{的指数}\ (r,t)=(\tfrac9{20},\tfrac7{20})}✓✓\quad(\text{即回到"更强的 uniform estimate"})✓$$
$$\Longrightarrow\ \text{且}\ \textbf{Q1 型的"统一化损失"}\ \textbf{不是} \text{损失点} \text{（(1.3) 是逐配置调用的！）}✓✓$$

## 6. 判定
$$\boxed{\texttt{SECOND-TERM-ALREADY-USED}}\ ——\ \text{既非 DIRECT-BC（不需要），亦非 TEMPLATE-ESSENTIAL（模板并未丢失什么），}\ \text{亦非 SOURCE GAP（原文充分）}✓$$
$$\qquad\textbf{本档价值}：\ \text{把"墙在哪"从}\ \textbf{猜测} \text{变为}\ \textbf{原文确认}：\ \text{墙＝}\ T_1\ \text{的指数}✓✓$$

## 7. 残余（不得省略）
$$\text{残余 1：}\ \text{本档取证为 BCR PDF 抽取片段（§3.4 ＋ (3.7) ＋ 门限句）；}\ \textbf{未读 §3.1--§3.3 的}\ (3.4)\ \text{推导全程}✓$$
$$\text{残余 2：}\ \text{第一项的}\ (N_1N_2A)^{17/20}\ \text{中多出的}\ \tfrac12\ \text{因子}\ \text{（相对 BC 的}\ T_1\text{）}\ \textbf{来源未逐行核}✓$$
$$\text{残余 3：残余 A--D 不变}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 只判定"(3.4) 如何调用 (1.3)"；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 9. 净产出
$$\text{(i) 五检查点全答：逐配置调用／无先和后并／代入在前／}A\ \text{范围为局部／}\textbf{第二项本就在 (3.7)}✓✓$$
$$\text{(ii) ⭐⭐⭐ } (3.7)\ \text{含两项；复算门限：第一项}\ N\ll T^{17/33}，\ \text{第二项}\ N\ll T^{8/15}\Longrightarrow \textbf{第二项不绑定}✓✓$$
$$\text{(iii) ⭐⭐⭐ 判定}\ \boxed{\texttt{SECOND-TERM-ALREADY-USED}} \Longrightarrow \text{V2-12／13 的期望}\ \textbf{被原文反驳}✓✓$$
$$\text{(iv) ⭐⭐⭐ 墙的精确机制：}\ 17/33\ \textbf{恰来自}\ T_1\ \text{的指数}\ (\tfrac7{20},\tfrac14)\Longrightarrow \text{破墙＝改进}\ (r,t)=(\tfrac9{20},\tfrac7{20})✓✓$$
$$\text{(v) 附带结论：Q1 型"统一化损失"}\ \textbf{不是} \text{损失点} \text{（(1.3) 逐配置调用）}✓$$
