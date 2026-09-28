# WITUOBJ-2026-09-28 — **$U$ 之对象声明（$|U|{\le}119$ 为构造性恒等式，非待证输入 ✗）；①② 确认；桥之干净形式 $X_L\to q$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:17 令 ✓）**：$U$ 之对象审计 ＋ 桥之重画；**零程序计算**（符号/整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-470／C-436／C-435，非新案 ✓）**
`docs/WITMAP-2026-09-28-…`（**状态图＋桥定量核心 ✓✓✓**）｜`docs/WITW2C-2026-09-28-…`（**$s{=}|U|\ge62$／$|H|{=}119{-}s$ ✓✓✓**）｜`docs/WITFIB-2026-09-28-…`（**$U_b\subseteq P_{1-b}$／$a,b\ge44$ ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §4）
D0: 本档对象 ＝ **档案已有** $U$／$H$／$X_L$／$q$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次定出 "$|U|{\le}119$" 为\ \textbf{构造性恒等式}（$U{:=}P_0{\cup}P_1$、$|P_0|{+}|P_1|{=}119$）而非待证输入 ＋ 首次确认全空间恒等式 $9|H|{+}2q$ 与 $|X_L|{\le}2q$ ＋ 首次指出 $U$ 之两义（层并 vs $A_0$-球并）** ✓）
**[RESEARCH]**

---

## §0 三件定死（**①✓ ②✓ ③✗定向更正**）

$$\boxed{\textbf{(1) ✓✓唐先生 §① 正确（}X_L\ \text{版本）}:\ }\text{令 }H:=C_0\cap C_1,\ X_L:=U^c\setminus N(H)✓\ \text{则仅对 }x\in X_L\ \text{可排除 }d(u,v){=}0✓$$
$$\qquad\Longrightarrow\ \boxed{x\in X_L\Longrightarrow\exists\,u\in C_0,\ v\in C_1:\ d(u,v){=}2}\ ✓✓\ \big(\text{＝C-438 ✓✓；C-469 之层距离-2 表\ \textbf{真正约束的是 }X_L✓}\big)$$
$$\boxed{\textbf{(2) ✓✓唐先生 §② 正确（全空间恒等式）}:\ }\sum_{x\in\mathbb F_2^9}r_0(x)\,r_1(x)\ =\ 9|H|\ +\ 2q\ ✓✓\quad\big(r_b{:=}|C_b\cap N(x)|,\ q{:=}\#\{(u,v)\in C_0{\times}C_1:d(u,v){=}2\}\big)$$
$$\qquad\textbf{（证明 ✓✓）}:\ \text{展开 }=\sum_{(u,v)\in C_0\times C_1}|N(u)\cap N(v)|✓;\ \text{对角 }u{=}v{=}h\in H\ \text{给 }|N(h)|{=}9✓;\ \text{非对角非零 iff }d{=}2\ \text{且给 }2✓⟹9|H|{+}2q✓✓$$
$$\qquad\Longrightarrow\ \text{限制到 }X_L\ \text{时 heavy 项消失（}X_L\cap N(H){=}\varnothing✓\big)\Longrightarrow\boxed{|X_L|\ \le\ \sum_{x\in X_L}r_0r_1\ \le\ 2q}\ ✓✓\ \big(\text{唐先生 ✓}\big)$$
$$\boxed{\textbf{(3) ✗✗唐先生 §③ 须定向更正：}|U|\le119\ \text{不是待证输入，而是}\textbf{构造性恒等式}\ ✓✓}$$
$$\qquad\textbf{（档案之定义 ✓✓，C-435／C-436 ✓）}:\ U:=P_0\cup P_1\ \big(\text{两层投影之并 ✓}\big);\ \boxed{|C|=|C_0|+|C_1|=|P_0|+|P_1|=119}\ ✓\ \text{（恒等式 ✓✓）}$$
$$\qquad H=P_0\cap P_1\Longrightarrow\boxed{|U|=|P_0\cup P_1|=|P_0|+|P_1|-|H|=119-|H|\ \le\ 119}\ ✓✓\ \textbf{平凡成立}$$
$$\qquad\text{且 }U\ \text{是 9-cover ✓}\ \big(\mathbb F_2^9=N[P_0]\cup P_1\wedge N[P_1]\cup P_0\Longrightarrow\mathbb F_2^9=N[U]✓\big)\Longrightarrow\boxed{|U|\ge K(9,1)=62}\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{62\le|U|\le119}\ \text{两端\ \textbf{皆已成立}}✓✓\Longrightarrow\ \text{撤回 }|U^c|\ge393\ \text{与 }q\ \text{之下界}\ \textbf{属误撤} ✗✗$$

---

## §1 为何 §③ 会误读（**对象两义 ✓✓**）

$$\textbf{根因 ✓✓}:\ \text{唐先生之 }U=\bigcup_{a\in A_0}N(a)\ \text{是\ \textbf{另一个对象}}\ ✗\ \big(\text{＝}A_0\ \text{之球并 ✓，}|{\cdot}|\le10|A_0|\le400✓\big)\ \text{与档案之 }U=P_0\cup P_1\ \textbf{不同} ✗$$
$$\qquad\Longrightarrow\ \textbf{纪律（再次 ✓✓）}:\ \text{凡用 }U/H/X_L/C_0/C_1/N/A_0\text{，须\ \textbf{先声明对象}（＝第 6 次同类混淆 ✓）}$$
| 记号 | 档案义（✓ 本线） | 唐先生本轮所用（✗） |
|---|---|---|
| $U$ | $P_0\cup P_1$（层并；$62\le|U|\le119$ ✓） | $\bigcup_{a\in A_0}N(a)$（球并；$\le400$ ✓） |
| $U^c$ | $\mathbb F_2^9\setminus U$（$|U^c|\ge393$ ✓） | 同左但基数不同 ✗ |
| $H$ | $P_0\cap P_1$（$|H|{=}119{-}s$ ✓） | 同 ✓ |
| $X_L$ | $U^c\setminus N(H)$ ✓ | 同 ✓ |

$$\Longrightarrow\ \textbf{结论 ✓}:\ \text{桥之输入\ \textbf{不}需重算}✓;\ |U^c|\ge393✓\ \text{与 }q\ge\lceil(8s{-}559)/2\rceil✓\ \text{保持 ✓✓}$$

## §2 桥之干净形式（**照唐先生 ✓✓**）

$$\boxed{\text{Type II }(F,G,D)\to U\to H\to X_L=U^c\setminus N(H)\to q\to\text{层容量}}\ ✓✓\ \big(\text{替代 }U^c\to q✓\big)$$
$$\textbf{(A) ✓}:\ |U|\ \text{上界}:\ 62\le|U|\le119✓\ \text{（构造性 ✓，无需重算 ✓✓）}$$
$$\textbf{(B) ✓}:\ |N(H)|\le9|H|\Longrightarrow|X_L|\ge|U^c|-9|H|=8s-559✓$$
$$\textbf{(C) ✓}:\ |X_L|\le2q\Longrightarrow\boxed{q\ \ge\ \Big\lceil\frac{8s-559}{2}\Big\rceil}\ ✓✓\ \big(\text{仅 }s\ge70\ \text{生效；}s<70\ \text{无约束 ✓}\big)$$
| $s=|U|$ | $\|U^c\|$ | $\|H\|$ | $8s{-}559$ | $q_{\min}$ |
|---|---|---|---|---|
| 62 | 450 | 57 | −63 | 0（无约束 ✓） |
| 70 | 442 | 49 | 1 | 1 |
| 80 | 432 | 39 | 81 | 41 |
| 100 | 412 | 19 | 241 | 121 |
| 119 | 393 | 0 | 393 | **197** ✓（此前 197 之来源 ✓） |
$$\textbf{(D) ✓}:\ \text{层允许矩阵}:\ q=\sum_{a,b}q_{ab}✓;\ \text{69 零格删去 ✓✓（C-469 ✓）}$$
$$\textbf{(E) ⚠️}:\ \text{层容量}: q\le Q_{\max}(\text{Type II state})✓\ \text{——\ \textbf{未求}（下一轮有限穷举 ✓）}$$
$$\textbf{(F) ⚠️}:\ \text{预算碰撞}:\ 11\le c{+}d\le18,\ d\le16✓\ \big(\text{C-465／C-467}\big)$$

## §3 下一轮唯一靶点（**照唐先生 ✓✓**）

$$\boxed{\text{Type II}\to\big(|U|,\ |H|,\ |X_L|\big)\to q_{\min}\quad\text{vs}\quad q_{\max}^{\text{layer}}}\ ✓✓$$
$$\textbf{（先不碰 197 ✓✓）}:\ \text{先问：Type II 全部合法 }(F,G,D)\ \text{状态下，}Q_{\max}:=\max q\ \text{与}\ L_{\rm cov}:=\min|X_L|\ \text{各为多少}✓$$
$$\qquad\textbf{若 }L_{\rm cov}>2Q_{\max}\ \Longrightarrow\ \text{Type II 直接死 ✓✓};\quad \textbf{若 }L_{\rm cov}\le2Q_{\max}\ \Longrightarrow\ \text{纯 }q\text{-容量桥不够 ⚠️，须进精细分配（共同邻落入 }U\ \text{vs }X_L\text{）}$$
$$\qquad\Longrightarrow\ \text{此检验\ \textbf{不依赖 }197✓\ \text{，且不依赖 }|U|\le119\ \text{之"待证"（实为恒等式 ✓）}}✓✓$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "对象声明" "恒等式分区" "条件撤回"
技术词 对象声明   命中文件数=0    ::
技术词 恒等式分区 命中文件数=0    ::
技术词 条件撤回   命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 对象声明 | 0 | 0 | ✓（自造标签 ✓） |
| 恒等式分区 | 0 | 0 | ✓（自造标签 ✓） |
| 条件撤回 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §5 边界（硬 ✓）

- **零程序计算** ✓（仅符号代数与整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **一处定向更正**（§0(3)：$|U|\le119$ 为恒等式）＋ **一处对象两义**（§1）已显式标注 ✓✓
- **词回查三词皆 0** ⟹ 本档新术语 0 ✓（皆自造结构标签，不作新性主张 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
