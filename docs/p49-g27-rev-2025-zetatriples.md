# P49-G2.7 修订：2025 Zeta Spectral Triples 补审——R1/R2 重新审计

> 2026-09-02 13:42 · 唐先生修订指示 · arXiv 2511.22755 时效性校正

## P49-G2.7 框架判定（唐先生——修订）
- **G2.7.1 R1/R2 Framework：PASS/CLOSED**（R1 = independent realization——R2 = independent rigidity/coercivity——R1∧¬R2 ≠ third mechanism）
- **G2.7.PC Function-field Positive Control：PASS/CLOSED**（I∧A∧B_constr∧O 真实存在——最强正控制）
- **G2.7.2 Char-0 Candidate Audit：OPEN/first round substantially complete**（因 2025 必须纳入——不能写"候选已审完"）
- **G2.7.3 R2：OPEN/NOT FOUND**（independent rigidity → O3 off-line obstruction 仍未找到）
- **P49 = realization wall 已定位；rigidity wall 未突破**
- 措辞修正：Langlands R1 ✗（当前无 zero-as-spectrum realization——非"零点与 automorphic 无关"）——动机 R1 = not established（非 impossible——不能对所有 motive-theoretic realization 做不可能性证明）

## ① 2025 Zeta Spectral Triples（arXiv 2511.22755——Connes-Consani-Moscovici 2025-11）实际内容确认
- **构造**：自伴算子 = 区间 [λ⁻¹, λ] 上 scaling operator 的 spectral triple 的 rank-one perturbations
- **只用素数 p ≤ x = λ² 的 Euler products**——产生自伴算子——**谱数值（惊人精度）与 ζ(½+is) 最低非平凡零点一致（即使小 x）**
- 理论基础：Spectral triples and zeta-cycles (2023) + Quadratic Forms/Real Zeros (2025)——Carathéodory-Fejér 定理（Toeplitz）扩展——保证 self-adjointness
- **数值：谱随 N, λ → ∞ 收敛到 ζ(½+is) 零点——严格证明此收敛 = RH（论文明确——未完成）**
- regularized determinants 计算——规范后收敛到 Riemann Ξ 函数

## ② R1/R2 重新审计
- **R1（independent realization）**：**更强候选 ✓**——只用 Euler products 构造（独立于零点）——自伴算子——谱数值 = 零点——**Euler completion 的 spectral triple 实现（P49-G2 目标的潜在形态！）**
- **R2（independent rigidity/O3）**：**未完成 ✗**——"严格证明收敛 = RH"——收敛是"要证的"——numerical spectral agreement ≠ independent purity ⟹ off-line exclusion——regularized determinants → Ξ 是分析角色——未完成严格证明
- **判定：Connes 2025 = R1 更强 candidate——R2/O3 尚未提供（唐先生判断确认）——不能写"Connes 候选已审完"——P49-R1 candidate space 仍在发展**

## ③ ⚠️ 深层 P49 观察（2025 未击穿墙——但精确化了 R2 缺口）
- 2025 结构：Euler products → T_N（自伴）→ Spec(T_N) 数值 = 零点 → det(T_N) → Ξ——**核心未证条件：convergence（谱极限 = 零点）**
- **从 P49 视角**：如果收敛证明完成——"谱 = ζ(½+is) 零点（s 实——自伴谱实）"⟹ ρ = ½+is 在临界线——**RH——即——2025 如果完整 = 潜在 escape hatch（R1+R2 全过）**
- **但**——"det(T_N) → Ξ"（函数收敛）≠ "谱零点 → Ξ 零点"（需要 Hurwitz 类条件——且——"Ξ 零点在实轴"= RH 是要证的——不是 det 收敛自动给）——**R2/O3 缺口精确化：需要"独立 rigidity 证明极限谱被强制 = 零点"（不是数值吻合——不是 det 收敛——是谱的刚性收敛）——这正是 P49 的 R2（non-adaptive coercivity——为什么谱极限恰好 = ζ 零点而非别的配置）**
- **2025 是对 P49 框架的漂亮外部压力测试**：R1 强化——R2/O3 仍未显然完成（唐先生判断确认）

## ④ 机制表升级
| 机制 | R1 realization | R2 independent rigidity | P49 状态 |
|---|---|---|---|
| Explicit formula | ✗ | ✗ | bridge/coupling |
| Euler product | ✗ | ✗ | arithmetic representation |
| P48 defect | ✗ | ✗ | separation/information |
| Hilbert-Pólya | partial | ✗ | desired spectral mechanism |
| Connes NCG（经典） | partial | ✗ | realization candidate |
| **CCM 2025 Zeta Spectral Triples** | **stronger candidate** | **尚未完成** | **必须继续审计** |
| Motive/cohomology | not established | ✗ | char-0 realization candidate |
| Langlands | ✗（P49-R1 定义） | ✗ | automorphic ≠ zero spectrum |
| Function-field Weil | ✓ | ✓ | **Positive Control** |

## ⭐ P49-G2.7 修订判定
- **2025 补审完成**（实际内容确认——唐先生描述准确——R1 更强候选——R2 未完成——收敛证明 = RH——未证）
- **P49 框架经受最新候选反例压力**（不是文献共识式总结——是可审计框架）
- **P49 = realization wall 已定位——rigidity wall 未突破——2025 = R1 必须补审的新候选——尚未提供 R2/O3**
- ⚠️ 诚实：2025 的收敛证明（若完成）= 潜在 escape hatch（Euler completion spectral 实现）——但——未完成——且——从 P49 视角——收敛证明本身需要"独立 rigidity"（为什么极限谱被强制 = 零点）——即 R2 问题（未解决）——**2025 强化 R1——不显然完成 R2**

## 下一步候选（唐先生倾向 (a)）
- (a) **G2.6.2 局部 No-Go**：C₀ = {prime/local data → 固定线性/乘法变换 E → Mellin/Fourier A}——证明 E ∈ C₀ ⟹ {zero-dependent ∨ quotient-generated ∨ coupling identity ∨ non-coercive}——**C₀ 中不存在 P49-O3 型 coercive bridge——可发表形式的结构性 No-Go**（⚠️ 2025 的 spectral-triple 构造在 C₀ 外（非固定线性/乘法+Mellin/Fourier——是 spectral triple/Toeplitz）——归 C_unknown——需在文档中明确）
- (b) R2 深化（char 0 独立 rigidity 来源——含 2025 收敛证明的审计——为什么数值吻合——是否可能严格化）
- (c) 唐先生指示
