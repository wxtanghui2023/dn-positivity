# V321 / §5-L — **非满射像链不稳定的真实性审计**（纯结构分解）

> 唐先生 2026-09-16 17:02 裁定。第一阶段**只做纯结构分解**：不碰 RH／零点／显式公式／$C_0$。
> 第一问：$$\text{有限阶段全非空}\ +\ \text{像链不稳定}\ +\ \pi_N\ \text{非满射}\ \Longrightarrow\ \text{是否产生真正的新结构？}$$

---

## 1. 第一刀：三个对象彻底分开（唐先生指定）
$$\text{固定}\ N，\ M\ge N：\quad I_{M,N}：＝\operatorname{im}(X_M\to X_N),\qquad I_{\infty,N}：＝\bigcap_{M\ge N}I_{M,N}\ (\text{稳定像})$$
$$\text{自然包含}：\boxed{\pi_N(\varprojlim X_i)\subseteq I_{\infty,N}\subseteq X_N}$$
$$\text{须审计的不是}\ I_{M+1,N}\subsetneq I_{M,N}，\text{而是最后一式是否可能}\ \textbf{严格}：\boxed{\pi_N(\varprojlim X_i)\subsetneq I_{\infty,N}\ ?}$$
$$\text{三层语义}：$$
$$\qquad\text{(i) 仅}\ I_{M,N}\ \text{不稳定}\ \Longrightarrow\ \text{只是}\ \textbf{有限阶段信息持续被淘汰}；$$
$$\qquad\text{(ii)}\ I_{\infty,N}\ne\varnothing\ \text{但投影不到逆极限}\ \Longrightarrow\ \textbf{genuine global compatibility obstruction}；$$
$$\qquad\text{(iii) 且不能被已有 G3 结构化的障碍}\ \Longrightarrow\ \text{才有资格}\ \mathrm{VI}$$

## 2. 第二刀：最小反例模型（**答案是否定的 —— 本档核心定理**）

### 2.1 定理（V321-A，本档证明，标准论证）
$$\textbf{设}\ X_N\ \text{皆非空}\ \textbf{紧致 Hausdorff}，\text{bonding}\ \pi_{M,N}\ \textbf{连续}。\ \text{则}\ \forall N：$$
$$\boxed{\pi_N(\varprojlim X_i)\ =\ I_{\infty,N}\ =\ \bigcap_{M\ge N}\operatorname{im}(X_M\to X_N)}$$
$$\textbf{证明}：\text{包含}\ \subseteq\ \text{显然}。\text{反之取}\ y\in I_{\infty,N}。\text{令}\ A_M：＝\{x\in X_M:\pi_{M,N}(x)=y\}\ (M\ge N)。$$
$$\qquad\text{(a)}\ A_M\ \textbf{非空闭}（y\in I_{M,N}\ \text{与}\ \pi_{M,N}\ \text{连续}）；\quad\text{(b) bonding 限制为}\ A_{M+1}\to A_M：$$
$$\qquad\qquad \text{若}\ x\in A_{M+1}\ \text{则}\ \pi_{M,N}(\pi_{M+1,M}x)=\pi_{M+1,N}x=y\ \Longrightarrow\ \pi_{M+1,M}x\in A_M\ ✓$$
$$\qquad\text{(c) 子系统}\ (A_M)\ \text{亦为非空紧致 Hausdorff ＋ 连续 mapping}\ \Longrightarrow\ \varprojlim A_M\ne\varnothing\ (\text{Tychonoff＋FIP})；$$
$$\qquad\text{(d) 取下标}\ i\le N\ \text{处}\ a_i：＝\pi_{N,i}(y)\ \text{补全得完整 thread}\ \Longrightarrow\ y\in\pi_N(\varprojlim X_i)\ ✓\qquad\square$$

### 2.2 推论（对 §5-L 的直接影响）
$$\Longrightarrow\ \textbf{在"紧致 Hausdorff ＋ 连续"内，严格包含}\ \pi_N(\varprojlim)\subsetneq I_{\infty,N}\ \textbf{不可能发生}\ ✓$$
$$\textbf{即：}"\text{像链不稳定}"\ \textbf{本身不足以} \text{产生新障碍 —— 稳定像}\ I_{\infty,N}\ \textbf{仍然被达到}。$$

### 2.3 逐点强化（点级有限见证）
$$\text{对给定证书}\ y\in X_N：$$
$$\qquad \text{(i)}\ y\in I_{\infty,N}\ \Longrightarrow\ y\ \textbf{延拓为全局 thread}（2.1）\ \Longrightarrow\ \textbf{无缺陷}；$$
$$\qquad \text{(ii)}\ y\notin I_{\infty,N}\ \Longrightarrow\ \exists M\ge N:\ y\notin\operatorname{im}(X_M\to X_N)\ \Longrightarrow\ y\ \textbf{被某有限阶段杀死}\ \Longrightarrow\ \textbf{有限阶段可见}$$
$$\Longrightarrow\ \boxed{\textbf{不存在"逐层局部一致但在极限处失败"的中间情形}}\quad(\text{点级有限见证})\ ✓$$

## 3. 第三刀：$\lim^{1}$ 检查（**不得先假定，也不得自动贴 G3**）
$$\text{由 2.1，}\pi_N(\varprojlim)=I_{\infty,N}\ \text{恒成立，故}\ \textit{不存在}\ \text{"稳定像之外的整体障碍"}。$$
$$\lim^{1}\ne0\ (\text{即非 ML}) \text{在此蕴含的是}\ I_{\infty,N}\subsetneq X_N，\text{即}\ \textbf{某些阶段元不延拓}（\text{不是全局障碍}）；$$
$$\qquad \text{而由 2.3(ii)，这类元皆}\ \textbf{有限阶段可见}\ \Longrightarrow\ \text{(a) 有限可判}\to\textbf{V259-A}；\ \text{(b) 非有限可判}\to\textbf{V271-A}\ (\text{非柱不给有限证书})$$
$$\textbf{故}\ \lim^{1}\ne0\ \text{不产生新的算术对象}；\ \text{更不自动升级为}\ \mathrm{VI}\ \text{或 G3}\ ✓\ (\text{V269 勘误纪律遵守：无显式结构不贴标签})$$

## 4. 逃逸口核查（§5-L 全部落格）
$$\text{(i) 紧致 Hausdorff ＋ 连续}\ \Longrightarrow\ \pi_N(\varprojlim)=I_{\infty,N}\ \Longrightarrow\ \textbf{L-DEAD}\ ✓\ (\text{本档定理})$$
$$\text{(ii) 非紧致}\ \Longrightarrow\ \text{阶段取值落}\ \mathbb R\ \text{等}\ \Longrightarrow\ \textbf{A-leak（V172 §5a）}\ \to\ \text{旧类}$$
$$\text{(iii) bonding 非连续}\ \Longrightarrow\ \text{非可计算}\ \Longrightarrow\ \textbf{V277-B}\ \to\ \text{V211 §1 八类}\ \to\ \text{旧类}$$
$$\text{(iv) 非 Hausdorff／其他拓扑病态}：\text{与"有限呈现算术机制"不符（E.2-A：有限呈现}\ \Longrightarrow\ \text{阶段空间实质离散／有限}\ \Longrightarrow\ \text{紧 Hausdorff）}\ ✗$$
$$\Longrightarrow\ \S5\text{-L}\ \text{在}\ \mathfrak M\ \text{内}\ \textbf{全数落格，无}\ \mathrm{VI}$$

## 5. 判定（三档标准，唐先生指定）
$$\textbf{L-DEAD}\ \checkmark：\text{非满射＋像链不稳定在}\ \mathfrak M\ \text{内}\ \textbf{必然只是有限阶段淘汰}（\text{点级有限见证，§2.3）或}\ \text{退化到已有类（§4）}$$
$$\textbf{L-G3}\ \times：\text{不需要（亦不允许）——}\ \lim^{1}\ \text{不携带新算术对象（§3）}$$
$$\textbf{L-VI}\ \times：\text{六项条件中的第三项（"极限产生新的 global obstruction"）被 §2.1 定理否定}\ \Longrightarrow\ \text{不构成 VI candidate}$$

## 6. 对 V320 勘误的**修复**（T10 续）
$$\text{V320 勘误原判：}\text{"§5 DEAD 未成立"}\ \text{—— 该勘误}\ \textbf{保留}（原结论确实误用提升性）。$$
$$\text{修复：以本档 §2.1（V321-A）}\ \textbf{证明形式}\ \text{替代被误引的"有限见证"：}$$
$$\qquad \text{原来需要的不是"}\lim_{\leftarrow}\ne\varnothing\text{"（存在性），\text{而是}\ \textbf{点级延拓性}\ \pi_N(\varprojlim)=I_{\infty,N}；}$$
$$\qquad \text{后者}\ \textbf{在紧致 Hausdorff＋连续下成立且可证}（V321-A，\text{本档证明，不依赖 ML）}\ ✓$$
$$\Longrightarrow\ \boxed{\text{V211 §5}\ \textbf{DEAD（}\text{证明形式，2026-09-16）}}\quad\text{且}\ \boxed{\mathfrak M=\mathfrak M_{\text{closed}}\ \sqcup\ C_0}\ \text{（恢复，但现为有效）}$$

## 7. 边界（N1/N2 严守）
$$\text{① V321-A 为}\ \textbf{标准论证的本档写全}（[标准事实]／[本档证明]），\textbf{未跑 Lean}；\quad\text{② §5 的"DEAD"}\ \textbf{枚举＋结构混合型}，\text{不得升级为"}\mathrm{VI}\ \text{不可能"；}$$
$$\text{③ §4(iv) 的"有限呈现}\Rightarrow\text{阶段实质离散"为}\ \textbf{[结构判定]}；\quad\text{④ 全档}\ \textbf{未碰 RH／零点／显式公式／}C_0；零数值。$$

## 8. 净产出
$$\text{(i) V321-A 定理：紧致 Hausdorff＋连续}\Longrightarrow\pi_N(\varprojlim)=I_{\infty,N}（\textbf{严格包含不可能}）；$$
$$\text{(ii) 点级强化：}\textbf{不存在"逐层局部一致但极限失败"的中间情形}\ \Longrightarrow\ \S5\text{-L}\ \text{的核心机制不存在}；$$
$$\text{(iii) }\lim^{1}\ \text{不携带新算术对象}\ \Longrightarrow\ \text{不贴 G3、不升级 VI；}$$
$$\text{(iv) L-DEAD}\ \checkmark\ \text{且以}\ \textbf{证明形式} \text{修复 V320 勘误} \Longrightarrow\ \mathfrak M\ \text{残余恢复为单一}\ C_0。$$
