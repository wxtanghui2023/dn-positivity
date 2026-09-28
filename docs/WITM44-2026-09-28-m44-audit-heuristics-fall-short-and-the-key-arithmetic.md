# WITM44-2026-09-28 — **$m(44)$ 审计：启发式远未抵达极值结构（独立集 29 vs 真值 40）⟹ 数值上\ \textbf{定不了} $m(44)\ge8$ ✗；P1 真但定量核未决**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:44 令 ✓）**：奇偶路线之 P1-A（$m(44)\ge8$）可行性审计；**有限穷举／局部搜索** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-476／C-475／C-472，非新案 ✓）**
`docs/WITPAR-2026-09-28-…`（**$\lambda_{\min}{=}-5$／谱界失效／上界侧有效 ✓✓✓**）｜`docs/WITINT-2026-09-28-…`（**② 归约 ✓✓**）｜`docs/C-427 registry`（**$107\le K(10,1)\le120$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §4）
D0: 本档对象 ＝ **档案已有** $\frac12Q_{10}$／$A(10,4)$／$m(s)$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次对 $m(44)$ 做局部搜索并判定启发式之\ \textbf{能力边界}（独立集仅达 29 vs 真值 40；44 点最少边仅达 18）⟹ 数值定不了 $m(44)\ge8$ ＋ 首次给出与搜索无关之\ \textbf{关键算术}（极大 40-码之外部度均值 $1800/472{=}3.814$）+ 首次指出 P1 之成立与否等价于"极大码之最小外部度"这一具体量** ✓）
**[RESEARCH]**

---

## §0 结论（**✗✗数值不可决｜✓关键算术｜P1 真而核未决**）

$$\boxed{\textbf{(1) ✗✗启发式能力不足（本档实测）}:\ }\text{纯贪心 ＋ 有限 1-交换：最大独立集仅达 }\mathbf{29}\ \text{点}\ \big(\text{真值 }A(10,4){=}40\ ✗✗\big)$$
$$\qquad\text{44 点最少边局部搜索（增量 ＋ 候选采样）：仅达 }\mathbf{18}{\sim}21\ \text{条边}\ \big(\text{目标}\le7\ ✓\big)\Longrightarrow\ \text{距目标 }10+\ \text{条边}\ ✗✗$$
$$\qquad\Longrightarrow\ \boxed{\text{数值无法判定 }m(44)\ge8\ ⟹\ \text{本档\ \textbf{不能}证实亦\ \textbf{不能}否证 P1}}\ ⚠️\ \big(\text{与唐先生 §10"不要现在就 SAT"之谨慎一致 ✓}\big)$$
$$\boxed{\textbf{(2) ✓✓关键算术（不依赖搜索 ✓）}:\ }\text{设 }I\ \text{为\ \textbf{极大} (10,4)-码}\ \big(|I|{=}40✓\big)\Longrightarrow\sum_{x\notin I}|N(x)\cap I|=40\cdot45=\mathbf{1800}\ \text{摊于 472 点}\Longrightarrow\boxed{\text{外部度均值}=3.814}\ ✓$$
$$\qquad\Longrightarrow\ \text{"40-码 ＋ 4 外部点"之边数}=\sum(\text{4 点之外部度})+(\text{4 点间之边})\ ✓$$
$$\qquad\textbf{（分岔 ✓）}:\ \text{若 }\min\text{外部度}{=}1\Longrightarrow\text{4 点至少 4 边（}\le7\ \text{可达 ⟹ P1 \textbf{死} ✗）};\quad \text{若 }\min\text{外部度}\ge2\Longrightarrow\text{4 点至少 8 边（⟹ 该族\textbf{支持} P1 ✓）}$$
$$\qquad\Longrightarrow\ \boxed{\text{P1 之成立与否}\iff\text{"极大码之最小外部度"这一具体量}}\ ✗\ \text{（本档未定 ✗）}$$
$$\qquad\textbf{（弱码之对照 ✓）}:\ \text{29-码之外部度分布}=\{1{:}32,\ 2{:}151,\ 3{:}231,\ 4{:}67,\ 5{:}2\}\ \big(\text{均值 }2.702✓\big)\Longrightarrow\ \text{度-1 外部点在\ \textbf{非极大}码上大量存在 ✓（极大码未知 ✗）}$$

---

## §1 P1 之性质审计（**✓真｜⚠️非小计算｜隐含子案**）

$$\boxed{\text{P1-A}:\ m(44)\ge8 \iff |S|{=}44,\ e(S)\le7\Longrightarrow\alpha(S)\ge41}\ ✓\ \text{（唐先生改写得正确 ✓✓）}$$
$$\qquad\Longrightarrow\ \text{与 }\alpha(\tfrac12Q_{10}){=}A(10,4){=}40\ \text{冲突 ⟹ }a{=}44\ \text{死 ✓✓}$$
$$\textbf{⚠️（性质 ✓）}:\ m(44)\ \text{是关于\ \textbf{一切} 44-点集之断言 ⟹ 它\ \textbf{蕴含}"不存在 }a{=}44\ \text{之 119-cover"}\ ✓——\text{即原问题之一\ \textbf{真子案} ✓}$$
$$\qquad\Longrightarrow\ \text{其难度与原问题同阶 ⚠️}\ \big(\text{档案之反复教训 ✓：攻缺口＝攻墙}\big);\ \text{唯本路线上界侧健全 ✓（C-476 ✓），故\ \textbf{形态}优于 C-472 ✗}$$
$$\textbf{（可达工具 ✓ 登记）}:\ \text{① 极大 (10,4)-码之\ \textbf{结构}（文献 ✓ 可取）⟹ 再作 blocking/extension 引理 ✓};\ \text{② min-edge 之\ \textbf{Delsarte-LP}（新 LP ✗ 未建）};\ \text{③ 更强搜索（退火／精确 ✗ 本档未做）}$$
$$\qquad\textbf{（风险 ✓）}:\ \text{若某极大码存在 4 个\ \textbf{两两相距 \ge4 且外部度 1} 之点 ⟹ }m(44)\le4{+}(\text{内部边})\le7\ ⟹\ \text{P1 \textbf{死} ✗✓}$$

## §2 状态（**照唐先生之修正 ✓✓**）

$$\boxed{\text{奇偶分层 }✓\quad 44\le a,b\le75\ ✓\quad L_E,L_O\ \text{上界}\ ✓\quad p_E,p_O\ \text{恒等式}\ ✓\quad p_E,p_O\ \text{上界}\ ✓}\ ✓✓$$
$$\boxed{\lambda_{\min}{=}-5\ \text{之谱下界}\ ✗\ \big(\text{废弃 ✓}\big)\quad m(44)\ge8\ \text{OPEN}\ ⚠️\quad m(45)\ge31\ \text{OPEN}\ ⚠️\quad \text{blocking/extension 引理 OPEN}\ ⚠️}$$
$$\qquad\Longrightarrow\ \text{唐先生之修正\ \textbf{接受} ✓✓}:\ \boxed{\text{P1 已形成，但 quantitative lower bound 尚未形成}}\ ✓\ \text{（与"整体无攻击点"不同 ✓）}$$
$$\qquad\textbf{（本档补充 ✓）}:\ \text{该 P1 之\ \textbf{定量核}＝极大码之外部度结构 ✗（未定）；且本档证明\ \textbf{现成启发式不够}（29 vs 40 ✗）⟹ 须走\ \textbf{结构路线} ✓（照唐先生 §10 ✓）}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "极值码结构" "阻断容量" "最小边数问题"
技术词 极值码结构   命中文件数=0    ::
技术词 阻断容量     命中文件数=0    ::
技术词 最小边数问题 命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 极值码结构 | 0 | 0 | ✓（自造标签 ✓） |
| 阻断容量 | 0 | 0 | ✓（自造标签 ✓） |
| 最小边数问题 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **有限穷举／局部搜索** ✓（$\frac12Q_{10}$ 之 512 点／度 45 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处能力边界之实测**（启发式不达极值 ✗✓）＋ **一处关键算术**（均值 3.814 ✓）已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $m(44)\ge8$ ✓✗（未定 ⚠️）；**不声称** P1 死 ✗（V290）
