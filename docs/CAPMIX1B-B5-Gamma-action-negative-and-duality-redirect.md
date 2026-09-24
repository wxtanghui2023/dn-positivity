已查地图：命中（`CAPMIX1B-B4-T-orbit-audit-and-lambda-mod-3-theorem`）⟹ 执行其 §6 之 (3)，不开新案
D0: 本档对象 = **`B5` 合并作用 `\Gamma=\langle F,T\rangle`**：`FT=TF` 验证 ＋ 轨道谱表 ＋ 混合稳定元统计（**否定结果**）＋ `23/89` 对偶比较 ＋ **路线降级与新指向**
D1: 1 （新自由度：`\Gamma\cong C_n\times C_3` 结构确立；同时**否定**"混合稳定元解释 `\lambda=0`"）
[RESEARCH]

# **`CAP-MIX-1B · B5`：合并作用（含否定结果）**

## §1 ⭐ `FT=TF` 验证通过

```
$$F(x)=x^2,\quad T(x)=1+x^{-1}\ \Longrightarrow\ F(T(x))=1+x^{-2}=T(F(x))\quad(\mathrm{char}\,2)$$ ✓✓
$$\textbf{实测}:\quad \texttt{FT\_commute}=11/11\ (\text{全部 } n),\qquad \texttt{FT\_bad}=0$$ ✓✓
$$\Longrightarrow\ \boxed{\Gamma=\langle F,T\rangle\cong C_n\times C_3\ \text{（或其商）}}$$ ✓✓
```

## §2 轨道谱（`Γ`-轨道）

```
$$\texttt{orbdiv3n\_bad}=0\ \Longrightarrow\ \boxed{\text{所有 }\Gamma\text{-轨道长度}\mid 3n}\quad(\text{实测尺寸}\in\{2,3,9,12,15,18,24\})$$ ✓✓
$$\text{谱直方图}:\ \begin{array}{c|c}
\text{spectrum}&\text{例数}\\
\hline
()&\mathbf9\ (\lambda=0)\\
(2)&11\\
(3,3)&6\\
(2,12)&4\\
(15,15)&2\\
(2,3,3)&2\\
(2,3,3,18,18,18)&2\\
(24),\ (9,9),\ (2,15,15)&1\ \text{each}\\
\end{array}$$ ✓✓
$$\Longrightarrow\ \lambda=0\iff\text{谱为空}\ (\text{同义重述});\ \ \lambda>0\ \text{时谱型不唯一}$$ ✓
```

## §3 ⛔⭐ 混合稳定元：**否定结果**（按您预设 EXIT 条件降级）

```
**【您 §3 的"真正新信息"】** $$\exists k\in[1,n-1],\ a\in\{1,2\}:\ T^a(F^k(x))=x\iff \boxed{x^{2^k}(1+x)=1}$$ ✓
**【实测】** $$\texttt{lam0}=9,\qquad \boxed{\texttt{lam0\_mixed\_G}=9},\qquad \texttt{lam0\_nomixed\_G}=\mathbf0$$ ✓✓
$$\Longrightarrow\ \textbf{全部 9 个 }\lambda=0\ \text{案例中，}G\ \textbf{内都有}混合稳定元存在}\ \Longrightarrow\ \textbf{混合稳定元\textbf{不是} }\lambda=0\ \text{的障碍}$$ ✓✓
$$\Longrightarrow\ \boxed{\textbf{按您预设 EXIT}:\ \text{"合并群作用}\to\lambda=0\ \text{判据"这条线\textbf{降级}}}$$ ✓✓✓
```

## §4 ⭐ `23/89` 对偶比较（`n=11`）

```
$$\text{实测两例}\ \textbf{完全同型}:\quad (n=11,\ q=2048,\ d=23):\ \lambda=0,\ \text{谱}=(),\ \text{mixed}(G)=1;\qquad d=89:\ \text{同}$$ ✓✓
$$\Longrightarrow\ \text{两者在 }\Gamma\text{-不变量上\textbf{无法区分}}\ \Longrightarrow\ \textbf{支持"互补 }d\leftrightarrow m\ \text{机制"}\ (\text{您给出的替代指向})$$ ✓✓
$$\text{注}:\ n=11,\ q-1=2047=23\cdot89\ \Longrightarrow\ (d,m)=(23,89)\ \text{与}\ (89,23)\ \text{严格互补};\ \mathrm{ord}_d(2)=11\ (\text{奇})$$ ✓
```

## §5 本档判词

```
$$\boxed{(i)\ \Gamma\cong C_n\times C_3\ \text{结构成立（含 }FT=TF\text{）};\qquad (ii)\ \text{轨道长度}\mid3n;\qquad (iii)\ \text{混合稳定元\textbf{不能}解释 }\lambda=0}$$ ✓✓
$$\Longrightarrow\ \textbf{两条并存结论}:\ \text{结构透镜有效；但"合并作用}\to\lambda=0\ \text{判据"路线\textbf{关闭}}$$ ✓✓
**【⟹ 新指向（照您 §末）】** $$\boxed{\text{转向互补 }d\leftrightarrow m\ \text{机制}\ (m=(q-1)/d)}$$ ✓✓
```

## §6 下一步

```
**(1)** **互补对偶机制**：对每个 `(d,m)` 对研究 $$\lambda(G_{q,d})\ \text{与}\ \lambda(G_{q,m})\ \text{的关系}$$ ✓✓（`n=11` 已有 `(23,89)` 同型样本）
**(2)** 已在手的两条充分机制分开登记：$$(a)\ -1\in\langle2\rangle_d\ \&\ 3\nmid d\Rightarrow\lambda=0\ (\text{B4，覆盖 }7/9);\qquad (b)\ \text{互补对偶（待定）}$$ ✓
**(3)** 盲类（`17/39`）与 `\lambda>0` 大容量结构仍待开 ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停 ✓
【数据】 `out/capmix1B5_Gamma.txt`（39 行，含谱与 mixed 计数）；脚本 `scripts/capmix1B5_Gamma_action.py` ✓
【边界】 §1–§4 为实测（39 例 / 11 个 `n` 实例）；§5 降级为**按您预设 EXIT 的判定** ✓

## §附 【技术词回查】（补录）
```
技术词 stabilizer       命中文件数=5    :: ./E-GATE-and-Lemma-R-R2-CLOSED.md ./ASTRA-TRANSFER-three-attacks.md ./A5-FORMAL-SPEC-r9-n38.md 
技术词 duality          命中文件数=61   :: ./MASTER-NOGO-AND-LIVE-PATHS.md ./O3-mechanism-audit-and-ontology.md ./V145-archimedean-boundary-three-gate-audit-deninger-hit.md 
```
