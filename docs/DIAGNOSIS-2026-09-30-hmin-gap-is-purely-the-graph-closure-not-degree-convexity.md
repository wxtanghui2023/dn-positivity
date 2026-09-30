# DIAGNOSIS-2026-09-30 — $\Delta$ 的来源 **纯是图闭合**（非度数凸性）：三级分解 $(a)\approx(b)\ll(c)$ ✓✓
已查地图：未覆盖（关键词: 图闭合|h_min|三角形重叠|判定式）—— 可开档，首行须照抄本行
D0: 本档对象 = 方法/诊断类（无档案同型；非已知 RH 对象重命名）
D1: 0


> 空间 B｜非 C 号｜唐先生 22:36 令（克制解释；找 $\Delta$ 的图论原因）｜**不主张任何新值**（V290）｜**不称公式，只称经验结构** ✓

---

## §0 **三级分解（$r{=}8$）**

| $m$ | (a) Jensen $J$ | (b) 超图 min（无闭合） | (c) 图 min（有闭合） |
|---|---|---|---|
| 10 | 2 | **3** | **13**（精确 ✓） |
| 13 | 11 | **11** | **23**（精确 ✓） |
| 14 | 14 | **14** | $\ge$22 |
| 16 | 20 | **20** | $\ge$28 |
| 18 | 26 | TL | $\ge$34 |

$$\textbf{(a)}\ \text{edge-load 凸性下界};\quad \textbf{(b)}\ \min\sum_e\binom{t_e}2\ \text{s.t.}\ \sum_Ty_T=m\ (\textbf{\text{任意三元组，无闭合}});\quad \textbf{(c)}\ \textbf{\text{加图闭合}}\ (y_T\Longleftrightarrow\text{三边俱全})$$

## §1 **诊断（本档核心 ✓✓）**

$$\boxed{(a)\approx(b)}:\ \text{Jensen 在\ \textbf{超图世界几乎可达}} ✓\ (\text{仅 }m{=}10\ \text{差 }1)\ \Longrightarrow \text{度数凸性侧无 $\Delta$} ✗$$
$$\boxed{(b)\ll(c)}:\ (3\ \text{vs}\ 13),\ (11\ \text{vs}\ 23),\ (14\ \text{vs}\ \ge22),\ (20\ \text{vs}\ \ge28) \Longrightarrow \textbf{\text{整个 $\Delta$ 来自\ \textbf{图闭合}}}} ✓✓$$
$$\therefore\ \text{唐先生原假设"度数凸性＋可画性联合修正"须\ \textbf{修正为}}:\ \Delta=\text{闭合代价（graphicality cost）}\ ✗✓$$

## §2 **量级与经验对应（克制 ✓）**

$$(c)-(b)\approx\mathbf{8}\text{--}\mathbf{12}\ = \text{观测之 }+8\text{--}+12 ✓ \Longrightarrow \textbf{\text{经验"+8"＝闭合代价之表现}} ✓\ (\text{不提为公式} ✗)$$
$$\text{且 }m{=}13\ \text{处 }J{+}8{=}19<23 \Longrightarrow \text{"}J{+}8\ \text{精确"已被排除} ✓\ (\text{与唐先生判断一致} ✓)$$

## §3 **改向后的可证目标（供下一步）**

$$\textbf{目标}:\ \forall\ \text{图 }G\ (r\ \text{顶点，每边至少属一个三角形，恰 }m\ \text{个三角形}):\quad \sum_{e}\binom{t_e}2\ \ge\ J(r,m)+\Delta(r,m)$$
$$\textbf{可用之局部关系（闭合特有 ✓）}:\ \tau_v=|E(N(v))|\ (\text{顶点 }v\ \text{处三角形数＝其邻域图之边数});\quad \sum_v\tau_v=3m;\quad \tau_v\le\binom{d_v}2;\quad 2h=\sum_{vw\in E}\binom{|N(v)\cap N(w)|}2 ✓$$
$$\Longrightarrow\ \textbf{\text{须证之核心}}:\ \text{闭合强迫"邻域图之边数分布"远离凸性最优分布} ✓\ (\text{研究级} ⚠️)$$

## §4 **r=9 之检验（判据按唐先生）**

$$\text{仅当 }r{=}9\ \text{也出现同类可解释整数修正时，方可升格为候选通用机制} ✓\ (\text{否则只记经验} ✓)$$

## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{三级皆为实测/证书（}b\ \text{为 ILP 精确，}c\ \text{之 }\ge\ \text{自 INFEASIBLE）}✓;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §6 【技术词回查】

```
技术词 闭合代价     命中文件数=1    :: 本档
技术词 graphicality  命中文件数=0    :: 
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{通用词（不计）}：\text{“诊断／三级”裸词} ✓$$

---

## §7 **更正（2026-09-30 22:46 自查 ⚠️）："+8" 是探针步长假象** ✗

$$\text{探针步长}=1,2,4,8,8,\dots \Longrightarrow \text{最后被测之不可行点\ \textbf{恒为} }J{+}7 \Longrightarrow \text{认证下界\ \textbf{恒为} }J{+}8\ ✗$$
$$\therefore\ \textbf{\text{§2 之"量级 }8\text{--}12\ \text{＝观测 }+8\text{--}+12\text{"一句\ \textbf{撤回}} ✗;\ \text{"+8 是闭合代价之表现"\ \textbf{撤回}} ✗$$
$$\text{（}\S1\ \text{之诊断\ }(a)\approx(b)\ll(c)\ \textbf{\text{不受影响}} ✓\ ——\ \text{其三项皆独立计算，不涉探针机制} ✓)$$
$$\text{新事实}:\ \text{认证下界之\ \textbf{真实偏移未知但} }\ge8;\ \text{且 }m{=}21,22\ \text{处偏移 }\ge24/\ge16 \Longrightarrow \text{偏移\ \textbf{随 }m\ \text{变化}} ✓$$
