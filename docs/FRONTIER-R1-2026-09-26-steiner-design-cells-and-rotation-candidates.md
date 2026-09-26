已查地图：已跑 scripts/prework_map_check.sh Steiner 3-design RoSQS CSQS 存在性 ⟹ **未覆盖**（本线首次触及设计论 frontier ✓；与 119 线／A23-D4 无重叠 ✓）；**已查**：`CLOSED-ROUTES-MAP`（无 Steiner 设计条目 ✓）、`MASTER-STATUS`、`ASSETS-REGISTRY`（A23-D4 模板可复用 ✓）。
D0: 本档对象 = Steiner 3-designs ≤50 点 与 RoSQS/CSQS 的存在性格子（**检索对象，非推导对象**）
D1: 0（产出为 frontier 地图、候选短表与 P0–P2 草案；**未跑计算** ✓）

# FRONTIER-R1-2026-09-26 · Steiner 设计格与旋转 SQS 候选（第一轮 dossier）

## §0 来源（逐字 ✓）

```
$$\text{Kiermaier, Kr\v{c}adinac, Wassermann, "Steiner 3-designs as extensions", arXiv:2509.23483 (2025-09-27)},\ \text{DCC \textbf{94} (2026), art.\ 157}\ ✓$$
$$\qquad\text{DOI}\ 10.1007/s10623-026-01888-w\ ✓;\quad \text{方法}: \text{扩张 Steiner 2-设计（prescribed extension groups）+ Kramer--Mesner 法}\ ✓$$
$$\qquad\text{该文自建}\ S(3,6,42)\ \text{（settling one of the smallest open parameter sets）}+\ \text{rotational SQS on 46, 92}\ ✓$$
$$
$$
```

---

## §1 frontier 地图（该文 Table 1 与 §2 逐字 ✓）

```
$$\textbf{(A) Steiner 3-designs}\ (v\le50):\ \textbf{三格存在性未定}\ ✓$$
$$\qquad S(3,5,41):\ v=41,k=5,b=1066;\ \text{派生}\ S(2,4,40)\ ✓;\quad \text{Table 1 中 }N_d=\text{"?"}$$
$$\qquad S(3,6,46):\ v=46,k=6,b=759;\ \text{派生}\ S(2,5,45)\ ✓;\quad N_d=\text{"?"}$$
$$\qquad S(3,5,50):\ v=50,k=5,b=1960;\ \text{派生}\ S(2,4,49)\ ✓;\quad N_d=\text{"?"}$$
$$\qquad\text{该文逐字}:\ \text{"We tried to construct designs for the remaining three open parameter sets ... but no designs were found"}\ ✓\ \text{（标准法已试 ✗）}$$
$$\textbf{(B) CSQS(94)}:\ \text{循环 SQS};\ \text{"only one unknown value below 100, namely }v=94\text{"};\ \text{"neither construct nor rule out"}\ ✗✓$$
$$\textbf{(C) RoSQS}(v):\ \text{旋转 SQS（order }v-1\ \text{循环 ＋ 不动点 }\infty\text{）};\ \text{原 7 开放值}\ 46,56,70,82,86,92,98\ ✓$$
$$\qquad\text{该文\textbf{构造}了}\ \text{RoSQS}(46),\ \text{RoSQS}(92)\ ✓✓\ \text{（base blocks 公开可下载）}\ \Longrightarrow\ \textbf{现剩 5 格}:\ 56,70,82,86,98\ ✓✓$$
$$
$$
```

---

## §2 形状指纹（为何与本项目能力同形 ✓）

```
$$\textbf{形状}:\ \text{有限存在性}\ +\ \text{证书＝分块表/基块表}\ +\ \text{可按\textbf{群轨道压缩}}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{与 A23-D4 已验证模板同形}:\ \text{群对称约化 → 穷举/启发搜索 → 独立 verifier → 机器证书}\ ✓$$
$$\textbf{与 119 线的关系}:\ \textbf{无}（不同对象 ✓）；\ \text{与本项目"dent"定义相容}:\ \text{构造出新值＝可验证的记录改进}\ ✓$$
$$\textbf{风险（诚实 ⚠️）}:\ \text{(A) 三格正被\textbf{活跃收获}}（2025--2026 该文即在此 ✓）；\ \text{(C) 该文已用同类方法拿下 46/92 ⟹ 标准法对剩余 5 格可能已试过}\ ⚠️$$
$$
$$
```

---

## §3 P0–P2 草案（每条候选 ✓）

```
$$\textbf{候选 C-1}:\ \text{RoSQS}(56)\ \text{（首选 ✓）}$$
$$\qquad P0\ \text{定义}:\ \text{在 }Z_{55}\cup\{\infty\}\ \text{上找 SQS}(56)\ \text{使 }Z_{55}\ \text{循环作用（}\infty\ \text{不动）}\ ✓;\ \text{证书＝基块集}\ ✓$$
$$\qquad P1\ \text{攻击点}:\ \text{基块集必须使每条 }\{\infty,a,b\}\ \text{型与 }\{\text{三元组}\}\ \text{型各恰被覆盖一次（orbit 计数精确）}\ ✓$$
$$\qquad P2\ \text{构造形式}:\ \text{固定 }\text{RoSQS}(46)\ \text{的基块模板（该文公开 ✓）扩展为 }55\ \text{阶循环群上的 orbit 选择问题}\ ✓$$
$$\textbf{候选 C-2}:\ \text{CSQS}(94)\ \text{（单格，干净 ✓）}:\ P0\ \text{＝在 }Z_{94}\ \text{上循环 SQS};\ P1\ \text{＝}4\text{-子集 orbit 覆盖精确一次};\ P2\ \text{＝Z}_{94}\text{-orbit 选择}\ ✓$$
$$\textbf{候选 C-3}:\ S(3,5,41)\ \text{（风险最高 ⚠️，但意义最大）}:\ P1\ \text{＝扩张条件（派生 }S(2,4,40)\ \text{＋群）};\ P2\ \text{＝Kramer--Mesner 全群搜索}\ ✓$$
$$
$$
```

---

## §4 校准门（本项目纪律 ✓）

```
$$\textbf{G-CAL}:\ \text{任何候选开工前，必须先\textbf{复现}该文已知结果之一}:\ \text{复现 RoSQS}(46)\ \text{的基块表（对其公开数据逐块核验 ✓）}$$
$$\qquad\Longrightarrow\ \text{过门方可推进 }56/70/82/86/98\ ✓;\ \text{未过门不得声称任何新构造}\ ✗$$
$$\textbf{验收}:\ \text{独立 verifier（不复用搜索脚本）＋ SHA256 指纹 ＋ 覆盖计数自检}\ ✓\ \text{（A23-D4 模板 ✓）}$$
$$
$$
```

---

## §5 待唐先生裁定（不含计算 ✓）

```
$$\textbf{Q-1}:\ \text{是否以 }\text{RoSQS}(56)\ \text{为首个 asset-native 目标（配校准门 G-CAL ✓）}?$$
$$\textbf{Q-2}:\ \text{或先做 CSQS}(94)（单格、对象最干净）?$$
$$\textbf{Q-3}:\ \text{是否允许我为校准门下载该文的公开数据（[29] 链接）与复现 RoSQS}(46)?\ \text{（纯本地核验，不外发 ✓）}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §0–§1 全部为**文献逐字**（arXiv v1 HTML 直读 ✓）；**未**独立复核该文结论 ✗
- §2 的"同形"为**本档判断** ✓（非定理 ✓）；风险已并列标注 ✓
- §3 的 P0–P2 仅为**草案**（未验证任何一步 ✓）；§4 校准门为**流程约束** ✓
- **未跑**任何计算/搜索 ✓（本轮严格遵守"先 dossier 后计算" ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Steiner 设计格 frontier 地图 命中文件数=1    :: ./FRONTIER-R1-2026-09-26-steiner-design-cells-and-rotation-candidates.md 
技术词 RoSQS 剩余五格 命中文件数=1    :: ./FRONTIER-R1-2026-09-26-steiner-design-cells-and-rotation-candidates.md 
技术词 校准门 G-CAL  命中文件数=1    :: ./FRONTIER-R1-2026-09-26-steiner-design-cells-and-rotation-candidates.md
```
- **本档新增**：Steiner 设计格 frontier 地图、RoSQS 剩余五格、校准门 G-CAL（见上方命中数）
- **档案已有（引用，不列为提出）**：A23-D4 模板、dent 定义、Kramer--Mesner 法（文献）
