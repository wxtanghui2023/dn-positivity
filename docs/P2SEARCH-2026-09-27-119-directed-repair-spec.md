已查地图：已跑 scripts/prework_map_check.sh 119-directed repair tabu 邻域 能量 ⟹ 续唐先生 16:50 的 (甲) 核验结论（历史路线 = construction + SA + tabu/local search；**120 是上界而非已证最优** ✓）；本档 = **可复现实验层规范（邻域／目标函数／repair／acceptance ✓）**。
D0: 本档对象 = P2 construction attack 之算法规范与首轮实现
D1: 3（**(甲) 结论采纳 ✓：119 是真 P2 target，非 P1 下界问题**；**算法四要素具体化 ✓**；**判据红线：找到 119 ⟹ P2；找不到 ⟹ 仅启发式负证据 ✗ 绝不升级为 P1 ✓**）

# P2：119-directed repair/local search —— 可复现规范（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(TA-1 ✅(甲) 结论采纳（唐先生 ✓）)}\ \text{历史路线} = \boxed{\text{construction}+\text{simulated annealing}+\text{tabu/local neighborhood}}\ ✓;\ \text{文献明确}\ \boxed{K(10,1)\le120}\ \text{是\textbf{上界}（SA 只给上界、不能证最优 ✓）}}$$
$$\qquad\Longrightarrow\ \text{不可写 }K(10,1)=120\ ✗;\ \boxed{119\ \text{是真正的 P2 construction target}}\ ✓\ \text{（若得 119 ⟹ }K(10,1)\le119\ \text{＝实质改进 ✓）}$$
$$\qquad\text{附带 ✓}:\ n{=}10,R{=}1\ \text{长期是被专门构造攻击过的参数（Östergård 1991 构造 60-word mixed code ✓）} \Longrightarrow \text{该侧竞争激烈但确为活口 ✓}$$
$$\boxed{\textbf{(TB-1 ⭐算法四要素具体化（可复现 ✓）)}\ \text{状态}:\ S\subseteq\mathbb F_2^{10},\ |S|=119\ ✓;\ \text{hole 集 }H(S)=\{x:\ d(x,S)>1\}\ ✓;\ \text{能量 }\mathcal E=|H|\ (+\lambda\cdot\text{二阶惩罚}\ ✓)}$$
$$\qquad\textbf{① 邻域（targeted repair ✓，非裸随机 ✗）}:\ \text{取 }y\in H\ \text{随机};\ \text{新位置 }c'\!\in B_1(y)\ \text{（保证覆盖 }y\ ✓\text{）};\ \text{被替换者 }c^\ast=\arg\min_c\ \#\{z\in B_1(c):\ \mathrm{cnt}(z){=}1\}\ \text{（唯一覆盖数最小者 ✓）}$$
$$\qquad\textbf{② tabu}:\ \text{最近移除点 }c^\ast\ \text{进入 tabu 表（tenure }\tau\approx10\text{--}20\ \text{迭代 ✓），期内禁止回插 ✓ ⟹ 防止 }(c,c')\ \text{来回交换 ✓}$$
$$\qquad\textbf{③ acceptance}:\ \Delta\mathcal E\le0\ \Longrightarrow\ \text{接受};\ \Delta\mathcal E>0\ \Longrightarrow\ \text{以 }\exp(-\Delta\mathcal E/T)\ \text{接受（}T\ \text{几何降温 }\times0.9999\ ✓\text{）};\ \text{周期升温以逃逸 ✓}$$
$$\qquad\textbf{④ 终止／验收}:\ |H|=0\ \Longrightarrow\ \textbf{立即独立验证全部 1024 点}\ \boxed{\forall x:\ |S\cap B_1(x)|\ge1\ \wedge\ |S|=119}\ \Longrightarrow\ \text{witness 落盘 ＋ P2 成立 ✓✓}$$
$$\qquad\textbf{实现要点 ✓}:\ \text{增量 } \mathrm{cnt}[\cdot]\ \text{维护（O(22)/步 ✓）} \Longrightarrow \sim10^5\ \text{步/秒 ✓};\ \text{每 restart 记录 best }|H|\ \text{与耗时 ✓}$$
$$\boxed{\textbf{(TC-1 🔴判据红线（已锁定 ✓，不得违反 ✗）)}\ \boxed{\text{找到 119}\Longrightarrow P2\ \text{成立（真实 upper-bound dent ✓）};\quad \text{找不到}\Longrightarrow \textbf{仅启发式负证据 ✗，绝不可升级为 P1}\ ✓}}$$
$$
$$
```

## §1 首轮（裸 SA）实测记录（**✗ 不足，已被本规范取代 ✓**）

```
$$\text{首轮 twohalf2（两半构造）}:\ 124\ \text{词合法覆盖 ✓ 但\textbf{不可约}（贪心一句删不掉 ✗）、局部搜索 25.4 万次迭代\textbf{零改进} ✗ \Longrightarrow \text{两半结构僵死 ✓（须打破 ✓）}$$
$$\text{首轮 anneal（裸 SA，}m{=}119\text{）}:\ \text{以 hole count 为能量、随机选洞＋随机移动 ✗（\textbf{无 targeted repair、无 tabu} ✗）} \Longrightarrow \text{已被 (TB-1) 取代 ✓}$$
$$
$$
```

## §2 状态（**✓**）

```
$$\boxed{P0:\ K(10,1);\quad P2:\ K(10,1)\le120\ (\text{历史构造 ✓});\quad P1:\ K(10,1)\ge120\ \text{未证};\quad \textbf{target}:\ |C|\le119\ ✓}$$
$$\qquad\text{刚结束 MIP（dual 99 / primal 138）只说明\textbf{通用 exact-MIP 路线 900s 未解决} ⟹ \textbf{不改变上述数学状态 ✓}}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：119-directed repair 规范四要素（邻域／tabu／acceptance／验收）、两半构造僵死之实测记录、判据红线
- **档案已有（引用，不列为提出）**：A-MIPRUN-1/2、A-PROJCUT-1、21 条封口表、唐先生 (甲) 核验结论


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 targeted repair  命中文件数=1    :: ./P2SEARCH-2026-09-27-119-directed-repair-spec.md 
技术词 判据红线     命中文件数=1    :: ./P2SEARCH-2026-09-27-119-directed-repair-spec.md
```
- **本档新增**：119-directed repair 规范四要素、两半构造僵死之实测记录、判据红线（见上方命中数；0 命中者为自造语／内部标签 ✓）
