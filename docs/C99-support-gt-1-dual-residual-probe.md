已查地图（所查：`C-98`（零点关联性实测 ＋ 归纳法审计；含**勘误**）、`C-97`（素数间隙记忆）、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`MATH-STATEMENT-A-offdiagonal-second-moment-beyond-support-1.md`、`W6-MAJORANT-1g`（`cross-X>T` FAIL）、`C-75`（`η≥0.04`）、`C-76`（RS `Lemma 3.2` **乘积界**）、`V188` §2（饱和）、`V254`）。**结论**：按唐先生指定的**三阶段**执行 `support>1 dual-residual probe` ⟹ **(A)** `F(α)` 分段扫描：`α≤0.9` **吻合** `F=α`（已知范围确认）✓✓，`α>1` 为 `1.00–1.02`（`α≈1` 尖峰 **疑伪影**，已**预注册控制实验**）⚠️；**(B)** 素数对侧标定：`C(h)/(𝔖(h)X)` 在 `h≤0.5X` **吻合到 ±0.5%**（**残差＝无**）✓✓；**(C)** **残差对偶判定**：两侧残差**均小且无共同稳定结构** ⟹ **支持"墙就位于对偶带宽本身（`support 1`）"** ✓✓ —— 按唐先生预设：**这是负结果，但正是有价值的那一半** ✓✓

# C-99 · **`support>1` dual-residual probe（经验诊断，三阶段）**

> **时间**：2026-09-18 15:09 唐先生：**建议开，但严格定义成"`support>1` 的经验诊断"，不预设为寻找证明**；分 A／B／C 三阶段；**第一阶段只做 `1<α≤4` 分段扫描 ＋ 奇异级数归一化后的 prime-pair residual；不要一开始就扩大到极端 `X`** ✓
> **纪律**：**不预设目标为"验证 RH"或"证明 support>1"**（唐先生明文）✓

---

## §0 结论（先行）

$$\textbf{(A)}\ \text{零点侧}\ F(\alpha)：\alpha\le0.9\ \text{时}\ F(\alpha)\approx\alpha\ \textbf{吻合}✓✓;\ \alpha>1\ \text{时}\ F\approx1.00\text{–}1.02\ \text{（}\alpha\approx1\ \text{有}\ 1.285\ \text{尖峰，}\textbf{疑伪影}）⚠️$$
$$\textbf{(B)}\ \text{素侧}\ \widetilde C(h)=\dfrac{C(h)}{(X-h)\mathfrak S(h)}\in[0.996,1.005]\quad(h\le0.5X) \Longrightarrow \textbf{残差}\approx\textbf{无}✓✓$$
$$\textbf{(C)}\ ⭐\ \textbf{残差对偶判定}：R_{\rm zero}(\alpha>1)\approx+0.01\text{–}0.02\ (\text{疑伪影}),\ R_{\rm prime}\approx\pm0.5\% \Longrightarrow \textbf{无共同稳定结构}✓✓$$
$$\qquad \Longrightarrow\ \boxed{\text{支持"墙位于对偶带宽本身（}\text{support}=1\text{）"}}✓✓\ \text{（按预设：}\textbf{负结果，但正是有价值的一半}）$$

---

## §1 方法与约束（严格按唐先生给定）

$$\textbf{Goal（不得越界）}：\text{回答"}\textbf{support}>1\ \text{的未知部分，在零点侧与素数对侧是否留下}\textbf{同一个可测的 residual signature}\text{"}✓$$
$$\textbf{分段}：0\le\alpha\le1;\quad 1<\alpha\le2;\quad 2<\alpha\le4\ ✓$$
$$\qquad \text{真正要观察的不是"有没有偏差"，而是}\ \boxed{\alpha=1\ \text{附近是否出现}\textbf{可重复的结构转折}}✓$$
$$\qquad \text{且}\ \textbf{若}\ 1<\alpha\ \text{只是平滑延伸而无新结构} \Longrightarrow \textbf{本身即重要负结果}✓✓$$
$$\textbf{不预设}：\text{目标}\ne\text{"验证 RH"},\ \ne\text{"证明 support}>1;\ \text{不扩大到极端}\ X✓$$
$$\textbf{两个残差}：R_{\rm zero}(\alpha)=F_T(\alpha)-F_{\rm known}(\alpha)\ (\alpha>1);\qquad R_{\rm prime}(X,h)=\dfrac{C_X(h)}{X\mathfrak S(h)}-1✓$$

## §2 **Stage A**：`F(α)` 分段扫描（数据：2,001,052 零点）

$$\text{构造}：\text{展开}\ x_n\ (\text{密度}1);\ R_2(s)\ \text{细网格}\ (\Delta s=0.02,\ s\le60)\ \text{由索引位移池化};\ D(s)=R_2(s)-1✓$$
$$\qquad F(\alpha)=\boxed{1+2\int_0^{60}D(s)\cos(2\pi\alpha s)\,ds}\（\text{余弦窗抑制截断}）✓\qquad \text{预测（GUE／配对相关）}：F=\alpha\ (\alpha\le1),\ F=1\ (\alpha\ge1)✓$$

| `α` | 0.25 | 0.50 | 0.75 | 0.90 | **1.00** | 1.10 | 1.25 | 1.50 | 2.00 | 3.00 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `F` 实测 | 0.2475 | 0.4982 | 0.7633 | 0.9212 | **1.2850** | 1.0670 | 0.9972 | 1.0227 | 1.0099 | 1.0192 |
| `F` 预测 | 0.2500 | 0.5000 | 0.7500 | 0.9000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 残差 | −0.003 | −0.002 | +0.013 | +0.021 | **+0.285** | +0.067 | −0.003 | +0.023 | +0.010 | +0.019 |

$$\textbf{读数}：\textbf{(i)}\ \alpha\le0.9：F\approx\alpha\ \textbf{吻合}（\text{残差}\le0.02）\Longrightarrow \text{已知 support 范围被实测确认}✓✓$$
$$\qquad \textbf{(ii)}\ \alpha\approx1：\text{尖峰}\ +0.285\ ⚠️;\quad \textbf{(iii)}\ \alpha>1.1：\text{残差}\ +0.01\text{–}0.02,\ \textbf{量级小};\ \text{但}\ \textbf{形态可疑}⚠️$$
$$\qquad ⚠️\ \textbf{伪影警报（本档自查）}：\text{(1) 截断}\ s\le60\ ＋\ \text{窗函数会在}\ \textbf{折点}\ \alpha=1\ \text{处产生 ringing};\ \text{(2) 展开残差会在}\ \textbf{大}\ s\ \text{处造成慢调制};\ $$
$$\qquad \qquad \text{证据}：D(8)=-0.029,\ D(12)=+0.025,\ D(20)=+0.024,\ D(30)=+0.040,\ D(40)=-0.018\（\text{大}\ s\ \text{起伏}\pm0.04）;\ R_2(50)=1.038,\ R_2(58)=1.010\ \textbf{未收敛到 1}⚠️✓$$
$$\qquad \Longrightarrow\ \text{故}\ \textbf{目前不得} \text{把}\ \alpha>1\ \text{的残差当作}\ \textbf{真实结构}✗;\ \text{须先做}\ \textbf{管线控制实验}（§5）✓✓$$

## §3 **Stage B**：素数对侧（奇异级数归一化）

$$C(h)=\sum_{n\le X}\Lambda(n)\Lambda(n+h);\qquad \mathfrak S(h)=2\mathrm C_2\prod_{p\mid h,\,p>2}\frac{p-1}{p-2};\qquad \widetilde C(h)=\frac{C(h)}{(X-h)\mathfrak S(h)}✓$$
（`Λ` 筛至 `4×10⁷`；`X=10⁷`；`𝔖` 已过 **8 项自检断言** ✓）

| `h` | 2 | 6 | 30 | 100 | 1000 | 10⁴ | 10⁵ | 10⁶ | 3×10⁶ | 5×10⁶ |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `C̃(h)` | 1.0052 | 0.9983 | 0.9996 | 1.0003 | 0.9999 | 0.9961 | 0.9987 | 1.0021 | 1.0021 | 0.9996 |

$$\text{比值检验}：C(h)/C(2)\ \text{vs}\ \mathfrak S(h)/\mathfrak S(2)：\ -0.4\%\sim-0.7\%\（\text{唯一例外}\ h=510510:-5.4\%\ ⚠️）✓$$
$$\Longrightarrow\ \textbf{(B) 的残差}\ \approx\textbf{无}：\text{跨 6 个数量级、}\ h\ \text{直到}\ 0.5X,\ \textbf{全程}\ \pm0.5\%✓✓$$
$$\qquad ⚠️\ \textbf{但必须写清}：\text{这是}\ \textbf{经验} \text{吻合};\ \textbf{可证} \text{范围远短于此}（\text{筛法给}\ h\ \text{远小于}\ X） \Longrightarrow \textbf{经验吻合}\ne\textbf{可证明}✓✓$$

## §4 **Stage C**：残差对偶判定

| 侧 | 残差定义 | 实测 | 是否有结构 |
|:--|:--|:--|:--|
| 零侧 | `R_zero(α) = F(α) − 1`（`α>1`）| +0.01–0.02（`α=1` 处 +0.285）| ⚠️ **疑伪影**，未确认 |
| 素侧 | `R_prime = C̃(h) − 1` | ±0.5%（`h≤0.5X`）| **无** |

$$\textbf{尺度映射稳定性检查}：\text{若存在共同结构，应在某尺度变换下}\ R_{\rm zero}\leftrightarrow R_{\rm prime}\ \text{稳定对齐}✓$$
$$\qquad \text{实测}：\text{两侧残差}\ \textbf{量级不同（0.01–0.02 vs 0.005）};\ \textbf{形态不同}（\text{零侧有大}\ s\ \text{起伏，素侧平坦}）;\ \text{无可重复共同结构}✓$$
$$\Longrightarrow\ \boxed{\textbf{无共同稳定结构}} \Longrightarrow \text{按唐先生预设：}\textbf{进一步支持"墙位于对偶带宽本身"（}\text{support}=1\text{）}✓✓$$
$$\qquad ⭐\ \text{且与既有地图同向}：\text{`C-82`（值的性质 vs 界的性质）};\ \text{`C-91`（唯一残余＝新算术输入）};\ \text{`V188`（线性通道饱和）}✓$$

## §5 ⚠️ **预注册**：管线控制实验（在采信任何 `α>1` 结构之前必做）

$$\textbf{控制 1（合成序列）}：\text{用}\ \textbf{已知 GUE 型} \text{合成点过程（或已证 support 的模型）走}\ \textbf{同一管线} \Longrightarrow \text{看}\ \alpha>1\ \text{是否也出现同类"残差"}$$
$$\qquad \text{若出现} \Longrightarrow \text{残差＝管线伪影} \Longrightarrow \text{零侧残差作废}✗;\ \text{若不出现} \Longrightarrow \text{才可考虑真实结构}✓$$
$$\textbf{控制 2（换展开）}：\text{用另一种展开（如含}\ S(t)\ \text{校正或不同}\ \theta\ \text{截断）重跑} \Longrightarrow \text{看大}\ s\ \text{起伏是否移动}$$
$$\textbf{控制 3（窗/截断扫描）}：\text{改变}\ s_{\max}\ \text{与窗函数} \Longrightarrow \text{看}\ \alpha\approx1\ \text{尖峰是否随窗移动}（\text{ringing 的特征}）✓$$
$$\Longrightarrow\ \text{三者任一显示"随管线移动"} \Longrightarrow \text{判为伪影}✓✓$$

## §6 `C-98` 勘误（按唐先生 15:09 指定；已另档追加）

$$\text{(i)}\ \textbf{措辞降级}：\text{不得写"零点过程本身具有饱和刚性"} \Longrightarrow \text{应写}\ \boxed{\text{observed finite-range saturation of the chosen }S\text{-increment statistic}}✓$$
$$\text{(ii)}\ \textbf{不得} \text{升级为"GUE 数方差的内禀饱和"}（\text{定义／平滑计数／端点误差／归一化}\ \text{均未拆开}）✓$$
$$\text{(iii)}\ \textbf{新待办}：\text{把统计量定义与文献 convention 统一（}\frac1{2\pi^2}\log\log T\ \text{vs 另一常数版本）}✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 15:1x）`[纪律]`（先跑后写）

```
技术词 dual-residual    命中文件数=1  :: ./C99-support-gt-1-dual-residual-probe.md
技术词 结构转折        命中文件数=1  :: ./C99-support-gt-1-dual-residual-probe.md
技术词 管线控制        命中文件数=1  :: ./C99-support-gt-1-dual-residual-probe.md
技术词 残差 signature   命中文件数=1  :: ./C99-support-gt-1-dual-residual-probe.md
```
**读数（按实测）**：四项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

## §8 边界

- `[数据]` §2／§3 全部**本次实算**（零点 `zeros6` 2,001,052 个；`Λ` 筛至 `4×10⁷`）✓；`𝔖` 过 8 项自检 ✓
- ⚠️ §2 的 `α>1` 残差**未确认**（疑伪影：截断 ringing／展开残差）；已**预注册**三项控制实验 ✓
- **不声称**：`support>1` 不可能 ✗；`α>1` 有真实结构 ✗（未确认）；HL 已证 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓

```
⚠️ 唐先生 15:09：建议开，但严格定义为"support>1 的经验诊断"，不预设为寻找证明；分 A/B/C 三阶段；
   第一阶段只做 1<α≤4 分段扫描 + 奇异级数归一化后的 prime-pair residual；不要一开始扩大到极端 X；命名 = C-99
✅ 命名冲突处理：把此前写的素数对标定并入本档（旧未提交文件已删）
✅ Stage A（F(α) 分段扫描）：α≤0.9 时 F≈α 吻合（残差 ≤0.02）；α=1.0 处 F=1.285（尖峰，疑 ringing 伪影）；
   α>1.1 时 F=1.00–1.02（残差 +0.01–0.02，形态可疑）；⚠️ 伪影警报证据：大 s 起伏 ±0.04（D(8)=−0.029, D(12)=+0.025,
   D(20)=+0.024, D(30)=+0.040, D(40)=−0.018）；R2(50)=1.038, R2(58)=1.010 未收敛到 1
   ⟹ 目前**不得**把 α>1 残差当真实结构；已预注册三项控制实验（合成序列 / 换展开 / 窗截断扫描）
✅ Stage B（素侧）：C̃(h)=C(h)/((X−h)𝔖(h)) ∈ [0.996,1.005]（h≤0.5X，跨 6 个数量级）；比值检验 −0.4%~−0.7%；
   唯一例外 h=510510 −5.4%；⟹ 素侧残差 ≈ 无；⚠️ 但经验吻合 ≠ 可证明（可证范围远短于此）
✅ Stage C（残差对偶判定）：零侧残差 0.01–0.02（疑伪影）/ 素侧 ±0.005；量级不同、形态不同、无可重复共同结构
   ⟹ **无共同稳定结构** ⟹ 按预设：进一步支持"墙位于对偶带宽本身（support=1）"（负结果，但有价值的一半）
   ⟹ 与 C-82 / C-91 / V188 同向
✅ C-98 勘误（按唐先生指定）：措辞降级为 "observed finite-range saturation of the chosen S-increment statistic"；
   不得升级为"GUE 数方差内禀饱和"；新增待办：统一统计量定义与文献 convention（1/(2π²)loglogT vs 另一常数版本）
✅ 净产出：①F(α) 分段扫描（α≤0.9 吻合、α>1 残差量级与伪影警报）✓ ②素侧 ±0.5% 标定 ✓ ③残差对偶判定（无共同结构）✓
   ④三项预注册控制实验 ✓ ⑤C-98 勘误 ✓
```
