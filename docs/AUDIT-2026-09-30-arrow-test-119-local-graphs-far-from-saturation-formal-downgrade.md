# AUDIT-2026-09-30 — **箭头实测**：真实 120-cover 之局部图 \le5$、\le10$，**远未接近极值层** ⟹ 机制不触发 ⟹ **正式降级** ✓（叠加 6× slack）

结论: 已查地图：命中 56 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 目标链接审计（无档案同型；非已知 RH 对象重命名）
D1: 0

## §0 三档档案状态（唐先生 23:43 定 ✓）

$$\boxed{\text{新机制原型：\textbf{成立}}}\quad \boxed{\text{119 接口：\textbf{未建立}}}\quad \boxed{\text{定量闭合：\textbf{不足}}}\ ✓$$

## §1 箭头检验（唐先生指令 ✓）

$$119\text{-cover}\ \stackrel{?}{\Longrightarrow}\ \text{某类 8 点局部图必跨 }20\to21$$

**实测（真实 120-cover，\in U$，$\mu(q)\ge2$；$＝代理定义 ⚠️：顶点 $=N(q)\cap C$，边＝距离 2 且除 $ 外另共享邻点）**

| 量 | 值 |
|---|---|
| $\mu$ 分布 | $\{1{:}746,2{:}136,3{:}13,4{:}2,5{:}7\}$ |
| 局部图 $(r,m)$ | $(2,0)^{136}$、$(3,1)^{13}$、$(4,4)^{2}$、$(5,10)^{7}$ |
| 最大 $r$ | **5** ✗ |
| 最大 $m$ | **10** ✗ |
| $(r{=}8,m\ge20)$？ | **否** ✗✗ |

## §2 判决

$$\text{真实码之局部图\ \textbf{极小}（}r\le5,\ m\le10\text{）} \Longrightarrow \text{离 }r{=}8\ \text{极值层极远} \Longrightarrow \textbf{\text{surplus 机制从未触发}}\ ✗$$
$$\text{唯一"饱和"点 }(5,10):\ e_{\max}(5,10)=10=\binom52 \Longrightarrow \text{此为\ \textbf{顶点饱和}（}m{=}\binom r3\text{）} \Longrightarrow \text{凸性恰取等、surplus}=0\ ✓\ \text{（非 }+3\ \text{机制所在之次饱和区 ✗）}$$
$$\therefore\ \text{按唐先生协议（箭头推不出 ＋ 6× slack）} \Longrightarrow \boxed{\text{本线\textbf{正式降级}}}\ ✓$$

## §3 诚实保留（防过杀 ⚠️）

$$\text{(i) 实测 }M{=}120\ (\text{而 }M{=}106\ \text{不可达});\ \text{"更密之码是否推大 }r\text{"}\ \textbf{\text{无定量论证}}\ ✗;\quad \text{(ii) }L_q\ \text{为\ \textbf{代理定义}}\ ⚠️\ \text{——若原定义不同需重算} ✓$$

## §4 降级后\ \textbf{保留} 之资产（不回撤 ✓）

$$\text{(A) }e_{\max}(8,m)\ \text{严格表} ✓;\quad \text{(B) }\Gamma(m)\ \text{表} ✓;\quad \text{(C) }h_{\min}(8,18/20/21/24)\ \text{精确} ✓;\quad \text{(D) 四步人工引理} ✓;\quad \text{(E) 极值层技法＋载荷谱}\ ✓$$

## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{实测可复现（}out/arrow\_test.log\text{）＋代理定义已声明} ⚠️;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §6 【技术词回查】

```
技术词 箭头实测   命中文件数=1
技术词 饱和度   命中文件数=0
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档} ✓;\ \textbf{通用词（不计）}：\text{"降级／需求侧"裸词} ✓$$
