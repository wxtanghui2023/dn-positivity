# V2-4 — **参数 $L$ 的最优点位置审计** ⟹ 判定 **E1**（内部最优 ⟹ 当前 envelope）

> 唐先生 2026-09-16 20:26 拍板 **V2-4**；要求把"结构判定"升级为**逐行证明审计**。
> **逻辑纠正（唐先生，采纳）**："边界最优"$\not\Rightarrow$"刚性"；只有证明**该边界来自不可突破的核心估计**才升级为刚性 ✓
> 本档取证：BC 原文 arXiv HTML（`arXiv:1502.00769v1`，**外部来源，仅作数据**）的 **§5 "Optimizing the parameter $L$"** 关键段与 (4.33)✓

---

## 1. 取证（逐字，原文 §5）
$$\textbf{平衡条件（原文）}：\ \text{"We wish to choose}\ L\ \text{so that"}$$
$$\qquad\boxed{\ b^{\frac12}AL^{\frac32}N^{\frac74}\ \approx\ \frac{AM^{2}}{bLN}+\frac{M^{2}}{L}+\frac{b^{\frac12}A^{\frac12}MN}{L}\ }$$
$$\qquad\text{且}\ \boxed{L\ \ge\ 2\log(b\vartheta M)}\quad(\textbf{唯一显式约束})✓$$
$$\textbf{原文给出的取值}：\ L=\frac{M^{\frac45}}{b^{\frac35}N^{\frac{11}{10}}}+\frac{M^{\frac45}}{b^{\frac15}A^{\frac25}N^{\frac7{10}}}+\frac{M^{\frac25}}{A^{\frac15}N^{\frac3{10}}}+M^{\varepsilon}$$
$$\qquad\Longrightarrow\ L\ \textbf{是三项单项式之和}（\text{各对应右端一项}）✓✓$$
$$\textbf{非对角界（4.33）}：\ \mathscr O_b\ll\|\beta\|^2\|\nu\|^2\Bigl(b+\frac{|\vartheta|A}{NM}\Bigr)^{\frac12}ALN^{\frac34}M^\varepsilon\Bigl(\frac{b^{\frac14}N^{\frac12}L^{\frac12}}{M^{\frac12}}+\frac{L^{\frac52}N}{M}+\frac{N^{\frac14}}{A^{\frac12}}\Bigr)$$
$$\text{随后："Combining (2.3) with the bounds for the diagonal (3.2) and off-diagonal terms (4.33) we obtain}\dots\text{"}\ \Longrightarrow\ \text{最终}\ (7/20,1/4)\ \text{型指数产生于此合并之后}✓$$

## 2. ⭐ 判定：**E1（内部最优点 ⟹ 当前 envelope）**
$$\textbf{依据 1（内部性）}：\ L^{*}\ \text{由}\ \textbf{平衡方程} \text{给出}（\text{左端＝右端三项之和}）\Longrightarrow \text{这是}\ \textbf{内部临界点}，\ \textbf{非} \text{被约束钉住}✓✓$$
$$\textbf{依据 2（唯一约束为技术性下界）}：\ L\ge 2\log(b\vartheta M)\ \text{是}\ \textbf{对数级下界}；\ \text{而}\ L^{*}\ \text{是}\ M,N,A,b\ \text{的}\ \textbf{单项式之和}$$
$$\qquad\Longrightarrow\ \text{在相关区域（}M,N,A\ \text{不退化）}，\ L^{*}\ \textbf{远大于} 2\log(b\vartheta M) \Longrightarrow \textbf{该约束松弛}✓✓$$
$$\Longrightarrow\ \boxed{\text{故}\ L^{*}\ \textbf{落在可行域内部}，\ \text{指数}\ (\tfrac7{20},\tfrac14)\ \text{是}\ \textbf{平衡优化的 envelope 输出}}✓✓$$
$$\textbf{四档（唐先生版）}：\ \boxed{\mathrm{E1}}\ \text{内部最优}\ \big|\ \mathrm{E2}\ \text{技术性边界}\ \big|\ \mathrm{E3}\ \text{核心估计边界（未证不可突破）}\ \big|\ \mathrm{E4}\ \text{可证不可突破}\Longrightarrow \textbf{本档落 E1}✓$$

## 3. B 判定的升级（结构判定 ⟶ 逐行读证）
$$\text{猎-V2-3 的 B（假刚性倾向）}\ \textbf{升级}：\ \text{由}\ \textbf{§5 原文逐字} \text{支撑：}$$
$$\qquad\boxed{\text{指数来自}\ \textbf{三项平衡} \text{（内部最优）}，\ \textbf{不是} \text{被强制边界钉住}}✓✓$$
$$\Longrightarrow\ s>\tfrac1{20}\ \text{的突破口}\ \textbf{被具体定位}：\ \text{改善}\ \textbf{右端三项之一} \text{（各对应 §4 的一个子估计）}✓$$
$$\qquad\text{而}\ L^{*}\ \text{的三项单项式，正对应右端三项}\ \Bigl(\tfrac{AM^2}{bLN},\ \tfrac{M^2}{L},\ \tfrac{b^{1/2}A^{1/2}MN}{L}\Bigr) \Longrightarrow \textbf{每项对应一个可独立攻击的目标}✓✓$$

## 4. 由此得到的具体突破口（本档新产出，供下一刀）
$$\textbf{突破口 1}：\ \text{右端第一项}\ \frac{AM^2}{bLN}\ ——\ \text{若该项能被更优估计替代，}\ L^{*}\ \text{的构造即改变}✓$$
$$\textbf{突破口 2}：\ \text{右端第二项}\ \frac{M^2}{L}\（\text{对角型}）\ ——\ \text{与 BC 自述的"保留更长 diagonal" refinements 同源}✓$$
$$\textbf{突破口 3}：\ \text{右端第三项}\ \frac{b^{1/2}A^{1/2}MN}{L}\（\text{谱／Weil 型输入所在}）✓$$
$$\Longrightarrow\ \text{三者}\ \textbf{并非同一机制} \Longrightarrow \text{按唐先生分档，}\ \text{本档}\ \textbf{未达 C}（\text{尚未找到}\ f_1+f_2=\tfrac{19}{20}\ \text{的共同变量耦合）}✓$$

## 5. 残余（不得省略）
$$\text{残余 1：本档取证为}\ \textbf{arXiv HTML 片段}（\text{§5 平衡条件＋}L^{*}\ \text{式＋(4.33)}），\ \textbf{未读 §4 完整链} \Longrightarrow \text{右端三项的}\ \textbf{各自来源} \text{未逐行定位}✓$$
$$\text{残余 2：}\ \text{"}L^{*}\gg2\log(b\vartheta M)\text{"}\ \text{为}\ \textbf{量级判断}（\text{未做退化区域边界讨论}）✓$$
$$\text{残余 3：残余 A--D（跨轮结转）不变}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① 只做 V2-4，}\textbf{不扩展搜索空间}；\ \text{② 取证为外部来源，仅作数据}；$$
$$\text{③ }\textbf{未用 RH}；\ \text{零数值（仅指数与量级演算）}✓$$

## 7. 净产出
$$\text{(i) 逐字取证：§5 的}\ \textbf{平衡条件}、\ L^{*}\ \text{的三项单项式形式、}\ \textbf{唯一约束}\ L\ge2\log(b\vartheta M)、\ (4.33)✓$$
$$\text{(ii) ⭐ 判定}\ \textbf{E1}：\ L^{*}\ \text{由平衡方程给出（内部临界点），}\ \text{且唯一约束为对数级下界（松弛）} \Longrightarrow \textbf{内部最优}✓✓$$
$$\text{(iii) B 判定升级：指数＝}\textbf{三项平衡的 envelope 输出}（\text{§5 原文逐字支撑）}⟹ \text{非强制边界}✓$$
$$\text{(iv) 突破口定位：右端三项各对应一个可独立攻击的子估计（对角型／谱型／}\tfrac{AM^2}{bLN}\text{型}）✓$$
$$\text{(v) 未达 C：（未找到共同变量耦合）；残余：§4 完整链未读}✓$$
