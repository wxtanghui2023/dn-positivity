# 🎯 PLAN-119 —— **目标（正名）／资产账／缺口／方法组合／我的工作流**

> **性质**：**规划（不产生新数学）**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 20:05 ✓　**唐先生令（四点）**：目标正名／资产-需求-缺口／方法组合／我的使用方案 ✓
> **关系**：本档为 `MASTER-FAILURE-MAP-107-LINE.md` 之**上位**（后者只防重复；本档管方向）✓

**已查地图**：`WITW2C`（$\mathcal L_9(U)$ 定义）／`ASSETS-REGISTRY` L1997（目标形式）／`kopt` 体系／`PLAN-2026-09-25` ✓

D0: 本档对象 ＝ **档案已有**（$\mathcal L_9$／资产／构造族—皆在档 ✓）
D1: 0（产出＝**一次目标正名 ＋ 资产-缺口表 ＋ 工作流** ⚠️✓）

---

## §1 ①**最终目标（正名）**

$$\boxed{\text{判定}:\ \exists\ \text{9-cover }U\subseteq Q_9\ \text{使}\ \mathcal L_9(U)\le119\ ?}\qquad(\mathcal L_9=\text{9 维\textbf{双色加权 2-覆盖}最轻配置})$$
$$\text{YES}\ \Longrightarrow\ K(10,1)\le119\ \Longrightarrow\ \textbf{改进已发表上界 }120\to119\ (\text{真新结果}✓)$$
$$\text{NO}\ \Longrightarrow\ K(10,1)\ge120\ \Longrightarrow\ \text{与手中 120-cover 合}\ \Longrightarrow\ \boxed{K(10,1)=\mathbf{120}\ \text{精确确定}}✓✓$$
$$\textbf{而 }107/120\ \text{复现}\ =\ \textbf{仅为学技术手段};\ \textbf{不是目标}✗\ (\text{唐先生 2026-09-29 19:59})$$

## §2 ②**资产-需求-缺口**

### 已有（✓ 可核）
| 资产 | 内容 | 出处 |
|---|---|---|
| **120-cover 证书** | 我方自构，可复跑，覆盖 1024/1024 | `sources/K10-1-120-cover-CERTIFICATE.txt` |
| **快速精确校验器** | 覆盖半径判定 | 本线脚本 |
| **$K(9,1){=}62$ 最优码 ×2** | 9 维最优 | `sources/KERI-CD-K_9_1-*` |
| **★ 目标形式** $\mathcal L_9(U)$ | 119 $\iff$ $\exists U:\mathcal L_9(U)\le119$ | `ASSETS-REGISTRY` L1997／`WITW2C` |
| **fiber 精确重述** | $C_0\sqcup C_1$，$a{+}b{=}119$，$D_A\subseteq B$，$D_B\subseteq A$ | `WITFIB` |
| **缺陷机制＋已证引理** | $\mathrm{Def}(A)\ge2(a-40)$ ✓；$K(5,1){=}7$✓、$K(6,1)\ge12$（我方递归自证）✓ | `RESULT`／`CALIBRATE-n*` |
| **kopt 引擎** | delete-refill／1-for-1 swap；$k{=}2$ **真完备**（$C(124,2){=}7626$ 全枚举，无出口） | `kopt*` |
| **局部搜索** | remove-repair（$n{=}9$ 得 66，差 6.5%） | `CALIBRATE-K9*` |
| **文献构造章（未打开）✗★** | Struik 1994 ch.4：直接和／**融合直接和 ADS**／normal-subnormal／piecewise constant／Golay／block designs | `sources/TUe-...pdf` |

### 需要（逐环节）
$$\textbf{构造侧}:\ \text{（i）从 120-cover 的 \textbf{1-for-1 替换}（允许"移动"，非仅增删）};\ \text{（ii）混合码参数优化};\ \text{（iii）ADS 构造代数}$$
$$\textbf{排除侧}:\ \forall\ \text{9-cover }U:\ \mathcal L_9(U)\ge120\ \text{之证明};\ \text{环节需求 ＝ \textbf{Q}_9\text{ 规模的独立缺陷定理}}$$
$$\text{两侧共同}:\ \text{每步须产出\ \textbf{可复跑证书} 或 \textbf{明确读数}}✓$$

### 缺口（✗ 目前没有）
$$\text{（1）119-cover 本身（未知）};\quad \text{（2）}Q_9\ \text{规模独立缺陷定理（only }Q_5/Q_6\ ✓,\ Q_9\ \text{未果）}✗$$
$$\text{（3）压缩 }Q_9\ \text{枚举之方法（}2^{256}\text{）}✗;\quad \text{（4）文献构造技術之\ \textbf{可执行化}（ch.4 未读）✗★}$$

## §3 ③**可用方法 ＋ 组合（关键诊断）**

$$\boxed{\text{诊断}:\ \textbf{目标在\textbf{上界（构造）}侧};\ \text{而我们近期全部精力在\textbf{下界（排除）}侧}\ \Longrightarrow\ \textbf{资产/方法错配}✗✓}$$

$$\textbf{(C1)}\ \text{120-cover}\ \otimes\ \text{1-for-1 替换（kopt 升级：允许移动）}\ \to\ 119?$$
$$\textbf{(C2)}\ \text{混合码构造（}F_4\times F_2^7\ \text{型，60 词）参数优化}\ \to\ 119{=}60{+}59\ \text{不对称?}$$
$$\textbf{(C3)}\ \text{ADS}\bigl(K(9,1){=}62\ \text{码},\ \cdot\bigr)\ \text{构造代数}\ \to\ 119?$$
$$\textbf{(C4)}\ \text{（排除侧）}\ \mathcal L_9(U)\ge120\ \text{之证明 ← 需缺口(2)}$$
$$\text{可用方法储备}:\ \text{直接和／ADS／normal-subnormal／piecewise constant／Golay／block designs／混合码};\ \text{我方: 精确枚举、证书、缺陷递归、kopt 引擎}$$

## §4 ④**我的使用方案（工作流）**

$$\textbf{角色① 技术转录员}:\ \text{把文献构造章逐条转录为\ \textbf{可执行构造库}（每构造 ＝ 一函数 ＋ 自测）}$$
$$\textbf{角色② 组合实验员}:\ \text{以构造库对 120-cover 做组合实验};\ \textbf{每实验产出可复跑证书}$$
$$\textbf{角色③ 读数报告员}:\ \text{排除侧先化为 ILP/枚举，}\textbf{如实报读数，不包装}$$
$$\textbf{硬性停止条件}:\ \text{每实验必须产出 (a) 可复跑证书 或 (b) 明确读数};\ \textbf{禁止再以"分析文档"充数}✗$$
$$\textbf{优先级}:\ \text{(C1)(C2)(C3) 先行（可达、可能直接出新结果）}\ \to\ \text{(C4)（难，需先补缺口(2)）}$$

## §5 边界（硬 ✓）

- **目标形式 $\mathcal L_9(U)$ 系档案原文（L1997／`WITW2C`）** ✓；**不占 C 号** ✓
- **本档为规划，不含数学结论**；**不主张** 119 存在/不存在 ✗（V290）
ROUTE-CHECK: R02=NA R05=NA R07=NA R11=NA R12=NA R13=NA
