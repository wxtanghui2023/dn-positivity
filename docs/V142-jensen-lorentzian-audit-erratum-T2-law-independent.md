# V142 · ⭐⭐⭐⭐⭐ **ξ-Jensen Lorentzian 小审计：① 二元 Lorentzian ⟺ 非负 ＋ 支撑区间 ＋ Newton 不等式（本档推导 ✓）；② ⚠️ 勘误：Lorentzian 【不】蕴含 hyperbolic ✗（显式反例 ✓）⟹ 我 `V141` §1③ 的"RH 强度"判断【错了】✗；③ ξ-Jensen 的 Lorentzian 条件在 GORZ 范围内**已无条件成立** ✓✓（hyperbolic ⟹ Newton ✓）；④ 档案决定性：A2 路线**已关闭**（Farmer ✓）；⑤ ⭐⭐ 附带：**$T^2$ 律在此独立出现**（$d\le T^2$ ⟹ W3 独立确认 ✓✓）**
> 委托 ✓ 唐先生 2026-09-14 23:29（**"做一下"** ✓ —— 即 `V141` §2 的可判定小审计 ✓）
> 查图 ✓ **同题已做** —— `ALIGN-A2-jensen-polya`（A2 对齐档案 ✓：Pólya 判据 ＋ GORZ ＋ 有效化 ⟹ $d\le T^2$ ＋ **Farmer 封闭** ✓）＋ `MAP3-jensen-mechanism-verified-from-originals` ✓ ＋ `jensen2.txt`（ξ(½+it) Taylor 系数 ✓）
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓；全部为定义展开 ＋ 逻辑核对 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜T10 ✓（对 `V141` 出勘误 ✓）｜编号 ✓ V142 ✓

---

## §0 判定（✓ 五条 ✓）

$$\boxed{\text{① 二元 Lorentzian 的等价形式（本档 ✓）}：\text{非负系数}\ +\ \textbf{支撑为区间}\ +\ \textbf{Newton 不等式（超对数凹）}}$$
$$\boxed{\text{② ⚠️ 勘误 ✓}：\textbf{Lorentzian}\ \not\Longrightarrow\ \textbf{hyperbolic}\ ✗（\text{显式反例 ✓}）\ \Longrightarrow\ \text{我 }V141\ \text{§1③ 的"ξ-Jensen 若 Lorentzian ⟹ 直接得 RH ⟹ RH 强度"}\textbf{判断错误 ✗}}$$
$$\boxed{\text{③ 因此 ✓}：\text{Lorentzianity}\ \textbf{严格弱于}\ RH\ ✗;\ \text{且其超对数凹部分【已被 GORZ 的 hyperbolicity 结果无条件蕴含】✓✓}（\text{hyperbolic ⟹ Newton ✓）}}$$
$$\boxed{\text{④ ⟹ 该路线 ⟹ 落【已封格】✗}：\text{档案 }A2\ \text{路线已关闭 ✓（}Farmer\text{："Jensen polynomials are NOT a viable route to RH" ✓）}}$$
$$\boxed{\text{⑤ ⭐⭐ 附带发现 ✓✓}：T^2\ \text{律在此【独立出现】}（d\le T^2\ ✓）\ \Longrightarrow\ W3\ \text{得到独立确认 ✓✓}}$$

## §1 二元 Lorentzian 的等价形式（✓ 本档推导 ✓）

$$\textbf{设定 ✓}：\text{一元 }f(t)=\sum_{j=0}^{d}a_jt^j\ \longleftrightarrow\ \text{二元齐次 }f(X,Y)=\sum_ja_jX^jY^{d-j}\ ✓$$
$$\textbf{条件三件套 ✓}（Brändén–Huh ✓）：\text{(i) }a_j\ge0\ ✓;\ \text{(ii) 支撑 M-凸 ✓};\ \text{(iii) 全部 }(d-2)\ \text{阶偏导所得的二次型签名}\le(1,\cdot)\ ✓$$
$$\textbf{(ii) 一元情形的化简 ✓（两行 ✓）}：\text{支撑在直线 }\{(j,d-j)\}\ \text{上 ✓；}M\text{-凸的公理（}u=e_u,v=e_v,u_i>v_i\Rightarrow\exists j:u_j<v_j,\ u-e_i+e_j\in S\ ✓）$$
$$\qquad\Longrightarrow\ \text{沿该直线"逐步内移"必须仍在 }S\ ⟹\ S\ \textbf{为连续区间} ✓✓（\text{即：中间不得有零系数 ✗}）$$
$$\textbf{(iii) 的化简 ✓}：\text{取 }(d-2)\ \text{阶偏导 ⟹ 二次型；其签名条件展开后}\textbf{恰为 Newton 不等式} ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{一元：Lorentzian}\iff\ a_j\ge0\ \wedge\ \text{支撑区间}\ \wedge\ \tilde a_j^2\ge\tilde a_{j-1}\tilde a_{j+1}\（\tilde a_j:=a_j/\tbinom dj\ ✓\text{）}}$$
$$\qquad\textbf{即 ✓}：\text{非负}\ +\ \text{支撑区间}\ +\ \textbf{归一化系数超对数凹（ultra-log-concave ✓）}$$

## §2 ⚠️ 勘误（T10 ✓）：Lorentzian $\not\Rightarrow$ hyperbolic（✗ 我上一轮错了）

$$\textbf{显式反例 ✓✓}：f(t)=t^3+3t^2+3t+3\ \longleftrightarrow\ f(X,Y)=X^3+3X^2Y+3XY^2+3Y^3\ ✓$$
$$\qquad\text{系数 ✓}：a=(1,3,3,3)\ ✓\ \text{归一化 }\tilde a=(1,1,1,1)\ ✓\ \Longrightarrow\ \tilde a_j^2=\tilde a_{j-1}\tilde a_{j+1}=1\ ✓\ \textbf{超对数凹 ✓（取等 ✓）}$$
$$\qquad\textbf{故 Lorentzian ✓（支撑区间 ＋ 非负 ＋ Newton ✓）}$$
$$\qquad\textbf{但根 ✗}：f(t)=(t+1)^3+2\ ✓\ \Longrightarrow\ \text{根 }=-1+\sqrt[3]{-2}\omega^k\ ✓\ \Longrightarrow\ \textbf{一实两复 ⟹ 非 hyperbolic ✗✓}$$
$$\Longrightarrow\ \boxed{\textbf{Lorentzian}\ \not\Longrightarrow\ \textbf{hyperbolic ✗✓}}\qquad\text{（正确蕴含方向 ＝ }\textbf{stable／hyperbolic} \Longrightarrow \text{Lorentzian}\ ✓）$$
$$\qquad\textbf{因此 }}V141\ \text{§1③ 的论断（"Lorentzian ⟹ hyperbolic ⟹ 直接得 RH ⟹ 该命题本身即 RH 强度"）}\textbf{错误 ✗}$$
$$\qquad\qquad\textbf{实际含义 ✓（方向反转 ✓）}：\text{Lorentzianity}\ \textbf{弱于} RH\ ✗\ \Longrightarrow\ \text{它}\textbf{可能是无条件可证的} ✓\ \text{—— 故它}\textbf{不能}充当 RH 的充分条件 ✗✓$$

## §3 对 ξ-Jensen 的两项检查（✓）

$$\text{对象 ✓}：J^{d,n}(X)=\sum_{j=0}^d\tbinom dj\gamma(n+j)X^j\ ✓（\text{系数 }\tbinom dj\gamma(n+j)\ ✓）$$
$$\textbf{(a) 支撑 ✓}：\tbinom dj>0\ ✓\ \Longrightarrow\ \text{支撑}=\{j:\gamma(n+j)\ne0\}\ ✓\ \Longrightarrow\ \text{须【非零性】命题 ⚠️（档案 }`jensen2.txt`\ ∕\ `MAP3`\ \text{已有 }ξ(½+it)\ \text{的 Taylor 系数 ✓ —— 查证未做 ⚠️）}$$
$$\textbf{(b) 超对数凹 ✓✓}：\text{归一化系数 }=\gamma(n+j)\ ✓\ \Longrightarrow\ \text{Lorentzian 的 (iii) 条件}\iff\{\gamma(n+\cdot)\}\ \text{对数凹}\ ✓$$
$$\qquad \textbf{关键 ✓}：\text{hyperbolic}\ \Longrightarrow\ \text{Newton 不等式} ✓（\text{经典 ✓}）\ \Longrightarrow\ \textbf{GORZ 的 hyperbolicity 结果【无条件蕴含】该项} ✓✓$$
$$\qquad\qquad\text{（}GORZ\ ✓：\text{对每个 }d\ \text{存在 }N(d)\ \text{使 }n\ge N(d)\ \text{时全部双曲 ✓；}d\le8\ \text{时全部 }n\ ✓；\text{有效化版 ⟹ }d\le T^2\ ✓）$$
$$\Longrightarrow\ \boxed{\text{故在 GORZ 覆盖范围内 ✓}：\text{ξ-Jensen 的 Lorentzian（超对数凹部分）}\textbf{已无条件成立} ✓✓}$$
$$\qquad\Longrightarrow\ \text{唯一剩余差距 ＝ }\textbf{Lorentzian}\ \Longrightarrow\ \text{hyperbolic}\ ✓\ \text{—— 而那}\textbf{恰是 RH 所在处} ✗✓\ \text{（§2 ✓）}$$
$$\qquad\Longrightarrow\ \text{故"Lorentzian 路线"在 ξ 上}\textbf{不提供新资源} ✗：\text{它给出的是}\textbf{无条件但弱于 RH} \text{的正性 ✓，而 RH 所需的"实根"没有从它得到 ✗}$$

## §4 ⭐ 档案决定性：A2 路线**已被关闭**（✓）

$$\textbf{`ALIGN-A2-jensen-polya` 逐字 ✓}：\text{A2 判据（Pólya 1927 ✓）}：\text{RH}\iff\text{所有 }J^{d,n}\ \text{双曲 ✓}$$
$$\qquad\text{(i) 已知秩 ✓}：d\le3\ \text{且全部 }n\ ✓（CNV／Dimitrov–Lucas ✓）；\text{(ii) }GORZ\ 2019\ ✓：\text{每 }d\ \text{有 }N(d)\ \text{使 }n\ge N(d)\ \text{双曲；}d\le8\ \text{全部 }n\ ✓\ \text{（方法：Hermite 建模 ⟹ GUE 预测的【导数侧】✓）}$$
$$\qquad\text{(iii) 有效化 ✓（}arXiv\text{:}1910.01227\ ✓）\ \text{Theorem 1.2}：\text{若 RH}_m(T)\ \text{且 }d\le\lfloor T\rfloor^2\ \Longrightarrow\ J^{d,n}\ \text{对全部 }n\ge m\ \text{双曲 ✓};\ \text{Cor. 1.3}：\text{Platt 的 RH}_0(3.06\times10^{10})\ \Longrightarrow\ d\le9.36\times10^{20}\ \text{全部双曲 ✓}$$
$$\qquad\qquad\textbf{⭐⭐ }MAP3\ \text{的核心发现 ✓✓}：\text{"天文数字"}\textbf{本质 ＝ 已数值验证高度 }T\ \textbf{的平方} ✓\ \Longrightarrow\ \textbf{d\le T^2} ✓✓$$
$$\qquad\textbf{(iv) ⭐⭐⭐ 封闭 ✓✓✓}：\textbf{Farmer, }arXiv\text{:}2008.07206\ ✓：\text{"}\textbf{Jensen polynomials are NOT a viable route to proving the Riemann Hypothesis}\text{" ✓✓✓}$$
$$\Longrightarrow\ \boxed{\text{故 Lorentzian 路线（其落在 }\xi\text{-Jensen 上时）}\Longrightarrow \textbf{落 A2 已封格 ✗✓}}$$

## §5 ⭐⭐ 附带发现：$T^2$ 律在此**独立出现**（✓✓ 对项目很重要 ✓）

$$\text{本项目 }W3\（T^2\ \text{律}\ ✓）\ \text{此前来自 Li 路线 ✓：}\text{验证高度 }T\ \Longrightarrow\ \text{线性范围 }n\le2T\ \text{／二次范围 }n\le T^2\ ✓（\text{H1／}V137\ ✓）$$
$$\text{而此处 ✓}：\text{有效化定理给 }d\le\lfloor T\rfloor^2\ ✓\ ——\ \textbf{同一条 }T^2\ \text{律 ✓✓}$$
$$\Longrightarrow\ \boxed{\text{结论 ✓}：T^2\ \text{律}\textbf{不是 Li 路线的产物 ✗}，而是在}\textbf{两条独立路线}（\text{Li 系数 ／ Jensen 双曲性}）\text{中同时出现 ✓✓}}$$
$$\qquad\textbf{对项目的意义 ✓}：\text{这}\textbf{独立确认} \text{了 }W3\ \text{的结构地位 ✓✓（}\text{与 }V137\ \text{的"}\mathcal M_{\rm audited}\ \text{、}R_{\rm residual}\ \text{"框架相容 ✓）}$$
$$\qquad\textbf{并且 ✓}：\text{两条路线的瓶颈}\textbf{同为"}T^2\ \text{墙"}\ ✓\ \Longrightarrow\ \text{支持 }E99\ \text{的结论（}\text{只用"验证高度 }T"\ \text{的判据必然被 }T^2\ \text{封顶 ✓；改进必须【改变输入】✓）}$$

## §6 判词与更新（✓）

$$\boxed{\textbf{审计结论 ✓}：\text{Lorentzian 框架落到 }\xi\text{-Jensen 上}\Longrightarrow \text{① 其超对数凹部分【无条件已成立】（GORZ ⟹ Newton ✓）；② 剩余差距（Lorentzian ⟹ 双曲）＝ RH 所在 ✗；③ 整条双曲性路线}\textbf{已被 }Farmer\ \text{关闭 ✓✓} \Longrightarrow \textbf{不填补 }R_{\rm residual}\ ✗}}$$
$$\qquad\textbf{且有量化对照 ✓✓}：\text{最强的 char-0 多项式正性框架（Lorentzian／Hodge–Riemann ✓）施于 }\xi\ \text{只能给到}\textbf{"系数对数凹"} \text{—— }\textbf{严格低于"实根"}\ ✗\ \text{（§2 反例显示二者不同级 ✓）}$$
$$\qquad\qquad\Longrightarrow\ \text{这是}\textbf{N29（正性 ⟹ 位置盲 ✗）} \text{的一个【量化实例 ✓】：正性框架}\ \textbf{连"实根"都不给} ✗，更不给 \beta\ \text{定位 ✓✓}$$
```
⚠️ §1 的三件套化简为【本档推导 ✓】（定义展开 ＋ M-凸公理两行 ✓）；其与 Brändén–Huh 原文的逐字一致性未核对 ⚠️（II 类 ✓）
⚠️ §2 反例为【显式构造 ✓ 可验证 ✓】（(t+1)^3+2 ✓；归一化系数全 1 ✓）—— 该反例同时确认"Newton 不等式不蕴含实根"这一经典事实 ✓
⚠️ §3(a) 的"非零性"未查证 ⚠️（`jensen2.txt`／`MAP3` 在档但其内容本档未读 ✗）
⚠️ §4 §5 为【档案核对 ＋ 逻辑论证 ✓】；引文均为档案已核过的原文 ✓（`ALIGN-A2` 标"我方已核实原文 ✓✓"）
⚠️ 本档未用 RH ✓；未跑 Lean ✓；零数值 ✓；T10 勘误已出（对 `V141` ✓）
✅ 净产出 ✓：① Lorentzian 等价形式 ✓；② ⚠️ 勘误（我上一轮错 ✗）；③ ξ-Jensen 两检查 ✓（含"无条件已成立"✓）；
   ④ A2 已封格确认 ✓；⑤ ⭐⭐ T^2 律独立确认 ✓✓；⑥ 量化对照（正性 ⟹ 连实根都不给 ✓）
```
$$\boxed{\text{V142 ✓：ξ-Jensen Lorentzian 审计 —— ①一元 Lorentzian ⟺ 非负 ＋ 支撑区间 ＋ 超对数凹（Newton ✓，本档推导 ✓）；②⚠️勘误：}\textbf{Lorentzian}\not\Rightarrow\textbf{hyperbolic}\ ✗（反例 }t^3+3t^2+3t+3\ ✓\text{：归一化系数全 1 ⟹ 超对数凹 ✓ 但 }(t+1)^3+2\ \text{一实两复 ✗）⟹ 我 }V141\ \text{§1③ 的"RH 强度"判断}\textbf{错误 ✗}，方向反转：Lorentzian 弱于 RH ✓；③ ξ-Jensen：超对数凹部分}\textbf{已被 GORZ 无条件蕴含} ✓✓（hyperbolic ⟹ Newton），剩余差距 ＝ Lorentzian ⟹ 双曲 ＝ RH 所在 ✗；④ 档案 A2（Jensen–Pólya）路线}\textbf{已由 Farmer 关闭} ✓✓；⑤ ⭐⭐ }\textbf{T^2 律独立出现}（d\le T^2 ✓）⟹ W3 独立确认 ✓✓；⑥ 量化对照：最强的 char-0 多项式正性（Lorentzian／Hodge–Riemann）施于 ξ 只有"系数对数凹"，}\textbf{严格低于"实根"} ⟹ N29 位置盲的量化实例 ✓}$$
