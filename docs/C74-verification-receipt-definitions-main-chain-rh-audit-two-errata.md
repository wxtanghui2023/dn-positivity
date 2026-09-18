已查地图：**取回原档**（`V185-paper-reading-notes-arXiv-2608-13637.md` §1–§3（论文精读，含 §2.1 定义／§2.2 三步 (Z)(P)(L)／§3 输入清单）、`V186-inertia-mechanism-audit-endpoint-degenerates-to-positivity.md` §0（端点退化定理）、`V184`、`CLOSED-ROUTES-MAP:346`／`:360`、`JIA-C-...wall-reduces-to-single-number-R.md`、`PROTOCOL-R8-prime-pair-carrier.md` §0 勘误）。**结论**：`R≤1⟹RH` 的**蕴含成立且未偷用 RH**（输入清单无 RH），**但**：① 我上一条写成"**⟺**"**不精确**（单链是**单侧**不等式）；② 更要紧——**"把 `R` 压到 `≤1`"这条路 `V186` 已判「关」**（端点退化到 Weil 正性 ⟺ RH）⟹ **我上一条把"目标＝`R≤1`"当作 A 的精确形态，等于把已判关的端点又端回来：勘误** ✗

# C-74 · **核实回执**：`G̃/P₁/s₀` 定义、主链逐步出处、循环审计，＋ **两处勘误**

> **时间**：2026-09-18 12:19 唐先生要求钉死 `R≤1⇒RH` 这条等价关系（定义／主链／是否循环），并指出项目有"表面独立、暗中用 RH"的先例（`R8` 勘误）
> **本档**：全部**逐字取回原档**；**不新增数学** ✓

---

## §1 对象定义（`V185` §2.1 逐字，带论文标签）

$$L=\log\tfrac T{2\pi},\quad X=e^L,\quad \phi(u):=\chi(\tfrac L2+u)\chi(\tfrac L2-u)\psi(u/L)^{1/2},\ \ \operatorname{supp}\phi=[-\tfrac L2,\tfrac L2]$$
$$\alpha_k:=T+\tfrac{2\pi k}{L}\ (0\le k<d:=\lfloor LT/(2\pi)\rfloor),\qquad d=N(T,2T)+O(L)$$
$$v_\rho:=\bigl(\widehat\phi(\gamma_\rho-\alpha_k)\bigr)_{0\le k<d}\in\mathbb C^d\qquad(\textbf{Gabor 系数}\ \Longrightarrow\ \text{把 Weil 形式压进 }d\text{ 维})$$
$$\widetilde G:=\frac1{aL^2}\sum_{\Re\gamma_\rho\in I'}m_\rho\,v_\rho v_\rho^{\mathsf T},\quad P:=\frac1{aL^2}\sum_{\rho\in\mathrm{on}}m_\rho\,v_\rho v_\rho^{\mathsf T},\quad Q:=\widetilde G-P,\quad a:=\|\phi\|_2^2/L$$
$$\textbf{Lemma 2.1（Poisson--Gabor）}：\sum_{k\in\mathbb Z}\widehat\phi(z-\alpha_k)\widehat\phi(z'-\alpha_k)=L\widehat{\phi^2}(z-z')$$
$$\text{计数记号}：N=\sum_{T<\gamma\le2T}m_\rho;\quad N_d=\#\{\rho\};\quad N_0^s=\#\{\beta=\tfrac12,\ m_\rho=1\}（\textbf{简单在线零点数}）$$

## §2 主链三行（`V185` §2.2 逐字）

$$\textbf{(Z) 零侧（签名与秩）}：\operatorname{tr}P\le N_0,\quad n_+(Q)\le p,\quad N\ge s_1+2s_2+2p,\quad \operatorname{tr}\widetilde G=(1+o(1))N$$
$$\qquad ⭐\ \textbf{功能方程把离轴零点成对配}\ \{\rho,1-\bar\rho\}\Longrightarrow\text{每对给 }Q\text{ 一个签名 }(1,1)\text{ 的 block};\ \text{每个在线点给 }P\text{ 一个非负 rank-one}$$
$$\qquad ⚠️\ \text{用法与我们旧结论}\ \textbf{相反}：\text{我们 }V147/V148/V174\ \text{把 FE 当"对合／无单边律／选择难题"};\ \textbf{本文把 FE 当}\textbf{计数装置}✓✓$$
$$\textbf{(P) 素数侧（无条件的 HS 范数）}：\|\widetilde G\|_{\rm HS}^2=\bigl(R(\psi)+o(1)\bigr)N,\quad R(\psi_0)=\tfrac43,\ \ R(\psi_{\rm MT})=c_{\rm MT}^{-1}\approx1.3275$$
$$\qquad ⭐\ \text{＝}\textbf{Montgomery 的无条件素数侧二阶矩}（[\mathrm{Mon73}],[\mathrm{Ary22}],[\mathrm{BGSTB24}]），\ \textbf{带宽}\le1✓✓$$
$$\textbf{(L) 秩-迹不等式（Lemma R，精确形式）}：P\succeq0,\ \operatorname{rank}P\le r,\ n_+(Q)\le b\ \Longrightarrow\ \forall c>0：\ \boxed{\|P+Q\|_F^2\ \ge\ c\operatorname{tr}P-\tfrac{c^2}{4}r+2c\operatorname{tr}Q-c^2b}$$
$$\qquad \text{骨架}：Q=Q_+-Q_-;\ \text{展开}\|\cdot\|_F^2;\ \text{弃}\operatorname{tr}(PQ_+)\ge0;\ \textbf{关键一步 von Neumann 迹不等式};\ \text{两个初等序列估计}$$
$$\textbf{单链（论文 (1.2)）}：\ N_0^s+o(N)\ \ge\ \operatorname{rank}P_1\ \ge\ 4\operatorname{tr}\widetilde G-2N-\|\widetilde G\|_{\rm HS}^2\ =\ \bigl(2-R(\psi)-o(1)\bigr)N$$
$$\qquad \text{第一不等号＝}\textbf{Prop 4.1};\quad \text{第二＝(L) 配 (Z) 的}\operatorname{tr}P_1+2n_+(Q')\le N;\quad \text{等式＝(Z)}\wedge\text{(P)}$$

## §3 循环审计（逐条）

$$\textbf{输入清单（`V185` §3 逐字）}：\text{Weil 显式公式};\ \text{RvM};\ N(t,t+1)\ll\log t;\ \Gamma'/\Gamma\ \text{Stirling};\ \text{Chebyshev--Mertens};\ \text{Montgomery--Vaughan}（X\le T）$$
$$\qquad \boxed{\textbf{不用}\ \text{mollifier};\ \textbf{不用}\ \text{零点密度估计};\ \textbf{不用}\ \text{零自由区}}\ ✓✓$$
$$\textbf{接口（}s_0\leftrightarrow\operatorname{rank}\textbf{）}＝\textbf{Prop 4.1}：\text{简单在线零点}\to P\text{ 的非负 rank-one} \Longrightarrow \operatorname{rank}P_1\ \text{至少数出}\ N_0^s✓$$
$$\textbf{无 RH 的痕迹}：\text{全程}\ \textbf{数符号}（\text{inertia}）\text{而}\ \textbf{不假设}\ \text{正性};\ \text{FE 只作计数配对}✓;\ \text{（对照：RH 下 0.6792 由 [CGdL20] 用 form factor 在 }[-1,1]\ \textbf{之外}\ \text{的正性得到 —— 本文}\ \textbf{不进入该区域}）✓✓$$

## §4 ⚠️ 两处勘误（本档核心）

$$\textbf{勘误①（方向）}：\text{单链给的是}\ \textbf{单侧} \text{不等式}\ N_0^s/N\ge2-R \Longrightarrow$$
$$\qquad ✅\ R\le1\ \Longrightarrow\ N_0^s\ge N\ \Longrightarrow\ \text{全部零点简单且在线}\ \Longrightarrow\ \textbf{RH}\（\textbf{蕴含}，未用 RH）✓$$
$$\qquad ✗\ \textbf{反向不成立}：R\ge1\ \text{只是}\ 100\%\ \text{的}\textbf{必要} \text{条件} \Longrightarrow \text{"}100\%\iff R\le1\text{"}\ \textbf{不成立}$$
$$\qquad ⚠️\ \text{故我上一条写的 "}R\le1\iff\text{RH}"\ \textbf{必须降级} \text{为 "}R\le1\Longrightarrow\text{RH}"✓$$
$$\textbf{勘误②（更要紧）}：\text{`V186` §0③}\ \textbf{端点退化定理}\ \text{逐字}：$$
$$\qquad n_-(Q_T)\ \text{恰数}\ \textbf{离轴对}\ \Longrightarrow\ 100\%\ \text{要求}\ n_-=0\ \text{对全族成立}\ \Longrightarrow\ \textbf{正性}\ \Longrightarrow\ \textbf{Weil 正性}\ \Longrightarrow\ \text{RH}$$
$$\qquad\Longrightarrow\ \boxed{\text{inertia 路线}\ \textbf{不是} \text{Weil 正性的替代；它是}\textbf{部分比例} \text{的替代，而在"消灭离轴零点"这一步}\textbf{退回正性}}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{`V186` 判词＝}\boxed{\textbf{关}}\（\text{按唐先生预定规则："若 }100\%\iff\text{已等价于 Weil 正性／RH}\Longrightarrow\text{立刻关}"）$$
$$\qquad\Longrightarrow\ ⚠️\ \textbf{我上一条把"目标＝把 }R\text{ 压到}\le1\text{"当作 A 的精确形态，等于把已判关的端点又端回来}\ ✗\ \textbf{勘误}$$

## §5 修正后的 A 目标（中间地带）

$$\text{可达输出（已核）}：2/3\ (\psi_0)\ \big|\ 0.67250\ (\psi_{\rm MT})\ \big|\ 0.83625\（N_d\ \text{版}）;\ \text{"带宽一证书类"天花板}\approx0.6820$$
$$\text{阶梯（support}>1\ \text{即得提升）}：0.70/0.80/0.90\ \Longleftarrow\ \text{support}\ 1.04/1.26/1.70\（\textbf{超出已知}）$$
$$\Longrightarrow\ \boxed{\text{A 的正确目标}＝R\ \text{的}\textbf{非平凡下降}（4/3\to\text{更小但}>1）＝\textbf{中间地带}，\text{不退化、不循环}}✓$$
$$\qquad \text{且须}\ \textbf{先证独立性}（\text{`R8` 勘误教训：GM87／1987／LPS／BKS 的等价都在 RH 下}）✓$$

## §6 出处与性质

$$\text{链条}\ \textbf{不是项目内部账本}：\text{第三方论文}\ \texttt{arXiv:2608.13637v2}（2026-08-24,\ 21\ \text{页};\ \text{署名 Claude},\ \text{专家注}\ \text{Alpöge--Furman};\ \textbf{全部 Lean 由 Claude 撰写},\ \text{Comparator＋NanoDa 重放}）$$
$$\qquad \text{本地克隆}：\texttt{\textasciitilde/lean-repro/formal-math/zeta23/}（\texttt{RankTrace.lean}＝Lemma R 精确形式;\ \texttt{Ceiling.lean};\ \texttt{Inertia.lean}）；docstring 逐句对应论文 LaTeX 标签✓$$
$$\text{我方}\ V184\text{--}V186\ \text{的角色}：\textbf{审计}（七问拆解＋关键一刀），\textbf{非}提出者✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 12:2x）`[纪律]`

```
技术词 核实回执     命中文件数=1    :: ./C74-verification-receipt-definitions-main-chain-rh-audit-two-errata.md
技术词 非平凡下降  命中文件数=1    :: ./C74-verification-receipt-definitions-main-chain-rh-audit-two-errata.md
技术词 端点退化     命中文件数=1    :: ./C74-verification-receipt-definitions-main-chain-rh-audit-two-errata.md
技术词 单侧不等式   命中文件数=2    :: ./V117-variation-diminishing-test.md ./C74-verification-receipt-definitions-main-chain-rh-audit-two-errata.md
```
**读数**：`核实回执`／`非平凡下降`＝**仅本档 ⟹ 本档新增** ✓；`端点退化`＝**仅本档 ⟹ 术语首现**（概念＝`V186` 的"终点会退化回 Weil 正性"，英文档名 `endpoint-degenerates-to-positivity`）✓；⚠️ `单侧不等式`＝**2 档 ⟹ 档案已有**（通用词）⟹ 引用 ✓

## §8 边界

- `[逐字]` §1／§2／§3／§4 全部取自 `V185`／`V186` 逐字（含论文标签）✓；`[本档]` 仅 §4 的两处勘误与 §5 的目标修正 ✓
- **不声称**：`R` 可在 support ≤1 内降到 ≤1 ✗；不判 `Λ_1`／support>1 的结局 ✓；不证 RH ✗；**不覆盖原档**（勘误留档）✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓；未跑 Lean ✓

```
⚠️ 委托（唐先生 12:19）：钉死 R≤1⇒RH 的定义/主链/是否循环（有 R8"表面独立暗中用 RH"的先例）
⚠️ 定义已取回（V185 §2.1）：phi/L/X/alpha_k/d/v_rho/G̃/P/Q/a ＋ Lemma 2.1 Poisson-Gabor ＋ N/N_d/N_0^s
⚠️ 主链出处：第一不等号=Prop 4.1（简单在线零点→P 的非负 rank-one；rank 至少数出 N_0^s）；第二=(L) Lemma R
   （P⪰0, rank P≤r, n_+(Q)≤b ⟹ ‖P+Q‖_F² ≥ c trP − (c²/4)r + 2c trQ − c²b；骨架含 von Neumann 迹不等式）；
   等式=(Z) trG̃=(1+o(1))N ∧ (P) ‖G̃‖²_HS=(R+o(1))N
⚠️ 循环审计：输入=Weil 显式公式/RvM/N(t,t+1)≪log t/Stirling/Chebyshev-Mertens/Montgomery-Vaughan(X≤T)；
   **不用 mollifier、不用零点密度、不用零自由区**；FE 只作**计数装置** ⟹ 无 RH 痕迹 ✓
⚠️ 勘误①：单侧不等式 ⟹ 只能写 R≤1 ⟹ RH（蕴含），不能写"⟺"
⚠️ 勘误②（更要紧）：V186 端点退化定理 ⟹ 把 R 压到 ≤1 = 端点 = 退回 Weil 正性 ⟹ 已判【关】；
   我上一条把 R≤1 当 A 的目标 = 把已判关的端点又端回来 ✗
⚠️ 修正后 A 目标：R 的非平凡下降（4/3 → 更小但 >1）= 中间地带；需 support>1 输入；且须先证独立性
✅ 净产出：①定义与主链逐步逐字 ✓；②循环审计（无 RH）✓；③两处勘误 ✓；④A 目标修正 ✓；⑤出处与性质界定 ✓
```
