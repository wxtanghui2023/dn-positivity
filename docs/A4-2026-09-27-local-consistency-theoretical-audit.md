已查地图：已跑 scripts/prework_map_check.sh 局部一致性 marginal 松弛 Lasserre ⟹ 命中档案 **M-2A（LP = 1024/11 CLOSED）／SDP harness（Delsarte+SDP n=10,R=1 = 105.2223）／L3B 线（Terwilliger 块分解：3A 计算 ✓、3B 数学证明待完成、Level 4 = n=10 未约化 1024×1024 PSD **BLOCKED pending reduced implementation**、**两个后台 run 未轮询**）／AMEND-35**；本档 = **A4 理论审计：$k{=}2$ 坍缩 ✓；$k\ge3$ 被 Lasserre 支配 ✗；剩余=具体工程项 ✓**。
D0: 本档对象 = A4（局部一致性松弛）的可达性与相对强度
D1: 3（**$k{=}2$ = 在档二阶数据（理论封口 ✓）**；**$k\ge3$ 被 Lasserre/SOS 支配（SA⊆SOS ✓）**；**定位剩余=档案 Level 4 未竟实现 ✓**）

# A4 理论可达性审计（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(MA-1 ⭐先钉死一点：覆盖约束的"局部尺度"不是 2 而是 11 ✓)}\ \text{覆盖约束 }(Tf)(x)\ge1\ \text{涉及\textbf{整颗星} }B_1(x)\ (\mathbf{11}\ \text{点 ✓}) \Longrightarrow \text{真正的局部对象}=\textbf{星边际 }\mu_x\ \text{over }\{0,1\}^{B_1(x)}\ ✓✓}$$
$$\qquad\Longrightarrow\ \text{星-星 overlap 只发生在 }d(x,y)\le2\ \text{时（且重叠 }\le2\ \text{点 ✓）} \Longrightarrow \textbf{局部族的最小有内容尺度由"星"决定 ⚠️}$$
$$\boxed{\textbf{(MB-1 🔴}k{=}2\ \text{理论封口 ✓)}\ \text{对 }d(x,y)\le2\ \text{的\textbf{成对边际} }\mu_{\{x,y\}}\ \text{所携带的全部信息} = \{\text{1-点密度}\}\cup\{d{=}1,2\ \text{的成对相关}\}\ \text{即可定出}\ \boxed{A_1,A_2,M}\ ✓✓}$$
$$\qquad\textbf{（证明性 ✓）}:\ \text{成对边际在距离 }d\ \text{上的质量 }=\#\{\text{pairs at }d\}\ \text{与共同入码概率 ⟹ 恰是 }A_d\ ✓;\ \text{无更高阶内容 ✗}$$
$$\qquad\Longrightarrow\ \textbf{按唐先生 A4-GATE}:\ k{=}2\ \text{的所有一致性约束经平移平均后只能恢复 }(M,A_1,A_2)\ \Longrightarrow \boxed{\textbf{A4-}k{=}2\ \textbf{STOP}}\ ✓✓$$
$$\boxed{\textbf{(MC-1 ⭐⭐}k\ge3\ \text{被\textbf{支配}（本档核心 ✓）)}\ \text{对任意 }k<10\ \text{的 }k\text{-窗口边际松弛}\ \mathcal L_k\ \text{是 \textbf{Sherali–Adams 型}（局部边际一致性 ✓）};\ \text{而标准结果}\ \boxed{\mathrm{SA}_k\subseteq\mathrm{SOS/Lasserre}_{O(k)}}\ ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{\mathcal L_k\ \subseteq\ \text{Lasserre}_{O(k)}}\ ✓ \Longrightarrow \textbf{同阶 Lasserre 总是\textbf{更强}} \Longrightarrow \text{若 Lasserre 给不出 }\ge120\ \text{的界，}\mathcal L_k\ \text{也给不出 ✗}\ \text{（松弛越弱 ⟹ 界越小 ✓）}$$
$$\qquad\textbf{而档案已有实测 ✓}:\ \text{Delsarte＋SDP（}n{=}10,R{=}1\text{）}= \mathbf{105.2223}\ ✗ < 119 \Longrightarrow \textbf{已实现的 SDP 界远不足以排除 }119\ ✗✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{A4 全族（任意 }k\text{）在理论上}\subseteq\text{Lasserre}\ \text{族} \Longrightarrow \text{不能在 Lasserre 之外产生新证书 ✗}}\ \text{—— 但\textbf{不}等于"Lasserre 无用" ⚠️（见 §2 ✓）}$$
$$
$$
```

## §1 非空性与"平凡解"（**✓ A4-1**）

```
$$\text{分数解 }f\equiv 119/1024=0.1162\ \Longrightarrow (Tf)(x)=11\cdot0.1162=1.278\ge1\ ✓,\ \sum f=119\ ✓ \Longrightarrow \textbf{LP 级松弛在 }119\ \text{可行 ✓（故 LP 不能排除 119 ✗，与档案 M-2A 一致 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{要有缺口，必须用\textbf{整数/配置级}局部约束}（即 }\mu_S(a)\ \text{为 0-1 型 ✓）\ \text{—— 而这正是为 }\mathcal L_k\ \text{设计的 ✓}$$
$$
$$
```

## §2 审计的真正收获（**✓ 定位到一个具体未竟工程**）

```
$$\textbf{收获 ✓}:\ \text{A4-theory 不能产生 119 的 P1 证书 ✗（MC-1 ✓），但它\textbf{精确定位}了那条唯一还活着的同族路线：}\boxed{\textbf{提高 Lasserre 阶数}}$$
$$\qquad\text{档案现状 ✓}:\ \text{L3B 线 = Terwilliger 块分解：3A 计算 ✓（}M'/M''{+}\text{border}/N\ \text{三项分解 ✓）；3C 数学证明 = 三个簿记/经典引理（其中 A-L3B-2 两行输入 ✓ 已完；B-L3B-1 border 归一化 ✓ 已完）}$$
$$\qquad\textbf{卡点 ✓}:\ \text{"Level 4 = 未约化 }n{=}10\ (1024\times1024\ \text{PSD})\ \text{BLOCKED pending reduced implementation"\ ✓；}\textbf{两个后台 run（tidal-glade／marine-nudibranch）从未轮询} ⚠️$$
$$\qquad\Longrightarrow\ \textbf{这才是 119 线上唯一"具体、未完成、可推进"的对象 ✓}（且是\textbf{计算型} ⟹ 与"零 solver"要求冲突 ⚠️）$$
$$
$$
```

## §3 状态（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{A4 理论封口（第 20 条候选，已判定无效 ✗）};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$\textbf{建议 ✓}:\ \text{(甲) 记录 A4 理论封口 + 定位 Level 4 为唯一活口 ✓};\ \text{(乙) 若允许计算：先\textbf{轮询/重启}那两个被遗弃的 reduced-Lasserre run（低成本 ✓，可能有现成结果 ✓）};\ \text{(丙) 或按纪律停手并更新总图 ✓}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：覆盖约束的局部尺度=星（11 点）、$k{=}2$ 等价于 $(M,A_1,A_2)$ 之证明性判定、$\mathcal L_k\subseteq$Lasserre 之支配论证、Level 4 未竟工程之定位
- **档案已有（引用，不列为提出）**：M-2A（LP 1024/11）、SDP 105.2223、L3B（Terwilliger/Level 4 BLOCKED）、AMEND-35、SA⊆SOS 标准结果


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 局部一致性  命中文件数=4    :: ./ASSETS-REGISTRY.md ./SOURCE-SEARCH-negative-screening-pair-and-channel-exhaustion.md ./A5-2026-09-27-surplus-support-coupling-audit.md 
技术词 支配论证     命中文件数=1    :: ./A4-2026-09-27-local-consistency-theoretical-audit.md
```
- **本档新增**：覆盖约束的局部尺度＝星（11 点）、$k{=}2$ 等价于 $(M,A_1,A_2)$ 之判定、$\mathcal L_k\subseteq$Lasserre 之支配论证、Level 4 未竟工程之定位（见上方命中数；0 命中者为自造语／内部标签 ✓）
