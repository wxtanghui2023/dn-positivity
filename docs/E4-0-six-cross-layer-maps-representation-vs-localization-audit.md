# E4-0 首份实质产物 — **六类跨层映射的「表示能力 vs 谱定位能力」逐项硬审计**

> 唐先生 2026-09-16 17:50「继续」；按 E4-0 章程 §9 三步骤执行。
> **本档不是候选机制清单**；只做审计。

---

## 第一步：把"定位"写成可检验命题（先定义，不先提机制）

### 1.1 三层能力（严格区分）
$$\textbf{(R) 表示型}：\text{存在映射}\ \Phi:\mathscr A\to\mathscr S_\infty,\ a\mapsto F_a(t)\ (\text{谱分布／函数})$$
$$\textbf{(L) 定位型}：\exists\ \text{可容许类}\ \mathscr A_{\rm adm}\subseteq\mathscr A\ \text{与}\ \textbf{被迫区域}\ \Omega\subseteq\mathbb R\ (\text{谱轴})，\text{使}$$
$$\qquad\boxed{\forall a\in\mathscr A_{\rm adm}:\ \operatorname{supp/spectrum}(F_a)\subseteq\Omega}\quad(\textbf{只依赖可容许性，不依赖}\ a\ \text{的偶然取值})$$
$$\textbf{(L}^\star\text{) RH 相关型（目标）}：\text{被迫区域}\ \textbf{即临界线本身}（\text{或收缩到它的邻域}），\text{即}\ \Omega=\{1/2\}\ \text{型}$$

### 1.2 关键判别式（本档用）
$$\Phi\ \text{具定位能力的判据}：\text{存在}\ \Omega\ \textit{真包含于}\ \text{平凡可达区域}，\text{且其被迫性}\ \textbf{不依赖 RH}、\textbf{不依赖}\ a\ \text{的具体选择}$$
$$\text{若}\ \Phi\ \text{只满足 (R)}\ \Longrightarrow\ \text{仅}\ \text{representation}；\ \text{若另有 (L) 但}\ \Omega\ne\{1/2\}\ \text{型}\ \Longrightarrow\ \text{部分定位（须记型）}$$

---

## 第二步：逐项审计六类 $\Phi$

### Φ1 Euler／Mellin
$$\text{输入}\ \text{算术数据}\ (a_n,\ \text{局部因子})\ \to\ \text{Dirichlet 级数／Mellin 像}\ (\text{s-平面上的对象})$$
$$\textbf{(R)}\ ✓\ \text{（识别／编码：级数}\leftrightarrow\text{算术数据）}$$
$$\textbf{(L)}\ ✓\ \textbf{部分}：\text{Euler 积}\Longrightarrow\text{右半平面无零点（}\mathrm{Re}\,s>1\text{）＋经典无零区}\ \Longrightarrow\ \text{被迫区域}\ \Omega^{\rm forbid}=\{\mathrm{Re}\,s>1\ (\text{及无零区})\}$$
$$\qquad\textbf{型}：\textbf{禁止区域型}；\ \textbf{不足原因}：\Omega^{\rm forbid}\ \text{距}\ 1/2\ \text{极远，无任何迫使靠拢临界线的内容}$$
$$\Longrightarrow\ \text{判定}：\textbf{(R)}＋\textbf{弱(L)}\ \text{（禁止区域型）}$$

### Φ2 Fourier／Poisson
$$\text{输入}\ \text{格点／周期化算术数据}\ \to\ \text{对偶和}$$
$$\textbf{(R)}\ ✓\ \text{（对偶恒等式）}；\ \textbf{(L)}\ \times：\text{对任意测试函数两侧恒等} \Longrightarrow \text{可容许性}\ \text{不产生任何谱位置限制}$$
$$\therefore\ \textbf{不可由该映射提取}\ \Omega\ \text{的非平凡形式}$$
$$\Longrightarrow\ \text{判定}：\textbf{仅(R)}$$

### Φ3 显式公式
$$\text{输入}\ \text{素数侧和}\ \to\ \text{零点侧和}$$
$$\textbf{(R)}\ ✓\ \text{（恒等式：把零点侧表示为素数侧）}；\ \textbf{(L)}\ \times：\text{对任意测试函数成立}，\text{零点}\ \text{出现但不被}\ \text{可容许性}\ \text{定位}$$
$$\qquad\text{注}：\text{若附加}\ \textbf{Weil 正性}\ \text{才产生约束 —— 但那}\ \textbf{与 RH 等价（循环）}，\text{不属于本映射自身能力}$$
$$\Longrightarrow\ \text{判定}：\textbf{仅(R)}（\text{正性加固}\to\ \text{循环通道}）$$

### Φ4 迹式（Selberg／Guinand 及算术迹式纲领）
$$\text{输入}\ \text{几何侧（闭测地线／共轭类）}\ \to\ \text{谱侧（特征值／零点）}$$
$$\textbf{(R)}\ ✓\ \text{（恒等式）}；\ \textbf{(L)}\ ✓\ \text{仅}\ \textbf{几何情形}：\text{迹式＋几何}\Longrightarrow\text{谱隙型区域限制}$$
$$\qquad\textbf{算术情形}：\text{Deninger／AOB 线}\ \textbf{停滞}（G10／Deninger 6.6）\Longrightarrow \text{无可用}\ \Omega$$
$$\Longrightarrow\ \text{判定}：\textbf{(R)}＋\textbf{弱(L)（区域型，仅几何侧）}；\ \text{算术侧}\ \textbf{空缺}$$

### Φ5 函数方程
$$\text{输入}\ \text{完备化}\ \Lambda(s)=\varepsilon\Lambda(1-s)\ \to\ \text{零点集的对称性}$$
$$\textbf{(R)}\ ✓；\ \textbf{(L)}\ ✓\ \textbf{（本档六类中约束最强的一个）}：\text{零点集在}\ \rho\mapsto1-\bar\rho\ \text{下不变} \Longrightarrow \text{真正的}\ \textbf{集合约束（并非恒等式）}$$
$$\qquad\textbf{型}：\textbf{对称型}；\ \textbf{结构性局限}：\text{对称是}\ \textbf{双侧} \text{的} \Longrightarrow \text{不能排除临界线}：$$
$$\qquad\qquad\text{V229-A：FE 迫使任何}\ \beta\text{-界}\ \textbf{双侧}；\quad\text{V248 §2：FE 对称不排除临界线，只排除单侧集}$$
$$\qquad\text{且}\ \text{FE}\ \in\ \textbf{Archimedean 层}\ \text{通道（A-leak，V172 §5a）}$$
$$\Longrightarrow\ \text{判定}：\textbf{(R)}＋\textbf{(L)（对称型，双侧）}\ \text{—— 最锐利但仍不足以逼到线}$$

### Φ6 表示论实现
$$\text{输入}\ \text{自守表示}\ \pi\ \to\ L(s,\pi)\ \text{的谱数据}$$
$$\textbf{(R)}\ ✓\ \text{（Langlands 式实现：}a\mapsto L(s,\pi)）$$
$$\textbf{(L)}\ \text{形式上}\ ✓，\text{但其关键约束（temperedness／Ramanujan）}\ \textbf{恰是未决猜想} \Longrightarrow \text{定位能力}\ \textbf{≡ 开放问题本身}$$
$$\Longrightarrow\ \text{判定}：\textbf{(R)}＋\textbf{猜想型(L)}（\text{无独立可用的}\ \Omega）$$

---

## 3. 审计汇总表
$$\begin{array}{c|c|c|c}
\Phi & (R)\ \text{表示} & (L)\ \text{定位} & \textbf{定位型}\\ \hline
\Phi_1\ \text{Euler/Mellin} & ✓ & ✓\ \text{弱} & \textbf{禁止区域型}（\mathrm{Re}\,s>1\ \text{及无零区）\\
\Phi_2\ \text{Fourier/Poisson} & ✓ & × & —（对偶恒等式）\\
\Phi_3\ \text{显式公式} & ✓ & × & —（恒等式；正性加固＝循环）\\
\Phi_4\ \text{迹式} & ✓ & ✓\ \text{仅几何} & \textbf{区域型}（谱隙）；\text{算术侧停滞}\\
\Phi_5\ \text{函数方程} & ✓ & ✓ & \textbf{对称型}（双侧）\\
\Phi_6\ \text{表示论实现} & ✓ & ≡\text{猜想} & \textbf{猜想型}
\end{array}$$

## 4. ⭐ 核心结论（对"representation vs localization"二分的精化）
$$\textbf{实测结果}\ \ne\ \text{"六类只有 representation"}：\text{其中}\ \textbf{三类}\ (\Phi_1,\Phi_4,\Phi_5)\ \textbf{确实提供定位}，$$
$$\qquad\text{但定位}\ \textbf{全部为弱型}，\text{落在}\ \textbf{三种类型}：\boxed{\text{禁止区域型}\ |\ \text{对称型}\ |\ \text{区域型（仅几何侧）}}；\ \text{另}\ \Phi_6\ \text{为}\ \textbf{猜想型}$$
$$\Longrightarrow\ \textbf{缺口的精确形态}：$$
$$\boxed{\text{现有跨层映射提供的定位} = \{\text{禁止区域},\ \text{双侧对称},\ \text{几何侧区域},\ \text{猜想型}\}\ \text{四类皆} \textbf{不能把谱位置逼到}\ 1/2\ \text{附近}}$$
$$\text{即：}\text{representation}\ne\text{localization}\ \text{的判断}\ \textbf{成立但不完整}；\text{更精确的陈述是}$$
$$\boxed{\text{缺失的是}\ \textbf{线强制型定位（line-enforcing localization）}：\text{一种}\ \Omega=\{1/2\}\ \text{型、}\textbf{非对称、非猜测、非仅几何} \text{的被迫区域}}$$

## 5. 两种结局的落点（按章程 §5）
$$\textbf{不是(甲)}：\text{并非"缺口不在跨层映射本身"} —— \text{六类中的三类}\ \textbf{确实有定位能力}，\text{但无一具线强制型}$$
$$\textbf{接近(乙)}：\text{现有}\ \Phi\ \textbf{确实不能产生线强制型定位}\ \Longrightarrow \text{这是一个}\ \textbf{干净缺口}；$$
$$\qquad\textbf{但须严格标注}：\text{本结论限于}\ \textbf{六个固定映射}，\text{不构成"任何跨层映射皆不能"的定理（N1/N2）}✓$$

## 6. 第三步：缺失结构是什么（**只给性质规格，不给候选**）
$$\text{须同时满足}：$$
$$\text{(i)}\ \text{由}\ \textbf{算术可容许性} \text{（而非}\ a\ \text{的偶然取值）驱动；}\quad\text{(ii)}\ \textbf{非双侧对称}（\text{否则撞 V229-A／V248 §2}）；$$
$$\text{(iii)}\ \textbf{非禁止区域型}（\text{否则撞}\ \mathrm{Re}\,s>1\ \text{型弱约束}）；\quad\text{(iv)}\ \textbf{非猜想型}（\text{不得等价于 Ramanujan／temperedness}）；$$
$$\text{(v)}\ \textbf{非循环}（\text{不得等价于 Weil 正性／POS}）；\quad\text{(vi)}\ \text{产生}\ \Omega=\{1/2\}\ \text{型（或收缩到它的）被迫区域}$$
$$\textbf{本档}\ \textbf{不就 (i)--(vi) 提出任何候选}（\text{章程 §9.3 明令}）$$

## 7. 边界（N1/N2 严守）
$$\text{① 本档为}\ \textbf{审计}，\text{非候选清单}；\quad\text{② 六类}\ \Phi\ \text{的划分为}\ \textbf{定义决策}（\text{照章程 §3 原列}）$$
$$\text{③}\ \Phi_5\ \text{的"双侧不足"依据 V229-A／V248 §2，}\Phi_4\ \text{的停滞依据 G10／Deninger 6.6，}\Phi_1\ \text{的无零区为经典结论，}\Phi_6\ \text{与猜想的关系为}\ \textbf{[结构判定]}；$$
$$\qquad\text{上述档案引用}\ \textbf{未逐行重验}；\quad\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 8. 净产出
$$\text{(i) 把"定位"数学化为可检验命题（(R)／(L)／(L}^\star\text{) 三层＋判别式）；}$$
$$\text{(ii) 六类}\ \Phi\ \text{逐项硬审计（含"哪三类确有定位"的实测事实）；}$$
$$\text{(iii) ⭐ 对二分的精化：缺口}\ \ne\ \text{"缺 localization"，而是缺}\ \textbf{线强制型定位}；$$
$$\text{(iv) 缺失结构的性质规格 (i)--(vi)（**不给候选**）；}$$
$$\text{(v) 结局落点：接近(乙) 但严格限于六个固定映射。}$$
