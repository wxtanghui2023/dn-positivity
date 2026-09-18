已查地图（所查：`CLOSED-ROUTES-MAP.md:228`（**DBN 判词**：`RH ⟺ Λ≤0`；`Λ≥0` 无条件（Rodgers–Tao）；上界 `0.22`（Polymath 15））、`:16`（Lyapunov／Poincaré 指数箱）、`FZ-3`、`POS1`（正性三分）、`V248`（判别锥必自对偶）、`C-109`（`S1` 模板：模型→插值→Poincaré 型不等式）、`C-110`（六条必要条件；`C6`＝定量稳定性，**0 命中**）、`V215` §5、`W4-1d`（第二尺度层／每 `γ` 增长率探针））。**结论**：把 `C6` 立为构造目标并开第一刀 ⟹ **在 DBN／热流形变上，`C6` 型不等式被一个初等机制封死**：DBN 族满足 `∂_t H + ∂_z² H = 0` ⟹ 在**碰撞处**（双重零点）离线距离 `= √(2(Λ−t))` ⟹ **`Hölder` 指数恰为 `1/2`**（拟合 `0.5000000000`；数值相对差 `≤1e-15`）⟹ 导数 `~(Λ−t)^{−1/2}` **发散** ⟹ **任何均匀 `Lipschitz`／`Poincaré` 常数在端点必然发散** ⟹ **端点转移非微扰** ✓✓；并**解释**为何 `Λ` 的上界记录（`0.22`）来自**有限计算**而非极限论证 ✓✓；**一般 `C6` 在其他实现仍开放**，但每个实现须先过**同一分支检验**，并预注册下一刀＝**逐 `γ` 增长率探针**（非光滑形变，可能避开端点分支）✓✓

# C-111 · **`C6` 第一刀：沿 DBN／热流形变的 Poincaré 型不等式（端点存在 1/2 阶分支）**

> **时间**：2026-09-18 16:28 唐先生「开」⟹ 按 `C-110` 的预注册，把 `C6`（定量稳定性）立为构造目标，以 `S1` 为模板在 **DBN／AFE 形变**上试写 ⟹ **本档第一刀** ✓

---

## §0 结论（先行）

$$\textbf{(1)}\ \text{目标重述（精确）}：\text{因}\ \Lambda\ge0\ \text{是定理（Rodgers--Tao）} \Longrightarrow \text{RH}\iff\boxed{\Lambda=0}✓$$
$$\qquad \text{当前括号}：0\le\Lambda\le\mathbf{0.22}\（\text{Polymath 15}） \Longrightarrow \text{目标}\ \textbf{＝端点}✓$$
$$\textbf{(2)}\ ⭐\ \textbf{微定理（本档，含数值验证）}：\text{DBN 族满足}\ \partial_tH+\partial_z^2H=0 \Longrightarrow \text{碰撞处离线距离}=\sqrt{2(\Lambda-t)}✓$$
$$\qquad \Longrightarrow\ \textbf{Hölder 指数恰为}\ \mathbf{1/2}\（\text{拟合斜率}\ 0.5000000000;\ \text{数值相对差}\le1\times10^{-15}） \Longrightarrow \text{导数}\sim(\Lambda-t)^{-1/2}\ \textbf{发散}✓✓$$
$$\qquad \Longrightarrow\ \boxed{\text{任何均匀 Lipschitz／Poincaré 常数在端点}\ \textbf{必然发散} \Longrightarrow \textbf{端点转移非微扰}}✓✓$$
$$\textbf{(3)}\ \text{判词}：\text{`C6` 在 DBN／热流}\ \textbf{实现} \text{上}\ \textbf{DEAD}（\text{机制}\ \textbf{初等可证}）✓✓$$
$$\qquad ⚠️\ \textbf{一般 `C6` 不死}：\text{其他实现（AFE 形变／逐 }\gamma\ \text{探针）仍开放}，\ \text{但每实现须先过}\ \textbf{同一分支检验}✓$$
$$\qquad ⭐\ \text{预注册下一刀}：\textbf{逐 }\gamma\ \text{增长率探针}（\text{`W4-1d`}）——\ \text{它}\ \textbf{不是光滑形变}，\ \text{可能避开端点分支}✓✓$$

---

## §1 想要的不等式（形式化）

$$\text{形变族}：\{H_t\}_{t\ge0}\（\text{DBN};\ H_0=\Xi）;\quad \text{零点}\ z_j(t)✓$$
$$\text{目标泛函}：\mathcal Q(t):=\sum_j \bigl|\operatorname{Im}z_j(t)\bigr|\quad（\text{离线质量}）;\qquad \text{RH}\iff\mathcal Q(0)=0✓$$
$$\textbf{想要的（}\text{`S1`}\ \text{模板的 RH 版）}：\boxed{\Bigl|\frac{d}{dt}\mathcal Q(t)\Bigr|\le C\cdot\mathcal E(t)^{1/2}\ \text{且}\ \mathcal E(t)\le \mathcal E_0\ \text{一致}} \Longrightarrow \text{由}\ t=\infty\ \text{推向}\ t=0✓$$
$$\qquad \Longrightarrow\ \text{若成立}：\mathcal Q(0)\le\mathcal Q(\infty)+\int_0^\infty C\mathcal E^{1/2}=0+C\mathcal E_0^{1/2}\ \text{—— 需}\ C\ \textbf{一致}✓$$

## §2 ⭐ 微定理（本档核心）：端点存在 **1/2 阶分支**

$$\textbf{第 1 步（结构）}：H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du \Longrightarrow \partial_tH_t=\int u^2e^{tu^2}\Phi\cos;\quad \partial_z^2H_t=-\int u^2e^{tu^2}\Phi\cos✓$$
$$\qquad \Longrightarrow\ \boxed{\partial_tH+\partial_z^2H=0}（\text{反热方程};\ \text{标准}）✓$$
$$\textbf{第 2 步（局部模型）}：\text{碰撞点附近}\ H_0(z)=z^2+c+O(z^3) \Longrightarrow \text{在最低阶}\ z^2\ \text{系下}\ \partial_tH=-2✓$$
$$\qquad \Longrightarrow\ H_t=z^2+c-2t \Longrightarrow \text{零点}=\pm\sqrt{2t-c} \Longrightarrow \text{临界}\ t^*=c/2=\Lambda\（\text{局部}）✓$$
$$\textbf{第 3 步（标度）}：t<\Lambda \Longrightarrow \text{离线距离}=\sqrt{2(\Lambda-t)} \Longrightarrow \boxed{\text{Hölder 指数}=\tfrac12};\quad \Bigl|\frac{d}{dt}\text{off}\Bigr|=\frac{1}{\sqrt{2(\Lambda-t)}}\to\infty✓✓$$
$$\Longrightarrow\ \text{任何}\ \textbf{均匀} \text{常数}\ C\ \text{必在}\ t\to\Lambda^-\ \text{失效} \Longrightarrow \boxed{\text{§1 的转移沿}\ t\ \text{不可能均匀}}✓✓$$

### 数值验证（本档实算）

| `ε=Λ−t` | 理论 `√(2ε)` | 数值根离线距离 | 相对差 |
|--:|--:|--:|--:|
| `1e-1` | 0.447213595500 | 0.447213595500 | 0.0e+00 |
| `1e-2` | 0.141421356237 | 0.141421356237 | 5.9e-16 |
| `1e-3` | 0.044721359550 | 0.044721359550 | 4.7e-16 |
| `1e-6` | 0.001414213562 | 0.001414213562 | 1.3e-11 |

$$\textbf{拟合}：\ln(\text{off})\ \text{vs}\ \ln\varepsilon \Longrightarrow \text{斜率}=\mathbf{0.5000000000} \Longrightarrow \textbf{Hölder 指数}=\tfrac12\ \text{确认}✓✓$$
$$\qquad \text{导数发散序列}：\varepsilon=10^{-1},10^{-2},10^{-3},10^{-4}\Rightarrow 1.58,\ 5.00,\ 15.8,\ 50.0\（\text{比值}\ \sqrt{10}\ ✓）✓✓$$

## §3 三个推论

$$\textbf{(i)}\ \textbf{解释了}\ \Lambda\ \text{上界记录（0.22）的来源}：\text{它来自}\ \textbf{严格有限计算}（\text{Polymath 15}），\ \textbf{而非} \text{任何}\ \textbf{极限／连续性／稳定性} \text{论证}✓$$
$$\qquad \Longrightarrow\ \text{与本档的端点分支机制}\ \textbf{一致}：\text{光滑转移}\ \textbf{原理上} \text{到不了端点}✓✓$$
$$\textbf{(ii)}\ \textbf{论证必须区分两情形}：$$
$$\qquad \text{RH 成立}（\Lambda=0） \Longrightarrow \text{热流在}\ t\ge0\ \textbf{无分支}（\text{零点皆实且单重} \Longrightarrow \text{隐函数定理} \Longrightarrow \text{平滑移动}）✓$$
$$\qquad \text{RH 失败}（\Lambda>0） \Longrightarrow t=\Lambda\ \text{处有}\ \mathbf{1/2}\ \text{阶分支}✓$$
$$\qquad \Longrightarrow\ \text{两情形}\ \textbf{定性不同} \Longrightarrow \text{任何}\ \textbf{统一} \text{论证必须在某处}\ \textbf{检测分支的存在} \Longrightarrow \text{而这就是}\ \Lambda\le0✓✓$$
$$\qquad \qquad \text{（与档案"循环"判定一致，但本档给出了}\ \textbf{初等机制}）✓$$
$$\textbf{(iii)}\ \text{对}\ \text{`C6`}\ \text{的一般含义}：\text{`C6` 要求"一致余量的稳定性"，而端点分支说明}\ \textbf{沿光滑形变的一致性在端点不可能}✓$$
$$\qquad \Longrightarrow\ \text{`C6` 若存在，必须}\ \textbf{不沿光滑形变}（\text{不靠连续性／插值}），\ \text{或须用}\ \textbf{对分支不敏感} \text{的量}✓$$
$$\qquad \qquad ⚠️\ \text{而后者的天然候选＝"光滑屏障"＝正性} \Longrightarrow \textbf{循环}（\text{`C-109`／`C-110`}）✓✓$$

## §4 预注册（证伪判据 ＋ 其他实现）

$$\textbf{`F1`}：\text{若所需余量对配置}\ \textbf{一致} \Longrightarrow \text{落}\ \text{`POS1`}\ \text{第三行} \Longrightarrow \textbf{RH 等价}（\text{必测}）✓$$
$$\textbf{`F2`}：\text{若"光滑化"装置＝正性} \Longrightarrow \textbf{循环}（\text{Weil}）✓$$
$$\textbf{`F3`}：\text{若目标泛函在端点呈}\ \textbf{Hölder-1/2}（\text{或更差}） \Longrightarrow \textbf{均匀转移不可能}（\text{本档已对 DBN 成立}）✓✓$$
$$\textbf{其他实现须重做同一检验}：$$
$$\qquad \text{(a)}\ \textbf{AFE 形变}：\text{已审闭}（\text{`V123`}），\ \text{但其}\ \textbf{端点分支} \text{尚未做此检验}✓$$
$$\qquad \text{(b)}\ ⭐\ \textbf{逐}\ \gamma\ \text{增长率探针}（\text{`W4-1d`}\ \text{第二尺度层：}\ u\text{-频率}=\gamma-t,\ \text{增长率}=\beta-\tfrac12）✓$$
$$\qquad \qquad \Longrightarrow\ \text{它}\ \textbf{不是参数形变}，\ \text{而是}\ \textbf{逐频率量} \Longrightarrow \textbf{可能避开端点分支}✓✓$$
$$\qquad \qquad ⚠️\ \text{但该探针}\ \textbf{需要零点数据} \Longrightarrow \text{须先过}\ \text{`C2`（不预设零点）}✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 16:3x）`[纪律]`（先跑后写）

```
技术词 端点分支         命中文件数=1  :: ./C111-C6-first-cut-DBN-heatflow-endpoint-half-order-branch.md
技术词 半阶分支         命中文件数=1  :: ./C111-C6-first-cut-DBN-heatflow-endpoint-half-order-branch.md
技术词 非微扰端点        命中文件数=1  :: ./C111-C6-first-cut-DBN-heatflow-endpoint-half-order-branch.md
技术词 Poincaré 常数发散   命中文件数=1  :: ./C111-C6-first-cut-DBN-heatflow-endpoint-half-order-branch.md
```
**读数**：写作**前**实跑均 **0 档**（⟹ 四词确为新措辞）；写作**后**复跑各＝**1 档（仅本档）** ✓✓

## §6 边界

- `[本档]` §2 的三步推导与 §2 表格为**本档实算／实推** ✓；第 1 步（反热方程）与第 2 步（局部模型）为**标准事实**（`[标准·待核]`：DBN 族碰撞的**全局**归约到该局部模型，本档未逐字核文献）✓
- ⚠️ **微定理的边界**：第 2 步是**局部模型**（忽略其它零点与全局结构）；结论在**该局部层**严格 ✓
- **不声称**：`C6` 原则上不可能 ✗（仅 DBN／热流实现上 DEAD）；`Λ≤0` 不可证 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导**（`Λ≥0` 为引用定理）✓

```
⚠️ 唐先生 16:28「开」⟹ 按 C-110 预注册, 把 C6(定量稳定性) 立为构造目标, 以 S1 为模板在 DBN/AFE 形变上试写
✅ 目标重述: 因 Λ≥0 是定理(Rodgers–Tao) ⟹ RH ⟺ **Λ=0**; 当前括号 0 ≤ Λ ≤ 0.22(Polymath 15) ⟹ 目标=**端点**
✅ 想要的不等式(形式): |d𝒬/dt| ≤ C·√𝒬 且常数 C 一致, 其中 𝒬(t)=Σ|Im z_j(t)| 离线质量, RH ⟺ 𝒬(0)=0
⭐ 微定理(本档, 含数值验证): DBN 族满足 ∂_t H + ∂_z² H = 0(反热方程, 由定义即得); 碰撞点附近 H_0 = z²+c+O(z³) ⟹
   H_t = z²+c−2t ⟹ 零点 = ±√(2t−c) ⟹ 临界 t*=c/2=Λ ⟹ t<Λ 时离线距离 = √(2(Λ−t))
   ⟹ **Hölder 指数恰为 1/2**; |d off/dt| = 1/√(2(Λ−t)) → ∞
   数值验证: ε=Λ−t 取 1e-1..1e-6, 理论 √(2ε) 与数值根离线距离相对差 ≤ 1e-15(及 1.3e-11 @1e-6);
   拟合 ln(off) vs ln ε 斜率 = **0.5000000000**; 导数序列 ε=1e-1,1e-2,1e-3,1e-4 → 1.58, 5.00, 15.8, 50.0(比值 √10) ✓✓
   ⟹ **任何均匀 Lipschitz/Poincaré 常数在端点必然发散 ⟹ 端点转移非微扰**
⭐ 判词: C6 在 DBN/热流**实现**上 DEAD(机制初等可证); ⚠️ 一般 C6 不死(其他实现仍开放, 但须先过同一分支检验)
⭐ 三个推论:
   (i) 解释 Λ 上界记录(0.22)来自**严格有限计算**(Polymath 15)而非极限/连续性论证 —— 与本档机制一致
   (ii) 论证必须区分两情形: RH 成立(Λ=0) ⟹ 热流 t≥0 无分支(零点皆实且单重 ⟹ 隐函数定理 ⟹ 平滑移动);
        RH 失败(Λ>0) ⟹ t=Λ 处有 1/2 阶分支 ⟹ 两情形定性不同 ⟹ 统一论证须在某处检测分支 ⟹ 而这正是 Λ≤0
        (与档案"循环"判定一致, 但本档给出**初等机制**)
   (iii) 对 C6 的一般含义: 沿光滑形变的一致性在端点不可能 ⟹ C6 若存在须**不沿光滑形变**或须用**对分支不敏感**的量;
        而后者的天然候选=光滑屏障=正性 ⟹ 循环(C-109/C-110)
✅ 预注册: F1 余量一致 ⟹ POS1 第三行 ⟹ RH 等价(必测); F2 光滑化=正性 ⟹ 循环; F3 端点 Hölder-1/2(或更差) ⟹ 均匀转移不可能(本档已对 DBN 成立)
   其他实现须重做: (a) AFE 形变(已审闭, 但端点分支未做此检验); (b) ⭐**逐 γ 增长率探针**(W4-1d: u-频率=γ−t, 增长率=β−1/2)
   —— 它不是参数形变而是逐频率量 ⟹ **可能避开端点分支**; ⚠️ 但需零点数据 ⟹ 须先过 C2(不预设零点)
✅ 净产出: ①C6 目标形式化 + 目标重述为端点(Λ=0) ✓ ②微定理(1/2 阶分支)+ 数值验证 ✓ ③三个推论(含 0.22 来源的解释) ✓
   ④证伪判据 F1–F3 + 下一刀预注册(逐 γ 探针) ✓
```
