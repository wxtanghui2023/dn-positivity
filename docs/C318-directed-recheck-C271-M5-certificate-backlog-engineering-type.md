已查地图（**先查后写**）：`C-317`（`C-261`→CLOSED(reopen) ✓）、`C-316`（`C-260`→GAP CONFIRMED ✓）、`C-314`（协议 ✓）、`C-271`（正本：M=5／0.5 预算未闭合 ＋ 失败模式精确诊断 ✓）、`C-272`（待审箱审计：零反例 ＋ 粗箱积压 ✓）。回查见 §5 ✓

D0: 本档对象 = **C-318：`C-271` 定向回查（M=5 箱证书积压）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论

$$\boxed{\textbf{C-271}\ \to\ \textbf{GAP CONFIRMED}}✓（\text{工程型缺口，原状态保留}✓）$$
$$\text{原状态}✓：\textbf{SEARCH-BUDGET LIMITED}✓／\text{失败模式}\ \textbf{未定}✓／\textbf{非 FAIL}✗✓$$

## §1 协议（沿用 `C-314` ＋ 本组附加纪律 ✓）

四问 ✓；三出口 ✓：**REOPEN**／**GAP CONFIRMED**／**CLOSED**。
**附加纪律**（唐先生 ✓）：若证书最终闭合，**只证明证书闭合**✗；\textbf{不}自动升级为 RH bridge ✗；三层须分开 ✓：
$$\text{certificate completeness} \ne \text{new arithmetic mechanism} \ne \text{RH bridge}✓$$

## §2 `C-271` 原结论（✓，正本口径）

- 对象 ✓：**M=5，目标 0.5**，预算 20M（v4 严格引擎 ✓）
- 结果 ✓：**未闭合** （`neval 19,971,000`／认证 9,886,371／未决 226,948／`全部认证 = False`／`[STOP] 预算耗尽` ✓）
- 重判 ✓✓：**非"预算不足"**，而是 **"当前箱证书造成严峻认证积压"** ✓✓（依 `C-272`：待审箱中 `L < 1/2` 占 70.3%、采样上界 `> 1/2` 占 100.0%、**真反例 0** ✓；箱宽中位数 ≈ π/12 ✓）
- 会计勘误 ✓：226,948 ＝ 预算终止时"已弹出未评估"批 ✓；队内余 220,142 **未计入** ✓；实际未评估 447,090 ✓；全程 `unres=0` ⟹ **无隐藏认证失败** ✓
- 预注册 ✓：单次实验 M=5、目标 0.5、预算 60M ✓

## §3 四问回答（✓）

**① Failure carrier** 🟡 部分成立 —— 存在**具体载体** ✓：**待审箱集合** ✓（`C-272` 已落盘 670,091 箱 ✓，可枚举可检验 ✓）；**但它不是"禁形型 failure"** ✗ ⟹ 属**工程／算法型缺口** ✓✓
**② 两传播** ✗ —— 天然操作只有**箱二分（B&B split）** ✓（**一个** ✓）；两类证书（可分界 vs λ-混合 ✓）是**两种证书机制** ✗，\textbf{不是} 两个传播 ✗✓；**未见**第二个独立传播 ✓
**③ 兼容律** ✗ —— 未见 ✓
**④ 出口判定** ✓✓ —— ②③ 皆无 ⟹ \textbf{不进 FSD 入口}✗；旧结论**不变** ✓ ⟹ **GAP CONFIRMED** ✓（\textbf{不} REOPEN ✗、\textbf{不} CLOSED ✗ —— 因证书确实**未闭合** ✓）

## §4 补记（协议第④条要求 ✓）

1. **非 failure-型** ✓✓：本缺口不适用七类反例探针 ✓（与 `C-270`／`C-260` 同型诊断 ✓）
2. **"未闭合"的诚实含义** ✓：\textbf{不}等于"命题错"✗（`C-272` 零反例 ✓）；也\textbf{不}等于"已证不可能"✗ ⟹ 保持 **OPEN/AUDIT** ✓
3. **三层分离已写死** ✓✓：即使 60M 跑通 ⟹ 只记"证书闭合" ✓；**不**自动升为机制 ✗；**更不**升为 bridge ✗
4. **不扩大** ✓：本档\textbf{不}跑 60M ✗、\textbf{不}动 v4 ✗、\textbf{不}改 `C-181` 的 GAP-A ✗

## §5 校准表更新（✓）

| 回查 | 出口 | 类型 |
|---|---|---|
| `C-270` ✓ | **GAP CONFIRMED** ✓ | 结构缺口 ＋ 封存分支 ✓ |
| `C-246` ✓ | **CLOSED** ✓ | 后续材料已闭合 ✓ |
| `C-260` ✓ | **GAP CONFIRMED** ✓ | 非 failure-型（theorem-strengthening）✓ |
| `C-261` ✓ | **CLOSED(reopen) ＋资产** ✓ | 结构性 no-bridge ✓ |
| `C-271` ✓ | **GAP CONFIRMED** ✓ | **工程型缺口（证书未闭合）** ✓ |

$$\Longrightarrow \text{五档}\ \textbf{出口三类}✓✓ \Longrightarrow \text{协议区分力持续}✓$$

## §6 【技术词回查】输出（**先跑后写**✓）

```
技术词 定向回查     命中文件数=4    :: ./C316-directed-recheck-C260-mainline-candidate-zero-GAP-CONFIRMED.md ./C314-directed-recheck-of-old-GAPs-protocol-and-first-verdicts.md ./C317-directed-recheck-C261-Lambda-upper-bound-asset-status-preserved.md 
技术词 工程型缺口  命中文件数=0    :: 
技术词 待审箱        命中文件数=1    :: ./C271-M5-half-budget-not-closed-formal-record-and-failure-mode-precise-diagnosis.md 
```
- 本档新增 ✓：`工程型缺口`（依上表判 ✓）；既有引用 ✓：`定向回查`／`待审箱`（`C-314`／`C-272`✓）—— 不作新增主张 ✗
- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：M=5 已失败 ✗；命题为假 ✗；证书闭合＝机制 ✗；证书闭合＝bridge ✗
