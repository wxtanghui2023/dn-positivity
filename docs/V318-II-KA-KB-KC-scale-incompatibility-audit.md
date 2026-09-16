# V318-Ⅱ — **尺度不相容审计**（K-A／K-B／K-C）＋ 「精确恒等式」出口的正式退出判定

> 唐先生 2026-09-16 16:55 指定。目标不是找 K8–K20，而是把 (a) 改造成**闭包判定**：
> $$\text{双侧 exact identity}\overset{?}{\Longrightarrow}\text{必然属于 I--V}$$

---

## 1. 最小结构定义（避免定义过宽／过窄）
$$A_T^{\text{local}}=\sum_{n\le X}a(n)F(n)\quad(a\ \text{来自乘性结构}，F\ \text{来自加性结构})$$
$$A_T^{\text{global}}=\sum_{m\le Y}b(m)G(m)\quad(\text{真正不同的全局表达})$$
$$\text{二者之间存在}\ \textbf{无条件 exact equality}。$$

## 2. 四项闭包检查（任一成立即坍缩）
$$\begin{array}{c|c}
\text{检查} & \text{坍缩到}\\ \hline
\text{global side 只是 Fourier/Poisson 对偶} & \mathrm{I}\\
\text{只是有限范围重排／计数} & \mathrm{V}\\
\text{产生大筛／相关型二次量} & \mathrm{III}\\
\text{本质上等价于已有 positivity} & \mathrm{IV}
\end{array}$$
$$\textbf{只有四项全部否定，才进入 VI}。$$

## 3. 关键观察（K1–K7 的共同现象）
$$\boxed{\text{exactness}\ \not\Rightarrow\ \text{new spectral information}}$$
$$\text{Poisson}\to\text{Fourier duality}；\text{CRT}\to\text{product decomposition}；\text{Möbius inversion}\to\text{incidence inversion}；\text{Voronoi}\to\text{dual summation}$$
$$\Longrightarrow\ \text{精确性本身}\ \textbf{不产生新约束}。\quad\text{应找的是：}\boxed{\text{exact identity}+\textbf{irreversible}\ \text{quantitative consequence}}$$
$$\textbf{irreversible 的定义（本轮新增判据）}：\text{若 consequence 可由原恒等式}\ \textbf{反向恢复}\ \text{或仅换表示}\ \Longrightarrow\ \text{非 VI}。$$

---

## 4. K-A 审计：局部—全局乘法/加法交换律
$$\text{模板：}\sum_n a(n)\sum_{d\mid n}F(d)\ \leftrightarrow\ \sum_d F(d)\sum_m a(dm)\quad(\text{divisor-swap / balance 型})$$
$$\text{结构检查：exact}\ ✓\quad\text{additive}\times\text{multiplicative}\ ✓\quad X\asymp T\ ✓\quad\text{RH-blind}\ ✓$$
$$\textbf{坍缩依据（三条独立路径）}：$$
$$\text{(a) 交换律：V241 已证}\ \textbf{所有 dilatation 生成元}\ T_p\ \text{彼此交换（}T_pT_q=T_qT_p\text{）} \Longrightarrow \text{“乘性}\times\text{加性”的交换}\ \textbf{只是重排}，\text{不产生新刚性}\to\mathrm{V}$$
$$\qquad \text{（V284 五族全败：}[D,U]\ \text{型算子在 V206–V208 中一律退回熟悉算术量 d}(n)-2^{\omega(n)}\text{、}d(n)-n\text{、}\mu/\text{Mertens 等）}$$
$$\text{(b) 后果落大筛／MV 型二次不等式}\ \to\mathrm{III}\ \text{（并已在 V300 被确认为纯调和分析、无 RH 输入）}$$
$$\text{(c) 其距离型推论（Nyman–Beurling 型）}\in\ \text{等价判据族}\ \to\mathrm{IV}\ \text{（POS1/POS2 同址）}$$
$$\Longrightarrow\ \textbf{K-A 坍缩}（\mathrm{V}+\mathrm{III}+\mathrm{IV}）$$

## 5. K-B 审计：模结构—整数结构的 exact compatibility
$$\text{模板：}\mathcal A(\mathbb Z/q\mathbb Z)\ \leftrightarrow\ \mathcal A(\mathbb Z)\quad(\text{须排除 CRT 已覆盖的情形})$$
$$\textbf{坍缩依据}：$$
$$\text{(a) 排除 CRT 后剩下的只是}\ \textbf{reciprocity｝（互反律）}\ \text{型内容}；\ \text{V241-D 已证其为}\ \textbf{trivial coboundary}\ ✗$$
$$\text{(b) 结构常数级：V177 证}\ H^{1}(C_2,K^{\times}_{\text{arith}})=1 \Longrightarrow \Phi\ \text{必为 coboundary} \Longrightarrow \textbf{平凡}；\ \text{V176 erratum 同向}$$
$$\text{(c) 支撑／平衡层：V179（cross-prime involution 锥 + balancing）}\to\text{V180 finite-support criterion}$$
$$\qquad \to\ \textbf{spectral-capacity conflict}\ \Longrightarrow\ \textbf{FSC-DEAD（V181 §7）}$$
$$\Longrightarrow\ \textbf{K-B 坍缩}（\mathrm{V}+\mathrm{I}）$$

## 6. K-C 审计：**尺度不相容**（本轮主轴，最值得审的一个）
$$\text{要求：存在}\ A_T\ \text{同时满足}\ A_T=\sum_{\text{additive}}(\cdots)=\sum_{\text{multiplicative}}(\cdots)，\text{且}\ X_{\text{add}}\asymp T^{\alpha},\ X_{\text{mult}}\asymp T^{\beta},\ \alpha\ne\beta$$
$$\textbf{动机（唐先生）}：\text{V316/V317 的墙全部发生在}\ \textbf{同尺度预算}（T^{1/3}、T、T\log T）\Longrightarrow\ \text{若存在精确双尺度硬约束，可能产生此前没有的 rigidity}。$$

### 6.1 候选精确跨尺度恒等式逐一
$$\textbf{K-C1 FE／theta 变换律（}\theta(1/x)=\sqrt x\,\theta(x)\text{）}：\text{exact}\ ✓\ \text{双尺度}\ ✓\ \text{但属}\ \textbf{archimedean/A-leak}\ \text{通道}$$
$$\qquad \Longrightarrow\ \text{V172 §5a ＋ V181 ⟹ 旧语言已封}（\text{且 V229-A／V248 §2 已审其在 }\beta\ \text{侧的双侧性）}\ ✗$$
$$\textbf{K-C2 Voronoi 型求和（短尺度和}\leftrightarrow\text{长尺度和）}：\text{exact}\ ✓\ \text{双尺度}\ ✓\ \text{但两侧由}\ \textbf{Poisson/Fourier 对偶}\ \text{联系}$$
$$\qquad \Longrightarrow\ \text{第 1 项检查即命中}\ \to\mathrm{I}；\text{其余后果为除数问题误差项}\ \to\mathrm{V}\ ✗$$
$$\textbf{K-C3 Selberg/Guinand 迹式（几何}\leftrightarrow\text{谱）}：\ \text{exact}\ ✓\ \text{但}\ \text{Deninger/AOB 线已在 G10／6.6 判死}\ \to\mathrm{I/IV}\ ✗$$
$$\textbf{K-C4 显式公式（素数}\leftrightarrow\text{零点，双尺度）}：\text{直接引零点}\ \Longrightarrow\ \textbf{违反 R7④}\ \to\mathrm{I}\ ✗$$
$$\textbf{K-C5 Mellin/Laplace（Perron＋留数）}：\text{由留数直接引零点}\ \to\mathrm{I}\ ✗$$

### 6.2 决定性障碍（为什么 α≠β 的机制无法产生 VI）
$$\textbf{V294-A（已 CLOSED）}：\text{对}\ \textbf{任何有限阶局部零侧核}，\text{聚合增益}\ G(K)\le0，\text{等号由 1-body 相位机制取到}$$
$$\qquad \Longrightarrow\ \text{有限阶局部聚构}\ \textbf{无法制造新尺度}；\text{“新尺度”只能来自非局部／无限阶／算术相关}$$
$$\text{而 V295 已进一步定位：}\text{非局部核的增益}\ \textbf{恰好}\ \text{等于}\ c^{\text{geom}}\ \text{的带宽需求} \Longrightarrow \text{与无条件支撑}>1\ \text{同址（V162 墙）}$$
$$\textbf{另一侧证据（本档）}：\text{所有已知精确跨尺度恒等式的双尺度对}\ (\alpha,\beta)\ \text{都由}\ \textbf{对偶}\ \text{联系（Poisson／Mellin／迹），}$$
$$\qquad \text{而非由}\ \textbf{独立两个算术聚合}\ \text{联系} \Longrightarrow \text{第 1 项检查必然命中}\ \to\mathrm{I}。$$
$$\Longrightarrow\ \textbf{K-C 坍缩}（\mathrm{I}+\mathrm{V}；\text{且 VI 型 rigidity 被 V294-A 从结构上排除）$$

---

## 7. 判定汇总
$$\begin{array}{c|c|c}
\text{类型} & \text{exact？} & \text{判定}\\ \hline
\text{K-A 局部—全局交换} & ✓ & \textbf{坍缩}（\mathrm{V/III/IV}；V241 交换律 + V284）\\
\text{K-B 模—整数兼容} & ✓ & \textbf{坍缩}（\mathrm{V/I}；V177／V241-D／V181 FSC-DEAD）\\
\text{K-C 尺度不相容} & ✓\ \text{（候选均含对偶）} & \textbf{坍缩}（\mathrm{I/V}；\+\ \textbf{V294-A 结构性排除}）
\end{array}$$
$$\Longrightarrow\ \mathrm{VI}\ \textbf{仍为空}。$$

## 8. 「精确恒等式」出口的正式退出判定（依唐先生 16:55 预设准则）
$$\text{预设准则（唐先生原话）：}\textbf{若 K-A/K-B/K-C 也全部坍缩，则正式退出“exact identity”出口，转向 §E.4 第二出口。}$$
$$\Longrightarrow\ \textbf{本档建议：}\ \boxed{\text{正式退出「精确恒等式」出口}}$$
$$\text{退出理由（三重）}：$$
$$\text{① }\mathcal D_{\text{new}}\ \text{内已审计的候选（K1–K7 ＋ K-A/B/C）}\ \textbf{全部坍缩}；$$
$$\text{② 坍缩机制有}\ \textbf{结构性共因}：\text{乘性与加性}\ \textbf{交换}（V241）、\text{对偶联系双尺度（Poisson/Mellin/迹）}、\text{有限阶局部核无新尺度}（V294-A）；$$
$$\text{③ 继续枚举 K8–K20}\ \text{只会在同一结构性共因下重复坍缩。}$$

## 9. 转向 §E.4 第二出口（下一步骤，待唐先生裁定）
$$\text{§E.4 活问题（V149 起登记）：}\text{“这张类表是否完整？”}\ \begin{cases}\text{找到}\Longrightarrow\text{新方向；}\\ \text{证明完整}\Longrightarrow\text{空间真正关闭、应改变目标。}\end{cases}$$
$$\text{第二出口的两种可执行形态}：$$
$$\text{(甲) 攻 E148（存在}\ \exists\text{-型 RH 等价判据的显式构造）—— 与覆盖论证命运绑定；}$$
$$\text{(乙) 攻"类表完整性"本身：}\text{给出可证的表征定理（}\S\text{E.2）以缩小范围，或给出第六类的独立性证据}$$

## 10. 边界（N1/N2 严守）
$$\text{① 本档为}\ \textbf{枚举型审计}，\text{不得升级为"}\mathrm{VI}\ \text{不可能存在"；}\quad\text{② "未找到"}\ne\text{"不存在"；}$$
$$\text{③ K-A／K-B／K-C 的坍缩依据分别引 V241／V284、V177／V241-D／V181、V294-A／V295（均为档案既有 CLOSED 或已审计结论，本轮未逐行重验）；}$$
$$\text{④ }\textbf{irreversible 判据（§3）是本轮的新工具}，\text{建议保留为后续筛选条件；}$$
$$\text{⑤ 全档}\ \textbf{未用 RH}；零数值；\text{未跑 Lean}。$$

## 11. 净产出
$$\text{(i) 把 (a) 改造成}\ \textbf{闭包判定}（四项检查）＋\ \textbf{irreversible 判据}；$$
$$\text{(ii) K-A／K-B／K-C 逐一审计，三者全部坍缩，并提炼出}\ \textbf{结构性共因}（乘加交换／对偶／有限阶无新尺度）；$$
$$\text{(iii) 依预设准则给出}\ \textbf{退出"精确恒等式"出口的正式判定}；$$
$$\text{(iv) 指向 §E.4 第二出口的两条可执行形态（甲／乙），待唐先生裁定。}$$
