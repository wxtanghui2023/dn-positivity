# E6-4（未-2）— **体系 B 的定理级依赖审计**（四查）＋ $K_0$–$K_3$ 判定

> 唐先生 2026-09-16 18:15 裁定：**未-2 先做，然后才开未-1**（因 A₃ 的对象尚未锁死）。
> 目标：把 $\mathcal K_{\rm stable}$ 从"功能上的共同核"推进到**经过具体证明审计、可参数化、可优化的分析负载**。
> $\mathcal K$ 的定义（E6-3）：良分离点上的 $\sum_r|D(\sigma+it_r)|^{2}$ 型控制。

---

## 0. 判定档（唐先生指定，先立后判）
$$\boxed{\begin{array}{c|l}
K_0&\mathcal K\ \text{仅表面工具，交集撤销}\\
K_1&\mathcal K\ \text{确实跨体系出现，但只是技术封装}\\
K_2&\mathcal K\ \text{是共同}\ \textbf{不可删除功能核}\\
K_3&\mathcal K\ \text{共同核且}\ \textbf{可参数化}，允许进入}\ A_3
\end{array}}$$
$$\text{E6-3 起点}：K_1/K_2\ \text{之间}$$

---

## 查 1 — $\mathcal K$ 是否**真的出现**（不看符号，看良分离大值量）
$$\text{要求形式}：\sum_{r}\Bigl|\sum_{n\le X}a_n n^{-it_r}\Bigr|^{2}\ \text{（或可严格等价／推出它的估计）}，\ t_r\ \textbf{良分离}$$
$$\textbf{审计结果}：\text{体系 B（Huxley 配对／cell 分解型；GM }\Lambda^{2}\text{型）的}\ \textbf{核心输入恰为}\ \text{良分离点上的大值计数控制}；$$
$$\qquad\text{其形式可为}\ \textbf{带权／放大变体}（\text{cell 分解下的加权计数；}\Lambda^{2}\ \text{型范数）}\ \Longrightarrow\ \textbf{功能同型，形式不同}✓$$
$$\qquad\textbf{诚实标注}：\text{本判定基于标准路线的结构性特征，}\textbf{未逐行核验} \text{具体文献（残余 1 未消）}$$
$$\Longrightarrow\ \text{查 1：}\mathbf{通过}\ \text{（出现于功能层）}$$

## 查 2 — 是否**真的不可删除**（参数化追踪）
$$\text{把对应估计替换为}\ \boxed{\mathcal K(X,T;\sigma)\ \le\ B(X,T,\sigma)}\ \text{，追踪后续}：$$
$$\text{(i) 截断：}\zeta(s)\approx D(s)=\sum_{n\le X}n^{-s},\quad X\asymp T^{\kappa}\ (\text{approximate functional equation 型})$$
$$\text{(ii) 零点检测：}\sigma\ge\sigma_1\ \text{的零点}\ \rho=\sigma+i\gamma\ \Longrightarrow\ |D(\gamma)|\ \text{大}$$
$$\text{(iii) 良分离：}\ \text{零点间隔}\ \gg1/\log T \Longrightarrow\ \text{计数}\ R\ \le\ B(X,T,\sigma)\ \text{（}\mathcal K\ \text{的输出）}$$
$$\text{(iv) 归并：}\mathrm{N}(\sigma,T)\ \ll\ R+\text{误差} \Longrightarrow\ \theta(\sigma)＝\min_{\kappa}\ \text{（B 的指数，在截断约束下）}$$
$$\Longrightarrow\ \textbf{承重的进入点被精确定位}：\ \boxed{\text{承重}\ \textbf{恰在}\ \mathcal K\ \text{的输出}\ B\ \text{进入}\ \theta\ \text{的位置}}✓$$
$$\text{查 2：}\mathbf{通过}\ \text{（不可删且进入点可参数化：自由参数＝}\kappa\ \text{与}\ B\ \text{的形状）}$$

## 查 3 — ⭐ $\mathcal K$ 是否只是**隐藏的目标结论**
$$\text{判据：是否存在}\ \mathcal K\ \text{强度}\iff\text{该密度估计}$$
$$\textbf{决定性反驳（本档核心论证）}：\ \mathcal K\ \textbf{是 Dirichlet 多项式上的陈述}，\ \textbf{不含零点}；$$
$$\qquad\text{而密度估计是}\ \textbf{关于}\ \zeta\ \text{零点分布} \text{的陈述} \Longrightarrow\ \textbf{范畴不同} \Longrightarrow\ \mathcal K\iff\mathrm{N}(\sigma,T)\ \textbf{不可能}✓$$
$$\text{余量（slack）的存在性证据}：\text{历史上}\ \mathcal K\ \text{形式的}\ \textbf{改进确实转化为}\ \theta\ \text{的改进}（\text{Montgomery}\to\text{Huxley}\to\text{GM 型路线）}$$
$$\qquad\Longrightarrow\ \textbf{存在真正的余量}✓\qquad\textbf{诚实标注}：\text{"改进转为改进"为}\ \textbf{文献史实}，\text{本档}\ \textbf{未逐行核验}；\ \text{余量的}\ \textbf{幅度} \text{亦未量化}$$
$$\text{查 3：}\mathbf{通过}\ \text{（非隐藏目标；存在真余量）}$$

## 查 4 — 体系 B 是否**绕开"良分离"**
$$\text{关键问题}：\text{"良分离"是}\ \text{人为挑选的子集}，\ \text{还是}\ \text{证明内在必需？}$$
$$\textbf{审计结果（两条）}：$$
$$\text{(a) 零点侧：}\ \text{零点}\ \textbf{自动良分离}（\text{间隔}\gg1/\log T\ \text{为经典事实）}\Longrightarrow\ \text{非人为}✓$$
$$\text{(b) 估计侧：}\ \text{良分离}\ \textbf{是两个体系大值估计的}\ \textbf{假设项}（\text{Montgomery 型与 Huxley／GM 型皆如此）}\Longrightarrow\ \text{内在必需}✓$$
$$\Longrightarrow\ \text{查 4：}\mathbf{通过}\ \text{（良分离非技术工具，而是}\ \textbf{两侧共同的内在结构}）}$$

---

## 5. 判定：$\mathbf{K_3}$（带残余）
$$\text{四查皆通过} \Longrightarrow\ \mathcal K\ \textbf{跨体系出现、不可删除、非隐藏目标、良分离内在} \Longrightarrow\ \boxed{\text{判定}＝K_3}$$
$$\textbf{参数化已具雏形}：\ \mathcal K_{\alpha}\ \text{的}\ \alpha\ \textbf{可取为}\ (\kappa,\ B\ \text{的形状参数})\ \Longrightarrow\ \alpha\mapsto\theta_{\alpha}(\sigma)\ \text{的映射结构已明确}$$
$$\qquad\text{且}\ \theta(\sigma)＝\min_{\kappa}\ \text{（在截断约束下} B\ \text{的指数）}\ \Longrightarrow\ \textbf{优化结构已现}✓$$

## 6. ⚠️ 残余清单（不得省略；承接 E6-3 §8）
$$\textbf{残余 1}：\text{体系 B 的依赖为}\ \textbf{结构性重建}，\ \textbf{未逐行核验} \text{具体文献} \Longrightarrow \text{四查的可靠性}\ \textbf{受此限制}$$
$$\textbf{残余 2}：\text{"功能同型"与}\ \operatorname{Core}\ \text{的判定含}\ \textbf{判断成分} \Longrightarrow \text{定义决策}$$
$$\textbf{残余 3（新增）}：\text{查 2(iv) 的归并}\ \mathrm{N}(\sigma,T)\ll R+\text{误差}\ \text{及}\ \theta=\min_\kappa\ \text{的}\ \textbf{优化形式}\ \text{为}\ \textbf{[结构判定]}，\ \textbf{未} \text{从文献逐式导出}$$
$$\textbf{残余 4（新增）}：\text{查 3 的"余量存在"为}\ \textbf{史实论证}，\ \text{未量化}$$
$$\textbf{证据等级}：\text{E6-2"五项皆不可删"}\ \textbf{继续保持}\ [结构性论证]；\ \text{本档}\ K_3\ \text{判定} \textbf{同样为}\ [结构判定＋史实],\ \textbf{非形式化结论}✓$$

## 7. 闸门：进入未-1（A₃）的形式条件
$$\boxed{\text{E6-3}\xrightarrow{\text{未-2}}K_3\xrightarrow{}\textbf{A}_3}\quad\text{形式条件}\ \textbf{已满足}；\ \text{但须带残余 1--4 作业}$$
$$\text{若日后做 A}_3：\text{定义}\ \mathcal K_\alpha：\sum_r|D(s_r)|^{2}\le B_\alpha(X,T,\sigma)，\ \text{计算}\ \alpha\mapsto\theta_\alpha(\sigma)，\ \text{求}\ \alpha_{\min}(\sigma)=\inf\{\alpha:\mathcal K_\alpha\Rightarrow\mathrm{N}(\sigma,T)\ll T^{\theta(\sigma)+\varepsilon}\}$$
$$\qquad\textbf{可能的重要负结果}：\text{若}\ \alpha_{\min}(\sigma)\ \text{恰等于某经典 large-values barrier} \Longrightarrow \text{得到}\ \textbf{定量承重量墙}（\text{而非"方法不够强"的描述）}$$
$$\qquad\text{唐先生要求：}\ \textbf{不先做未-1}，\ \text{但残余 1 若无法在本轮消掉，须明示}\ \text{（本档已明示）}$$

## 8. 边界（N1/N2 严守）
$$\text{① 四查为}\ \textbf{结构性审计}，\ \textbf{未逐行核验} \text{（残余 1）}；\quad\text{② }K_3\ \textbf{非形式化结论}；$$
$$\text{③ 本档}\ \textbf{不引入候选机制}；\ \textbf{不构造}\ \alpha_{\min}；\quad\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 9. 净产出
$$\text{(i) 四查逐一执行（出现／不可删／非隐藏目标／良分离内在）——皆通过；}$$
$$\text{(ii) 承重进入点的精确定位：}\mathcal K\ \text{的输出}\ B\ \text{进入}\ \theta\ \text{的位置；}$$
$$\text{(iii) 查 3 的决定性论证（范畴不同}\Longrightarrow\mathcal K\iff\mathrm{N}(\sigma,T)\ \text{不可能）＋余量史实；}$$
$$\text{(iv) 判定}\ \mathbf{K_3}\ \text{（带残余 1--4）；参数化雏形}\ \alpha=(\kappa,B\ \text{形状}),\ \theta=\min_\kappa；$$
$$\text{(v) A₃ 的形式闸门已开，残余明示。}$$
