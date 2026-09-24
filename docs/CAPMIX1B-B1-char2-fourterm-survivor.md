已查地图：命中（`CAPMIX1A-11-character-route-CLOSED`）⟹ 执行其 §6 之唯一未开分支（`CAP-MIX-1B`），不开新案
D0: 本档对象 = **`CAP-MIX-1B` 第一刀（`B1`）**：`B1`-A 信息指数／`B1`-B 退化因子／`B1`-C 二维 survivor／`B1`-D 真值交叉 ＋ ⭐**char 2 异常彻底闭合**
D1: 1 （新自由度：char 2 四项的**二维压缩机制**成立）
[RESEARCH]

# **`CAP-MIX-1B · B1`：char 2 四项（survivor）**

## §0 设定与结构差异

```
$$q=2^n,\qquad G=G_{q,d}\ (d\mid q-1),\qquad \boxed{d\ \text{恒为奇数}}\ (\text{因 }q-1\ \text{奇})$$ ✓
$$a+b+c+d=0\ \text{（四点 distinct）}\iff x+y+z+1=0,\ z=1+x+y,\ \text{要求}\ x,y,z,1\in G$$ ✓
```
`d` 恒奇 ⟹ **`-1\notin G` 恒成立**（与 1A 的分支结构不同）✓

## §1 `B1`-A：信息指数

```
$$r_j=2^{\,j}\bmod d,\qquad J_{\rm info}=\{j:\ r_j\notin\langle2\rangle_d\}$$ ✓
**【关键现象（与 1A 平行）】** $$r_j\ \text{为 }2\text{-幂}\ \Longrightarrow\ Q_j\equiv0:\quad (1+x+y)^{2^k}=1+x^{2^k}+y^{2^k}$$ ✓（char 2）✓✓
**【实测分布】** 39 例中 **`blind`（`J_{\rm info}=\varnothing`）＝17 例（44%）**，非盲 22 例 ✓
```

## §2 `B1`-B：退化因子（三因子）

```
$$x=y\Rightarrow Q_j(x,x)=0;\quad y=1\Rightarrow Q_j(x,1)=0;\quad x=1\Rightarrow Q_j(1,y)=0\ \Longrightarrow\ \boxed{(x+y)(x+1)(y+1)\mid Q_j}$$ ✓✓
**【⟹ 实现含义】** 在**非退化对**（`x\ne y`、`x\ne1`、`y\ne1`）上三因子非零 ⟹ 可直接用 `Q_j=0` 判定，**无需做多项式除法** ✓（本档即如此实现）✓
**【四点的相异性自动满足（照您 §6）】** $$z=1\iff x=y;\quad z=x\iff y=1;\quad z=y\iff x=1$$ ✓
```

## §3 `B1`-C：二维 survivor（⭐⭐ 本档主结果）

```
$$\text{pairs}=\{(x,y)\in G^2:\ \text{非退化}\},\qquad V_\ast=\bigcap_{r\in J_{\rm info}}\{(x,y)\in\text{pairs}:\ Q_j(x,y)=0\}$$ ✓
**【压缩率（非盲 22 例，`|V_\ast|/|\text{pairs}|`）】** $$\text{最大}\ \mathbf0.320\ (n=8,d=85);\ \text{其余多在 }0.002\text{–}0.27;\ \textbf{9 例 }V_\ast=\varnothing$$ ✓✓
**【⟹ 判定：第三层 SURVIVOR】** $$\boxed{\text{二维 Frobenius survivor \textbf{确实压缩}（} \le 0.32\cdot|\text{pairs}|\text{）}}$$ ✓✓✓（**不是二维 residual wall，也不是只有 blind**）✓
$$\text{且 }V_\ast=\varnothing\ \text{的 7 个非盲 CAP 例给出\textbf{干净 CAP 证书}}$$ ✓
```

## §4 `B1`-D：真值交叉（**单侧成立，双条件为假**）

```
**【单向（必要）】** $$\text{有效四项关系}\ \Longrightarrow\ (x,y)\in V_\ast:\quad \textbf{39/39 全过，0 违例}$$ ✓✓
**【双向为假】** $$V_\ast\ \textbf{是严格过近似}:\ |V_\ast|-|\text{valid}|\in\{0,2,6,8,14,18,24,32\}\ (\text{小量伪 survivor})$$ ⚠️
$$\text{例}:\ (6,64,21):\ \text{valid}=96,\ V_\ast=104;\quad (8,256,85):\ \text{valid}=2208,\ V_\ast=2232;\quad (11,2048,89):\ \text{valid}=264,\ V_\ast=264\ (\text{精确})$$ ✓
$$\Longrightarrow\ \textbf{可用的仍是"证书方向"}:\ V_\ast\cap\text{pairs}=\varnothing\ \Longrightarrow\ \text{CAP}$$ ✓（与 1A 同一逻辑形态）
```

## §5 ⛔ 自纠（本档检查的表观性质）

```
**【`truth` 由 `valid` 定义】** ⟹ "一致性违例＝0"是**表观（重述）**，**不是独立检验** ⚠️
$$\text{真正的独立检验是}: \textbf{valid}\subseteq V_\ast\ (\text{39/39 通过})\ \text{与}\ \text{压缩率统计}$$ ✓✓ **本档据此下判** ✓
```

## §6 ⭐⭐ 副产品：**早先的 char 2 异常彻底闭合**

```
**【论文族】** $$G_{2^{2n},\,2^n+1}\ (\Rightarrow d=2^n+1):\ \text{本档网格内 }d=5,9,17,33,65$$ ✓
**【按论文 `Definition 1` 四项定义实测】** $$\boxed{(4,16,5),\ (6,64,9),\ (8,256,17),\ (10,1024,33),\ (12,4096,65)\ \textbf{全部 CAP}}$$ ✓✓✓
$$\Longrightarrow\ \text{与论文 `Thm 1(4)`（}a+b+c+d=0\Rightarrow a=b,c=d\text{）\textbf{完全一致}}$$ ✓✓
$$\boxed{\text{早先"（64,9）非 cap"的"异常"＝我们用了\textbf{三项}定义 ⟹ 现按四项定义\textbf{彻底闭合}}}$$ ✓✓✓
```

## §7 `CAP-MIX` 全线状态与下一步

```
$$\begin{array}{c|c|c}
\text{分支}&\text{机制}&\text{状态}\\
\hline
\text{1A 奇特征三项}&R_\ast\ \text{压缩（}43\ \text{witness}+32\ \text{certificate}）\ +\ \lambda_{\rm valid}\ \text{定盲区}&CLOSED\\
\text{1A 角色路线}&Jacobi\ \longleftrightarrow\ \lambda_{\rm raw}\ \text{重编码}&CLOSED\\
\text{1B char 2 四项}&V_\ast\ \text{二维压缩（}\le0.32\text{）}&SURVIVOR（首刀）\\
\end{array}$$ ✓✓
**【下一步（1B 第二刀）】** (i) 把 char 2 的盲类（`17/39`）单独统计，试点**二阶加法 incidence**（照您 §10：`\lambda_2(G)=\sum_{x\in G}\#(G\cap(1+x+G))_{\rm valid}`）；(ii) 对 `V_\ast` 的**伪 survivor**（小量）做结构刻画 ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停 ✓
【数据】 `out/capmix1B_char2_fourterm.txt`（39 行，含 `pairs/valid/V_*/blind/truth`）；脚本 `scripts/capmix1B_char2_fourterm.py` ✓
【边界】 §3 压缩率与 §4 单侧性为实测（39 例）；§6 一致性为**逐例核对论文定义** ✓

## §附 【技术词回查】（补录）
```
技术词 survivor         命中文件数=19   :: ./ZF-3-minimal-arithmetic-input-audit.md ./C264-beta-sensitive-channel-census-three-gates-zero-candidates-and-the-location-vs-counting-criterion.md ./ASSETS-REGISTRY.md 
技术词 additive defect  命中文件数=0    :: 
```
