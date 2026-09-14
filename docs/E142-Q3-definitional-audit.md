# E142 · ⭐⭐⭐ **Q3 定义原文审计 ＋ 二读法蕴含审计：**独立内容只剩【上界】✗（删/留取决于您的裁定 ✓）

> 委托 ✓ 唐先生 2026-09-14 11:35（**不进入构造 ✓**；查清 Q3 原始定义 ✓；做两读法蕴含证明 ✓）
> 执行 ✓ 小灵｜**纸面审计 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**逐字引档 ✓**

---

## 0. 原文审计结果（✓ 先给事实 ✓）

$$\text{档内逐字 ✓（}`arith-frob-flow-final-2026-09-09.md`\ \text{行 17 ✓）：}\text{"Q3: h\_top = 1（PNT——）"}$$
$$\text{严格版逐字 ✓（同档 ✓）：}\text{"Q3 h\_top = 1（PNT 全局统计）"}$$
$$\Longrightarrow\ ⚠️\ \boxed{\textbf{档案【未显式定义】}h_{\rm top}\ \textbf{指哪一个 ✗ —— 只给了【据以成立的理由：PNT】✓}}$$
$$\text{而 PNT 只能支撑【读法 1 ✓】：}\pi(e^T)\sim e^T/T\ \text{是【素数标记轨道】的计数 ✓，}\textbf{不是全系统的拓扑熵 ✗}$$
$$\Longrightarrow\ \textbf{故【原意】倾读法 1 ✓（因理由栏写 PNT ✓）；但}\ \textbf{记号 }h_{\rm top}\ \textbf{本身倾读法 2 ✗}\ \Longrightarrow\ \textbf{须裁 ✓}$$

## 1. 读法 1（素数标记子系统的指数率 ✓）：**Q3 冗余 ✓**

$$\text{由 }Q1{+}Q2：T(\gamma_p)=\log p\ \Longrightarrow\ N_\gamma(T)=\#\{\gamma_p\le T\}=\#\{p:\log p\le T\}=\pi(e^T)\ ✓$$
$$\text{PNT ✓}：\pi(e^T)\sim\frac{e^T}{T}\ \Longrightarrow\ \log N_\gamma(T)=T-\log T+o(1)\ \Longrightarrow\ \boxed{\lim_{T\to\infty}\frac{\log N_\gamma(T)}{T}=1}\ ✓$$
$$\Longrightarrow\ \boxed{Q1+Q2+\mathrm{PNT}\ \Longrightarrow\ Q3\ \textbf{✓（读法 1 下 Q3 无独立内容 ✗）}}$$

## 2. 读法 2（全系统的拓扑熵 ✓）：**独立内容【只剩上界】✗**

$$h_{\rm top}(\varphi)=\lim_{\epsilon\to0}\limsup_{t\to\infty}\frac1t\log s(t,\epsilon)\ ✓\ \text{—— 计数【全体】(}t,\epsilon)\text{-分离轨道 ✗，不只见素数标记者 ✓}$$
$$\text{① 下界 ✓ 自动}：\#\{\text{闭轨（周期}\le T\text{）}\}\ge\#\{\gamma_p\}\sim e^T/T\ \Longrightarrow\ h_{\rm top}\ \ge\ 1\ \textbf{（由 }Q1{+}Q2{+}\mathrm{PNT}\ ✓\text{）}$$
$$\text{② 上界 ✓ 是额外内容 ✗}：h_{\rm top}\le1\ \text{——【}Q1/Q2\ \text{完全给不出 ✓】}\ \Longrightarrow\ \textbf{独立部分 ＝ 上界 }h_{\rm top}\le1\ ✗✓$$
$$\Longrightarrow\ \boxed{\textbf{读法 2 下：}Q3\ \text{的独立内容【仅为】}h_{\rm top}\le1\ \text{（禁额外指数复杂度 ✗）}}$$

## 3. ⭐ 关键：**Bowen 定理**把两读法【条件性地】合一 ✓

$$\text{Bowen（1971 ✓，Axiom A／扩张＋specification ✗）：}h_{\rm top}=\lim_{T\to\infty}\frac1T\log\#\{\text{周期}\le T\ \text{的闭轨}\}\ ✓$$
$$\Longrightarrow\ \textbf{在良性系统上 ✓，闭轨计数率【就等于】拓扑熵 ⟹ 上界自动 ✓ ⟹ }Q3\ \textbf{完全冗余 ✓✓}$$
$$\Longrightarrow\ \text{反之（无 specification／非扩张 ✗）：上界 }h_{\rm top}\le1\ \textbf{真为独立约束 ✗✓}$$
$$\boxed{\text{合并 ✓}：Q3\ \text{的独立内容} ＝ \begin{cases}\varnothing,&\text{读法 1 ✓（或读法 2 ＋ Bowen 假设 ✓）}\\[1mm] h_{\rm top}\le1,&\text{读法 2 且无 Bowen 假设 ✗}\end{cases}}$$

## 4. 因此的**缩面**（✓ 依您的两种结局 ✓）

$$\text{【结局甲 ✓】若您裁定 }Q3=\text{读法 1（或取 Bowen 良性假设 ✓）}\ \Longrightarrow\ \boxed{Q1,Q2,Q5,Q6\ \textbf{四项 ✓ —— }Q3\ \textbf{删 ✓}}$$
$$\text{【结局乙 ✗】若您裁定 }Q3=\text{读法 2 且不假设 Bowen}\ \Longrightarrow\ \boxed{Q3\ \textbf{保留 ✓，且其内容明确为【上界】}h_{\rm top}\le1\ ✗}$$
$$\text{（不论哪一结局 ✓，}\textbf{下界 }h_{\rm top}\ge1\ \text{【都自动 ✓】⟹ Q3 的"=1"中【一半是重言式 ✓】）}$$

## 5. 判定与建议（✓）

```
⭐ **本档判定 ✓**：**Q3 的"= 1"中，【下界 ≡ 1】自动 ✓（Q1+Q2+PNT ✓）；【上界 ≤ 1】才有独立内容 ✗**
   ⟹ **Q3 的正确书写 ✓ 应为**：$\boxed{h_{\rm top}\le1\ \text{（上界才是指标 ✓）}}$ —— **而档案写作"=1"掩盖了这一点 ✗**
⭐⭐ **我的建议（等您裁定 ✓）**：
   ① **取结局甲 ✓**（读法 1 ／ Bowen 假设 ✓）⟹ **删 Q3，规格缩到 4 项 ✓**（$Q1/Q2/Q5/Q6$ ✓）
   ② **若取结局乙 ✗** ⟹ 把 Q3 **改写为"$h_{\rm top}\le1$ 上界约束"** ✓ —— 这样它与 Q1/Q2 **不再重叠** ✓，成为**真正独立的第 5 项** ✓
   ⚠️ **关键 ✓**：**档案原文的"=1"是【未分离下界/上界】的写法 ✗ ⟹ 无论哪一结局，都应留勘误 ✓（T10 ✓）**
```

## 6. 边界与纪律（✓）

```
✅ **纸面 ✓（零数值 ✓）**；逐字引档 ✓（arith-frob-flow-final 行 17 ✓／严格版 Q3 行 ✓）
⚠️ **① Bowen 定理的假设（扩张／specification／Axiom A ✓）未对任何具体候选核验 ✗** —— 本档只做【条件性】结论 ✓
⚠️ **② "PNT ⟹ 读法 1" 是我的【判定 ✓】**（依据：PNT 是素数侧统计 ✓，给不出全系统熵的上界 ✗）
⚠️ **③ 不声称 Q3 在任何读法下都冗余 ✗** —— 读法 2 无 Bowen 时它保留 ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **原文未定义 h_top ✗（只有理由 PNT ✓）**；② **两读法各判定 ✓**；③ **独立内容精确为【上界】✗**；
   ④ **Bowen 定理条件性合一 ✓**；⑤ **缩面结论 ＋ 勘误建议 ✓**
