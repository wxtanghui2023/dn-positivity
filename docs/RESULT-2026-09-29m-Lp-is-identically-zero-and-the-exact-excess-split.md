# RESULT-m（2026-09-29）—— $L(p)\equiv\mathbf 0$（packing 零 excess，硬检查否掉该提案）✗；得**精确过剩分解** ✓✓

> **性质**：**实测 ＋ 结构判定**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:55 ✓

**已查地图**：`RESULT-l`（$|D_A|>106-a$ 重述）／`RESULT-j`／`RESULT-c` ✓

D0: 本档对象 ＝ **档案已有**（packing／excess 分解—经典 ✓）
D1: 0（产出＝**一否证 ＋ 一精确分解 ＋ 一量级数据** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ }L(p)\equiv0:\ P\ \text{packing}\Rightarrow B_1(p)\ \text{互不相交}\Rightarrow p_x\in\{0,1\}\Rightarrow\Sigma(p_x-1)_+=0}$$
$$\boxed{\text{② ✗ }p>A(9,3)=40\ \text{时 packing 不存在}⟹\ L(p)\ \text{无定义（非零）}}$$
$$\boxed{\text{③ ✓✓ 精确分解}:\ \mathrm{Def}(A)=\sum_{x\in N_1(P)}q_x+\sum_{x\notin N_1(P)}(q_x-1)_+\ (\text{实测 }20/20)}$$
$$\text{② }p>A(9,3)=40\ \text{时 packing 不存在}\ \Longrightarrow\ L(p)\ \text{无定义}\ ✗$$

## §1 $L(p)\equiv0$（✗ 硬检查否掉提案）

$$L(p)=\min_{P\ \text{3-packing},\ |P|=p}\sum_x\bigl(|P\cap B_1(x)|-1\bigr)_+$$
$$\text{packing}\Rightarrow\text{球互不相交}\Rightarrow p_x=|P\cap B_1(x)|\le1\Rightarrow L(p)=\mathbf 0\ \forall p\le40✓$$
$$\therefore\ \text{基础下界}\ F\ge\sum(p_x-1)_+=\mathbf 0\ \text{—— 零信息}✗$$

## §2 精确过剩分解（✓✓ 本档真正产物）

$$\mu(x)=p_x+q_x,\quad p_x=|P\cap B_1(x)|\in\{0,1\},\quad q_x=|Q\cap B_1(x)|$$
$$\therefore\ (\mu-1)_+=\begin{cases}q_x,&x\in N_1(P)\\ (q_x-1)_+,&x\notin N_1(P)\end{cases}$$
$$\boxed{\mathrm{Def}(A)=\sum_{x\in N_1(P)}q_x+\sum_{x\notin N_1(P)}(q_x-1)_+}\qquad\textbf{实测 }20/20✓✓$$

## §3 量级（✓ 关键读数）

| $a{=}53$ | $|P|{=}27$ | $|Q|{=}26$ |
|---|---|---|
| part1（$Q$ 撞 $P$ 之地盘） | $\mathbf{68}$ |
| part2（$Q$ 于 $P$ 外之自身重叠） | $11$ |
| $\mathrm{Def}(A)$ | $79$ |
| 需 $>9a-406$ | $71$ |

$$\therefore\ \boxed{\text{过剩 }\mathbf{86\%}\ \text{来自 }Q\ \text{撞 }P\ \text{之地盘}⟹\ \textbf{敌人是 }Q,\ \text{不是 }P}✓$$

## §4 边界（硬 ✓）

- **三项实测（$\Sigma(p_x-1)_+\equiv0$、分解、量级）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；$L(p)$ 提案**明确否证** ✗

## §5 【技术词回查】（**提交前实跑，逐字粘贴**）

```
packing零excess : 技术词 packing零excess 命中文件数=0    ::
过剩分解 : 技术词 过剩分解     命中文件数=0    ::
L(p)恒零 : 技术词 L(p)恒零   命中文件数=0    ::
```
