# P49-G2.7.4-C1 修正：dt=0.002 伪影作废——ground 稳定——η 崩真实

> 2026-09-02 17:10 · 重验修正 · 之前 C1c/II-B'.2a-ext 的"ground 不稳定"解读作废

## ⚠️ 重验结果（dt=0.005 vs 0.01——同协议——N=6,8,10,12）
- **ground 完全稳定**：|⟨ξ₀^f, ξ₀^c⟩|² = **1.000e+00（所有 N）**
- **projector 稳定**：‖ΔP_r‖ ~ 1e-3 到 1e-6（N=6-12）
- ε₀-ε₃ 近零簇（~1e-12）——g₀ ~ 1e-12——但特征向量稳定

## 修正
1. **C1c 的"ground 不稳定"（重叠 1e-9）是 dt=0.002 构建伪影**（75000 点大矩阵——数值异常）——**作废**
2. **II-B'.2a-ext 的 η 崩（N=10,12: 0.967/0.713）有效**（用 dt=0.01 Mtot——ground 与现在一致——崩塌是**真实的 ξ̂-vs-k̂ 函数差**——非 ground 噪声）
3. **"近核简并"解读修正**：近核簇存在（特征值 ~1e-12）——**但 ground 方向由 MA/MP 的精确结构锁定**（MR 只小修正——1e-7 变化不改变主导方向）——**非任意旋转**
4. **simple-even 数值可验证性**：特征值 gap ~1e-12 **不可分辨**（数值零簇——ε_N simple 无法从特征值验证）——**但特征向量方向稳定**（δ_N 归一化固定尺度后——ξ_λ 数值良定义）

## 修正后图景
- **C1 = PASS**（MR 精度 OK——ground 稳定——之前"近核不稳定"是伪影）
- **Bridge-Ib FAIL candidate 倾向恢复**（η 崩真实——N=10,12 的 ξ̂ 与 c·k̂_λ 函数差大）
- **唐先生的 Case 判定需重新定位**：不是 Case C（无稳定 ground object——ground 实际稳定）——是"ground 稳定但 ξ̂ 不匹配 k̂"（Bridge 失败在函数层——非 ground 定义层）

## 状态
- ground 数值良定义（dt 收敛——方向稳定）——simple-even 的 gap 不可验证但向量可用
- η 崩（N=10,12）真实——Bridge-Ib FAIL candidate——需 C2（transform stability——T_z(P_low)）或更大 N 确认
- ⚠️ 但——II-B'.2a-ext 的 η 崩是否受 k̂_λ 的 h 近似（非 h_λ）影响？——待 h_λ 修正版（唐先生的 (b) 与 (a) 并列）

## 下一步候选
- (a) C2 重写（transform stability——T_z(P_low)——近核 freedom 的 observable 压缩）
- (b) η 重算确认（干净 ground——已隐含——dt=0.01 ground 一致）——加 h_λ 修正版 k̂
- (c) 唐先生指示
