# AUDIT-2026-09-28aa — **Kéri 档方法章：确认下界家族（Zhang 系列），但\ \textbf{不含 BÖW 公式}**

> **性质**：**审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:05 ✓
> **唐先生令**：目标固定为 **BÖW 2004 之专门 general-$R{=}1$ bound**；从引文反提 ✓

**已查地图**：接续 `AUDIT-z`（逐步出处锁定）／`AUDIT-y`（$103$）✓

D0: 本档对象 ＝ **档案已有**（文献／方法——无新数学对象 ✓）
D1: 0（产出＝**方法章取证 ＋ 一处否证 ＋ 目标固定** ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{① Kéri 档 2.4.5 节（"Alsó korlátokat tárgyaló publikációk"）确认下界家族}\ ✓}$$
$$\boxed{\text{② ★ 但\ \textbf{该档不含 BÖW 之 general }R{=}1\ \text{公式}\ ✗\ \text{（否证）}}$$
$$\boxed{\text{③ 目标固定}:\ \textbf{BÖW 2004 general }R{=}1\text{-bound};\ \text{取法 ＝ 2005--2011 引文反提}}$$

## §1 方法章逐字（**匈牙利文 ✓**）

$$\textbf{逐字}:\ "\text{2.4.5. Alsó korlátokat tárgyaló publikációk}\ldots\ \textbf{Zhang}\ \text{két, 1991-ben, ill. 1992-ben megjelent cikkében }([67,\ 71])\ldots\ \text{a szerzők }\textbf{lineáris egyenlőtlenség-rendszerek}\ \text{vizsgálata alapján határoznak meg új alsó korlátokat}."$$
$$\qquad \text{（译：Zhang 之 1991／1992 两文（}[67,71]\text{）基于\ \textbf{线性不等式组} 之研究确定新下界）}$$
$$\textbf{逐字}:\ "\text{Habsieger }[82](1994),[91](1996),[100](1997),\ \text{Habsieger és Plagne }[116](2000),\ \text{valamint Haas }[117](2000)\ \text{cikke, valamint Blass és Litsyn }[103,104](1998)"$$
$$\textbf{逐字（★对 Zhang 之评价）}:\ "\text{Később azonban az e cikkekben megadott konkrét alsó korlátok helyett mások }\textbf{kifinomultabb módszerekkel}\ldots\ \text{jobb alsó korlátokat bizonyítottak, egy kivétellel}"$$

## §2 ★ 否证：档内**无** BÖW 公式（**诚实 ✓**）

$$\text{档内关键词命中}:\ \text{Zhang }9,\ \text{Haas }11,\ \text{Habsieger }7,\ \text{Weakley }11,\ \text{Blass }8,\ \text{Litsyn }15,\ \text{Honkala }21,\ \text{van Wee }12;\quad \textbf{"excess" }0,\ \textbf{"linearis" }0$$
$$\text{全部 "general" 命中（}3\ \text{处）皆在\ \textbf{参考文献}，非正文公式} ✗$$
$$\therefore\ \boxed{\text{Kéri 档（191 页，匈牙利文综述/学位论文）}\ \textbf{不给 BÖW 之具体不等式}}\ ✗$$

## §3 ★ Zhang 系列（**新确认之细节 ✓**）

$$[67]\ \textbf{Z. Zhang}, "\text{Linear inequalities for covering codes: Part I --- }\textbf{Pair covering inequalities}",\ \text{IEEE TIT 37 (1991), 573--582}\ ✓$$
$$[71]\ \textbf{Z. Zhang \& C. Lo}, "\text{Linear inequalities for covering codes: }\textbf{Part II --- Triple covering inequalities}",\ \text{IEEE TIT 38 (1992)}\ ✓$$
$$[69]\ \text{Lo \& Zhang (1992) 手稿（未刊）}:\ \text{业界\ \textbf{不}接受其下界为已证 —— 逐字"a szakma nem fogadja el bizonyítottnak"}\ ⚠️$$
$$\therefore\ \text{线性不等式族之谱系}:\ \textbf{Zhang(1991) Pair}\to\textbf{Zhang--Lo(1992) Triple}\to\text{Habsieger(1994/96/97)}\to\text{H-P(2000)}\to\text{BÖW(2004)}\ ✓$$

## §4 目标与取法（**照唐先生 ✓**）

$$\boxed{\text{固定目标}:\ \textbf{BÖW 2004 \S general }R{=}1\ \text{inequality}\ \text{（可能为分段/取整多参数 bound，非 }F(n)\text{）}}$$
$$\text{取法（按优先级）}:\ \textbf{① 2005--2011 之 covering-code／domination 论文与学位论文，逐篇反提 BÖW 之 theorem statement};\ \text{②}\ \texttt{pypdf}\ \text{路数（已通）处理其 PDF};\ \text{③ 引文网络向 BÖW 之后（cited-by）} ⚠️$$
$$\text{注意}:\ \text{Wu--Chen 2024（arXiv:2203.16901）仅处理 }n\equiv0 \bmod 6 \Longrightarrow \textbf{n{=}10 不在其内} \Longrightarrow 107\ \text{仍是\ \textbf{小维度专门值}}\ ✓$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "方法章证据" "Zhang系列" "反提未成"
技术词 方法章证据   命中文件数=0    ::
技术词 Zhang系列   命中文件数=0    ::
技术词 反提未成    命中文件数=0    ::
```

## §6 边界（硬 ✓）

- 本地抽文（`pypdf`）＋ 逐字引证（匈牙利文）＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** BÖW 公式 ✗（遵令 ✓）；**不主张** $107\to108$ 可行 ✗（V290）
