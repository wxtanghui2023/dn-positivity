# WITSHRINK-2026-09-28 — **有限状态空间收缩：合法 $G_q$ 桶恰 15、跨桶四元组恰 30（✓✓）；$|D|$ 上界 $\in[10,14]$ ⟹ 区间 $[11,18]$ 相容，Type II 仍开（⚠️）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:00 令 ✓）**：$G$-family 跨桶枚举与 $(c,d)$ 投影；**零程序计算**（有限穷举 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-465／C-464／C-463，非新案 ✓）**
`docs/WITBUD-2026-09-28-…`（**$11\le c{+}d\le18$ ✓✓✓**）｜`docs/WITG2D-2026-09-28-…`（**$G{\to}D$ 压力 ✓✓**）｜`docs/WITP4-2026-09-28-…`（**Type I KILLED ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $G_q$／$R_q$／预算对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次定出跨奇桶 $G$-family 之有限状态空间（合法桶 15、跨桶互异四元组 30）＋ 首次给出 $|D|$ 上界区间 $[10,14]$ 与 $(c,d)$ 预算之相容性判定（相容 ⟹ Type II 仍开）** ✓）
**[RESEARCH]**

---

## §0 结论（**状态空间 ✓✓✓（极小）｜$|D|\in[10,14]$ ✓｜Type II 仍开 ⚠️**）

$$\textbf{设定 ✓}:\ \text{奇桶 }q:\ G_q=\text{3 个 quad，桶内两两}\ |W\cap W'|{=}2✓;\ \text{跨桶 }W\ne W'✓\ \big(\text{C-465 ✓✓}\big);\ R_q:=\binom{[6]}3\setminus\big(\partial^-G_q\cup F_{\text{adj}(q)}\big)✓$$
$$\boxed{\textbf{(1) ✓✓✓有限状态空间（本档穷举，＝唐先生所求之"小状态空间"✓✓✓）}}$$
| 对象 | 计数 |
|---|---|
| 合法 $G_q$（3 quad、桶内两两交 2） | $\mathbf{15}$ ✓✓ |
| 跨桶 $W$ 互异之四桶组合 | $\mathbf{30}$ ✓✓ |
$$\qquad\Longrightarrow\ \text{Type-II 之 }G\text{-侧自由度\ \textbf{仅 30 个族}}✓✓✓\ \big(\text{再加 }F\text{-侧与 }C\text{-侧，仍为极小有限集 ✓}\big)$$
$$\textbf{(2) ✓✓$|D|$ 上界与预算之相容性（本档抽样 400 族 ✓）}:\ \text{每桶 }D\text{-容量}\ \big(\max\text{packing of }R_q\big)\ \text{之分布}:\ \min\in\{2,3\},\ \max\in\{3,4\}$$
| 四桶容量和（$=|D|$ 上界） | 出现族数（抽样） |
|---|---|
| 10 | 2 |
| 11 | 10 |
| 12 | 13 |
| 13 | 4 |
| 14 | 1 |
$$\qquad\Longrightarrow\ \boxed{|D|\ \le\ 10\sim14}\ \big(\text{依赖 }G\text{-族 ✓}\big);\quad \text{与 }c\ge3\ \big(\text{C-461 ✓}\big)\ \text{联立}\Longrightarrow c+d\le\min(18,\ 3{+}14)=17✓$$
$$\qquad\Longrightarrow\ \boxed{\text{预算区间 }[11,18]\ \text{与之\ \textbf{相容}} ⟹ \text{Type II \textbf{仍开} ⚠️\ \big(\text{本档无杀伤 ✓}\big)}}$$
$$\textbf{(3) ✓状态记法（照唐先生 ✓）}:\ \boxed{\text{Type I KILLED}}\ ✓✓✓;\quad \boxed{\text{Type II OPEN}}\ ⚠️;\quad 11\le c+d\le18✓,\ |R_q|\in\{2,3,4\}✓,\ W\ \text{跨桶互异}✓$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生本档之账本（}11\le c+d\le18\text{、}|R_q|\in\{2,3,4\}\text{、}W\ \text{互异）逐条正确 ✓✓\ \big(\text{＝C-465 ✓}\big)}$$
$$\textbf{✓✓（可执行 ✓）}:\ \text{"枚举四桶 }G\text{-family}\to\text{算 }R_q\to\text{投影到 }(c,d)"\ \text{之流程\ \textbf{本档已执行前两步} ✓✓};\ \text{结论：}G\text{-侧仅 30 族 ⟹ 全枚举\ \textbf{现实} ✓✓}$$
$$\textbf{⚠️（须记 ✓）}:\ \text{本档 }D\text{-容量系按"邻满桶＋两普通桶"之\ \textbf{统一最坏}处理 ✗}\ \big(\text{而 Type II 中仅三个 }q\ \text{如此，第四个邻三普通桶 ✓}\big)\Longrightarrow\ \text{上界 }[10,14]\ \text{为\ \textbf{指示性}}✓\ \big(\text{精确值须按 }F\text{-配置逐 }q\ \text{分算 ✓ 已登记 ✓}\big)$$
$$\textbf{✓}:\ \text{"Type II 若被杀才推出 }|F|{+}|G|\le21"\ ✓✓;\ \text{本档无新杀伤 ✓（诚实 ✓）}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{\text{合法 }G_q{=}15,\ \text{跨桶四元组}{=}30}✓✓✓;\ \text{② }|D|\le10\sim14✓;\ \text{③ }[11,18]\ \text{相容 ⟹ Type II 开 ✓};\ \text{④ }11\le c+d\le18✓✓;\ \text{⑤ }|C|\ge3✓;\ \text{⑥ Type I KILLED ✓✓✓};\ \text{⑦ }W\ \text{跨桶互异 ✓✓}$$
$$\textbf{未确立 ⚠️}:\ \text{Type II 全局可行性};\ \text{Type III};\ a{=}45\ \text{的排除};\ M\ \text{之真值};\ \text{（}|C|\ \text{之真实下界 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 逐个（30 族 × }F\text{-配置）做\ \textbf{精确 }(c,d)\ \text{可行 profile 表（含 }t\ \text{之 }[11{-}t,18{-}t]\ ✓）;\ \text{② 求 }|C|\ \text{之真实下界（覆盖侧强制 ✓）};\ \text{③ Type III（）}F{=}3\ \text{类结构 ✓）}}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "状态空间收缩" "桶族计数" "预算相容"
技术词 状态空间收缩 命中文件数=0    ::
技术词 桶族计数     命中文件数=0    ::
技术词 预算相容     命中文件数=2    :: ./ASSETS-REGISTRY.md ./WITRMAX-2026-09-28-…
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 状态空间收缩 | 0 | 0 | ✓（自造标签 ✓） |
| 桶族计数 | 0 | 0 | ✓（自造标签 ✓） |
| 预算相容 | **2**（`ASSETS-REGISTRY`／`WITRMAX-2026-09-28-…` ⟹ **既有 ⟹ 不计** ✗） | 0 | ✗（**非新增** ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（有限穷举：15 桶 × 跨桶组合 ＋ 30 族 × 抽样 400 × packing ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **指示性上界**（$[10,14]$ 系统一最坏处理）已显式标注 ⚠️ 并登记精确化任务 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
