已查地图：已跑 scripts/prework_map_check.sh triple 邻域 独立杠杆 终止性实验 ⟹ 执行自 `TRIP-2026-09-27`（(Z-4) 撤回 ✓）＋ 唐先生 2026-09-27 09:22 令 ✓；本档为**终止性实验判定**；含穷举 ＋ 构造式搜索 ✓。
D0: 本档对象 = 唯一 triple 点的邻域局部结构是否携带独立信息
D1: 0（产出为终止性否定：邻域结构被完全决定 ⟹ 封存三阶耦合 ✗）

# TERM-2026-09-27 · triple 邻域终止性实验

## §0 判定（先给）

```
$$\textbf{实验定义（唐先生 09:22 ✓）}:\ \text{只测唯一 triple 类}\ (a_3+d_3=1\ ✓);\ \textbf{判停}:\ \text{若全部新约束化回已知}\ (N_1+N_2=143\ /\ \text{匹配度}\le2\ /\ \text{中点容量}) \Longrightarrow \textbf{直接封存三阶耦合}\ ✓$$
$$\boxed{\textbf{(BB-1)}\ n=4\ \textbf{全枚举}（480 例 ✓）:\ (|C|,N_1,N_2,\mathrm{case})\ \text{共 3 组};\ \text{邻域结构}\ (\mathrm{shell1}+\mathrm{shell2})\ \textbf{零变化}\ \Longrightarrow\ \textbf{被完全决定}\ ✗}$$
$$\boxed{\textbf{(BB-2)}\ \Longrightarrow\ \textbf{无独立杠杆}\ ✗\ \Longrightarrow\ \text{按判停条件}\ \textbf{封存三阶耦合}\ ✓✓\ \text{（Boolean-fiber／triple-neighbourhood 机制 ✗）}}$$
$$\boxed{\textbf{(BB-3)}\ n=5:\ \text{构造式局部搜索（}4000\ \text{次重启）命中}\ \mathbf 0\ \text{例}\ ⚠️\ \Longrightarrow\ \textbf{无数据};\ \textbf{不得断言不存在}\ ✗}$$
$$
$$
```

---

## §1 实验记录（数据格式按唐先生要求 ✓）

```
$$\text{记录项}:\ (t,\ C\cap N(t),\ \text{两两距离},\ \text{二阶邻域 occupancy},\ N_1,\ N_2)\ ✓$$
$$\textbf{n=4 结果}:\ \text{在 }(|C|,N_1,N_2,\mathrm{case})\ \text{固定的 3 组内，}\mathrm{shell1}=(\text{距 }t\ \text{为 1 处各点 }b\ \text{值})\ \text{与}\ \mathrm{shell2}=(\text{距 }2\ \text{处})\ \text{均}\ \textbf{恒定}\ ✓$$
$$\qquad\Longrightarrow\ \text{任何由邻域导出的约束皆为 }(|C|,N_1,N_2,\mathrm{case})\ \text{的\textbf{重参数化}}\ ✗\ \text{（与 FACE／THIRD 同型 ✓）}$$
$$
$$
```

---

## §2 判停执行（唐先生明令 ✓）

```
$$\boxed{\text{三阶耦合（Boolean-fiber ／ triple-neighbourhood）\textbf{封存}}\ ✗}\ \text{（依据：邻域结构不携带超出 }(|C|,N_1,N_2,\mathrm{case})\ \text{的信息 ✓）}$$
$$\textbf{不升级四阶}\ ✗\ \text{（唐先生明令 ✓：防止"又发现漂亮结构"的循环 ✓）}$$
$$\textbf{封存对象}:\ \text{机制（triple 邻域／三阶耦合）}\ ✓;\quad \textbf{非}\ 119\ \text{本身}\ ✓\ \text{（119 状态不变：}\texttt{OPEN}\ /\ \text{表示待寻 ✓}）$$
$$
$$
```

---

## §3 本线（Boolean-fiber）自 09-26 22:52 起的净产出（诚实 ✓）

```
$$\text{① 逐点平方恒等式：}\textbf{含一处修正}\ ✓\ (\text{仅 }x\in C\ \text{时为 }f+3S+2P\ ✓)$$
$$\text{② (Z-4) "独立三阶不变量"：}\textbf{已撤回}\ ✗\ (\text{TRIP 档 ✓：实为 }(|C|,N_1,d_3)\ \text{的重参数化 ✓})$$
$$\text{③ 唐先生三条恒等式：}\textbf{核验通过}\ ✓\ (\text{唯一 triple 类中 ✓})$$
$$\text{④ 终止性实验：}\textbf{否定}\ ✗\ \text{（邻域无独立杠杆 ⟹ 封存 ✓）}$$
$$\Longrightarrow\ \textbf{净产出} = \text{一次核验 ＋ 一次撤回 ＋ 一次终止性否定};\ \textbf{无新定理}\ ✗\ \text{（诚实 ✓）}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §0 的 n=4 证据为**穷举**（480 例 ✓）但**规模小** ⚠️；n=5 **无数据** ✗（搜索未命中，**不断言不存在** ✓）
- 封存为**机制级** ✓（非"三阶不可能"✗，非"119 不可解"✗）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗
- 本轮未跑 SAT/CP-SAT ✓（穷举 ＋ 局部搜索 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 终止性实验  命中文件数=1    :: ./TERM-2026-09-27-triple-neighbourhood-terminating-experiment.md 
技术词 triple 邻域无独立杠杆 命中文件数=1    :: ./TERM-2026-09-27-triple-neighbourhood-terminating-experiment.md
```
- **本档新增**：终止性实验判定（triple 邻域无独立杠杆）（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：唯一 triple 类、(Z-4) 撤回、匹配定理、中点容量、FACE/THIRD 同型
