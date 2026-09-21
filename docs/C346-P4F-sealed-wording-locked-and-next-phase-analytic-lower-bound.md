已查地图（**先查后写**）：`C-345`（P4-F ✓✓）、`C-344`（全域搜索 ✓）、`C-343`（straddling 判据 ✓✓）、`C-342`（`E` 非空且宽 ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-346：P4-F 封口 ＋ 措辞锁定 ＋ 下一阶段（解析下界）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① 措辞锁定}✓✓：\text{正确表述}＝\ f_{best,E} = \textbf{1.3626}✓（\text{6 次}\ E\ \text{内硬约束搜索的当前最小值}✓），\ \textbf{不是} \ f_*✓、\textbf{不是} \text{全局下确界}✗✓$$
$$\textbf{② } E\ \text{内突破确立}✓✓：6/6\ E\text{-ok}✓，0\ \text{个反例候选}✗✓，\text{裕量}\ 1.3626 - \tfrac12 \approx \textbf{0.8626}✓✓$$
$$\textbf{③ 关键比较}✓✓：f_{best,E} \approx 1.3626 \ > \ f_{best,all} \approx 1.01065✓（\text{C-344}✓），\text{差} \approx 0.352✓ \ \Longrightarrow \text{仅可称}\ \textbf{数值机制证据}✓✓，\textbf{不}可称解析蕴含✗✓$$
$$\textbf{④ 下一阶段}✓✓：\textbf{解析下界}✓ \ —— \text{目标}\ \exists c > \tfrac12\ \text{使}\ f(x,\sigma) \ge c\ \forall x \in E✓；\text{例}：\text{若只得}\ c = \tfrac35✓ \ \text{亦足以推出}\ H = \varnothing✓✓$$

## §1 封口定位段（**逐字采用唐先生表述** ✓✓）

> **P4-F 数值阶段完成：E 的可行性入口已通过硬约束搜索验证；在 6 个独立 E 内优化运行中，奇频目标均显著超过 1/2，当前最佳值为 1.3626，未发现反例。该结果强烈支持全域 straddling，但尚不构成全域证明。下一阶段转入解析下界。**

$$\textbf{纪律}✓✓：\ \textbf{P4-F 不再重复跑}✗✓；\textbf{不}\ \text{写成「已证明全域 straddling」}✗；\textbf{不}\ \text{写成}\ f_* = 1.3626✗$$

## §2 状态锁定（✓✓）

| 档 | 结论 ✓ |
|---|---|
| `C-342` ✓ | **偶频 `E` 非空且宽** ✓✓ |
| `C-343` ✓ | **`E` 内单点出现奇频 straddling** ✓ |
| `C-344` ✓ | **全域搜索未击穿，但未有效覆盖 `E`** ✓ |
| `C-345` ✓ | **`E` 已可靠进入；奇频仍有巨大突破** ✓✓ |
| **下一步** ✓ | **解析下界** ✓✓ |

## §3 下一阶段目标（✓✓，登记不执行 ✓）

$$\textbf{要证}✓✓：\ \inf_{x \in E,\ \sigma \in \{\pm 1\}^5} \max_{0 \le r \le 12} \Big| \sum_{j=1}^{5} \sigma_j \sqrt{x_j}\, R_r(x_j) \Big| \ > \ \tfrac12✓$$
$$\textbf{攻击形态}✓：\text{不求}\ 1.3626✗（\text{数值上界}✓）；\text{只求}\ \textbf{某明确常数}\ c > \tfrac12✓✓ \Longrightarrow \text{门槛低、路更宽}✓✓$$
$$\textbf{已备工具}✓：\text{straddling 判据}✓（C-343✓）\ ＋\ \text{偶频矩／Hankel 结构}✓（C-341／C-342✓）\ ＋\ \text{符号层分解}✓ \ —— \ \textbf{不}\ \text{引入新框架}✗✓$$
$$\textbf{禁项}✓✓：\textbf{不}\ \text{扩频率}✗、\textbf{不}\ \text{拆}\ SOS✗、\textbf{不}\ \text{追}\ G_*✗、\textbf{不}\ \text{重跑}\ P4\text{-}A \sim F✗、\textbf{不}\ \text{重开}\ C\text{-}284✗$$

## §4 边界（✓✓）

$$\textbf{不得}\ \text{写成}✗：\text{全域 straddling 已证}✗；\ H = \varnothing\ \text{已证}✗；f_* = 1.3626✗；\text{偶频路线已死}✗$$
$$\textbf{诚实标注}⚠️✓：\text{6 个}\ E\ \text{内点}\ \textbf{不构成} \text{全域证明}✗；\ f\ \text{在}\ E\ \text{上的下确界}\ \textbf{未确认}✗；\text{但}\ \text{数值机制}\ \textbf{强支持}✓✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 封口档        命中文件数=0    :: 
技术词 解析下界阶段 命中文件数=0    :: 
技术词 措辞锁定     命中文件数=2    :: ./C204-T13-A-YI-1-cluster-separation.md ./C205-T13-A-YI-2-three-cluster-suite-mechanism-shared-constants-not-uniform.md 
```
- **零计算** ✗（封口档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
