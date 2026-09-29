# AUDIT-2026-09-29-P07 — **BOW 重建链 P0–P7 审计** ＋ 四类"隐形细节"逐条审

> 空间 B｜非 C 号｜唐先生 23:40 核心工作假设｜**不主张任何新值**（V290）
> 时间：2026-09-29 23:40（本机 00:4x）

**已查地图**：`ASSESS-SCALE`／`INV1–INV5`／`AUDIT-28q`（公式链）／`AUDIT-29j/l/m`（口径三次纠错）／`TECH-word 回查`（见 §5）
D0: 本档对象 = **档案已有**（三条链之阈值/等号结构）之**逐层审计**（新数学对象：无 ✗）
D1: 0（产出 = **一条"等号排除机制不可用"之判定 ＋ 四类细节之审计结论** ⚠️✓）

---

## §0 唐先生之**核心工作假设**（逐字登记 ✓）

$$\boxed{\text{107 不能复现，更可能不是"缺第 9、第 10 条新路线"，而是重建 BOW 原始证明机制时，}\textbf{有一个定义/计数口径/边界条件/中间不等式没有恢复}}$$
$$\text{推论}:\ \textbf{BOW 的路径数可能只有 1 条，我们在搜的是这 1 条路径的各种投影};\ \therefore\ \text{目标改为：}\textbf{找出 }106\to107\text{ 所需那 1 单位来自哪里}\ ✓$$

## §1 P0–P7 逐层审计（**对我方三条链**）

$$\text{结构}:\ P0\ \text{对象}|\ P1\ \text{一层计数}|\ P2\ \text{重复数}|\ P3\ \text{消元}|\ P4\ \textbf{严格性从哪来}|\ P5\ \text{等号构型}|\ P6\ \text{为何不存在}|\ P7\ 106{+}1$$

| 链 | 阈值 | P4 严格性来源 | P5 等号构型 | P6 可用？ |
|---|---|---|---|---|
| **A 聚合**（μ-恒等式＋整数性） | **95** | 整数性 | 可行集**极大**（已见"$\mu\le2$、$A_1{=}0$"退化解） | **不可用**（等号非唯一） ✗ |
| **B van Wee** | **103** | 修正项（偶 $n$ 精确 $\Rightarrow2^n/n{=}102.4$） | $n{=}8$ 时**可达**（32 ✓）；$n{=}10$ 值**非整数** ⟹ 无整数等号 | **不可用** ✗ |
| **C SDP-3**（引用值） | **106** | PSD 约束 | 值 $105.2223$ **非整数** ⟹ $M{=}106$ **不是等号** | **不可用** ✗ |

$$\boxed{\text{判定}:\ \textbf{我方三条链没有一条在 }M{=}106\ \textbf{处是"紧"的}\ \Longrightarrow\ \text{唐先生之机制"106 等号构型不存在 }\Rightarrow107\text{"\ \textbf{在我方手上不可用}}\ ✗}$$
$$\qquad\text{该机制需要 }\textbf{BÖW 的一条在整数处 sharp 的链};\ \text{而那条链}\ \textbf{源不可得} \Longrightarrow \text{与首条约束正面冲突} \ ⚠️$$

## §2 四类"隐形细节"逐条审

$$\textbf{A 口径（open/closed）}:\ \text{我方全部恒等式皆\ \textbf{数值验证过}}（F1–F9；\ \delta_{N[v]}\ \text{恒等式 }1024/1024;\ r_q{=}2t_q\ \textbf{开邻域}\ ✓）$$
$$\qquad\Longrightarrow\ \textbf{恒等式内不可能藏口径错}（否则数值立刻不符）✓;\ \text{残留风险\ \textbf{仅在不等式之常数项}（无现实可验）}$$
$$\textbf{B private/shared 归属}:\ \text{档案已\ \textbf{三次}同型纠错}（29j/29l/29m:\ 对象＝\textbf{球 excess}，非点计数）；\ \text{今晚又证该层\textbf{平凡} ⟹ 口径已钉死}\ ✓$$
$$\textbf{C 等号排除}:\ \textbf{结构性不可用}（§1）\ ✗\ \text{——本档最重要判定}$$
$$\textbf{D 双侧计数}:\ \textbf{我们已经做过}:\ F8:\ E=\sum_{x\notin C}\binom{\mu}3+\sum_{y\in C}\binom{a_y}3;\ F9:\ 2A_2=\sum_{x\notin C}\binom{\mu}2+P\ ✓✓\ (\text{数值验证})$$
$$\qquad\text{这正是"两侧计数 ＋ 恒等式消元"之形};\ \textbf{但它们是恒等式、不产生严格性} ✗$$

## §3 判定

$$\boxed{\text{在唐先生假设下，尚可能藏"细节"之处只剩两处}:\ \textbf{A 之不等式常数项}\ \text{与}\ \textbf{P4 之严格性来源}}$$
$$\qquad\text{而这两者\ \textbf{都要求 BÖW 链的原文式} \Longrightarrow \text{与"论文不可得"之约束冲突} \ ⚠️}$$
$$\therefore\ \text{本假设\ \textbf{未被证伪}（且与全部实验事实吻合 ✓），但\ \textbf{在本约束下不可执行}}$$

## §4 建议（**待唐先生定**）

$$\textbf{(甲) 收束归档（我的推荐）}:\ \text{保留 }K(10,1)\ge\mathbf{106};\ \text{把本假设（"缺一个定义/口径/等号细节"）作为\ \textbf{已知未决} 登记；工具＋九条 kill 入册}$$
$$\textbf{(乙) 唯一残余动作}:\ \text{逐项重推档案中\ \textbf{未数值验证过的不等式常数}（清单可列）——期望值低但非零} \ ⚠️$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "等号排除" "双侧计数" "证明接口" "P4-P6"
技术词 等号排除     命中文件数=0    ::
技术词 双侧计数     命中文件数=0    ::
技术词 证明接口     命中文件数=2    :: ./C380-FINAL-STAGE-REPORT.md ./C380-LAYER5-GATE-FREEZE.md
技术词 P4-P6        命中文件数=0    ::
```
$$\textbf{本档新增} = \{\text{等号排除},\ \text{双侧计数}\}\ (\text{首次命名},\ \text{方法学词});\quad
\textbf{档案已有（引用）} = \{\text{证明接口}（C380\ \text{系列}）\};\quad
\textbf{通用词（不计）} = \{\text{P4-P6}\}$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**链审计 ＋ 假设登记** ✓
- 未取论文原文（R16–17）✓；未重攻已 kill 之族 ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
