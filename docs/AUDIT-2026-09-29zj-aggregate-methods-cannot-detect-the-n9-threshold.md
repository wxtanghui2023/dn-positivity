# AUDIT-2026-09-29zj — 标定：**聚合/谱方法连 n=9 的阈值都检测不到** ⟹ 该类整体过弱

> 空间 B｜非 C 号｜唐先生令（22:45「继续」）｜**不主张 107／不主张 106 可排除**（V290）
> 时间：2026-09-29 22:5x–23:0x

**已查地图**：承 `AUDIT-zi`（层覆盖族不足）／`AUDIT-zh`（α/β）／`AUDIT-zg`（聚合可行）／`ERRATUM-n1`
D0: 本档对象 = **档案已有**（Delsarte/Krawtchouk／层覆盖／$A_k$）之**能力标定**（新数学对象：无 ✗）
D1: 0（产出 = **一条能力上限读数** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{聚合/谱类方法（}\mu\text{-恒等式 ＋ 层覆盖族 ＋ Krawtchouk 正性 ＋ }\Sigma A_k{=}\binom M2\text{）}\ \textbf{在 }n{=}9\ \textbf{连 }M{=}61\ \textbf{都判为可行}}$$
$$\text{而}\ K(9,1){=}62\ \text{为真（已独立核验 62-码）}\ \Longrightarrow\ \textbf{该类方法连已知真值都检测不到}\ ✗✗$$
$$\boxed{\text{其对 }n{=}10\ \text{之最强下界} = M_{\rm agg}(10) = \mathbf{95}\quad(\text{目标 }107;\ \text{差 }\mathbf{12})}$$

## §1 标定数据（实跑，逐条）

| $n$ | $M$ | 聚合系统判定 | 真值 |
|---|---|---|---|
| 9 | 61 | **可行** ✗ | 不可能（$K{=}62$） |
| 9 | 62 | 可行 ✓ | 可能（62-码在手） |
| 9 | 63 / 64 | 可行 ✓ | 可能 |
| 10 | 95 | 可行（= 最小可行） | 真下界 $\ge107$ |

$$\Longrightarrow\ \text{二分得}\ M_{\rm agg}(10){=}\mathbf{95}\ \text{（即该类方法最多给 }K\ge95\text{）}$$

## §2 战略含义（**本档最重要**）

$$\text{我方已复现之阶梯}:\ \underbrace{94}_{\text{球界（线性）}}\ <\ \underbrace{103}_{\text{van Wee excess}}\ <\ \underbrace{105.2223}_{\text{SDP-3}\ \textbf{非线性（PSD）}}\Rightarrow106\ <\ \mathbf{107}$$
$$\therefore\ \textbf{(i)}\ \text{线性/组合（Delsarte 谱类）}\ \le\ 95\ \text{（本档标定）}\ \text{或}\ 103\ \text{（excess 技巧）}\ ——\ \textbf{远不足}$$
$$\qquad\ \textbf{(ii)}\ \text{真正承重者是 }\textbf{SDP（PSD 非线性）}\Rightarrow106;\ \text{而}\ 107\ \textbf{超出全部松弛类天花板}$$
$$\qquad\ \textbf{(iii)}\ \therefore\ 107\ \text{只能出自\ \textbf{非线性 ＋ 整性}（或非 Aut-不变之结构论证）}\ ✓$$

## §3 与既有档案判定的一致性

- `MASTER-FAILURE-MAP` §2 定理 A：Aut-不变线性/谱泛函 $\le105.2223$ ⟹ 与 §1 标定**同向**（本档把界进一步压到 95，因约束更弱）
- `AUDIT-29e`：单条线性不等式 $\le$ LP $\le$ SDP $=105.2223$ ✓ 一致
- `AUDIT-29c/d`：pair 层／高阶 SDP 皆死 ✓ 一致
- ⟹ **本档给出的是一条"类级"证据**：不是"我们没找到"，而是"这一类**结构上**不够"

## §4 下一步（**待唐先生定**）

- **(I) 整性/同余**：Habsieger 型同余于 $n\equiv4\bmod6$（$n{=}10$ 在其内）—— 档案记其给 104（低于 106）⟹ 须与 **SDP 105.2223 合用**才是新组合 ⚠️
- **(II) 非 Aut-不变结构论证**：选破对称的局部结构（如深洞邻域）做统一论证
- **(III) 承认当前手段边界**，把 106→107 记为**需新数学**（并保留 106 为我方已达成之下界）✓

## §5 边界（硬 ✓）

- **不主张** 107／105／任何新值 ✗；本档为**能力标定**（否定性），非新上/下界 ✓
- 标定所用系统为**我们的**约束集（非文献最强 LP），故"95"是**我方该类方法的**上界，**不是**文献界的上界 ⚠️✓
- 未取论文原文（R16–17）／未重攻 pair 层（R02）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
