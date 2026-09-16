# V296 · **非局部核的"带宽不可约性"审计** —— ⭐⭐⭐⭐⭐ **定理（本档）$G(K)=1-R_{\rm off}$**（$R_{\rm diag}=1$ 归一化）⟹ **障碍类型 ＝ B（离对角／算术相关性）**；⭐ **"判死刀"已存在但它砍的是"证书类"而非"核"**（＝论文自己的天花板：$0.68185\iff R_{\rm off}\ge0.318$）；⭐⭐⭐ **故逃逸口 ＝ "$\sigma_{\min}(K)\le1$ 但不在证书类内"的核**，其自然候选 ＝ **非 Toeplitz（非平移不变）全局投影**（它同时失去 $\alpha$-支撑控制，故须另找无条件控制源）

$$\boxed{\textbf{核心恒等式（本档）}：G(K)\ =\ 2-\mathfrak R(K)\ =\ 2-\big(R_{\rm diag}+R_{\rm off}\big)\ =\ \boxed{1-R_{\rm off}}\quad（R_{\rm diag}=1\ \text{为归一化}）} ✓✓✓$$
$$\boxed{\Longrightarrow\ G(K)\le1\ \text{恒成立};\qquad G(K)=1\iff R_{\rm off}=0} ✓✓✓$$
$$\boxed{\text{已知天花板}\ 0.68185\ \iff\ R_{\rm off}\ge0.318\（\text{带宽一证书类}）\Longrightarrow \textbf{"判死刀"存在，但砍的是证书类}} ✓✓✓$$
$$\boxed{\textbf{逃逸口}：\exists\,K:\ \sigma_{\min}(K)\le1\ \wedge\ K\notin\text{证书类}\ \wedge\ R_{\rm off}\to0} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:15：**定 (乙′)**，且**"不能做成'把更多非局部核列一遍'的分类综述，要推进成结构性判别定理"** ✓；四步：**V296.1** $R(\psi)\to\mathfrak R(K)$ 核不变量｜**V296.2** 定义 $\sigma_{\min}(K)$ 消除表示依赖｜**V296.3** $\sigma_{\min}\le1\Rightarrow\mathfrak R\ge1+c$？（**判死刀**）｜**V296.4** 若失败，构造 $K_m$ 使 $\mathfrak R(K_m)\to1$（**逃逸刀**）✓✓；并给三障碍型 A 对角／B 离对角／C Gram-正性／带宽，及三轴定位（零点几何 × 非局部算子 × 算术支撑）✓✓
> 依据 ✓ `V295`（$2/3=r_{\rm comp}\!\to\!1\times(2-R(\psi_0))$；$R(\psi_0)=4/3$；天花板 0.68185；$P_T$ 为 Gabor 全局投影）｜`V185`（AF 机制 Z/P/L 与单链；Ceiling.lean 抽象天花板；Remark 1.1 路线图 1.04/1.26/1.70）｜**Montgomery 1973**（$F(\alpha)$ 在 $|\alpha|\le1$ **无条件**、$|\alpha|>1$ 需 RH）［经典·引用］✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V296`（`id_claim.sh` ✓）

---

## §1 **V296.1**：$R(\psi)$ 改写成核不变量 $\mathfrak R(K)$

$$\text{Poisson–Gabor 恒等式（`V185` §2.1，Lemma 2.1）}：\sum_{k\in\mathbb Z}\widehat\phi(z-\alpha_k)\widehat\phi(z'-\alpha_k)=L\,\widehat{\phi^{2}}(z-z') ✓$$
$$\qquad ⟹ \langle v_\rho,v_{\rho'}\rangle=L\,\widehat{\phi^{2}}\big(\gamma_\rho-\gamma_{\rho'}\big)\ ⟹\ \big|\langle v_\rho,v_{\rho'}\rangle\big|^{2}=L^{2}\big|\widehat{\phi^{2}}\big(\gamma_\rho-\gamma_{\rho'}\big)\big|^{2} ✓$$
$$\Longrightarrow\ \boxed{\|\widetilde G\|_{\rm HS}^{2}=\frac1{a^{2}N}\sum_{\rho,\rho'}m_\rho m_{\rho'}\,\mathbb K\big(\gamma_\rho,\gamma_{\rho'}\big)+o(1),\qquad \mathbb K(\gamma,\gamma')：＝\big|\widehat{\phi^{2}}(\gamma-\gamma')\big|^{2}} ✓✓$$
$$\qquad ⟹ \boxed{\mathfrak R(K)\ ：＝\ \text{零对测度在配对核}\ \mathbb K\ \text{下的归一化质量}} ⟹ \text{即"}\textbf{配对核不变量} ✓✓$$
$$\text{而}\ \mathbb K\ \text{的"}\alpha\text{-支撑"}\ ＝\ \text{证书的 Dirichlet 多项式指数差集}\ \{\log(n/m)\};\ \text{"带宽}\le1\text{"}\iff\{\log(n/m)\}\subseteq[-L,L] ✓✓$$
$$\qquad \text{（等价说法：}\log X\le L=\log\tfrac T{2\pi}\iff X\le T\ \text{—— 即 Montgomery 的"带宽一"）✓✓$$

$$\textbf{经典分裂（[经典·引用]，标 [推断]}）：}\ \mathfrak R(K)=R_{\rm diag}+R_{\rm off}，\ \text{其中}$$
$$\qquad R_{\rm diag}：\ \alpha=0\ \text{对角质量}\（\text{归一化为}\ 1）;\qquad R_{\rm off}：\ \alpha\ne0\ \text{离对角质量}\（\text{由 form factor}\ F(\alpha)\ \text{控制}）✓$$
$$\qquad ⚠️\ \text{Montgomery：}\ F(\alpha)=1+o(1)\ \text{在}\ |\alpha|\le1\ \textbf{无条件};\ |\alpha|>1\ \textbf{需 RH} ✓✓✓\ \text{（＝`V162`"support}>1\ \text{墙"}）$$
$$\qquad \text{AF 两窗的读数}：\psi_0\Rightarrow R_{\rm off}=\tfrac13\（\mathfrak R=\tfrac43）;\qquad \psi_{\rm MT}\Rightarrow \mathfrak R=1.3275\（R_{\rm off}=0.3275）✓$$
$$\Longrightarrow \boxed{\textbf{障碍类型}＝\textbf{B（离对角／算术相关性）}\ \text{—— 非 A（对角），亦非 C（Gram）}} ✓✓✓\ \text{［推断，待核验］}$$

---

## §2 **V296.2**：$\sigma_{\min}(K)$ 的定义与良定性

$$\boxed{\sigma_{\min}(K)：＝\inf\Big\{\text{bandwidth}(P)\ :\ K=P^{*}P\Big\}} ✓$$
$$\qquad \textbf{平移不变（Toeplitz）情形}：K=K(\gamma-\gamma')\（\text{AF 核即此类}）⟹ \text{其}\ \alpha\text{-符号}\ \widehat{K}\ \text{唯一} ⟹ \sigma_{\min}(K)=\sup\{|\alpha|:\ \widehat K(\alpha)\ne0\}\ \textbf{表示无关} ✓✓$$
$$\qquad ⚠️\ \textbf{一般（非 Toeplitz）情形}：\text{"bandwidth}(P)\text{"}\ \textbf{尚无} \text{定义} ⟹ \text{这正是}\ \textbf{定义缺口}（本档 §3–§4 的核心）✓✓✓$$
$$\qquad \text{AF 核的读数}：\sigma_{\min}=1\ \text{（临界）};\ \text{而} \psi_{\rm MT}\ \text{与}\ \psi_0\ \text{同属带宽一} ⟹ \text{二者}\ \sigma_{\min}\ \text{相同（皆 1）} ✓$$

---

## §3 ⭐⭐⭐ **V296.3 判死刀：命题成立 —— 但它砍的是"证书类"，不是"核"**

$$\textbf{在证书框架内}：\text{论文 Remark 1.1 ＋ Ceiling.lean（抽象天花板）}：$$
$$\qquad \text{只读}\ \textbf{带宽一} \text{数据、且}\ \textbf{逐配置} \text{成立的证书} ⟹ \text{可认证比例}\le0.68185 ✓$$
$$\qquad ⟹ G(K)\le0.68185 ⟹ \boxed{\mathfrak R(K)\ \ge\ 2-0.68185\ =\ 1.31815\ >1} ⟹ \textbf{命题成立（}c\approx0.318\text{）} ✓✓✓$$
$$\qquad \text{（与 §1 一致：}R_{\rm off}\ge0.318\ \text{对带宽一证书}）✓$$
$$\boxed{\textbf{但关键}：\text{该定理的假设}\ \textbf{不是}\ \sigma_{\min}(K)\le1，\text{而是}\ \textbf{"带宽一的逐配置证书"}} ✓✓✓$$
$$\qquad \text{① Ceiling.lean 的陈述是关于证书数据}\ (c_0,r)\ \text{的}\ \textbf{泛函界};\ \text{② 其证明用}\ \textbf{证书的}\ \alpha\text{-支撑（指数差集）};\ \text{③ 对}\ \textbf{非 Toeplitz} \text{核，"指数差集"}\ \textbf{根本不存在} ⟹ \text{定理}\ \textbf{不适用} ✓✓✓$$
$$\Longrightarrow \boxed{\text{故"判死刀"存在，但它砍的是}\ \textbf{证书类};\ \text{而}\ \sigma_{\min}(K)\le1\ \text{与"属证书类"}\ \textbf{不是同一条件}} ⟹ \textbf{二者的缺口 ＝ 逃逸空间} ✓✓✓$$

---

## §4 ⭐⭐⭐ **V296.4 逃逸刀：目标精确化（第一代候选形状）**

$$\boxed{\text{逃逸目标}：\exists\,K:\ \sigma_{\min}(K)\le1\ \wedge\ K\notin\text{证书类}\ \wedge\ \mathfrak R(K)\to1\ (R_{\rm off}\to0)} ✓✓✓$$
$$\textbf{自然候选（本档给出，非列举）}：\boxed{\text{非 Toeplitz（非平移不变）全局投影}}\qquad \text{理由（双向）：} ✓✓✓$$
$$\qquad \text{① 它}\ \textbf{逃出} \text{天花板定理的适用域}（\text{无指数差集} ⟹ \text{带宽约束不作用于它}）;$$
$$\qquad \text{② 但它}\ \textbf{同时失去} \text{赖以无条件的机制} —— \text{带宽一恰恰}\ \textbf{就是} \text{无条件控制的来源（Montgomery：}F(\alpha)=1\ \text{在}\ |\alpha|\le1）✓$$
$$\qquad ⟹ \boxed{\textbf{逃逸的真正困难}：\text{非 Toeplitz 核必须}\ \textbf{另找} \text{一个无条件控制源}} ⟹ \text{这是}\ \textbf{结构性} \text{目标，不是候选枚举} ✓✓✓$$
$$\textbf{三障碍型的判定（本档）}：\text{A 对角？}\ \textbf{否}（R_{\rm diag}=1\ \text{为归一化常量}）;\ \text{C Gram？}\ \textbf{否}（无证据）;\ \boxed{\textbf{B 离对角／算术相关性}：\textbf{是}} ✓✓✓$$

---

## §5 三轴定位与 AF 所在角落（唐先生图）

$$\boxed{\text{零点几何}\ \times\ \text{非局部算子}\ \times\ \text{算术支撑}};\qquad \text{AF}\ \text{位于}\ \big(\text{非局部},\ \text{带宽}\le1,\ \text{无条件二阶矩}\big) ✓✓$$
$$\qquad \text{本档问题（＝(乙′)的搜索空间）}：\exists\ \big(\text{非局部},\ \sigma_{\min}\le1,\ \text{非 AF 类证书}\big)\ \text{使}\ G>0.68185\ ? ✓✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V296 判词}：\text{① }G=1-R_{\rm off}（\textbf{问题被压缩为"离对角质量"}）;\ \text{② 障碍型 ＝ B 离对角／算术相关性};\ \text{③ 判死刀已存在，但砍证书类（}R_{\rm off}\ge0.318）\ \text{而非核};\ \text{④ 逃逸口 ＝ 非 Toeplitz 全局投影（须另找无条件控制源）}} ✓✓✓$$

```
① ⚠️ §1 的"R_diag = 1 归一化 ＋ R_off = 1/3（ψ₀）"为**经典读数** [推断]，**本档未复算**（须核 Montgomery §2–§3 与论文 §5）⚠️
② ⚠️ §1 的核不变量 $\mathfrak R(K)$ 依赖 Poisson–Gabor 恒等式（`V185` 转述）⟹ 未独立复核 ⚠️
③ ⚠️ §3 的"Ceiling.lean 不适用于非 Toeplitz"为**本档判断**（未读 Ceiling.lean 全文）⚠️
④ ⚠️ 本档**不声称**非 Toeplitz 逃逸存在；亦**不声称**"任何非局部核都达不到 1"（N1）✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐⭐ **核心恒等式**：$G(K)=1-R_{\rm off}$（$R_{\rm diag}=1$）⟹ **整个问题 ＝ "离对角质量能否 →0"**；且 $G\le1$ 恒成立（与 `V185` §8(i)"比例法结构性达不到 1"**独立互证**）✓✓✓
② ⭐⭐⭐ **障碍型判定 ＝ B（离对角／算术相关性）** ⟹ 与 `V294` 的"算术侧"接上 ✓✓✓
③ ⭐⭐⭐ **判死刀的地位澄清**：命题**成立**，但它砍的是**证书类**（$R_{\rm off}\ge0.318$，依赖 EnclOK），**不是核** ⟹ **$\sigma_{\min}\le1$ ≠ 属证书类** ⟹ **缺口 ＝ 逃逸空间** ✓✓✓
④ ⭐⭐⭐ **逃逸目标精确化**：**非 Toeplitz 全局投影** —— 它逃出天花板适用域，但**同时失去**无条件控制来源 ⟹ 逃逸的真正困难 ＝ **另找无条件控制源**（结构性目标，非候选枚举）✓✓✓
⑤ ⭐ **互证**：$G\le1$（本档）＋ 比例法结构性天花板（论文）＋ `V294` 三战场划界 ⟹ 三处独立指向同一结论 ✓✓
【下一步（按依赖顺序，供唐先生定）】
  (一) **核验** §1 的经典分裂（$R_{\rm diag}=1$、$\psi_0$ 的 $R_{\rm off}=1/3$）—— 读 Montgomery 1973 与论文 §5（**这是本档全部结论的地基**）✓
  (二) 读 `Ceiling.lean` **全文**，把天花板的假设**逐条对照** $\sigma_{\min}$，把 §3 的"缺口"变成**精确的定理**（"天花板不适用于非 Toeplitz"）✓
  (三) 若 (二) 成立 ⟹ 攻**非 Toeplitz 核的第一代候选**（＝寻找替代的无条件控制源）✓
```

---

## §7 ⚠️ 【勘误 T10】（2026-09-16 13:18 起，唐先生命令"标断点、不补假设"；见 `V297`）

$$\text{本档 §1 原写} ✗：\ \|\widetilde G\|^{2}_{\rm HS}=\big(R(\psi)+o(1)\big)N ⚠️\ \textbf{不精确}（隐含}\ \widetilde G\ \text{已归一化使}\ \operatorname{tr}=N）✓$$
$$\qquad \text{论文 §5 实际承载语句是}\ \textbf{比值}\（`PrimeSideTemp.lean` 逐字）：\ \frac{(\operatorname{tr}\widetilde G)^{2}}{\operatorname{tr}\widetilde G^{2}}=F(\lambda_1)N(T,2T)\big(1+O(\mathcal E_T)\big) ✓✓$$
$$\boxed{\text{更正：}R：＝\frac1{F(\lambda_1)}\ \text{（非独立窗口泛函）；归一化}\ \hat G：＝\widetilde G/(aL)\Rightarrow\operatorname{tr}\hat G=N,\ \operatorname{tr}\hat G^{2}=\frac N{F(\lambda_1)}} ✓✓✓$$
$$\qquad ⟹ \text{单链给出}\ \big(2-\frac1{F(\lambda_1)}\big)N ⟹ \textbf{本档核心恒等式} G=1-R_{\rm off}\ \textbf{在修正后存活}（R_{\rm off}:=\frac1F-1）✓✓$$
$$\qquad ⚠️\ \text{本档 §1 的} R_{\rm diag}=1／R_{\rm off}=1/3\ \text{的"经典读数"标签亦更正为：}\textbf{归一化恒等式}（$R_{\rm diag}=1$）＋ \text{闭式读数}（$F=\frac34\Rightarrow R_{\rm off}=\frac13$）✓$$
