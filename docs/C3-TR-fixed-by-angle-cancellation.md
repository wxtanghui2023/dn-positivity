已查地图：命中（`C3-rho-framing-setup-and-status-check`／`C3-TL-verified-and-Zomega-structure`）⟹ 引用，不开新案
D0: 本档对象 = **`T_R` 的精确 `\rho`-表达式定稿**（角度抵消检验）＋ **`T_L,T_R` 的对称形状** ＋ **首条左右混合恒等式** ＋ 下一刀分步
D1: 0 （[REVIEW] 轮次：手工符号推导，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`T_R` 定稿：`T_R=(\rho_1\rho_2)^2(\rho_2\rho_3)^{-1}`**

## §1 ⚠️ 前档写法更正

```
【前档（`C3-rho-framing-setup-and-status-check`）曾写】 `T_R=(\rho_2\rho_3)^2(\rho_1\rho_2)^{-1}` ⟹ **本档更正（角度抵消检验不过）** ✓
```

## §2 ⭐ 角度抵消检验（定 `T_R` 的判据）

```
**【平移词的来历】** `\langle s_1,s_2\rangle`（`s_1^p=s_2^q=(s_1s_2)^2=1`）中的平移词须使**旋转角相消**：$$2\cdot\frac{2\pi}{q}-\frac{2\pi}{p}=0\quad\Longleftrightarrow\quad 2p=q$$ ✓
　`\{3,6\}`：`(p,q)=(3,6)`，`2\cdot3=6` ✓ ⟹ `x=s_2^2s_1^{-1}` ✓（**与文献逐字一致**）✓
【左侧（facet `\langle\rho_0,\rho_1,\rho_2\rangle`，第一对阶 `3`、第二对阶 `6`）】 `\sigma_1=\rho_0\rho_1=a`（阶 `3`）、`\sigma_2=\rho_1\rho_2=b`（阶 `6`）⟹ $$\boxed{T_L=b^2a^{-1}}$$ ✓（`2\pi/3-2\pi/3=0` ✓）
【右侧（vertex-figure `\langle\rho_1,\rho_2,\rho_3\rangle`，**阶序对调**：第一对阶 `6`、第二对阶 `3`）】 取 `\sigma_1=\rho_2\rho_3=c`（阶 `3`）、`\sigma_2=\rho_1\rho_2=b`（阶 `6`）⟹ $$\boxed{T_R=b^2c^{-1}=(\rho_1\rho_2)^2(\rho_2\rho_3)^{-1}}$$ ✓✓（角：`2\pi/3-2\pi/3=0` ✓）
【⛔ 前档之错】 若照抄 `c^2b^{-1}`：角 `4\pi/3-\pi/3=\pi\neq0` ⟹ **不是平移** ✗ ⟹ **该写法作废** ✓✓
```

## §3 ⭐ 对称形状（本档核心观察）

```
$$\boxed{T_L=b^2a^{-1},\qquad T_R=b^2c^{-1}}$$ ✓✓ —— **两者共用同一个 `b^2=(\rho_1\rho_2)^2`**，差别只在"外侧生成元"：`a^{-1}=(\rho_0\rho_1)^{-1}` 与 `c^{-1}=(\rho_2\rho_3)^{-1}` ✓✓
【⟹ 结构含义】 两条额外关系都作用在**同一个核心 `b`**（`b\in\Gamma_{12}` 内）上：$$T_L^2=1\ (2,0),\qquad T_R^3=1\ (3,0)$$ ✓
```

## §4 ⭐ 首条"左右混合"恒等式（可直接用）

```
$$T_L^{-1}T_R=(ab^{-2})(b^2c^{-1})=ac^{-1}=(\rho_0\rho_1)(\rho_2\rho_3)=\rho_0\rho_1\rho_2\rho_3$$ ✓✓
【⟹ 意义】 `T_L^{-1}T_R` **同时含左生成元 `\rho_0` 与右生成元 `\rho_3`** ⟹ **天然是"双侧来源"候选**（正是我们要在 `\Gamma_{012}\cap\Gamma_{123}` 里找的形态）✓
【可用工具（改写它要用）】 远距交换：$$(\rho_0\rho_2)^2=(\rho_0\rho_3)^2=(\rho_1\rho_3)^2=1$$ ✓
【候选清单（下一步逐个试）】 $$\rho_0\rho_1\rho_2\rho_3;\quad (\rho_0\rho_1\rho_2\rho_3)^2;\quad T_LT_R,\ T_LT_R^2,\ T_LT_RT_L,\ T_RT_LT_R^2;\quad [T_L,T_R]$$ ✓
```

## §5 下一刀（分步，全部手工）

```
**【步 1】** 用 `(\rho_0\rho_2)^2=(\rho_0\rho_3)^2=(\rho_1\rho_3)^2=1` 尝试把 `\rho_0\rho_1\rho_2\rho_3` **改写**：一侧写成 `\Gamma_{123}` 内词、另一侧写成 `\Gamma_{012}` 内词 ✓
**【步 2】** 若步 1 成功 ⟹ 再判 $$x\notin\Gamma_{12}$$（若落入 `\Gamma_{12}` ⟹ **只是普通交集元素，不是 defect**）✓
**【步 3】** 若步 1 不成功 ⟹ 依次试 §4 候选清单中的下一个，**只追最短** ✓
**【⛔ 纪律】** **不跑 `GAP`、不做 `Todd\text{–}Coxeter`、不做 word enumeration**（`B` 仍 `LOCKED`）✓；若候选族全数落回 `\Gamma_{12}` ⟹ 只写 **"该手工候选族未产生 intersection-defect 证书"**，$$\textbf{绝不写 CLOSED/不存在}$$ ✓✓
【⛔ 边界】 本档**未得到任何证书**：`T_R` 为**手工定稿（角抵消判据）**、`T_L^{-1}T_R=ac^{-1}` 为**代数恒等式**；两者皆**未**证明 `\notin\Gamma_{12}` ✓
【边界】 §2 角抵消判据与 §1 更正为**本档推导**；`T_L` 部分**已有逐字印证**；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 angle cancellation 命中文件数=0    :: 
```
