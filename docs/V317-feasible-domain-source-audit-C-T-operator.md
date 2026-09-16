# V317 — **可行域来源审计**（feasible-domain source audit）：$\mathcal C_T$ 算子能否来自真实算术恒等式

> 唐先生 2026-09-16 16:53 指定的下一阶段（V316 冻结后的第一个新问题）
> 定位：**不使用「支撑增益」**的算术量，能否改变 $c^{\text{geom}}$ 的可达上界？

---

## 1. 问题的反转（本轮的方法论核心）

$$\textbf{旧拓扑（已撞死）}：\text{arithmetic information}\longrightarrow\lambda\longrightarrow c^{\text{geom}}$$
$$\qquad \text{S1–S8 已把 forcing 语言压回：finite-order local correlation}\cup N(\sigma,T)\cup\text{value-surface}\cup\text{positivity cone}\cup\text{spectral re-encoding}$$
$$\textbf{新拓扑（本轮目标）}：\boxed{\text{arithmetic structure}\longrightarrow\text{new constraint / new identity on admissible }u\longrightarrow\text{variational value}}$$
$$\text{即：}\textbf{不强迫}\ \lambda>1，\text{而是改变 V316 的「可优化对象」本身。}$$

## 2. 机制形式（唐先生指定）

$$\text{寻找算术产生的约束算子}\ \mathcal C_T\ \text{使}\ \mathcal C_Tu=0，\text{且}\ v_\lambda\notin\ker\mathcal C_T，\text{研究}\ \inf_{u\in\ker\mathcal C_T}Q_\lambda(u)$$
$$\text{若}\ \inf_{\ker\mathcal C_T}Q_\lambda>Q_\lambda(v_\lambda)，\text{则突破来自}\textbf{可行域几何变化}，\textbf{而非 kernel norm 增长}\ \text{（与 forcing}\ \lambda>1\ \text{是完全不同的机制）}$$
$$\textbf{硬判死条件（唐先生原话）}：\mathcal C_T\ \textbf{不能是为了证明 RH 临时设计的}；必须先在\ \textbf{RH 不出现的条件}下从某自然算术对象导出。$$
$$\text{例：}\ \text{multiplicative law}+\text{additive law}\Longrightarrow\mathcal C_Tu=0；\quad\text{若推到末了}\ \mathcal C_Tu=0\iff\text{Weil positivity}\ \text{或}\iff N(\sigma,T)\ \text{条件}\ \Longrightarrow\ \textbf{立即 DEAD}。$$

## 3. 准入条件 A1–A7（唐先生指定，逐步执行）
$$\textbf{A1}\ \text{不是}\ N(\sigma,T)；\ \textbf{A2}\ \text{不是显式公式重写}；\ \textbf{A3}\ \text{不是 Weil/POS 正性}；$$
$$\textbf{A4}\ \text{不是有限阶局部相关核}；\ \textbf{A5}\ \text{不是单纯扩大}\ \lambda；\ \textbf{A6}\ \textbf{能够改变 admissible-space 的结构}；$$
$$\textbf{A7}\ \textbf{这种结构来自真实算术恒等式，而非人为加约束}$$
$$\textbf{A6+A7 是核心}：\text{若仅把}\ u\in\mathcal A\ \text{换成更小的}\ \mathcal A'\ \text{（人为）}\Longrightarrow\ \text{极小值变漂亮但}\ \textbf{无 RH 内容}；$$
$$\text{必须证：}\ \boxed{\text{Arithmetic identity}\Longrightarrow\mathcal A_{\text{arithmetic}}\subsetneq\mathcal A}\quad\text{且该 inclusion 在}\ X\asymp T\ \textbf{无条件、定量、可验证}。$$

## 4. 候选来源审计（逐一）
$$\textbf{C1 函数方程／Archimedean 对称（}\iota:\rho\mapsto1-\bar\rho\text{）}：\text{给的是 admissible 空间的}\ \textbf{反射对称约束}；$$
$$\qquad \text{但 V172 §5a（A-leak）＋ V181 ⟹ 属 archimedean 层}\ \textbf{已封} ✗$$
$$\qquad \text{（V229-A：FE 迫使任何 β-bound 双侧；V248 §2：FE 对称不排除临界线——只排除单侧集）}$$
$$\textbf{C2 乘性＋加性闭包：}\text{V241（所有 dilatation 生成元交换；Möbius/CF 的 holonomy 平凡）＋ V206–V208（}[D,U]\ \text{退回熟悉算术量）＋ \textbf{V284（五族全败）} ⟹ \text{已封} ✗$$
$$\textbf{C3 自相关／正定结构：}\text{kernel}\ |s-t|\ \text{与}\ B_{\text{fun}}\ \text{的正性结构}\ \textbf{已内建} \text{在 V316 的二次型里；}$$
$$\qquad \text{且其充分性}\iff\text{RH（POS1/POS2）}\Longrightarrow\ \textbf{A3 违反} ✗$$
$$\textbf{C4 值面／显式公式通道：}\ \textbf{A2 违反} ✗\ \text{（V283 §1／V258）}$$
$$\textbf{C5 零计数／密度：}\ \textbf{A1 违反} ✗$$
$$\textbf{C6 有限阶局部相关核：}\ \textbf{A4 违反} ✗\ \text{（V294-A 增益}\le0\text{）}$$
$$\textbf{C7 人为缩小}\ \mathcal A：\ \textbf{A7 违反} ✗$$
$$\textbf{C8 ⭐ 唯一真正自然且「非人为」的 C}_T\ \textbf{型对象}：\text{cross-prime involution 锥 + balancing（V179）}$$
$$\qquad \text{—— 由乘法结构与 FE 的交互产生的}\ \textbf{支撑/平衡约束}，\text{正文路线为}\ V173\to V180；$$
$$\qquad \textbf{结局：}V180\ \text{（finite-support criterion）遇上}\ \textbf{spectral-capacity conflict}\Longrightarrow\ \textbf{FSC-DEAD}\ \text{（V181 §7，唐先生判「结构性关闭，非临时搁置」）}$$

## 5. 审计结论
$$\textbf{C8 是档案中唯一的自然算术}\ \mathcal C_T\ \text{候选（A1–A5 均不违反），而它已在 V180/V181 死于 spectral-capacity conflict；}$$
$$\text{其余候选}\ \textbf{C1–C7 各违反 A1–A7}\ \text{之一}。$$
$$\Longrightarrow\ \boxed{\text{「可行域约束路线」DEAD（已审计范围）}}$$
$$\text{与 C⋆ 审计（V316-FREEZE）的关系：}\ \text{两者共同构成}\ \textbf{双向封口}——$$
$$\qquad \text{kernel 向：}\text{阈值}\Longrightarrow\lambda>1\ \text{而}\ \lambda>1\ \text{无独立来源（V316-FREEZE §7）}；$$
$$\qquad \text{可行域向：}\text{自然}\ \mathcal C_T\ \text{仅 C8，而 C8 已 FSC-DEAD（本档 §4）}。$$
$$\Longrightarrow\ \textbf{V316 变分座标系内的两条逃逸路径均已被排除}。$$

## 6. 重建准则（在 R1–R5 之上新增 R6）
$$\textbf{R6（本档核心新增）}：\text{给出一个自然算术恒等式，}\textbf{无条件}导出约束算子}\ \mathcal C_T\ \text{且}\ v_\lambda\notin\ker\mathcal C_T；$$
$$\qquad \text{该恒等式不得涉及 RH／Weil／POS／显式公式／零计数／有限阶局部相关（A1–A5）}；$$
$$\qquad \text{且不得是人为缩小}\ \mathcal A\ \text{（A7）}。$$
$$\text{R1–R5 同前（V316-FREEZE §9）。}$$

## 7. 边界（N1/N2 严守）
$$\text{① 本档为}\ \textbf{枚举型审计}，\text{不得升级为「}\mathcal C_T\ \text{不可能存在」；}\quad\text{② 「未找到」}\ne\text{「不存在」；}$$
$$\text{③ C8 的描述（cross-prime involution 锥 + balancing、FSC-DEAD）取自档案 V179/V180/V181 的既有结论，本轮未逐行重验；}$$
$$\text{④ 全档}\ \textbf{未用 RH}；零数值；\text{未跑 Lean。}$$

## 8. 净产出
$$\text{(i) 问题反转的形式化（两种拓扑的明确区分）；}\quad\text{(ii) A1–A7 准入条件挂牌；}$$
$$\text{(iii) C1–C8 逐一审计（唯一自然候选 C8 已 FSC-DEAD）；}\quad\text{(iv) R6 重建准则；}$$
$$\text{(v) 与 C⋆ 审计共同构成}\ \textbf{双向封口}（kernel 向 + 可行域向）。$$
