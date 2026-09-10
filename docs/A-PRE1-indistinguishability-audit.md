# A-PRE1：Arithmetic indistinguishability audit

**日期**：2026-09-10 14:56+ ｜ 依据：唐先生 A1–A4 + 本轮指定新入口 ｜ 预算：纸面（无代码）

**入口改写（唐先生）**：不做 $\Theta$ 钉扎；先找**原生算术等价关系** $a\sim_{X,H}b$，再从它内生导出 $\Theta$ 与 $\sqrt X$。
$$\boxed{A\neq\text{"设计一个 }\Theta\text{ 把 fixed point 放到 }\sqrt X\text{"}\quad\Longrightarrow\quad\text{先找 arithmetic indistinguishability}}$$
**三关**：① 非乘法分解型（避 divisor/hyperbola）② **加法—乘法兼容**型（唯一有机会同时满足 X5+X6）③ 尺度变化下有 canonical refinement（真信息损失，非投影）

---

## 1. 候选原生等价关系枚举 + 预筛

| # | 等价关系 | 类型 | A-X0 | A-X2 真损失 | A-X3 对合 | 判定 |
|---|---|:-:|:-:|:-:|:-:|---|
| E1 | 指数多重集相同（同 divisibility 形状） | 乘法 | ✓ | ✗ | ✗ | **杀**（无尺度） |
| E2 | $\operatorname{rad}(n)$ 相同（同素支撑） | 乘法 | ✓ | ✗ | ✗ | **杀**（无绝对尺度 = B1 型） |
| E3 | $\Omega(n)$ 相同（同素因子个数） | 乘法复杂度 | ✓ | △ | **✗** | **杀**（= A2：无 $r\leftrightarrow X/r$） |
| E4 | $d(n)$ 相同（同除数个数） | 乘法 | ✓ | ✗ | ✗ | **杀** |
| E5 | $m=n/d$（divisor-complement 轨道） | 乘法 | ✗ | — | ✓ | **杀**（非等价关系 + 因子对 ⟹ N43） |
| E6 | $a\equiv b\ (\mathrm{mod}\ q)$ | 加法/CRT | ✓ | ✓ | **✗** | **杀**（CRT/p-adic NO-GO，见 §2 S8） |
| E7 | $\lvert\log a-\log b\rvert\le\tau$ | archimedean 窗口 | ✓ | ✓ | ✗ | **杀**（S1 截断 ⟹ N43） |
| E8 | $\lvert a-b\rvert\le\tau$ | 加法窗口 | ✓ | ✓ | ✗ | **杀**（加法结构 + 显式公式 ⟹ A-X6 禁列） |
| E9 | 同数量级/同首位数字（Benford 型） | archimedean | ✓ | ✓ | ✗ | **杀**（大小分箱 = S1 型） |
| E10 | $\sigma(a)/a$ 相同（abundancy） | 乘法 | ✓ | ✗ | ✗ | **杀** |
| E11 | $r_k(a)$ 相同（表为 $k$ 次幂和的方式数） | **加×乘** | ✓ | ✗ | ✗ | **杀**（无尺度对合） |
| E12 | $a\equiv b\ (\mathrm{mod}\ L(H))$，$L(H)=\operatorname{lcm}(1..H)$ | 加法/CRT | ✓ | ✓ | **✗** | **杀**（见 §2 S8：$L$ 对 $H$ 单调 ⟹ 无对合） |
| **E13** | **双通道：乘法数据到 $H$ 且加法数据到 $X/H$** | **加×乘** | ✓ | ✓ | **✓** | **唯一形态（见 §3）** |

## 2. ⭐ 新筛查门 S8：**单调性杀**
$$\boxed{\textbf{S8}:\ \text{若不可区分性的"分辨模数"是单一尺度 }H\text{ 的【单调函数】，则它【不可能】携带 }H\leftrightarrow X/H}$$
```
原因：H↔X/H 要求分辨结构对换两支；而单一单调函数只有一个方向
⟹ E6/E12 一类 CRT 型关系【结构性地】拿不到对合（不只是"撞上旧 NO-GO"）
⟹ E12 尤其清楚：L(H)=lcm(1..H) 随 H 单调 ⟹ 无对偶支
```

## 3. ⭐⭐ 唯一存活形态 E13：**双通道架构**
$$\boxed{\mathcal S_{X,H}=\Big(\underbrace{\text{乘法通道：数据到 }H}_{\text{reach}=H},\ \underbrace{\text{加法通道：数据到 }X/H}_{\text{reach}=X/H}\Big)}$$
$$\text{对换 }\mathcal J:(\text{乘法支},\text{加法支})\longmapsto(\text{加法支},\text{乘法支})\iff H\leftrightarrow X/H$$
$$\boxed{\text{这是【唯一】满足 A-X3/A-X4 且【不记录因子对】的形态}\ \Longrightarrow\ \text{恰好满足唐先生的新硬条件}}$$
> 唐先生新硬条件：**$\sqrt X$ 必须是 coarse-graining 的 fixed point，但 state 不能是 factor pair** ✓ E13 形式满足

## 4. ⚠️ 但 E13 的 fixed point 恰好退化
```
在 H=X/H=√X 处，两个通道的 reach 相等 ⟹ 两通道覆盖范围【重合】
⟹ 该重合点正是【经典两范围边界】（= 双曲线记账结构，N43）
（与上一轮最小 Ω 的发现【完全一致】：两范围对换的不动点 = 双曲线边界）
```
$$\boxed{\text{E13 的 fixed point}\ =\ \text{两通道 reach 重合点}\ =\ \text{经典两范围边界}\ =N43\ \text{继承}}$$
**⟹ 架构在【最需要它的那一点】上退化。**

**⚠️ 两层诚实标注**：
```
① 不得声称"到 √X 时乘法通道已完全决定 n"—— 【这是错的】：
   反例：小除数集 {1,p} 同时来自 n=p² 与 n=pq (q>p) ⟹ 小除数集不决定 n
   （我初稿曾想这样表述，已自查否掉）
② 因此本条的正确表述是：√X 是【两通道 reach 重合】的边界，
   而该边界即经典双曲线边界 ⟹ N43 继承（结构性论证，非定理）
```

## 5. ⭐ 机制级诊断（本轮最有价值产出）
$$\boxed{\text{任何 }H\leftrightarrow X/H\text{ 架构的 fixed point，必然是【某两支 reach 的重合点】}}$$
$$\boxed{\text{而 all 已知算术 reach 的重合点都落在【两范围/双曲线边界】⟹ 反复被 N43 吸收}}$$
```
这【解释】了为什么 N43 反复出现（不是巧合）：
   · 最小 Ω（截断×乘法）：两范围对换不动点 = 双曲线边界
   · E13（双通道）：两通道 reach 重合点 = 同一结构
⟹ 要逃出 N43，必须找到【reach 重合点不是两范围边界】的架构
   —— 而这正是目前【无候选】的地方（与 B4 残余同型：inactive）
```

## 6. 当前裁决
$$\boxed{\text{A 已激活，但 A-PRE1 未找到通过 A-X0..X6 的等价关系}}$$
```
· 存活形态 E13 形式满足 A-X3/A-X4（且不含因子对）
· 但其 fixed point 结构性地落在经典两范围边界 ⟹ N43 继承，退化
· 其余 12 类候选各自死于：无尺度（E1–E5,E10,E11）／单调性（S8：E6,E12）／截断 S1（E7,E9）／加法禁列（E8）
```
**必产 R**：
```
R_A-ind【新】：reach 重合点不是两范围边界的等价关系架构 —— 无候选，状态 inactive
S8【新筛查门】：单调分辨模数 ⟹ 无 H↔X/H
```

## 7. 诚实边界
```
· §1 的枚举与小灵；判定依据混用既有登记（S1/S3/CRT-NO-GO/N43）与新门 S8
· §2 S8 为【结构性论证】：单调函数无对偶支——逻辑清楚，但"分辨结构必须由对合承载"未形式化
· §3 的"唯一存活形态"是【在已枚举 13 类内】的结论，非穷尽性定理
· §4 的退化诊断为【结构性识别】，非定理；两层标注已在正文写明（含自查否掉的错误表述）
· §5 的机制级诊断为【结构性归纳】
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 8. 提交链
```
9a0ba98 B4-IA/II → 本篇（A-PRE1）
```
