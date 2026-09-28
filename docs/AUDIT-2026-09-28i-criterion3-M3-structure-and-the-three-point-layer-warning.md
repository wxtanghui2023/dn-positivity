# AUDIT-2026-09-28i — **Criterion 3：$M_3$ 结构定理（$\Phi_2$ 细于距离分布）＋ ⚠️ 三点数据层预警**

> **性质**：**审计/实验**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:46 ✓
> **唐先生令**：Criterion 3 收紧版＝找 $N_d(C){=}N_d(C')$ 而 $\Phi_2(C){\ne}\Phi_2(C')$；**先 $M_3$ 理论判别**，不随机采样 ✓

**已查地图**：接续 `AUDIT-h`（$\Phi_2$ 定义）／`AUDIT-f/g`／`SUBSPACELP` ✓

D0: 本档对象 ＝ **档案已有**（$D_2(c)$／方向度／三点配置——**无新数学对象** ✓）
D1: 1（**首次给出 $M_3$ 之精确结构定理 $\sum_x a_x^3{=}\sum_{c}\sum_i m_i^2$（实测三例全等 ✓✓）＋ 首次定位 $\Phi_2$ 高阶矩\ \textbf{落在三点数据层} ⚠️**）

---

## §0 结论（先给）

$$\boxed{\textbf{(1) $M_3$ 结构定理（实测 ✓✓）}:\quad \sum_x a_x^3\ =\ \sum_{c\in C}\sum_{i=1}^{10} m_i(c)^2},\qquad m_i(c):=\#\{j:c{\oplus}e_i{\oplus}e_j\in C\}$$
$$\boxed{\textbf{(2) Criterion 3：\textbf{应通过}} \Longrightarrow \Phi_2\ \text{细于距离分布（}\because\ \sum_i m_i{=}10+2|D_2(c)|\ \text{仅给一阶，}M_3\ \text{需\ \textbf{方向度谱} }\{m_i\})}$$
$$\boxed{\textbf{(3) ⚠️ 但\ \textbf{早期否决预警}}:\ \Phi_2\ \text{之高阶矩\ \textbf{落在三点数据层}} = \text{正是 Gijswijt 2005 SDP 之\ \textbf{输入层}（已给 }105.2223{<}119\text{）}}$$

## §1 $M_3$ 结构定理（**本档主结果 ✓✓**）

$$\text{双重计数 }(x,i,j,k)\ \text{三条件 }x{\oplus}e_i,x{\oplus}e_j,x{\oplus}e_k\in C:\ \text{令 }c{=}x{\oplus}e_i\ \Longrightarrow\ \text{双射}$$
$$\Longrightarrow\ \sum_x a_x^3=\sum_{c,i,j,k}[c{\oplus}e_i{\oplus}e_j\in C][c{\oplus}e_i{\oplus}e_k\in C]=\boxed{\sum_c\sum_i m_i(c)^2}\ ✓$$
$$\textbf{实测（三例，全部相等 ✓✓）}:\ 5958{=}5958\ (K{=}150);\ 5188{=}5188\ (K{=}145);\ 5646{=}5646\ (K{=}147)$$

$$\textbf{一阶对照}:\ \sum_i m_i(c)=10+2\,|D_2(c)|\quad\big(D_2(c){:=}\{\{i,j\}:c{\oplus}e_i{\oplus}e_j\in C\}\big),\qquad \sum_c|D_2(c)|=2N_2\ ✓$$
$$\therefore\ \sum_i m_i\ \text{仅由 }N_2\ \text{定};\ \text{但 }M_3=\sum_c\sum_i m_i^2\ \text{需\ \textbf{方向度谱} }\{m_i(c)\}_i\text{，非仅其和}\ ✓$$

## §2 Criterion 3 判定

$$\textbf{理论}:\ M_3=\sum_c\big(\sum_i m_i^2\big);\ \text{若 }\{m_i\}\ \text{非均匀则 }M_3>\frac1{10}\sum_c(\sum_i m_i)^2;\ \text{方向度谱不由 }\{N_d\}\ \text{决定（一般）} ✓$$
$$\boxed{\therefore\ \text{Criterion 3}\ \textbf{应通过}:\ \exists C,C'\ \text{同距离分布而 }M_3\ne M_3'}\ \text{（待构造验证 ⚠️）}$$

## §3 ⚠️ 早期否决预警（**本档真正的价值 ✓✓**）

$$\boxed{\Phi_2\ \text{（及其高阶矩）}\ \subseteq\ \text{三点（triple）数据层}}$$
$$\text{而 Gijswijt 2005／Gijswijt–Polak 2025 之 SDP 变量＝\textbf{3-point configurations}}\ \big(\text{C-474 已录：论文自述}\big)$$
$$\Longrightarrow\ \boxed{\text{该数据层\ \textbf{已被 SDP 优化过}，所得 }105.2223<119}\ \text{（C-474 ✓）}$$
$$\therefore\ \text{按 C-546 之\textbf{机制族穷尽}，}\Phi_2\ \text{极可能\ \textbf{继承同一天花板}} ⚠️$$

**诚实边界 ✓**：SDP 是**松弛**，不榨尽三点数据的组合力量 ⟹ **不构成逻辑否决** ✗；但按本项目"早期杀"纪律，此为**强预警**，须**先量化**再投入 ⚠️

## §4 判定与建议

$$\boxed{\text{Criterion 3}:\ \text{理论应过（未构造验证）};\quad \text{但 Criterion 4/5 面临\ \textbf{三点层天花板} ⚠️}}$$
$$\textbf{建议}:\ \text{先做\ \textbf{一次廉价量化}——}\Phi_2\ \text{之信息是否已被 SDP 之三点约束覆盖？}$$
$$\qquad\text{若"是" ⟹ 按 C-546 ⟹ \textbf{早期 KILL}}\ ✗;\quad \text{若"否" ⟹ 再构造同距离分布异 }\Phi_2\ \text{之对，进 Criterion 4}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "方向度谱" "三点数据层" "M3结构定理"
技术词 方向度谱     命中文件数=0    ::
技术词 三点数据层   命中文件数=0    ::
技术词 M3结构定理   命中文件数=0    ::
```

## §6 边界（硬 ✓）

- 有限计算（三例恒等式核验）＋ 双重计数推导 ＋ 既有档引证 ✓；**不占 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §3 之预警为**类比推理（未证）**⚠️，已显式标注；**不主张** $\Phi_2$ 已死 ✗
