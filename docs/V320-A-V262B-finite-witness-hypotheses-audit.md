# V320-A — **V262-B finite-witness 条件核验**（地基审计）＋ **V320 勘误**

> 唐先生 2026-09-16 17:00 提出的逻辑质疑：**"紧致＋闭"不足以单独推出"每级非空 ⟹ 逆极限非空"／"极限空 ⟹ 某一级空"**。
> 本档严格核验 V262-B 所依赖的假设，范围**严格限定在这一条定理**。

---

## 1. 标准事实（本档 §1，[标准事实]，须与 V262-B 逐条对齐）
$$\text{(T1) 逆系统}\ (X_N,\pi_N)\ \text{，若每}\ X_N\ \textbf{非空紧致 Hausdorff}、\pi_N\ \textbf{连续}，\text{则}\ \lim_{\leftarrow}X_N\ne\varnothing$$
$$\qquad\text{证法：}\prod X_N\ \text{紧（Tychonoff）；兼容条件}\ f_{ij}(x_j)=x_i\ \text{定义}\ \textbf{闭集}；\ \text{FIP 由"取最大层}\ N\ \text{并令}\ x_i：＝f_{iN}(x_N)"\ \text{给出}\ \Longrightarrow\ \text{交非空}\ ✓$$
$$\text{(T2) 由 (T1) 取逆否：}\lim_{\leftarrow}=\varnothing\Longrightarrow\exists N:X_N=\varnothing\quad(\textbf{有限见证})\ ✓$$

### 1.1 ⭐ 关键区分（本档核心，也是 V320 的错源）
$$\textbf{(T1)/(T2) 只涉及}\ \textbf{存在性}：\text{（"某个"全局点存在）}。\ \textbf{不需要}\ \text{满射性，\textbf{不需要} ML 条件}\ ✓$$
$$\textbf{但"给定有限证书}\ C_T\ \text{可延拓为全局证书"是}\ \textbf{提升性}\ (\texttt{lifting})，\text{不是存在性}：$$
$$\qquad \text{要求}\ \pi_T:\lim_{\leftarrow}X_N\twoheadrightarrow X_T\ \textbf{满射}，\text{即}\ \forall x\in X_T,\ \exists\ \text{thread extending}\ x$$
$$\qquad\text{该满射性}\ \textbf{需要额外条件}：\text{bonding 满射，或}\ \textbf{Mittag–Leffler}（像链稳定}\Longrightarrow\lim^{1}=0\Longrightarrow\text{投影满射）}$$
$$\Longrightarrow\ \boxed{\text{紧致＋闭}\ \not\Rightarrow\ \text{提升性}}\quad\text{—— 唐先生质疑成立}\ ✓$$

## 2. V262-B 的原始表述核验
$$\text{V262-B（档案）：}\text{非空紧致 Hausdorff ＋ 任意连续}\pi_n\Longrightarrow\lim_{\leftarrow}\ne\varnothing；\ \text{且}\ \lim_{\leftarrow}=\varnothing\iff\exists N:X_N=\varnothing$$
$$\Longrightarrow\ \text{其}\ \textbf{存在性}\ \text{部分}\ =\ \text{(T1)/(T2)}\ \textbf{正确}\ ✓\ (\text{无需满射／ML})$$
$$\text{V262-A 自身的附注（档案已记录）}：\text{逃逸口 C（非满射）的活化}\ \textbf{要求像链}\ X_{n+1}\to X_n\ \textbf{不稳定}（无降链条件）$$
$$\qquad \Longrightarrow\ \text{此时}\ \textbf{已不是有限阶段系统}（\text{与 V262-A 原文一致）}\ ✓$$
$$\Longrightarrow\ \textbf{档案本身已含线索：}\text{非满射逃逸 = 像链不稳定 = 提升性失效之处}$$

## 3. V320 的错处（勘误，T10）
$$\textbf{V320 §4.1 写的：}"\text{每层有限证书非空}\Longrightarrow\text{全局对象存在}"\ ——\ \textbf{作为存在性陈述正确}（T1）✓$$
$$\textbf{但 V320 的}\ \textbf{B 分支判定}\（"\Longrightarrow\ §5\ \text{无独立地位}"）\ \text{隐性使用了}\ \textbf{提升性}：$$
$$\qquad \text{机制问题是"}\textbf{给定的}\ C_T\ \text{是否延拓}"，\text{而非"是否存在某个全局点}" \Longrightarrow\ \textbf{需要 ML／满射}\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{V320 的 B 分支结论需附加条件，}\textbf{故 V320 的"§5 DEAD"判定尚未成立}}\ ✗$$
$$\qquad\textbf{因此}\ \mathfrak M\ \text{不能写为}\ \mathfrak M_{\text{closed}}\sqcup C_0；\ \textbf{残余不是收缩为单一}\ C_0\ ✗$$

## 4. 由此浮现的**新残余**（§5-L）
$$\boxed{\text{有限阶段全部非空}\ +\ \text{逐层局部一致}\ +\ \textbf{特定证书不延拓}（lifting failure）}$$
$$\text{所需结构}：\text{bonding}\ \pi_N\ \textbf{非满射}\ 且\ \text{像链}\ \text{Im}(\pi_N)\ \textbf{不稳定}（无 ML）$$
$$\text{其障碍度量}：\lim^{1}\ne0\ \text{（或更高阶）}\ \Longrightarrow\ \text{若} \textbf{能显式给出} \text{群／纤维化／链复形结构}\ \to\ \textbf{G3（V193–V198，旧类）}；$$
$$\qquad \textbf{若给不出显式结构}\ \Longrightarrow\ \text{按 V269 勘误：}\textbf{不得自动贴 G3 标签}，\text{应记作}\ \textbf{未分类}（\text{new residual}\ \S5\text{-L）}$$
$$\Longrightarrow\ \text{这正是唐先生预警的}\ \boxed{\iota(M_T)\ \text{稳定}\not\Rightarrow\iota(M_\infty)\ \text{稳定}}\ \text{可能真实发生的位置}\ ✓$$

## 5. 修正后的状态
$$\boxed{\mathfrak M=\mathfrak M_{\text{closed}}\ \sqcup\ C_0\ \sqcup\ \S5\text{-L}}\qquad(\S5\text{-L}：\text{lifting failure，未分类})$$
$$\text{三情形判定表（修正版）}：$$
$$\text{(A) 有限截断失效}\to\mathrm{DEAD}\ ✓\ \text{（不变）}$$
$$\text{(B-存在) 紧致＋连续}\to\lim_{\leftarrow}\ne\varnothing\ ✓\ \text{（T1，成立）}$$
$$\text{(B-提升) 需 ML／满射}\to\ \text{不满足时}\ \textbf{提升失败}\to\ \S5\text{-L（未分类）}\ \text{或}\ G3（\text{若能显式给结构）}$$
$$\text{(B′/B″) 非紧致}\to\text{A-leak；非投射}\to\ \text{上同调（需显式结构）}$$
$$\text{(C) 开而不闭}\to\text{V259-A 或 V271-A}\ ✓\ \text{（不变）}$$

## 6. 判定与边界
$$\textbf{V320-A 判定}：\textbf{情形 II（V262-B 缺少必要条件）成立} \Longrightarrow\ \textbf{V320 的核心 DEAD 判定未成立}\ ⟹\ \textbf{不得转向}\ C_0$$
$$\qquad\text{（即：}\text{"如果 V262-B 不足}\Rightarrow V320\ \text{核心 DEAD 尚未成立}\Rightarrow C_0\ \text{还不能称为唯一残余"}\ ——\ \text{与唐先生预设一致）}$$
$$\text{边界：① (T1)/(T2) 为}\ \textbf{[标准事实]}（Tychonoff＋FIP；本档未引 Lean）；\ \text{② ML 与提升性的对应关系为}\ \textbf{[标准事实]}；$$
$$\qquad\text{③ §3 的勘误区分为本档}\ \textbf{[结构判定]}；\ \text{④ 全档}\ \textbf{未用 RH}；零数值；\text{未跑 Lean}。$$

## 7. 净产出
$$\text{(i) 严格区分}\ \textbf{存在性}（T1/T2，无需 ML）\ \text{与}\ \textbf{提升性}（需 ML／满射）；$$
$$\text{(ii) 确认 V262-B 的}\ \textbf{存在性部分正确}，\text{但 V320 的 B 分支误用了}\ \textbf{提升性}；$$
$$\text{(iii) V320 勘误：}\S5\ \text{DEAD 判定未成立；}\ \mathfrak M\ \text{残余恢复为}\ \{\S5\text{-L},\ C_0\}\ \text{（非单一}\ C_0)；$$
$$\text{(iv) 命名新残余}\ \S5\text{-L}（\text{lifting failure，未分类}）\ \text{并给出其判据（bonding 非满射＋像链不稳定＋}\lim^{1}\ne0）。}$$
