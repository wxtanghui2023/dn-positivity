已查地图（所查：`C-76`（**RS 消失引理逐字**：`Φ` supported in `\sum|\xi_j|\le(2-\delta)/m` ⟹ 除非 `|n_j|\ll T` 且 `n_1n_2\cdots n_{r+s}\ll T^{2-\delta}`；**四方同址**：support>1 ⟺ 无条件三阶矩 ⟺ 乘积超 `T^2` ⟺ prime-pair 输入）、`C-75`（前沿 `§7.2(e)` 逐字：prime-side `tr\tilde G^k` 用对角法**只在 Rudnick–Sarnak 范围** `X^k\le T^{2-\varepsilon}`；`X\asymp T` 时只允许 `k=1`）、`C-118`／`C-119`（残留是真结构；真三体记忆）、`W6`／`SUPPORT-1`（`h\le x^{1/2}`）、`Hejhal 1994`／`Rudnick–Sarnak 1996`（`n\ge3` **前提 RH**）、`C-116`（**登记不否决**））。**结论**：把 `RS` 支持条件翻成素数侧 ⟹ **`k` 级可达窗＝`h\le x^{1/k}`**（`k=2`：`x^{1/2}`＝support 1；`k=3`：`x^{1/3}`）✓；**检查我们的三体数据**：`h\le40`、`x=10^9` ⟹ `T\asymp x^{1/2}=31623`，`X^3\approx6.4\times10^4\ll T^2=10^9` ⟹ **深在可达窗内** ⟹ **"对上"**：我们的三体测量落在**无条件可达**的范围内（**矩／平均**层面）✓✓；⭐ **但结构结论**：**窗随 `k` 收缩**（`h\le x^{1/k}`）⟹ `x=10^9` 下 `k=2/3/4/5/6/7/8/10` 分别为 `31623／1000／177／63／31.6／19.3／13.3／7.9` ⟹ **中等 `M`（`M\approx5\text{–}7`）起，我们的跨度已越过窗** ⟹ **`M` 窗口方向作为"通向定理"的路线在中等 `M` 处终止**（**经验测量不受限**）✓✓

# C-120 · **`RS` 支持条件的素数侧翻译 ＋ 三体数据落点 ＋ "窗随 `k` 收缩"**

> **时间**：2026-09-18 18:10 唐先生：**「继续」** ⟹ 把 `RS` 的 `n=3` 支持条件翻成素数侧乘积界，检查我们的三体数据是否落在其预测范围内 ✓

---

## §0 结论（先行）

$$\textbf{(1)}\ \text{翻译（用 `C-76` 逐字）}：\text{支持条件}\ \sum|\xi_j|\le\frac{2-\delta}{m} \iff \text{乘积界}\ n_1\cdots n_{r+s}\ll T^{2-\delta}✓$$
$$\qquad \text{取各因子}\ \asymp X \Longrightarrow X^k\le T^{2-\delta} \Longrightarrow \boxed{h\le x^{1/k}}\（T\asymp x^{1/2}）✓✓$$
$$\qquad \qquad k=2：h\le x^{1/2}（\text{support }1，\text{已知}）;\quad k=3：h\le x^{1/3}✓$$
$$\textbf{(2)}\ \text{我们的数据落点}：h\le40,\ x=10^9 \Longrightarrow T\asymp31623,\ X^3\approx6.4\times10^4\ll T^2=10^9✓$$
$$\qquad \Longrightarrow \boxed{\text{深在可达窗内} \Longrightarrow \textbf{"对上"}}：\text{三体测量落在}\ \textbf{无条件可达} \text{的范围内（}\textbf{矩／平均} \text{层面）}✓✓$$
$$\textbf{(3)}\ ⭐\ \textbf{结构结论}：\text{窗}\ \textbf{随}\ k\ \textbf{收缩}（h\le x^{1/k}） \Longrightarrow \text{中等}\ M\ \text{起即越窗}✓✓$$
| `k`（素数个数）| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 10 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| 可达窗 `x^{1/k}`（`x=10^9`）| 31623 | 1000 | 177 | 63 | 31.6 | 19.3 | 13.3 | 7.9 |
$$\qquad \Longrightarrow\ \text{我们的跨度上限}\ 40\ \text{在}\ k\ge6\ \text{时}\ \textbf{已越过窗} \Longrightarrow \boxed{\text{路线在}\ M\approx5\text{–}7\ \text{处终止（作为通向定理之路）}}✓✓$$
$$\qquad \qquad ⚠️\ \textbf{但经验测量不受限}：\text{任何}\ M\ \text{都能测};\ \text{受限的是}\ \textbf{理论支持窗}✓$$

---

## §1 `RS` 条件的逐字与翻译

$$\text{`C-76` 逐字}：\text{Let}\ \Phi\ \text{be supported in}\ |\xi_1|+\cdots+|\xi_n|\le\frac{2-\delta}{m}.\ \text{Then}\ A_{r,s}(n,T)=0\ \text{unless}\ |n_j|\ll T\ \text{and}\ n_1n_2\cdots n_{r+s}\ll T^{2-\delta}✓$$
$$\text{机制（}\text{`C-76`}）：\text{积分非零要求}\ \eta\in\operatorname{Supp}\Phi\ \text{且}\ |T(\eta_jL+\log n_j)|\ll1 \Longrightarrow n_j\ll T^{m|\eta_j|} \Longrightarrow \prod n_j\ll T^{m\sum|\eta_j|}\le T^{2-\delta}✓$$
$$\qquad \Longrightarrow \text{纯代数后果，}\ \textbf{改权重不能绕过}（\text{`C-76`}）✓$$
$$\text{前沿自述（}\text{`C-75`} 逐字）：\text{prime-side}\ tr\tilde G^k\ \text{用对角法}\ \textbf{只在}\ X^k\le T^{2-\varepsilon};\ X\asymp T\ \text{时只允许}\ k=1✓$$
$$\qquad \Longrightarrow \text{故}\ \boxed{h\le x^{1/k}}\ \text{是}\ \textbf{前沿与档案一致的} \text{可达窗}✓✓$$

## §2 我们的数据落点（计算）

$$x=10^9 \Longrightarrow T\asymp x^{1/2}=3.16\times10^4;\quad \text{我们的跨度}\ h\le40✓$$
$$\text{三体}（k=3）：X^3\approx6.4\times10^4\quad\text{vs}\quad T^2=10^9 \Longrightarrow \frac{X^3}{T^2}\approx6.4\times10^{-5}✓✓$$
$$\Longrightarrow \textbf{深在窗内}\（\text{余量}\ \sim4\ \text{个量级}） \Longrightarrow \text{三体测量}\ \textbf{落在无条件可达范围}✓✓$$

## §3 量化表与"窗随 `k` 收缩"

| 量 | 值 |
|:--|:--|
| 我们的 `x` | `10⁹` |
| `T ≍ x^{1/2}` | `3.16×10⁴` |
| 我们的跨度上限 `h` | `40` |

| `k` | `x^{1/k}` | `h=40` 是否在窗内 |
|--:|--:|:--|
| 2 | 31623 | ✓（余量 3 个量级）|
| 3 | 1000 | ✓（余量 1.4 个量级）|
| 4 | 177 | ✓ |
| 5 | 63 | ✓（勉强）|
| 6 | 31.6 | ⚠️ **越窗**（`40>31.6`）|
| 7 | 19.3 | ✗ |
| 8 | 13.3 | ✗ |
| 10 | 7.9 | ✗ |

$$\Longrightarrow \boxed{\text{可用}\ k\lesssim5\text{–}6 \Longrightarrow \text{路线在}\ M\ (\text{间隙数})\ \approx4\text{–}5\ \text{处到顶}}✓✓$$
$$\qquad ⚠️\ \text{且}\ \textbf{最小可能跨度}\ \text{随}\ M\ \text{线性增}（\text{如全 2 间隙}：span=2M）;\ \text{窗}\ \text{随}\ M\ \text{指数缩}（x^{1/(M+1)}）✓$$
$$\qquad \Longrightarrow\ \text{两条线}\ \textbf{在中}\ M\ \text{相交} \Longrightarrow \text{更高}\ M\ \text{的经验测量}\ \textbf{失去理论支持}✓✓$$

## §4 与 `C-118`／`C-119` 的关系（两件不同的事）

$$\text{`C-119`}：M\ \text{窗口记忆}\ \textbf{不是两体} \Longrightarrow \textbf{真三体结构存在}（\text{经验事实}）✓✓$$
$$\text{`C-120`}：\text{其}\ \textbf{理论支持窗} \text{随}\ k\ \text{收缩} \Longrightarrow \text{越往高阶}\ \textbf{越没有已知理论可对}✓✓$$
$$\Longrightarrow\ \text{二者}\ \textbf{不矛盾}：\text{结构}\ \textbf{真实}，\ \text{但}\ \textbf{可判理论的支撑} \text{在中等}\ M\ \text{处枯竭}✓✓$$
$$\qquad \text{即：}\text{该方向}\ \textbf{不是错的}，\ \text{而是}\ \textbf{越走越孤立} \text{（无已知结果可比）}✓$$

## §5 边界与回查

- `[档案]` §1 的 `C-76`／`C-75` 逐字为**引用** ✓
- `[本档]` §2 的落点计算、§3 的量化表与"两线相交"结论为**本档工作** ✓
- ⚠️ **`h\le x^{1/k}` 的语义**：它是 **矩／平均**层面（对角法）的可达窗；**单个固定型**的渐近**在任何 `k` 都未证**（`k`-tuple 猜想）⟹ 本档**不**声称我们的数据可由已知定理**预测** ✓
- ⚠️ **不否决**（`C-116`）✓
- **不声称**：`M` 窗口方向无价值 ✗（经验结构真、且在窗内）; 不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 18:1x）`[纪律]`（先跑后写）

```
技术词 可达窗         命中文件数=1  :: ./C120-RS-support-translation-prime-side-window-shrinks-with-k.md
技术词 窗随 k 收缩      命中文件数=1  :: ./C120-RS-support-translation-prime-side-window-shrinks-with-k.md
技术词 两线相交        命中文件数=1  :: ./C120-RS-support-translation-prime-side-window-shrinks-with-k.md
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

```
⚠️ 唐先生 18:10「继续」⟹ 把 RS n=3 支持条件翻成素数侧乘积界 + 检查我们三体数据落在哪
⭐ 翻译(C-76 逐字): 支持条件 Σ|ξj| ≤ (2−δ)/m ⟺ 乘积界 n1…n_{r+s} ≪ T^{2−δ}; 取各因子 ≍X ⟹ X^k ≤ T^{2−δ} ⟹ **h ≤ x^{1/k}**(T≍x^{1/2})
   k=2: h ≤ x^{1/2}(support 1, 已知); k=3: h ≤ x^{1/3}; 一般 h ≤ x^{1/k}
   机制: 积分非零要求 η∈SuppΦ 且 |T(ηj L + log nj)| ≪ 1 ⟹ nj ≪ T^{m|ηj|} ⟹ ∏nj ≪ T^{mΣ|ηj|} ≤ T^{2−δ} = 纯代数后果, 改权重不能绕过
   前沿自述(C-75 逐字): prime-side tr G̃^k 用对角法只在 X^k ≤ T^{2−ε}; X≍T 时只允许 k=1
⭐ 我们的落点: x=1e9 ⟹ T≍3.16e4; h ≤ 40 ⟹ X³ ≈ 6.4e4 ≪ T² = 1e9(余量 ~4 个量级) ⟹ **深在窗内 ⟹ "对上"**
   即: 三体测量落在**无条件可达**范围内(矩/平均层面)
⭐ 量化表(x=1e9, h上限40): k=2→31623 ✓(3个量级余); k=3→1000 ✓(1.4个量级余); k=4→177 ✓; k=5→63 ✓(勉强);
   k=6→31.6 ⚠️**越窗**; k=7→19.3 ✗; k=8→13.3 ✗; k=10→7.9 ✗
   ⟹ 可用 k ≲ 5–6 ⟹ 路线在 M(间隙数) ≈ 4–5 处到顶
   ⚠️ 且最小可能跨度随 M 线性增(全2间隙: span=2M), 窗随 M 指数缩(x^{1/(M+1)}) ⟹ 两线在中 M 相交
⭐ 与 C-118/C-119 关系(两件不同的事): C-119 = 记忆不是两体, **真三体结构存在**(经验事实); C-120 = 其**理论支持窗随 k 收缩**(越往高阶越无已知理论可对)
   ⟹ 不矛盾: 结构真实, 但可判理论的支撑在中等 M 处枯竭 ⟹ 该方向不是错的, 而是**越走越孤立**
⚠️ 语义边界: h ≤ x^{1/k} 是**矩/平均**层面的可达窗(对角法); **单个固定型**的渐近在任何 k 都未证(k-tuple 猜想) ⟹ 本档**不**声称我们的数据可由已知定理预测
⚠️ 纪律(C-116): 不否决; 不声称 M 窗口方向无价值(经验结构真、且在窗内); 不证 RH
✅ 净产出: ①RS 支持条件的素数侧翻译 h ≤ x^{1/k}(含机制与前沿逐字对照) ②三体数据落点=深在窗内("对上") ③量化表 +
   缩放律(x^{1/k} vs 2M 两线相交) ⟹ 路线在 M≈4–5 到顶 ④与 C-118/C-119 的关系澄清(结构真实 vs 理论支持窗窄)
```
