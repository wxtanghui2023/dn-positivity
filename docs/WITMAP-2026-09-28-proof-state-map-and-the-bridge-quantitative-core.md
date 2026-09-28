# WITMAP-2026-09-28 — **当前证明状态图（C-448→C-469 五栏总览）＋ 桥之定量核心恒等式**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:10 令 ✓）**：一页状态图（供下次开工 ✓）＋ 覆盖桥之定量化；**零程序计算**（仅符号/整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-469／C-468／C-465，非新案 ✓）**
`docs/WITBRIDGE1-2026-09-28-…`（**层间距离-2 表／双覆盖配对 ✓✓✓**）｜`docs/WITCSIDE-2026-09-28-…`（**三更正／$c_{\min}^{\rm local}{=}0$ ✓✓✓**）｜`docs/WITBUD-2026-09-28-…`（**$11\le c{+}d\le18$ ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §4）
D0: 本档对象 ＝ **档案已有** 状态图／$q_{ab}$／共同邻点对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 C-448→C-469 之五栏状态图（含状态符号与下一步）＋ 首次写出桥之\ \textbf{定量核心恒等式}（含 heavy 项与 $|H|{=}|U^c|{-}393$）＋ 首次指出粗界在 $s\gtrsim80$ 非真空** ✓）
**[RESEARCH]**

---

## §0 一页状态图（**C-448 → C-469**）

| 模块 | 当前结论 | 状态 | 下一步 |
|---|---|---|---|
| **P0 结构／定义** | $A_0$ 按 $A_1$ 之 profile 分 14 层 ✓；$C,D,F,G$ 依 profile 定层 ✓；跨层距离公式（$d{=}d_{\text{pref}}{+}\|\triangle\|$）✓；$N$＝$Q_9$ 普通 Hamming 邻域 ✓；$C_0,C_1$ 为 $(x,b)\in C$ 之投影、$A_0\subseteq A=C_0\setminus\{h\}$ ✓ | **✓ 闭** | 不再改标签（$\operatorname{supp}$ 须声明 ✓） |
| **F/G 局部结构** | Type I $(0,4,4,4)$：**KILLED** ✓✓✓（30 状态图无三角形，C-463；不依赖 $D$）｜Type II $(4,2,2,2)$：局部**有显式见证** ✓（C-463）｜Type III $(2,2,3,3)$：未查 | **I ✓ ＼ II ○ ＼ III ○** | 先 II |
| **D 侧** | 角色分算：近三桶 $(4,4,4)$、远桶 $2{\sim}4$ ⟹ $|D|\le14{\sim}16$ ✓；跨层 $d{=}2$ **空** ✗（奇偶性）；$d{=}1$ 四机制 ✓ | **✓ 天花板（暂停）** | 不再细抠 |
| **C 局部侧** | $c_{\min}^{\rm local}{=}0$ ✓✓（$C_p$ 可取空）；仅有上界 $|C_p|\le3$（满桶 ✓ C-461）／$\le9$；$\|C\|\le12$ | **✓ 已排除（局部无下界）** | 转全球覆盖 |
| **覆盖桥** | 双覆盖 ⟹ $C_0\times C_1$ 须含距离-2 对；C-469 给出 14 层允许表（69 零对 ✗）；**定量核心＝§1 恒等式** | **○ 唯一主攻口** | 数量化 $q_{ab}$ |

$$\textbf{累计关键不等式 ✓}:\ \boxed{11\le c+d\le18}\ \big(\text{C-465}\big);\quad |D|\le14{\sim}16\ \big(\text{C-467}\big);\quad |C|\le12\ \big(\text{C-453}\big);\quad |A_0|\le40\ \big(\text{C-457}\big);\quad |C_0|\ge45\ \big(\text{C-442}\big)$$
$$\textbf{已闭负结果（不再重开 ✓）}:\ \text{跨层 }d{=}2\ \text{机制}\ ✗;\ \text{"}|C_p|\ge6\Rightarrow F_p{=}\varnothing\text{"}\ ✗;\ \text{"单 triple 贡献 lemma"}\ ✗;\ \text{"}t{=}\#\{d_i{\ge}5\}\text{"}\ ✗;\ \text{"}|R_q|{=}4\ \text{恒成立"\ ✗;\ \text{"}c_{\min}\ \text{可局部取得"\ ✗;\ \text{C-466 之 }[10,14]\ ✗;\ \text{"}F_0\ \text{与}\ \partial^-G\ \text{不重叠"}\ ✗}}$$

---

## §1 桥之定量核心（**新 ✓✓**）

$$\textbf{设定 ✓}:\ C_0,C_1\subseteq Q_9\ \text{为 119-码之两层投影 ✓};\ U^c:=\{\,x\notin U\,\}✓;\ H:=C_0\cap C_1\ \big(\text{heavy ✓}\big);\ |H|{=}119-s{=}|U^c|-393✓\ \big(s{=}|U|✓\big)$$
$$\boxed{\textbf{(1) ✓✓✓精确恒等式（本档）}:\ }\sum_{x\in U^c}\big|C_0\cap N(x)\big|\cdot\big|C_1\cap N(x)\big|\ =\ \sum_{(u,v)\in C_0\times C_1}\big|N(u)\cap N(v)\cap U^c\big|$$
$$\qquad\Longrightarrow\ \boxed{\ \sum_{h\in H}\big|N(h)\cap U^c\big|\ +\ r\ \ \ge\ \ |U^c|\ }\qquad \Big(r:=\sum_{\substack{u\ne v\\ d(u,v)=2}}\big|N(u)\cap N(v)\cap U^c\big|\Big)✓✓$$
$$\qquad\textbf{两项之结构 ✓✓}:\quad \text{heavy 项}\ \le 9|H|;\qquad r\le 2\cdot\#\{\text{距离-2 对}\}\ \big(Q_9\ \text{中 }d{=}2\ \text{恰有两个共同邻 ✓}\big)$$
$$\qquad\textbf{（右端 }|U^c|✓\big)}:\ \text{每 }x\in U^c\ \text{两因子皆}\ \ge1✗\Longrightarrow \text{乘积}\ \ge1✓\ \big(\text{C-437 ✓\big)$$
$$\boxed{\textbf{(2) ✗✗但须保留 heavy 项（唐先生此轮写 }u\ne v\Rightarrow d(u,v){=}2\text{）}:\ }\text{对 }U^c\ \textbf{全体}\ \text{不成立}\ ✗✗$$
$$\qquad\textbf{反例 ✓✓}:\ h\in H=C_0\cap C_1\ne\varnothing\ \big(|H|{=}|U^c|-393✓\big)\Longrightarrow u=v=h\ \text{可单独完成双覆盖} \Longrightarrow d{=}0✓\ \text{非 }2✗$$
$$\qquad\Longrightarrow\ \text{正确定义（＝C-438 之修正 ✓✓）}:\ \text{仅对 }X_L:=U^c\setminus N(H)\ \text{才强制 }d{=}2✓ \big(\text{即}\ r\ \text{项只服务于 }X_L✓\big)$$
$$\boxed{\textbf{(3) ✓粗界之真空/非真空分界（本档 ✓）}:\ }\text{用}\ \sum_H\le9|H|\ \text{与 }|H|{=}|U^c|-393:$$
| $s=|U|$ | $\|U^c\|$ | $\|H\|$ | $9\|H\|$ | 粗界 $|U^c|\le9|H|+r$ |
|---|---|---|---|---|
| 62 | 450 | 57 | 513 | **真空** ✗（须 $r\ge0$ 自动成立 ✓） |
| 80 | 432 | 39 | 351 | **有约束** ✓（须 $r\ge81$ ✓） |
| 100 | 412 | 19 | 171 | **有约束** ✓（须 $r\ge241$ ✓） |
| 119 | 393 | 0 | 0 | **有约束** ✓（须 $r\ge393$ ✓，全由距离-2 对承担 ✓） |
$$\qquad\Longrightarrow\ \text{桥之定量目标（唐先生 §"共同邻点容量"✓✓）}:\ \boxed{r\ \ge\ |U^c|-9|H|\ =\ 8|U^c|-3537}\ ✓\ \text{须与 }q_{ab}\ \text{之层上界冲突 ✓}$$
$$\qquad\textbf{（层细化之接口 ✓✓）}:\ q_{ab}:=\#\{(u,v)\in C_0^{(a)}\times C_1^{(b)}:d(u,v){=}2\}\Longrightarrow r\le2\sum_{a,b}q_{ab}✓;\ \text{且 }q_{ab}{=}0\ \text{对 C-469 之 69 零层对 ✓✓}$$

---

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生之总览五栏结构\ \textbf{照其指定} ✓✓（本档 §0 ✓）};\ \text{其 }q_{ab}\ \text{之定义（含层上标）✓✓};\ \text{"共同邻点恰 2"}\ ✓✓;\ Q(C_0,C_1){=}2q\ \text{之写法 ✓✓};\ \text{"目标应攻 }c{+}d\ \text{预算而非 }c\ \text{本身"\ ✓✓（}c{+}d{<}11\ \text{即死 ✓✓ 正确）}$$
$$\textbf{✗✗}:\ \text{"}u\ne v\Rightarrow d(u,v){=}2\ \text{对 }U^c\ \text{全体"\ ✗（见 §1(2)；须拆分 }H\ \text{与 }X_L✓）$$
$$\textbf{⚠️}:\ \text{其 }|A_0|{=}22+c+d\ ✓✓\ \text{仅在 }t{=}0\ \text{时 ✓}\ \big(\text{C-468 ✓：正确 }t\ \text{为高层点数，未必 }0✗\big)\Longrightarrow\ \text{通式 }|A_0|{=}22+c+d+t✓$$
$$\textbf{✓}:\ \text{"}d\le16\ \text{与 }11\le c+d\le18\ \text{联立 ⟹ 不需强 }c\ \text{下界"\ ✓✓（诚实且正确 ✓）}$$

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{正式靶题 ✓（照唐先生 ✓）}:\ \boxed{\text{Type II covering bridge}:\ (F,G,D)\Longrightarrow\ \text{共同邻点容量上界}\ \Longrightarrow\ c+d\le10\ ?}\ ✓✓$$
$$\textbf{第一步 ✓}:\ \text{把 }\S1(3)\ \text{之 }r\ \text{下界}\ 8|U^c|-3537\ \text{按层分裂，与 }q_{ab}\ \text{之层上界（含 C-469 之 69 零对 ✓）冲突 ✓}$$
$$\textbf{第二步 ✓}:\ \text{若不成，退守 }q_{ab}\ \text{之\ \textbf{精确层矩阵}}✓\ \text{（14×14，可穷举 ✓）};\quad \textbf{第三步 ✓}:\ \text{Type III}$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "当前证明状态图" "共同邻点计数" "heavy替代"
技术词 当前证明状态图 命中文件数=0    ::
技术词 共同邻点计数   命中文件数=0    ::
技术词 heavy替代      命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 当前证明状态图 | 0 | 0 | ✓（自造标签 ✓） |
| 共同邻点计数 | 0 | 0 | ✓（自造标签 ✓） |
| heavy替代 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §5 边界（硬 ✓）

- **零程序计算** ✓（仅符号代数与整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **一处必改**（§1(2) 之 heavy 项）已在 §0／§1 显式标注 ✓✓；**一处补充**（$|A_0|{=}22{+}c{+}d{+}t$）已标 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
