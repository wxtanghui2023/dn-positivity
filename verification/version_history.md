# Version History（v2.14）

## 版本演化（2026-08-30 单日完成投稿工程）

| 版本 | 内容 | 关键事件 |
|------|------|----------|
| v2.4 | 文献接口 | Reference Map——Weil 1952/Barner 1981/Schwartz-Hörmander |
| v2.5 | 参考文献表 + Final Audit A-D | 冻结引用层级——Audit 四轮（A 外部/B 引理/C 符号/D 措辞） |
| v2.6 | 压力测试 | Attack 1-4——**发现 Δ_H 全区域正性表述过强（γ=0 反例）** |
| v2.6.1 | Lemma C 正性范围修正 | 全域 → 零点谱限定（|γ| ≥ γ₁）——三处同步 |
| v2.6.2 | Final Attack Surface Scan | Attack 1-8 全过 |
| v2.7 | 最终一致性审计 | 第一轮主恒等式链——第二轮 Lemma A3/C1——**发现 Δ_H ~ |δ| 线性（非 δ²）** |
| v2.8 | LaTeX 正式稿 | 四页初稿——编译成功 |
| v2.8.1 | 模拟审稿（保守） | Major Revision——Major 1-6（Q'_RH 定义/W 空间/c̃_H 正性/A3 提升/H_0 构造） |
| v2.8.2 | 修正 | Major 1-6 全部解决——零频消去闭式 |
| v2.8.3 | 真实性压力测试 | Round A-F——7 项过——**C1 零频修正（配对仅乘积 L¹）** |
| v2.8.4 | 黄色项补强 | 逐点正性——c̃_H ~ 1/(2γ²) 渐近——**inf > 0 不需要** |
| v2.8.5 | Final Audit v2 | 6 项全绿——正性链重新闭合——等号刚性完整 |
| v2.9 | 投稿级 LaTeX | 6 节 + 3 附录 + Limitations——Check 1-3 |
| v2.10 | Blind Referee Test | 7/8 绿——**Referee 6 引用边界 🟡（Barner 精确假设）** |
| v2.10.1 | Barner 核对 | **重要发现：H_0 ∉ L¹——"H_0 ∈ W 经典"过度声称** |
| v2.10.2 | Proposition B 修正 | Distributional Weil compatibility——配对 ⟨S,H_0⟩ = ⟨log\|ξ\|,H_0''⟩ |
| v2.11 | 怀疑型审稿 | Attack 1-5 全过——单一 H_0 谱刚性（非 Weil 重写） |
| v2.12 | 最终投稿版 | Title 谨慎版——Referee Response Appendix（C1-C5）——关键词扫描 |
| v2.12.1 | Pre-submission Integrity Check | **发现 Section 4 编辑回滚（PDF 含旧过度声称）——已修复**——最终扫描全 0 |
| v2.13 | Submission Package | manuscript/cover_letter/README/bibliography/referee_response |
| v2.13.1 | Final Package Integrity Check | A-F 六项全过——从零编译一致 |
| **v2.13.2** | **Submission Candidate Freeze** | **No mathematical modification after freeze——Only formatting/metadata/journal-specific** |

## 已抓住的版本漂移/表述过强（历史风险清单）

1. δ²w_H 回流 → 已抓（Audit 1——改为 ΣΔ_H）
2. H_0 ∈ W 过度声称 → 已抓（v2.10.1——改为分布配对）
3. global positivity → 已抓（v2.6.1——改为零点谱限定）
4. inf c_H → 已抓（v2.8.4——改为逐点正性）
5. PDF/TeX 不一致 → 已抓（v2.12.1——编辑回滚）
6. δ²c_H（二阶表述）→ 已抓（v2.7——改为 |δ|c̃_H）

## 状态声明（严格表述）

> The manuscript presents a criterion equivalent to the Riemann
> Hypothesis under the stated distributional framework and verified
> identities.
>
> **不是**：The Riemann Hypothesis has been proved.
