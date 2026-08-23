# 文献发现：FSZ/Fujii 的零点分布框架（2026-08-23 18:50）

> 状态：✅ 文献定位完成——FSZ 给了我们"相位均匀性"的现成研究框架
> 关键：他们的公式解释了我们发现的 Σcos 线性 + 给 Σx^{iγ} 无条件界

## 1. 核心文献

1. **Fujii (1978)**：On the uniformity of the distribution of the zeros of ζ（J. reine angew. Math. 302）——均匀分布 + discrepancy
2. **Fujii (2002)**：On the Discrepancy Estimates of the Zeros of ζ——D_{N(T)} = O(loglog T/log T)（无条件）
3. **Ford-Zaharescu (2005)**：On the distribution of imaginary parts of zeros of ζ（J. reine angew. Math. 579）——Lemma 1 核心公式
4. **Ford-Soundararajan-Zaharescu (2009)**：...II（Math. Ann. 343）——Σx^{iγ} 无条件界 + 显式公式连接
5. **Ford-Meng-Zaharescu**：Simultaneous Distribution of Fractional Parts——多 α 联合分布
6. **Murahara-Onozuka (2025)**：arXiv:2510.07710——计数函数渐近 ⟹ 均匀分布（广义）
7. **Hlawka**：RH 下 D = O(1/log T)

## 2. FSZ Lemma 1——核心显式公式（2005）

$$\sum_{0<\gamma\le T} x^\rho = -\frac{\Lambda(n_x)}{2\pi}\cdot\frac{e^{iT\log(x/n_x)}-1}{i\log(x/n_x)} + O\left(x\log^2(2xT) + \frac{\log 2T}{\log x}\right)$$

其中 n_x = 离 x 最近的素数幂。**x 为素数幂时**：主项 = −T·Λ(x)/(2π)。

**这解释了我们发现的 Σcos(γ_k log p) ~ c_p·K 线性**（p 素数——主项 −T·log p/(2π)——实数——贡献给 cos 部分——线性增长）！

## 3. FSZ II 无条件界（2009）

$$\sum_{0<\gamma\le T} x^{i\gamma} \ll_\varepsilon T\cdot x^{-1/2+\varepsilon} + T^{1/2}x^\varepsilon$$
（对所有 x, T ≥ 2 一致——无条件）

**对 x = p（素数）**：|Σp^{iγ}| ≤ T·p^{−1/2+ε} + T^{1/2}p^ε——**T 量级——弱**（我们数值 O(1)）——差距 = 相位均匀性 = RH。

## 4. 关键公式链（(3.8)——零密度方法）

$$\sum_{0<\gamma\le T}(x^{i\gamma} - x^{\rho-1/2}) \ll T\log^2 x/\log T$$

- Σx^{ρ−1/2} = x^{−1/2}·Σx^ρ——用 Lemma 1 的显式公式
- 离轴零点贡献用**零密度估计**（Ingham：N(σ,T) ≪ T^{2(1−σ)/3+ε} 等）——**无条件**
- **连接**：零点指数和 ⟺ 显式公式 + 零密度 + 素数误差

## 5. 对我们的意义

### 5.1 解释数值发现
- **Σcos(γ log p) ~ c_p·K** = Lemma 1 主项（素数幂共振——−T·Λ(p)/(2π·√p)——实数）
- **Σsin(γ log p) = O(1)** = 虚部（主项是实的——虚部来自误差项——需要振荡控制）

### 5.2 无条件框架（FSZ——现成工具）
```
Σ_k sin(γ_k log p) = Im Σ_{γ≤T} p^{iγ}
≈ Im[p^{−1/2}·Σ p^ρ]（Lemma 1——主项实——虚部 0）
+ O(T·log²p/log T)（(3.8)——零密度——无条件）
```

### 5.3 差距定位
- **无条件界**：O(T·log²p/log T)（FSZ）
- **数值**：O(1)（到 2M）
- **差距 = 相位均匀性 = RH**——但 FSZ 框架把差距**显式化**了（主项 + 零密度 + 素数误差——每一步都明确）

## 6. 下一步（候选）

1. **用 FSZ 框架重写 Σsin(γ_k log p) 的估计**——把我们的 Guinand 发现与 FSZ 公式统一
2. **检查 FSZ 的 Conjecture 3**（Σx^{iγ} = o(T)——他们证明 RH + 对关联 ⟹ 它）——我们的数值 O(1) 比 o(T) 强得多——**但证明了什么？**
3. **Fujii 的 D = O(loglog T/log T)**——discrepancy 上界——与我们的 O(1) 数值对比——差距量化
4. **Murahara 方法**（计数函数渐近——广义）——可能给我们"相位均匀性"的新工具

## 7. 文件

- 文献笔记（本文件）
- 后续：FSZ 公式的应用脚本
