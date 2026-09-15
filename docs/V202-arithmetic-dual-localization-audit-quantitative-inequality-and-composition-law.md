# V202 · **Arithmetic Dual-Localization Audit**（第一档：只做定量不等式与复合律）—— ① ⭐ Canonical 对 I（区间／模 $M$ × 小素数模式）：**CRT／筛独立 ⟹ 计数因子化 ⟹ 只有平凡界 ⟹ $\Delta=0$** ✓✓；② ⭐⭐ Canonical 对 II（区间 × 小分母频率／Farey）：**大筛法有效区间 $Q\gtrsim\sqrt N$ 与 FUP 需稀疏 $|\Omega|\ll N$（$Q\ll\sqrt N$）恰好相反，二者在 $Q=\sqrt N$ 相切且同时临界 ⟹ 缺陷消失** ✓✓✓；③ FUP 复合律的四个结构前提逐条对照（**嵌套 ✓／变换互换 ✗／乘积律 ✗／严格缺陷 ✗**）⟹ **放大引擎在 canonical 算术对上无法启动**；④ 判词：**canonical 算术对偶局域化 DEAD**（两种独立原因），**第二阶段按指示不进入** ✓

> 委托 ✓ 唐先生 2026-09-15 13:50：**"V200 的收口不是'研究结束'，而是说明 A1/A3 这条生成器已经耗尽；下一步必须重新找一个不同的数学/物理模型。"** 新模型 ＝ **Dual-localization defect amplification**；**"我建议直接开 V201，而且第一步就算，不再做概念讨论：先求 additive/multiplicative 双局域化的精确定量不等式及其跨尺度复合律。"** ＋ **第一关（残酷）**：若 $B_{\rm mult}(S)$ 仅由 $\prod_{p\le y}(1-1/p)$ 控制（sieve density）⟹ 死；若加法侧只是 Fourier uncertainty $|\operatorname{supp}f||\operatorname{supp}\hat f|\ge N$ ⟹ 死；要的是第三种：**加法尺度 × 乘法尺度 × 非因子化缺陷** ＋ **最终测试**：若 $\Delta_k>0$ 且 $\Delta_{k+\ell}\ge1-(1-\Delta_k)(1-\Delta_\ell)$ ⟹ $\Delta_{mk}\to1$ 指数逼近 ＋ **"如果第一阶段本身都做不出来，直接关闭，不碰 RH。"**
> ⚠️ 编号说明：**`V201` 已被 A1／A3 Restart Gate 占用** ⟹ 本档为 **V202** ✓
> 查图 ✓ `V199`／`V200`（锥源；**本档不复用其判据**）｜`V198`（机制 II 门；**本档不回**）
> 执行 ✓ 小灵（**§3 因子化、§4 相反区间、§6 四前提对照 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V202**

---

## §1 精确设置（对象、算子、缺陷、复合律）

$$A_N=\{1,\dots,N\};\qquad \text{加法坐标}\ L_{\rm add}(n)\（\text{如}\ n\bmod M\ \text{或二进制位}\bigr);\qquad \text{乘法坐标}\ L_{\rm mult}(n)=(\mathbf 1_{p\mid n})_{p\le y}$$
$$\text{对}\ S\subseteq A_N：\ B_{\rm add}(S):=\bigl|\{L_{\rm add}(n):n\in S\}\bigr|,\qquad B_{\rm mult}(S):=\bigl|\{L_{\rm mult}(n):n\in S\}\bigr| ✓$$
$$\textbf{算子化（为写复合律；与 FUP 对齐）}：\ \mathcal F=\text{单位 DFT};\ P_I=\text{位置侧截断};\ P_\Omega=\text{频率侧截断}（\text{小分母集合}\ \Omega_Q）$$
$$\qquad T(N,Q):=P_{\Omega_Q}\,\mathcal F\,P_{I_N};\qquad r(N,Q):=\|T(N,Q)\|;\qquad r^{\rm triv}=1\ \（\text{单位化下平凡界}\bigr）✓$$
$$\textbf{缺陷}：\ \Delta:=1-r/r^{\rm triv}=1-r\ge0;\qquad \textbf{目标}：\ \exists k:\ r_k<1\（\text{严格缺陷}\bigr)\ \text{且}\ r_{k+\ell}\le r_kr_\ell ✓$$

---

## §2 复合律的等价形式（**先把要求写准**）

$$\text{唐先生的律}：\Delta_{k+\ell}\ge1-(1-\Delta_k)(1-\Delta_\ell)\quad\Longleftrightarrow\quad \boxed{\rho_{k+\ell}\le\rho_k\rho_\ell}\ \ \text{其中}\ \rho:=1-\Delta=r ✓✓$$
$$\Longrightarrow\ \text{即}\ \textbf{FUP 型次可乘性};\qquad \text{若某尺度}\ r_{k_0}<1\ \text{严格} ⟹ r_{mk_0}\le r_{k_0}^m\ \textbf{指数趋零} ✓$$
$$\qquad ⚠️\ \textbf{关键警告}：\text{次可乘性}\ \textbf{本身不产生放大} —— \text{若}\ r\equiv1（\text{各尺度均无严格缺陷}），\text{律}\ \textbf{恒取等且空洞} ✓✓$$
$$\qquad\Longrightarrow\ \textbf{第一要件}：\text{某个尺度存在}\ r<1\ \textbf{严格缺陷};\ \text{否则引擎}\ \textbf{无输入} ✓✓✓$$

---

## §3 Canonical 对 I：加法 = $n\bmod M$；乘法 = 小素数模式 —— **因子化 ⟹ $\Delta=0$**

$$\text{固定}\ M\ \text{与}\ y,\ \text{取}\ (M,\textstyle\prod_{p\le y}p)=1。\ \text{模式}\ P\subseteq\{p\le y\};\ \text{计数}：$$
$$\qquad \#\{n\le N:\ n\equiv r\bmod M,\ \mathbf 1_{p\mid n}=P\}\ \approx\ \frac NM\cdot\prod_{p\in P}\frac1p\prod_{q\le y,\ q\notin P}\Bigl(1-\frac1q\Bigr) ✓$$
$$\qquad ⭐\ \textbf{右端完全因子化}：\bigl(\text{加法因子}\ \tfrac1M\bigr)\times\bigl(\text{乘法因子（筛密度）}\bigr)，\ \textbf{无交叉项} ✓✓$$
$$\qquad\Longrightarrow\ \text{联合支撑}\ =\ (\text{加法可取值})\times(\text{乘法可取值})\ \textbf{直积};\ \text{全部对}\ (r,P)\ \text{可实现} \iff N\gtrsim M\,e^{\theta(y)}=M\,e^{\,y} ✓$$
$$\Longrightarrow\ \boxed{\ \Delta_{\rm I}=0\ }:\ \text{仅有}\ \textbf{平凡计数界}\ B_{\rm add}B_{\rm mult}\ge|S|\ \text{（每纤维}\ge1\ \text{元）} ✓✓$$
$$\qquad ⚠️\ \text{按唐先生第一关}：\text{该对}\ \textbf{只是筛密度＋平凡计数} ⟹ \textbf{杀} ✓✓✓$$

---

## §4 ⭐⭐ Canonical 对 II：加法 = 区间；乘法 = 小分母频率（Farey）—— **相反区间 ⟹ 缺陷消失**

$$\text{取}\ \Omega_Q:=\{a/q:\ q\le Q,\ (a,q)=1\}\（\text{个数}\ |\Omega_Q|\asymp Q^2\bigr）。\ \textbf{大筛法}：$$
$$\qquad \sum_{\omega\in\Omega_Q}\bigl|\hat a(\omega)\bigr|^2\ \le\ (N+Q^2)\sum_{n\le N}|a_n|^2\ \ \Longrightarrow\ \textbf{节省因子}\ =\ \frac{N}{N+Q^2}\ \Longrightarrow\ \boxed{\ r(N,Q)\lesssim\sqrt{1+\frac{Q^2}{N}}\ \text{的}\textbf{倒数}\ \text{形式}\ \text{即}\ r\ \text{的界由}\ \tfrac{N}{N+Q^2}\ \text{控制}} ✓$$
$$\qquad ⚠️\ \text{精确归一化与常数}\ \textbf{待核};\ \text{但}\ \textbf{临界尺度}\ Q\asymp\sqrt N\ \text{是标准的} ✓$$

$$\textbf{⭐⭐ 相反区间（本档核心）}：$$
$$\qquad \text{(i)}\ \text{大筛法}\ \textbf{有内容} \iff \frac{N}{N+Q^2}\ \text{显著}<1 \iff Q\gtrsim\sqrt N;\qquad \text{此时}\ |\Omega_Q|\asymp Q^2\gtrsim N\ \（\textbf{频率集不再稀疏}）$$
$$\qquad \text{(ii)}\ \text{FUP 型}\ \textbf{严格节省} \text{需要}\ \textbf{正余维}：\ |\Omega_Q|\ll N\ \（\text{稀疏}\bigr) \iff Q\ll\sqrt N$$
$$\qquad\Longrightarrow\ \boxed{\text{两个机制的有效区间}\ \textbf{恰好相反}，\text{且仅在}\ Q=\sqrt N\ \textbf{相切}};\ \text{在该点}\ |\Omega_Q|\asymp N\ \（\text{满维、临界}\bigr) \Longrightarrow\ \text{节省}\to0,\ \text{缺陷}\to0 ✓✓✓$$
$$\qquad ⚠️\ \text{补充：区间}\ [1,N]\ \text{与 Farey 集}\ \Omega_Q\ \text{在各自尺度上都是}\ \textbf{满维}（\text{临界}\bigr），\ \text{不满足 FUP 所需的维数亏缺} ✓✓$$
$$\Longrightarrow\ \boxed{\ \Delta_{\rm II}=0\ \ \text{（无严格缺陷）}\ }\ ⟹ \textbf{引擎无输入} ✓✓✓$$

---

## §5 第三种候选：有限群 DFT × 乘法特征变换

$$\text{纯加法侧（NTT／Donoho--Stark 型）}：|\operatorname{supp}f|+|\operatorname{supp}\hat f|\ge q+1\ \text{（}\mathbb Z/q,\ q\ \text{素数）}$$
$$\qquad ⚠️\ \text{这是}\ \textbf{additive-only} \text{的不确定性原理} ⟹ \textbf{不含乘法坐标} ⟹ \text{不足以构成"对偶局域化"} ✓✓$$
$$\text{真正的对偶候选}：\text{同一}\ f:\mathbb Z/q\to\mathbb C\ \text{上}\ \textbf{两个不同变换}：\text{加法 DFT}\ \ \text{vs}\ \ \text{乘法特征变换}\（(\mathbb Z/q)^\times\to\mathbb C^\times\bigr）✓$$
$$\qquad ⚠️\ \text{该方向}\ \textbf{确有已知结果}（\text{加法}×\text{乘法不确定性}）⟹ \text{均为}\ \textbf{已知定理} ⟹ \text{按}\ \text{`V201`}\ \S1(2)\ \textbf{不产生新的无条件输入} ✓$$
$$\qquad ⚠️\ \text{且其}\ \textbf{是否跨尺度放大}\ \text{未解} ⟹ \text{不得据此开第二阶段} ✓$$

---

## §6 ⭐ FUP 复合律的**四个结构前提**：逐条对照算术对

$$\text{在 FUP 中}\ r_{k+\ell}\le r_kr_\ell\ \text{之所以成立，依赖}：$$
$$\textbf{(i) 嵌套族}：C_{A,k+\ell}\subseteq C_{A,k};\ C_{B,k+\ell}\subseteq C_{B,k} —— \text{算术侧}\ \textbf{满足} ✓\（\text{区间与频率截断随尺度单调}\bigr）$$
$$\textbf{(ii) 变换把两族互换}：\text{使}\ P_{B,k_2}\mathcal F P_{A,k_1}\ \text{可归约为同型算子} —— \text{算术侧}\ \textbf{不满足} ✗\（\text{区间}\leftrightarrow\text{小分母频率在 DFT 下}\textbf{不互换}\bigr）$$
$$\textbf{(iii) 乘积律}：T_{k+\ell}=T_kT_\ell —— \text{算术侧}\ \textbf{不满足} ✗\（\text{缺 (ii) 即无乘积律}\bigr）$$
$$\textbf{(iv) 某尺度严格缺陷}：r_{k_0}<1 —— \text{算术侧}\ \textbf{不满足} ✗\（\S3／\S4\ \text{均得}\ \Delta=0\bigr）$$
$$\Longrightarrow\ \boxed{\text{四前提中算术侧只满足 (i)};\ \text{放大引擎}\ \textbf{无法启动}} ✓✓✓$$
$$\qquad ⚠️\ \text{本结论}\ \textbf{不} \text{来自四类锥源、}\textbf{不} \text{来自}\ \text{`V198` 门} —— \text{它是}\ \textbf{双局域化模型内部} \text{的}\ \textbf{几何／临界性} \text{型障碍} ✓✓✓$$

---

## §7 Granville–Soundararajan 的诚实定位

$$\text{G--S（Annals 2007）：}\text{真}\ \textbf{算术不确定性原理}（\text{序列不能同时在短区间与算术级数中过度均匀}\bigr) ✓✓$$
$$\qquad ⚠️\ \text{但 (a)}\ \text{它}\ \textbf{是已证定理} ⟹ \text{按}\ \text{`V201`}\ \S1(2)\ \textbf{不产生新的无条件输入} ✓$$
$$\qquad ⚠️\ \text{(b) 其形式是"双边均匀 ⟹ 受限"，阈值仍在}\ \sqrt N\（\textbf{尺度不变}\bigr） ⟹ \textbf{不提供放大} ✓✓$$
$$\qquad ⚠️\ \text{(c) 故正确的定位}：\text{它是}\ \textbf{已知语料} \text{的一员};\ \text{若本模型只是"引用它"，则}\ \text{`V201`}\ \S1(2)\ \text{立即判死} ✓$$

---

## §8 判词

$$\boxed{\ \textbf{Canonical 算术对偶局域化：DEAD（}\Delta=0\ \text{／无严格缺陷）}\ } ✓✓✓$$
$$\qquad \textbf{两个独立原因}：\text{(I) canonical 对 I}\ \textbf{因子化}（\text{CRT／筛独立}\bigr) ⟹ \text{只有平凡界};\ \text{(II) canonical 对 II}\ \textbf{相反区间＋满维临界} ⟹ \text{节省与稀疏不可兼得} ✓✓$$
$$\qquad \textbf{第二阶段（}\to\zeta／L\text{-函数谱排除）按唐先生指示}\ \textbf{不进入} ✓✓✓$$
$$\qquad ⚠️\ \text{范围严格限定}：\textbf{canonical 对};\ \textbf{不} \text{声称"对偶局域化模型不可能"} ✓$$

---

## §9 门：若要重开本模型（四条件；缺一不可）

$$\boxed{(1)\ \text{正余维}：\text{两侧集合}\ \textbf{都}\ \text{稀疏}（|\Omega|\ll N\ \text{且}\ |I|\ll N）;\quad (2)\ \textbf{嵌套};\quad (3)\ \textbf{变换互换}（\text{存在变换}\mathcal T\ \text{把两族互换}）;\quad (4)\ \textbf{乘积律}\ T_{k+\ell}=T_kT_\ell}$$
$$\qquad ⚠️\ \text{且须}\ \textbf{产生一条定量不等式}，\text{它}\ \textbf{不} \text{是}\ \text{G--S／大筛法／NTT 不确定性已给出的} ✓$$
$$\qquad ⚠️\ \text{按}\ \S4：\text{条件 (1) 与"大筛法有内容"}\ \textbf{互斥} ⟹ \text{若候选仍在大筛法框架内},\ \textbf{立即判死} ✓$$

---

## §10 边界与待核

$$\textbf{(a)}\ \text{§1 算子化与}\ r\ \text{定义为}\ \textbf{本档构造}（\text{为写复合律}）;\ \text{与 FUP 原文的对应关系}\ \textbf{待核} ⚠️$$
$$\textbf{(b)}\ \text{§4 的节省因子}\ \frac{N}{N+Q^2}\ \text{与临界尺度}\ Q\asymp\sqrt N\ \text{为}\ \textbf{大筛法标准形};\ \textbf{精确归一化／常数}\ \textbf{待核} ⚠️$$
$$\textbf{(c)}\ \text{§4 的"相反区间"论证为}\ \textbf{本档核心推导} ✓✓✓;\ \text{FUP 需正余维为}\ \textbf{标准事实}（\text{Bourgain--Dyatlov 型}）⚠️\ \textbf{待核原文} ✓$$
$$\textbf{(d)}\ \text{§5 的 additive×multiplicative 已知结果为}\ \textbf{外部}，\textbf{本档未逐篇核} ⚠️$$
$$\textbf{(e)}\ \text{§7 对 G--S 的定位为}\ \textbf{本档判断};\ \text{其}\ \textbf{是否可跨尺度复合}\ \textbf{未证} ⚠️$$

```
⚠️ §0 委托与"第一步就算"为唐先生逐字 ✓✓；编号说明（V201 已被门占用 ⟹ 本档 V202）✓
⚠️ §2 复合律等价形式（ρ_{k+ℓ} ≤ ρ_kρ_ℓ ＝ FUP 次可乘性）为【本档形式化 ✓✓】；并指出次可乘性本身不产生放大 ✓✓✓
⚠️ §3 canonical 对 I 的因子化为【本档实算 ✓✓✓】⟹ 按唐先生第一关**杀**
⚠️ §4 canonical 对 II 的"相反区间＋满维临界"为【本档核心推导 ✓✓✓】⟹ Δ=0
⚠️ §6 四前提逐条对照为【本档核心 ✓✓✓】：算术侧只满足嵌套；缺变换互换／乘积律／严格缺陷
⚠️ §7 G--S 定位：已证定理 ⟹ 无新无条件输入 ＋ 阈值 √N 尺度不变 ⟹ 不放大 ✓✓
⚠️ §8 判词范围严格＝canonical 对；第二阶段不进入 ✓✓✓
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 设置与复合律形式化 ✓✓；② 两 canonical 对均 Δ=0（因子化／相反区间）✓✓✓；
   ③ FUP 四前提对照（只满足嵌套）✓✓✓；④ 新障碍类型＝几何-临界性（非四类锥源、非 V198 门）✓✓✓；
   ⑤ 重开四条件门 ✓；⑥ G--S 诚实定位 ✓
```
