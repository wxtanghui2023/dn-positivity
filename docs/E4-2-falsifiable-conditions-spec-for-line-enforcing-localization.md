# E4-2 — **「单侧破对称 → 线强制定位」缺口填充结构的可证伪条件规格**

> 唐先生 2026-09-16 17:56「继续」；按 REVIEW-E4 §6 登记入口开工。
> **本档不命名机制、不造候选**；只给**可证伪条件**（先条件，后结构）。

---

## 0. 本档性质
$$\text{对象}：\text{REVIEW-E4 压缩所得的唯一箭头}\quad\boxed{\text{单侧破对称}\ \xrightarrow{\ X\ }\ \text{线强制定位}}$$
$$\text{任务}：\text{给出}\ \textbf{任何}\ X\ \text{若要合法填充该箭头，}\textbf{必须满足的可證伪条件}；\ \textbf{不给出}\ X\ \text{的实例}$$
$$\textbf{纪律}：\text{条件须}\ \textbf{可检验}（\text{每条附}\ \textbf{kill witness}）；\ \text{不写}\ \forall X\ \text{型否定定理；}\ \text{不写完备性断言。}$$

## 1. 术语（承接 E4-0／E4-1，不新增）
$$\mathscr A_{\rm adm}\ \text{可容许类；}\ G=\langle s\mapsto1-s,\ s\mapsto\bar s\rangle；\ \rho=\tfrac12+\delta+it$$
$$(R)\ \text{表示型}\ a\mapsto F_a(t)；\ (L)\ \text{定位型}\ \forall a\in\mathscr A_{\rm adm}:\operatorname{supp/spectrum}(F_a)\subseteq\Omega；\ (L^\star)\ \Omega=\{1/2\}\ \text{型}$$
$$\mathcal A_{\rm old}=\{\text{计数},\text{值面},\text{correlation},\text{指标},\text{层错配},\text{复杂度}\}\ \cup\ \{\text{交换/恒等式},\text{coboundary},\text{有限局部},\text{传播},\text{呈现依赖}\}\ (\text{V328})$$

---

## 2. 可证伪条件（C1–C11，每条附 kill witness）

### C1 破双侧性（G-非不变）
$$\textbf{要求}：X\ \text{的输出}\ \textbf{不是}\ G\text{-不变的}；\ \text{形式上}\ \exists\ \text{配置}\ Z:V_X(Z)\ne V_X(gZ)\ \text{对某}\ g\in G\ (\text{尤指}\ s\mapsto1-\bar s)$$
$$\textbf{kill witness}：\text{若}\ V_X\ \text{在}\ G\ \text{下不变}\ \Longrightarrow\ \mathrm{DEAD}\ (\text{S1 定理的直接后果})$$

### C2 由可容许性驱动（非偶然取值）
$$\textbf{要求}：\text{约束}\ \textbf{对}\ \mathscr A_{\rm adm}\ \text{全体一致成立}，\text{不依赖}\ a\ \text{的特殊选择或测试函数的特选}$$
$$\textbf{kill witness}：\text{若约束只在特选}\ a／\text{特选测试函数下出现}\ \Longrightarrow\ \mathrm{DEAD}\ (\text{退化为}\ (R))$$

### C3 非禁止区域型（须逼近线）
$$\textbf{要求}：\text{输出}\ \Omega\ \text{满足}\ \Omega\subseteq\{|\mathrm{Re}\,s-\tfrac12|\le\varepsilon\}\ \text{且}\ \textbf{机制内可令}\ \varepsilon\to0\ (\text{或直接}\ \Omega=\{1/2\})$$
$$\textbf{kill witness}：\text{若输出仅形如}\ \mathrm{Re}\,s>1-\tfrac{c}{\log|t|}\ \text{型区域}\ \Longrightarrow\ \mathrm{DEAD}\ (\text{区域型，与 E4-0 }\Phi_1\ \text{同型})$$

### C4 非猜想型
$$\textbf{要求}：X\ \text{的输出}\ \textbf{不等价于} \text{任何}\ \textbf{已命名未决猜想}（\text{Ramanujan／temperedness 等}）$$
$$\textbf{kill witness}：\text{若}\ V_X\iff\text{某已命名猜想}\ \Longrightarrow\ \mathrm{DEAD}\ (\text{猜想型，与 E4-0 }\Phi_6\ \text{同型})$$

### C5 非循环
$$\textbf{要求}：X\ \text{的输出}\ \textbf{不等价于} \text{RH／Weil positivity／POS1-POS2／Robin 型见证}；\text{须能给出}\ \textbf{独立性证据}$$
$$\textbf{kill witness}：\text{若}\ V_X\iff\mathrm{RH}\ \text{或}\iff\text{Weil 二次型}\ge0\ \Longrightarrow\ \mathrm{DEAD}\ (\text{循环})$$

### C6 非旧语言（须逐项排除 V328 的}\ \mathcal A_{\rm old}\text{）
$$\textbf{要求}：V_X\ \text{不可表达为}\ \text{计数／值面／}\ N(\sigma,T)\ \text{／有限阶相关／指标-上同调／复杂度／交换-恒等式／coboundary／有限局部／传播}$$
$$\textbf{kill witness}：\text{任一项可表达}\ \Longrightarrow\ \mathrm{DEAD}\ (\text{按 V328 吸收表})$$

### C7 非呈现依赖
$$\textbf{要求}：V_X\ \text{在生成元／表示／坐标的更换下}\ \textbf{不变}$$
$$\textbf{kill witness}：\text{若因换较短的表示／较简单的编码而使}\ V_X\ \text{改变}\ \Longrightarrow\ \mathrm{DEAD}\ (\text{V325 的"呈现依赖"教训})$$

### C8 单侧量须具定量强制（**S3 的核心**）
$$\textbf{要求}：\text{存在}\ \mathcal D：\text{配置}\to\mathbb R\ \text{使}\ \mathcal D\ge0\ \text{且}\ \boxed{\mathcal D=0\iff\mathrm{Re}\,\rho=\tfrac12}\ (\text{定位，而非仅区分两侧})$$
$$\qquad\text{且}\ \mathcal D\ \text{的正性}\ \textbf{来自可容许性}，\textbf{不得} \text{为}\ \mathcal D=|\mathrm{Re}\,\rho-\tfrac12|\ \text{型重写}$$
$$\textbf{kill witness}：\text{(a) 若只给}\ \mathcal D(\delta)>\mathcal D(-\delta)\ \text{而无}\ \mathcal D=0\iff\delta=0\ \Longrightarrow\ \text{不足；}\ \text{(b) 若}\ \mathcal D\ \text{为 RH 重写}\ \Longrightarrow\ \mathrm{DEAD}$$

### C9 可证伪性（须自带独立可检验推论）
$$\textbf{要求}：X\ \text{须蕴含一条}\ \textbf{可独立检验} \text{的算术陈述}\ Q（\text{理想状况：其反例可在}\ X\asymp T\ \text{尺度搜索}）$$
$$\textbf{kill witness}：\text{若换不出任何独立可检验推论}\ \Longrightarrow\ \mathrm{DEAD}\ (\text{不可证伪})$$

### C10 与既有单侧成分相容（sanity check）
$$\textbf{要求}：X\ \text{的定位}\ \textbf{须蕴含或复现} \text{已知无零点区域（}\mathrm{Re}\,s>1\ \text{及其向左延伸）作为特例}$$
$$\textbf{kill witness}：\text{若与已知无零区矛盾}\ \Longrightarrow\ \mathrm{DEAD}\ (\text{不一致})$$

### C11 反循环构造纪律（承接 E3-A 的 D1／D2）
$$\textbf{要求}：X\ \text{须在}\ \textbf{目标命题之外} \text{定义，且三段箭头}\ \boxed{\text{输入信息}\to X\ \text{的定义}\to V_X}\ \textbf{逐段可列}$$
$$\qquad\text{(ii) 判定}\ V_X\ \text{的观测形式须}\ \textbf{在构造}\ X\ \text{之前固定}\ (\text{禁事后挑选})$$
$$\textbf{kill witness}：\text{任一段不可列，或观测形式事后选定}\ \Longrightarrow\ \mathrm{DEAD}$$

---

## 3. 可证伪性矩阵（验收表）
$$\begin{array}{c|c|c}
\text{条件} & \text{检验方式} & \text{kill witness}\\ \hline
C1\ \text{破双侧} & \text{对}\ G\ \text{作用查}\ V_X & G\text{-不变}\\
C2\ \text{可容许驱动} & \text{全}\ \mathscr A_{\rm adm}\ \text{一致性} & \text{仅特选}\ a\ \text{成立}\\
C3\ \text{逼近线} & \text{量化}\ \Omega\ \text{与}\ 1/2\ \text{距离} & \text{仅区域型}\\
C4\ \text{非猜想} & \text{与已命名猜想比对} & \text{等价于 Ramanujan 型}\\
C5\ \text{非循环} & \text{与 RH／Weil／POS 比对} & \text{等价于 Weil 型}\\
C6\ \text{非旧语言} & \text{对}\ \mathcal A_{\rm old}\ \text{逐项试表达} & \text{任一可表达}\\
C7\ \text{非呈现依赖} & \text{更换生成元／编码} & V_X\ \text{随编码变}\\
C8\ \text{定量强制} & \text{检验}\ \mathcal D=0\iff\delta=0\ \text{且}\ \mathcal D\ \text{来源} & \text{仅分两侧／RH 重写}\\
C9\ \text{可证伪} & \text{抽出独立推论}\ Q & \text{无可检验推论}\\
C10\ \text{相容性} & \text{含已知无零区为特例} & \text{与无零区矛盾}\\
C11\ \text{反循环} & \text{三段可列＋观测前固定} & \text{不可列／事后选定}
\end{array}$$

## 4. 判定协议
$$\textbf{术语}：\text{任一}\ \mathrm{kill\ witness}\ \text{出现}\ \Longrightarrow\ \boxed{\mathrm{DEAD}}；\ \text{全部通过}\ \Longrightarrow\ \boxed{\text{ALIVE candidate（仍非 VI）}}$$
$$\text{ALIVE 后仍须过}\ \textbf{irreducible novelty}（\text{V322 §6}\）\text{与}\ \texttt{irreversible}（\text{V318-II §3}\）$$
$$\textbf{重要}：\text{本规格}\ \textbf{不保证}\ \text{存在满足全部 C1--C11 的}\ X；\ \text{它的作用是}\ \textbf{把"是否该反向构造"变成可判定问题}✓$$

## 5. 明确非声明（本档边界）
$$\text{① 本档}\ \textbf{不命名任何机制}，\ \textbf{不给任何}\ X\ \text{的实例}；$$
$$\text{② C1--C11 的条目划分为}\ \textbf{定义决策}（\text{可修订}）；\ \text{其中 C1 由 S1 支撑，C3--C6 由 E4-0／V328 支撑，C8 由 S3 支撑，C11 由 E3-A 支撑；}$$
$$\text{③ 本档}\ \textbf{不声称} \text{该缺口必有填充物，}\ \textbf{也不声称} \text{其必无}；$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 6. 净产出
$$\text{(i) 把"是否该反向构造"}\ \textbf{转为可判定问题}：\ \text{须先通过 C1--C11 的}\ \mathrm{kill\ witness}\ \text{检验；}$$
$$\text{(ii) 每条条件附}\ \textbf{具体 kill witness}（\text{可操作，不依赖直觉}）；$$
$$\text{(iii) 验收协议与"ALIVE 后仍非 VI"的层级纪律；}$$
$$\text{(iv) 明确不命名机制、不给实例、不断言存在或不存在}✓$$
