# P1-D5-2026-09-27 — **缺失邻居的坐标结构**：精确结构恒等式（新 ✓✓）＋ layer-5 接口 ＋ 诚实判定（接口不给矛盾 ✗）

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 23:24 令 ✓）**：用 $d_1(y)\le6$ 的**缺失邻居坐标结构**（非数值 6 ✓）；零程序计算 ✓；**不升级任何项** ✓。

**已查地图：命中（接续 C-420／C-419／P1-MICRO，非新案 ✓）**
`docs/P1-B4-2026-09-27-…`（**$S(y)\cap u=\varnothing$／$d_1(y)\le6$／$C_1$ 无界** ✓✓）｜`docs/P1-NINT-2026-09-27-…`（**折衷关系** ✓✓）｜`docs/P1-SCREEN-2026-09-27-…`（**C-418 门** ✓✓）｜`docs/P1-MICRO-2026-09-27-…`（**$(\alpha)(\alpha')$** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词，**已分线**，见 §5）
D0: 本档对象 ＝ **档案已有** 内部块邻域对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出内部块度数的\*\*结构恒等式\*\*（$d_1(c\oplus u)=\#\{i\notin u:c\oplus e_u\oplus e_i\in C\}$，把 layer-5 接入本线）＋ 缺失坐标结构的等价性判定** ✓）
**[RESEARCH]**

---

## §0 结论（**精确结构恒等式 ✓✓｜缺失结构无新信息 ✗｜接口不给矛盾 ⚠️**）

$$\boxed{\textbf{(1) ★精确结构恒等式（新 ✓✓）}:\ \text{内部块 }y=c\oplus u\ \big(u\subseteq S(c),|u|=4✓\big) \Longrightarrow \boxed{d_1(y)\ =\ \#\{i\notin u:\ c\oplus e_u\oplus e_i\in C\}}\ ✓✓}$$
$$\qquad\textbf{读法 ✓✓}:\ \text{内部块的\textbf{全部}一阶邻居恰是\textbf{重量 5 码字}}\ c\oplus e_u\oplus e_i\ (i\notin u✓)\ \Longrightarrow\ \textbf{第一次把 layer-5 接入本线}✓✓;\ \text{且 }d_1(y)\le|\{i\notin u\}|=6✓\ \big(\text{＝C-420 的结构版 ✓}\big)$$
$$\boxed{\textbf{(2) 缺失坐标结构的判定 ✗}:\ "缺失集\supseteq u"\ \text{由 }(\alpha)\ \text{解释（}u\subseteq S(c)\Rightarrow u\cap S(y)=\varnothing✓\big) \Longrightarrow \textbf{不提供超出 }b_4\ \text{定义的新信息}✗✓}$$
$$\boxed{\textbf{(3) 存在侧结构自由 ⚠️}:\ \{i\notin u:c\oplus e_u\oplus e_i\in C\}\ \textbf{不受}\ (\alpha)\ \text{（重量 2／3 ✓）与 }A(c)=0\ \text{约束} \Longrightarrow \textbf{接口未产生 demand }>\text{ capacity}⚠️}$$
$$\boxed{\textbf{(4) 状态（照唐先生 23:24 ✓）}:\ \textbf{avoidance: STOP}✗\ |\ \textbf{profile/capacity: STOP}✗\ |\ \textbf{内部 block 邻接结构: LIVE}✓;\ \text{C-419 HOLD}✓;\ \text{本档未形成新全局约束}✗}$$

---

## §1 **结构恒等式的证明**（**逐 $i$ ✓✓**）

$$\text{设 }y=c\oplus u\in C\ \big(u\subseteq S(c),|u|=4✓\big);\quad d_1(y)=\#\{i:y\oplus e_i\in C\}✓$$
$$\textbf{情形 }i\in u\ ✓:\ y\oplus e_i=c\oplus e_{(u\setminus i)}✓\ \big(\text{重量 3、支撑}\subseteq S(c)✓\big)\ \overset{(\alpha)}{\Longrightarrow}\ \notin C✓ \Longrightarrow \text{不计数}✓$$
$$\textbf{情形 }i\notin u\ ✓:\ y\oplus e_i=c\oplus e_u\oplus e_i✓\ \big(\text{重量 5 ✓}\big) \Longrightarrow\ \text{计数当且仅当}c\oplus e_u\oplus e_i\in C✓$$
$$\Longrightarrow\ \boxed{d_1(c\oplus u)=\#\{i\notin u:c\oplus e_u\oplus e_i\in C\}}\ ✓✓\qquad \text{（含上界 }d_1\le6✓\ \text{作为系 ✓）}$$
$$\textbf{对偶读法 ✓}:\ \text{称 }c\oplus e_u\oplus e_i\ (i\notin u)\ \text{为"由 }c\ \text{与内部块 }u\ \text{生成的 weight-5 点"✓} \Longrightarrow \text{内部块的邻居 ＝ 该生成集的 }C\text{-成员 ✓}$$

## §2 **缺失坐标结构**（**判定 ✗**）

$$\textbf{已证 ✓（C-420 §1）}:\ u\subseteq S(c)\Longrightarrow u\cap S(y)=\varnothing✓;\ \text{即"\textbf{缺失集}\ \mathrm{miss}(y):=[10]\setminus S(y)\ \textbf{包含 }u"✓}$$
$$\textbf{结构内容 ✓}:\ 4=|u|\ \le\ |\mathrm{miss}(y)|=10-d_1(y)\ \le\ 10 \Longrightarrow d_1(y)\le6✓\ \text{（与 §1 一致 ✓）}$$
$$\textbf{⚠️ 判定 ✗}:\ \text{"}\mathrm{miss}(y)\supseteq u\text{" 的内容\textbf{就是 }u\subseteq S(c)✓\ \text{（经 }(\alpha)\ \text{解释 ✓）} \Longrightarrow \text{它\textbf{等价}于 }b_4\ \text{的定义条件 ✓（"哪些 }u\ \text{是内部块"✓）}$$
$$\qquad\Longrightarrow\ \text{故\textbf{单靠缺失集}不能产生新量 ✗（再走一步就会退回 C-417／C-419 的同源链 ✓）}$$

## §3 **存在侧为何自由**（**⚠️ 本档的真正接口**）

$$\text{自由部分是 }S(y)\cap\big([10]\setminus u\big)=\{i\notin u:c\oplus e_u\oplus e_i\in C\}\ \text{（＝§1 的生成集 ✓）}$$
$$\textbf{为何不受约束 ✓}:\quad\text{① }(\alpha)\ \text{只覆盖重量 2／3（以 }c\ \text{为中心 ✓）};\ \text{② }A(c)=0\ \text{只管重量 2}✗;\ \text{③ 重量 5 点\textbf{不}在 }(\alpha')\ \text{的已证范围内}✗✓$$
$$\qquad\Longrightarrow\ \text{该生成集可任意（}\subseteq\{i\notin u\}\text{，}\le6\ \text{个 ✓）} \Longrightarrow \textbf{接口处无 demand }>\text{ capacity}✗⚠️$$
$$\textbf{（但接口本身有价值 ✓✓）}:\ \text{它把"内部块"与\textbf{重量 5 层}绑定} \Longrightarrow \text{若将来能对重量 5 层建立独立约束（非 avoidance／非容量 ✓），则将直接回传到 }b_4✓$$
$$\qquad\textbf{（注 ✓）}:\ \text{这与 C-418 的"下一个候选须在 degree profile 之外"一致：重量 5 层的\textbf{排列}信息正是该类型 ✓}$$

## §4 状态锁与下一步（**照唐先生 23:24 ✓**）

$$\boxed{\textbf{avoidance: STOP}✗\quad\textbf{profile/capacity: STOP}✗\quad\textbf{内部 block 的邻接结构: LIVE}✓}$$
$$\textbf{已确立 ✓}:\ \text{① 结构恒等式（layer-5 接口 ✓✓）};\ \text{② 缺失集无新信息 ✗};\ \text{③ 存在侧自由 ⚠️};\ \text{④ C-420 结论（}C_1\Rightarrow b_4\ \text{可达 210 ✓）保留 ✓}$$
$$\textbf{未确立 ✗}:\ b_4\ \text{的独立控制}✗;\ \text{新全局约束}✗;\ \text{无矛盾}✓$$
$$\textbf{下一步（登记未做 ⚠️）}:\ \text{① 对 weight-5 层建\textbf{排列级}约束（非 avoidance／非容量 ✓）；② 用"生成集"定义新的 global 量（如 }\sum_{u}\big|\{i\notin u:c\oplus e_u\oplus e_i\in C\}\big|\ \text{的排列敏感函数 ✓）；③ 检验其是否与 }119\ \text{的覆盖需求碰撞 ⚠️}$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "邻居结构恒等式" "第五层接口" "缺失坐标"
技术词 邻居结构恒等式 命中文件数=0    ::
技术词 第五层接口    命中文件数=0    ::
技术词 缺失坐标      命中文件数=4    :: ./REVERSE-0-counterexample-invisible-kernel-scan.md ./CC-INVERSION-STAGE-REGISTRATION.md ./ASSETS-REGISTRY.md
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 邻居结构恒等式 | 0 | 0 | 0（本档自造标签 ✓） |
| 第五层接口 | 0 | 0 | 0（本档自造标签 ✓） |
| 缺失坐标 | 2（`ASSETS-REGISTRY.md`／`SEARCH-FIREWALL.md` ✓） | 2（`REVERSE-0-…`／`CC-INVERSION-…` **属线未定 ⟹ 不计** ✗） | 0（既有词 ✓） |

- **本档新增**：**0** 个术语 ✓（两词命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`缺失坐标` 的本线命中皆既有系统档 ✓）
- **注 ✓**：本档实质＝**§1 结构恒等式 ＋ §2 缺失集判定 ＋ §3 存在侧自由**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **不声称** 119-cover 中 $b_4$ 可大 ✗；**不声称** 重量 5 层路线有效 ✗（仅登记接口 ✓）；**不声称** P1 成立 ✗（V290）
- §2 的"缺失集 $\equiv$ $u\subseteq S(c)$"**必须保留** ✓（防把缺失集当新量重复开发 ✗）
