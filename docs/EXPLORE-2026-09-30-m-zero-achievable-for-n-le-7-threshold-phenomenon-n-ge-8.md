# EXPLORE-2026-09-30-m0 — **$m=0$ 在 $n\le7$ 可达**（弱靶非通用真理）；但 **$n\ge8$ 出现阈值现象**（$n{=}8$: $\ge0.106$；$n{=}9$: $\ge0.67$）

> 空间 B｜非 C 号｜唐先生 10:10「下一刀＝证 $m\ge c(2^n{-}M)$」｜**不主张任何新值**（V290）
> 时间：2026-09-30 11:2x

**已查地图**：承 `ANALYSIS-INV2`／`AUDIT-29j`（$m$ 之上界向）／`AUDIT-zj`（类级标定）
D0: 本档对象 = **档案已有**（$m$、$a_1{+}a_2$ 层）之**小 $n$ 最小化搜索**（新数学对象：无 ✗）
D1: 0（产出 = **一条通用性否证 ＋ 一条阈值现象之实测记录** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\textbf{① }m=0\ \textbf{在 }n\in\{5,6,7\}\ \textbf{可达}\ (m/(2^n{-}M)=0.000) \Longrightarrow \text{"}m\ge c(2^n{-}M),\ c>0\ \text{通用"}\ \textbf{为假}} ✗}$$
$$\boxed{\textbf{② 但 }n\ge8\ \textbf{出现阈值现象}:\ n{=}8\Rightarrow m/(2^n{-}M)\ge\mathbf{0.106};\quad n{=}9\Rightarrow\ge\mathbf{0.667}\ (\text{样本内最小})}$$
$$\boxed{\textbf{③ 故 弱靶 } "m\ge46\ @(n{=}10,M{=}106)"\ \text{不能被\ \textbf{通用论证} 得到，须\ \textbf{n 专属/阈值型} 论证} \ ⚠️}$$

## §1 小 $n$ 最小化搜索（实跑，每 $n$ 6 次独立起点 ＋ 局部最小化）

| $n$ | $M$ | $m_{\min}$ | $m/(2^n{-}M)$ |
|---|---|---|---|
| 5 | 8 | **0** | **0.000** |
| 6 | 14–16 | **0** | **0.000** |
| 7 | 16, 19, 22 | **0** | **0.000** |
| **8** | 38–44 | 23–90 | **0.106–0.425** |
| **9** | 77–82 | 288–328 | **0.667–0.761** |

$$\therefore\ \text{存在 }n\le7\ \text{之覆盖码使\ \textbf{所有非码字点皆 }a_1{+}a_2=6\ (\delta{=}1)}\ \Longrightarrow\ m=0\ ✓\ (\text{与 }INV2\ \text{之下界相容})$$
$$\qquad\text{（注：}$n{=}7$ 之完美码反而有 }m>0\ \text{（}a_1{+}a_2{=}7\text{）};\ m{=}0\ \text{由\ \textbf{非完美} 码（含冗余词）达到} ✓）$$

## §2 与本题之关系（**判定的边界**）

$$\text{本题只需 }n{=}10,M{=}106\ \text{处 }m\ge46 \Longrightarrow n\le7\ \text{之反例\ \textbf{不构成反驳}} ✓$$
$$\text{但亦表明：}\ \text{任何仅依赖 }(\text{INV2}+\text{全局恒等式}+\text{一般几何})\ \text{之论证皆不能得结论（否则 }n\le7\ \text{亦成立）} ✗$$
$$\therefore\ \text{弱靶之证明必须用到\ \textbf{“}n\ \text{大”之特殊性（阈值 }\ge8\text{）}\ \text{或 }n{=}10\ \text{之专属几何} } ⚠️$$

## §3 新增之**可攻目标**（本档最有价值之产出 ✓）

$$\boxed{\textbf{阈值猜想}:\ \exists\ c>0,\ n_0\ \text{使}\ n\ge n_0\Rightarrow m\ \ge\ c\,(2^n-M)\ \text{（对一切覆盖码）}}$$
$$\text{实测支持}:\ n{=}8\Rightarrow c\ge0.106;\ n{=}9\Rightarrow c\ge0.667;\ \text{而}\ n\le7\Rightarrow c=0\ \text{（反例）} \Longrightarrow \text{阈值}\ n_0\in\{8\}\ \text{附近}$$
$$\text{若可得 }c\ \text{与 }n_0\ \text{之证明且 }c\ \text{在 }n{=}10\ \text{足够大}（c\cdot918>322-2N_{\le2}\approx42\Rightarrow c>0.046）\ \Longrightarrow\ \textbf{闭合} ✓$$
$$\text{此目标之优点}:\ \text{①\ \textbf{与 }n\ \text{有关}（非又一个总量）};\ \text{②\ 已有 }n{=}8,9\ \text{之数值支撑};\ \text{③\ 可先做 }n{=}8\ \text{（最小反例之外）作为突破口} \ ⚠️$$

## §4 建议之后续（**不依赖本线存活** ✓）

$$\textbf{(甲)}\ \text{攻 }n{=}8\ \text{之阈值}:\ \text{证 }m\ge23\ \text{对一切 }(8,\ M{\le}44)\ \text{覆盖码};\ \text{若成，方法或可推至 }n{=}9,10 ✓$$
$$\textbf{(乙)}\ \text{若 }n{=}8\ \text{都不可得} \Longrightarrow \textbf{本线（}m\ \text{下界）整体记 CLOSED-不足};\ \text{转入归档} ✓$$
$$\textbf{(丙)}\ \text{归档时务必写入}:\ \text{唯一缺口之} \textbf{两种等价形式}（A_2\le139\ \text{／}\ m\ge44-2A_1）\ ＋\ \textbf{六条已否路线} ＋\ \textbf{阈值现象}（$n\le7$ 反例）$$
$$\qquad\Longrightarrow\ \text{使后续者不必重走，并能立刻从"阈值"这一新角度切入} ✓$$

## §5 边界（硬 ✓）

- **不主张**任何新值；本档为**计算探索 ＋ 一条新猜想之登记** ✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
