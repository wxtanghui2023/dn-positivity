# V325 / 丁-1 — **有限算术闭包的传播退化定理审计**（丁-1A ＋ 丁-1B）

> 唐先生 2026-09-16 17:15 拍板。仅做 **丁-1A ＋ 丁-1B**；不碰 RH／$\lambda$／Weil／显式公式。
> 目标命题：$$\text{有限元算术闭包}\ \Longrightarrow\ \delta\ \text{的增长是否必然来自已有的传播机制}$$

---

## 1. 固定闭包系统与 $\delta_T$
$$\mathcal R_T^{(0)}\subseteq\mathcal R_T^{(1)}\subseteq\cdots,\qquad \mathcal R_T^{(k+1)}=\operatorname{Cl}\bigl(\mathcal R_T^{(k)}\bigr)$$
$$\operatorname{Cl}\ \text{每步只允许}\ \textbf{有限次} \text{使用预先固定的算术生成规则}：+,\ \times,\ \text{localization},\ \text{quotient}$$
$$\text{对真新关系}\ r：\quad \delta_T(r)：＝\min\{k:r\in\mathcal R_T^{(k)}\}$$

### 1.0 ⚠️ 先钉死"同阶"的定义（唐先生预警的漏洞）
$$\text{取}\ \operatorname{dist}(r)：＝\textbf{对数尺度} \text{距离（从}\ T_0\ \text{到}\ r\ \text{的尺度所需"倍增"次数）}：\quad \operatorname{dist}\sim\log_2\frac{\operatorname{scale}(r)}{\operatorname{scale}(T_0)}$$
$$\textbf{理由}：\text{若以}\ \textbf{加法尺度差} \text{度量，则连}\ +\text{-闭包都给出}\ \delta\ll\text{dist}，\text{命题在定义层即崩}\ \Longrightarrow\ \text{必须用对数尺度。}$$

---

## 2. 丁-1A：单步影响半径（**按字面为假，且原因具结构性**）

### 2.1 逐步影响半径 $\rho(k)$ 的实际计算
$$\text{设}\ \rho(k)：＝\text{经}\ k\ \text{步闭包可达的最大算术尺度（自}\ T_0\ \text{起）}。$$
$$\textbf{(i) 仅}\ +：\text{取两个最大元相加可翻倍} \Longrightarrow \rho(k)=2^{k}T_0 \Longrightarrow \rho(k)\ \textbf{指数}（\text{非线性}）$$
$$\textbf{(ii) 含}\ \times：\text{取最大元自乘} \Longrightarrow \rho(k)=T_0^{\,2^{k}} \Longrightarrow \rho(k)\ \textbf{双指数}$$
$$\qquad\text{（+，loc，quot 对尺度的影响均} \textbf{不超过倍化}，\text{故}\ \times\ \text{主导）}$$
$$\Longrightarrow\ \boxed{\text{丁-1A 声称的}\ \rho(k)\le Ck+C_0\ \textbf{为假}\ \text{（}\times\text{-闭包下}\ \rho(k)=T_0^{2^k}）}\ ✗$$
$$\textbf{推论}：\text{由}\ \rho(k)\le Ck+C_0\ \text{推出的下界}\ \delta_T(r)\ge c\cdot\operatorname{dist}(r,\mathcal R_{T_0})-O(1)\ \textbf{不成立}\ ✗$$

### 2.2 反向（更值得注意）—— 双指数可达 ⟹ **跨尺度一步生成存在**
$$\rho(k)=T_0^{2^{k}} \Longrightarrow \text{一步即从}\ T_0\ \text{跨到}\ T_0^{2}；\ \text{两步}\ T_0^{4}；\ \text{即}\ \textbf{非局部一次生成能力存在}\ ✓$$
$$\qquad \text{（唐先生预判："只要找到一次这种跨尺度生成现象，丁-1立即出现反例" —— }\textbf{该现象确实存在}）$$
$$\text{但要看清方向}：\text{它给出的是}\ \textbf{捷径}（\delta\ \textbf{小}），\text{而非}\ \textbf{不可约深度}（\delta\ \textbf{大}）\ \Longrightarrow\ \text{见 §4。}$$

## 3. 丁-1B：反向构造（上界成立，但**等价式失败**）
$$\text{上界}：\text{由上尺度计算，}\delta_T(r)=O\bigl(\log_2\operatorname{dist}(r)\bigr)\ (\times\text{-闭包})；\delta_T=O(\operatorname{dist})\ (+ \text{-闭包})\ \Longrightarrow\ \delta_T\le C'\operatorname{dist}+C'_0\ \text{成立}\ ✓$$
$$\text{但等价式}\ \boxed{\delta_T(r)\asymp\operatorname{dist}(r,\mathcal R_{T_0})}\ \textbf{失败}：$$
$$\qquad\times\text{-闭包下}\ \delta_T=\Theta(\log_2\operatorname{dist})\ \textbf{远小于}\ \operatorname{dist}\ ✗$$
$$\Longrightarrow\ \textbf{丁-1B 的结论（$\asymp$）不成立} \Longrightarrow\ \text{按唐先生判据："丁-1B 失败}\Longrightarrow\text{丁-1}\ \textbf{不能判死}"（\text{不做无据判死}）✓$$

## 4. ⭐ 本档主结果：**二分（取代单一的"传播退化"）**
$$\textbf{按闭包是否含乘法，}\delta_T\ \text{落入两行之一}：$$
$$\boxed{\text{Cl}\subseteq\{+,\text{loc},\text{quot}\}：\ \rho(k)=2^{k}T_0 \Longrightarrow \delta_T=\Theta(\operatorname{dist})\ \Longrightarrow \textbf{传播型} \Longrightarrow \text{撞第 2 行}\ (\text{V162/V295})}$$
$$\boxed{\text{Cl}\ni\times：\ \rho(k)=T_0^{2^{k}} \Longrightarrow \delta_T=\Theta(\log_2\operatorname{dist})\ \Longrightarrow \textbf{复杂度型} \Longrightarrow \text{违反 D3.5}\ (\text{证书/算法复杂度})}$$
$$\Longrightarrow\ \text{两种情形的}\ \delta_T\ \textbf{均被吸收}（\text{传播型 或 复杂度型）}\Longrightarrow\ \textbf{E3-A（此族）} = \mathrm{DEAD}$$
$$\qquad\textbf{但关闭理由须更正}：\text{不是 V324 §4.2(丙) 的"与传播同阶"，而是}\ \textbf{二分}（\text{传播型}\ \cup\ \text{复杂度型}）✓$$

### 4.1 为什么"跨尺度一步生成"不构成第五行反例
$$\text{第五行须}\ \delta_T(r_T)\ \textbf{大} \text{且不可被 传播／复杂度／指标 吸收}；$$
$$\qquad \text{而}\ \times\text{-闭包的跨尺度生成给的是}\ \delta_T\ \textbf{小}（\log_2\operatorname{dist}），\text{即}\ \text{把"大尺度"}\ \textbf{快速} \text{缩短为"短推导"}；$$
$$\qquad \text{这说明}\ \delta_T\ \text{只是}\ \textbf{项结构的复杂度度量}（\text{呈现相关}），\text{而非尺度结构量} \Longrightarrow \text{D3.5 违反} \Longrightarrow \mathrm{DEAD}\ ✓$$
$$\Longrightarrow\ \boxed{\text{该现象存在，但不产生第五行实例；它恰好}\ \textbf{把}\ \delta\ \text{压进复杂度类}}$$

## 5. 丁-1C（排除隐藏重命名）—— 未达（A 已失败），但结论已由 §4 给出
$$\text{由 §4，}\delta_T\in\{\text{传播型},\ \text{复杂度型}\}\ \text{两者皆在 D3.4／D3.5 排除表内} \Longrightarrow \text{无需再走 C 即已归旧}\ ✓$$

## 6. 【勘误 T10】对 V324 §4.2(丙) 的更正
$$\textbf{V324 §4.2(丙) 原述}："\text{对算术闭包操作}\ (+,\times,\text{局部化},\text{商化})，\delta_T\ \textbf{与传播／支撑扩散不可分离}\ \Longrightarrow\ \text{撞第 2 行}"$$
$$\textbf{更正}：\text{该断言}\ \textbf{对含}\ \times\ \text{的闭包为假} —— \times\ \text{使}\ \rho(k)\ \text{双指数增长}，\text{故}\ \delta_T=\Theta(\log_2\operatorname{dist})\ \textbf{远小于} \text{传播距离}；$$
$$\qquad \text{正确表述＝}\textbf{§4 的二分}：\text{不含}\times\Rightarrow\text{传播型（第 2 行）}；\text{含}\times\Rightarrow\text{复杂度型（D3.5）}。$$
$$\qquad\textbf{DEAD 的结论不变}，\text{但}\ \textbf{关闭理由被更正} \Longrightarrow \text{V324 的 DEAD 依据需以本档 §4 替换。}$$

## 7. 判定（按唐先生硬标准）
$$\text{唐氏二分标准}：\text{(i)}\ A+B+C\Rightarrow\mathrm{DEAD}；\ \text{(ii)}\ \exists r_T\ \text{不可吸收}\Rightarrow\text{第五行实例。}$$
$$\text{本档实际结果}：\text{丁-1A}\ \text{按字面}\ \textbf{为假}（\rho(k)\ \text{非线性}）；\text{丁-1B}\ \text{等价式}\ \textbf{失败}；$$
$$\qquad\textbf{但}\ \text{（§4）给出更强形式的结论}：\delta_T\ \textbf{必落传播型或复杂度型} \Longrightarrow \textbf{E3-A（有限算术闭包族）DEAD}；$$
$$\qquad \text{第五行}\ \textbf{仍无实例}；\ \exists\ \text{跨尺度一步生成（§2.2）}\ \text{但被 D3.5 吸收（§4.1）。}$$

## 8. 边界（N1/N2 严守）
$$\text{① §2 的}\ \rho(k)\ \text{计算为}\ \textbf{初等计算}（\text{本档完成，未跑 Lean}）；\ \text{② §4 的"吸收"为}\ \textbf{[结构判定]}；$$
$$\text{③ §1.0 的 dist 定义选择为}\ \textbf{定义决策}（\text{若以加法尺度差度量，}\delta\ll\mathrm{dist}\ \text{在}\ +\text{-闭包即发生，命题在定义层崩）；}$$
$$\text{④ V162／V295 引用为档案既有结论，未逐行重验；}\quad\text{⑤ }\textbf{未用 RH}；零数值（仅初等计数）；未跑 Lean。}$$

## 9. 净产出
$$\text{(i) 丁-1A}\ \textbf{按字面为假}，\text{给出}\ \rho(k)\ \text{的实际形态（}\times\text{-闭包双指数）；}$$
$$\text{(ii) 丁-1B 上界成立但}\ \asymp\ \textbf{失败}；$$
$$\text{(iii) ⭐ 更强结果：}\textbf{二分}（传播型 ／ 复杂度型）\ \text{覆盖全部有限算术闭包} \Longrightarrow \textbf{E3-A（此族）DEAD}；$$
$$\text{(iv) }\textbf{跨尺度一步生成确实存在}（\text{唐先生预判命中）}\ \text{但被 D3.5 吸收，}\textbf{不构成第五行实例}；$$
$$\text{(v) 【勘误 T10】更正 V324 §4.2(丙) 的关闭理由（DEAD 不变，依据替换为 §4 二分）。}$$
