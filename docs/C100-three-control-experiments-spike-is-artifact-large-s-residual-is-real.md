已查地图（所查：`C-99`（`dual-residual probe` 三阶段，含**预注册三项控制**）、`C-98`（含勘误）、`C-97`、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`V188` §2–§3）。**结论**：三项控制跑完 ⟹ **`α≈1` 尖峰与 `α>1` 残差＝截断 ringing 伪影**（`F(1.0)` 随 `s_max` 单调增长 `1.18→1.60→2.25`）⟹ **撤回** ✓✓；**Poisson 对照**：管线**不制造结构** ✓；**分段展开对照**：大 `s` 起伏（`±0.03`）**不受展开影响** ⟹ **该项残差是真的**（可信的新登记项）✓✓；**合成 GUE 控制无效**（第 6 处实现问题，已标）⚠️ ⟹ **净结论：Stage A 无"超越 support 1"的证据**，与 Stage B／C 一致支持**"墙位于对偶带宽本身"** ✓✓

# C-100 · **`support>1` 残差诊断：三项控制实验（结论：尖峰为伪影；大 `s` 残差为真）**

> **时间**：2026-09-18 15:13 唐先生「继续」⟹ 执行 `C-99` §5 **预注册**的三项控制
> **纪律**：控制实验**跑在采信之前** ✓；结果与预期相反时**照实登记**（不修饰）✓

---

## §0 结论（先行）

$$\textbf{(1)}\ ⭐\ \textbf{尖峰＝伪影（撤回）}：F(1.0)\ \text{随}\ s_{\max}\ \textbf{单调增长}：\ 1.18\ (30)\to1.60\ (60)\to2.25\ (120)\ \text{（无窗）}✓✓$$
$$\qquad \Longrightarrow\ \boxed{\alpha\approx1\ \text{尖峰}＋\alpha>1\ \text{残差}\ \textbf{均为截断 ringing 伪影}} \Longrightarrow \textbf{撤回}✓✓$$
$$\textbf{(2)}\ \text{Poisson 对照}：F\approx1.00\ \text{全平}（0.993\text{–}1.001） \Longrightarrow \textbf{管线不制造结构}✓✓$$
$$\textbf{(3)}\ ⭐\ \text{分段展开对照}：\text{大}\ s\ \text{起伏}\ \textbf{几乎不变} \Longrightarrow \text{该起伏}\ \textbf{非展开伪影} \Longrightarrow \textbf{真实残差（新登记）}✓✓$$
$$\textbf{(4)}\ ⚠️\ \text{合成 GUE 控制}\ \textbf{无效}（\text{间距方差}\ 0.00037\ \text{vs}\ 0.1781） \Longrightarrow \text{第 6 处实现问题};\ \textbf{不作证据}✓$$
$$\Longrightarrow\ \textbf{净结论}：\text{Stage A}\ \textbf{无"超越 support 1"的证据} \Longrightarrow \text{与 Stage B／C 一致支持}\ \boxed{\text{墙位于对偶带宽本身}}✓✓$$

---

## §1 控制 (a)：**Poisson 对照**（管线自检）

$$\text{构造}：\text{同}\ N、\text{同密度}（\text{指数间隔}）\ \text{的 Poisson 过程} \Longrightarrow \text{走}\ \textbf{同一}\ R_2\to F(\alpha)\ \text{管线}✓$$
| `α` | 0.25 | 0.5 | 0.9 | 1.0 | 1.5 |
|:--|--:|--:|--:|--:|--:|
| `F`（Poisson）| 0.9933 | 1.0010 | 0.9938 | 1.0014 | 0.9979 |

$$\Longrightarrow\ \textbf{全平}（\text{无三角、无尖峰}） \Longrightarrow \textbf{管线干净}✓✓\ \text{故真实零点的}\ F=\alpha\（\alpha\le1）\ \textbf{是真结构}✓$$
$$\qquad ⚠️\ \text{同时说明}：\alpha\approx1\ \text{尖峰}\ \textbf{不是"管线从零制造"}，\text{而是}\ \textbf{截断与真结构的相互作用}（\text{见 §2}）✓$$

## §2 ⭐ 控制 (b)：**窗／截断扫描**（决定性）

| `s_max` | 窗 | `F(0.9)` | **`F(1.0)`** | `F(1.1)` |
|--:|:--|--:|--:|--:|
| 30 | 无 | 0.8951 | **1.1801** | 1.1663 |
| 30 | `cos²` | 0.8955 | **1.0503** | 1.1794 |
| 60 | 无 | 0.9216 | **1.6025** | 1.1876 |
| 60 | `cos²` | 0.9212 | **1.2850** | 1.0670 |
| 120 | 无 | 0.9105 | **2.2512** | 1.1350 |
| 120 | `cos²` | 0.9429 | **1.3952** | 1.1418 |

$$\textbf{判据（预注册）}：\text{若随窗移动} \Longrightarrow \textbf{ringing 伪影}✓$$
$$\qquad \textbf{实测}：F(1.0)\ \text{随}\ s_{\max}\ \textbf{单调放大}（1.18\to1.60\to2.25） \Longrightarrow \boxed{\textbf{伪影确认}}✓✓$$
$$\qquad \qquad \text{而}\ F(0.9)\（0.895\text{–}0.943）\ \textbf{稳} \Longrightarrow \text{已知范围的}\ F=\alpha\ \textbf{仍可信}✓✓$$
$$\qquad \qquad ⚠️\ F(1.1)\ \text{亦随窗变}（1.05\text{–}1.19） \Longrightarrow \textbf{`α>1` 残差同样不可信}✓$$

## §3 ⭐ 控制 (c)：**分段展开对照**

$$\text{构造}：\text{每}\ 2000\ \text{个零点一段、段内独立归一化密度} \Longrightarrow \text{消除全局展开误差}✓$$
| `s` | 8 | 20 | 30 | 40 | 55 |
|:--|--:|--:|--:|--:|--:|
| `D(s)` 原始 | −0.02901 | +0.02374 | +0.03980 | −0.01829 | +0.00857 |
| `D(s)` 分段展开 | −0.03048 | +0.02374 | +0.04315 | −0.02149 | +0.00412 |

$$\Longrightarrow\ \textbf{起伏位置与量级}\ \textbf{不变} \Longrightarrow \boxed{\text{大}\ s\ \text{残差}\ (\pm0.03,\ s\gtrsim8)\ \textbf{是真的}}✓✓$$
$$\qquad \text{且}\ F(0.5)\ \text{几乎不变}（0.4982\to0.4984）;\ F(1.0)\ \text{基本不变}（1.2850\to1.2727）✓$$
$$\qquad ⚠️\ \textbf{但}：\text{该残差}\ \textbf{无法} \text{用本方法分解成}\ \alpha>1\ \text{结构}（\text{因}\ \alpha>1\ \text{分量被截断伪影污染}） \Longrightarrow \textbf{预注册更精细方法}（\S5）✓$$

## §4 ⚠️ 控制 (d)：**合成 GUE 控制无效**（第 6 处实现问题）

$$\text{构造}：\text{Dumitriu--Edelman 三对角}\ \beta=2,\ N=20000✓$$
$$\qquad ⚠️\ \textbf{实测}：\text{间距方差}=0.00037（\text{应}\ 0.1781）;\ F(0.25)=0.4101\ \text{vs}\ 0.25 \Longrightarrow \textbf{构造与展开的尺度常数不一致}✗$$
$$\Longrightarrow\ \textbf{处置}：\text{该控制}\ \textbf{无效}，\textbf{不作证据};\ \text{修正需}\ \textbf{统一三对角常数与半圆展开尺度} \Longrightarrow \text{列为可选后续}✓$$
$$\qquad ⚠️\ \text{（本会话第 6 处实现问题};\ \text{与前 5 处同一教训}：\textbf{结果异常先怀疑自己的实现}）✓✓$$

## §5 综合判词与预注册

$$\textbf{(i)}\ \text{Stage A 的"}\alpha>1\ \text{结构"}\ \textbf{撤回};\ \text{已知范围}\（\alpha\le1）\ \text{的}\ F=\alpha\ \textbf{确认}✓✓$$
$$\textbf{(ii)}\ \text{素侧残差}\approx\text{无}\（\pm0.5\%）;\ \text{零侧可信残差}= \text{大}\ s\ \text{的}\ R_2\ \text{起伏}\（\pm0.03）✓$$
$$\qquad \Longrightarrow\ \text{两侧}\ \textbf{量级不同、形态不同} \Longrightarrow \textbf{无共同稳定结构} \Longrightarrow \textbf{支持"墙在对偶带宽本身"}✓✓$$
$$\textbf{(iii)}\ \text{预注册（更精细的零侧方法）}：\text{用}\ \textbf{显式窗函数} \text{的成熟做法}（\text{而非余弦截断}）\ \text{把}\ F(\alpha)\ \text{算到}\ \alpha\le4;$$
$$\qquad \qquad \text{或直接对}\ \textbf{未截断} \text{的}\ R_2(s)\ \text{做}\ \textbf{解析拟合}（\text{GUE 曲线＋慢变包络}），\ \text{分离"真实慢变分量"}✓$$
$$\textbf{(iv)}\ \text{可选}：\text{修好合成 GUE 控制（统一尺度）以取得独立基准}✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 15:1x）`[纪律]`（先跑后写）

```
技术词 窗截断扫描  命中文件数=2  :: ./C100-three-control-experiments-spike-is-artifact-large-s-residual-is-real.md ./C99-support-gt-1-dual-residual-probe.md
技术词 伪影确认    命中文件数=1  :: ./C100-three-control-experiments-spike-is-artifact-large-s-residual-is-real.md
技术词 管线自检    命中文件数=1  :: ./C100-three-control-experiments-spike-is-artifact-large-s-residual-is-real.md
```
**读数（按实测）**：`伪影确认`／`管线自检`＝**1 档（仅本档）⟹ 本档新增** ✓；`窗截断扫描`＝**2 档**（`C-89`… 实为 `C-99` 同档）⟹ 沿用 ✓

## §7 边界

- `[数据]` §1–§4 全部**本次实算**（真实零点 `zeros6` 2,001,052 个；Poisson 对照同 `N`；GUE 合成 `N=20000`）✓
- ⚠️ §4 的合成 GUE 控制**无效**（尺度不一致）；已列修正为可选后续 ✓
- **不声称**：`α>1` 有任何真实结构 ✗（**已撤回**）；`support>1` 不可能 ✗；不证 RH ✗
- **纪律**：控制实验**先跑后判** ✓；**未用 RH 作推导** ✓

```
⚠️ 唐先生 15:13「继续」⟹ 执行 C-99 §5 预注册的三项控制
✅ (a) Poisson 对照: F≈1.00 全平(0.993–1.001) ⟹ 管线不制造结构 ⟹ 真实零点的 F=α(α≤1) 是真结构
✅ (b) 窗/截断扫描（决定性）: F(1.0) 随 s_max 单调放大 —— 30: 1.18(无窗)/1.05(cos²); 60: 1.60/1.285; 120: 2.25/1.395
   ⟹ **尖峰＝ringing 伪影确认** ⟹ 撤回; 而 F(0.9) 稳(0.895–0.943) ⟹ 已知范围的 F=α 仍可信;
   ⚠️ F(1.1) 亦随窗变(1.05–1.19) ⟹ α>1 残差同样不可信
✅ (c) 分段展开对照: 大 s 起伏几乎不变(s=8: −0.029→−0.030; s=20: +0.0237→+0.0237; s=30: +0.040→+0.043)
   ⟹ **±0.03 的大 s 残差是真的**（非展开伪影）; F(0.5) 0.4982→0.4984 基本不变
   ⚠️ 但该残差无法用本方法分解成 α>1 结构（被截断伪影污染）
⚠️ (d) 合成 GUE 控制**无效**: Dumitriu–Edelman 三对角 β=2 (N=20000) 间距方差 0.00037（应 0.1781）⟹ 构造与展开尺度常数不一致
   ⟹ 不作证据; 第 6 处实现问题; 修正列为可选后续
⭐ 综合判词: Stage A 的 α>1 结构**撤回**; 已知范围确认; 素侧残差≈无; 零侧可信残差=大 s 的 R₂ 起伏(±0.03)
   ⟹ 两侧量级/形态不同 ⟹ 无共同稳定结构 ⟹ **支持"墙位于对偶带宽本身"**
✅ 预注册更精细方法: 用成熟显式窗函数把 F(α) 算到 α≤4；或对未截断 R₂(s) 做解析拟合分离慢变分量
✅ 净产出: ①尖峰伪影确认并撤回 ✓ ②管线自检通过 ✓ ③大 s 残差判为真实（新登记）✓ ④第 6 处实现问题记录 ✓ ⑤更精细方法预注册 ✓
```
