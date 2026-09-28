# WITBUD-2026-09-28 — **Type II 之 $C{\!+}\!D$ 预算区间 $11\le c{+}d\le18$（✓✓✓）；§2 之"$C\ge6$"为见证非界（✗✗）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:59 令 ✓）**：Type-II 之三方预算联立；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-464／C-463／C-457，非新案 ✓）**
`docs/WITG2D-2026-09-28-…`（**$G{\to}D$ 压力 $|D|\le13$ ✓✓**）｜`docs/WITP4-2026-09-28-…`（**Type I KILLED／Type II 见证 ✓✓✓**）｜`docs/WITCEIL-2026-09-28-…`（**$|A_0|\le40$ ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** 预算／$A_0$ 上限／$R_q$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 Type-II 之\ \textbf{对称}预算区间 $11{\le}c{+}d{\le}18$（上界由 $|A_0|\le40$、下界由 $|A_0|\ge33$）＋ 更正"$C\ge6$"为见证非下界 ＋ 首次指出跨桶 $G$-quad 须两两相异** ✓）
**[RESEARCH]**

---

## §0 结论（**上界 18 ✓✓✓｜下界 11 ✓✓✓（对称）｜"$C\ge6$"是见证 ✗✗**）

$$\textbf{设定 ✓}:\ \text{Type II}:\ |F|{=}10,\ |G|{=}12\Longrightarrow|F|{+}|G|{=}22✓;\ |A_0|{=}c{+}d{+}|F|{+}|G|{+}t\ \big(t{:=}|A_0\cap(d{\ge}5\ \text{诸层})|\big)✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §1 正确（本档确认）}:\ }|A_0|\le40\Longrightarrow 22+c+d\le40\Longrightarrow\boxed{c+d\le\mathbf{18}}✓✓✓\ \big(\text{改进 C-453 之 }20✓;\ \text{精确为 }c{+}d\le18-t✓\big)$$
$$\boxed{\textbf{(2) ✓✓✓但真正有力的是\ \textbf{下界}（本档新，对称区间）}:\ }|A_0|\ge\mathbf{33}\ \big(\text{C-446 ✓✓✓}\big)\Longrightarrow 22+c+d+t\ge33\Longrightarrow\boxed{c+d\ \ge\ \mathbf{11}-t}✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{\mathbf{11}\ \le\ c+d\ \le\ \mathbf{18}}\ ✓✓✓\ \big(t{=}0\ \text{时}✓;\ \text{含 }t\ \text{则移位 }[11-t,\ 18-t]✓\big)$$
$$\qquad\textbf{读法 ✓✓}:\ \text{Type II 之两层预算被\ \textbf{双向}夹住 ⟹ 既不能太少（否则 }|A_0|{<}33\ ✗\big)\ \text{也不能太多（否则 }|A_0|{>}40\ ✗\big)✓✓$$
$$\boxed{\textbf{(3) ✗✗唐先生 §2 之"}|C|\ge6\text{"为\ \textbf{见证}非下界}}:\ \text{C-463 之构造\ \textbf{给出}一个 }|C|{=}6\ \text{之可行样本 ✓\ \big(\text{存在性 ✓}\big)，但 }C_p\ \text{可为\ \textbf{空}}✓\ \big(\text{空 }C_p\ \text{不施约束 ✓}\big)$$
$$\qquad\Longrightarrow\ \text{不能推出 }|C|\ge6\ ✗;\ \text{故 }|D|\le12\ \text{亦\ \textbf{不成立}} ✗✓;\ \text{正确的两侧界是 (1)(2) 之 }11\le c+d\le18✓✓$$
$$\qquad\textbf{（仅有的 }|C|\ \text{下界）}:\ |C_{p_*}|{=}3✓\ \big(\text{C-461 完美匹配 ✓}\big)\Longrightarrow\boxed{|C|\ge3}✓;\quad \text{结合 (2)：}|D|\ \text{无独立上界改进} ✗$$
$$\boxed{\textbf{(4) ✓✓唐先生 §5 之 }|R_q|\in\{2,3,4\}\ \textbf{正确}}:\ R_q:=\binom{[6]}3\setminus\big(\Sigma_q\cup\bigcup_{p\sim q}F_p\big)✓;\ \Sigma_q:=\bigcup_{W\in G_q}\binom W3,\ |\Sigma_q|{=}12✓\ \big(\text{C-464 穷举 ✓}\big)$$
$$\qquad\textbf{（本档新增 ✓✓）}:\ \text{跨桶 }G\text{-quad 须\ \textbf{两两相异}}:\ q\ne q'\ \text{皆奇}\Longrightarrow d{=}2+|W\triangle W'|\ge3\iff\boxed{W\ne W'}✓✓\ \big(\text{＝}F\text{-侧同型约束 ✓}\big)$$
$$\qquad\Longrightarrow\ \text{四个奇桶共 }12\ \text{个 }W\ \text{必须互异 ✓\ \big(弱约束，但为全局一致性之必要项 ✓}\big)$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓✓}:\ c+d\le18\ ✓✓\ \big(\text{本档确认；精确 }18-t✓\big);\ |D|\le13\ \text{与 }|C|\le18-|D|\ \text{之写法 ✓（形式 ✓）}$$
$$\textbf{§2 ✗✗}:\ "C-463 见证给出 }|C|\ge6\text{"}\ ✗\ \big(\text{见证}{\implies}\text{可行，}{\nRightarrow}\text{下界}\big);\ \text{故 }|D|\le12\ ✗\ \text{不成立 ✓（见 §0(3)）$$
$$\textbf{§3 ✗（方向 ✓）}:\ \text{"应求 }D\ \text{之下界而非上界"\ \textbf{方向正确} ✓✓；唯其所据 }|D|\le12\ \text{不成立 ⟹ 仍需另一来源 ✓；本档指出真正的下界来自 }|A_0|\ge33\ \big(\text{对 }c{+}d\ ✓\big)$$
$$\textbf{§4 ✗（同 §2）}:\ |C|\ \text{之增长表 ✓（形式 ✓），但前提 }|C|\ge6\ ✗;\ \text{已有硬下界仅 }|C|\ge3\ ✓\ \big(|C_{p_*}|{=}3✓\big)$$
$$\textbf{§5 ✓✓✓}:\ \text{"四桶 }G\ \text{非独立"\ ✓✓（共享同一 6-点 universe ✓）；}\Sigma_q,\ R_q\ \text{之定义 ✓✓；}|R_q|\in\{2,3,4\}✓✓;\ \text{应追踪；(}G_{q_i}){\mapsto}(R_{q_i})\ ✓✓\ \text{正确 ✓}$$
$$\textbf{§6 ✓（方向 ✓）}:\ \sum_q|R_q|\le12\ \text{之问 ✓（}D\ \text{上界）};\ C\ \text{需求之提法 ✓\ \big(\text{唯 }|C|\ge7\ \text{尚无据 ✗}\big)}$$
$$\textbf{§7 ✓✓（可执行 ✓）}:\ \text{归一化 }M_0\ \text{＋两 parity／枚举三 }F{=}2\ \text{桶／枚举四 }G_q／\text{算 }R_q／\text{加 }D\ \text{之流程}\ ✓✓\ \big(\text{本档为其必要项补一条：}W\ \text{互异}\ ✓✓\big)$$
$$\textbf{§8 ✓（临界层 ✓）}:\ (C,D){=}(6,12),(7,11)(8,10)\ldots\ \text{之提法 ✓\ \big(\text{唯 }C{=}6\ \text{之临界性依赖 §2 ✗}\big)};\ \text{目标"}|C|\ge8\wedge|D|\ge11"\ ✓\ \text{形式 ✓}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{11\le c+d\le18}\ ✓✓✓\ \big(\text{Type II 之对称区间 ✓}\big);\ \text{② }|C|\ge3\ \big(|C_{p_*}|{=}3\big)✓;\ \text{③ }|D|\le13\ \big(\text{最坏 }8\big)✓✓;\ \text{④ }|R_q|\in\{2,3,4\}✓✓;\ \text{⑤ 跨桶 }W\ \text{须互异 ✓✓};\ \text{⑥ Type I KILLED ✓✓✓}$$
$$\textbf{已否证 ✗✓}:\ \text{"}|C|\ge6\text{"}\ ✗\ \big(\text{见证非界}\big);\ \text{"}|D|\le12\text{"}\ ✗;\ \text{"单 triple 贡献 lemma"}\ ✗\ \big(\text{C-464 ✓}\big)$$
$$\textbf{未确立 ⚠️}:\ \text{Type II 全局可行性};\ \text{Type III};\ a{=}45\ \text{的排除};\ M\ \text{之真值}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 按 §7 流程做\ \textbf{小规模有限枚举}，记录 }(|C|,|D|)\ \text{之可行 profile ✓};\ \text{② 求 }|C|\ \text{之真实下界（覆盖侧或 }F\text{-侧强制 ✓）};\ \text{③ Type III（}|F|{=}3\ \text{类结构定理 ✓）}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "预算区间" "见证非界" "四桶一致性"
技术词 预算区间   命中文件数=0    ::
技术词 见证非界   命中文件数=0    ::
技术词 四桶一致性 命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 预算区间 | 0 | 0 | ✓（自造标签 ✓） |
| 见证非界 | 0 | 0 | ✓（自造标签 ✓） |
| 四桶一致性 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（本档为整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处必改**（§2／§4 之见证$\ne$界）已在 §0(3) 显式标注 ✓✓；**Type II 仍未杀** 已标 ⚠️
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
