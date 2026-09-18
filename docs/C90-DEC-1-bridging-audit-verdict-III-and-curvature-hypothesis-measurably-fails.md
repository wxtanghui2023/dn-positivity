已查地图 + **命中已撤回原档**（所查：`PAPERA-uniformity-attack.md`（**§4 区域 B 结论【已撤回】** 逐字 ＋ §4.1 vdC 二阶差分检验式）、`PAPERA-expsum.md` §4、`PAPERA-sigma-form-lemma.md`（判死档）、`NEGATIVE-RESULTS-2026-09-12-ROUND.md`、`C2-W6-UB-4-strict-Abel-attempt-rigorous-gap-named.md`、`C-86`／`C-87`／`C-88`／`C-89`）。**结论**：`D3(b)-DEC-1` = **(III) 根本没有可用对象转换** ⟹ 且**附一条更强的定量否定**：曲率/横截性假设**在档案里已被实测否掉**——`vdC` 二阶导检验要求 `λ ≤ |f''| ≤ αλ`（**定号＋下有界**），而 `φ_k = nθ(γ_k)` 的二阶差分**符号 50/50 混合**（实测 正 999942／负 1001108）⟹ **标准检验在假设层面即失效** ⟹ `decoupling`（同族，需 Hessian 非退化／横截）同样不能咬 ✓✓ ⟹ **`UQRL` 四分支全关**，`UQRL` 仍开放但**技术族已穷尽** ✓✓

# C-90 · **`D3(b)-DEC-1`：zero-ordinate exponential sum → curved exponential sum 桥接审计**

> **时间**：2026-09-18 13:35 唐先生：收紧为六门（A 对象转换／B 曲率来源／C `n`-保持／D 一致性／E RH-free／F 强度），三分判定 (I)／(II)／(III)
> **判定**：**(III)**（＋ 曲率假设已实测失败）✓

---

## §0 结论（先行）

$$\boxed{\textbf{(III)}\ \text{根本没有可用对象转换}}\quad\Longrightarrow\quad \text{四分支}\ \textbf{全关};\quad UQRL\ \text{仍开放但}\ \textbf{技术族已穷尽}✓✓$$
$$\text{且}\ \textbf{更强的否定（本档）}：\text{即便}\ \textbf{假设} \text{存在桥，曲率／横截性假设}\ \textbf{已在档案中被实测否掉}：$$
$$\qquad \text{`vdC` 二阶导检验要求}\ \boxed{\lambda\le|f''|\le\alpha\lambda}\ \text{（}\textbf{定号＋下有界}）;\ \text{而}\ \phi_k=n\theta(\gamma_k)\ \text{的二阶差分}\ \textbf{符号 50/50 混合}✓✓$$
$$\qquad \text{（实测：正}\ 999942\ /\ \text{负}\ 1001108\text{）} \Longrightarrow \textbf{标准检验在假设层面即失效}✓✓$$

---

## §1 **Gate A（对象转换）**：✗ **失败**

$$\text{要求}：\exists\ \text{RH-free、算术自然的}\ \mathcal T:\ \sum_{\gamma\le T}w(\gamma)e^{in\phi(\gamma)}\mapsto\ \sum_{x\in X_T}a_xe^{i\Phi_n(x)}✓$$
$$\text{但三类已知转换}\ \textbf{全部被排除}：\quad \mathcal T\ne\text{显式公式}\quad\big|\quad \mathcal T\ne\text{Fourier 反演}\quad\big|\quad \mathcal T\ne\text{Nyman--Beurling／Burnol 型 Hilbert 对偶}✓$$
$$\qquad \Longrightarrow\ \text{未见第四类}\ \mathcal T \Longrightarrow \textbf{A 失败}\ \text{（仅有"}\textbf{伪桥}\text{"：经 ζ 大值／Dirichlet 多项式大值估计中转者，其中间是}\ \textbf{已有平均值不等式} \Longrightarrow \text{仍回}\ (\beta)）✓$$

## §2 ⭐ **Gate B（曲率来源）**：✗ **失败——且在假设层面**（档案已实测）

$$\text{档案逐字（`PAPERA-uniformity-attack.md` 首段）}：\text{"}\text{[§4 区域 B 的结论}\textbf{已撤回}\text{]}\ \text{标准 van der Corput 二阶导检验要求}\ \lambda\le|f''|\le\alpha\lambda\ \textbf{（定号＋下有界）}，\text{而}\ \phi_k=n\theta(\gamma_k)\ \text{的二阶差分}\ \textbf{符号 50/50 混合}\ \text{（实测 正 999942／负 1001108）——由符号随机 gap 跳变主导} \Longrightarrow \textbf{标准检验／sup-form／run-split 均为误用}\text{"}✓✓$$
$$\text{vdC 离散式（`PAPERA-expsum.md` §4 复现）}：\Bigl|\sum e^{i\phi_k}\Bigr|\le M\sqrt\Lambda+\Lambda^{-1/2},\qquad \Lambda=\max_k|n\,\Delta^2\theta_k|,\quad \Delta^2\theta_k=\theta_{k+2}-2\theta_{k+1}+\theta_k✓$$
$$\Longrightarrow\ \textbf{B 失败的两重理由}：\text{(i)}\ \textbf{定号假设} \text{不成立（实测 50/50）};\ \text{(ii)}\ \text{即便形式套用，也得不出所需界（配额不足）}✓✓$$
$$\qquad ⭐\ \text{推论（本档）}：\text{decoupling 与 vdC}\ \textbf{同族}（\text{均需曲率／横截性"非退化且有下界"） \Longrightarrow \text{定号失效} \Rightarrow \textbf{decoupling 亦不能咬}}✓✓$$
$$\qquad ⭐\ \textbf{循环性（本档）}：\text{检验失败}\ \textbf{恰由} \text{零点间距（gap）的不规则性造成} \Longrightarrow \text{要应用它须先有}\ \textbf{gap 正则性} \text{＝研究对象的性质} \Longrightarrow \textbf{循环}✓✓$$
$$\qquad ⚠️\ \text{正确的严格状态（档案逐字）}：\text{该区域}\ \textbf{只有平凡界}（M_B=5.81\times10^5=0.888\times\ \text{额度，本就闭合}）;\ \textbf{区域 A 才是墙}（M_A=1.42\times10^6=2.17\times,\ 2N_A=2.84\times10^6=4.34\times）✓$$

## §3 **Gate C（`n`-保持）**：✗

$$\text{若走显式公式，}n\ \text{进入}\ \textbf{检验函数的 Fourier 变换} \Longrightarrow \text{问题变为"对}\ n\ \textbf{一致} \text{的 Fourier 变换估计"} \Longrightarrow \textbf{与}\ UQRL\ \text{同型} \Longrightarrow \text{不解决}✓$$

## §4 **Gate D（一致性）**：✗

$$\text{decoupling 定理输出}＝\textbf{大值估计／}L^p\ \text{型} \Longrightarrow \text{本质}\ \textbf{平均型} \Longrightarrow \text{落}\ (\beta)\ \text{（}\int|E|^2\ \text{型，而需}\ \sup_n\text{）}✓$$

## §5 **Gate E（RH-free）**：⚠️ **部分**

$$\text{Bourgain 型 zeta decoupling：}\textbf{RH-free}✓\ \text{但}\ \textbf{对象错}（\zeta(1/2+it)\ \text{大值}\ \ne\ \text{零点序指数和}）✗$$
$$\text{Ivić 型零点序指数和线：}\text{已有渐近}\ \textbf{RH/GRH 依赖}✗ \Longrightarrow \text{循环风险}✓$$

## §6 **Gate F（强度）**：✗

$$\text{已有增益形式}＝\textbf{指数改进}（\text{如}\ \zeta(1/2+it)\ll t^{13/84+\varepsilon}\ \text{型}）\ \text{而非}\ \textbf{"}\to0\ \text{一致"}\Longrightarrow \textbf{定量不足}✓$$

## §7 判词与全局位置

$$\boxed{\textbf{(III)}\ \text{根本没有可用对象转换}}\quad（\text{附：曲率／横截性假设已实测失败}）✓✓$$
$$\textbf{四分支全关表}：$$
| 分支 | 判定 | 失配类型 |
|:--|:--|:--|
| `Burnol` | ✗ | (α) 参数（`λ→0` vs `n≲T₀²`）|
| `FINT` | ✗ | (α)＋(β)（框架型 `L²`）|
| `large sieve`（＋频率正则性）| ✗ | (β)（天然 `L²`）|
| **`decoupling`** | ✗ | **(A) 对象＋(B) 曲率假设实测失效** |
$$\Longrightarrow\ \boxed{UQRL：\textbf{仍开放}，\text{但四条候选技术族已}\textbf{全部审计并关闭}}✓✓$$
$$\qquad ⚠️\ \text{按纪律}\ \textbf{不得} \text{升级为"UQRL 不可解"}\ ✗;\ \text{可写}\ \text{"}\textbf{已知技术族穷尽} \text{"}✓$$

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 13:3x）`[纪律]`（先跑后写）

```
技术词 二阶导检验   命中文件数=7    :: ./NEGATIVE-RESULTS-2026-09-12-ROUND.md ./PAPERA-uniformity-attack.md ./C2-W6-UB-4-strict-Abel-attempt-rigorous-gap-named.md
技术词 曲率不足    命中文件数=0
技术词 对象失配    命中文件数=1    :: ./C89-FINT-1-fourier-interpolation-transferability-audit-two-mismatches.md
技术词 伪桥      命中文件数=0
```
**读数**：`曲率不足`／`伪桥`＝**0 档 ⟹ 本档新增** ✓；⚠️ `二阶导检验`＝**7 档 ⟹ 档案已有**（`PAPERA-uniformity-attack` 等）⟹ 引用 ✓；`对象失配`＝**1 档**（`C-89`）⟹ 沿用 ✓

## §9 边界

- `[逐字]` §2（`PAPERA-uniformity-attack` 首段／§4.1／`PAPERA-expsum` §4）✓；`[本档]` §1 三类排除、§2 的"同族推论"与"循环性"、§3–§6 各门判定、§7 表 ✓
- ⚠️ §2 的 vdC 常数档内自标"**常数待核**" ⟹ 引用时保留该标注 ✓
- **不声称**：UQRL 不可解 ✗；不声称"没有任何桥存在" ✗（仅"未见第四类 𝒯"）；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓；**零数值** ✓（引用的 999942/1001108 为**档案实测值**）

```
⚠️ 唐先生 13:35：执行 D3(b)-DEC-1（zero-ordinate exponential sum → curved exponential sum 桥接审计），六门 A–F，三分判定 (I)/(II)/(III)
✅ 判定 = **(III) 根本没有可用对象转换**；且附一条**更强的定量否定**：
   · Gate A ✗：三类已知转换全被排除（显式公式 / Fourier 反演 / Nyman–Beurling·Burnol 型 Hilbert 对偶）⟹ 未见第四类 𝒯；
     经 ζ 大值/Dirichlet 多项式大值中转者 = **伪桥**（中间是已有平均值不等式）⟹ 仍回 (β)
   · ⭐ Gate B ✗ **且在假设层面**（档案已实测并已自行撤回）：vdC 二阶导检验要求 λ ≤ |f''| ≤ αλ（**定号＋下有界**），
     而 φ_k = nθ(γ_k) 的二阶差分**符号 50/50 混合**（实测 正 999942/负 1001108，由符号随机 gap 跳变主导）
     ⟹ 标准检验/sup-form/run-split 均为误用；且 vdC 离散式 |Σe^{iφ_k}| ≤ M√Λ + Λ^{−1/2}, Λ = max|nΔ²θ_k| 形式套用亦配额不足
     ⭐ 推论：decoupling 与 vdC **同族**（均需曲率/横截非退化＋下有界）⟹ 定号失效 ⟹ decoupling 亦不能咬
     ⭐ 循环性：检验失败**恰由**零点间距不规则造成 ⟹ 要应用它须先有 gap 正则性 = 研究对象 ⟹ 循环
     ⚠️ 该区域严格状态只有平凡界（0.888× 额度，本就闭合）；区域 A 才是墙（2.17×/4.34×）
   · Gate C ✗：显式公式路线下 n 进入检验函数 Fourier 变换 ⟹ 同型一致性问题
   · Gate D ✗：decoupling 输出＝大值/L^p 型 ⟹ 平均型 ⟹ (β)
   · Gate E ⚠️：Bourgain 型 RH-free ✓ 但对象错；Ivić 型零点序指数和 RH/GRH 依赖 ✗
   · Gate F ✗：已有增益＝指数改进（t^{13/84} 型），非"→0 一致"
⭐ 四分支全关表：Burnol ✗(α) | FINT ✗(α)(β) | large sieve ✗(β) | decoupling ✗(A)(B) ⟹ **UQRL 仍开放，但四条候选技术族已全部审计并关闭**
   （纪律：不得升级为"UQRL 不可解"；可写"已知技术族穷尽"）
✅ 净产出：①六门逐条判定 ✓；②(β) 伪桥识别 ✓；③曲率假设实测失效＋同族推论＋循环性 ✓；④四分支全关表 ✓；⑤UQRL 状态（开放／技术族穷尽）✓
```
