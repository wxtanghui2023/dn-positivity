# V197 · **Steinberg branch：obstruction 值域审计** —— ① ⚠️ **V196 §4 勘误（定义级核对）**：$\hat{\mathbb Z}^\times$ 的 torsion **不是** $\bigoplus_p\mu_{p-1}$，而是 $\bigcup_N\prod_p\mu_{\gcd(N,p-1)}$（**含不可数的 $\mu_2^\infty$、非直和、非离散**）⟹ **V196 §4 的"离散前提存在"撤回** ✓✓；② **$a\to1-a\to\{a,1-a\}\to\partial_v\to$ global** 全链实算 ⟹ **$\partial_v\{a,1-a\}=1$ 对所有 $v$** ⟹ **$\Omega=0$** ⟹ 三分判定落 **A** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 13:31：**"开 V197……不是先问 Steinberg relation 能不能产生离散类，而是把它作为一个候选 obstruction，完整算它的值域"**；**技术点核实**：**"$\hat{\mathbb Z}^\times$ 的 torsion $=\bigoplus_p\mu_{p-1}$ 这个表述涉及有限阶元素在 profinite 单位群中的具体分解；V197 不要沿用它作为未经证明的前提。先从标准结构分解逐项核。"**（并指出 V196 核心结论不依赖此表述）；**只允许链**：$a\mapsto1-a\mapsto\{a,1-a\}\mapsto\partial_v\{a,1-a\}\mapsto\text{global obstruction}$；**禁令同 V196**（$\rho,\gamma,\beta,\Xi$、RH、Weil、Li）；**最终三分**：A $\Omega=0$／B $\Omega\in\mu_N$ 或 $\mathrm{Br}[N]$／C $\Omega\in D_{\rm new}$
> 查图 ✓ `V196`（五步；§4 待核）｜`V195`（机制 II）
> 执行 ✓ 小灵（**§1 勘误、§2 全链实算 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜编号 ✓ **V197**（台账已修正：误占的 V197 改为本档；误领的 V198 删除）

---

## §1 ⚠️ V196 §4 勘误（定义级核对；**你说对了**）

$$\textbf{标准结构分解（逐项）}：\mathbb Z_p^\times\cong\mu_{p-1}\times(1+p\mathbb Z_p)\ \（p\ \text{奇},\ \mu_{p-1}\ \text{阶}\ p-1\text{）};\qquad \mathbb Z_2^\times\cong\mu_2\times\mathbb Z_2$$
$$\qquad\Longrightarrow\ \hat{\mathbb Z}^\times=\prod_p\mathbb Z_p^\times;\qquad \text{挠元的}\ \textbf{正确判据}：\text{各分量挠}\ \textbf{且阶有界}（\text{因元组的阶}\ =\ \mathrm{lcm}\ \text{分量阶}）$$
$$\qquad ⚠️\ \textbf{关键}：\text{判据}\ \textbf{不要求}\ \text{"只有限多分量非平凡"} ⟹ \text{例如}\ x_p=-1\ (\forall p)\ \text{阶}\ 2\ ✓$$
$$\qquad\Longrightarrow\ \boxed{(\hat{\mathbb Z}^\times)[N]=\prod_p\mu_{\gcd(N,p-1)}}\ \text{—— 是}\ \textbf{积}\ \text{而非直和};\ \text{对}\ N\ge2\ \text{为}\ \textbf{无限积}$$
$$\qquad ⚠️\ \text{例}：(\hat{\mathbb Z}^\times)[2]=\mu_2^{\infty}\ \textbf{不可数}、\text{Cantor 型}、\ \textbf{非离散}\ ⟹ \text{挠子群}\ \textbf{不是}\ \text{离散子群} ✗$$
$$\textbf{结论}：\text{V196 §4 的}\ \boxed{\text{"}\hat{\mathbb Z}\ \text{挠}=\bigoplus_p\mu_{p-1}\ \text{且为离散子群} ⟹ \text{刚性前提存在}\text{"}}\ \textbf{撤回} ✓✓$$
$$\qquad ⭐\ \text{但}\ \text{V196 的}\ \textbf{核心结论}\ \text{（四支全落判据 ①／③）}\ \textbf{不依赖} \text{此表述} ⟹ \textbf{不受影响} ✓✓\（\text{唐先生已预判}）$$

---

## §2 ② local boundary：**全链实算**（本档核心）

$$\text{tame symbol}：\partial_v:\ K_2^M(F)\to k(v)^\times,\qquad \partial_v\{a,b\}=(-1)^{v(a)v(b)}\ a^{v(b)}\ b^{-v(a)} \in k(v)^\times$$
$$\text{关键输入}：a+(1-a)=1\ \Longrightarrow\ v(1)=0\ \ge\ \min\bigl(v(a),v(1-a)\bigr)\ \（\text{等号除非两者相等}\bigr）$$
$$\textbf{情形穷尽（五种，无遗漏）}：$$
$$\qquad\text{(i)}\ v(a)=0,\ v(1-a)=n>0：a=1-(1-a)\equiv1\bmod\mathfrak m\ \Longrightarrow\ \partial_v=a^{n}\mapsto 1^{n}=1 ✓$$
$$\qquad\text{(ii)}\ v(1-a)=0,\ v(a)=n>0：1-a\equiv1\bmod\mathfrak m\ \Longrightarrow\ \partial_v=(1-a)^{-n}\mapsto 1 ✓$$
$$\qquad\text{(iii)}\ v(a)=v(1-a)=0：\partial_v=a^{0}(1-a)^{0}=1 ✓$$
$$\qquad\text{(iv)}\ v(a)=v(1-a)=m<0：a=u\pi^{m},\ 1-a=u'\pi^{m},\ u+u'=\pi^{-m}\in\mathfrak m^{|m|}\ \Longrightarrow\ \bar u'=-\bar u$$
$$\qquad\qquad\Longrightarrow\ \partial_v=(-1)^{m^2}\Bigl(\tfrac{u}{u'}\Bigr)^{m}=(-1)^{m}(-1)^{m}=1 ✓$$
$$\qquad\text{(v)}\ m>0\ \textbf{不可能}：\text{否则}\ v(1)\ge m>0 ✗$$
$$\Longrightarrow\ \boxed{\partial_v\{a,1-a\}=1\qquad(\forall\ v\ \text{离散赋值})} ✓✓✓$$
$$\qquad ⭐\ \textbf{结构性原因}：a+(1-a)=1\ \text{强制}\ a\ \text{或}\ 1-a\ \text{为}\ \textbf{主单位}（\equiv1\bmod\mathfrak m\text{）} ⟹ \text{残数恒平凡} ✓✓$$
$$\qquad ⭐\ \textbf{逐层传播}：\text{由}\ a\in1+\mathfrak m\ \text{（或}\ 1-a\in1+\mathfrak m\text{）}，\ \text{迭代边界}\ \text{同样平凡} ⟹ \text{Steinberg 对在}\ \textbf{所有边界层}\ \text{不可见} ✓✓$$

---

## §3 ③ localization：值域审计（逐类区分，**不把 torsion 一律归 Brauer**）

$$\textbf{链}：K_2^M(F)\xrightarrow{\ \partial_v\ }\bigoplus_v k(v)^\times\longrightarrow\cdots$$
$$\qquad ⭐\ \text{对}\ \textbf{Steinberg 对}：\text{由 §2，}\ \textbf{该链无输出}（\text{每一分量皆为}\ 1）⟹ \text{Steinberg 对}\ \textbf{不产生任何局部数据} ✓✓✓$$
$$\qquad\Longrightarrow\ \text{故}\ \text{"Steinberg relation}\to\text{local data}\to\text{global quotient"}\ \text{的中间环节}\ \textbf{为空} ⟹ \text{quotient}\ \textbf{无内容} ✓$$
$$\textbf{一般符号}\ \{a,b\}\（b\ne1-a\text{）}：\text{此时}\ \text{局部数据}\ \textbf{非平凡};\ \text{其离散不变量由经典定理确定：}$$
$$\qquad ⭐\ \textbf{Merkurjev--Suslin}：K_2^M(F)/N\ \cong\ \mathrm{Br}(F)[N]\ \（\text{定理，非假设};\ F\ni\mu_N\text{）}$$
$$\qquad\Longrightarrow\ \text{从}\ K_2\ \text{符号提取的离散不变量，在}\ N\text{-商上}\ \textbf{恰是 Brauer 类} ⟹ \textbf{B 类} ✓✓$$
$$\textbf{其余候选逐项排除}：$$
$$\qquad\mu_N：\text{是}\ \mathrm{Br}[N]\ \text{的局部/取值层，} \textbf{不独立} ⟹ \text{归 B};\qquad \mathrm{Br}[N]：\text{即 B 本身}$$
$$\qquad K_2\ \textbf{未商部分}／K_2/\text{divisible}：\textbf{非离散}（\text{可除／无限秩}）⟹ \text{不满足 V196-4 的离散性要求} ⟹ \textbf{非候选} ✗$$
$$\qquad\Longrightarrow\ \textbf{无第五类出现} ✓$$

---

## §4 ④ $a\leftrightarrow1-a$ 是否产生**新** obstruction

$$\text{设构造得}\ \Omega(a)\ \text{满足}\ \Omega(a)+\Omega(1-a)=0\ \text{或}\ \Omega(a)\Omega(1-a)=1;\qquad \text{问}：\Omega(a)\ \text{是否只是 Steinberg 的另一种表示}？$$
$$\qquad ⚠️\ \text{本档严格限于唐先生允许的链（含}\ \partial_v\ \text{边界型构造）}：\text{由 §2，Steinberg 对的}\ \textbf{所有 tame 边界已平凡}$$
$$\qquad\Longrightarrow\ \text{任何}\ \textbf{由边界构造} \text{的}\ \Omega\ \textbf{必为}\ 0 ⟹ \boxed{\Omega=0}\ ⟹ \textbf{A 类} ✓✓✓$$
$$\qquad ⚠️\ \text{诚实边界}：\text{"非边界型"的}\ a\mapsto1-a\ \text{构造}\ \textbf{不在本条链内}（\text{本档不涉及}）;\ \text{若日后要试，}\ \text{须另立档并显式声明}\ ✓$$

---

## §5 三分判定（✓ 逐条对照唐先生）

$$\boxed{\begin{array}{ll}
\text{A.}\ \Omega=0 & \Longrightarrow\ \text{trivial}\\
\text{B.}\ \Omega\in\mu_N\ \text{或}\ \mathrm{Br}[N] & \Longrightarrow\ \text{经典 torsion}\\
\text{C.}\ \Omega\in D_{\rm new}, & \Longrightarrow\ \textbf{新 obstruction}\\
\end{array}}$$
$$\qquad\textbf{本档落点}：\text{Steinberg 支}\ \Longrightarrow\ \textbf{A}（\Omega=0，\text{§2 结构原因}）✓;\ \text{一般符号支}\ \Longrightarrow\ \textbf{B}（\text{Merkurjev--Suslin}）✓;\ \textbf{C 未出现} ✓✓$$

---

## §6 判词：**Mechanism II 的 canonical arithmetic branch 收口**

$$\textbf{收口链（全部实算过）}：\text{transition}\to\text{cocycle}\to\text{localization}\to\text{obstruction}\ \Longrightarrow\ \text{落点}\ 0/\mu_N/\mathrm{Br}[N] ✓✓✓$$
$$\qquad ⭐\ \text{意义}：\text{这不是}\ \textbf{猜测性死亡};\ \text{而是}\ \text{经}\ \textbf{实际计算} \text{（V196 的过渡/cocycle ＋ V197 的边界/localization）}\ \text{后的}\ \textbf{收口} ✓✓$$
$$\qquad ⚠️\ \text{严格表述}：\text{收口范围}\ =\ \text{"canonical 分支"}（\text{公共对象道路 ＋ 边界型 obstruction}）;\ \textbf{不} \text{声称}\ \text{机制 II 整类死亡} ✓$$

---

## §7 残余与登记（**不给方向**）

$$\text{唯一未被覆盖的形状}：\text{非 tame 边界、非}\ \mathrm{Br}[N]\ \text{的}\ \textbf{离散} \text{不变量}$$
$$\qquad ⚠️\ \text{本轮}\ \textbf{未见实例} ⟹ \text{登记为}\ \textbf{UNINSTANTIATED};\ \textbf{不给方向、不投入、不杀} ✓\（\text{按纪律}）$$

---

## §8 边界与待核

$$\textbf{(a)}\ \text{本档}\ \textbf{未使用}\ \text{被禁符号};\ \text{只走唐先生允许的链} ✓✓$$
$$\textbf{(b)}\ \text{§1 勘误为}\ \textbf{本档自查}，\ \text{由唐先生提示触发};\ \text{标准结构分解为}\ \textbf{经典} ✓✓$$
$$\textbf{(c)}\ \text{§2 的五情形穷尽为}\ \textbf{本档完整推导}（\text{含一个先前算错后被纠正的例子}）✓✓;\ \text{tame symbol 归一化为经典}，\ \text{具体形式}\ \textbf{待核原文} ⚠️$$
$$\textbf{(d)}\ \text{§3 Merkurjev--Suslin 为}\ \textbf{经典定理};\ \text{"由此离散不变量＝Brauer 类"为}\ \textbf{推论} ✓$$
$$\textbf{(e)}\ \text{§6 收口范围严格限定为}\ \textbf{canonical 分支} ✓$$

```
⚠️ §0/§5 链与三分判定为唐先生逐字 ✓✓；本档全程遵守禁令 ✓
⚠️ §1 勘误：撤回 V196 §4 的"ℤ̂^× 挠=⊕μ_{p−1} 且离散"；正确=(ℤ̂^×)[N]=∏μ_gcd(N,p−1)（含不可数 μ_2^∞，非离散）
   ⭐ 并确认：V196 核心结论（四支落①/③）**不依赖**此表述 ✓（唐先生已预判）
⚠️ §2 ∂_v{a,1−a}=1 为【本档完整推导 ✓✓✓】—— 五情形穷尽、含传播性
⚠️ §3 值域审计逐类区分（μ_N／Br[N]／K₂／K₂/divisible／第五类）—— 无第五类
⚠️ §4 结论限于"边界型构造"；非边界型的 a↦1−a 不在本条链内（诚实边界 ✓）
⚠️ §6 收口范围＝canonical 分支，**不**声称机制 II 整类死亡 ✓
⚠️ 未用 RH 等被禁符号 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 定义级勘误确认（你说对了）并撤回 V196 §4 表述 ✓✓；② 全链实算 ⟹ ∂_v{a,1−a}=1（五情形穷尽）✓✓✓；
   ③ 值域审计（无第五类；一般符号＝Brauer 依 Merkurjev–Suslin）✓✓；④ 三分判定落 A ✓✓✓；
   ⑤ Mechanism II canonical branch 收口（实算而非猜测）✓✓✓；⑥ 残余登记 UNINSTANTIATED，不给方向 ✓
```
