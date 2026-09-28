# AUDIT-2026-09-28p — **119 certificate 冻结核 ＋ $107$ 下界来源拆解**

> **性质**：**审计/路线**——**不占 C 号** ✓；**不作方向性决策** ✗（唐先生已令冻结 ✓）；空间 B ✓
> **时间**：2026-09-28 21:17 ✓
> **唐先生令**：**立即冻结 119 certificate**；把 $107$ 来源彻底拆开；**不预设数字** ✓

**已查地图**：接续 `AUDIT-o`（真值定位）／C-427／C-541 ✓ ｜ Tavily 432 ⟹ Firecrawl ✓

D0: 本档对象 ＝ **档案已有**（$K_2(10,1)$／下界来源——无新数学对象 ✓）
D1: 0（产出＝**冻结核 ＋ 下界来源定位 ＋ 两端"陈旧度"实测** ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{① 119 certificate\ \textbf{冻结}（照令）};\quad \text{② }107\ \text{源自\ \textbf{BÖW 2004}\ 且\ \textbf{自 2004 年未再改进}};\quad \text{③ 两端皆\ \textbf{陈旧}}\ ✓}$$
$$\boxed{\text{④ 新目标（对称）}:\ \text{improve either }107{\to}108\ \text{or}\ 120{\to}119}$$

## §1 目标重定义（**照唐先生 ✓**）

$$\textbf{旧（已废）}:\ \text{研究 }K_2(10,1)\ge119 \Longrightarrow \text{预设了数字} ✗$$
$$\boxed{\textbf{新}:\ \text{Target}＝\text{improve either }107{\to}108\quad\text{or}\quad120{\to}119\ (\text{对称，至两端碰撞})}\ ✓$$
$$\text{另合法目标（悬赏 PARTIAL 认可 ✓）}:\ \text{具名受限族（线性／给定自同构群）之\ \textbf{精确最小值} ＋ 穷举证}\ ✓$$

## §2 $107$ 来源拆解（**本档核心 ✓**）

$$\textbf{源}:\ \text{R. Bertolo, P. R. J. Östergård, W. D. Weakley,}\ "\text{An updated table of binary/ternary mixed covering codes}",\ \textbf{J. Combin. Designs 12 (2004), 157--176}\ ✓$$
$$\qquad \text{（DOI }10.1002/jcd.20008\text{；OEIS A000983 之 }\%D\ \text{引条目;Kéri 表之基表）}$$
$$\textbf{机 制（据文献谱系）}:\ \text{mixed covering codes 表} \Leftarrow \text{excess 方法（Johnson／van Wee 修正下界）} ＋ \text{mixed 关系（}+ \text{deletion/construction}）＋ \text{计算机搜索}$$

### ★★ 关键负面证据：$107$ **自 2004 年起未再改进**

$$\text{Kéri\ \textbf{变更日志}（2004.12.20 起之"improvements and corrections"）逐字检索}:\ \text{含 }K(19,2),K(27,1)\ \text{等大量二元下界改进}\ \Longrightarrow\ \textbf{无一条涉及 }K(10,1) ⚠️$$
$$\therefore\ \boxed{107\ \text{自 2004 年起\ \textbf{稳定}\ (\approx\mathbf{22}\ \text{年})};\quad 120\ \text{自 Östergård 1991 起\ \textbf{稳定}\ (\approx\mathbf{35}\ \text{年})}}$$
$$\therefore\ \boxed{\text{区间 }[107,120]\ \text{两端皆\ \textbf{陈旧}} \Longrightarrow \text{问题\ \textbf{确实卡在文献前沿}，非"无人算过"}}\ ✓$$

## §3 上界侧（$120$）之具体状态

$$\text{Östergård 1991：60-word \textbf{mixed} covering code}\ \Longrightarrow\ K(10,1)\le120\ ✓$$
$$\text{Kamenetsky 之显式构造文件（}\textbf{2020-07-27}\text{）}:a(10)\le120,\ \text{给出全部 }120\ \text{个 codeword};\ \textbf{无 }119/118\ ✓\ \text{（OEIS 链接）}$$
$$\boxed{\text{未见任何公开来源\ \textbf{宣称} }120\ \text{不能降到 }119} ⚠️$$

## §4 证据表（$107..120$，本档定稿）

| $k$ | 已知 $k$-code？ | 已知排除 $K\le k$？ | 来源 | 状态 |
|---|---|---|---|---|
| $107$ | — | — | BÖW 2004（**下界**，非构造） | **下界值** |
| $108..118$ | **未找到公开记录** | 无 | — | **未知** |
| $119$ | **未找到公开记录** | 无 | — | **未知** |
| $120$ | $✓$（Kamenetsky 显式 120 词） | — | Östergård 1991 | **上界值** |

$$\Longrightarrow\ \boxed{14\ \text{个整数字\ \textbf{无一被排除}};\ 119\ \text{与 }108\ \text{地位\ \textbf{相同}}}\ ✓$$

## §5 建议下一步（**待唐先生定 ✓**）

$$\textbf{(甲) 上界路线（本档推荐优先，因现成抓手 ✓）}:\ \text{取 Kamenetsky 之 }120\text{-code},\ \text{做\ \textbf{删点/小改实验}}$$
$$\qquad \text{① 单个删除：}\exists c\ \text{使 }C\setminus\{c\}\ \text{仍覆盖？}\quad \text{② 小规模 replacement/switch：能否得 }119\ ?\quad \text{③ 若得 }119 \Longrightarrow \textbf{直接 FULL（悬赏）}$$
$$\qquad \text{（此法\ \textbf{便宜、可即时判定}、且\ \textbf{上界侧是构造问题}，与下界侧之表示审计负证据无冲突 ✓）}$$
$$\textbf{(乙) 下界路线}:\ \text{受本会话表示审计之负证据约束（incidence／coset／boundary／spectral 四类皆无独立 }P_1\ ⚠️\text{）}$$
$$\textbf{(丙) 受限族路线}:\ \text{线性码／给定自同构群之精确最小值（悬赏逐字"Closing a route is a result"）}\ ✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "两端冻结" "下界来源拆解" "对称目标"
技术词 两端冻结    命中文件数=0    ::
技术词 下界来源拆解  命中文件数=0    ::
技术词 对称目标    命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **权威源直取**（Kéri 变更日志／OEIS／arXiv）＋ 档案引证 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️（第三方页面）；本档**只作状态记录**，**不主张**新数学 ✗
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- $\S5$(甲) **未执行** ✗；**不主张**删点实验必成 ⚠️
