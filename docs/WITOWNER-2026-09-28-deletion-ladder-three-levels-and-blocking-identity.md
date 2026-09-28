# WITOWNER-2026-09-28 — **删点阶梯三级封死：${r}{=}0$（$\ge12$）／$r{=}1$（$\ge8$）／$r{=}2$（$\ge8$ ✓✓）；blocking identity 全量成立（780 对，反例 0 ✓✓）；owner 超图资产**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:57 令 ✓）**：删点塔 $r{=}1,2,3$ ＋ blocking identity 验证；**有限穷举＋局部搜索** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-479／C-478／C-477，非新案 ✓）**
`docs/WITBEST-2026-09-28-…`（**Best 验算／$r{=}1$ 唯一谱 ✓✓✓**）｜`docs/HANDOFF-2026-09-28-…`（**单页交接 ✓✓**）｜`docs/WITM44-2026-09-28-…`（**均值 3.814 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §5）
D0: 本档对象 ＝ **档案已有** $\frac12Q_{10}$／删点族／owner 集对象（重命名：否 ✗；新对象：**owner 超图首次入档** ✓）
D1: 1（**首次全量验证 blocking identity（780 对，反例 0）＋ 首次\ \textbf{封死 }$r{=}2$\ 支**（唯一危险模式 $(0,0,1,2,2,2)$ 与 $(0,0,1,1,2,2)$ 被 identity 杀死）＋ 首次给出\ \textbf{删点阶梯三级}（$r{=}0,1,2$）＋ 首次确认 $r{=}3$ 之兼容伙伴计数亦为 0** ✓）
**[RESEARCH]**

---

## §0 结论（**✓✓三级封死｜✓✓identity 全量成立｜⚠️延拓引理为关键**）

$$\textbf{设定 ✓}:\ I_{40}\ \text{＝Best 码（40 字，全\ \textbf{奇}重量 ✓）};\ \frac12Q_{10}\ \text{（同奇偶层，512 点，度 45 ✓）};\ I_{40-r}:=I_{40}\setminus D,\ |D|{=}r✓$$
$$\qquad d_{I_{40-r}}(x)=|O(x)\setminus D|,\quad O(x):=N_2(x)\cap I_{40}\ ✓\ \big(\text{owner 集 ✓}\big);\quad |O(x)|\in\{3,4,5\}✓\ \big(160/240/72✓\big)$$
$$\boxed{\textbf{(1) ✓✓✓blocking identity 全量成立（本档，780 对）}:\ }\forall D\ (|D|{=}2),\ \forall x\in D_1,\ \forall y\in E_2:\ \boxed{d(x,y){=}2\ \vee\ d(y,c_1){=}2\ \vee\ d(y,c_2){=}2}\ ✓✓$$
| 检验量 | 结果 |
|---|---|
| 存在"兼容 degree-2 点"之对数 | $\mathbf{0}\ /\ 780$ ✓✓ |
| 最大兼容计数 | $\mathbf{0}$ ✓✓ |
| $(\|D_1\|,\|E_2\|)$ 分布 | $\{(1,25){:}160,\ (2,23){:}160,\ (0,28){:}120,\ (0,24){:}340\}$ ✓ |
$$\qquad\Longrightarrow\ \text{唐先生 §6 之断言\ \textbf{完全成立}}✓✓\ \big(\text{＝owner 超图对 2-subset }D\ \text{之局部 blocking ✓ 唐先生 §10 之框架 ✓}\big)$$
$$\boxed{\textbf{(2) ✓✓✓r{=}2 支封死（}e_2\ge8\textbf{）（本档）}:\ }S\supseteq I_{38},\ |S|{=}44\Longrightarrow R{=}S\setminus I_{38},\ |R|{=}6;\ e_2(S)=\sum_{x\in R}d(x)+e_2(R)✓$$
$$\qquad\textbf{（危险模式唯有两种 ✓）}:\ \text{用两个 degree-0（＝被删码字 ✓）时，}\sum\le7\iff\ (0,0,1,2,2,2)\ (\sum{=}7)\ \text{或}\ (0,0,1,1,2,2)\ (\sum{=}6)✓$$
$$\qquad\text{两者皆需一个\ \textbf{degree-2 点与某个 degree-1 点及 }c_1,c_2\ \text{两两不相邻}\ ✗\ \text{——\ 由 §0(1)\ 不存在}✓✓\Longrightarrow\ \text{若取之则 }e_2(R)\ge1\Longrightarrow e_2(S)\ge8✓✓}$$
$$\qquad\text{}\ \text{其余模式}\ (0,0,2,2,2,2)\ \text{给}\sum{=}8✓;\ \text{不用 degree-0 点则}\ \sum\ge10✓\ \big((2,23)\ \text{支}:\ 1{+}1{+}2{\cdot}4{=}10✓\big)$$
$$\qquad\Longrightarrow\ \boxed{r{=}2\ \text{（Best 子码之 38-码）}\ \text{支}\ e_2\ge8\ \text{✓✓ 封死}}$$
$$\boxed{\textbf{(3) ✓✓删点阶梯（三级皆封）}:\ }$$
| $r$ | $|I|$ | 谱（同层 ✓） | 结论 |
|---|---|---|---|
| 0 | 40 | $\{3{:}160,4{:}240,5{:}72\}$ ✓ | $e_2\ge\mathbf{12}$ ✓✓ |
| 1 | 39 | $\{0{:}1,2{:}12,3{:}172,4{:}225,5{:}63\}$ ✓（唯一谱 ✓） | $e_2\ge\mathbf8$ ✓✓ |
| 2 | 38 | 4 种谱（如 $\{0{:}2,1{:}1,2{:}25,3{:}181,4{:}209,5{:}56\}$ ✓） | $e_2\ge\mathbf8$ ✓✓（本档 ✓） |
$$\boxed{\textbf{(4) ✓r{=}3（抽样 400 三元组）}:\ }\text{低度谱 20 种（如 }\{0{:}3,1{:}1,2{:}37\}{:}73✓\big);\ \text{"兼容伙伴}\ge2"\ \text{之情形数}=\mathbf0\ ✓✓;\ \text{局部搜索最小 }e_2=\mathbf{12}\ ✓$$
$$\qquad\Longrightarrow\ \text{同型 blocking 现象\ \textbf{延续}}✓;\ \text{唯}\ r{=}3\ \text{之\ \textbf{严格} 封死须更多情形分析 ✗（本档未做完 ⚠️）}$$
$$\boxed{\textbf{(5) ✓✓新资产：owner 超图（唐先生 §9 之框架 ✓）}:\ }\mathcal H_{\rm Best}:=\{O(x):x\in \frac12Q_{10}\setminus I_{40}\}\ ✓\ \text{＝40 顶点上 472 条超边（大小 3/4/5 ✓）}$$
$$\qquad d_{I_{40}\setminus D}(x)=|O(x)\setminus D|\ ✓\Longrightarrow\ \text{低度点}\iff O(x)\ \text{与 }D\ \text{高交 ✓✓}\ \big(\text{把 }Q_{10}\ \text{几何压成有限超图 ✓}\big)$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生 §1（同奇偶层 512／472／度 45／距离分布 }(1,0,0,0,22,0,12,0,5,\dots)\ ✓\big);\ \S2\ \text{（外部谱 }\min{=}3✓,\ \ge12✓\big);\ \S4\ \text{（}r{=}1\ \text{谱与 }\ge8✓✓\big);\ \S5\ \text{（}r{=}2\ \text{谱 }\{0{:}2,1{:}1,2{:}25,3{:}181,4{:}209,5{:}56\}\ ✓\big);\ \S6\ \text{（blocking ✓✓\ 本档全量验 ✓）};\ \S8\text{–}\S10\ \text{（owner 集／超图框架 ✓✓）}$$
$$\textbf{✓（本档补强）}:\ \text{§5 之"唯一危险模式 }(1,2,2,2)"\ \text{应扩为两种（含 }(1,1,2,2)\ ✓\ \text{——}\ 160\ \text{对含\ \textbf{两个} degree-1 点 ✓）};\ \text{两者皆被 §0(1) 杀死 ✓✓}$$
$$\textbf{⚠️}:\ \text{唐先生 §1 之核心\ \textbf{警告正确}}✓✓:\ \text{Litsyn–Vardy 证的是 }(10,40,4)\ \text{之唯一性 ✗\ 非"任意 }(10,39,4)\ \text{可延拓"}\ ✓\ \text{——\ 本档 }\S0(2)\ \text{之封死仅覆盖\ \textbf{Best 子码}\ ✓}$$
$$\textbf{✓}:\ \S11\ \text{之建议（停在 38 ✓，转 P1-A 延拓引理 ✓）\ \textbf{采纳} ✓✓（}\S2\ \text{并给理由 ✓）}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已封 ✓✓}:\ \text{Branch A（}\alpha{=}40\big):\ e_2\ge12✓;\quad r{=}1:\ e_2\ge8✓;\quad r{=}2:\ e_2\ge8✓\ \big(\text{本档 ✓}\big)$$
$$\textbf{OPEN ⚠️}:\ \text{① }r\ge3\ \text{之严格封死（现象延续 ✓ 但情形分析未完 ✗）};\ \text{② }\boxed{\text{延拓引理（P1-A ✓）}};\ \text{③ 不可延拓之 39/38-码 ✗}$$
$$\boxed{\textbf{（下一轮唯一靶 ✓✓，照唐先生 §11–§12）}:\ }\boxed{\text{Extension Lemma}:\ \alpha(S)\ge38\Longrightarrow S\ \text{之最大 }(10,4)\text{-码可延拓至 Best 40-code}}\ ✓$$
$$\qquad\Longrightarrow\ \text{若成立，则}\ \S0(3)\ \text{之三级计算\ \textbf{立刻升级为正式证明}}✓✓:\ \alpha(S)\ge38\Longrightarrow e_2(S)\ge8✓;\ \text{余 }\alpha(S)\le37\ \text{再另杀 ✓}$$
$$\qquad\textbf{（诚实评估 ⚠️）}:\ \text{该引理\ \textbf{不}由 Best 唯一性蕴含 ✗（唯一性只覆盖 40-码 ✓）};\ \text{须独立论证 ✓（LP／距离分布先压 ⟹ 优于 SAT ✓）};\ \text{且其\ \textbf{难度未知} ⚠️（可能重新触及"真子案＝原问题"之经验 ✓）}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "删点阶梯" "owner超图" "延拓引理"
技术词 删点阶梯 命中文件数=0    ::
技术词 owner超图 命中文件数=0    ::
技术词 延拓引理 命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 删点阶梯 | 0 | 0 | ✓（自造标签 ✓） |
| owner超图 | 0 | 0 | ✓（自造标签 ✓） |
| 延拓引理 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **有限穷举＋局部搜索** ✓（780 对全量 ✓；$r{=}3$ 抽样 400 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处外部引用**（Best 唯一性未离线核 ✓ C-479 ✓）＋ **一处覆盖范围限定**（封死仅 Best 子码 ✗✓）已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $m(44)\ge8$ ✓✗（OPEN ⚠️）；**不声称** 延拓引理成立/不成立 ✗（V290）
