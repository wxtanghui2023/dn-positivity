# （丙）· **研究生成器更换：Audit ≠ Discovery**（P0 协议）

> 依唐先生 2026-09-17 11:01 指令：**真正需要纠正的不是某个候选方向，而是研究生成器本身** ✓✓
> $$\boxed{\text{Audit}\ \ne\ \text{Discovery}}\qquad\text{今天把一个优秀的}\ \textbf{closure engine}\ \text{误当成了}\ \textbf{discovery engine}✓✓$$

## 0. 病灶（存证）
$$\text{今日固定模式}：\text{候选}\to\text{幂次计算}\to\text{conductor 判据}\to\mathrm{DEAD}✓$$
$$\Longrightarrow\ \text{审计机器}\ \textbf{只能关闭路线、不能生产路线} \Longrightarrow \text{待在框架内枚举}\ \textbf{必然} \text{返回 NO-GO}✓✓$$

## 1. 新生成器：构造算术对象 $\mathcal O$，满足 **G1--G4**

$$\begin{array}{ll}
\mathrm{G1}&\mathcal O\ \text{有明确的}\ \textbf{素数／整数算术定义} \text{，而非由}\ \zeta\ \text{或零点反定义};\\
\mathrm{G2}&\mathcal O\ \text{在每个有限层}\ X\ \text{上存在，}\ \text{但对}\ \textbf{有限数据具有盲性};\\
\mathrm{G3}&\displaystyle\lim_{X\to\infty}\mathcal O_X\ \textbf{保留一个有限层无法看到的全局量};\\
\mathrm{G4}&\text{该全局量能与}\ \beta-\tfrac12\ \text{建立}\ \textbf{可检验的数学接口}.\\
\end{array}✓$$

$$\textbf{关键变化在 G2}\to\textbf{G3}：\text{不是找"更强的有限估计"，而是}\ \textbf{主动制造}：$$
$$\boxed{\text{finite blindness}\ \longrightarrow\ \text{limit visibility}}✓✓$$

## 2. 目标形式（唐先生给定）
$$\mathcal O_X=\mathcal F\big(\{p\le X\},\ \{\text{有限模信息}\}\big)，\ \text{要求}\ \textbf{主动证明}：$$
$$\forall X<\infty,\ \mathcal O_X\ \text{无法区分某类不同的全局算术状态}\quad\text{而}\quad \lim_{X\to\infty}\mathcal O_X\ \text{能区分}✓$$
$$\text{新链}：\ \boxed{\text{有限算术对象}\to\text{一致兼容系统}\to\text{极限对象}\to\text{谱／零点信息}}✓$$
$$\qquad(\textbf{把"极限"本身变成机制，而不是误差项})✓✓$$

## 3. 两个生成器
$$\textbf{P1 极限显影器}：\text{寻找}\ \mathcal O_X\ \text{finite-blind}\to\mathcal O_\infty，\ \text{研究}\ \mathcal O_\infty\ \text{是否有谱分解}✓$$
$$\qquad\text{第一阶段}\ \textbf{不要求 RH}：\text{只要求发现一个}\ \textbf{真实存在的现象} \text{——"有限层看不到，但极限稳定地产生某种全局结构"}✓$$
$$\textbf{P2 物理机制搬运}：\text{从数学物理寻找}\ \text{局域自由度}\to\text{尺度演化}\to\text{固定点／极限}\to\text{谱约束}\ \text{的机制}，\ \text{强制落到素数算术}✓$$
$$\qquad\text{重点}\ \textbf{不是} \text{"p-adic"三字，而是}\ \textbf{非阿基米德体系的局部}\to\text{全局组织方式}\ \text{能否提供 G2／G3 所缺者}✓$$

## 4. 验收规则（**旧流程禁止**）
$$\textbf{第一轮禁止}：\text{候选 A／B／C}\to\text{幂次计算}\to\text{conductor}\to\mathrm{DEAD}✓✗$$
$$\text{只允许三种结果}：$$
$$\boxed{\text{①}\ \mathrm{ALIVE}：\text{构造出新对象，且数值／理论显示}\ \text{finite blind}+\text{limit visible}}✓$$
$$\boxed{\text{②}\ \mathrm{FALSE}：\text{构造出对象，但数值直接显示有限层}\ \textbf{不盲} \text{或极限}\ \textbf{不显影}——\textbf{这也是正成果}（\text{迅速排除整个机制}）}✓$$
$$\boxed{\text{③}\ \mathrm{UNRESOLVED}：\text{对象成立，但极限性质未知}——\textbf{只有此类才允许进入审计}}✓$$

## 5. 工作纪律（**收紧为一句**）
$$\boxed{\text{（丙）第一阶段不是"找证明"，而是"制造一个}\ \textbf{能失败} \text{的新对象"}}✓✓$$
$$\qquad\text{若连一个}\ \textbf{可被数值直接杀掉} \text{的新对象都没造出来，}\ \textbf{不准} \text{回到 BC 式估计优化}✓✓$$

## 6. ⭐⭐ 首批候选（P1），附**可测试命题**
$$\textbf{P1-}\alpha\ (\text{调和加权素数竞赛}）：\mathcal O_X^{q}:=\Big(\sum_{p\le X,\,p\equiv a(q)}\tfrac1p\Big)_{a\in(\mathbb Z/q)^*}✓\ \mathrm{G1}✓$$
$$\qquad\text{G2（盲）}：\text{有限层的}\ \textbf{符号序} \text{反复翻转（Littlewood）}✓\qquad\text{G3（显影）}：\text{对数密度极限存在且由}\ \textbf{低阶零点结构} \text{决定（Rubinstein--Sarnak）}✓$$
$$\qquad\text{G4}：\text{偏置的}\ \textbf{标度} \asymp X^{\beta-\frac12}\ \text{型} \Longrightarrow \textbf{可检验的指数接口}✓$$
$$\textbf{P1-}\gamma\ (\text{截断 Mellin 算子}，\text{承接资产 A-2}）：\mathcal O_X(s):=\int_1^X(\psi(u)-u)u^{-s-1}du\quad(\text{只用}\ p\le X)✓\ \mathrm{G1}✓$$
$$\qquad\text{G2（盲）}：\text{高度}\ \gamma\ \text{的零点需}\ X\gtrsim e^{\gamma} \Longrightarrow \textbf{有限层系统性看不见高处零点}✓$$
$$\qquad\text{G3／G4}：X\to\infty\ \text{极限}\to-\tfrac{\zeta'}{\zeta}\ \text{相关} \Longrightarrow \beta\ \text{直接可读}✓$$
$$\qquad ⚠️\ \text{诚实标注}：\text{该通道已知有}\ \textbf{A-leak 结构}（\text{V172}）；\ \text{本节问题}\ \textbf{不是} \text{"能否改进指数"，而是}\ \textbf{"有限层}\ \beta\text{-提取是否存在系统性偏移"}（\text{②判据}）✓$$
$$\textbf{P1-}\beta\ (\text{Guinand 相位锁定}，\text{资产 A-1}）：\ \textbf{不合格} \text{——它由}\ \gamma_k\ \text{定义} \Longrightarrow \mathrm{G1}\ \textbf{不满足}✓\quad(\text{诚实剔除})✓$$

## 7. 下一步（下一轮直接执行）
$$\text{(i)}\ \text{对 P1-}\alpha\ \text{跑数值：有限层翻转计数（盲）＋对数密度极限（显影）}✓$$
$$\text{(ii)}\ \text{对 P1-}\gamma\ \text{跑数值：有限层}\ \beta\text{-谱的稳定性／系统性偏移}✓$$
$$\text{(iii)}\ \text{按①／②／③归档，}\ \textbf{禁止} \text{滑回幂次审计}✓$$
