# R_8^{(v)} 纸面协议：变换链审计（宪法 §0 格式）

**日期**：2026-09-10 13:44+ ｜ 起草：小灵 ｜ 提案：唐先生
**性质**：**精确变换链**审计——不打"可能的无条件方法"清单，而是写出链并找**不可逆缺口**
**预算**：1 轮纸面，不写代码

---

## 0. 目标链
$$\boxed{V(X,H)\ \overset{?}{\longleftrightarrow}\ \sum_h w_H(h)\sum_n\Lambda(n)\Lambda(n+h)\ \overset{?}{\longleftrightarrow}\ F(\alpha),\ \ \alpha\leftrightarrow H}$$
等价 Fourier 形式（唐先生）：
$$C(X,H)\ \leftrightarrow\ \int|\widehat w_H(\alpha)|^2\,|S_X(\alpha)|^2\,d\alpha,\qquad |\alpha|\sim H^{-1}$$

## 1. 逐箭审计（A1–A4）
| 箭 | 内容 | 必须回答 |
|---|---|---|
| **A1** | $(q,a)$-平均 → $h$-shift 平均 | 是否存在**无条件**转换？（Hooley 的 h 是区间长度，非平均坐标） |
| **A2** | short-interval variance → $\sum_h w_H(h)\sum_n\Lambda(n)\Lambda(n+h)$ | **恒等式**／单向估计／需额外 prime-pair 信息？ |
| **A3** | 得到 $C(X,H)$ 后，主项 $HX\log(X/H)$ 是否足以恢复完整 $1-\eta$ 连续自由度？ | 端点项控制问题 |
| **A4** | $C(X,H)\to F(\alpha)$ 是 exact／asymptotic／单向／仅在 RH+PC 下成立？ | **决定性**；且须解决 §3 的未对齐 |

## 2. ⭐ 小灵的预判（须被证实或被推翻，不得当作结论）
```
· A2 疑为【可逆】：V(X,H) 对 H 作二阶差分，可回收 C(h)=Σ_nΛ(n)Λ(n+h)
  （三角权 (H−|h|) 的差分结构）——但须扣除 principal/diagonal/规范化项（S5）
  ⟹ 若 A2 可逆，则困难【不在变换】，而在【求值】
· A4 为决定性：若 $C\to F$ 是 exact/asymptotic 双向 ⟹ S2-c ⟺ F(α)(α>1)（等价点被精确定位）
  若为单向 ⟹ 缺口位置本身即新结构性结果
```

## 3. ⭐ 必解决的未对齐（见 R-A8.3-verify 勘误）
$$\boxed{\lambda=\frac1{1-\eta}\ (\Rightarrow H=\sqrt X\mapsto\lambda=2)\quad\text{vs}\quad \alpha=1+\eta\ (\Rightarrow H=\sqrt X\mapsto\alpha=1.5)}$$
```
两式不能同时作为映到同一 F 参数的映射
⟹ A4 必须核实 LPZ / Montgomery–Soundararajan 的 α↔H 约定
⟹ 此未对齐不解决，R8 的"自对偶尺度 H=√X"陈述【悬空】
```

## 4. 四输出（事先声明）
```
R8v-i   A2 可逆 且 A4 为双向 ⟹ **S2-c 与 F(α)(α>1) 的等价点被精确定位**（重大结构性结果）
R8v-ii  A2 可逆 但 A4 单向 ⟹ **缺口位置明确**（新结构性结果，指向具体哪一步失去信息）
R8v-iii A2 不可逆 ⟹ 缺口在变换本身（须指明是端点项还是 prime-pair 信息）
R8v-iv  未对齐无法解决 ⟹ 坐标层问题（须先统一 α/λ/H 三者的约定）
```

## 5. 硬禁令
```
· 不得写"char-0 中不存在这种二阶主项机制"（Hooley 已给无条件反例，范围 H≥X^{7/12+ε}）
· 不得把 Hooley 的 h（区间长度）当作其平均坐标（AOC*）
· 不得用一般 Parseval/频率均方恒等式冒充"频率均方 ⟹ S2-c"
· 未解决 §3 未对齐前，不得引用 H=√X 的自对偶陈述
```

## 6. 留档/预算/必产 R
```
预算：1 轮纸面（不写代码、不做数值）
留档：docs/R_8v-transform-chain-audit.md（固定格式：目标链 → A1–A4 逐箭（含证据等级）
      → §3 未对齐处理 → 输出判定（i–iv）→ 【必产 R】→ 诚实边界）
必产 R：至少一条
```

## 7. 预注册预期
```
最可能：A2 可逆、A4 单向 ⟹ R8v-ii（缺口位置明确）
最理想：R8v-i（等价点精确定位）
须避免：跳过 §3 未对齐直接下结论
```

## 8. 诚实边界（起草自限）
```
· §2 的"可逆"预判基于三角权差分结构，未核实（须处理 principal/diagonal/规范化项）
· §3 的未对齐为结构性问题陈述；孰对孰错须核原文
· Hooley 主项公式与范围取自唐先生提供的 LPZ 页面（标【文献级】）
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```
