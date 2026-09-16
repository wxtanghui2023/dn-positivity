# V2-1 — **审计 $\mathfrak F_{\rm uncond}$ 的下边界**

> 唐先生 2026-09-16 20:23 拍板：**V2-1**（不预设"证明 $\ge8$"；先让 $\mathfrak F_{\rm uncond}$ 自己决定）。
> 三档（唐先生）：$$\textbf{V2-A}\ \exists(r,t)\in\mathfrak F_{\rm uncond}:17r+t<8\ \big|\ \textbf{V2-B}\ \inf=8\ \big|\ \textbf{V2-C}\ \text{目前无法确定}$$
> **警告（唐先生，采纳）**：BC 点给出 $L=8$ 只证明 $\inf L\le8$，$\textbf{绝不能} \text{反证} \inf L\ge8$✓

---

## 1. $\mathfrak F_{\rm uncond}$ 的已映射点（据既有资料）
$$\text{DFI}\ (\text{双线性},\ 1997\ \text{Inventiones})：\ (r,t)=(\tfrac{23}{48},\tfrac12)\Longrightarrow L=17r+t=\tfrac{415}{48}\approx8.646$$
$$\text{Bettin--Chandee}\ (\text{三线性},\ 2018\ \text{Adv.\ Math})：\ (r,t)=(\tfrac9{20},\tfrac7{20})\Longrightarrow L=\mathbf{8.000}\ (\textbf{恰在边界})✓$$
$$\text{2026 KF I／II：}\ \textbf{情形受限}（\text{subdyadic／partial moduli}）\Longrightarrow \textbf{不产生统一}\ (r,t)\ \text{点（猎-6 判定 C）}✓$$
$$\Longrightarrow\ \text{目前}\ \textbf{已映射点仅两个}；\ \inf L\le8\ \text{（由 BC 点）}✓$$

## 2. ⭐ 与文献"节省"结构的对应（本档新识别）
$$\text{文献以"平衡情形节省}\ s\ \text{"表述}：\ \text{DFI}\ s=\tfrac1{48}；\ \text{BC}\ s=\tfrac1{20}\ ✓$$
$$\Longrightarrow\ \text{两点均满足}\ \boxed{r=\tfrac12-s}\：\ \tfrac12-\tfrac1{48}=\tfrac{23}{48}✓；\ \tfrac12-\tfrac1{20}=\tfrac9{20}✓✓\ (\textbf{两点吻合})$$
$$\text{BC 另有}\ t=\tfrac12-3s\：\ \tfrac12-\tfrac3{20}=\tfrac7{20}✓\ (\text{DFI 不符：其}\ t=\tfrac12，\text{且 DFI 为双线性})$$
$$\Longrightarrow\ \text{在 BC 线上}：\ L=17\bigl(\tfrac12-s\bigr)+\bigl(\tfrac12-3s\bigr)=9-20s \Longrightarrow \boxed{L<8\iff s>\tfrac1{20}}✓✓✓$$
$$\textbf{自校验}：s=\tfrac1{20}\Longrightarrow L=9-1=8 ✓✓\ (\text{与}\ (9/20,7/20)\ \text{一致})$$
$$\Longrightarrow\ \boxed{\text{破墙条件在 BC 线上等价于：}\textbf{平衡情形节省}\ s>\tfrac1{20}}✓✓\quad(\textbf{一个单数条件})$$

## 3. 判定（本档诚实落点）
$$\textbf{V2-A}：\ \textbf{未得} \text{——无任何已知无条件统一估计给出}\ s>\tfrac1{20}\ (\text{即}\ L<8)✓$$
$$\textbf{V2-B}：\ \textbf{未证} \text{——要证}\ \inf=8\ \text{须证明}\ s\le\tfrac1{20}\ \text{对所有（含未发表）证明成立} \Longrightarrow \textbf{远超本档}✓$$
$$\textbf{V2-C}：\ \boxed{\textbf{本档落在 C}}\：\ \text{已知点显示}\ \inf\le8；\ \text{下界}\ \textbf{无法确定}✓$$
$$\qquad\textbf{但本档给出可证伪的替代形式（§2）}：\ \text{问题}\ \textbf{不再是抽象的}\ \inf(17r+t)，\ \text{而是}\ \boxed{s\le\tfrac1{20}\ \text{是否为该估计体系的结构上限}}✓$$

## 4. 由此得到"究竟什么阻止 $17r+t<8$"的候选答案（待证）
$$\text{候选（本档}\ \textbf{[结构判定]}）：\ \text{阻止项}\ \textbf{不是} \text{某个未知约束，而是}\ \text{三线性 Kloosterman 估计的}\ \textbf{已知证明结构}：$$
$$\qquad\text{DFI／BC 的节省来自}\ \text{同一类方法}（\text{reciprocity／Kloosterman 平均／谱型输入}） \Longrightarrow \text{其节省被}\ \textbf{方法本身} \text{限制在}\ s\le\tfrac1{20}\ \text{附近}✓$$
$$\qquad\text{而 2026 年的改进}\ \textbf{只在子情形} \text{生效} \Longrightarrow \text{提示：}\ s>\tfrac1{20}\ \text{需要}\ \textbf{新机制}，\ \text{而非}\ \text{现有机制的常数优化}✓$$
$$\qquad\Longrightarrow\ \text{这与猎-6 的判定 C}\ \textbf{相互印证}✓$$

## 5. 残余（不得省略）
$$\text{残余 1：§1 的两点映射来自}\ \textbf{唐先生提供的引文与检索片段}，\ \textbf{本档未逐篇核验}✓$$
$$\text{残余 2：§2 的}\ r=\tfrac12-s\ \text{为}\ \textbf{两点观察}，\ \textbf{非} \text{已证定律；}\ t=\tfrac12-3s\ \textbf{仅 BC 成立}✓$$
$$\text{残余 3：残余 A--D（跨轮结转）不变；}\ \text{其中残余 B（BCR 配置是否落入 2026 子情形）}\ \textbf{直接决定此处}\ s\ \text{能否被抬高}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① }\textbf{不预设} \text{"证明}\ \ge8\text{"；}\ \text{② }\textbf{未用 RH}；\text{零数值（仅分数演算）}✓$$

## 7. 净产出
$$\text{(i) }\mathfrak F_{\rm uncond}\ \text{已映射点仅两个（DFI}\ L\approx8.646；\text{BC}\ L=8）；2026 改进为情形受限} \Longrightarrow \inf L\le8✓$$
$$\text{(ii) ⭐ 与节省}\ s\ \text{的对应}：\ r=\tfrac12-s\ \text{两点吻合；BC 线上}\ L=9-20s \Longrightarrow \boxed{L<8\iff s>\tfrac1{20}}✓✓$$
$$\text{(iii) 判定}\ \textbf{V2-C}（\text{下界无法确定}）\ \text{＋可证伪替代形式：}s\le\tfrac1{20}\ \text{是否为结构上限}✓$$
$$\text{(iv) 候选答案：阻止项＝}\textbf{估计方法本身}（同一类机制封顶}\ s\approx\tfrac1{20}\text{），与猎-6 判定 C 印证}✓$$
$$\text{(v) V1-1 措辞已按唐先生收紧（"§3.4 模型中"）✓}$$
