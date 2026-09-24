已查地图：命中（`C1-LIN-TOP1-3-scan`／`C1-LIN-linear-covering-codes-locked`）⟹ 引用，不开新案
D0: 本档对象 = `TARGET-L9` 源取报告：README 已取部分（含交叉核实）＋ `r=9` 五项待核（本档**未完成**）
D1: 0 （[REVIEW] 轮次：取源与核对，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`TARGET-L9` 取源报告（未完成，含交叉核实）**

## §1 ✅ 已取到（逐字，`wustep/maths` README）

```
【仓库性质】 "A public notebook of attacks on open problems"；agent 编排攻击，**术语**："**A dent is a verified finite improvement of a published record. A residue is an incomplete search.**" ✓✓（与我方 `SURVIVOR-5`／"量变"判据同型）
【`\ell_2(10,2)\le50`】 "A binary linear code of length 50 and dimension 40 has covering radius exactly 2 … `H_r10_n50.txt` hits every syndrome … (1024/1024, **two independent verifiers**)" ✓✓
【前值】 Nov 2025 表（Davydov–Marcugini–Pambianco, **arXiv:2511.02542 Table 5.1**）为 `\le51` ✓（与您提供一致 ✓）
【⚠️ 关键限定（逐字）】 "**Sphere covering still only gives `\ge45`，and an `n=49` search left 7 holes, so 50 is not shown optimal**" ⟹ **`r=10` 亦未闭**，且 `n=49` 搜索**留 7 洞**（"residue"）✓
【密度常数（交叉核实 ✓）】 "`(2,0)`-partition with `p(H)=10` … `\mathrm{QM}_2^2` … density bound `\bar\mu(2)\le2601/2048\approx1.27002`" ⟹ **与 `2609.16078` 摘要的 `1.27002` 一致** ✓✓
【其它已核实值】 `\mathrm{QM}_3^2,\mathrm{QM}_5^2` 给 `\ell_2(22,2)\le3325,\ \ell_2(24,2)\le6653,\ \ell_2(26,2)\le13070,\ \ell_2(28,2)\le26111`（论文值 `3389,6781,13565,26623`）✓；`r=26` 有 **19-block partition** ⟹ 定理式提升 `\ell_2(36,2)\le418271`；`r=28` 有 **28-block partition** ⟹ `\ell_2(40,2)\le1671167,\ \ell_2(42,2)\le3342335` ✓
```

## §2 ⛔ 未能取到（本档未完成项，须诚实标注）

```
【未取到】 您所述 `r=9` 的**五项**：**(1)** 39 列记录的确切 `H`；**(2)** 38 列搜索的 **17 个 kernel-block classes**；**(3)** "**14 missing incidences**" 的具体覆盖缺口；**(4)** 17 类是否穷尽目标结构族；**(5)** 是否另有结构入口 ✓
【原因】 README 可取的 3000 字符片段**只覆盖 `r=10/22–28/36–42`**；`r=9` 材料在**按问题分目录**的文件里（`problems/covering/ATTACK.md`、`WALKTHROUGH.md`、`PROBLEM.md`、`compute/*`）——**本次未取** ✓
【已触发的取源限制】 首次 `github.com/.../blob/...` **超时**；`raw.githubusercontent.com` 成功但**只回前 3000 字符**（`truncated: true`）✓
```

## §3 下一步（精确，不含猜测）

```
**(i)** 取 `problems/covering/` 目录清单（定位 `r=9` 的 `ATTACK.md`/`PROBLEM.md`/`n=38` 搜索脚本）✓
**(ii)** 逐项核对五项，并特别判定 **第 (4) 项**：17 类是否＝**整个结构族**；若仅为子族 ⟹ **在边界找第二种结构入口** ✓
**(iii)** 若 `n=38` 已有**完整非存在性证明** ⟹ **立即 CLOSED**；若只是 "residue（不完整搜索）" ⟹ **进入实际攻击** ✓✓
【⚠️ 措辞纪律（照录您 §3）】 现状只可写 $$\boxed{\text{record: }\ell_2(9,2)\le39,\quad n=38\ \text{尚未找到}}$$ **不得**写成 `\ell_2(9,2)=39` ✓
【边界】 §1 为**逐字**（README，2026-09-24 取）；§2 未取到项**明确标注未完成**；§3 为**本档自行推导**；未制造候选／未启动搜索／未碰 RH。

## §4 【技术词回查】（补录）
```
技术词 saturating set   命中文件数=1    :: ./C1-LIN-TOP1-3-scan.md 
技术词 覆盖码        命中文件数=3    :: ./C1-LIN-linear-covering-codes-locked.md ./HUNT-R2-OPEN-MATH-POOL-round1.md ./ENGINE-X-PROBLEM-pilot-v2-no-RH-ancestry.md 
技术词 kernel-block     命中文件数=1    :: ./TARGET-L9-source-fetch-report.md 
```
