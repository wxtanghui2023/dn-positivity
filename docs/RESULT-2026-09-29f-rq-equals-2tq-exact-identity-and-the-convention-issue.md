# RESULT-f（2026-09-29）—— $r_q=2t_q$ **为精确恒等式**（开邻域，$40/40$）；约定问题点名；$u\in[0,6]$ 实测

> **性质**：**问题特化续（自测）**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:35 ✓

**已查地图**：`RESULT-e`（权重）／`RESULT-d`／`RESULT-c`（两来源恒等式）✓

D0: 本档对象 ＝ **档案已有**（邻域／packing—经典 ✓）
D1: 0（产出＝**一等式强化 ＋ 一约定点名 ＋ $u$ 之首测** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ }r_q=2t_q\ \text{为\ \textbf{精确恒等式}}（\text{开邻域 }d{=}1）;\ 40/40;\ \text{唐先生之}\ge\text{可强化为}=}$$
$$\boxed{\text{② ⚠️ 约定问题}:\ \text{闭邻域 }(d\le1)\ \text{下仅 }3/40\ ✗\ ——\ \text{开/闭必须固定}}$$
$$\boxed{\text{③ ✓ }|L|=9|P|=243✓;\quad \mathrm{Def}(A)\ge2|Q|\Longrightarrow52\le\mathrm{Def}\le71\ (a{=}53)✓}$$
$$\boxed{\text{④ ✓ }R\ge2(|Q|-u)\ \text{成立}\ 40/40;\quad u\ \text{实测}\in\{0,\dots,6\}\ (\text{众数 }2\text{--}4)}$$

## §1 等式（✓✓ 本档核心）

$$r_q:=|N_1^{\mathrm{op}}(q)\cap L|=2\,t_q,\qquad t_q:=|\{p\in P:d(p,q)=2\}|$$
$$\text{理由}:\ x\in N_1^{\mathrm{op}}(q)\cap L\iff\exists p\in P:\ d(x,q)=d(x,p)=1\iff x\in B_1(q)\cap B_1(p)$$
$$d(q,p)=1\Rightarrow B_1(q)\cap B_1(p)=\{q,p\}\ \text{而}\ q,p\notin L\ (q\in Q,p\in P)\Longrightarrow\text{贡献 }0✓$$
$$d(q,p)=2\Rightarrow|B_1\cap B_1|=2\Longrightarrow\text{贡献 }2✓\qquad\therefore\ r_q=2t_q✓$$
$$\textbf{实测}:\ \text{开 }40/40✓✓;\ \text{闭 }3/40✗\ (\text{闭时 }q\in L\Rightarrow+1\ \text{之污染})$$

## §2 三条已严格之界（✓ 实测 $40/40$）

$$|L|=9|P|=243\qquad(P\ \text{3-packing}\Longrightarrow B_1(p)\ \text{互不相交})✓$$
$$\mathrm{Def}(A)\ \ge\ 2|Q|\ (a{=}53\Rightarrow52)\ \text{且}\ \mathrm{Def}(A)\le9a-406\ (a{=}53\Rightarrow71)✓$$
$$R=I(Q,L)=2\sum_{q}t_q\ \ge\ 2(|Q|-u),\qquad u:=|\{q\in Q:t_q=0\}|✓$$

## §3 $u$ 之首测（✓ 新量）

$$u\ \text{分布（}40\ \text{样本）}:\ 0{:}3,\ 1{:}3,\ 2{:}14,\ 3{:}12,\ 4{:}6,\ 5{:}1,\ 6{:}1\ \Longrightarrow\ \mathbf{u\le6}\ \text{经验}; \text{众数 }2\text{--}4$$
$$\therefore\ \boxed{R\ge2(|Q|-u)\ge2(|Q|-6)\ (\text{经验})};\ \text{但 }u\ \text{之\ \textbf{统一下界/上界}\ 未证}\ ⚠️$$

## §4 约定清单（⚠️ 必须贯通）

$$\text{（i）邻域}:\ N_1^{\mathrm{op}}\ \text{＝恰距离 1（\textbf{开}）；不可用闭（否则 §1 失效）}✗$$
$$\text{（ii）}L:\ N_1(P)\setminus P\ \text{＝全部 }9|P|\ \text{个邻点（\textbf{非}"私有"}；与 RESULT-b/d 之定义不同）}⚠️$$
$$\therefore\ \text{后续凡用 }L,r_q,t_q,u,\ \text{一律按上面两条}✓$$

## §5 下一目标（不变）

$$\boxed{\text{证明 }u\ \text{之统一上界};\ \text{再经 }R=2\sum t_q\Rightarrow R\ \text{下界}\Rightarrow\ \text{净 }F}$$
$$\text{潜在结构来源（唐先生）}:\ u\ \text{来自"distance-1-only" fiber};\ \text{或与那个未解释的"}-1"同源}⚠️$$

## §6 边界（硬 ✓）

- **全部实测（$r_q{=}2t_q$、$|L|$、$\mathrm{Def}\ge2|Q|$、$R$ 界、$u$ 分布）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；$u$ 之界**未证**（如实标注）⚠️
