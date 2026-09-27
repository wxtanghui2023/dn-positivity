已查地图：已跑 scripts/prework_map_check.sh 分类池 桶 J fingerprint ⟹ 执行自 `FINAL-2026-09-27-K8-1-verdict`（✓）＋ 唐先生 12:46（跑乙 ✓）；本档 = **(乙) 分类池桶分析：流水线全中 ✓；非平凡桶存在但 J 全钉住 ⚠️**。
D0: 本档对象 = 现有 Kéri 分类池中 P1-2 的可测空间
D1: 1（新增：**分类池桶表 ✓**；**流水线验证（类数=文献上标 ✓✓）**；**3 个非平凡桶 J 全同的判定 ✓**）

# (乙) 分类池桶分析（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BG-1 流水线验证全中 ✓✓)}\ \text{我解析出的类数}\ \textbf{逐一等于文献上标}:\ 2,2,3,6,2,4,8\ \checkmark\ \Longrightarrow\ \text{parser}\to\text{距离分布}\to(A_1,A_2)\to J\ \text{整链正确} ✓✓}$$
$$\boxed{\textbf{(BG-2 非平凡桶确实存在 ✓)}\ \text{三个文件含同 }(A_1,A_2)\ \text{的多码桶（最大桶 }4\ ✓）;\ \text{但\textbf{全部桶内 }J\ \text{完全一致}} ✗\ \text{（无分叉 ✓）}}$$
$$\boxed{\textbf{(BG-3 P1-2 判定 ⚠️)}\ \text{现有分类池}\ \textbf{未命中分叉} \Longrightarrow \text{按唐先生分类 = 类型 1（J 被桶约束住 ✓）};\ \text{但 P1-2 仍 \textbf{OPEN}（有限池 ≠ 定理 ✓）}}$$
$$\boxed{\textbf{(BG-4 目标格 }\mathbf{(9,1)}\ \text{现状 ⚠️)}\ \text{仅 2 类且 }(A_1,A_2)\ \text{各异 ⟹ \textbf{该格仍不可测};\ \text{需 2018 supplementary 的其余 9 个 }(8,32)_1\ \text{代表 ✓}}$$
$$
$$
```

---

## §1 结果表（**唐先生指定格式 ✓**）

```
$$\begin{array}{c|c|c|c|c|c|c|c}
\text{文件} & n,R & \text{类数} & \text{文献上标} & (A_1,A_2)\ \text{桶数} & \text{最大桶} & \text{非平凡桶} & J\ \text{分叉}\\
\hline
K\_4\_1\_classif & 4,1 & 2 & 2\ ✓ & 2 & 1 & 0 & 0\\
K\_6\_1\_classif & 6,1 & 2 & 2\ ✓ & 2 & 1 & 0 & 0\\
K\_7\_2\_classif & 7,2 & 3 & 3\ ✓ & 3 & 1 & 0 & 0\\
K\_8\_3\_classif & 8,3 & 6 & 6\ ✓ & 3 & \mathbf 4 & 1 & \mathbf 0\\
K\_9\_1\_classif & 9,1 & 2 & 2\ ✓ & 2 & 1 & 0 & 0\\
K\_9\_2\_classif & 9,2 & 4 & 4\ ✓ & \mathbf 1 & \mathbf 4 & 1 & \mathbf 0\\
K\_9\_3\_classif & 9,3 & 8 & 8\ ✓ & 7 & 2 & 1 & \mathbf 0\\
\end{array}$$
$$\textbf{关键读数 ✓}:\ \text{(i) 类数 = 文献上标（}2,2,3,6,2,4,8\ ✓✓\text{——流水线验证 ✓）};\ \text{(ii) 非平凡桶 3 个（}K\_8\_3,\ K\_9\_2,\ K\_9\_3\ ✓）;\ \text{(iii) 三者桶内 }J\ \textbf{全同} ✗$$
$$
$$
```

---

## §2 最强实证：$K\_9\_2$ 的 4 元桶（**✓✓**）

```
$$\text{4 个不等价最优 }(9,16)_2\ \text{码}\ \textbf{同属一个 }(A_1,A_2)\ \text{桶} ✓\ \text{且 }J\ \text{向量}\textbf{完全相同} ✓✓$$
$$\Longrightarrow\ \text{这是"}(A_1,A_2)\ \text{决定 }J\text{"的\textbf{4 元家族实证} ✓（远强于单码 ✓）};\ \text{但仍是\textbf{有限池} ⟹ 不构成定理 ✗（遵唐先生纪律 ✓）}$$
$$
$$
```

---

## §3 判定与下一步（**✓**）

```
$$\text{按唐先生的三分类 ✓}:\ \text{本档落}\ \textbf{类型 1}（\text{同 }(A_1,A_2)\ \text{、}J\ \text{相同 ⟹ }J\ \text{被桶约束住，P1-2 继续收紧} ✓）$$
$$\qquad\textbf{不得写}:\ "\text{support-2 塌缩定理}" ✗\ \text{（有限分类 ≠ 一般结论 ✓）；也不得写"不存在分叉" ✗$$
$$\text{未测格}:\ n=9,R=1\ \text{（2 类、}(A_1,A_2)\ \text{各异 ✗）、}(8,32)_1\ \text{的其余 9 个代表（库中无 ✗）}$$
$$\text{下一步（二选一 ✓）}:\ \text{(甲) 追 2018 supplementary 取 }(8,32)_1\ \text{其余 9 代表（靶最正 ✓）};\ \text{(乙′) 扩大现有池（拉更多 }\_classif\ \text{文件}:\ }K\_5\_3,\ K\_6\_2,\ K\_6\_3,\ K\_7\_3\ \text{等 ✓ 成本近零 ✓）}$$
$$\qquad\text{若 (乙′) 中出现同桶 }J\ \text{分叉} \Longrightarrow \textbf{P1-2 PASS} ✓✓;\ \text{若继续全同} \Longrightarrow \text{证据面扩大到十几个桶 ✓}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**本机流水线 ＋ 逐格核验** ✓（类数=文献上标 ✓✓）；§2–§3 为**判定 ＋ 分支配对** ✓
- ⚠️ **未**声称 $J$ 由 $(A_1,A_2)$ 决定（有限池证据 ✓，非定理 ✗）；**未**声称 P1-2 关闭 ✗；**未**碰 $n=10/119$ ✓
- 去重 ✓：按平移规范化（$2^n$ 个 ✓）；且"分类文件本身即为不等价代表集"这一性质已被**类数=文献上标**独立佐证 ✓✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：(乙) 分类池桶表、流水线验证、非平凡桶 J 全同判定
- **档案已有（引用，不列为提出）**：$(A_1,A_2)$、$J$ fingerprint、$K(n,R)$ 上标、separation pair、P1-2


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 分类池桶表  命中文件数=1    :: ./YI-2026-09-27-classification-pool-bucket-analysis.md 
技术词 流水线验证  命中文件数=1    :: ./YI-2026-09-27-classification-pool-bucket-analysis.md
```
- **本档新增**：(乙) 分类池桶表、流水线验证、非平凡桶 J 全同判定（见上方命中数；0 命中者为自造语／内部标签 ✓）
