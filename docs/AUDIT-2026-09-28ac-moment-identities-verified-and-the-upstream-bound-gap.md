# AUDIT-2026-09-28ac — **三条矩恒等式实测通过，但\ \textbf{按判据 STOP}：缺的是 $N_1{+}N_2$ 之\ \textbf{上界}**

> **性质**：**审计（含实测与判据执行）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:13 ✓
> **唐先生令**：把 $107$ 之**数学结构**往下拆；找二阶/三阶 incidence 不等式，证 $E\ge153$；**判据：只得 $E\ge142$ 或更弱 ⟹ 立即 STOP** ✓

**已查地图**：★**命中既有档** —— `EXCESS-2026-09-25`（$\delta$-场恒等式系统，**已含本档三条** ⚠️）／`AUDIT-ab`（链实测）／`AUDIT-aa`（Zhang 系列）✓

D0: 本档对象 ＝ **档案已有**（$\delta$／$a$／$N_i$／三条矩恒等式——`EXCESS-2026-09-25` 已载 ✓）
D1: 0（产出＝**三式实测复现 ＋ 判据执行 ＋ 缺口精确定位** ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{① 唐先生三条矩恒等式\ \textbf{全部精确实测通过}（120-code）}}✓✓$$
$$\boxed{\text{② 但为 $M{=}106$ 只需给\ \textbf{一个下界} $N_1{+}N_2\ge71$；要证伪需 $N_1{+}N_2$ 之\ \textbf{上界} —— 三式皆不给}}$$
$$\boxed{\text{③ 三阶项对 }E\ \text{之下界贡献恰为 }0\ \Longrightarrow\ \text{按判据}\ \boxed{\textbf{STOP}}}$$

## §1 三条恒等式之实测（**120-code，$n{=}10$，$K{=}120$ ✓✓**）

| 式 | 实测 | 判定 |
|---|---|---|
| (1) $\sum_x\delta(x)=11M-2^n$ | $296=11\cdot120-1024$ | ✓ |
| (2a) $\sum_x\binom{a(x)}2=2(N_1{+}N_2)$ | $398=2(50{+}149)$ | ✓ |
| (2b) $E+\sum_x\delta(x)^2=4(N_1{+}N_2)$ | $796=4\cdot199$ | ✓ |
| (3) $\sum_x\binom{a(x)}3=\big(\sum_x\delta^3-\sum_x\delta\big)/6$ | $138=138$ | ✓ |

$$\text{（$N_1{=}50$，$N_2{=}149$（无序）；$\sum\delta^2{=}500$；$\delta$ 分布 $\{0{:}801,1{:}172,2{:}36,3{:}8,4{:}7\}$）}$$
$$\therefore\ \boxed{\text{三式皆为\ \textbf{恒等式}（由构型完全决定），非不等式}}\ ⚠️$$

## §2 ★ 缺口精确定位（**本档核心 ✓✓**）

$$\text{设 }M{=}106\ (\Rightarrow E{=}142)。\ \text{由 (2b)}:\ 4(N_1{+}N_2)=E+\sum\delta^2$$
$$\text{又 }\delta\in\mathbb Z_{\ge0}\Longrightarrow \sum\delta^2\ \ge\ \sum\delta\ =\ E\ \Longrightarrow\ \boxed{N_1{+}N_2\ \ge\ E/2\ =\ 71}\quad(\textbf{下界})$$
$$\text{另 Cauchy--Schwarz}:\ \sum\binom{a}{2}\ge\frac{(\sum a)^2/2^n-\sum a}{2}\ \Longrightarrow\ N_1{+}N_2\ge41\ (\text{更弱})$$
$$\therefore\ \boxed{\text{三式合起来只给\ \textbf{下界}；而矛盾需\ \textbf{上界}\ }N_1{+}N_2\le70\ \text{（或}\sum\delta^2\ \text{之上界）}}$$
$$\text{三阶项}:\ \sum\delta^3=E+6\sum\binom{a}{3}\ \text{且}\ \sum\binom a3\ge0\ \Longrightarrow\ \sum\delta^3\ \ge\ E\ \text{（**贡献 }0\text{**）} ✗$$

## §3 ★ 判据执行（**照唐先生之 STOP 条 ✓✓**）

$$\text{判据逐字}:\ "\text{如构造出的高阶不等式最后只得到 }E\ge142\ \text{或更弱，就立即 STOP}"$$
$$\text{实测结论}:\ \text{三式（含三阶）所得之最强结论 ＝ }N_1{+}N_2\ge71\ \text{暨}\ E\ge142\ (\text{＝假设本身})$$
$$\therefore\ \boxed{\textbf{STOP}\ \text{—— 矩堆叠路线（一阶}\to\text{二阶}\to\text{三阶）\ 已于本档关闭}}\ ⚠️✓$$
$$\text{（与既有结论一致}:\ \texttt{EXCESS-2026-09-25}\ \text{已判"首阶 excess 不能区分 }118/119"\text{；}\ S\ \S\ \text{"不得再堆 }\delta\ \text{之矩"}\ ✓）$$

## §4 为何三式不给上界（**机制说明 ✓**）

$$\text{三式之共同结构}:\ \text{左端皆为\ \textbf{构型之函数}（}\delta,a\ \text{给定后完全确定），右端亦然} \Longrightarrow \text{对任何具体构型皆\ \textbf{恒成立}}$$
$$\therefore\ \text{它们\ \textbf{限制构型空间}（约束 }(\delta,N)\ \text{之一致性），但\ \textbf{不产生} }E\ \text{之下界不等式}$$
$$\text{故要 }E\ge153,\ \text{必须引入\ \textbf{独立不等式}（如 Zhang 之 pair covering inequality）},\ \text{而非矩之堆叠}\ ✓$$

## §5 下一代攻击点（**据本档诊断 ✓**）

$$\boxed{\text{真正缺口} ＝ \textbf{上界}:\ N_1{+}N_2\le70\ (\text{或}\ \sum\delta^2\ \text{之上界）},\ \text{即\ \textbf{"散布性 vs 重叠"} 之不等式}}$$
$$\text{此恰为 Zhang 1991「pair covering inequalities」（}$\to105$\text{）与 BÖW（}$\to107$\text{）所提供之类型} ✓$$
$$\therefore\ \text{下一步（唯一有据）}:\ \textbf{取 Zhang 1991 pair-covering inequality 之原式},\ \text{观其如何约束}\ (N_1,N_2)\ \text{与 face 占用}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "矩恒等式实测" "上界缺口" "STOP触发"
技术词 矩恒等式实测  命中文件数=0    ::
技术词 上界缺口     命中文件数=0    ::
技术词 STOP触发     命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **本地实测**（120-code，三式全通过）＋ 判据执行 ＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** Zhang／BÖW 公式 ✗；**不主张** $E\ge153$ 可得 ✗（V290）
