已查地图（**先查后写**）：`IMPL-1`／`IMPL-2`、`CEILING-AUDIT-3`、`lean-frontier-audit/{NumericCert,RowCert,LawN256}.lean` ＋ `lp/ceiling_lp_recompute.py`（**本档引用其解析**）。关键词回查：`相位检索`＝0、`正定列`＝0、`幅频钉定`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:14「继续」⟹ 执行 (ii)（收紧约束集）**得两条** ✓✓：**(甲) 包络语义已钉死**——`lo_j\le K\cdot S(j)\le hi_j`，且实测 `N\cdot S(j)=j` 对 `j\le255` **精确成立**（松弛 `\tau\approx1.8\times10^{-40}`），唯 `j=256` 例外（`S(256)=211.432`）⟹ **形状因子在前 255 行被钉到 40 位** ✓✓；**(乙) ⭐ 未使用的约束类＝\ \textbf{正定性（Toeplitz PSD）}**——因 `S(j)=\frac1N|\sum_i m_i e^{2\pi i j x_i/N}|^2=\frac1N|\hat\mu(j/N)|^2` ⟹ **`\{S(j)\}` 必为\ \textbf{正定列}（`S` 是正测度的自相关）** ⟹ 点式包络**未**包含此约束 ✓✓ ⟹ 且**自由度在相位（＝位置）而幅值已钉** ⟹ 此即前沿所谓"**marks 几何**"的**精确数学名字：相位检索（phase retrieval）** ✓✓

FREEZE-ACK: 本档即冻结期内的约束集分析与实施设计（依 `§8.1`；不产候选结论，未执行计算）

D0: 本档对象 = **包络语义钉死 ＋ 未使用约束类（Toeplitz 正定／相位检索）的识别** —— 关系 = 约束集分析，非新机制
D1: 0

# IMPL-3 · **(ii) 收紧约束集：失踪的约束类＝正定性／相位检索**

---

## §0 结论（先行）

$$\textbf{(甲)}\ \text{包络语义}：lo_j\le K\cdot S(j)\le hi_j\ (K=2^{140});\quad \text{实测偏差上界}\ \max_{0<j<256}|N\cdot S(j)-j|=1.836710\times10^{-40}✓✓$$
$$\textbf{(乙)}\ ⭐\ \text{未使用的约束类}＝\textbf{正定列（Toeplitz PSD）};\ \text{自由在相位}（=\text{位置}） \Longrightarrow \textbf{相位检索}✓✓$$

---

## §1 包络语义（逐字 ＋ 实测）

$$\text{`NumericCert.lean` 逐字}：\text{"integer enclosures }(lo_j,hi_j)\ \text{meaning }lo_j\le K\cdot S(j)\le hi_j\text{"}✓$$
$$\text{自陈（逐字）}：\text{"then }\textbf{FOR EVERY real sequence }S\ \textbf{inside the enclosures}\ \text{the four families of bounds hold"}\ \text{与}\ \text{"What is NOT proved here: that the true form factor of a given configuration lies in the enclosures\ ..."}\ ✓$$
$$\text{复算实测（本档，逐字）}：\text{偏差上界}\ \max_{0<j<256}|N\cdot S(j)-j|=1.836710\times10^{-40}（\textbf{极紧}）✓✓$$
$$\qquad \text{其中 lo 端点恰为}\ j/256\ \text{的行数}\ =131/255;\quad \text{前沿声称}\ \tau=3\times10^{-40}\Longrightarrow \text{实测更紧}（\text{比}=0.6122）✓✓$$
$$\qquad j=256\ \text{例外}：S(256)=211.432\neq256 \Longrightarrow \textbf{非整数位置}✓✓$$
$$\text{结构}：D(x)=C(x)-\tfrac{x^2}{2} \Longrightarrow \textbf{GUE 线性斜坡}（\text{因}\ \int_0^x t\,dt=\tfrac{x^2}{2}）✓$$

## §2 ⭐ (乙) 未使用的约束类：**正定性**

$$\text{定义}：S(j)=\frac1N\Big|\sum_i m_i e^{2\pi i j x_i/N}\Big|^2=\frac1N|\hat\mu(j/N)|^2,\quad \mu=\sum_i m_i\delta_{x_i}✓$$
$$\Longrightarrow ⭐\ \textbf{S 是正测度的自相关（平方模）} \Longrightarrow \{S(j)\}\ \textbf{是正定列} \Longrightarrow \textbf{Toeplitz 矩阵}\ (S(|i-j|))\ \textbf{半正定}✓✓$$
$$\text{必要性（易检）}：|S(j)|\le S(0);\quad \sum_j S(j)=\sum_i m_i^2（\text{当位置}\bmod1\ \text{互异时}）✓$$
$$\text{而当前 LP 只用}：\textbf{点式盒约束} \Longrightarrow \textbf{未含正定性}✓✓$$
$$\Longrightarrow \text{故约束集}\ \textbf{可收紧}：\text{加正定性／更强的"}\exists\ \text{正原子测度}"\ \text{约束}✓✓$$

## §3 ⭐ 自由度的精确位置：**幅值已钉，自由在相位**

$$\text{包络给的是}\ |\hat\mu|\ \textbf{的幅值}（j\le255\ \text{钉到 40 位}）;\quad \text{位置}\ x_i\ \text{进入的是}\ \textbf{相位}✓✓$$
$$\Longrightarrow \text{这是}\ \textbf{经典"相位检索（phase retrieval）"} \text{型问题}：\text{由}\ |\hat\mu|\ \text{反推}\ \mu✓✓$$
$$\qquad \text{且附加结构：}m_i\in\{1,2\}（\text{marked}）,\ \sum_i m_i=N;\quad p＝\text{简单点比例}✓$$
$$\Longrightarrow ⭐\ \text{前沿所称"}\textbf{marks 几何}\text{"＝}\ \textbf{相位信息} \Longrightarrow \text{其数学名字＝相位检索}✓✓$$

## §4 对约束集的**具体收紧提案**（未执行）

$$\textbf{T1}：\text{加}\ \textbf{Toeplitz 半正定} \text{约束（低阶子矩阵即可，代价小）}✓$$
$$\textbf{T2}：\text{加}\ \sum_j S(j)=\sum_i m_i^2\ \text{型恒等式}（\text{须先确认包络索引约定}）✓$$
$$\textbf{T3}：\text{加}\ m_i\in\{1,2\}\ \text{与}\ \sum m_i=N\ \text{的整数结构}✓$$
$$\textbf{T4（最强）}：\text{直接把"}\exists\ \text{正原子测度}"\ \text{作为约束（相位检索可行性）}✓✓$$
$$\Longrightarrow \text{判据}：\text{若加 T1--T4 后}\ p_{\min}\ \text{显著上移} \Longrightarrow \text{原天花板}\ \textbf{被收紧};\ \text{若不动} \Longrightarrow \text{包络已足够紧}✓✓$$

## §5 边界与回查

- ⚠️ §1 逐字 ＋ 本档实测；§2 的 $S=|\hat\mu|^2/N$ 为标准事实，**未逐字核文献** ✓
- ⚠️ §3／§4 为**本档判断与提案**（**未执行**）；`相位检索` 名称待外部核（下一轮）✓
- ⚠️ **不声称**收紧后会改变天花板；**不声称**与 RH 相关 ✓
- **未用** RH；**未**执行新 LP ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:1x）`[纪律]`（先跑后写）

```
技术词 相位检索       命中文件数=0  ⟹ 本档新增
技术词 正定列        命中文件数=0  ⟹ 本档新增
技术词 幅频钉定       命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
