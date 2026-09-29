# RESULT-2026-09-29-M106-DLA — 离散层攻击：**$0\le 2A_2{-}P\le23$ 全被排除**（得 $\ge24$）；压测仍可行 ⟹ **binding 约束是 INV2**

> 空间 B｜非 C 号｜唐先生 23:54「攻 $2A_2{-}P=1$ 这一唯一剩余的最低离散层」｜**不主张任何新值**（V290）

**已查地图**：`PRESSURE-M106`（slack 表）／`DERIVE-c`（F9、$E{=}142$）／`INV2`
D0: 本档对象 = **档案已有**（$A_2,P,A_1$／F9）之**离散层穷推**（新数学对象：无；**新不等式：$H+2A_1\ge142$** ⚠️）
D1: 0（产出 = **一条更强之强化 ＋ 一条 binding 判定** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 比唐先生所求\textbf{更强}：}0\le 2A_2{-}P\le\mathbf{23}\ \textbf{全部不可能} \Longrightarrow 2A_2{-}P\ \ge\ \mathbf{24}}$$
$$\boxed{\text{② 新不等式（一般式）}:\quad H+2A_1\ \ge\ 142\quad\left(H:=2A_2{-}P=\sum_{x\notin C}\binom{\mu(x)}2\right)\ \text{—— 比 }F7\ \text{更强}}$$
$$\boxed{\text{③ 但压测仍可行}\ ✗\ \Longrightarrow\ \text{可行域中\textbf{binding 者＝INV2}（解处 }A_1{+}A_2{=}161\ \text{取等）}}$$

## §1 离散层穷推（**逐层实算**）

$$2A_2-P\ \overset{F9}{=}\ \sum_{x\notin C}\binom{\mu(x)}2;\qquad 142=\Sigma\delta=\sum_{x\notin C}(\mu-1)+2A_1$$
$$\Longrightarrow\ \sum_{x\notin C}(\mu-1)\ =\ 142-2A_1\ \ \textbf{恒为偶数}\ ✓$$
| $2A_2{-}P$ | 所需 $\sum_{x\notin C}(\mu-1)$ | 推出 $A_1$ | 判定 |
|---|---|---|---|
| 0 | 0 | 71.0 | ✗（$>59$） |
| 1 | 1 | **70.5** | ✗（**非整**） |
| 2 | 2 | 70.0 | ✗（$>59$） |
| 3 | 3 | 69.5 | ✗ |
| 4 | 4 | 69.0 | ✗ |
| 5 | 5 | 68.5 | ✗ |
$$\textbf{一般}:\ 2A_2{-}P=k\Rightarrow A_1=71-\tfrac k2 \Longrightarrow A_1\le59\ \text{要求}\ k\ge\mathbf{24}\ \Longrightarrow\ \boxed{2A_2-P\ge24}\ ✓✓$$
$$\text{（其中 }k\ \text{奇者连整数性都不过 ⟹ 更强）}$$

## §2 一般式（**本档新不等式**）

$$\binom{\mu}2\ \ge\ \mu-1\ (\forall\mu\ge1,\ \text{等号}\iff\mu\le2)\quad\text{逐点成立} \Longrightarrow \text{在 }C^c\ \text{侧求和}:$$
$$\boxed{H\ =\ \sum_{x\notin C}\binom{\mu}2\ \ge\ \sum_{x\notin C}(\mu-1)\ =\ 142-2A_1 \quad\Longleftrightarrow\quad H+2A_1\ \ge\ 142}$$
$$\text{相比 }F7\ (\ \Sigma\binom\mu2=H+P+2A_1\ge142\ ):\ \text{本式\textbf{剔除了 }P\ge0\ 之松弛} \Longrightarrow \textbf{严格更强}\ ✓$$

## §3 压测（新式加入后）

| 系统 | $M{=}106$ | 解处 $H{=}2A_2{-}P$／$A_1$ |
|---|---|---|
| 基线（恒等式＋层覆盖＋Krawtchouk＋F7＋F5＋$A_1{\le}59$） | **可行** ✗ | $H{=}416,\ A_1{=}3$ |
| ＋新式 $H+2A_1\ge142$ | **可行** ✗ | $H{=}418,\ A_1{=}6$ |

$$\therefore\ \text{新式虽把 }H\ \text{之最低值从 }1\ \text{推到 }\mathbf{24}\ \text{（幅度 }23\text{），但\ \textbf{不 bite}：可行解处 }H\approx418\ \text{远高于 }24$$

## §4 **binding 判定**（本档第二条收获）

$$\text{可行解处 }A_1{+}A_2=\mathbf{161}\ \text{（取等）} \Longrightarrow \textbf{真正压住可行域者＝INV2}\ \left(A_1{+}A_2\le161\right)$$
$$\text{而 INV2 之等价形式（INV3 给出）}:\quad v\notin C\Rightarrow\delta_{N[v]}=2(a_1{+}a_2)-11\ge1\iff \boxed{a_1(v)+a_2(v)\ \ge\ 6}$$
$$\therefore\ \textbf{下一刀唯一目标}:\ \textbf{强化 INV2}\ ——\ \text{即证"足够多之 }v\notin C\ \text{满足}\ a_1{+}a_2\ge7\ (\iff\delta\ge3)"$$
$$\qquad\text{（档案 }AUDIT\text{-}29j\ \text{只给出其上界向 }m\le180\ ✗\text{；要的是\textbf{下界向}，此即缺口）}$$

## §5 边界（硬 ✓）

- **不主张**任何新值；新式为**本档推导**（$H+2A_1\ge142$），幅度 23，**不足杀 106** ✓
- 未取论文原文（R16–17）✓；未重攻已 kill 之族 ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
