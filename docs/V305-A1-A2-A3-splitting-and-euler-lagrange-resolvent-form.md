# V305 · **(A) 拆为 A1/A2/A3：单变量解析已解决；真正的极值定理归约为 resolvent＋ODE（未证，引用保留）** —— ⭐⭐⭐⭐⭐ **A2（$\lambda$-形式）**：$\dfrac{d}{d\lambda}c^{*}(\lambda)=\dfrac{1}{\big(1+\frac{\lambda}{\sqrt2}\tan\frac{\lambda}{\sqrt2}\big)^{2}}>0$（**$\sqrt2$ 精确抵消** ✓）；⭐⭐⭐⭐ **A3 归约**：E–L 为 $(I+\lambda K_\lambda)v=\mu\mathbf 1$ ⟹ $C(\lambda)=\dfrac{\lambda}{\mu}=\lambda\big\langle\mathbf 1,(I+\lambda K_\lambda)^{-1}\mathbf 1\big\rangle$（**resolvent 形式**）；⚠️ **A3 未证 ⟹ 外部引用 `CCLM17 Cor.14` 必须保留**（按唐先生验收标准：**不得把形式化单调性冒充完整自足证明**）

$$\boxed{\textbf{A2（单变量解析，已完成）}：c^{*}(\lambda)=\frac{\sqrt2\tan\vartheta}{1+\vartheta\tan\vartheta}\Big|_{\vartheta=\lambda/\sqrt2} \Longrightarrow \frac{dc^{*}}{d\lambda}=\frac{1}{\big(1+\frac{\lambda}{\sqrt2}\tan\frac{\lambda}{\sqrt2}\big)^{2}}\ >0} ✓✓✓$$
$$\boxed{\textbf{A3（真正的极值定理）}：\text{归约}：C(\lambda)=\frac{\lambda}{\mu},\qquad (I+\lambda K_\lambda)v=\mu\mathbf 1 \Longrightarrow C(\lambda)=\lambda\big\langle\mathbf 1,(I+\lambda K_\lambda)^{-1}\mathbf 1\big\rangle} ✓✓✓$$
$$\boxed{\textbf{验收判定}：\text{A1}\ ✓\ |\ \text{A2}\ ✓\ |\ \text{A3}\ ✗（未证）⟹ \textbf{引用保留，不得声称自足}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:44：**同意先做 (A)**，但**纠正一个逻辑点**：**Lean 不能把 `CCLM17 Cor.14` 的最优性"形式化掉"**，除非把 Cor.14 所依赖的**谱极值命题本身**放进库并证明；仅形式化 $f'>0$ 只消除"单调性"这一层依赖 ⟹ **A 的正确目标升级为：把 $C(\lambda)=c^{*}_\lambda$ 拆成"可独立验证的最优性定理＋三行单调性定理"** ✓✓；并要求 **A1（闭式候选＋定义域）／A2（严格单调，$\lambda$-形式）／A3（真正的极值定理：$\forall v\in\mathcal A_\lambda,\ c_\lambda(v)\le c^{*}$ 且 $\exists$ extremizer）** ✓✓✓；**验收标准（逐字）**："**不是'Lean 能证明导数为正'，而是把 `CCLM17 Cor.14` 拆成可在本库独立证明的 Rayleigh/积分算子极值命题；若做不到，就明确保留外部引用，不能把形式化单调性冒充成完整自足证明**" ✓✓✓；并给出 **E–L 应导出 $(I+\lambda K_\lambda)v=\mu\mathbf 1$，再由积分方程求 $\mu$，则 $C(\lambda)=1/\mu$** ✓✓
> 依据 ✓ `ChallengeDeps.lean`（$c^{*}_\lambda$ 闭式）｜`V303`（闭式／域／情形 A）｜`V304`（$f'>0$ 三行）｜`XiPrime/Window.lean`（`jWin_nonneg`／`cWin_pos`；$\lambda\le1$ 域）｜`Window/{FlatAdm,Quartic}.lean` ✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；数值仅闭式算术 ✓｜编号 ✓ `V305`（**先领号后写档** ✓）

---

## §1 **A1：闭式候选与定义域**（✓）

$$c^{*}(\lambda)：＝\frac{\sqrt2\tan\vartheta}{1+\vartheta\tan\vartheta},\qquad \vartheta：＝\frac{\lambda}{\sqrt2};\qquad \textbf{定义域}\ 0<\lambda<\frac{\pi}{\sqrt2}=2.22144\ldots ✓$$
$$\qquad \text{理由}：\tan\ \text{在}\ \vartheta=\frac\pi2\ \text{有极点} ⟹ \text{域上界}\ \lambda=\sqrt2\cdot\frac\pi2=\frac\pi{\sqrt2};\qquad \text{域内}\ \tan\vartheta>0 ⟹ 1+\vartheta\tan\vartheta>1>0 ✓$$
$$\qquad \text{边界值}：c^{*}(1)=0.7532960\ldots;\qquad \lim_{\lambda\to\pi/\sqrt2^-}c^{*}=\frac{2\sqrt2}\pi=0.9003163\ldots ✓$$

---

## §2 ⭐⭐⭐⭐⭐ **A2：严格单调（$\lambda$-形式，$\sqrt2$ 精确抵消）**

$$\frac{dc^{*}}{d\lambda}=f'(\vartheta)\cdot\frac{d\vartheta}{d\lambda}=\underbrace{\frac{\sqrt2}{(1+\vartheta\tan\vartheta)^{2}}}_{（\text{V304 已证}）}\cdot\frac1{\sqrt2}=\boxed{\frac{1}{\big(1+\frac{\lambda}{\sqrt2}\tan\frac{\lambda}{\sqrt2}\big)^{2}}}>0\qquad(0<\lambda<\tfrac\pi{\sqrt2}) ✓✓✓$$
$$\qquad ⚠️\ \text{唐先生说的"}\sqrt2\ \text{正好抵消"}\ \textbf{已核验成立} ✓;\qquad \text{该形式}\ \textbf{Lean 友好}（无附加系数）✓$$
$$\qquad ⟹ \textbf{A2 完成；且}\ c^{*}\ \text{在}\ (0,\frac\pi{\sqrt2})\ \text{严格递增} ⟹ \sup_{0<\lambda\le1}c^{*}=c^{*}(1)=c_1^{*} ✓✓$$

---

## §3 ⭐⭐⭐⭐ **A3：真正的极值定理 —— 归约成立，证明未完成**

$$\textbf{归约（本档）}：L(v)：＝\int v,\quad Q(v)：＝\int v^{2}+\lambda\langle v,K_\lambda v\rangle ⟹ C(\lambda)=\sup_{v\in\mathcal A_\lambda}\frac{\lambda L(v)^{2}}{Q(v)} ✓$$
$$\qquad \text{尺度不变（}v\to tv ⟹ L^{2},Q\ \text{同阶缩放）} ⟹ C(\lambda)=\frac{\lambda}{\inf\{Q(v):\ L(v)=1\}}=\frac{\lambda}{\mu} ✓✓$$
$$\textbf{E–L（二次型＋线性约束）}：\frac{\delta}{\delta v}\Big[Q-\mu\big(L-1\big)\Big]=0\ \Longrightarrow\ \boxed{(I+\lambda K_\lambda)v=\mu\mathbf 1} ✓✓✓\（=\text{唐先生所给形式}）$$
$$\qquad \Longrightarrow v=\mu(I+\lambda K_\lambda)^{-1}\mathbf 1;\quad L(v)=\mu\big\langle\mathbf 1,(I+\lambda K_\lambda)^{-1}\mathbf 1\big\rangle=1 ⟹ \mu=\big\langle\mathbf 1,(I+\lambda K_\lambda)^{-1}\mathbf 1\big\rangle^{-1} ✓$$
$$\qquad \Longrightarrow \boxed{C(\lambda)=\lambda\,\big\langle\mathbf 1,\ (I+\lambda K_\lambda)^{-1}\mathbf 1\big\rangle} ✓✓✓\（\textbf{resolvent 矩阵元形式}）$$
$$\textbf{把它内生化的具体路子（未做）}：$$
$$\qquad \text{① }\textbf{核识别}：\mathcal J_D(\lambda;v)=2\!\int_0^1\!\lambda r(v⋆v)(r)dr\ ⟹ \text{写成}\ \iint v(s)v(s')k(|s-s'|)ds\,ds'\ \text{的显式核}（\text{待做}）;$$
$$\qquad \text{② }\textbf{算子求逆}：|x-y|\ \text{／}\ \min(x,y)\ \text{型核的逆为}\ \textbf{二阶微分算子}（\text{经典}）⟹ (I+\lambda K)^{-1}\ \text{化为}\ \textbf{ODE 边值问题};$$
$$\qquad \qquad \text{其解为}\ \textbf{三角函数} ⟹ \boxed{\tan\ \text{结构正是该 ODE 的指纹}}（\text{解释了}\ c^{*}_\lambda\ \text{闭式}）;$$
$$\qquad \text{③ ⚠️ }\textbf{锥约束}：`jWin_nonneg`\ \text{只对}\ v\ge0\ \text{给}\ \mathcal J\ge0 ⟹ \sup\ \text{是在}\ \textbf{非负锥} \text{上取} \Longrightarrow \text{E–L 的 Lagrange 论证须验证 extremizer}\ v_\lambda\ge0 ✓$$
$$\Longrightarrow \boxed{\textbf{A3 未证}：\text{归约＋E–L＋resolvent 形式成立};\ \text{但核识别／BC／锥三项未做}} ⟹ \textbf{引用保留} ✓✓✓$$

---

## §4 **两墙表**（结构结论，**条件性**：以 A3 为条件）

$$\lambda\le1\ \Longrightarrow\ G(\lambda)\le2-\frac1{c_1^{*}}=0.67250 ✓$$
$$1<\lambda<\frac\pi{\sqrt2}\ \Longrightarrow\ 0.67250<G(\lambda)<2-\frac\pi{2\sqrt2}=0.889280 ✓$$
$$\lambda\to\frac\pi{\sqrt2}^{\,-}\ \Longrightarrow\ G(\lambda)\to0.889280;\qquad \boxed{G=1\ \textbf{在该}\ D(s)=s\ \text{窗族内不可达}} ✓✓$$
$$\qquad \text{即：}\textbf{突破}\ \lambda>1\ \text{之后仍有第二堵墙}\（G<0.8893）\ —— \text{比"support}>1\ \text{才能突破"更进一步} ✓✓✓$$

---

## §5 **验收判定（按唐先生标准，逐字对表）**

$$\text{"不是'Lean 能证明导数为正'，而是把 `CCLM17 Cor.14` 拆成可在本库独立证明的 Rayleigh/积分算子极值命题"}：$$
$$\qquad \text{A1}\ ✓\（\text{闭式＋域}）;\qquad \text{A2}\ ✓\（\text{$\lambda$-形式导数} >0）;\qquad \text{A3}\ ✗\（\text{归约完成，证明未完成}）✓$$
$$\Longrightarrow \boxed{\textbf{结论}：\text{不得声称完全自足};\ \textbf{外部引用}\ \texttt{CCLM17 Cor.14}\ \text{保留};\ \text{A3 的具体路子已给出（核识别→ODE→锥）}} ✓✓✓$$

---

## §6 边界 ＋ 净产出 ＋ 下一步

```
① ⚠️ §3 的"`|x-y|` 型核的逆为二阶微分算子"为**经典事实的引用**（未在本档验证具体 BC）⚠️
② ⚠️ §3 的锥约束（$v\ge0$）是本档**新提出的注意点**；未验证 extremizer 在锥内 ✓
③ ⚠️ §4 两墙表**条件性**：以 A3（$C(\lambda)=c^{*}_\lambda$）为前提 ✓
④ **不声称** A3 成立；**不声称**本档自足；**不声称** $G=1$ 在任何更大族内不可达（限本窗族）✓
⑤ 未用 RH ✓；未跑 Lean ✓；数值仅闭式算术 ✓
```

```
① ⭐⭐⭐⭐⭐ **A2 完成**：$$\frac{dc^{*}}{d\lambda}=\frac{1}{(1+\frac{\lambda}{\sqrt2}\tan\frac{\lambda}{\sqrt2})^{2}}>0$$（$\sqrt2$ 抵消已核验；Lean 友好）✓✓✓
② ⭐⭐⭐⭐ **A3 归约完成**：E–L $(I+\lambda K_\lambda)v=\mu\mathbf 1$ ⟹ $$C(\lambda)=\lambda\langle\mathbf 1,(I+\lambda K_\lambda)^{-1}\mathbf 1\rangle$$（resolvent 形式）＋ 内生化三步路子（核识别→ODE（tan 指纹）→锥）✓✓✓
③ ⚠️⚠️ **A3 未证 ⟹ 引用保留**；按唐先生验收标准**不冒充自足** ✓✓✓
④ ⭐⭐⭐ **两墙表**：$\lambda\le1\Rightarrow G\le0.67250$；$1<\lambda<\pi/\sqrt2\Rightarrow G<0.889280$；$G=1$ 本族内不可达 ⟹ **突破后有第二堵墙** ✓✓✓
⑤ ⭐ **A1 完成**：域 $0<\lambda<\pi/\sqrt2$ 由 $\tan$ 极点定 ✓
【下一步（二选，且 (B) 现在有资格）】
  (A′) **继续 A3**：做 ① 核识别（写出 $k(|s-s'|)$ 显式）→ ② 解 ODE 边值问题复现 $\tan$ ⟹ 真正内生化；③ 锥验证 ✓
  (B) **(5b)**：以"引用保留"为前提，把两墙翻译为 $\sigma$-语言（$\sigma=\lambda$ ⟹ $\sigma>1$；第二墙 $\sigma>\pi/\sqrt2$）✓
```
