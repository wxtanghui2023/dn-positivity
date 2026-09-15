# V162 · ⭐⭐⭐⭐⭐ **C-i「有理性 → 零密度受限」升级审计 —— ①⚠️ 纠正：**不写**"零密度 $\Rightarrow$ 非有理"的无条件泛化（$\text{non-rational}\not\Rightarrow$ Weyl spectrum）✗✓；②正确升级 ＝ **有限状态谱容量定理 FSC**（Artin–Mazur／Ruelle 型）＋ **C-i$^\star$**；③三级结构确立：有限状态 ⟹ 排除 ζ 完整谱；**无限状态 $\not\Rightarrow$ operator ⟹ 仍开放** ✓✓；④⭐ 本档新增：**计数条件(W)便宜、内生／点定位才是承重** ⟹ 五条件压缩后残余回到同一点**
> 委托 ✓ 唐先生 2026-09-15 10:59（**"可以做 ②，但我要先纠正一个关键点：不要把它写成'零密度 ⇒ 非有理'的无条件泛化定理"** ✓；并给出 §①–§⑤ 全部核心论证 ✓）
> 查图 ✓ `V161`（类 C 三障碍 C-i／C-ii／C-iii；唯一未封闭形态）｜`V160`（$A1/A3\subsetneq C_{\rm analytic}$）｜`V153`（∃／λ 分裂）｜`V155`（箭头形态）｜`L1`（非自伴谱刚性 NO-GO）｜**Artin–Mazur／Ruelle（经典）**｜`V136`（超积 ⟹ 仅模型论容器）
> 执行 ✓ 小灵（落档＋纠正＋边界标注＋**§6 两项分解为本档新增** ✓）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V162**

---

## §0 判定（✓ 四条 ✓）

$$\boxed{\text{① 纠正成立} ✗✓：\textbf{不写}\ \text{"零密度}\Rightarrow\text{非有理"}\ \text{作为一般定理};\ \text{完整形式}\ \boxed{\text{有理动力学}\Rightarrow\text{周期／代数型谱}\Rightarrow\text{零点计数增长受限}}\ \text{再证 ζ 违反该上界} ✓✓}$$
$$\boxed{\text{② 正确升级 ＝ }\textbf{FSC} ✓✓：\boxed{\dim(\text{state space})<\infty\Longrightarrow\text{independent spectral channels}<\infty}\ \Longrightarrow\ \boxed{\text{finite-state combinatorial carrier}\not\cong Z_\zeta-\tfrac12}\ \text{(C-i}^\star\text{)}}$$
$$\boxed{\text{③ 三级结构} ✓✓：\text{有限状态}\Rightarrow\text{rational／有限谱通道}\Rightarrow\text{排除 ζ 完整谱};\ \textbf{无限状态}\not\Rightarrow\text{operator}\Rightarrow\textbf{仍开放}\ \text{—— 故 C-ii}\ \textbf{不能}\text{由 C-i 推出} ✗✓}$$
$$\boxed{\text{④ ⭐ 本档新增} ✓✓：\text{计数条件 (W) }\textbf{便宜}（\text{任何递增序列可实现任意给定计数函数}）\ \Longrightarrow\ \text{承重的是}\textbf{内生＋点定位} ⟹ \text{五条件压缩后残余回到同一点（}\lambda\text{-supply／箭头}）✓}$$

---

## §1 动力 ζ 与其有理性（✓ 唐先生逐字 ✓）

$$\zeta_T(z)=\exp\Bigl(\sum_{n\ge1}\tfrac{a_n}{n}z^n\Bigr)\ ✓;\ \text{若}\ \zeta_T(z)=\tfrac{P(z)}{Q(z)}\ ✓,\ \text{则其极点／零点集合在 }z\text{-平面上只有}\textbf{有限多个位置} ✓$$
$$\Longrightarrow\ \text{对任何固定参数化}\ z=z(s)\ ✓,\ \text{所得零点只能来自}\textbf{有限个代数分支} ✓$$
$$\qquad\boxed{\text{关键不是"有理函数零点有限"这么简单} ✓,\ \text{而是}：\text{有限状态}\Rightarrow\zeta_T\ \text{rational}\Rightarrow\textbf{有限基本谱参数}} ✓$$

---

## §2 ⚠️ 纠正：不得写成"零密度 $\Rightarrow$ 非有理"（✓✓ 本档第①件 ✓）

$$\text{反例 ✓}：f(z)=\prod_{n=1}^{\infty}(1-z/2^n)\ \text{有}\textbf{无限零点}\ ✓,\ \text{但它}\textbf{当然不是}\text{有理函数} ✓\ \Longrightarrow\ \text{无限零点}\Rightarrow\text{非有理}\ \textbf{成立} ✓$$
$$\qquad ⚠️\ \text{但"零密度"若指 }N(T)\sim cT\ ✓,\ \text{则它}\textbf{不是}\text{"有理函数"的充分必要刻画} ✗✓$$
$$\qquad\Longrightarrow\ \boxed{\text{non-rational}\not\Rightarrow\text{Weyl spectrum}} ✓✓\ \text{—— 故}\textbf{不能}\text{把 C-i 升级成"零密度判定有理性"的一般定理} ✗$$

---

## §3 ⭐ FSC：有限状态谱容量定理（✓ 本档核心判据 ✓）

$$\text{对有限状态转移矩阵 }A\ ✓：Z_A(z)=\tfrac{1}{\det(I-zA)}\ ✓\（\text{Artin–Mazur／Ruelle 型有限状态情形} ✓\text{）}$$
$$\qquad\text{若}\ \operatorname{Spec}(A)=\{\lambda_1,\dots,\lambda_m\}\ ✓,\ \text{则}\ Z_A(z)=\prod_{j=1}^{m}(1-\lambda_jz)^{-1}\ ✓\ \Longrightarrow\ \boxed{N_{Z_A}(R)\le m} ✓$$
$$\qquad\text{即：有限 }z\text{-平面内只有}\textbf{有限个基本零／极点} ✓;\ \text{若通过固定解析参数化}\ z=\chi(s)\ \text{产生 }s\text{-零点} ✓,\ \text{则其零点只能来自}\textbf{有限个代数条件}\ \chi(s)=\lambda_j^{-1} ✓$$
$$\Longrightarrow\ \boxed{\dim(\text{state space})<\infty\ \Longrightarrow\ \text{independent spectral channels}<\infty}\ \tag{FSC}$$
$$\qquad\textbf{形式化链条 ✓（可长期引用）}：\boxed{\text{finite-state}\Rightarrow\text{rational dynamical zeta}\Rightarrow\text{finite independent spectral channels}\Rightarrow\Phi\ \text{不可能完整识别 ζ 零谱}} ✓✓$$

---

## §4 与 ζ 比较 ⟹ **C-i$^\star$**（✓✓）

$$N_\zeta(T)=\tfrac{T}{2\pi}\log\tfrac{T}{2\pi}-\tfrac{T}{2\pi}+O(\log T)\ ✓\ \Longrightarrow\ N_\zeta(T)\to\infty\ ✓,\ \text{且更强}：\tfrac{N_\zeta(T)}{T}\sim\tfrac{1}{2\pi}\log T\to\infty\ ✓✓$$
$$\Longrightarrow\ \text{任何满足 FSC 的有限状态组合模型}\ \textbf{不可能}\text{拥有}\ Z_\zeta-\tfrac12\ \text{作为其完整谱} ✓$$
$$\Longrightarrow\ \boxed{\text{finite-state combinatorial carrier}\not\cong Z_\zeta-\tfrac12}\ \tag{C-i}^\star\ ✓✓\ \text{（}\textbf{长期可引用的排除式}）$$

---

## §5 ⚠️ 但**不能**杀掉 C-i 的"无穷状态"部分（✓✓ 最重要的边界 ✓）

$$\text{无限状态可以有}\ N(T)\asymp T\log T\ ✓,\ \text{甚至可直接产生非常复杂的谱} ⟹ \boxed{N_\zeta(T)\sim T\log T\ \not\Rightarrow\ \text{operator}} ✓✓$$
$$\Longrightarrow\ \text{即 }V161\ \text{的 C-ii}\ \textbf{仍不能}\text{由 C-i 推出} ✗✓$$

$$\boxed{\text{三级结构} ✓}：\text{有限状态}\Rightarrow\text{rational／有限谱通道}\Rightarrow\text{排除 ζ 完整谱};\qquad \text{无限状态}\not\Rightarrow\text{operator}\Rightarrow\textbf{仍开放} ✓$$

---

## §6 ⭐ 本档新增：两项分解 —— **(W) 便宜，内生／点定位才是承重**（✓✓）

$$\text{设无限组合对象产生}\ \Lambda=\{\lambda_n\}\ ✓\ \text{满足 ζ 所需 Weyl 型增长}\ N_\Lambda(T)\sim\tfrac{T}{2\pi}\log\tfrac{T}{2\pi}\ \tag{W};\ \text{且要求}\ \Lambda=Z_\zeta-\tfrac12$$

$$\textbf{⭐ 观察 1（(W) 单独}\textbf{不构成约束} ✓✓）：\text{对}\textbf{任何}\text{给定的递增计数函数}\ N(T)\ ✓,\ \text{都存在递增序列}\ \lambda_n\ \text{实现它} ✓\ \text{（取 }\lambda_n:=N^{-1}(n)\ \text{即可}）$$
$$\qquad\Longrightarrow\ \boxed{\text{计数／Weyl 条件是可}\textbf{廉价实现}\text{的};\ \text{它}\textbf{不是}\text{承重约束}} ✓✓$$

$$\textbf{⭐ 观察 2（承重的是"内生＋逐点"）✓✓}：\text{三项要求}\ ✓：\text{(1) 无限性}（\text{有限已被 C-i}^\star\ \text{杀}）;\ \text{(2) Weyl 容量}（\text{须自然产生 }T\log T\ \text{而非 }T／T^\alpha／e^T）;\ \text{(3) }\textbf{点定位}（\text{须产生}\textbf{每一个 }\lambda_n,\ \text{而非只产生 }N(T) ✓）$$
$$\qquad\Longrightarrow\ \text{由观察 1，(2)}\ \textbf{不承重};\ \text{真正承重的是}\ \boxed{\text{内部机制产生 }\lambda_1,\lambda_2,\dots\ \text{而不能作为外部参数输入}} ✓✓$$

$$\textbf{⭐ 观察 3（}T\log T\ \text{的"非组合性"）✓}：\text{纯组合计数的天然增长是}\ \text{多项式 }T^d\ \text{或}\ \text{指数 }e^{cT} ✓;\ \text{而}\ T\log T\ \text{介于两者之间} ✓,\ \text{且恰是}\ \textbf{1 维半经典（Weyl）密度律} ✓$$
$$\qquad\Longrightarrow\ \text{要}\textbf{自然}\text{产生}\ T\log T\ ✓,\ \text{通常须一个}\ \boxed{\textbf{连续化}\text{步骤}}\（\text{把离散参数映到连续 }s\text{-平面并按 log 密度分布}）✓,\ \text{而这一步}\textbf{正是解析结构} ✓\ \text{（}\textbf{[结构性] ⚠️\ 非定理}）$$

$$\Longrightarrow\ \boxed{\text{故 V162 的净结论} ✓}：\text{五条件中真正承重的不是"无限状态能不能有很多零点"（当然能）} ✗,\ \text{而是}\ ✓：\boxed{\text{一个非算子化的无限组合对象，凭什么自然地产生 }N(T)\sim T\log T\ \textbf{且逐点锁定}\ \gamma_n？}$$

---

## §7 五条件压缩后的残余（✓ 唐先生逐字 ✓）

$$\boxed{\textbf{无限状态}\ \downarrow\ \textbf{非算子化}\ \downarrow\ \textbf{内生地产生 }T\log T\ \textbf{的离散谱}\ \downarrow\ \textbf{不输入 }\gamma_n\ \downarrow\ \Lambda_M=Z_\zeta-\tfrac12}\ \text{—— 五项须}\textbf{同时}\text{成立} ✓✓$$
$$\qquad\Longrightarrow\ ⭐\ \text{若可证该形态}\textbf{必然退化}\text{为算子谱／解析谱／外部编码} ⟹ \textbf{C 类真正接近封口} ✓✓$$
$$\qquad\Longrightarrow\ ⭐\ \text{若找到满足五项的具体机制} ⟹ \text{这不是包装变化，而是目前整个 RH 搜索中}\textbf{第一个真正有资格叫 C6／第七类}\ \text{的东西} ✓✓$$
$$\qquad ⚠️\ \textbf{与 }V153/V155\ \text{的接口 ✓}：\text{承重项（内生＋逐点锁定）＝ }V153\ \text{的 }\lambda\text{-supply}\ ＝\ V155\ \text{的 }A\to\lambda\ \text{箭头} ⟹ \text{残余}\textbf{回到同一点}（\text{未产生新墙}）✓$$

---

## §8 判词与下一步（✓）

$$\boxed{\textbf{V162 判词 ✓}：① 纠正成立（不写"零密度 ⇒ 非有理"）✓✓;\ ② \text{FSC ＋ C-i}^\star\ \text{（长期可引用）} ✓✓;\ ③ \text{三级结构（有限杀／无限开）} ✓✓;\ ④ \text{两项分解：(W) 便宜、内生承重} ✓✓;\ ⑤ \text{五条件压缩后残余回到 }V153/V155\ \text{同一点} ✓}$$
$$\qquad\textbf{净收获 ✓（判据升级＋承重点识别）}：\text{C-i}\ \text{被升级为}\textbf{可复用判据（FSC）};\ \text{同时}\textbf{识别出承重项} ⟹ \text{避免在"计数条件"上做无用功} ✓✓$$
$$\qquad\textbf{诚实边界 ✓（三条）}：\text{(i) §6 观察 3（}T\log T\ \text{非组合性）为}\textbf{[结构性]} ⚠️\ \text{非定理};\ \text{(ii) §6 观察 2 的"不承重"是}\textbf{归约陈述} ⚠️;\ \text{(iii) FSC 依【Artin–Mazur／Ruelle 经典} ✓\ \text{＋ }L1\ \text{NO-GO（档案级）} ✓】$$
$$\qquad\textbf{下一步三选 ✓}：\text{① 攻承重项：}\textbf{内生＋逐点锁定}（＝V153 }\lambda\text{-supply／V155 箭头）—— \text{但该靶早已登记，须}\textbf{新入口}才能再攻};\ \text{② 把 FSC 写成}\textbf{工具卡}（\text{可执行判据：给定组合载体 ⟹ 检查 state space 有限性 ⟹ 判 }\Phi\ \text{不可能}）✓;\ \text{③ 审 §6 观察 3 能否成为定理（}T\log T\ \Rightarrow\ \text{连续化）✓$$
$$\text{`CLOSED-ROUTES-MAP` §F.5x 增补 ✓}：\text{纠正行 ＋ FSC 行 ＋ C-i}^\star\ \text{行 ＋ 三级结构行 ＋ 两项分解行 ＋ 五条件行 ✓}$$

```
⚠️ §2 纠正为【唐先生判定 ✓✓】＋附反例 f(z)=∏(1−z/2^n) ✓
⚠️ §3 FSC 依【Artin–Mazur／Ruelle 经典 ✓】；§4 C-i⋆ 依【RvM 计数（经典）✓】
⚠️ §5 三级结构为【本档确立 ✓】（无限状态不杀）
⚠️ §6 观察 1 为【构造性 ✓✓】（λ_n := N^{-1}(n)）—— 故 (W) 便宜；观察 2 为【归约 ⚠️】；观察 3 为【结构性 ⚠️】
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 纠正（不写零密度⇒非有理）✓✓；② FSC 判据 ＋ C-i⋆ 排除式 ✓✓；③ 三级结构 ✓✓；
   ④ 两项分解（(W) 便宜／内生承重）✓✓；⑤ 五条件残余 ＋ 承重点归约回 V153/V155 ✓
```
