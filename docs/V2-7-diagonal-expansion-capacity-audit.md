# V2-7 — **Diagonal-Expansion Capacity Audit**

> 唐先生 2026-09-16 20:35 拍板：立即转 V2-7，**对象重新定义**（不叫"攻 II"）。
> 核心问题：$$\boxed{\text{BC 的}\ \{\ell_1,\ell_2\}\to\{d,a_1,\ell_1,\ell_2\}\ \text{是否已达可扩张极限}？}$$
> 三档：**V2-7-A** 仍可扩张（ALIVE）$\big|\$ **V2-7-B** 不能扩张（＝BC diagonal architecture 容量墙，**不得**称普遍墙）$\big|\$ **V2-7-C** 容量未知（OPEN）✓

---

## 0. 采纳三处修正（唐先生）
$$\textbf{(1)}\ \mathrm{II}\ \textbf{不作第一攻击目标}：\ \frac{M^2}{L}\ \text{只是}\ F_-(L)\ \text{三衰减项之一}；\ \text{须问"改 II 后新}\ L^{*}\ \text{是否使整体 envelope 真降"}✓$$
$$\textbf{(2) 局部代入不可行}：\ M=N,A=1\ \text{时三衰减项}\ \asymp\frac NL,\frac{N^2}{L},\frac{N^{3/2}}{L} \Longrightarrow F_2\ \text{最大}，\ \textbf{但} \ L^{*}\ \text{随三项共同变化}；\ \text{两两项平衡给}\ L\sim N^{-3/10},\,F_2\sim N^{23/10} \Longrightarrow \textbf{与}\ N^{19/20}\ \text{不同尺度}✓$$
$$\qquad\Longrightarrow \boxed{\text{下一步必须在 BC 完整参数化中做，}\textbf{不能} \text{再做局部指数猜测}}✓$$
$$\textbf{(3) III 的准确标签}：\ \beta\ \text{判定成立（}A^{1/2}\ne\text{Weil 直接来源）}，\ \textbf{但} \boxed{\text{"非 Weil"}\ne\text{"可自由改善"}} \Longrightarrow \mathrm{III}=\boxed{\text{C--S／变量消去型候选；可攻击性}\ \textbf{OPEN}}✓\ (\textbf{非} \text{D1，}\textbf{非} \text{DEAD})$$

## 1. ⭐ 变量清单审计（本档新产出：显式枚举）
$$\text{§4.1.2}\ \text{后所涉变量（共 8 个）}：\ \underbrace{d}_{\text{互补除数}},\ \underbrace{a_1,a_2}_{\text{大小}\asymp A},\ \underbrace{\ell_1,\ell_2}_{\asymp L},\ \underbrace{n_1,n_2}_{\asymp N},\ \underbrace{c}_{(\mathrm{mod}\ b)}✓$$
$$\textbf{逐字（§4.1.2 原文）}：\ \text{"we apply the C--S inequality to the sums over}\ \boxed{n_1,n_2,a_2,c}\ \textbf{but not} \text{ to the sums over}\ \boxed{d,a_1,\ell_1,\ell_2}\text{.}\ \textbf{As a comparison, in [DFI97] the C--S is applied to all the sums except those over}\ \ell_1,\ell_2\text{"}$$
$$\qquad\Longrightarrow\ \textbf{平方组}\ \{n_1,n_2,a_2,c\}\ \big|\ \textbf{未平方组（＝"longer diagonal"）}\ \{d,a_1,\ell_1,\ell_2\}✓✓$$
$$\textbf{关键成本（原文，同段）}：\ \text{"Notice that we lost a factor of}\ b^{\frac12}\ \text{over the trivial bound when applying Cauchy--Schwarz with respect to}\ c\text{"}$$
$$\qquad\Longrightarrow\ \boxed{\text{平方是}\textbf{要付代价} \text{的（}c\ \text{一项即付}\ b^{1/2}\text{）} \Longrightarrow \textbf{问题＝哪些变量可以"不用付"}✓✓$$

## 2. ⭐⭐ 四个平方变量的逐个可解放性（本档分析）
$$\textbf{(i)}\ n_1,n_2\ (\asymp N)：\ \text{尺寸主导项}\ \Longrightarrow \text{必须}\ \textbf{平方以获得}\ \ell^2\ \text{控制} \Longrightarrow \textbf{结构性强制}✓$$
$$\textbf{(ii)}\ c\ ((\mathrm{mod}\ b))：\ \text{同余类变量，}\ \text{平方是}\ \textbf{故意付代价}（b^{1/2}） \Longrightarrow \text{非自然候选}✓$$
$$\textbf{(iii)}\ a_2\ (\asymp A)：\ \textbf{自然候选}✓✓：$$
$$\qquad\text{(a) 尺寸}\ \asymp A\ \text{与}\ a_1\ \textbf{同阶有界}；\ \text{(b) 参与}\ \delta=a_2(d\ell'_1-d'\ell_1)\ell_2\ell'_2(\dots)\ \text{的}\ \textbf{乘法结构}✓$$
$$\qquad\text{(c) ⭐ }\textbf{不对称性即结构信号}：\ a_1\ \textbf{已被保留} \text{（未平方）而}\ a_2\ \text{被平方} \Longrightarrow \text{同阶、同类变量处理不同}✓✓$$
$$\Longrightarrow\ \boxed{\text{下一个可解放候选}＝a_2\ (\text{次选}\ c)}✓✓\quad([结构判定])$$

## 3. 容量判据（唐先生五条件，用于检验 $a_2$ 扩张）
$$\text{扩张}\ \{d,a_1,\ell_1,\ell_2\}\to\{d,a_1,a_2,\ell_1,\ell_2\}\ \text{须同时保持}：$$
$$\qquad\text{(1) C--S 后变量可控}\ \big|\ \text{(2) diagonal 条件仍可解}\ \big|\ \text{(3) 所得 Kloosterman 型对象仍获}\ \textbf{平均估计}✓$$
$$\qquad\text{(4) 不引入比原问题更大的 off-diagonal}\ \big|\ \text{(5) 能把}\ D_b\ \textbf{主导项指数下降}✓$$
$$\text{五条件齐备}\Longrightarrow \mathrm{V2\text{-}7\text{-}A}\ (\text{ALIVE})；\ \text{任一必然破坏}\Longrightarrow \mathrm{V2\text{-}7\text{-}B}；\ \text{无法判定}\Longrightarrow \mathrm{V2\text{-}7\text{-}C}✓$$

## 4. 判定：**V2-7-C（容量未知）**，但候选已命名
$$\textbf{本档未能完成五条件检验}：\ \text{须读 §4.1.3--§4.4 以判定}\ a_2\ \text{能否在不破坏}\ \delta\text{-split、reciprocity (4.18) 与 Weil 应用的前提下留外}✓$$
$$\qquad\Longrightarrow \boxed{\mathrm{V2\text{-}7\text{-}C}}：\ \text{容量}\ \textbf{OPEN}；\ \text{但已把"下一枪"精确化为}：$$
$$\qquad\boxed{\text{检验}\ a_2\ \text{能否从平方组移入未平方组（}\text{否则}：\text{BC diagonal architecture 容量墙}\ \mathrm{B}）}✓✓$$

## 5. ⭐ 本档确立的**方法论转变**（唐先生）
$$\text{V2-6b 把"继续优化一个指数"提升为}：\ \boxed{\text{优化}\ s\ \longleftrightarrow\ \text{优化 C--S 后保留下来的}\ \textbf{变量维度}}✓✓$$
$$\qquad\text{这与此前反复撞上的"重新参数化"}\ \textbf{不同}：\ \text{这里存在一个}\ \textbf{原证明中的离散结构选择} \text{（哪些变量平方、哪些留在 diagonal）}✓$$
$$\qquad\text{且 BC 提供了一次真实成功案例}：\ \{\ell_1,\ell_2\}\to\{d,a_1,\ell_1,\ell_2\}\Longrightarrow\frac1{48}\to\frac1{20}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{当前主线最有价值的 LIVE 机制}＝\text{diagonal expansion}}✓\quad(\textbf{但} \text{不声称存在下一次 expansion})✓$$

## 6. 残余（不得省略）
$$\text{残余 1：}a_2\ \text{候选为}\ \textbf{[结构判定]}，\ \text{五条件未检验（须 §4.1.3--§4.4）}✓$$
$$\text{残余 2：}D_b\ \text{六项中另四项仍未逐项溯源（承 V2-6b 残余 1）}✓$$
$$\text{残余 3：残余 A--D（跨轮结转）不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 不攻 II；\ 不做局部指数猜测；}\ \text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) 采纳三修正：II 非首攻／局部代入不可行／III＝C--S 消去型候选（OPEN）}✓$$
$$\text{(ii) ⭐ 变量清单：8 变量；平方组}\{n_1,n_2,a_2,c\}\ \big|\ \text{未平方组}\{d,a_1,\ell_1,\ell_2\}✓$$
$$\text{(iii) ⭐ 平方有代价（}c\ \text{付}\ b^{1/2}，原文逐字）\Longrightarrow \textbf{问题＝哪些变量可"不付"}✓$$
$$\text{(iv) ⭐⭐ 候选命名：}\ a_2\（\text{同阶于}\ a_1\ \text{却处理不同——不对称即信号；次选}\ c）✓$$
$$\text{(v) 判定}\ \mathrm{V2\text{-}7\text{-}C}（\text{容量 OPEN}）\ \text{＋下一枪精确化：检验}\ a_2\ \text{可否移出平方组}✓$$
$$\text{(vi) 方法论转变登记：优化}\ s\ \leftrightarrow\ \text{优化 C--S 后的变量维度}✓$$
