# DERIVE-2026-09-29c — 直推：**恒等式 $E+\Sigma\delta^2=4(A_1{+}A_2)$ 已双码验证 ✓✓**；$M{=}106$ 之 mod 4 同余**成立但可满足**；链中**两步须更正**

> 空间 B｜非 C 号｜唐先生 23:49「直接推」｜**不主张任何新值**（V290）

**已查地图**：`RESULT-f`（$r_q{=}2t_q$ 定义与约定）／`DERIVE-2026-09-29b`（$s_x$、局部恒等式）／`AUDIT-29j`（旧 parity 链断裂）／本会话 `INV3`
D0: 本档对象 = **档案已有**（$\mu,\delta,A_i,r_x,s_x$）之**直接推导**（新数学对象：无 ✗）
D1: 0（产出 = **一条恒等式之双码验证 ＋ 一条 mod 4 同余 ＋ 两处更正** ⚠️✓）

---

## §0 精确定义（**照唐先生要求，先取定义，不凭记忆**）

$$\textbf{(1) RESULT-f（}\texttt{ASSETS-REGISTRY L3846–3848}\text{）}:\quad r_q=|N_1^{\mathrm{op}}(q)\cap L|=2t_q,\qquad t_q=|\{p\in P:\ d(p,q)=2\}|$$
$$\qquad\textbf{开邻域 }40/40\ ✓✓;\ \text{闭邻域 }3/40\ ✗;\quad |L|=9|P|=243;\quad \texttt{滑位提醒}:\ 2E\neq\Sigma_q r_q\ \text{（}R=\Sigma r_q\ \text{为 incidence）}$$
$$\textbf{(2) DERIVE-107-…b}:\ s_x:=\#\{d\in C\cap S_2(x):\ d(c,d)=1\}\ (\text{x 私有点，owner }c);\quad \Sigma_{y\in N(x)\setminus\{c\}}\bigl(\mu(y)-1\bigr)=2r_x-s_x-9\ (\text{746/746 ✓✓})$$
$$\textbf{(3) 本档（μ-框架）}:\ \delta(x):=\mu(x)-1\ge0;\quad E:=\Sigma_x\delta(x)=(n{+}1)M-2^n;\quad N_{\le2}=A_1+A_2$$

## §1 恒等式 $E+\Sigma\delta^2=4N_{\le2}$（**实跑双码 ✓✓**）

$$\text{推导}:\ \Sigma_x\mu^2=\Sigma_{c,c'}|N[c]\cap N[c']|=(n{+}1)M+4N_{\le2}\quad(|N[c]\cap N[c']|=2\iff1\le d\le2)$$
$$\qquad\text{又}\ \Sigma\mu^2=\Sigma(\delta+1)^2=\Sigma\delta^2+2E+2^n \Longrightarrow \boxed{E+\Sigma\delta^2=4N_{\le2}}\ ✓$$
| 码 | $E$ | $\Sigma\delta^2$ | $4N_{\le2}$ | 判定 |
|---|---|---|---|---|
| 62-码（$n{=}9$） | 108 | 184 | $4\cdot73{=}292$ | $292{=}292$ ✓✓ |
| 120-码（$n{=}10$） | 296 | 500 | $4\cdot199{=}796$ | $796{=}796$ ✓✓ |

## §2 $M{=}106$ 之 mod 4（**成立，但可满足 ⟹ 无矛盾** ✗）

$$E+\Sigma\delta^2=4N_{\le2}\Longrightarrow \Sigma\delta^2\equiv -E\equiv -\bigl((n{+}1)M-2^n\bigr)\equiv M\ (\mathrm{mod}\ 4)\quad(n{=}10)$$
$$\textbf{实测一致性}:\ 62\text{-码}\ \Sigma\delta^2{=}184\equiv0,\ -E{=}-108\equiv0\ ✓;\quad 120\text{-码}\ 500\equiv0,\ -296\equiv0\ ✓$$
$$M=106:\ \boxed{\Sigma\delta^2\equiv2\ (\mathrm{mod}\ 4)}\ \iff\ \#\{x:\mu(x)\ \text{偶}\}\equiv2\ (\mathrm{mod}\ 4)$$
$$\Longrightarrow\ \textbf{可满足}（如恰 2 个偶 }\mu\text{ 点）\ ✗;\ \text{且它\ \textbf{已被}恒等式＋整数性蕴含} \Longrightarrow \textbf{零新信息}$$
$$\text{档案早已定性}:\ \text{该类式"}\textbf{是恒等式（非约束）}\text{"（}ASSETS\text{-}L3613\text{）} \Longrightarrow \textbf{恒等式不产生严格性} \therefore \text{此路不出 }107\ ✗$$

## §3 **两处更正**（按唐先生"不偷换符号"之要求）

$$\textbf{(a) "}N_1=71\text{"} ✗:\ \text{档案 }N_1,N_2\ \text{即 }A_1,A_2; \text{而有据者为 }\boxed{N_1+N_2\ge\Sigma\delta/2=71}\ (\textbf{下界，非等式});\ \text{旧"}\Sigma e/2{=}71\text{"链已被 }AUDIT\text{-}29j\ \text{证断}\ ✗$$
$$\textbf{(b) "}E=2R-S-9M\text{"} ✗:\ \text{档案恒等式为}\ \Sigma_{y\in N(x)\setminus\{c\}}(\mu(y)-1)=2r_x-s_x-9\ \text{—— 对\ \textbf{私有点 }x\ \text{求和};\ \text{其 LHS 是\ \textbf{邻点} excess 之和（非 }\mu(x)-1\text{），且不可"对所有码字 }x\text{ 求和"}\ ✗$$
$$\textbf{(c) 框架警示}:\ r_q,t_q\ \text{属\ \textbf{P/Q 框架}（}|L|{=}9|P|{=}243\text{）};\ \text{与 μ-框架之 }E,N_{\le2}\ \textbf{不同层} \Longrightarrow \text{直接混用即唐先生所戒之"偷换符号"} ⚠️$$

## §4 判定

$$\boxed{\text{本轮直推获得: 一条双码验证之恒等式 ＋ 一条 mod 4 同余; 但\ \textbf{无矛盾} ⟹ 不出 }107}$$
$$\qquad\text{根因（与 }AUDIT\text{-}P07\ \S1\ \text{一致）}:\ \text{此路所有可用式子皆\ \textbf{恒等式}，而\ \textbf{恒等式不能产生严格性}}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "mod4攻击" "恒等式非约束"
技术词 mod4攻击     命中文件数=0    ::
技术词 恒等式非约束  命中文件数=0    ::
```
$$\textbf{本档新增} = \varnothing\ (\text{二词为通用描述，不计});\quad \textbf{档案已有} = \{r_q{=}2t_q,\ s_x,\ \text{球 excess}\}\ ✓$$

## §6 边界（硬 ✓）

- **不主张**任何新值；两处更正为**按定义**执行 ✓；未取论文原文（R16–17）✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
