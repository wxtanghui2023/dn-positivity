# E95 · ⭐⭐ **Theorem C 证明逐行审计 ＋ 速率判据** ✓ —— 证明【确实逐项分离余项】✓；**判据尖锐：需 $L^{-1}$ 或更好** ⚠️

> 委托 ✓ 唐先生（20:56 指示：逐行审计 Theorem C 证明，找 $S$ 级余项；警惕"整体矩 ⟹ 余项"偷换 ✓）
> 执行 ✓ 小灵｜脚本 ✓ `scripts/E95_rate_thresholds.py` ＋ `.txt` ✓
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜**已渲染论文页 927／928／930 供唐先生核对** ✓

---

## 0. 三条结论（✓）

```
✅ **① 证明【确实逐项分离并控制余项】** ✓ —— **唐先生警告的"偷换"在证明里【没有发生】** ✓✓
   页 930 ✓ 逐字："Proof of Theorem B. Taking x = T^{a/k} in Theorem 3, we have …(48) where R1, R2 …"
   ⟹ **(48) 显式给出两个余项 $R_1,R_2$** ✓；**(49) 用 Selberg 渐近公式** ✓；**(50) 用 Theorem 3 估 $R_1$：$\int R_1=O(H)$** ✓；
      **(51) Hölder：$\int=O(H(\log\log T)^{k-0.5})$** ✓；"The theorem follows from (48)-(51)" ✓
   页 931 ✓："**Theorem 4 is the basis of the proof of Theorem C**; in other details it coincides with the proof of Theorem B" ✓
   ⟹ **故 $S$ 级余项界【在证明中存在】** ✓（作为 $(R_1,R_2)$ 的逐项估计 ✓，**非**从整体矩反推 ✓）
⚠️ **② 但【速率】决定生死** ✗ —— 见 §2 表 ✓
   **判据**：$S$ 级余项 $\|R_S\|_2^2=H\cdot M(T)$ ✓ ⟹ **需 $M\ge L^{-1}$（$C\le1.42$ ✓）才 LIVE** ✓
   **仅 $(\log\log T)^{-1/2}$（(51) 式可见速率 ✗）⟹ 需 $C\le0.165$ ⟹ 实质 DEAD** ✗
⚠️ **③ 对象仍未定** ✗：Theorem 4 的求和号内为 $\cos(t\log n)/(\sqrt n\log^2 n)$ ✓（**$\log^2$ ＝ $S_1$ 签名** ✓）
   ⟹ **Theorem 4 疑为 $S_1$ 级** ✗ ⟹ **须以原图裁决** ✓（已附 ✓）
```

## 1. 证明结构（✓ 逐字抽出 ✓）

| 页 | 内容 |
|:--|:--|
| **927** | Theorem 4（对象含 $S_1$ ＋ $\log^2n$ ✗）；其证明"repeat the proof of Theorem 4 in [1]" ✓；Theorem 3 的证明：$x=T^{a/60k}$ ✓，(43) 式分离出 $R_1,R_2,R_3,R_5,R_6,R_7$ ✓ |
| **928** | 把各 $R_j$ 化为统一形式 ✓；引入 $R_4$（含 $\int_{1/2}^{1}(\cdots)du$ ✓）；(44) 式：$\int_T^{T+H}\lvert\sum_{p<x^3}\frac{\sin(t\log p)}{\sqrt p}\rvert^{2k}dt=\sum_{j=1}^{4}K_j$ ✓ |
| **929** | Lemma 12 ⟹ $K_2=O(H)$ ✓；Cauchy＋Hölder 估 $K_3,K_4$ ✓；⟹ $K_j\ll H$ ✓ ⟹ **Theorem 3 证毕** ✓（$y=T^{a/20k}$ ✓） |
| **930** | **§5 Proof of Theorems B, C, D** ✓：Theorem B 取 $x=T^{a/k}$ ✓ ⟹ (48) $R_1,R_2$ ✓ →(49) Selberg 渐近 ✓ →(50) Theorem 3 估 $R_1=O(H)$ ✓ →(51) Hölder ⟹ $O(H(\log\log T)^{k-0.5})$ ✓ |
| **931** | **"Theorem 4 is the basis of the proof of Theorem C"** ✓；Remark：$H=T^a$，$27/82<a<1$ ✓ |

```
⭐ **关键 ✓**：Theorem B 的证明【不】从"整体二阶矩"反推余项 ✗
   —— 它把被积量写成【主体 ＋ 显式余项 $R_1,R_2$】，再逐项控制 ✓✓
   ⟹ **您警示的逻辑陷阱在此【不存在】** ✓ —— 这正是我们需要的那种分解 ✓
```

## 2. ⭐ 速率判据（✓ 脚本产出 ✓）

$$\|R_S\|_2^2=C\cdot H\cdot M(T)\ \Longrightarrow\ \Bigl|\int_IRK\Bigr|\le\sqrt{C}\,H\sqrt{\Lambda_\infty M(T)},\qquad \Lambda_\infty=16.933166,\ H=7.9103\times10^{5}$$

$$\text{预算（允许 }1.062658\times10^{6}-\text{素数侧 }2.401189\times10^{4}\text{）}=1.038646\times10^{6}$$

| $M(T)$ | $\sqrt{\Lambda_\infty M}$ | 余项项（$C=1$） | $\boxed{C_{\max}}$ | 判定 |
|:--|:--|:--|:--|:--|
| $L^{-2}$ ✓（Theorem 4 级 ✓） | $0.2952$ | $2.3351\times10^{5}$ | $\mathbf{19.785}$ | ✅ **LIVE** ✓ |
| $L^{-1}$ ✓ | $1.1021$ | $8.7183\times10^{5}$ | $\mathbf{1.419}$ | ✅ **LIVE** ✓ |
| $L^{-1/2}$ | $2.1296$ | $1.6846\times10^{6}$ | $0.380$ | ⛔ DEAD（除非 $C\le0.38$ ✗） |
| $(\log\log T)^{-1/2}$ ✗（**(51) 可见级** ✗） | $3.2299$ | $2.5549\times10^{6}$ | $0.165$ | ⛔ **DEAD** ✗ |
| $(\log\log T)^{-1}$ | $2.5351$ | $2.0054\times10^{6}$ | $0.268$ | ⛔ DEAD |
| $1$ | $4.1150$ | $3.2551\times10^{6}$ | $0.102$ | ⛔ DEAD |

$$\boxed{\textbf{LIVE}\iff S\text{ 级余项 }\|R_S\|_2^2\ \text{按 }L^{-1}\ \text{或更快衰减}\ \checkmark}$$

## 3. ⚠️ 当前缺口（✓ 精确 ✓）

```
✗ **未定**：Theorem C 的证明中，$S$ 级余项究竟达到哪个速率 ✗：
   · 若证明用 Theorem 4 的 $L^{-2k}$ **原样搬到 $S$ 级** ✓ ⟹ $C_{\max}=19.79$ ✓ **LIVE** ✓✓
   · 若只达到 (51) 式的 $(\log\log T)^{k-1/2}$ ✗ ⟹ $C_{\max}=0.165$ ✗ **DEAD** ✗
   · 若达到 $L^{-1}$ ✓ ⟹ $C_{\max}=1.42$ ✓ **LIVE** ✓
⚠️ **且 Theorem 4 的对象（$S_1$ vs $S$）须以南图裁决** ✓
⟹ **故 20:56 的判据【完全正确】** ✓：**能否从 Theorem C 的证明抽出与 E93 的 $R$ 同对象的 $L^{-1}$ 或更强的界** ✓
⚠️ **未宣布 E93 成立** ✗；**未宣布 T1 已证** ✗
```

## 4. 纪律（✓）

```
✓ **未用 RH** ✓；**未跑 Lean** ✓；R1–R7 ✓（脚本入仓 ✓、输出入仓 ✓、docstring ✓、check_archive ✓）
✓ **附原图** ✓：页 927（Theorem 4）／928（证明）／930（Theorems B,C 证明）—— 供唐先生逐字核对 ✓
```
