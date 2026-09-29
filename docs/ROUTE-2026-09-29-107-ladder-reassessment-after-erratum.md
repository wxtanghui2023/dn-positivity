# ROUTE-2026-09-29-107-ladder — 复现 107 的路线重估（×2 勘误后）

> 空间 B｜非 C 号｜依唐先生令（22:21「先复现 107」）＋ 新勘误 `ERRATUM-2026-09-29-n1`｜**不主张 107 已证**（V290）
> 时间：2026-09-29 22:4x

**已查地图**：承 `AUDIT-2026-09-29c/d/e/f/n`、`MASTER-FAILURE-MAP-107-LINE` §2–§6、`ROUTE-FINGERPRINTS`（R02 pair 层已封／R15 高阶 SDP 已死／R16–R17 论文禁区）
D0: 本档对象 = **档案已有**（复现账／阶梯／恒等式）之**重估**（新数学对象：无 ✗）
D1: 0（产出 = 路线重估 ＋ 一张可用等式/不等式清单 ⚠️✓）

---

## §1 勘误后的正确起点（引 `ERRATUM-2026-09-29-n1`）

$$\boxed{\text{已撤回}:\ N_{\le2}\ge\Sigma\delta\ \text{（}M{=}106\Rightarrow142\text{）};\quad \text{正确}:\ N_{\le2}\ \ge\ \tfrac12\Sigma\delta\ \text{（}M{=}106\Rightarrow\mathbf{71}\text{）}}$$
$$\therefore\ \mu_{\max}\ge4\ \text{之推论作废；「一格缺口」为假象，真缺口}\approx\mathbf{72}\ (N_{\le2}\ \text{单位})\ ✗$$

## §2 复现阶梯（**按序爬**，逐级可判定）

$$94\ (\text{球界})\ \checkmark\ \to\ 103\ (\text{van Wee},\ \checkmark\ \text{已自推})\ \to\ \mathbf{105}\ (\text{Zhang--Lo 三重层},\ \textbf{缺})\ \to\ \mathbf{107}\ (\text{BÖW 混合框架},\ \textbf{缺})$$

$$\boxed{\text{⚠️ 对我 22:2x 说法的更正}:\ \text{「甲」（三重层）\ \textbf{不自动直接给 }107}$$
$$\text{文献谱系（档案）}:\ \text{van Wee}\to103\ \text{（已自推）};\ \text{Zhang 1991 \textbf{pair}}\to105\ \text{（我方 R02 已封 ⟹ 未复现）};\ 107\ \text{出自 BÖW 2004 \textbf{混合框架}}$$
$$\therefore\ \text{甲（三重层）之 \textbf{最近检查点} = \text{排除 }M{=}104\ (\Sigma\delta{=}120)\Longrightarrow K\ge105;\ \text{能否越过 105 \textbf{待算}，\textbf{不得预设}}⚠️$$

## §3 可用等式/不等式清单（**本档汇总，全部已核**）

| 编号 | 内容 | 状态 |
|---|---|---|
| F1 | $\Sigma_x\mu(x)=11M$ | 恒等式 ✓ |
| F2 | $y\in C\Rightarrow\mu(y)=1+a_y,\ \delta(y)=a_y$（$a_y=$ 距 1 邻词数） | 恒等式 ✓（**是 E1 之根**） |
| F3 | $\Sigma_x\binom{\mu(x)}2=2N_{\le2}$，$N_{\le2}=A_1+A_2$ | 恒等式 ✓ |
| F4 | $\Sigma_x\binom{\mu(x)}3=P+E$，$P=\Sigma_{y\in C}\binom{a_y}2$，$E=$ 等边三点组 | 恒等式 ✓（恒等式 T） |
| F5 | $P\le2A_2$ | **新** ✓（两码核验） |
| F6 | $\Sigma_{x\notin C}\delta(x)=11M-1024-2A_1\ \ge0$ | 恒等式 ✓ ⟹ $A_1\le71$（$M{=}106$） |
| F7 | $\Sigma_x\binom{\mu}2\ \ge\ \Sigma\delta$ ｜ $N_{\le2}\ge\tfrac12\Sigma\delta$ | 勘误后正确式 ✓ |
| F8 | $E=\Sigma_{x\notin C}\binom{\mu(x)}3+\Sigma_{y\in C}\binom{a_y}3$ | 恒等式 ✓（由 F2＋F4；**双码穷举核验** 42=40+2／97=91+6 ✓✓） |

## §4 结构性要点（**决定攻击形态**）

$$\text{因 } E=11M-1024\ \text{是\ \textbf{恒等式}}\ \Longrightarrow\ \text{排除 }M{=}106\ \text{不可能靠"某个只含 }M\ \text{的单量界"}\ \text{反复套用}$$
$$\Longrightarrow\ \text{必须给出一套\ \textbf{多量联立}（}M,\ N_{\le2},\ A_2,\ P,\ E,\ \mu\text{-剖面}）\text{，并使该系统在 }M{=}106\ \text{处\ \textbf{不可行}}$$
$$\text{且因 }E\ \text{被 }M\ \text{锁定}，\text{任何"强制 excess"路线都需\ \textbf{在 }M\ \text{的特定值上扣}——这与 }AUDIT\text{-}29x\ \text{的"逆趋势"结论一致}\ ⚠️$$

## §5 下一步（可执行，按序）

- **S1（甲·第一级）**：用 F4/F8 ＋ F5 求 $\Sigma_x\binom{\mu}3$ 之**两侧夹逼**，目标先**排除 $M{=}104$** ⟹ $K\ge105$
- **S2**：把 F5 强化为 $P\le2A_2-\Theta$（$\Theta$＝共同邻点非码字之双计数），再回代 F4
- **S3**：$M{=}106$ 级（⟹107）须引入**混合/短化框架**（BÖW 型），**非**三重层所能及 ⚠️；须先做完 S1/S2 再评估

## §6 边界（硬 ✓）

- **不主张 105／107** ✗；S1/S2 为**候选**，未动算前不得预设可行 ✓
- **未重攻** pair 层（R02）／高阶 SDP（R15）／论文原文（R16–17）✓；未碰 RH ✓
- 勘误后的数字一律**两个已知码双验**（本次已验）✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=NA R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
