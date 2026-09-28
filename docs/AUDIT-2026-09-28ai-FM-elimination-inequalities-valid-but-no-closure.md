# AUDIT-2026-09-28ai — **FM 消元所得不等式\ \textbf{全部有效}（0/904 违反）✓✓，但两条辅助断言为假、\textbf{闭合不成立}**

> **性质**：**审计（逐条实测）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 08:0x ✓
> **唐先生令**：做有限整数消元（Fourier--Motzkin），目标 $M\ge107$ ✓

**已查地图**：接续 `AUDIT-ah`（$Z^{(i)}$ 全表 ＋ pair 层闭合）／`AUDIT-ag`（Zhang $r{=}1$）✓

D0: 本档对象 ＝ **档案已有**（$A_j(u)$／Zhang 不等式／FM 消元——无新数学对象 ✓）
D1: 0（产出＝**五式全部实测有效 ＋ 两处断言否证 ＋ 一处闭合否证** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 唐先生之 (I1')、(I2')、(I3')、(★)、(C1)\ \textbf{全部有效}（0/904 违反）}}$$
$$\boxed{\text{② ✗ 断言 }u\in C\Rightarrow A_1{=}0\ \textbf{为假}（A_1\ \text{分布 }\{0{:}55,1{:}36,2{:}23,3{:}6\}\text{）}}$$
$$\boxed{\text{③ ✗ 断言 }u\notin C\Rightarrow A_1\le4\ \textbf{为假}（实测 }\max A_1=\mathbf 5\text{，7 例）}}$$
$$\boxed{\text{④ ✗ FM 闭合\ \textbf{不成立}：}(\text{C1})\ \text{与}\ M\le106\ \text{预算合起来给平凡式}\ 40A_1+29e\ge-388}$$

## §1 ① 五式之逐条实测（**✓✓ 全对，本档最重要正面结果**）

$$\text{(I1')}\ 76A_1+15A_3\le176+18e+4A_4:\quad \textbf{违反 }0/904\ ✓$$
$$\text{(I2')}\ 24A_1-15A_3\le21e+6A_4+10A_5-528:\quad \textbf{违反 }0/904\ ✓$$
$$\text{(I3')}\ 444A_1+70A_3\le96e+56A_4+10A_5+20A_6-528:\quad \textbf{违反 }0/904\ ✓$$
$$\text{(★)}\ 100A_1\le39e+10A_4+10A_5-352:\quad \textbf{违反 }0/904\ ✓$$
$$\text{(C1)}\ 39e+10(A_4+A_5)\ge452:\quad \textbf{违反 }0/904\ ✓$$
$$\therefore\ \text{FM 消元之\ \textbf{代数步骤正确}};\ \text{所得皆为\ \textbf{合法}不等式}\ ✓✓$$
$$\text{样本}:\ u{=}0000000000:\ (A_1,A_2,A_3,A_4,A_5)=(1,5,13,26,30),\ e{=}1;\ (★):\ 100\le247\ ✓$$

## §2 ②③ 两处辅助断言之否证（**✗✗**）

$$\text{断言 }u\in C\Rightarrow A_1{=}0:\quad \textbf{实测}A_1\ \text{分布}\ \{0{:}55,\ 1{:}36,\ 2{:}23,\ 3{:}6\}\ \Longrightarrow\ \mathbf{65/120}\ \text{条码字有}\ A_1>0\ ✗✗$$
$$\qquad(\text{因 120-code 本有 }50\ \text{个距离-1 码字对};\ A_1(c)>0\ \text{于其端点}）$$
$$\text{断言 }u\notin C\Rightarrow A_1\le4:\quad \textbf{实测}\ \max A_1=\mathbf 5\ (\text{7 例});\ A_1\ \text{分布}\ \{1{:}746,2{:}136,3{:}13,4{:}2,5{:}7\}\ ✗$$
$$\text{根因}:\ 5A_1+A_2+A_3\ge22\ \text{只给}\ A_1\ \text{之\ \textbf{下界联动}（}\min(A_2{+}A_3)=22-5A_1\text{）};\ \text{当 }A_1\ge5\ \text{时该约束\ \textbf{自动满足}（真空）}$$
$$\qquad\text{故}\ A_1\le4\ \text{系\ \textbf{非推理}（把"最小值为负"误读为"不可行"）}✗$$

## §3 ④ FM 闭合之实测否证（**✗**）

$$\text{预算（}M\le106\text{）}:\ \sum_{j\ge4}A_j=M-(A_1{+}A_2{+}A_3)\le106-(22-4A_1+e)=84+4A_1-e$$
$$\text{与 (C1)}:\ 10(A_4+A_5)\ge452-39e\ \text{合起来}:\ 10(84+4A_1-e)\ge452-39e\ \Longrightarrow\ \boxed{40A_1+29e\ge-388}\ \text{（\textbf{恒真}）}✗$$
$$\therefore\ \boxed{\text{FM 消元路线的\ \textbf{闭合不成立}};\ \text{pair-level 整数闭包同样止步}}$$
$$\text{（与 }\texttt{AUDIT-ah}\ \text{之"pair 层闭合于 }103"\ \text{一致};\ \text{亦与 }\texttt{AUDIT-af}\ \text{之"excess 族止于 }103"\ \text{一致}）$$

## §4 累计层级账（**五族皆止于 }103\text{，定稿 ✓✓**）

| 机制族 | $n{=}10$ 之界 | 出处/档 |
|---|---|---|
| sphere covering | $94$ | 平凡 |
| excess（van Wee／Habsieger／Honkala／Haas） | $\mathbf{103}$ | `AUDIT-af`（Thm 24/52/54） |
| **Zhang pair inequality（单条）** | $\mathbf{103}$ | `AUDIT-ag`（$102.4$，van Wee 级） |
| **induced $Z^{(i)}$ ＋ 非负组合** | $\mathbf{103}$ | `AUDIT-ah`（$11/11$ 皆 $102.4$） |
| **induced ＋ FM 整数消元** | $\mathbf{103}$（无闭合） | **本档** |
| **线性不等式族（Zhang 1991 pair）** | $\mathbf{105}$ | 文献（Kéri 表 $[67]$） |
| **混合码 general $R{=}1$（BÖW 2004）** | $\mathbf{107}$ | 文献（Kéri 表 $[130]$） |

$$\therefore\ \boxed{\text{自助路线在\ \textbf{pair 层三重独立失败}（单条／组合／整数消元）} \Longrightarrow \text{下一步\ \textbf{triple-covering}（Zhang--Lo 1992）}} ✓$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "FM消元实测" "A1上界失效" "闭合不成立"
技术词 FM消元实测   命中文件数=0    ::
技术词 A1上界失效   命中文件数=0    ::
技术词 闭合不成立   命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **120-code 全量实测**（五式＋两断言＋闭合）＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** 公式 ✗；**不主张** $106$ 已排除 ✗（V290）
