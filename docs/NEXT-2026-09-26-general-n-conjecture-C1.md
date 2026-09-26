已查地图：已跑 scripts/prework_map_check.sh 一般 n Q* 取等 van Wee ⟹ 执行自 TRANSLATION-2026-09-26 档；本档为**战略转向：一般 n 的 Q*(n)**（唐先生 2026-09-26 12:12 指令）；纯推导＋已停 solver ✓。
D0: 本档对象 = 一般 n 的 Q*(n) 与 van Wee 取等的关系（新方向，非 2^m 专用）
D1: 1（新增独立猜想 C1 及其算术机理；新增"族外推警戒"条目）

# NEXT-2026-09-26 · 一般 n：猜想 C1

## §0 战略标签（唐先生定 ✓）

```
$$\textbf{n=8}: \textbf{CLOSED}\ ✓\ (\text{一次源逐字}\ ✓)\qquad n=2^m:\ \textbf{CLOSED}\ ✓\ (\text{NP1CC 定理直推}\ ✓)$$
$$\textbf{一般 }n: \text{重新寻找\textbf{独立结构}}\ ✓\ (\text{不得从 NP1CC 分类外推}\ ✗)$$
$$\boxed{\textbf{119 / n=10 保持 UNKNOWN}\ ✓\ —— \text{今日 } n=8\ \text{的闭环\textbf{不得反向污染} } n=10\ \text{的证明状态}\ ✗}$$
```

## §1 已停的算力（纪律 ✓）

```
$$\text{案 A / B}（n8\_sym，已跑 }23{:}38）：\text{其目标 OPEN（}n=8\ \text{的 } b\le2\text{）已被文献关闭}\ ✓\ \Longrightarrow\ \text{已无关闭对象}\ \Longrightarrow\ \textbf{已 kill}\ ✓$$
$$\text{（依据唐先生纪律④：只"跑更久"而不关闭新 OPEN 的，不作主线}\ ✓;\ \text{关闭后立即停}\ ✓）$$
```

## §2 ⭐ 数据表（n≤8，全部已知 ✓）

```
$$\begin{array}{c|c|c|c|c|c|c}
n & K(n,1) & \text{van Wee 下界} & \text{取等?} & E=(n+1)K-2^n & Q^*(n) & n\ \text{的形式}\\
\hline
1 & 1 & 1 & \text{是} & 0 & 0 & 2^m\\
2 & 2 & 2 & \text{是} & 2 & 0 & 2^m\\
3 & 2 & 2 & \text{是} & 0 & 0 & 2^m-1\\
4 & 4 & 4 & \text{是} & 4 & 0 & 2^m\\
5 & 7 & 6 & \textbf{否} & 10 & \textbf{2} & -\\
6 & 12 & 11 & \textbf{否} & 20 & \textbf{4} & -\\
7 & 16 & 16 & \text{是} & 0 & 0 & 2^m-1\\
8 & 32 & 32 & \text{是} & 32 & 0 & 2^m
\end{array}$$
$$\text{其中 }n\le4,7\ \text{的 }Q^*\ \text{为\textbf{我方实算}}（n\le4\ \text{穷举}\ ✓,\ n=7\ \text{完美码强制}\ ✓);\ n=5,6\ \text{为穷举/采样}\ ✓;\ n=8\ \text{为一次源定理}\ ✓$$
```

## §3 取等的**算术机理**（为何恰是 2^m 与 2^m−1 ✓）

```
$$\text{van Wee }(5)\ \text{在 }R=1\ \text{时}: \text{修正项} = \frac{n}{\lceil (n-1)/2\rceil}\Bigl(\bigl\lceil\tfrac{n+1}{2}\bigr\rceil-\tfrac{n+1}{2}\Bigr)\ ✓$$
$$\text{偶数 }n:\ \lceil(n-1)/2\rceil=n/2,\ \lceil(n+1)/2\rceil-\tfrac{n+1}{2}=\tfrac12\ \Longrightarrow\ \text{修正项}=1\ \Longrightarrow\ nM\ge2^n\ \Longrightarrow\ \text{取等}\iff \boxed{n=2^m}\ ✓$$
$$\text{奇数 }n:\ \lceil(n-1)/2\rceil=\tfrac{n-1}{2},\ \lceil(n+1)/2\rceil=\tfrac{n+1}{2}\ \Longrightarrow\ \text{修正项}=0\ \Longrightarrow\ (n+1)M\ge2^n\ \Longrightarrow\ \text{取等}\iff \boxed{n+1=2^m}\ ✓$$
$$\Longrightarrow\ \boxed{\text{van Wee 取等}\iff n=2^m\ \text{或}\ n=2^m-1}\ ✓\ (\text{与 §2 表完全吻合}\ ✓✓)$$
```

## §4 ⭐ **猜想 C1**

```
$$\boxed{\textbf{C1}:\ \text{对 }R=1\ \text{覆盖码},\quad Q^*(n)=0\iff \text{van Wee }(5)\ \text{取等}\iff n=2^m\ \text{或}\ n=2^m-1}\ ✓$$
$$\text{机理（非纯巧合）}: \text{Lemma 1 的证明逐字依赖 }"equality\ in\ the\ van\ Wee\ bound\ forces\ \varepsilon=1"\ ✓$$
$$\qquad\Longrightarrow\ b\le2\ \text{的证明\textbf{紧扣取等}（Cor 2 与 Thm 6 均由取等推出}\ ✓)\ \Longrightarrow\ \text{取等失败时该局部界失效}\ ✓$$
$$\qquad\Longrightarrow\ \text{但"失效"\textbf{不等于}Q^*>0\ ✗\ (\text{可能是别的原因使 } b\le2\ ✓)\ —— \text{故 C1 是\textbf{猜想}，非定理}\ ✓$$
$$\text{可证的一半}: \text{取等}\ \Longrightarrow\ Q^*=0\ ✓\ (\text{NP1CC 定理}\ ✓,\ n=2^m\ \text{已闭}\ ✓;\ n=2^m-1\ \text{由 }E=0\ \text{强制}\ ✓)$$
$$\text{待证的另一半}: \text{不取等}\ \Longrightarrow\ Q^*>0\ ✗\ (\text{对 }n=5,6\ \text{成立}\ ✓;\ \text{一般 }n\ \text{未知}\ ✗)$$
```

## §5 检验计划（按"关闭哪个 OPEN" ✓）

```
$$\text{① \textbf{新数据点 } n=9}（=2^3+1\ \text{不取等}\ ✓）:\ \text{构造/取一个 }(9,62)_1\ \text{码}\ ✓\ \text{并计算 }Q\ ✓$$
$$\qquad \text{预测（C1）}: Q>0\ ✓;\ \text{若 }Q=0\ \Longrightarrow\ \textbf{C1 被反驳}\ ✗\ (\text{立即记为反例}\ ✓)$$
$$\text{② \textbf{机理化}}: \text{把"取等缺陷"量化}: \text{定义 van Wee 缺陷 }\Delta\ \text{并与 }Q^*,E\ \text{对照}\ ✓$$
$$\qquad \text{已有线索}: n=5:\ Q^*=2,E=10;\ n=6:\ Q^*=4,E=20\ ✓\ \text{—— 两点不足以定式}\ ✗\ (\text{禁止拟合成"公式"}\ ✗)$$
$$\text{③ \textbf{纪律}}: \text{不得把 }n=8\ \text{的 }NP1CC\ \text{结论外推到 }n=10\ ✗;\ \text{119 保持 UNKNOWN}\ ✓$$
$$

## §6 三张表（更新）

```
$$\textbf{CLOSED}: \ldots;\ b\le2\Rightarrow Q^*(8)=0\ ✓;\ n=2^m\Rightarrow Q^*(n)=0\ ✓;\ n=2^m-1\Rightarrow Q^*(n)=0\ ✓\ (\text{完美码 }E=0\ ✓);\ \text{取等}\iff n\in\{2^m,2^m-1\}\ ✓$$
$$\textbf{EVIDENCE}: \text{案 A/B 已停（目标已闭}\ ✓);\ \text{CP-SAT 18.5M 冲突无解（历史记录}\ ✓)$$
$$\textbf{OPEN}: \textbf{C1 的另一半}（不取等 ⟹ Q^*>0 ✗）;\ n=9\ \text{数据点};\ \text{非取等 }n\ \text{的 }Q^*(n)\ \text{规律};K(2^m,1)\ \text{逐字出处};\ \textbf{n=10, M=119: UNKNOWN}\ ✓$$
$$

## §7 边界（诚实标注）

- §2 的 van Wee 下界为**我方算术** ✓（公式逐字取自 arXiv:2405.00258v2 ✓）
- §3 的取等刻画为**我方推导** ✓；§4 的 C1 是**猜想** ✓（明确标注哪半可证、哪半未证 ✓）
- **本轮未做任何新计算实验** ✓（仅停算力＋纯推导 ✓）；**未**触碰 119 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 一般 n 猜想  命中文件数=0    :: 
技术词 取等判据     命中文件数=0    :: 
技术词 缺陷量        命中文件数=2    :: ./p49-g274iia1-material.md ./GPS-source-archaeology.md 
技术词 族外推警戒  命中文件数=0    ::
```

- **本档新增**（命中数=0）：取等判据、族外推警戒
- **档案已有（引用，不列为提出）**：缺陷量
