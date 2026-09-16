# E4-3-R2 — **T2／T3／T4 内部完备性审计**（R2-1／R2-2／R2-3）

> 唐先生 2026-09-16 18:02 裁定：继续（丑-1），**逐类做完备性/坍缩审计**；**不进入候选搜索**。
> 严格对象形式：$X=(\mathcal X,\mathcal A,\Phi_X,V_X)$，C1 要求 $V_X(Z,\mathcal X)\ne V_X(Z)$。

---

## 0. 状态表（唐先生指定，本档为起点）
$$\begin{aligned}T2_{\rm pure\ order}&=\mathrm{DEAD},&T2_{\rm arithmetic\ label}&=\mathrm{OPEN},\\ T3_{\rm complexity}&=\mathrm{DEAD},&T3_{\rm arithmetic\ definability}&=\mathrm{OPEN},\\ T4_{\rm spectral\ dynamics}&=\mathrm{DEAD},&T4_{\rm arithmetic\ invariant}&=\mathrm{OPEN}.\end{aligned}$$
$$\text{审计优先级}：\boxed{T4>T3>T2}\ (\text{逻辑剩余空间优先级，非优劣排名})$$

---

## R2-1：T2（序型／指标附着）

### R2-1a 纯序型 —— **严格 DEAD**
$$\text{设}\ n(\rho)：＝\#\{\rho'\in Z:\operatorname{Im}\rho'<\operatorname{Im}\rho\}，\ t_n,\ \Delta_n：＝t_{n+1}-t_n,\ N(T)：＝\#\{\rho:\operatorname{Im}\rho\le T\},\ N^{-1}(n)$$
$$\text{全部由}\ Z\ \textbf{恢复} \Longrightarrow n=n(Z,\rho)\ \text{等} \Longrightarrow \boxed{\text{纯"序型/高度指标"}\subseteq\text{零点集函数}} \Longrightarrow \textbf{C1 失败}\ \to\ \mathrm{DEAD}\ ✓$$
$$\qquad\text{(且：}\ Z\ \text{在}\ G\ \text{下作为集合不变}\Longrightarrow\text{任意}\ Z\text{-函数}\ G\text{-不变 —— 与 E4-3-A 一致)}$$

### R2-1b 外部算术标签 —— **OPEN，但桥很重且高度可疑**
$$\text{若要逃脱 C1，须有}\ \boxed{a\mapsto\rho\ \text{配对}，\text{且}\ a\ \text{不能由}\ Z\ \text{恢复}}$$
$$\text{逐一检查自然配对来源}：\text{(i) conductor／modulus／character index}\ \text{是}\ \textbf{对象的不变量}，\text{非附着于单个零点}\ \to\ \text{需}\ \text{Chebotarev／自守参数化}\ \to\ \textbf{T5}；$$
$$\qquad\text{(ii) Frobenius index}\ \text{仅函数域}\ \to\ \text{V144 层诊断：archimedean 层无 Frobenius}\ ✗；\quad\text{(iii)}\ p\text{-adic／Iwasawa}\ \to\ \textbf{T6}；$$
$$\qquad\text{(iv) 一般}\ L\text{-函数族上的}\ a\mapsto\rho(a)\ \text{配对}\ \Longrightarrow\ \text{需要}\ \textbf{典范零点选择律}\ \to\ \text{档案已审：V147 T1／T2（无严格单边选择律）、V210}$$
$$\Longrightarrow\ \boxed{T2_{\rm arith\ label}\ \text{的"桥"＝典范零点选择}\ \text{本身已是最硬的墙之一}} \Longrightarrow \textbf{OPEN 但优先级最低}✓$$

## R2-2：T3（可定义性附着）

### R2-2a 区分（唐先生指定，不得偷杀）
$$\boxed{\text{"可定义"}\ \ne\ \text{"复杂度"}}\quad\text{复杂度衡量}\ \text{定义／证明／计算的}\ \textbf{资源}；\ \text{T3 可用的是}\ \textbf{定义本身携带的算术结构}$$
$$\text{若}\ V_X=\operatorname{complexity}(\mathcal C_\rho)\ \text{或}\ \min\{\text{程序长度}\}\ \text{或}\ \min\{\text{证书尺寸}\} \Longrightarrow \textbf{T3}_{\rm complexity}\ \mathrm{DEAD}\ (\text{V259/V269/V271})✓$$

### R2-2b 满足 C1／C2／C7 的"定义结构"形态
$$\text{(甲) 可定义闭包}\ \mathrm{dcl}(Z)\ \text{在自然扩张（算术谓词）中}：\text{扩张的谓词是算术的（独立于}\ Z）\Longrightarrow\ \mathrm{dcl}(Z)\ \text{可携带}\ Z\ \text{之外信息}\ \Longrightarrow \textbf{C1 OK}✓$$
$$\qquad\text{(C2)}\ ✓\（\text{由算术谓词给出）；(C7)}\ ✓\（\text{不依赖表示）}；\quad\text{(C6)}\ \text{邻近"complexity"但}\ \textbf{不等同} \Longrightarrow\ \textbf{未分类}$$
$$\text{(乙) 由算术条件确定的"最小／典范对象"}\ \mathcal C(\rho)：\text{同上，}\textbf{未分类}$$
$$\Longrightarrow \boxed{T3_{\rm arith\ definability}\ \text{在 C1--C7 层}\ \textbf{确实 OPEN}}$$

### R2-2c ⭐ 但 T3 的末端约束（本档关键发现）
$$\text{凡最终要产生}\ \textbf{线定位}，\text{都必须在末端满足}\ \mathrm{C8}：\ \exists\mathcal D\ge0,\ \mathcal D=0\iff\mathrm{Re}\,\rho=\tfrac12\ (\text{来源须为算术可容许性})$$
$$\qquad\text{而 C8 的真实形式＝}\textbf{区域型}\to\text{线型的}\ \textbf{强度升级}（\text{E4-3 §2.3}）\ \Longrightarrow\ \textbf{继承角 II 的全部难度}$$
$$\Longrightarrow\ \boxed{\text{T3 的"定义结构"必须}\ \textbf{自己供应强度升级}，\text{否则}\ \text{停在}\ \mathrm{C8}}$$
$$\qquad\textbf{[结构判定]}：\text{定义结构}\ \text{本身不携带定量强度} \Longrightarrow \text{T3 OPEN 的"可用性"取决于它能否附带一个}\ \textbf{定量控制}✓$$

## R2-3：T4（动力学附着）—— **结构二分（本档主结果）**

### R2-3.1 二分的精确陈述
$$\textbf{设}\ (\mathcal A,\Theta_t)\ \text{为算术动力学，}\ I\ \text{为其不变量，}\ \Theta_t\ \text{不是由}\ Z\ \text{决定（C1 OK）}。\ \text{则}\ \textbf{二分}：$$
$$\boxed{\text{任何 T4}\ \Longrightarrow\ \begin{cases}\textbf{(A) 谱重编码}：\exists\ \text{Hilbert 空间}\ \mathcal H,\ \text{自伴}\ L,\ U_t=e^{itL}\ \text{使}\ \Theta_t\ \text{可实现，且}\ V_X(\rho)=\langle u_\rho,Ku_\rho\rangle\ (\text{K 为}\ L\ \text{的函数})\\ \textbf{(B) 独立算术不变量}：\text{不存在上述可实现性，}\ I\ \textbf{仅由算术数据} \text{承载}\end{cases}}$$

### R2-3.2 分支 (A)：**DEAD**
$$\text{若动力学最终只作用于谱表示} \Longrightarrow \text{arithmetic dynamics}\to\text{operator dynamics}\to\text{spectral localization}$$
$$\qquad\Longrightarrow\ \text{撞}\ \boxed{\text{spectral re-encoding}（\text{V322 §6 明文排除项}）}\ \text{与}\ \textbf{V162 有限传播／带宽墙}$$

### R2-3.3 分支 (B)：**OPEN，但义务为两段**
$$\text{(B1)}\ \textbf{独立构造}：I\ \text{须是}\ \textbf{算术动力学的本征不变量}（\text{先独立存在}）；$$
$$\qquad\text{档案相关结果：}\textbf{V284（五族操作全败）}\Longrightarrow I\ \textbf{必须来自五族之外}；$$
$$\text{(B2)}\ \textbf{控制}：\text{须证}\ \boxed{I(\rho)\ \ge\ c\,(\mathrm{Re}\,\rho-\tfrac12)^{2}}\ \text{或更强}\ I(\rho)=0\iff\mathrm{Re}\,\rho=\tfrac12$$
$$\qquad\textbf{唐先生纪律}：\text{不得直接说"这就是 C8，所以循环"} —— \text{真正的审计对象是}\ \textbf{两段义务的独立性}：$$
$$\qquad\qquad\underbrace{\text{算术动力学守恒量}}_{\text{先独立构造}}\Longrightarrow\underbrace{\text{零点偏离量的控制}}_{\text{后证明}}$$

### R2-3.4 ⭐ 二分的诚实限度（本档标注）
$$\text{二分的"可实现性"判据须}\ \textbf{先固定}\ \text{"谱重编码"的定义（}\mathcal H,L,K\ \text{的存在性}）\Longrightarrow \text{该二分}\ \textbf{部分依赖定义选择}；$$
$$\qquad\text{本档将其登记为}\ \textbf{[结构二分（定义依赖）]}，\ \textbf{非定理}✓$$

---

## 4. ⭐ 角 I 的末端汇合（本档最重要的结构性发现）
$$\text{三个 OPEN 槽（T2-标签／T3-定义／T4-不变量）}\ \textbf{全部} \text{必须在末端过}\ \mathrm{C8}$$
$$\qquad\text{而 C8 的真实形式＝}\textbf{区域型}\to\text{线型的强度升级}＝\textbf{角 II}\ (\text{V316}\ C^\star／\text{V162})$$
$$\Longrightarrow\ \boxed{\text{角 I 与角 II 在末端}\ \textbf{汇合}} \Longrightarrow \text{三个 OPEN 槽}\ \textbf{不独立于} \text{角 II 的墙}$$
$$\qquad\textbf{[结构判定]}；\ \text{与 STRATEGY-2026-09-16 的"三副面孔一堵墙"（V181＋V283＋V172＋POS）}\ \textbf{一致}✓$$
$$\text{但}\ \textbf{不得} \text{由此宣布"角 I DEAD"} —— \text{B1（独立算术不变量）的}\ \textbf{存在性} \text{仍未审计}✓$$

## 5. 更新后的状态（唐先生原表）
$$\boxed{\begin{aligned}T2_{\rm pure\ order}&=\mathrm{DEAD}\ (\text{R2-1a 严格}),&T2_{\rm arithmetic\ label}&=\mathrm{OPEN}\ (\text{桥＝典范选择，优先级最低}),\\ T3_{\rm complexity}&=\mathrm{DEAD},&T3_{\rm arithmetic\ definability}&=\mathrm{OPEN}\ (\text{末端须自供强度}),\\ T4_{\rm spectral\ dynamics}&=\mathrm{DEAD},&T4_{\rm arithmetic\ invariant}&=\mathrm{OPEN}\ (\text{义务 B1＋B2})\end{aligned}}$$

## 6. 判定与下一步
$$\textbf{E4-3-R 的"结局 B"成立}；\ \textbf{但}\ \textbf{不能} \text{把整个角 I 称为"真正的开放突破槽"}；$$
$$\text{下一步须完成}\ \textbf{R2-3 的二分}\（\text{已给，登记为 definition-dependent）\ \text{并进一步审}\ \textbf{B1：独立算术不变量来自五族之外的可能性}；$$
$$\text{若二分最终把}\ T4\text{-B}\ \text{也压回}\ V162／V280／\text{旧类} \Longrightarrow \text{角 I}\ \textbf{才真正收口}；\ \textbf{若压不回} \Longrightarrow T4\text{-B}\ \text{是本弧线中最干净的}\ \textbf{新机制入口}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① R2-1a 严格；R2-1b／R2-2／R2-3 的落类与二分为}\ \textbf{[结构判定]}，\ \text{非定理；}$$
$$\text{② §4 的"末端汇合"为}\ \textbf{[结构判定]}；\quad\text{③ 二分}\ \textbf{依赖"谱重编码"的定义选择}（\text{§R2-3.4}）；$$
$$\text{④ 本档}\ \textbf{不引入候选机制}；\ \text{不构造任何}\ \Theta_t；\quad\text{⑤ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 8. 净产出
$$\text{(i) R2-1a 严格证明纯序型／高度指标}\subseteq\text{零点集函数}\ \to\ \mathrm{DEAD}；$$
$$\text{(ii) T2-标签的"桥"＝}\textbf{典范零点选择}（\text{已审：V147/V210}）\ \to\ \text{OPEN 但优先级最低；}$$
$$\text{(iii) T3：区分可定义结构}\ne\text{复杂度}；列形态（甲）（乙）；}\textbf{末端须自供强度}；$$
$$\text{(iv) T4 结构二分（谱重编码＝DEAD／独立算术不变量＝OPEN，义务 B1＋B2）；}$$
$$\text{(v) ⭐ 角 I 三 OPEN 槽}\textbf{末端全部汇合到 C8＝角 II}（\text{与"三副面孔一堵墙"一致）。}$$
