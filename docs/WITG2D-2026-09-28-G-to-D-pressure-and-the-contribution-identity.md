# WITG2D-2026-09-28 — **$G{\to}D$ 侧压力（新 ✓✓）：Type II 下 $|D|\le13$（最坏 8，改进 16）｜§6 之"贡献"实为恒等式（✗）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:55 令 ✓）**：Type-II 跨桶耦合（$G$ 侧 → $D$ 侧）；**零程序计算**（仅有限穷举 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-463／C-461／C-456，非新案 ✓）**
`docs/WITP4-2026-09-28-…`（**Type I KILLED／Type II 见证 ✓✓✓**）｜`docs/WITP2-2026-09-28-…`（**完美匹配定理 ✓✓✓**）｜`docs/WITCAPP-2026-09-28-…`（**$s_q$ 局部耦合 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $s_q$／$G$-quad／$D$-packing 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $G{=}12$ 对 $D$ 侧之精确压力（每 $D_q$ 须避 $\partial^-G_q$ 与相邻 $F$）⟹ $|D|\le13$（最坏 $8$，改进平凡界 $16$）＋ 更正 §6 之"单 triple 贡献"为恒等式（$r_{ij}{=}f_{p_j}{=}2$）** ✓）
**[RESEARCH]**

---

## §0 结论（**§6 恒等式 ✗｜$G{\to}D$ 压力 ✓✓（新）｜Type II 仍未杀 ✗**）

$$\textbf{设定 ✓}:\ \text{Type II}:\ f=(4,2,2,2),\ |F|{=}10,\ |G|{=}12\ \big(g_q{\equiv}3✓\big),\ s=(6,8,8,8)✓;\ C_{p_*}\ \text{完美匹配（C-461 ✓✓）}$$
$$\boxed{\textbf{(1) ✗唐先生 §6–§7 之"单 triple 跨桶贡献 $\le1$ lemma"为\ \textbf{恒等式}（无信息）}}$$
$$\qquad\textbf{理由 ✓✓}:\ s_q:=\sum_{p\sim q}f_p\ \text{是\ \textbf{triple 计数}}\ ✓\ \big(\text{C-456 ✓}\big)\Longrightarrow r_{ij}=f_{p_j}=\mathbf2\ \text{恒成立}\ ✓\Longrightarrow \boxed{r_{ij}=2\ \text{自动取等}}✓$$
$$\qquad\Longrightarrow\ \text{其"equality case"\ \textbf{无条件成立} ⟹ 不构成新结构约束 ✗✓\ \big(\text{但方向——"跨桶耦合"——正确 ✓✓}\big)}$$
$$\boxed{\textbf{(2) ✓✓✓真正的跨桶压力在 }G{\to}D\ \textbf{（本档新）}:\ }\text{由 C-458/C-460：}(q,S)\in D_q,\ (q,W)\in G_q,\ S\subset W\Longrightarrow d{=}1\ ✗\ \text{禁 ✓✓}$$
$$\qquad\Longrightarrow \text{每个 }D_q\ \text{之 triple 须避}\ \partial^-G_q:=\bigcup_{W\in G_q}\binom W3\ \big(|\partial^-G_q|{=}\mathbf{12}✓\ \text{穷举 ✓}\big)\ \text{以及相邻偶桶之 }F\text{-triple ✓✓}$$
$$\qquad\textbf{穷举定值 ✓✓}:\ \text{纯 }G\ \text{约束下\ \textbf{每桶} }\max|D_q|{=}\mathbf4\ \big(\text{可用 }8✓\big);\ \text{叠加相邻 }F\ \text{后（精确版 ✓，只禁相邻桶 ✓）}:$$
| 情形 | 缺满桶之 $q$：$\max\|D_q\|$ | 其余三个 $q$ 之最坏 $\max\|D_q\|$ | 出现次数 |
|---|---|---|---|
| | 2 | 2 | 1 |
| | 3 | 2 | 5 |
| | 4 | 2 | 2 |
| | 3 | 3 | 5 |
| | 4 | 3 | 2 |
$$\qquad\Longrightarrow\ \sum_q|D_q|\le\max\Big(\underbrace{4+3{\times}3}_{\text{最松}}=13,\ \underbrace{2+3{\times}2}_{\text{最紧}}=8\Big)\Longrightarrow\boxed{|D|\le\mathbf{13}\ \text{（最坏}8\big)}✓✓\ \big(\text{改进平凡界 }16✗\big)$$
$$\qquad\textbf{读法 ✓✓}:\ \text{“}G\ \text{满载（}g_q{\equiv}3\big)\Longrightarrow\text{每奇桶被}12\ \text{个 triple 占住}\Longrightarrow D\ \text{之可用面缩半”}\ ✓✓ =\ \text{唐先生所期之跨桶耦合（且方向在 }G{\to}D,\ \text{非 }D{\to}F\ ✓）$$
$$\boxed{\textbf{(3) ⚠️但 Type II \textbf{仍未被杀}（诚实 ✓）}:\ }\text{C-463 之局部见证（}|F|{=}10,\ |C|{\ge}6✓\big)\ \text{与 }|D|\le13\ \text{相容}✓;\ |C|+|D|\le20✓;\ |A_0|\le40✓$$
$$\qquad\Longrightarrow\ \text{无矛盾 ⟹ Type II 之全局可行性\ \textbf{仍开} ⚠️\ \big(\text{须 }G\ \text{侧与 }C\text{-预算之更强耦合，或覆盖侧联合 ✓}\big)}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓}:\ (f_p){=}(4,2,2,2)✓,\ (s)=(6,8,8,8)✓\ \big(s{=}|F|-f_{p(q)}✓\big),\ |F|{=}10✓,\ |G|{=}12✓;\ \text{"特殊桶 }C\ \text{为完美匹配"\ ✓✓（C-461 ✓）};\ S_6\ \text{对称 ⟹ 可固定 }M_0✓✓$$
$$\textbf{§2 ✓✓}:\ \text{"须做跨桶耦合"\ 正确 ✓✓};\ s_{p_*}{=}6,\ s_{p_i}{=}8\ ✓✓\ \big(\text{三邻桶各收到 8 ✓}\big)$$
$$\textbf{§3 ✓（算术 ✓）}:\ 3f_{p_*}{=}12✓;\ 8{+}8{+}8{=}24✓;\ \text{余 }12\ \text{由邻桶间提供 ✓✓};\ \text{平均每桶再需 }4✓$$
$$\textbf{§4 ✗（措辞 ✗，实质 ✓）}:\ \text{"}6\ \text{个 }F\text{-对象须高效同时满足三邻桶"\ —— 由 (1)，其满足是\ \textbf{恒等}的 ✗✓；真正的稀缺在 }G{\to}D\ \text{侧 ✓✓（§0(2) ✓）}$$
$$\textbf{§5 ✓✓}:\ F_{p_*}\in\{\mathcal P_0,\mathcal P_1\}\ \text{（两奇偶类 ✓✓ C-461/M 档 ✓）};\ \text{普通桶须落 16 个剩余 triple ✓✓};\ \text{四条约束并列 ✓✓ 正确 ✓}$$
$$\textbf{§6 ✗✗}:\ \text{见 §0(1)（贡献恒等式 ⟹ 无 lemma 可证 ✗）}$$
$$\textbf{§7 ✗}:\ \text{其"交集为空 ⟹ P2 否证"之目标\ \textbf{落空} ✗（因 §6 前提不成立 ✓）}$$
$$\textbf{§8 ✓✓}:\ |C_{p_*}|{=}3\Longrightarrow\ \text{其余三桶至多 }9⟹|C|\le12✓✓;\ \text{与 }|C|+|D|\le20\Longrightarrow|D|\le8✓\ \big(\text{若 }|C|{=}12✓\big)✓;\ \text{"}C\ \text{越满载 ⟹ }D\ \text{越低"\ \textbf{正确} ✓✓\ \big(\text{本档 §0(2) 给出其镜像 }G{\to}D✓\big)}$$
$$\textbf{§9–§10 ✓（路线 ✓）}:\ \text{Type II 优先、Type III 后置 ✓✓ 合理 ✓（Ⅰ已 KILLED ✓）};\ \text{唯其链中"六个贡献同时取等"\ 一环应替换为 }G{\to}D\ \text{压力 ✓✓}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{|D|\le13\ (\text{最坏 }8)}✓✓\ \big(G{=}12\ \text{之压力 ✓}\big);\ \text{② }G{=}12\Rightarrow\partial^-G_q\ \text{占 12 ⟹ 可用 8 ⟹ 纯 }G\ \text{下每桶}\le4✓✓;\ \text{③ }G{\to}D\ \text{为 }d{=}1\ \text{内含型（C-460 ✓✓）};\ \text{④ Type I KILLED（C-463 ✓✓✓）};\ \text{⑤ }|C_{p_*}|{=}3\Rightarrow|C|\le12✓✓$$
$$\textbf{已否证 ✗✓}:\ \text{"单 triple 贡献 }\le1\ \text{lemma"}\ ✗\ \big(\text{恒等式 ⟹ 无内容}\big);\ \text{"六个贡献取等为刚性约束"}\ ✗\ \big(\text{自动成立}\big);\ \text{"}|D|\le16\ \text{为紧"\ ✗}$$
$$\textbf{未确立 ⚠️}:\ \text{Type II 全局可行性};\ \text{Type III};\ a{=}45\ \text{的排除};\ M\ \text{之真值}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 把 }G{\to}D\ \text{压力与 }C\text{-预算（}|C|+|D|\le20✓\big)、|A_0|\le40\ \text{三方联立 ✓};\ \text{② Type II 之 }G\ \text{结构（四桶 trio 之 }W\text{-族）全局一致性 ✓};\ \text{③ 若 II 排除 ⟹ }F{+}G\le21✓$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "贡献恒等式" "满效率" "G侧压力"
技术词 贡献恒等式 命中文件数=0    ::
技术词 满效率     命中文件数=0    ::
技术词 G侧压力     命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 贡献恒等式 | 0 | 0 | ✓（自造标签 ✓） |
| 满效率 | 0 | 0 | ✓（自造标签 ✓） |
| G侧压力 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限穷举：$G$ 之 3-quad 结构 ＋ 相邻 $F$ 叠加 ＋ 各桶 packing ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处必改**（§6／§7 之恒等式）已在 §0(1) 显式标注 ✓✓；**Type II 仍未杀** 已标 ⚠️
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
