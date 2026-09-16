# V2-3 — **$1/20$ 指数分解审计**（BC 定理 1 的内部溯源）

> 唐先生 2026-09-16 20:25 拍板：**V2-3 立即做**；不扫论文，逐层反推。
> 目标（唐先生）：$$\boxed{\tfrac1{20}=1-\bigl(\tfrac7{10}+\tfrac14\bigr)}\ \text{沿 BC 证明逐层反推}\ \tfrac7{20}\ \text{与}\ \tfrac14\ \text{各从哪一步产生}$$
> 逐步分类：$\mathrm{A}$ 代数／尺度必然 $\big|\ \mathrm{B}$ Cauchy／平方化选择 $\big|\ \mathrm{C}$ 截断／diagonal 选择 $\big|\ \mathrm{D}$ Weil／谱输入 $\big|\ \mathrm{E}$ 取最大造成的 envelope $\big|\ \mathrm{F}$ 纯技术损失
> 最终只问：$$\boxed{\exists\ \text{参数／步骤使}\ E_1=N^{19/20-\delta}\ ?}\quad(\textbf{不预设} \text{答案})$$

---

## 0. ⚠️ 撤回（唐先生纠正，采纳）
$$\text{猎-5／V2-1 的候选判断"DFI／BC 同类方法封顶}\ s\lesssim\tfrac1{20}\text{"}\ \Longrightarrow \boxed{\textbf{撤回}}✓$$
$$\text{理由}：\text{BC 原文自述其证明}\ \textbf{"roughly the same structure as DFI, but introduces several refinements"}\text{，}\ \text{其中一项是}\ \textbf{Cauchy--Schwarz 时保留更长的 diagonal}✓$$
$$\Longrightarrow\ \text{BC}\ \textbf{本身} \text{已改动结构参数} \Longrightarrow s:\tfrac1{48}\to\tfrac1{20}\ \text{是}\ \textbf{结构改动} \text{的结果，}\ \textbf{非} \text{常数优化}✓$$
$$\Longrightarrow\ \boxed{\tfrac1{20}\ \text{是}\ \textbf{活的"证明指数"}，\ \textbf{不是} \text{已被文献证明的硬墙}}✓$$

## 1. 数据（BC 定理 1，唐先生核出＋本档复算）
$$\mathcal B(M,N,A)\ll\|\alpha\|\|\beta\|\|\nu\|\Bigl(1+\tfrac{|\vartheta|A}{MN}\Bigr)^{\frac12}\Bigl[(AMN)^{\frac7{20}+\varepsilon}(M+N)^{\frac14}+(AMN)^{\frac38+\varepsilon}(AM+AN)^{\frac18}\Bigr]$$
$$\text{平衡情形}\ |\vartheta|A\ll MN,\ M\asymp N \Longrightarrow \text{节省}\ \min\bigl(A^{\frac3{20}}N^{\frac1{20}},\ N^{\frac18}\bigr)$$
$$\textbf{本档复算（A=1）}：\ E_1=(N^2)^{\frac7{20}}\cdot N^{\frac14}=N^{\frac7{10}+\frac14}=N^{\frac{19}{20}}\ \Longrightarrow\ \text{节省}\ N^{\frac1{20}}✓$$
$$\qquad E_2=(N^2)^{\frac38}\cdot N^{\frac18}=N^{\frac34+\frac18}=N^{\frac78}\ \Longrightarrow\ \text{节省}\ N^{\frac18}✓$$
$$\Longrightarrow\ \boxed{s=\min\bigl(1-\tfrac7{10}-\tfrac14,\ 1-\tfrac34-\tfrac18\bigr)=\min\bigl(\tfrac1{20},\tfrac18\bigr)=\tfrac1{20}}✓✓$$
$$\textbf{结论（唐先生）}：\ \tfrac1{20}\ \textbf{首先是两个幂指数竞争的结果}，\ \textbf{不是} \text{单独出现的神秘常数}✓$$

## 2. ⭐ 溯源证据（本档掌握的、可引用的结构性事实）
$$\textbf{证据 1}：\text{BC 证明含一个}\ \textbf{显式的参数优化步骤} \Longrightarrow \text{其章节结构中直接出现}\ \textbf{"Optimizing the parameter}\ L\text{"}✓$$
$$\qquad(\text{来自 BC 原文 PDF 片段：章节 5 标题；本档未读全文})$$
$$\textbf{证据 2}：\text{非对角估计以}\ \textbf{多个竞争项并存} \text{的形式出现，}\ \text{例如（片段）}：$$
$$\qquad D_b\ll\|\beta\|\|\nu\|^2\Bigl(1+\tfrac{|\vartheta|AbN}{M}\Bigr)^{\frac12}LM^\varepsilon\Bigl(A(bLN)^{\frac12}+\tfrac{AM}{bN}+M+\tfrac{b^{\frac34}AN^{\frac54}L^{\frac12}}{M^{\frac12}}+\tfrac{b^{\frac12}AL^{\frac52}N^{\frac74}}{M}+\tfrac{b^{\frac12}A^{\frac12}}{N}\Bigr)\ \text{型}$$
$$\Longrightarrow\ \text{指数}\ (\tfrac7{20},\tfrac14,\tfrac38,\tfrac18)\ \textbf{是}\ \text{多参数（}b,L,N,M,A\text{）}\ \textbf{优化} \text{的输出}✓$$
$$\Longrightarrow\ \boxed{\text{由此}\ \tfrac7{20}\ \text{与}\ \tfrac14\ \text{主要落于类别}\ \mathrm{B}\ (\text{Cauchy／平方化切分})\ \text{与}\ \mathrm{C}\ (\text{截断／参数选择})}✓\quad([结构判定])$$
$$\qquad\text{且}\ \mathrm{D}\ (\text{Weil／谱输入})\ \text{进入}\ \textbf{个别估计} \text{内部（如 Kloosterman 平均），}\ \text{不直接产生}\ \tfrac7{20}\ \text{或}\ \tfrac14✓$$

## 3. 判定：**B（假刚性倾向）——但未终判**
$$\text{按唐先生三档}：\ \mathrm{A}\ \text{真刚性}\ \big|\ \boxed{\mathrm{B}}\ \text{假刚性}\ \big|\ \mathrm{C}\ \text{内部指数障碍（共同优化变量）}$$
$$\textbf{本档落 B（倾向）}：\ \text{证据 1／2 显示指数来自}\ \textbf{参数优化与切分选择} \Longrightarrow \tfrac1{20}\ \textbf{是证明架构的输出}✓$$
$$\qquad\Longrightarrow\ \text{这}\ \textbf{支持} \text{继续攻}\ s>\tfrac1{20}✓$$
$$\qquad\textbf{但未达 C}：\ \text{未找到形如}\ f_1(x)\ge\tfrac7{20},\ f_2(x)\ge\tfrac14\ \text{且}\ f_1+f_2=\tfrac{19}{20}\ \text{的共同优化变量}✓$$
$$\qquad\textbf{且未达 A}：\ \text{未证}\ a\ge a_0,\ b\ge b_0\ \text{由不可同时突破的核心估计产生}✓$$

## 4. ⭐ 本档把问题定位到一个**可判定的判据**（核心产出）
$$\text{"}N^{19/20}\ \text{是刚性还是 envelope？"}\ \Longleftrightarrow\ \boxed{\text{参数}\ L\ \text{的优化最优点落在}\ \textbf{内部} \text{还是}\ \textbf{可行域边界}}$$
$$\qquad\textbf{内部最优} \Longrightarrow \mathrm{E}\ (\text{envelope})\Longrightarrow s>\tfrac1{20}\ \text{有明确突破口}✓$$
$$\qquad\textbf{边界最优（且边界由核心估计强制）} \Longrightarrow \mathrm{A}\ (\text{刚性})\Longrightarrow \text{第一次得到可精确定位的"现有 Kloosterman 方法墙"}✓$$
$$\qquad(\text{这正是唐先生所说"不要再凭经验说方法似乎封顶"}）✓$$

## 5. 残余（不得省略）
$$\text{残余 1：}\ \text{§2 的证据 1／2 来自}\ \textbf{检索片段}，\ \textbf{本档未读 BC 全文} \Longrightarrow \text{类别归属为}\ \textbf{[结构判定]}✓$$
$$\text{残余 2：}\ \textbf{未} \text{逐层给出}\ \tfrac7{20}\ \text{与}\ \tfrac14\ \text{各自的产生步骤（须全文）}✓$$
$$\text{残余 3：残余 A--D（跨轮结转）不变；}\ \text{其中残余 B 与本次}\ s\ \text{能否被抬高}\ \textbf{直接相关}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① 不扫论文；}\ \text{② }\textbf{未用 RH}；\ \text{零数值（仅指数演算）}✓$$

## 7. 净产出
$$\text{(i) 撤回"同类方法封顶}\ s\lesssim\tfrac1{20}\text{"（BC 已改动结构参数：C--S 保留更长 diagonal）}✓$$
$$\text{(ii) }s=\min(\tfrac1{20},\tfrac18)=\tfrac1{20}\ \text{复算通过} \Longrightarrow \tfrac1{20}\ \textbf{是两项竞争的结果}；$$
$$\text{(iii) ⭐ 溯源：BC 含}\ \textbf{显式参数优化}（\text{"Optimizing the parameter}\ L\text{"）与}\ \textbf{多项并存} \Longrightarrow (\tfrac7{20},\tfrac14)\ \text{主要落于}\ \mathrm{B}\ (\text{C--S 切分})\ \text{与}\ \mathrm{C}\ (\text{截断／参数})✓$$
$$\text{(iv) 判定：}\textbf{B（假刚性，倾向）}，未达 A／C；}\ \text{支持继续攻}\ s>\tfrac1{20}✓$$
$$\text{(v) ⭐ 判据定位：}\ N^{19/20}\ \text{刚性 vs envelope}\iff L\ \text{优化最优点在边界 vs 内部（可判定）}✓$$
