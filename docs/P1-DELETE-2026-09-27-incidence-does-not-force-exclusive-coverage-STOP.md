# P1-DELETE-2026-09-27 — **窄问题攻坚**：三重 incidence 能否迫使独占覆盖？**答：不能** ⟹ **建议 STOP $4\to5$ 线**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 23:35 令 ✓）**：① 打窄问题"incidence ⟹ 独占覆盖／不可删性 witness？"；② 按硬判据给出 STOP/继续；零程序计算 ✓。

**已查地图：命中（接续 C-424／C-423／C-422，非新案 ✓）**
`docs/P1-GLOBAL-2026-09-27-…`（**三重相关恒等式／过门** ✓✓）｜`docs/P1-BRIDGE-2026-09-27-…`（**零需求／无桥** ✓✓）｜`docs/P1-L5-2026-09-27-…`（**4-面判定／精细容量** ✓✓）｜`docs/R4-P1-2026-09-27-…`（**$p(c)$／可删性判据** ✓✓）｜`docs/P1-SCREEN-…`（**C-418 门** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，**两空间皆 0**，见 §6）
D0: 本档对象 ＝ **档案已有** 三重 incidence／可删性对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 incidence 的精确局部分解（$\iff i\in S(y)$）＋ "无 forcing"判定 ＋ 案例分裂 caveat ＋ STOP 判定** ✓）
**[RESEARCH]**

---

## §0 结论（**精确分解 ✓✓｜无 forcing ✗✓｜案例分裂 ✓｜STOP 建议 ✓**）

$$\boxed{\textbf{(1) 精确分解（本档补 ✓）}:\ T(C)=\sum_{c\in C}\Big[\ \sum_{u\in M_4^{\rm int}(c)}d_1(c\oplus e_u)\ \big(\text{C-421 适用 ✓}\big)\ +\ \sum_{u\in M_4(c)\setminus\mathrm{int}}\big|E_5(u)\big|\ \big(\text{非内部部分，C-424 §0(3) 未列 ✓}\big)\ \Big]}\ ✓$$
$$\boxed{\textbf{(2) ★incidence 的精确内容（新 ✓✓）}:\ \text{三重 }(c,\ y=c\oplus e_u,\ z=c\oplus e_v)\ \big(u\subset v,\ v=u\cup\{i\}✓\big)\iff\boxed{i\in S(y)}\ ✓✓}$$
$$\qquad\Longrightarrow\ \text{incidence 是\textbf{关于 }y\ \text{的局部邻域}的纯局部陈述} ⟹ T(C)\ \text{＝逐中心局部数据的\textbf{求和}} ⟹ \textbf{跨中心只体现在求和、不体现在对象本身}⚠️✓$$
$$\boxed{\textbf{(3) ★窄问题答案：无 forcing ✗}:\ \text{incidence 仅钉住 }i\in S(y);\ \text{而 }y\ \text{的不可删性} ⟺ \big|S(y)\cup V(H_y)\big|\le9✓\ \text{（R4-P1 ✓）}}$$
$$\qquad\text{二者\textbf{无关} ⟹ }S(y)\cup V(H_y)=[10]\ \text{（每坐标被触及 ⟹ }y\ \textbf{可删}✓\big)\ \text{与 incidence \textbf{兼容}} \Longrightarrow \boxed{\text{incidence}\ \not\Rightarrow\ \text{独占覆盖}}✗✓$$
$$\boxed{\textbf{(4) 案例分裂（诚实必需 ✓）}:\ "\text{119 最小性}"\ \textbf{不可无条件假设}✗}:\ \text{若某 119-cover 含可删字}⟹\exists\,118\text{-cover}⟹K(10,1)\le118\ ✓\big(\text{更强的上界、属\textbf{另一案}}✓\big)$$
$$\boxed{\textbf{(5) STOP 判定（照唐先生硬判据 ✓）}:\ \textbf{建议 STOP 此 }4\to5\ \text{incidence 线}✓;\ \text{证据四行见 §5};\ \textbf{不再向 layer 6／7 堆叠}✓}$$

---

## §1 **$T(C)$ 的精确分解**（**本档补 ✓**）

$$T(C):=\sum_{u\subset v,\,|u|=4,|v|=5}\big|C\cap(C\oplus e_u)\cap(C\oplus e_v)\big|=\sum_{c\in C}\#\{u\subset v:c\oplus e_u,\ c\oplus e_v\in C\}✓$$
$$\qquad=\sum_{c}\ \sum_{u\in M_4(c)}\ \#\{i\notin u:c\oplus e_u\oplus e_i\in C\}=\sum_c\sum_{u\in M_4(c)}\big|E_5(u)\big|✓$$
$$\textbf{与 C-421 拼接 ✓}:\ \text{对 }u\subseteq S(c)\ \big(\text{内部 ✓}\big):\ \big|E_5(u)\big|=d_1(c\oplus e_u)✓;\ \text{对 }u\not\subseteq S(c):\ \big|E_5(u)\big|=d_1(c\oplus e_u)-\#\{j\in u:c\oplus e_{(u\setminus j)}\in C\}✓$$
$$\Longrightarrow\ \text{§0 (1) 成立}✓\ \big(\text{C-424 §0(3) 只列了内部部分 ⟹ 此处\textbf{补齐}}✓\big)$$

## §2 **incidence 的精确内容**（**✓✓**）

$$\text{设 }u\subset v,\ |u|=4,\ |v|=5 \Longrightarrow v=u\cup\{i\},\ i\notin u \Longrightarrow c\oplus e_v=c\oplus e_u\oplus e_i=y\oplus e_i✓$$
$$\Longrightarrow\ \big(c\oplus e_v\in C\big)\iff\big(y\oplus e_i\in C\big)\iff i\in S(y)✓✓$$
$$\textbf{读法 ✓✓}:\ \text{incidence 的全部内容 ＝ }y\ \text{有一个方向 }i\notin u\ \text{的一阶邻居}\ \Longrightarrow\ \textbf{无额外跨中心信息}⚠️;\ T(C)\ \text{的"全局性"仅来自对 }c\ \text{求和}✓$$
$$\textbf{（何以此前像"跨中心" ✓）}:\ C\cap(C\oplus e_u)\cap(C\oplus e_v)\ \text{是按 }c\ \text{写的三重交}✓;\ \text{但交换求和后每项只依赖一个 }c\ \text{的局部数据 ✓（§1 ✓）}$$

## §3 **窄问题的答案：无 forcing**（**✗✓ 诚实**）

$$\textbf{（不可删性回顾 ✓ R4-P1）}:\ y\ \text{可删}\iff p(y)=0\iff\big|S(y)\cup V(H_y)\big|=10✓;\ \text{不可删}\iff \big|S(y)\cup V(H_y)\big|\le9✓$$
$$\qquad\text{（}S(y)=\{j:y\oplus e_j\in C\}✓;\ V(H_y)=\text{距离-2 邻居所触及的坐标集}✓\big)$$
$$\textbf{（无关性 ✓）}:\ \text{incidence 只给出 }i\in S(y)\ ✓;\ \text{而 }\big|S(y)\cup V(H_y)\big|\ \text{可独立地取 }1,\dots,10✓\ \text{（无约束 ✓）}$$
$$\qquad\Longrightarrow\ \big|S(y)\cup V(H_y)\big|=10\ \text{（}y\ \text{可删 ✓）与 incidence \textbf{相容}}✓ \Longrightarrow \textbf{incidence 不迫使独占覆盖}✗✓$$
$$\textbf{（构造性支持 ✓）}:\ C_1\ \text{型族（C-420 ✓）中 }y=e_u\ \text{有 }E_5(u)=\varnothing✓,\ \text{且（在只含 }0,e_i,e_w\ \text{的族里）}S(y)\cup V(H_y)\ \text{小 ⟹ }y\ \text{不可删}✓\ \text{—— 反向兼容同样存在 ✓}$$
$$\qquad\Longrightarrow\ \text{两种极端（可删／不可删）皆与 incidence 相容} \Longrightarrow \textbf{该 witness 机制不存在}✗✓$$

## §4 **案例分裂 caveat**（**✓ 必须写**）

$$\textbf{"119 最小性"的合法形态 ✓}:\ \text{只有在 }K(10,1)=119\ \text{时，任何 119-cover 才自动最小}✓;\ \text{而 }K(10,1)\le118\ \text{时 119-cover 可含可删字}✓$$
$$\textbf{（分案 ✓）}:\ \text{Case A}:\ K(10,1)=119\Longrightarrow\text{最小性可用}✓;\ \text{Case B}:\ \text{存在 119-cover 含可删字}\Longrightarrow K(10,1)\le118\ ✓\big(\textbf{更强上界、独立成果}✓\big)$$
$$\Longrightarrow\ \text{故"最小性"是\textbf{条件假设}（Case A ✓），\textbf{不可}无条件引用 ✗✓};\ \text{本档的 STOP 判定\textbf{不依赖}该假设 ✓（见 §5 ✓）}$$

## §5 **STOP 判定**（**照唐先生硬判据 ✓**）

$$\textbf{证据四行 ✓}:\quad\text{① \textbf{covering 侧零输入}}✓\ \big(\text{C-423 零需求 ⟹ 唯一"下层"来源为空 ✓}\big);\qquad\text{② }T(C)\ \text{＝局部数据的\textbf{求和}}✓\ \big(\text{§1／§2 ✓}\big)$$
$$\qquad\text{③ incidence \textbf{无局部 forcing 内容}}✗\ \big(\text{§3 ✓}\big);\qquad\text{④ 唯一可行推导形态＝逐 }c\ \text{用 C-422 的\textbf{上界}再求和 ⟹ 只得上界}✗\ \big(\text{无法与 C-419 的\textbf{下界需求}碰撞 ✓}\big)$$
$$\Longrightarrow\ \boxed{\textbf{STOP 此 }4\to5\ \text{incidence 线}}✓\ \big(\textbf{路线级 STOP}✓\ \text{—— \textbf{不}是对 119 的断言 ✗（V290 ✓）}\big);\ \textbf{不再向 layer 6／7 堆叠}✓$$
$$\textbf{（保留项 ✓✓）}:\ \text{① C-421 接口恒等式（结构资产 ✓）};\ \text{② C-422 精细容量（排列级上界 ✓）};\ \text{③ C-423 零需求引理（防错 ✓）};\ \text{④ C-424 三重相关恒等式（对象层 ✓）};\ \text{⑤ C-419 折衷关系（HOLD ✓）}$$
$$\textbf{（为何是"方向不匹配"而非"缺一个恒等式" ✓）}:\ \text{上层 incidence 需要\textbf{下界}输入来碰撞 C-419 的下界需求};\ \text{而所有覆盖侧输入都是\textbf{下层}（单调下型 ✓）} \Longrightarrow \textbf{方向系统性错配}✓✓$$

## §6 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "不可删性" "独占覆盖" "案例分裂" "方向不匹配"
技术词 不可删性      命中文件数=0    ::
技术词 独占覆盖      命中文件数=0    ::
技术词 案例分裂      命中文件数=0    ::
技术词 方向不匹配    命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 不可删性 | 0 | 0 | 0（本档自造标签 ✓） |
| 独占覆盖 | 0 | 0 | 0（本档自造标签 ✓） |
| 案例分裂 | 0 | 0 | 0（本档自造标签 ✓） |
| 方向不匹配 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（四词**两空间皆 0** ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 精确分解 ＋ §2 incidence 分解 ＋ §3 无 forcing ＋ §4 case split ＋ §5 STOP**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§6 已分栏 ✓）
- **STOP 是\*\*路线级\*\***（$4\to5$ incidence ✓），**不是**对 119 的断言 ✗✓；**不声称** P1 成立／不成立 ✗（V290 ✓）
- §4 的 case split **必须与 STOP 判定同引** ✓（防把"最小性"当无条件假设 ✗）；§5 的保留项**不得随 STOP 一起废弃** ✓
