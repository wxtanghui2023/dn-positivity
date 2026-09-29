# DERIVE-107-c（2026-09-29）—— **$T\!\leftrightarrow\!P$ incidence 判门：②\ \textbf{关闭}（压制仅由 $\mu$ 自身买得，无法转入 $E$）**

> **性质**：**纯推导 ＋ 全量实测（含我之 bug 更正）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 13:1x ✓
> **唐先生令**：选 ②（$\mu\ge3$）；先测 $T\!\leftrightarrow\!P$ incidence 再决定 ✓

**已查地图**：`DERIVE-107-b`（private-owner 恒等式）／`DERIVE-107`（充电形式）✓

D0: 本档对象 ＝ **档案已有**（$T,P,p(y),\mu$——无新数学对象 ✓）
D1: 0（产出＝**一处 bug 更正 ＋ $(T1)(T2)$ 证实 ＋ 平凡但饱和之压制 ＋ ②之关闭** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 你的 }(T1)(T2)\ \textbf{皆成立}:\ x\in P\cap N(y)\Rightarrow\text{owner}(x)\in C\cap S_2(y);\ p(y)\le2|C\cap S_2(y)|\ (\text{实测 }0/22\ \text{违例})}$$
$$\boxed{\text{② ✗✗ 但出现\ \textbf{平凡压制}}:\ p(y)\le10-\mu(y)\ (\text{码字邻域者不可能是私有点})\ ——\ \text{且实测\ \textbf{近乎饱和}}$$
$$\boxed{\text{③ ⟹ 压制的"代价"恰是 }\mu(y)\ \text{自身}\Longrightarrow\ \text{求和后 }\mu\ \text{相消} \Longrightarrow\ \textbf{无法转入 }E \Longrightarrow\ \textbf{② 关闭}}✗✓$$
$$\boxed{\text{④ ✓ 实测 }I_{TP}/|T|=5.27\ (\text{高相邻})\ ⟹\ T\ \text{对 }P\ \text{之排斥性\ \textbf{极弱}}}$$

## §1 ① 你的两条（**✓✓ 成立**）

$$(T1):\ x\in P\cap N(y)\Rightarrow c{=}\text{owner}(x)\ \text{满足}\ d(x,y){=}1,\ d(x,c){=}1\Longrightarrow d(c,y)\in\{0,2\};\ c\ne y\ (\text{因 }y\notin C)\Longrightarrow \boxed{d(c,y)=2}✓$$
$$(T2):\ c\in C\cap S_2(y)\ \text{与 }y\ \text{差两坐标}\Longrightarrow N(y)\ \text{中恰两点距 }c\ \text{为 }1\Longrightarrow\ \boxed{p(y)\le2|C\cap S_2(y)|}✓$$
$$\text{实测（120-code，}|T|{=}22\text{）}:\ \textbf{0 违例}✓;\quad |C\cap S_2(y)|\ \text{分布}\ \{4{:}1,5{:}14,6{:}7\}✓$$
$$\text{你的判断\ \textbf{正确}:\ }\mu(y)\ \text{不进入 }(T2)\ \text{右边}✓$$

## §2 ② 我之 bug 更正（**⚠️ 诚实**）

$$\text{首测我把 }p(y)\ \text{写成}\ \{\text{码字且 }\mu{=}1\}\ \text{之邻点数}\ ✗\ (\text{应为}\ \{\text{非码字且 }\mu{=}1\})$$
$$\text{暴露方式}:\ \text{账目不平（}82{+}46{+}14{+}8{=}150\ne220{=}10|T|\text{）}✓\ \text{—— 靠恒等式自查抓到}$$
$$\textbf{修正后账目}:\ \underbrace{\Sigma_{y\in T}\mu(y)}_{82}+\underbrace{I_{TP}}_{116}+\underbrace{I_{T2}}_{14}+\underbrace{I_{T3+}}_{8}=220=10|T|\ ✓✓$$

## §3 ★ ③ 平凡但饱和之压制（**关键读数**）

$$\text{因 }y\ \text{之码字邻点}\ (\mu(y)\ \text{个})\ \text{皆非私有点}\Longrightarrow\ \boxed{p(y)\le10-\mu(y)}\ (\textbf{平凡})$$
| $\mu(y)$ | $y$ 数 | $p$ 均值 | $p$ 最大 | 上界 $10-\mu$ |
|---|---|---|---|---|
| $3$ | $13$ | $6.46$ | $\mathbf{7}$ | $7$ — **饱和** |
| $4$ | $2$ | $4.50$ | $\mathbf{6}$ | $6$ — **饱和** |
| $5$ | $7$ | $3.29$ | $4$ | $5$ — 近饱和 |

$$\therefore\ \text{压制\ \textbf{存在}（}p\le10-\mu\text{）但\ \textbf{其代价恰为 }\mu\ \text{自身}}:\ \text{求和得}\ I_{TP}\le10|T|-\Sigma\mu(y)$$
$$\therefore\ \boxed{\text{求和后 }\mu\ \text{相消} \Longrightarrow \textbf{不能转入 }E \Longrightarrow\ \text{② 之充电价值为零}}✗✓\ (\text{与你预判一致})$$

## §4 ④ 四个量之实测（**✓**）

$$I_{TP}=\mathbf{116}\ (I_{TP}/|T|=5.27)\big|\ I_{T2}=14\ (0.64)\big|\ I_{T3+}=8\ (0.36)\big|\ \Sigma\mu(y)=82$$
$$\text{读数}:\ \text{（i）}I_{TP}/|T|=5.27\Longrightarrow T\ \text{与 }P\ \text{\textbf{高度相邻}}⟹ \text{排斥性弱}✓$$
$$\text{（ii）}I_{T3+}=8\ \text{很小}\Longrightarrow T\ \text{点彼此\ \textbf{几乎不相邻}}\Longrightarrow \mu\ge3\ \text{点\ \textbf{分散}}✓$$
$$\text{（iii）}p(y)\ \text{分布}\ \{3{:}6,4{:}2,5{:}1,6{:}6,7{:}7\}:\ \textbf{无一为 }0,\ \textbf{无一}\ge8✓$$

## §5 判门结论（**按你 §8 之三条**）

$$\textbf{判据①}\ p(y){=}0\ \text{大量存在？}\ \textbf{否}（0/22）\qquad\textbf{判据②}\ p(y)\ \text{可达 }8{-}10？\ \textbf{否}（最大 7）$$
$$\textbf{判据③}\ \text{是否被"明显小于 10 之常数统一压住"\ 且\ \textbf{能转入 }E？}\ \text{前半\ \textbf{是}（}p\le10-\mu\text{）；后半\ \textbf{否}（}\mu\ \text{相消）}$$
$$\therefore\ \boxed{\text{②\ \textbf{关闭}}:\ \text{压制是平凡的，代价由 }\mu\ \text{自付，不产生 }6E\ \text{级信息}}✗✓$$

## §6 下一刀（**③，同一纪律 ✓**）

$$\text{③ 目标}:\ \mu{=}2\ \text{点之\ \textbf{配对结构}}:\ \text{设 }n_2=\#\{\mu{=}2\}\text{；对 }y\in\{\mu{=}2\}\ \text{记其两个 owner}\ (u,v)$$
$$\text{待测（P-a）}:\ \text{①}(u,v)\ \text{之距离分布};\ \text{②}y\ \text{与其它 }\mu{=}2\ \text{点之相邻结构};\ \text{③有无\ \textbf{一个 excess 单位只能被少数几次复用}之载体}$$
$$\textbf{门槛同前}:\ \text{载体之复用次数}\ \le5\ \text{才有 }6E\ \text{级希望}✓$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "T与P相邻" "p≤10-μ平凡界" "②判门关闭"
技术词 T与P相邻      命中文件数=0    ::
技术词 p≤10-μ平凡界  命中文件数=0    ::
技术词 ②判门关闭     命中文件数=0    ::
```

## §8 边界（硬 ✓）

- **120-code 全量实测 ＋ 账目恒等式自查 ＋ bug 更正** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张** $107$ 不可达 ✗（V290）；②之关闭系**本载体**之结论 ✓
