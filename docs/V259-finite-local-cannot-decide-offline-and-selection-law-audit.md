# V259 · **Horn 1 做成定理 ＋ 选择律审计：残余压缩为单一性质「非聚合组合律」** —— ⭐⭐ **V258 §4 降级（本档，唐先生技术边界）**：**"global coupling ⇒ L-值"比现有证据强**，不得写成定理；正确形式＝四类清单 ✓✓；⭐⭐⭐⭐ **定理 V259-A（本档，可证、初等、不用 RH）**：$$\boxed{\text{有限局部数据}\ \textbf{不能} \text{决定 off-line collision}}$$ 构造：$F_\sigma(s):=\zeta(s)\big(1-q^{\sigma-s}\big)$（$q>P$ 素数）⟹ 零点含 $s=\sigma+\frac{2\pi ik}{\log q}$，**在 $\Re s=\sigma$ 上无穷多个**，而 $p\le P$ 处局部 Euler 因子**完全不变** ⟹ **任意有限局部窗口都可被一个远处局部因子骗过** ✓✓✓✓；⭐⭐ **反转（采纳）**：真正的二分**不是**局部 vs 全局，而是 $$\boxed{\text{有限可判定}\quad\text{vs}\quad\text{无限极限选择}}$$ ✓✓✓；⭐⭐⭐⭐ **选择律审计（本档）**：$F$ 若"置换不敏感＋因子独立＋连续＋有限和积／绝对收敛组合" ⟹ 只能依赖**聚合量** $\sum_p f,\prod_p g$ ⟹ 回 `V234`–`V236`；**而四条假设的否定已全部被本档案覆盖**（`V241`-D／`V236`／`V147`-`V210`）⟹ $$\boxed{\text{残余}\ =\ \textbf{单一性质}：\text{非聚合组合律（non-aggregable combination law）}}$$ ✓✓✓✓；⭐⭐⭐⭐ **残余最锐形式**：一个 **canonical 的"局部状态全球兼容性"**，其**失败 ⟺ off-line**（Selmer 型，但**非上同调、非聚合**）✓✓✓✓

> 委托 ✓ 唐先生 2026-09-15 22:48：**"V258 第一步是对的……但第 4 节目前还不能叫'墙体定理'，因为'全局耦合全部实现于 L-值面'明显比现有证据强。"** ＋ **V259 两刀**（第一刀把 Horn 1 做成可证定理；第二刀审计无限极限的选择律）＋ **G1–G3** ＋ **判死标准** ✓✓
> 纪律 ✓ **不造新模型**；未用 RH 作推导 ✓（**本档定理为 RH-free**）；未跑 Lean ✓；**零数值** ✓｜编号 ✓ **V259**

---

## §1 ⚠️ **V258 §4 降级（唐先生技术边界，逐字采纳）**

$$\textbf{不得写}：\text{"global coupling}\Longrightarrow L\text{-值"} \qquad（\textbf{比现有证据强}）✓✓$$
$$\textbf{正确形式}：\boxed{\text{目前已知的 canonical global compatibility}\ \subset\ \begin{cases}\text{(a) cohomological obstruction}\\\text{(b) class-group／Selmer 型}\\\text{(c) L-值／automorphic measurement}\\\text{(d) explicit spectral coupling}\end{cases}} ✓✓✓$$
$$\qquad ⚠️\ \textbf{只有 (d) 直接触碰 $\beta$};\ \text{Selmer 反例只证明}\ \text{global}\ne\text{local factorized},\ \textbf{未证明}\ \text{global}\Longrightarrow L\text{-值} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{V258 §4 由"墙体定理"降级为"候选／观察"};\ \text{G1–G3 也}\ \textbf{不要求} \text{住在 (c)} ✓✓$$

## §2 ⭐⭐⭐⭐ **定理 V259-A（本档，可证、初等、RH-free）：有限局部数据不能决定 off-line collision**

$$\textbf{"有限局部可判定"的严格化（采纳唐先生形式）}：\text{机制只读取}\ \mathcal L_{P,N}=\{\ell_p(n):p\le P,\ n\le N\},\ \text{判定为}\ C_{P,N}=F_{P,N}(\mathcal L_{P,N}) ✓$$
$$\qquad \text{即}\ \boxed{\text{有限阶段输出只依赖有限局部坐标}} \qquad（\text{`V205` 型"有限记忆／有限局部规则"的严格版}）✓$$

$$\textbf{构造（本档）}：\text{取素数}\ q>P，\text{定义}\qquad \boxed{F_\sigma(s):=\zeta(s)\big(1-q^{\sigma-s}\big)} ✓✓$$
$$\qquad \text{因子}\ 1-q^{\sigma-s}=0\iff q^{\sigma-s}=1\iff\sigma-s=\frac{2\pi ik}{\log q} \iff \boxed{s=\sigma+\frac{2\pi ik}{\log q}\quad(k\in\mathbb Z)} ✓✓✓$$
$$\qquad \Longrightarrow \text{它在}\ \Re s=\sigma\ \text{上有}\ \textbf{无穷多个零点};\ \text{取}\ \sigma\in(0,1),\ \sigma\ne\tfrac12 \Longrightarrow \textbf{全部 off-line} ✓✓✓$$
$$\qquad \text{而}\ p\le P\ \text{处：}\text{Euler 局部因子}\ \textbf{完全不变}（\text{因子只在}\ q\ \text{处改动}）\Longrightarrow \mathcal L_{P,N}(F_\sigma)=\mathcal L_{P,N}(\zeta)\ \textbf{逐坐标相同} ✓✓✓$$

$$\textbf{定理（V259-A）}：\text{对任意}\ P,N\ \text{与任意}\ \sigma\in(0,1)，\text{存在算术对象与}\ \zeta\ \text{在}\ (P,N)\text{-局部数据上}\ \textbf{完全一致}，\ \text{却在}\ \Re s=\sigma\ \text{上有}\ \textbf{无穷多个零点} ✓✓✓$$
$$\qquad \Longrightarrow \boxed{\text{有限局部数据}\ \textbf{不能决定}\ \text{off-line collision}}\qquad（\text{也不决定其否定}）✓✓✓✓$$
$$\qquad \textbf{性质}：\textbf{初等、可证、不用 RH、无统计论证} ✓✓✓$$
$$\qquad ⭐\ \textbf{与本档案一致}：\text{这正是}\ \text{`V220`}\ \text{的乘子族}\ 1-am^{-s}\ \text{与}\ \text{`V233`-C}\ \text{的同一机制}（\text{零点可取任意}\ \Re s=\log|a|/\log m\text{）};\ \textbf{本档把它用于"骗过有限局部窗口"} ✓✓✓$$

## §3 ⭐⭐⭐ **反转（采纳）：真正的二分不是"局部 vs 全局"**

$$\text{若机制允许读取}\ \textbf{全部无限多个} \text{局部因子再做}\ \textbf{真正的全局极限}：\ C_\infty=\lim_{P\to\infty}C_P，\ \text{则}\ q\ \text{虽能逃出任何固定}\ P，\ \textbf{但最终必然被看到} ✓✓$$
$$\qquad \Longrightarrow \textbf{V259-A 不能推出原始 Horn 1}（\text{"纯局部／因子化机制不能产生 off-line collision"}）✓✓$$
$$\Longrightarrow \boxed{\text{真正的二分}：\textbf{有限可判定}\quad\text{vs}\quad\text{无限极限选择}} ✓✓✓✓$$

## §4 ⭐⭐⭐⭐ **选择律审计（第二刀）：残余压缩为「非聚合」**

$$\text{设}\ C_P=F(\ell_p:p\le P)\ \text{有极限}\ C_\infty;\ \text{若}\ F\ \text{满足}：$$
$$\qquad \text{(1)}\ \textbf{置换不敏感};\quad \text{(2)}\ \textbf{各素数因子独立};\quad \text{(3)}\ \textbf{连续};\quad \text{(4)}\ \textbf{只通过有限和、有限积、绝对收敛极限组合} ✓$$
$$\qquad \Longrightarrow \text{只能依赖}\ \textbf{密度／总量型量}：\ \sum_p f(\ell_p),\ \prod_p g(\ell_p),\ \text{或其有限层复合} ⟹ \textbf{回 `V234`–`V236`}：$$
$$\qquad \qquad \boxed{\text{无限局部聚合}\ \longrightarrow\ \text{Euler／Dirichlet aggregate}\ \longrightarrow\ \text{density／explicit-formula interface}} ✓✓✓$$

$$\textbf{⭐ 本档新增（关键）：四条假设的}\textbf{否定} \textbf{已全部被本档案覆盖}：$$

| 否定的哪一条 | 开放的形状 | 已封于 |
|:--|:--|:--|
| ✗ (1) 置换不敏感 | 顺序敏感 ⟹ 需 canonical 序／canonical 非交换性 | **`V241`-D**（算术非交换性＝互反律＝coboundary ⟹ 平凡） |
| ✗ (2) 因子独立 | 跨素数耦合 | **`V236`**（C 类关系解析上回落到统计；唯一桥＝显式公式） |
| ✗ (3) 连续 | 不连续 ⟹ 选择／超滤／序 | **`V147`／`V210`**（序路线不存在；T1/T2） |
| ✗ (4) 有限和积／绝对收敛 | **真正非可聚合的组合** | — **唯一残余** |

$$\Longrightarrow \boxed{\text{残余}\ =\ \textbf{单一性质}：\text{非聚合组合律（non-aggregable combination law）}} ✓✓✓✓$$
$$\qquad \text{即：它必须决定}\ (\ell_2,\ell_3,\ell_5,\dots)\longmapsto\ \textbf{一个不能分解成局部聚合的全局状态}，\ \text{且}\ \textbf{不是}\ \prod_p A_p\ \text{或}\ \sum_p B_p ✓✓✓$$

## §5 **G1–G3 登记 ＋ 判死标准（采纳）**

$$\textbf{G1}：\textbf{不是有限阶段可见}（\text{否则 V259-A 杀掉}）✓$$
$$\textbf{G2}：\textbf{不是可加／可乘聚合}（\text{否则回 `V234`–`V236`}）✓$$
$$\textbf{G3}：\textbf{不是现有 cohomological obstruction 的重命名}（\text{否则回 Brauer／Selmer／Ш／class group／reciprocity ＝ `V193`–`V198`／`V241`}）✓✓$$

$$\textbf{判死标准（采纳）}：\text{若}\ \mathcal G\ \text{能写成}\ \lim_{n\to\infty}F_n\ \text{且每个}\ F_n\ \text{为有限局部聚合} \Longrightarrow \text{必须继续证明该极限}\ \textbf{是否只是某个 Dirichlet／Euler aggregate 的另一种表示}：$$
$$\qquad \text{是}\ \Longrightarrow \textbf{DEAD，回 `V236`};\qquad \text{否}\ \Longrightarrow \textbf{第一次得到一个不属于旧 archive 的全局算术机制} ✓✓✓$$

## §6 ⭐⭐⭐⭐ **残余的最锐形式（本档提炼）**

$$\text{把 §4 的"非聚合"与 §5 的 G1–G3 合起来}，\ \text{残余只剩一个形状}：$$
$$\qquad \boxed{\text{一个}\ \textbf{canonical} \text{的}\ \textbf{"局部状态全球兼容性"},\ \text{其}\ \textbf{失败}\iff\text{off-line}} ✓✓✓✓$$
$$\qquad \text{（即 Selmer 型："处处局部可解、整体无解"，但要求}\ \textbf{非上同调、非聚合} \text{，且"无解"由}\ \textbf{canonical 算术} \text{给出}）✓✓$$
$$\qquad \text{⭐ 注意它与 V257 §3 的碰撞刻划}\ \textbf{不是同一句}：\text{那里是"碰撞存在"（}\text{存在性}），\ \text{这里是"}\textbf{兼容性失败} \text{"（}\Pi_1\ \text{型否定}）⟹ \text{本档把它换成}\ \textbf{更可判定的形式} ✓✓✓$$

$$\textbf{下一步的审计（可判定，本档建议）}：\boxed{\text{"无限局部兼容性"能否脱离聚合／上同调／显式公式三者？}} ✓✓✓$$
$$\qquad \text{逐条可做}：\text{(i) 写出最小非聚合组合律的候选形状};\ \text{(ii) 逐条检验 G1–G3};\ \text{(iii) 检验判死标准（有限聚合极限？）} ✓$$

## §7 判词 ＋ 状态表 ＋ 边界

$$\boxed{\textbf{V259}：\text{V258 §4 降级};\ \textbf{定理 V259-A 成立（有限局部不够）};\ \text{二分改为"有限可判定 vs 无限极限选择"};\ \text{残余压缩为}\ \textbf{单一性质"非聚合组合律"};\ \text{最锐形式＝canonical 全球兼容性的失败}} ✓✓✓$$

| 项 | 判定 | 依据 |
|:--|:--|:--|
| "global coupling ⇒ L-值" | ✗ **降级**（比证据强） | 本档 §1（唐先生） |
| 有限局部能否决定 off-line | ✗ **不能（定理）** | 本档 §2（V259-A） |
| 二分 | **有限可判定 vs 无限极限选择** | 本档 §3 |
| $F$ 四假设 ⟹ | 聚合成 Euler／Dirichlet ⟹ `V234`–`V236` | 本档 §4 |
| 四假设的否定 | **全部已封**（`V241`-D／`V236`／`V147`-`V210`） | 本档 §4 |
| 残余 | ⭐ **单一性质：非聚合组合律** | 本档 §4 |
| 残余最锐形式 | **canonical 全球兼容性的失败 ⟺ off-line** | 本档 §6 |
| 是否造新模型 | ✗ **否**（唐先生明令） | — |

$$\textbf{边界（诚实）}：\S2\ \text{的构造与计算}\ \textbf{为本档推导（初等，复核：}1-q^{\sigma-s}=0\iff s=\sigma+2\pi ik/\log q\text{；}p\le P<q\ \text{处 Euler 因子不变）} ✓✓;\ \S4\ \textbf{四条假设的否定全部已封} \text{中，"}\`V241\text{-D／}\`V236\text{／}\`V147\text{-}\`V210"\ \text{的对应为}\ \textbf{本档整理}，\ \text{各条本身是既有结论} ✓;\ \S4\ \text{的"四假设 ⟹ 聚合"是}\ \textbf{[结构性] 论证（依赖 (1)–(4) 的完整清单，本档未证明清单完备）} ⚠️;\ \S6\ \text{为}\ \textbf{本档提炼};\ \textbf{未用 RH};\ \text{未跑 Lean};\ \textbf{零数值} ✓$$

```
⚠️ 委托（唐先生 22:48）：V258 第一步对（打掉了错误命题）；但第 4 节还不能叫"墙体定理"——
   "全局耦合全部实现于 L-值面"明显比现有证据强
   V259 两刀：① 把 Horn 1 切成可证定理（严格化"有限局部可判定"＝只读 L_{P,N} 的有限函数
   C_{P,N}=F_{P,N}(L_{P,N})）；② 无限极限要产生新信息必须有选择律
   反转：真正的二分不是"局部 vs 全局"，而是"有限可判定 vs 无限极限选择"
   Selmer 的价值：局部可解 ⇏ 整体可解 ⟹ 需要 local states --global compatibility--> global state
   三条件 G1 不是有限阶段可见；G2 不是可加/可乘聚合；G3 不是现有 cohomological obstruction 的重命名
   ⚠️ G1–G3 并不要求它住在 L-值面 ⟹ 建议把 V258 §4 降级：
   不能写 global coupling ⇒ L-value；正确的是"目前已知的 canonical global compatibility ⊂
   {cohomological obstruction, class-group/Selmer 型, L-值/automorphic measurement, explicit
   spectral coupling}"，其中只有最后一类直接触碰 β
   判死标准：G 若能写成 lim F_n 且每个 F_n 为有限局部聚合 ⟹ 必须证明该极限是否只是某个
   Dirichlet/Euler aggregate 的另一种表示；是 ⟹ DEAD 回 V236；否 ⟹ 第一次得到不属于旧 archive
   的全局算术机制
   下一步不是造模型，而是审计："无限局部兼容性"能否脱离聚合/上同调/显式公式三者？
⚠️ §2 定理 V259-A（本档，初等、RH-free、可证）：取素数 q>P，F_σ(s):=ζ(s)(1−q^{σ−s})；
   因子零点 ⟺ σ−s=2πik/log q ⟺ s=σ+2πik/log q ⟹ 在 Re s=σ 上无穷多个零点；
   取 σ∈(0,1)、σ≠1/2 ⟹ 全部 off-line；而 p≤P 处 Euler 局部因子完全不变 ⟹ L_{P,N}(F_σ)=L_{P,N}(ζ)
   ⟹ 对任意 P,N 与任意 σ，存在算术对象与 ζ 在 (P,N)-局部数据上完全一致却在 Re s=σ 上有无穷多零点
   ⟹ 有限局部数据不能决定 off-line collision（也不决定其否定）
   ⭐ 与本档案一致：这正是 V220 的乘子族 1−am^{−s} 与 V233-C 的同一机制
⚠️ §3 反转：若机制读全部无限多个局部因子再做真正全局极限（C_∞=lim C_P），q 最终必被看到
   ⟹ V259-A 不能推出原始 Horn 1 ⟹ 真正的二分：有限可判定 vs 无限极限选择
⚠️ §4 选择律审计：F 若(1)置换不敏感(2)因子独立(3)连续(4)只通过有限和/积/绝对收敛极限组合
   ⟹ 只能依赖聚合量 Σ_p f、Π_p g ⟹ 回 V234–V236（无限局部聚合→Euler/Dirichlet aggregate→
   density/explicit-formula interface）
   ⭐ 本档新增（关键）：四条假设的否定全部已被本档案覆盖 ——
   ✗(1) 顺序敏感 ⟹ V241-D（算术非交换性＝互反律＝coboundary 平凡）
   ✗(2) 跨素数耦合 ⟹ V236（C 类关系解析上回落到统计；唯一桥＝显式公式）
   ✗(3) 不连续 ⟹ V147/V210（序路线不存在）
   ✗(4) 真正非可聚合组合 ⟹ 唯一残余
   ⟹ 残余 = 单一性质：非聚合组合律（必须决定 (ℓ_2,ℓ_3,…) → 不能分解成局部聚合的全局状态，
   且不是 Π_p A_p 或 Σ_p B_p）
⚠️ §5 G1–G3 登记 + 判死标准：G 若能写成 lim F_n 且每个 F_n 为有限局部聚合 ⟹ 须证明该极限是否只是
   Dirichlet/Euler aggregate 的另一表示；是 ⟹ DEAD 回 V236；否 ⟹ 第一次得到非旧 archive 的全局机制
⚠️ §6 残余最锐形式：一个 canonical 的"局部状态全球兼容性"，其失败 ⟺ off-line（Selmer 型，但要求
   非上同调、非聚合）；⭐ 与 V257 §3 的碰撞刻划不同：那是"碰撞存在"（存在性），这是"兼容性失败"
   （Π_1 型否定）⟹ 换成更可判定的形式
   下一步审计（可判定）："无限局部兼容性"能否脱离聚合/上同调/显式公式三者？
⚠️ §7 边界：§2 构造与计算为本档推导（初等）；§4 的对应关系为本档整理；§4 的"四假设 ⟹ 聚合"是
   [结构性] 论证（未证明清单完备）；§6 为本档提炼；未用 RH；未跑 Lean；零数值
✅ 净产出：① V258 §4 降级 + 正确四类清单（技术边界）
   ② 定理 V259-A：有限局部数据不能决定 off-line collision（初等、RH-free、可证）
   ③ 二分改为"有限可判定 vs 无限极限选择"
   ④ 选择律审计：四假设 ⟹ 聚合；且四假设的否定全部已封 ⟹ 残余压缩为单一性质"非聚合组合律"
   ⑤ 残余最锐形式：canonical 全球兼容性的失败 ⟺ off-line
   ⑥ 下一步可判定审计：无限局部兼容性能否脱离聚合/上同调/显式公式
```


---

## 【型标注】（`NEG-REGISTER-1`，2026-09-18 20:1x）

$$\text{本档定级}：\textbf{T-V}\ \text{（诊断性判据：判死标准为启发式，无定理）}✓$$
$$\qquad \text{内容}：\textbf{"可写成}\ \\lim F_n\（\text{有限局部聚合}）\Longrightarrow\text{DEAD"}\ \text{是}\ \textbf{启发式判据}✓✓$$
$$\qquad ⚠️\ \text{无证明};\ \text{残余压成}\ \textbf{"非聚合组合律"}\ \text{（未实例化）}✓$$
$$\qquad \Longrightarrow \text{可作}\ \textbf{筛子};\\ \textbf{不得} \text{引为"有限局部路线已被证明不可能"}✓$$
$$\textbf{引用纪律（本档确立）}：\text{引用本档时必须}\ \textbf{随引其型};\ \textbf{不得} \text{去条件化引用}✓✓$$
