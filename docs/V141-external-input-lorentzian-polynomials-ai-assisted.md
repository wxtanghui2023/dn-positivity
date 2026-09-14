# V141 · ⭐⭐⭐⭐ **外部输入评估：Lorentzian 多项式有界比率（AI 协助，arXiv:2609.05341）—— 与我们 $R_{\rm residual}$ 的关系**
> 委托 ✓ 唐先生 2026-09-14 23:27（**"洛伦兹多项式被 AI 协助攻克，看看对我们分析有没有帮助"** ✓）
> 执行 ✓ 小灵｜**网络核查 ✓（一手 arXiv ＋ 两独立新闻源 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ V141 ✓
> ⚠️ 定位 ✓：本档为**外部输入评估**，不是新一轮机制搜索 ✗；不改写 `V137` 的 SEARCH BRANCH CLOSED ✓

---

## §0 事实（✓ 一手核查 ✓）

$$\textbf{论文 ✓}：\text{"Bounded ratios for Lorentzian polynomials"}\ ✓;\ \text{arXiv:}\textbf{2609.05341v2}\ ✓;\ \text{math.CO}\ ✓;\ \text{MSC }05\text{B}20/05\text{E}14/14\text{P}10\ ✓;\ 75\ \text{页 ✓}$$
$$\textbf{作者 ✓}：\text{Aayush Bathija, Prince Rohatgi（加州 Oak Park 高中 ✓）＋ Daniel Soskin（UCLA 博士后 ✓）}$$
$$\textbf{AI 使用 ✓（作者自述 ✓）}：\text{Claude Opus 5 ＋ GPT-5.6 Sol}\ ✓\ \text{—— 用于【数值计算／证明思路／文稿编辑】}\ ✓;\ \text{关键推导与核验由三人组独立完成 ✓}$$
$$\textbf{数学内容 ✓}：\text{`Huh`（＋Soskin 及合作者）此前刻画了 }\textbf{二次 }\text{Lorentzian 多项式的【哪些系数比值有上界】}\ ✓;\ \text{本文推到}\textbf{任意次数}：\text{"比值是否有上限"完全由}\textbf{离散凸性条件}决定 ✓;\ \text{并给出【有界比率锥】的对偶刻画 ✓}$$
$$\textbf{同期背景 ✓}：\text{25 位菲尔兹奖得主（陶哲轩／Scholze／邓煜等）发声明警示 AI 与数学严谨性 ✓};\ \text{Gowers 观察 ✓：近例 AI"解决"名题多为}\textbf{反例型} \text{而非完整证明 ✓};\ \text{AI＋Lean 趋势 ✓（Claude 11 天形式化 Fermat 证明 ＝ 1300 万行 Lean ✓；Erdős 问题经 Aristotle Lean 验证 ✓）}$$

## §1 ⭐ 与我们项目的关系（✓ 三层 ✓）

### ① Lorentzian 多项式 ＝ **char-0 的"极化／正性"框架** ✓✓（最重要 ✓）
$$\text{定义 ✓}：\text{非负系数}\ +\ \textbf{M-凸支撑}\ +\ \text{所有二次型（Hessian）至多一个正特征值（签名 }(1,n-1)\ ✓\text{）}$$
$$\qquad\Longrightarrow\ \text{蕴含 }\textbf{Hodge–Riemann 型不等式／强对数凹性}\ ✓✓（\text{Mason／Newton 型 ✓}）$$
$$\qquad\text{典型来源 ✓}：\text{nef 除子的体积多项式 ✓；拟阵基生成多项式 ✓}$$
$$\boxed{\text{关键 ✓}：\text{这是一整套}\textbf{不需要 Frobenius} \text{的 char-0 极化正性理论 ✓✓}}$$
$$\qquad\Longrightarrow\ \textbf{须修正 }V136\ \text{§2 (v) 的表述 ✓}：\text{不是"char-0 未发现对应结构 ✗"，}\textbf{而是"char-0 有 Lorentzian 框架，但能否触达 }\zeta\ \text{是另一回事"}\ ✓$$
$$\qquad\textbf{与 }V105\ \text{第 6 行／G13 的同域性 ✓}：\text{那里问"什么数学装置能在 char-0 产生 }\sqrt{}\ \text{尺度正性 ⟹ 尚无"}\ ✗\ \text{—— Lorentzian 理论正是}\textbf{该问题的现代答案域} ✓\ \text{（虽然其 }\sqrt{}\ \text{是以对数凹／二项式尺度出现 ✓）}$$

### ② 方法形状与我们的同构 ✓
$$\text{本文核心 ✓}：\text{"比值是否有上界"}\iff\textbf{离散凸性（M-凸）}\ +\ \textbf{锥对偶}\ ✓$$
$$\qquad\Longleftrightarrow\ \text{我们反复使用的"预算／比率 ＋ 锥／对偶"推理 ✓（}E187\text{／}E199\text{／}E202\text{／}E212\ \text{的 }D/|B|,\ \lambda,\ \rho\ ✓）$$
$$\qquad\textbf{差别 ✓}：\text{他们得到}\textbf{尖锐、无条件、对偶型}答案 ✓；\text{我们得到的是经验／结构型 ✗}$$

### ③ ⚠️ 但它**不**填补 $R_{\rm residual}$（✓ 三条理由 ✓）
$$\text{(i) }\text{Lorentzian 是}\textbf{有限多项式} \text{上的条件 ✓（支撑须 M-凸 ✓）⟹ }\zeta\ \text{的零点数据不是这种有限支撑对象 ✗}$$
$$\text{(ii) }\text{对 }\xi\ \text{的可对接点 ＝ }\textbf{Jensen 多项式}\ J^{d,n}(X)=\sum_j\binom dj\gamma_j(n)X^j\ ✓;\ \text{而 }\textbf{hyperbolicity（实根）}\iff\text{RH}\ ✓（\text{Jensen–Pólya ✓；Griffin–Ono–Rolen–Zagier 已证 }d\le\text{界／大 }n\ \text{的情形 ✓）}$$
$$\text{(iii) }\textbf{Lorentzian}\Longrightarrow\textbf{hyperbolic}\ ✓\ \Longrightarrow\ \text{若 }\xi\text{-Jensen 是 Lorentzian ⟹ }\textbf{直接得 RH}\ ✗✓$$
$$\qquad\Longrightarrow\ \boxed{\text{"ξ-Jensen 是 Lorentzian"这一命题}\textbf{本身是 RH 强度}\ ✗\ \Longrightarrow\ \text{不能作为无条件输入 ✓}}$$
$$\qquad\qquad\text{（与 }L3\text{／}N29\text{／}V124\ \text{的结论同型 ✓：正性型 ⟹ 位置盲／循环 ✓）}$$
$$\Longrightarrow\ \boxed{\textbf{净收益 ✓}：\text{新闻给我们一个【精确的框架名】，}\textbf{而非填补缺口};\ \text{故 }R_{\rm residual}\ \text{的描述被锐化为：}\ \text{"char-0 的 }\textbf{Lorentzian／Hodge–Riemann 型正性，带算术支撑"}\ ✓✓}$$

## §2 由此得到的一个**具体、可判定的小审计**（⛔ 可选 ✓）
$$\boxed{\text{ξ-Jensen 多项式路线是否【形式上】落入 Lorentzian 框架？}}$$
- 已知 ✓：hyperbolicity ⟺ RH（Jensen–Pólya ✓）；Lorentzian ⟹ hyperbolicity ✓
- 待审两点 ✓：**(a)** ξ-Jensen 的**支撑／递归**是否满足 M-凸（一元多项式情形 M-凸退化为普通对数凹 ✓ —— 系数是 $\binom dj\gamma_j(n)$ ✓，即问 $\{\gamma_j(n)\}$ 是否 ultra-log-concave ✓）；**(b)** 其**签名条件**是否形式上等价于 RH 强度 ✗
$$\qquad\Longrightarrow\ \text{若 (b) 成立 ⟹ 该路线落在我们已封的 }D_1\text{／}L3\ ✗✓\ \text{（与 §1③ 一致 ✓）}$$
$$\qquad\textbf{性质 ✓}：\text{有界、可判定 ✓，不需要新机制 ✓（\textbf{未做 ✓}}—— 需您指示 ✓）$$

## §3 方法论层面可借用的三条（✓）

$$\textbf{(a) }\text{"把二次情形推到任意次数"}\ ✓\ ——\ \text{正是我们 }H1\text{／}H2\ \text{面对的"线性 → 二次"形状 ✓；其工具 ＝ }\textbf{离散凸性 ＋ 锥对偶} \✓（可借鉴为审计工具 ✓）$$
$$\textbf{(b) }\textbf{AI 的正确用法 ✓}（本文自述 ✓）：\text{数值计算 ＋ }\textbf{证明思路} ＋ \text{编辑};\ \text{关键推导与核验仍由人类完成 ✓}$$
$$\qquad\Longrightarrow\ \text{对本会话的映射 ✓}：\text{AI 擅长}\textbf{审计／查重／分类／交叉引用} ✓\ ——\ \text{这正是我们这几轮在做的事 ✓；而"发明新机制"仍是短板 ✗（与 Gowers 观察一致 ✓：AI 目前多为反例型 ✓；我们项目也以负面／NO-GO 结果为主 ✓ —— }\textbf{结构性共鸣 ✓）}$$
$$\textbf{(c) }\textbf{Lean 形式化成本骤降 ✓}：\text{Claude 11 天形式化 Fermat 证明（1300 万行 Lean ✓）};\ \text{Erdős 问题经 Aristotle Lean 验证 ✓}$$
$$\qquad\Longrightarrow\ \text{对我方}\textbf{已停放的两篇论文}\ ✓（`dn-project/papers/li-range` ✓、`brown-thm2-classical` ✓）\textbf{有直接实践意义 ✓}：\text{可用 Lean 加固 ✓（本机已装 Lean 4.33 ✓；Mathlib 未装 ⚠️ —— 安装需数 GB ⚠️，见 TOOLS.md ✓）}$$

## §4 建议与边界（✓）

$$\textbf{(1) 记档 ✓}（本档 ✓）：\text{外部输入候选 ＋ 锐化后的 }R_{\rm residual}\ \text{描述 ✓}$$
$$\textbf{(2) 可选小审计 ⛔}：\text{ξ-Jensen ⟹ Lorentzian 的}\textbf{形式} \text{等价性检验（有界、可判定 ✓，§2 ✓）}$$
$$\textbf{(3) }\textbf{不改写 }V137\ \text{的 SEARCH BRANCH CLOSED ✓}：\text{因为新闻}\textbf{没有} \text{给出不过 }E105\text{／}T5\text{、}AOB\text{／}O2\text{、}V127\ \text{的新箭头 ✗ —— 它给的是 char-0 正性框架，而 char-0 正性 ≡ 我们已封的 }D_1\ ✗✓$$
```
⚠️ §1① 的"Lorentzian ＝ char-0 极化框架"为【数学事实级 ✓】（Brändén–Huh 定义与主定理 ✓）；其与 V105/G13 的"同域"判断为【本档结构性 ✓ II 类】
⚠️ §1③ 的三条理由为结构性 ✓；其中 (iii)（Lorentzian ⟹ hyperbolic ⟹ RH 强度）为【逻辑蕴含 ✓ 层次清楚 ✓】
⚠️ 本档未使用任何 RH ✓；未跑 Lean ✓；未做计算 ✓（除网络核查 ✓）
✅ 净产出 ✓：① 一手事实核清 ✓；② ⭐ 与 V136 §2(v) 的修正项 ✓；③ ⭐ 不填补残量的三条理由 ＋ 残量描述锐化 ✓；④ 一个可判定小审计的登记 ✓；⑤ 方法论三条（含 Lean 成本骤降 ✓）
```
$$\boxed{\text{V141 ✓：Lorentzian 有界比率（arXiv:2609.05341 ✓ AI 协助 ✓）对我们}\textbf{有帮助但是框架级，不是缺口级}：\text{① }\textbf{它正是 char-0 的极化／Hodge–Riemann 正性框架}（不需 Frobenius ✓）⟹ \textbf{须修正 }V136\text{ §2(5) 的"char-0 未发现对应结构"}\ ✓；\text{② 其方法（离散凸性 ＋ 锥对偶）与我们同形但更尖锐 ✓；③ }\textbf{但不填补 }R_{\rm residual}\ ✗：\text{Lorentzian 是有限小多项式条件 → }\zeta\ \text{不可对接；可对接的 }\xi\text{-Jensen 路线中 hyperbolicity ⟺ RH，而 Lorentzian ⟹ hyperbolic ⟹ }\textbf{该命题本身即 RH 强度 ✗（＝}D_1\text{ 型，已封）} ⟹ \textbf{净收益 ＝ 残量描述锐化为"char-0 Lorentzian／Hodge–Riemann 型正性，带算术支撑"}\ ✓；\text{④ 附一个可判定小审计（ξ-Jensen 是否形式上 Lorentzian）＋ 方法论三条（含 Lean 形式化成本骤降 ✓ 对我方停放论文有直接意义 ✓）}$$


---

## §5 ⚠️ 勘误（2026-09-14 23:33，`V142` 审计后 ✓ T10 ✓）

$$\text{原文（§1③，已废止 ✗）}：\text{"Lorentzian}\Longrightarrow\text{hyperbolic}\ ⟹\ \text{"ξ-Jensen 是 Lorentzian"这一命题本身是 RH 强度 ✗"}\ ✗$$
$$\textbf{错误 ✓}：\textbf{Lorentzian}\ \not\Longrightarrow\ \textbf{hyperbolic}\ ✗\ ——\ \text{反例（`V142` §2 ✓）}：t^3+3t^2+3t+3\ ✓\ \text{归一化系数全 1 ⟹ 超对数凹 ✓ 但 }(t+1)^3+2\ \text{一实两复 ✗}$$
$$\textbf{正确方向 ✓}：\text{stable／hyperbolic}\ \Longrightarrow\ \text{Lorentzian}\ ✓（\text{弱化关系 ✓）}\ \Longrightarrow\ \text{Lorentzianity}\ \textbf{弱于}\ RH\ ✗\ \text{（可能无条件可证 ✓）}$$
$$\textbf{结论不变但机制更正 ✓}：\text{Lorentzian 路线}\textbf{确实不填补 }R_{\rm residual}\ ✗，\text{但理由}\textbf{不是}\text{"它与 RH 等价 ✗"}，\text{而是}\text{（`V142` §3 ✓）：其超对数凹部分}\textbf{已被 GORZ 无条件蕴含} ✓✓，\text{剩余差距（Lorentzian ⟹ 双曲）＝ RH 所在 ✗，且整条双曲性路线}\textbf{已由 Farmer 关闭} ✓✓$$
