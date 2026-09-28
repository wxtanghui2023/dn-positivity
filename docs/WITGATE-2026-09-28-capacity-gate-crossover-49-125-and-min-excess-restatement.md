# WITGATE-2026-09-28 — **容量闸门的精确形式**：交界点 $|C_0|=49.125$ ／「强制重叠损失 ≤ 滑动余量」／ $s\le61$ 分支为空

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:43 令 ✓）**：把容量闸门推进 → 收窄到 $\mathrm{cov}_9$ 精确形状／$|C_0|\le50$ 控制；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-439／C-435／C-436，非新案 ✓）**
`docs/WITCAP-2026-09-28-…`（**$9|C_0|+s\ge512$／去特化 ✓✓**）｜`docs/WITFIB-2026-09-28-…`（**$a,b\ge44$／$\mathrm{cov}_9$ 闸门 ✓✓**）｜`docs/WITW2C-2026-09-28-…`（**精确条件／双色 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词，见 §5）
D0: 本档对象 ＝ **档案已有** 容量闸门／$\mathrm{cov}_9$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出交界点 $393/8=49.125$ 的精确来源 ＋ 闸门的「重叠损失 ≤ 滑动余量」重述 ＋ $\mathrm{cov}_9(m)=9m\ (m\le40)$ 紧性事实 ＋ $s\le61$ 分支为空之更正** ✓）
**[RESEARCH]**

---

## §0 结论（**参数化形式与表 ✓｜交界点 ✓✓｜闸门重述 ✓✓｜致密度事实 ✓｜$s\le61$ 为空 ✗✗更正**）

$$\text{记号 ✓}:\ a:=|C_0|\ (\text{取小层 }\therefore44\le a\le59✓),\ b=|C_1|=119-a✓,\ s=|U|✓,\ |H|=119-s✓,\ |A|=a+s-119✓,\ |B|=b+s-119✓$$
$$\boxed{\textbf{(1) ✓参数化形式与表逐位核验通过（本档复核 ✓）}:\ \boxed{s\ \ge\ 512-9a}\ ✓\ \text{共 }a{=}42\Rightarrow134;\ 43\Rightarrow125;\ 44\Rightarrow116;\ 45\Rightarrow107;\ 50\Rightarrow62;\ 51\Rightarrow53;\ 56\Rightarrow8;\ 57\Rightarrow\text{−1（自动）}✓✓}$$
$$\boxed{\textbf{(2) ★★交界点的精确来源（新 ✓✓）}:\ \text{除容量约束外还有第二条}:\ H\subseteq C_0\Longrightarrow|H|=119-s\le a\Longrightarrow \boxed{s\ \ge\ 119-a}\ ✓✓}$$
$$\qquad\text{两者相等处}:\ 512-9a=119-a\iff393=8a\iff \boxed{a=\tfrac{393}8=49.125}\ ✓✓\ \Longrightarrow\ \text{交界在 }a=49\ \text{与}\ 50\ \text{之间}✓$$
$$\qquad\Longrightarrow\ \boxed{a\le49\ \text{由容量主导};\quad a\ge50\ \text{由「}H\subseteq C_0\text{」主导}\ (\text{例 }a{=}50:69>62✓)\ }\ ✓✓\ \big(\textbf{＝唐先生"转折点在 }50\text{"的精确原因}✓✓\big)$$
$$\boxed{\textbf{(3) ★★闸门的精确重述（新 ✓✓）}:\ \mathrm{cov}_9(a)\ \ge\ 512-s\iff \boxed{9a-\mathrm{cov}_9(a)\ \le\ 9a+s-512}\ \iff\ \boxed{\text{「}C_0\text{ 的\textbf{强制重叠损失}\ \(\le\) \ \textbf{滑动余量}」}}\ ✓✓}$$
$$\qquad\text{（左＝}9a-\mathrm{cov}_9(a)=\min_{|S|=a}\big(9a-|N_9[S]|\big)\ \text{＝}a\ \text{点的\ \textbf{最小重叠损失}✓；右＝}\text{由 }s\ \text{与 }a\ \text{共同给出的余量}✓\big)}$$$
$$\qquad\Longrightarrow\ \text{等价形式 ✓}:\ \boxed{\ s\ \ge\ \mathrm{min\_excess}_9(a):=512-\mathrm{cov}_9(a)\ }\ ✓✓\ \big(\text{＝"9 维最小洞数"✓ ＝ C-435 §0(5) ✓}\big)$$
$$\boxed{\textbf{(4) ★致密度事实（新 ✓）}:\ \mathrm{cov}_9(m)=9m\iff m\le A(9,3)=\mathbf{40}\ ✓✓\ \big(\text{最小距离}\ge3\ \text{的集合无重叠 ⟹ 度数界在此\ \textbf{紧}✓}\big)}$$
$$\qquad\Longrightarrow\ m\ge41\ \Longrightarrow\ \mathrm{cov}_9(m)<9m\ \textbf{必有重叠损失}>0✓✓\ \big(\text{故闸门只在 }a\ge41\ \text{处才有"额外牙齿"✓}\big)$$
$$\boxed{\textbf{(5) ✗✗更正（本档必标）}:\ }s\le61\ \textbf{分支为空}✗\ \big(\text{因 }U\ \text{是 9-cover（C-435 §0(2)✓）}\Longrightarrow s\ge K(9,1)=62\ ✓✓\ \text{恒成立}\big)}$$$
$$\qquad\Longrightarrow\ \text{唐先生"若已有独立的 }s\le61\text{"——该前提\ \textbf{不存在}✗；}\ \text{故"把 }|C_0|\le50\ \text{切掉"}\ \textbf{不再需要}（空分支）✓；\ \textbf{真正剩余}:\ a\in[44,59]\ \text{区间内的 }\mathrm{min\_excess}_9\ \text{值 ⚠️}$$
$$\qquad\textbf{（但唐先生的方法论要点仍成立 ✓✓）}:\ \text{即 }|C_0|\le50\ \text{区域由容量切掉}\ ⟹\ \textbf{一般 NO-GO 只剩 }a\ge51\ \text{侧的 }\mathrm{cov}_9\ \text{精确形状}\ ⚠️$$

---

## §1 两条约束的核验（**✓✓**）

$$\textbf{（一）容量 ✓}:\ U^c\subseteq N_9(C_0)\Longrightarrow|U^c|=512-s\le|N_9(C_0)|\le9a\ \big(\text{开邻域度数界 ✓}\big) \Longrightarrow s\ge512-9a✓$$
$$\textbf{（二）}H\subseteq C_0\ ✓:\ |H|=119-s\le|C_0|=a\Longrightarrow s\ge119-a\ ✓\ \big(\text{此前只用于 }|A|\ge0✓，\textbf{从未与容量并列}✗\big)$$
$$\textbf{（三）有效下界 ✓}:\ s\ \ge\ \max\big(512-9a,\ 119-a,\ 62\big)\ ✓\ \text{—— 核验表（逐位 ✓）}:$$

| $a=\vert C_0\vert$ | $512-9a$ | $119-a$ | $\max(\cdot,62)$ | 主导 |
|---|---|---|---|---|
| 42 | 134 | 77 | **134** | 容量 |
| 44 | 116 | 75 | **116** | 容量 |
| 46 | 98 | 73 | **98** | 容量 |
| 48 | 80 | 71 | **80** | 容量 |
| 49 | 71 | **70** | **71** | 容量（临界） |
| 50 | 62 | **69** | **69** | **$H$-子集** |
| 51 | 53 | **68** | **68** | $H$-子集 |
| 56 | 8 | **63** | **63** | $H$-子集 |
| 57 | −1 | **62** | **62** | $H$-子集（＝已知下界 ✓） |

$$\Longrightarrow\ \text{交界 }a=49.125✓✓;\quad \textbf{故容量闸门的\ \textbf{有效作用域}是 }a\le49✓✓\ \text{（与唐先生"转折点在 50"一致 ✓）}$$

## §2 闸门重述与剩余问题（**✓✓**）

$$\textbf{精确形式 ✓}:\ \mathrm{min\_excess}_9(a):=512-\mathrm{cov}_9(a)✓;\qquad \text{闸门}:\ \boxed{s\ge\mathrm{min\_excess}_9(a)}\ ✓✓$$
$$\qquad\textbf{已知锚点 ✓}:\ \mathrm{min\_excess}_9(62)=0✓\ \big(K(9,1)=62\ \text{精确 ✓}\big);\ \mathrm{cov}_9(m)=9m\ (m\le40)\Longrightarrow\mathrm{min\_excess}_9(m)=512-9m\ (m\le40)✓$$
$$\qquad\Longrightarrow\ \text{对 }a\in[44,49]:\ \text{闸门给 }s\ge\max(512-9a,\ \mathrm{min\_excess}_9(a))✓;\ \text{因 }a\ge41\ \text{时}\ \mathrm{cov}_9(a)<9a \Longrightarrow \mathrm{min\_excess}_9(a)>512-9a✓✓\ \big(\text{容量界\textbf{不再是紧的}}✓\big)$$
$$\boxed{\textbf{★剩余问题（本档收窄 ✓✓）}:\ \text{求 }\mathrm{min\_excess}_9(a)\ \text{对 }a\in[44,59]\ \text{的值（或足够强的下界）};\ \text{若 }\exists a:\ \mathrm{min\_excess}_9(a)>119\Longrightarrow\boxed{\text{该 }a\ \text{不可行}}✓✓}$$
$$\qquad\text{（若 }a\in[44,59]\ \text{全被排除，则 }|C_0|\notin[44,59]\ \text{—— 但 }|C_0|+|C_1|=119\ \text{且 }|C_0|,|C_1|\ge44\ \text{迫使 }|C_0|\in[44,59]✓✓\ \Longrightarrow\ \textbf{矛盾}✓✓\big)}$$$
$$\qquad\Longrightarrow\ \textbf{这是一条\ \textbf{无需新机制}的完整 NO-GO 路线}✓✓\ \big(\text{只用 }U\ \text{cover}\Rightarrow s\ge62✓\ +\ \mathrm{min\_excess}_9\ \text{的值}\big)\ \text{—— 但依赖 9 维极值函数 ✗（文献/计算 ⚠️）}$$

## §3 状态与档案接口（**✓ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 参数化形式与表（§1）};\ \text{② 交界点 }49.125\ \text{（§0(2)）};\ \text{③ 闸门重述 min\_excess}_9✓;\ \text{④ 致密度事实（}m\le40\ \text{紧 ✓）};\ \text{⑤ }s\le61\ \text{为空 ✗✓}$$
$$\textbf{未确立 ⚠️}:\ \mathrm{min\_excess}_9(a)\ (a\in[44,59])\ \text{的值/强下界};\ \text{以及 }a\ge50\ \text{侧还需独立输入}✓$$
$$\textbf{档案接口 ✓}:\ \text{① MCOVER／OBREVERSE（Östergård–Blass 子空间＋LP ✓）＝本类极值函数的标准工具 ✓};\ \text{② DLP1A/1B（Delsarte LP／SDP ✓）给出 }K(9,1)\ \text{侧锚点 ✓};\ \text{③ C-435 §0(5) 的 }\mathrm{cov}_9\ \text{闸门与此处 }s\ge\mathrm{min\_excess}_9\ \text{为同一物}✓✓$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "交界点" "重叠损失" "滑动余量"
技术词 交界点    命中文件数=0    ::
技术词 重叠损失  命中文件数=1    :: ./E6-6-yiyi1-exponent-ledger-rebuild-and-reverse-implication-check.md
技术词 滑动余量  命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间／属线未定（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 交界点 | 0 | 0 | 0（本档自造标签 ✓） |
| 重叠损失 | 0（1 命中属 `E6-6-yiyi1-*` ⟹ **属线未定 ⟹ 不计** ✗） | 1 | 0（本档自造标签 ✓） |
| 滑动余量 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词**本线皆 0** ⟹ 自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 双约束核验＋表 ＋ §0(2)(3)(4)(5) 四结论 ＋ §2 收窄**（推导性 ✓）

## §5 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **$s\le61$ 空分支的更正**已在 §0(5) 显式标注 ✓✓（防误用 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）：本档只给交界点、重述与收窄；是否投入 $\mathrm{min\_excess}_9$ 由唐先生定 ✓
- **不声称** 119 已排除 ✗；**不声称** $\mathrm{min\_excess}_9$ 路线必成 ✗；不声称 P1 成立 ✗（V290）
