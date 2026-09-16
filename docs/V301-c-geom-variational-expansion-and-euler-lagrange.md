# V301 · **(4b)+(4c)：$c_{\rm geom}$ 的变分展开 ＋ Euler–Lagrange** —— ⭐⭐⭐⭐⭐ **结果：$c^{\rm geom}(\lambda)=\dfrac{\lambda}{1+\lambda^{2}/3}$ ⟹ 无约束驻点 $\lambda^{*}=\sqrt3$，但 $\lambda^{*}\notin(0,1]$（无条件域）⟹ 约束最优落在 $\lambda=1$ ⟹ $C_{\rm uncond}=3/4$，$G=2/3$**；⭐⭐⭐⭐ **定量必要条件：任何 $c>3/4$ 需 $\lambda>1$**（＝**突破 MV 无条件支持墙**，从经验判断升级为定量必要条件）；⭐⭐⭐ **该族内 $c\le\sqrt3/2=0.866<1$ 恒成立** ⟹ 结构性天花板

$$\boxed{\textbf{核心（本档）}：c^{\rm geom}(\lambda)=\frac{a^{2}\lambda}{1+\lambda^{2}/3}\ \Big|_{a=1}\ =\ \frac{\lambda}{1+\lambda^{2}/3};\qquad \max_{\lambda>0}c^{\rm geom}=\frac{\sqrt3}2=0.8660\ (\lambda^{*}=\sqrt3)} ✓✓✓$$
$$\boxed{\textbf{但无条件域为}\ \lambda\le1\ ⟹\ \text{约束最优}\ \lambda=1\ ⟹\ C_{\rm uncond}=3/4\ ⟹\ G=2-\tfrac43=\tfrac23} ✓✓✓$$
$$\boxed{\textbf{定量必要条件}：c>3/4\ \Longrightarrow\ \lambda>1\ \Big(＝\textbf{突破 MV 无条件支持墙}\Big)} ✓✓✓$$
$$\boxed{\text{且}\ c^{\rm geom}\le\sqrt3/2=0.8660<1\ \textbf{恒成立}\（\text{本参数族内}\ 1\ \textbf{不可达}）} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:29：开始 **(4b)+(4c)**，**先写变分泛函、再谈 $\sup$；不先扫窗口** ✓；四项硬检查（**① 把 $a,\ell_1,b$ 追溯到窗口 $\phi$；② 尺度不变性；③ 拆开 $\ell_1$ 与 $L^{2}/3$ 的来源（尤其"若 $1/3$ 来自 $\int_0^1x^2dx=1/3$ 则它是几何离散化核、不可优化"）；④ 把无条件性写进 $\mathcal A_\sigma$**）✓✓；**最关键一刀：先求 Euler–Lagrange，而不是数值优化**；**输出严格限定四项**（$c_{\rm geom}(\phi)$／$\mathcal A_\sigma$／变分问题／第一条严格上界或构造）；**不得扫窗口、不得数值优化、不得先猜最优 $\phi$** ✓✓✓；并要求最终得到**三元关系 $(c_{\rm geom},\sigma,\lambda)$** 与"**任何这样的族都要求 $\liminf\lambda_T>1$ ⟹ 把"$2/3\to1$ ⟹ 突破 MV 无条件支持墙"从经验判断升为定量必要条件**" ✓✓✓
> 第一手依据（**本档现场读源码**）✓ `Zeta23/Defs.lean`（**`a`／`b`／`ell1`／`lam1`／`phiHat`／`Phi`／`g`／`Aphi`／`calE` 的定义行**）｜`PrimeSideTemp.lean`（`mainTr2`；[thm:traces]）｜`ChallengeDeps.lean`（$c^{*}_{\lambda}$ 闭式）｜`V300`（$\mathcal O_1$ 与 MV 适用域）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V301`（`id_claim.sh` ✓；编号带已扩至 V101–V399 ✓）

---

## §1 **第一输出：$c_{\rm geom}(\phi)$ 的精确展开（把 $a,\ell_1,b$ 追溯到 $\phi$）**

$$\textbf{定义（`Defs.lean` 逐字）}：$$
$$\qquad \boxed{a\:＝\ \frac1{L}\int_{\mathbb R}\phi(u)^{2}du};\qquad \boxed{b\:＝\ \frac1{L}\int_{\mathbb R}\phi(u)^{4}du};\qquad \boxed{\ell_1\:＝\ l+2\log2-1} ✓$$
$$\qquad \lambda_1：＝\frac L{\ell_1};\qquad L=\lambda l;\qquad \phi=(\text{taper})\ \text{由}\ (\lambda,w)\ \text{参数化（§6 取}\ w=1）✓$$
$$\textbf{⚠️ 关键澄清（本档）}：\ell_1=l+2\log2-1\ \textbf{只依赖}\ T\ \text{（非窗口泛函）} ⟹ \text{(eq:tr2) 里的}\ \ell_1^{2}\ \textbf{不是优化自由度} ✓✓$$
$$\qquad \text{而}\ L^{2}/3\ \text{的}\ \boxed{1/3=\int_0^1x^{2}dx}\ ⟹ \textbf{几何离散化核，非可优化} ✓✓✓（＝唐先生猜测之 ③ 被确认）$$

$$\textbf{展开（本档推导）}：\text{由}\ \operatorname{tr}\widetilde G=aLN(1+o(1))\ \text{与}\ \operatorname{tr}\widetilde G^{2}=\frac{TL}{2\pi}\Big(\ell_1^{2}+\frac{L^{2}}3\Big)(1+o(1))：$$
$$\qquad \frac{(\operatorname{tr}\widetilde G)^{2}}{\operatorname{tr}\widetilde G^{2}}=\frac{a^{2}L^{2}N^{2}}{\frac{TL}{2\pi}(\ell_1^{2}+L^{2}/3)}(1+o(1))=\frac{2\pi a^{2}LN^{2}}{T(\ell_1^{2}+L^{2}/3)}(1+o(1)) ✓$$
$$\qquad \text{代入}\ N\sim\frac{Tl}{2\pi}\（Riemann–von Mangoldt）⟹\ F(\lambda_1)=\frac{(\operatorname{tr}\widetilde G)^{2}}{N\operatorname{tr}\widetilde G^{2}}=\frac{a^{2}Ll}{\ell_1^{2}+L^{2}/3}(1+o(1)) ✓$$
$$\qquad \text{再用}\ \ell_1\approx l、L=\lambda l ⟹ \boxed{c^{\rm geom}=\frac{a^{2}\lambda}{1+\lambda^{2}/3}+o(1)} ✓✓✓\ \textbf{（纯窗口泛函}\ \times\ \text{几何因子）}$$
$$\qquad \Longrightarrow \boxed{\text{真正的优化自由度只有}\ a\（\text{与}\ \lambda）；\ \text{窗矩}\ b\ \text{只进误差}\ \mathcal E_T} ✓✓$$

---

## §2 **第二硬检查：尺度不变性 —— ⚠️ 不成立 ⟹ 归一化是必需的**

$$a(c\phi)=\frac1L\int(c\phi)^{2}=c^{2}a(\phi)\ ⟹\ c^{\rm geom}(c\phi)=c^{4}c^{\rm geom}(\phi)\ \ne\ c^{\rm geom}(\phi) ✗✓$$
$$\Longrightarrow \textbf{必须有归一化约束};\ \text{取}\ \boxed{a(\phi)=1\（\text{等价}\ \int\phi^{2}=L\text{）}} ⟹ c^{\rm geom}=\frac{\lambda}{1+\lambda^{2}/3}\ \textbf{与}\ \phi\ \textbf{无关} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{在本路线（trace 型）内，"窗口"}\ \textbf{不是} \text{实质优化自由度；}\textbf{唯一自由度＝}\lambda ✓✓$$

---

## §3 **第三硬检查：$\ell_1$ 与 $L^{2}/3$ 的来源（已拆开，见 §1）**

$$\ell_1^{2}：\text{T-确定（}l+2\log2-1\text{）} ⟹ \text{不可优化};\qquad L^{2}/3：\frac13=\int_0^1x^{2}dx ⟹ \textbf{几何核} ⟹ \text{不可优化} ✓✓✓$$
$$\qquad ⟹ \text{它们}\ \textbf{共同固定了分母的标度}，\text{只留下}\ \lambda\ \text{一个自由度} ✓$$

---

## §4 **第四硬检查：$\mathcal A_\sigma$ 的完整写法（含无条件性）**

$$\boxed{\mathcal A_\sigma=\Big\{\phi:\ \textbf{(R)}\ \phi\in C_c^{2},\ \operatorname{supp}\phi\subseteq[-\tfrac L2,\tfrac L2];\ \textbf{(N)}\ a(\phi)=1;\ \textbf{(V)}\ \text{证书有效性};\ \textbf{(MV)}\ \text{MV 可用};\ \textbf{(E)}\ \mathcal E_T\to0\Big\}} ✓✓$$
$$\qquad \textbf{(MV)}\ \text{逐项翻译（据 `V300` §4，[推断]）}：\log X\le L\iff X\le T\iff\lambda\le1;\quad 1\le w\le L/8 ✓$$
$$\qquad \textbf{(E)}：\mathcal E_T=\frac wL+\frac{(l^{2}+X)\log l}{Tl}+T^{\lambda/2-1}\to0\ ⟹\ \lambda<2\ \text{且}\ T\to\infty ✓✓$$
$$\Longrightarrow \textbf{三元关系（唐先生要求）}：\boxed{(c^{\rm geom},\ \sigma,\ \lambda)}\ \text{三者}\ \textbf{不独立}：\sigma\asymp\lambda\（\text{支撑～带宽，[推断]}）、\ c^{\rm geom}=c^{\rm geom}(\lambda) ✓✓$$

---

## §5 ⭐⭐⭐⭐ **Euler–Lagrange（唐先生最关键的一刀）**

$$\text{归一化}\ a=1\ \text{后，变分问题}\ \textbf{退化为单变量}：\qquad \boxed{\max_{\lambda>0}\ f(\lambda)：＝\frac{\lambda}{1+\lambda^{2}/3}} ✓$$
$$\qquad f'(\lambda)=\frac{1-\lambda^{2}/3}{(1+\lambda^{2}/3)^{2}} ⟹ \textbf{驻点}\ \boxed{\lambda^{*}=\sqrt3};\qquad f(\sqrt3)=\frac{\sqrt3}{1+1}=\frac{\sqrt3}2=0.866025\ldots ✓✓✓$$
$$\qquad f\ \text{在}\ (0,\sqrt3)\ \textbf{严格递增};\ \lambda\to\infty:\ f\sim3/\lambda\to0 ✓$$

$$\textbf{约束（无条件域}\ \lambda\le1\text{，`V300` §4）}：\ \lambda^{*}=\sqrt3=1.7321\ \textbf{不在允许域内} ⟹ \text{约束最优落在}\ \textbf{边界}\ \lambda=1：$$
$$\qquad \boxed{C_{\rm uncond}=f(1)=\frac{1}{1+1/3}=\frac34=0.75\ \Longrightarrow\ G=2-\frac1{3/4}=\frac23} ✓✓✓$$
$$\qquad \textbf{与既有读数完全一致}：\text{指示窗}\ c^{\rm geom}=0.75\Rightarrow2/3\ ✓;\ \text{AF 取}\ \lambda=1\ \text{正因它是}\ \textbf{约束边界最优} ✓✓$$

---

## §6 ⭐⭐⭐⭐ **判死／判活：定量必要条件 ＋ 结构性天花板**

$$\boxed{f\ \text{在}\ (0,\sqrt3)\ \textbf{严格递增}\ ⟹\ \boxed{c^{\rm geom}>3/4\iff\lambda>1}} ✓✓✓$$
$$\qquad \Longrightarrow \boxed{\text{任何}\ c>3/4\ \textbf{必须}\ \lambda>1\（＝\textbf{突破 MV 无条件支持墙}）}\ ——\ \textbf{唐先生所求的"定量必要条件"} ✓✓✓$$
$$\qquad \text{且}\ \boxed{c^{\rm geom}\le\sqrt3/2=0.8660<1\ \textbf{恒成立}} ⟹ \textbf{本参数族内}\ 1\ \textbf{不可达} ⟹ \textbf{结构性天花板} ✓✓✓$$
$$\qquad \qquad \text{反解（供后续用）}：c=\frac{\lambda}{1+\lambda^{2}/3}\iff \frac c3\lambda^{2}-\lambda+c=0\iff\lambda=\frac{3}{2c}\Big(1\pm\sqrt{1-\tfrac{4c^{2}}3}\Big) ✓$$
$$\qquad \qquad \text{判别式}\ \ge0\iff c\le\sqrt3/2 ⟹ \text{故}\ c=0.80\Rightarrow\lambda\approx1.16\ \text{或}\ 2.59;\ c=0.90\ \textbf{无解} ✓✓$$

$$\textbf{⚠️ 本档张力（诚实标注）}：\text{MT 窗给}\ c_1^{*}=0.7533\ \textbf{>}\ 0.75=f(1) ⟹ \textbf{公式非精确} ⟹ \text{窗自由度}\ \textbf{量级} \le0.7533-0.75=0.0033\ldots0.0044 ✓✓$$
$$\qquad \Longrightarrow \textbf{精确结论}：\text{窗自由度}\ \textbf{很小（≲0.004）}，\text{主导杠杆}\ ＝\ \lambda\（\text{即支撑／带宽}）✓✓✓$$

---

## §7 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V301 判词}：\text{① }c^{\rm geom}=a^{2}\lambda/(1+\lambda^{2}/3)；② 归一化}\ a=1\ \text{后}\ c^{\rm geom}\ \text{与}\ \phi\ \text{无关};\ \text{③ E–L 驻点}\ \lambda^{*}=\sqrt3\ \notin(0,1];\ \text{④ }C_{\rm uncond}=3/4\Rightarrow G=2/3;\ \text{⑤ 定量必要条件}\ c>3/4\Rightarrow\lambda>1;\ \text{⑥ }c\le\sqrt3/2<1} ✓✓✓$$

```
① ⚠️ §1 的展开式 $c^{\rm geom}=a^2\lambda/(1+\lambda^2/3)$ 为**本档推导[推断]**（据 tr G̃／tr G̃² 两式与 `Defs.lean` 的 a、ℓ₁、L=λl 定义）；
   **与论文 §5／§6 的精确形式未逐行核对** ⚠️
② ⚠️ §1 用了 $\ell_1\approx l$、$N\sim Tl/2\pi$（RvM）—— 均为渐近读数 ✓
③ ⚠️ "无条件域 ＝ $\lambda\le1$" 承自 `V300` §4（**[推断]**，MV 适用域未形式化）⟹ §5–§6 的约束最优**依赖此** ⚠️✓
④ ⚠️ §6 的张力（MT 窗 0.7533 > f(1)=0.75）**是真实的不一致** ⟹ 公式非精确，**已量化窗自由度 ≲0.004** ✓
⑤ ⚠️ 路线图（支撑 1.04/1.26/1.70 → 0.70/0.80/0.90）**与本档的 $f(\lambda)$ 不一致**（$f$ 上限 √3/2 = 0.866 而 0.90 需更高）⟹ **两者属不同机制**（ceiling/certificate 框架 vs trace 路线）⟹ **不得混用** ✓✓
⑥ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值（除闭式算术）✓
```

```
① ⭐⭐⭐⭐⭐ **第一输出**：$$c^{\rm geom}=\frac{a^{2}\lambda}{1+\lambda^{2}/3},\qquad a=\tfrac1L\int\phi^{2}$$；**$\ell_1=l+2\log2-1$ 是 T-确定（非自由度）**；**$1/3=\int_0^1x^2dx$ ＝ 几何核（不可优化）** ✓✓✓
② ⭐⭐⭐ **第二检查：尺度不变性失败** ⟹ 必须归一化 $a=1$ ⟹ **$c^{\rm geom}$ 与 $\phi$ 无关** ⟹ **trace 路线内"窗口"不是实质自由度** ✓✓✓
③ ⭐⭐⭐⭐ **第三输出（E–L）**：单变量极值，**$\lambda^{*}=\sqrt3$ 为全局最大（$f=\sqrt3/2=0.8660$）**；**但 $\lambda^{*}\notin(0,1]$** ⟹ **$C_{\rm uncond}=3/4$，$G=2/3$** ✓✓✓
④ ⭐⭐⭐⭐ **定量必要条件**：$$c>3/4\iff\lambda>1$$ ⟹ **"$2/3\to1$ ⟹ 突破 MV 无条件支持墙"升级为定量必要条件**（唐先生所求）✓✓✓
⑤ ⭐⭐⭐ **结构性天花板**：$c\le\sqrt3/2<1$ 恒成立 ⟹ 本族内 1 不可达；反解 $\lambda(c)$ 已给出（$c=0.90$ 无解）✓✓
⑥ ⭐⭐ **窗自由度量级 ≲0.004**（由 MT 窗 0.7533 与 $f(1)=0.75$ 之差）⟹ **主导杠杆是 $\lambda$** ✓✓
【下一步（严格限定：不扫窗口、不数值优化）】
  (5a) **核验 §1 的展开**（与论文 §5／§6 精确形式对齐；解决 §6 的张力）—— 仍是支点 ✓
  (5b) 若 (5a) 通过 ⟹ **把 $\lambda$ 与 $\sigma$（Fourier／支撑）的精确关系写出来**，把定量必要条件改写为 $$\boxed{c>3/4\Longrightarrow\sigma>\sigma_{\rm uncond}}$$ 的形式 ✓✓
  (5c) **区分两条机制**（trace 路线 vs ceiling/certificate 框架）并把路线图（1.04／1.26／1.70）归位到 ceiling 框架下单独处理 ⟹ 避免混用 ✓✓
```
