# AUDIT-2026-09-29n — **BÖW 2004 为 closed access：取原文之路\ \textbf{穷尽}；Kéri 只给归因、\textbf{不给公式} ⟹ 自推为\ \textbf{唯一路}**

> **性质**：**取证穷尽 ＋ 路线判定**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 11:1x ✓
> **唐先生问（逐字）**：「要能获取原作论文，我们还需要自己推导么？」✓

**已查地图**：接续 `AUDIT-29i`（van Wee 一手）／`29f`（复现账）✓

D0: 本档对象 ＝ **档案已有**（文献状态——无新数学对象 ✓）
D1: 0（产出＝**取原文穷尽 ＋ 反事实前提否证** ⚠️✓）

---

## §0 先直接回答唐先生

$$\boxed{\text{若真能获取原文} \Longrightarrow \text{对"复现 }107\text{"而言，\ \textbf{不必}自推（读它即可）}✓}$$
$$\boxed{\text{但前提\ \textbf{不成立}:\ BÖW 2004 为 closed access，\ \textbf{取不到}}✗\ \Longrightarrow\ \text{自推\ \textbf{不是可选项，是唯一路}}}$$

## §1 取证穷尽（**✓✓ 逐条实测**）

| 源 | 手段 | 结果 |
|---|---|---|
| OpenAlex | `works/doi:10.1002/jcd.20008` | $\texttt{oa\_status}=\textbf{closed}$；$\texttt{any\_repository\_has\_fulltext}=\textbf{False}$；**无任何副本** ✗ |
| Wiley | `pdfdirect/...` 与 `pdf/...` | **403**（5677 / 5659 B HTML，非 PDF）✗ |
| Kéri 综述（423k 字符，免费） | 搜 Bertolo(13)／Weakley(11) | **只给归因，不转录公式** ✗ |
| Haas 2008 论文 | 搜 Bertolo(0)／Weakley(0) | **未引** ✗ |

$$\textbf{摘要逐字}（可得）:\ "\text{The results include new explanations of short binary and ternary covering codes, several new constructions and codes, and }\textbf{a general lower bound for }R=1"✓$$
$$\therefore\ \text{确知有该界，}\textbf{但正文不可得}✗$$

## §2 Kéri 之归因逐字（**✓ 确认 107 之归属，但不给式**）

$$\textbf{Kéri 逐字}:\ "107\le K(10,1)\le120.\ \text{Prompt felső korlát }128.\ \text{A felső korlát javítása }120\text{-ra }[58,64].\ \text{Prompt alsó korlát: }94.\ \text{Az alsó korlát javítása }96\text{-ra }[18],\ 97\text{-re }[46],\ 103\text{-ra }[52],\ 105\text{-re }[67],\ \mathbf{107\text{-re }[130]}"$$
$$[130]=\text{R. Bertolo, P.R.J. Östergård, W.D. Weakley, \textit{An updated table of binary/ternary mixed covering codes}, J. Combin. Des. }\mathbf{12\ (2004)\ 157\text{--}176}$$
$$\therefore\ \boxed{\text{107\ \textbf{确实}归 }[130];\ \text{且 }105\ \text{归 }[67]=\text{Zhang 1991}\ \text{—— 归因链完整}✓}$$
$$\text{但 Kéri 之 13 处 Bertolo 皆用于\ \textbf{分类/构造/Table}（如 }K(3,1){=}5\text{、}K((3h{-}1)/2,1;1)\text{、}(9,16)_2\ \text{码）}，\textbf{未}给 general }R{=}1\ \text{之式}}✗$$

## §3 本会话可取之全部一手源（**✓✓ 已尽**）

| 源 | 状态 |
|---|---|
| van Wee 1991 博论（含 Paper 5/6） | **✓✓ 已取**（TU/e 免费，8.28 MB）→ 给 $103$ |
| Gijswijt--Polak 2025 | **✓✓ 已取**（arXiv 免费）→ 给 $105.2223\Rightarrow106$ |
| Wu--Chen 2024 | **✓✓ 已取**（arXiv 免费）→ surfeit，$n{=}10$ 不适用 |
| Haas 2008 博论 | **✓✓ 已取**（freidok 免费）→ excess 族止于 $103$ |
| Kéri 综述 | **✓✓ 已取**（免费）→ 归因链 |
| **BÖW 2004** | **✗ closed，取不到** |

$$\therefore\ \boxed{\text{可取者已尽取；不可取者恰是\ \textbf{唯一藏 }107\ \text{之处}}}$$

## §4 因此（**路线判定 ✓**）

$$\textbf{(i)}\ \text{自推}\ \text{—— 唯一路，但本会话已系统证：可实现算术族 }103{-}104,\ \text{SDP-3 }105.2223\Rightarrow106$$
$$\textbf{(ii)}\ \text{取原文}\ \text{—— 本档证\ \textbf{不可行}（closed）}✗$$
$$\therefore\ \boxed{\text{须自推\ \textbf{且须非松弛型（integrality/几何）机制}；本会话已定位缺口，但未产出该机制}}✓$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "取原文穷尽" "归因有公式无" "自推唯一路"
技术词 取原文穷尽   命中文件数=0    ::
技术词 归因有公式无  命中文件数=0    ::
技术词 自推唯一路   命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **OpenAlex／Wiley／Kéri／Haas 四处实测** ＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）
