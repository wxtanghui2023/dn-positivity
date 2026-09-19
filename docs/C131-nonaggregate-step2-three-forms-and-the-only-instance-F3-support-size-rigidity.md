已查地图（**先查后写**）：`V188 §2`（逐字："RH ⟺ supp μ ⊂ ℝ；而'支撑在某条实轴上'**不是线性条件**"；"线性泛函只'看见'**位置的加权和**，看不见'某点是否离开了轴'"）、`V193 §⑤`（残余：β-敏感，但既不是重数/指数、也非二次型、也非逐点算术对象）、`C-110`（六条必要条件，C6 = 定量稳定性，**从未被直接攻过**）、`C-130`（三分类 S1/S2/S3；**第四类实例＝0**）、`C-125`（sumset 饱和／尺度感知）、`C-126`（SUSPENDED ＋ 唯一破口）、`W6`（support>1 原子墙；BGSTB24 无条件窗 `0≤x≤T`）、`P3-B2`（P2 硬要求 ＋ 本线加强：本征值须为**非聚合读数**）。关键词回查：`支撑集`=0、`支撑大小`=0（**新**）；`刚性`=337、`非聚合`=21（**沿用**，generic）。
**本档任务（唐先生 2026-09-19 11:21「先看甲」）**：**尝试构造一个"非聚合形状"的 step 2。**
**结论（先行）**：$$\textbf{(一)}\ \text{非聚合形状只有}\ \textbf{三型可用}：\text{F1 支撑包含}／\text{F2 逐点误差}／\text{F3 }\boxed{\textbf{支撑大小刚性}}✓✓$$
$$\textbf{(二)}\ \text{F1／F2}\ \textbf{都是已知 RH 等价}（\text{S1}）;\ \textbf{F3 是我们唯一的具体非聚合实例}✓✓$$
$$\textbf{(三)}\ ⚠️\ \textbf{更正}\ \text{`C-130`}\ \text{§4(乙)}："\text{第四类实例}＝0"\ \Longrightarrow\ \textbf{实例数＝1}（\text{F3}）,\ \text{但【未证明 ＋ 未接通}✓✓$$
$$\textbf{(四)}\ \text{F3 的 ζ-接口}\ \textbf{仍受 W6}（\text{幅频钉定只在 support}\le1\ \text{窗口无条件已知}）✓$$

FREEZE-ACK: 本档即冻结期内的形状构造与自我更正（依 `§8.1`；不产候选结论）

D0: 本档对象 = **非聚合 step 2 的三型清单 ＋ 唯一具体实例 F3（支撑大小刚性）＋ 对 C-130「实例数＝0」的更正** —— 关系 = 构造与更正，非新机制
D1: 0

# C-131 · **非聚合形状的 step 2：三型清单 ＋ 唯一实例 F3（支撑大小刚性）**

> **唐先生 2026-09-19 11:21**：**「先看甲」**（尝试构造非聚合 step 2）✓

---

## §1 非聚合形状的形态清单（逐项判定）

$$\begin{array}{c|c|c|c}
\text{形态} & \text{step 2 写出来} & \text{非聚合？} & \text{判定}\\
\hline
\text{F1 支撑包含} & \operatorname{supp}\mu\subset\mathbb R & ✓\ (\text{`V188` §2 逐字：支撑性质}) & \textbf{S1}\ (=\text{RH 本身})\\
\text{F2 逐点误差} & \psi(x)-x=O(x^{1/2+\varepsilon});\ S(T)=O(\log T/\log\log T) & ✓ & \textbf{S1}\ (\text{von Koch}\iff\text{RH})\\
\text{F3 支撑大小刚性} & \text{正测度＋幅频钉定}\ \Longrightarrow\ \#\operatorname{supp}\mu\le B & ✓✓ & \boxed{\textbf{新形状候选（唯一）}}\\
\text{F4 极值/端点} & \Lambda\le0 & ✗\ (\text{参数端点}) & \textbf{S1}\\
\text{F5 比例/计数} & N_0^s/N_d\to1 & ✗ & \textbf{S2}\\
\end{array}$$
$$\Longrightarrow\ \boxed{\text{非聚合＝}\{\text{F1},\text{F2},\text{F3}\};\ \text{其中 F1／F2}\ \textbf{已知等价（S1）},\ \textbf{只有 F3 不是已知等价}}✓✓$$

## §2 ⭐ F3 的详细写出（step 1 ／ step 2）

$$\text{对象}：\text{正原子测度}\ \mu=\sum_i m_i\,\delta_{x_i}\ (\text{支撑集}\ X:=\operatorname{supp}\mu\subset\text{单位圆});\ \text{幅频}\ |\hat\mu(j)|^2\ \text{在窗口}\ j\le W\ \text{内被}\ \textbf{钉定}✓$$
$$\textbf{step 1（存在性）}：\text{给定幅频数据，是否存在满足它的正测度？}\ \Longrightarrow\ \text{这是经典}\ \textbf{相位检索}：\text{幅频}\Longrightarrow\text{相位不唯一}✓$$
$$\qquad \Longrightarrow\ \text{解集非空（除非约束过强）}\ \Longrightarrow\ \textbf{step 1 平凡}✓✓$$
$$\textbf{step 2（写出来）}：\ \forall\ \text{满足钉定幅频的正测度}：\ \#\operatorname{supp}\mu\ \le\ B(W,\tau)✓✓$$
$$\qquad ⚠️\ \text{这不是支撑包含（F1），不是逐点误差（F2），不是比例（F5）—— 它是}\ \textbf{支撑大小} \text{型}✓✓$$

**为何确为非聚合（用 `V188` §2 的逐字逻辑）**：
$$\text{"线性泛函只'看见'}\textbf{位置的加权和}\text{"}\ \Longrightarrow\ \text{幅频数据只看见}\ \textbf{支撑加权差集之和}✓✓$$
$$\qquad \Longrightarrow\ \text{它}\ \textbf{看不见支撑的大小}（\text{同一幅频可由"少而重"或"多而轻"的支撑实现}）✓✓$$
$$\qquad \Longrightarrow\ \textbf{支撑大小＝真正的非聚合读数}✓✓$$

**与已知残余的关系**：这**正是** `V193` §⑤ 的残余形状（"β-敏感，但既非重数/指数、也非二次型、也非逐点算术对象"）—— 本档把它**具体化**为"**支撑大小刚性**" ✓✓

## §3 与 ζ 的接口（诚实）

$$\text{要接到}\ \zeta\ \text{需要两件}：\text{①一个}\ \textbf{算术正测度};\ \text{②其幅频在某个窗口内被}\ \textbf{无条件钉定}✓$$
$$\text{现成可用}：\nu_x:=\sum_{n\le x}a_n\,\delta_{\log n}\ (\text{素数侧}),\ \widehat{\nu_x}\ \text{＝素数侧指数和}✓$$
$$\text{无条件钉定窗口}＝\textbf{support}\le1\ (\text{Montgomery}／\text{BSGTB24}：0\le x\le T)\ \Longrightarrow\ \text{卡点}＝\boxed{\textbf{W6 原子墙}}✓✓$$
$$\Longrightarrow\ \text{形状对了，接口仍在 W6 —— 但这是}\ \textbf{第一次} \text{把"非聚合 step 2"}\ \textbf{具体写出来}✓✓$$

## §4 诚实边界与自我更正

- ⚠️ **更正** `C-130` §4(乙)：此前写"第四类（新形状）实例＝0" ⟹ **实例数＝1**（F3）；但 F3 的 step 2 **未证**，且它**等价于 B2-1 的 pairwise geometry 定理**（未找到）✓
- ⚠️ F3 与 ζ 的接口**受 W6**；**不声称**能跨 ✓
- ⚠️ **不声称** F3 可证；**不声称** 三型清单穷尽（可能漏）✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 11:2x）`[纪律]`（先跑后写）

```
技术词 支撑集       命中文件数=0 ::   ⟹ 本档新增
技术词 支撑大小     命中文件数=0 ::   ⟹ 本档新增
技术词 刚性        命中文件数=337 ::  ⟹ 沿用（generic，不作新性主张）
技术词 非聚合       命中文件数=21 ::  ⟹ 沿用（generic，不作新性主张）
```
**读数（按实测）**：`支撑集`／`支撑大小` 为**本档新增**；`刚性`／`非聚合` 为**沿用** ✓
