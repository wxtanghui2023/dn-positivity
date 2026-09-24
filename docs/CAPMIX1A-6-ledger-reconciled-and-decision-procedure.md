已查地图：命中（`CAPMIX1A-5-degenerate-candidates-and-falsewall-orbit-structure`）⟹ 执行其 §5 之 (1)，并**升级其 §2/§4 的解释**，不开新案
D0: 本档对象 = **账本对齐**（`204=\text{processed}+\text{skipped}`，每条 `continue` 计数）＋ **差异解释**（纯口径）＋ ⭐**升级结论：非盲类上是"判定过程"而非"不完备判据"**
D1: 1 （延续新自由度；本档把"缺失判据"**更正为"完备判定过程（限非盲类）"**）
[RESEARCH]

# **`CAP-MIX-1A(6)`：账本对齐 ＋ 判定过程**

## §1 ⭐ 账本（照您要求，每条 `continue` 都计数）

```
$$\textbf{LEDGER}:\quad \text{cases\_after\_d\_filter}=204$$
$$\text{blind}(J=\varnothing)=126,\qquad \text{individual}(h_j=X-1)=3,\qquad \boxed{\text{skip } \mathrm{deg}\,g_*<2=20}\ (\text{其中 }\deg0:7,\ \deg1:13),\qquad \text{skip }\deg>200=0$$
$$\boxed{\text{processed}=55},\qquad \text{cls}: T>0=43,\ \text{Fwall}=11,\ \text{degen}=1$$
**【自洽检查（全部通过）】** $$55=43+11+1\ \checkmark;\qquad 126+3+20+55=204\ \checkmark;\qquad \text{skip total}=149\ \checkmark$$ ✓✓
**【⟹ 您的怀疑成立】** `N_skipped = 20`（正是 `\deg g_*<2` 两条路径），故本档得 `1+11`，前档得 `8+24` ✓✓
```

## §2 ⭐ 差异解释：**纯口径，两档皆正确**

```
**【原因（已定位）】** 前档把 `\deg g_*<2` 的 20 例**也纳入三层分类**；本档把它们**排除在 processed 之外** ✓
$$\text{前档}:\ \text{case3}=24=\underbrace{11}_{\text{多根 Fwall}}+\underbrace{13}_{\deg g_*=1,\ g_*=X-a\ (a\ne1)};\qquad \text{case4}=8=\underbrace{7}_{\deg g_*=0\ (g_*=1)}+\underbrace{1}_{\text{仅退化根}}$$ ✓✓
$$\text{本档}:\ \text{Fwall}=11,\ \text{degen}=1,\ \text{skip}=20\ (13+7)$$ ✓✓ **两者数字一致，只是切法不同** ✓✓
**【⟹ 统一母集合（今后唯一口径）】**
$$\boxed{204=\underbrace{126}_{\text{blind}}+\underbrace{3}_{\text{个体证书}}+\underbrace{75}_{\text{非盲}}\ ;\qquad 75=\underbrace{43}_{\text{显式 witness}}+\underbrace{32}_{\text{无有效端点（证书）}}}$$ ✓✓
$$\text{细分为}:\quad 32=\underbrace{11}_{\text{多根}}+\underbrace{13}_{\deg g_*=1}+\underbrace{7}_{\deg g_*=0}+\underbrace{1}_{\text{退化根}}$$ ✓✓
```

## §3 ⭐⭐ 升级结论（本档核心，取代"不完备判据"）

```
**【关键观察】** AP 端点 `x` 必须满足**所有**信息型 `j` 的 `Q_j(x)=0` ⟹ $$x\in R_*:=\{\text{根集}(\gcd_j h_j)\cap G\}$$ ✓✓
　而 `x=1` 是否在 `R_*` 中**并非必然**（`Q_j(1)=0` 仅当 `2^{\,r-1}\equiv1\ (\mathrm{mod}\ p)`）⟹ 故 `\deg g_*` 可为 `0` ✓（**解释了 §2 的 7 例**）
**【⟹ 判定过程（非判据）】** 算 `R_*`，然后：
$$(i)\ \exists x\in R_*\ \text{为\textbf{有效端点}}\ (x\ne1,\ -1-x\in G,\ -1-x\ne1,\ -1-x\ne x)\ \Longrightarrow\ \textbf{非 cap，且给出显式 witness};$$
$$(ii)\ \text{无有效端点}\ \Longrightarrow\ \textbf{cap，且给出证书}$$ ✓✓
**【⟹ 在非盲类上\textbf{完备}】** $$75=43\ (\text{witness})+32\ (\text{证书}):\quad \textbf{每一例都被判定，且零错误（}\text{cap\_with\_true}=0,\ \text{noncap\_no\_true}=0\text{）}$$ ✓✓✓
**【⟹ 机制的真实身份】** $$\boxed{\text{Frobenius 机制}=\text{候选集压缩}:\ G\ (d\ \text{个})\ \longrightarrow\ R_*\ (\text{通常 }2\text{–}4\ \text{个})}$$ ✓✓（**这正是我们要的"容量压缩"，而不是"另一个证书形式"**）
**【⟹ 前一档"伪根墙＝机制边界"的说法\textbf{应更正}】** 那 24 例**不是墙**，而是**证书**（`R_*` 内无有效端点）✓✓
```

## §4 真正的剩余缺口 = **blind 类（126 例，62%）**

```
$$\text{blind}:\ J=\varnothing\iff\{p^{\,j}\bmod d\}_j\subseteq\{p^0,p^1,\dots\}\ \Longrightarrow\ \text{所有 }Q_j\equiv0\ \Longrightarrow\ R_*=G\ (\text{零压缩})$$
**【⟹ 缺口精确表述】** **不是"判据不完备"，而是"压缩失效区"** ✓✓
$$\text{blind 内含}:19\ \text{caps},\ 107\ \text{non-caps}\ (\text{由 }54=3+32+19\ \text{推出})$$ ✓
**【⟹ 下一步方向（唯一）】** 为 blind 类**另找压缩源**，而非在高阶 gcd 上继续加 `j` ✓✓
```

## §5 下一步（三件）

```
**(1)** 跑一遍**判定过程**脚本：对全部 75 例输出"witness 或 certificate"＋与独立真值逐项比对（**把"限非盲类完备"变成可核验表格**）✓✓
**(2)** 把 §3 的**证书可靠性**写成一行证明（推导已在档：`x+y=-1,\ x,y\in G\Rightarrow Q_j(x)=0\ \forall j`）✓
**(3)** blind 类另找压缩源（候选：**用 `x^d=1` 与 `(-1-x)^d\ne1` 的联立**，或子群在加法下的像结构）✓
【⛔ 纪律】 **今后计数一律用 §2 统一口径**（`8/24` 与 `1/11` 作废）✓；计算仅本实验；`U_{2,3}` 暂停 ✓
【数据】 `out/capmix1J_ledger.txt`（脚本输出）；脚本 `scripts/capmix1j_ledger_audit.py` ✓
【边界】 §3 的"完备"为**本批 75 例实测 + 推导支持**，未写成定理文本 ✓

## §附 【技术词回查】（补录）
```
技术词 candidate set    命中文件数=0    :: 
技术词 decision procedure 命中文件数=0    :: 
```
