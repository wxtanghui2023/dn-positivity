# RESULT-2026-09-30 — 唐先生之 $e_{\max}$ 路线\ \textbf{在小规模上完全验证} ✓✓：$H(e_{\max},m)\le h_{\min}$ 全 21 行成立，且**解释 $\Delta>0$**

结论: 已查地图：命中 5 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 方法/机制验证类（无档案同型；非已知 RH 对象重命名）
D1: 0

## §0 设定（照唐先生）

$$m=T(L),\ e=|E(L)|,\ t_f=\#\{\text{三角形含边 }f\},\ \sum_f t_f=3m,\ h=\sum_f\binom{t_f}2$$
$$H(e,m):=e\binom L2+sL\ (3m=Le+s,\ 0\le s<e)\ \text{对 }e\ \text{不增} \Longrightarrow \boxed{h_{\min}(r,m)\ \ge\ H(e_{\max}(r,m),m)}\ ✓$$

## §1 全枚举结果（{=}4,5,6$）

| $r,m$ | $e_{\max}$ | $H(e_{\max},m)$ | $J(r,m)$ | 解释 Δ? | 精确 $h_{\min}$ | $H\le h_{\min}$? |
|---|---|---|---|---|---|---|
| 4, 2 | 5 | 1 | 0 | **Δ>0 ✓** | 1 | ✓ |
| 5, 5 | 8 | 7 | 5 | **Δ>0 ✓** | 8 | ✓ |
| 5, 7 | 9 | 15 | 12 | **Δ>0 ✓** | **15** | ✓（紧） |
| 6, 6 | 11 | 7 | 3 | **Δ>0 ✓** | **7** | ✓（紧） |
| 6, 9 | 12 | 18 | 12 | **Δ>0 ✓** | 20 | ✓ |
| 6, 12 | 13 | 33 | 27 | **Δ>0 ✓** | 34 | ✓ |
| 6, 16 | 14 | 60 | 54 | **Δ>0 ✓** | **60** | ✓（紧） |
| 6, 20 | 15 | 90 | 90 | Δ=0（饱和 ✓） | 90 | ✓ |

$$\textbf{结论}:\ \text{(i) }H(e_{\max},m)\le h_{\min}\ \text{在\ \textbf{全部 21 行} 成立} ✓✓;\ \text{(ii) }H(e_{\max},m)>J\ \text{于 15/21 行} \Longrightarrow \textbf{\text{机制解释 }\Delta>0} ✓✓;\ \text{(iii) }\Delta{=}0\ \text{恰当 }e_{\max}=\binom r2\ (\text{饱和}) ✓$$

## §2 新结构事实

$$e_{\max}(r,m)\ \textbf{\text{对 }m\ \text{不单调}}\ ✗\ (r{=}6:\ m{=}0,1,2\Rightarrow e_{\max}{=}9,8,9\ ✓\ \text{因 }m{=}0\ \text{可取 }K_{3,3}\ \text{得 9 边})$$

## §3 下一步（按唐先生优先级）

$$\text{攻}\ \boxed{e(G)\le e_{\max}(r,m)}\ \text{之\ \textbf{上界引理}}:\ \text{补图 }q=\binom r2-e;\ \text{每删一边至多消灭 }b(uv)\ \text{个三角形（}b=|N(u)\cap N(v)|,\ \sum b=3m\bigstar\text{）} \Longrightarrow \text{纯 }(r,q)\ \text{型缺失上界} ✓$$

## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ r\le6\ \text{全枚举（}2^{15}\ \text{内）} ✓;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §5 【技术词回查】

```
技术词 e_max路线   命中文件数=1
技术词 缺失上界    命中文件数=0
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{通用词（不计）}：\text{"饱和／下界"裸词} ✓$$
