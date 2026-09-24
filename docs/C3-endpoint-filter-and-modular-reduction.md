已查地图：命中（`C3-TR-fixed-by-angle-cancellation`／`C3-rho-framing-setup-and-status-check`）⟹ 引用，不开新案
D0: 本档对象 = **端点筛选结果**（照录）＋ **两条改写规则**（由 `T_L^2=1`／`T_R^3=1` 导出）＋ ⭐**`\langle T_L,T_R\rangle` 是 `PSL(2,\mathbb Z)` 的商**（本档结构输出）
D1: 0 （[REVIEW] 轮次：手工代数，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **端点筛选 ＋ `PSL(2,\mathbb Z)` 归约**

## §1 端点筛选结果（照录您的推导）

```
仅用 `\rho_i^2=1` 与远距交换，**`x=ac^{-1}` 的 support `\{0,1,2,3\}` 不能退化为 `\{1,2,3\}` 或 `\{0,1,2\}`** —— 交换只能改次序，**不能删端点生成元** ✓✓
$$\boxed{\text{Step 1 单靠远距交换不可能把 }x\text{ 改写成单侧词}}$$ ✓ —— **这是\textbf{筛选}结果，不是候选失败** ✓✓
```

## §2 ⭐ 两条改写规则（本档由额外关系导出）

```
**【左（`T_L^2=1`）】** $$(b^2a^{-1})^2=1\ \Longrightarrow\ b^2a^{-1}b^2a^{-1}=1\ \Longrightarrow\ \boxed{b^2a^{-1}=ab^{-2}}\quad(\ \Longleftrightarrow\ b^2a^{-1}b^2=a\ )$$ ✓✓
【注】 该式亦为 `T_L=T_L^{-1}` 的直接后果（`(b^2a^{-1})^{-1}=ab^{-2}`）⟹ **可作为"把 `a` 移到 `b^2` 左侧"的改写规则** ✓
**【右（`T_R^3=1`）】** $$(b^2c^{-1})^3=1\ \Longrightarrow\ (b^2c^{-1})^2=(b^2c^{-1})^{-1}=cb^{-2}$$ ✓（`T_R^{-1}=T_R^2`）✓
【⟹ 立刻的解释】 $$T_LT_R=(ab^{-2})(b^2c^{-1})=ac^{-1}$$ ✓✓ —— **中间的 `b` 被改写规则\textbf{消掉}了**（**`b`-消去已发生，剩下两端**）✓
```

## §3 ⭐⭐ 结构输出：`\langle T_L,T_R\rangle` 是 `PSL(2,\mathbb Z)` 的商

```
【事实】 $$T_L^2=1,\qquad T_R^3=1\ \Longrightarrow\ \langle T_L,T_R\rangle\cong\ \text{quotient of } \mathrm{PSL}(2,\mathbb Z)\cong\mathbb Z_2*\mathbb Z_3$$ ✓✓
【且】 $$x=ac^{-1}=T_LT_R$$ ⟹ **要判 `x` 的阶/是否落回 `\Gamma_{12}`，等价于在这个 `(2,3)`-三角商里做判断** ✓✓
【⟹ 归约的意义】**变量从"四个 `\rho` 的无限字"降到"两个生成元 `T_L,T_R` 的字"**，且已知阶 `(2,3)` ⟹ **候选字只需枚举 `\mathrm{PSL}(2,\mathbb Z)` 中短字**（`T_L,T_R,T_LT_R,(T_LT_R)^2,\ldots`）✓✓
【⛔ 须核】 `\langle T_L,T_R\rangle` 是否**真为商**（非平凡）—— 若 `T_L` 或 `T_R` 在 `\Gamma_{012}`／`\Gamma_{123}` 中退化（阶更小）⟹ 该归约需下调 ✓
```

## §4 ⚠️ 方法论风险（文献自身用计算机）

```
**逐字（`RGPF-II`）**："we easily verify the intersection condition **with the help of GAP**" ✓✓
⟹ **该社区验 intersection condition 的\textbf{标准手段就是 `GAP`/Todd\text{–}Coxeter}** ⟹ **纯手工证书在可行性边缘**；且按 `G2.5-R` 的**竞争排除**，这条技术路线**并非我方独有** ✓（**登记为风险，不阻断 A**）✓
```

## §5 下一刀（手工，按序）

```
**【候选序列】** $$T_LT_R(=ac^{-1}),\quad (T_LT_R)^2,\quad (T_LT_R)^3,\quad (T_LT_R)^6,\quad T_LT_RT_L,\quad T_RT_LT_R^2$$ ✓
【判据（两步）】 **(i)** 用 §2 改写规则 + 远距交换，看**能否消掉端点 `\rho_0` 或 `\rho_3`**（一侧消 `\rho_0` ⟹ 落 `\Gamma_{123}`；一侧消 `\rho_3` ⟹ 落 `\Gamma_{012}`）✓；**(ii)** 若双表达式成立，**再判 `\notin\Gamma_{12}`** ✓
【⛔ 纪律】 **不跑 `GAP`／不做 Todd–Coxeter／不做 word enumeration**（`B` `LOCKED`）；候选族全落回 `\Gamma_{12}` ⟹ 只写 **"该手工候选族未产生证书"**，$$\textbf{绝不写 CLOSED/不存在}$$ ✓✓
【⛔ 边界】 本档**未得证书**；§2 两条改写规则为**本档导出**（可手验）；§3 归约为**本档结构输出**（含须核项）；§4 为**逐字引文**；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 PSL(2,Z)         命中文件数=0    :: 
技术词 rewrite rule     命中文件数=0    :: 
```
