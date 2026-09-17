# ⚔️ W6-MAJORANT-1f · **J1 的精确归约 ＋ 路线 2 的判定**

> 依唐先生 12:49「走 2」＋「先攻 J1，而不是继续做一般 Parseval」✓
> **本档结果**：J1 被 (§5.2) 归约到**单一配对关系**；路线 2 作为**一般论证**＝**C（工具失效）** ✓✓

---

## §1 唐先生的 J1／J2 拆分（照录）

$$\boxed{\textbf{J1}：\text{global Parseval}\ \not\Rightarrow\ \text{local}\ y\sim\log X\ \text{mass}}✓$$
$$\boxed{\textbf{J2}：\text{local}\ L^2\ \text{mass}\ \not\Rightarrow\ \lambda_{\max}\sim X\quad(\text{有效秩}\ r\asymp T)}✓$$
$$\text{两者}\ \textbf{性质不同}：\text{J1＝Fourier tail localization}；\ \text{J2＝spectral concentration／effective rank}✓✓$$
$$\text{唐先生判据}：\text{若证 J1 在 (§5.2) 假设下}\ \textbf{无统一下界} \Longrightarrow \textbf{路线 2 直接判死，不必碰 J2}✓✓$$

## §2 ⭐⭐⭐ 本节新得：**(§5.2) 把问题压到一条**（J1 的归约）

$$\text{§5.2 逐字}：\mathbf 1_{[-L/2+w,L/2-w]}\le\phi^2\le\phi\le\mathbf 1_{[-L/2,L/2]} \ \Longrightarrow\ \phi\equiv1\ \textbf{on core}\ [-L/2+w,\ L/2-w]✓$$
$$\Longrightarrow\ f=c^2\phi^4\ \textbf{在 core 上恰好等于}\ c^2\ (\textbf{常数})✓✓$$
$$\Longrightarrow\ \text{（因}\ \phi\le1\ \text{同时给出}\ f\le c^2\ \text{处处）}\ \text{边缘余项}\ \eta:=f-c^2\mathbf 1_{\rm core}\ \textbf{满足}：$$
$$\qquad \boxed{\operatorname{supp}\eta\subset\ \text{两层宽}\ w=1\ \text{的边缘带}\ (\textbf{总测度恰}\ 2),\qquad 0\le\eta\le c^2}✓✓✓$$
$$\Longrightarrow\ \boxed{\hat f(y)=\underbrace{c^2\frac{2\sin(\ell y)}{y}}_{\rm core,\ \ell=L/2-w}+\underbrace{\hat\eta(y)}_{\text{边缘}}},\qquad |\hat\eta(y)|\le\|\eta\|_1\le2c^2✓✓$$

$$\textbf{关键读数}：\text{在}\ y\asymp L\ \text{处}\ |{\rm core}|\asymp\frac{2c^2}{L}\ \textbf{而}\ |\hat\eta|\le2c^2$$
$$\qquad\Longrightarrow\ \textbf{尺寸上边缘项}\ \textbf{足以} \text{抵消 core 尾部} ⟹ \textbf{J1 不能仅由尺寸判定}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{J1 归约为一条配对关系}：\text{测度-2 边缘层上的}\ \eta\ge0\ \text{能否在窗口}\ [\log X,\log2X]\ \text{上抵消}\ 2\sin(\ell y)/y\ \text{的尾部？}}✓✓✓$$

## §3 三个方向的初步读数（本档）

$$\textbf{(a) 锐利}\ \phi\ (w\to0,\ \eta=0)：\ \hat f=c^2\frac{2\sin(\ell y)}{y} \Longrightarrow \frac1{\log2}\!\int_{\rm win}\!|\hat f|^2\asymp\frac{2c^4}{y^2} \Longrightarrow \boxed{I_X\asymp\frac{c^4}{L^2}}✓✓$$
$$\qquad(\text{窗口含}\ \asymp L\ \text{个周期，}\sin^2\ \text{平均稳定} ⟹ \text{相位无关})✓$$
$$\textbf{(b) 光滑}\ \phi：\text{边缘层}\ \eta\ \text{光滑且过渡宽固定}\ (w=1) \Longrightarrow \hat\eta\ \text{快衰} \Longrightarrow \textbf{core 主导} ⟹\ \textbf{仍}\ I_X\asymp\frac{c^4}{L^2}✓✓$$
$$\textbf{(c) 粗糙／共振}\ \phi：\text{若}\ \eta\ \text{沿边缘带被构造成使}\ \hat\eta\approx-\frac{2c^2\sin(\ell y)}{y}\ \text{于窗口上} \Longrightarrow I_X\ \text{可被压小}$$
$$\qquad ⚠️\ \text{但}\ \eta\ \text{的自由度只有"两条各宽}\ w=1\ \text{的带内非负函数"；能否在}\ \asymp L\ \text{个周期的窗口上}\ \textbf{整段} \text{抵消，\textbf{未定}}✓✓$$

$$\Longrightarrow\ \boxed{\textbf{J1}\ =\ \textbf{OPEN}，\ \text{但已归约到}\ \textbf{可判定} \text{的单条配对问题（(a)(b) 给下界，(c) 是唯一可能的反例方向）}}✓✓✓$$

## §4 路线 2 的判定（TACTICAL ATTACK 标注）

$$\text{路线 2 ＝"绕过}\ \alpha_n\ \text{下界，改用均方／Parseval"}✓$$
$$\text{本档结论}：\text{Parseval}\ \textbf{已证不足以} \text{给 dyadic 局部质量（唐先生 §2--§4 逐字成立）}；$$
$$\qquad \text{而 (§5.2) 又把问题压到 §2 的单条配对关系上——}\textbf{该关系在论文假设内}\ \textbf{两种行为都可能}✓✓$$
$$\Longrightarrow\ \boxed{\text{路线 2 作为}\ \textbf{一般论证} ＝ \textbf{C（工具失效）}}✓✓$$
$$\qquad(\text{即：} \text{"用 Parseval／均方绕过}\ \alpha\ \text{下界"}\ \textbf{不可能} \text{做到}；\ \text{它不能替代}\ \alpha_n\ \text{的逐点下界})✓✓$$

## §5 最终状态表（本档合并唐先生表 ＋ 本档结果）

| 机制 | 状态 |
|:--|:--|
| 消除裸 Hilbert 奇核 | $\checkmark$ |
| 严格带限 $[-3T/2,3T/2]$ | $\checkmark$ |
| 去掉粗糙的 $L$ 权 | $\checkmark$ |
| bandlimit $\Rightarrow X\to T$ | $\times$ |
| $\alpha$ 振荡自动产生 power saving | $\times$（模型层） |
| global Parseval | $\checkmark$ |
| Parseval $\Rightarrow$ local $y\sim\log X$ mass | **J1（已归约；OPEN）** |
| local 均方 $\Rightarrow \lambda_{\max}\sim X$ | **J2（秩 $\asymp T$）** |
| 路线 1（额外光滑假设） | 需论文未给的假设 |
| 路线 2（均方绕过） | **C：工具失效** ✓ |

$$\boxed{\textbf{W6-majorant-1}\ =\ \textbf{LOCAL ALIVE ／ CROSS-}X>T\ \textbf{UNRESOLVED}}✓✓$$

## §6 下一刀（唯一）
$$\text{攻 §2 那条配对关系：}\ \boxed{\text{测度-2 边缘层的}\ \eta\ge0\ \text{能否在}\ \asymp L\ \text{周期的窗口上整段抵消 core 尾部？}}✓✓$$
$$\qquad\text{(i) 证不能} \Longrightarrow \textbf{J1 通过} \Longrightarrow \text{局部质量}\ I_X\gtrsim c^4/L^2：
\text{再算 J2（秩损失）}✓$$
$$\qquad\text{(ii) 构造出能} \Longrightarrow \textbf{路线 2 死，且}\ \textbf{W6-majorant-1}\ \text{在模型层即 FAIL}✓✓$$
$$\qquad ⚠️\ \text{本档}\ \textbf{未} \text{判 (i)／(ii)}✓$$

## §7 边界
$$\text{(i)}\ §1／§5\ \text{照录唐先生 12:49}✓\quad\text{(ii)}\ §2\ \text{为}\ (§5.2)\ \text{的直接推论（}\phi\equiv1\ \text{＋}\ \phi\le1\Rightarrow\ \text{core 上}\ f\equiv c^2）✓✓$$
$$\text{(iii)}\ §3\ \text{为}\ [\textbf{结构}] \text{级估读}✓\quad\text{(iv)}\ \textbf{未用 RH／HL／pair correlation}；\ \textbf{零数值}✓$$
