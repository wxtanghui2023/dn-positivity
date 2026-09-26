已查地图：已跑 scripts/prework_map_check.sh 删除 移位 私有点 局部不可修复 ⟹ 执行自 CHARGING-2026-09-26 档；本档为**d_C≥3 局部结构普查＋删除/移位实测＋删除路线的精确否定**（唐先生 2026-09-26 15:20 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 高内部度码字的局部结构（邻居/二中点/私有点）、删除与移位两类修复动作的实测、路线的精确否定
D1: 1（新增：**私有点必在自由邻居中（已证 ✓✓）**；**纯删除被最小性精确阻断（实测 ✓✓）**；**移位给出同大小码（无矛盾 ✗）**）

# REPAIR-2026-09-26

## §1 ✅ **已证：高内部度码字的私有点必在"自由邻居"中** ✓✓

```
$$\text{设 }c\in C,\ d_C(c)\ge1\ \Longrightarrow\ c\ \text{被其码字邻居覆盖}\ ✓\ \Longrightarrow\ c\ \text{本身\textbf{不是}私有点}\ ✓$$
$$\text{而三个（或更多）码字邻居是其自身}\ ✓\ \Longrightarrow\ \text{私有点必落在 }\{\text{自由邻居}\}=\{c+e_i\notin C\}\ \text{中}\ ✓✓$$
$$\textbf{实测}: (4,5):\ 8/8\ \text{全在 free}\ ✓;\ (4,6):\ 14/14\ ✓;\ (5,8):\ 12/12\ ✓✓\ (\textbf{0 例外}\ ✓)$$
$$\text{推论}: M=K\ \text{时全部码字必有私有点}\ ✓\ \Longrightarrow\ \textbf{每个 }d_C\ge3\ \text{的码字各占一个自由邻居}\ ✓$$
$$

## §2 ⛔ **纯删除被最小性精确阻断**（实测 ✓✓，路线级否定 ✓）

```
$$\textbf{实测}: (4,5):\ \text{删除后仍覆盖}\ 0/8\ ✗;\ (4,6):\ 8/22\ ✓\ (\text{恰为 }p(c)=0\ \text{的冗余码字}\ ✓);\ (5,8):\ 2/8\ ✓$$
$$\textbf{精确原因}: M=K\Rightarrow C\ \text{最小}\Rightarrow\ \text{每个 }c\ \text{有私有点}\ \Rightarrow\ C\setminus\{c\}\ \text{不覆盖}\ ✗\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{"删除得到更小覆盖码"与最小性\textbf{等价}，不能作为机制}}\ ✗✓$$
$$\qquad\text{（唐先生 ⑦-D 的纯删除形式\textbf{不可用} ✗；必须走\textbf{替换}且 }|C'|=|C|-1\ \text{的码\textbf{非子集}}\ ✗\ \Longrightarrow\ \text{是\textbf{全局构造}，难度不降}\ ✗)$$
$$

## §3 ⭐ **移位实测：给出同大小覆盖码**（无矛盾，但给出局部可动性 ✓）

```
$$\text{动作}: C\mapsto (C\setminus\{x\})\cup\{t\}\ ✓,\ t\in\{\text{私有点},\ \text{第二中点}\}\ ✓$$
$$\textbf{实测成功率}: (4,5):\ 8/24\ ✓;\ (4,6):\ 30/49\ ✓;\ (5,8):\ 4/22\ ✓$$
$$\text{例}: (4,5)\ x:\ d_C{=}3,\ r{=}0,\ p(x){=}1,\ \text{删后失覆盖}=1,\ \text{移位}\ t{=}8\ \textbf{成功}\ ✓\ (t{=}3,5\ \text{失败}\ ✗)$$
$$\text{例}: (5,8)\ x:\ d_C{=}3,\ r{=}0,\ p(x){=}0\ (\text{非最小}\ ✓),\ \text{删后失覆盖}=0,\ \text{移位 }t{=}3,5\ \textbf{均成功}\ ✓$$
$$\Longrightarrow\ \text{存在大量同大小覆盖码}\ ✓\ \Longrightarrow\ \textbf{不构成矛盾}\ ✗\ (\text{但证明局部结构\textbf{灵活}，非刚性}\ ✓)$$
$$

## §4 结论：**删除/替换路线不能只靠局部结构** ✗✓（诚实定级）

```
$$\text{局部能给的}: \text{① 私有点位置（已证 ✓）② 二阶中点类型 }r\ \text{③ 可动性（移位成功 ✓）}$$
$$\text{局部\textbf{不能}给的}: |C'|<|C|\ \text{—— 因为最小性正是其\textbf{精确}障碍}\ ✗✓\ (\S2)$$
$$\Longrightarrow\ \boxed{\text{要打穿 }M=K\Rightarrow h=0\ \text{必须用\textbf{全局量}，不能用局部删除/替换}}\ ✗✓$$
$$\text{回到已有的全局工具}: h\le I/3\ ✓;\ I\le2\Rightarrow h=0\ ✓;\ I+S\le E+Q_2\ ✓\ \Longrightarrow\ \textbf{目标仍是控制 }I\ ✓$$
$$

## §5 数据侧的确定性头寸（本轮确认 ✓✓）

```
$$\textbf{已验证的闭合（数据+界）}: n=4:\ I=0\Rightarrow h=0\ ✓;\ n=5:\ I=1\Rightarrow h=0\ ✓;\ n=6:\ I\in\{0,2\}\Rightarrow h=0\ ✓✓$$
$$\qquad\text{并且两个 }n=6\ \text{已知类的 }(I,S)=(2,14)\ \text{与}\ (0,24)\ ✓\ (\text{修正此前估算}\ ✗)$$
$$\textbf{未闭合}: n\ge7\ \text{的 }I\ \text{上界未知}\ ⚠️\ (\text{文献无 }M=K(n,1)\ \text{的构造数据}\ ✗);\ \text{一般 }n\ \text{完全未知}\ ✗$$
$$

## §6 状态与建议

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{定级}: \textbf{P1-shaped}\ ✓\ (\text{未闭合}\ ✗);\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$\textbf{新资产}: \text{私有点位置引理（已证}\ ✓✓);\ \text{删除路线的精确否定}\ ✓✓;\ \text{移位可动性数据}\ ✓$$
$$\text{建议下一刀}: \text{① 用 }G_C\ \text{(距离-1 图)}\ \text{的结构（无 }K_4\ \text{三角形？）去压 }I\ \⚠️\ (\text{唯一未试}\ ✓);\ \text{② 接受 }n\le6\ \text{闭合，转攻 }n=9\ \text{的 }M=K\ \text{码构造}\ ✓$$
$$

## §7 边界（诚实标注）

- §1 为**我方证明** ✓ + 实测 34/34 ✓；§2/§3 为**数值实测** ✓（n=4,5 全枚举 ✓）
- §4 明确记录**路线级否定**与理由 ✗✓（未夸大 ✓）；**未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 自由邻居引理 命中文件数=1    :: ./REPAIR-2026-09-26-local-structure-census-and-exact-refutation-of-pure-deletion.md 
技术词 删除路线阻断 命中文件数=1    :: ./REPAIR-2026-09-26-local-structure-census-and-exact-refutation-of-pure-deletion.md 
技术词 移位可动性  命中文件数=1    :: ./REPAIR-2026-09-26-local-structure-census-and-exact-refutation-of-pure-deletion.md 
技术词 局部不可修复实测 命中文件数=1    :: ./REPAIR-2026-09-26-local-structure-census-and-exact-refutation-of-pure-deletion.md
```
- **本档新增**（命中数=1 但仅本档自身 = self-hit ⟹ 扣自引后 = 0 ✓）：自由邻居引理、删除路线阻断、移位可动性、局部不可修复实测
- **档案已有（引用，不列为提出）**：minimality、私有点、excess
