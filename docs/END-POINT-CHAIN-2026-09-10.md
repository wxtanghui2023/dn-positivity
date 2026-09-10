# 机制搜索终点链（End-Point Chain）｜本阶段封存

**日期**：2026-09-10 ｜ 拍板：唐先生（停止候选搜索）｜ 性质：**方法论终点，不是 RH 终点**

---

## 0. 终审修正（唐先生，必须留档）

原文：显式公式下 $D$ 的频率就是零点，故任何 $\sqrt x$ 抵消系统必须重现零点相位。

**收紧为**：
$$\boxed{\text{显式公式固定了 }D\text{ 的【实际】频率（频谱唯一性）；}
\text{但"所有机制均须等价于该频率系统"（【机制唯一性】）尚未证明}}$$
前者属频谱唯一性框架；后者是更强的蕴含，目前无证明。

---

## 1. 终点链（四道墙）

$$\boxed{\text{Info wall}\ \rightarrow\ \text{Complexity wall fails}\ \rightarrow\ \text{Type wall}\ \rightarrow\ \text{Phase wall}}$$

| 墙 | 内容 | 证据等级 |
|---|---|---|
| **Info wall** | 局部(sieve/CRT)信息预算 $\log\log x$ vs 输出 $(x/\log x)\log\log x$ ⟹ 差 $x/\log x$ 量级 | 严格（Mertens） |
| **Complexity wall 不成立** | 素性 ∈ P（AKS）；Eratosthenes $O(x\log\log x)$ ⟹ 低复杂度+无 oracle+逐点确定位置【已存在】 ⟹ 复杂度无法判别 | 严格（引用） |
| **Type wall** | 点式正确性 $\not\Rightarrow$ 聚合刚性（缺蕴含，非独立性定理） | 方法学边界 |
| **Phase wall** | 单尺度平均统计量对相位盲（正交性，严格）；$\sqrt x$ 恰是 $L^2$ 尺度（无条件）；RH = $L^2\to L^\infty$ 零损失 ⟹ 需要全局 coherent phase cancellation | 步二严格；必要性侧为结构性论证 |

## 2. 三层结构（本阶段的核心图景）

```
点式层 n ↦ 1_ℙ(n)          : AKS 说明低复杂度 ≠ 聚合刚性
聚合幅度层 Σ|c_γ|²         : 只给出 L² 尺度 D ~ √x（无条件，免费）
聚合相位层 coherent phase  : RH 的真正困难被压缩到此
```

## 3. 统一解释：为什么前面几十条路线反复失败（本阶段最有价值的产物）

```
路线                        缺失
────────────────────────────────────────
CRT / sieve                 全局相位
Euclid / Mullin             位置相位
rad/product curvature       相位
K₂ 非交换矩阵               真实 prime-distribution phase
holonomy                    真实 phase coherence
carry dynamics              跨尺度 phase locking
A–M affine closure          prime-position constraint
聚合统计量                  relative phase
────────────────────────────────────────
共同点：能产生【结构】，不能产生【coherent prime phase】
```

## 4. 仍未关闭的唯一问题（下一阶段唯一入口）

$$\boxed{\text{什么【非零点等价】的全局结构能够产生 coherent phase rigidity？}}$$

**首要硬门槛（唐先生定）**：
```
X 不得预设：Hilbert–Pólya ｜ 谱自伴性 ｜ 显式公式 ｜ 零点频率
```
（否则必然是"在我指定的谱结构里唯一谱就是零点"——与已关闭的谱路线同类。）

## 5. 门槛总表（最终）
```
P1″      约束【具体】素数位置（非仅消除标签置换自由）
P0′      不读取未来 prime label
P-Info   三量分离 I_state/I_rule/I_out（允许 ≪；原 Ω(x/log x) 断言作废）
P-Type   点式正确性 ⇒/⇒ 聚合刚性（缺蕴含）
P-Phase  必须携带相位信息；单尺度平均数据相位盲
P-Comp   【不采纳】（素性 ∈ P，无法判别）
```

## 6. 处置

```
【封存】"寻找 RH 模型"这一搜索策略（机制层）
【不动】RH 问题本身（仍完全开放）
【禁止】在未回答 §4 问题前再制造新的算术不变量
【允许】围绕 §4 做纸面结构研究
```

## 7. 相关提交链
```
2aa89cd  FPCA 两处撤回 + FPCA-2（复杂度墙不成立）
4fe1887  A–M affine 终审（G_N={1}，定理式）
78f7310  ACA-1（相位墙、L²→L∞ 表述）
本篇     终点链封存
```
