# AUDIT-2026-09-29k — **P1 靶（"$M{=}106\Rightarrow\ge72$ 个 $\mu\ge3$ 点"）被\ \textbf{单调趋势否掉}**；另纠正一处上界（$161$，非 $411$）

> **性质**：**实测（趋势）＋ 自查纠错**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 10:5x ✓
> **唐先生令**：「继续」（沿几何方向）✓

**已查地图**：接续 `AUDIT-29j`（parity 属球 excess；方向相反）／`29c`（框架 ≡ 球界）✓

D0: 本档对象 ＝ **档案已有**（$\mu$／excess 分布——无新数学对象 ✓）
D1: 0（产出＝**一处趋势否靶 ＋ 一处上界纠正 ＋ 一张趋势表** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ★★ }\#\{x:\mu\ge3\}\ \text{随 }M\ \textbf{单调上升}:\ 51\ (M{=}120)\to146\ (M{=}156) \Longrightarrow\ M{=}106\ \text{应}\ \lesssim51\ \ll72}$$
$$\boxed{\text{② ⟹ P1 靶「}\ge72\ \text{个 }\mu\ge3\ \text{点}\text{」\ \textbf{被趋势否掉}}✗✗}$$
$$\boxed{\text{③ ✗ 我上轮算术滑误}:\ M{=}106\ \text{之}\ N_1{+}N_2\ \text{上界应为 }\mathbf{161}\ (\text{非 }411)}$$

## §1 ① 趋势测量（**决定性 ✗✓**）

$$\text{方法}:\ \text{以 120-code 为基，随机加 }k\ \text{个码字得 }M=120\ldots156;\ \text{逐点算 }\mu(x)$$

| $M$ | $E$ | $\#\{\mu\ge2\}$ | $\#\{\mu\ge3\}$ | $\#\{\mu\ge4\}$ | $\sum\binom e2$ | $P_1{+}P_2$ |
|---|---|---|---|---|---|---|
| $120$ | $296$ | $223$ | $\mathbf{51}$ | $15$ | $102$ | $199$ |
| $123$ | $329$ | $250$ | $56$ | $16$ | $109$ | $219$ |
| $127$ | $373$ | $282$ | $66$ | $18$ | $123$ | $248$ |
| $130$ | $406$ | $308$ | $71$ | $18$ | $134$ | $270$ |
| $138$ | $494$ | $372$ | $88$ | $24$ | $166$ | $330$ |
| $147$ | $593$ | $439$ | $111$ | $33$ | $207$ | $400$ |
| $156$ | $692$ | $497$ | $\mathbf{146}$ | $33$ | $262$ | $477$ |

$$\therefore\ \boxed{\text{全部计数（}\#\{\mu\ge2\},\#\{\mu\ge3\},\#\{\mu\ge4\},\sum\binom e2,P_1{+}P_2)\ \text{皆随 }M\ \textbf{单调上升}}✓$$
$$\text{机理解释}:\ E=11M-1024\ \text{随 }M\ \text{增};\ E/M=11-\tfrac{1024}M\ \text{亦随 }M\ \text{增}\ (M{=}106:\ \mathbf{1.34}\ \text{最低})\Longrightarrow \text{小 }M\ \text{时 excess \ \textbf{更稀薄}}$$
$$\therefore\ M{=}106\ (\text{若存在})\ \text{之}\ \#\{\mu\ge3\}\ \textbf{应小于 }51\ \ll72 \Longrightarrow \boxed{\text{P1 靶\ \textbf{为假}}}✗✗$$

## §2 ② 为何靶必假（**结构原因 ✓**）

$$\text{靶要求}:\ M\ \text{减小时}\ \#\{\mu\ge3\}\ \textbf{增};\qquad \text{实测}:\ \text{方向\ \textbf{相反}}$$
$$\text{根源}:\ \text{集中度由 excess 总量 }E=11M-1024\ \text{驱动};\ M\downarrow\Rightarrow E\downarrow\Rightarrow\ \text{集中点}\downarrow$$
$$\therefore\ \boxed{\text{「迫使更多高重数点」\ \textbf{不是} 106→107 的机制}}✗$$
$$\text{须换成}:\ \text{一条在 }M{=}106\ \text{处\ \textbf{失效}、在 }M\ge120\ \text{处\ \textbf{成立}的\ 不等式}$$

## §3 ③ 自查纠错：$N_1{+}N_2$ 之上界（**✗✓**）

$$\text{链}:\ \sum_{x\in A}(\text{球 excess})\ =\ 11E-4(N_1{+}N_2)\ \ge\ |A|\ =\ 1024-M$$
$$M{=}106:\quad 11\cdot142-4(N_1{+}N_2)\ \ge\ 918\ \Longrightarrow\ 4(N_1{+}N_2)\le644\ \Longrightarrow\ \boxed{N_1{+}N_2\ \le\ \mathbf{161}}$$
$$\textbf{我上轮误写 }411\ (\text{把 }12288\ \text{记成 }11288)\ ✗;\ \text{本档更正为 }\mathbf{161}$$
$$\text{下界仍为}\ N_1{+}N_2\ \ge\ E/2\ =\ 71 \Longrightarrow\ \text{余量 }90\ (\text{仍未闭合})✗$$

## §4 当前缺口之精确定位（**收束 ✓**）

$$\text{所需}:\ \text{一条在 }M{=}106\ \text{失效之不等式};\ \text{形式上等价于\ \textbf{把 van Wee 之 }9\ \text{因子抬到 }>12.7} \Longrightarrow\ \text{即 }E\ \text{之下界须 }>142$$
$$\text{已知}:\ \text{该因子来自 }2t{+}b{-}R=9\ (\text{结构常数，不可调});\ \text{本会话已证可实现算术族上确界 }103{-}104,\ \text{SDP-3}=105.2223\Rightarrow106$$
$$\therefore\ \boxed{\text{缺口定位}:\ \text{须\ \textbf{非松弛型（integrality/几何）}机制},\ \text{且\ \textbf{不是}"更多高重数点"型}}}✓$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "趋势否靶" "上界纠正" "集中度单调"
技术词 趋势否靶     命中文件数=0    ::
技术词 上界纠正     命中文件数=0    ::
技术词 集中度单调    命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **120–156 七档实测 ＋ 自查纠错** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）
