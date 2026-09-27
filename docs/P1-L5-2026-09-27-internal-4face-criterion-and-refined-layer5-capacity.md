# P1-L5-2026-09-27 — **layer-5 接口的结构分类**：内部 4-面判定定理 ＋ 精细容量不等式（新，排列级）

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 23:27 令 ✓）**：回答纯结构问题 —— 一个 weight-5 码字能同时作为多少个内部 weight-4 block 的 extension；其 4-faces 与 $S(c)$ 的交结构受何限制；零程序计算 ✓。

**已查地图：命中（接续 C-421／C-420／C-419，非新案 ✓）**
`docs/P1-D5-2026-09-27-…`（**结构恒等式／layer-5 接口** ✓✓）｜`docs/P1-B4-2026-09-27-…`（**$S(y)\cap u=\varnothing$／$C_1$** ✓✓）｜`docs/P1-NINT-2026-09-27-…`（**折衷关系／独立性闸** ✓✓）｜`docs/P1-SCREEN-2026-09-27-…`（**C-418 门** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** layer-5 接口对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出内部 4-面判定定理 ＋ 精细容量不等式（layer-5 侧首个非平凡界）** ✓）
**[RESEARCH]**

---

## §0 结论（**分类定理 ✓✓｜精细容量 ✓✓｜下界不可得 ⚠️**）

$$\boxed{\textbf{(1) ★分类定理（新 ✓✓）}:\ w=c\oplus e_v\ \big(v\in M_5(c)✓\big);\ \text{其 4-面 }u_i:=v\setminus\{i\}\ (i\in v)\ \text{是内部 block}\iff\boxed{i\in S(w)\ \textbf{且}\ v\setminus\{i\}\subseteq S(c)}✓✓}$$
$$\qquad\textbf{推论（按 }a:=|v\setminus S(c)|\ \text{分三类 ✓✓）}:\quad a=0\Rightarrow\#=\#\{i\in v:i\in S(w)\}\le5✓;\qquad \boxed{a=1\Rightarrow\#\le\mathbf 1}\ ✓✓;\qquad a\ge2\Rightarrow\#=0✓$$
$$\qquad\qquad\text{（}a=1\ \text{的唯一性 ✓✓）}:\ \text{设 }v\setminus S(c)=\{j\}✓,\ \text{则唯一候选面 }u_j=v\setminus\{j\}✓;\ \text{它成为内部 block}\iff j\in S(w)✓$$
$$\boxed{\textbf{(2) ★精细容量不等式（新，排列级 ✓✓）}:\ \boxed{I(c)\ \le\ 5\,|M_5^{(0)}|\ +\ 1\,|M_5^{(1)}|}\ \ \big(\text{平凡界为 }I(c)\le5|M_5(c)|✓\big)}$$
$$\qquad\big(M_5^{(k)}:=\{v\in M_5(c):|v\setminus S(c)|=k\}✓\big);\quad \textbf{过 C-418 门}✓\ \big(\text{依赖 }v\ \text{相对 }S(c)\ \text{的\textbf{位置} ⟹ 非 degree/profile ✓}\big)$$
$$\boxed{\textbf{(3) ⚠️ 诚实}:\ I(c)\ \textbf{的下界不可得}✗\ \big(\text{内部 block 可有 }|E_5|=0\ ✓\text{—— 孤立内部块 ✓}\big) \Longrightarrow \textbf{尚不能形成 collision}⚠️}$$

---

## §1 **分类定理的证明**（**⟺ 两方向 ✓✓**）

$$\text{固定 }c\in C\ \text{与 }v\in M_5(c)\ \big(⇔w:=c\oplus e_v\in C✓\big);\ \text{对 }i\in v\ \text{取 }u_i=v\setminus\{i\}\ (|u_i|=4✓)$$
$$\textbf{方向 ⟸ ✓}:\ i\in S(w)\Rightarrow w\oplus e_i=c\oplus e_{(v\setminus i)}=c\oplus e_{u_i}\in C✓\ \big(\text{故 }u_i\in M_4(c)✓\big);\ \text{又 }v\setminus\{i\}\subseteq S(c)\Rightarrow u_i\subseteq S(c)✓\ \Longrightarrow\ u_i\ \textbf{是内部 block}✓$$
$$\textbf{方向 ⟹ ✓}:\ u_i\ \text{是内部 block}\Rightarrow c\oplus e_{u_i}\in C\ \text{且}\ u_i\subseteq S(c)✓;\ \text{而 }w\oplus e_i=c\oplus e_{u_i}\in C\Rightarrow i\in S(w)✓;\ \text{且 }u_i\subseteq S(c)\ \text{即 }v\setminus\{i\}\subseteq S(c)✓$$
$$\Longrightarrow\ \textbf{（1）得证}✓✓;\qquad \textbf{关键观察 ✓}:\ v\setminus\{i\}\subseteq S(c)\iff\big(v\setminus S(c)\big)\subseteq\{i\}\iff a=0\ \text{或}\ (a=1\ \text{且}\ i=j✓\big)✓$$

## §2 **三情形 ＋ 精细容量**（**✓✓**）

$$\textbf{（i）}a=0\ \big(v\subseteq S(c)✓\big):\ \text{五面皆 }\subseteq S(c)\ \Longrightarrow\ \text{内部面数}=|\{i\in v:i\in S(w)\}|=|v\cap S(w)|\le5✓$$
$$\textbf{（ii）}a=1\ \big(v\setminus S(c)=\{j\}✓\big):\ \text{仅 }i=j\ \text{满足 }v\setminus\{i\}\subseteq S(c) \Longrightarrow\ \text{内部面数}=1_{j\in S(w)}\le\mathbf 1✓✓$$
$$\textbf{（iii）}a\ge2:\ \text{无面满足} \Longrightarrow 0✓$$
$$\textbf{容量侧重数 ✓}:\ I(c)=\#\{(u,v):u\in M_4(c),v\in M_5(c),u\subset v\}=\sum_{v\in M_5(c)}\#\{\text{内部面 of }v\}\le5|M_5^{(0)}|+1|M_5^{(1)}|✓✓$$
$$\textbf{平凡界对照 ✓}:\ I(c)\le5|M_5(c)|✓\ \big(\text{每 }v\ \text{至多 5 个 4-面 ✓}\big) \Longrightarrow \text{本档的精化来自 }a\ge1\ \text{的\textbf{位置敏感}压制 ✓✓}$$

## §3 **$I(c)$ 的三重表达**（**接口恒等式 ✓**）

$$I(c)=\sum_{u\in M_4(c)}\big|E_5(u)\big|=\sum_{u\in M_4(c)}d_1(c\oplus e_u)\ \big(\text{对\textbf{内部} }u\ \text{由 C-421 ✓}\big)=\sum_{v\in M_5(c)}\#\{\text{内部 4-面 of }v\}✓$$
$$\qquad\Longrightarrow\ \textbf{双层接口}:\ M_4\ \longrightarrow\ I\ \longleftarrow\ M_5✓\ \big(\text{照唐先生 23:27 ✓}\big);\ \text{本档补上的是 \textbf{右侧的第一次精化}}✓$$
$$\textbf{注 ✓}:\ \text{对\textbf{非内部} }u\ \text{（}u\not\subseteq S(c)✓\big)\ \text{仍可定义 }E_5(u)✓,\ \text{但 }d_1(c\oplus e_u)=\big|E_5(u)\big|+\#\{i\in u:c\oplus e_{(u\setminus i)}\in C\}✓\ \big(\text{不可省项 ✓}\big)$$

## §4 诚实边界 ＋ 状态锁（**照唐先生 ✓**）

$$\textbf{（下界侧 ✗）}:\ I(c)\ \text{有下界吗？} \text{否（现无）}✗:\ \text{内部 block }u\ \text{可满足 }E_5(u)=\varnothing\ \big(\text{即 }d_1(c\oplus e_u)=0✓\text{，孤立内部块 ✓}\big);\ A(c)=0\ \text{与 }(\alpha)\ \text{皆不禁 ✓}$$
$$\qquad\Longrightarrow\ \text{故 }I(c)\ \text{只有上界（本档 ✓）与平凡下界 }0✗ \Longrightarrow \textbf{无法夹逼}⚠️\ \big(\text{照唐先生判据：须"另一侧独立不等式"✓}\big)$$
$$\textbf{（另一条可能下界通道 ✓）}:\ \text{若能把 C-419 的需求 }b_3+4b_4\ge\binom s3\ \text{与 }I(c)\ \text{相连（如 }\sum_{u\in M_4^{\rm int}}|E_5(u)|\ge\text{某函数}(b_4)✓\big) \Longrightarrow \text{方可碰撞 ⚠️——\textbf{未做}✓}$$

| 部分 | 状态 |
|---|---|
| avoidance／missing-set | **STOP** ✗ |
| degree／profile／capacity | **STOP** ✗ |
| $4\to5$ 精确邻接接口 | **LIVE** ✓ |
| C-419 $b_3/b_4$ tradeoff | **HOLD** ✓ |
| 新的全局碰撞 | **尚未形成** ⚠️ |

$$\textbf{（C-421 状态照唐先生 ✓）}:\ \textbf{不 CLOSED}✗;\ \text{是合格的 \textbf{LIVE interface}，但\textbf{尚不是攻击点本身}}✓;\ \text{本档为其补上"右侧第一次精化"✓}$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "延拓算子" "5-延拓" "精细容量" "4-面"
技术词 延拓算子      命中文件数=0    ::
技术词 5-延拓        命中文件数=0    ::
技术词 精细容量      命中文件数=0    ::
技术词 4-面          命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 延拓算子 | 0 | 0 | 0（本档自造标签 ✓） |
| 5-延拓 | 0 | 0 | 0（本档自造标签 ✓） |
| 精细容量 | 0 | 0 | 0（本档自造标签 ✓） |
| 4-面 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（四词**两空间皆 0** ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 分类定理 ＋ §2 精细容量 ＋ §3 三重表达 ＋ §4 下界不可得**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **不声称** $I(c)$ 路线有效 ✗；**不声称** 119-cover 中存在内部块 ✗（$C_1$ 非覆盖码 ✓）；**不声称** P1 成立 ✗（V290）
- §4 的"下界不可得（孤立内部块 ✓）"**必须保留** ✓（防把单侧界当 collision ✗）
- 本档**不**重复登记 C-421 的内容 ✓（仅引其恒等式 ✓）
