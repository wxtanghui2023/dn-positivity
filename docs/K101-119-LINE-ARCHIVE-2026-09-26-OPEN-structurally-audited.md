已查地图：已跑 scripts/prework_map_check.sh K(10,1) 119 归档 机制地图 A_1<=49 ⟹ 汇总既有全部细档（B2QUOTA／SUM-P1P4／GRAMSIGN／PACKB／ISOB3／STAR3／TCOLL／SCOL／HQ1／MIDSUP／K1AUDIT／L4AUDIT／ADJCOUP／L2AUDIT／L2-CLOSURE／GAPTHEOREM／DELSARTE／ISOCUT ✓）。
D0: 本档对象 = $K_2(10,1)=119$ 假设线（既有对象）
D1: 0（产出为归档状态与资产挂牌）

# K(10,1)=119 线 · 正式归档（2026-09-26 收刀）

## §0 状态标签（唐先生 2026-09-26 21:26 裁定 ✓）

```
$$\boxed{\textbf{OPEN — structurally audited / current mechanisms NO-GO}}\ ✓$$
$$\qquad\textbf{不是} CLOSED ✗;\ \textbf{不是} "119 不存在" ✗;\ \text{而是"局部资源型攻击已系统审计完毕、现有机制全部 NO-GO"}\ ✓$$
$$
$$
```

**NO-GO 诊断（本线核心结论 ✓）**：

```
$$\boxed{\text{现有一阶／二阶局部 incidence 量\textbf{全部存在 conservation law}，无法产生严格亏损}}\ ✓$$
$$\qquad\Longrightarrow\ \text{119 的障碍\textbf{不是}缺一个局部 counting trick，而是缺一个\textbf{真正改变 quantity 的新不变量}（或新的外部数学资产）}\ ✓$$
$$
$$
```

---

## §1 审计总表（逐项可溯源 ✓）

```
$$\textbf{(1) }A_1\le59\ \text{（匹配定理）}:\ \text{基线}\ ✓;\ \text{细档}\ \texttt{PACKB}\ ✓$$
$$\textbf{(2) Delsarte＋}Q{=}1\ \Longrightarrow\ \mathbf{A_1\le49}:\ \textbf{本轮真正的新定理}\ ✓✓;\ \text{细档}\ \texttt{DELSARTE}\ ✓$$
$$\textbf{(3) }|I|\ge21\ \text{（孤立码字）}:\ \text{新结构事实，\textbf{非 binding}}\ ✓$$
$$\textbf{(4) 三阶}\ \sum_x\binom{b(x)}3=1:\ \text{成立，但\textbf{等价于 }Q{=}1\ \text{假设}\ ✗;\ \text{细档}\ \texttt{DELSARTE}\ \S2\ ✓$$
$$\textbf{(5) isolated→private capacity}:\ \textbf{失败}（\text{正确式＝既有 }(C{-}1)\ \text{恒等式}）\ ✗;\ \text{细档}\ \texttt{ISOCUT}\ ✓$$
$$\textbf{(6) midpoint capacity}:\ \text{精确饱和，无 leverage}\ ✗;\ \text{细档}\ \texttt{MIDSUP／K1AUDIT}\ ✓$$
$$\textbf{(7) }G_m\ \text{／ ADJCOUP 等局部传播}:\ \text{饱和／重述}\ ✗;\ \text{细档}\ \texttt{L4AUDIT／ADJCOUP}\ ✓$$
$$\textbf{(8) 三点／Terwilliger（文献）}:\ \text{已有；对本 cell 仅约}\ 105.22<107<119\ ✗;\ \text{细档}\ \texttt{L2AUDIT}\ ✓$$
$$\textbf{(9) 119 不存在}:\ \textbf{未证明，仍 OPEN}\ ✓$$
$$
$$
```

**十一族机制（同向汇合 ✓，细档见 §1 各项）**：

```
$$\text{线性局部求和}\to\text{二次符号}\to\text{双重计数}\to\text{packing 方向}\to\text{行闭合}\to\text{Haas×}Q_1\to\text{中点 load}\to\text{层限制}\to L_4\ \text{局部图}\to\text{相邻耦合}\to\text{孤立码字/三阶唯一性}$$
$$\qquad\Longrightarrow\ \text{全部只触及 }\sum_xf(\delta(x))\ \text{型或\textbf{由之决定的量}} \Longrightarrow\ \textbf{状态↔守恒律，无缺口}\ ✓$$
$$
$$
```

---

## §2 参数现状（供后续复用 ✓）

```
$$\text{假设 119 覆盖（}Q{=}1\text{ 分支）}:\quad 0\le A_1\le49\ ✓;\quad A_2=143-A_1\in[94,143]\ ✓;\quad |I|=119-2A_1\ge21\ ✓$$
$$\text{指纹}:\ N_1=740,\ N_2=283,\ N_3=1\ ✓;\quad 2A_2-3=283-2A_1\ \text{（恒等式 ✓）};\quad 2A_1\le98\ ✓$$
$$\text{基线}:\ 107\le K_2(10,1)\le120\ ✓\ (\text{下界 BÖW 2004};\ \text{上界 Östergård 构造});\quad \text{新 SDP 在 }(2,10,1)\ \text{给}\ 105.22\ ✗$$
$$
$$
```

---

## §3 新资产挂牌（可迁移 ✓）

```
$$\boxed{\textbf{ASSET: Delsarte × covering-identity}\ \Longrightarrow\ A_1\le49}$$
$$\qquad\textbf{形式}:\ \text{对 }|C|=M\ \text{、覆盖半径 }1\ \text{、且已知 }\sum_x\binom{b(x)}2=2(A_1+A_2)\ \text{（或其 }Q\text{-指纹）的码}:\ $$
$$\qquad\qquad\text{把 Delsarte 不等式族 }M_r=\sum_ja_jK_r(j)\ge0\ \text{与覆盖恒等式并联 LP}\ \Longrightarrow\ \text{得 }A_1\ \text{的上界（本例 }0.825236\times M/2=49.102\text{）}\ ✓$$
$$\qquad\textbf{可迁移性}:\ \text{任意 }(n,R=1)\ \text{参数只要知道 }b\text{-指纹或 }\sum\binom b2\ \text{即可照搬}\ ✓;\ \text{亦可用作\textbf{筛选工具}（快速判某 }(n,R)\ \text{的 }A_1\ \text{窗）}\ ✓$$
$$\qquad\textbf{细档}:\ \texttt{DELSARTE-2026-09-26-krawtchouk-route-and-the-a1-bound.md}\ ✓\ \text{（含 3 法 LP ＋ 直测 ＋ 对照 ✓）}$$
$$
$$
```

---

## §4 重开条件（明确 ✓）

```
$$\textbf{R-1}:\ \text{出现\textbf{新的 P1 机制}（非 }b\text{／midpoint／distance distribution 的线性重排）}\ ✓$$
$$\textbf{R-2}:\ \text{出现针对 }n=10,R=1\ \text{的\textbf{特殊结构定理}，使 119 假设产生\textbf{非守恒型} obstruction}\ ✓$$
$$\textbf{R-3}:\ \text{出现能咬 }(2,10,1)\ \text{此格的\textbf{更强外部工具}（如新的三阶/高阶 SDP 且 >107）}\ ✓$$
$$\textbf{禁止}:\ \text{为"再压一点 }A_1\text{"而继续跑同类 LP}\ ✗\ (\text{49}\to48\to\cdots\ \text{不改变存在性}\ ✗)$$
$$
$$
```

---

## §5 消费规则（后来者必读 ✓）

```
$$\text{复用本线者须声明消费何者}:\ \text{① 11 类机制"已试且不足"清单};\ \text{② }A_1\le49\ \text{及其证明路径};\ \text{③ 指纹 }(740,283,1)\ \text{与恒等式};\ \text{④ 缺口＝支撑型约束}\ ✓$$
$$\textbf{禁止误读}:\ \text{"119 不可达"}\ ✗;\ \text{"局部计数无用"}\ ✗;\ \text{"已 CLOSED"}\ ✗\ (\text{实为 OPEN—structurally audited}\ ✓)$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1 每项均**有独立细档** ✓（本档为汇总，不新造数学 ✓）
- §1 (2) 的 $A_1\le49$ 为**本日新定理** ✓（Delsarte 不等式 ＋ 本线 $Q=1$ 恒等式并联 LP ✓；三法一致 ＋ 直测 ＋ 对照 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张任何机制"不可能" ✗
- **未跑**搜索／求解器（除 §1(2) 的 LP ✓ 与若干构造性反例 ✓，均已在细档标注 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 119 线归档状态标签 命中文件数=1    :: ./K101-119-LINE-ARCHIVE-2026-09-26-OPEN-structurally-audited.md 
技术词 Delsarte×covering-identity 资产挂牌 命中文件数=1    :: ./K101-119-LINE-ARCHIVE-2026-09-26-OPEN-structurally-audited.md
```
- **本档新增**：119 线归档状态标签、Delsarte×covering-identity 资产挂牌（见上方命中数）
- **档案已有（引用，不列为提出）**：全部 11 族机制、$A_1\le49$、指纹 (740,283,1)、$A_1+A_2=143$
