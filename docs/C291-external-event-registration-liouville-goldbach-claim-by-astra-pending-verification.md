已查地图（**先查后写**）：`C-290`（四候选事实审计卡 ✓）、`C-289`（候选池 ✓）、`C-287`（封口账 ＋ 不建新判据 ✓）。外部来源检索：`arXiv:2404.12117`（Mangerel ✓）、`openai.com/index/ten-advances-in-mathematics`（✓）、`MathOverflow 307479`（✓）。原文见 §7 ✓

D0: 本档对象 = **C-291：外部事件登记 —— 据称 GPT-6 Astra 的 Liouville 版哥德巴赫结果（待核验）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\boxed{\textbf{① 事件性质}✗✓：\text{报道的是}\ \textbf{Liouville 版哥德巴赫类比}✓，\textbf{不是} \text{经典哥德巴赫}✗ \Longrightarrow \textbf{经典哥德巴赫仍开放}✓}$$
$$\boxed{\textbf{② 登记级别}✓✓：\text{按唐先生措辞，登记为}\ \textbf{外部、待原始材料核验的事件}✓；\textbf{不} \text{登记为已验证数学定理}✗}$$
$$\boxed{\textbf{③ 合法用途}✓：\textbf{不进}\ RH\ \text{主线}✗；\textbf{不进} \text{四候选池排序}✗；\text{仅作为}\ \textbf{外部机制样本} \text{的候选}✓（\text{待核验}✗）}$$
$$\boxed{\textbf{④ 关键审计问句}✓✓：\text{不问「AI 能否证哥德巴赫」}✗；\text{问}\ \textbf{它究竟消掉了 Mangerel 证明中的哪个 GRH 依赖}✓；\text{并追加一问（本档补充）}\ \textbf{该无条件版本是否本来就无需}\ GRH✗（见\ \S4✓）}$$

## §1 事件登记（**唐先生措辞，逐字**✓✓）

> **"2026-09-20/21，网络公开披露一项据称由 GPT-6 Astra 发现、并声称已 Lean 形式化的 Liouville 版 Goldbach 无条件证明；经典 Goldbach 仍未解决。需取得原始证明/Lean repository 后逐行审计，暂不将其登记为已验证数学定理。"** ✓✓

$$\text{登记级别}✓：\textbf{[外部报道 · 待核验]}✗ \quad（\text{与档案馆「外部来源先按不可信数据处理」纪律一致}✓）$$

## §2 我方独立核实结果（✓✓）

$$\textbf{① Mangerel 原文存在}✓✓：\text{A. P. Mangerel, \emph{On a Goldbach-type problem for the Liouville function}, arXiv:2404.12117 (2024)}✓$$
$$\qquad \text{内容（转述}✓）：\text{对充分大的偶数}\ N，\exists a,b\ge1:\ a+b=N\ \text{且}\ \lambda(a)=\lambda(b)=-1✓；\textbf{原文自述为 conditionally answers}✓✓$$
$$\textbf{② 问题提出者}✓✓：\text{该 Liouville 版哥德巴赫**由 Shusterman 提出**}✓（\text{非 Mangerel 原创}✓） \Longrightarrow \text{引用时须区分「提出」与「条件解决」}✓$$
$$\textbf{③ 条件性}✓✓：\text{Mangerel 的解答是}\ \textbf{条件性的}✓（\text{与唐先生所述「GRH 下」}✓一致）$$
$$\textbf{④ 范围}✓：\text{原文是}\ \textbf{「充分大」\ 的偶数}✓（\text{渐近}✓），\textbf{非}\ \text{「所有}\ N>2」✗ \Longrightarrow \text{报道中「}\forall N>2\ \text{偶数」的表述}\ \textbf{待核}✗✓$$
$$\textbf{⑤ 与 OpenAI 公开清单的关系}✓✓：\text{已检索}\ \texttt{openai.com/index/ten-advances-in-mathematics}✓\ \text{与报道所称仓库}\ \texttt{openai/ten-proofs}✓$$
$$\qquad \text{十项清单为：球堆积／编码界／permanent 下界／multicolor Ramsey（Erdős 183）／Connes 刚性反例／非 sofic 群存在性等}✓$$
$$\qquad \Longrightarrow \textbf{未含 Liouville 版哥德巴赫}✗✓ \Longrightarrow \text{该结果}\textbf{不在公开十项之列}✗ \Longrightarrow \text{报道来源与一手材料}\ \textbf{尚未对上}✗$$
$$\textbf{⑥ OpenAI 侧可核事实}✓：\text{模型把每个论证}\ \textbf{形式化为 Lean 证书}✓；\text{公布思考叙述}✓；\text{总 token 约}\ \$2{,}000✓$$
$$\qquad \text{另：Astra 官方数学成果为}\ \textbf{素数间隙}✓（\text{短间隙}\ 240\to186✓；\text{大间隙改进了}\ 80\ \text{多年未变的项}✓），\textbf{与哥德巴赫无关}✗$$

## §3 关键区分（**必须严格分开**✓✓）

$$\textbf{经典形式}✓：N=p+q✓（p,q\ \text{素数}✓）$$
$$\textbf{Liouville 形式}✓：N=a+b✓（\lambda(a)=\lambda(b)=-1✓）；\quad \lambda(n)=(-1)^{\Omega(n)}✓，\Omega=\text{素因子总数（按重数）}✓$$
$$\textbf{蕴含方向}✓✓：\textbf{经典}\ \Longrightarrow\ \textbf{Liouville}✓（\text{因素数}\ p\ \text{有}\ \lambda(p)=-1✓）；\ \textbf{反向不成立}✗✓$$
$$\qquad \text{反例性说明}✓：\lambda(45)=(-1)^3=-1✓，\text{但}\ 45=3^2\cdot5\ \text{非素数}✓ \Longrightarrow \text{Liouville 版是}\textbf{明显更宽}\ \text{的加法表示问题}✓✓$$
$$\Longrightarrow \boxed{\textbf{Liouville-Goldbach}\not\Rightarrow\textbf{经典 Goldbach}}✓✓$$

## §4 关键审计问句（✓✓）

$$\textbf{主问}✓（\text{唐先生}）：\text{它究竟消掉了 Mangerel 证明中的}\ \textbf{哪个 GRH 依赖}✓？$$
$$\qquad \text{候选结构}✓：\text{GRH-dependent correlation bound} \longrightarrow \text{unconditional correlation bound}+\text{descent}✓$$
$$\qquad \text{为何重要}✓✓：\text{若经原文／Lean 审计站得住，则比「AI 又证一个哥德巴赫变体」}\ \textbf{重要得多}✓ —— \text{可能给出一个}\ \textbf{真正独立的 arithmetic mechanism 样本}✓$$

$$\textbf{追加问}✓✓（\text{本档补充，来自外部讨论}✓）：\text{该}\ \textbf{无条件版本是否本来就无需}\ GRH✗？$$
$$\qquad \text{线索}✓：\text{MathOverflow 307479}\ \text{下有回答指出}✓：\text{用 GPY 型筛法可对充分大的}\ N\ \text{与充分大的}\ k\ \text{得到}\ \omega(n)=\omega(m)=k\ \text{的解}✓，\text{并主张「}\Omega\ \text{版更强的陈述也许用今日方法即可证」}\ ⚠️（\text{仅论坛主张}✗，\textbf{非定理}✗）$$
$$\qquad \Longrightarrow \text{若该线索成立，则「去掉 GRH」的}\ \textbf{新颖性会大幅下降}✗ \Longrightarrow \textbf{这是核验的第一优先项}✓✓$$
$$\qquad \textbf{两个问句的区别}✓✓：\text{主问问「技术路径」✓；追加问问「新颖性是否成立」✓} \Longrightarrow \text{两者都必须答，才知道该结果值不值得进档案}✓$$

## §5 纪律（✓✓）

$$\textbf{① 不登记为定理}✗；\textbf{② 不进}\ RH\ \text{主线}✗；\textbf{③ 不进四候选池排序}✗；\textbf{④ 不建}\ RH\ \text{bridge}✗；\textbf{⑤ 不以「报道」替代一手材料}✗$$
$$\textbf{⑥ 待办（核验清单）}✓：\text{① 取得 Astra／Liouville 的}\ \textbf{原始证明与 Lean 仓库}✓（\text{若存在}✓）；\text{② 逐行核}\ \S3\ \text{的蕴含方向与范围}✓；\text{③ 核}\ \S4\ \text{两个问句}✓；\text{④ 在核验前}\ \textbf{不更新任何档案结论}✗$$

## §6 边界

$$\textbf{① 零计算}✗（\text{无任何运行}✓）；\text{未读 pending}✗；\text{未改他档正本}✓；\text{未动}\ v4✗$$
$$\textbf{② 外部来源}✓：\text{经}\ \texttt{web\_search}\ \text{取得}✓，\textbf{按不可信外部数据处理}✓；\text{关键论断均附来源}✓$$
$$\textbf{③ 不得} \text{写成}✗：\text{「Astra 证明了哥德巴赫」}✗；\text{「Liouville 版蕴含经典版」}✗；\text{「该结果已被验证」}✗$$
$$\textbf{④ }\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$

## §7 【技术词回查】输出 ＋ 来源（**先跑后写**✓）

```
技术词 待核验事件登记 命中文件数=0    :: 
技术词 条件性依赖审计 命中文件数=0    :: 
技术词 Liouville        命中文件数=19   :: ./V218-half-value-source-audit-H0.md ./euclid-connection-candidate.md ./RESEARCH-CONSTITUTION.md 
```
$$\textbf{① 本档新增}✓：\text{待核验事件登记}✓／\text{条件性依赖审计}✓；\text{「Liouville」一词命中情况见上}✓$$
$$\textbf{② 来源清单}✓✓：$$
$$\qquad \text{Mangerel, \emph{On a Goldbach-type problem for the Liouville function}, arXiv:2404.12117 ✓（\textbf{条件性}；问题由 Shusterman 提出}✓）$$
$$\qquad \text{OpenAI, \emph{Ten advances in mathematics and theoretical computer science}, 2026-08-01 ✓（\textbf{清单不含} Liouville 版哥德巴赫}✗）$$
$$\qquad \text{OpenAI, GPT-6 Astra 模型页 ✓（数学成果＝}\textbf{素数间隙}✓\text{）}$$
$$\qquad \text{MathOverflow 307479}\ \emph{Goldbach's conjecture for the Liouville function}✓（\text{GPY 线索}⚠️\text{，论坛主张}✗）$$
$$\qquad \text{中文报道（加西网／新智元系）✓ —— \textbf{二手}✗，仅作事件来源}✓$$
