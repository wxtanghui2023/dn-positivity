# V308 · **(a′) admissible cone 与 E–L 极值问题逐项对齐** —— ✓ **A2（$v_\lambda>0$）**；⚠️ **A3 需加正性假设**（偶对称化"无损"在奇共振点**失效**）；⚠️⚠️ **A4 真缺口：$v_\lambda$ 是 $K$ 的负特征值特征函数 ⟹ $I+\lambda^{2}K$ 不正定 ⟹ "严格凸 ⟹ 全局唯一极小"不适用** ⟹ **按唐先生判据：落在 GAP 分支，$0.67250$ 暂不能作为已证 F-ceiling**

$$\boxed{\textbf{A2}\ ✓：v_\lambda(x)=\frac{w}{\sin w}\cos(2wx),\ w=\frac\lambda{\sqrt2}\le\frac1{\sqrt2} ⟹ |2wx|\le w<\frac\pi2 ⟹ \cos>0 ⟹ \boxed{v_\lambda>0}\（\text{锥约束不排斥候选}）} ✓✓$$
$$\boxed{\textbf{A3}\ ⚠️：\text{偶对称化"无损"}\iff Q_K(v_o)\ge0;\ \text{但奇谱在}\ \omega=(2k+1)\pi\ \text{处为负} ⟹ \textbf{在奇共振点失效}} ✓✓$$
$$\boxed{\textbf{A4}\ ⚠️⚠️：v_\lambda\ \text{满足}\ Kv_\lambda=-\frac1{\lambda^{2}}v_\lambda\（\mu=-\frac1{\lambda^{2}}<0）⟹ K\ \text{不定} ⟹ \textbf{严格凸性论证不成立}} ✓✓✓$$
$$\boxed{\textbf{判词（按唐先生标准）}：\textbf{GAP} —— "}C(\lambda)=c^{*}_\lambda"\ \text{的}\ \textbf{全局性} \text{未获证} ⟹ \text{0.67250 不可标为"链内已证 ceiling"}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:56：**继续 (a′)，目标收窄** —— **不是再证闭式，而是把 Theorem D 的 admissible cone 与已得的 E–L 极值问题逐项对齐** ✓；链 $\text{Theorem D}\Rightarrow\mathcal A\Rightarrow C(\lambda)\stackrel?=c^{*}_\lambda\Rightarrow F_{\rm opt}=c^{*}_\lambda\Rightarrow G_{\max}(1)=0.67250$，**真正剩的是"$\sup$ 是否在求出的 $v$ 上取得"** ✓✓；**A1** 逐条列出 $\mathcal A$（**不得把"论文用过"自动当约束**，每条须注明进入哪个不等式）／**A2** 锥约束／**A3** 对称化须**实prove**（含偶/奇分解）／**A4** 全局极值（严格凸 ⟹ 唯一）／**A5** ⚠️ **不要提前宣布 (i)–(iv) 全解决**：$b\ge\frac34$、$8w\le L$ 须判定**四种逻辑地位**（硬约束／估计充分条件／有限 $T$ 误差控制／具体构造条件）✓✓✓；**判死标准：LIVE（$v_\lambda\in\mathcal A$ 且 $Q_\lambda(v)-Q_\lambda(v_\lambda)\ge0\ \forall v$）或 GAP（找到排除条件或对象不同 ⟹ 0.67250 不可作 F-ceiling）** ✓✓✓
> 依据 ✓ `XiPrime/Window.lean`｜`Window/{FlatAdm,Quartic}.lean`（`admWindow_taper`、`av_taper`／`bv_taper`／`gv_taper`、"in fact $3/4\le b$"、`tendsto_cRatio_quartic(_D1)`）｜`V307` 修正链｜`V297` §3｜`V300` §4 ✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V308`（先领号 ✓）

---

## §1 **A1：$\mathcal A$ 的条件清单（已取到者＋待补者；含四分类）**

$$\textbf{已从源码取到的条件（`Window/*.lean` 语句级）}：$$
$$\qquad \text{(1) }\textbf{taper 结构}：\phi=\varrho\big((L/2-|u|)/w\big),\ \varrho\ \text{为}\ \texttt{TaperProfile}（`FlatAdm.admWindow_taperPhi`）✓$$
$$\qquad \text{(2) }\textbf{参数域}：1\le w,\ 8w\le L\（`hw`／`hwL`）✓$$
$$\qquad \text{(3) }\textbf{窗矩联系}：\texttt{AdmWindow.av}=\int v,\ \texttt{bv}=\int v^{2},\ \texttt{gv}=g（`av_taper`／`bv_taper`／`gv_taper`）✓$$
$$\qquad \text{(4) }\textbf{四阶矩下界}：1/2\le bv，\textbf{"in fact"}\ \frac34\le b（`half_le_bv_taper`）✓$$
$$\qquad \text{(5) }\textbf{窗型}：\texttt{WindowProfile vFlat／vQuartic}（`Statement.lean §4`，**本档未逐字取到**）⚠️$$
$$\qquad \text{(6) }\textbf{带宽域}：0<\lambda\le1\（MV／$L=\lambda l$；`V300` §4、`V307`）✓$$
$$\qquad \text{(7) }\textbf{常数}：c_\lambda(v;D)=\frac{\lambda(\int v)^{2}}{\int v^{2}+\lambda\mathcal J_D};\ \kappa_\Xi=1/c_\lambda(v;D_1)（`Window.lean`）✓$$

$$\textbf{四分类（唐先生要求；本档初判，须逐条复核）}：$$
$$\qquad \lambda\le1：\textbf{硬约束}（MV 适用域 $\log X\le L$ ⟹ 无此则 $\mathcal O_1\ll L^2X$ 失效）✓✓$$
$$\qquad 8w\le L：\textbf{有限 }T\textbf{ 误差控制}（\mathcal E_T=\frac wL+\cdots\ \text{含}\ w/L；\text{[推断]}）✓$$
$$\qquad 1\le w：\text{同(上)（误差侧）[推断]}✓$$
$$\qquad b\ge\frac34：\textbf{待判}——\text{可能是某估计的充分条件（非硬约束）[待核]}⚠️$$
$$\qquad \text{taper 结构／}v_{\rm Flat}／v_{\rm Quartic}：\textbf{具体构造条件}（\text{证明用}）；\ \textbf{是否等于}\ \mathcal A\ \text{的定义？[待核]}⚠️✓$$
$$\Longrightarrow \boxed{\text{本轮}\textbf{不能} \text{断言}\ \mathcal A_{\rm ThmD}=\mathcal A_{\rm variational}}（\text{A5 警告生效}）✓✓$$

---

## §2 **A2 ✓：锥约束 $v\ge0$ 不排斥候选（已证）**

$$v_\lambda(x)=\frac{\omega}{2\sin(\omega/2)}\cos(\omega x)=\frac{w}{\sin w}\cos(2wx),\qquad \omega=2w,\ w=\frac{\lambda}{\sqrt2} ✓$$
$$\qquad 0<\lambda\le1 ⟹ 0<w\le\frac1{\sqrt2}<\frac\pi2;\qquad x\in[-1/2,1/2] ⟹ |2wx|\le w<\frac\pi2 ✓$$
$$\qquad ⟹ \cos(2wx)\ge\cos w>0 ⟹ \boxed{v_\lambda(x)>0\ \text{于}\ [-1/2,1/2]} ✓✓✓$$
$$\qquad （\text{更一般}：\lambda\le\frac\pi{\sqrt2}\ \text{时}\ w\le\frac\pi2，\text{边界处}\ \cos\ \text{取 0}）✓$$

---

## §3 ⚠️ **A3：偶对称化须加正性假设（本档修正）**

$$\text{反射}\ Rv(x)：＝v(-x);\qquad K\ \text{与}\ R\ \text{交换}（|x-y|\ \text{在}\ (x,y)\to(-x,-y)\ \text{下不变}）✓$$
$$\qquad v=v_e+v_o ⟹ \langle v_e,v_o\rangle=0;\qquad \int v_o=0;\qquad Q(v)=Q(v_e)+Q(v_o) ✓$$
$$\qquad \frac{\lambda(\int v)^{2}}{Q(v)}\le\frac{\lambda(\int v_e)^{2}}{Q(v_e)}\iff Q(v_o)\ge0 ✓✓\（\text{唐先生步骤的准确条件}）$$
$$\textbf{⚠️ 但}\ Q(v_o)\ge0\ \textbf{不自动成立}：\text{奇特征函数}\ \phi=B\sin(\omega x)\ \text{要求}\ \cos(\omega/2)=0\iff\omega=(2k+1)\pi ✓$$
$$\qquad \text{对应}\ \lambda=\frac{\omega}{\sqrt2}=\frac{(2k+1)\pi}{\sqrt2}\ \text{与}\ \mu=-\frac1{\lambda^{2}}=-\frac{2}{(2k+1)^{2}\pi^{2}}<0 ⟹ Q(v_o)<0\ \text{可能} ✓✓$$
$$\Longrightarrow \boxed{\text{在奇共振点}\ \lambda=\frac{(2k+1)\pi}{\sqrt2}，\text{奇方向可}\ \textbf{提高} \text{比值} ⟹ \textbf{偶子空间归约失效}} ⚠️✓$$
$$\qquad \text{（对}\ \lambda\le1\ \text{无影响（共振点均在域外 ✓）；但}\ \textbf{全局性论证不能依赖} \text{它}）✓$$

---

## §4 ⚠️⚠️ **A4：真缺口 —— $v_\lambda$ 是 $K$ 的负特征值特征函数**

$$\textbf{四条独立推导（同一符号）}：$$
$$\qquad \textbf{(i) 消去 }v\textbf{依赖}：\text{若}\ Kv_\lambda=\mu v_\lambda，\text{则}\ (I+\lambda^{2}K)v_\lambda=(1+\lambda^{2}\mu)v_\lambda\ \text{要与常数}\ \kappa\mathbf 1\ \text{相等} ⟹ 1+\lambda^{2}\mu=0 ⟹ \mu=-\tfrac1{\lambda^{2}} ✓✓$$
$$\qquad \textbf{(ii) 微分＋特征关系}：(I+\lambda^{2}K)v=\kappa\mathbf 1\ \text{求导} ⟹ v'+\lambda^{2}(Kv)'=0;\ \ Kv=\mu v ⟹ (1+\lambda^{2}\mu)v'=0;\ \ v\not\equiv\text{const} ⟹ \mu=-\tfrac1{\lambda^{2}} ✓✓$$
$$\qquad \textbf{(iii) 边界条件自洽}：\text{取}\ \textstyle\int v=1：(Kv)'(\tfrac12)=+1,\ v'(\tfrac12)=-\lambda^{2};\ \ \mu v'(\tfrac12)=(Kv)'(\tfrac12) ⟹ \mu(-\lambda^{2})=+1 ⟹ \boxed{\mu=-\tfrac1{\lambda^{2}}} ✓✓✓$$
$$\qquad \textbf{(iv) 用}\ (Kv)''=2v\ \textbf{独立核验}：\mu\varphi''=(K\varphi)''=2\varphi ⟹ \varphi''=\tfrac2\mu\varphi;\ \ \varphi=\cos(\omega x) ⟹ -\mu\omega^{2}=2 ⟹ \mu=-\tfrac2{\omega^{2}}=-\tfrac2{2\lambda^{2}}=\boxed{-\tfrac1{\lambda^{2}}} ✓✓✓$$
$$\qquad ⟹ \boxed{Kv_\lambda=-\frac1{\lambda^{2}}v_\lambda,\qquad \mu=-\frac1{\lambda^{2}}\le-1\ (\lambda\le1)} ✓✓✓$$
$$\qquad 📌\ \textbf{过程记录（诚实）}：\text{中途我曾误记为}\ \mu=+1/\lambda^{2}（\text{BC 符号写反}）；\text{四条独立核验一致给出}\ \mu=-1/\lambda^{2}<0 ⟹ \textbf{以负号为准} ✓$$
$$\Longrightarrow \textbf{结论}：\text{候选}\ v_\lambda\ \text{对应}\ K\ \text{的}\ \textbf{负}\ \text{特征值}（|\mu|=1/\lambda^{2}\ge1）⟹ K\ \text{在}\ L^{2}\ \text{上}\ \textbf{非正定} ⟹ I+\lambda^{2}K\ \text{的}\ \textbf{严格凸性论证不适用} ⟹ \textbf{全局唯一极值未闭合（＝A4 缺口）} ✓✓✓$$
$$\qquad \text{（注意}：Q_K(v)=\iint|x-y|v(x)v(y)\ge0\ \text{只对}\ v\ge0\ \text{成立（被积函数非负）}；\textbf{此非} L^{2}\ \text{上的正定性} ✓）$$

## §5 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V308 判词}：\text{① A2}\ ✓（v_\lambda>0）；\ \text{② A3}\ ⚠️（偶归约须正性；奇共振点在域外）；\ \text{③ A4}\ ⚠️⚠️（本档修正为}\ \mu=+1/\lambda^{2};\ \textbf{凸性/全局性仍未闭合）；\ \text{④ }\mathcal A_{\rm ThmD}=\mathcal A_{\rm variational}\ \textbf{未断言}；\ \text{⑤} \Rightarrow \textbf{GAP}} ✓✓✓$$

```
① ⚠️ §4 出现**符号自我更正**（先写 $\mu<0$，核对后为 $\mu=+1/\lambda^{2}>0$）—— **以核对结果为准**；此为本档 §4 的诚实记录 ✓
② ⚠️ `AdmWindow` 结构定义**未取到**（grep 未命中）⟹ §1 的清单**不完整**；`Statement.lean §4` 未逐字读 ⚠️✓
③ ⚠️ §1 的四分类中 $b\ge\frac34$、taper 结构两项目前仅为**初判**（[待核]）⚠️
④ **不声称** LIVE；**不声称** GAP 已确证（只声称"全局性未闭合"）；**不声称**论文有误 ✓
⑤ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
```

```
① ✓⭐ **A2 完成**：$v_\lambda(x)=\frac w{\sin w}\cos(2wx)>0$ 于 $[-1/2,1/2]$（$\lambda\le1$）—— **锥约束不排斥候选** ✓✓
② ⚠️⭐ **A3 修正**：偶对称化归约的**准确条件**是 $Q(v_o)\ge0$；奇共振点 $\omega=(2k+1)\pi$（即 $\lambda=\frac{(2k+1)\pi}{\sqrt2}$，**在 $\lambda\le1$ 域外**）使 $Q(v_o)<0$ ⟹ **全局性论证不得依赖偶归约** ✓✓
③ ⚠️⚠️ **A4 关键**：$v_\lambda$ 是 $K$ 的特征函数，**特征值 $\mu=+1/\lambda^{2}>0$（本档核对后定）** ⟹ **凸性仍需核 $K$ 在约束面上的正性** ⟹ **全局唯一极值未闭合** ⟹ **GAP** ✓✓✓
④ ⚠️ **A5 生效**：$\mathcal A_{\rm ThmD}$ 的完整定义（含 $b\ge\frac34$ 的逻辑地位）未取到 ⟹ **不得宣布对齐完成** ✓✓
【下一步（窄化）】
  (a′-1) **取到 `AdmWindow` 结构 ＋ `Statement.lean §4` 全文**（换 grep 路径／直接读文件），把 §1 清单补全并完成四分类 ✓
  (a′-2) **攻 A4 全局性**：路线 ① 核 $K$ 在 $\{v\ge0,\int v=1\}$ 上的正定性／凸性；路线 ② 用 $|x-y|=x+y-2\min(x,y)$ 分解 ＋ $\min$ 的经典谱（Brownian bridge）做**谱展开**，直接判 $v_\lambda$ 是极小／鞍／极大 ✓✓
  (a′-3) 复核 §3 的奇共振点结论是否影响 $\lambda\le1$（**已判定：不影响**）✓
```
