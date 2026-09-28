# WITR2CLOSE-2026-09-28 — **$r{=}2$ 支严格封闭（$\alpha(G_R){=}2$ 全 780 对 ＋ \textbf{结构证明} ✓✓）；$r{=}3$ 诚实状态：\textbf{未封} ⚠️（新障碍：额外零点 160/9880、度 $\le2$ 集可分离 10 点）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 14:00 令 ✓）**：$r{=}2$ 精确证书 ＋ $r{=}3$ 状态；**有限穷举＋局部搜索** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-480／C-479／C-478，非新案 ✓）**
`docs/WITOWNER-2026-09-28-…`（**blocking identity／三级阶梯 ✓✓✓**）｜`docs/WITBEST-2026-09-28-…`（**Best 验算／$\min d_I{=}3$ ✓✓✓**）｜`docs/HANDOFF-2026-09-28-…`（**单页交接 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $\frac12Q_{10}$／$G_R$／$L_R$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $r{=}2$ 之\ \textbf{精确证书}（全 780 对 $\alpha(G_R){=}2$；$|L_R|\le4$；度多重集）＋ 首次给出 $\alpha(G_R){=}2$ 之\ \textbf{结构性证明}（由 $\min d_I{=}3$ 推出，非枚举）＋ 首次指出 $r{=}3$ 之两项\ \textbf{新障碍}（额外零点 160／度 $\le2$ 集可分离至 10 点）** ✓）
**[RESEARCH]**

---

## §0 结论（**✓✓$r{=}2$ 严格封闭｜⚠️$r{=}3$ 未封**）

$$\textbf{设定 ✓}:\ I_{40}\ \text{＝Best 码};\ D{=}\{a,b\};\ S{=}I_{40}\setminus D;\ L_R:=\{x\notin I_{40}:d_S(x)\le1\};\ G_R:=(\text{冲突图，边}\iff d(x,y){=}2)✓$$
$$\qquad\textbf{✗笔误更正 ✓}:\ \text{唐先生写 }d_S(x){=}|\{c\in S:d(x,c){=}\mathbf1\}|\ ✗\ \text{——\ 同奇偶层内距离皆\ \textbf{偶} ⟹ 恒为 0 ✗；应为 }d(x,c){=}\mathbf2✓✓$$
$$\boxed{\textbf{(1) ✓✓精确证书（全 780 对，本档）}:\ }$$
| 量 | 分布 |
|---|---|
| $\|L_R\|$ | $\{2{:}460,\ 3{:}160,\ 4{:}160\}$ ✓（$\le4$ ✓✓） |
| $L_R$ 之度多重集 | $\{(0,0){:}460,\ (0,0,1){:}160,\ (0,0,1,1){:}160\}$ ✓ |
| $M_R{=}\alpha(G_R)$ | $\mathbf{\{2{:}780\}}$ ✓✓✓ |
| $d(a,b)$ | $\{4{:}440,\ 6{:}240,\ 8{:}100\}$ ✓ |
$$\qquad\Longrightarrow\ \boxed{\alpha(G_R)=\mathbf2\ \text{对全部 780 个 }R\ \text{成立}}\ ✓✓\ \big(\text{远低于击穿所需之 }6\ ✓✓\big)$$
$$\boxed{\textbf{(2) ✓✓✓结构性证明（本档，非枚举）}:\ }\text{由 C-479 之\ \textbf{关键事实}：}\forall x\notin I_{40}:\ d_{I_{40}}(x)\ge3✓✓$$
$$\qquad\text{删 }D{=}\{a,b\}\Longrightarrow d_S(x)=d_{I_{40}}(x)-|O(x)\cap D|\ \ge\ 3-2=\mathbf1✓\ \big(\text{故除 }a,b\ \text{外无 degree-0 点 ✓，与 \S0(1) 之度多重集一致 ✓}\big)$$
$$\qquad\textbf{（degree-1 点 ∎）}:\ d_S(x){=}1\Longrightarrow|O(x)\cap D|=d_{I_{40}}(x)-1\ \ge2✓\ \text{而}\ \le|D|{=}2\Longrightarrow d_{I_{40}}(x){=}3\ \wedge\ D\subseteq O(x)✓$$
$$\qquad\Longrightarrow d(x,a)=d(x,b)=\mathbf2\Longrightarrow\boxed{x\ \text{于 }G_R\ \text{中同时邻接 }a\ \text{与 }b}\ ✓✓$$
$$\qquad\text{又 }d(a,b)\in\{4,6,8\}\Longrightarrow a,b\ \text{于 }G_R\ \text{中\ \textbf{不}相邻}✓\Longrightarrow\boxed{\alpha(G_R){=}2,\ \text{唯一最大独立集}=\{a,b\}}\ ✓✓$$
$$\qquad\textbf{（副产品 ✓）}:\ \text{degree-1 点只在 }d(a,b){=}4\ \text{时出现 ✓（须 }D\subseteq O(x)\ \text{且}\ |O(x)|{=}3✓\big)\ \text{——\ 与 \S0(1) 之分类完全一致 ✓}$$
$$\boxed{\textbf{(3) ✓✓r{=}2 之严格封闭（}e_2\ge8\textbf{）}:\ }\text{要 }e_2(S\cup X)\le7\ \big(|X|{=}6\big)\ \text{须}\ \sum_{x\in X}d_S(x)+e_2(X)\le7✓\ \text{（以 }a,b\ \text{为仅有的 degree-0 点 ✓）}$$
$$\qquad\text{度型枚举（用 }a,b\big):\ (1,1,1,1){=}4✓,\ (1,1,1,2){=}5✓,\ (1,1,2,2){=}6✓,\ (1,2,2,2){=}7✓,\ (2,2,2,2){=}8✗$$
$$\qquad (1,1,1,1)\ \text{与}\ (1,1,1,2)\ \text{需}\ \ge3\ \text{个 degree-1 点，而}\ |D_1|\le2✓\ \big(\S0(1)\big)\Longrightarrow\ \textbf{不可能}\ ✗✓$$
$$\qquad (1,1,2,2)\ \text{与}\ (1,2,2,2)\ \text{需一个 degree-2 点与某 degree-1 点及 }a,b\ \text{两两不相邻 ⟹ 与 C-480 之 blocking identity 冲突}✗$$
$$\qquad\text{不用 }a,b:\ 6\ \text{点皆度}\ \ge1\ \text{且至多 2 个度-1}\Longrightarrow\sum\ \ge\ 1{+}1{+}2\cdot4=10>7✓$$
$$\qquad\Longrightarrow\ \boxed{r{=}2\ \text{支}\ e_2\ge8\ \text{（严格封闭 ✓✓，结构性证明非枚举 ✓✓）}}\ \big(\text{＝唐先生 §"严格封"\ ✓✓}\big)$$
$$\boxed{\textbf{(4) ⚠️⚠️r{=}3 之诚实状态：\textbf{未封}（本档新障碍）}:\ }$$
$$\qquad\textbf{(a) ✓blocking 延续}:\ \text{全 9880 三元组中，degree-1 点之"可用 degree-2 伙伴"最大计数}=\mathbf0✓✓$$
$$\qquad\textbf{(b) ✗新障碍一}:\ \text{外部 degree-0 点数分布}=\{0{:}9720,\ \mathbf1{:}160\}\ ✗\ \text{——\ \textbf{160 个三元组\ \textbf{有额外零点}}（除 }a,b,c\ \text{外 ✓）}✗$$
$$\qquad\textbf{(c) ✗新障碍二}:\ \text{度}\le2\ \text{集之贪心最大分离度可达 }\mathbf{10}\ ✗\ \big(\text{度}\le1\ \text{集仅达 3 ✓ 但其大小可达 8 ✓}\big)$$
$$\qquad\Longrightarrow\ \text{"纯低度点两两拉开"之逃逸\ \textbf{未被排除} ✗};\ \text{本档局部搜索（7-子集）最小 }e_2=\mathbf{12}✓\ \text{（提示 P1 存活）但\ \textbf{非证明} ✗}$$
$$\qquad\Longrightarrow\ \boxed{r{=}3\ \text{支\ \textbf{OPEN}}\ ⚠️\ ——\ \text{且此处正是 P1 可能真正断裂的格子}\ ✗}$$

---

## §1 删点阶梯状态（**照唐先生之表格 ＋ 本档升级 ✓✓**）

| $r$ | 结论 | 性质 |
|---|---|---|
| 0 | $e_2\ge12$ | **严格封 ✓✓** |
| 1 | $e_2\ge8$ | **严格封 ✓✓** |
| 2 | $e_2\ge8$ | **严格封 ✓✓（本档：结构证明 ＋ 全 780 对证书 ✓✓）** |
| 3 | 局部搜索 $\ge12$；blocking $=0$ ✓ | **未封 ⚠️（额外零点 160／度 $\le2$ 集可分离 10 ✗）** |

$$\textbf{✓✓}:\ \text{唐先生 §"危险度型唯二"}（(0,0,1,2,2,2)、(0,0,1,1,2,2) ✓）\ \text{\textbf{完全正确}}✓✓;\ \text{其"}\min d_I{=}3\ 之关键作用"\ ✓✓\ \text{本档据此给出\ \textbf{结构证明}}✓✓$$
$$\textbf{✓}:\ \text{唐先生 §"不要马上打一般 }r\ge3\text{"}\ ✓✓\ \text{采纳 ✓};\ \text{其 }\Sigma_7\le7\ \text{之 profile 枚举方向\ \textbf{正确} ✓✓（本档 \S0(4) 之 (c) 显示须含度-2 点之 profile 需逐一处理 ✗）}$$

## §2 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（唐先生之两条命题 ✓ 采纳）}:\ \textbf{Lemma E1}:\ |S|{=}39,\ d_{\min}\ge4\Longrightarrow S\ \text{可延拓为 }(10,40,4)✓;\ \textbf{Lemma E2}（较弱 ✓）:\ \text{仅须"可能产生 }e_2\le7\ \text{之 39-码"可延拓 ✓✓}$$
$$\qquad\Longrightarrow\ \text{（本档补充 ✓）}:\ \text{逻辑区分\ \textbf{必须保持} ✓✓}:\ \text{Best}\ (10,40,4)\ \text{唯一}\ \not\Rightarrow\ \text{每个 39-码可延拓 ✓（唐先生 ✓✓）};\ \text{故 }\S0(3)\ \text{之封闭\ \textbf{仅覆盖 Best 子码} ✗}$$
$$\qquad\textbf{（两条并行 ✓）}:\ \text{① }r{=}3\ \text{之 profile 引理（须处理额外零点 160 与度}\le2\ \text{集之分离度 10 ✗）};\ \text{② Lemma E1/E2（}\alpha(S)\ge38\ \text{之延拓 ✓）}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "严格封闭" "警示格" "低度分离度"
技术词 严格封闭   命中文件数=1    :: ./p49-phase-diagram-summary.md
技术词 警示格     命中文件数=0    ::
技术词 低度分离度 命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 严格封闭 | 0 | **1**（`p49-*` 属**空间 A（RH 线）** ⟹ **空间 A 同名，不计** ✗） | ✓（本线新增 ✓） |
| 警示格 | 0 | 0 | ✓（自造标签 ✓） |
| 低度分离度 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **有限穷举＋局部搜索** ✓（780 对全量 ✓；9880 三元组全量 ✓；600 抽样之分离度 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处笔误更正**（$d_S$ 之距离 1→2 ✗✓）＋ **一处严格化**（$\alpha(G_R){=}2$ 之结构证明 ✓✓）＋ **一处新障碍**（$r{=}3$ 未封 ✗）已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $m(44)\ge8$ ✓✗（OPEN ⚠️）；**不声称** $r{=}3$ 已封/已破 ✗（V290）
