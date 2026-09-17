# 🔬 **变量—对象—相位 三级对齐审计** ⟹ **UB-θ 属"对象偷换"；W6 的真实相位是 log 变量的线性相位**

> 依唐先生 15:49「必须先做记法对齐，且升级成对象对齐审计」＋ `N13`（须取原文，不凭印象）✓
> **本档结果**：三档原文逐字取回；⭐⭐⭐ **W6 相位的自变量＝$U=\log n$（非谱变量）**；⟹ **UB-θ-2 判据 $n_\theta\gg L U^2$ 系跨坐标假判据**；UB-3C 的线性模型**正是 W6 的模型**✓✓✓

---

## §1 `E91` 原文逐字（`docs/E91-abel-numeric-criterion.md`）
$$\phi(t)=n\theta(t),\qquad \theta(t)=2\arctan\frac1{2t},\qquad \phi'(t)=n\theta'(t)=-\frac{4n}{4t^2+1}✓$$
$$\text{带}\ I=[\sqrt{n/11},\sqrt n]:\quad u:=\frac t{\sqrt n}\in[0.3015,\,1] \Longrightarrow |\phi'|=\frac1{u^2}\in[\boxed{1,\,10.98}]✓✓$$
$$\text{结构澄清（逐字）}：\phi'\ \textbf{不是} \text{固定幂次的}\ \log\ \text{结构，而是}\ \textbf{尺度不变幂律}\ n/t^2✓$$
$$\Longrightarrow \boxed{\text{E91 的相位自变量＝}\textbf{高度}\ t}；\ n\ \text{是}\ \textbf{系数}；\ u=t/\sqrt n\ \text{是无量纲}\ \textbf{谱变量}✓✓$$

## §2 `W6` 原文逐字（`docs/W6-MAJORANT-1-verbatim-source-and-jam-step.md`／`TA-W6-3-…`）
$$P_X(\tau)=-\frac1{2\pi}\sum_na_n\big(n^{i\tau}+n^{-i\tau}\big),\qquad a_n=\frac{\Lambda(n)}{\sqrt n}✓\qquad(\textbf{此处}\ \tau\ \text{＝谱变量，属多项式})✓$$
$$O_1=\frac1{2\pi^2}\mathrm{Re}\sum_{n\ne m}\frac{a_na_m}{i(y_n-y_m)}\Big[\Big(\frac nm\Big)^{2iT}\big(\alpha_m^++\alpha_n^-\big)-\Big(\frac nm\Big)^{iT}\big(\alpha_n^++\alpha_m^-\big)\Big]✓$$
$$y_n=\log n,\qquad \vartheta=y_n-y_m=\log\frac nm✓\qquad \Big(\frac nm\Big)^{iT}=e^{\,iT\log(n/m)}✓✓$$
$$\Longrightarrow \boxed{\text{W6 的振荡相位＝}\ T\cdot\log\frac nm}\ \text{——}\textbf{自变量是 log 变量}；\ T\ \text{是}\ \textbf{斜率（乘子）}✓✓✓$$
$$\text{离对角核（逐字）}：K(h)=K(y_n-y_m)=K(\log(n/m))✓$$

## §3 ⭐⭐ 三级对齐表（本档核心）
| 档案对象 | 统一符号 | 数学角色 | 能否等同 HB 的 $U=\sum\log m_i$ |
|:--|:--|:--|:--:|
| W6/Prop5.4: $y_n=\log n$、$\log(n/m)$ | $U$ | **相位自变量（log 变量）** | **是** ✓✓ |
| W6: $T$（高度） | $\tau_{\rm sp}$ | **斜率／乘子**（$e^{i\tau_{\rm sp}U}$）| 否（是系数）|
| W6: $P_X(\tau)$ 的 $\tau$ | $\tau$ | 谱变量（多项式自变量）| **否** ✗ |
| E91: $t$（高度） | $t$ | **相位自变量（高度）** | **否** ✗ |
| E91: $u=t/\sqrt n$ | $v$ | 无量纲谱变量（带 $[0.3015,1]$）| **否** ✗ |
| E91/$\theta$ 的整数 $n$ | $n_\theta$ | 相位**系数** | **否** ✗（与 HB 的 $n$ 同名异物）|
| T1: $r,t$（BCR 统一化） | $r,t$ | 指数坐标（$17r+t$ 型）| **否** ✗ |

## §4 ⭐⭐⭐ 判决
$$\boxed{\text{① W6 的相位＝}\textbf{log 变量}\ \text{的}\ \textbf{线性相位}（\text{斜率}\ T）\ ⟹ \textbf{UB-3C 的线性模型正是 W6 的模型}}✓✓✓$$
$$\boxed{\text{② 我的 UB-}\theta\ \text{把}\ \textbf{E91 的相位}\ \phi(u)=-\frac{4n_\theta u}{4u^2+1}\ \text{移植进 log 变量}\ u\ ⟹ \textbf{对象偷换}}✗✗✓$$
$$\qquad \text{故}\ \boxed{n_\theta\gg L U^2\ \textbf{是跨坐标假判据}}\ ——\ \text{唐先生的怀疑}\ \textbf{成立}✓✓✓$$
$$\qquad 📌\ \text{正确关系}：\text{UB-}\theta\text{-1/2 的}\ \phi\ \text{属于}\ \textbf{E91 坐标系}（\text{自变量＝高度}\ t），\ \text{不属于 HB/W6 坐标系}✓✓$$
$$\boxed{\text{③ E91 自身：}|\phi'|\in[1,10.98]\ \textbf{有界} \Longrightarrow \textbf{非驻相压制不适用}⟹ \text{与 E91 的定量失败一致}（\Lambda_I=16.94\gg0.38）✓✓}$$
$$\qquad \text{且 E91 路线 B}＝\text{E79′}（\text{相位坐标 Fourier 抵消已被用过}）⟹ \textbf{循环}✓✓$$

## §5 判词
$$\boxed{\text{① 撤销：}\ n_\theta\gg LU^2\ \text{作为主线判据（跨坐标伪造）}}✓✓✓$$
$$\boxed{\text{② 保留：}\ \text{UB-3C 的结论（线性相位}\Longrightarrow\text{局部强振荡}\Longrightarrow\text{非对角压制）——}\textbf{它才是 W6 侧的正确模型}}✓✓✓}$$
$$\qquad(\text{因 W6 相位}\ =\ T\cdot U\ \text{恰为 UB-3C 的}\ \phi(u)=tu\ \text{型，}\ t\leftrightarrow T)✓✓$$
$$\boxed{\text{③ UB-}\theta\text{ 的}\ G_i／R_i\ \text{公式}\ \textbf{本身有效}，但只适用于}\ \textbf{E91 坐标系}；\ \text{不可回灌 W6}}✓✓$$
$$\Longrightarrow \text{C2 的现状}：\textbf{W6 侧（线性相位）已压制}；\ \textbf{E91 侧（有界}\ \phi'\text{）属另一机制，且已被}\ \text{E91/E79′}\ \text{判为循环}✓✓$$

## §6 边界
$$\text{(i)}\ §1--§2\ \textbf{逐字取原文}（`N13` 已执行）✓✓；\ §3\ \text{为对齐判断}；\ §4\ \text{为}\ [\textbf{结构}] \text{级判决}✓$$
$$\text{(ii)}\ ⚠️\ \text{未逐字核}：T1 档（\texttt{T1-2-r-t-template-extraction.md}\ 等）\ \text{的}\ r,t\ \text{定义——本档仅按其"统一化坐标"性质标注}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零数值}；\ \text{本档}\ \textbf{只做对齐}，\ \text{不新增机制}✓✓$$
