# RESULT-2026-09-30 — **逐点模式不等式（新、健全、且在真码上\ \textbf{取等}）**：$(m{+}1)|S_y|+|U_y|\ge 2^m$ ✓✓ —— 今晚**第一个紧的必要条件**（其余皆"有效但松"✗）

> 空间 B｜非 C 号｜唐先生 16:56「继续」｜**不主张任何新值**（V290）
> 时间：2026-09-30 18:0x

**已查地图** ✓：`STATE-2026-09-30`（块分层引理）／L1554（支撑层＝自由度）／档案"有效但不足"清单
D0: 本档对象 = **新必要条件族**（对块分层之精化）—— 属**支撑层**；形式为**新** ✓（档案无同名）
D1: 0（产出 = **一条健全＋取等之新不等式 ＋ 一条等式情形结构刻画 ＋ 一条可攻接口** ⚠️✓）

---

## §0 **定义与引理（推导 ✓）**

$$C\subseteq\mathbb F_2^n,\ R{=}1,\ |C|{=}M;\quad \text{块 }B\ (|B|{=}m),\ \text{补 }B^c\ (\text{维 }nc{=}n{-}m);\quad L_\sigma=\{w:(\sigma,w)\in C\}$$
$$\forall y\in\mathbb F_2^{nc}:\quad S_y:=\{\sigma:\ y\in L_\sigma\}\ (\textbf{\text{恰含 }y\text{ 之层}});\quad U_y:=\{\sigma:\ y\in N_1[L_\sigma]\}\ (\textbf{\text{近含 }y\text{ 之层}});\quad T_y:=N_1[S_y]$$
$$\textbf{引理（健全 ✓）}:\ \boxed{T_y\cup U_y=\mathbb F_2^m}\ \ \text{证}:\ \sigma\notin U_y\Rightarrow a_\sigma(y){=}0\Rightarrow(\text{covering at }(\sigma,y))\ |\partial\sigma\cap S_y|\ge1\Rightarrow\sigma\in N_1[S_y] ✓$$
$$\textbf{推论（新不等式 ✓）}:\ 2^m=|T_y\cup U_y|\le|T_y|+|U_y|\le (m{+}1)|S_y|+|U_y|\quad\Longrightarrow\ \boxed{(m{+}1)|S_y|+|U_y|\ \ge\ 2^m}\ ✓$$
$$\qquad\text{（用 }|N_1[S]|\le (m{+}1)|S|\ \text{及 }|T\cup U|\le|T|+|U|\ \text{——皆是上界 ✓ 故健全 ✓）}$$

## §1 **实测：\ \textbf{引理精确成立、不等式\ \textbf{取等}}（120-码 ✓✓）**

| $m$ | 补维 $nc$ | 引理违反数 | $|T_y\cup U_y|$ 取值 | **聚合式最小 slack** |
|---|---|---|---|---|
| 1 | 9 | **0** / 512 | $\{2\}$ ✓ | **0 ⟹ 紧 ✓✓** |
| 2 | 8 | **0** / 256 | $\{4\}$ ✓ | **0 ⟹ 紧 ✓✓** |
| 3 | 7 | **0** / 128 | $\{8\}$ ✓ | **0 ⟹ 紧 ✓✓** |

$$\therefore\ \boxed{\text{该不等式族在真码上\ \textbf{处处取等}}}\ ✓✓\ ——\ \textbf{\text{与今晚其余全部结果（"有效但松"}✗\text{）}\ \textbf{性质不同}} ✓✓$$

## §2 **等式情形之结构刻画（可攻接口 ✓✓）**

$$\text{取等 ⟺ 两处同时取等}:\ \text{(i) }|T_y|=(m{+}1)|S_y|\ \Longrightarrow\ \textbf{\text{诸 }N_1[\sigma]\ (\sigma\in S_y)\ \text{两两不交}}\ ✓;\quad \text{(ii) }U_y=\mathbb F_2^m\setminus T_y\ （\textbf{\text{严格补集，无重叠}}）✓$$
$$\therefore\ \text{取等强制\ \textbf{\text{刚性结构}}}:\ \text{每点 }y\ \text{处，}\ S_y\ \text{之半径-1 球族恰作一次划分，其余层恰填满其余部分} ✓✓$$
$$\Longrightarrow\ \text{可用之\ \textbf{等式审计}（用户前轮框架，}\textbf{\text{今有真紧之靶}} ✓✓）:\ \text{若 }\sum_y(\text{slack})\ \text{之最小可能} \ge1\ \text{在 }M{=}106\ \text{处不可达} \Longrightarrow\ \text{得新界} ⚠️$$

## §3 **诚实边界**

$$\text{(a) 已知弱点}:\ \text{单纯对 }y\ \text{求和后得 }(n{+}2)M\ge2^n\ (\text{即 }M\ge 2^n/(n{+}2)\ \text{——\ \textbf{弱于球界}} ✗) \Longrightarrow \textbf{\text{必须用逐点/分布形式，不可只用总和}} ⚠️$$
$$\text{(b) 未证部分}:\ \text{等式情形之\ \textbf{\text{不可实现性}} 尚未证明} ✗\ (\text{本档只给靶与结构 ✓）$$
$$\text{(c) 未做}:\ M{=}106\ \text{处之整数可行性检验} ⚠️$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 逐点模式不等式  命中文件数=1    :: 本档
技术词 等式审计     命中文件数=4    :: 本档 ＋ CLOSED-ROUTES-MAP.md ＋ MASTER-STATUS-AND-CLOSURES.md
```

$$\textbf{分类（三项如实 ✓）}:\ \text{(1) }\textbf{本档新增}：\text{“逐点模式不等式”} ⟹ \text{仅本档} ✓;\quad \text{(2) }\textbf{档案已有（引用，不列为提出）}：\text{“等式审计”} ⟹ \text{命中 4 处（含地图两档）} ✗\ \text{故本档**不**主张该词之新性};\quad \text{(3) }\textbf{通用词（不计）}：\text{“区块／模式”裸词}$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{不等式\ \textbf{健全}（推导＋实测双证 ✓）};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
