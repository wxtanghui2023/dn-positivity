# CLOSE-2026-09-30 — $\delta{=}1$ 线收口：**A₂ 联合 LP 不闭合**（max $A_2{=}161$；需 $\le124$）

> 空间 B｜非 C 号｜唐先生 09:49「继续」（做 $A_2$ 联合 LP）｜**不主张任何新值**（V290）
> 时间：2026-09-30 09:5x

**已查地图**：承 `RESULT-MULT`／`MULT2`／`REFUTE-2026-09-30{,b}`／`ASSETS-A-DELSARTE-1`
D0: 本档对象 = **档案已有**（Delsarte/Krawtchouk／覆盖恒等式／$A_k$）之**联合 LP**（新数学对象：无 ✗）
D1: 0（产出 = **一条"不闭合"之定量判定 ＋ 本线收口** ⚠️✓）

---

## §0 判定（先给）

$$\boxed{A_2\ \text{联合 LP（Delsarte＋Krawtchouk＋覆盖恒等式＋层覆盖族}＋\text{INV2）}:\ \max A_2=\mathbf{161}\ (\text{被 INV2 卡住})}$$
$$\boxed{\text{链闭合需 }A_2\le\mathbf{124}\ (\text{且 }A_1\le50);\ \text{LP 另给 }\max A_1=\mathbf{102}\ ✗✗ \Longrightarrow \textbf{A2 路线不闭合}}$$

## §1 LP 结果（实跑，$M{=}106$）

| 约束集 | $\max A_2$ | $\min A_2$ | $\max A_1$ |
|---|---|---|---|
| 恒等式 ＋ Delsarte ＋ 层覆盖 | **386** | 52 | 178 |
| ＋ INV2（$A_1{+}A_2\le161$） | **161** | 52 | **102** |

（解例：$\max A_2$ 含 INV2 时取 $A_1{=}0,A_2{=}161,A_3{=}990,P{=}424$；$\max A_1$ 时取 $A_1{=}102,A_2{=}58$）

$$\therefore\ \text{缺额}:\ A_2\ \text{需再紧 }\mathbf{37}\ \text{单位};\ A_1\ \text{需再紧 }\mathbf{52}\ \text{单位} \Longrightarrow \text{现工具\ \textbf{给不出}}$$

## §2 本线（$\delta{=}1$ 层）之**完整账**（供续线，逐条已核验）

$$\textbf{✓ 成立}:\ (a)\ \text{二型分类}\ (a_1,a_2)\in\{(1,5),(2,4)\};\ (b)\ n_B\le2A_2;\ (c)\ \text{A2 之共享对}\ \{e_j{+}e_a,e_j{+}e_b\}\ \text{两中点皆非码}\Longrightarrow\text{落 }H_{00}$$
$$\qquad(d)\ \text{三恒等式}\ H_{00}{+}H_{01}{+}H_{11}{=}A_2,\ P{=}H_{01}{+}2H_{11},\ H{=}2H_{00}{+}H_{01}\ (\text{双码 }\checkmark);\ (e)\ \text{耦合}\ H_{00}=\tfrac{H-P}2+H_{11}=A_2-P+H_{11}$$
$$\qquad(f)\ \text{重数实测}\ r_{A1}{=}\mathbf4\ (\text{远小于 }9),\ r_{A2}{=}\mathbf5;\ H_{00}{=}110,\ H{=}298\ (M{=}120)$$
$$\textbf{✗ 不成立／不足}:\ (g)\ n_A\le9A_1\ \text{（被 120-码 301/338 反例推翻）};\ (h)\ \text{A2 经 }H_{00}\ \text{收费}\Longrightarrow\text{需 }r_{A2}\le4,\ \text{实测 }5\ (\text{差 }1)$$
$$\qquad(i)\ \textbf{本档}:\ \text{联合 LP 给不出 }A_2\le124\ \text{与}\ A_1\le50$$

$$\boxed{\therefore\ \text{链闭合之充要条件}:\ H_{00}\le99\ (\Longleftrightarrow A_2\le99+P-H_{11})\ \text{且}\ A_1\le50;\ \text{二者现工具皆给不出}\ ✗}$$

## §3 收口与去向

$$\textbf{(甲)}\ \textbf{本线记 CLOSED-不足}（\text{非"不可能"}）:\ \text{结构已完全刻画（四型＋三恒等式＋耦合式），缺的只是}\boxed{\text{一条更紧的 }A_2/H_{00}\ \text{上界}} \ ⚠️$$
$$\textbf{(乙)}\ \text{若继续，唯一有信息量之形式}:\ \text{证 }H_{00}/A_2\le0.8\ \text{（}\text{局部引理}）\ \text{或}\ A_1\le50\ \text{（}M{=}106\text{）—— 皆超出 Delsarte/聚合类} ✗$$
$$\qquad\text{实测比 }H_{00}/A_2 = 0.738\ (M{=}120)\ /\ \mathbf{0.909}\ (n{=}9\ \text{最优}) \Longrightarrow \textbf{临界，风险高} ⚠️$$

## §4 边界（硬 ✓）

- **不主张**任何新值；本档为**不闭合之定量判定**（LP 实跑）＋ 本线完整账 ✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
