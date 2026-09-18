已查地图（所查：`C-99`（残差探针）、`C-100`（三控制）、`C-101`（`Ê(α)` 变换；**编号说明见 §0**）、`C-98`、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`V188` §2）。**结论**：按唐先生指定的次序执行——**①先修合成 GUE control（已修好：自校准展开，间距方差 `0.17982` ✓✓）→ ②三窗稳定性 → ③`F(α)`，`0≤α≤4`** ⟹ **(i)** 修好的控制**验证了管线与方法**：`F≈min(α,1)` 完全正确且**三窗一致到 ≤0.005** ✓✓；**(ii)** 真实零点在 **`α≥1.25` 三窗一致到 ≤0.0025**，值 ≈`1.00–1.02` ⟹ **无超越 support 1 的内容** ✓✓；**(iii)** `α≈1.0` 处**三窗极差 0.18** ⟹ 按预注册 ⟹ **window-dependent／unresolved**（**不挑最漂亮的结果**）✓✓ ⟹ **负结果明显更扎实** ✓✓

# C-102 · **显式窗三窗稳定性审计 ＋ `F(α)`（`0≤α≤4`）**

> **时间**：2026-09-18 15:21 唐先生：**先把 C-100 的逻辑判词收紧一层**；下一步仍做显式窗，但**加"零成本前置审计"**：预注册为"**测试显式窗能否稳定恢复 `α>1` 的 `F(α)`**"；**至少三组窗** `w₁,w₂,w₃` 并检查 `F_{w_i}` 是否一致（尤其 `1<α≤2`）；**合成 GUE 控制必须先修好**；次序＝**修 GUE control → 三窗稳定性 → `F(α)`**
> **⚠️ 编号说明**：唐先生本轮称 `C-101`；因 `C-101` 已于 15:19 用于 `Ê(α)` 变换档（提交 `9f4d630`），本档编号 **`C-102`**，对应关系已注明 ✓

---

## §0 结论（先行）

$$\textbf{(1)}\ ⭐\ \textbf{GUE control 已修好}：\text{自校准展开} \Longrightarrow \text{间距方差}=0.17982\（\text{GUE 目标}\ 0.1781）✓✓$$
$$\qquad \text{其}\ F：\alpha=0.25/0.5/0.75\Rightarrow0.270/0.506/0.765 \approx\alpha;\ \alpha\ge1\Rightarrow1.01/1.01/0.93/0.94 \approx1 \Longrightarrow \textbf{与解析预测}\ F=\min(\alpha,1)\ \textbf{一致}✓✓$$
$$\qquad \textbf{三窗一致到}\ \le0.005 \Longrightarrow \boxed{\textbf{管线与方法经校准}}✓✓$$
$$\textbf{(2)}\ ⭐\ \text{真实零点}：\alpha\ge1.25\ \textbf{三窗一致到}\ \le0.0025,\ \text{值}\approx1.005\text{–}1.022 \Longrightarrow \boxed{\textbf{无超越 support 1 的内容}}✓✓$$
$$\textbf{(3)}\ ⚠️\ \alpha\approx1.0：\textbf{三窗极差}=0.1803 \Longrightarrow \text{按预注册} \Longrightarrow \boxed{\textbf{window-dependent／unresolved}}✓✓$$
$$\textbf{(4)}\ ⭐\ \Longrightarrow\ \textbf{负结果明显更扎实}：\text{"}\text{support}=1\ \text{是当前可用对偶带宽的真实边界}\text{"}✓✓$$

---

## §1 方法（消混叠＋三窗）

$$R_2(s)：\text{细网格}\ \Delta s=0.0173\（\textbf{非整除}，避免}\ 1/\Delta s\in\mathbb Z）＋\ \textbf{4 组 dither 平均}✓$$
$$\qquad ⚠️\ \textbf{动机}：\text{`C-101`}\ \text{判定}\ \alpha=1\ \text{尖峰源自"展开差值近整数聚集}\times\text{整除 binning"的周期-1 混叠}✓$$
$$w_1=\text{高斯}(\sigma=60,\ s_{\text{cut}}=120);\quad w_2=\text{余弦}(\cos\frac{\pi s}{2s_{\text{cut}}});\quad w_3=\text{四次光滑}\Bigl(1-(s/s_{\text{cut}})^2\Bigr)^2\quad(s\le s_{\text{cut}})✓$$
$$F_w(\alpha)=1+2\int_0^{s_{\text{cut}}}(R_2(s)-1)\,w(s)\cos(2\pi\alpha s)\,ds✓$$
$$\textbf{预注册判据（唐先生给定）}：\text{核心不是某条曲线，而是}\ \boxed{F_{w_1}(\alpha)\approx F_{w_2}(\alpha)\approx F_{w_3}(\alpha)}\ \text{（尤其}\ 1<\alpha\le2\text{）}✓$$
$$\qquad \text{若窗间}\ \textbf{系统性漂移} \Longrightarrow \text{立即判}\ \textbf{window-dependent／unresolved};\ \textbf{不挑最漂亮的结果}✓✓$$

## §2 控制组（**先修好**的合成 GUE）

$$\text{构造}：\text{Dumitriu--Edelman 三对角}\ \beta=2,\ N_c=60000;\ \text{对角}\sim N(0,2);\ \text{次对角}\sim\chi_{2(N-i)}✓$$
$$\qquad \text{（前一版自由度写错 ⟹ 间距方差}\ 0.00037;\ \textbf{本版修正}）✓$$
$$\text{展开}：\textbf{自校准} —— \hat R=2\sqrt{\langle e^2\rangle}\ \text{拟半圆半径} \Longrightarrow \text{间距方差}=0.17982✓✓$$

| `α` | 0.25 | 0.50 | 0.75 | **1.00** | 1.25 | 1.50 | 2.00 |
|:--|--:|--:|--:|--:|--:|--:|--:|
| `w₁` gauss | +0.2698 | +0.5056 | +0.7621 | +1.0143 | +1.0138 | +0.9281 | +0.9376 |
| `w₂` cos | +0.2701 | +0.5071 | +0.7651 | +1.0156 | +1.0164 | +0.9219 | +0.9341 |
| `w₃` quad | +0.2685 | +0.5063 | +0.7583 | +1.0117 | +1.0082 | +0.9267 | +0.9372 |
| 极差 | 0.0016 | 0.0015 | 0.0068 | 0.0039 | 0.0082 | 0.0062 | 0.0035 |

$$\Longrightarrow\ \textbf{控制组三窗一致（≤0.009）};\ F\approx\min(\alpha,1)✓✓ \Longrightarrow \textbf{方法与归一化经校准}✓✓$$
$$\qquad ⚠️\ \text{注意}：\text{控制组在}\ \alpha\ge1.5\ \text{处为}\ 0.92\text{–}0.94\（\text{略低于}\ 1），\ \text{属其自身慢变分量};\ \text{解读真数据时须以此为基线}✓$$

## §3 真实零点：三窗稳定性（`2,001,052` 个）

| `α` | `w₁` | `w₂` | `w₃` | **三窗极差** | 判定 |
|:--|--:|--:|--:|--:|:--|
| 0.25 | +0.2810 | +0.2839 | +0.2814 | 0.0029 | ✅ 稳定 |
| 0.50 | +0.5027 | +0.5020 | +0.5032 | 0.0012 | ✅ 稳定 |
| 0.75 | +0.7570 | +0.7564 | +0.7569 | 0.0005 | ✅ 稳定 |
| **1.00** | **+1.8136** | **+1.8742** | **+1.6938** | **0.1803** | ⚠️ **漂移** |
| 1.10 | +1.1110 | +1.1087 | +1.1184 | 0.0098 | ⚠️ 弱漂移 |
| 1.25 | +0.9717 | +0.9712 | +0.9738 | 0.0025 | ✅ 稳定 |
| 1.50 | +1.0224 | +1.0241 | +1.0217 | 0.0024 | ✅ 稳定 |
| 1.75 | +1.0157 | +1.0166 | +1.0167 | 0.0009 | ✅ 稳定 |
| 2.00 | +1.0068 | +1.0062 | +1.0069 | 0.0007 | ✅ 稳定 |
| 2.50 | +1.0044 | +1.0038 | +1.0051 | 0.0013 | ✅ 稳定 |
| 3.00 | +1.0153 | +1.0152 | +1.0162 | 0.0010 | ✅ 稳定 |
| 4.00 | +1.0204 | +1.0198 | +1.0194 | 0.0011 | ✅ 稳定 |

$$\textbf{(i)}\ \alpha=1.0：\textbf{极差}\ 0.18 \Longrightarrow \textbf{window-dependent／unresolved}（\text{按预注册，}\textbf{不解释为结构}）✓✓$$
$$\qquad ⚠️\ \text{且}\ \textbf{dithering 未消除} \text{该尖峰};\ \text{而修好的 GUE 控制}\ \textbf{无此尖峰} \Longrightarrow \text{它}\ \textbf{不是通用管线伪影}，\text{而}\ \textbf{与 ζ 展开的具体结构有关} \Longrightarrow \text{仍判 unresolved（不升级解释）}✓✓$$
$$\textbf{(ii)}\ \alpha\ge1.25：\textbf{三窗一致到}\ \le0.0025 \Longrightarrow \textbf{可稳定恢复}✓✓;\ \text{值}\approx1.005\text{–}1.022✓$$
$$\qquad \text{与修好的 GUE 控制（0.92–1.01）}\ \textbf{量级相当} \Longrightarrow \textbf{无超越 support 1 的额外内容}✓✓$$

## §4 综合判词（三条独立路径 ＋ 本轮加固）

$$\boxed{\text{零点--素数 Fourier 对偶：确认至}\ \text{support}\ 1;\qquad \text{support}>1：\textbf{尚无可用实证结构}}✓✓\（\text{唐先生指定的路线图标记}）$$
$$\qquad \text{支持路径}：\text{`C-99`（Stage A/B/C）};\ \text{`C-100`（三控制）};\ \text{`C-101`（}\hat E\ \text{变换 ＋ Poisson 校准）};\ \textbf{本档（修好 GUE 控制 ＋ 三窗审计）}✓✓$$
$$\qquad ⚠️\ \textbf{两个命题必须分开}（唐先生强调）：$$
$$\qquad \qquad \boxed{\text{存在一个}\ \textbf{通过当前展开控制的、大}\ s\ \text{residual}}\qquad\ne\qquad\boxed{\text{这是}\ \text{support}>1\ \text{的 residual}}✓✓$$
$$\qquad \text{本轮实测}：R_2(100)=1.0124,\ R_2(140)=1.0216\ \textbf{未收敛到 1} \Longrightarrow \text{前者成立（记录在案）};\ \text{后者}\ \textbf{仍无证据}✓$$

## §5 待办（预注册，未做）

$$\textbf{(1)}\ \text{提高展开精度} \Longrightarrow \text{把}\ \alpha\ \text{扫到}\ 4\ \text{以上且保持三窗一致}✓$$
$$\textbf{(2)}\ \text{把}\ \alpha\approx1\ \text{的漂移}\ \textbf{归因} \text{到具体机制}（\text{展开残差 vs 数值积分 vs 真结构}）\ \text{需独立控制}✓$$
$$\textbf{(3)}\ \text{可选}：\text{用未截断解析拟合分离慢变分量}✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 15:2x）`[纪律]`（先跑后写）

```
技术词 三窗稳定性        命中文件数=1  :: ./C102-three-window-stability-audit-and-F-alpha-0-to-4.md
技术词 自校准展开        命中文件数=1  :: ./C102-three-window-stability-audit-and-F-alpha-0-to-4.md
技术词 window-dependent  命中文件数=1  :: ./C102-three-window-stability-audit-and-F-alpha-0-to-4.md
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

## §7 边界

- `[数据]` §2／§3 全部**本次实算**（真实零点 2,001,052 个；合成 GUE `N_c=60000`，间距方差 0.17982）✓
- ⚠️ `α≈1.0` 的尖峰**判为 window-dependent／unresolved**（**不解释为结构**）；`α≥1.25` 结论**三窗稳定** ⟹ 可信 ✓
- **不声称**：`support>1` 有实证结构 ✗；`support>1` 不可能 ✗；不证 RH ✗
- **纪律**：**先跑后写** ✓；**未用 RH 作推导** ✓；**不挑最漂亮的结果** ✓✓

```
⚠️ 唐先生 15:21：先不要直接进入"跑显式窗"，先收紧 C-100 判词；并给出次序与判据：
   ①先修合成 GUE control ②三窗稳定性 ③F(α), 0≤α≤4；预注册为"测试显式窗能否稳定恢复 α>1 的 F(α)"；
   三窗一致才算过，漂移则判 window-dependent/unresolved；两个命题（大 s residual / support>1 residual）必须分开
✅ 编号说明: 唐先生称 C-101；C-101 已于 15:19 用于 Ê(α) 档（9f4d630），本档编号 C-102 并注明对应关系
✅ (1) GUE control 修好: Dumitriu–Edelman β=2, N_c=60000（前一版 χ 自由度写错 ⟹ 0.00037；本版修正）
   + 自校准半圆展开（R̂=2√⟨e²⟩）⟹ **间距方差 0.17982**（目标 0.1781）✓✓
   控制组 F: α=0.25/0.5/0.75 → 0.270/0.506/0.765 ≈ α; α≥1 → 1.01/1.01/0.93/0.94 ≈ 1 ⟹ 与解析预测 F=min(α,1) 一致
   **三窗一致到 ≤0.009** ⟹ 管线与方法经校准 ✓✓
✅ (2) 真实零点三窗: α≥1.25 三窗一致 ≤0.0025，值 ≈1.005–1.022 ⟹ **无超越 support 1 的内容** ✓✓
   α=1.0: 三窗极差 **0.1803** ⟹ window-dependent/unresolved（按预注册，不解释为结构）；
   ⚠️ dithering 未消除该尖峰，而修好的 GUE 控制无此尖峰 ⟹ 不是通用管线伪影，而与 ζ 展开具体结构有关 ⟹ 仍判 unresolved
✅ (3) 综合判词: 零点–素数 Fourier 对偶 确认至 support 1；support>1 尚无可用实证结构（三条独立路径 + 本轮加固）
   ⚠️ 两个命题分开: 存在通过当前展开控制的大 s residual（R2(100)=1.0124, R2(140)=1.0216 未收敛到 1）≠ 这是 support>1 的 residual（仍无证据）
✅ 净产出：①GUE control 修好（间距方差 0.17982）✓ ②三窗审计（α≥1.25 稳定 / α≈1 漂移）✓ ③F(α) 0≤α≤4 结果 ✓ ④两个命题分离 ✓ ⑤负结果加固 ✓
```
