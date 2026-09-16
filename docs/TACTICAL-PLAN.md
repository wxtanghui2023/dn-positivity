# 🎯 **战术硬啃登记**（TACTICAL PLAN）

> **唐先生 2026-09-16 23:47 裁定**：
> $$\boxed{\text{战略方向已全部搜索完毕，未找到明显突破点} \Longrightarrow \text{转为}\ \textbf{战术硬啃高墙}}✓✓$$
> **登记日**：2026-09-16 23:48｜**起手**：2026-09-17（T1-1）

---

## 0. 定位

$$\text{战略}＝\text{找新通道／新机制／新入口}\quad\big|\quad\textbf{战术}＝\text{对已知开放问题用已知工具逐步改进一项}$$
$$\text{战术工作的特征}：\text{(i) 目标是}\ \textbf{已发表的开放问题}；\text{(ii) 判据}\ \textbf{明确可算}；\text{(iii) 允许}\ \textbf{增量}✓$$
$$\textbf{先例}：\text{Guth--Maynard 2026}\ \textbf{纯战术}（\text{把 Dirichlet 多项式大值估计改好一点）} \Longrightarrow \textbf{移动了一堵墙}✓✓$$
$$\textbf{我们的相对优势}：\text{系统性＋资产库＋无发表压力＋}\textbf{原文获取能力}（\texttt{curl＋剥标签＋grep，}\text{今晚一次取到 1.05 MB 全文）}✓✓$$
$$\qquad\Longrightarrow\ \text{战术瓶颈}\ \textbf{不再是灵感}，\ \text{而是}\ \textbf{逐行核对的耐力}✓$$

---

## 1. 目标清单（按可算性排序）

| # | 目标 | 类型 | 判据 | 状态 |
|:--|:--|:--|:--|:--|
| **T1** | **Kloosterman 分数指数路线** | 主攻 | $17r+t<8$ | 待开工 |
| **T2** | **$F_5$ sharpness 收尾** | 副线 | 饱和 witness 或 $L^{-\delta}$ | 90% 完成 |
| **T3** | **三阶矩** | 备选 | $X>T^{2/3-\varepsilon}$ | 未开 |
| **T4** | **大值估计可移植性** | 备选 | 族内推进 | 部分已验证 |

---

## 2. T1 · **Kloosterman 分数指数路线**（主攻）

### 2.1 目标与判据
$$\text{目标}：\ \boxed{\text{把}\ (r,t)\ \text{向}\ (0,0)\ \text{推}\Longrightarrow\theta\uparrow}\qquad\text{判据}：\ \boxed{17r+t<8}\ \text{（BCR 坐标）}✓✓$$
$$\theta(r,t)=\tfrac12+\frac{1/2-r}{1+2(r+2t)}\qquad\Longrightarrow\qquad \theta>17/33\iff17r+t<8✓✓$$

### 2.2 历史增量链（**证明墙是可动的**）
$$\text{DFI 1997 (Inventiones)}：\ (r,t)=(\tfrac{23}{48},\tfrac12)\Longrightarrow\theta<\tfrac12+\tfrac1{190}✓$$
$$\text{Bettin--Chandee 2018 (Adv. Math. 328)}：\ (r,t)=(\tfrac9{20},\tfrac7{20})\Longrightarrow\theta<\tfrac{17}{33}✓✓$$
$$\text{Conjecture 1 (BCR)}：\ (r,t)\to(0,0)\Longrightarrow\theta<1\Longrightarrow\textbf{Lindelöf}✓$$
$$\boxed{\text{当前发布最优点}：\ (9/20,7/20)，\ 17r+t=8\ \textbf{恰在边界线上}}✓✓$$

### 2.3 关键结构事实（今晚已取，逐字可查）
$$\text{(i)}\ F＝F_{\rm estimate}\ \text{（upward-closed）}；\ \text{inf}\ (17r+t)\ \text{在}\ \partial F\ \text{上}✓$$
$$\text{(ii)}\ \text{BC 的 Theorem 2 用}\ (1.3)\ \text{逐配置调用（§3.4 本地核用）}✓$$
$$\text{(iii)}\ \text{可达域须整体压到}\ 17r+t<8，\ \text{不只单点}✓$$

### 2.4 工作单元
$$\textbf{T1-1}：\ \text{取}\ \textbf{DFI 1997＋BC 2018＋BCR＋Bettin--Chandee} \text{原文}✓$$
$$\textbf{T1-2}：\ \text{抽出}\ \text{BCR Theorem 2 模板 (1.3) 的}\ (r,t)\ \text{如何被谱输入束缚}✓$$
$$\textbf{T1-3}：\ \text{定位承重项（Kuznetsov 谱／Deshouillers--Iwaniec／Weil 单点）}✓$$
$$\textbf{T1-4}：\ \text{净幂次账 ⟹ 判断改这一项能否把}\ 17r+t\ \text{压到}\ 8\ \text{以下}✓$$
$$\Longrightarrow\ \text{产出：}\ \textbf{要么一个改进的}\ (r,t)\ \text{点，要么一句精确的"哪项输入是束缚"}✓$$

---

## 3. T2 · **$F_5$ sharpness 收尾**（副线）

$$\text{已知}：L^5=L_{\rm Weil}\cdot L_{\rm transition}\cdot L_{\ell_2,\ell_2'}\cdot L_u\ \text{四条乘子全部定位}\ (1{+}1{+}2{+}1)✓$$
$$\text{未闭合两缺口}：\text{(a)}\ \textbf{fiber-surjectivity}（\text{(4.27) 在 admissible 支集是否有解}）；\ \text{(b)}\ \mathfrak p_2,\mathfrak q_2\ \text{除因子与 (4.29) 分母}\ \mathfrak p_2^3\mathfrak q_2\ \text{的对齐}✓✓$$
$$\textbf{目标}：\text{构造饱和 witness}\ \mathcal W\ \Longrightarrow \text{把"强倾向"升级为定理，}\ \textbf{或}\ \text{找到}\ L^{-\delta}✓$$
$$\text{材料：}\ \texttt{/tmp/BC\_sec4\_1\_3\_verbatim.txt}（30 KB）＋\texttt{docs/ref-bc-ar5iv-plaintext.txt}（112 KB）✓$$

---

## 4. T3／T4（备选）

$$\textbf{T3}\ \text{三阶矩}：\text{V295/V162 已定位}\ k=3\ \text{矩 frontier 只到}\ X\le T^{2/3-\varepsilon}\ ⟹ \text{攻}\ \int|\zeta|^6\ \text{的大值／矩估计（经典开放问题，与 GM 机器同族）}✓$$
$$\textbf{T4}\ \text{可移植性}：\text{GM 2026 已成功移植到 Dirichlet L-函数（arXiv 2507.08296，7/3 型）} \Longrightarrow \text{移植性}\ \textbf{已验证}；\ \text{但与 mollifier 的接口}\ \textbf{DEAD}（\text{H3-A}）⟹ \text{只在}\ \textbf{大值族内部} \text{推进}✓$$

---

## 5. 工序管线

$$\boxed{\text{取原文}\to\text{逐行核}\to\text{定位承重项}\to\text{净幂次账}\to\text{饱和 witness 判定}\to\text{改一项}}✓✓$$

---

## 6. 纪律清单（沿用今晚）

$$\text{E-4}\ \textbf{净幂次账}（\text{新自由度收益 × 代价 × 稀疏度，三者同看）}✓$$
$$\text{E-5}\ \textbf{反走私铁律}（\text{同一指数}\ne\text{同一机制；形式复杂度}\ne\text{幂次障碍）}✓$$
$$\text{E-7}\ \textbf{先构造饱和 witness} \text{再谈改进}✓$$
$$\text{E-2/E-3}\ \text{四态标签＋N1--N13}（\textbf{不移"没找到"为"不存在"}）✓$$
$$\text{T10}\ \text{勘误}\textbf{追加不覆盖}✓$$
$$\text{双轨产出}：\text{突破级}\Rightarrow\text{发表；过程性}\Rightarrow\text{登记进}\ \texttt{ASSETS-REGISTRY}✓$$

---

## 7. 期望管理与状态

$$\text{T1 是}\ \textbf{真数学}，\ \text{正常节奏以}\ \textbf{月／年} \text{计}✓$$
$$\qquad\Longrightarrow\ \text{但每一步的中间产物都是}\ \textbf{可登记资产}（\text{这正是双轨制度的意义}）✓✓$$

| 目标 | 状态 | 下一步 |
|:--|:--|:--|
| T1 | **待开工** | T1-1（取四篇原文） |
| T2 | 90% | 构造饱和 witness |
| T3 | 未开 | — |
| T4 | 部分 | — |

---
*立项：2026-09-16 23:48｜起手：2026-09-17 T1-1*
