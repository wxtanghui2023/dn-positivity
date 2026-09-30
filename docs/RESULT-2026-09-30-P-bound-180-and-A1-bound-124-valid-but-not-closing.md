# RESULT-2026-09-30-P180 — 新硬约束 **$P\le180$** 与 **$A_1\le124$**：**逐条验算成立 ✓✓，但不闭合** ✗

> 空间 B｜非 C 号｜唐先生 09:58 之链（$n_B\le H$、$9q_1$、$8r_1$、$(9/2)$ 不等式）｜**不主张任何新值**（V290）
> 时间：2026-09-30 10:0x

**已查地图**：承 `CLOSE-delta1`／`MULT`／`MULT2`／`REFUTE-2026-09-30{,b}`／`ASSETS-A-DELSARTE-1`
D0: 本档对象 = **档案已有**（$\delta$ 三型／$q_1,r_1,P,H$／度数分布）之**逐条验算 ＋ 联合 LP**（新数学对象：无 ✗）
D1: 0（产出 = **两条新硬约束（已验算） ＋ 一条"不闭合"之 LP 判定** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\textbf{① 链成立 ✓✓}:\ n_B\le H=2A_2-P,\ n_{A1}\le9q_1,\ n_{A2}\le8r_1,\ q_1\le2A_1-\tfrac29P,\ r_1\le142-2A_1 \Longrightarrow \boxed{P\le180}}$$
$$\boxed{\textbf{② 推论 ✓}:\ P\ \text{之凸性下界}\ +\ P\le180\Longrightarrow \boxed{A_1\le124}\ (\text{核验}: A_1{=}124\Rightarrow P_{\min}{=}178\ ✓;\ A_1{=}125\Rightarrow182>180\ ✗)}$$
$$\boxed{\textbf{③ 但不闭合 ✗}:\ \text{全部有效约束（含 }P\le180,\ A_1\le124\text{）}@M{=}106\ \textbf{仍可行};\ \text{甚至 }P\le41\ \text{亦可行}}$$

## §1 链之逐条验算（**本档复核，皆成立**）

$$\textbf{(B)}\ n_B\le H:\ \text{B 型点}\ v\notin C,\ \mu(v){=}2\Longrightarrow v\ \text{对}\ H=\sum_{x\notin C}\binom{\mu}2\ \text{贡献恰 1};\ \text{各点互异}\Longrightarrow n_B\le H\ ✓$$
$$\textbf{(A1)}\ n_{A1}\le9q_1\ (q_1:=\#\{c\in C:e(c){=}1\}):\ \text{固定 }c,\ \text{其 10 邻点中除唯一码字邻居外 9 个非码}\ \Longrightarrow\le9\ ✓\ (\text{实测：每 }c\ \text{最多 }4)$$
$$\textbf{(A2)}\ n_{A2}\le8r_1\ (r_1:=\#\{x\notin C:e(x){=}1\}):\ \mu(x){=}2\Longrightarrow x\ \text{两码字邻居}\Longrightarrow\le8\ ✓\ (\text{实测最多 }5)$$
$$\textbf{(2)}\ q_1\le2A_1-\tfrac29P:\ \binom d2\le\tfrac92d\ (2{\le}d{\le}10)\Longrightarrow P\le\tfrac92(2A_1-q_1)\ ✓$$
$$\textbf{(3)}\ r_1\le142-2A_1:\ \sum_{x\notin C}e(x)=E-2A_1=142-2A_1\ ✓$$
$$\Longrightarrow\ n_1\le9\bigl(2A_1-\tfrac29P\bigr)+8(142-2A_1)+(2A_2-P)=1136+2A_1+2A_2-3P$$
$$\Longrightarrow\ \sum_{v\notin C}\delta\ge2754-2n_1\ \ge\ 482-4A_1-4A_2+6P;\qquad \text{恒等式}\ \sum_{v\notin C}\delta=1562-4A_1-4A_2$$
$$\Longrightarrow\ 6P\le1080\Longrightarrow \boxed{P\le\mathbf{180}}\ ✓✓;\qquad \text{又 }P_{\min}(A_1)\ \text{凸性}\Longrightarrow \boxed{A_1\le\mathbf{124}}\ ✓$$
$$\textbf{凸性下界}:\ 2A_1=106q+r\Rightarrow P\ge(106-r)\binom q2+r\binom{q+1}2\ ✓$$

## §2 决定性 LP 测试（**不闭合** ✗）

$$\text{约束集}:\ \text{恒等式（含 }E{=}142\ \text{强制}）\ +\ \text{Delsarte/Krawtchouk}\ +\ \text{层覆盖}\ +\ \text{INV2}\ +\ \text{度数分布}\ (m_d)\ +\ \text{整数性}$$
| 测试 | 判定 | 解得 |
|---|---|---|
| 基线（不加 P 上界） | **可行** ✗ | $A_1{=}54,A_2{=}106,P{=}193$ |
| $+P\le180$ | **可行** ✗ | $A_1{=}92,A_2{=}68,P{=}179$ |
| $+P\le180+A_1\le124$ | **可行** ✗ | $A_1{=}93,A_2{=}67,P{=}179$ |
| $+P\le41$（＝120-码实测值） | **可行** ✗ | $A_1{=}14,A_2{=}119,P{=}34$ |

$$\therefore\ \textbf{新约束虽真，但联合全部工具仍不能排除 }M{=}106\ ✗$$

## §3 对唐先生 §12（"证 $P\ge181$"）之判定 ⚠️

$$\text{由凸性}:\ P\ge181\iff A_1\ \gtrsim\ 125\ (\text{即 }P_{\min}(A_1)\ge181\iff A_1\ge125)$$
$$\text{而真实码之实测}:\ 120\text{-码 }P{=}41\ (A_1{=}50);\ 62\text{-码 }P{=}6\ (A_1{=}7) \Longrightarrow \textbf{真实码之 }P\ \text{极小（}\sim40\text{）}$$
$$\therefore\ \text{"}P\ge181\text{" 与实测严重相悖} \Longrightarrow \textbf{该方向不应作为闭合路线} ⚠️\ (\text{本线之 }P\ \text{上界}\le180\ \text{与实测 }41\ \text{亦相去甚远，故对该区间无约束力})$$

## §4 本档保留（**可正式入册 ✓**）

$$\textbf{(i)}\ P\le180\ (M{=}106\ \text{之必要条份});\qquad \textbf{(ii)}\ A_1\le124;\qquad \textbf{(iii)}\ n_B\le H=2A_2-P;\qquad \textbf{(iv)}\ n_{A1}\le9q_1,\ n_{A2}\le8r_1,\ q_1\le2A_1-\tfrac29P,\ r_1\le142-2A_1$$
$$\qquad\text{（其中 (iii) 严格强于旧 }n_B\le2A_2\ ✓\text{）}$$

## §5 边界（硬 ✓）

- **不主张**任何新值；本档为**验算 ＋ LP 判定**（不闭合）✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
