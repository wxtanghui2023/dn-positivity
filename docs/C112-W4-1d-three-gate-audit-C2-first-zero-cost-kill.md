已查地图（所查：`W4-1d-second-scale-layer-exists-frequency-separable.md`（**逐字定义**）、`W4-1e-blind-readout-growth-coordinate-NOT-resolvable.md`、`W4-LEAKAGE-AUDIT-and-sealing-frequency-localization-only.md`、`W4-1b`（全线性滤波 DEAD）、`W4-1c`、`ASSETS-REGISTRY.md`（`C-33`）、`V215` §4（三型全封／逐 `γ` 通道）、`V188` §2（**线性通道饱和；反演到逐点需无界精度**）、`W1`（**检测 ≠ 排除**）、`d7-boundary-audit`（**恒等通道只产等式**）、`C-46`／`C-62`（**窗口空洞**先例）、`C-107`（**改变泛函类型不改变信息通道**）、`C-111`（**端点 `1/2` 阶分支**，`F3`））。**结论**：按唐先生指定执行 **`C-112`：`W4-1d` 三门审计**，**第一刀只做 `C2`**（定义级／非零点输入），**不做数值实验** ⟹ **`W4-1`（定义级）✓**：`G(γ)` **不是新算术量**，它就是 `δ_T` 的**逐模指数**，而 `δ_T` 的零点侧身份**就是显式公式本身** ✓；**`W4-2`（`C2`）✗ FAIL**：读出**可完全化约为对 `{γ_n}` 的逐点泛函**（峰位＝`γ`；逐模指数＝逐原子分离），且**反演饱和线性数据到逐点需无界精度**（`V188` §2）⟹ 按唐先生**零成本判死** ⟹ **C2 FAIL：zero-side encoding** ✓✓；并附**两项零成本定量发现**（分辨窗口 `γ<2πe^{U}` 落在**已验证范围**内 ⟹ **窗口空洞**；振幅 `~1/γ²`）✓✓；**`W4-3`（端点分支）不执行**（`C2` 已 FAIL），但**登记为检查单** ✓

# C-112 · **`W4-1d` 三门审计（第一刀：`C2` 定义审计）**

> **时间**：2026-09-18 16:31 唐先生：「**开**」，但**把下一刀从"验证一个候选"升级成"先验资格审计 ＋ 分支检验"**；顺序固定 **`C2` 非零点性 → 端点分支 → RH 信息增益**；**第一刀只做 `C2` 定义审计，不先做数值实验**；并加**零成本判死**（`W4-1d` 是否可化约为 `F({γ_n})`）✓
> **外部文献核对（唐先生）**：Rodgers–Tao（arXiv:1801.05914）证明 `Λ ≥ 0`；Polymath 15 给无条件 `Λ ≤ 0.22`；`RH ⟺ Λ ≤ 0` ✓

---

## §0 结论（先行）

$$\textbf{`W4-1`（定义级）✓}：\text{`G(γ)`} \textbf{不是新算术量} —— \text{它就是}\ \delta_T\ \text{的}\ \textbf{逐模指数}，\ \text{而}\ \delta_T\ \text{的零点侧身份}\ \textbf{就是显式公式本身}✓✓$$
$$\textbf{`W4-2`（`C2`）✗ FAIL}：\text{读出}\ \textbf{可完全化约为对}\ \{\gamma_n\}\ \text{的逐点泛函}（\text{峰位}=\gamma;\ \text{逐模指数}=\text{逐原子分离}）✓✓$$
$$\qquad \text{且}\ \textbf{反演饱和线性数据到逐点需无界精度}（\text{`V188` §2}） \Longrightarrow \text{按零成本判死} \Longrightarrow \boxed{\textbf{C2 FAIL：zero-side encoding}}✓✓$$
$$\qquad ⚠️\ \text{这与}\ \text{`C-107`}\ \text{的实测教训}\ \textbf{同址}：\textbf{改变泛函类型不改变信息通道}✓$$
$$\textbf{附：两项零成本定量发现}：\text{(i)}\ \text{分辨窗口}\ \gamma<2\pi e^{U}\ \text{落在}\ \textbf{已验证范围} \text{内} \Longrightarrow \textbf{窗口空洞}（\text{`C-46`／`C-62` 同型}）✓;$$
$$\qquad \text{(ii)}\ \text{模振幅}\sim1/\gamma^2 \Longrightarrow \textbf{可测高度偏小} \Longrightarrow \text{同向}✓$$
$$\textbf{`W4-3`（端点分支）不执行}（\text{`C2` 已 FAIL}），\ \text{但}\ \textbf{登记为检查单}✓$$
$$\Longrightarrow\ \text{按唐先生判词表}：\boxed{\text{C2 直接失败} \Longrightarrow \textbf{DEAD：zero-side encoding}} \Longrightarrow \text{并入}\ \text{`V215` §4 逐 }\gamma\ \text{通道}✓✓$$

---

## §1 `W4-1d` 逐字定义（档内原文）

$$A(T):=\sum_{n\le T}\frac{\Lambda(n)}{\sqrt n}\（\text{增量前缀和}）;\qquad \text{主项}=2\sqrt T-1;\qquad \delta(T):=A(T)-\text{主项}✓$$
$$\delta_T(s)=-\sum_\rho\frac{T^{\rho-s}}{\rho(\rho-s)}+\ldots \Longrightarrow \text{每项}=T^{\beta-\frac12}\cdot e^{i(\gamma-t)u},\qquad u=\log T✓$$
$$\qquad \Longrightarrow\ \boxed{\ u\text{-频率}=\gamma-t\（\text{零点位置}）\ \big|\ \ u\text{-增长率}=\beta-\tfrac12\（\text{零点偏移}）\ }✓✓$$
$$\text{实算设置}：\text{阶梯}\ u=\log T\ \text{上}\ 256\ \text{点},\ T\in[10^5,2\times10^8],\ s=\tfrac12;\ \Delta u=0.0298,\ \Delta\nu=0.827✓$$
$$\qquad \text{结果：}\nu\approx0\ \text{背景层（}A=1.688）\ \big|\ \nu=\gamma\ \text{峰层（}0.024\text{–}0.063）;\ \text{动态范围}\ 30\text{–}80\times✓$$

## §2 `W4-1`：定义级审计（`G(γ)` 是什么？）

$$\text{唐先生要求}：\text{先明确}\ G(\gamma)\ \text{到底是}\ \textbf{什么对象}，\ \text{且}\ G(\gamma)=\beta-\tfrac12\ \text{中的}\ \beta\ \text{是}\ \textbf{哪个原始算术量}✓$$
$$\textbf{本档判定}：G\ \text{是}\ \delta_T\ \text{在}\ u=\log T\ \text{谱中、频率}\ \nu=\gamma\ \text{处模的}\ \textbf{对数增长率}：G(\gamma)=\dfrac{d}{du}\log\bigl|\widehat{\delta_T}(\gamma)\bigr|\ \text{的渐近值}✓$$
$$\qquad \text{而}\ \delta_T\ \text{的}\ \textbf{零点侧身份}（\text{逐字，§1}）＝\text{显式公式} \Longrightarrow G\ \textbf{不是新对象}，\ \text{是}\ \textbf{显式公式对象的谱读出}✓✓$$
$$\qquad \Longrightarrow\ \text{按}\ \text{`V215` §4}：\text{显式公式＝值面} \Longrightarrow \text{`W4-1d`}\ \text{落在}\ \textbf{已知唯一桥} \text{上}✓$$
$$\qquad ⚠️\ \text{但}：\text{"落在显式公式上"}\ \textbf{不必} \text{等于}\ \textbf{信息饱和}——\text{须看读出是否越出线性层}（\text{§3 处理}）✓$$

## §3 ⭐ `W4-2`：`C2` 非零点输入审计（**零成本判死**）

$$\text{判死检验（唐先生逐字）}：\boxed{\text{`W4-1d`}\ \stackrel{?}{=}\ F(\{\gamma_n\})} \Longrightarrow \text{若可完全化约为零点测度的}\ \textbf{逐点泛函} \Longrightarrow \textbf{C2 FAIL}✓$$

$$\textbf{逐步判定}：$$
$$\qquad \text{(1)}\ \textbf{对象定义}：A(T)=\sum_{n\le T}\Lambda(n)/\sqrt n \Longrightarrow \textbf{纯素数侧}✓\（\text{定义层不用}\ \gamma）✓$$
$$\qquad \text{(2)}\ ⚠️\ \textbf{读出层}：\text{要得到}\ G(\gamma)\ \text{必须}：\text{(i)}\ \textbf{定位峰位}\ \nu=\gamma \Longrightarrow \text{峰位}\ \textbf{就是}\ \gamma;\ \text{(ii)}\ \text{在该频率测}\ \textbf{逐模指数} \Longrightarrow \textbf{分离单个原子}✓✓$$
$$\qquad \qquad \Longrightarrow \text{该读出}\ \textbf{就是}\ \text{对}\ \{\gamma_n\}\ \text{的逐点泛函} \Longrightarrow \boxed{\textbf{C2 FAIL}}✓✓$$
$$\qquad \text{(3)}\ \text{更硬的理由（}\text{`V188` §2 逐字要点）}：\text{线性通道}\ \textbf{饱和};\ \text{反演饱和线性数据到}\ \textbf{逐点位置} \text{需}\ \textbf{无界精度}✓$$
$$\qquad \qquad \Longrightarrow\ \text{"分离单个原子"}\ \text{正是该无界精度步} \Longrightarrow \text{即}\ \text{`S(T)`}\ \text{问题本身}✓✓$$
$$\qquad \text{(4)}\ \text{与}\ \text{`V215` §4 的关系}：§4 已封\ \textbf{逐 }\gamma\ \text{通道};\ \text{本档}\ \textbf{完成合并}（\text{不新增入口}）✓$$

$$\Longrightarrow\ \boxed{\text{`C2` FAIL，理由＝zero-side encoding（读出级）}} \Longrightarrow \text{按唐先生规定：}\textbf{无需再跑大规模数据}✓✓$$
$$\qquad ⚠️\ \textbf{与}\ \text{`C-107`}\ \text{同址}：\text{那里实测出}\ \textbf{"改变泛函类型不改变信息通道"}（\text{free probability}）；\ \text{此处}\ \textbf{从标量}\ |\delta_T|\ \text{改成}\ \log T\ \text{谱}\ \text{亦然}✓✓$$

## §4 附：两项零成本定量发现（未做实验，纯标度算术）

$$\textbf{(i)}\ \textbf{分辨窗口}：\text{峰可分辨} \iff \text{零点间距}> \Delta\nu=\frac{2\pi}{U}\（U＝\ u\text{-窗宽}）✓$$
$$\qquad \text{零点间距}\approx\frac{2\pi}{\log(\gamma/2\pi)} \Longrightarrow \text{可分辨} \iff \log(\gamma/2\pi)<U \iff \boxed{\gamma<2\pi e^{U}}✓✓$$
$$\qquad \text{`W4-1d` 设置}：U=\log(2\times10^8)-\log(10^5)=7.60 \Longrightarrow \gamma<2\pi e^{7.6}\approx\mathbf{1.3\times10^4}✓$$
$$\qquad \text{而}\ \textbf{已验证高度}：\gamma\le3.000175\times10^{12} \Longrightarrow \boxed{\text{可分辨高度}\ \textbf{深在已验证范围内}} \Longrightarrow \textbf{窗口空洞}✓✓$$
$$\qquad \qquad \text{（同型先例：}\text{`C-46`}／\text{`C-62`}\ \text{——比较只在已被覆盖的窗口内成立}）✓$$
$$\qquad ⚠️\ \textbf{诚实边界}：\text{窗口随}\ U\ \text{增大}（\gamma<2\pi e^{U}）;\ \text{要越过已验证高度需}\ U\gtrsim27 \Longrightarrow \text{素数数据比}\ e^{27}\approx5\times10^{11}，\ \textbf{且}\ A(T)\ \text{须从}\ \sim2\sqrt T\ \text{中提取微小涨落} \Longrightarrow \text{灾难性相消}✓$$
$$\qquad \qquad \Longrightarrow\ \text{故此项是}\ \textbf{标度／精度限制}，\ \textbf{非} \text{结构性封死}（\text{与 (2) 的 C2 结构失败分开记}）✓$$
$$\textbf{(ii)}\ \textbf{模振幅}：\text{显式公式权重}\ \frac{1}{\rho(\rho-s)}\approx\frac{1}{\gamma^2} \Longrightarrow \text{大}\ \gamma\ \text{的模}\ \textbf{指数级小} \Longrightarrow \text{可测高度偏小} \Longrightarrow \text{同向}✓$$
$$\qquad \Longrightarrow\ \text{且}\ \text{`W1`}：\text{即使测出，也只给出"}\textbf{未检测到} \text{"}\ \textbf{而非"排除"}（\textbf{检测}\ne\textbf{排除}）✓✓$$

## §5 `W4-3`（端点分支检验）：**不执行**，登记为检查单

$$\text{唐先生规定}：\text{若}\ \text{`C2`}\ \text{尚未杀死它，再检查是否存在}\ (\Lambda-t)^{1/2}\ \text{型奇性}✓$$
$$\text{本档：}\text{`C2`}\ \text{已 FAIL} \Longrightarrow \textbf{不执行}\ \text{`W4-3`};\ \text{但}\ \textbf{登记检查单} \text{（若将来 C2 复活）：}$$
$$\qquad \text{须查}\ \frac{d}{dt}G_t,\ \frac{d}{d\gamma}G_t\ \text{在端点是否}\ \sim(\Lambda-t)^{-1/2} \Longrightarrow \text{若是则}\ \text{`F3`}\ \text{命中（}\text{`C-111`}\ \text{同墙）}✓✓$$

## §6 判词（按唐先生判词表）

| 结果 | 判定 | 本档 |
|:--|:--|:--|
| `C2` 直接失败 | **DEAD：zero-side encoding** | ⭐ **命中** |
| `C2` 过、端点 `1/2` 奇性 | DEAD：`F3` 吸收 | 未执行（已由上行终止）|
| `C2` 过、无奇性但只得到 `β≤1/2` | `POS1`／RH 等价残留 | 未执行 |
| `C2` 过、无奇性、有独立 arithmetic realization | **真正开放** | ✗ |

$$\Longrightarrow\ \boxed{\text{`W4-1d` DEAD（zero-side encoding）};\ \text{并入}\ \text{`V215` §4}\ \text{逐 }\gamma\ \text{通道}}✓✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 16:3x）`[纪律]`（先跑后写）

```
技术词 读出级失败      命中文件数=1  :: ./C112-W4-1d-three-gate-audit-C2-first-zero-cost-kill.md
技术词 逐点泛函化约     命中文件数=1  :: ./C112-W4-1d-three-gate-audit-C2-first-zero-cost-kill.md
技术词 分辨窗口       命中文件数=1  :: ./C112-W4-1d-three-gate-audit-C2-first-zero-cost-kill.md
技术词 端点分支检验     命中文件数=1  :: ./C112-W4-1d-three-gate-audit-C2-first-zero-cost-kill.md
```
**读数**：写作**前**实跑均 **0 档**（⟹ 四词确为新措辞）；写作**后**复跑各＝**1 档（仅本档）** ✓✓

## §8 边界

- `[档案]` §1 的 `W4-1d` 定义、§3 的 `V188` §2、§4 的 `W1`、`V215` §4 均为**档内引用** ✓
- `[本档]` §2 的 `G` 判读、§3 的零成本判死、§4 的窗口／振幅标度算术为**本档工作** ✓
- ⚠️ §4(i) 的窗口结论**只是标度限制**（可被更大 `U` 推开，代价是灾难性相消），**非**结构封死 ✓
- **不声称**：`W4-1d` 原则上不可能 ✗（只判 `C2` FAIL）；`Λ≤0` 不可证 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未做数值实验**（按唐先生规定）✓；**未用 RH 作推导** ✓

```
⚠️ 唐先生 16:31「开」+ 升级要求: 把下一刀从"验证候选"改成"先验资格审计+分支检验"; 顺序固定 C2 → 端点分支 → RH 信息增益;
   第一刀只做 C2 定义审计**不做数值实验**; 加**零成本判死**(W4-1d =? F({γ_n})); 命名 C-112
✅ 取档: W4-1d 逐字定义 —— A(T)=Σ_{n≤T}Λ(n)/√n(增量前缀和); 主项=2√T−1; δ(T)=A(T)−主项;
   δ_T(s)=−Σ_ρ T^{ρ−s}/(ρ(ρ−s))+… ⟹ 每项 = T^{β−1/2}·e^{i(γ−t)u}, u=log T
   ⟹ u-频率=γ−t(零点位置) | u-增长率=β−1/2(零点偏移); 实算设置: 256 点, T∈[10^5,2×10^8], Δu=0.0298, Δν=0.827;
   结果: ν≈0 背景层(A=1.688) | ν=γ 峰层(0.024–0.063), 动态范围 30–80×
✅ W4-1(定义级): G(γ) = δ_T 在 u=log T 谱中频率 ν=γ 处模的对数增长率; 而 δ_T 的零点侧身份 = **显式公式本身**
   ⟹ G **不是新算术量**(它是显式公式对象的谱读出) ⟹ 落在 V215 §4 的"唯一已知桥"上; 但需查读出是否越出线性层
✅ W4-2(C2) ✗ FAIL(零成本判死): (1) 对象定义纯素数侧 ✓; (2) ⚠️读出层 —— 要得 G(γ) 必须 (i) 定位峰位 ν=γ (峰位就是 γ)
   (ii) 在该频率测逐模指数 ⟹ 分离单个原子 ⟹ 该读出**就是对 {γ_n} 的逐点泛函** ⟹ C2 FAIL;
   (3) 更硬理由(V188 §2): 线性通道饱和, 反演到逐点需**无界精度** —— "分离单个原子"正是该无界精度步 ⟹ 即 S(T) 问题本身;
   (4) 完成并入 V215 §4 逐 γ 通道(不新增入口)
   ⟹ C2 FAIL 理由 = zero-side encoding(读出级) ⟹ 按唐先生规定**无需再跑大规模数据**
   ⚠️ 与 C-107 同址: "改变泛函类型不改变信息通道"(free probability) —— 此处从标量 |δ_T| 改成 log T 谱亦然
✅ 附两项零成本定量发现(纯标度算术, 未做实验):
   (i) 分辨窗口: 峰可分辨 ⟺ 间距 > Δν=2π/U ⟺ log(γ/2π)<U ⟺ **γ < 2πe^U**;
       W4-1d 设置 U=7.60 ⟹ γ<2πe^7.6≈1.3×10^4; 而已验证高度 γ≤3.000175×10^12 ⟹ **可分辨高度深在已验证范围内** ⟹ **窗口空洞**
       (同型先例: C-46/C-62); ⚠️诚实: 窗口随 U 增大, 要越过需 U≳27(素数数据比 e^27≈5×10^11 且要从 ~2√T 提取微小涨落 ⟹ 灾难性相消)
       ⟹ 此项是**标度/精度限制**, 非结构性封死(与 C2 的结构失败分开记)
   (ii) 模振幅: 权重 1/(ρ(ρ−s)) ≈ 1/γ² ⟹ 大 γ 的模指数级小 ⟹ 可测高度偏小 ⟹ 同向; 且 W1: 即使测出也只给"未检测到"而非"排除"(检测≠排除)
✅ W4-3(端点分支): **不执行**(C2 已 FAIL), 但登记检查单(若将来 C2 复活须查 dG_t/dt、dG_t/dγ 在端点是否 ~(Λ−t)^{−1/2} ⟹ 则 F3 命中)
⭐ 判词(按唐先生表): C2 直接失败 ⟹ **W4-1d DEAD: zero-side encoding**; 并入 V215 §4 逐 γ 通道
⚠️ 边界: W4-1d 原则上不可能 ✗(只判 C2 FAIL); 未做数值实验(按规定); 未用 RH 作推导
✅ 净产出: ①W4-1d 逐字定义与导出 ②W4-1 G(γ) 判读(非新算术量) ③⭐C2 FAIL(零成本判死, 读出级 zero-side encoding + V188 无界精度理由) ④两项零成本定量发现(分辨窗口 γ<2πe^U ⟹ 窗口空洞; 振幅 1/γ²) ⑤W4-3 检查单登记 ⑥并入 V215 §4
```
