已查地图：命中（`C3-endpoint-filter-and-modular-reduction`／`C3-TR-fixed-by-angle-cancellation`）⟹ 引用，不开新案
D0: 本档对象 = **（乙）判定：`\langle T_L,T_R\rangle` 非平凡**（由 **dart 计数 vs 塌缩界** 得出）＋ 状态更新
D1: 0 （[REVIEW] 轮次：手工代数，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **非平凡性：`T_L,T_R,T_LT_R\neq1`**

## §1 逻辑缺口（照录）

```
$$T_L^2=1,\ T_R^3=1\ \Longrightarrow\ \langle T_L,T_R\rangle\ \text{是 } C_2*C_3\cong\mathrm{PSL}(2,\mathbb Z)\ \text{的商}$$ ✓
【但】**不能**推出商非平凡、也**不能**推出 `T_L` 确为二阶、`T_R` 确为三阶**（极端情形 `T_L=T_R=1` 同样满足两式，群平凡）✓✓
```

## §2 阶数本身排除不了（照录您的推导）

```
若 `T_L=b^2a^{-1}=1` ⟹ `a=b^2`；代入 `(ab)^2=1` 得 `(b^2\cdot b)^2=b^6=1` ⟹ **不矛盾**（`b^2` 可有阶 `3`）✓
若 `T_R=b^2c^{-1}=1` ⟹ `c=b^2`；`c^3=1,b^6=1` **允许**该识别 ⟹ **不能仅凭阶数排除** ✓✓
⟹ **必须用 `(3,6)`／`(6,3)` 三角群的真实结构** ✓
```

## §3 ⭐⭐ 判定：用 **dart 计数 vs 塌缩界**

```
**【标准事实（档级）】** 正则地图 `\{3,6\}_{(s,0)}` 的**旋转群在 darts 上\textbf{sharply transitive}** ⟹ `|\mathrm{Rot}|=#darts=2\cdot E=6s^2` ✓
　`\{3,6\}_{(2,0)}`：`V=s^2,E=3s^2,F=2s^2`（`s=2`：`V=4,E=12,F=8`；Euler `4-12+8=0` ✓）⟹ `#darts=2E=24` ⟹ $$\boxed{|\langle a,b\rangle|=24}$$ ✓✓
　`\{6,3\}_{(3,0)}`（`\{3,6\}_{(3,0)}` 的对偶）：`V=2s^2,E=3s^2,F=s^2`（`s=3`：`V=18,E=27,F=9`；Euler `18-27+9=0` ✓）⟹ `#darts=2E=54` ⟹ $$\boxed{|\langle b,c\rangle|=54}$$ ✓✓
**【判 `T_L`】** 若 `T_L=1` 则 `a=b^2` ⟹ `\langle a,b\rangle=\langle b\rangle\cong` 商 of `C_6` ⟹ `|\cdot|\mid 6`；但实测 `24` ⟹ $$24\nmid 6\ \text{矛盾}\ \Longrightarrow\ \boxed{T_L\neq1}$$ ✓✓
**【判 `T_R`】** 若 `T_R=1` 则 `c=b^2` ⟹ `|\cdot|\mid6` vs `54` ⟹ 矛盾 ⟹ $$\boxed{T_R\neq1}$$ ✓✓
**【判 `T_LT_R`（最强）】** $$T_LT_R=1\ \Longrightarrow\ T_L=T_R^{-1}=T_R^2\ \Longrightarrow\ T_R^4=T_L^2=1;\ \text{又}\ T_R^3=1\ \Longrightarrow\ T_R^{\gcd(4,3)}=T_R=1\ \text{矛盾}$$ ⟹ $$\boxed{T_LT_R\neq1}$$ ✓✓✓
**⟹ 结论**：$$\boxed{\langle T_L,T_R\rangle\ \text{非平凡，是}\ \mathrm{PSL}(2,\mathbb Z)\ \text{的真商}}$$ ✓✓✓
```

## §4 须核（标准事实的等级）

```
**(i)** dart-sharp-transitivity of regular maps 的旋转群 —— **标准（档级）** ✓
**(ii)** parabolic `\Gamma_{012}`／`\Gamma_{123}` 的旋转子群 ≅ 对应 toroid 的旋转群 —— **由 universal polytope 定义给出**（`\{3,6\}_{(2,0)}`／`\{6,3\}_{(3,0)}` 即 facet／vertex-figure）✓
**(iii)** 若 `\{3,6\}_{(2,0)}` 或 `\{6,3\}_{(3,0)}` 在文献中另有**参数等价**（如 `\{6,3\}_{(b,0)}\cong\{6,3\}_{2b}`）⟹ **`54` 的取值须复核** ✓⚠️
```

## §5 状态更新

```
$$\begin{array}{c|c}
T_L=b^2a^{-1}\ \text{（已逐字印证）}&\checkmark\\
T_R=b^2c^{-1}\ \text{（角度判据）}&\checkmark\\
T_L^2=1,\ T_R^3=1&\checkmark\\
T_LT_R=ac^{-1}&\checkmark\\
\langle T_L,T_R\rangle\ \text{是 } C_2*C_3\ \text{的商}&\checkmark\\
\textbf{非平凡性}&\textbf{RESOLVED：}T_L,T_R,T_LT_R\ \text{皆}\neq1\\
\text{⑤ 短字追踪}&\text{可进入（曾暂缓）}\\
\mathrm{GAP}\ \text{／Todd–Coxeter}&\textbf{LOCKED}\\
\text{intersection-defect 证书}&\textbf{尚无}\\
\end{array}$$ ✓
【下一步】 依您的纪律进入 **⑤**：`T_LT_R`、`(T_LT_R)^2`、`(T_LT_R)^3`、`(T_LT_R)^6`、`T_LT_RT_L`、`T_RT_LT_R^2` 逐个追端点消除；**不跑 GAP／不做 Todd–Coxeter／不做 word enumeration** ✓
【⛔ 边界】 本档**未得 intersection-defect 证书**；§3 判定基于 **dart 计数**（可手核）＋两项标准事实（§4）；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 dart             命中文件数=1    :: ./C3-nontriviality-resolved-by-dart-counting.md 
技术词 sharply transitive 命中文件数=1    :: ./C3-nontriviality-resolved-by-dart-counting.md 
```
