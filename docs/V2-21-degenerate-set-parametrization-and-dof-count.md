# V2-21 — **退化集合 $a_1\ell_1=a_2\ell_2$ 的精确参数化 ＋ 自由度计数**

> 唐先生 2026-09-16 21:28 拍板：**V2-21 先做结构性穷举，不假设它能压**✓
> **表述校正（采纳）**：$\text{"}F_3\ \text{是纸墙"}\ \Longrightarrow \textbf{撤回}$；已证的只是 $\boxed{F_3\leftarrow\{a_1\ell_1=a_2\ell_2\}\leftarrow\text{trivial count}}$✓
> 判死标准（唐先生）：$\mathrm{ALIVE}$＝发现 BC **未使用**的结构约束 **且** 证明退化族获 $N^{-\delta}$ 级节省；$\mathrm{DEAD}$＝精确参数化后仍为原数量级，或"限制退化"只是重用已有 coprimality／range／counting；$\mathrm{OPEN}$＝有额外约束但尚不能证幂次节省✓

---

## 1. 精确参数化（唐先生版，本档**验证**）
$$g：＝(\ell_1,\ell_2),\quad \ell_1=gu,\ \ell_2=gv,\ (u,v)=1；\quad a_1\ell_1=a_2\ell_2 \Longrightarrow a_1u=a_2v$$
$$\qquad (u,v)=1 \Longrightarrow u\,|\,a_2,\ v\,|\,a_1 \Longrightarrow \boxed{(a_1,a_2,\ell_1,\ell_2)=(kv,\ ku,\ gu,\ gv),\quad (u,v)=1}✓✓\quad(\textbf{参数化成立})✓$$

## 2. ⭐ 自由度计数（本档计算）
$$\text{参数：}u,v\ (\text{互素，同阶}),\ k\ (\text{使}\ kv\asymp A),\ g\ (\text{使}\ gu\asymp L)$$
$$\qquad\text{约束}：kv\asymp A \Rightarrow k\asymp\frac Au；\quad gu\asymp L \Rightarrow g\asymp\frac Lu；\quad \textbf{且}\ u\asymp v\ (\text{因}\ ku\asymp A,\ kv\asymp A)✓$$
$$\text{计数（对}\ u,v\ \text{求和，}v\ \text{取} \asymp u\ \text{且与}\ u\ \text{互素，}\ \#v\asymp u\text{）：}$$
$$\qquad N_{\rm degen}\ \asymp\ \sum_{u\ \le\ \min(A,L)}\ \underbrace{u}_{\#v}\cdot\underbrace{\frac Au}_{\#k}\cdot\underbrace{\frac Lu}_{\#g}\ =\ A\,L\sum_{u\le\min(A,L)}\frac1u\ \asymp\ \boxed{A\,L\,\log\min(A,L)}✓✓$$
$$\textbf{对照}：\ \text{无约束四元组计数}\ \asymp A^2L^2 \Longrightarrow \frac{N_{\rm degen}}{A^2L^2}\ \asymp\ \frac{\log\min(A,L)}{AL}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{退化族的}\ \textbf{计数} \text{比无约束族小}\ \asymp AL/\log\ \text{倍}}✓✓$$

## 3. ⚠️ 唐先生的关键警句：**代数降维 ≠ 幂次降维**
$$\text{退化约束给出}\ \frac{a_1}{a_2}=\frac{\ell_2}{\ell_1} \Longrightarrow \text{两边皆}\ \asymp1 \Longrightarrow \textbf{仅靠 dyadic 区间同量级不产生节省}✓✓\quad(\text{唐先生之警，}\textbf{成立})$$
$$\textbf{但}：\ \text{本档 §2 的节省}\ \textbf{不是} \text{来自区间约束，而是来自}\ \textbf{参数个数} \text{从 4 降到 3}（k,u,v,g\ \text{带一个互素条件}） \Longrightarrow \text{节省量级}\ AL/\log✓✓$$
$$\Longrightarrow\ \text{故}\ \text{"代数降维}\ne\text{幂次降维"}\ \textbf{在区间层面成立}，\ \text{但}\ \text{在}\ \textbf{计数层面} \text{确实出现}\ \textbf{幂次级} \text{落差（}AL\ \text{倍}）✓✓$$

## 4. ⭐⭐ 决定性问题（第 3 问，唐先生指定）
$$\text{BC 对退化子情形的界为}\ O(\|\alpha\|^2\|\nu\|^2\,L\,M^{1+\varepsilon})（\text{§3 逐字："is trivially}\ O(\|\alpha\|^2\|\nu\|^2LM^{1+\varepsilon})\text{"}）✓$$
$$\text{本档计数}\ N_{\rm degen}\asymp AL\log\min(A,L) \Longrightarrow \textbf{是否已由 BC 的界精确反映}？$$
$$\qquad\text{若}\ M\asymp A：\ LM^{1+\varepsilon}\asymp AL\log^{O(1)} \Longrightarrow \boxed{\text{BC 的界}\ \textbf{已是} \text{退化族在现有约束下的计数}} \Longrightarrow \textbf{DEAD}✓$$
$$\qquad\text{若}\ M\gg A\ \text{或}\ M\ll A：\ \text{则}\ BC\ \text{的界}\ \textbf{与计数不匹配} \Longrightarrow \text{可能存在}\ \textbf{未使用的计数优势}✓✓$$
$$\Longrightarrow\ \boxed{\text{第 3 问的判据被压缩成一个具体比较}：\ M\ \text{与}\ A\ \text{的相对大小}}✓✓$$

## 5. 判定：**OPEN**（按唐先生标准）
$$\boxed{\textbf{OPEN}}：\ \text{已得}\ \textbf{精确参数化} \text{＋}\ \textbf{计数量级} \text{（}AL\log\text{）}，}\ \textbf{但} \text{尚不能断定是否产生}\ N^{-\delta}\ \text{级节省}✓$$
$$\qquad\text{不落 ALIVE}（\text{未证 BC 未使用该计数优势}）；\ \text{不落 DEAD}（\text{未证}\ M\asymp A）✓$$
$$\qquad\textbf{第 4 步（移动平衡点）}\ \textbf{不开} \text{——按唐先生：须先有}\ M^{1-\delta}\ \text{级改善}✓$$

## 6. 残余（不得省略）
$$\text{残余 1：}\ M\ \text{与}\ A\ \text{在 BC／BCR 参数化中的相对大小}\ \textbf{未定}（\text{§4 的决定性比较}）✓$$
$$\text{残余 2：本档计数未纳入 §3 的其他约束（}(b\eta,\ell_1\ell_2n_1n_2)=1,\ (m,b\ell_1\ell_2n_1n_2)=1,\ \text{支撑条件}）\Longrightarrow \text{实际计数}\ \le\ \text{本档估计}✓$$
$$\text{残余 3：残余 A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 不假设退化可压（唐先生指定）；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值（仅计数量级）}✓$$

## 8. 净产出
$$\text{(i) ✓ 参数化成立：}(a_1,a_2,\ell_1,\ell_2)=(kv,ku,gu,gv),\ (u,v)=1✓✓$$
$$\text{(ii) ⭐ 自由度计数：}N_{\rm degen}\asymp AL\log\min(A,L) \Longrightarrow \text{比无约束}\ A^2L^2\ \text{小}\ \asymp AL/\log\ \text{倍}✓✓$$
$$\text{(iii) ⚠️ 唐先生之警成立（区间层面无节省）；但计数层面确有幂次落差}✓$$
$$\text{(iv) ⭐⭐ 第 3 问压缩为：}\ \text{是否}\ M\asymp A\ \text{（若是 ⟹ BC 的界已是精确计数 ⟹ DEAD；若否 ⟹ 可能存在未使用的优势）}✓✓$$
$$\text{(v) 判定}\ \boxed{\textbf{OPEN}}；\ \text{第 4 步（移动平衡点）按纪律不开}✓$$
