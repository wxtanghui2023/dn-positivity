# E141 · ⭐⭐⭐ **Q4 独立性终审：Q4 【自动成立】✗ ⟹ 情形 A ⟹ 立即封口 ✓**

> 委托 ✓ 唐先生 2026-09-14 11:33（**③ 但目标改为"先证 Q4 是否独立"** ✓；三情形 A/B/C ✓；**原始对象层幂律 $\Phi_{p^n}=\Phi_p^n$** ✓）
> 执行 ✓ 小灵｜**纸面审计 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**逐字引档 ✓**
> ⚠️ **结论是"Q4 无独立自由度"✗ —— 即【不是突破点】✓（依您的规则：立即封口 ✓）**

---

## 0. 判定：**情形 A（Q4 自动成立）✗**

$$\boxed{\textbf{Q4}\ \textbf{自动成立于任何【半群作用】✗ —— 它不是独立自由度 ✓，不能作为突破点 ✓}}$$
$$\textbf{两步恒等 ✓（零假设 ✓）}：$$
$$\text{(i) 流/半群 ✓}：\varphi_{t+s}=\varphi_t\circ\varphi_s\ \forall t,s\ \Longrightarrow\ \varphi_{n\log p}=\varphi_{\log p}^{\ n}\ \textbf{恒等 ✓（定义即得 ✓，无任何额外条件 ✓）}$$
$$\text{(ii) 长度 ✓}：\ell\ \text{为加法同态（}\ell(\varphi_{t+s})=\ell(\varphi_t)+\ell(\varphi_s)\ ✓\ \text{—— 任何"长度"定义必如此 ✓）}\ \Longrightarrow\ \ell(\varphi_{n\log p})=n\ell(\varphi_{\log p})=n\log p=\log p^n\ \textbf{恒等 ✓}$$
$$\Longrightarrow\ \boxed{\textbf{Q4} ＝ \text{半群公理 ＋ 长度同态【的重言式】✗}\ \text{—— 与 }Q1/Q2/Q3/Q5/Q6\ \textbf{无独立冲突可能 ✓}}$$

## 1. 为什么"候选在 Q4 失败"是**误框**✗（逐字核 ✓）

$$\text{档内逐字 ✓（}`arith-frob-flow-final-2026-09-09.md` ✓）：\text{"多数像算术动的对象在此失败 ✗"}\ \text{—— 但同档【同一行的分裂说明】✓：}$$
$$\qquad\text{"只有 }A\ ⇒\ \text{有频率无轨道 ✓；只有 }B\ ⇒\ \text{Selberg 型长度错 ✗"}\ ✓$$
$$\Longrightarrow\ \textbf{失败的其实是 }Q1/Q2\ \text{（长度来源 ✗）与 }Q5\ \text{（}F_p\ \text{内生成 ✗）}\ \textbf{—— 不是幂律 }Q4\ ✗✓$$
$$\text{逐字 ✓（同档 ✓）：}\text{"}A=\text{Length generation（}p\to\log p\text{）✓，}B=\text{Power generation（}p^n\to\gamma_p^n\text{）✓，}\textbf{二者不能分别解决 ✗"}$$
$$\Longrightarrow\ \text{故 }B\ \text{（幂生成）之所以"不能与 }A\ \text{分别解决"✓，}\textbf{正因为 }B\ \text{是 }A\ \text{的推论 ✗ ⟹ Q4 无独立内容 ✓✓}$$

## 2. 原始对象层（您的 $\Phi_{p^n}=\Phi_p^n$ ✓）—— 同一结论 ✓

$$\Phi_p\ \text{为【不依赖零点的 arithmetic 作用】✓}\ \Longrightarrow\ \Phi_p\ \text{若属于一个【可复合】的族（}\Phi_{p}\Phi_{q}=\Phi_{pq}\ \text{型 ✓），则}\ \Phi_{p^n}=\Phi_p^{\ n}\ \textbf{自动 ✓}$$
$$\text{① char }p\ \text{对照 ✓}：\mathrm{Frob}_{p^n}=\mathrm{Frob}_p^{\ n}\ \textbf{自动 ✓（函子性 ✓）}\ \text{—— 无需额外假设 ✓}$$
$$\text{② char 0 的实情 ✓}：\text{无 Frob【元素】✓（只有共轭类 ✓）⟹ \textbf{障碍在 }Q5\ \text{（存在性 ✗），不在 }Q4\ \text{（幂律 ✗）}}$$
$$\Longrightarrow\ \textbf{您提醒的"char-0 Frobenius／共轭类"障碍 ✓ 确实出现 ✓，但它落在 }Q5\ ✗\ \text{—— \textbf{与 }Q4\ \text{无关 ✗✓（故不必假定 Q4 是同一堵墙 ✓：Q4 是空命题 ✓）}}$$

## 3. 由此得到的**结构产出**（✓ 小但真实 ✓）

$$\textbf{规格 }Q1\text{–}Q6\ \textbf{【缩减】为 }Q1,Q2,Q3,Q5,Q6\ \text{（}Q4\ \text{冗余 ✓）}\ \Longrightarrow\ \textbf{规格被"删除"而变锐 ✓}$$
$$Q1\ p\leftrightarrow\gamma_p\ \big|\ Q2\ T(\gamma_p)=\log p\ \big|\ Q3\ h_{\rm top}=1\ \big|\ \textbf{（}Q4\ \text{删 ✓）}\ \big|\ Q5\ F_p\ \text{内部生成}\ \big|\ Q6\ \Theta^*=1-\Theta\ ✓$$
$$\textbf{且 ✓}：Q1+Q2+Q5\ \text{一旦同时成立 ✓，}Q4\ \text{自动跟随 ✓ ⟹ 攻击面【缩小到 }Q1/Q2/Q5/Q6\ \text{四项 ✓】}$$

## 4. 边界与唯一残余（✓ 诚实 ✓）

```
⚠️ **① 唯一使 Q4 变为【非空】的情形 ✗**：若载体**【不是半群作用】**（无可复合结构 ✗ —— 例如只是"对应(correspondence)集合"而【无复合律】✓），
   则 $\Phi_{p^n}=\Phi_p^n$ 变成真约束 ✗ —— **但那同时违反 }Q1\ \text{的"闭点＝动力对象"✗ ⟹ 该情形已出局 ✓**
⚠️ **② 本轮【不声称】Q4 在任何可能载体上都空 ✓** —— 只声称：**在 }Q1\ \text{（动力对象）成立的前提下 ✓，}Q4\ \text{必空 ✗✓**
⚠️ **③ 这是对档内 }Q1\text{–}Q6\ \text{框法的【更正 ✓】**（把 }Q4\ \text{列为独立硬约束 ✗ → 标为冗余 ✓）—— 依 T10 应留勘误 ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓；**零数值 ✓**
⭐ **净产出 ✓**：① **判定情形 A ✓（两步恒等 ✓）**；② **"候选在 Q4 失败"是误框 → 实为 }Q1/Q2/Q5\ ✗**；
   ③ **原始对象层同一结论 ✓**（char 0 障碍落 }Q5\ ✗）；④ **规格缩减为 5 项 ✓（攻击面缩小 ✓）**
```

## 5. 依您的规则处置（✓）

$$\text{您规则 ✓："若 }Q4\ \text{自动成立 ⟹ 立即封口 ✓，不再浪费时间 ✓"}\ \Longrightarrow\ \boxed{\textbf{本轮即止 ✓ —— 不进入构造 ✗}}$$
