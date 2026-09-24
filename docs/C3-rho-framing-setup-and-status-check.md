已查地图：命中（`C3-pivot-to-offdiagonal-amalgamation`／`C3-self-correction-s4-is-indefinite-not-degenerate`）⟹ 引用，不开新案
D0: 本档对象 = **`\rho` 记号下的精确设定**（`T_L`／`T_R` 显式词 ＋ 目标 ＋ 窄边界）＋ `U_{2,3}` 状态核验（第二轮）
D1: 0 （[REVIEW] 轮次：设定与核验，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`\rho` 记号设定 ＋ `U_{2,3}` 核验**

## §1 ⭐ 显式设定（本档推导）

```
$$\Gamma=[3,6,3]=\langle\rho_0,\rho_1,\rho_2,\rho_3\rangle:\quad \rho_i^2=1,\quad(\rho_0\rho_1)^3=(\rho_1\rho_2)^6=(\rho_2\rho_3)^3=1,\quad(\rho_0\rho_2)^2=(\rho_0\rho_3)^2=(\rho_1\rho_3)^2=1$$ ✓
【两条平移词（本档由层结构推出，与文献逐字关系一致）】 对 `\{3,6\}` 型层：`[3,6]^+=\langle\sigma_1,\sigma_2\rangle`，`\sigma_1=\rho_0\rho_1`、`\sigma_2=\rho_1\rho_2`，平移 `x=\sigma_2^2\sigma_1^{-1}` ✓（**与您引的文献逐字 `(\sigma_2^2\sigma_1^{-1})^s=1` 吻合**）✓✓
$$\boxed{T_L:=(\rho_1\rho_2)^2(\rho_0\rho_1)^{-1}\in\langle\rho_0,\rho_1,\rho_2\rangle}$$ ✓
　对 `\{6,3\}` 型层（vertex-figure 侧）：`\langle\rho_1,\rho_2,\rho_3\rangle`，同理 $$\boxed{T_R:=(\rho_2\rho_3)^2(\rho_1\rho_2)^{-1}\in\langle\rho_1,\rho_2,\rho_3\rangle}$$ ✓✓
【⟹ `U_{a,b}` 的群】 $$\boxed{\Gamma_{a,b}=[3,6,3]/\langle\langle T_L^{\,a},\ T_R^{\,b}\rangle\rangle}$$ ✓✓（`U_{2,3}` 即 `a=2,b=3`）✓
【目标（窄）】 $$\exists\,x\in\Gamma_{012}\cap\Gamma_{123},\quad x\notin\Gamma_{12}\quad\Longrightarrow\quad \mathcal U_{2,3}\ \text{不存在}$$ ✓✓
【⚠️ 须核（承前档）】 `T_L`／`T_R` 的**精确落位**（facet 侧 vs vertex-figure 侧）须按 `§11E/§11F` 复核 —— 本档的推法依据**层结构的旋转子群**，与引文一致但**未逐字核对原书公式** ✓
```

## §2 边界（照录您的窄化）

```
【只追】**`T_L,T_R` 加入后产生的\textbf{最短} intersection-defect word** ✓
【若低长度候选全化入 `I_2(6)`】**报告为"当前 word search 未产生证书"**，$$\textbf{绝不写成"不存在"}$$ ✓✓
【记号纪律（照录）】**采用 regular C-group 的 `\rho` 记号**；**暂不碰 `[3,6,3]^+`／`\sigma`** ✓✓
```

## §3 状态核验（第二轮）

```
【本地（已做）】 `RGPF-II`＋`MS2008` 中**无 `(2,0)`×`(3,0)` 混合对** ✓
【文献级（您已核）】 `\{3,6,3\}` 全分类**长期未决**（`Problem 17`）；`(1,1),(2,0),(3,0)` 只是**单侧相同参数**的已知有限情形，**不能推出非对角组合已判** ✓✓
【⟹ 三态判定】 $$\boxed{\text{既未"explicitly classified"、也未"explicitly excluded"；属"仍开放参数族"}}$$ ⟹ **`U_{2,3}` 在文献层面 = OPEN（可投入）** ✓✓
【⚠️ 保留】 该判定为**文档级**（未逐字核 `§11E/§11H` 表）；若日后发现 `§11E` 已列该对，**即回退** ✓
```

## §4 下一步（待您一句授权）

```
$$\boxed{\text{是否授权执行"有界 word search"？}}$$ ✓
【选项 A（纯手工）】 只用 `\rho`-关系做**结构化推导**（寻找 `x` 的双表达式：一侧在 `\Gamma_{012}`、一侧在 `\Gamma_{123}`）—— **零程序** ✓
【选项 B（有界程序）】 用 `Todd\text{–}Coxeter`／低长度 word 枚举**追踪最短 defect**（`GAP` 类）—— **属"实现"，超出本线"不计算/不实现"之纪律** ⟹ **需您明示解禁** ✓✓
【⛔ 纪律】 本档仍**不计算、不实现**；`C2` 暂停 ✓
【边界】 §1 的 `T_L`／`T_R` 为**本档由层结构推导**（与引文一致，未逐字核原书）；§3 为**核验判定**；未制造候选／未启动搜索／未碰 RH。

## §5 【技术词回查】（补录）
```
技术词 string C-group   命中文件数=2    :: ./C3-modular-coverage-range-and-free-next-stop.md ./C3-pivot-to-offdiagonal-amalgamation.md 
技术词 Todd-Coxeter     命中文件数=0    :: 
```
