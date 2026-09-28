# WITCEIL-2026-09-28 — **$|A_0|\le A(9,3)=40$ 支配层和：唐先生的 $42$／$41$ 均不可达（✓✓✓）；跨层禁配 ✓**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:39 令 ✓）**：$d{=}3$ 与 $d{=}4$ 两层耦合；**零程序计算**（仅有限集合构造核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-456／C-455／C-453，非新案 ✓）**
`docs/WITCAPP-2026-09-28-…`（**$\max(|F|{+}|G|)\le22$ ✓✓✓**）｜`docs/WITDEC-2026-09-28-…`（**$c+d\le20$／$|F|\le16$／$|G|\le12$ ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $A(9,3)$／层和／跨层距离-2 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次指出 $c+d+f+g\le|A_0|\le A(9,3)=40$ 支配独立层和（$42$／$41$ 不可达）＋ 首次定出 $(6,6,6,8)$ 与 $(6,8,8,8)$ 两层各 $\le1$** ✓）
**[RESEARCH]**

---

## §0 结论（**天花板支配 ✓✓✓｜跨层机制 ✓（但需精确极值）｜两小层 $\le1$ ✓**）

$$\textbf{设定 ✓}:\ A_0\subseteq R\ \big(396\ \text{点}\ ✓\big)\ \text{为前缀空间 }Q_9\ \text{之子集},\ d(A_0)\ge3✓✓;\quad C{=}A_0{\cap}(3,3,3,5),\ D{=}A_0{\cap}(3,5,5,5),\ F{=}A_0{\cap}(4,4,4,6),\ G{=}A_0{\cap}(4,6,6,6)✓$$
$$\boxed{\textbf{(1) ✓✓✓经典天花板支配（本档关键观察）}:\ A_0\ \text{是 }Q_9\ \text{上最小距离}\ge3\ \text{之码}\Longrightarrow\boxed{|A_0|\le A(9,3)=\mathbf{40}}✓✓\ \big(\text{经典值，C-442 已核 ✓}\big)}$$
$$\qquad\Longrightarrow\ \boxed{c+d+f+g\ \le\ |A_0|\ \le\ 40}✓✓✓$$
$$\qquad\Longrightarrow\ \textbf{唐先生 §1 之"独立相加得 }42\text{"}\ \textbf{一出现即被支配} ✗✗\ \big(\text{两层界}\ 20+22=42\ \text{并非独立 ✓}\big);\quad \text{其 §11 所拟"}$41$\text{"}\ \textbf{亦不可达} ✗✓$$
$$\qquad\Longrightarrow\ \text{（直接推论 ✓）}:\quad c+d=20\ \Longrightarrow\ f+g\le40-20=\mathbf{20}✓✓\ \big(\text{唐先生 §11 猜"}\le21\text{"✓\ \textbf{成立但理由平凡} ✗}\big)$$
$$\qquad\Longrightarrow\ c+d=19\Rightarrow f+g\le21✓;\qquad c+d=18\Rightarrow f+g\le22✓\ \big(\text{即 }C{+}D\text{ 每多 1 点，}F{+}G\text{ 上限自动降 1 ✓}\big)$$
$$\textbf{(2) ✓跨层机制（唐先生 §5）成立}:\ z\in C_3\cup D_3,\ v\in F\cup G,\ d(z,v)=2\Longrightarrow \text{非 }\exists✓✓\ \big(\text{因 }d(A_0)\ge3\ ✓;\ \text{此即既有约束之跨层实例}\ ✓\big)$$
$$\qquad\textbf{但 ⚠️}:\ \text{欲用 }\Phi(w):=N_2(w)\cap(F\cup G)\ \text{得 }\boxed{|F|{+}|G|\le22-\delta}\ \text{须先求}\ \textbf{精确极值}\ \max\{c{+}d{+}f{+}g:\ d\ge3\}✓$$
$$\qquad\qquad\text{本档仅得\ \textbf{构造下界} }25\ \big(\text{贪心，多重启 ✓}\big)\ \text{与上界 }40\Longrightarrow \textbf{该极值未定 ⚠️（登记，未穷尽 ✓）}$$
$$\qquad\qquad\textbf{诚实 ✓}:\ \text{贪心 }25\ \text{之 profile 分布 }=\{(3,3,3,5){:}8,\ (3,5,5,5){:}5,\ (4,4,4,6){:}6,\ (4,6,6,6){:}6\}\Longrightarrow c{=}8,d{=}5,f{=}6,g{=}6✓$$
$$\textbf{(3) ✓✓本档新小事实}:\ (6,6,6,8)\ \text{层与}\ (6,8,8,8)\ \text{层\ \textbf{各仅 4 点、且两两距离 2}}\ \Longrightarrow\ \boxed{\text{各}\le1}\ ✓✓\ \big(\text{同 C-453 之 singleton 论证}\ ✓\big)$$
$$\qquad\Longrightarrow\ \text{故 }d\ge5\ \text{诸层（}116\ \text{点}\ ✓\big)\ \text{中至少两层各}\ \le1✓\ \text{—— 对 }|A_0|{\ge}33\ \text{之计数有钳制作用 ✓}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✗✗}:\ \text{其 }|C|{+}|D|{+}|F|{+}|G|\le42\ \text{作为\ \textbf{可达上界}不成立}\ ✗\ \big(\text{被 }40\ \text{支配}\ ✓\big);\quad \text{唯 }22\ \text{与 }20\ \text{两式本身 ✓（C-456／C-453 ✓）}$$
$$\textbf{§2 ✓✓}:\ s_q\ \text{之局部函数（}g_q\le3\ (s\le8);\ \le1\ (9..12)\big)\ \text{引用正确 ✓✓};\quad 3|G|=\sum_q3g_q\ \text{之写法 ✓（形式 ✓）}$$
$$\textbf{§3 ✓✓}:\ |G|{=}12\Rightarrow g_q{\equiv}3\Rightarrow s_q\le8\Rightarrow3|F|\le32\Rightarrow|F|\le10✓✓\ \text{（=C-456 ✓）；}F{+}G\le22✓;\ |F|{=}10\ \text{时 }3|F|{=}30<32\ \text{留 2 单位 slack ✓✓（其观察对 ✓）}$$
$$\textbf{§4 ✓}:\ (0,4,4,4)\rightsquigarrow(12,10)\ \text{与}\ (2,2,2,4)\rightsquigarrow(10,12)\ \text{两端点 ✓（C-456 穷举 ✓）；"非唯一 extremal"\ ✓✓}$$
$$\textbf{§5 ✓✓}:\ \text{跨层 }\Phi(w)\ \text{提法 ✓✓};\ \text{唯须与 (1) 之天花板并列使用 ✓（否则 }42\ \text{无意义 ✗）}$$
$$\textbf{§6 ✓（形式 ✓）}:\ (s_q,g_q,r_q)\ \text{二维/三维 profile 之提法 ✓；}g_q\le h(s_q)-\rho_q\ \text{之形式 ✓（未验 ⚠️）}$$
$$\textbf{§7–§8 ✓（方向 ✓）}:\ \text{三元 }\mathcal W\ \text{之分类 ✓（}|Q_3|=8\ \text{自同构群小 ✓};\ \text{单/双/三重覆盖之分 ✓✓）；}|\mathcal W|{=}3\ \text{已定值 ✓（C-455 ✓）}$$
$$\textbf{§9 ✓（形式 ✓）}:\ \text{总量式 }42-\Delta\ \text{应改为 }40-\Delta✗\ \big(\text{天花板 }\big)✓$$
$$\textbf{§10 ✓✓}:\ "c{+}d{=}20\ \text{时不能任取 }F{+}G"\ ✓✓\ \text{—— 本档给出精确形式：}f+g\le20✓✓\ \big(\text{其猜 }21\ \text{不够紧 ✓}\big)$$
$$\textbf{§11 ✗}:\ "|C|{+}|D|{=}20\Rightarrow|F|{+}|G|\le21"\ ✓\ \text{但\ \textbf{真值为 }\le20}✓\ \big(\text{由 }40\ \text{直接 ✓}\big);\quad "C{+}D{+}F{+}G\le40"\ ✓\ \text{（与其 }\le41\ \text{相比即天花板 ✓）}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{c+d+f+g\le|A_0|\le40}✓✓✓;\ \text{② }c+d=20\Rightarrow f+g\le20✓✓;\ \text{③ }(6,6,6,8)\le1,\ (6,8,8,8)\le1✓✓;\ \text{④ 跨层 }\Phi\ \text{机制 ✓;\ \text{⑤ }|F|{+}|G|\le22\ (C-456 ✓),\ c+d\le20\ (C-453 ✓)}$$
$$\textbf{已否证 ✗✓}:\ "42\ \text{可达}"\ ✗;\ "41\ \text{可达}"\ ✗;\ "C{+}D{=}20\Rightarrow F{+}G\le21\ \text{为紧}"\ ✗;\ \text{"两层界独立"\ ✗}$$
$$\textbf{未确立 ⚠️}:\ \max\{c{+}d{+}f{+}g:\ d\ge3\}\ \big(\text{本档仅 }25{\le}\cdot{\le}40\ ✓\big);\ a{=}45\ \text{的排除};\ 3^4\ \text{全局可行性}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 精确求 }\max\{c{+}d{+}f{+}g\}\ \text{（须机制化/算法化，非贪心 ✗）};\ \text{② 若其 }<40\ \text{则天花板可再降 ✓；}\ \text{③ 更重要 ✓：转向\ \textbf{覆盖侧} —— }|A_0|{\ge}33\ \text{与 119 覆盖条件之联合（层容量已近耗尽 ✓）}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "经典天花板" "跨层禁配" "层和支配"
技术词 经典天花板 命中文件数=0    ::
技术词 跨层禁配   命中文件数=0    ::
技术词 层和支配   命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 经典天花板 | 0 | 0 | ✓（自造标签 ✓） |
| 跨层禁配 | 0 | 0 | ✓（自造标签 ✓） |
| 层和支配 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限集合构造（贪心下界）与层结构核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处必改**（$42\to40$ 之天花板）已在 §0(1) 显式标注 ✓✓；**贪心 25 仅下界 ⚠️** 已标 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
