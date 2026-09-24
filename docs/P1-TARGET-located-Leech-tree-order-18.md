已查地图：命中（`RESEARCH-PIVOT-asset-centered-independent-problem-pool`（`P1` 首选）／`HUNT-R2-OPEN-MATH-POOL-round1`）⟹ 引用，不开新案
D0: 本档对象 = `P1` 首攻**靶子定位**（30 分钟窗口内）：候选断言清单 ＋ 四门核查 ＋ 已封池标注；**未做独立复核**
D1: 0 （[REVIEW] 轮次：定位与核查，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`P1` 靶子定位（首轮）**

## §1 ⭐ 首选靶子（本档发现）

```
【候选】**`arXiv:2609.20492`｜"Nonexistence of a Leech Tree of Order 18: A Computer-assisted proof"** ✓✓
【逐字证据（摘要页 snippet）】 "**The exhaustive search, certificates, and certificate checkers are not Lean verified. The final result is therefore a computer-assisted proof**" ✓✓✓
　⟹ **有证书、有校验器，但明确"未 Lean 验证"** ⟹ **正是"相信计算结果"尚未升级为"可独立核验证书"的典型形态** ✓✓
【问题独立性】 Leech tree（`n` 阶）＝纯有限组合存在性问题，**与 RH／零点／`n=38`／TARGET-L9 全无关系** ✓
```

## §2 四门核查（照录您给的门）

```
**`G1` 独立性** ✓（纯有限组合；陈述中不含 RH／零点／`n=38`／`A,B,g,\tau`）✓
**`G2` 资产自然适配** ✓✓ —— `D`＋`H` **正是其核心方法**（穷尽搜索、证书、独立 verifier、完整性/覆盖性检查、对称性处理）；**非硬套** ✓
**`G3` 新 `Q_{\rm new}`／证书对象** ✓ —— 新的证书对象＝**可独立核验（进而 Lean 验证）的 `18` 阶不存在性证书**；**不是** `F(A,B,g,\tau,C)` ✓
**`G4` 公开可核验新结果** ✓ —— 成功形态二选一：**(a)** 独立核验通过（把 CAP 升级为机器可核）；**(b)** **发现缺陷**（近期同类审计**确有**先例）✓✓
【⟹ 四门全过】**进入"原始出处"阶段** ✓
```

## §3 同类靶子清单（按您的优先级排序）

```
**`1` 有限组合分类**：✅ **`2609.20492`（Leech tree 18 阶不存在）为首选**；同类域：graceful／`\alpha`-labeling、tree 嵌入、design 非存在性 ✓
**`2` 有限 SAT/UNSAT 穷尽断言**：⚠️ **部分池已被封**：`R(3,8)`／`R(3,9)` 的证书已由 `IJCAI 2025`「Verified Certificates via SAT and Computer Algebra」补齐（逐字："**To our knowledge, these are the only two known Ramsey numbers that have not been verified with proof certificates**"）✓；Lam 问题（`10` 阶射影平面）已由 `AAAI 2021` 用 SAT 出证书（逐字："**did not produce nonexistence certificates**" → 该文补上）✓ ⟹ **此子池已收窄** ✓
**`3` 数值常数上界且证书不透明**：待查（尚未定位具体靶子）✓
【⟹ **方法论文献（可作模板，非靶子）**】**`arXiv:2608.13067`「Computer-assisted Proof Under Audit: Typos, Certificate Errors, and Reproducible Exact Checks」** ✓ —— 其引用的先例逐字：某次复核对 Lam 问题"**found inconsistent enumeration counts while preserving the nonexistence conclusion**" ⟹ **审计确能查出缺陷** ✓✓
```

## §4 下一步（严格按您的链）

```
$$\text{公开断言}\to\textbf{原始出处}\to\text{独立复核}\to\begin{cases}\text{独立证书}\\\text{或 明确缺陷}\end{cases}$$ ✓
【下一动作】**取 `2609.20492` 原始材料**：精确陈述、搜索空间规格、证书格式、校验器代码、以及"未 Lean 验证"具体所缺环节 ✓
【⛔ 纪律】**未做独立复核前不得宣称其有错**；**本轮不投入大计算**；`n=38`／`TARGET-L9`／RH **全部禁止作为筛选依据** ✓✓
【边界】 §1–§3 为**检索所得（摘要/snippet 级，档级）**，**未读原文、未复核**；`2609.20492` 的题录与"未 Lean 验证"为**逐字 snippet**；`IJCAI 2025`／`AAAI 2021` 两句为**逐字 snippet**；四门判定为**本档自行给出**；未制造候选／未启动搜索／未碰 RH。
