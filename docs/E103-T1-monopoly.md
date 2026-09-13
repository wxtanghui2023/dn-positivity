# E103 · ⭐⭐⭐ **T1 垄断性：两条排除** ✓ —— **Lemma A（可证 ✓）＋ 文献定理（Lagarias–Rodgers ✓）**

> 委托 ✓ 唐先生 21:50 "继续" ✓（攻 **T1 垄断性**：零点的可识别性是否必须经过解析延拓 ✓）
> 执行 ✓ 小灵｜脚本 ✓ `scripts/E103_finite_stage_blindness.py` ＋ `.txt` ✓｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 结论（✓ 四条 ✓）

```
⭐⭐ **① Lemma A（初等，可证 ✓）**：**有限 Euler 积在开临界带内【无零点】** ✗
   $$F_P(s)=\prod_{p\le P}(1-p^{-s})^{-1}\ \Longrightarrow\ \text{零点集}=\varnothing\ ✗\ ;\qquad \text{极点全在}\ \sigma=0\ ✗\ (\textbf{边界，非带内})$$
   ⟹ **零点是【极限现象】** ✓ ⟹ ⭐ **地图的"limit-seeing"条件被【推出】，而非假设** ✓✓（**本轮对地图的一处实质性改进** ✓）
⭐⭐ **② 数值核验 ✓**：截断级数 $D_N(s)=\sum_{n\le N}n^{-s}$ 在同一盒内的零点计数
   $$\zeta:\ \mathbf{3}\qquad D_{10}:\ 6\ \ \ D_{20}:\ 9\ \ \ D_{50}:\ 14\ \ \ D_{100}:\ 19\ \Longrightarrow\ \textbf{单调增长、不收敛}\ ✗✓$$
   （$D_N$ 在带内**发散** ✗，故其函数值不收敛于 $\zeta$ ⟹ **其零点集亦不收敛** ✓）⟹ **朴素有限极限看不见零点** ✓
⭐⭐ **③ 文献定理（✓ 项目已有 ✓）**：**Lagarias–Rodgers** 证明 **Montgomery–Hejhal–Rudnick–Sarnak 的【全部已知 band-limited 相关信息】与 Alternative Hypothesis 相容** ✓✓
   （构造反例点过程 ✓）⟹ **统计/相关型 transport 【无法定位单个零点】** ✗✓ —— **这是覆盖的一处实质增益 ✓**
⭐ **④ 合并结论 ✓**：transport 表的排除状态变为
   $$\underbrace{T3}_{\text{C2 失败 ✗}}\ \ \underbrace{T2}_{\text{purity/HP ✗}}\ \ \underbrace{T4}_{\text{须回 T2 ✗}}\ \ \underbrace{\text{统计型}}_{\text{文献定理 ✗}}\ \ \underbrace{\text{朴素有限}}_{\text{Lemma A ＋ 数值 ✗}}\ \Longrightarrow\ \textbf{仅剩 }T1\ \text{与未知的 }T5$$
```

## 1. Lemma A（✓ 初等证明 ✓）

$$\text{对有限素数集 }P:\quad F_P(s)=\prod_{p\in P}\frac1{1-p^{-s}}$$
```
✓ 每个因子 $1/(1-p^{-s})$ 在 $1-p^{-s}\neq0$ 处**非零** ✓（有限个非零之积 ⟹ $F_P$ **无零点** ✗）
✓ $F_P$ 的极点：$p^{-s}=1\iff s=2\pi ik/\log p\iff \sigma=0,\ t=2\pi k/\log p$ ✓
   —— 全在 $\sigma=0$ ✗，即**临界带的边界**，**不在开带 $0<\sigma<1$ 内** ✓
$$\Longrightarrow\ \boxed{\text{任何有限阶段 $(p\le P)$ 的素数数据【不能定位任何零点】}\ ✗}$$
```
⟹ ⭐ **推论 ✓**：能定位零点者**必须是极限程序** ✓ —— **地图"limit-seeing/finite-blind"中的"limit-seeing"由此【成为定理】✓**

## 2. 数值核验（✓ $\zeta$ 自身零点用 mpmath ✓；$D_N$ 零点用幅角原理 ✓）

| $N$ | $\#\{\text{zeros of }D_N\}$ | 与 $\zeta$（3）之比 |
|--:|--:|--:|
| 10 | 6 | 2.00 |
| 20 | 9 | 3.00 |
| 50 | 14 | 4.67 |
| **100** | **19** | **6.33** |

$$\text{盒：}\ \sigma\in[0.02,0.98],\ t\in[0.5,30]\ ;\qquad \zeta\ \text{的零点（前五个纵坐标）}：14.1347,\ 21.0220,\ 25.0109,\ 30.4249,\ 32.9351$$

⟹ **计数随 $N$ 单调增长、不趋于 3** ✓ ⟹ **截断级数的零点集不收敛于 $\zeta$ 的零点集** ✓✓

## 3. ⭐ 文献定理：统计型 transport 被排除（✓ 项目档案已有 ✓）

```
【A3-third-moment-barrier.md 逐字 ✓，据 Lagarias–Rodgers arXiv:1905.12123v3 ✓】
   "Lagarias–Rodgers 另证：**Montgomery–Hejhal–Rudnick-Sarnak 的全部已知 band-limited 信息
    与 Alternative Hypothesis 相容**（构造反例点过程）——现有高阶相关信息**连"替代假设"都排除不了**" ✓✓
   （另 ✓：其 Theorem 2.4 明文"**Assume RH**" ⟹ Hejhal(n=3)、RS(n>3) 均 RH 条件 ✓）
⟹ ⭐ **含义 ✓**：若载体的输出是**相关/统计型**数据（密度、pair correlation、band-limited 相关 ✓），
   则该数据**与离轴构型相容** ✗ ⟹ **不能定位单个零点** ✗ ⟹ **C2 失败** ✗✓
```

## 4. Transport 表的**排除状态汇总**（✓ 更新 ✓）

| # | Transport | 排除依据 | 状态 |
|:--:|:--|:--|:--|
| **T1** | **显式公式／解析延拓** | —— | ⚠️ **唯一存活**（但属**类 IV** ⟹ P-Scale ✗） |
| **T2** | 正性／几何（Hodge–Riemann／Weil 配对／自伴／酉） | 箱 12 ＋ F-5 ＋ 类 II/III | ✗ |
| **T3** | 局部 character（Chebotarev/Artin） | **AOB3 §1**（共轭类 ⟹ 只给不变数据） | ✗ **C2 失败** |
| **T4** | 动力学／遍历 | 箱 5；钉线须正性 ⟹ 回 T2 | ✗ |
| **T5-stats** | 统计／相关型 | **Lagarias–Rodgers（文献 ✓）** | ✗ **本轮增益 ✓** |
| **T5-naive** | 朴素有限极限（有限 Euler 积／截断级数） | **Lemma A ＋ 数值 ✓** | ✗ **本轮增益 ✓** |
| **T5** | ??? | —— | ⭐ **所缺 ✓** |

$$\boxed{\text{故 T1 的"垄断"在【上述类中】成立 ✓ —— 而唯一逃逸口是 }T5\ \text{（非解析延拓、非算子/谱、非统计、非朴素的 canonical 极限程序）}}$$

## 5. ⭐ 排除之后的**唯一问题**（✓ 收窄到一句 ✓）

$$\boxed{\text{是否存在一个 canonical 极限程序，从素数数据出发，}\textbf{既非解析延拓、又非算子/谱、又非统计型}，\ \textbf{却能定位【单个】零点？}}$$

```
【若否 ✓】⟹ **T1 垄断 ⟹ transport 表完整 ⟹ RepThm ⟹ 项目真正封口** ✗ —— **重大结论** ✓✓
【若是 ✓】⟹ **强制给出构造** ⟹ **表外新类（V = 第五种 transport）＝ 唯一新方向** ✓ LIVE ✓
```

## 6. 边界与纪律（✓）

```
✅ **本轮两处实质增益 ✓**：① **"limit-seeing"由假设变为【定理】** ✓（Lemma A ✓ 初等、严格 ✓）；
   ② **统计型 transport 被【文献定理】排除** ✓（Lagarias–Rodgers ✓，非启发式 ✓）
⚠️ **Lemma A 不是 T1 垄断的证明** ✗ —— 它只排除**朴素有限阶段** ✗；
   ⚠️ **无法排除"非朴素极限"** ✗（如算子极限／范畴极限／模型论极限 ✓）—— 那正是 T5 的所在 ✓
⚠️ **未宣布封口** ✗；**未宣布 T5 存在** ✗；**未用 RH** ✓；**未跑 Lean** ✓
⭐ **下一步（唯一）✓**：攻 **§5 的问题** ✓ —— 具体入口 ✓：**"极限程序"的完整分类** ✓
   （即：从素数数据到复平面的极限程序，是否只有"解析延拓 ⟹ 亚纯函数"这一种能承载**单点**信息 ✓）
```
