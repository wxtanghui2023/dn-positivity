# AUDIT-2026-09-30 — **P2a**：定义对齐 ⟹ 撤回我的"近饱和"发现 ✗；$2A_2(R)$ 标度律成立 ✓；**P2b 无需执行** ✗

结论: 已查地图：命中 2 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 定义对齐与撤回（无档案同型；非已知 RH 对象重命名）
D1: 0

## §0 正确定义（档案取回 ✓）

$$L_q=(V_q,E_q),\quad V_q=\{i:q^i\in R\},\quad E_q=\{\{i,j\}:q^{ij}\in U\};\qquad R,U\subseteq C\ \textbf{\text{为码字集之分拆}}\ (\text{唐先生 }|R|{=}i{\approx}40\text{--}44)\ ✓$$

## §1 撤回（我上一轮之错 ✗）

| 我上轮所用 | 正确 |
|---|---|
| $R=C$（全部码字） | $R\subsetneq C$（$\sim40$ 个码字） |
| $U=$ 非码字集 | $U=C\setminus R$（码字） |
| $q$ 取非码字 | $q\in B\subseteq U\subseteq C$ |

$$\therefore\ \text{"}\Sigma h_q(219\text{--}273)\ \text{与}\ 2A_2(R)(298)\ \text{仅差 10\%"}\ \textbf{\text{作废}} ✗\ \text{（两个不同 }q\text{ 集之量级巧合）}\ ✓$$

## §2 随机分拆扫描（120-cover，每 $i$ 30 次）

| $i$ | 30 | 40 | 45 | 50 | 60 | 75 |
|---|---|---|---|---|---|---|
| $2A_2(R)$ | 17.3 | 33.3 | 41.2 | 51.8 | 75.3 | 114.7 |
| $\Sigma h_q$ | **0** | **0** | **0** | **0** | **0** | **0** |

$$\because\ \text{随机分拆下 }r_q\approx0.4\ll3 \Longrightarrow L_q\ \text{无三角形} \Longrightarrow \textbf{\text{真实分拆必为结构化}}\ ✗\ (\text{该准则为 106 分析之\ \textbf{情形参数}},\ \text{现有数据不可实现} ⚠️)$$

## §3 稳健定量事实 ✓✓

$$\boxed{2A_2(R)\ \approx\ \left(\tfrac{i}{|C|}\right)^2\cdot 2A_2(C)}\ ✓\ (\text{集中性};\ i{=}45:\ \text{预测 }41.9\ \text{vs 实测 }41.2\ ✓✓)$$
$$\Longrightarrow\ 2A_2(R)\approx\mathbf{18}\ (M{=}106,i{\approx}42)\ \text{至}\ \mathbf{41}\ (M{=}120,i{=}45)\ \Longrightarrow\ \Sigma h_q\le2A_2(R)\ \text{之\ \textbf{预算极小}}\ ✓$$

## §4 判决（P2a / P2b）

$$\textbf{(P2a)}\ \text{(i) 撤回近饱和 ✗};\ \text{(ii) 正确比较在现有数据上\ \textbf{不可判定}（缺分拆准则＋缺 106-code）} ⚠️;\ \text{(iii) }h\ \text{预算}\approx18\text{--}42\ \ll\ \text{唐先生线 }\Sigma m_q\gtrsim120\ ✗$$
$$\textbf{(P2b)}\ \boxed{\text{无需执行}}\ ✗:\ \text{因 }h_q\ \text{可为 }0\ (D_{\rm true}\ \text{型}) \Longrightarrow h\ \text{侧\ \textbf{给不出} }\Sigma m_q\ \text{之下界} \Longrightarrow M{=}106\ \text{处无符号可判}\ ✓$$

## §5 保留资产（不回撤 ✓）

$$\text{(A) }L_q\ \text{之\ \textbf{正确定义}（防未来再次错对象测量）} ✓;\quad \text{(B) }2A_2(R)\ \text{标度律} ✓;\quad \text{(C) 前档之 }e_{\max}/\Gamma/h_{\min}/\text{四步引理}\ ✓$$

## §6 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{定义取自档案原文；扫描可复现（}out/p2a\_scan.log\text{）} ✓;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §7 【技术词回查】

```
技术词 P2a定义对齐   命中文件数=1    :: ./AUDIT-2026-09-30-P2a-definition-alignment-retraction-and-2A2R-scaling.md
技术词 标度律       命中文件数=11   :: （含 p5-8-distortion-test.md / ASSETS-REGISTRY.md / delta-rigidity-spectrum.md 等）
```
$$\textbf{分类}：\textbf{本档新增}：\text{仅「P2a定义对齐」（1 档）} ✓;\quad \textbf{档案已有（引用，不列为提出）}：\text{「标度律」11 档 ✗ 非新} ✓;\quad \textbf{通用词（不计）}：\text{"分拆／撤回"裸词} ✓$$
