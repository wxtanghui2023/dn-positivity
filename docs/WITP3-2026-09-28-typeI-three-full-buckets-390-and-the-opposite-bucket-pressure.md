# WITP3-2026-09-28 — **$F_p{=}4$ 之 $Q_3$ 结构（✓✓✓）；Type-I 三满桶**可行**（390 组）但"对面桶" $D$-容量掉到 2（✓✓ 新）

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:51 令 ✓）**：Type-I 三满桶耦合（P2）；**零程序计算**（仅有限穷举 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-461／C-460／C-458，非新案 ✓）**
`docs/WITP2-2026-09-28-…`（**完美匹配定理／$D$ 不施压 ✓✓✓**）｜`docs/WITD1-2026-09-28-…`（**$M_C$ 表／$d{=}1$ 四机制 ✓✓✓**）｜`docs/WITPARITY-2026-09-28-…`（**三 extremal ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $F_p{=}4$ 族／$Q_3$ 候选／$D$-容量对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $F_p{=}4$ 之"完美匹配 $\to Q_3$ 候选立方体 $\to$ 两个奇偶类"精确结构（30 个互异 $F$）＋ 首次算出 Type-I 三满桶可行（**390** 组）且"对面桶" $D$-容量由 4 降为 **2**（$(2,4,4,4)$）** ✓）
**[RESEARCH]**

---

## §0 结论（**$Q_3$ 结构 ✓✓✓｜Type-I 可行 ✓（390 组）｜对面桶压力 ✓✓（新）**）

$$\textbf{设定 ✓}:\ \text{偶 bucket }p;\ C_p\subseteq\binom{[6]}2;\ F_p\subseteq\binom{[6]}3\ \text{为 packing}✓;\ D_q\subseteq\binom{[6]}3\ \text{为 packing}✓;\ \text{三偶桶满}\ \big(|F_{p_i}|{=}4\big)✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §1 之结构表述\ \textbf{完全正确}（本档穷举核验 ✓✓✓）}:\ |C_p|{=}3\wedge|F_p|{=}4\iff C_p\ \text{为 }K_6\ \text{完美匹配}}$$
$$\qquad\textbf{（}Q_3\ \text{候选立方体 ✓✓）}:\ \text{取 }C_p{=}\{\{1,2\},\{3,4\},\{5,6\}\}✓ \Longrightarrow \text{避 pair 之 triple}= \text{每匹配边取一点}\ \big(2^3{=}8\ \text{个}\ ✓\big)$$
$$\qquad\qquad\text{恰成 }Q_3{=}\{1/2\}\times\{3/4\}\times\{5/6\}✓✓;\ \text{packing}\iff\text{立方体中两点 Hamming 距离}\ge2\iff\textbf{同奇偶类}✓✓$$
$$\qquad\qquad\Longrightarrow \boxed{\text{两个 4-packing ＝ 两个奇偶类}}\ ✓✓:\ F^{(0)}{=}\{135,146,236,245\},\ F^{(1)}{=}\{136,145,235,246\}✓✓\ \big(\text{与唐先生逐字一致 ✓}\big)$$
$$\qquad\textbf{（计数 ✓✓）}:\ 15\ \text{个完美匹配}\times2\ \text{奇偶类}=30\ \text{个\ \textbf{互异} }F✓✓;\ \text{兼容对 }15{\times}2{=}30✓✓$$
$$\boxed{\textbf{(2) ✓✓唐先生 §2 正确}:\ }\text{跨 }D_q\ \text{之条件＝suffix 集\ \textbf{两两不相交}}\ ✓✓\ \big(\text{非 triple 集不相交 ✗};\ \text{源自 }S{=}S'\Rightarrow d{=}2\ ✗\big);\ |D(p)|\le12✓✓;\ \textbf{无 }D\text{-侧坍缩}\ ✓✓\ \big(\text{C-461 ✓}\big)$$
$$\boxed{\textbf{(3) ✓✓✓Type-I 三满桶\ \textbf{可行}（本档新，且给出计数 ✓✓）}:\ }\text{三偶桶皆 }|F|{=}4\ \text{且两两不相交之}\textbf{无序三元组数}\ ＝\ \mathbf{390}✓✓\ \big(\text{有序 }2340✓\big)$$
$$\qquad\Longrightarrow\ \text{Type I }(0,4,4,4)\ \textbf{未被排除} ✗✓;\ \text{三种 }(M_i,\epsilon_i)\ \text{组合大量存在 ✓✓}$$
$$\boxed{\textbf{(4) ✓✓✓但出现\ \textbf{真正的多桶耦合}（新）}:\ }\text{Type I 中，与"空桶"相对的那个奇 }q^*\ \big(\text{其三偶邻恰为三个满桶}\big):$$
$$\qquad\bigcup_{p\sim q^*}F_p=F_1\cup F_2\cup F_3\ \big(12\ \text{个 triple}\ ✓\big)\Longrightarrow \text{可用}＝20-12=\mathbf8\Longrightarrow \boxed{\max|D_{q^*}|=\mathbf2}✓✓\ \big(\text{由 8 个 triple 的 packing 最大仅 }\le2✓\big)$$
$$\qquad\textbf{（其余三个奇桶 ✓）}:\ \text{各邻 2 满桶}\ \big(\cup{=}8\big)\Longrightarrow \text{可用 12}\Longrightarrow\max|D_q|=\mathbf4✓$$
$$\qquad\Longrightarrow\ \boxed{\text{Type-I 之 }D\text{-容量谱}=(2,4,4,4)}\ ✓✓\Longrightarrow \sum_q|D_q|\ \le\ \mathbf{2+4+4+4=14}✓✓\ \big(\text{原一律 16 ✗}\big)$$
$$\qquad\textbf{读法 ✓✓}:\ \text{“三个 }F{=}4\ \text{桶共享一个对面奇桶"之结构 ⟹ 该桶\ \textbf{被三个满桶的禁配夹住} ⟹ 容量减半 ✓✓（＝唐先生所求之\ \textbf{多桶耦合}\ ✓）}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓✓}:\ \text{完美匹配}\to Q_3\ \text{候选}\to2\ \text{奇偶类}\ ✓✓✓;\ 15{\times}2{=}30\ ✓✓;\ \text{且 30 个 }F\ \text{互异 ✓✓（穷举 ✓）};\ \text{立方体读法 ✓✓}$$
$$\textbf{§2 ✓✓}:\ \text{跨 }D\ \text{条件＝suffix 集不交 ✓✓};\ \text{单 }D_q\ \text{内 }|S\cap S'|\le1✓✓;\ |D(p)|\le12✓✓;\ "D\ \text{杀不掉边界"\ ✓✓\ \big(\text{＝C-461 ✓}\big)}$$
$$\textbf{§3 ✓✓}:\ F\text{-profile}\to C\text{-profile}\ \text{之表 ✓✓\ \big(\text{C-461 ✓}\big)};\ \text{Type I}\Rightarrow|C_{p_i}|{=}3\Rightarrow|C|{\ge}9✓✓;\ \text{Type II}\Rightarrow|C|{\ge}3✓;\ \text{Type III 无 ✓}$$
$$\textbf{§4 ✓✓（方向 ✓，且本档已部分执行 ✓）}:\ \text{"多个完美匹配之耦合"\ \textbf{是正确靶点} ✓✓};\ \text{唯 }Q_3\ \text{中偶点三元组：四个偶点取三个 ⟹ 四种，且由 }V_4\ \text{平移\ \textbf{互相等价} ✓（故 390 组已覆盖全部情形 ✓）}$$
$$\qquad\textbf{⚠️（一处须补）}:\ \text{Type-II 之三个 }|F_p|{=}2\ \text{桶}\ \textbf{不由 }C_p\ \text{单独确定} ✗\ \big(\text{只知 }|C_p|\le9✓\big)\Longrightarrow\ \text{其 }D\text{-耦合需额外输入 ✓（登记 ✓）}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{\text{完美匹配}\to Q_3\to2\ \text{奇偶类}}✓✓✓;\ \text{② 30 个互异 }F✓✓;\ \text{③ Type-I 可行（}\mathbf{390}\ \text{组}\big)✓✓;\ \text{④ }\boxed{\text{Type-I }D\text{-谱}=(2,4,4,4)}\Rightarrow\sum\le14✓✓✓;\ \text{⑤ 跨 }D\ \text{＝suffix 集不交 ✓✓};\ \text{⑥ }|C|{\ge}9\ \big(\text{Type I}\big)✓✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}D\ \text{杀 }(|F_p|{=}4,|C_p|{=}3)\text{"}\ ✗;\ \text{"Type-I 三满桶被排除"\ ✗};\ \text{"}\sum_q|D_q|\le16\ \text{为紧"\ ✗\ \big(\text{实 }14\big)}$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ M\ \text{之真值};\ \text{（}C\text{-侧 }9\le|C|\le12\ \text{与 }D\text{-侧 }\le14\ \text{之联合尚未成式 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① }C\text{-侧：三完美匹配 ＋ 第四桶之联合可行性（}|C|\le12✓\big)✓;\ \text{② }D\text{-侧：由 }(2,4,4,4)\ \text{谱反推四桶之联合预算 ✓;\ \text{③ Type-II 之 }|F_p|{=}2\ \text{桶结构分类（须新输入 ✓）}}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "奇偶类" "候选立方体" "对面桶压力"
技术词 奇偶类     命中文件数=0    ::
技术词 候选立方体 命中文件数=0    ::
技术词 对面桶压力 命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 奇偶类 | 0 | 0 | ✓（自造标签 ✓） |
| 候选立方体 | 0 | 0 | ✓（自造标签 ✓） |
| 对面桶压力 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限穷举：$15$ 匹配 × $2$ 奇偶 × $\binom{30}3$ 三元组 ＋ 各桶 packing ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处须补**（Type-II 之 $|F_p|{=}2$ 桶非 $C$-确定）已在 §1 标注 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
