已查地图：已跑 scripts/prework_map_check.sh P0 P1 P2 P3 P4 P5 A≤2 逻辑审计 证据等级 ⟹ 执行自 STATUS-2026-09-26 档；本档为**全链逻辑审计**（唐先生 2026-09-26 14:31 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 主链 P0–P5 的逐箭头逻辑审计、证据等级标注、A 定义锁死、三难点定位、新全局对象 G(C) 的四要件
D1: 1（新增：**证据四级分类** ✓；**A 定义锁死（审计发现）** ✓；**P1 唯一主缺口** ✓；**G(C) 四要件** ✓）

# PROOF-AUDIT-2026-09-26 · 全链逻辑审计

## §0 证据等级约定（本档统一使用 ✓）

```
$$\textbf{[P] 我方已证} = \text{本会话/档案内给出完整推导或恒等式，并可复核}\ ✓$$
$$\textbf{[L] 文献事实} = \text{来源为文献（需逐字复核的标 ⚠️）}\ ✓$$
$$\textbf{[C] 计算观察} = \text{枚举/采样/构造得到，}\textbf{未}升为一般命题\ ⚠️$$
$$\textbf{[G] 缺口} = \text{无证明、无构造、无观察支撑}\ ✗$$
```

## §1 ⚠️ **审计发现第 1 号：A 的定义必须锁死**（唐先生 §5 指出 ✓，我方确认为真实混乱 ✗）

```
$$\text{历史用法中 "}A_{\le2}\text{" 至少混过三件事}\ ✗: \text{(a) }A_{\le2}:=A_1+A_2\ \text{（码字对计数）};\ \text{(b) "}A\le 2\text{" 当作\textbf{上界};\ \text{(c) 与 }\sum_x\binom{b(x)}2\ \text{混用}\ ✗$$
$$\textbf{锁死（本档生效 ✓）}:$$
$$\quad A_j := \#\{\{c,c'\}\subset C:\ d(c,c')=j\}\ (\text{无序码字对})\ ✓;\qquad \boxed{A_{\le2}:=A_1+A_2}\ ✓\ (\text{是\textbf{计数}，不是上界}\ ✓)$$
$$\quad \textbf{关键恒等式 [P]}: \sum_x\binom{b(x)}2=2A_{\le2}\ ✓✓\ (\text{距离}\le2\ \text{的码字对恰共覆盖 2 点}\ ✓)$$
$$\quad \Longrightarrow\ \boxed{2A_{\le2}=E+Q_2}\ ✓✓\ (\text{由 }\sum\binom b2=E+Q_2\ ✓)\ \Longrightarrow\ A_{\le2}=\frac{E+Q_2}{2}\ ✓$$
$$\Longrightarrow\ \textbf{审计结论}: \text{"界住 }A_{\le2}\text{"} \equiv \text{"界住 }Q_2\text{"}\ ✓;\ \text{历史措辞 "}A\le2\text{" 若读作上界则\textbf{无意义}}\ ✗\ \text{—— 今后一律写 }A_{\le2}\ \text{或 }Q_2\ ✓$$
$$\textbf{数值验证（三向，全过 ✓✓）}: \sum_x C(b,2)=E+Q_2\ ✓;\quad 2(A_1+A_2)=E+Q_2\ ✓;\quad \sum_xC(b,2)=2(A_1+A_2)\ ✓$$
$$\qquad (4,4):\ E=4,\ Q_2=0,\ A_{\le2}=2\ ✓;\quad (5,7):\ E=10,\ Q_2=2,\ A_{\le2}=6\ ✓;\quad (9,64):\ E=128,\ Q_2=64,\ A_{\le2}=96\ ✓$$
$$\qquad \textbf{M=62 换算}: A_{\le2}=\frac{108+Q_2}{2}=54+\frac{Q_2}{2}\ ✓\ (\text{若 }Q_2\le26\Rightarrow A_{\le2}\le67\ ✓)$$
```

## §2 P0 逐项审计（底座 ✓）

```
$$\begin{array}{c|l|c|c}
 & \text{命题} & \text{等级} & \text{备注}\\
\hline
\text{P0.1} & b(x):=|C\cap B_1(x)|\ge1\ \text{覆盖条件} & [P]\ \text{定义} & \text{无争议}\ ✓\\
\text{P0.2} & \sum_xb(x)=M(n+1);\ E:=M(n+1)-2^n & [P]\ \text{已证明} & \text{逐码字计 }n+1\ \text{点}\ ✓\\
\text{P0.3} & N_j\ \text{三层}; \sum N_j=2^n;\ \sum jN_j=M(n+1);\ E=\sum_{j\ge2}(j-1)N_j & [P] & \text{纯计数}\ ✓\\
\text{P0.4} & Q:=N_{\ge2};\ Q_2:=\sum_xC(b(x)-1,2)=\sum_{j\ge3}C(j-1,2)N_j & [P] & \text{定义＋展开}\ ✓\\
\text{P0.5} & Q_2-(E-Q)=\sum_{j\ge4}C(j-2,2)N_j\ \ge0\ \Longrightarrow\ Q_2\ge E-Q & [P]\ \text{已证＋全枚举验} & \text{等号}\iff b\le3\ ✓\\
\text{P0.6} & E-2N_{\ge3}=N_2+\sum_{j\ge4}(j-3)N_j\ge0\ \Longrightarrow\ N_{\ge3}\le E/2 & [P]\ \text{已证＋验} & \text{等号}\iff b\equiv\{1,3\}\ ✓\\
\text{P0.7} & \sum_xC(b(x),2)=2A_{\le2}\ \text{（overlap↔距离分布接口）} & [P]\ \text{已证} & \text{见§1锁死}\ ✓\\
\text{P0.8} & 4S\le Q_2\ （S=\text{完全含于 }C\ \text{的 2-面数}） & [P]\ \text{已证＋全枚举验} & \textbf{逐点版} r(x)\le C(b(x)-1,2)\ \Longrightarrow\ \sum r=4S\le Q_2\ ✓\\
\text{P0.9} & t_x=0\ \Longrightarrow\ B_1(x)\ \text{全 }b=1\ \wedge\ \text{恰 1 个距离-1 码字}\ \wedge\ \text{其余 }n-1\ \text{坐标完美匹配} & [P]\ \text{已证＋验（270/270）} & \text{奇 }n\ \text{必需}\ ✓\\
\text{P0.10} & \sum_{x\notin C}\mathrm{OC}(B_1(x))=\sum_y(b(y)-1)(n+1-b(y))\ (I1) & [P]\ \text{已证＋全枚举验} & \text{双计数}\ ✓\\
\text{P0.11} & Q_2=\frac{(n-1)E-\sum_{x\notin C}\mathrm{OC}(B_1(x))}{2}\ (I2) & [P]\ \text{已证＋全枚举验} & \text{桥的重写}\ ✓\\
\end{array}$$
$$\textbf{P0 审计结论}: \text{底座\textbf{完整且自洽}}\ ✓✓;\ \text{全部为恒等式或短证明}\ ✓;\ \text{无隐藏假设}\ ✓\ (\text{除 P0.7 依赖 }|N[c]\cap N[c']|=2\ \text{对 }d\le2\ ✓\ \text{—— 已证}\ ✓)$$
```

## §3 P1 逐路审计（唯一主缺口 ✗）

```
$$\textbf{目标 (G)}: \text{minimality}\ (|C|=K(n,1))\ +\ n\ \text{奇}\ +\ E>0\ \Longrightarrow\ Q_2\le Q_2^*(n)\ (\text{即 }A_{\le2}\ \text{被钉住})\ ✓\ \textbf{[G]}$$
$$\begin{array}{c|l|c|l}
 & \text{候选机制} & \text{等级} & \text{否证／状态}\\
\hline
\text{P1-A} & \text{单个 }B_1(x)\ \text{局部账本} & [P]\ \text{否} & \text{单位成本}\le33\ll\text{headroom}\ ✓\ \text{原理上够不着}\ ✗\\
\text{P1-B} & Z\text{-ball / gadget} & [P]\ \text{否} & \text{perfect code 反例（}Z=112,\ E=0,\ \text{结论平凡}\ ✓)\ ✗\\
\text{P1-C} & \text{private-point 计数} & [P]\ \text{否} & \text{完美码 reuse}=28\ ✗✗\\
\text{P1-D} & \text{ball-disjointness} & [P]\ \text{否} & \text{gadget 内部不交但不产生外部 excess}\ ✗\\
\text{P1-E} & \text{square concentration} & [G] & \text{只有 }4S\le Q_2\ ✓;\ \textbf{缺 }M=K\Rightarrow S\ \text{足够大}\ ✗\\
\text{P1-F} & \text{generic 二阶 }\Psi_2/Z_2 & [P]\ \text{否} & \text{Q=0 组内自变}\ ✗\\
\text{P1-G} & \Psi_{\mathrm{mid}}\ \text{中点泛函} & [P]\ \text{否} & \text{极值壳被距离分布决定}\ ✗\\
\text{P1-H} & \text{ladder}/\sigma\ \text{系统} & [P]\ \text{否} & \text{共享壳与 }u_\ell/v_\ell\ \text{断言数值证伪}\ ✗\\
\end{array}$$
$$\Longrightarrow\ \textbf{P1 审计结论}: \textbf{八条候选全灭或未立}\ ✗;\ \textbf{主缺口唯一}: \text{minimality}+n\ \text{奇}+E>0\Rightarrow Q_2\ \text{被钉}\ \textbf{[G]}\ ✓$$
$$

## §4 P2–P5 审计

```
$$\text{P2}: \text{若 }Q_2\le Q_2^*\ \text{成立，则 }\sum\binom b2=E+Q_2\ \text{给出距离分布窄约束}\ ⟹\ \text{控 }N_2,N_3,N_{\ge4},Q,Q_2\ ✓$$
$$\qquad\text{等级}: \textbf{[△ 部分接口已有]}\ ——\ \text{中间不等式齐备}\ ✓,\ \text{但 collision 依赖 P1}\ ✗$$
$$\text{P3}: \text{需 }\ \text{P1 lower}\le\text{量}\le\text{P2 upper}\ \text{相撞}\ ✓\ ——\ \textbf{目前无 collision}\ ✗\ (\text{此前把恒等式误当 P3}\ ⚠️)$$
$$\text{P4}: \text{equality}\Rightarrow\text{分类}\ ——\ \text{仅局部（}4S=Q_2\ \text{的等号分类}\ ✓）；\ \textbf{主问题分类未开始}\ ✗$$
$$\text{P5}: \text{census／等价类}\ ——\ \textbf{未进入}\ ✗;\ \text{历史资料（}n\le8\ \text{的分类}\ [L]\ ⚠️)\ \text{不能冒充本目标的 census}\ ✓$$
$$

## §5 证据分级清单（唐先生 §20 ✓，我方补标 ⚠️）

```
$$\textbf{[L] 文献事实（须逐字复核者标 ⚠️）}: K(9,1)=62\ ⚠️\ (\text{Östergård–Blass 2001 下界 ＋ Wille 1996 构造};\ \text{我方已见 Aalto 页面与 ALCOMA10 幻灯片 ✓，未读原文}\ ⚠️);$$
$$\qquad\text{covering-excess 为经典下界工具}\ ✓;\ n\le8\ \text{最优覆盖码等价分类}\ ⚠️;\ n=2^j\ \text{的结构定理（Weakley duo/tile）}\ ⚠️$$
$$\qquad\Longrightarrow\ \textbf{全部不得算作我方新证明}\ ✗$$
$$\textbf{[P] 我方已证}: E=M(n+1)-2^n\ ✓;\ N_{\ge3}\le E/2\ ✓;\ Q_2\ge E-Q\ ✓;\ 4S\le Q_2\ ✓;\ t_x=0\ \text{的匹配结构}\ ✓;\ I1,I2\ ✓;\ \text{中点引理}\ ✓;\ \text{传播引理}\ ✓;\ \mathrm{OC}\ \text{奇偶引理}\ ✓$$
$$\textbf{[C] 计算观察（不得冒充 theorem）}: \text{小 }n\ \text{全枚举};\ (9,64)\ \text{的 }4S=Q_2\ \text{饱和};\ Z\ \text{的具体值};\ \text{各 solver UNKNOWN};\ \text{gadget 不交性};\ \text{square 等号样式}\ \Longrightarrow\ \text{支持 conjecture／机制发现}\ ✓,\ \text{升级需一般证明}\ ✗$$
$$\textbf{[G] 缺口}: \text{唯一}: \text{minimality}+n\ \text{奇}+E>0\Rightarrow Q_2\ \text{被钉}\ ✓$$
$$

## §6 三大难点（唐先生 §21 ✓ 逐条确认）

```
$$\textbf{难点 1 · minimality}\to\textbf{不等式}: \text{已知 }\forall c\ \text{有私有点}\ ✓,\ \text{但未转成对 }A_{\le2}\ \text{的约束}\ ✗$$
$$\textbf{难点 2 · 奇 }n\ \text{的全球传播}: \text{奇 }n\Rightarrow n-1\ \text{偶}\Rightarrow\text{matching}\ ✓\ \text{（局部）};\ \text{需 }\text{奇性}\Rightarrow A_{\le2}\ \text{在 }Q_2\ \text{大时的全局不相容}\ \textbf{[G]}\ ✗$$
$$\textbf{难点 3 · 必须同时看见 }E>0: \text{perfect code（}E=0\text{）是最大警告牌}\ ✓;\ \text{任何在 }E=0\ \text{处不退化的机制\textbf{必然错误}}\ ✗$$
$$

## §7 下一入口：全局对象 G(C) 的四要件（唐先生 §23 ✓）

```
$$\text{需找新的全局对象 }G(C)\ \text{满足}:$$
$$\quad\text{(i) }G(C)\ \text{能由 minimality 强制}\ ✓;\quad\text{(ii) }G(C)\ \text{对奇 }n\ \text{有传播/奇偶约束}\ ✓;$$
$$\quad\text{(iii) }G(C)\ \text{中显式出现 }E>0\ ✓;\quad\text{(iv) }G(C)\ \text{最终能控制 }A_{\le2}\ (\text{等价 }Q_2)\ ✓$$
$$\textbf{排除}: \text{再加一个 }Q_3/Z_2/S_2\ \text{类局部量}\ ✗\ (\text{已证无效}\ ✓)$$
$$

## §8 骨架（唯一断箭头 ✓）

```
$$\boxed{\text{minimality}\to\text{global propagation}\to A_{\le2}\to(Q,Q_2,N_j)\to\text{collision}\to\text{classification}}\ ✓$$
$$\text{其中唯一真正断的箭头}: \boxed{\text{minimality}+n\ \text{奇}+E>0\Longrightarrow A_{\le2}\ \text{钉住}}\ ✗$$
$$

## §9 状态总表（P0.1–P1–P5）

```
$$\begin{array}{c|l|c}
\text{环节} & \text{目标} & \text{状态}\\
\hline
\text{P0.1--P0.11} & \text{定义／恒等式／接口（含 }I1,I2,4S\le Q_2,t_x=0\ \text{结构）} & \textbf{✓ 已有 [P]}\\
\text{P1} & \text{minimality＋奇 }n＋E>0\Rightarrow Q_2\ \text{钉住} & \textbf{✗ 核心 OPEN [G]}\\
\text{P2} & Q_2\ \text{小}\Rightarrow Q,Q_2,N_j\ \text{强约束} & \textbf{△ 部分接口 [P]}\\
\text{P3} & \text{lower/upper collision} & \textbf{✗ 未形成 [G]}\\
\text{P4} & \text{equality}\Rightarrow\text{结构分类} & \textbf{△ 仅局部等号分类 [P]}\\
\text{P5} & \text{census／等价类} & \textbf{✗ 未进入 [G]}\\
\end{array}$$
$$

## §10 边界（诚实标注）

- 本档为**审计与状态重述** ✓，不含新数学命题 ✓
- §5 的 [L] 项**我方仅经二手页面确认**（Aalto 出版页、ALCOMA10 幻灯片、Kéri 讲义）⚠️，**未逐字读原文** ⚠️
- §1 的 A 定义锁死为**本档新立** ✓，与档案旧措辞（"A≤2 有上界"）**不一致** ✗ ⟹ 旧文按本档解读 ✓
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：证据四级分类、A 定义锁死、全局对象 G(C) 四要件、唯一断箭头
- **档案已有（引用，不列为提出）**：P0–P5、minimality、excess、collision
