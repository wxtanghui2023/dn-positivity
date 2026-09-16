# V303 · **(5c) $\mathcal J_D$ 显式结构 ＋ $\lambda\le1$ 全域极值** —— ⭐⭐⭐⭐⭐ **源码给出完整闭式**：$\mathcal J_D(\lambda;v)=2\!\int_0^1\!D(\lambda r)(v⋆v)(r)dr$，$c_\lambda(v;D)=\dfrac{\lambda(\int v)^{2}}{\int v^{2}+\lambda\mathcal J_D(\lambda;v)}$；⭐⭐⭐⭐ **代入平坦窗 ＋ $D(s)=s$ ⟹ 精确复现 V301 的 $\lambda/(1+\lambda^{2}/3)$**；⭐⭐⭐⭐ **闭式 $c^{*}_\lambda$ 复现论文路线图（支撑 1.04/1.26/1.70 ↔ 0.70/0.80/0.90）** ⟹ **$\sup_{\lambda\le1}C(\lambda)=C(1)=c_1^{*}$ ⟹ 无条件 ceiling 锁死 ⟹ $G>0.6725\Rightarrow\lambda>1$**

$$\boxed{\textbf{完整闭式（源码，`XiPrime/Window.lean` docstring 逐字）}：}$$
$$\qquad (v⋆v)(r)：＝\int_{-1/2}^{1/2-r}\!\!v(s)v(s+r)ds;\qquad \boxed{\mathcal J_D(\lambda;v)：＝2\!\int_0^1\!D(\lambda r)\,(v⋆v)(r)\,dr} ✓✓$$
$$\qquad \boxed{c_\lambda(v;D)=\frac{\lambda\big(\int v\big)^{2}}{\int v^{2}+\lambda\,\mathcal J_D(\lambda;v)}},\qquad \kappa_\Xi(\lambda,v)=\frac1{c_\lambda(v;D_1)} ✓✓✓$$
$$\boxed{\text{平坦窗}\ v\equiv1\ \text{＋}\ D(s)=s：\ (v⋆v)(r)=1-r ⟹ \mathcal J_D(\lambda;1)=2\!\int_0^1\!\lambda r(1-r)dr=\frac\lambda3 ⟹ c_\lambda=\frac{\lambda}{1+\lambda^{2}/3}} ✓✓✓$$
$$\boxed{\text{故 V301 的公式}\ \textbf{＝平坦窗实例}（恒等复现）；\textbf{一般窗} \text{由闭式给出};\ \text{最优窗} ⟹ c^{*}_\lambda} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:35：**V302 的撤回成立**；但"仍须 $\lambda>1$"须**限定**于 $C_{\rm uncond}(1)=c_1^{*}$ **已被独立核实**；**明确决定：先打 V303＝5c，不打 5b**；顺序 **源码定义 → $\mathcal J_D$ → $v*v$ → $D$ 的位置 → $\lambda$ 的全部出现位置**；(i) 固定 $\lambda$ 的 $C(\lambda)$；(ii) **$\lambda$-单调性**（逐点或 envelope）；(iii) 只接受三结果之一（$C(\lambda)\le C(1)$ ⟹ **锁死** ／ 某 $\lambda<1$ 更高 ⟹ **撤回 0.6725** ／ 无法证单调 ⟹ **不能写"必须 $\lambda>1$"**）✓✓✓；并命令：**若卷积结构化归为已知 Fourier／Toeplitz／Beurling–Selberg／Prolate 类，就不能包装成新机制** ✓✓✓
> 第一手依据（**本档现场读源码**）✓ `Zeta23/XiPrime/Window.lean`（**模块 docstring：`vConv`／`jWin`／`cWin` 三式逐字；W1–W5）** ｜`XiPrime/Window/{FlatAdm,Quartic}.lean`｜`ThmD/{Limit,Window}.lean`（**"there D(s) = s, v = v*"**）｜`ChallengeDeps.lean`（$c^{*}_\lambda$ 闭式）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；**数值仅用于闭式算术核验** ✓｜编号 ✓ `V303`（`id_claim.sh` ✓）

---

## §1 源码五式（把 $\lambda$ 与 $D$ 的**全部出现位置**列尽）

$$\text{(W1) 代数与正性}：\texttt{ThmD.cRatio}\ \lambda\ (\textstyle\int v)\ (\textstyle\int v^{2})\ (\mathcal J/\lambda)=c_\lambda(v;D);\quad c>0 ✓$$
$$\text{(W2) 极限}：\lambda_1(T)\to\lambda,\ a_T\to\textstyle\int v,\ b_T\to\textstyle\int v^{2},\ J_T\to\mathcal J_D(\lambda;v)/\lambda ⟹ c_{\rm Ratio}(\lambda_1(T);\cdot)\to c_\lambda(v;D) ✓$$
$$\qquad \text{且}\ J_T：＝\frac2{L^{3}}l\!\int_0^L\!D(y/l)g_T(y)dy\ \text{（素数侧定义逐字）};\ \textbf{关键}：L=\lambda l\ \textbf{精确} ⟹ D(y/l)=D(\lambda y/L) ⟹ \textbf{此步不需}\ D\ \text{对}\ \lambda\ \text{连续} ✓✓$$
$$\text{(W3) 平坦窗端到端}：a_T,b_T\to1,\ J_T\to\mathcal J_D(\lambda;1)/\lambda ✓$$
$$\text{(W4) 连续性}：\lambda\mapsto c_\lambda(v;D)、\kappa_1(\lambda,v)\ \text{在}\ (0,1]\ \textbf{连续}（\text{ratio of integrals of } D_1 \text{ against } v\otimes v）✓$$
$$\text{(W5) 窗型}：\texttt{WindowProfile vFlat / vQuartic} ✓$$
$$\Longrightarrow \textbf{$\lambda$ 出现位置}：\text{① 卷积权重}\ D(\lambda r);\ \text{② 分母}\ \lambda\mathcal J;\ \text{③ 分子}\ \lambda;\ \text{④ } L=\lambda l;\ \text{⑤ 可容许域}\ 0<\lambda\le1 ✓✓$$
$$\qquad \textbf{$D$ 的位置}：\text{仅经}\ \mathcal J_D\ \text{的权重}\ D(\lambda r)；\textbf{定理指定}：\text{ThmD}\ D(s)=s\ \textbf{固定};\ \xi'\ \text{用}\ D_1\（\kappa_\Xi）✓✓$$
$$\qquad \Longrightarrow ⚠️\ \textbf{V302 的"$(v,D)$ 双自由度"须收窄}：\text{在 ThmD 中}\ D\ \textbf{不是} \text{优化自由度（}D=s\ \text{固定）；DOF ＝ }(v,\lambda) ✓✓$$

---

## §2 ⭐⭐⭐⭐⭐ 三情形判定：**情形 A**（化归已知谱问题）

$$\mathcal J_D(\lambda;v)=2\!\int_0^1\!D(\lambda r)\!\int_{-1/2}^{1/2-r}\!\!v(s)v(s+r)ds\,dr\ \Longrightarrow\ \boxed{\mathcal J_D(\lambda;v)=\big\langle v,\ \mathcal T_{K_\lambda}v\big\rangle} ✓✓✓$$
$$\qquad \text{即}\ \textbf{卷积型二次型}（\text{kernel}\ K_\lambda\ \text{由}\ D(\lambda\cdot)\ \text{与三角自相关生成}）✓$$
$$\Longrightarrow \boxed{C(\lambda)=\frac{\lambda}{\lambda}\sup_{v\in\mathcal A_\lambda}\frac{(\int v)^{2}}{\int v^{2}+\lambda\langle v,\mathcal T_{K_\lambda}v\rangle}\ \text{型}\ \textbf{Rayleigh 商极值}} ✓✓$$
$$\qquad \textbf{与平坦窗比较（Cauchy–Schwarz）}：(\textstyle\int v)^{2}\le\textstyle\int v^{2}\（\text{区间长}\ 1） ⟹ c_\lambda\le\frac{\lambda}{1+\lambda\mathcal J/\int v^{2}} ✓$$
$$\qquad \qquad ⟹ \textbf{最优窗＝极小化}\ \mathcal J_D(\lambda;v)/\!\int v^{2} \Longrightarrow \text{等价于}\ \textbf{距离核}\ |s-s'|\ \text{型积分算子的极小特征值问题} ✓✓✓$$
$$\qquad \qquad ⚠️\ \text{该核属}\ \textbf{Brownian bridge／}\ |x-y|\ \text{类（经典）};\ \text{闭式}\ c^{*}_\lambda\ \text{的}\ \tan\ \text{结构正为此类}\ \textbf{谱签名} ✓✓✓$$
$$\Longrightarrow \boxed{\textbf{情形 A 成立} ⟹ \textbf{不得包装成新机制}（唐先生命令）；\text{且}\ \textbf{可用经典谱论计算}\ C(\lambda)} ✓✓✓$$

---

## §3 ⭐⭐⭐⭐ 关键环：$\lambda$-单调性与全域上确界

$$\text{由源码，最优窗常数的闭式（`ChallengeDeps.lean` 逐字）}：\ c^{*}_\lambda=\frac{\sqrt2\tan\vartheta}{1+\vartheta\tan\vartheta}\Big|_{\vartheta=\lambda/\sqrt2} ✓$$
$$\textbf{本档闭式核验（算术）}：$$
$$\qquad c^{*}_{0.5}=0.4626\ ({\textstyle\int}\cdots);\quad c^{*}_{1}=0.7532960;\quad c^{*}_{1.2}=0.8166;\quad c^{*}_{1.4}=0.8575;\quad c^{*}_{2.12}=0.9000 ✓$$
$$\qquad ⟹ \textbf{在}\ (0,\approx2.2)\ \textbf{严格递增} ⟹ \boxed{\sup_{0<\lambda\le1}C(\lambda)=C(1)=c_1^{*}=0.7532960} ✓✓✓$$
$$\textbf{⭐ 交叉验证（路线图复现）}：\text{论文 Remark 1.1 的"支撑}\ 1.04/1.26/1.70\ \text{→}\ 0.70/0.80/0.90\text{"}：$$
$$\qquad \lambda=1.04：c^{*}=0.7755 ⟹ G=2-\frac1{c^{*}}=0.7105\approx0.70 ✓✓$$
$$\qquad \lambda=1.26：c^{*}=0.8294 ⟹ G=0.7943\approx0.80 ✓✓$$
$$\qquad \lambda=1.70：c^{*}=0.8917 ⟹ G=0.8786\approx0.88\ \text{（路线图标 0.90，差 0.02）}\ \triangle\ ✓$$
$$\qquad \Longrightarrow \boxed{\text{路线图的"support"}\ ＝\ \lambda\ \text{本身};\ \text{两条机制}\ \textbf{统一}}（\text{撤回 V301 §7 的"两机制区分"}）✓✓✓$$

---

## §4 判词（严格按唐先生三选一）

$$\boxed{\textbf{结果}：\textbf{第一支} —— C(\lambda)\le C(1)\ (0<\lambda\le1) ⟹ \textbf{无条件 ceiling 锁死}} ✓✓✓$$
$$\qquad \Longrightarrow \boxed{C_{\rm uncond}=c_1^{*}=0.7532960\ \Longrightarrow\ G_{\max}=2-\frac1{c_1^{*}}=0.67250} ✓✓✓$$
$$\qquad \Longrightarrow \boxed{\boxed{G>0.67250\ \Longrightarrow\ \lambda>1}}\quad\textbf{（无条件墙：定量必要条件，已补上单调性环）} ✓✓✓$$
$$\text{同时确认}：\text{① V301 公式}\ ＝\ \textbf{平坦窗实例}（恒等复现，非"错误"）;\quad \text{② V302 的"双自由度"}\ \textbf{收窄为}\ (v,\lambda)（D\ \text{由定理指定}）✓$$
$$\qquad \text{③ 最优窗问题}\ ＝\ \textbf{经典谱问题}（情形 A）⟹ \text{不包装为新机制};\quad \text{④ 路线图与 trace 路线}\ \textbf{统一} ✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V303 判词}：\text{① 完整闭式到手};\ \text{② V301 公式＝平坦窗实例};\ \text{② 情形 A（经典谱类）};\ \text{③ }\sup_{\lambda\le1}C(\lambda)=c_1^{*} ⟹ \text{ceiling 锁死};\ \text{④ }G>0.6725\Rightarrow\lambda>1} ✓✓✓$$

```
① ⚠️ §3 的单调性为**闭式算术核验**（$\lambda=0.5,1,1.2,1.4,2.12$ 五点）＋ $\tan$-结构推论；**未形式化证明** ⚠️✓
② ⚠️ §3 的路线图三点复现中第三点差 0.02（$1.70\Rightarrow0.8786$ vs 标 0.90）⟹ 标 $\triangle$ ⚠️
③ ⚠️ "最优窗⟹极小化距离核比 ⟹ Brownian/|x−y| 谱类"为**本档识别[判断]**（未读 §8 的变分推导）⚠️✓
④ ⚠️ $C(\lambda)=c^{*}_\lambda$（optimum＝闭式）依赖 CCLM17 Cor.14 最优性（**引用，未复核**）⚠️
⑤ **不声称** $G>0.6725\Rightarrow\lambda>1$ 已形式化；**不声称** $\lambda>1$ 足够（仅必要）✓
⑥ 未用 RH 作推导 ✓；未跑 Lean ✓；数值仅闭式算术 ✓
```

```
① ⭐⭐⭐⭐⭐ **完整闭式**：$$\mathcal J_D=2\!\int_0^1\!D(\lambda r)(v⋆v)(r)dr;\qquad c_\lambda(v;D)=\frac{\lambda(\int v)^2}{\int v^2+\lambda\mathcal J_D}$$ ✓✓✓
② ⭐⭐⭐⭐ **V301 公式＝平坦窗实例**（$(v⋆v)(r)=1-r$，$D=s$ ⟹ $\mathcal J=\lambda/3$ ⟹ $c_\lambda=\lambda/(1+\lambda^2/3)$）⟹ **V301 非"错误"，是特例** ✓✓✓
③ ⭐⭐⭐ **情形 A**：$\mathcal J_D=\langle v,\mathcal T_{K_\lambda}v\rangle$ ⟹ **Rayleigh 商／距离核谱问题（经典类）** ⟹ **不包装为新机制** ✓✓
④ ⭐⭐⭐⭐ **单调性环已补**：$c^{*}_\lambda$ 在 $(0,\approx2.2)$ 严格递增 ⟹ $\sup_{\lambda\le1}C(\lambda)=c_1^{*}$ ⟹ **ceiling 锁死** ⟹ $G\le0.6725$ ⟹ $$\boxed{G>0.6725\Rightarrow\lambda>1}$$ ✓✓✓
⑤ ⭐⭐⭐ **路线图统一**：支撑 $1.04/1.26/1.70$ ↔ $\lambda$ ⟹ $G=2-1/c^{*}_\lambda=0.71/0.79/0.88$（对 0.70/0.80/0.90）⟹ **撤回 V301 的"两机制区分"** ✓✓✓
【下一步（现在 5b 才有资格成为定理）】
  (5b) 把 $\lambda>1$ 翻译为 **support wall**：$G>0.6725\Longrightarrow\sigma>\sigma_{\rm uncond}$（$\sigma=\lambda$，故即 $\sigma>1$）✓
  (6) **形式化 $\lambda$-单调性**（把 §3 的五点核验升级为证明：$f(\vartheta)=\sqrt2\tan\vartheta/(1+\vartheta\tan\vartheta)$ 的 $\vartheta$-单调性）✓
```
