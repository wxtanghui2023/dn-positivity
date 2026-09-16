# V2-10 — **§4.1.3.2 中 $a_2$ 的角色 ＋ 分支锁**

> 唐先生 2026-09-16 20:51 拍板 **V2-10**（暂不做 V2-9b／不追 DFI；先打穿 BC 的另一半）。
> 追踪链：$$\boxed{a_2\to\text{相位}\to\text{C--S 后平方和}\to\text{Weil/Kloosterman 估计}}$$
> 三问：(1) $a_2$ 是否真振荡变量？(2) 若不平方，所得对象是否仍属 BC 已有可控类？(3) 释放后新增项在完整参数中是否产生严格 saving？✓
> **分支锁（唐先生）**：须 $\mathscr V^{*}$ **与** $\mathscr V$ **都可释放** **＋** 整体 envelope 下降 ⟹ 才 ALIVE；仅第一项成立 ⟹ **C**；$\mathscr V$ 中出现不可控制的平方和 ⟹ **B**✓

---

## 1. §4.1.3.2 的结构（PDF 逐段，**外部来源，仅作数据**）
$$\textbf{(a) 互反律入口}：\ \text{用 (4.18)（"holds for}\ \eta,\eta'\ \text{pairwise coprime"）}\ \textbf{把}\ a_2(d\tilde\ell'_1-d'\tilde\ell_1)\ (\mathrm{mod}\ 1)\ \text{改写}\ ✓✓$$
$$\textbf{(b) }\delta\ \text{的定义}：\ \delta：＝a_2(d\tilde\ell'_1-d'\tilde\ell_1)\dots\ \text{型（}\textbf{a}_2\ \text{作为}\ \delta\ \text{的乘性因子）}✓$$
$$\textbf{(c) 关键同余 (4.22)}：\ \text{原文}\ \text{"}\dots\text{Weil's bound on the sum over}\ n'_0\dots\text{(4.22) and it allows us to }\boxed{\text{express either}\ a_1\ \text{or}\ a'_1}\text{"}$$
$$\qquad\Longrightarrow\ a_1=f(a'_1;a_2;d;d';\ell_1,\ell_2,\ell'_1,\ell'_2,\dots)✓✓\quad(\text{即}\ a_1\ \text{由含}\ a_2\ \text{的同余}\ \textbf{解出})✓✓$$
$$\textbf{(d) 整除条件}：\ \text{"if}\ \dots=1\ \text{then (4.22) implies that}\ \tilde\ell'_1\,|\,a_2\tilde\ell'_1\,|\,a_2\tilde\ell_1\ \text{and}\ \tilde\ell_2\,|\,a_1\tilde\ell'_2\,|\,\dots\text{"} \Longrightarrow \boxed{\text{由 (4.22) 导出对}\ a_2\ \text{的}\ \textbf{整除约束}}✓✓$$
$$\textbf{(e) 求和列}：\ a_1,a'_1,a_2\asymp A\ \text{且}\ \ell_1|a_2\ell'_1,\ \ell_2|a_1\ell'_2\ \text{型条件}；\ \text{最终界含}\ (p_1+q_1)(p_2+q_2)\ \text{型因子}✓$$

## 2. ⭐⭐ 分支锁证据（本档核心发现）
$$\boxed{\text{两分支中}\ a_1,a_2\ \textbf{角色互换}}✓✓：$$
$$\qquad\mathscr V^{*}\ (\text{case}\ d=d',\ell_1=\ell'_1,\ell_2=\ell'_2,a_1\ne a'_1)：\ \boxed{a_1\ \text{仅以差分}\ (a_1-a'_1)\ \text{出现}；\ a_2\ \text{自由}}✓\ (\text{V2-9})$$
$$\qquad\text{§4.1.3.2}\ (\text{case}\ (d,\ell_1,\ell_2)\ne(d',\ell'_1,\ell'_2))：\ \boxed{a_2\ \text{进入}\ \delta\ \text{与 (4.22)}；\ a_1\ \text{被 (4.22)}\ \textbf{解出}}✓✓$$
$$\Longrightarrow\ \boxed{\mathscr V^{*}\ \text{中}\ a_2\ \text{的自由}\ \textbf{不自动} \text{迁移到 §4.1.3.2}}✓✓\quad(\text{唐先生的"分支锁"担忧}\ \textbf{被证实存在})✓$$
$$\qquad\textbf{且更强}：\ \text{在 §4.1.3.2 中}\ a_2\ \text{是}\ \textbf{求 a}_1\ \text{所必需的输入} \Longrightarrow \text{把}\ a_2\ \text{移出后，}\ a_1\ \text{的求解结构}\ \textbf{须重推}}✓$$

## 3. 三问逐项回答
$$\textbf{问 1：}a_2\ \text{是否真振荡变量}？\ \Longrightarrow\ \boxed{\textbf{是}}✓\quad(\text{在 §4.1.3.2 中经}\ \delta\ \text{进相位，并经 (4.22) 进同余})$$
$$\textbf{问 2：若不平方，所得对象是否仍属可控类}？\ \Longrightarrow\ \boxed{\textbf{本档无法判定}}✓$$
$$\qquad\text{理由}：\ \text{释放}\ a_2\ \text{后，外层出现一个}\ \textbf{以}\ a_2\ \text{为新振荡变量的和} \text{，其模数与}\ n'_0\ \text{的和}\ \textbf{不同}；\ \text{BC 现有的 Weil 界是施加在}\ n'_0\ \text{之和上} \text{的（逐字 (c)），}\ \text{未含}\ a_2\ \text{之和}✓$$
$$\qquad\text{同时 (d) 的整除约束}\ \tilde\ell'_1|a_2\tilde\ell_1\ \text{会}\ \textbf{限制} \text{外层}\ a_2\ \text{的取值范围（}\text{约束而非障碍）}✓$$
$$\textbf{问 3：释放后是否产生严格 saving}？\ \Longrightarrow\ \boxed{\textbf{本档无法判定}}（\text{须完整 envelope 重推}）✓$$

## 4. 判定：**C**
$$\boxed{\textbf{C}}：\ \text{局部分支开放（}\mathscr V^{*}\ \text{可释放），}\ \textbf{整体仍未判定}（\text{§4.1.3.2 的可控性未决}）✓$$
$$\qquad\text{按唐先生规则}：\ \text{仅第一项成立} \Longrightarrow \textbf{C}✓\quad(\text{尚未出现}\ \mathscr V\ \text{中"明确不可控制的平方和"} \Longrightarrow \textbf{不落 B})✓$$
$$\qquad\text{亦不落 A}（\text{三分支＋envelope 未齐}）✓$$

## 5. ⭐ 对"BC 第一次 expansion"的更精确刻画（采纳唐先生）
$$\text{BC 的第一次 expansion}\ \textbf{不是} \text{"释放某个特殊算术变量"}，\ \text{而更接近}：$$
$$\qquad\boxed{\text{改变 C--S 后的求和几何，使某些原本被平方的变量进入}\ \textbf{可处理的差分结构}}✓✓$$
$$\text{而本档显示}：\ \text{在 §4.1.3.2 中}\ a_2\ \text{进入的是}\ \textbf{乘性}（\delta）\ \text{结构}，}\ \textbf{不是} \text{差分结构} \Longrightarrow \boxed{\text{尚未找到}\ \textbf{可重复的 diagonal-expansion rule}}✓$$
$$\qquad(\text{即不能把 BC 的技巧直接套到}\ a_2\ \text{上——}\ \textbf{但也不能据此判定容量墙}）✓$$

## 6. 残余（不得省略）
$$\text{残余 1：§4.1.3.2 的}\ a_2\ \text{之和的模数与可控性}\ \textbf{未取全}（(4.19)--(4.23) 的完整形式）✓$$
$$\text{残余 2：}\ \mathscr V\ \text{与 §4.1.3.2 的对应关系}\ \textbf{未完全对齐}（\mathscr V\ \text{是}\ U\ \text{中}\ (d,\ell_1,\ell_2)\ \text{互素情形）✓$$
$$\text{残余 3：}D_b\ \text{另四项未溯源；残余 A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 不假设释放成功；}\ \text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) §4.1.3.2 结构取证：(4.18) 改写}\ a_2(d\tilde\ell'_1-d'\tilde\ell_1)；(4.22)\ \textbf{解出}\ a_1\ \text{（含}\ a_2\ \text{为输入）；整除约束}\ \tilde\ell'_1|a_2\tilde\ell_1；\text{Weil 界施于}\ n'_0\ \text{之和}✓$$
$$\text{(ii) ⭐⭐ 分支锁证实：}\ \mathscr V^{*}\ \text{中}\ a_2\ \text{自由}\ \ne\ \text{§4.1.3.2 中}\ a_2\ \text{为必需输入} \Longrightarrow \text{两分支}\ \textbf{角色互换}✓✓$$
$$\text{(iii) 三问：(1) 真振荡＝}\textbf{是}；(2)(3)\ \textbf{无法判定}✓$$
$$\text{(iv) 判定}\ \boxed{\textbf{C}}（\text{局部分支开放，整体未判定；不落 A/B}）✓$$
$$\text{(v) BC expansion 的精确刻画＋}\ \textbf{未找到可重复 rule}✓$$
