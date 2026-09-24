已查地图：命中（`C3-audit-of-54-and-correction-of-folding-note`／`C3-nontriviality-resolved-by-dart-counting`／`C3-endpoint-filter-and-modular-reduction`）⟹ 引用，不开新案
D0: 本档对象 = **⑤ 六候选展开**（`⑤-1`\ldots`⑤-6`）＋ **合法改写引理表（含一处自捉）** ＋ **⑤ 的结构性天花板**
D1: 0 （[REVIEW] 轮次：手工化简，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **⑤ 六候选 ＋ ⑤ 的天花板**

## §1 合法改写引理（逐条自验）

```
**【A】** 对任意对合 `u,v`：$$uv\ \text{是对合}\iff uv=vu$$ ✓（`(uv)^2=1\iff uvuv=1\iff uv=v^{-1}u^{-1}=vu`）✓
**【B】** 生成元共轭翻转：$$\rho_0a\rho_0=\rho_1a\rho_1=a^{-1},\qquad \rho_2c\rho_2=\rho_3c\rho_3=c^{-1},\qquad \rho_1b\rho_1=\rho_2b\rho_2=b^{-1}$$ ✓（直接验：`\rho_0(\rho_0\rho_1)\rho_0=\rho_1\rho_0=a^{-1}` ✓）
**【C】** 阶关系给的改写：$$a^{-1}=a^2,\quad c^{-1}=c^2,\quad b^{-1}=b^5$$ ✓
**【D】** 额外关系给的改写：$$T_L=b^2a^{-1}=ab^{-2};\qquad T_R=b^2c^{-1};\qquad T_R^{-1}=cb^{-2}=(b^2c^{-1})^2$$ ✓
**【E】** 远距交换：$$[\rho_0,\rho_2]=[\rho_0,\rho_3]=[\rho_1,\rho_3]=1$$ ✓
```

## §2 ⚠️ 自捉：一条**看似自然实则错误**的"引理"

```
**我一度想用** $$uvu=vu\ (\text{对合 }u,v)$$ **✗✗ 这是\textbf{错的}** ✓
【反例】 `S_3` 中 `u=(12),v=(23)`：`uvu=(13)` 而 `vu=(132)=(123)^{-1}`，**不相等** ✓✓
【错因】 把"若 `uvu=vu` 则 `uv=v`"的\textbf{蕴含方向}当成了恒等式 ✓
【⟹ 正确可用者只有 §1 的 A–E】 ✓
```

## §3 六候选的首轮改写（保留完整 `\rho`-链）

```
**`⑤-1\ x_1=T_LT_R=ac^{-1}`**：$$ac^{-1}=\rho_0\rho_1\rho_3\rho_2\ \xrightarrow{[\rho_1,\rho_3]=1}\ \rho_0\rho_3\rho_1\rho_2\ \xrightarrow{\rho_1\rho_2=b}\ \boxed{\rho_0\rho_3b}$$ ✓
　⟹ **两端 `\rho_0,\rho_3` 同时保留**；判：**未进入 `\Gamma_{012}\cap\Gamma_{123}`**（`T_LT_R` 一般只在\textbf{乘积集} `\Gamma_{012}\Gamma_{123}` 内，不在交集内）✓✓
**`⑤-2\ x_2=x_1^2=(\rho_0\rho_3b)^2`**：令 `w:=\rho_0\rho_3`（对合）⟹ $$x_2=wbwb=w(bwb)$$；而 `\rho_0b\rho_0=\rho_0\rho_1\rho_2\rho_0\xrightarrow{[\rho_0,\rho_2]=1}\rho_0\rho_1\rho_0\rho_2`，其中 `\rho_0\rho_1\rho_0=a\rho_0` ⟹ **`\rho_0` 无法消去**（**无可用关系**）✓✓
　⟹ **该项同样保留两端；无证书** ✓
**`⑤-3/⑤-4\ (T_LT_R)^3,(T_LT_R)^6`**：同理展开为 `\rho_0\rho_3b` 的奇/偶幂；**`\rho_0,\rho_3` 只能被"移动到彼此相邻"**，**不能被删除**（**§3 的链与您前档的端点筛选一致**）✓
**`⑤-5\ T_LT_RT_L=(ac^{-1})(b^2a^{-1})`**：由 `a^{-1}` 引入**第三个 `\rho_0` 因子**；**目前无引理可把两个 `\rho_0` 相关因子合并消去**（**`a` 与 `b^2` 只有 `T_L=b^2a^{-1}=ab^{-2}` 一条换序关系，不产生 `\rho_0` 的成对消去**）✓
**`⑤-6\ T_RT_LT_R^2`**：`T_R^2=cb^{-2}`；$$T_RT_LT_R^2=(b^2c^{-1})(ab^{-2})(cb^{-2})$$ ⟹ **左右各带一次 `\rho_3`、中间带 `\rho_0`**；**无端点消去** ✓
```

## §4 ⭐⭐ 结构性命结论：⑤ 的天花板

```
【观察】 全部候选的化简卡在同一处：$$\text{能否消去端点}=(\text{子群}\ \textbf{成员性问题})\ \text{而非}\ \text{字改写问题}$$ ✓✓
【⟹ 天花板】**合法交换 ＋ 基本共轭**（`§1` A–E）**只能验证"短字形式的证书"**，**不能判定成员性** ✓✓
【⟹ 对 `⑤` 的判定】**该手工候选族\textbf{未产生} intersection-defect 证书** ✓（**照您纪律：不写 CLOSED／不存在**）✓✓
【⟹ 三条出路（供裁）】 **(i)** 手工**结构化**论证：把 `\Gamma` 表为某个已知商（如 modular 商），在其上读 intersection（**需新的结构输入**）✓；**(ii)** 解禁 `B`（有界 `Todd\text{–}Coxeter`／低长度枚举）——**唯一能\textbf{判定}成员性的手段** ✓；**(iii)** 承认 `⑤` 到此为止，回参数级审计 ✓
```

## §5 状态（未变）

```
$$\begin{array}{c|c}
⑤-1\ldots⑤-6\ \text{展开}&\checkmark\ (\text{已做})\\
\text{端点消去}&\times\ (\text{合法手段不足})\\
\text{intersection-defect 证书}&\textbf{尚无}\\
U_{2,3}&\textbf{OPEN}\\
\mathrm{GAP}\ \text{／Todd–Coxeter}&\textbf{LOCKED}\\
\end{array}$$ ✓
【⛔ 边界】 本档**未得证书**；§1 引理 A–E 与 §3 各链**皆可手验**；§2 为**自捉**；§4 为**本档判定**；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 coset enumeration 命中文件数=0    :: 
技术词 subgroup membership 命中文件数=0    :: 
```
