# V316 **FREEZE（BASELINE）** ＋ **C⋆ 墙「必要条件来源审计」**

> 冻结时间：2026-09-16 16:51（唐先生判定）
> 形式化资产：`~/lean-repro/zeta23-local/V316_kernel_bound.lean` = **60 条声明，ERROR_COUNT = 0**（零 sorry／零 axiom／未用 RH）

---

## Part I — V316 冻结（CLOSED / BASELINE）

### ① 完整链（全部机器化）
$$\boxed{\text{kernel bound}\Longrightarrow\text{coercivity}\Longrightarrow\text{E--L stationarity}\Longrightarrow\text{quadratic gap}\Longrightarrow\text{equality case}\Longrightarrow u=v_\lambda\ \text{a.e.}}$$

| 段 | 内容 | 声明数 |
|---|---|---|
| V316-A | `bilin_le` … `schur_L2`／`kernel_bound`／`Q_pos_alg`／`Q_pos`／接线 | 15 |
| V316-B | `vtheta`／`vStarAffineConst`／`vStarELConst`／`cos_integral`／`KvStar_left/right`／`KvStar_abs_split`／`KvStar_affine_general`／`KvStar_affine`／`vStar_EL` | 14 |
| V316-C ②③ | `Qfun`（Irest 层）／`Bfun`／`pol_pointwise(_kernel)`／`Bfun_symm`／`Bfun_polarization`／`Bfun_quadratic_gap` | 7 |
| V316-C ④ | `kernel_hv_integrable`／`kernel_hv_prod_integrable`／`integrable_of_continuousOn_Icc'`／`integrable_cos_Irest`／`mul_prod_integrable`／`kernel_domination`／`integrable_h_mul_cos`／`integrable_const_mul_h`／`integrable_h_mul_kernel_int`／`intervalIntegral_eq_integral_Irest`／`nested_eq_prod_integral`／`prod_integral_eq_Bfun`／`vStar_EL_ae`／`weak_EL`／`weak_EL_constrained` | 15 |
| V316-C ⑤ | `sq_diff_Irest`／`Qfun_diff`／`Qfun_diff_constrained`／`Qfun_global_gap` | 4 |
| V316-C ⑥ | `integral_sq_eq_zero_of_min`／`sq_eq_zero_ae`／`sub_eq_zero_ae`／`minimizer_uniqueness_ae` | 4 |

### ② 唯一性未越级
$$\text{level-1}\ \int h^{2}=0\ \longrightarrow\ \text{level-2}\ h^{2}=^{\text{a.e.}}0\ \longrightarrow\ \text{level-3}\ h=^{\text{a.e.}}0$$
**点态等式、a.e. 等式、$L^2$ 等式三层严格分离**（⑥-1／⑥-2／⑥-3 各自独立成 theorem）✓

### ③ 明确**未**做到（冻结时必须写明）
$$\text{(a)}\ \textbf{未证 RH}，也\textbf{未新增}任何 RH 等价命题；$$
$$\text{(b)}\ u\ \text{的可容许窗口类}\ \textbf{人为限定} \Longrightarrow \text{唯一极小是}\ \textbf{该泛函内}的唯一性，\textbf{不是}\ \zeta\ \text{的唯一性}；$$
$$\text{(c)}\ c^{*}_{\lambda}\ \text{依赖 CCLM17 Cor.14 最优性（}\textbf{外部引用，未自证}）；$$
$$\text{(d)}\ \lambda>1\ \text{是}\textbf{必要条件}，且}\ \lambda>1\ \text{恰是 FSC/MV 无条件支撑墙（V162／V181）；}$$
$$\text{(e)}\ \text{与 RH 的 bridge（正性}\iff\text{RH）}\ \textbf{仍是 POS1/POS2 循环}。$$
$$\Longrightarrow\ \text{V316 = 变分层形式化}\ +\ \text{量化天花板定位}\ \in\ \text{"理解／工具"资产，}\textbf{不得表述为 RH 进展}。$$

### ④ V316 的真正用途：**反向诊断器**（筛选未来机制）
$$\text{任何候选桥接机制}\ M：\text{若只证}\ M\Rightarrow\lambda\le1,\ \text{或只在}\ \lambda\le1\ \text{窗口内改善常数}\ \Longrightarrow\ \textbf{无法承担突破任务}\ \text{(淘汰)}$$

---

## Part II — C⋆ 墙「必要条件来源审计」

### ⑤ 问题（唯一形式，唐先生 16:51 指定）
$$\boxed{\text{Can the arithmetic source force }\lambda>1\ \text{without assuming RH-equivalent positivity?}}$$

$$\text{已知量化压力（V316-B／V303–V309）：}\quad \lambda\le1\ \Longrightarrow\ G\le2-\frac{1}{c^{*}_{1}}=0.672501\ldots$$
$$\text{族内上限：}\ G\ \le\ 2-\frac{\pi}{2\sqrt2}=0.889280\ <\ 1\ \text{（}\lambda\to(\pi/\sqrt2)^{-}\text{）}$$

### ⑥ 独立性筛选条件（forcing 机制必须**独立于**下列全部）
$$\textbf{(i)}\ \text{RH；}\ \textbf{(ii)}\ \text{Weil positivity；}\ \textbf{(iii)}\ \text{POS1/POS2；}\ \textbf{(iv)}\ \text{已知显式公式通道；}$$
$$\textbf{(v)}\ \text{FSC/MV 本身（不得直接假设支撑}>1\text{）；}\ \textbf{(vi)}\ \text{仅重新编码}\ Q_\lambda\ \text{的谱正性；}\ \textbf{(vii)}\ \text{Robin 型见证（V150 W2／E4 §2）}。$$

### ⑦ 候选来源逐一审计
$$\textbf{S1 高阶矩／高相关（}k\ge3\text{）：}\ \text{V294-A 已证}\ \textbf{有限阶局部核的聚合增益}\ G(K)\le0 \Longrightarrow\ \text{不产生新尺度}\ ✗$$
$$\qquad \text{frontier 对齐：}k{=}3\ \text{对角法仅覆盖}\ X\le T^{2/3-\varepsilon}\ \text{，差}\ T^{1/3}\ \text{（V283／A3-third-moment-barrier）⟹ 同址，且非原理性不可能}$$
$$\textbf{S2 零密度／无零区：}\ \text{de la Vallée Poussin 型（V287-B）}\Longrightarrow\ \text{给的是}\ \lambda\le1\ \text{型输入；GRH 型更强输入}\ \in\ \text{循环}\ ✗$$
$$\textbf{S3 值面／显式公式：}\ \text{V283 §1}\ \text{（argument principle ⟹ 计数本性属值面）＋ V258（全局碰撞全在值面）}\Longrightarrow\ \text{是既有通道，}\textbf{不产生无条件支撑}>1\ ✗$$
$$\textbf{S4 算子论／AF 有限压缩：}\ \text{V295 已证}\ 2/3\ \text{损失全在}\ c^{\text{geom}}_{\phi}\ \text{（窗口几何），压缩率}\to1\text{；}$$
$$\qquad \textbf{三方合一}：2/3\to1\iff\text{无条件支撑}>1\iff\text{V162 墙}\iff k{=}3\ \text{缺口}\ ✗$$
$$\textbf{S5 第三类正性（非自对偶锥）：}\ \text{V247/V248（存在性 OK）}\to\text{V267 三情形审计}\Longrightarrow\text{无已知实例（}\textbf{同一堵墙的锥语言）}\ ✗$$
$$\textbf{S6 非柱／非有限阶谓词：}\ \text{V269–V271}\Longrightarrow\ \text{证书必为柱型；非柱不给有限证书；常数／自指型回}\ \text{V270-A}\ ✗$$
$$\textbf{S7 算术一致性／非交换闭包：}\ \text{V284 五族全败 ＋ (III)}\perp\text{(V) 原理级互斥；S-line 由 V177/V181 封}\ ✗$$
$$\textbf{S8 轨道不变量：}\ \text{V280（词-字符 span）}\Longrightarrow\ k{=}1\ \text{落}\ \zeta\text{-local}\to L1\text{；}k\ge2\ \text{落相关预算墙}\ ✗$$

### ⑧ 审计结论
$$\textbf{在已审计范围内：不存在已知的、独立的算术机制能迫使}\ \lambda>1。$$
$$\text{四条独立语言在同一处汇合：无条件支撑}>1\ \text{（MV）}\ =\ \text{V162 墙}\ =\ k{=}3\ \text{缺口}\ =\ c^{\text{geom}}\to1\ \text{的带宽需求。}$$
$$\Longrightarrow\ \textbf{C⋆ 墙（必要条件来源）：DEAD（已审计范围）}。$$
$$\text{DEAD 的含义（严格）：}"\text{要求目标量}\ >0.672501\ \text{的机制必须提供无条件支撑}>1\text{"——这是}\ \textbf{必要条件}，\text{不是充分条件。}$$
$$\text{故 DEAD} = "\text{任何}\ \lambda\le1\ \text{型机制被排除}"，\textbf{不等于} "\text{RH 不可能}"。$$

### ⑨ 重建准则（reopen criteria，须逐条满足才重开）
$$\textbf{R1：}\ \text{给出一个\textbf{非}显式公式通道的算术恒等式／不等式，其在}\ X\asymp T\ \text{尺度无条件成立；}$$
$$\textbf{R2：}\ \text{该对象的系数不在 V294-A 的有限阶局部核类内（即非有限阶、或非局部）；}$$
$$\textbf{R3：}\ \text{其谱侧敏感量}\ \textbf{不经过}\ N(\sigma,T)\ \text{型计数（V283）且非值面；}$$
$$\textbf{R4：}\ \text{与 RH/Weil/POS 的独立性可验证（不是重编码）；}$$
$$\textbf{R5：}\ \text{若成立，必须给出}\ \lambda>1\ \text{的\textbf{定量}推论（如支撑}>\sigma_0>1\text{）。}$$

### ⑩ 边界标注（N1/N2 遵守）
$$\text{① 本审计是}\ \textbf{枚举型}，\text{不得升级为"}\lambda>1\ \text{不可能"；}\quad\text{② "未找到"}\ne\text{"不存在"；}$$
$$\text{③ §7 各条的等级：S1／S4／S8 为已 CLOSED 命题（V294-A／V295／V280）；S2／S3／S5／S6／S7 为已审计族内结论；}$$
$$\text{④ 全档未用 RH；零数值（除既有闭式常数）。}$$
