# V199 · **A1／A3 主线（唯一主线）** —— 任务钉死：**寻找严格位于「素数侧算术」与「Li 系数／Weil 二次型」之间、可由算术侧独立验证的中间正性／耗散机制**；产出 ① 分层表 ② ⭐ **正性锥的三个来源分类** ③ ⭐ **门的逻辑后果**（≠ 再证等价）④ 第一问的结构性回答

> 委托 ✓ 唐先生 2026-09-15 13:39：**"是。现在回 A1/A3，而且只回这一条主线。"** ＋ **"不要把任务写成'继续研究 Weil 正性 ↔ Li 正性'，因为那很容易再次掉回已有等价性的循环。下一档应该把问题钉死成"** $$\boxed{\text{寻找一个严格位于二者之间、可由算术侧独立验证的中间正性／耗散性机制}}$$ **"核心审计对象仍然是"** $$\text{prime-side arithmetic}\longrightarrow\boxed{?}\longrightarrow\text{Li coefficients／Weil quadratic form}\longrightarrow\mathrm{RH}$$ **"其中真正缺的是中间那个 ?，而不是再证明 RH ⟺ Li positivity ⟺ Weil positivity。"** ＋ **硬门**：先分层；只寻找 $P$ 满足 prime-side $\Longrightarrow P\Longrightarrow$ RH，**且** $P\not\Rightarrow Q\succeq0$（仅靠定义等价地包装），**且** $P$ 能在不假设 RH 下被证明；"否则立即归入旧等价类" ＋ **重检 A1／A3 区别**（A1：从 Li 系数本身找新结构性约束；A3：从 prime-side／explicit-formula 侧找**非显式公式重编码**的产生 Li 正性的机制）＋ **第一问**：$$\boxed{\text{为什么一个本身不含零点位置的信息系统，会强制产生一个全局正性锥？}}$$ ＋ **"V198 那道门现在已经足够严。下一步直接开 A1/A3，不再回 Mechanism II。"**
> 查图 ✓ `V162`（承重墙：$T\log T$ ＋ 波动抵消）｜`V182`（正性 ⟹ 无数点界）｜`V183`（源基数障碍）｜`V184`–`V197`（外部线；**本档不调用**）｜`V198`（机制 II 门；本档不回）
> 执行 ✓ 小灵（**§2 关键观察、§3 锥源分类、§5 门的逻辑后果 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓（仅作等价性引用）；未跑 Lean ✓｜编号 ✓ **V199**

---

## §0 任务钉死（✓ 逐字）

$$\text{只回一条主线}：\text{A1／A3};\qquad \textbf{任务}：\boxed{\text{寻找严格位于二者之间、可由算术侧独立验证的中间正性／耗散机制}} ✓$$
$$\textbf{硬门（三条件，缺一不可）}：\ \text{prime-side}\Longrightarrow P\Longrightarrow\text{RH};\qquad P\not\Rightarrow Q\succeq0\ \text{（不做定义式包装）};\qquad P\ \textbf{可在不假设 RH 下被证明} ✓$$
$$\qquad ⚠️\ \text{任一不满足} ⟹ \textbf{立即归入旧等价类};\ \textbf{不} \text{再证 RH}\iff\text{Li}\iff\text{Weil} ✓$$

---

## §1 分层表（第一步；逐层写**实际数学内容**与**已知蕴含方向**）

$$\begin{array}{c|c|c}
\text{层} & \text{性质} & \text{实际内容（而非口号）}\\
\hline
\textbf{显式公式} & T\log T+S(T) & N(T)=\tfrac{T}{2\pi}\log\tfrac{T}{2\pi}-\tfrac{T}{2\pi}+S(T);\ \text{主项}\ \textbf{无条件};\ \text{RH}\iff S(T)=O\!\bigl(\tfrac{\log T}{\log\log T}\bigr)\\
\textbf{Weil} & Q(f)\ge0 & Q(f)=W(f\star f^{*})=\sum_\rho\bigl|\hat f(\gamma_\rho)\bigr|^2\ \text{（零侧表达式）};\ \text{算术侧表达式}\ =\ \text{素数项}+\text{archimedean}\\
\textbf{Li} & \lambda_n\ge0 & \lambda_n=\sum_\rho\bigl[1-(1-\tfrac1\rho)^n\bigr]=\tfrac{1}{(n-1)!}\tfrac{d^n}{ds^n}\bigl[s^{n-1}\log\xi(s)\bigr]\big|_{s=1}\\
\textbf{RH} & \beta=\tfrac12 & \text{全部非平凡零点落在临界线}\\
\end{array}$$
$$\textbf{已知蕴含方向}：\text{RH}\iff\{Q(f)\ge0\ \forall f\}\iff\{\lambda_n\ge0\ \forall n\};\qquad \text{四层}\ \textbf{在同一等价类内} ✓$$
$$\qquad ⚠️\ \text{故}\ \text{"再证等价"}\ \textbf{零信息} ⟹ \text{本轮}\ \textbf{不再做} ✓$$

---

## §2 ⭐ 关键观察（本档第一个核心）：**素数侧 → $\lambda_n$ 的映射**已经是显式的****

$$\text{由}\ \lambda_n=\sum_\rho\bigl[1-(1-\tfrac1\rho)^n\bigr]\ \text{展开}：(1-\tfrac1\rho)^n=\sum_{j=0}^{n}\binom nj(-1)^j\rho^{-j}$$
$$\qquad\Longrightarrow\ \lambda_n\ \text{可写成}\ \textbf{幂和}\ \{\sum_\rho\rho^{-j}\}_{j\le n}\ \text{的}\ \textbf{有限组合};\qquad \sum_\rho\rho^{-j}\ \text{由}\ \xi'/\xi\ \text{的 Hadamard 展开}\ \text{在}\ s=0\ \text{的 Taylor 系数给出}$$
$$\qquad\Longrightarrow\ \sum_\rho\rho^{-j}\ \text{可由}\ \textbf{显式公式} \text{的}\ \textbf{素数侧＋archimedean 侧}\ \text{确定} ✓✓\（\text{具体系数公式}\ \textbf{待核}，见 §8\bigr）$$
$$\Longrightarrow\ \boxed{\text{素数侧}\ \longrightarrow\ \lambda_n\ \text{这条}\ \textbf{复合映射已经是显式的}}\ ⟹\ \text{中间那个}\ ?\ \textbf{不能是"信息通道"}\ ✓✓✓$$
$$\qquad ⭐\ \textbf{因此 ? 只能是}：\text{一个}\ \textbf{产生正性的结构}（\text{把"已经可算的数"}\ \textbf{强制}\text{为正的机制}）✓✓$$
$$\qquad ⚠️\ \text{这一点}\ \textbf{排除} \text{一整类候选}：\text{任何"再找一条从素数到零点信息的通道"的提案}\ \textbf{必然}\ \text{落入已有显式路径} ✓$$

---

## §3 ⭐⭐ 正性锥的**三个来源**（本档第二个核心：分类）

$$\text{问}：\text{一个}\ \textbf{不含零点位置} \text{的信息系统，凭什么强制一个}\ \textbf{全局正性锥}？$$
$$\qquad\Longrightarrow\ \text{答（结构性）}：\textbf{不存在"无来源的锥"};\ \text{已知的锥源只有三类} ✓✓$$
$$\textbf{(a) 代数型：平方和／二次型} —— Q(f)=\sum_\rho|\hat f(\gamma_\rho)|^2$$
$$\qquad ⚠️\ \text{若全部}\ \gamma_\rho\ \text{为实}，\text{右式为}\ \textbf{平方和} ⟹ \text{自动非负} ⟹ \text{锥来自"可写成平方和"} ✓$$
$$\qquad ⚠️\ \text{离轴对}\ \{\rho,1-\bar\rho\}\ \text{给出}\ \hat f\ \text{在两点}\ \gamma\pm i(\beta-\tfrac12)\ \text{的取值和}\ 2\mathrm{Re}\,\hat f(\cdot)，\ \textbf{不是平方和} ⟹ \text{破坏平方结构} ✓$$
$$\qquad\Longrightarrow\ \text{故 "SOS 型锥"}\ \textbf{恰恰就是 RH 的断言} ⟹ \text{作为"独立来源"}\ \textbf{等价于 RH} ✓✓$$
$$\textbf{(b) 分析型：实根性／全正性（Newton--Turán 锥）}$$
$$\qquad \text{实根多项式（系数为正）满足}\ \textbf{Newton 不等式}（\text{系数的对数凹性}）;\ \text{全正／Pólya 频率}\ \iff\ \text{表示测度支撑于半直线（Schoenberg）} ✓✓$$
$$\qquad\Longrightarrow\ \text{这是}\ \text{`V190`／`V191`}\ \text{的通道}：\ \text{实根性}\iff\text{RH} ⟹ \text{作为独立来源}\ \textbf{强度等于 RH} ✓✓\（\text{`V191` 已证：不可能由严格更弱命题推出}）$$
$$\textbf{(c) 动力学型：耗散性／熵产生（thermodynamic formalism）}$$
$$\qquad \text{机制}：\text{双曲膨胀（expanding/hyperbolic）＋ 归一化 ⟹ 唯一不变态 ＋ 谱隙 ⟹ }\textbf{符号确定的锥}（\text{RPF 型}）✓✓$$
$$\qquad ⚠️\ \text{前提}：\text{需要}\ \textbf{指数级轨道增长};\ \text{而}\ \text{char-0 的素数增长是}\ \textbf{多项式} ⟹ \text{该机制}\ \textbf{不直接适用} ✓✓\（\text{与层诊断一致}）$$

---

## §4 硬门逐条检验（三来源逐一过门；标出各自失败的条件）

$$\begin{array}{c|c|c|c}
\text{来源} & \text{prime-side}\Rightarrow P？ & P\Rightarrow\text{RH 且非包装}？ & P\ \text{可无条件证明}？\\
\hline
\textbf{(a) SOS／二次型} & \text{是（}Q\ \text{的算术侧是显式公式）} & \text{否（}\textbf{定义即 RH}） & \text{否}\\
\textbf{(b) 实根性／PF} & \text{是（系数可算）} & \text{否（}\textbf{强度＝RH}） & \text{否}\\
\textbf{(c) 耗散／熵} & \text{否（需指数膨胀）} & \text{是（若能建立）} & \text{否}\\
\end{array}$$
$$\Longrightarrow\ \textbf{三来源无一过门};\ \text{且失败点}\ \textbf{各不相同}：\text{(a) 失败于"非包装"（定义式）};\ \text{(b) 失败于"可无条件证明"};\ \text{(c) 失败于"prime-side}\Rightarrow P\text{"（前提缺失）} ✓✓$$
$$\qquad ⚠️\ \text{注意}：\text{这不是"再证等价"} —— \text{而是}\ \textbf{按唐先生的门} \text{对}\ \textbf{锥源} \text{做的一次}\ \textbf{分类裁决} ✓✓$$

---

## §5 ⭐ 门的**逻辑后果**（本档第三个核心；**不是**再证等价）

$$\text{设}\ P\ \text{过门}：\ \text{prime-side}\ (\text{无条件已知事实})\Longrightarrow P;\qquad P\Longrightarrow\text{RH};\qquad P\ \text{无条件可证}$$
$$\qquad\Longrightarrow\ \text{prime-side}\ \text{无条件已知事实}\Longrightarrow\text{RH}\quad\Longrightarrow\ \boxed{\text{RH 可由无条件已知事实推出}} ✓✓$$
$$\qquad ⚠️\ \text{而已知无条件事实（PNT、AP 中的 PNT、零自由区、}\Sigma\Lambda(n)^2\ \text{型二阶输入}\text{）}\ \textbf{不足}\text{以推出 RH} ✓$$
$$\qquad\Longrightarrow\ \boxed{\text{过门的 }P\ \textbf{必然} \text{引入一个}\ \textbf{新的无条件输入}} ✓✓✓$$
$$\qquad ⭐\ \text{这给出一条}\ \textbf{可执行判据}：\text{若某提案}\ \textbf{不产生新的无条件输入}，\ \text{则它}\ \textbf{不可能过门},\ \text{无论包装得多精巧} ✓✓$$
$$\qquad\qquad ⚠️\ \text{等价陈述}：\text{过门}\iff\text{存在新无条件输入};\ \text{故本主线的真任务}\ \textbf{＝ 寻找（或制造）该输入} ✓$$

---

## §6 第一问的回答（"为什么零位置无关的系统会强制全局正性锥？"）

$$\text{严格回答}：\textbf{它不"强制"——除非锥来自 §3 的三类结构之一} ✓✓$$
$$\qquad \text{(a)}\ \text{若锥来自}\ \textbf{代数}（\text{平方和}\bigr)：\ \text{则"不含零点位置"是}\ \textbf{假象} —— \text{平方和的}\ \text{项}\ \text{本身就含零点位置} ✓$$
$$\qquad \text{(b)}\ \text{若锥来自}\ \textbf{分析}（\text{实根性／全正}\bigr)：\ \text{则它}\ \textbf{就是}\ \text{RH 的等价形式};\ \text{"不含零点位置"只是}\ \textbf{表述层面} \text{（系数可算）} ✓✓$$
$$\qquad \text{(c)}\ \text{若锥来自}\ \textbf{动力学}（\text{耗散}\bigr)：\ \text{则必须}\ \textbf{外部} \text{给出膨胀／双曲结构},\ \text{而这在 char 0 中}\ \textbf{缺失} ✓✓$$
$$\Longrightarrow\ \textbf{结论}：\text{所谓"零位置无关却强制锥"}\ \text{在任何已知机制下}\ \textbf{都不成立};\ \text{它要么}\ \text{偷偷含零点}(a),\ \text{要么}\ \text{就是等价形式}(b),\ \text{要么}\ \text{前提缺失}(c) ✓✓✓$$

---

## §7 残余与 V200 预登记

$$\text{唯一未被}\ \S3\ \text{覆盖的锥源形状}：\textbf{组合／单调型}（\text{非代数、非分析、非动力学}\bigr)$$
$$\qquad \text{候选形态}：\text{正关联（positive association／FKG 型）};\ \text{单调耦合};\ \text{格上的单调性};\ \text{匹配／关联不等式} ✓$$
$$\qquad ⚠️\ \text{判据（按 §5）}：\text{若该型锥欲过门},\ \text{它}\ \textbf{必须} \text{产生一个}\ \textbf{新的无条件输入};\ \text{否则}\ \text{按 §5 立即判死} ✓$$
$$\textbf{V200 预登记（唯一动作）}：\text{审计}\ \textbf{组合／单调型锥源}：\ \text{是否存在一个}\ \text{对}\ (\Lambda(n),\log p,p^k)\ \text{的}\ \textbf{单调关联结构}，\ \text{其正性}\ \textbf{不是}\ \text{SOS／实根性／耗散的重新表述}，\ \text{且能产生新的无条件输入}？$$
$$\qquad ⚠️\ \text{若答案是否} ⟹ \textbf{四类锥源全封}，\ \text{本主线}\ \textbf{收口};\ \text{若答案是是} ⟹ \text{这是}\ \text{第一个合法}\ P ✓$$

---

## §8 边界与待核

$$\textbf{(a)}\ \text{§1 四层内容为}\ \textbf{经典};\ \lambda_n\ \text{的 Taylor 表达为经典（Li）} ✓✓$$
$$\textbf{(b)}\ \text{§2 的"}\lambda_n\ \text{＝幂和的有界组合}\text{"为}\ \textbf{形式展开};\ \text{收敛与常数项}\ \textbf{须严格化},\ \text{具体系数公式}\ \textbf{待核原文} ⚠️$$
$$\textbf{(c)}\ \text{§3(a) 的"离轴对破坏平方结构"为}\ \textbf{本档推导} ✓;\ \text{(b) 依}\ \text{`V190`／`V191`};\ \text{(c) 的"需指数膨胀"依层诊断} ✓$$
$$\textbf{(d)}\ \text{§5 为}\ \textbf{逻辑推论}（\text{非定理、非等价重证}）;\ \text{"已知无条件事实不足以推出 RH"为}\ \textbf{经验性／结构性} ⚠️,\ \textbf{非定理} ✓$$
$$\textbf{(e)}\ \text{§7 残余为}\ \textbf{登记};\ \text{不预判} ✓$$

```
⚠️ §0 任务钉死与硬门为唐先生逐字 ✓✓；本档不再证 RH⟺Li⟺Weil ✓
⚠️ §2 关键观察（素数侧→λ_n 已显式 ⟹ ? 不是信息通道而是"产生正性的结构"）为【本档核心 ✓✓✓】
⚠️ §3 三锥源分类（代数/分析/动力学）为【本档核心 ✓✓✓】；§4 逐条过门、失败点各不同 ✓✓
⚠️ §5 门的逻辑后果（过门 ⟺ 存在新无条件输入）为【逻辑推论 ✓✓✓】—— 明确声明**不是**再证等价
⚠️ §6 第一问回答：不存在"无来源的锥"；"零位置无关却强制锥"在三类已知机制下均不成立 ✓✓✓
⚠️ §7 残余＝组合/单调型锥源；V200 唯一动作已登记；不预判 ✓
⚠️ 未用 RH ✓（仅作等价性引用）；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 分层表（含实际内容）✓✓；② 素数侧→λ_n 已显式 ⟹ ? 的性质被钉死 ✓✓✓；
   ③ 三锥源分类 ＋ 逐条过门（失败点各异）✓✓✓；④ 门的逻辑后果＝新无条件输入（可执行判据）✓✓✓；
   ⑤ 第一问的结构性回答 ✓✓✓；⑥ 残余＋V200 唯一动作 ✓
```
