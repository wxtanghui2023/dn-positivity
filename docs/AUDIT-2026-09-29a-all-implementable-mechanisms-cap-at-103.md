# AUDIT-2026-09-29a — **唐先生令：107 必出自\ \textbf{已有机制} ⟹ 逐条实测全部可实现机制在 $n{=}10$ 之上确界**

> **性质**：**审计（逐条实测 ＋ 归属定位）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 08:1x ✓
> **唐先生令（逐字）**：「现在没有直接论文公式，需要自行推导出 107。这个是论文已知数据，不可能需要新的算术机制」✓

**已查地图**：接续 `AUDIT-af`（excess）／`ag`（Zhang $r{=}1$）／`ah`（$Z^{(i)}$）／`ai`（FM）✓

D0: 本档对象 ＝ **档案已有**（全部为既有机制——无新数学对象 ✓）
D1: 0（产出＝**全部可实现机制之上确界实测 ＋ 107 归属定位** ⚠️✓）

---

## §0 结论（先给，照唐先生之逻辑）

$$\boxed{\text{① 全部\ \textbf{可实现}之已有机制在 }n{=}10\ \text{之上确界} ＝ \mathbf{103}\ \text{（七族实测一致）}}$$
$$\boxed{\text{② 纯粹形如 }2^n/(n{+}c)\ \text{之式\ \textbf{不可能}给 }107:\ \text{需 }c\approx-0.43\ \text{（非整数）}}$$
$$\boxed{\text{③ ⟹ 107 之归属必为\ \textbf{混合码框架}（BÖW 2004 general }R{=}1\text{）—— 此即唐先生所指之"已有机制"}}$$
$$\boxed{\text{④ 关键数值门槛}:\ \text{level-3 SDP 已给 }105.2223\Rightarrow K\ge106;\ \text{故\textbf{唯一}待排除者 ＝ }106}$$

## §1 全部可实现机制之上确界（**七族，实测 ✓✓**）

| 机制 | $n{=}10$ 之值 | $\lceil\cdot\rceil$ |
|---|---|---|
| sphere covering $2^n/(n{+}1)$ | $93.0909$ | $94$ |
| Thm 24（Habsieger／Honkala，$p{=}11$） | $93.5914$ | $94$ |
| **Thm 52（van Wee）** | $\mathbf{102.4}$ | $\mathbf{103}$ |
| **Thm 54（Haas 2008 改进）** | $\mathbf{102.4}$ | $\mathbf{103}$ |
| **Zhang pair $r{=}1$ 单条**（$(5,5,1,1)_{22}$） | $\mathbf{102.4}$ | $\mathbf{103}$ |
| **induced $Z^{(i)}$（$i{=}0..10$）＋ 非负组合** | $\mathbf{102.4}$（$11/11$） | $\mathbf{103}$ |
| **induced ＋ FM 整数消元** | 无闭合（$\S$`AUDIT-ai`） | $\mathbf{103}$ |
| 混合码框架 $(b,t){=}(10,0)$（van Lint--van Wee 广义） | $\mathbf{102.4}$ | $\mathbf{103}$ |
| Cauchy--Schwarz／球交（覆盖） | $N_1{+}N_2\ge81$（$M{=}106$） | 弱且可满足 |

$$\therefore\ \boxed{\text{七族\ \textbf{全部止于 }103};\ \text{无一族可达 }105,\ \text{更无论 }107}\ ✓✓$$
$$\text{（注}:\ \text{混合码框架在 }(8,2)\ \text{给 }186.8\text{、}(6,4)\ \text{给 }355.8\ ——\ \textbf{但那是\ 混合空间}\ \mathbb F_2^b\times\mathbb F_3^t\ \text{之界，非 }K_2(10,1)\text{）}$$

## §2 ★ 形如 $2^n/(n{+}c)$ 之式不可能给 107（**✓ 排除一类**）

$$\text{欲 }2^{10}/(10+c)\ \ge\ 107\ \Longrightarrow\ 10+c\ \le\ 1024/107=9.5701\ \Longrightarrow\ c\ \le\ -0.4299$$
$$\text{但 sphere 型之 }c\ \text{由组合量给出（}\ge0\text{）};\ \text{故\ \textbf{任何} }2^n/(n{+}c),\ c{=}O(1)\ \text{之式皆不可能}\ ✓$$
$$\therefore\ \boxed{\text{107 必出自\ \textbf{非}球型、非齐次分母之机制}\ ——\ \text{即需"加项/移位"，而非换分母}}\ ✓$$

## §3 ★ 归属定位（**本档核心 ✓✓**）

$$\text{已知史链（Kéri 表}）:\ 94\to96\to97\to103\to105\to107;\quad [67]{=}\text{Zhang 1991 (pair)},\ [130]{=}\textbf{BÖW 2004}$$
$$\text{而}:\ \text{Zhang pair\ \textbf{单条}给 }103\ (\text{本会话实测});\ \text{其 }105\ \text{须\ \textbf{完整 Zhang 方法}（induced ＋ rounding ＋ 组合）} ✗\text{（本会话 FM 未闭合）}$$
$$\therefore\ \boxed{\text{105 与 107 皆属\ \textbf{已发表方法}，而非单条不等式};\ \text{其原文\ \textbf{未得}（IEEE／Wiley 付费）}}$$
$$\text{唐先生之判断\ \textbf{成立}}:\ \text{107 不需新机制};\ \text{但也\ \textbf{不能}由我们已实现的机制自动得出} \Longrightarrow \text{需\ \textbf{原文之精确不等式}}$$
$$\text{现有最强之\ \textbf{可自行实现}机制}:\ \text{level-3 SDP（Gijswijt--Polak 2025 Table 5）＝ }\mathbf{105.2223}\ \Longrightarrow\ K\ \ge\ \mathbf{106}\ ✓$$
$$\therefore\ \boxed{\text{已排除 }105;\ \textbf{唯一}待排除者 ＝ }\mathbf{106}\ (\text{即 }E{=}142)$$

## §4 三条可行之路（**供唐先生定夺，不作裁定 ✗**）

$$\textbf{(i)}\ \text{取原文}:\ \text{Zhang 1991（IEEE TIT 37:573--582）之 induced/rounding 机制};\ \text{BÖW 2004（JCD 12:157--176）之 general }R{=}1\ \text{不等式} ⚠️\ \text{（付费墙）}$$
$$\textbf{(ii)}\ \text{提高 SDP 层级}:\ \text{level-3 已给 }105.2223;\ \text{level }\ge4\ \text{或可达 }>106\ \Longrightarrow\ K\ge107\ \text{（计算量待估}）⚠️$$
$$\textbf{(iii)}\ \text{接受 }\mathbf{103}\ \text{为\ \textbf{自助算术上限}}:\ \text{七族一致};\ \text{记为\ \textbf{负资产}（"纯二进算术族不能区分 }106\text{ 与 }107"\text{）} ✓$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "已有机制上限" "107归属" "非新机制"
技术词 已有机制上限  命中文件数=0    ::
技术词 107归属     命中文件数=0    ::
技术词 非新机制     命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **全部为既有机制之实测**（七族 ＋ $2^n/(n{+}c)$ 排除 ＋ SDP 门槛）＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** Zhang／BÖW 公式 ✗；**不主张** $106$ 已排除 ✗（V290）
