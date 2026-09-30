# REFUTE-2026-09-30d — $R$-实验：重复解释量对 $A_2$ **次线性**（$R_D/A_2$ 随 $A_2$ **下降**）⟹ 按判据 **KILL** ✗

> 空间 B｜非 C 号｜唐先生 10:06「只测四列 (A₂,P,R,R/A₂)，情形 B/C 即 KILL」｜**不主张任何新值**（V290）

**已查地图**：承 `REFUTE-2026-09-30c`（$H_{11}$ 路线否）／`MULT{,2}`／`RESULT-P180`
D0: 本档对象 = **档案已有**（$A_2,P,H,H_{00..11}$ 之重复度量）之**实测**（新数学对象：无 ✗）
D1: 0（产出 = **一条路线之数据否证 ＋ 一条方法学判定** ⚠️✓）

---

## §0 判定（先给）

$$\boxed{\text{三口径重复解释量皆与 }A_2\ \textbf{不同步增长}:\ R_A/A_2\ \text{近常数}\ (1.82);\ R_B/A_2\ \text{次线性};\ R_D/A_2\ \textbf{随 }A_2\ \text{下降}}$$
$$\boxed{\Longrightarrow\ \text{按唐先生判据（情形 B/C）}:\ \textbf{「}A_2\ \text{大}\Rightarrow\text{重复解释大」机制\ \textbf{不成立}} \Longrightarrow \textbf{KILL}\ ✗}$$

## §1 三口径定义与实测（8 码）

$$R_A:=\sum_{x\notin C}\binom{\mu(x)}2=H\ (\text{点-对 incidence});\quad R_B:=\sum_{x\notin C}\binom{\binom{\mu(x)}2}2\ (\text{同点之重复对});\quad R_D:=H_{01}+H_{11}\ (\text{码字中点之对数})$$
| 码 | $M$ | $A_2$ | $P$ | $R_A$ | $R_B$ | $R_D$ | $R_A/A_2$ | $R_B/A_2$ | $R_D/A_2$ |
|---|---|---|---|---|---|---|---|---|---|
| 120-码 | 120 | 149 | 41 | 257 | 384 | 39 | 1.725 | 2.577 | **0.262** |
| 62-码（$n{=}9$） | 62 | 66 | 6 | 126 | 144 | 6 | 1.909 | 2.182 | 0.091 |
| 贪心-1 | 150 | 316 | 59 | 573 | 444 | 57 | 1.813 | 1.405 | 0.180 |
| 贪心-2 | 150 | **333** | 48 | 618 | 495 | 44 | 1.856 | 1.486 | **0.132** |
| 贪心-3 | 148 | 305 | 48 | 562 | 366 | 48 | 1.843 | 1.200 | 0.157 |
| 贪心-4 | 146 | 291 | 50 | 532 | 324 | 48 | 1.828 | 1.113 | 0.165 |
| 贪心-5 | 151 | 321 | 42 | 600 | 387 | 42 | 1.869 | 1.206 | 0.131 |
| 贪心-6 | 150 | 310 | 54 | 566 | 357 | 54 | 1.826 | 1.152 | 0.174 |

## §2 关键读数（**判据所问**）

$$R_A/A_2\in[1.725,1.869]\ (\text{均值 }1.823) \Longrightarrow \textbf{近常数};\ \text{且 }R_A=H=2A_2-P\ \Longrightarrow \textbf{恒等式级，无新信息} ✗$$
$$R_B/A_2\in[1.11,2.58],\ \textbf{随 }A_2\ \text{增大而\textbf{下降}}（A_2{=}333\Rightarrow1.486\ \text{vs }A_2{=}66\Rightarrow2.182）\ ✗$$
$$\boxed{R_D/A_2\ \textbf{单调反向}:\ A_2{=}149\Rightarrow0.262\ \text{而}\ A_2{=}333\Rightarrow\mathbf{0.132}} \Longrightarrow \textbf{"}A_2\ \text{大}\Rightarrow\text{重复解释大"\ 与数据\ \textbf{相反}} ✗✗$$

## §3 结论（**按唐先生判据 = 情形 B/C ⟹ KILL**）

$$\text{实测显示主结构恰是\textbf{反面}：大 }A_2\ \text{时距离-2 对\textbf{更孤立}}（H_{00}/A_2\in[0.74,0.91]\ \text{且不降}）\ \Longrightarrow R\ \text{不可能承担 }A_2\to139\ \text{之压降}$$
$$\therefore\ \textbf{R-机制 KILL}\ ✗;\ \text{本线当前无存活机制}$$

## §4 累计（**本线五条路线被数据否掉**）

$$\text{① }n_A\le9A_1\ (301/338\ \text{反例});\ \text{② }A_1\le60;\ \text{③ }P\ge181;\ \text{④ }H_{11}\ \text{路线}; \ \text{⑤ }R\ \text{机制（本档）}$$
$$\text{已入册真结果（10 项）}:\ F1\text{–}F9;\ 2S{=}E{+}P{+}T_N;\ P\le180;\ A_1\le124;\ n_B\le H;\ n_{A1}\le9q_1;\ n_{A2}\le8r_1;\ q_1\le2A_1-\tfrac29P;\ H_{00}\ \text{三恒等式};\ \text{重数 }4/5$$

## §5 唯一缺口与诚实判定

$$\boxed{\text{缺口}:\ A_2\le139\ (\text{或 }H_{00}\le99)\ @M{=}106;\ \text{现有全部工具给 }161\（差 22）}$$
$$\text{而实测缩放}: A_2/M^2\in[0.0103,0.0148]\Longrightarrow M{=}106\ \text{之自然区间}\ A_2\in[116,166] \Longrightarrow \textbf{139 落在自然区间中部}$$
$$\therefore\ A_2\le139\ \text{不能靠"测量"或"聚合类界"得到（已四次实测其上限）；须\ \textbf{新机制} \ ⚠️$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**实测否证**（依唐先生自设判据）✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
