# REFUTE-2026-09-30c — $H_{11}$ 路线**被数据否掉**（真实码 $H_{11}\in\{0,2,4\}$，需 $\gtrsim100$）；缺口收敛为**一条 $A_2$ 上界**

> 空间 B｜非 C 号｜唐先生 10:03「下一主攻点＝$H_{00}\le99\Rightarrow H_{11}$ 结构性下界」｜**不主张任何新值**（V290）

**已查地图**：承 `VERIFY-2026-09-30-2nd`／`RESULT-P180`／`MULT{,2}`／`RESULT-M106-DLA`
D0: 本档对象 = **档案已有**（$H_{00},H_{01},H_{11},A_2,P$）之**实测范围**（新数学对象：无 ✗）
D1: 0（产出 = **一条路线的数据否证 ＋ 一条缺口之收敛** ⚠️✓）

---

## §0 判定（先给）

$$\boxed{\text{路线 }"H_{00}\le99\Rightarrow H_{11}\ge g(A_1,P)"\ \textbf{被实测否掉}\ ✗:\quad \text{真实码 }H_{11}\in\{0,2,4\}\ll100}$$
$$\boxed{\text{缺口收敛}:\ \text{闭合成败}\iff A_2\le\mathbf{139}\ (\text{或}\ H_{00}\le99)\ @M{=}106;\ \text{而我方全部工具只给 }A_2\le161\ ✗\ (\text{差 22})}$$

## §1 实测（8 个真实码）

| 码 | $M$ | $A_1$ | $A_2$ | $P$ | $H$ | $H_{00}$ | $H_{01}$ | $\mathbf{H_{11}}$ | $H_{00}/A_2$ |
|---|---|---|---|---|---|---|---|---|---|
| 120-码 | 120 | 50 | 149 | 41 | 257 | 110 | 37 | **2** | 0.738 |
| 62-码（$n{=}9$ 最优） | 62 | 7 | 66 | 6 | 126 | 60 | 6 | **0** | 0.909 |
| 贪心-1 | 150 | 83 | 316 | 59 | 573 | 259 | 55 | **2** | 0.820 |
| 贪心-2 | 150 | 67 | 333 | 48 | 618 | 289 | 40 | **4** | 0.868 |
| 贪心-3 | 148 | 70 | 305 | 48 | 562 | 257 | 48 | **0** | 0.843 |
| 贪心-4 | 146 | 71 | 291 | 50 | 532 | 243 | 46 | **2** | 0.835 |
| 贪心-5 | 151 | 71 | 321 | 42 | 600 | 279 | 42 | **0** | 0.869 |
| 贪心-6 | 150 | 81 | 310 | 54 | 566 | 256 | 54 | **0** | 0.826 |

$$\therefore\ H_{11}\ \textbf{恒 ≤4}\ (\text{多数为 0});\ \text{而路线所需}\ g>28+A_1+\tfrac P2\ (\text{以 }A_1{=}50,P{=}40\Rightarrow g\gtrsim98)\ ✗✗$$

## §2 路线之代数复核（**代数本身对 ✓，量级不可能** ✗）

$$\text{由 }H_{00}=A_2-P+H_{11}:\quad H_{00}\le99\iff A_2\le99+P-H_{11}\ ✓;\quad H=2A_2-P\Longrightarrow H\le198+P-2H_{11}\ ✓$$
$$\text{又 }H=(142-2A_1)+T_N\Longrightarrow T_N+2H_{11}\le56+2A_1+P\ ✓;$$
$$\text{若 }H_{11}\ge g,\ \text{则 }A_2\le99+P-g;\ \text{与 }S=71+\tfrac{P+T_N}2\ \text{联立需 }g>28+A_1+\tfrac P2\ \Longrightarrow\ \textbf{需 }H_{11}\gtrsim100\ ✗\ (\text{实测 }\le4)$$

## §3 由实测推出的**两条经验规律**（供瞄准用，非定理 ⚠️）

$$H_{00}/A_2\in[0.74,\ 0.91]\ (\text{8 样本，皆 }>0.73) \Longrightarrow \text{若 }M{=}106\ \text{沿用}\ \approx0.80,\ \text{则 }A_2\gtrsim124$$
$$H_{11}/A_2\le0.027\ (\text{恒近零}) \Longrightarrow \textbf{任何依赖 }H_{11}\ \text{有效的路线皆不可行} ✗$$

## §4 缺口之**最终收敛形式**

$$\textbf{闭合所需（二选一）}:\quad \text{(a)}\ \boxed{A_2\le139}\quad\text{或}\quad\text{(b)}\ \boxed{H_{00}\le99}$$
$$\text{现有工具给出}:\ \max A_2=161\ (\text{INV2 卡住})\ ✗;\ \text{Delsarte/Krawtchouk/层覆盖/恒等式族皆不改善}$$
$$\text{实测比 }H_{00}/A_2\in[0.74,0.91]\Longrightarrow \text{(b) 等价于 }A_2\lesssim118\text{–}134\ (\text{视比值}) \Longrightarrow \textbf{与 (a) 同量级} ⚠️$$

## §5 本轮累计之**被数据否掉的路线**（不可再投入 ✗）

$$\text{① }n_A\le9A_1\ (301/338\ \text{反例});\quad \text{② }A_1\le60;\quad \text{③ }P\ge181\ (\text{真实 }P{\approx}41);\quad \text{④ }H_{11}\ \text{路线（本档）};\quad \text{⑤ }"δ{=}1\ \text{层直接收费}"\ \text{各类变体}$$
$$\text{已入册之真结果}:\ F1\text{–}F9,\ 2S{=}E{+}P{+}T_N,\ P\le180,\ A_1\le124,\ n_B\le H,\ n_{A1}\le9q_1,\ n_{A2}\le8r_1,\ q_1\le2A_1-\tfrac29P,\ H_{00}\ \text{三恒等式},\ \text{重数 }4/5$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**实测否证 ＋ 缺口收敛** ✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
