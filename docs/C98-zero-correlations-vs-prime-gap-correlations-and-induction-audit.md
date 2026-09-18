已查地图（所查：`dn-project/zeros/zeros6`（**2,001,052 个零点，`t≤1.05×10^6`**）、`CLOSED-ROUTES-MAP.md:228`／`:919`、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`C-89`（两条失配）、`C-91` §4（硬过滤器）、`V192` §③、`V188` §2（饱和定理）、`V259`（**判死判据：可写成 `lim F_n` 有限局部聚合 ⟹ DEAD**）、`V211`（有限-无限八类）、`E45-ceiling-law-construction.md`、`C-62`／`C-63`（`(ISO)` 两输入循环））。**结论**：**零点间关联性（真实数据实测）**——间隙分布与**配对相关均与 GUE 吻合** ✓✓；**间隙自相关 `r₁ = −0.34889`（493σ）**远强于素数侧（`−0.03556`）✓✓；**数方差 `Σ²(L)` 平坦 ≈0.4（饱和刚性）**，并已查明其正确性（`= Var(S(u+L)−S(u)) ≤ 4Var(S)`，实测 `std(S)=0.332`）✓✓。**唐先生判断成立**：零点关联性与相邻素数关联性**确有关系**——即档案已登记的 **`support>1` 等价链**（`Montgomery F(α)` ↔ Hardy–Littlewood 素数对相关）✓✓。**归纳法**：不能解决无限问题，理由不是"没想到"，而是**归纳步所需的算术输入正是那堵墙本身** ✓✓

# C-98 · **零点关联性实测 ＋ 与素数间隙关联性的关系 ＋ 归纳法审计**

> **时间**：2026-09-18 14:59／15:01 唐先生：看**零点之间的关联性**；**归纳法能否解决无限问题**；**零点关联性与相邻素数关联性应当相关**
> **数据**：`dn-project/zeros/zeros6`，**2,001,052 个零点**（`t` 至 `1.05×10^6`）；脚本 `scripts/zero_correlation_probe.py` ✓

---

## §0 结论（先行）

$$\textbf{(1)}\ \text{零点间隙分布}\ \textbf{与 GUE（Wigner surmise）吻合}✓✓;\ \text{配对相关}\ R_2(s)\ \textbf{与}\ 1-(\sin\pi s/\pi s)^2\ \textbf{吻合}✓✓$$
$$\textbf{(2)}\ ⭐\ \text{间隙自相关}\ \boxed{r_1=-0.34889\ (493.5\sigma)},\ r_2=-0.07472,\ r_3=-0.03323,\ r_4=-0.02310,\ r_5=-0.01701✓✓$$
$$\qquad \text{对照素数间隙}\ r_1=-0.03556\ (40\sigma) \Longrightarrow \textbf{零侧负关联强度约为素侧的 10 倍}✓$$
$$\textbf{(3)}\ ⭐\ \text{数方差}\ \Sigma^2(L)\ \textbf{平坦}\approx0.33\text{–}0.43\（L=1\ \text{到}\ 10^4） \Longrightarrow \textbf{饱和刚性}✓✓$$
$$\qquad \text{原因（本档查明）}：\Sigma^2(L)=\mathrm{Var}\bigl(S(u+L)-S(u)\bigr)\le4\,\mathrm{Var}(S);\quad \text{实测}\ \mathrm{std}(S)=0.332 \Longrightarrow \text{上限}\approx0.44✓✓$$
$$\textbf{(4)}\ ⭐\ \textbf{唐先生判断成立}：\text{零点关联性与相邻素数关联性}\ \textbf{有关系}——\text{即}\ \text{`support>1`}\ \textbf{等价链}✓✓$$
$$\textbf{(5)}\ \textbf{归纳法}：\textbf{不能} \text{解决无限问题};\ \text{理由＝}\textbf{归纳步所需的算术输入正是那堵墙}✓✓$$

---

## §1 零点侧实测（`Part A`）

### A1 归一化间隙分布（展开后平均间距 `= 1.000000`）

| `s` | 实测 | GUE(Wigner) | Poisson |
|:--|--:|--:|--:|
| [0,0.2) | 0.00714 | 0.00845 | 0.18127 |
| [0.2,0.4) | 0.04727 | 0.05294 | 0.14841 |
| [0.4,0.6) | 0.11196 | 0.11729 | 0.12151 |
| [0.6,0.8) | 0.17095 | 0.16867 | 0.09948 |
| [0.8,1.0) | 0.19422 | 0.18566 | 0.08145 |
| [1.0,1.4) | 0.30495 | 0.29436 | 0.12128 |
| [1.4,2.0) | 0.14885 | 0.15583 | 0.11126 |
| [2.0,3.0) | 0.01467 | 0.01740 | 0.08555 |
| [3.0,5.0) | 0.00001 | 0.00005 | 0.04305 |

$$\text{间隙方差}：\mathrm{Var}(d)=0.166075\quad（\text{GUE 预测}\ 3\pi/8-1=0.1781;\ \text{Poisson}=1）✓✓ \Longrightarrow \textbf{GUE 型排斥}✓$$

### A2 配对相关 `R₂(s)`（索引位移池化，`s≤60`）

| `s` | 0.55 | 1.55 | 2.55 | 3.55 | 5.05 | 10.05 | 20.05 | 30.05 | 45.05 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 实测 | 0.6437 | 0.9611 | 0.9921 | 0.9972 | 0.9973 | 0.9942 | 1.0197 | 1.0401 | 1.0131 |
| GUE | 0.6733 | 0.9589 | 0.9848 | 0.9922 | 0.9999 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

$$\text{小}\ s\ \textbf{吻合}✓;\ ⚠️\ \text{大}\ s\（\ge20\text{）}\ \text{实测偏}\ \textbf{+1\text{–}4\%}\ \Longrightarrow \text{待核（可能是展开/有限范围效应）}✓$$

### A3 间隙自相关（**核心**）

| 滞后 | 1 | 2 | 3 | 4 | 5 |
|:--|--:|--:|--:|--:|--:|
| `r`（零点）| **−0.34889** | −0.07472 | −0.03323 | −0.02310 | −0.01701 |
| `\|r\|/se` | **493.5σ** | 105.7σ | 47.0σ | 32.7σ | 24.1σ |
| `r`（素数间隙，`C-97`）| −0.03556 | −0.01479 | −0.00831 | −0.00455 | — |

$$\Longrightarrow\ \textbf{两侧同为负};\ \text{零侧强度}\approx\textbf{10 倍}✓✓$$

### A4 数方差 `Σ²(L)`（**饱和刚性**）

| `L` | 1 | 10 | 100 | 1000 | 5000 | 10000 |
|:--|--:|--:|--:|--:|--:|--:|
| `Σ²` | 0.329 | 0.406 | 0.378 | 0.388 | 0.386 | 0.388 |
| Poisson(`=L`) | 1 | 10 | 100 | 1000 | 5000 | 10000 |

$$\Sigma^2(L)\ \textbf{几乎与}\ L\ \textbf{无关} \Longrightarrow \textbf{计数涨落被锁在}\ \pm0.6\ \text{个零点以内}✓✓$$
$$\qquad \text{机制}：\Sigma^2(L)=\mathrm{Var}\bigl(S(u+L)-S(u)\bigr),\ S(t)=\tfrac1\pi\arg\zeta(\tfrac12+it);\ \text{而}\ \mathrm{Var}(S)\ \text{有限} \Longrightarrow \textbf{上界}\ 4\mathrm{Var}(S)✓✓$$
$$\qquad \text{自检}：\mathrm{std}(S)=\mathrm{std}(x_n-n)=0.332 \Longrightarrow 4(0.332)^2=0.441 \approx \text{实测上限}✓✓$$
$$\qquad \qquad \text{且}\ (1/2\pi^2)\log\log T\ \text{于}\ T=1.05\times10^6\ \text{给出}\ 0.13 \Longrightarrow \mathrm{std}\approx0.36 \approx \text{实测}\ 0.332✓✓$$
$$\qquad ⚠️\ \text{故"}\ \Sigma^2\sim\log L\ \text{"的 GUE 渐近在本有限范围内}\ \textbf{看不到};\ \text{本档记}\ \textbf{饱和刚性}✓$$

### A5 ⚠️ **三处自我实现错误（已自查修正）** `[纪律]`

$$\text{(i)}\ cnt=idx-\mathrm{arange}(len)\ \text{应为}\ idx-50j \Longrightarrow \text{曾得}\ \Sigma^2\approx3.2\times10^{11}✗$$
$$\text{(ii)}\ \text{大}\ L\ \text{时窗口越界未掩码}\（st+L>x_{\max}\text{）} \Longrightarrow \text{方差虚高}✗$$
$$\text{(iii)}\ \text{窗口起点取}\ \textbf{零点} \text{（锚定）而非任意展开位置} \Longrightarrow \text{只测到端点}\ S\ \text{之差}✗$$
$$\Longrightarrow\ \text{均按既有纪律}\ \textbf{"结果异常先怀疑自己的实现"}\ \text{自查修正}✓✓\（\text{该纪律在本项目已应验 11+ 次}）$$

## §2 ⭐ 零点关联性 ↔ 素数间隙关联性（`Part B`；唐先生判断）

$$\textbf{档案已登记的等价链（`C-86`／`SUPPORT-1`）}：\boxed{\text{support}>1\iff\text{无条件三阶矩（}X\asymp T\text{）}\iff\textbf{prime-pair}\iff X\le T\ \text{的可扩带宽}}✓✓$$
$$\qquad \text{其机制＝}\textbf{显式公式的 Fourier 对偶}：\text{Montgomery 的}\ F(\alpha)\ \text{↔}\ \text{Hardy--Littlewood 型素数对相关}✓✓$$
$$\qquad \qquad \text{（条件等价：}\ F(\alpha)=|\alpha|\ (|\alpha|\le1)\ \text{↔ 素数对的奇异级数行为）}✓$$
$$\Longrightarrow\ \textbf{唐先生的判断＝该等价链的内容}：\text{两侧统计量}\ \textbf{同源}✓✓$$

| 侧 | 对象 | 实测负关联 | 机制 |
|:--|:--|--:|:--|
| 零侧 | `{γ_ρ}` 间隙 | `r₁ = −0.34889` | **能级排斥**（GUE）|
| 素侧 | 相邻素数间隙 | `r₁ = −0.03556` | **可容许性**（`mod 2`／`mod 3`，奇异级数）＋残差 |

$$\textbf{边界的精确位置}：\text{局部两侧统计量}\ \textbf{形状同源}（同一对偶）;\ \text{但}\ \textbf{定量等价只到}\ \text{support}\le1（\text{Montgomery 无条件范围}）✓$$
$$\qquad ⚠️\ \text{support}>1\ \text{的定量对应}\ \textbf{正是缺输入} \text{——即}\ \text{`C-91`}\ \text{所记的}\ \textbf{唯一残余}✓✓$$

## §3 归纳法审计（`Part C`；唐先生前问）

$$\text{归纳法}＝\text{"}\textbf{有限}\to\textbf{无限}\text{"}\ \text{机制};\ \text{档案}\ \textbf{已审该类}（`V211` 八类;\ `V259` 判死判据）✓$$
$$\textbf{判死判据（`V259`，逐字）}：\text{若命题可写成}\ \lim F_n（F_n\ \text{＝有限局部聚合}） \Longrightarrow \textbf{DEAD}✓✓$$
$$\textbf{归纳步需要什么}：\text{一个}\ n\to n+1\ \text{的}\ \textbf{算术内容}\ \text{（不能是纯逻辑陈述}）;\ \text{而}\ \textbf{零点不是递归定义的} \Longrightarrow \textbf{无}\ n\to n+1\ \text{的算术桥}✓✓$$
$$\qquad \text{具体地}：\text{"第 }n\ \text{个零点成立}\Rightarrow\text{第 }n+1\ \text{个成立"}\ \text{需要一个把}\ \gamma_n\ \text{与}\ \gamma_{n+1}\ \text{相连的}\ \textbf{算术关系};\ \text{已知唯一此类关系＝}\textbf{显式公式}（\text{已饱和}）✓✓$$
$$\textbf{唯一现成的"一}\Rightarrow\text{多"步}＝\text{`(ISO)`}（\text{一个离轴}\Rightarrow\text{无穷多}）;\ \text{其两个输入已在}\ \text{`C-62`／`C-63`}\ \text{判}\ \textbf{循环}⟹ \textbf{归纳的燃料不可用}✓✓$$
$$\textbf{反例（已证）}：\text{GORZ 的 Jensen 阶梯}\ \textbf{确是归纳式结果}（n\ge N(d)\ \text{无条件}）;\ \text{但}\ \textbf{其余部}\equiv\text{RH}\（\text{`V191`}） \Longrightarrow \text{归纳只能搬动}\ \textbf{已证部分}✓✓$$
$$\Longrightarrow\ \boxed{\text{归纳法不能解决无限问题}：\textbf{归纳步所需的算术输入}\ \textbf{正是那堵墙本身}（\text{与}\ \text{`R1`／`R2`}\ \text{同址}）}✓✓$$

## §4 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 15:0x）`[纪律]`（先跑后写）

```
技术词 饱和刚性      命中文件数=0
技术词 零点-素数侧对偶  命中文件数=0
技术词 两体相关      命中文件数=0
技术词 归纳步       命中文件数=1  :: ./E45-ceiling-law-construction.md
```
**读数**：`饱和刚性`／`零点-素数侧对偶`／`两体相关`＝**0 档 ⟹ 本档新增** ✓；`归纳步`＝**1 档 ⟹ 档案已有**（`E45`）⟹ 引用 ✓

## §5 边界

- `[数据]` §1 全部**本次实算**（数据 `zeros6` 2,001,052 个零点；脚本入仓）✓；⚠️ A2 大 `s` 的 `+1–4%` 超额**待核**；A4 的 GUE 常数系数（`1/π²` vs `2/π²`）本档**两种并列**并标待核 ✓
- `[档案]` §2 等价链、§3 判死判据与 `V191`／`(ISO)` 均为**档内引用** ✓
- **不声称**：零侧与素侧的定量等价超出 `support≤1` ✗；**不声称**归纳法"原则上不可能" ✗（仅：**已枚举类内**其燃料不可用）；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓

```
⚠️ 唐先生 14:59／15:01：①看零点间关联性 ②归纳法能否解决无限问题 ③零点关联性与相邻素数关联性应当相关
✅ 数据：dn-project/zeros/zeros6 = **2,001,052 个零点**（t 至 1.05×10^6）；脚本 scripts/zero_correlation_probe.py
   [A1] 归一化间隙分布: 与 GUE(Wigner surmise) 吻合; Var(d)=0.166075(GUE 0.1781, Poisson 1) ⟹ GUE 型排斥
   [A2] 配对相关 R2(s): 小 s 吻合 1−(sinπs/πs)² (s=0.55: 0.6437 vs 0.6733; s=1.55: 0.9611 vs 0.9589);
        ⚠️ 大 s(≥20) 实测偏 +1–4% 待核
   [A3] ⭐间隙自相关: r1=−0.34889(493.5σ), r2=−0.07472(105.7σ), r3=−0.03323, r4=−0.02310, r5=−0.01701
        ⟹ 对照素数间隙 r1=−0.03556(40σ) ⟹ 零侧负关联强度约素侧 10 倍
   [A4] ⭐数方差 Σ²(L) 平坦 ≈0.33–0.43（L=1..10^4）⟹ **饱和刚性**
        机制查明: Σ²(L)=Var(S(u+L)−S(u)) ≤ 4Var(S); 实测 std(S)=std(x_n−n)=0.332 ⟹ 上限 0.441 ≈ 实测
        且 (1/2π²)loglogT 于 T=1.05e6 给 0.13 ⟹ std≈0.36 ≈ 实测 0.332 ⟹ 展开正确、S 量级正确
        ⟹ "Σ²~logL"的 GUE 渐近在本有限范围看不到；记为饱和刚性
   [A5] ⚠️ 三处自我实现错误（已自查修正）: ①cnt 用 arange 而非 50j（曾得 3.2e11）②大 L 窗口越界未掩码 ③窗口起点锚在零点上
        ⟹ 均按"结果异常先怀疑自己的实现"纪律修正
⭐ [B] 唐先生判断成立：零点关联性与素数间隙关联性**有关系** = 档案已登记 support>1 等价链
   （support>1 ⟺ 无条件三阶矩(X≍T) ⟺ prime-pair ⟺ X≤T 可扩带宽）；机制 = 显式公式的 Fourier 对偶
   （Montgomery F(α) ↔ Hardy–Littlewood 素数对相关）；两侧实测均负（零侧 −0.349 / 素侧 −0.0356）；
   机制各自: 零侧=能级排斥(GUE)；素侧=可容许性(mod2/mod3, 奇异级数)+残差
   ⚠️ 边界精确位置: 局部两侧形状同源，但**定量等价只到 support≤1**；support>1 的定量对应正是缺输入（C-91 唯一残余）
⭐ [C] 归纳法审计：归纳法=有限→无限机制，档案已审该类（V211 八类; V259 判死判据: 可写成 lim F_n 有限局部聚合 ⟹ DEAD）；
   归纳步需要 n→n+1 的**算术内容**，而零点非递归定义 ⟹ 无算术桥（唯一此类关系=显式公式，已饱和）；
   唯一"一⇒多"步=(ISO)，其两输入已被 C-62/C-63 判循环 ⟹ 燃料不可用；
   反例: GORZ Jensen 阶梯确是归纳式结果，但余部 ≡ RH（V191）⟹ 归纳只能搬动已证部分
   ⟹ 归纳不能解决无限问题，理由 = 归纳步所需的算术输入正是那堵墙本身（与 R1/R2 同址）
✅ 净产出：①零点侧五项实测（含 493σ 自相关、饱和刚性）✓ ②两侧关系定位（= support>1 等价链）✓ ③归纳法判词 ✓ ④三处自我错误修正记录 ✓
```
