# V319 — **E.2-A：机制宇宙的非循环定义**（＋ E.2-B 分类不变量初稿 ＋ E.2-C 首轮判定）

> 唐先生 2026-09-16 16:57 裁定：选 **(乙) 类表完整性**，且**不先证「类表完整」**，先攻 **E.2-A**。
> 动机：V316／V317／V318-Ⅱ 三条出口（kernel×domain×exact identity）均关闭后，须先确认**搜索空间是否被错误坐标化**。

---

## 0. 为什么不是"再审一遍档案"
$$\text{V172/V177/V181/V241/V258/V267/V269/V280/V284/V294/V295 的再整理}\ \textbf{无新信息}。$$
$$\text{现状：大量}\ C_i\Rightarrow\text{DEAD}\quad\text{但}\ \textbf{没有}\ \Big[\text{所有可能的}\ M\Rightarrow M\in\mathscr C\Big]。\quad\textbf{后者才是类表完整性的真正数学问题}。$$

## 1. 防循环条件（唐先生 16:57，硬约束）
$$\textbf{类表完整性证明}\ \textbf{绝不能以"最终都会变成 RH 等价命题"为前提}（否则循环分类）。$$
$$\text{对象须定义为}\ \boxed{\text{RH-blind arithmetic mechanism}}\ \text{，最后才问是否产生 RH-relevant consequence}：$$
$$\text{mechanism}\overset{\text{classification}}{\longrightarrow}C_i\overset{\text{independent audit}}{\longrightarrow}\text{consequence}\quad✓$$
$$\textbf{禁止}：\text{RH-relevant consequence}\longrightarrow\text{倒推机制属于某类}\quad✗$$

---

## 2. E.2-A：机制的非循环定义（本档主结果）

### 2.1 定义（[定义决策]，本档提出）
$$\textbf{机制}\ M=(\mathcal O,\mathcal R,\Phi)\ \text{，其中：}$$
$$\text{(i)}\ \mathcal O：\textbf{有限呈现的算术对象}\ \text{——由整环}\ \mathbb Z、\text{素数、乘性函数、Dirichlet 特征、}p\text{-adic 结构、数域整环}\ \text{之一的}\ \textbf{有限描述}\ \text{给出}$$
$$\qquad\text{（"有限呈现"是防"把 RH 编进对象定义"的关键：}\text{对象描述长度}\ \textbf{不依赖 RH 真值）}$$
$$\text{(ii)}\ \mathcal R：\text{无条件关系，且}\ \text{(a)}\ \text{在尺度}\ X\asymp T\ \textbf{可证}；\text{(b)}\ \textbf{RH-blind}（不可用}\ L\text{-零点表达）；\text{(c)}\ \text{非平凡（不是定义展开）}$$
$$\text{(iii)}\ \Phi：\mathcal R\ \text{的后果到}\ \mathbb R\ \text{值量的映射，且}\ \textbf{有限可计算}\ \text{（同一算术数据）}$$
$$\Longrightarrow\ \textbf{机制宇宙}\ \mathfrak M=\{(O,R,\Phi)\}\ \text{（注意：}\mathfrak M\ \text{的定义}\ \textbf{不引用 RH／零点／任何 RH 等价判据}）$$

### 2.2 非循环性自检
$$\text{定义}\ \mathfrak M\ \text{只引用三项}：\text{(1) 有限算术呈现；(2) 尺度}\ X\asymp T\ \text{的无条件可证性；(3) }\Phi\ \text{的有限可计算性}$$
$$\text{三项均}\ \textbf{不含}\ \text{RH、零点、}\lambda_n\ge0\text{、Weil positivity} \Longrightarrow\ \textbf{非循环}\ ✓$$
$$\text{（对照：若把"机制"定义为"能判 RH 的东西"，则}\ \mathfrak M\ \text{与目标同义，后续分类必循环 ✗）}$$

### 2.3 ⭐ 结构性推论（关键：}\mathfrak M\ \text{已被档案中的工具分解）$$
$$\text{由 (iii)「有限可计算」＋档案既有结果，}\mathfrak M\ \text{的元素立刻受两条硬约束}：$$
$$\text{【约束 1】V277-A：}\text{有限值}\ +\ \text{可计算}\ \Longrightarrow\ \text{柱型（cylinder）}\ \text{（Type-Two Effectivity：可计算}\Rightarrow\text{连续）}$$
$$\text{【约束 2】V271-A：}\text{柱型}\ \text{证书即为有限数据证书；}\text{非柱}\ \Longrightarrow\ \text{不给有限证书}$$
$$\Longrightarrow\ \mathfrak M\ \text{按两条判定位分成四格：}$$
$$\begin{array}{c|c|c|c}
 & \text{柱型} & \text{载体}\ \zeta\text{-local} & \text{判定}\\ \hline
(1) & ✓ & ✓\ \text{（类层）} & \text{DEAD（V270-A 乘子构造）}\\
(2) & ✓ & ✓\ \text{（单对象）} & \text{须非柱内容（V270-B）}\\
(3) & ✓ & ✗ & \boxed{\text{唯一未定格}\ C_0\ \text{（V274-A／V275）}}\\
(4) & ✗ & — & \text{无有限证书（V271-A）；非可计算成分}\in\text{V211 §1 八类（已封）}
\end{array}$$
$$\textbf{即：}\mathfrak M\ \text{不是一张经验清单，而是}\ \textbf{由判定位}\ (\text{柱型？},\ \zeta\text{-local？})\ \text{张成的二维格}\ ✓$$

---

## 3. E.2-B：分类不变量初稿
$$\textbf{候选不变量}：\iota(M)：＝(\text{柱型？},\ \text{载体是否}\ \zeta\text{-local？},\ \text{是类层还是单对象？})\in\{0,1\}^{3}$$
$$\text{目标命题：}\ M\sim M'\iff\iota(M)=\iota(M')\quad(\text{同构类由不变量决定})$$
$$\textbf{与经验类表的关系}：\text{档案中的五／六类（explicit formula／positivity／counting／correlation／support／…）}$$
$$\qquad \text{是}\ \iota\ \text{的各分支的}\ \textbf{进一步细化}，\text{而非并列的独立类型} \Longrightarrow \text{经验分类}\ \textbf{不是机制层面的分类}（本档判定）$$
$$\text{证据（本档）}：\text{§2.3 的二维格已足以吸收}\ \text{V262（非满射空性）／V270-A／V271-A／V274-A／V277-A／V279（FQS）／V281（C0 分叉）}\ \text{的组织方式}$$

## 4. E.2-C：第六类是否存在（首轮判定）
$$\textbf{在}\ \mathfrak M\ \text{的定义（有限呈现＋有限可计算＋RH-blind）内}：$$
$$\text{格 (1)、(2)、(4) 已 DEAD；}\textbf{唯一活格 = (3) = }C_0\ \text{（已知唯一未定格，V274-A／V275）}$$
$$\Longrightarrow\ \boxed{\mathfrak M=\{\text{已封格}\}\cup\{C_0\}}\quad\text{即：}\textbf{类表在}\ \mathfrak M\ \text{内完备，}\textbf{模}\ C_0$$
$$\text{与 §E.4 的关系（V149 登记）：}\text{V275 已证「证书存在}\iff\text{该格被填充」} \Longrightarrow\ \text{E.2-C 与}\ C_0\ \text{的填／空问题}\ \textbf{同一}。$$

## 5. ⚠️ 两个残余格（诚实标注，**不得隐藏**）
$$\textbf{残余 1}：C_0\ \text{（非}\ \zeta\text{-local 有限柱载体）}\ \text{—— V274-A／V275 已登记为唯一未定格；}
$$\qquad \text{其空／非空}\ \textbf{未决}（V275 明示：不声称空，不声称非空）$$
$$\textbf{残余 2}：V211 §5\ \text{UNINSTANTIATED}\ \text{（非加性／非上同调／非指标／非}\ \Pi^1_1\text{／非选择的"有限→无限缺陷"）}$$
$$\qquad \text{—— 已登记为"无实例、无方向"；}\textbf{本档未消除}（非柱成分落 V211 §1 八类，但 §5 的第五类从未被实例化）$$
$$\Longrightarrow\ \textbf{完备性陈述的精确形式}：\mathfrak M=\{\text{已封格}\}\cup\{C_0\}\cup\{\text{V211 §5}\}\ \text{（后者空缺但未闭合）}$$

## 6. 判定与边界
$$\textbf{E.2-A 结论}：\textbf{成立}（本档给出非循环定义，并通过非循环性自检 §2.2）✓$$
$$\textbf{E.2-B 结论}：\textbf{初稿成立}（\iota：\text{3-bit 判定位；经验类表为其细化而非并列类型）}$$
$$\textbf{E.2-C 结论}：\textbf{条件完备}（在}\ \mathfrak M\ \text{内完备，模}\ C_0\ \text{与 V211 §5）}$$
$$\textbf{边界}：$$
$$\text{① }\mathfrak M\ \text{的定义是}\ \textbf{本档的定义决策}（[定义决策]）；\text{换定义须重验完备性；}$$
$$\text{② §2.3／§3／§4 的分解}\ \textbf{不是新定理}，\text{而是}\ \textbf{对档案既有结果（V262/V270/V271/V274/V277/V279/V281/V211）的重新组织}；}$$
$$\text{③ 完备性是}\ \textbf{条件性}（依赖}\ \mathfrak M\ \text{的定义与 §2.3 的落格判定）；$$
$$\text{④ 残余 1／残余 2}\ \textbf{未消除}；\quad\text{⑤ 全档}\ \textbf{未用 RH}；零数值；\text{未跑 Lean}。$$

## 7. 净产出
$$\text{(i) E.2-A：机制宇宙的非循环定义}\ (\mathcal O,\mathcal R,\Phi)\ \text{＋三项定义约束＋非循环性自检；}$$
$$\text{(ii) E.2-B：3-bit 分类不变量}\ \iota\ \text{初稿，并判定"经验类表＝}\iota\ \text{的细化而非并列类型"；}$$
$$\text{(iii) E.2-C：}\mathfrak M=\{\text{已封格}\}\cup\{C_0\}\cup\{\text{V211 §5}\}\ \text{—— 模两残余格的完备性；}$$
$$\text{(iv) 明确残余：}\ C_0\ \text{（已知唯一未定格）与 V211 §5（UNINSTANTIATED，无方向）。}$$
