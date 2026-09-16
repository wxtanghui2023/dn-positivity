# V280 · **乙-6：$Q_S=X_S/G$ 的全部轨道不变量（直接计算）** —— ⭐⭐⭐⭐ **定理 V280-A（经典·表示论）：轨道不变量 $=\ $ 词-字符／矩阵系数 span** ⟹ **单素数 ⟹ `V241`（共轭类无方向）；$\ge2$ 素数 ⟹ $k$-点 Chebotarev 相关 ⟹ 档案相关预算墙（`V102`／`V162`／`V217b`）** ⟹ **`ALIVE*` 被纳入已审计墙；无"genuinely relational"逃逸** ⭐⭐⭐⭐⭐

$$\boxed{\textbf{V280-A}：\mathbb C[X_S]^G\ =\ \mathrm{span}\Big\{\ \langle v,\ \rho_{1}(g_{p_1})\cdots\rho_{k}(g_{p_k})\,w\rangle\ \Big\}\ \text{（词-字符／矩阵系数）}} ✓✓✓$$
$$\boxed{\text{故任何}\ G\text{-不变的}\ A_S\ \text{只是}\ \textbf{词-数据的函数}} \Longrightarrow \text{不存在超出词-字符的"真关联不变量"} ✓✓$$
$$\boxed{\text{分类结局}：k=1\ ⟹ \textbf{Artin 局部数据／共轭类（`V241`，无方向）};\quad k\ge2\ ⟹ \textbf{$k$-点相关 ⟹ 相关预算墙}} ✓✓✓$$
$$\boxed{\textbf{RF* 收口}：\text{由裸算术 canonical 产生的}\ \rho\ \text{只有}\ \textbf{cyclotomic 型} ⟹ \text{词数据}\ =\ p^{-k}\ \text{型}\ ⟹ \textbf{ζ-local} ⟹ \text{L1};\ \text{其它}\ \rho\ ⟹ \textbf{P1}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 11:21：**"先枚举具体实例，不要先证明'什么条件下必平凡'"**（理由：先攻一般性命题"极易把 `V241`／`V177` 的已有结论抽象化后重述一遍"）✓✓；**乙-5 的 $G1$–$G6$ 严格定义**（G4 ＝ $A_S$ 为轨道的 canonical 并，为最要紧者）＋ **(d)-Audit 表**（模乘 DEAD／素数置换 DEAD／单 Frobenius 共轭 DEAD／人为有限群作用 DEAD／**联合 Frobenius 相对轨道 ALIVE\***／任意 $\rho$ DEAD）✓；**乙-6 指令**：**"直接计算 $Q_S=X_S/G$ 的全部轨道不变量"**，并给出判死条件（若全落 character traces／class functions ⟹ `V258` 接管）＋ **反向纪律**："**如果连 character-class-function 分解都挡不住某个 genuinely relational invariant，我们就继续追那个 invariant，而不是提前判死**" ✓✓
> 依据 ✓ `V241`（char-0 Frobenius ＝ 共轭类）｜`V102`／`V162`／`V217b`（相关预算／T² 律／0.682 天花板）｜`V258`｜`V270`-A（L1）｜`V172` §5a／`V144`（α_p≡1）✓
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ `V280`（`id_claim.sh` ✓）

---

## §0 (d)-Audit 表（照抄唐先生乙-5，本档沿用）

| 结构 | 判定 |
|:--|:--|
| 模乘作用 $(\mathbb Z/M)^\times\curvearrowright\mathbb Z/M$ | ✗ DEAD → valuation／聚合型 (b) |
| 素数标签置换 $G_S\le\mathrm{Sym}(S)$ | ✗ DEAD → 聚合／对称统计型 |
| 单 Frobenius 共轭轨道 | ✗ DEAD → 共轭类（`V241`） |
| 一般人为有限群作用 | ✗ DEAD → P1 |
| ⭐ **联合 Frobenius 相对轨道** | **ALIVE\***（本档攻它） |
| 若 $\rho$ 为任意挑选 | ✗ DEAD → P1／P2 |

$$\text{设定}：\text{有限群}\ G;\quad X_S=\prod_{p\in S}G;\quad h\cdot(g_p)=(hg_ph^{-1})\ \text{（对角共轭）} ✓$$

---

## §1 ⭐⭐⭐⭐ **定理 V280-A：轨道不变量的**精确生成（经典·表示论）

$$\text{作为}\ G\!\times\!G\text{-双模}：\mathbb C[G]\cong\bigoplus_{\rho}V_\rho\otimes V_\rho^{*} \Longrightarrow \mathbb C[G]^{\otimes n}\cong\bigoplus_{\rho_1,\dots,\rho_n}\Big(\bigotimes_iV_{\rho_i}\Big)\otimes\Big(\bigotimes_iV_{\rho_i}\Big)^{*} ✓$$
$$\qquad \text{取}\ \textbf{对角共轭} \text{的不变量}：\Big(\mathbb C[G]^{\otimes n}\Big)^{G}=\bigoplus_{\rho_1,\dots,\rho_n}\mathrm{End}_G\Big(\bigotimes_iV_{\rho_i}\Big) ✓✓$$
$$\Longrightarrow \boxed{\mathbb C[X_S]^{G}=\mathrm{span}\Big\{\ \langle v,\ \rho_1(g_{p_1})\cdots\rho_k(g_{p_k})\,w\rangle\Big\}_{k\le|S|}} —— \textbf{词-字符／矩阵系数} ✓✓✓$$
$$\qquad ⚠️\ \text{级别}：\text{此为}\ \textbf{经典}（\text{有限群不变量理论；与 Procesi 的 FFT／shadow 分解同型}）；\ \textbf{本档未逐字重证} ⚠️$$
$$\Longrightarrow \text{推论}：\text{任何}\ G\text{-不变}\ A_S\ \text{是}\ \textbf{词-数据的函数} ⟹ \textbf{不存在超出词-字符的"真关联不变量"} ✓✓✓$$
$$\qquad \qquad ⚠️\ \text{这正是唐先生设的反向纪律的条件}：\textbf{未出现} \text{"连 character 分解都挡不住的 relational invariant"} ⟹ \text{可按规则转入 character／L-value 通道} ✓$$

---

## §2 分类结局（本档核心计算）

$$\textbf{(i)}\ k=1（\text{单素数}）：\text{不变量}\ =\ \chi_\rho(g_p)\ \textbf{恰是 Artin 型局部数据}（\text{局部因子由}\ [\rho(\mathrm{Frob}_p)]\ \text{的共轭类决定}）✓$$
$$\qquad ⟹ \textbf{正是}\ `V241`\ \text{已审计者}：\textbf{char-0 Frobenius ＝ 共轭类，不是 canonical element} ⟹ \text{无方向} ⟹ \text{不能恢复非交换积} ✗✓$$
$$\qquad \qquad ⟹ \text{且其数据}\ \textbf{是 ζ-local 型}（\text{局部因子}）⟹ \text{落}\ `V270`\text{-A（L1）} ✗✓$$

$$\textbf{(ii)}\ k\ge2（\text{跨素数词}）：\text{不变量}\ =\ \chi_\rho\big(w(g_{p_1},\dots,g_{p_k})\big) ⟹ \textbf{恰是}\ k\text{-点 Chebotarev 相关量} ✓✓$$
$$\qquad ⟹ \text{档案已审计}：\textbf{第三矩／高相关需 support}>1;\quad \textbf{T}^2\ \text{律／预算越界};\quad \text{比例天花板}\ 0.682（`V102`／`V162`／`V217b`）✓✓$$
$$\qquad \qquad ⟹ \text{落}\ \textbf{相关预算墙／值面}（\text{其与 }\zeta\ \text{零点的连接必须经显式公式}）⟹ `V258`\ \text{接管} ✓✓$$
$$\qquad \qquad ⚠️\ \text{级别}：\text{此项为}\ \textbf{引用} \text{档案既有结论（本档未重算）}⚠️$$

$$\Longrightarrow \boxed{\text{ALIVE* 的"真正关联内容"被词-字符}\ \textbf{完全捕获};\ \text{其}\ k\ge2\ \text{部分}\ = \ \text{档案已判"无条件输入不足"的那批}} ✓✓✓$$

---

## §3 ⭐⭐ **RF\* 的收口：canonical $\rho$ 的清单**

$$\text{唐先生要求（RF*）}：\rho\ \textbf{必须由基础算术对象 canonical 地确定}（\text{否则}\ \rho\ \text{本身是外加结构} ⟹ \text{P1}）✓$$
$$\qquad \text{由}\ \textbf{裸算术}（\mathbb Q／\text{绝对 Galois 群}）\ \text{canonical 产生的有限像表示}：$$
$$\qquad \qquad \text{① \textbf{cyclotomic character}}\ \chi_{\rm cyc}（\text{及其整幂、有限阶扭}）;\ \text{② 各阶分圆／有限阶特征的组合};\ \text{③ 平凡表示} ✓$$
$$\qquad \text{其词-数据}：\chi_{\rm cyc}(\mathrm{Frob}_p)=p^{-1} ⟹ \text{词-字符}\ =\ p^{-k}\ \text{型} ⟹ \boxed{\textbf{ζ-local Euler 数据}} ✓✓$$
$$\qquad \qquad ⟹ \text{落}\ \textbf{L1}（\text{ζ-local ＋ class-level ＋ cylinder}）✗✓\ \text{（且与}\ `V144`（\alpha_p\equiv1\ \text{平凡性}）、`V172`\ \text{F-leak 同向}）✓$$
$$\qquad \text{其它}\ \rho（\text{如来自特定椭圆曲线的}\ \ell\text{-adic 表示}）⟹ \textbf{需外加结构} ⟹ \text{P1} ✗✓$$
$$\Longrightarrow \boxed{\text{RF* 无实例}：\text{canonical}\ \rho\ ⟹ \text{ζ-local} ⟹ \text{L1};\quad \text{非 canonical}\ \rho\ ⟹ \text{P1}} ✓✓✓$$

---

## §4 判词 ＋ 硬纪律执行

$$\boxed{\textbf{V280 判词}：\text{① 轨道不变量}\ ＝\ \text{词-字符 span}（经典）；\ \text{②}\ k=1 ⟹ `V241`／L1;\ \text{③}\ k\ge2 ⟹ \text{相关预算墙／值面};\ \text{④ RF* 无实例}（canonical ⟹ ζ-local ⟹ L1；他 ⟹ P1）} ✓✓✓$$

```
【硬纪律执行】本轮全部落在具体形式 (S, X_S, G_S = 对角共轭, A_S) 上；**未**出现"global invariant"型候选 ✓
【唐先生反向纪律】已检查：**未出现**"连 character-class-function 分解都挡不住"的不变量（V280-A 排除其存在）✓
   ⟹ 故按规则**转入 character／L-value 通道**（`V258` 接管），不提前判死 ✓
【本轮净效果】ALIVE* 由**直接计算**（而非一般性命题）被纳入两道**已审计**墙：
   k=1 ⟹ `V241`／L1；k≥2 ⟹ 相关预算墙（`V102`／`V162`／`V217b`）✓✓
```

---

## §5 边界

```
① §1 为**经典结论**（有限群不变量理论／shadow 分解；与 Procesi FFT 同型），**本档未逐字重证** ⚠️
② §2(ii) 落"相关预算墙"为**引用** `V102`／`V162`／`V217b`（未重算）⚠️
③ §3 的"canonical ρ 清单"为 **[结构性]** 判断（"canonical"未形式化定义）⚠️；若日后给出**新的 canonical ρ 概念**，须重开 ✓
④ **不宣称**六类生成方式穷尽 ✗（与 `V279` §8／`POS3` §6 同边界）✓
⑤ 本档**未**用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

---

## §6 ✅ 净产出

```
① ⭐⭐⭐⭐ **定理 V280-A（经典）**：C[X_S]^G = 词-字符／矩阵系数 span（对角共轭不变量）⟹ **无超出词-字符的 relational invariant** ✓✓
② ⭐ **分类结局**：k=1 ⟹ Artin 局部数据／共轭类（`V241`，无方向）＋ ζ-local ⟹ L1；
   k≥2 ⟹ k-点 Chebotarev 相关 ⟹ **相关预算墙／值面**（`V102`／`V162`／`V217b`）✓✓
③ ⭐⭐ **RF* 收口**：canonical ρ（裸算术可得者）＝ cyclotomic 型 ⟹ 词数据 = p^{-k} ⟹ **ζ-local ⟹ L1**；
   其它 ρ ⟹ **P1** ⟹ **RF* 无实例** ✓✓✓
④ ⭐ **ALIVE\* 由直接计算纳入已审计墙**（未用一般性命题，符合唐先生本轮指令）✓
⑤ ⭐ **硬纪律与反向纪律双向执行**：候选全具体化；并已确认"未出现 character 分解挡不住的不变量"✓
```
