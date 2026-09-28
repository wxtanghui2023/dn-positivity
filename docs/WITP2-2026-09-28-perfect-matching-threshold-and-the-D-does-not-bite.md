# WITP2-2026-09-28 — **$|F_p|{=}4$（$|C_p|{=}3$）$\iff C_p$ 是 $K_6$ 完美匹配（新 ✓✓✓）；但 $D$ 杀不掉该边界（✗✗）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:49 令 ✓）**：P2 联合容量（$C_p$ 与三个相邻 $D_q$）；**零程序计算**（仅有限穷举 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-460／C-458／C-456，非新案 ✓）**
`docs/WITD1-2026-09-28-…`（**$M_C$ 精确表／$d{=}1$ 四机制 ✓✓✓**）｜`docs/WITPARITY-2026-09-28-…`（**三 extremal ✓✓✓**）｜`docs/WITCAPP-2026-09-28-…`（**$\max|F|{+}|G|\le22$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $M_C$／$D{\to}F$／packing 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次证 $|F_p|{=}4\wedge|C_p|{=}3\iff C_p$ 为 $K_6$ 完美匹配（15 个，各 2 个 $F$）＋ 首次算出该边界下 $|D|$ 可达 $12$（$D$ 不能杀它）** ✓）
**[RESEARCH]**

---

## §0 结论（**完美匹配定理 ✓✓✓（新）｜$D$ 杀不掉边界 ✗✗｜$C$ 预算后果 ✓**）

$$\textbf{设定 ✓}:\ \text{固定偶 bucket }p;\ C_p\subseteq\binom{[6]}2\ (\text{pair});\ F_p\subseteq\binom{[6]}3\ (\text{triple},\ \text{两两}|\cap|\le1\big);\ D_q\subseteq\binom{[6]}3✓$$
$$\qquad\text{约束（C-460／C-458 ✓）}:\ F_p\ \text{避 }C_p\text{-pair 之超集}\ \big(S\subset V\big)\ ✓;\quad F_p\cap D(p)=\varnothing\ \big(D(p){=}\bigcup_{q\sim p}D_q\big)\ ✓;\quad \text{每个 }D_q\ \text{亦为 packing}\ ✓$$
$$\boxed{\textbf{(1) ✓✓✓完美匹配定理（本档新，穷举确认）}:\ \big(|F_p|{=}4\ \wedge\ |C_p|{=}3\big)\ \Longrightarrow\ \boxed{C_p\ \text{是 }K_6\ \text{的完美匹配}}✓✓✓}$$
$$\qquad\textbf{穷举 ✓✓}:\ \binom{15}3=455\ \text{个 3-pair }C_p\ \text{中，仅 }\mathbf{15}\ \text{个容 }|F_p|{=}4✓;\ \text{且这 15 个\ \textbf{恰是} }K_6\ \text{的 15 个完美匹配 ✓✓（逐一如实核对 ✓）}$$
$$\qquad\Longrightarrow\ \text{每个完美匹配 }C_p\ \text{恰容\ \textbf{2 个} 4-packing}\ ✓\big(\text{15}\times2=30\ \text{个 }(C_p,F)\ \text{对 ✓}\big);\quad \mathbf{F_p=4\ \text{是极稀有构型}✓✓}$$
$$\boxed{\textbf{(2) ✗✗唐先生 §7 所期"}$D$ 杀掉边界"$\ \textbf{不成立}:\ }\text{对全部 30 个 }(C_p,F)\ \text{对，穷举三个相邻 }D_q\ \text{之最大 packing 皆}\ =\mathbf4✓✓$$
$$\qquad\Longrightarrow\ \text{每个 }D_q\ \text{仍可\ \textbf{满取 4 个}（避开 }F\ \text{与 }C_p\text{-pair ✓）}\Longrightarrow \boxed{|D(p)|{=}|D_{q_1}|{+}|D_{q_2}|{+}|D_{q_3}|\ \text{可达}\ 12}✓✓\ (\text{兼容}|F_p|{=}4✓)$$
$$\qquad\textbf{（跨 }D_q\ 之唯一约束 ✓）}:\ q\ne q'\ \text{皆奇 ⟹ }d_{\text{pref}}{=}2\Longrightarrow d=2+|S\triangle S'|\ge3\iff\boxed{S\ne S'}✓✓\ \text{—— 故非"不相交"而是\ \textbf{仅需相异} ✓（更正唐先生 §4 之"自动成立" ✗：}S{=}S'\ \text{时 }d{=}2\ \text{仍禁 ✓）$$
$$\boxed{\textbf{(3) ✓唐先生 §1 之反向界表正确（＝C-460 表之直读 ✓✓）}:\ }|F_p|{=}4\Rightarrow|C_p|\le3✓;\ |=3\Rightarrow\le6✓;\ |=2\Rightarrow\le9✓;\ |=1\Rightarrow\le12✓$$
$$\boxed{\textbf{(4) ✓✓$C$-预算之直接后果（新构型约束 ✓）}:\ }\text{由 (1)：}|F_p|{=}4\ \text{要求 }C_p\ \text{为完美匹配（}|C_p|{=}3✓\big)\Longrightarrow$$
$$\qquad\textbf{Type I}\ (0,4,4,4)✓:\ \text{三个满 bucket}\ \Longrightarrow\ |C_{p_1}|{=}|C_{p_2}|{=}|C_{p_3}|{=}3✓\ \big(\text{各为完美匹配 ✓}\big)\Longrightarrow\boxed{|C|\ \ge\ 9}✓✓\ \big(\text{第四个 bucket}\le3✓\ \Longrightarrow |C|\le12✓\big)$$
$$\qquad\textbf{Type II}\ (2,2,2,4)✓:\ \text{唯一满 bucket}\Longrightarrow |C_{p_4}|{=}3\Longrightarrow\boxed{|C|\ge3}✓;\qquad \textbf{Type III}\ (2,2,3,3)✓:\ \text{无 }F{=}4\Rightarrow\ \text{无此约束 ✓}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓}:\ \text{反向界表 ✓✓（C-460 直读 ✓）；Type I/II/III 之逐型预算写法 ✓（唯 Type I 之"}|C|\le24\ \text{粗预算"\ 仅作提示 ✓，真约束为 }|C|\le12✓\big)$$
$$\textbf{§2 ✓✓}:\ M(C_p,\mathcal D(p))\ \text{之定义 ✓✓;\ }D(p){=}\bigcup_{q\sim p}D_q✓✓;\ F_p\ \text{须同时避 pair-超集与 }D(p)✓✓$$
$$\textbf{§3 ✓✓}:\ \text{"每 }p\ \text{只看到三个 }D_q"\ ✓✓（}Q_3\ \text{每点 3 邻 ✓）；"无需全局搜索"\ ✓✓$$
$$\textbf{§4 ✓（一处须补 ✗）}:\ \text{"同 }q\ \text{内 }|S\cap S'|\le1\Rightarrow D_q\ \text{为 packing"\ ✓✓；"不同 }q\ \text{基本自由"\ ✓\ \text{大体对 ✓；唯 }S{=}S'\ \text{时 }d{=}2\ \text{仍禁 ✗ ⟹ 应写\ \textbf{仅需 }S\ne S'✓✓}}$$
$$\textbf{§5 ✓✓（且本档已执行 ✓）}:\ \text{对 270 个 packing 过滤之提法 ✓✓;\ 本档进一步：300 对全枚举 ＋ }D\text{-容量 ✓✓}$$
$$\textbf{§6 ✓（方向 ✓）}:\ \text{三型分别打 }M(C_p,D_{\sim p})\ \text{之提法 ✓✓;\ 唯其"若 }M{=}4\Rightarrow|C_p|+\text{cost}\le k\text{"\ 之期待已由 §0(2) 否证 ✗✓（}D\ \text{不施压 ✓）}$$
$$\textbf{§7 ✗✗}:\ \text{其所指"最值得优先测试"之边界 }(|F_p|{=}4,|C_p|{=}3)\ \text{已算实：}\boxed{\text{可实现且 }|D|\ \text{可达 }12}✗✓\ \text{（但换来一条\ \textbf{更强} 的结构定理 ✓✓）}$$
$$\textbf{§8 ✓（路线 ✓）}:\ M_C\to M_{C,D}\to\ \text{三 extremal}\to|C|\le12\ \text{之路线 ✓✓\ 合理 ✓（且已排除 }d{=}2\ \text{回头路 ✓）}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{|F_p|{=}4\wedge|C_p|{=}3\iff C_p\ \text{为完美匹配}}✓✓✓;\ \text{② }|F_p|{=}4\ \text{仅 30 个 }(C_p,F)\ \text{对 ✓✓};\ \text{③ }D\ \text{不施压（}|D|\ \text{可达 }12\big)✓✓;\ \text{④ 跨 }D_q\ \text{仅需 }S\ne S'✓✓;\ \text{⑤ Type I }\Rightarrow|C|\ge9✓✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}D\ \text{杀边界 }(|F_p|{=}4,|C_p|{=}3)\text{"}\ ✗✗;\ \text{"不同 }q\ \text{之间自动 }d\ge4\text{"}\ ✗\ \big(\text{须 }S\ne S'\big);\ \text{"}|C_p|\ge6\Rightarrow F_p{=}0\text{"}\ ✗\ \big(\text{C-460 ✓}\big)$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ M\ \text{之真值};\ \text{（}|C|\le12\ \text{与三型之联合尚未成式 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① Type I 之三完美匹配 + 第四 bucket 之联合可行性（}|C|\le12✓\big)✓;\ \text{② Type II 之 }|C_{p_4}|{=}3\ \text{与其他三 bucket 之相容 ✓;\ \text{③ }|F_p|{=}3\ \text{类（}|C_p|\le6\big)\ \text{之结构定理（对应完美匹配之推广 ✓）}}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "完美匹配门槛" "联合容量" "反向界"
技术词 完美匹配门槛 命中文件数=0    ::
技术词 联合容量     命中文件数=3    :: ./WITD1-2026-09-28-… ./ASSETS-REGISTRY.md ./WITAUDIT-2026-09-28-…
技术词 反向界       命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 完美匹配门槛 | 0 | 0 | ✓（自造标签 ✓） |
| 联合容量 | **3**（`WITD1-2026-09-28-…`／`ASSETS-REGISTRY`／`WITAUDIT-2026-09-28-…` ⟹ **本线既有 ⟹ 不计** ✗） | 0 | ✗（**非新增** ✓） |
| 反向界 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限穷举：$2^{15}$ 个 $C_p$ × 270 packing × 30 对 $(C_p,F)$ ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处必改**（§4 之"自动成立"）已在 §0(2) 显式标注（须 $S\ne S'$ ✓）；**一处理想被否证**（§7）已在 §0(2) 标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
