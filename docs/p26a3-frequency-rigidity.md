# P26-A3：Continuation → Bohr-frequency rigidity——快速衰减类干净证明

> 2026-09-01 · 唐先生 P26-A3 指令 · 攻击"全球解析延拓是否保持/决定 Euler-Bohr 频谱"

## 唐先生 P26-A3 框架（采纳）
- **核心命题**：analytic continuation + almost-periodicity + Euler-prime support ⟹ frequency rigidity
- 右半平面 Bohr spectrum 已知 ⇏ 左半平面 Bohr spectrum 已知——"延拓自然性"是核心
- 不要直接上 Phragmén-Lindelöf（growth rigidity ≠ frequency rigidity）
- 不能把"ζ'/ζ 特殊方向"升级成唯一性（需要单独分类定理）
- 即使 A3 成功——T_ζA={0} 不 ⟹ RH——最后一步 rigidity ⟹ critical-line geometry 仍是 Gate F

## P26-A3 本轮进展——快速衰减类的干净证明

### ⭐ 定理（快速衰减类）
**若 Σ_p |b_p| p^{−1/2} < ∞（快速衰减——含有限支撑）且 M_b 满足反射（临界线 M_b(½+it) = M_b(½−it)）——则 b_p = 0（全 p）**

**证明**：
1. 临界线级数收敛（快速衰减）——1/(p^{½+it}−1) = Σ_{k≥1} p^{−k(½+it)} = Σ_k p^{−k/2} e^{−ikt log p}（|p^{½+it}|=√p>1）
2. M_b(½+it) = Σ b_p p^{−k/2} e^{−ikt log p}——**只含负频率 {−k log p}**
3. M_b(½−it) = Σ b_p p^{−k/2} e^{+ikt log p}——**只含正频率 {+k log p}**
4. 反射 ⟹ 两者相等（全 t）——负频率函数 = 正频率函数
5. **Bohr 唯一性**（频率全不同——log p Q-线性无关——p^k = q^ℓ ⟹ p=q, k=ℓ）——系数 b_p p^{−k/2} = 0——**b_p = 0 ∎**

**关键性质**：不需要延拓——不需要自然边界——不需要 ζ 零点——**RH-independent**——有限支撑是特例（快速衰减）——统一了之前的证明

### 数值验证
- 反射失败（Im ≠ 0——t=0.5: Im=0.488——b≠0 不可能反射）✓
- 频率系数匹配（p=2: 0.1768 vs 理论 b_p p^{−1/2} = 0.1768 ✓）

### 一般类（有界 b_p——σ_c = 1）——开放
- 临界线级数不收敛（Σ|b_p|p^{−1/2} 发散）——论证不适用
- 核心仍是"延拓值（Re<0）的频率系数"（P26-A3 完整命题——未证）
- "ζ'/ζ（log p）不反射"（差 5.98）——独立验证——与定理一致

## ⭐ P26-A3 判定（本轮）
- **快速衰减类（Σ|b_p|p^{−1/2}<∞——含有限支撑）：反射 ⟹ b=0——干净证明（RH-independent）**
- **一般类（有界 b_p）：未决**——核心是延拓值的频率系数
- **"Continuation → Bohr-frequency rigidity"在快速衰减类成立**——实质进展

## 下一步
- (a) 扩展快速衰减类（衰减条件放宽——σ_c < 1/2 的类——级数在临界线收敛的充分条件）
- (b) 攻一般类（延拓值的频率系数——几乎周期延拓假设——P26-A3 完整命题）
- (c) 接受本轮（快速衰减类干净证明——一般类未决）
- (d) 唐先生指示
