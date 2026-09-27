已查地图：已跑 scripts/prework_map_check.sh 交接 119 P2 搜索 ⟹ 本档 = **新会话用自包含交接档（含卡点／定义／唯一动作／红线 ✓）**。
D0: 本档对象 = 119 线会话交接（P2 construction attack reproduction 阶段）
D1: 2（交接整理 ＋ 状态固化 ✓，不含新数学命题 ✗）

# 119 线交接档（2026-09-27 18:18 GMT+8）

## §0 一句话状态
$$\boxed{\text{P0}:K(10,1)\quad \text{P2}:K(10,1)\le120\ (\text{历史构造})\quad \text{P1}:K(10,1)\ge120\ \textbf{未证}\quad \textbf{target}:|C|\le119}$$
$$\text{当前阶段}=\textbf{P2 construction attack 的 reproduction 阶段}（\text{搜索实现未达文献水准 ⟹ 尚未产生任何 P1/P2 结论 ✓}）$$

## §1 本会话已确立结论（分层 ✓）
- **21 条机制封口**：档案既有 18（GAPTHEOREM/PROPAGATION/FAILSET/SCOL/MIDSUP/FACE/T3-MIN-1/L-GREEN-1/GRAM-LIFT/HQ1/L4AUDIT/STAR3/M-1/M-2A/M-2A′/M-2B/Fourier/Del6）＋ 本会话 3（**A5 surplus×支撑**／**A4 局部一致性**／**g=11T⁻¹δ 模 11 核**）⟹ 末端：**21 mechanisms CLOSED ⟶ irreducible core = Boolean covering feasibility**
- **整数覆盖形 = 等价重参数化**（$\min\{\mathbf 1^Tf:Tf\ge1,f\in\mathbb Z_{\ge0}\}=K(n,1)$ ✓）**非松弛** ✗（资产 A-INTRELAX-1 ＋ 改档 A-INTRELAX-REFILE-1）
- **投影割 = covering 约束之和** ⟹ **正锥内割先验无力** ✗✓（资产 A-PROJCUT-1；并解释 A4/SA 之无力为结构性 ✓）
- **MIP 900s 终态**：dual 99.0 / primal 138 / gap 28% ⟹ **UNKNOWN** ✗（资产 A-MIPRUN-1/2）⟹ 通用 exact-MIP 路线 900s 未解决 ✓
- **P2 搜索规范四要素**（targeted repair 邻域／tabu／SA acceptance／独立验收 ✓）＝ 资产 A-P2SEARCH-1
- **m=120 自检门 FAILED** ✗（已知 120 可行 ⟹ 必须能搜到，实测 best_unc 24–34 ✗）＝ 资产 A-P2VAL-1 ⟹ **实现未达文献水准 ✓**
- **搜索代际记录**：lns2（65k 步 **零接受** ✗ 因"禁用 R"导致接受门逻辑不可能触发 ✓）→ lns3（148 起点亦零下降 ✗）→ lns4（Metropolis 修复 ✓ 但停 **143** ✗）→ kopt1（acc=0 ✗ 同因）→ **kopt2**（acc 3.1–6.3 万 ✓、neutral 3.1–6.3 万 ✓、**max_R=2** ✓、first R≥1 ≤1517 步 ✓、**desc=0** ✗）→ **kopt3**（cleanup 生效 ✓ 每次真删 1 词 ✓，但净效应 **125→124 中性** ✗）

## §2 当前精确卡点（下一步的**唯一**问题 ✓）
$$\text{要得 }124\to123\ \text{，需存在}\ \boxed{|S|{=}124,\ h{=}0,\ R\ge1}\ \text{的状态（纯中性移动 }r{=}k\ \text{且新结构含可删词 ✓）} \Longrightarrow \text{此时 cleanup 立即给 }123\ ✓$$
$$\text{现状只观测到 }r{=}k{+}1\ (|S|{=}125)\Longrightarrow \text{cleanup 只把 125 拉回 124}\ ✗$$
$$\Longrightarrow \boxed{\textbf{瓶颈}=\text{repair 能否产出"等基数但带冗余"的 124 码}}\ ✓\ \text{（\textbf{不是}"能不能删"——已证能删 ✓）}$$

## §3 精确定义（防误用 ✓ 唐先生校正）
$$\textbf{U}(c):=B_1(c)\setminus B_1(C\setminus\{c\})\ ✓;\quad U(c)=\varnothing\iff c\ \text{可直接删除}\iff C\setminus\{c\}\ \text{仍是覆盖码（123 词, }h{=}0\ ✓\text{）}$$
$$\textbf{R}(C):=\#\{c:U(c)=\varnothing\}\ =\ \textbf{严格可删除词数}\ \Longrightarrow\ \boxed{R\ge1\ \Longrightarrow\ \exists c\ \text{可直接删除}}\ ✓\quad \textbf{不得称"伪冗余"}\ ✗$$
$$\text{删除后 }H=\text{未覆盖点};\quad \rho(H):=\min\{|X|:H\subseteq B_1(X)\}\ ✓;\quad \rho(H){=}1\iff\ \text{存在直接 }124\to123\ ✓$$

## §4 下一轮**唯一**动作
```
① 恢复四事件分开计数：accepted ／ neutral(|S|不变) ／ R>=1 ／ descent
   ＋ **新增判定性事件：neutral 且 R>=1** ✓（唐先生机制假设的唯一未观测环节 ✓）
② 若该事件出现 ⟹ 立即 cleanup ⟹ 123（机制获证 ✓✓）
③ 若大量 neutral 而 R 恒 0 ⟹ 情形 B（等基数轨道无出口 ✓，干净负结论 ✓）
④ 120/119 **不碰** ✗；只有 |C|=120 ∧ h=0 才做 **1024 点独立逐点验证** ✓
```

## §5 红线（硬 ✓）
```
· 找不到 ⟹ 只记"该配置／预算未找到" ✗，**绝不推出 }K(10,1)\ge120** ✗
· /tmp/cov ＝ covering-**design** 搜索器（Nurmela–Östergård）⟹ 与 code 搜索**严格分账** ✗，不得称"复现" ✓
· 不写"不可能／不存在／方向已死" ✗（MASTER-STATUS 纪律 ✓）
· 有限时间 MIP bound ≠ relaxation family 理论最优值 ✗（94.027/99.0 均只能作"本次运行观察" ✓）
```

## §6 关键文件与命令
```
· 基准码：work/k10/c62/keri_pool/K_9_1_classif.txt（两个 62-码 → 两半构造 124 词，合法覆盖 ✓ 不可约 ✓）
· 脚本（未入仓，可重建）：/tmp/kopt2.py、/tmp/kopt3.py、/tmp/lns4.py、/tmp/twohalf2.py
· 运行：setsid nohup bash ~/.openclaw/workspace/scripts/pyguard.sh 2500 <script> > /tmp/<log> 2>&1 &
   ⚠️ 不要轮询 ✗；用 cron 到点检查 ✓；按 PID kill ✓（绝不 pkill -f 含自身串 ✗）
· 自检门：**m=120 必须先 h=0** 才算实现达标 ✓（未过则一切 119 读数无效 ✗）
· 验收：|C|=120 ∧ h=0 ⟹ 独立逐点验证全部 1024 点 ✓
```

## §7 文献（唐先生 (甲) 核验 ✓）
```
· 历史路线 = construction + **simulated annealing** + **tabu/local search**
· **120 是上界**（SA 只给上界）⟹ **不可写 K(10,1)=120** ✗；119 是真 P2 target ✓
· Östergård 1991 已有 60-word mixed code 改进该参数 ⟹ 该侧长期为活口 ✓
· 下界侧：107（BÖW 2004）远低于 119；LP 93.09、SDP 105.2、本 MIP 99.0 ⟹ **证明侧被现有技术堵死** ✓
```
