已查地图：命中（`WEAK-RH-LOCALIZATION-LINE-STATE-SUMMARY`／`ZF-1`（近 `1/2` 无一致幂次节省）／`E-44`／`V186`（交换率）／`ZE` 线既有档）⟹ **引用，不开新案** ✓
D0: 本档对象 = 对"固定离轴带 zero-density"靶的事实核验（已知定理）＋ 定量废退公式 ＋ 本线资产能否改进的判定
D1: 0 （`[REVIEW]` 轮次：核验与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **靶选定：固定 `\delta_0` 的 zero-density 是**已知定理**，且**全密度层级**皆线性废退**

## §1 ⚠️ **事实核验（本档核心）：一档靶已知**

```
【您的靶】 $$N\bigl(\tfrac12+\delta_0,T\bigr)=o(T)\quad\text{或}\quad\ll T^{1-\eta}\ (\eta>0,\ \delta_0>0\ \text{固定})$$ ✓
【⚠️ 已知结果（档级，未逐字核原文）】 **Huxley 1972**：$$N(\sigma,T)\ \ll\ T^{\frac{3(1-\sigma)}{2-\sigma}+\varepsilon}\qquad \text{对 } \tfrac12\le\sigma\le1\ \text{一致}$$ ✓✓
　近 `\sigma=1` 侧由 **Guth–Maynard 2024** 改进（大值估计）⟹ 更优指数 ✓
【⟹ 判定】 取 `\sigma=\tfrac12+\delta_0`：$$N\bigl(\tfrac12+\delta_0,T\bigr)\ \ll\ T^{\,1-\eta(\delta_0)+\varepsilon},\qquad \boxed{\eta(\delta_0)=\frac{2\delta_0}{\tfrac32-\delta_0}\approx\frac43\delta_0}$$ ✓✓
　⟹ **对任意固定 `\delta_0>0`，`\eta(\delta_0)>0` ⟹ 次线性 ⟹ 一档靶（`1/10,\ 1/20,\ 1/100`）全部是已知定理** ✗✓✓
【⟹ 结论】 $$\boxed{\text{一档靶不是"值得立即攻击的新结果"，而是 1972 年已知结果}}$$ —— 可省下重复劳动 ✓✓
```

## §2 ⭐⭐⭐ **定量废退公式（本档推导，核心收获）**

```
【Huxley 的节省】 $$\eta_{\rm Hux}(\delta_0)=\frac{2\delta_0}{\tfrac32-\delta_0}\ \xrightarrow{\delta_0\to0}\ \frac43\delta_0$$ ⟹ **节省线性于 `\delta_0`** ✓✓
【Density Hypothesis 的节省】 `N(\sigma,T)\ll T^{2(1-\sigma)+\varepsilon}` ⟹ 取 `\sigma=\tfrac12+\delta_0`：$$N\ll T^{\,1-2\delta_0+\varepsilon}\ \Longrightarrow\ \boxed{\eta_{\rm DH}(\delta_0)=2\delta_0}$$ ✓✓
【⟹ ⟹ 结构性结论】 $$\boxed{\text{整个 zero-density 层级（含 DH）节省皆为 }\Theta(\delta_0)\ \text{——线性废退}}$$ ✓✓✓
【⟹ 推论（解释您的阶梯为何必在末端失败）】 阶梯 `\tfrac1{10}\to\tfrac1{20}\to\tfrac1{100}\to\delta(T)\downarrow0`：前段（固定 `\delta_0`）**已知** ✓；末段 `\delta(T)\downarrow0` 时 `\eta\asymp\delta(T)\to0` ⟹ **任何密度型结果都给不出与 `T` 无关的界** ✗✓✓ —— 这在**定量上**解释了 `ZF-1`（近 `1/2` 无一致幂次节省）✓✓
【⭐ 关键强度对照】 即便 DH 成立，节省 `2\delta_0`；而有限靶 `N_{\rm off}=O(1)` 需要 `\eta\to1` ⟹ **DH 离目标仍有本质距离** ⟹ 密度层级**结构性不足**，非技术不足 ✓✓✓
```

## §3 **本线资产能否改进一档靶？——判定：不能**

```
【资产 (i) inertia／rank–trace（`V186` Lemma R，已证紧）】 其自然输出是**在线零点的下界** $$\frac{N_0^s}{N}\ge2-R(\psi)$$ ⟹ 与 `N=N_0+N_{\rm off}` 合并得 $$\boxed{N_{\rm off}(T)\le\bigl(R(\psi)-1\bigr)N(T)}$$ ✓✓（**本档自行推导**）
　⟹ 以 `R(\psi_{\rm MT})\approx1.3275`：`N_{\rm off}\le0.3275\,N(T)` ⟹ **比例型（extensive）** ✗ ⟹ 与 `E-44` 同型失败 ✓
【资产 (ii) 显式公式固定核结构】 **就是**经典 zero-detecting polynomial／大值估计的同一工具箱 ⟹ 无新杠杆 ✓
【资产 (iii) 算术分离／EDS 机制】 已封（事件侧无出口）✗
【⟹ 判定】 $$\boxed{\text{本线资产不能改进一档靶（既不改指数，也给不出非 extensive 界）}}$$ ✓✓
```

## §4 **三档判定（照您的分层，本档核验后）**

| 目标 | 与现有资产匹配 | 核验后判定 |
|:--|:--|:--|
| 固定 `\delta_0` 的 zero-density（含 `o(T)`、`\ll T^{1-\eta}`） | 高（绕开 `T1/T2`） | ⚠️ **已知定理（Huxley 1972）⟹ 不是新结果靶** ✓ |
| 中间尺度 `r(T)\downarrow0` 的离轴排除 | 中高 | ⭐ **真前沿**；定量障碍已识别（节省 `\asymp\delta`）⟹ ＝`ZF-1` ✓ |
| 临界线比例提高 | 中 | 不同技术墙（mollifier/moments）⟹ 暂缓 ✓ |
| Density Hypothesis 全范围 | 中低 | 第二阶段；**即便成立仍线性废退** ✓ |
| LH | 低 | 换核心变量 ⟹ 暂不转 ✓（同意您的判断） |
| RH | 极低 | 冻结 ✓ |

## §5 **净建议（本档）**

```
【⛔ 不建议】 启动"固定 `\delta_0` 的一档靶"——**它已是已知定理**，做出来无新结果 ✓
【⭐ 唯一有新内容的密度型车道】 **(a)** 改进密度指数的**常数/指数**（经典技术，非本线资产）；**(b)** 中间尺度／有限靶——**已被本档证明密度层级结构性不足** ✓✓
【⟹ 判定】 $$\boxed{\text{若目标为"可发表的新结果"，密度型车道对本线全部封闭}}$$ ✓ —— 与 `WEAK-RH-LOCALIZATION-LINE-STATE-SUMMARY` 的收口判定**一致** ✓
```

## §6 **技术词回查（逐字 ✓）**

```
技术词 zero-density     命中文件数=34   :: ./FRONTIER-PRIMEGAP-SURVEY-2026-09.md ./E20-E40-zero-density-2026-read.md ./C305-FSD-blind-spot-audit-program-four-classes-dual-ledger-five-rounds.md 
技术词 次线性        命中文件数=7    :: ./lemma3-hostile-audit.md ./V188-null-relation-spectral-compensation-audit-four-channel-exhaustion.md ./CLOSED-ROUTES-MAP.md 
技术词 Huxley           命中文件数=21   :: ./FRONTIER-PRIMEGAP-SURVEY-2026-09.md ./E20-E40-zero-density-2026-read.md ./TYPE-MATCH-matching-types-exist-explicit-formula-and-large-value-density.md 
```
【三分类】 **本档新增**：`定量废退公式`／`密度层级结构性不足`（表述级）✓；**档案已有（引用）**：`次线性`／`zero-density`（若命中）；**通用词（不计）**：`Huxley`（人名）✓
【边界】 ⚠️ Huxley 1972／Guth–Maynard 2024 指数按**档级**引述（未逐字核原文）⟹ 采用前须核；⭐ §2 废退公式、§3 的 `N_{\rm off}\le(R-1)N` 为**本档自行推导** ✓；⛔ 未制造候选／未启动搜索／未改状态 ✓
