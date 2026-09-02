# ARCHIVE：P49-G2.7.4 Prolate-Weil Bridge——三层数值封档

> 2026-09-02 17:25 · CCM (arXiv:2511.22755) 审计终结 · 桥三层否证 · 结构性结论

## 结论（一句）
**CCM 的 prolate ground state 不是 QW_λ 算术 ground state 的正确渐近解释——"k_λ ≈ ξ̂_λ"在数值上无任何层面的支持（在我们的实现与测试协议下）。**

## 三层否证证据链（全部 λ=3，N 扫描）
### 层 1：向量域（II-A.2b——V 基 ground 重叠）
- O(λ,N) = |⟨k_λ/‖k_λ‖, ξ_{λ,N}⟩|²：N=4: 0.977(λ=3)/0.921(λ=4)/0.544(λ=6)——N=8: 0.727/0.537/0.395
- **O 随 N 降 + 随 λ 降**——O_low 同步降（V 内方向分离）——97.7% 是 N=4 有限尺度现象
- ⟹ ground-vector bridge 不成立（FAIL candidate）

### 层 2：变换域 Rouché（II-B'.2a——ξ̂ vs c·k̂_λ 圆盘边界）
- η = sup_{∂D_r}|ξ̂−c·k̂_λ|/|c·k̂_λ|：N=6,8: η<1（0.177/0.186——Rouché 局部 PASS——第一零点计数转移）
- **N=10,12: η 崩（0.967/0.713——free——fixed 爆炸 14.4/10.4）**
- ⟹ Rouché 计数一致是有限截断现象——ξ̂ 不是 k̂_λ 的渐近稳定扰动

### 层 3a：低能压缩（C2——κ_K = sup‖T_z P_⊥‖/sup|T_z ξ₀|）
- **κ_K > 1 所有 N（2.2-9.3）——transform 不压缩近核自由度——反而放大**
- ⟹ "spectral near-degeneracy ⟹̸ observable near-degeneracy"机制未出现

### 层 3b：canonical direction（C-variant——f_z = P_r v(z) 归一——防作弊协议）
- **O_k(z) = |⟨f_z, k̂_λ⟩|² ~ 1e-4 到 1.5e-2（几乎正交）——f_z 不追踪 k̂_λ**
- ⟹ T(E_low) 中不存在天然的 k_λ 对应方向

## 数值审计教训（本线）
1. **dt=0.002 大矩阵构建产生伪影**（ground 假不稳定——重叠 1e-9）——**同协议重验（dt=0.005 vs 0.01）ground 完全稳定（1.000）**——伪影 REVOKED
2. **ground 稳定但 η 崩是真实函数层不匹配**（非 ground 噪声）
3. **近零簇（ε ~1e-12）真实存在——但 ground 方向由 MA/MP 精确结构锁定**——"简并"≠"ground 不唯一"
4. **simple-even 的 gap 双精度不可判定**（OPEN）——但特征向量数值良定义

## P49-G2.7.4 最终状态
| 组件 | 状态 |
|---|---|
| k_λ → Ξ（Lemma 7.3） | PASS（定理——带内） |
| D_{λ,N} self-adjoint | PASS_conditional（simple-even） |
| Z(ξ̂) ⊂ ℝ | PASS_conditional |
| Stage 1: det_reg → −iλ^{−iz}ξ̂_λ (N→∞) | 论文断言（未核验证明） |
| ξ̂_λ ↔ k_λ（missing step 2） | **FAIL candidate（三层否证）** |
| simple-even | OPEN（数值 gap 不可判定） |
| RH | OPEN（经 CCM 路线无进展） |

## 限定（不扩大）
- 不证明统一算术 rigidity 框架不存在——不证明 QW 无用
- 只否证：**CCM 的 k_λ ≈ ξ̂_λ 具体桥**（vector/transform/canonical 三层）
- CCM 其他路线（det_reg 直接谱分析——不经 prolate 桥）未排除

## 关键文件
- docs/p49-g274iia2b-scan.md（向量域）
- docs/p49-g274iib2a-rouche.md + iib2a-ext-collapse.md（Rouché）
- docs/p49-g274c1-ground-instability.md + c1-correction.md（数值审计）
- docs/p49-g274c2-compression.md + c2cv-cvariant-close.md（压缩 + canonical）
- 本文档（封档）
