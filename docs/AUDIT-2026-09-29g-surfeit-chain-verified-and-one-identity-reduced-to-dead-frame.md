# AUDIT-2026-09-29g — **唐先生 surfeit 链之逐条核验：一处恒等式须校正；「二阶 excess」\ \textbf{恰等于已证死之框架}；一条约束为假**

> **性质**：**实测核验 ＋ 纠错**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 10:3x ✓
> **唐先生令**：「先把 107 是怎么来的拆出来，完整复现」✓

**已查地图**：接续 `AUDIT-29c`（$N_1{+}N_2$ 框架已证等价球界）／`29f`（复现账）✓

D0: 本档对象 ＝ **档案已有**（$\delta$／excess／$H$／$D_i$——无新数学对象 ✓）
D1: 0（产出＝**一处恒等式校正 ＋ 一处等价性（致命）＋ 一处约束否证** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ 恒等式 (8) 须校正}:\ H+H_C=2U_2\ \text{差}\ \mathbf{2D_1};\ \text{正确为}\ H+\sum_{c}\binom{1+d_1(c)}2=2U_2}$$
$$\boxed{\text{② ★★ 「二阶 excess」}\ \sum_x\binom{\delta(x)}2\ \textbf{恰等于}\ 2(N_1{+}N_2)-E\ ——\textbf{即已证死之框架}}✗$$
$$\boxed{\text{③ ✗ 唐先生约束 ②}\ 78D_2+70D_3+70D_4+60D_5+60D_6\ge559442\ \textbf{在 120-code 上为假}（376{,}822）}$$

## §1 ① 恒等式校正（**✗✓ 实测**）

$$\text{唐先生 (8)}:\ D_2=H+H_C\ (H_C=\sum_{c\in C}\binom{d_1(c)}2)$$
$$\textbf{120-code 实测}:\ H=257,\ H_C(\text{唐})=41,\ 2U_2=\sum_x\binom{\mu(x)}2=398;\quad H+H_C^{\text{唐}}=298\ne398\ \textbf{差}\ \mathbf{100}=2D_1\ ✗$$
$$\textbf{成因}:\ x\in C\ \text{时}\ \mu(x)=1+d_1(x)\ (\text{非}\ d_1),\ \text{故码字贡献为}\ \binom{1+d_1}2=\binom{d_1}2+d_1$$
$$\therefore\ \boxed{H+\sum_{c\in C}\binom{1+d_1(c)}2=2U_2}\quad(\text{实测 }257+141=398\ ✓✓)$$

## §2 ★★ ② 「二阶 excess」之真身（**本档核心，致命 ✗**）

$$\textbf{恒等式（实测 True）}:\quad \sum_x\binom{\delta(x)}2\ =\ 2(N_1{+}N_2)-E\qquad(120\text{-code}:\ 102=2(50{+}149)-296\ ✓)$$
$$\therefore\ \boxed{\text{「二阶 excess」}\ \textbf{逐一等于}\ N_1{+}N_2\ \text{框架 —— 即 }\texttt{AUDIT-29c}\ \text{已证}\ \textbf{等价球界}\ \text{之量}}✗✗$$
$$\text{（}M{=}106:\ 71\le N_1{+}N_2\le411;\ \text{上下界之差 }25M-2310>0\ \Longrightarrow\ \textbf{不可能闭合}）$$
$$\therefore\ \text{唐先生所提「}\sum\binom\delta2\ \text{须足够大}\Rightarrow D_2\ \text{太大}\Rightarrow\text{矛盾}\text{」}\ \textbf{不能成立}——\text{该量与球界同强}$$

## §3 ③ 两条声称约束之实测（**✗ ✓**）

$$\text{①}\ 27D_1+5D_2+D_3+D_4\le22416:\quad \textbf{120-code}\ 4691\le22416\ ✓\ (\text{但极松};\ \text{离界 }17{,}725)$$
$$\text{②}\ 78D_2+70D_3+70D_4+60D_5+60D_6\ge559442:\quad \textbf{120-code}\ \mathbf{376{,}822}<559442\ \textbf{差 }182{,}620\ ✗✗$$
$$\therefore\ \text{约束 ② 作为普适不等式\ \textbf{为假}};\ \text{若它出自某推导，则该推导有误}$$

## §4 附带结构观察（**✓ 新，可用**）

| 码 | $M$ | $E=11M{-}1024$ | $E/M$ | $\sum\binom\delta2$ | 非码字 excess |
|---|---|---|---|---|---|
| 120-code | $120$ | $296$ | $\mathbf{2.47}$ | $102$ | $196$ |
| 贪心 | $148$ | $604$ | $4.08$ | $136$–$150$ | $468$–$488$ |
| 贪心 | $150$ | $626$ | $4.17$ | $136$–$166$ | $476$–$484$ |
| **假设** | $\mathbf{106}$ | $142$ | $\mathbf{1.34}$ | — | $142-2D_1$ |

$$\therefore\ \boxed{E/M\ \text{随 }M\ \text{单调下降};\ M{=}106\ \text{要求}\ E/M{=}1.34\ ——\ \textbf{远低于任何真实码}}✓$$
$$\text{读法}:\ \text{这正是"107 之难"的定量形态}:\ \text{需证明在小 }M\ \text{时 excess 不能如此稀薄}$$

## §5 机制判定（**诚实 ✓**）

$$\text{唐先生所指"surfeit"（Wu--Chen）——本会话\ \textbf{未得其形式}};\ \text{而本次核验表明}:\ \text{若 surfeit 等同于}\ \sum\binom\delta2,\ \text{则}\ \textbf{无效}$$
$$\therefore\ \boxed{\text{若要 }surfeit\ \text{有效，必须是与 }N_1{+}N_2\ \textbf{独立}的\ \text{新量}};\ \text{否则仍落回 `29c` 之死框架}$$
$$\text{可行动作}:\ \text{取 Wu--Chen 2024（arXiv:2203.16901；或 Discrete Math 347 之正文）之 }surfeit\ \text{定义逐字，再判定独立性}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "二阶excess真身" "恒等式校正" "约束否证"
技术词 二阶excess真身  命中文件数=0    ::
技术词 恒等式校正     命中文件数=0    ::
技术词 约束否证      命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code ＋ 4 随机码全量实测** ＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）
