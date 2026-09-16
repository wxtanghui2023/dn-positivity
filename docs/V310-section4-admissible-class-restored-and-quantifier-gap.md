# V310 · **(a′-1) §4 原文恢复 ＋ 三类量词/域差异** —— ⭐⭐⭐⭐⭐ **判词重构：不是"两集合相等"，而是 $\mathcal A_{\rm var}\supsetneq\mathcal A_{\rm ThmD}$ ＋"极值点 $\tilde v_\lambda\in\mathcal A_{\rm ThmD}$"**；⭐⭐⭐⭐ **候选（重标后）满足 `WindowProfile` 全部四条件**（原归一化 $w/\sin w$ **违反** `le_one`，重标因比值尺度不变而无损）；⚠️ **精确 GAP ＝ 三个具体命题 P1/P2/P3**；⚠️ **重大副产品：ξ′ 版本常数（0.8584／0.8686）远高于 ζ 版本（0.6725）⟹ V303 §3 的"两机制统一"须降为[待复核]**

$$\boxed{\textbf{`WindowProfile`（§4 逐字）}：\text{even}\ (v(-s)=vs)\ \wedge\ \texttt{ContDiff}\ \mathbb R\ 3\ (C^{3})\ \wedge\ \big(\forall s\in[-\tfrac12,\tfrac12],0<vs\big)\ \wedge\ \big(\forall s,vs\le1\big)} ✓✓✓$$
$$\boxed{\textbf{量词/域差异（恰是你警告的那类）}：\text{(A)}\ \textbf{P.lam}<1\ \textbf{严格};\quad \text{(B)}\ \tfrac12\le\texttt{AdmWindow.bv};\quad \text{(C)}\ \texttt{ThmD.AdmWindow}\ \varphi\ L\ w\ c} ✓✓✓$$
$$\boxed{\textbf{候选核对}：\tilde v_\lambda(x)：＝\cos(2wx)\ \Longrightarrow\ \text{even}\ ✓,\ C^{3}\ ✓,\ 0<\tilde v\le1\ ✓\ \Longrightarrow\ \textbf{四条件全满足}} ✓✓✓$$
$$\boxed{\textbf{精确 GAP}：\text{P1 读}\ \texttt{ThmD.AdmWindow}\ \text{定义};\ \text{P2 核}\ \texttt{bv}\ \text{下界};\ \text{P3 }\lambda<1\ \text{vs}\ \lambda\le1\ \text{的域}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 14:02：**直接接着打 (a′-1)，不要再碰已闭合的凸性环** ✓；**只审一个命题** $\mathcal A_{\rm ThmD}\stackrel?=\mathcal A_{\rm variational}$ ✓；**四层硬审**（① 原样恢复 `AdmWindow` 定义：参数域／$\lambda$ 允许范围／$v_\lambda$ 的 admissibility／Theorem D 对候选与参数的全部限制／**隐藏的 endpoint、strict/non-strict、正则性要求**；② 逐项展开 $\mathcal A_{\rm ThmD}$，**不接受"显然满足"**，每项标 **直接定义／由已证引理推出／需新证明／不成立**；③ 逐项展开 $\mathcal A_{\rm variational}$（凸性黑箱已闭合，不再重复谱论证）；④ **双向包含**，最后落四分类 **EQUIVALENT／STRICT SUBSET／STRICT SUPERSET／GAP**，**GAP 必须指出精确缺失命题**）✓✓✓；**"尤其要查的是量词和定义域，而不是再寻找一个算子性质"** ✓✓✓
> 第一手依据 ✓ **`XiPrime/Statement.lean §4`（184–275 行，本档直读）**：`XiEF`／`XiTraceTransfer`／`CoeffMoments`／`GzMoments`／**`WindowProfile`**／**`CertFlat`**／**`CertQuartic`** ✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V310`（先领号 ✓）

---

## §1 **§4 原文恢复（本档直读摘录）**

$$\texttt{WindowProfile}\ \text{（逐字结构）}：\text{even};\ \texttt{ContDiff}\ \mathbb R\ 3\ v;\ \texttt{pos}：\forall s\in[-\tfrac12,\tfrac12],0<vs;\ \texttt{le\_one}：\forall s,vs\le1 ✓$$
$$\qquad \text{注释逐字}：\text{"admissible window profiles }v\text{ on }[-\tfrac12,\tfrac12]\ \text{(realised as }\varphi_v=\sqrt{v(u/L)}\cdot\varphi,\ \texttt{Defs.phiV})\text{: even, }C^{3}\text{, strictly positive on the closed interval (so }\sqrt v\ \text{is }C^{3}\ \text{there), bounded by 1. }vFlat\ \text{and}\ vQuartic\ \text{qualify."} ✓$$
$$\texttt{CoeffMoments}\ \text{的 producer 形状（逐字要点）}：\texttt{CoeffFamily.Hyps}\to\texttt{RvM}\to\texttt{GammaFacts}\to\texttt{MVHilbert}\to\texttt{P.Valid}\to\boxed{\texttt{P.lam}<1}\to$$
$$\qquad \text{(window realisation, per profile: }\exists c\ T_0,\forall T\ge T_0,\ \boxed{\texttt{ThmD.AdmWindow}\ ((Pf\ T).\varphi\ T)\ (P.L\ T)\ P.w\ c}\ \wedge\ \boxed{\tfrac12\le\texttt{AdmWindow.bv}})\to$$
$$\qquad (\forall T,(Pf\ T).\texttt{lam}=P.\texttt{lam}\wedge(Pf\ T).w=P.w)\to\texttt{Tendsto}\ (\texttt{cRatio}\ (\texttt{lam1}\ T)\ (a\ T)\ (b\ T)\ (J_T\ T))\to 0<c_\infty\to\texttt{CoeffMoments}\ \dots\ c_\infty^{-1} ✓✓$$
$$\qquad \text{且}\ J_T\ T：＝\tfrac2{(P.L\ T)^{3}}l\ T\!\int_0^{P.L\ T}\!\big(F.D\ (y/l\ T)\cdot(Pf\ T).g\ T\ y\big) ✓$$
$$\texttt{CertFlat}：\exists\lambda\in[\tfrac12,1)：0.85838<2-\kappa_\Xi(\lambda,vFlat)\ \wedge\ 0.92919<\tfrac32-\kappa_\Xi(\lambda,vFlat)/2 ✓$$
$$\qquad （\text{注释}：1/c\le\frac{100905635384}{88388425125}+\varepsilon_9\le1.1416163\ \text{于}\ \lambda=1 ⟹ 2-1/c\ge0.8583837）✓$$
$$\texttt{CertQuartic}：v(s)=1-\tfrac7{100}(2s)^{2}-\tfrac{51}{200}(2s)^{4};\qquad 0.86864<2-\kappa_\Xi(\lambda,vQuartic)\ \wedge\ 0.93432<(\cdots) ✓$$
$$\qquad （1/c\le\frac{277244140547469154168336}{245053976636191319722125}+\varepsilon_9\le1.1313598 ⟹ \ge0.8686402／0.9343201）✓$$
$$\kappa_\Xi(\lambda,v)：＝1/c_\lambda(v;D_1)\（\texttt{Defs.kappaXi}\ \text{＋ FULL series}\ D_1）✓$$

---

## §2 ⚠️ **三类量词/域差异（本档核心发现）**

$$\text{(A)}\ \textbf{严格不等式}\ \texttt{P.lam}<1：\text{producer 前提逐字};\ \text{且}\ \texttt{CertFlat}／\texttt{CertQuartic}\ \textbf{只主张}\ \exists\lambda\in[\tfrac12,1)\ —— \textbf{避开}\ \lambda=1 ✓✓$$
$$\qquad \Longrightarrow \text{我 V301–V309 的}\ \lambda\le1\ \text{表述与 ThmD 的}\ \lambda<1\ \textbf{不同域};\ \text{"ceiling at}\ \lambda\le1\text{"}\ \text{须改写为}\ \sup_{\lambda<1}\ \text{＋边界讨论} ✓✓✓$$
$$\text{(B)}\ \tfrac12\le\texttt{AdmWindow.bv}：\text{显式列在 producer 前提里} ⟹ \textbf{硬条件}（消费链上）✓✓$$
$$\text{(C)}\ \texttt{ThmD.AdmWindow}\ \varphi\ L\ w\ c：\text{带常数}\ c\ \text{的谓词}（\text{在}\ \texttt{Zeta23/ThmD/}）\ —— \textbf{本档未读到} ⚠️✓$$
$$\qquad \Longrightarrow \text{这三项}\ \textbf{都不是} \text{算子性质}，\text{正是你要求查的}\ \textbf{量词／定义域} ✓✓✓$$

---

## §3 ⭐ **候选核对（`WindowProfile` 四条件；含关键重标）**

$$\text{我的候选}：v_\lambda(x)=\frac{w}{\sin w}\cos(2wx)\ (w=\lambda/\sqrt2) ✓$$
$$\qquad \text{even}\ ✓（\cos\ \text{偶}）;\qquad \texttt{ContDiff}\ \mathbb R\ 3\ ✓（\text{解析}）;\qquad \texttt{pos}\ ✓（\text{V308}：\cos(2wx)\ge\cos w>0\ \text{当}\ |x|\le\tfrac12,w<\tfrac\pi2）✓$$
$$\qquad ⚠️\ \texttt{le\_one}\ \textbf{✗}：v_\lambda(0)=\frac w{\sin w}>1\（0<w<\tfrac\pi2\ \text{时}\ \sin w<w）✓✓$$
$$\textbf{修正（关键）}：\text{比值}\ \frac{\lambda(\int v)^{2}}{Q(v)}\ \textbf{在}\ v\to tv\ \textbf{下不变} ⟹ \text{可任意重标} ✓✓$$
$$\qquad \text{取}\ \boxed{\tilde v_\lambda(x)：＝\cos(2wx)} ⟹ \tilde v(0)=1,\ \textbf{且}\ 0<\tilde v\le1\ \text{于}\ [-\tfrac12,\tfrac12] ✓✓✓$$
$$\qquad \Longrightarrow \boxed{\tilde v_\lambda\ \textbf{满足 `WindowProfile` 全部四条件}}\（\text{even}\ ✓\ C^{3}\ ✓\ \text{pos}\ ✓\ \texttt{le\_one}\ ✓）✓✓✓$$
$$\qquad \text{比值不变性核验}：\tilde v_\lambda=\tfrac{\sin w}w\cdot v_\lambda ⟹ \frac{\lambda(\int\tilde v)^{2}}{Q(\tilde v)}=\frac{\lambda(\int v_\lambda)^{2}}{Q(v_\lambda)}=\boxed{c^{*}_\lambda} ✓（\text{故重标无损}）✓✓$$

---

## §4 ⭐⭐⭐⭐⭐ **判词重构：不是集合相等，而是"极值点归属性"**

$$\mathcal A_{\rm var}：＝\{v:\ \text{比值有意义}\ (\int v\ne0,\ Q(v)>0)\ \text{＋足以推 E–L 的微性}\} ✓$$
$$\mathcal A_{\rm ThmD}\subseteq\mathcal A_{\rm var}？\ \textbf{是}（\text{ThmD 侧更强：even/}C^3/\text{pos}/\le1+\texttt{AdmWindow}+bv\ge\tfrac12+\lambda<1）✓$$
$$\mathcal A_{\rm var}\subseteq\mathcal A_{\rm ThmD}？\ \textbf{否}（\text{var 允许非偶、可变号、无界}）⟹ \boxed{\mathcal A_{\rm var}\ \textbf{STRICT SUPERSET}\ \mathcal A_{\rm ThmD}} ✓✓✓$$
$$\Longrightarrow \textbf{故正确命题不是"集合相等"}，\text{而是}：\boxed{\tilde v_\lambda\in\mathcal A_{\rm ThmD}\ \text{？}}$$
$$\qquad \text{若}\ \checkmark：\text{因}\ \sup_{\mathcal A_{\rm var}}=\tilde v_\lambda\ \text{（\text{V307–V309} 已闭）} ⟹ C_{\rm ThmD}(\lambda)=c^{*}_\lambda\ \text{（\text{在}\ \lambda<1\ \text{内}）} ✓✓✓$$
$$\qquad ⟹ \text{0.67250 可升为}\ \textbf{"链内已证"}\（\text{域}\ \lambda<1;\ \text{边界另行}）✓$$

---

## §5 **精确 GAP ＝ 三个具体命题**

$$\text{P1}：\textbf{读}\ \texttt{Zeta23/ThmD/*.lean}\ \text{中}\ \texttt{AdmWindow}\ \text{的定义}，\text{判定}\ \tilde v_\lambda\ \text{是否满足}（\text{含常数}\ c\ \text{的角色}）✓$$
$$\text{P2}：\text{核对}\ \tfrac12\le\texttt{AdmWindow.bv}\ \text{对}\ \tilde v_\lambda\ \text{（按}\ \texttt{bv}\ \text{的定义算}）✓$$
$$\text{P3}：\text{决定"ceiling"陈述的正确域}\ \lambda<1\ \text{vs}\ \lambda\le1\ \text{（}\texttt{CertFlat}／\texttt{CertQuartic}\ \text{用}\ \exists\lambda\in[\tfrac12,1)\text{）✓✓}$$
$$\qquad ⚠️\ \textbf{另附重大副产品（须降级）}：\text{ξ′ 版本常数}\ \textbf{远高于} \text{ζ 版本}（\texttt{CertFlat}\ 2-1/c\ge0.8583837;\ \texttt{CertQuartic}\ge0.8686402\ \text{vs ThmD}\ 0.6725）$$
$$\qquad \qquad ⟹ \text{V303 §3 的"路线图＝}c^{*}_\lambda\text{、两机制统一"}\ \textbf{降为[待复核]}（\text{ξ′ 与 ζ 是不同定理、不同常数}）✓✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

| 项 | 状态 | 依据 |
|:--|:--|:--|
| `WindowProfile` 四条件（候选） | **✓**（重标后 $\tilde v_\lambda=\cos(2wx)$） | §4 原文 ＋ V308 pos |
| `le_one` | **✗ 原式 → ✓ 重标后** | §3 |
| $\mathcal A_{\rm var}\supseteq\mathcal A_{\rm ThmD}$ | **✓ STRICT SUPERSET** | §4 |
| `AdmWindow` 谓词 | **未读 ⟹ P1** | §5 |
| $bv\ge\tfrac12$ | **未核 ⟹ P2** | §5 |
| $\lambda<1$ vs $\lambda\le1$ | **域差异 ⟹ P3** | §2(A) |

```
① ⚠️ §1 的 §4 摘录为**直读转述**（非逐字全文）；`CertFlat`／`CertQuartic` 的分数界未逐位复核 ⚠️
② ⚠️ §3 的"比值尺度不变"为标准事实（本档已给核验式）✓
③ ⚠️ §5 的"ξ′ vs ζ 常数差异"仅从 `CertFlat/CertQuartic` 的数值与 ThmD 的 0.6725 并列观察 ⟹ **[待复核]** ✓
④ **不声称** $\tilde v_\lambda\in\mathcal A_{\rm ThmD}$（P1/P2 未做）；**不声称** 0.67250 已升格 ✓
⑤ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐⭐ **判词重构**：$$\mathcal A_{\rm var}\ \textbf{STRICT SUPERSET}\ \mathcal A_{\rm ThmD}\ \Longrightarrow\ \text{正确命题＝}\tilde v_\lambda\in\mathcal A_{\rm ThmD}？$$（非集合相等）✓✓✓
② ⭐⭐⭐⭐ **候选通过 `WindowProfile` 四条件**（重标 $\tilde v_\lambda=\cos(2wx)$；原 $w/\sin w$ 违反 `le_one`，重标无损）✓✓✓
③ ⭐⭐⭐ **三类量词/域差异到手**：$\texttt{P.lam}<1$（严格，且 Cert 避开 $\lambda=1$）／$\tfrac12\le bv$／`ThmD.AdmWindow` ✓✓✓
④ ⚠️ **精确 GAP ＝ P1/P2/P3**（三个具体命题，非"似乎需补充"）✓
⑤ ⚠️ **副产品**：ξ′（0.8584／0.8686）vs ζ（0.6725）常数差异 ⟹ V303 §3 统一降为[待复核] ✓
【下一步（唯一入口）】
  **P1**：读 `Zeta23/ThmD/` 下的 `AdmWindow` 定义（`Window.lean`／`Limit.lean`／`Defs.lean`）⟹ 判 $\tilde v_\lambda$ 归属；随后 P2（$bv$ 下界）与 P3（域 $\lambda<1$）✓
```
