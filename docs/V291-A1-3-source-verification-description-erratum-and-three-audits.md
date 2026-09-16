# V291 · **A1-3 文献对象核验 ＋ 描述勘误 ＋ 三项审计** —— ⚠️ **错在 V290 的推荐（不在档案）**；⭐⭐ **档案 `E4-palojarvi-finitely-many.md`（09-12，读过全文）早已完成本项分析**，其判词是"纯技术推广，但 buys nothing unless you can independently bound the number of off-line zeros" ⟹ **A1-3 价值判定：低** ⟹ **V290 推荐降级** ⭐⭐⭐⭐

$$\boxed{\text{核验结果}：\text{归档 PDF}\ ＝\ \textbf{Neea Palojärvi}（\mathrm{arXiv}{:}1807.01506v3,\ 26\ \text{页}）✓\ \text{非 Stevenhagen} ✓}$$
$$\boxed{\text{Thm 4.1 的真实形态}：\textbf{"至多一个"是假设，不是结论}};\ \text{结论}\ ＝\ \textbf{充要判据（iff）} ✓✓✓$$
$$\boxed{\text{⚠️ V290 §3 描述错误（本档勘误）}：\text{不是"无条件结构定理／对离轴零点}\ \textbf{个数} \text{的界"} ✗✓}$$
$$\boxed{\text{⭐ 档案早已分析过}：`E4-palojarvi-finitely-many.md`（2026-09-12，逐字读过 PDF）\ \text{已给出三条 locus ＋ 扩展代价 ＋ 判词}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 12:03：**"拍板：开论文线，但暂时不能批准'首攻 A1-3 的数学证明'"**；指出检索到的是 **Stevenhagen《Redei Reciprocity…》** 而 **其 Thm 4.1 是 $r_8=r_4-\mathrm{rank}_{\mathbf F_2}R_8$，与离轴零点无关** ⟹ **"不能凭项目档案里的二手描述直接开证明"** ✓✓；要求：**先锁定 Paljärvi 原文 ＋ Thm 4.1 全文 ＋ 假设 ＋ 证明**，然后只做**三项审计**（① 原定理到底说什么 ② "有限多个"是否逻辑直接 ③ 证明机制能否移植：纯技术推广 vs 需新零点排斥机制）；并给出**危险误读警告**：$$\boxed{\text{"每个对象至多一个离轴零点"}\not\Rightarrow\text{"整个算术类只有有限个离轴零点"}}$$（除非对象族固定或有统一参数约束）✓✓
> 依据 ✓ 归档 PDF `docs/Palojarvi-2019-tau-Li-explicit-zero-free.pdf`（本档**亲自抽取正文核验** ✓）｜`docs/E4-palojarvi-finitely-many.md`（09-12，逐字读原文 ✓）｜`PENDING-ITEMS-MASTER.md` A1-3 行（**terse 行，本档于最末更正**）✓
> 执行 ✓ 小灵｜**纸面 ✓（提取正文核验；零数值推导 ✓）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ `V291`（`id_claim.sh` ✓）

---

## §1 核验结果（本档亲自抽正文，非引用）

$$\text{文件名}：\texttt{Palojarvi-2019-tau-Li-explicit-zero-free.pdf}（335{,}337\ \text{字节},\ 26\ \text{页}）✓$$
$$\text{首页逐字}：\textbf{"EXPLICIT ZERO-FREE REGIONS AND A $\tau$-LI-TYPE CRITERION, NEEA PALOJÄRVI"};\ \mathrm{arXiv}{:}1807.01506v3\（\text{29 Apr 2020}）✓✓$$
$$\text{摘要逐字要点}：\text{① 第一主结果}：\text{显式}\ N_1,N_2\ \text{使若}\ \tau\text{-Li 系数的实部在}\ [N_1,N_2]\ \text{上非负，则函数在某区域外}\textbf{无零点};\ \text{② 第二主结果}：\text{若某些}\ \tau\text{-Li 系数实部在某}\ [n_1,n_2]\ \text{上有负者，则}\textbf{至少存在一个零点} \text{在某区域外} ✓✓$$
$$\qquad ⚠️\ \text{注意：论文是"}\textbf{至少一个}"\ \text{方向的结果} ＋ \text{一个}\ \textbf{iff}\ \text{判据（Thm 4.1）};\ \text{"}\textbf{至多一个}"\ \text{只出现在}\ \textbf{假设} \text{中} ✓✓✓$$

### Thm 4.1 逐字（本档抽取）
$$\text{假设}：F(s)\ \textbf{至多有一个} \text{零点}\ \rho_1\ \text{满足}\ \Big|\tfrac{\rho_1}{\rho_1-\tau}\Big|>1;\ \text{若存在，设}\ R>1\ \text{使}\ \Big|\tfrac{\rho_1}{\rho_1-\tau}\Big|\ge R ✓$$
$$\text{结论}：\textbf{该零点}\ \rho_1\ \text{存在}\iff\Big|\Re\big(\lambda_F(n,\tau)\big)\Big|\ \ge\ \big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)\,n\log n\ \ \text{对}\ \textbf{某个}\ n\in[N,5N],\ N\mid n ✓✓$$
$$\qquad \text{其中}\ N\ \text{为显式量（依赖}\ \tau,T_0,R,K\ \text{与}\ W_{-1}）;\qquad \text{且}\ \big|\tfrac{\rho}{\rho-\tau}\big|=1\iff\Re\rho=\tfrac{\tau}{2}\ \left(\text{故}\ \tau=1\ \text{时区域即}\ \Re\rho>\tfrac12\right) ✓$$

---

## §2 ⚠️ T10 勘误（对 `V290` §3 的更正）

$$\text{V290 §3 原写} ✗：\text{"`A1-3` ＝ 无条件结构定理（对离轴零点}\ \textbf{个数} \text{的界）"} ⚠️$$
$$\qquad \textbf{错处 1}：\text{Thm 4.1}\ \textbf{不给出} \text{离轴零点个数的界 —— 它}\ \textbf{假设} \text{"至多一个"},\ \text{结论是}\ \textbf{判据} ✓$$
$$\qquad \textbf{错处 2}：\text{故它不是"无条件结构定理"，而是}\ \textbf{条件性充要判据} ✓$$
$$\qquad \textbf{错处 3（流程）}：\text{本档}\ \textbf{凭 terse 台账行} \text{（`PENDING` A1-3）下推荐，而}\ \textbf{未读已验证原文的那份档}（`E4-…`，09-12 已写）✓✓$$
$$\Longrightarrow \boxed{\text{更正}：\text{`A1-3` 的}\ \textbf{正确表述} \text{＝"把 Thm 4.1 的}\ \textbf{假设} \text{从'至多一个'放宽到'至多}\ m\ \text{个'，并重推判据"}} ✓✓$$

---

## §3 ⭐⭐⭐ 关键发现：**档案早已完成本项分析**（`E4-palojarvi-finitely-many.md`，2026-09-12）

$$\text{该档自标}：\textbf{"Source read: … arXiv:1807.01506v3 … All quotations below are from the author's PDF"} ⟹ \textbf{逐字读过原文} ✓✓$$
$$\qquad \text{本档核验：其引文与 Thm 4.1 形态}\ \textbf{与本档 §1 完全一致} ✓✓$$

$$\textbf{三 locus（"至多一个"被用在何处，该档 §3）}：$$
$$\qquad \textbf{A（分类／抽出一项）}：\text{"对}\ \rho\ne\rho_1\ \text{有}\ |w|\le1\ \text{故}\ \Re\rho\le\tau/2"\ ⟹ \text{两个显式和都可限制在半条带}\{0\le\Re\rho\le\tau/2\},\ \text{只漏}\ \rho_1 ✓$$
$$\qquad \textbf{B（每零点记 2 的界）}：\ |1-w^n|\le2\ \text{需}\ |w|\le1\ \text{对和中的}\ \textbf{每个} \text{零点成立 —— 靠 A 才成立} ✓$$
$$\qquad \textbf{C（单项检测）}：\text{下界用"至多一个"}\ ⟹\ \text{"5"}\ ＝\ \text{Lemma 2.2 的}\ 5M\ \text{取}\ M=1 ✓$$

$$\textbf{扩展代价（该档 §6–§7）}：\text{只需}\ \textbf{先验界}\ m\ ＋\ \text{窗口拉长}\ m\ \text{倍}\ ＋\ \text{常数降级};\ \textbf{m=1 时复现 Thm 4.1} ✓✓$$
$$\boxed{\textbf{该档 §7 判词（逐字）}：\text{"the extension to finitely many zeros is a genuine, cheap generalization,}\ \textbf{but it buys nothing unless you can independently bound the number of off-line zeros"}} ✓✓✓$$
$$\qquad \Longrightarrow \text{故}\ \text{"纯技术推广"}\ \textbf{＝ 是}（\text{用户的第三项审计}）;\ \textbf{但收益条件在一个未知输入上}（m\ \text{对一般}\ F\ \textbf{未知}）✗$$
$$\qquad ⚠️\ \text{该档 §8 自标}：\textbf{未读} \text{Montgomery《Ten Lectures》Ch.5 Thm 11}（＝ Lemma 2.2 的引擎）／Brown 2005／McCurley 1984 ⚠️✓$$

$$\Longrightarrow \boxed{\text{结论}：\textbf{V290 §3 的 A1-3 推荐须降级} —— 它}\ \textbf{技术上便宜但收益为空} \text{（除非另行独立界住离轴零点个数）} ✓✓✓$$

---

## §4 三项审计（逐项回答唐先生）

$$\textbf{① 原定理到底说什么？}：\text{不是"至多一个离轴零点"的定理};\ \text{而是}\ \textbf{"在至多一个例外零点的假设下，该零点存在}\iff\tau\text{-Li 系数超阈值"} ✓✓$$
$$\qquad \text{（}\tau=1\ \text{时例外区域}\ =\ \Re\rho>\tfrac12;\ \tau\ne1\ \text{时}\ =\ \Re\rho>\tfrac{\tau}{2}\ \text{——}\textbf{"至多一个"的内容随}\ \tau\ \text{变}）✓✓$$
$$\textbf{② "有限多个"是否逻辑直接？}：\textbf{不直接} —— \text{原定理}\ \textbf{不含} \text{个数界};\ \text{且唐先生警告成立：}\boxed{\text{逐对象界}\not\Rightarrow\text{类级有限性}}（\text{除非对象族固定或统一参数约束}）✓✓$$
$$\qquad \text{更准确地说：扩展后是}\ \textbf{条件性} \text{判据（假设"至多}\ m\ \text{个"）},\ \text{而}\ m\ \text{恰是}\ \textbf{新的非平凡输入}（`E4` §6–§7）✓✓$$
$$\textbf{③ 机制能否移植？}：\textbf{能，且已被本项目于 09-12 分析过}（`E4` §3–§7）——\ \text{唯一载荷处是 A／B 的记账，检测引擎（Lemma 2.2）}\ \textbf{本就是}\ M\ \text{个复数的陈述} ⟹ \boxed{\text{纯技术推广}} ✓✓$$
$$\qquad ⚠️\ \text{但三份底料未读}（Montgomery Thm 11／Brown 2005／McCurley 1984）⟹ \text{"纯技术推广"的判断}\ \textbf{建立在未读引擎证明的基础上} ⚠️✓$$

---

## §5 ⭐ 纪律新增（N13）

$$\boxed{\textbf{N13}：\text{推荐任何条目之前，必须核对"}\textbf{已验证原文的那份档} \text{"};\ \textbf{不得} \text{依赖 terse 台账行}} ✓✓$$
$$\qquad \text{本条源自本档流程错（凭 `PENDING` A1-3 行推荐，未读 `E4-…`）；}\text{与 N10（先查重）同类但更细} ✓$$

---

## §6 修正后的下一步建议

$$\text{① }\textbf{论文线的真正可交付项}：\text{P1–P8}\（\text{投稿去向／引文核对／送达}\）＋ \text{A1-4}\（Lagarias 测试函数}\ g_n\ \text{显式形式}）✓$$
$$\text{② }\textbf{A1-3 的处置}：\textbf{降级} \text{（技术便宜、收益为空）；若仍要做，须}\ \textbf{先读} \text{`E4` §8 三份未读文献（尤其 Montgomery Thm 11 ＝ 引擎）} ✓$$
$$\text{③ }\textbf{不建议} \text{以 A1-3 为"首攻"};\ \text{若要开论文线，优先}\ \textbf{P6（投稿去向）／P8（引文）／A1-4} ✓$$

---

## §7 边界 ＋ 净产出

```
① ⚠️ 本档 §1 为**亲自抽取正文**（PyPDF2；`pdftotext` 不可用 ⟹ 抽取可能有排版噪声 ⟹ 关键式以 `E4` 档逐字引文交叉核对）✓
② ⚠️ 唐先生检索到的 Stevenhagen 文档**不在本项目 docs 内**（本档核验：归档件首页即为 Palojärvi）⟹ 其检索来源须另行定位 ✓
③ ⚠️ §3 的"纯技术推广"判断**继承 `E4` 档**，而该档 §8 自标"未读引擎证明"⚠️
④ **不声称** A1-3 扩展无价值到"不值得写"程度（仅：收益条件在未知输入 m 上）✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值（本档为文献核验）✓
```

```
① ⚠️ **核验**：归档 PDF ＝ **Palojärvi arXiv:1807.01506v3**（26 页）✓；其摘要为"**至少一个**"方向 ＋ **iff** 判据；**"至多一个"只在假设中** ✓✓
② ⚠️ **T10 勘误**：`V290` §3 的三处错（把条件性判据写成无条件界；混淆假设与结论；凭 terse 行推荐）已更正 ✓✓
③ ⭐⭐⭐ **档案早已完成**：`E4-palojarvi-finitely-many.md`（09-12）已给三条 locus ＋ 扩展代价 ＋ 判词"**cheap but buys nothing unless you can independently bound the number of off-line zeros**" ⟹ **A1-3 推荐降级** ✓✓✓
④ ⭐ **三项审计回答**：① 原定理＝假设下的 iff 判据；② "有限多个"**不**逻辑直接，且**逐对象界 ⇏ 类级有限性**（唐先生警告成立）；③ **纯技术推广**（待读 Montgomery Thm 11）✓
⑤ ⭐ **N13 纪律**：推荐前须核对"已验证原文的档"，不得依赖 terse 台账行 ✓
⑥ ⭐ **修正建议**：论文线优先 P6／P8／A1-4；A1-3 降级（若做，先读三份未读文献）✓
```
