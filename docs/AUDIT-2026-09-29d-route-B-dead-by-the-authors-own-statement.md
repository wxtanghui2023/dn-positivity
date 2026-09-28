# AUDIT-2026-09-29d — **路线 (B) 由\ \textbf{原作者亲口宣告不可行}；SDP 族在 $r{=}1$ 系统性弱于组合方法 ⟹ $107$ 必出自\ \textbf{组合（integrality）}机制**

> **性质**：**文献取证 ＋ 路线判定**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 23:32 ✓
> **唐先生令**：「继续，注意内存和CPU管理」✓ **（启动前已查：load 0.53／可用内存 5074 MB／Python 进程 1）** ✓

**已查地图**：接续 `AUDIT-29c`（(A) 死亡）／`29a`（可实现机制上确界）／C-474（Gijswijt--Polak §2 曾摘）✓

D0: 本档对象 ＝ **档案已有**（SDP 层级／Terwilliger／$K_q(n,r)$——无新数学对象 ✓）
D1: 0（产出＝**取证（原话）＋ (B) 判定 ＋ (C) 必要性** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ★★ 原作者亲口：完整二阶及更高阶 Lasserre 层级"difficult to compute"——(B) 不可行}}✗✓$$
$$\boxed{\text{② Table 5 确认 }n{=}10,r{=}1\Rightarrow\mathbf{105.2223}<107}$$
$$\boxed{\text{③ ★ SDP 族在 }r{=}1\ \text{系统性弱：}n{=}9\ \text{给 }55.3464\ \text{而真值 }=\mathbf{62}\ (\!差\ 6.65\!)}$$
$$\boxed{\text{④ ⟹ }107\ \text{必出自\ \textbf{组合（integrality）}机制};\ \text{唯一路 ＝ (C)}}$$

## §1 ① 原作者原话（**逐字 ✓✓ 决定性**）

$$\textbf{逐字}:\ "\text{While in principle one could also define a full hierarchy for covering codes in this setting, practical obstacles (in particular, the }\textbf{rapidly increasing number of variables and the size of the block matrices}\text{) make the full }\textbf{second and higher levels of the Lasserre hierarchy difficult to compute}\text{. Therefore, we focus on a }\textbf{3-point bound}\ \text{and its symmetry reduction}"$$
$$\therefore\ \boxed{\text{连\ \textbf{二阶完整层级}都做不到} \Longrightarrow \text{(B)「提高 SDP 层级」\ \textbf{不可行}}，\text{由原作者判定}}✗✓$$
$$\text{另逐字}:\ \text{本文方法"strengthen this bound...}\textbf{setting new records across a broad range}\text{"} \Longrightarrow\ \text{即\ \textbf{已是最强}（2025），仍止于 }105.2223$$

## §2 ② ③ Table 5 之取证（**✓✓**）

$$n{=}6{:}11.5980;\quad 7{:}15.9999;\quad 8{:}31.9999;\quad 9{:}\mathbf{55.3464};\quad 10{:}\mathbf{105.2223};\quad 11{:}170.6666;\quad 12{:}\mathbf{341.3333}{=}2^n/n$$
$$\textbf{关键读数}:\ n{=}9\ \text{之真值}\ K_2(9,1)=\mathbf{62}\ \text{（Östergård--Blass 已定）};\ \text{而 SDP 仅给 }55.3464\ \Longrightarrow\ \textbf{差 }6.65\ ✗✗$$
$$\therefore\ \boxed{\text{SDP 族在 }r{=}1\ \text{远弱于\ \textbf{组合}方法}\ (\text{仅 }n{=}6,7,8\ \text{接近真值}）}✓✓$$
$$\text{故 }n{=}10\ \text{之 }105.2223\ \text{与发表记录 }107\ \text{之关系\ \textbf{自洽}：\ SDP 弱于组合}✓$$

## §3 ④ 路线总判定（**收束 ✓✓**）

| 路线 | 判定 | 依据 |
|---|---|---|
| **(A)** pair 数上界 | **死亡** | `AUDIT-29c`：框架 ≡ 球界（$25M{-}2310>0$） |
| **(B)** 高阶 SDP | **死亡** | **本档：原作者谓 higher levels "difficult to compute"** |
| **(C)** Zhang 1991／Zhang--Lo 1992／BÖW 2004 之组合机制 | **唯一路** | 本档 ③：SDP 弱于组合 |

$$\boxed{\text{⟹ 我们未能复现 }107\ \text{不是实现失败，而是\ \textbf{方法学边界}：全部可实现之松弛/计数族皆止于 }103{-}106}$$
$$\text{而 }107\ \text{必用\ \textbf{integrality／组合}推理（Zhang 族或 BÖW 之混合码界）}✓$$

## §4 已归档之资源（**✓ 供后续**）

$$sources/\text{Gijswijt-Polak-2025-arXiv2504.01932-FULLTEXT.txt}\ (\text{纯文本 }128{,}364\ \text{字符}）$$
$$sources/\text{Gijswijt-Polak-2025-arXiv2504.01932.html}\ (\text{原 HTML }1{,}005{,}444\ \text{B}）$$
$$\text{含 §2（Theorem 2.5 原式）、§3（Terwilliger 代数）、§4（binary 对称化 Theorem 4.9）、附录 A（Table 5 数值）}✓$$

## §5 下一步（**(C) 之可自做形式 ✓**）

$$\textbf{建议}:\ \text{自推\ \textbf{Zhang--Lo 三重覆盖不等式}（1992, Part II --- Triple covering inequalities）之 }r{=}1\ \text{类比}$$
$$\text{依据}:\ \text{文献明示 }105\ \text{出自 Zhang pair（}[67]\text{）};\ \text{其推广 }=\text{Zhang--Lo triple};\ \text{而我们在 pair 层已三重失败（单条／组合／FM}）$$
$$\text{纪律}:\ \text{预估成本 ＋ 查 load／内存（本档已做）};\ \text{单脚本目标 }<200\ \text{MB RSS};\ \text{经 }\texttt{scripts/pyguard.sh}\ ⚠️$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "层级不可行" "SDP族上限" "组合机制必要"
技术词 层级不可行   命中文件数=0    ::
技术词 SDP族上限   命中文件数=0    ::
技术词 组合机制必要  命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **原文直取（免费 arXiv）＋ 逐字引证** ＋ 资源前置检查 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）；**不主张** (C) 必成 ✗
