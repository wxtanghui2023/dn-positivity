已查地图（**先查后写**）：查 `C-253`（证书完成）、`C-251`、`C-250`、`C-238`、`C-233`（数值表）。回查见 §6 ✓

D0: 本档对象 = **C-254：B2-1 FROZEN/CLOSED 登记 ＋ 方法论模板 ＋ 数值核验** —— 关系 = 冻结登记
D1: 0
FREEZE-ACK: 本档即冻结期内的冻结登记（依 §8.1；不产候选结论）

---

## §0 登记

$$\boxed{\textbf{B2-1：FROZEN，CLOSED}✓✓✓（2026-09-20✓）}$$
$$\boxed{\forall w\ge5,\qquad g_w(10)\ =\ w\cos\frac{2\pi}{11}\ -\ \cos\frac{\pi}{11}\ ✓✓✓}$$
$$\textbf{证明结构}✓：\underbrace{\text{C-238 上界}}_{\text{初等}✓}\ +\ \underbrace{\text{C-250 Case II}}_{|\varepsilon|<0.1/w✓}\ +\ \underbrace{\text{C-251/C-253 Case I}}_{|\varepsilon|\ge0.1/w✓}\ \Longrightarrow\ \text{CLOSED}✓✓$$

## §1 数值核验（本档新增，回答唐先生量纲问题 ✓✓）

$$\cos\frac{2\pi}{11}=\cos(32.727°)=\boxed{0.841253532831}✓✓\qquad \textbf{唐先生所用}\ 0.1423\ \textbf{系误值}✗✗$$
$$\qquad (\text{推测来源}：\text{角单位混淆}✓；0.1423\approx\cos(81.83°)✓，\text{非任何自然角}✓)$$
$$\cos\frac{\pi}{11}=\cos(16.364°)=0.959492973614✓\qquad \Longrightarrow\ g_w(10)=w(0.8412535)-0.9594930✓$$
```
     w        w·cos(2π/11)      −cos(π/11)        g_w(10)
     5         4.206267664      -0.9594929736     3.246774691  ← 正数 ✓✓
     6         5.047521197      -0.9594929736     4.088028223
    10         8.412535328      -0.9594929736     7.453042355
    20        16.825070660      -0.9594929736    15.865577680
   100        84.125353280      -0.9594929736    83.165860310
  1000       841.253532800      -0.9594929736   840.294039900
```
$$\textbf{双重独立对照}✓✓：\text{(i) C-233 数值表}\ w=5\ \text{时}\ g_w/w=0.649\Longrightarrow3.2468✓✓；\text{(ii) 渐近}\ g_w/w\to\cos\frac{2\pi}{11}=0.8413✓✓$$
$$\Longrightarrow \textbf{定理数值自洽}✓✓（\text{唐先生的}\ \cos(2\pi/11)=0.1423\ \text{是唯一错值}✗）$$

## §2 方法论模板（本档提炼，唐先生指定保留 ✓✓）

$$\boxed{\text{模板 A}：\ \text{错误的统一曲率界}\ \longrightarrow\ \text{branch-consistent 不对称曲率}\ \longrightarrow\ \text{可证明的全局门槛}✓✓}$$
$$\qquad \text{具体}✓：\text{尖点}\ F(\theta_j+\varepsilon)-\kappa=s_j\max(-a_j\varepsilon,+b_j\varepsilon)+\cdots✓\ \textbf{不可}✗\ \text{压成}\ c_j|\varepsilon|-C\varepsilon^2✓$$
$$\qquad \qquad \text{因两侧 binding 分支不同} \Longrightarrow \text{曲率分别为}\ \tfrac{a_j^2\kappa}2,\ \tfrac{b_j^2\kappa}2✓✓（\text{统一取}\max^2\Longrightarrow\text{高估}\sim100\times✗）$$
$$\boxed{\text{模板 B}：\ \text{数值发现}\ \longrightarrow\ \text{有限分割证书}✓✓}$$
$$\qquad \text{具体}✓：\text{候选点}=\{\text{全部分支交点}\}\cup\{\text{约束边界}\}✓✓；\text{段内单一分支}\Longrightarrow\text{极小在端点}✓；\text{闭集（含边界}✓）$$
$$\qquad \qquad \text{陷阱}✗：\text{单位混用}✗、\text{边界被浮点过滤}✗、\text{"数值通过"冒充证书}✗$$

## §3 审计 errata（5 项，保留不隐藏 ✓✓）

| # | 错误 | 类别 | 是否残留 |
|---|---|---|---|
| 1 | $\zeta$ 符号配对反 | 实现/推导 | ✗ 无残留（C-250 ✓） |
| 2 | $\eta$ 顺序（对抗 vs 最小） | 逻辑 | ✗ 无残留（C-250 ✓） |
| 3 | $\varphi$ 与 $\varphi/\pi$ 单位混用 | 实现 | ✗ 无残留（C-253 ✓） |
| 4 | 空值短路（枚举漏点） | 实现 | ✗ 无残留（C-248 ✓） |
| 5 | 先提交后修正 | 纪律 | ✗ 无残留（C-253 fix ✓） |

$$\Longrightarrow \textbf{5 项全部纠正且未进入最终证明链}✓✓ \Longrightarrow \textbf{不降低 C-253 的证明状态}✓✓，\text{作为审计 errata 保留}✓$$

## §4 停止条件（唐先生指定，自我施加 ✓✓）

$$\boxed{\textbf{不再优化本证明的常数}✗✓，\text{除非为了【形式化}】✓\ \text{或【压缩证明文本}】✓}$$
$$\qquad \text{允许}✓：\text{形式化（区间/代数数精确比较}✓、Lean 化 ✓）｜\text{证明文本压缩}✓$$
$$\qquad \text{不允许}✗：\text{再推更高精度}✗｜\text{找更漂亮的常数}✗｜\text{重开已闭合环节}✗$$
$$\textbf{停止性质}✓✓：\text{【判断式停止}】✓（\text{证明链完整后主动收手}✓）\ \textbf{而非【撞墙式停止}】✗$$

## §5 状态表

| 项目 | 状态 |
|---|---|
| Exact upper bound | ✓✓ |
| 11-grid localization | ✓✓ |
| Case II | ✓✓✓ |
| Case I local cusp | ✓✓✓ |
| Case I far region（有限分割证书） | ✓✓✓ |
| **B2-1 数学结论** | **✓✓✓** |
| **完整审计级证明文本** | **✓✓** |
| **冻结状态** | **FROZEN / CLOSED** |

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 方法论模板A            命中文件数=1  ::  ./C254-B2-1-FROZEN-CLOSED-registration-and-methodology-template.md
技术词 判断式停止            命中文件数=1  ::  ./C254-B2-1-FROZEN-CLOSED-registration-and-methodology-template.md
技术词 审计errata保真        命中文件数=1  ::  ./C254-B2-1-FROZEN-CLOSED-registration-and-methodology-template.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓

## §7 边界

$$\textbf{① 未用 RH}✓；\text{未改他档正本}✓（\text{仅追加指针}✓）；\text{未塞回 }C_\infty✓$$
$$\textbf{② 本档为冻结登记}✓，\text{不新增数学结论}✓（\text{定理已在 C-253}✓）$$
$$\textbf{③ 数值核验顺带纠正唐先生一步误值}✗✓（\cos\frac{2\pi}{11}=0.8413✓，\text{非}0.1423✗）$$
