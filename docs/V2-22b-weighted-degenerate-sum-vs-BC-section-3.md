# V2-22 ＋ V2-22b — **$M$ vs $A$ 排除；加权退化求和 vs §3 的 $LM^{1+\varepsilon}$**

> 唐先生 2026-09-16 21:32：**V2-22 不收口，继续 V2-22b**✓
> **关键校正（采纳）**：不能只比字面大小，必须保持 **BC 的 $A,M,N$** 与 **BCR §3.4 代入 BC 定理时的 $A,M,N_i,d$** 的角色对应✓
> 判据升级：$\boxed{M\asymp A?}$ $\Longrightarrow$ $\boxed{\text{退化参数化后的}\ \textbf{实际加权贡献}\ \stackrel{?}{\le}\ \text{BC §3 的}\ LM^{1+\varepsilon}}$

---

## 1. ✓ 唐先生校正成立：$M\asymp A$ **不是** BCR 的自然关系
$$\text{§3.4 逐字}：A_{\rm BC}=\frac{N_1N_2}{d^2T^{1-\varepsilon}}✓\qquad \frac{N_i}{d}\le N\le T^{\frac12+\frac{0.5-r}{1+2(r+2t)}}✓\qquad M\ll T^{\frac12+\varepsilon}\sqrt{\frac{N_2}{N_1}}✓$$
$$\text{对称情形}\ N_1\asymp N_2\asymp N_0：\ A_{\rm BC}\asymp\frac{N_0^2}{d^2T},\quad M\ll T^{\frac12+\varepsilon}\Longrightarrow \frac{M_{\max}}{A_{\rm BC}}\asymp\frac{T^{3/2}}{N_0^2}✓$$
$$\text{临界尺度}\ N_0=T^{17/33}：\frac{M_{\max}}{A_{\rm BC}}\asymp T^{\frac32-\frac{34}{33}}=T^{\frac{49}{66}} \Longrightarrow \boxed{M_{\max}\gg A_{\rm BC}}✓✓$$
$$\Longrightarrow\ \boxed{\text{简单 DEAD 理由（}M\asymp A\text{）}\ \textbf{被排除}}✓✓\quad(\text{但}\ \textbf{不} \text{因此宣称有计数优势——唐先生之二次校正})✓$$

## 2. ⭐⭐ V2-22b：把 $(k,u,v,g)$ 代入 §3 的**加权**和
$$\text{参数化（V2-21）}：\ell_1=gu,\ \ell_2=gv,\ a_1=kv,\ a_2=ku,\ (u,v)=1✓$$
$$\text{再解}\ \ell_1n_1=\ell_2n_2：\ un_1=vn_2,\ (u,v)=1\Longrightarrow \boxed{n_1=vw,\ n_2=uw}✓✓$$
$$\textbf{完整参数族}：\ \boxed{(k,u,v,g,w)},\quad (u,v)=1；\quad \text{dyadic 约束}\：k\asymp\frac Au,\ g\asymp\frac Lu,\ w\asymp\frac Nu,\ u\asymp v✓$$
$$\textbf{(3.2) 的权重}：\ |n_1a_1|^2+|n_2a_2|^2=(vw\cdot kv)^2+(uw\cdot ku)^2=\boxed{k^2w^2(u^4+v^4)}✓✓$$
$$\textbf{加权退化求和}（含}\ m\ \text{-求和的}\ \asymp M\ \text{因子）：$$
$$\qquad \Sigma_{\rm wd}\ \asymp\ M\sum_{u,v,k,g,w}\frac{k^2w^2(u^4+v^4)}{\text{（权重）}}\ \asymp\ M\sum_{u\ge1}\underbrace{u}_{\#v}\cdot\underbrace{\Bigl(\frac Au\Bigr)^3}_{\sum_k k^2}\cdot\underbrace{\Bigl(\frac Nu\Bigr)^3}_{\sum_w w^2}\cdot\underbrace{\frac Lu}_{\#g}\cdot u^4$$
$$\qquad =\ A^3N^3L\,M\sum_{u\ge1}\frac{u^{1+4}}{u^{3+3+1}}\ =\ A^3N^3L\,M\sum_{u\ge1}\frac1{u^2}\ =\ \boxed{A^3N^3L\,M\cdot\zeta(2)}✓✓$$

## 3. ⭐⭐ 结构性发现：**收敛于 $u\asymp1$**（有界比值支配）
$$\sum_{u\ge1}u^{-2}=\zeta(2)=O(1)\ \textbf{收敛} \Longrightarrow \boxed{\text{加权退化求和由}\ u\asymp1\ \textbf{支配}}✓✓$$
$$\qquad\text{即：}\ \frac{\ell_2}{\ell_1}=\frac vu\asymp1,\ \frac{n_1}{n_2}=\frac vw\cdot\frac{u}{w}\ \text{型比值}\ \textbf{有界} \text{的配置支配整体}✓✓$$
$$\qquad\text{而大比值尾部（}u\gg1\text{）}\ \textbf{总量}\ O(1) \Longrightarrow \text{不贡献幂次级}✓$$
$$\Longrightarrow\ \boxed{\text{退化族的}\ \textbf{支配部分} \text{是"}\textbf{有界比值}\text{"子集，而非整个退化族}}✓✓\quad(\text{新结构信息})✓$$

## 4. ⚠️ 与 BC 的 $LM^{1+\varepsilon}$ 比较：**出现量级落差**
$$\text{BC §3 逐字}：\text{"The contribution}\dots\text{with}\ a_1\ell_1=a_2\ell_2\ \textbf{is trivially}\ O(\|\alpha\|^2\|\nu\|^2LM^{1+\varepsilon})\text{"}✓$$
$$\text{本档计算}：\ \Sigma_{\rm wd}\asymp A^3N^3L\,M\,\zeta(2)$$
$$\text{在归一化}\ \|\alpha\|=\|\nu\|=1\ \text{下}：\ \text{BC 的界}\ \asymp LM^{1+\varepsilon}\quad\big|\quad \text{本档}\ \asymp A^3N^3LM\Longrightarrow \textbf{相差}\ A^3N^3✓✓$$
$$\Longrightarrow\ \boxed{\text{两种可能}：\text{(甲) BC 的"trivial 界"}\ \textbf{并非紧}（\Longrightarrow \textbf{存在缺口！}）；\text{(乙) 本档权重记账有误}}✓✓$$
$$\qquad\textbf{本档}\ \textbf{不能} \text{在现有抽取精度下裁定}\ \text{(甲)/(乙)} \Longrightarrow \text{判}\ \boxed{\textbf{OPEN}}✓\quad(\text{残余 1})✓$$

## 5. 状态与判据（按唐先生框架）
$$\boxed{M_{\max}\gg A_{\rm BC}}\ \textbf{已排除} \text{"}M\asymp A\text{"这一简单 DEAD 理由}✓$$
$$\boxed{\text{退化计数优势是否穿透 BC §3 的权重体系}\ =\ \textbf{OPEN}}✓✓$$
$$\text{不落 ALIVE}（\text{未证穿透}）；\ \text{不落 DEAD}（\text{已排除简单理由}）✓$$
$$\text{第 4 步（移动平衡点）}\ \textbf{按纪律不开}✓$$

## 6. 残余（不得省略）
$$\text{残余 1（决定性）：}\ \text{§3 的}\ O(\|\alpha\|^2\|\nu\|^2LM^{1+\varepsilon})\ \text{与本档}\ A^3N^3LM\ \text{的}\ \textbf{量级落差}\ \text{未裁定}\Longrightarrow \text{须}\ \textbf{逐行读 (3.2)} \text{的权重记账}✓$$
$$\text{残余 2：本档未纳入}\ (b\eta,\ell_1\ell_2n_1n_2)=1,\ (m,b\ell_1\ell_2n_1n_2)=1,\ \text{supp 条件} \Longrightarrow \text{实际}\ \le\ \text{本档估计}✓$$
$$\text{残余 3：}\ \alpha,\nu\ \text{的归一化约定}\ \text{未核}（\text{影响 §4 的比较基准}）✓$$
$$\text{残余 4：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 不做尺度猜测（唐先生指定），只做}\ \textbf{加权比较}；\quad\text{② }\textbf{未用 RH}；\ \text{零数值（仅计数量级）}✓$$

## 8. 净产出
$$\text{(i) ✓ 唐先生校正成立：}\ A_{\rm BC}=N_1N_2/(d^2T^{1-\varepsilon}),\ M_{\max}/A_{\rm BC}\asymp T^{49/66}\Longrightarrow M_{\max}\gg A_{\rm BC} \Longrightarrow \textbf{简单 DEAD 理由被排除}✓✓$$
$$\text{(ii) ⭐⭐ 完整参数族}\ (k,u,v,g,w)\ \text{＋权重}\ k^2w^2(u^4+v^4)\Longrightarrow \Sigma_{\rm wd}\asymp A^3N^3LM\,\zeta(2)✓✓$$
$$\text{(iii) ⭐⭐ 新结构发现：收敛于}\ u\asymp1 \Longrightarrow \textbf{有界比值子集支配退化族}✓✓$$
$$\text{(iv) ⚠️ 与}\ LM^{1+\varepsilon}\ \text{相比出现}\ A^3N^3\ \text{量级落差} \Longrightarrow \text{（甲）BC 的界非紧（有缺口）或（乙）记账有误}\Longrightarrow \textbf{OPEN}✓✓$$
$$\text{(v) 判据状态：}\ M\asymp A\ \text{已排除；}\textbf{穿透性＝OPEN}✓$$
