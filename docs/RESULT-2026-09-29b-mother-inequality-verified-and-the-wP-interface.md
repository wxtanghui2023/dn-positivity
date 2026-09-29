# RESULT-b（2026-09-29）—— **母式 $\mathrm{Def}\ge2\sum m(c)$ 核实 ✓✓；下一对象 $w_P$ 之接口确立（含首个数据）**

> **性质**：**问题特化续**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 18:55 ✓

**已查地图**：`RESULT-2026-09-29`（$[47,59]$ 勘误后）／`AUDIT-29ze`／`CALIBRATE-n6` ✓

D0: 本档对象 ＝ **档案已有**（packing／$B_2$ 多重度—经典 ✓）
D1: 0（产出＝**母式核实 ＋ 接口 ＋ 首个数据** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 勘误确认}:\ a,b\in[\mathbf{47},\mathbf{59}]\ (\text{15 例}\to13\text{ 例};\ \text{仅排 }a{=}46,60)\ ✓\ \text{已落档}}$$
$$\boxed{\text{② 母式（更干净之证明）}:\ \mathrm{Def}(A)\ \ge\ 2\sum_{c\in A\setminus P}m(c),\ m(c)=|P\cap B_2(c)|\ ✓✓\ (\text{实测 }40/40)}$$
$$\boxed{\text{③ 我方旧引理 ＝ 其特例}:\ m(c)\ge1\Longrightarrow\mathrm{Def}\ge2(a-|P|)\ge2(a-40)\ ✓}$$
$$\boxed{\text{④ 斜率问题}:\ \text{母式斜率}\ 2\sum m\ \text{vs 所需}\ 9a-406\ (\text{斜率 }9)};\ \text{差 7 倍}\ ⚠️}$$
$$\boxed{\text{⑤ 首个数据}:\ \text{极大 packing：}w_P(x)\ge1\ \forall x\ (\text{实测}\ ✓);\ \text{且低重区\ \textbf{确实存在}\ (w{=}1\ \text{有 }32\ \text{点})⚠️}$$

## §1 母式之干净证明（✓ 逐行）

$$|N_1(A)|\le|N_1(P)|+\sum_{c\in A\setminus P}\bigl(10-|B(c)\cap N_1(P)|\bigr)$$
$$P\ \text{packing}\Longrightarrow B(p)\ \text{互不相交}\Longrightarrow|B(c)\cap N_1(P)|=\sum_{p\in P}|B(c)\cap B(p)|=2m(c)✓$$
$$\therefore\ |N_1(A)|\le10|P|+10(a-|P|)-2\sum m(c)=10a-2\sum m(c)$$
$$\therefore\ \boxed{\mathrm{Def}(A)=10a-|N_1(A)|\ \ge\ 2\sum_{c\in A\setminus P}m(c)}\ ✓✓$$
$$\textbf{注}:\ \text{唐先生之"逐个加回"论证计数的是}\ \sum\tbinom{\mu}2\ \text{型增量；}\ \text{上式为\ \textbf{精确}之}|\cdot|\ \text{论证，二者同结论}$$

## §2 数值核实（✓）

$$\textbf{① 母式}:\ 40/40\ \text{样本成立（真 62-码之 }42\text{--}58\text{-子集，贪心 packing}）✓✓$$
$$\textbf{② 三常数}:\ |B_2(p)|_{Q_9}=1+9+\tbinom92=46✓;\quad \sum_xw_P=40\cdot46=\mathbf{1840}✓;\quad \bar w=\tfrac{1840}{512}=3.594✓$$
$$\textbf{③ 极大性}:\ w_P(x)\ge1\ \forall x\ ✓\ (\text{实测 }w{=}0\ \text{点数}=0)$$

## §3 下一对象与首个数据（⚠️）

$$w_P(x):=|P\cap B_2(x)|;\qquad \sum_xw_P(x)=1840\ (\text{平均 }3.59)$$
$$\textbf{危险（唐先生已警告）}:\ \text{不可用均值}:\ \sum_{c\in A\setminus P}w_P(c)\ \ge\ 3.59(a-40)\ ✗\ (\text{额外中心可偏向低重区})$$
$$\textbf{首个经验数据（贪心极大 packing，}|P|{=}32）：w\ \text{分布}=1{:}32,\ 2{:}256,\ 4{:}192,\ 5{:}32$$
$$\therefore\ \boxed{\text{低重区}\ L_1\ \textbf{确实非空}（32 点）\Longrightarrow\ \text{集中风险真实}\ ⚠️}$$

## §4 下一目标（唯一正确形式）

$$\boxed{\text{求}\ L_t(P)=|\{x:w_P(x)\le t\}|\ \text{之\ \textbf{结构容量界}（含极大性 }w\ge1）}$$
$$\text{若}\ \sum_{c\in A\setminus P}m(c)\ \text{有真下界}\ \Longrightarrow\ \mathrm{Def}\ \text{斜率提升}\ \Longrightarrow\ \text{可逼近 }9a-406✓$$

## §5 边界（硬 ✓）

- **证明为解析（$|N_1|$ 论证）＋ 实测（$40/40$ 母式、常数、$w$ 分布）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达 ✗（V290）；本档为**接口确立 ＋ 首数据** ✓
