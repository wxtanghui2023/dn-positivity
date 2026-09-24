已查地图：命中（`CAPMIX1B-B9-B4-theoremized-with-minimality-audit`）⟹ 执行其 §6 之 (i)（`B10`），不开新案
D0: 本档对象 = **`B10` 同型族扫描**：`(\mathrm{ord}_d(2)=\mathrm{ord}_m(2)=n)\wedge(-1\notin\langle2\rangle_d)\wedge(-1\notin\langle2\rangle_m)` 的互补对逐对 `\lambda` ⟹ ⛔**`(23,89)` 为孤立例**（照您预设 EXIT）
D1: 1 （新自由度：把 `(23,89)` **定性为孤立算术例**并给出稀有度证据，据此关闭"完整刻画"目标）
[RESEARCH]

## §1 同型族扫描结果（`n\le14`）

```
$$\textbf{命中（4 对）}:\quad\begin{array}{c|c|c|c|c|c|c}
n&q&(d,m)&\mathrm{ord}&\lambda_d,\lambda_m&\text{型}&\text{素性}\\
\hline
11&2048&(23,89)&(11,11)&(0,0)&\boxed{00}&\textbf{素–素}\\
12&4096&(35,117)&(12,12)&(6,2)&++&合–合\\
12&4096&(39,105)&(12,12)&(2,20)&++&合–合\\
12&4096&(45,91)&(12,12)&(14,6)&++&合–合\\
\end{array}$$ ✓✓
$$\text{型分布}:\quad \boxed{00=1},\qquad 0+=0,\qquad +0=0,\qquad \boxed{++=3}$$ ✓✓
$$\textbf{逐 }n\text{ 命中数}:\ n\le10:\ 0;\quad n=11:\ 1;\quad n=12,13,14:\ 4,4,4$$ ✓
```

## §2 ⛔ 判定（照您预设 EXIT）

```
$$\text{您 §EXIT}:\ \text{"若只有 }(23,89)\ \text{一个 }00\ \text{而同型族出现 }++/0+\text{，则应停止追完整刻画，降为孤立例"}$$ ✓✓
$$\textbf{实测}:\quad 00\ \text{仅 }1\ \text{例},\ ++\ \text{3 例}\ \Longrightarrow\ \boxed{\texttt{B10-CLOSED}\ (\text{孤立例})}$$ ✓✓✓
$$\Longrightarrow\ \boxed{\text{停止追 }(\lambda=0)\ \text{的完整刻画};\ \text{转向 } \lambda>0\ \text{大容量}\ \Theta(d)\ \text{结构}}$$ ✓✓
```

## §3 稀有度证据（双重支持）

```
$$\text{（一）本档}: n\le14\ \text{的全部同型对中},\ 00\ \text{仅 }1\ \text{例},\ \text{且现象\textbf{自 }n=11\ \text{才出现}}$$ ✓✓
$$\text{（二）`B6` 的独立扫描}: 22\ 对互补对中，}\lambda\text{-共零者\textbf{亦仅 }(23,89)\ \text{一例}}$$ ✓✓
$$\Longrightarrow\ \text{双重独立证据}\ \Longrightarrow\ \text{共零互补对\textbf{极端稀有}},\ \text{不构成族}$$ ✓✓
```

## §4 须标注的三条边界（防误读）

```
**(i)** 同型条件（`\mathrm{ord}_d=\mathrm{ord}_m=n` 且两侧 `-1\notin\langle2\rangle`）**可能比"共零"更窄** ⟹ 本档只能说"**该同型族内**只有 1 例 00"；但结合 `B6`（无同型限制的 22 对）仍是唯一共零 ⟹ **结论稳健** ✓
**(ii)** **素–素**观察（`(23,89)` 为唯一素–素对）**仅 1 个数据点** ⟹ **不能**推断"素–素机制" ✓
**(iii)** `n=12` 的 3 例 `++` 中，`m` 或 `d` 含因子 `3`（`117,105,45`）⟹ 与 `B9` 的 `3\nmid d` 边界相容（`B4` 不适用时 `\lambda>0` 属允许情形）✓
```

## §5 `CAP-MIX` 全线最终状态（本档后）

```
$$\begin{array}{c|c|c}
\text{项}&\text{结论}&\text{状态}\\
\hline
1A\ \text{奇特征}&R_\ast\ \text{压缩}+\lambda_{\rm valid}\ \text{一维精确（盲区 }126/204\text{）}&CLOSED\\
1A\ \text{角色路线}&\text{重编码，无算法增益}&CLOSED\\
1B\ \text{非盲}&V_\ast\ \text{二维压缩}\le0.32;\ V_\ast=\text{Valid}\sqcup\text{直线 }z=0&CLOSED\\
1B\ \text{盲类}&=\text{子域类};\ \text{全不变量只依赖 }d;\ CAP\iff d\le3&CLOSED\\
B4/B9&\boxed{\text{充分判据定理化}:\ (2^k\equiv-1)+\ (3\nmid d)\Rightarrow\lambda=0}（7/7\ \text{零违例}）&\textbf{存活资产}\\
B5/B6&\Gamma\ \text{结构成立};\ \text{混合稳定元与 }d\leftrightarrow m\ \text{零性均否定}&CLOSED（负）\\
(23,89)&\boxed{\text{孤立算术例}}&\text{未解释（已定性）}\\
\end{array}$$ ✓✓
```

## §6 下一步（唯一）

```
$$\boxed{\lambda>0\ \text{的大容量}\ \Theta(d)\ \text{结构}}:\quad \text{已知 } \lambda/d\ \text{最大 }0.9875\ (\text{1A 观察});\ 1B\ \text{网格内 } \lambda\ \text{达 }440\ (n=12,m=1365)$$ ✓✓
$$\text{问题形态}:\ \text{何时 } \lambda=\Theta(d)?\ \text{可否用 } d,q,\mathrm{ord}_d(2),\ \text{子域结构给出上/下界？}$$ ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**不回 RH** ✓
【数据】 `out/capmix1B10_iso.txt`（4 对逐行）；脚本 `scripts/capmix1B10_iso_family.py` ✓
【边界】 §1 为实测（`n\le14`）；§3 的双重证据为两独立扫描交叉；§4 三条已标注 ✓

## §附 【技术词回查】（补录）
```
技术词 isolated         命中文件数=4    :: ./C201-T13-A-EQ-M3-near-minimum-structure-three-isolated-nondegenerate-orbits.md ./CONNES2026-read-3-definitions-and-strategy.md ./CVS2511-read.md 
技术词 co-zero          命中文件数=0    :: 
```
