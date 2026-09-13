# E99 · ⭐⭐⭐ **$T^2$ 律的机制（已解 ✓）＋ K1 的尖锐形式** —— E30-2 待查项**闭合** ✓

> 委托 ✓ 唐先生 21:18 "继续" ✓（＝ 切 K1：找 $h(n)$ 优于 $\sqrt n$ 的转换定理 ✓）
> 执行 ✓ 小灵｜脚本 ✓ `scripts/E99_onset_mechanism.py` ＋ `.txt` ✓
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 三条结论（✓）

```
⭐⭐⭐ **① $T^2$ 律的机制【已解】✓** —— E30 §2 的"待核"项 ✓ 现闭合 ✓：
   $$\text{离轴零点 }(\beta,\gamma)\ (\varepsilon=\beta-\tfrac12)\ \Longrightarrow\ \text{配对伙伴 }(\tfrac12-\varepsilon,\gamma)\ \text{的项按}\ \exp(\varepsilon n/\gamma^{2})\ \textbf{指数增长}\ ✗$$
   $$\Longrightarrow\ \textbf{起始指标}\ n_0=\frac{\gamma^{2}\log M}{\varepsilon}\ \ \xrightarrow{\ \varepsilon=O(1)\ }\ \ n_0\sim\gamma^{2}\ \Longrightarrow\ \textbf{T}^2\ \text{律}\ \checkmark$$
⭐⭐ **② 对 K1 的判定（负向但结构性 ✓）**：**任何只消费"高度 $T$ 以内无离轴零点"的判据，都必须按最坏情况 $\varepsilon=O(1)$ 定标 ⟹ $T^2$ 是【被迫的】** ✓✓
   ⟹ **K1 的"找 $h(n)$ 优于 $\sqrt n$"在此输入类下【答案是负的】** ✗ ⟹ **改进必须换【输入】** ✓（E30 §3 的第二支 ✓）
⭐ **③ 尖锐的开放形式（新 ✓）**：找一个**起始指标按 $\gamma^{p}/\varepsilon^{q}$ 且 $p<2$** 的判据 ✓
   —— 即**对"近线零点"更敏感**的判据 ✓ —— 若存在 ⟹ **对一切 $\varepsilon$ 都优于 $T^2$** ✓✓
```

## 1. 机制推导（✓ 初等 ＋ 40 位数值检验 ✓）

$$\rho'=\tfrac12-\varepsilon+i\gamma\quad(\varepsilon>0),\qquad q'=1-\frac1{\rho'},\qquad |q'|=\frac{|{\rho'-1}|}{|{\rho'}|}=\frac1r$$
$$r^{2}=\frac{(\tfrac12-\varepsilon)^{2}+\gamma^{2}}{(\tfrac12+\varepsilon)^{2}+\gamma^{2}}\ \Longrightarrow\ 1-r=\frac{\varepsilon}{(\tfrac12+\varepsilon)^{2}+\gamma^{2}}\Big/\ (1+r)\cdot 2\ \approx\ \boxed{\frac{\varepsilon}{\gamma^{2}}}$$

$$\text{配对项贡献}\ \sim|q'|^{n}=r^{-n}\approx\exp\!{\Bigl(\frac{\varepsilon n}{\gamma^{2}}\Bigr)}\ \ \textbf{指数增长}\ ✗\ \Longrightarrow\ n_0=\frac{\gamma^{2}\log M}{\varepsilon}\ \checkmark$$

| 检验 ✓ | 结果 |
|:--|:--|
| $1-r$ vs $\varepsilon/\gamma^{2}$ | 比值 → **1.00000** ✓（$\gamma=10^{3}\sim10^{6}$ ✓） |
| $|q_{\rm in}|\cdot|q_{\rm out}|-1$ | $\mathbf{0.000e+00}$（**40 位 ✓** —— 函数方程配对使模长**严格互逆** ✓✓） |
| $n_0$（$\gamma=10^{6}$、$M=10^{2}$） | $\varepsilon=0.5$：$9.2\times10^{12}$ ✓；$\varepsilon=0.1$：$4.6\times10^{13}$ ✓；$\varepsilon=0.01$：$4.6\times10^{14}$ ✓ |

$$\boxed{\text{最坏情况 }\varepsilon=O(1)\ \Longrightarrow\ n_0\sim\gamma^{2}\ (\text{modulo}\ \log)\ \Longrightarrow\ \textbf{E30 律 I 的机制} = \textbf{离轴配对的指数增长起始点}}$$

## 2. ⭐ 为什么 $T^2$ 是**被迫的**（✓ K1 的负向判定 ✓）

```
【论证 ✓】"RH 验证至高度 $T$" ≡ 一条【不存在性】信息 ✗：**在 $\gamma\le T$ 内无离轴零点** ✓
   ⟹ 此信息**完全不携带 $\varepsilon$ 的大小** ✗（只知"没有" ✓，不知"若有会多近" ✓）
   ⟹ 任何仅消费该信息的判据，必须在**所有允许的构型**上成立 ✓
   ⟹ 而允许构型含 $\varepsilon=O(1)$（**粗离轴** ✗）⟹ 起始指标 $n_0\sim\gamma^{2}$ ✓
   ⟹ $$\boxed{\text{故对}\ \gamma\ \text{的敏感度必然是二次的}\ \Longrightarrow\ \textbf{T}^2\ \text{无法在不换输入的前提下改进}}$$
【⭐ 反向的同一发现 ✓】**近线离轴零点是盲区** ✗：$\varepsilon\ll1$ 时 $n_0=\gamma^{2}/\varepsilon\cdot\log M$ **远大于** $\gamma^{2}$ ✓
   ⟹ 判据**对它们迟钝** ✓ ⟹ 这与经典困难（"近线零点难排除" ✓）**结构一致** ✓✓
```

## 3. ⭐⭐ K1 的**尖锐形式**（本轮新产出 ✓）

$$\boxed{\text{找判据，其【起始指标】}\ n_0(\gamma,\varepsilon)\ \text{按}\ \frac{\gamma^{p}}{\varepsilon^{q}}\ \text{且}\ p<2\ \text{（"对近线零点更敏感"）}}$$

$$\text{若存在}\ p<2\ \Longrightarrow\ \text{对【一切】}\varepsilon\ \text{都优于 }T^{2}\ \checkmark\checkmark\qquad\text{（律 I 的边界被打破 ⟹ 真突破 ✓）}$$

**待查的候选族** ✓（每条须给出其 $n_0(\gamma,\varepsilon)$ 标度 ✓）：

| 候选 | 出处 | 已知/待查 |
|:--|:--|:--|
| **$\tau$-Li 判据族** | Palojärvi（arXiv:1807.01506 ✓，项目已归档 ✓） | 待查其 $n_0$ 标度 ✓ |
| **高阶 Li** $\lambda_n^{(m)}$ | 经典／Bombieri–Lagarias ✓ | 待查 ✓ |
| **Jensen–Pólya** $J^{d,n}$ | GORZ（A2 ✓，$T^2$ ✓） | $n_0$ 标度待查 ✓（$d$-$n$ 双指标 ✓） |
| **衍生态**（$\xi^{(k)}$） | GORZ Hermite 建模 ✓（derivative aspect ✓） | ⭐ **"高度"定义不同 ⟹ 标度可能不是 $T^2$** ✓✓ |
| ⭐⭐ **函数域对照** | 函数域 RH **已证** ✓ ⟹ 其 Li 型判据**无条件** ✓ | ⭐ **最锐工具 ✓**：对照可判定 $T^2$ 是**数域特有**还是**内在** ✓✓ |
| $M(x)/\psi(x)-x$/Farey 型 | 经典 ⟺ RH ✓ | ⚠️ 多为**渐近**判据 ✗，**无有限高度转换** ✗ ⟹ 不入 $h(n)$ 框架 ✓ |

## 4. 边界与纪律（✓）

```
⚠️ **本推导为【启发式起始估计】✗** —— 它**解释**了 $T^2$ 律为最坏情况 ✓，但**不是**"任何仅消费验证高度的判据都不能优于 $T^2$"的证明 ✗
   （宪法纪律 ✓："未找到"≠"不存在" ✓ —— 此处同理："已解释"≠"已证明被迫" ✓）
✓ **自我更正 1 处 ✓**：初稿写 $1-r\approx2\varepsilon/\gamma^{2}$ ✗ —— **数值检验当场抓到因子 2** ✓ ⟹ 更正为 $\varepsilon/\gamma^{2}$ ✓
   （项目纪律"先怀疑自己的实现" ✓ 再次生效 ✓）
✓ **未用 RH** ✓；**未跑 Lean** ✓；**E30-2 待查项现已闭合** ✓（机制已给出 ✓）
✓ **未宣布 K1 已判死** ✗ —— 只判**"仅消费验证高度"这一输入类** ✗；换输入（定量零自由区／矩／零点实际位置 ✓）**仍开放** ✓
```

## 5. 对 E30 框架的两处**更新建议** ✓

```
【更新 1 ✓】E30 §2 的"⚠️ 待核：Li 的线性关系 vs $T^2$" —— **已解** ✓：
   表面线性（$n/\gamma$ 的【相位】✓）**不**决定检测能力 ✗；
   检测能力由**指数起始点** $n_0=\gamma^{2}/\varepsilon\cdot\log M$ 决定 ✓
【更新 2 ✓】E30 §3 的突破判据应**加一行** ✓：
   $$\text{突破必要条件：判据的 }n_0(\gamma,\varepsilon)\ \text{须按}\ \gamma^{p}/\varepsilon^{q},\ p<2$$
   （**仅看 $h(n)$ 不够** ✗ —— 必须看**对 $\varepsilon$ 的敏感度** ✓）
```
