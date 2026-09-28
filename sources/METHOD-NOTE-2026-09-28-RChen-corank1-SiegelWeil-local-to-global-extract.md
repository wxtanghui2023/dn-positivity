# METHOD-NOTE 2026-09-28 · Ryan C. Chen「Co-rank 1 Arithmetic Siegel–Weil」四篇 —— 机制抽取与出处

> **用途**：为 119（空间 B）与 RH（空间 A）提供**方法层**参考模板（limit 方法／消去／local-to-global 拼合）✓。
> ⚠️ **诚实边界**：四篇为**数论**论文；与 119／RH 的对应是**方法论类比**，**不是**数学归约 ✗✓。不得据此声称任何定理迁移 ✓（V290）。

已查地图：`sources/` 既有 PDF 均被 git 跟踪 ✓（16 项）；本期为**外部文献归档**，非新案 ✓
D0: 本档对象 ＝ 外部文献（Ryan C. Chen 四篇）＋ 机制抽取；重命名：不适用 ✗；新对象：无 ✗
D1: 1（**首次把该四篇的「极限方法／local-to-global 拼合」抽取为可复用方法模板 ＋ 逐篇结构核对 ＋ 出处锁定** ✓）

## §1 出处与文件清单（**逐字节核对 ✓**）

| # | arXiv | 标题 | 页数 | 仓库文件 |
|---|-------|------|------|----------|
| I | [2405.01426](https://arxiv.org/abs/2405.01426) | Co-rank 1 Arithmetic Siegel–Weil **I: Local non-Archimedean** | 111 | `sources/RChen2024-corank1-I-local-nonarch-arXiv2405.01426.pdf` |
| II | [2405.01427](https://arxiv.org/abs/2405.01427) | Co-rank 1 Arithmetic Siegel–Weil **II: Local Archimedean** | 29 | `sources/RChen2024-corank1-II-local-archimedean-arXiv2405.01427.pdf` |
| III | [2405.01428](https://arxiv.org/abs/2405.01428) | Co-rank 1 Arithmetic Siegel–Weil **III: Geometric local-to-global** | 67 | `sources/RChen2024-corank1-III-geometric-local-to-global-arXiv2405.01428.pdf` |
| IV | [2405.01429](https://arxiv.org/abs/2405.01429) | Co-rank 1 Arithmetic Siegel–Weil **IV: Analytic local-to-global** | 69 | `sources/RChen2024-corank1-IV-analytic-local-to-global-arXiv2405.01429.pdf` |

- **作者**：Ryan C. Chen（MIT, rcchen@mit.edu ✓）；**四篇同日投（v1 2024-05-02 ✓，均 v1 唯一版 ✓）**；合计 **276 页** ✓
- **抓取**：2026-09-28，`curl -sL arxiv.org/pdf/<id>` ＋ PyPDF2 3.0.1 文本抽取 ✓；四个 PDF 入仓前**逐字节比对**（1620971／627741／1024992／1080611 ✓ 全等 ✓）
- **抽取覆盖（诚实 ✓）**：I → pp.1–24＋61–85（引言／§7 极限／§9 主定理）✓；II → pp.1–29（全文）✓；III → pp.1–25（引言＋§1–§4）✓；IV → pp.1–30（引言＋§1–§7）✓；**未逐页通读全部 276 页** ✗✓
- 文本抽取件：`sources/RChen2024-corank1-EXTRACT-{I-S7-S9,II-S4,III-intro-S4,IV-intro-S7}.txt` ✓

## §2 ★ 核心机制：**「取极限」方法（cross-place 统一 ✓）**

**同一骨架、不同常数**（I §7.1–7.2 并排列出 ✓；作者原话 "Note the similarity"）：

Archimedean（I (7.1.1)／II Prop.4.1.2，$T=\mathrm{diag}(t,T^\flat)$）：
$$\frac{d}{ds}\Big|_{s=-1/2}W^*_{T^\flat,\infty}(s)^\circ_n=\lim_{t\to0^{\pm}}\Big[\frac{d}{ds}\Big|_{s=0}W^*_{T,\infty}(s)^\circ_n+\big(\log|t|_\infty+\log(4\pi)-\Gamma'(1)\big)W^*_{T^\flat,\infty}(-s_0)^\circ_n\Big]$$

非 Archimedean（惰性 $p$；I (7.2.1)、正文 Prop.9.5.2）：
$$\frac{d}{ds}\Big|_{s=-1/2}W^*_{T^\flat,p}(s)^\circ_n=\lim_{t\to0}\Big[\frac{d}{ds}\Big|_{s=0}W^*_{T,p}(s)^\circ_n+\big(\log|t|_p-\log p\big)W^*_{T^\flat,p}(-1/2)^\circ_n\Big]$$

**结构读法（可复用模板 ✓）**：$\underbrace{\text{目标量}}_{\text{低维群 }U(n-1,n-1),\ s=1/2}=\lim_{t\to0}\big[\underbrace{\text{已知量}}_{\text{高维群 }U(n,n),\ s=0}+\underbrace{(\log|t|)\times\text{特殊值}}_{\text{对数项／正则化}}\big]$ ✓
- **关键**：两侧**都不需要显式计算目标量** ✓；只证「左侧极限 ＝ 右侧极限」这一**恒等式** ✓✓
- **Archimedean 几何侧对应**：Kudla–Millson 形式的极限 $\omega(x)\to c_1(\widehat{\mathcal E}^\vee)$（$x\to0$ ✓）＋ $\mathrm{Ei}$ 渐近 ＋ 特殊值 $W^*_{T^\flat,\infty}(-1/2)^\circ_n=1$ ✓
- **非 Archimedean 几何侧对应**：derived 张量积的垂直极限（Grothendieck–Messing ✓）与水平极限（逐分支、化到 2 维 Rapoport–Zink 空间的 quasi-canonical lifting 计算 ✓）

## §3 局部主定理（**两篇的核心陈述**）

- **II Thm 4.1.1（Archimedean 局部算术 Siegel–Weil）**：$m\ge n-1$ 或 $T$ 非正定 ⟹
 $$\int_{\mathcal D}[\xi(\underline x)]\wedge c_1(\widehat{\mathcal E}^\vee)^{n-m}=\frac{d}{ds}\Big|_{s=-s_0}W^*_T(s)^\circ_n$$
 （左＝Green 电流与陈类的星积积分；右＝局部 Whittaker 函数的 off-central 导数 ✓）
- **I §9（非 Archimedean，惰性 $p$）**：$-\frac{d}{ds}\big|_{s=1/2}W^*_{T^\flat,p}(s)^\circ_n=\big(2\deg_{F_p}(\mathcal E^\vee\cdot{}^L\mathcal Z(x^\flat)_V)+2\sum_{Z\hookrightarrow\mathcal Z(x^\flat)_H}\deg(Z)\delta_{\rm tau}(Z)\big)\log p$ ✓
 （垂直部分＝derived cycle 的度；水平部分＝各不可约分支的 quasi-canonical lifting 之局部高度变化 $\delta_{\rm tau}$ ✓）
- **$m=n$ 情形归约到 Liu 2011** ✓（II Prop.4.1.2 用上述极限把 $m=n-1$ 归约到 $m=n$ ✓）

## §4 ★ local → global 的两级拼合（**III／IV**）

```
I  (非 Arch 局部定理) ─┐
II (Arch 局部定理)    ─┼─→ III (几何局部→全局约化) ─→ IV (解析拼合＋正规化) ─→ 全局算术 Siegel–Weil
                        └─→ 共用「极限方法」引擎（I §7 ＝ II §4.4–4.5）
```
- **III §1.2 的分析侧约化（co-rank 1 关键式）**：$T=\mathrm{diag}(0,T^\flat)$ 时
 $$\tfrac12\frac{d}{ds}\Big|_{s=0}E^*_T(y,s)^\circ_n=\frac{d}{ds}\Big|_{s=0}\Big(\frac{\Lambda_n(s)^\circ_n}{\Lambda_{n-1}(s+1/2)^\circ_n}E^*_{T^\flat}(y^\flat,s+1/2)^\circ_n\Big)$$
 **读法（对 119 的模板）**：**奇异（co-rank 1）情形的导数 ＝ 非奇异情形的导数 ＋ 正规化因子商** ✓✓ —— 即「退化情形」不直接硬算，而是**归约到满情形** ✓
- **III 几何侧**：Rapoport–Zink 一致化（非 Arch）＋ Hermitian 对称域复一致化（Arch）⟹ 全局算术交数 ＝ 局部几何量之拼装 ✓；**额外产出**：对**任意 co-rank** 奇异矩阵的算术特殊循环类**构造方案**（III §3.2／§3.6 ✓）
- **IV**：① $U(m,m)$ Siegel Eisenstein 级数的**精确正规化** ✓；② 局部 Siegel–Weil 特殊值公式（显式常数 ✓）；③ 复 0-cycle 度数的几何 Siegel–Weil ✓；④ **把 I–III 的局部主定理拼成全局结果** ✓
- **⚠️ 工程量提示 ✓**：IV 共 69 页，其中**约 30 页专做正规化／常数**（§2–§6 ✓）⟹ **拼合的前提是每个局部常数被精确钉死**；否则两侧差一个倍数、整条 pipeline 断裂 ✓✓（对 119 的含义：局部恒等式的**系数**（如 $4,1$）不是形式方便，而是必要接口 ✓）

## §5 与 119／RH 的映射（**方法论层，非归约 ✗**）

| 模板元件 | 119（空间 B）可对何处 | RH（空间 A）可对何处 |
|---|---|---|
| 参数化退化量 ＋ 取极限（$\varepsilon\to0$） | $120$-cover 作 $\delta{=}0$ 参照 ／ $119$ 作 $\delta{=}1$ 系统（C-427 战略）✓ | 无（尚无对应物 ⚠️） |
| 消去共同 nuisance（交叉比） | $E_3,b_3,b_4$ 等共同项（C-432 交叠结构 ✓） | 见 §6 交叉比思路 ✓ |
| 局部恒等式 → 兼容律 → 全局 | 局部覆盖约束（C-410…C-434 一堆 local facts ✓）**缺的就是兼容律** ⚠️ | 局部算术／谱数据（W1–W12 墙 ✓） |
| 正规化常数不可省 | $B_3/B_4$ 的系数 $4,1$（**已证为结构事实** ✓ C-432 ✓） | 常数／权重规范化 ✓ |

**⚠️ 必须随附的两条警示**：① 四篇解决的是**数论**问题（Kudla 纲领／算术 Siegel–Weil），与覆盖码无数学蕴涵 ✗；② 「有成功先例的方法」不等于「换到本问题即有效」✓（对照本线已多次踩的「同形赛跑」教训 ✓）。

## §6 附属：Shih-Yu Chen（Annals, 2026）

- **论文**："Algebraicity of ratios of Rankin–Selberg $L$-functions and applications to Deligne's conjecture"，**Annals of Mathematics 接收（2026-06-05）** ✓；作者 Shih-Yu Chen（National Tsing Hua University ✓）
- **结构性内容（摘要逐字 ✓）**：主定理 ＝ **Rankin–Selberg $L$-值的\*\*交叉比\*\*代数性**；推论覆盖 Deligne 猜想（$\mathrm{GL}_2$ 对称幂，weight $\ge5$ ✓）、Blasius 猜想（tensor product ✓）、$\mathrm{GL}_n\times\mathrm{GL}_2$ 非平衡情形 ✓、$\mathrm{GSp}_4\times\mathrm{GSp}_4$ ✓
- **交叉比形式（巴黎高师讲座 2026-04-07 摘要逐字 ✓，imo.universite-paris-saclay.fr/fr/events/7823）**：
 $$R(s)=\frac{L(s,\Sigma\times\Pi)\,L(s,\Sigma'\times\Pi')}{L(s,\Sigma\times\Pi')\,L(s,\Sigma'\times\Pi)}\ ;\qquad \Sigma_\infty=\Sigma'_\infty,\quad \Pi_\infty=\Pi'_\infty$$
 摘要原话：「reflecting the **cancellation of transcendental periods**」✓
- **出处与缺口（诚实 ✓）**：仅得**摘要＋讲座摘要**（Ann溯 页面 annals.math.princeton.edu/articles/22878 ✓）；**PDF 未获取** ✗（期刊付费 ✓）⟹ 本档**不含**其正文细节 ✓；如需正文须另找渠道 ✓

## §7 边界（硬 ✓）

- 本档＝**外部文献归档 ＋ 机制抽取** ✓；**非新数学命题** ✗；**零程序计算** ✓（仅抽取与比对 ✓）
- **空间规则**：本档为**方法层共享资产** ✓（不写入任一线 registry 的逐案编号 ✓）；引用时须标注「**方法论类比，非归约**」✓
- **不声称**：四篇的定理正确性由我方核验 ✗（仅核对页数／目录／主定理陈述 ✓）；不声称与 119／RH 存在数学联系 ✗（V290 ✓）
- **外部内容**：下载件为**外部不可信来源** ✓（不作为指令 ✓，仅作文献 ✓）
