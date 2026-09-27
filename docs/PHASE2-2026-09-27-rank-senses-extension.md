已查地图：已跑 scripts/prework_map_check.sh p-rank extension 感知 rank 障碍 ⟹ 执行自 `FRONTIER-R3-2026-09-27-phase1`（机制占用 ✓）＋ 唐先生 09:49 ✓；本档为**第二阶段裁决：BLOCKED**（**未动算** ✓）。
D0: 本档对象 = "p-rank 是否感知 extension"的机制判定
D1: 1（新增：**自正交引擎对 λ=1 设计的结构性否证** ✓✓；**BLOCKED 裁决** ✓）

# PHASE2-2026-09-27 · p-rank 是否感知 extension

## §0 裁决（先给，按唐先生三态 ✓）

```
$$\boxed{\textbf{(HH-1)}\ \textbf{BLOCKED}}\ ✗\ \text{——\textbf{没有任何经典引擎}能对 }\lambda=1\ \text{的 Steiner 2-design 给出 extension-specific 的 rank 限制}\ ✓$$
$$\qquad\text{（即：只有普通 p-rank 下界；无 (extendible}\Rightarrow\text{rank}\in\mathcal R_{\rm extend}\text{) 型信息 ✓）}$$
$$\boxed{\textbf{(HH-2)}\ \textbf{结构性否证（本档新 ✓✓）}:\ } \text{自正交（self-orthogonality）引擎}\ \textbf{对一切 }\lambda=1\ \text{设计不可能成立}\ ✗\ \text{——因两块必交于恰 1 点 ⟹ }\langle 1_A,1_B\rangle=1\not\equiv0\ (\mathrm{mod}\ p)\ \forall p\ ✓✓}$$
$$\qquad\Longrightarrow\ \text{"自正交 }\Rightarrow\ \dim\le v/2"\ \text{这条主引擎\textbf{结构性死掉}}\ ✗\ \text{（非"算不出来"，是"不可能成立" ✓）}$$
$$\boxed{\textbf{(HH-3)}\ \text{故若继续，唯一出路＝}\textbf{经验判定}:\ \text{在\textbf{已知可扩张}的小参数对上测 rank 是否被限制}\ ✓\ \text{（不碰 }S(3,5,41)\ \text{的 SAT／枚举 ✓）}}$$
$$
$$
```

---

## §1 P0/P1/P2（按唐先生格式 ✓）

```
$$P0:\ \text{刻画 }2\text{-}(40,4,1)\ \text{设计 }D\ \text{能成为 }3\text{-}(41,5,1)\ \text{的导数的条件}\ ✓$$
$$\qquad\textbf{等价形式（本档给出 ✓）}:\ \exists\ 936\ \text{个 }5\text{-子集 }B\subseteq(40\ \text{点})\ \text{s.t.}\ \text{每个"D-不共线"三元组恰属一个 }B\ ✓;\ \text{"D-共线"三元组不属任何 }B\ ✓$$
$$\qquad\text{（此即 KKW 的搜索空间；})\ \text{且}\ \text{每个点}\ \in\ 117\ \text{个 }M_0\text{-块}\ ✓;\ \text{每对}\ \in\ 12\ \text{个}\ ✓$$
$$P1\ (\text{唐先生要的强形式 ✓}):\ \text{是否存在 }\mathbb F_p\ \text{与 }F\ \text{s.t.}\ D\ \text{extendible}\Rightarrow\operatorname{rank}_p(M_D)\ge F\ \text{或}\ \operatorname{rank}_p\in\mathcal R_{\rm extend}\subsetneq\mathcal R_{\rm all}\ ✓$$
$$P2:\ \text{独立的 universal 上界 }\operatorname{rank}_p\le U\ \text{与 }L>U\ \text{矛盾}\ ✓$$
$$
$$
```

---

## §2 (HH-2) 自正交引擎的结构性否证（本档核心 ✓）

```
$$\text{经典"rank }\Rightarrow\text{ 上界"引擎}:\ \text{若块码 }C\ \text{自正交（}\langle x,y\rangle\equiv0\ \forall x,y\in C\ ✓\text{）}\Longrightarrow\dim C\le v/2\ ✓\ \text{（此即 DHV／Assmus 型的核心机制 ✓）}$$
$$\text{但其\textbf{前提}对 }\lambda=1\ \text{设计永不成立}:\ \text{取两块 }A\ne B\ ✓\ \Rightarrow\ |A\cap B|\in\{0,1\}\ ✓;\ \text{而 }\langle1_A,1_B\rangle=|A\cap B|\cdot1\ ✓$$
$$\qquad\text{若 }A\cap B\ne\varnothing\ \Rightarrow\ \langle1_A,1_B\rangle=1\ \not\equiv\ 0\ (\mathrm{mod}\ p)\ \forall p\ ✓\ \Longrightarrow\ C\ \textbf{不正交}\ ✗$$
$$\qquad\text{（Steiner 2-design 的块必相交：}v\ge k+1\ \Rightarrow\ \text{存在相交块对}\ ✓\text{）}\ \Longrightarrow\ \boxed{\text{自正交引擎对 }\lambda=1\ \textbf{结构性失效}}\ ✗✗$$
$$\Longrightarrow\ \text{故 DHV／Hamada 型"rank 下界"机制}\ \textbf{不能}被搬来给出 extension 限制\ ✗\ \text{（唐先生此前的刹车正确 ✓✓）}$$
$$
$$
```

---

## §3 其余候选引擎的清点（本档 ✓）

```
$$\text{① 自正交（AM 型）}:\ \textbf{死}\ ✗\ (\text{HH-2}\ ✓);\quad \text{② Hamada 型最小 rank}:\ \text{仅对\textbf{几何设计}参数}\ ⚠️\ \text{——本三 cell 非 }q^2+1/q+1\ \text{型}\ ✓\ \text{（}41\ne q^2+1,\ 46\ne q^2+1,\ 50\ne q^2+1\ ✓\text{）}\ \Longrightarrow\ \text{不适用}\ ✗$$
$$\text{③ 广义 AM（}s\ge2\text{）}:\ \text{需 }t\ge 2s\ ⟹\ t\ge4\ ✓\ \text{——本 cell }t=3\ \text{不满足}\ ✗;\quad \text{④ 模 p 同余（Wu--Chen 型）}:\ n=10\ \text{已证明落在"好同余情形"之外}\ ✗\ (\texttt{ALIGN}\ ✓)$$
$$\Longrightarrow\ \textbf{四类引擎全部不适用／已死}\ ✗\ \Longrightarrow\ \textbf{BLOCKED}\ \text{为当前阶段的诚实裁决}\ ✓$$
$$
$$
```

---

## §4 (HH-3) 唯一剩余的（允许的）判定实验（下一轮，仍不碰开 cell ✓）

```
$$\textbf{设计}:\ \text{取\textbf{已知}可扩张小对}:\ \text{如 }S(3,5,17)\supset S(2,4,16)\ (\text{导数}\ ✓),\ S(3,4,8)\ \text{型}\ ✓,\ \text{及已知不可扩张／随机 }2\text{-}(v,k,1)\ \text{设计群}\ ✓$$
$$\qquad\text{对每对：计算 }\operatorname{rank}_p(M_D)\ (p=2,3,5\ ✓),\ \text{并比较"可扩张子族"与"全体"的 rank 分布}\ ✓$$
$$\textbf{判据}:\ \text{若可扩张子族的 rank 落在\textbf{真子集}}\ \mathcal R_{\rm extend}\subsetneq\mathcal R_{\rm all}\ \Longrightarrow\ \textbf{GO}\ ✓\ (\text{机制有内容 ✓});\ \text{若两分布无差别}\ \Longrightarrow\ \textbf{DROP}\ ✓$$
$$\textbf{边界}:\ \text{此实验\textbf{不触及} }S(3,5,41)\ \text{（仅用已知设计 ✓）}\ \Longrightarrow\ \text{符合唐先生"不碰开 cell"约束 ✓；但仍属计算 ⟹ 须唐先生批准 ✓}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §2 为**结构性证明** ✓（初等 ✓：两块交 1 点 ⟹ 不正交 ✓）；§3 为**引擎清点** ✓
- §4 的判据为**提案** ✓（未执行 ✓）；**未**主张 extension 对 rank 无影响 ✗（只主张经典引擎不适用 ✓）
- **未**排除 $S(3,5,41)$ 存在 ✗、**未**排除其不存在 ✗；本档**未动算** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 自正交引擎  命中文件数=1    :: ./PHASE2-2026-09-27-rank-senses-extension.md 
技术词 rank 感知判据 命中文件数=1    :: ./PHASE2-2026-09-27-rank-senses-extension.md
```
- **本档新增**：自正交引擎的结构性否证、BLOCKED 裁决、rank 感知判据提案（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：DHV 1978、Hamada、AM 定理、KKW、FRONTIER-R3-phase1
