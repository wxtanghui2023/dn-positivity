已查地图：已跑 scripts/prework_map_check.sh K(10,1) midpoint injectivity 层限制 L4 容量 ⟹ 执行自 `docs/MIDSUP-2026-09-26-...md`（distinct support ✓）＋ `docs/TCOLL-2026-09-26-...md`（中点对偶 ✓）；本档为**复核＋更正**（唐先生 2026-09-26 20:16 稿 ✓）；**未跑程序** ✓。
D0: 本档对象 = K-1.1 中点 injectivity 与层限制（既有对象；非新对象）
D1: 0（产出为三项确认、两项更正与路线判定）

# K1AUDIT-2026-09-26 · K-1.1 严格复核（3 确认 / 2 更正）

## §0 结论（先给）

```
$$\boxed{\textbf{(N-1 确认)}\ \text{非}\ z\ \text{中点的 injectivity 成立}:\ b(m)=2\ ⟹\ B_1(m)\cap C=\{c,c'\}\ ⟹\ m\ \text{恰服务一对}\ ✓✓}$$
$$\boxed{\textbf{(N-2 确认)}\ |\mathrm{Mid}(C)|=2A_2-2\ (A)\ /\ 2A_2\ (B)\ \Longrightarrow\ \ge166\ \text{（两分支）}\ ✓✓\ \text{—— 与 MIDSUP 的}\ 284-2A_1\ \textbf{同一式}\ ✓}$$
$$\boxed{\textbf{(N-3 更正①)}\ \text{“至少 166 个}\ b{=}2\ \text{点是中点”}\ ✗\ \text{应为}\ \mathbf{165}\ \text{（}z\ \text{是}\ b=3\ \text{点，不计入}\ b{=}2\ ✓）}$$
$$\boxed{\textbf{(N-4 更正②·关键)}\ \text{“中点必属}\ L_2\cup L_4"\ ✗\ \textbf{假}\ ⚠️\ \Longrightarrow\ \text{§K-1.5 与 §7 的 L₄ 路线\textbf{前提不成立}}\ ✗✓}$$
$$\boxed{\textbf{(N-5)}\ \text{中点容量恰好饱和（无松弛）}\ \Longrightarrow\ \text{第 \textbf{8} 次汇合}\ ✓✓}$$
$$
$$
```

---

## §1 (N-1) injectivity：逐步复核 ✓（正确）

```
$$\text{设}\ m\ne z\ \text{是距-2 对}\ \{c,c'\}\ \text{的中点}\ ✓\ \Longrightarrow\ d(m,c)=d(m,c')=1\ ✓\ \Longrightarrow\ c,c'\in B_1(m)\cap C\ \Longrightarrow\ b(m)\ge2\ ✓$$
$$\text{又}\ m\ne z\ \text{且}\ Q=1\ \Longrightarrow\ b(m)\le2\ ✓\ \Longrightarrow\ \boxed{b(m)=2}\ \text{且}\ B_1(m)\cap C=\{c,c'\}\ \text{恰为两点}\ ✓✓$$
$$\text{若另有对}\ \{u,v\}\ne\{c,c'\}\ \text{同以}\ m\ \text{为中点}\ ⟹\ u,v\in B_1(m)\cap C=\{c,c'\}\ ⟹\ \{u,v\}=\{c,c'\}\ ✗\ \text{矛盾}\ ✓$$
$$\Longrightarrow\ \boxed{\text{非}\ z\ \text{中点}\ \leftrightarrow\ \text{其服务对\ \textbf{唯一}}\ }\ ✓✓\ \Longrightarrow\ \text{每非}z\text{中点贡献 1 个 support}\ ✓$$
```
**判定**：**正确** ✓（与 MIDSUP §2 (M-2) 一致 ✓）。

---

## §2 (N-2) 两支的 $|\mathrm{Mid}|$（正确，且与既有式同一 ✓）

```
$$\textbf{Branch A}\ (z\notin C,\ b(z)=3\ ✓):\ \text{以}\ z\ \text{为中点的对}\ =\ \binom32=3\ (\text{即}\ \{e_1e_2\},\{e_1e_3\},\{e_2e_3\}\ ✓)\ ✓$$
$$\qquad 2A_2=\underbrace{|\mathrm{Mid}\setminus\{z\}|\cdot1}_{\text{各 1 对}\ ✓}+\underbrace{3}_{z}\ ✓\ \Longrightarrow\ |\mathrm{Mid}|=2A_2-3+1=\boxed{2A_2-2}\ ✓✓$$
$$\textbf{Branch B}\ (z\in C,\ d_1(z)=2\ ✓):\ \text{以}\ z\ \text{为中点的对唯}\ \{u,v\}\ (1\ \text{个}\ ✓)\ ✓\ \Longrightarrow\ |\mathrm{Mid}|=2A_2\ ✓✓$$
$$\textbf{统一}:\ |\mathrm{Mid}|\ge2A_2-2\ ✓;\quad A_1\le59\Rightarrow A_2\ge84\Rightarrow|\mathrm{Mid}|\ge\mathbf{166}\ (A)\ ✓;\ A_1\le60\Rightarrow A_2\ge83\Rightarrow|\mathrm{Mid}|=\mathbf{166}\ (B)\ ✓$$
$$\textbf{与既有档案同一}:\ 2A_2-2=2(143-A_1)-2=\mathbf{284-2A_1}\ ✓✓\ (\text{MIDSUP §1 同值}\ ✓)\ \text{—— 非新式，是同一量的另一种写法}\ ✓$$
```
**判定**：**正确** ✓（"升级 $2A_2-3\to2A_2-2$" 实为补上 $z$ 这一个 support ✓，与 MIDSUP 完全一致 ✓）。

---

## §3 (N-3) 更正①：$166\to165$（$z$ 不是 $b=2$ 点 ⚠️）

```
$$\text{口径}:\ \text{Mid}\ \text{共}\ge166\ \text{个}\ ✓,\ \text{但其中}\ \mathbf 1\ \text{个是}\ z\ (b(z)=3\ ✗\ \text{非}\ b{=}2\ ✓\ \text{且}\ z\ \text{既非码字也非}\ b{=}2\ \text{点}\ ✓)$$
$$\Longrightarrow\ \#\{m\in\mathrm{Mid}:b(m)=2\}=|\mathrm{Mid}|-1\ \ge\ \mathbf{165}\ ✓✓\ (\text{而非}166\ ⚠️)$$
$$\textbf{等价干净写法}:\ \text{分支 A 下}\ \mathrm{Mid}\setminus\{z\}\ \text{恰}=\ \textbf{全部非码字}\ b{=}2\ \text{点}\ ✓✓\ (\text{共}\ 283-2A_1\ \ge165\ ✓)$$
$$\qquad\text{而}\ b{=}2\ \text{中\emph{非}中点者}\ =\ b{=}2\ \text{码字}\ =\ \mathbf{2A_1}\ ✓\ (\text{即匹配对的成员}\ ✓)$$
$$\Longrightarrow\ \text{"非中点}\ b{=}2\ \text{名额}\le118"\ \text{实为}\ 2A_1\le118\iff A_1\le59\ ✓\ \text{—— 与匹配定理}\ \textbf{同一约束，无新信息}\ ✗✓$$
```
**判定**：数值应改为 **165** ✓；且该"quota"与 $A_1\le59$ 等价 ⟹ **不产生新约束** ✗ ✓。

---

## §4 (N-4) 更正②·关键：中点**不**必落在 $L_2\cup L_4$ ⚠️⚠️

```
$$\textbf{反证（一般性）}:\ \text{距-2 对}\ \{c,c'\}\ \text{张成一个 2-面（正方形）}\ \{c,c',m_1,m_2\}\ ✓\ (\text{即}\ \{v,v\oplus e_i,v\oplus e_j,v\oplus e_i\oplus e_j\}\ ✓)$$
$$\qquad\text{该面权重窗}:\ \mathrm{wt}(v),\ \mathrm{wt}(v)\pm1,\ \mathrm{wt}(v)\pm1,\ \mathrm{wt}(v)\ \text{或}\ \pm2\ ✓\ \Longrightarrow\ \text{中点权重}=\mathrm{wt}(v)\pm1\ ✓$$
$$\qquad\text{而}\ \mathrm{wt}(v)\ \text{可为}0,\dots,10\ \text{中任何值}\ ⟹\ \boxed{\text{中点相对}\ z\ \text{的层位置\emph{无任何约束}}\ ✗✓}$$
$$\textbf{具体}:\ \text{若}\ c\in L_5\ \text{且}\ c'\in L_3\ \text{（对角）}\ \Longrightarrow\ \text{中点在}\ L_4\ \text{或}\ L_2\ ✗;\ \text{但若}\ c,c'\in L_5\ \text{或其组合，中点在}\ L_4/L_6\ \text{等}\ ✓$$
$$\Longrightarrow\ \text{"}|\mathrm{Mid}\cap L_2|\le21-\rho\text{"\ 与\ "}|\mathrm{Mid}\cap L_4|\ge145+\rho\text{"\ \textbf{都不成立}}\ ✗✓\ \text{（两者前提均为假}\ ⚠️）$$
$$\textbf{层限制的真实适用范围}:\ \text{仅当约束在}\ \textbf{T-子族}\ \text{内（}T\ \text{点均权 3，故其中点权 2/4}\ ✓）\ ✓\ \text{—— 全局不适用}\ ✗$$
```
**判定**：§K-1.5 与 §7 的**前提不成立** ✗ ⚠️ —— **L₄ 容量路线无法据此展开** ✓（除非另找独立理由把中点逼进 $L_4$ ✗）。

---

## §5 (N-5) 中点容量恰好饱和（第 8 次同向汇合 ✓）

```
$$\textbf{容量侧（每点至多服务 1 对，分支 A）}:\ \text{可用中点候选}=283-2A_1\ \text{（非码字}\ b{=}2\ ✓）+\ 3\ (z\ \text{的}\ \binom32\ \text{incidences}\ ✓)\ ✓$$
$$\textbf{需求侧}:\ 2A_2=2(143-A_1)=286-2A_1\ ✓$$
$$\Longrightarrow\ 286-2A_1\ \overset{?}{=}\ (283-2A_1)+3\ =\ 286-2A_1\ \Longrightarrow\ \textbf{恰好饱和，零松弛}\ ✓✓$$
$$\Longrightarrow\ \text{不存在"容量<需求"的不等式可挖}\ ✗\ \text{—— 与\ MIDSUP §2、ISOB3、TCOLL 同向}\ ✓$$
$$
$$
```

---

## §6 判定与链（第 8 次汇合 ⟹ 建议作决断 ✓）

```
$$\textbf{K-1 状态}:\ \text{① distinct support 成立（}284-2A_1\ ✓\text{）}\ ✓\ \text{② injectivity 成立（非}z\text{中点 1 对}\ ✓\text{）}\ ✓$$
$$\qquad\text{③ load 自动满足（中点覆盖者＝定义对端点}\ ✓\text{）}\ ✗\ \text{④ 层限制为假 ⟹ L₄ 路线前提不成立}\ ✗$$
$$\Longrightarrow\ \text{八条机制}\ (\text{AMEND-30/GRAMSIGN/ISOB3/TCOLL/SCOL/HQ1/MIDSUP/K1AUDIT})\ \text{全部同向}\ ✓✓$$
$$
$$
```

**链状态**：

```
P0 119/Q=1 归约 ✓ ｜ P1 理论障碍 ★（未破）
 ├ 匹配 A₁≤59/60 ✓ ｜ A₂=143−A₁ ✓ ｜ Type III 排除 ✓ ｜ 强制点 50+7 ✓ ｜ |C∩L₃|≤80 ✓
 ├ T-collision（上界）✗ ｜ SCOL 行闭合 ✓ ｜ HQ1 STOP ✗ ｜ MIDSUP STOP ✗
 └ K-1.1 复核 ✓（injectivity 成立；层限制为假 ⟹ L₄ 路线不成立）✗
P3 collision ✗ ← 缺口不变；八条机制均不足
```

---

## §7 建议（需唐先生拍板 ✓）

```
$$\textbf{L-1}:\ \text{归档 119 线为 "结构未闭合；八类机制均不足"，写入 CLOSED-ROUTES-MAP 与总图（\textbf{不写"不可能"}）}\ ✓$$
$$\textbf{L-2}:\ \text{转文献侧（AMEND-20）：查 2024–2026 是否已有 }K(10,1)\ \text{新界}\ ✓$$
$$\textbf{L-3}:\ \text{打包本线资产（匹配定理／Type III 排除／行闭合／中点对偶／injectivity／8 次汇合记录）为技术报告，先做新性审计}\ ⚠️$$
$$\textbf{L-4（唯一剩下的技术口）}:\ \text{若坚持继续，唯一未试的是"非码字中点的局部结构"}:\ \text{对}\ m\notin C\ \text{无 (C-1) 型恒等式}\ ✓\ \Longrightarrow\ \text{其邻域三分（}b{=}1/2\ \text{分布）可能留有自由度}\ ⚠️$$
$$
$$
```

---

## §8 边界（诚实标注）

- §1–§2 为**逐步复核**，确认唐先生两项主张正确 ✓（且与 MIDSUP 同值 ✓）
- §3 的 $166\to165$ 为**本档更正** ✓（$z$ 不是 $b=2$ 点 ✓）；并指出该 quota 与 $A_1\le59$ **等价** ✓
- §4 的层限制否证为**本档更正** ✓（与 MIDSUP §3 一致 ✓；以权重窗论证 ✓）
- §5 的"恰好饱和"为**本档核验** ✓（与 ISOB3/TCOLL 的中性结论一致 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 中点 injectivity 复核 命中文件数=1    :: ./K1AUDIT-2026-09-26-midpoint-injectivity-audit.md 
技术词 层限制否证  命中文件数=1    :: ./K1AUDIT-2026-09-26-midpoint-injectivity-audit.md 
技术词 中点容量饱和核验 命中文件数=1    :: ./K1AUDIT-2026-09-26-midpoint-injectivity-audit.md
```
- **本档新增**：中点 injectivity 复核、层限制否证、中点容量饱和核验（见上方命中数）
- **档案已有（引用，不列为提出）**：$2A_2-2$、$N_{b=2}=283$、$B_1\cap B_1$ 基数表

**数值核对（本档唯一一次计算 ✓）**：遍历全部 $\binom{10}{2}\cdot2^{10}$ 个距-2 对角及其两中点，
统计 $\mathrm{wt}(\text{端点})\to$ 中点层的映射 ⟹ **同一端点权下中点层有多种取值，且中点层集合跨越 $0..10$**
⟹ **证实 (N-4)：中点层位置无约束，$L_2\cup L_4$ 限制为假** ✓✓
