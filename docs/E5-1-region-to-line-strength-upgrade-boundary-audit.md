# E5-1 — **region→line 强度升级机制**的边界审计（第一轮）

> 唐先生 2026-09-16 18:07「继续」；入口＝REVIEW-E4-FINAL §7：
> $$\boxed{\text{寻找一种此前未被 V162／V316 覆盖的}\ \textbf{region}\to\textbf{line 强度升级机制}}$$
> 纪律：**先审搜索空间边界，不先列候选**；DEAD 皆为审计范围内结论（N1/N2）。

---

## 1. 升级问题的形式化
$$\textbf{区域型陈述（已知可达）}：\quad \mathrm{N}(\sigma,T)=0\ \ \text{或}\ \ \mathrm{N}(\sigma,T)\ll T^{a(\sigma)}\quad\text{for}\ \sigma\ge 1-\tfrac{c}{\log T}\ \text{型}$$
$$\textbf{线型陈述（目标）}：\quad \mathrm{N}(\sigma,T)=0\ \ \forall\sigma>\tfrac12\ (\Longleftrightarrow\mathrm{RH})，\ \text{或定量型}\ \mathrm{N}(\sigma,T)\ll T^{1-\delta(\sigma)},\ \delta(\sigma)\to1\ (\sigma\to\tfrac12)$$
$$\textbf{升级}＝\text{把边界}\ \sigma_0(T)=1-f(T)\ \text{推向}\ \tfrac12\ \text{（或令}\ \delta\to1\text{）}$$
$$\Longrightarrow\ \text{本档审"有哪些}\ \textbf{类型} \text{的升级机制"，以及它们是否被 V162／V316 或}\ \mathcal A_{\rm old}\ \text{覆盖}$$

## 2. 已知升级机制的类型审计（六型）

### 型 I 定量区改进（zero-free region improvement）
$$\text{de la Vallée Poussin}\to\text{Vinogradov--Korobov 型改进}\to\text{现代记录}$$
$$\textbf{结构性天花板}：\text{该方法的极限形式为}\ \mathrm{Re}\,s>1-\tfrac{c}{\log T}\ \text{型}，\ \textbf{不能到达}\ 1/2；\ \text{此限制是该方法的}\ \textbf{结构性限制}（\text{非技术性）}$$
$$\to\ \textbf{机制天花板型}（\text{与}\ C^\star\ \text{天花板同类）}；\ \text{且其定量输出为}\ \text{计数型}\to\mathcal A_{\rm old}\ (N(\sigma,T))\ ✗$$

### 型 II 矩／相关性升级（moments / correlations）
$$\int|\\zeta|^{2k}\ \text{的渐近}\ (k\ge3\ \text{未知})\ \Longrightarrow\ \text{frontier 仅覆盖}\ X\le T^{2/3-\varepsilon}\ \text{（}\textbf{k=3 缺口）}$$
$$\to\ \textbf{V295 三方合一}（2/3\to1\iff\text{无条件支撑}>1\iff\text{V162 墙}\iff k=3\ \text{缺口）}\ ✗$$

### 型 III 正性升级（positivity）
$$\text{Weil 显式公式判据（二次型}\ge0\iff\mathrm{RH}）\to\ \textbf{循环}（\text{C5／V328 A}_{\rm old}\ \text{的 positivity 项）}✗$$

### 型 IV 谱／算子升级（spectral / trace）
$$\text{Hilbert--Pólya／trace formula}\to\ \text{Deninger／AOB 停滞（G10／6.6）}；\ \text{且}\ \text{spectral re-encoding}\ \text{为 V322 明文排除项}\ ✗$$

### 型 V 有限压缩／变分升级（finite compression / variational）
$$\text{Levinson--Conrey--AF 线法}\ \to\ \textbf{V316 的}\ C^\star\ \text{天花板}：\ \lambda\le1\Rightarrow G\le0.672501；\ \text{越墙须}\ \lambda>1✗$$

### 型 VI 完备化／对偶升级（completion / duality）
$$\text{函数方程对偶}\ \to\ \textbf{E4-1 S1}：\ G\text{-不变条件无}\delta\ \text{符号信息} \Longrightarrow \textbf{无法单侧选线}\ ✗$$

## 3. 归并表
$$\begin{array}{c|c|c}
\text{型} & \text{升级机制} & \text{覆盖}\\ \hline
\mathrm{I}\ \text{定量区改进} & \text{无零区／密度改进} & \text{机制天花板＋计数型（}\mathcal A_{\rm old}\text{）}\\
\mathrm{II}\ \text{矩／相关} & k\ge3\ \text{矩} & \textbf{V295／V162}（k=3 缺口）\\
\mathrm{III}\ \text{正性} & \text{Weil 型二次型} & \textbf{循环}（C5）\\
\mathrm{IV}\ \text{谱／算子} & \text{HP／迹式} & \text{停滞＋V322 排除项}\\
\mathrm{V}\ \text{有限压缩／变分} & \text{AF 线法} & \textbf{V316}\ C^\star\ \text{天花板}\\
\mathrm{VI}\ \text{完备化／对偶} & \text{FE 对偶} & \textbf{E4-1 S1}（无单侧信息）
\end{array}$$
$$\Longrightarrow\ \textbf{六型全数覆盖，未出现第七型}$$

## 4. ⭐ 结构性观察（本档核心，非"又一次全灭"）
$$\text{六型的"天花板"}\ \textbf{不是六个独立障碍}，\text{而是}\ \textbf{同一堵墙的六种语言}：$$
$$\qquad\text{型 I（}\mathrm{Re}\,s>1\ \text{型极限）／型 II（}k=3\ \text{缺口）／型 III（循环）／型 IV（停滞）／型 V（}\lambda>1\text{）／型 VI（双侧性）}$$
$$\qquad\Longrightarrow\ \text{与 STRATEGY-2026-09-16"三副面孔一堵墙"}\ \textbf{一致}\ ✓\ \textbf{[结构判定]}$$
$$\textbf{正面表述（本档新信息）}：\text{region}\to\text{line 升级}\ \textbf{不是"缺少一个聪明技巧"}，$$
$$\qquad\text{而是}\ \boxed{\text{已知升级机制的}\ \textbf{定量天花板} \text{全部与同一个承重量绑定}}$$
$$\textbf{反面警告（纪律）}：\ \textbf{不得} \text{由此写"不存在第七型"}（N1/N2 —— 六型为}\ \textbf{枚举}，\text{非完备分类）}$$

## 5. 由此得到的唯一"非循环目标"（本档的净结论）
$$\text{若要从升级角度继续，唯一}\ \textbf{非循环} \text{的目标是：}$$
$$\boxed{\text{越过 V316}\ C^\star\ \text{的参数条件}\ \lambda>1\ \text{（＝无条件支撑}>1\text{）}}$$
$$\qquad\textbf{措辞纪律（承接 REVIEW-E4-FINAL §4）}：\lambda>1\ \text{须标注为}\ \textbf{当前特定 variational carrier 的越墙条件}，\ \textbf{不得泛化} \text{为"一切 RH 方法皆须}\ \lambda>1\text{"}✓$$
$$\text{而该目标的现状}：\text{V316／V317／V318（二轮）}\ \text{已连续判定其现有来源为 DEAD}；\ \text{故"越过}\ \lambda>1\text{"}\ \textbf{当前同样无已知通道}✓$$

## 6. 判定
$$\textbf{E5-1 结果}：\text{region}\to\text{line 升级的六型机制}\ \textbf{全数覆盖}；\ \textbf{未出现第七型}；$$
$$\qquad\text{且六型天花板}\ \textbf{归并到同一承重量} \Longrightarrow \text{与 E4-FINAL 的结论}\ \textbf{一致}（\text{独立复核}✓）$$
$$\textbf{状态}：\text{本轮}\ \textbf{不宣布 DEAD}（\text{枚举型，N1/N2}）；\ \text{但}\ \textbf{未找到非循环的新升级机制}✓$$

## 7. 边界
$$\text{① 六型划分为}\ \textbf{定义决策}（\text{可修订}）；\ \text{② §4 的"同一堵墙"为}\ \textbf{[结构判定]}；$$
$$\text{③ 各型覆盖引用（V162／V295／V316／E4-1／G10／Deninger 6.6）}\textbf{未逐行重验}；$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}；\quad\text{⑤ 本档}\ \textbf{不引入候选机制}。}$$

## 8. 净产出
$$\text{(i) 升级问题的形式化（区域型／线型／升级的定义）；}$$
$$\text{(ii) 六型升级机制审计（定量区／矩／正性／谱／有限压缩／完备化）——全数覆盖；}$$
$$\text{(iii) ⭐ 结构性观察：六型天花板＝同一堵墙的六种语言（独立复核 E4-FINAL 结论）；}$$
$$\text{(iv) 唯一非循环目标＝}\lambda>1（\text{标注为特定 carrier 条件，不泛化}），\text{且其现有来源已连续判定 DEAD；}$$
$$\text{(v) 明确不宣布 DEAD（枚举型），未找到新的非循环升级机制。}$$
