# RESULT-2026-09-29-INV5 — 第 5 轮：$\gamma_2(Q_9)$ **平凡**（更正第 4 轮）＋ 切片交叉结构**两处最优皆不紧**

> 空间 B｜非 C 号｜唐先生 23:37「继续」｜**不主张任何新值**（V290）

**已查地图**：本会话 `INV4`（切片引理）／`DE1`（紧度扫描）／`AUDIT-28q`
D0: 本档对象 = **档案已有**（切片/缩短）之**精化 ＋ 紧度实测**（新数学对象：无 ✗）
D1: 0（产出 = **一处自我更正 ＋ 一张紧度实测表 ＋ 一条路线否决** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\textbf{① 更正第 4 轮}:\ \gamma_2(Q_9)=\mathbf{62}\ \textbf{平凡}\ (\text{取 }P_0{=}\text{62-码},P_1{=}\varnothing\ \text{即达}; \text{又 }\ge K(9,1){=}62) \Longrightarrow \text{第 4 轮 }\gamma_2\ \text{路线\ \textbf{vacuous}}\ ✗}$$
$$\boxed{\textbf{② 精化切片关系（实测全成立 ✓✓）}:\quad Q_9=N[P_0]\cup P_1\ \ \textbf{且}\ \ Q_9=N[P_1]\cup P_0\ (\text{即 }G_0{\subseteq}P_1,\ G_1{\subseteq}P_0)}$$
$$\boxed{\textbf{③ 但两处最优处\ \textbf{皆不紧}}:\ |G_0|\ \text{远小于}\ |P_1|\ (\text{120-码: }25\text{–}47\ \text{vs }59\text{–}64;\ \text{62-码: }10\text{–}26\ \text{vs }30\text{–}32) \Longrightarrow \text{无 D/E 型极值信号}\ ✗}$$
$$\therefore\ \text{缩短/切片族\ \textbf{亦只给球界型弱界}} \Longrightarrow \textbf{该族对 107 死} ✗$$

## §1 精化切片关系的推导（**比第 4 轮更准**）

$$\text{点 }(1,x)\in Q_{10}\ \text{之覆盖者 }c:\ d(c,(1,x))\le1$$
$$\qquad c\in C_1(\text{b 位}=1)\Longrightarrow d(\mathrm{proj}\,c,x)\le1\Longrightarrow x\in N[P_1]\ ✓$$
$$\qquad c\in C_0\Longrightarrow 1+d(\mathrm{proj}\,c,x)\le1\Longrightarrow \mathrm{proj}\,c=x\Longrightarrow x\in P_0\ ✓$$
$$\therefore\ Q_9=N[P_1]\cup P_0;\ \text{对称地}\ Q_9=N[P_0]\cup P_1\ \Longrightarrow\ \boxed{G_0:=Q_9\setminus N[P_0]\subseteq P_1,\quad G_1\subseteq P_0}\ ✓$$

**实测（120-码 10 切片 / 62-码 9 切片）**：全部成立 ✓✓（见 §0③ 数据）

## §2 紧度实测（**D/E 筛选之第四处**）

| 码 | $|P_0|,|P_1|$ | $|G_0|$ 范围 | $|G_1|$ 范围 | $|N[P]|/(10|P|)$ | 紧度判定 |
|---|---|---|---|---|---|
| 120-码（$Q_{10}$） | 56–61 / 59–64 | 24–47 | 10–48 | 0.773–0.871 | **不紧** ✗ |
| 62-码（$Q_9$ 最优） | 30–32 | 10–26 | 10–26 | 0.742–0.787 | **不紧** ✗ |

$$\Longrightarrow\ \text{与 }DE1\ \text{（层覆盖紧度 }\le0.87\text{）\ \textbf{同向}}:\ \text{已知最优处\ \textbf{处处松弛}} \Longrightarrow \text{D/E 无入口（第四次确认）}$$

## §3 五轮逆向重建之**总账**

| 轮 | 对象 | 结果 |
|---|---|---|
| INV1 | 同余律搜索（聚合＋三点总量） | **否定**（可行集极大，含 $\mu\le2,A_1{=}0$ 退化解） |
| INV2 | 细节审计（van Wee 代入） | **精确无细节空间**；可调空间＝excess 同余层 |
| INV3 | 球 excess parity / 深层同余 | parity **平凡**（新恒等式）；深层同余**不存在** |
| INV4 | 切片引理 | 得 $K(10,1)\ge\gamma_2(Q_9)$，**但**（本档）$\gamma_2{=}62$ ⟹ vacuous |
| INV5 | 精化切片 ＋ 紧度 | 关系成立但**不紧** ⟹ 族死 |

$$\boxed{\text{五轮结论}:\ \text{未复原那 1 格};\ \text{但\ \textbf{逐轮排除}五族（同余/细节/parity/γ}_2\text{/切片）};\ \text{且证据指向\ \textbf{107 出自 }n{=}10\text{ 专属论证}}}$$

## §4 边界（硬 ✓）

- **主动更正**第 4 轮之 vacuous 路线 ✓（纪律：自查不得掩）
- **不主张**任何新值 ✓；未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
