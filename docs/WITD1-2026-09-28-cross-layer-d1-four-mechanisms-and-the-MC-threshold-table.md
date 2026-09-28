# WITD1-2026-09-28 — **跨层 $d{=}1$ 四机制（✓✓✓ 全对）＋ $M_C$ 精确定值表；$\tau_3(6){=}6$ 门槛\ \textbf{须改为"必要不充分"}（✗✗）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:46 令 ✓）**：跨层 $d{=}1$ 禁配精确化；**零程序计算**（仅有限穷举 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-458／C-457／C-453，非新案 ✓）**
`docs/WITPARITY-2026-09-28-…`（**跨层 $d{=}2$ 为空／三 extremal ✓✓✓**）｜`docs/WITCAPP-2026-09-28-…`（**$\max|F|{+}|G|\le22$ ✓✓**）｜`docs/WITDEC-2026-09-28-…`（**$c+d\le20$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** 跨层 $d{=}1$／$M_C$／packing 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出跨层 $d{=}1$ 四机制之逐条证明 ＋ $M_C(m)$ 之精确最坏/最好表 ＋ 修正 $\tau_3(6){=}6$ 为"必要不充分"（$P^c$ 无三角形才算杀尽）** ✓）
**[RESEARCH]**

---

## §0 结论（**四机制 ✓✓✓｜$M_C$ 表 ✓✓｜门槛须改 ✗✗**）

$$\textbf{设定 ✓（照唐先生 ✓）}:\ C_3=(p,S),\ |S|{=}2,\ p\in E;\ D_3=(q,S),\ |S|{=}3,\ q\in O;\ F=(r,V),\ |V|{=}3,\ r\in E;\ G=(s,W),\ |W|{=}4,\ s\in O✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §1 之四条跨层公式\ \textbf{全部正确}（本档逐条复核 ＋ 与 C-458 穷举一致 ✓✓✓）}}$$
| 对 | $d$ 公式 | $d{=}1$ 唯一条件 | 与 C-458 穷举 |
|---|---|---|---|
| $C$–$F$ | $d(p,r)+5-2\|S\cap V\|$ ✓ | $\boxed{p=r\ \wedge\ S\subset V}$ ✓ | $d{=}1$ 240 对 ✓ |
| $D$–$F$ | $d(q,r)+6-2\|S\cap V\|$ ✓ | $\boxed{d(q,r){=}1\ \wedge\ S=V}$ ✓ | $d{=}1$ 240 对 ✓ |
| $D$–$G$ | $d(q,s)+7-2\|S\cap W\|$ ✓ | $\boxed{q=s\ \wedge\ S\subset W}$ ✓ | $d{=}1$ 240 对 ✓ |
| $C$–$G$ | $d(p,s)+6-2\|S\cap W\|\in\{3,5,7,9\}$ ✓ | $\boxed{\text{无}}$ ✓✓ | 最小 $d{=}3$ ✓✓ |
$$\qquad\Longrightarrow\ \boxed{\text{跨层图\ \textbf{确实分裂为三局部机制}}}\ ✓✓:\ C{\to}F\ (\text{内含})\mid D{\to}F\ (\text{精确等式})\mid D{\to}G\ (\text{内含});\quad \boxed{C\not\to G}\ ✓✓$$
$$\boxed{\textbf{(2) ✓✓✓$M_C$ 精确定值表（本档穷举，＝唐先生 P1 ✓✓）}:\ \text{合法 packing（两两 }|\cap|\le1\big)\ \text{共 }\mathbf{270}\ \text{个}\ \big(1{:}20,2{:}100,3{:}120,4{:}30✓\big);\ \text{无约束最大 }=\mathbf4✓}$$
| $\|C_p\|{=}m$ | 最坏 $M_C$ | 最好 $M_C$ | 备注 |
|---|---|---|---|
| 0–1 | 4 | 4 | 满容量 ✓ |
| 2–3 | 3 | 4 | |
| 4 | **2** | 3 | |
| 5 | **1** | 3 | |
| 6 | **0** | **3** ✗✗ | **最坏/最好分裂** |
| 7–9 | 0 | 2 | |
| 10–12 | 0 | 1 | |
| 13–15 | 0 | 0 | |
$$\qquad\Longrightarrow\ \text{（配对使用量对偶 ✓）}:\ \text{配对的 pair 集 }U\text{（}|\U|{=}3s\big)\ \text{必须避开 }P\Longrightarrow\ \text{等效于"}m\ \text{个 pair 之补图无三角形"\ ✓}$$
$$\boxed{\textbf{(3) ✗✗唐先生 §6 之门槛须改}:\ \tau_3(6){=}6\ \text{作为\ \textbf{最小值}正确}\ ✓\ \big(\text{Turán }\mathrm{ex}(6,K_3){=}9\Rightarrow|\mathcal P|\ge6✓\big);}$$
$$\qquad\textbf{但"}|C_p|\ge6\Longrightarrow F_p=\varnothing\text{"}\ \textbf{为假}\ ✗✗\ \big(\text{穷举：}m{=}6\ \text{时最好情形仍有 }M_C{=}\mathbf3✓✓\big)$$
$$\qquad\textbf{正确 ✓✓}:\ F_p=\varnothing\iff \text{每个三元组皆含 }P\ \text{中某 pair}\iff \boxed{P^c\ \text{无三角形}}\ \big(\text{＝}P\ \text{含某 }K_{3,3}\ \text{划分之补}\ ✓\big)$$
$$\qquad\qquad\Longrightarrow\ \text{最小杀尽集恰为 }P^c\cong K_{3,3}\ \big(\text{10 个划分 × 各自补}\ ✓\big)\Longrightarrow\ \text{方向①：}\boxed{F_p=\varnothing\Rightarrow|C_p|\ge6}\ ✓\ \big(\text{必要 ✓，非充分 ✗}\big)$$
$$\qquad\qquad\Longrightarrow\ \text{方向②（更强 ✓✓）}:\ \text{由表 }\ |F_p|{=}4\Longrightarrow|C_p|\le\mathbf3✓✓\ \big(\text{非唐先生之 }\le5\ ✗✗\big);\quad |F_p|{=}3\Rightarrow|C_p|\le6✓;\ |F_p|{=}2\Rightarrow|C_p|\le9✓$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓✓}:\ \text{四条公式与三条 }d{=}1\ \text{刻画全部正确 ✓✓✓\ \big(\text{见 §0(1) 表 ✓}\big)；唯 }C\text{–}F\ \text{之 }d\ \text{式宜写 }5-2|S\cap V|+\dots\ ✓\ \text{（其写 }d(p,r)+5-2|\cdot|\ ✓✓\big)$$
$$\textbf{§2 ✓✓}:\ \text{机制分裂图 ✓✓;\ 表 ✓✓（}C{\to}F\ \text{内含}、D{\to}F\ \text{等式}、D{\to}G\ \text{内含}、C{\not\to}G\ ✓✓\big)$$
$$\textbf{§3 ✓✓}:\ \text{对固定 }p:\ V\in\mathcal F_p\Rightarrow S\not\subset V\ \forall S\in\mathcal C_p✓✓;\ \mathcal F_p\ \text{为 packing（}|\cap|\le1✓\big)\ ✓;\ \text{故 }|F_p|\le M_C(\mathcal C_p)✓✓$$
$$\textbf{§4 ✓✓}:\ \text{一个 }S\ (\|S\|{=}2\big)\ \text{之超集三元组 }=\ 6-2=\mathbf4\ \text{个 ✓✓;\ 故一 }C\text{-点杀同 bucket 恰 4 个 }F\text{-候选 ✓✓}$$
$$\textbf{§5 ✓（情形分类 ✓）}:\ \text{相交/不相交两情形 ✓;\ \text{"pair-cover ⟹ }F_p{=}0\text{"}\ ✓\ \text{方向正确 ✓（唯 }|C_p|{=}6\ \text{不足 ✗，须补图无三角形 ✓）}}$$
$$\textbf{§6 ✗✗}:\ \text{见 §0(3)：}\tau_3(6){=}6✓\ \text{但"}\ge6\ \text{即杀尽"}\ ✗\ \text{—— 系把 Turán 之\ \textbf{边数下界} 当成了\ \textbf{充分条件} ✗✓}$$
$$\textbf{§7 ✗（方向 ✓，数值弱）}:\ |F_p|{=}4\Rightarrow|C_p|\le5\ ✗\to\ \le\mathbf3✓✓;\quad \text{其"实 coupling"\之定性 ✓✓}$$
$$\textbf{§8 ✓✓}:\ D{\to}F\ \text{为精确删点}:\ (q,S)\ \text{杀 }(p,S)\ \forall p\sim q\ ✓✓\ (\text{至多 3 个 bucket ✓✓});\ \text{故 }F_p\ \text{须避开 }\bigcup_{q\sim p}\mathcal D_q✓✓$$
$$\textbf{§9 ✓✓}:\ \text{删除 }N_2\ \text{路线 ✓✓（C-458 已证空 ✓）；P1/P2/P3 之提法 ✓✓（P1 本档已完成 ✓✓）}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 跨层 }d{=}1\ \text{四机制（含 }C{\not\to}G\ \text{）}✓✓✓;\quad \text{② }M_C(m)\ \text{精确最坏/最好表}✓✓✓;\quad \text{③ }F_p{=}\varnothing\iff P^c\ \text{无三角形}✓✓;\quad \text{④ }|F_p|{=}4\Rightarrow|C_p|\le3✓✓;\quad \text{⑤ }D{\to}F\ \text{精确删点}✓✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}|C_p|\ge6\Rightarrow F_p{=}0\text{"}\ ✗✗;\ \text{"}|F_p|{=}4\Rightarrow|C_p|\le5\text{"}\ ✗;\ \text{"跨层 }d{=}2\text{"}\ ✗\ \big(\text{C-458 ✓}\big)$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ M\ \text{之真值};\ \text{（}|C|\le12\ \text{与 }\sum_p|C_p|\ \text{之联合尚未成式 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① P2：}\bigcup_{q\sim p}\mathcal D_q\ \text{叠加后之四 bucket 联合容量 ✓;\ \text{② P3：三 extremal（}(0,4,4,4),(2,2,2,4),(2,2,3,3)\big)\ \text{配 }|C_p|\le3\ \text{之可行性 ✓;\ \text{③ }|C|\le12\ \text{与 }\sum|C_p|\ \text{之预算分配 ✓}}}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "四机制分解" "精确删点" "容量门槛表"
技术词 四机制分解 命中文件数=0    ::
技术词 精确删点   命中文件数=0    ::
技术词 容量门槛表 命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 四机制分解 | 0 | 0 | ✓（自造标签 ✓） |
| 精确删点 | 0 | 0 | ✓（自造标签 ✓） |
| 容量门槛表 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限穷举：$2^{15}$ 个 $P$ × 270 packing ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **两处必改**（§6 门槛之充分性／§7 之 $\le5\to\le3$）已在 §0(3) 显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
