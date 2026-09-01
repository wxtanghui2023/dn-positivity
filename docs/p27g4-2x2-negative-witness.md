# P27-G4：2×2 Negative-Witness Lemma——正测度正半定（分叉结果）

> 2026-09-01 · 唐先生 G4 指令 · 固定离轴零点——2×2 Gram——det G<0？∃θ：Q(fθ)<0？

## P27-G4 结果

### 设定
- G_ρ = [[A,B],[B̄,C]]——A=D(f1,f̄1)——B=D(f1,f̄2)——C=D(f2,f̄2)
- f_θ = f1+e^{iθ}f2——Q(fθ) = A+2Re(e^{iθ}B)+C——Q_min = A+C−2|B|（Q<0 ⟺ |B|>(A+C)/2）
- det G = AC−|B|²（det<0 ⟺ |B|>√(AC)——比 Q<0 更强）

### 数值验证（δ=0.5——γ=5.0——大 β 信号——相位可控）
| (u1,σ1) | (u2,σ2) | A | B | C | Q_min |
|---|---|---|---|---|---|
| (1.0,0.4) | (1.5,0.4) | 0.147 | **−0.236** | 0.558 | 0.234 |
| (1.0,0.4) | (0.5,0.4) | 0.147 | −0.054 | 0.028 | 0.066 |
| (1.0,0.4) | (2.0,0.4) | 0.147 | 0.158 | 1.820 | 1.650 |
| (0.5,0.4) | (1.5,0.4) | 0.028 | 0.042 | 0.558 | 0.503 |

**全部 Q_min ≥ 0——det G ≥ 0——2×2 self-form 正半定（正测度）**

### ⭐ 关键发现
1. **B 可以变号**（(1.0,0.4)/(1.5,0.4)：B = −0.236——相对相位——cos 振荡）——但 **|B| ≤ √(AC)**（0.236 < √(0.147·0.558) = 0.286）——det G ≥ 0
2. **"负 witness 不存在"（2×2——正测度）**——即使 B 负——|B| 被 √(AC) 限制——Q_min ≥ 0
3. **"不定核可以有正半定的 Gram"**（W 的核 cos(γ(u−v)) 变号——不定——但测试族 {f1,f2} 上的 Gram 正半定）

### ⭐ 分叉结论——Detectability ⇏ Indefiniteness（2×2 正测度）
- **G4-A（2×2 Negative-Witness——正测度）——失败**：
  - 单 orbit 可检测（G3——Level G1——D(f,f) > 0）✓
  - 但 quadratic self-form（2×2）正半定——无负方向 ✗
- **"这正是唐先生 15 的分叉"**（G4-A 失败也是好结果——Detectability ⇏ Indefiniteness）

### 下一步分叉
- (a) **复测度 2×2**（dμ 复——f 复——B 的相位自由——负 witness 可能）
- (b) **B 的严格上界证明**（|B| ≤ √(AC)——正测度——Detectability ⇏ Indefiniteness——严格定理）
- (c) 更高维（3×3——）
- (d) bilinear/non-Hermitian structure（唐先生 15）

## ⭐ 核心价值
- 2×2（正测度）的严格分叉：**单 orbit 可检测但 quadratic self-form 正半定**——负方向需要复测度/更高维/非厄米结构
- 这是 P27 链条（kernel structure → local detectability → isolation → global positivity）中 isolation 前的关键分叉点
