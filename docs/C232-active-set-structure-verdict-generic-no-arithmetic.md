已查地图（**先查后写**）：查 `C-231`（甲线冻结）、`C-230`（最终闭合）、`C-153`（lcm-12 恒等式）、`C-200`（T13-B2 等号集）、`C-207`（连续族排除）。回查见 §6 ✓

D0: 本档对象 = **active-set 结构的判定**（"5 维为何恰 6 个 active branches" 的解答：通用几何，无算术结构）—— 关系 = 结构性负面判定 ＋ 价值判据登记
D1: 0
FREEZE-ACK: 本档即冻结期内的判定与登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 判定（先行）

$$\boxed{\text{"5 自由度}\to\text{6 个正权 active branches"}\ \text{是【通用非光滑极小极大几何}】✓，\textbf{不含算术结构}✗✓}$$
$$\textbf{分解}：\textbf{① }|A|\ge d+1\ ⟸\ \text{Carathéodory}✓（0\in\mathrm{int}\,\mathrm{conv}\{\nabla S_k\}\subset\mathbb R^d\ \text{至少需}\ d+1\ \text{点}✓）——\textbf{被迫，无信息}✗$$
$$\qquad \textbf{② }|A|=d+1\ ⟸\ \text{非退化（无冗余）}✓——\textbf{generic，无信息}✗$$
$$\qquad \textbf{③ 具体是哪些 }k\ ⟸\ \text{可被【通用机制】解释}✓：r_1=1\ \text{坐标不衰减（偏窗口端点 }k=15✓）＋\ r_2,r_3\ \text{阻尼（偏小 }k=1..5✓）$$
$$\qquad \Longrightarrow \text{无需算术结构即可完全解释}✗ \Longrightarrow \textbf{价值判据：【不能】升级为 }M\text{-一般定理}✗$$

## §1 三个高精度探针（全部阴性 ✓）

$$\textbf{① 梯度核}✓：6\ \text{个 }5\ \text{维向量} \Longrightarrow \text{Gram 最小特征值} \approx -6.4\times10^{-60}✓（\text{核为 1 维}✓）$$
$$\qquad \text{核向量（归一）}=(1.0,\ 0.8921986486846397,\ 0.8273281320004751,\ 0.9738318490406051,\ 0.5591506038258176,\ 0.7461497392009032)✓$$
$$\qquad \text{PSLQ(maxcoeff }10^6/10^8/10^{10}）= \textbf{None}✗✗ \Longrightarrow \text{核方向【无理}】✗ \Longrightarrow \text{无算术关系}✗$$
$$\textbf{② 半径代数性}✓：r_2,r_3\ \text{次数}\le10\ \text{无整系数多项式关系}（maxcoeff\ 10^{10}）✗ \Longrightarrow \text{非低次代数数}✗$$
$$\textbf{③ 相位有理性}✓：\text{PSLQ}(1,\varphi_1/\pi,\varphi_2/\pi,\varphi_3/\pi,\ \text{maxcoeff}\ 10^6)= \textbf{None}✗ \Longrightarrow \text{非单位根}✗ \Longrightarrow \textbf{无}\ \mathrm{lcm}\ \text{结构}✗$$

## §2 ⚠️ 方法论陷阱（必须记录 ✓）

$$\textbf{陷阱}✗：\text{PSLQ 对【有理截断输入】必然找到格关系}✗（20\ \text{位小数是有理数} \Longrightarrow \text{必有整关系}✓）$$
$$\qquad \text{首次跑}：\text{阻尼用 20 位截断} \Longrightarrow \text{PSLQ 报出 }[939121,-2840920,680965,-2572972]✗（\text{代回残差恰为 }0✗）$$
$$\qquad \text{且}\ \text{"}\Sigma=0.0\text{"}\ \text{看起来像真关系}✗ \Longrightarrow \textbf{极易误判}✗✗$$
$$\textbf{解药}✓：\text{用【高精度重算的根】复跑}✓：\text{Newton 3 次（残差 }4.7\times10^{-81}✓）\Longrightarrow \text{PSLQ}=\textbf{None}✗ \Longrightarrow \text{前一步确认是截断伪影}✓✓$$
$$\qquad \Longrightarrow \textbf{规则}：\text{凡用 PSLQ 判"结构"，必须先重算到}\ \ge50\ \text{位，并同时报残差}✓$$

## §3 ⭐ 对照：算术结构出现在哪里（二分 ✓）

| 构型 | 相位 $\varphi_j/\pi$ | 有理？（maxcoeff $10^6$） | 结论 |
|---|---|---|---|
| **M=2 $(\pi/3,\pi/2)$** | $1/3,\ 1/2$ | **是** ✓（PSLQ $=[1,0,-2]$ ✓） | **单位根 ⟹ 有算术结构** ✓：$\mathrm{lcm}(6,4)=12$，恒等式 $7g_5+5g_7=0$ ✓（`C-153`），等号集＝本原根 ✓（`C-200`） |
| 无阻尼 M=3（T13-A） | 0.1158…, 0.3319…, 0.7356… | 否 ✗ | 一般几何 ✗ |
| 阻尼 M=3（甲线） | 0.1091…, 0.8207…, 0.4617… | 否 ✗ | 一般几何 ✗ |

$$\Longrightarrow \textbf{二分}✓：\text{算术结构}\iff\text{极值构型落在【有理相位}】✓（\text{单位根}✓） \Longrightarrow \text{周期性恒等式}✓$$
$$\qquad \text{而两个 M=3 极值构型均为【非有理相位}】✗ \Longrightarrow \text{无结构}✗✓$$
$$\textbf{注}：\text{该二分的正命题（有理相位} \Longrightarrow \text{周期恒等式）接近经典事实}✓，\textbf{新颖度低}✗ \Longrightarrow \text{不足以支撑独立论文}✗$$

## §4 价值判据（按唐先生 2026-09-20 18:01 口径 ✓）

| 层级 | 判据 | 本线现状 |
|---|---|---|
| 1 | 只证 $C_3$ 与两个 minimizers | ✅ **已达成**（扎实但有限 ✓） |
| 2 | 找到并证明 active-set 的**一般机制** | ✗ **已判否**：机制是通用的，无算术结构 ✓ |
| 3 | 机制进一步给出 $C_M$／active indices／minimizer 的一般定理 | ✗ **本路不通** |

$$\Longrightarrow \textbf{本线作为"结构实验室"的入口已关闭}✗（\text{负面结论，但干净}✓）$$
$$\qquad \textbf{甲线资产不变}✓：\text{仍为 level-1 的严格 }M=3\ \text{结果}✓（\text{已冻结}✓，\text{不因本判定而改动}✓）$$

## §5 仍未被否的可能（登记备用 ✓，均非本路 ✓）

$$\textbf{① }C_M\ \text{的渐近规律}✓（\text{纯数值/半严格}✓，\text{不依赖算术结构}✓）$$
$$\textbf{② 阻尼参数的 phase transition}✓（\text{active set 随 }(r_2,r_3)\ \text{变化的相图}✓）$$
$$\textbf{③ 一般 }M\ \text{的 }|A|=d+1\ \text{非退化性定理}✓（\text{Carathéodory＋横截性}✓，\text{可能是可发表的【一般几何}】结果✗\text{但与算术无关}✓）$$

## §6 边界与出处

$$\textbf{① 本档为判定与登记}✓，\text{不含新数学}✓；\textbf{② 阴性结果}✗（\text{PSLQ 上限}\ 10^{10}✓，\text{不构成"绝对无关系"的定理}✓）$$
$$\textbf{③ 未用 RH}✓；\text{未改他档}✓（\text{甲线冻结不受影响}✓）$$
$$\textbf{④ 探针脚本}：\text{内联 heredoc}✓（\text{未单独落盘}✗，\text{如需复现可据本档 §1 重建}✓）$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 截断伪影           命中文件数=1  ::  ./C232-active-set-structure-verdict-generic-no-arithmetic.md
技术词 有理相位二分       命中文件数=1  ::  ./C232-active-set-structure-verdict-generic-no-arithmetic.md
技术词 结构实验室入口关闭   命中文件数=1  ::  ./C232-active-set-structure-verdict-generic-no-arithmetic.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
