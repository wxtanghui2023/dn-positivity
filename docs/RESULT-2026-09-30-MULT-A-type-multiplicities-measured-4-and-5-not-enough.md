# RESULT-2026-09-30-MULT — A 型重数实测：$r_{A1}{=}4$、$r_{A2}{=}5$；代回全局链**不足**（差 1）

> 空间 B｜非 C 号｜唐先生 00:06「压这条线，但不要预设它够强」｜**不主张任何新值**（V290）

**已查地图**：承 `REFUTE-2026-09-30`／`REFUTE-2026-09-30b`（两次反例）／`DEFS-2026-09-29`
D0: 本档对象 = **档案已有**（$\delta,a_1,a_2,H$ 之局部结构）之**重数实测**（新数学对象：无 ✗）
D1: 0（产出 = **两条重数分布 ＋ 一条"不够"之定量判定** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{r_{A1}=4\ (\text{实测最大重数}),\quad r_{A2}=5;\qquad H_{00}=110,\ H=298\ (2H_{00}\le H\ ✓)}$$
$$\boxed{\text{代回全局链：**无矛盾**}\ ✗\ ——\ \text{该路线需要 }r_{A2}\le4,\ \text{实测 }5\ (\text{差 1})}$$

## §1 A 型之正确二子情形（**本档建图实测**，120-码）

$$\text{A 型 }v\ (v\notin C,\ a_1{=}1,\ a_2{=}5,\ \delta{=}1);\ \text{平移 }v{=}0,\ \text{唯一距离-1 码字 }c{=}e_1$$
$$\text{5 个距离-2 码字}\ \leftrightarrow\ \{1..10\}\ \text{上 5 条边};\ \mu(e_i){=}\deg(i)\ (i{\ge}2),\ \mu(e_1){=}1{+}\deg(1)$$
$$\delta(0)=1\ (\text{自动})\ \text{＋各点 excess}{\ge}0 \Longrightarrow \textbf{恰两支}:$$
$$\textbf{A1}:\ \deg(1){=}1,\ \deg(i){=}1\ \forall i{\ge}2 \Longrightarrow \text{10 顶点完美匹配};\ e(c){=}1;\ \textbf{收费对象＝距离-1 边}\ \{c,d\}$$
$$\textbf{A2}:\ \deg(1){=}0,\ \text{恰一 }j{\ge}2\ \text{有}\ \deg(j){=}2,\ \text{余 8 点}\ \deg{=}1 \Longrightarrow \text{度列}\ (2,1^8);\ e(c){=}0;\ \textbf{收费对象＝共享对}$$
$$\qquad\text{A2 之共享对}\ \{e_j{+}e_a,\ e_j{+}e_b\}:\ \text{两中点 } e_j,\ e_a{+}e_b\ \textbf{皆非码}\ ✓\ (\text{受 }a_2{=}5\ \text{与 }a_1{=}1\ \text{双约束}) \Longrightarrow \textbf{落 }H_{00}\ ✓$$

## §2 重数实测（**唐先生所要求的"真实重数引理"**）

| 型 | 点数（120-码） | 映射到之不同对象数 | 重数分布 | **最大重数** |
|---|---|---|---|---|
| **A1** | 37 | 16 条距离-1 边 | $\{1{:}6,\ 2{:}2,\ 3{:}5,\ 4{:}3\}$ | $\mathbf4$ |
| **A2** | 301 | 86 个距离-2 对 | $\{1{:}6,\ 2{:}12,\ 3{:}25,\ 4{:}19,\ 5{:}24\}$ | $\mathbf5$ |

$$H_{00}=\#\{\text{距离-2 码字对：两中点皆非码}\}=\mathbf{110};\qquad H=\sum_{x\notin C}\binom{\mu}2=298;\qquad 2H_{00}=220\le H\ ✓$$
$$\text{注：}A_1\ \text{侧重数 }\le4\ (\text{远小于此前假设的 }9);\qquad n_{A2}/H_{00}=2.74$$

## §3 代回全局链：**不足** ✗

$$\text{正确收费}:\quad n_1\ \le\ r_{A1}A_1+r_{A2}H_{00}+2A_2\ \le\ 4A_1+5H_{00}+2A_2,\qquad H_{00}\le\tfrac H2=A_2-\tfrac P2\le A_2$$
$$\therefore\ n_1\ \le\ 4A_1+7A_2 \Longrightarrow \sum_{v\notin C}\delta\ \ge\ 2754-2n_1\ \ge\ 2754-8A_1-14A_2$$
$$\text{与恒等式}\ \sum_{v\notin C}\delta=1562-4A_1-4A_2\ \text{联立}:\quad 1192\ \le\ 4A_1+10A_2\ \Longrightarrow\ \textbf{可满足}\ ✗\ (\text{如 }A_2\ \text{大})$$
$$\boxed{\text{要得矛盾需}\ 1192>4A_1+2r_{A2}H_{00};\ \text{以 }A_1{\approx}50,\ H_{00}{\approx}110\ \text{计}:\ r_{A2}\le\mathbf4\ \text{才够，而实测 }\mathbf5\ ✗}$$

## §4 判定与去向

$$\therefore\ \text{A2 经 }H_{00}\ \text{收费之路线\ \textbf{定量上不足}}（差 1）;\ \text{且 }H_{00}\le A_2\ \text{之代换使 }A_2\ \text{自由度吞掉了矛盾}\ ✗$$
$$\text{可选之补救（未验，供唐先生定）}:\ ①\ \text{把 }H_{00}\ \text{与 }A_2\ \text{更紧耦联（}H_{00}\le A_2-\text{缺陷项}）;\ ②\ \text{把 A2 与 A1 合并收费（同一结构不同口径）};\ ③\ \text{放弃 }\delta{=}1\ \text{层，回到 INV2 之强化}$$
$$\textbf{纪律}:\ \text{本档不由"想要结论"而虚报}; 重数 4/5 为实测，非推测 ✓$$

## §5 边界（硬 ✓）

- **不主张**任何新值；本档为**重数实测＋定量判定**（路线不足）✗
- 未取论文原文（R16–17）✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
