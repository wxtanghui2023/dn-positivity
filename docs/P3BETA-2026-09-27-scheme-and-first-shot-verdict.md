已查地图：已跑 scripts/prework_map_check.sh P3-β 剪枝 9 块 ⟹ 执行自 `P3JIA-2026-09-27-...`（✓）＋ 唐先生 13:33（开 β，先方案后一枪 ✓）；本档 = **β 方案 ＋ 第一枪判定（STOP-β，含自身修正与加强 ✓）**。
D0: 本档对象 = 9 块剪枝链的可行性与第一枪结果
D1: 2（**方案 ✓**；**第一枪：STOP-β ＋ (d',s)↔A₂ 非一一对应（自我修正 ✓）＋ J 分辨 ⊥ 子类（加强 ✓）**）

# P3-β：方案与第一枪（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BT-1 方案 ✓)}\ \text{剪枝链}=\text{候选}\to(d',s)\to\text{算术/affine 必要条件}\to\text{排除};\ \textbf{预固定 gates}:\ \text{STOP-}\beta\text{-1（只复用已知 }A_2/B_i\text{ 关系）};\ \text{STOP-}\beta\text{-2（affine 只是定义重述）};\ \text{PASS-}\beta\text{（须\textbf{排除}一个原本未排除的块）}}$$
$$\boxed{\textbf{(BT-2 ⚠️ 标量修正（对我方表述 ✓）)}\ \textbf{不是 }\lambda=J\ ✗\ \text{（唐先生 P1-b 处）}\ \text{正确关系}:\ \boxed{\lambda=\frac{A_2}{|S|}},\quad J=\lambda A_2=\frac{A_2^2}{|S|}\ ✓✓\ \text{（9 块算术表逐项验过 ✓）}}$$
$$\qquad\text{根源}:\ \sum_vq_v=A_2\ \text{（\textbf{不是 }A_2^2 ✗）}\ \text{——}q\ \text{计数距离-2 跨界对 ✓;\ 用 }n=16\ \text{实例核}:\ \lambda{=}128,\ |S|{=}15,\ A_2{=}1920\ \Longrightarrow\ \lambda{=}1920/15{=}128\ ✓,\ J{=}128\cdot1920{=}245760\ ✓}$$
$$\boxed{\textbf{(BT-3 ⭐自我修正 ✓)}\ (d',s)\ \textbf{不}与 }A_2\ \text{一一对应} ✗:\ \textbf{四个 }\bot\text{ 块}(d'{=}0,1,2,3)\ \textbf{共享 }A_2{=}2048=M/2\ (A_1{=}0\ ✓)\ \text{但 }J\ \text{各异}:\ \{2^{22},2^{21},2^{20},2^{19}\}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{这正是 }n=8\ \text{P1-2 PASS 现象的}\textbf{升维版} ✓（n{=}8:\ (0,16)\ \text{桶 }3\ \text{子类 }J{=}256/128/64\ ✓;\ n{=}16:\ \bot\ \text{族 }m{=}4\ \text{子类}\ ✓✓\text{）}$$
$$\boxed{\textbf{(BT-4 第一枪判定 = STOP-}\beta\ ✓)}\ \text{9 块\textbf{全部可实现}（纯代数论证 ✓，}(4,\bot)\ \text{不可实现 ✓）\ \Longrightarrow\ \text{任何必要条件\textbf{排除不了任一块}} \Longrightarrow\ \textbf{PASS-}\beta\ \text{判据不可达} \Longrightarrow\ \textbf{STOP-}\beta\text{-1}\ ✓}$$
$$
$$
```

---

## §1 9 块算术表（**✓ 全项验过**）

```
$$\begin{array}{c|c|c|c|c|c|c|c}
d' & s\in\mathrm{Im}f & \lambda & |S| & A_2=\lambda|S| & A_1=2048-A_2 & J=\lambda A_2 & \text{可实现?}\\
\hline
0 & \top & 2048 & 0 & 0 & 2048 & —\ (\text{退化 }\lambda\ \text{无定义 ✓}) & ✓\\
0 & \bot & 2048 & 1 & 2048 & 0 & 2^{22} & ✓\\
1 & \top & 1024 & 1 & 1024 & 1024 & 2^{20} & ✓\\
1 & \bot & 1024 & 2 & 2048 & 0 & 2^{21} & ✓\\
2 & \top & 512 & 3 & 1536 & 512 & 3\cdot2^{18} & ✓\\
2 & \bot & 512 & 4 & 2048 & 0 & 2^{20} & ✓\\
3 & \top & 256 & 7 & 1792 & 256 & 7\cdot2^{16} & ✓\\
3 & \bot & 256 & 8 & 2048 & 0 & 2^{19} & ✓\\
4 & \top & 128 & 15 & 1920 & 128 & 15\cdot2^{14} & ✓\\
(4,\bot) & \bot & 128 & 16>15 & \textbf{不可实现} ✗ & — & — & ✗\\
\end{array}$$
$$\textbf{算术审计 ✓}:\ \lambda=A_2/|S|\ ✓\ \text{与}\ J=\lambda A_2\ ✓\ \text{在 8 个非退化块\textbf{全部成立}};\ |S|\mid A_2^2\ \text{全成立} ✓ \Longrightarrow\ \textbf{算术层无剪枝力} \Longrightarrow \text{STOP-}\beta\text{-1}\ \text{部分触发} ✓$$
$$\qquad\textbf{重要发现 ✓}:\ \text{四个 }\bot\ \text{块的 }A_2\ \text{全为 }2048\ \text{——}\textbf{块不含超出 }(A_1,A_2)\ \text{的...不，含 }J\ ⚠️\ \text{（见 BT-3 ✓）}$$
$$
$$
```

---

## §2 可实现性（**✓ 纯代数，P2 攻击点 ✓**）

```
$$\text{(i)}\ \mathrm{Im}\,g=\mathbb F_2^4\ \text{（}g\ \text{的 15 列 = 全部非零向量 ⟹ 满射 ✓）};\ \text{(ii)}\ d'=4\Longrightarrow\mathrm{Im}f=\mathbb F_2^4\Longrightarrow s\in\mathrm{Im}f\ \text{恒真} \Longrightarrow \boxed{(4,\bot)\ \text{不可实现}}\ ✓$$
$$\text{(iii)}\ d'\le3\Longrightarrow\mathrm{Im}f\subsetneq\mathbb F_2^4\ \text{且}\ \mathrm{Im}g=\mathbb F_2^4\Longrightarrow\exists e:\ s=g(e)\notin\mathrm{Im}f \Longrightarrow (d',\bot)\ \text{可实现} ✓$$
$$\text{(iv)}\ e=0\Longrightarrow s=0\in\mathrm{Im}f \Longrightarrow (d',\top)\ \text{可实现} ✓ \quad（\text{配合 §1 的 }d'{=}0..4\ \text{已全部实例化 ✓）}$$
$$\Longrightarrow\ \textbf{9 块全部可实现} \Longrightarrow \text{必要条件只能"描述"块、\textbf{不能排除}块} \Longrightarrow \textbf{PASS-}\beta\ \text{判据不可达 ✓}\ \text{（遵唐先生：不得以"某块不可能"推"整 Type 不可能" ✓）}$$
$$
$$
```

---

## §3 加强：$\bot$ 族的 $J$ 分层（**⭐ 与 P1-2 PASS 同型 ✓**）

```
$$\text{四个 }\bot\ \text{块}:\ (A_1,A_2)=(0,2048)\ \text{完全相同}\ ✓;\ \lambda=2^{11-d'},\ |S|=2^{d'}\ \text{各异} \Longrightarrow J=2^{22-d'}\ \text{各异}\ ✓✓$$
$$\qquad\Longrightarrow\ \textbf{同一 }(A_1,A_2)\ \text{桶内有 }m=4\ \text{个 }J\ \text{层};\ \text{且该分层\textbf{被文献的 Type 分类与重量分布层完全看不见}} ✓（\text{Type B 只有一种重分布 ✓）$$
$$\qquad\text{与 }n=8\ \text{对照 ✓}:\ (0,16)\ \text{桶 }J\in\{256,128,64\}\ (3\ \text{层},\ =m_{n=8}\ ✓);\ n=16:\ \bot\ \text{族 }m=4\ \text{层 ✓} \Longrightarrow \textbf{层数}=m\ \text{的统一定律} ✓✓$$
$$\qquad\textbf{诚实标注 ✓}:\ \text{这是 A-ALIGNTHM-1 的直接推论（非新定理 ✓），本档价值 = 把"}(d',s)\ \text{与 }A_2\ \text{一一对应"这一\textbf{我方旧表述证伪}} ✗\ \text{并给出正确图景 ✓}$$
$$
$$
```

---

## §4 判定与下一步（**✓**）

```
$$\textbf{P3-}\beta\ \text{判定}:\ \textbf{STOP-}\beta\text{-1 触发} ✓\ \text{（算术层只复用已知 }A_2/J\ \text{关系，无新剪枝力）};\ \textbf{STOP-}\beta\text{-2 部分触发} ✓\ \text{（affine support 是\textbf{族内定理}，作为一般候选剪枝工具需先有"候选属于 Theorem-13 形" ✓）}$$
$$\qquad\textbf{PASS-}\beta\ \text{不可达}（9 块全可实现 ✓）\ \Longrightarrow\ \textbf{不得声称任何块被排除} ✓$$
$$\text{唯一能改变此判定的问题}:\ \boxed{\text{Theorem-13 形是否为\textbf{全部} NP1CC（通用性）}} \Longrightarrow\ \text{若真，则 }(d',s)\ \text{升级为全体 NP1CC 的粗不变量（\textbf{研究级} ⚠️）};\ \text{若不真，须给出反例族 ✓}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：β 方案与 gates、$\lambda=A_2/|S|$ 算术修正、$(d',s)\not\leftrightarrow A_2$ 自我修正、$\bot$ 族 $J$ 分层（$m$ 层律）
- **档案已有（引用，不列为提出）**：A-ALIGNTHM-1、P1-2 PASS、Type A/B/C、$J$、$|S|$、Theorem 13


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 算术修正     命中文件数=1    :: ./P3BETA-2026-09-27-scheme-and-first-shot-verdict.md 
技术词 J 分层         命中文件数=0    ::
```
- **本档新增**：β 方案与 gates、$\lambda=A_2/|S|$ 算术修正、$(d',s)\not\leftrightarrow A_2$ 自我修正、$\bot$ 族 $J$ 分层（$m$ 层律）（见上方命中数；0 命中者为自造语／内部标签 ✓）
