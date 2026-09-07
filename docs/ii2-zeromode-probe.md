# II-2 zero-mode forcing 探索——dilation 自伴化不产生 zero mode

> 2026-09-07 15:05 · II-2 概念探索

## 唐先生 II-2 定义
找 zero-blind A₀ + 算术对偶 J（JA₀J = A₀*——）使缺陷空间配对——**zero mode 被对偶结构强迫**（F(s)=0——非手动 ker——）

## 探索结果（dilation 族——）
| 组合 | 结果 |
|---|---|
| B_f + B_f*（对称——） | level set Re F(s) = 0（非零点——） |
| i(B_f − B_f*)（反自伴——） | level set Im F(s) = 0（非零点——） |
| B_f*B_f（平方——） | h_s 非特征函数（谱结构破坏——） |
| ker B_f | 手动编码零点（死——） |

## 核心观察
**zero mode（F(s)=0）需要"对偶结构强迫"——非简单自伴组合**：
- "0 是 FE 不变值（±i 不是——）"——需要把 FE 编进算子对偶
- **但 FE 是 Archimedean（Gamma——）结构——纯 dilation（整除——）无 FE**
- → 回到"算术-解析断裂"（反射需 Archimedean——ARP-2 同因——）

## 结构性认识（II 系列的深层——）
- II-1：dilation → Mellin 角色 → Hilbert 边界 Re s = ½（真结构——但 level set 缺陷——）
- II-2：zero-mode 需要 FE 对偶——FE 是 Archimedean——纯算术 dilation 给不了
- **dilation 算子族的天花板**：Hilbert 边界 ½ ✓——但 level set → zero 的跃迁需要 FE（跨断裂——）

## 文件
- scripts/ii2_zeromode_probe.py
