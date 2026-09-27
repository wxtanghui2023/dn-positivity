# P1-GLOBAL-2026-09-27 — **状态锁 ＋ 跨中心全局耦合**：三重相关全局恒等式（过 C-418 门）＋ 覆盖侧仍缺

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 23:33 令 ✓）**：① 锁定五格状态；② 检验"跨 block／跨中心的全局耦合"是否存在且过 C-418 门；零程序计算 ✓。

**已查地图：命中（接续 C-423／C-422／C-421，非新案 ✓）**
`docs/P1-BRIDGE-2026-09-27-…`（**局部无需求／无桥定理** ✓✓）｜`docs/P1-L5-2026-09-27-…`（**4-面判定／精细容量** ✓✓）｜`docs/P1-D5-…`（**layer-5 接口** ✓✓）｜`docs/P1-NINT-…`（**折衷关系** ✓✓）｜`docs/P1-SCREEN-…`（**C-418 门** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词，**已分线**，见 §5）
D0: 本档对象 ＝ **档案已有** $4\leftrightarrow5$ 全局耦合对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出跨中心的\*\*三重相关全局恒等式\*\*（$\sum_c I(c)=\sum_{u\subset v}|C\cap(C\oplus e_u)\cap(C\oplus e_v)|$）＋ 过门判定 ＋ 覆盖侧缺失的显式登记** ✓）
**[RESEARCH]**

---

## §0 结论（**状态锁 ✓｜全局恒等式 ✓✓｜过门 ✓✓｜覆盖侧仍缺 ⚠️**）

$$\boxed{\textbf{(1) 状态锁（照唐先生 23:33 ✓）}:\ \underbrace{\text{local layer-5 forcing: STOP}}_{\text{C-423 §1}}\ \Big|\ \underbrace{\text{local missing-set: STOP}}_{\text{C-421 §2}}\ \Big|\ \underbrace{\text{profile/capacity bridge: STOP}}_{\text{C-409／C-417}}\ \Big|\ \underbrace{\text{global }4\leftrightarrow5\text{ incidence: HOLD}}_{\textbf{本档}} \ \Big|\ \underbrace{\text{C-422 structural asset: LIVE}}_{\text{保留 ✓}}}$$
$$\qquad\textbf{（照唐先生 ✓）}:\ \textbf{不}把整个方向 CLOSED ✗;\ \text{最关键新增信息 ＝ C-423 的\textbf{零需求证明} ⟹ }M_4^{\rm int}\ne\varnothing\ \not\Rightarrow\ M_5\ne\varnothing✓,\ \text{且 }E_5(u)=0\ \text{与局部覆盖职责\textbf{完全兼容}}✓$$
$$\boxed{\textbf{(2) ★跨中心全局恒等式（新 ✓✓）}:\ \boxed{\sum_{c\in C}I(c)\ =\ \sum_{u\subset v,\,|u|=4,|v|=5}\big|C\cap(C\oplus e_u)\cap(C\oplus e_v)\big|}\ ✓✓}$$
$$\qquad\textbf{（推导 ✓）}:\ I(c)=\#\{u\subset v:c\oplus e_u\in C,\ c\oplus e_v\in C\}✓ \Longrightarrow \text{交换求和次序即得 ✓（＝\textbf{三重相关}之和 ✓）}$$
$$\boxed{\textbf{(3) 过 C-418 门 ✓✓}:\ \text{该量是\textbf{三重相关}级（排列级 ✓）};\ \text{对内部块由 C-421 有 }I(c)=\sum_{u\in M_4^{\rm int}(c)}d_1(c\oplus e_u)\ ✓}$$
$$\qquad\Longrightarrow\ \text{它依赖"\textbf{哪些} }u\ \text{是内部块"与"\textbf{哪些}码字在何处"（排列 ✓） ⟹ \textbf{非 degree/profile 函数} ⟹ \textbf{过门}✓✓\ \big(\text{故"过门的全局对象"\textbf{确实存在}}✓\big)}$$
$$\boxed{\textbf{(4) ⚠️ 覆盖侧仍缺（诚实）}:\ \text{C-423 的零需求引理 ⟹ \textbf{无局部覆盖下界}};\ \text{该量的覆盖侧不等式仍无}✗ \Longrightarrow \textbf{HOLD}✓}$$

---

## §1 **全局恒等式的推导**（**交换求和 ✓✓**）

$$I(c):=\#\{(u,v):u\in M_4(c),v\in M_5(c),u\subset v\}\ ✓;\qquad |v|=5,|u|=4,u\subset v\iff v=u\cup\{i\},\ i\notin u✓$$
$$\sum_{c\in C}I(c)=\sum_{c\in C}\ \sum_{u\subset v}\ \mathbf 1\big[c\oplus e_u\in C\big]\mathbf 1\big[c\oplus e_v\in C\big]\ \big(\text{含 }c\in C\ \text{由求和范围 ✓}\big)$$
$$\qquad\overset{\text{交换}}{=}\sum_{u\subset v}\sum_{c\in C}\mathbf 1\big[c\oplus e_u\in C\big]\mathbf 1\big[c\oplus e_v\in C\big]=\sum_{u\subset v}\big|C\cap(C\oplus e_u)\cap(C\oplus e_v)\big|\ ✓✓$$
$$\textbf{读法 ✓}:\ \text{右侧对 }\binom{10}4\cdot6=210\cdot6=1260\ \text{个 }(u\subset v)\ \text{对求"三重相关"}\ \big|\{c:c,\ c\oplus e_u,\ c\oplus e_v\in C\}\big|✓\ \text{—— \textbf{跨中心}（}c\ \text{跑遍整个 }C✓\big)✓✓$$
$$\textbf{性质 ✓}:\ \text{三重相关\textbf{不由}距离分布 }\{A_i\}\ \text{决定（与 C-418 的门判据一致 ✓）};\ \text{且它不是 }\{n_j\}\ \text{或 }\{N_j\}\ \text{的函数 ✓✓}$$

## §2 **过门判定**（**✓✓ 本档对唐先生问题的正面答复**）

$$\textbf{问 ✓}:\ \text{是否存在一个"跨 block／跨中心的全局耦合"且\textbf{过 C-418 门}？} \Longrightarrow \ \textbf{答：对象存在 ✓✓（§1）}$$
$$\qquad\textbf{（门检验 ✓）}:\ S1\ \text{仅依赖度数／聚合？} \textbf{否}✗（依赖排列 ✓）;\ S2\ \text{依赖排列／交叠？} \textbf{是}✓;\ S3\ \text{范围闸}:\ \text{定义于任意 }119\text{-cover ✓} \Longrightarrow \textbf{PASS}✓✓$$
$$\textbf{（同一对象的三重形态 ✓）}:\ \text{① }\sum_cI(c)\ \text{（中心视角 ✓）};\ \text{② }\sum_{u\subset v}|C\cap(C\oplus e_u)\cap(C\oplus e_v)|\ \text{（三重相关视角 ✓）};\ \text{③ }\sum_c\sum_{u\in M_4^{\rm int}(c)}d_1(c\oplus e_u)\ \text{（内部块视角 ✓，须配 C-421 ✓）}$$
$$\Longrightarrow\ \boxed{\text{"过门的全局量"确实存在}}✓✓\ \big(\text{这回答了"是否有全局耦合可写"的\textbf{对象层面}问题 ✓}\big)$$

## §3 **覆盖侧为何仍缺**（**⚠️ 诚实 ＋ 照唐先生判据 ✓**）

$$\textbf{零需求引理（C-423）✓}:\ \text{内部块的 6 个 layer-5 点已被 }y\ \text{覆盖} \Longrightarrow \text{无局部需求 ⟹ \textbf{无局部下界}}✓$$
$$\textbf{全局亦是 ✓}:\ \text{covering 是"逐点 }\ge1\text{"（单调下型 ✓）} \Longrightarrow \text{它只能产生\textbf{下层}结论（覆盖需求 ✓）};\ \text{而 }\sum_cI(c)\ \text{统计的是\textbf{码字的邻接 incidence}（上层 ✓）}$$
$$\qquad\Longrightarrow\ \text{两者\textbf{对象不同}（C-423 §2 无桥定理 ✓）} \Longrightarrow \textbf{覆盖侧不等式仍无}✗✓$$
$$\textbf{（照唐先生判据 ✓）}:\ \text{若找不到"过 C-418 门且有覆盖侧独立不等式"的全局量}\ \Longrightarrow\ \text{此 }4\to5\ \text{线应 STOP}✗$$
$$\qquad\textbf{现状 ✓}:\ \text{对象过门 ✓，但覆盖侧不等式\textbf{未得}✗} \Longrightarrow \textbf{HOLD}✓\ \big(\text{既未到 STOP（对象已过门 ✓）、也未到 P1（覆盖侧缺 ✗）}\big)$$

## §4 状态与下一步（**诚实 ＋ 最后一步判据 ✓**）

$$\textbf{已确立 ✓}:\ \text{① 五格状态（§0 (1) ✓）};\ \text{② 全局恒等式（三重相关 ✓✓）};\ \text{③ 过门（对象存在 ✓✓）};\ \text{④ 覆盖侧缺失的\textbf{原因}（无桥 ✓✓）}$$
$$\textbf{唯一剩余形态 ✓}:\ \text{要形成碰撞，须\textbf{不}经"内部块自身负责的 layer-5 点"（C-423 ✗），而须经\textbf{跨中心}约束：}$$
$$\qquad\text{① 119 的\textbf{全局最小性}能否约束三重相关 }\sum_{u\subset v}|C\cap(C\oplus e_u)\cap(C\oplus e_v)|\ ?$$
$$\qquad\text{② 若能，且证明\textbf{不是} C-409／C-417 型 profile 重包装（过 C-418 ＋ 独立性闸 ✓）⟹ 真正的新 P1 ✓}$$
$$\qquad\text{③ 若不能 ⟹ 照判据 \textbf{STOP} 此 }4\to5\ \text{线，不再堆 layer identities}✓\ \big(\text{照唐先生 23:33 ✓}\big)$$
$$\textbf{（登记未做 ⚠️）}:\ \text{上述 ① 的检验＝下一步唯一动作；本档\textbf{未}做（零程序计算 ✓）}$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "三重相关" "跨中心耦合" "全局接口恒等式"
技术词 三重相关      命中文件数=3    :: ./NEGATIVE-RESULTS-2026-09-12-ROUND.md ./A3-third-moment-barrier.md ./A3-break-682-attempt.md
技术词 跨中心耦合    命中文件数=1    :: ./LEDGER-2026-09-27-k101-closed-form-and-next-round-protocol.md
技术词 全局接口恒等式 命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 三重相关 | 0（`A3-*`／`NEGATIVE-RESULTS-*` **属线未定 ⟹ 不计** ✗） | 3 | 0（既有词 ✓） |
| 跨中心耦合 | 1（`LEDGER-2026-09-27-k101-…` ✓） | 0 | 0（既有词 ✓） |
| 全局接口恒等式 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（`全局接口恒等式` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`跨中心耦合` 本线已有 ✓、`三重相关` 的命中**未定／空间 A ⟹ 不计** ✗）
- **注 ✓**：本档实质＝**§1 全局恒等式 ＋ §2 过门 ＋ §3 覆盖侧缺失 ＋ §4 判据**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **不声称** $4\to5$ 线已死 ✗（照判据：须覆盖侧不可能才 STOP ✓）；**不声称** 三重相关路线有效 ✗；**不声称** P1 成立 ✗（V290）
- §3 的"对象不同 ⟹ 无桥"**必须与 C-423 同引** ✓；§4 的"STOP 判据"**必须保留** ✓（防无限堆 layer identities ✗）
