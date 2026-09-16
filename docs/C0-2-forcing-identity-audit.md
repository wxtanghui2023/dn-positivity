# C0-2 — **forcing 通道的同一性审计**（T1–T4 四层测试）

> 唐先生 2026-09-16 19:25 裁定：**这是 C0-2，不再搜索载体**。
> 判定对象：$$\boxed{\mathcal F_S:\ \text{有限、非}\ \zeta\text{-local certificate}\ \longrightarrow\ \text{关于}\ \zeta\ \text{零点分布的强制命题}}$$
> **防偷渡铁律（唐先生指定）**：$$\boxed{\text{"有限"}\ \text{只是载体性质，}\ \textbf{不能} \text{把"有限性本身"当成 forcing mechanism}}$$

---

## T1 — 输入对象是否相同
$$\text{C0 forcing 输入}：A_S\subset X_S,\ |X_S|<\infty,\ A_S\ \text{genuinely non-}\zeta\text{-local}$$
$$\text{E4 输入}：\mathscr A\xrightarrow{\ \Phi\ }\mathscr S_\infty\ (\text{arithmetic}\to\text{Archimedean spectral localization})；\ \text{E6 输入}：\mathcal K_{\rm disc}\ \text{或}\ \mathcal K_{\rm meas}$$
$$\textbf{判据}：\ A_S\to Z(\zeta)\ \text{是否}\ \textbf{必须} \text{先经}\ \Phi(A_S)\to\mathscr S_\infty\ \text{或}\ A_S\to\mathcal K？$$
$$\textbf{T1 结果}：\text{任何 forcing 的输出都是}\ \textbf{关于零点} \text{的命题} \Longrightarrow \text{必经"独立数据}\to\text{零点约束"这一}\ \textbf{同类映射} \Longrightarrow \textbf{同型}$$
$$\qquad\textbf{但（唐先生警告）}：\textbf{不能仅凭此判同一}✓$$

## T2 — forcing 的输出是否同型
$$\text{C0 所需输出}：A_S\ \text{满足}\Longrightarrow\forall\rho\in Z(\zeta),\ \mathrm{Re}\,\rho=\tfrac12$$
$$\text{E4 缺口}：\text{arithmetic asymmetry}\to\text{line localization}；\ \text{E6 缺口}：\text{analytic strength}\to\text{density/LV upgrade}$$
$$\textbf{须区分}：\ \boxed{\text{"有限数据最终需要控制零点"}\ \ne\ \text{"forcing 就是 E4 的 line-localization"}}✓$$
$$\textbf{分支}：\text{(i) 若 forcing 最终要求}\ \mathcal D_S(\rho)\ge0,\ \mathcal D_S(\rho)=0\iff\mathrm{Re}\,\rho=\tfrac12 \Longrightarrow \textbf{立即落入 E4／Weil／POS 旧类}；$$
$$\qquad\text{(ii) 若产生}\ \textbf{不同的零点约束}（\text{如"有限对象诱导的全局 rigidity 定理"） \Longrightarrow \textbf{不得提前判死}✓$$
$$\textbf{T2 结果}：\text{输出}\ \textbf{同型}（\text{同为 line-class 约束）}；\ \text{机制}\ \textbf{未定} \Longrightarrow \text{仍不足判同一}$$

## T3 — 不可替代步骤（**真正同一性所在**）
$$\text{把 forcing 拆成最小证明 DAG}：\ A_S\to B_1\to\cdots\to B_k\to\mathrm{RH}；\ \text{逐个问}$$
$$\qquad B_i\ \in\ \{\text{explicit formula},\ \text{FE},\ \text{density},\ \text{large-value},\ \text{spectral positivity},\ \text{known RH criterion}\}\ ?$$
$$\text{若}\ \textbf{全部} \text{可归入已有节点} \Longrightarrow \boxed{C_0\to\text{旧机制}}；\ \text{若存在}\ B_\star\ \text{满足七条件（非}\zeta\text{-local／非 FE／非显式公式／非 Weil-POS／非 density-LV／非 operator 重编码／却严格连}\ A_S\ \text{与全部零点）} \Longrightarrow \textbf{C0 才真新}$$
$$\textbf{T3 结果}：\text{可资利用的}\ B_i\ \textbf{恰为 C0-1 的通道清单}（\text{显式公式／局部因子／FE）；}$$
$$\qquad\Longrightarrow\ \text{任何由已知数学构造的 forcing}，\ \text{其}\ B_i\ \textbf{全属旧类（或禁）} \Longrightarrow \text{该情形下}\ \textbf{C}；$$
$$\qquad\text{而}\ B_\star\ \textbf{无实例}（\text{"未发现"}\ne\text{"不存在"}） \Longrightarrow \text{A 类要件}\ \textbf{未满足}✓$$

## T4 — 有限性到底在哪里发挥作用（**本档最强一刀**）
$$\text{若 forcing＝"}\ A_S\ \text{finite}\Rightarrow\text{某有限判定}\Rightarrow\mathrm{RH}\ \text{"}，\ \text{须找到}\ \textbf{有限性不可替代的数学作用}：\text{真正的}\ \boxed{\text{finite}\Rightarrow\text{global rigidity}}$$
$$\qquad\textbf{而不能是}：\text{finite}\Rightarrow\text{把已有无限对象截断}\Rightarrow\text{再做已知 RH criterion}\（\text{那直接回到 V320／V321 的 finite}\to\text{infinite wall）}$$
$$\textbf{关键结构事实}：\ \text{forcing 须给出}\ A_S\ \text{有限}\Longrightarrow\ \forall\rho\ (\text{全高度、无界})：\text{此为}\ \textbf{关于无限对象的一致（uniform）陈述}$$
$$\qquad\text{而已知的"有限数据}\to\text{零点"通道只有显式公式，且它给的是}\ \textbf{高度有界} \text{的控制}（\text{素数侧到}\ X\ \text{只控制}\ |\gamma|\lesssim X\ \text{的零点，误差随}\ X\ \text{衰减）}$$
$$\qquad\Longrightarrow\ \text{要}\ \textbf{无界高度的一致控制}，须}\ \text{(a) 用被禁的显式公式，或 (b) 用局部因子（}\zeta\text{-local，非}\ C_0\text{），或 (c) 新机制}$$\Longrightarrow$$
$$\boxed{\text{"finite}\Rightarrow\text{uniform global rigidity"}\ \textbf{无已知实现}} \Longrightarrow \text{且经已知机制者或为}\ \zeta\text{-local、或属禁、或仅高度有界}✓$$

---

## 判定：$\mathbf{D}$（并登记 C 型理由）
$$\boxed{\mathbf{D}}\：\ \text{有限 certificate 对}\ \textbf{全部高度}\ T\to\infty\ \text{的零点}\ \textbf{无统一控制} \Longrightarrow \text{V320／V321 型}\ \textbf{finite}\to\text{infinite wall 重现}}$$
$$\qquad\textbf{并列理由（C）}：\text{一切由已知数学构造的 forcing，其不可替代节点}\ B_i\ \textbf{全属旧类或禁区}✓$$
$$\textbf{逐档对照}：$$
$$\qquad\text{C0-2-A（真正不同）}：\ \textbf{未满足}（B_\star\ \text{无实例，}\text{A 类要件缺新定理）$$
$$\qquad\text{C0-2-B（同目标不同实现）}：\ \textbf{未满足}（\text{无新的不可替代桥}）$$
$$\qquad\text{C0-2-C（只是 E4／E6 另一种入口）}：\ \textbf{成立}（\text{已知节点全属旧类}）$$
$$\qquad\text{C0-2-D（finite}\to\text{infinite wall 重现）}：\ \textbf{成立}（\text{uniform global rigidity 无已知实现）}$$
$$\Longrightarrow\ \textbf{取 D 为主判定，C 为并列理由}；\ \textbf{仅 A／B 值得继续，本档二者皆不可得}✓$$

## 出口枚举的闭环（唐先生预定形式）
$$\boxed{C_0\ \to\ \text{forcing}\ \to\ \begin{cases}\text{新 global-rigidity bridge}&\mathbf{A/B}\ (\textbf{未得})\\ \text{E4／E6／旧墙}&\mathbf{C}\ (\textbf{成立})\\ \text{finite}\to\text{infinite wall}&\mathbf{D}\ (\textbf{主判定})\end{cases}}$$
$$\Longrightarrow\ \text{今日形成的"唯一残余入口"}\ \textbf{在审计范围内关闭}✓$$

## 边界（N1/N2 严守）
$$\text{① 本档}\ \textbf{不造}\ X_S、\textbf{不优化} \text{certificate、}\textbf{不做 GM、不回头 E6；}\quad\text{② T1／T2／T3／T4 的判定为}\ \textbf{[结构判定]}；$$
$$\text{③ "未发现}\ B_\star\text{"}\ \ne\ \text{"不存在"（N1/N2）；}\ \textbf{不宣告}\ \text{C}_0\ \text{被证明不可能}；$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 净产出
$$\text{(i) T1＝同型（必经"独立数据}\to\text{零点约束"映射；但单独不足判同一）；}$$
$$\text{(ii) T2＝输出同型（line-class 约束），机制未定；分支 (i)/(ii) 已登记；}$$
$$\text{(iii) T3＝已知数学构造的}\ B_i\ \textbf{全属旧类或禁区}；\ B_\star\ \textbf{无实例}；$$
$$\text{(iv) ⭐ T4＝}\textbf{"finite}\Rightarrow\text{uniform global rigidity"无已知实现}（\text{显式公式仅给高度有界控制）}；$$
$$\text{(v) 判定}\ \mathbf{D}（\text{主）＋}\mathbf{C}（\text{并列）}；\ \text{出口枚举在审计范围内闭环；A／B 未得。}$$
