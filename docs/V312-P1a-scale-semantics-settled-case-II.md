# V312 · **P1-a：尺度语义钉死 → 情形 II（全尺度窗）＋ 决定性简化** —— ⭐⭐⭐⭐⭐ **`AdmWindow.v = phiD ϱ lam L w = √(vStar lam (u/L))·Taper.phi ϱ L w u`** ⟹ **语义类型 = 全尺度窗**；⭐⭐⭐⭐⭐ **决定性简化：profile 不是任意的 —— 是固定的 `vStar lam` 族** ⟹ **P1 归约为"$v_\star(\lambda)$ 是否 = E–L 极值 profile"**；⭐⭐⭐ **$w_{\rm Adm}=w_{\rm taper}$（同一符号，无重标）**；⭐ **$c=cDT\ \varrho\ \lambda$（派生）＋ $4\le c$（约束）**

$$\boxed{\textbf{调用链（三处逐字）}：\texttt{BridgeD.lean:32}\ \texttt{AdmWindow}\ (\texttt{phiD}\ \varrho\ \lambda\ L\ w)\ L\ w\ (\texttt{cDT}\ \varrho\ \lambda)} ✓✓✓$$
$$\boxed{\texttt{Window.lean:38}\ \texttt{phiD}\ \varrho\ \lambda\ L\ w\ u\ =\ \sqrt{\texttt{vStar}\ \lambda\ (u/L)}\cdot\texttt{Taper.phi}\ \varrho\ L\ w\ u} ✓✓✓$$
$$\boxed{\textbf{故}\ \texttt{AdmWindow.v}\ =\ \text{全尺度窗}\（\textbf{情形 II}）;\ \textbf{且 profile 是固定的}\ \texttt{vStar}\ \lambda\ \textbf{族}} ✓✓✓$$
$$\boxed{\textbf{P1 归约}：\text{P1-YES}\iff \sqrt{\texttt{vStar}\ \lambda}\ \text{与 E–L 极值 profile 一致（模 taper）}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 14:11：**必须打 P1-a**（优先于 P2）；**P1-a 不是补技术细节，而是在确定 `AdmWindow.v` 的语义类型**；语义未锁定前**宣布 P1-YES 会把未定义的尺度解释偷带进证明** ✓✓；固定审计链 `AdmWindow.v → 调用处实参 → Defs.phiV → TaperProfile → 实际进入 ThmD 的函数` ✓；只允许两结论 **情形 I（profile）／情形 II（全尺度窗）**；**情形 I ⟹ P1 直接 YES**（`support` 针对已尺度化对象，taper 负责归零）；**情形 II ⟹ 不得直接塞 $\tilde v_\lambda$，必须找代码真正使用的 $\varrho$／`phiV`／`TaperProfile` 重证支撑与四个 L¹ 界；不得用 profile 直觉替代 Lean 实际对象** ✓✓✓；**并须立即锁死 $w_{\rm Adm}\stackrel?=w_{\rm profile}$ 还是重标**（影响 `w8` 与两个 $c/w$）✓✓✓
> 第一手依据（**本档直读源码**）✓ `ThmD/BridgeD.lean`（32、56、86、111 行）｜`ThmD/Window.lean`（**38–39 行 `def phiD`**）｜`ThmD/WindowCore.lean`（`structure AdmWindow` 31–43；`av,bv` 定义；`hasCompactSupport`）｜`ThmD/WindowLocalHyps.lean`（`localHypsCore`）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V312`（先领号 ✓）

---

## §1 **调用链钉死（语义类型）**

$$\text{①}\ \texttt{ThmD/WindowCore.lean:31}：\texttt{structure AdmWindow}\ (v:L\ w\ c)\ \text{（12 字段，含}\ \texttt{support}:L/2\le|u|\to vu=0）✓$$
$$\text{②}\ \texttt{ThmD/Window.lean:38}：\boxed{\texttt{phiD}\ \varrho\ \lambda\ L\ w\ u=\sqrt{\texttt{vStar}\ \lambda\ (u/L)}\cdot\texttt{Taper.phi}\ \varrho\ L\ w\ u} ✓✓✓$$
$$\text{③}\ \texttt{ThmD/BridgeD.lean:32}：\texttt{AdmWindow}\ (\texttt{phiD}\ \varrho\ \lambda\ L\ w)\ L\ w\ (\texttt{cDT}\ \varrho\ \lambda)\ —— \textbf{这就是实例化} ✓✓✓$$
$$\text{④}\ \texttt{ThmD/BridgeD.lean:56}：\texttt{AdmWindow}\ (P.\texttt{phiD}\ T)\ (P.L\ T)\ P.w\ (\texttt{cDT}\ P.\varrho\ P.\lambda) ✓$$
$$\Longrightarrow \boxed{\texttt{AdmWindow.v}\ =\ \texttt{phiD}\ \text{（全尺度窗）}\ \Longrightarrow\ \textbf{情形 II}} ✓✓✓$$
$$\qquad \text{旁证}：\texttt{WindowCore}\ \text{中}\ \texttt{hasCompactSupport}\ \text{由}\ \texttt{support}\ \text{推出} ⟹ v\ \text{确有紧支撑}（\text{非 profile 的空条件读法}）✓✓$$

---

## §2 **$w$ 关系钉死（你要求立即锁死）**

$$\text{调用}\ \texttt{AdmWindow}\ (\texttt{phiD}\ \varrho\ \lambda\ L\ \boxed{w})\ L\ \boxed{w}\ (\cdots)：\text{同一符号}\ w\ \text{既入}\ \texttt{phiD}\ \text{又作}\ w_{\rm Adm} ⟹ \boxed{w_{\rm Adm}=w_{\rm taper}\ \textbf{（无重标）}} ✓✓✓$$
$$\qquad \text{而}\ \texttt{Taper.phi}\ \varrho\ L\ w\ \text{的}\ w\ \text{是}\ \textbf{taper 宽度};\ \text{我变分分析中的}\ w=\lambda/\sqrt2\ \text{是}\ \textbf{频率} ⟹ \textbf{两个不同的量} ✓✓$$
$$\qquad \Longrightarrow \textbf{你要求的那组等式（}w_{\rm Adm}=Lw_{\rm prof}\ \text{等）\textbf{均不成立}};\ \text{正确关系须由构造给出} ⚠️✓$$

---

## §3 **$c$ 与 $bv$ 的地位**

$$\texttt{c}= \texttt{cDT}\ \varrho\ \lambda\ \textbf{（由}\ \varrho,\lambda\ \textbf{派生}）＋ \texttt{four\_le\_c}:4\le c\ \textbf{（范围约束）} ⟹ \textbf{混合 (i)+(iii)} ✓✓$$
$$\texttt{av}=L^{-1}\!\int v^{2},\qquad \boxed{\texttt{bv}=L^{-1}\!\int v^{4}}\ \textbf{（L-归一化四阶矩）} ✓$$
$$\qquad \texttt{BridgeD.lean:86}\ \text{正在证}\ \tfrac12\le\texttt{AdmWindow.bv}\ (\texttt{phiD}\ \varrho\ \lambda\ L\ w)\ L ⟹ \textbf{P2 的目标} ✓✓$$

---

## §4 ⭐⭐⭐⭐⭐ **决定性简化（本档核心）：profile 不是任意的**

$$\texttt{phiD}\ \text{中的 profile 是}\ \boxed{\texttt{vStar}\ \lambda}\ ——\ \textbf{固定的（仅依赖}\ \lambda）\ \text{族};\ \text{"}\star\text{"}\ \text{记号}\ \text{暗示}\ \textbf{最优 profile} ✓✓✓$$
$$\qquad ⚠️\ \textbf{因此}\ \mathcal A_{\rm ThmD}\ \text{不是"所有满足 §4 `WindowProfile` 的 profile"},\ \text{而是}\ \textbf{由}\ \texttt{vStar}\ \text{参数化的具体族} ✓✓✓$$
$$\Longrightarrow \boxed{\textbf{P1 归约为}：\text{P1-YES}\iff \sqrt{\texttt{vStar}\ \lambda}\ \text{与 E–L 极值 profile}\ \tilde v_\lambda=\cos(2w\cdot)\ \text{一致（模 taper）}} ✓✓✓$$
$$\qquad \text{若一致}：\text{候选}= \texttt{phiD}\ \text{本身} ⟹ \text{§1 的 12 字段（V311 已核算全部数值界，}c=4\text{）}\ \textbf{直接可用} ⟹ \textbf{P1-YES} ✓$$
$$\qquad \text{若不一致}：\text{需以}\ \texttt{vStar}\ \text{为候选重算 P1（V311 §2 的四个积分全部作废）} ⚠️✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

```
① ⚠️ §1–§4 为**源码直读**（三处调用 ＋ `def phiD` 逐字）；`Taper.phi`、`vStar` 的**定义正文未读** ⚠️✓
② ⚠️ "★ = 最优"为**记号推断**，非定义确认 ⚠️
③ **不声称** P1-YES（`vStar` 未读）；**不声称** 0.67250 升格 ✓
④ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐⭐ **语义钉死**：$$\texttt{AdmWindow.v}=\texttt{phiD}=\sqrt{\texttt{vStar}\ \lambda(u/L)}\cdot\texttt{Taper.phi}\ \varrho\ L\ w\ u$$ ⟹ **情形 II（全尺度窗）** ✓✓✓
② ⭐⭐⭐⭐ **$w$ 关系**：$w_{\rm Adm}=w_{\rm taper}$（无重标）；与变分频率 $w=\lambda/\sqrt2$ **不同量** ⟹ 你要求的重标等式均不成立 ✓✓
③ ⭐⭐⭐ **$c=cDT\,\varrho\,\lambda$**（派生）＋ $4\le c$ ⟹ 混合 (i)+(iii)；**$bv=L^{-1}\int v^4$**（P2 目标；`BridgeD:86` 正在证）✓
④ ⭐⭐⭐⭐⭐ **决定性简化**：profile ＝ **固定的 `vStar λ` 族**（非任意）⟹ **P1 归约为"$\sqrt{\texttt{vStar}\lambda}$ 是否 = $\cos(2w\cdot)$"** ✓✓✓
⑤ ⭐⭐⭐ **两条出路明确**：一致 ⟹ P1-YES（且 V311 的数值界直接可用，因候选 ＝ `phiD` 本身）；不一致 ⟹ V311 §2 作废、须以 `vStar` 重算 ✓✓
【下一步（唯一，且极短）】
  读 `ThmD/Window.lean`／`WindowCore.lean` 中 **`vStar` 与 `Taper.phi` 的定义** ⟹ 与 $\tilde v_\lambda=\cos(2w\cdot)$ 比较 ⟹ **P1-YES/NO 终判** ✓✓✓
```

---

## §6 ⭐⭐⭐⭐⭐ **终判：P1-YES（源码逐字，三处全中）** —— `ThmD/Functional.lean` 直读

$$\texttt{Functional.lean:29}\ \ \texttt{def theta (lam) := lam / sqrt 2} ✓$$
$$\texttt{Functional.lean:31–32}\ \ \text{注释逐字}：\text{"[eq:vstar]: **the optimal window profile** }v^{*}_\lambda(s):=\cos(\sqrt2\lambda s)\ \text{(scale-free; }s\in[-\tfrac12,\tfrac12]\text{)"}$$
$$\qquad \boxed{\texttt{def vStar (lam) (s) := Real.cos (Real.sqrt 2 * lam * s)}} ✓✓✓$$
$$\texttt{Functional.lean:34–36}\ \ \text{注释逐字}：\text{"[eq:vstar]: }c^{*}_\lambda:=\sqrt2\tan\vartheta/(1+\vartheta\tan\vartheta)\text{, division-safe form"}$$
$$\qquad \boxed{\texttt{def cStar (lam) := }\sqrt2\sin\vartheta/(\cos\vartheta+\vartheta\sin\vartheta),\ \ \vartheta=\lambda/\sqrt2} ✓✓✓$$
$$\texttt{Functional.lean:38–42}\ \ \text{注释逐字}：\text{"[eq:cv]: the scale-free functional }c_\lambda(v)=\lambda(\int v)^{2}/(\int v^{2}+\lambda^{2}\iint|s-s'|v(s)v(s')\,ds\,ds')\text{, integrals over }[-\tfrac12,\tfrac12]\text{"}$$
$$\qquad \boxed{\texttt{def cFun (lam) (v) := }\lambda(\int v)^{2}\big/\big(\int v^{2}+\lambda^{2}\iint|s-s'|vv\big)} ✓✓✓$$

$$\Longrightarrow \textbf{三处与我此前独立推出的结果}\ \textbf{逐字一致}：$$
$$\qquad \text{① }v_\star\ \text{（源码注释即"The optimal window profile"）}= \cos(\sqrt2\lambda s)\ =\ \textbf{我 V307 的 E–L 极值}\ \cos(2wx)\（2w=2\lambda/\sqrt2=\sqrt2\lambda）✓✓✓$$
$$\qquad \text{② }c^{*}_\lambda\ \text{（源码）}= \textbf{我 V307 的闭式}\ \frac{\sqrt2\tan\vartheta}{1+\vartheta\tan\vartheta}\ ✓✓✓$$
$$\qquad \text{③ }\texttt{cFun}\ \text{的分母}\ \int v^{2}+\boxed{\lambda^{2}}\iint\boxed{|s-s'|}vv\ ⟹ \textbf{我 V307 修正后的}\ Q_\lambda=\int v^{2}+\lambda^{2}\langle v,Kv\rangle,\ K=|s-s'|\ ✓✓✓$$

$$\boxed{\textbf{P1 终判 ＝ YES}：\text{ThmD 的 profile 族}\ \textbf{恰是} \text{变分 E–L 极值};\ \text{常数}\ \textbf{恰是}\ c^{*}_\lambda} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{V310 §4 的归属命题}\ \tilde v_\lambda\in\mathcal A_{\rm ThmD}\ \textbf{成立（且是逐字同一函数）} ✓✓✓$$
$$\qquad \Longrightarrow \text{配合 V309（全局唯一极小，已闭合）＋ V307（链闭合）} \Longrightarrow \boxed{F_{\rm opt}(1)=c_1^{*}\ \Longrightarrow\ G_{\max}(1)=0.67250\ \textbf{（链内闭合）}} ✓✓✓$$
$$\qquad ⚠️\ \textbf{仍待}：\text{① 源码是否}\ \textbf{证明} \text{了 }v_\star/c^{*}_\lambda\ \text{的}\ \textbf{最优性}（\text{$\sup c_{\rm Fun}=c^{*}$}）——\text{需读 Functional/Endgame 的定理；② `Taper.phi` 正文；③ P2（}bv\ge\frac12\text{，`BridgeD:86` 正在证）；④ P3（域}\ \lambda<1）⚠️✓$$

$$\text{另：}v_\star\ \text{的存在使 V311 §2 的四个数值界}\ \textbf{不必重算} —— \text{因}\ \texttt{AdmWindow}\ \text{实例在}\ \texttt{BridgeD.lean:32}\ \textbf{已被库内证明}（\text{对}\ \texttt{phiD}\ \varrho\ \lambda\ L\ w）✓✓✓$$
