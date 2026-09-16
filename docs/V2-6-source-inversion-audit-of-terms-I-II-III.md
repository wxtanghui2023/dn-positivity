# V2-6 — **三项来源逐项反演审计**

> 唐先生 2026-09-16 20:28 拍板：**先 V2-6，再 V2-5**（避免"凭一个看起来最有希望的项就开始优化"）。
> **两处修正（唐先生，采纳）**：
> $$\textbf{(1)}\ \boxed{\text{"满足平衡方程"}\ne\text{"已证明是全局内部最优点"}} \Longrightarrow \text{当前状态应写为}\ \boxed{\mathrm{E1\text{-}strong}\ \textbf{尚未完全闭合}；\ \mathrm{E1\text{-}preliminary}\ \textbf{已成立}}✓$$
> $$\textbf{(2)}\ \boxed{\text{单项改善}\ne\text{抬高}\ s}\：\ \text{真正的突破判据是}\ \inf_{L\in\mathcal L}\max(F_1,F_2,F_3)\le N^{\frac{19}{20}-\delta+o(1)}，\ \textbf{而非} \text{单项变小}✓$$
> 四档：$\mathrm{D1}$ 技术 envelope 可重新优化 $\big|\ \mathrm{D2}$ 改善 II 后他项接管 $\big|\ \mathrm{D3}$ 某项含核心不可突破估计 $\big|\ \mathrm{D4}$ 三项来自同一底层约束（＝C 型耦合）✓

---

## 1. 待反演的三项（原文 §5 平衡条件右端）
$$\mathrm{(I)}\ \frac{AM^{2}}{bLN}\qquad\mathrm{(II)}\ \frac{M^{2}}{L}\qquad\mathrm{(III)}\ \frac{b^{\frac12}A^{\frac12}MN}{L}$$
$$\text{目标链（唐先生指定）}：\ \text{原始和}\to\text{Cauchy--Schwarz}\to\text{平方化}\to\text{diagonal／off-diagonal}\to\text{Kloosterman 估计}\to\mathrm{(I),(II),(III)}✓$$

## 2. 已掌握的两个结构指纹（本档，据已取证的片段）
$$\textbf{指纹 A（参数指纹）}：\ \mathrm{(I)}\ \text{含}\ b\ (\text{人工参数});\ \mathrm{(III)}\ \text{含}\ b^{\frac12}A^{\frac12}；\ \text{而}\ \mathrm{(II)}\ \textbf{不含}\ b\ \text{与}\ A$$
$$\qquad\Longrightarrow\ \mathrm{(I)}\ \text{来自}\ \textbf{含}\ b\ \text{的 C--S／平方化步骤}；\ \mathrm{(II)}\ \text{来自}\ \textbf{不含人工参数} \text{的步骤（对角型候选）}✓\quad([结构判定])$$
$$\textbf{指纹 B（}\ A^{\frac12}\ \text{＝Weil 指纹）}：\ \mathrm{(III)}\ \text{中的}\ A^{\frac12}\ \text{与}\ (4.33)\ \text{末项}\ \frac{N^{1/4}}{A^{1/2}}\ \text{同源} \Longrightarrow \text{与}\ \textbf{单个 Weil 界}\ S(a,b;c)\ll c^{\frac12+\varepsilon}\ \text{同形}✓$$
$$\qquad\Longrightarrow\ \boxed{\mathrm{(III)}\ \text{是}\ \textbf{深层输入（Kloosterman／谱）} \text{所在之处}}✓\quad([结构判定])$$

## 3. ⭐ 由指纹 B 得到的战略判读（本档新产出）
$$\mathrm{(III)}\ \text{携带}\ A^{1/2}\ \text{型（单点 Weil）签名} \Longrightarrow \text{其}\ \textbf{单点形式} \text{不可改进（Weil 界是sharp的）}✓$$
$$\qquad\textbf{但}：\ \text{单点和} \text{的}\ \textbf{平均} \text{可优于 Weil 界（Deshouillers--Iwaniec／Kuznetsov 型平均）}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{改善}\ \mathrm{(III)}\ \text{的机制}\ne\text{"找更强的单点界"}，\ \text{而是}\ \textbf{"用平均替代单点"}}✓\ (\text{这正是 BC 相对 DFI 的成功机制})✓$$
$$\textbf{反向判读}：\ \mathrm{(I)}\ \text{含}\ b\ \text{与}\ L \Longrightarrow \text{很可能是}\ \textbf{技术 envelope}\ (\mathrm{D1}\ \text{型})；\ \mathrm{(II)}\ \text{不含参数} \Longrightarrow \textbf{对角主项候选}\ (\mathrm{D2}\ \text{型风险：改善后他项接管})✓$$

## 4. 判定：**本档未闭合（D1--D4 无法确定）**
$$\text{理由}：\ \text{反演}\ \mathrm{(I),(II),(III)}\ \text{的}\ \textbf{各自来源} \text{须读 §4 的}\ \textbf{完整链}（4.1--4.33），\ \text{本档仅持有}\ (4.33)\ \text{与 §5}\ \text{的片段}✓$$
$$\qquad\Longrightarrow\ \boxed{\text{本档}\ \textbf{不落}\ \mathrm{D1}\ \text{--}\mathrm{D4}\ \text{中任何一档}} \Longrightarrow \text{登记为}\ \textbf{待读 §4 的决定性项}✓$$
$$\textbf{但取得两项指纹（§2）与一项战略判读（§3）} \Longrightarrow \text{可显著缩短下次读证范围}：$$
$$\qquad\rightarrow\ \text{重点读 §4 中}\ \textbf{产生}\ \mathrm{(II)}\ \text{的步骤}（\text{是否与"保留更长 diagonal"同源}）\ \text{与}\ \textbf{产生}\ \mathrm{(III)}\ \text{的步骤}（\text{Weil 单点 vs 平均}）✓$$

## 5. 对 V2-4 的精确化（采纳唐先生修正）
$$\boxed{\mathrm{E1\text{-}preliminary}}：\ L^{*}\ \text{满足一个}\ \textbf{平衡方程}（\text{原文"We wish to choose}\ L\ \text{so that"）}✓\ \textbf{成立}$$
$$\boxed{\mathrm{E1\text{-}strong}}：\ \text{须再知}\ (1)\ F(L)\ \text{的来源}；\ (2)\ F\ \text{对}\ L\ \text{的单调／凸性}；\ (3)\ L^{*}\ \text{使所有前置条件同时成立}；\ (4)\ L^{*}\ge2\log(b\vartheta M)\ \text{在实际参数域成立}；\ (5)\ L^{*}\ \text{代回后哪一项产生}\ \tfrac{19}{20} \Longrightarrow \textbf{尚未闭合}✓$$
$$\textbf{故突破判据的正确形式（唐先生）}：\ \boxed{\exists\delta>0:\ \inf_{L}\max(F_1,F_2,F_3)\le N^{\frac{19}{20}-\delta+o(1)}}✓$$

## 6. 残余（不得省略）
$$\text{残余 1：反演须 §4 全文；}\ \text{本档仅凭}\ (4.33)\ \text{与 §5 片段} \Longrightarrow \text{§2 的两指纹为}\ \textbf{[结构判定]}✓$$
$$\text{残余 2：}\ A^{1/2}\ \text{＝Weil 指纹的判断为}\ \textbf{同形推断}，\ \textbf{未} \text{核 §4 的实际推导}✓$$
$$\text{残余 3：残余 A--D（跨轮结转）不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只做 V2-6，}\textbf{不} \text{攻}\ \mathrm{(II)}；\quad\text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) 采纳两处修正：}\mathrm{E1\text{-}preliminary}\ \text{成立／}\mathrm{E1\text{-}strong}\ \text{未闭合；}\ \text{突破判据改为}\ \inf_L\max(F_1,F_2,F_3)\le N^{19/20-\delta}✓$$
$$\text{(ii) 指纹 A：}\mathrm{(I)}\ \text{含}\ b\ (\text{C--S／平方化来源})；\ \mathrm{(II)}\ \textbf{不含参数}（\text{对角主项候选}）；\ \mathrm{(III)}\ \text{含}\ b^{1/2}A^{1/2}✓$$
$$\text{(iii) ⭐ 指纹 B ＋ 战略判读：}\mathrm{(III)}\ \text{携带}\ A^{1/2}\ \text{＝单点 Weil 签名} \Longrightarrow \text{其改善机制}\ne\text{更强单点界}，\ \text{而是}\ \textbf{用平均替代单点}✓$$
$$\text{(iv) 判定：}\textbf{本档不落 D1--D4} \Longrightarrow \text{登记为待读 §4 的决定性项（已缩小读证范围）}✓$$
$$\text{(v) 对 V2-4 的精确化：}\ \mathrm{E1}\ \text{拆为 preliminary／strong 两档}✓$$
