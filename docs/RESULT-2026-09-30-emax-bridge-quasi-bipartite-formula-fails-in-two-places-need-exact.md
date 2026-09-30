# RESULT-2026-09-30 — $e_{\max}$ 桥梁：quasi-bipartite 闭式**在两端失效** ✗（{=}6$ 两处）⟹ $\Delta$ 表仅**指示性**，须用判定式精算 $e_{\max}$

结论: 已查地图：未覆盖（关键词: quasi-bipartite|边数上界|e_max精确）—— 可开档，首行须照抄本行
D0: 本档对象 = 方法/核验类（无档案同型；非已知 RH 对象重命名）
D1: 0

## §0 候选闭式与验证

$$\text{quasi-bipartite}:\ e_{\max}(r,m)\approx\left(\tfrac r2\right)^2+\left\lfloor\tfrac{m}{r/2}\right\rfloor\ \text{（偶 }r\text{）}\ ✓$$

| $r$ | 与全枚举比较 |
|---|---|
| 4 | **全吻合** ✓✓ |
| 5 | $\times$ 1 处（$m{=}10$ 饱和：枚举 10 vs 公式 11 ⟹ 须封顶 $\binom r2$ ✓） |
| 6 | $\times$ 2 处：$m{=}1$（枚举 8 vs 公式 9，**偏安全** ✓）；**$m{=}8$（枚举 12 vs 公式 11 ⟹ $\textbf{低估}$ ✗✗）** |

## §1 致命点（诚实 ⚠️）

$$\text{链 }h\ge H(e_{\max},m)\ \text{需要 }e_{\max}\ \text{的\ \textbf{上界}};\ \text{而 }r{=}6,m{=}8\ \text{处公式\ \textbf{不是上界}} ✗ \Longrightarrow \textbf{\text{据公式算出的 }\Delta\ \text{表（13--33）非严格}} ✗\ \text{（仅指示性）}$$

## §2 仍成立的正向结论 ✓

$$\Delta\ \text{之量级（十几至三十几）与"边数受限＋载荷凸性"预期\ \textbf{相称}} ⟹ \text{唐先生 §4 判据方向获支持} ✓\ ——\ \textbf{\text{无需第二层 closure}} ✓$$$

## §3 已知桥表（$r{=}8$，指示性）

| $m$ | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 | 35 |
|---|---|---|---|---|---|---|---|---|---|---|
| $e_{\max}$（公式） | 19 | 20 | 20 | 21 | 21 | 22 | 22 | 23 | 23 | 24 |
| $H$ | 27 | 36 | 48 | 57 | 72 | 84 | 102 | 114 | 132 | 180 |
| $J$ | 14 | 20 | 26 | 36 | 48 | 60 | 72 | 84 | 102 | 147 |
| $\Delta$（指示） | 13 | 16 | 22 | 21 | 24 | 24 | 30 | 30 | 30 | 33 |

## §4 下一步（照唐先生原方案 ✓）

$$\text{用\ \textbf{判定式} 精算 }e_{\max}(8,m):\ \text{"}\exists G:\ |E(G)|\ge E,\ T(G)=m?\text{"}\ \text{二分} \Longrightarrow \text{严格 }e_{\max}(8,m)\ \Longrightarrow \text{严格 }\Delta\ ✓$$

## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ r\le6\ \text{全枚举} ✓;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §6 【技术词回查】

```
技术词 quasi-bipartite  命中文件数=1
技术词 桥表   命中文件数=0
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档} ✓;\ \textbf{通用词（不计）}：\text{"桥梁／指示性"裸词} ✓$$
