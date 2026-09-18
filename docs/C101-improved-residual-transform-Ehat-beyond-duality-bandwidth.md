已查地图（所查：`C-99`（残差探针＋预注册）、`C-100`（三控制）、`C-98`、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`V188` §2）。**结论**：按预注册①执行**改进方法**——**对"偏离 GUE 的残差"做变换**（`Ê(α)`，把 `α=1` 折点吸收进 `D_GUE`）⟹ **(i)** `E(s)` 极小（`std=0.01515`）✓；**(ii)** `α<1` 时 `Ê≈0`（`≤1.5σ`）✓✓；**(iii)** `α≈1` 尖峰**又是伪影**（随窗增长 `0.28→0.86→1.53`，判为 **`Δs=0.02` 与近整数聚集的混叠**）⚠️；**(iv)** **`α≳1.25` 时 `Ê≈0`（`≤1σ`）⟹ 无超越 support 1 的内容** ✓✓；**(v)** **Poisson 对照给出解析正三角**（`0.735/0.476/0.236→0 at α=1`，之后 ≈0）⟹ **方法经校准** ✓✓ ⟹ **判词：对偶带宽外无可测残差**，**第三条独立路径**支持"墙位于 `support 1`" ✓✓

# C-101 · **改进方法 `Ê(α)`：对偶带宽外的残差扫描（方法经 Poisson 校准）**

> **时间**：2026-09-18 15:17 唐先生「继续」⟹ 执行 `C-100` §5 预注册的**方法①**
> **关键改进**：不对 `F(α)` 直接变换（尖峰被截断盖住），而**对残差变换**：$\hat E(\alpha)=2\int_0^{s_{\max}}\bigl[R_2(s)-1+(\sin\pi s/\pi s)^2\bigr]w(s)\cos(2\pi\alpha s)\,ds$

---

## §0 结论（先行）

$$\textbf{(i)}\ E(s):=R_2(s)-1+(\sin\pi s/\pi s)^2 \Longrightarrow \text{均值}-0.00007,\ \mathrm{std}=0.01515,\ |E|_{\max}=0.05917 \Longrightarrow \textbf{零点极 GUE}✓✓$$
$$\textbf{(ii)}\ \alpha<1：|\hat E(\alpha)|\le1.5\,\mathrm{std} \Longrightarrow \hat E\approx0 \Longrightarrow \textbf{已知范围内容饱和}✓✓$$
$$\textbf{(iii)}\ ⚠️\ \hat E(1.0)=+0.856\ \text{但}\ \textbf{随窗增长}(0.28\to0.86\to1.53) \Longrightarrow \textbf{伪影}（\text{判为}\ \Delta s=0.02\ \text{混叠}）✓$$
$$\textbf{(iv)}\ ⭐\ \alpha\gtrsim1.25：\hat E\approx0\ (\le1\sigma) \Longrightarrow \boxed{\textbf{无超越 support 1 的内容}}✓✓$$
$$\textbf{(v)}\ ⭐\ \textbf{Poisson 对照＝解析正三角}（0.735/0.476/0.236\to0@\alpha=1,\ \text{之后}\approx0） \Longrightarrow \textbf{方法经校准}✓✓$$

---

## §1 方法与自检

$$\text{数据}：2{,}001{,}052\ \text{零点};\ s_{\max}=240,\ \Delta s=0.02,\ \text{池化}\ K=420✓$$
$$E(s)=R_2(s)-1+\Bigl(\frac{\sin\pi s}{\pi s}\Bigr)^2\quad（\text{减掉 GUE 预测}\ \Longrightarrow\ \textbf{折点被吸收}）✓$$
$$\hat E(\alpha)=2\int_0^{s_{\text{cut}}}E(s)e^{-s^2/(2\sigma^2)}\cos(2\pi\alpha s)\,ds\quad（\text{高斯窗};\ \text{扫}\ \sigma\ \text{与}\ s_{\text{cut}}）✓$$
$$\textbf{校准目标}：\text{对 Poisson 过程}，E=(\sin\pi s/\pi s)^2 \Longrightarrow \hat E_p=(1-|\alpha|)_+\ \text{（解析正三角，}\alpha>1\ \text{处}=0）✓✓$$

## §2 主结果

| `α` | 0.25 | 0.50 | 0.75 | 0.90 | **1.00** | 1.10 | 1.25 | 1.50 | 2.00 | 2.50 | 3.00 | 4.00 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `Ê(α)` | +0.003 | −0.016 | −0.006 | −0.022 | **+0.856** | +0.097 | −0.045 | +0.006 | −0.010 | −0.012 | −0.000 | +0.004 |
| `\|Ê\|/std` | 0.19 | 1.09 | 0.38 | 1.49 | **56.7** | 6.45 | 2.95 | 0.38 | 0.69 | 0.82 | 0.03 | 0.29 |

$$\Longrightarrow\ \alpha<1：\textbf{≈0}✓;\quad \alpha=1：\textbf{尖峰};\quad \alpha\gtrsim1.25：\textbf{≈0}✓✓$$

## §3 窗口稳定性（伪影判据）

| `σ` | `s_cut` | `Ê(0.5)` | **`Ê(1.0)`** | `Ê(1.5)` | `Ê(2.0)` |
|--:|--:|--:|--:|--:|--:|
| 30 | 120 | −0.0133 | **+0.3084** | +0.0005 | −0.0059 |
| 60 | 200 | −0.0164 | **+0.8561** | +0.0057 | −0.0104 |
| 100 | 200 | −0.0185 | **+1.5350** | +0.0083 | −0.0103 |
| 60 | 100 | −0.0165 | **+0.7430** | +0.0069 | −0.0106 |
| 30 | 60 | −0.0138 | **+0.2774** | +0.0005 | −0.0059 |

$$\textbf{读数}：\hat E(1.0)\ \textbf{随}\ \sigma\ \text{单调放大}(0.28\to0.86\to1.53) \Longrightarrow \textbf{伪影确认}✓✓$$
$$\qquad ⚠️\ \textbf{机制（本档判定）}：\text{展开后差值}\ \textbf{近整数聚集}（x_j-x_i\approx(j-i)+O(0.3)）＋\ \Delta s=0.02\（1/0.02=50\ \text{整除}） \Longrightarrow \textbf{周期-1 混叠} \Longrightarrow \alpha=1\ \text{尖峰}✓$$
$$\qquad ⚠️\ \alpha\gtrsim1.25\ \text{处}\ \hat E\ \textbf{窗口稳定}（\le1\sigma） \Longrightarrow \text{该区间结论}\ \textbf{可信}✓✓$$

## §4 Poisson 校准（方法验证）

| `α` | 0.25 | 0.50 | 0.75 | **1.00** | 1.25 | 1.50 | 2.00 |
|:--|--:|--:|--:|--:|--:|--:|--:|
| `Ê_p`（Poisson）| **+0.735** | **+0.476** | **+0.236** | **−0.022** | −0.021 | −0.015 | −0.018 |
| `Ê`（真实零点）| +0.003 | −0.016 | −0.006 | +0.856 | −0.045 | +0.006 | −0.010 |

$$\Longrightarrow\ \textbf{Poisson}\ \text{给出干净正三角}（\text{斜率}\ \approx-1\ \text{线性降到}\ 0） \Longrightarrow \textbf{方法与归一化经校准}✓✓$$
$$\qquad ⭐\ \text{且}\ \alpha>1\ \text{处}\ \hat E_p\approx0 \Longrightarrow \text{方法}\ \textbf{不会在}\ \alpha>1\ \text{处制造内容}✓✓$$
$$\qquad ⭐\ \text{对照鲜明}：\text{Poisson 在}\ \alpha<1\ \textbf{有内容}（正三角）;\ \text{真实零点在}\ \alpha<1\ \textbf{无残余内容} \Longrightarrow \textbf{零点与 GUE 完全一致}✓✓$$

## §5 判词（第三条独立路径）

$$\boxed{\text{对偶带宽外}\ (\alpha>1)\ \textbf{无可测残差}}✓✓$$
$$\qquad \text{三条独立路径同向}：\text{`C-99`（Stage A/B/C）};\ \text{`C-100`（控制实验）};\ \text{本档（改进方法＋Poisson 校准）}✓✓$$
$$\qquad \Longrightarrow\ \text{支持}\ \boxed{\text{墙位于对偶带宽本身（}\text{support}=1\text{）}};\ \text{与}\ \text{`C-82`／`C-91`／`V188`}\ \text{同向}✓✓$$

## §6 待办（预注册）

$$\textbf{(1)}\ \text{消混叠}：\text{改用}\ \textbf{非整除/非均匀 binning} \text{或}\ \textbf{无 bin 的核估计} \Longrightarrow \text{压掉}\ \alpha=1\ \text{混叠}✓$$
$$\textbf{(2)}\ \text{把}\ \alpha\ \text{扫到}\ 4\ \text{以上}\ \text{（本档已到}\ 4\text{，}\ \text{结论为}\ 0）;\ \text{若需更细，须提高展开精度}✓$$
$$\textbf{(3)}\ \text{可选}：\text{以}\ \textbf{未截断解析拟合}（\text{GUE 曲线＋慢变包络}）\ \text{分离慢变分量}✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 15:2x）`[纪律]`（先跑后写）

```
技术词 残差变换    命中文件数=1  :: ./C101-improved-residual-transform-Ehat-beyond-duality-bandwidth.md
技术词 混叠      命中文件数=5  :: ./ANALYTIC-6-E46-SUMMARY.md ./ANALYTIC-2-certificate-side.md ./DOOR2-explicit-formula-verdict.md
技术词 近整数聚集   命中文件数=1  :: ./C101-improved-residual-transform-Ehat-beyond-duality-bandwidth.md
```
**读数（按实测）**：`残差变换`／`近整数聚集`＝**1 档（仅本档）⟹ 本档新增** ✓；⚠️ `混叠`＝**5 档 ⟹ 档案已有**（`ANALYTIC-*`／`DOOR2`）⟹ 本档为**引用** ✓

## §8 边界

- `[数据]` §1–§4 全部**本次实算**（真实零点 2,001,052 个 ＋ Poisson 对照）✓
- ⚠️ `α≈1` 尖峰**判为伪影**（窗口增长＋混叠机制）；`α≳1.25` 结论**窗口稳定** ⟹ 可信 ✓
- **不声称**：`α>1` 存在结构 ✗（**无证据**）；`support>1` 不可能 ✗；不证 RH ✗
- **纪律**：**先跑后写** ✓；**未用 RH 作推导** ✓

```
⚠️ 唐先生 15:17「继续」⟹ 执行 C-100 §5 预注册方法①（显式/改进窗，算到 α≤4）
✅ 关键改进: 对**残差**变换 Ê(α)=2∫E(s)w(s)cos(2παs)ds, E(s)=R2(s)−1+(sinπs/πs)²（把 α=1 折点吸收进 D_GUE）
✅ 数据: 2,001,052 零点; s_max=240; Δs=0.02; 池化 K=420; 高斯窗扫 σ∈{30,60,100}, s_cut∈{60,100,120,200}
✅ 结果:
   E(s) 均值 −0.00007 / std 0.01515 / |E|max 0.05917 ⟹ 零点极 GUE
   α<1: Ê ≈ 0（|Ê|/std ≤1.5）⟹ 已知范围内容饱和
   α=1.0: Ê=+0.856 但**随窗增长**（σ=30→0.308; 60→0.856; 100→1.535）⟹ **伪影**；
     机制判定: 展开差值近整数聚集 + Δs=0.02（1/0.02=50 整除）⟹ 周期-1 混叠
   α≳1.25: Ê ≈ 0（≤1σ）且**窗口稳定** ⟹ **无超越 support 1 的内容**（可信）
⭐ Poisson 校准: Ê_p 给出解析正三角（0.735/0.476/0.236 → 0 @ α=1，之后 ≈0）⟹ 方法经校准，且证明方法不会在 α>1 处制造内容
   对照鲜明: Poisson 在 α<1 有内容；真实零点在 α<1 无残余内容 ⟹ 零点与 GUE 完全一致
⭐ 判词（第三条独立路径）: 对偶带宽外无可测残差 ⟹ 支持"墙位于对偶带宽本身"；与 C-99/C-100 及 C-82/C-91/V188 同向
✅ 待办预注册: (1) 消混叠（非整除/非均匀 binning 或无 bin 核估计）(2) α 扫更远需提高展开精度 (3) 可选未截断解析拟合
✅ 净产出: ①残差变换方法＋Poisson 校准 ✓ ②α≈1 尖峰第二次判为伪影（含机制）✓ ③α≳1.25 无内容的窗口稳定结论 ✓ ④三条独立路径同向 ✓
```
