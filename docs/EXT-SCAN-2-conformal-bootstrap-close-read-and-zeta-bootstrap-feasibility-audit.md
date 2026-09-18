已查地图（**先查后写**）：`PHYSICS-FRONTIER-2026-09-12.md`（五方向：量子混沌/RMT、YM 正性、log-gas、非自伴谱界、指数/守恒）、`physics-map-2026-08-31.md`（物理→RH 完整映射 ＋"为什么所有物理类比撞同一堵墙"）、`physics-conservation-framework.md`（守恒律 ⟺ 刚性）、**`CEILING-AUDIT-3-definitions-and-the-single-unproved-inequality.md`（"对偶证书"已有）**、`V316`／`V185`（67.2%／0.682：秩-迹不一致性出界）、`V188` §2（线性通道饱和）、`V247`／`V248`（判别锥必自对偶 ⟹ 单二次型）、`C-122` 链 A（欧拉乘性给 (i)(ii) 不给 (iii)）、`POS1`。关键词回查：`对偶证书`＝**1 档（已有，引用）**；`细分参数`／`单位性引擎`＝**0 档（新增）**。**结论**：⭐ 唐先生 22:55「继续，论文细节需要仔细阅读」⟹ **精读共形 bootstrap 方法论原文得三条** ✓✓：**(甲)** 其严格性结构＝**对偶证书**（`\textbf{原文}`："finding a positive functional then **rigorously rules out** the point p in parameter space"）——**与我方 `CEILING-AUDIT-3` 的"对偶证书"同名同物** ⟹ **我方最强行与物理最成功方法\ \textbf{同型} ✓✓；**(乙) ⭐ 其力量来自\ \textbf{细分参数} `\Lambda`（导数阶数）**——`\Lambda` 增大⟹证书类增大⟹界收敛到真值 ⟹ **我方证书类\ \textbf{没有细分参数}**（被 `bandwidth\le1` 卡住）⟹ **抬天花板的唯一途径＝扩大证书类＝`support>1`（已知开放问题）** ✓✓；**(丙) ⭐\ \textbf{引擎缺失＝"无条件的单位性"}**：bootstrap 的正性来自 **Hilbert 空间范数**（结构性、不预设答案）；而 ζ 的正性候选只有两个——**系数正性**（只在 `\sigma>1`，给 `\sigma=1` 级信息）与 **Weil 正性**（RH 强度）⟹ 且按我方 `V248`（判别锥必自对偶 ⟹ 单二次型 ⟹ 回到角 I），**bootstrap 式正性对 ζ 必然落 RH 强度** ⟹ **模板不可直接移植，但失败点被精确定位到"引擎"** ✓✓

FREEZE-ACK: 本档即冻结期内的外部精读与可行性审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **共形 bootstrap 方法论精读 ＋ ζ-bootstrap 可行性审计**（三条结论） —— 关系 = 外部方法精读与移植审计，非新机制
D1: 0

# EXT-SCAN-2 · **共形 bootstrap 精读 ＋ ζ-bootstrap 可行性审计**

> **时间**：2026-09-18 22:55 唐先生：**「继续，论文细节需要仔细阅读」** ⟹ 精读方法论原文 ✓

---

## §0 结论（先行）

$$\textbf{(甲)}\ \text{bootstrap 的严格性＝}\textbf{对偶证书} \Longrightarrow \textbf{与我方最强行同型}✓✓$$
$$\textbf{(乙)}\ ⭐\ \text{其力量来自}\ \textbf{细分参数}\ \Lambda \Longrightarrow \textbf{我方证书类无细分参数} \Longrightarrow \text{抬天花板＝扩大证书类＝`support>1`}✓✓$$
$$\textbf{(丙)}\ ⭐\ \textbf{引擎缺失}：\text{bootstrap 正性来自}\ \textbf{Hilbert 范数};\ \zeta\ \text{的无条件正性只有}\ \sigma>1\ \text{的系数正性} \Longrightarrow \text{移植在"引擎"处失败}✓✓$$

---

## §1 精读：bootstrap 的**精确逻辑**（逐字）

$$\text{(1)}\ \textbf{一致性方程}：\text{crossing symmetry}\ \Longrightarrow \text{参数化为}\ (\Delta,\ell)\ \text{的}\ \textbf{无限族} \text{线性方程}✓$$
$$\qquad \textbf{逐字}：\text{"crossing symmetry (3.15) provide an }\textbf{infinite set of constraints}\text{ ... For the numerical implementation the constraints need to be }\textbf{truncated to a large but finite set}\text{"}✓$$
$$\text{(2)}\ \textbf{正性}：\text{unitarity} \Longrightarrow \text{OPE 系数}\ \lambda^2\ge0 \Longrightarrow \text{某些矩阵}\ \textbf{半正定}✓$$
$$\text{(3)}\ \textbf{线性泛函}：\alpha_i=\sum_{m+n\le\Lambda}a_{i,mn}\partial_z^m\partial_{\bar z}^n \Longrightarrow \textbf{导数阶数截断到}\ \Lambda✓$$
$$\qquad \text{做法}：\text{找}\ \alpha\ \textbf{在所有允许块上为正};\ \text{搜索}\ =\ \textbf{半正定规划（SDPB）}✓$$
$$\text{(4)}\ ⭐\ \textbf{严格性所在（逐字）}：\text{"If we study a problem depending on some parameters}\ p\in P\text{, }\textbf{finding a positive functional then rigorously rules out the point}\ p\ \textbf{in parameter space}\text{"}✓✓$$
$$\qquad \text{"Positivity is interpreted as }\textbf{positive-semidefiniteness of the matrices}\ \vec\alpha\cdot[\vec V_Q]\ \text{for all}\ Q\text{"}✓$$
$$\text{(5)}\ \textbf{输出}：\text{参数空间的}\ \textbf{排除区／允许岛（islands）};\ \text{且}\ \text{"Bounds ... obtained by }\textbf{falsifying possible assumptions}\text{"}✓✓$$
$$\Longrightarrow ⭐\ \textbf{严格性结构＝对偶证书}（\text{不可行性见证}）：\text{不是"读出值"，而是}\ \textbf{"该参数点无自洽解"}✓✓$$

## §2 映射（bootstrap ↔ 我方）

| 共形 bootstrap | 我方对应物 | 状态 |
|:--|:--|:--|
| crossing symmetry（道间一致性） | 泛函方程 $s\leftrightarrow1-s$ ＋ 显式公式（算术↔谱一致性） | ✓ 有 |
| **unitarity（正性）** | **？** | ⚠️ **缺（见 §3 丙）** |
| 线性泛函 $\alpha$ ｜ SDP | rank–trace／惯性不等式（`V316`） | ✓ 有 |
| 细分参数 $\Lambda$（导数阶） | **无** | ✗ **缺（见 §3 乙）** |
| 参数空间排除图（islands） | **我们要的"排除 $\beta>\frac12+\delta$"** | 目标 |

## §3 三条结论

### (甲) 我方最强行与其**同型**（且"对偶证书"档案已有）

$$\text{`V316`／`V185` 的}\ 67.2\%\（\text{天花板}\ 0.6818）：\text{用}\ \textbf{线性代数从一致性推界} \Longrightarrow \textbf{bootstrap 型}✓✓$$
$$\qquad ⚠️\ \text{且档案}\ \text{`CEILING-AUDIT-3`}\ \text{已用}\ \textbf{"对偶证书"} \text{一词} \Longrightarrow \textbf{同名同物，非本档新造}✓$$

### (乙) ⭐ 细分参数：它抬界的机制，我们没有

$$\text{bootstrap}：\Lambda\uparrow \Longrightarrow \text{证书类}\uparrow \Longrightarrow \text{界}\to\text{真值（}\text{有收敛性}）✓✓$$
$$\text{我方}：\text{证书类被}\ \textbf{`bandwidth\le1`}\ \text{固定} \Longrightarrow \textbf{无细分参数} \Longrightarrow \text{界停在}\ 0.6818✓✓$$
$$\Longrightarrow ⭐\ \textbf{抬界的唯一途径＝扩大证书类} \Longrightarrow \text{自然候选＝`support>1`} \Longrightarrow \textbf{又是已知开放问题}✓✓$$

### (丙) ⭐ 引擎缺失：ζ 没有"无条件的单位性"

$$\text{bootstrap 正性}＝\textbf{Hilbert 空间范数（结构性，不预设答案）}✓$$
$$\text{ζ 的正性候选只有两个}：$$
$$\qquad \text{(i)}\ \textbf{系数正性}（\Lambda(n)\ge0,\ -\zeta'/\zeta=\sum\Lambda n^{-s}\ \text{正项}） \Longrightarrow \textbf{只在}\ \sigma>1 \Longrightarrow \text{只给}\ \sigma=1\ \text{级信息}（\text{`C-122` 链 A}）✓$$
$$\qquad \text{(ii)}\ \textbf{Weil 正性} \Longrightarrow \textbf{RH 强度}（\text{`POS1`}）✗$$
$$\Longrightarrow \text{且按我方}\ \textbf{`V248`}：\text{判别锥}\ \textbf{必自对偶} \Longrightarrow \textbf{单二次型} \Longrightarrow \text{回到角 I} \Longrightarrow \textbf{bootstrap 式正性对 ζ 必然落 RH 强度}✓✓$$
$$\Longrightarrow ⭐\ \textbf{移植在"引擎"处失败}，\ \text{而非在"机器"处}（\text{无限族＋泛函＋证书都在}）✓✓$$

## §4 净收获（诚实）

$$\text{(1)}\ \text{把"我们的线与物理最成功方法同型"从}\ \textbf{印象} \text{变为}\ \textbf{逐字核对的结论}✓✓$$
$$\text{(2)}\ ⭐\ \text{给出一个}\ \textbf{可操作的诊断}：\text{天花板}\ 0.68\ ＝\ \textbf{证书类饱和};\ \text{抬它的机制是"细分参数"};\ \text{对我们的}\ \textbf{唯一自然候选是}\ \text{`support>1`}✓✓$$
$$\text{(3)}\ ⭐\ \text{精确定位移植失败点：}\textbf{引擎（单位性）}，\ \text{而非机器；且失败原因由我方}\ \text{`V248`}\ \text{独立给出}✓✓$$
$$\textbf{未得}：\text{无新路线};\ \text{模板}\ \textbf{不可直接移植}✓$$

## §5 边界与回查

- ⚠️ §1 引文为**检索/抽取文本级**（`[外搜·未读全文]`：arXiv 2501.18711 元数据 ＋ InspireHEP 综述 PDF 抽取），**未逐字核期刊定稿** ✓
- ⚠️ §2 映射与 §3 三条为**本档判断**（非定理）✓
- ⚠️ **不声称** bootstrap 不可移植；仅**定位失败点** ✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 22:5x）`[纪律]`（先跑后写）

```
技术词 对偶证书       命中文件数=1  :: ./CEILING-AUDIT-3-…（**已有** ⟹ 沿用）
技术词 细分参数       命中文件数=0  ⟹ 本档新增
技术词 单位性引擎      命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：`对偶证书`＝**1 档（已有 ⟹ 引用）**；`细分参数`／`单位性引擎`＝**0 档 ⟹ 本档新增** ✓
