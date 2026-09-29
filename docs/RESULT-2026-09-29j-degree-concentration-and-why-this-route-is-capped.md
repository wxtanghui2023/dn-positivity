# RESULT-j（2026-09-29）—— $G_3(P)$ **度数集中**（强规律）＋ 该路线**被 $|Q|$ 截断**之判定

> **性质**：**实测 ＋ 结构判定**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:25 ✓

**已查地图**：`RESULT-i`（$f$ 表）／`RESULT-h`（单射）／`RESULT-g` ✓

D0: 本档对象 ＝ **档案已有**（图论度数分布—经典 ✓）
D1: 0（产出＝**一强经验规律 ＋ 一否证 ＋ 一相关性观察** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ }m_p=\deg_{G_3(P)}(p)\ \text{确认};\ n_j=\#\{p:\deg=j\};\ \sum jn_j=2E_3(P)✓}$$
$$\boxed{\text{② ✓✓ 强规律（新）}:\ n_0+n_1+n_2+n_3\le\mathbf 5\ (\text{实测 }0\text{--}5;\ |P|\approx23\text{--}28)\ ⟹\ \text{度数集中在 }4\text{--}7}✓✓$$
$$\boxed{\text{③ ✗ 该路线被 }|Q|\ \text{截断}:\ u\le\sum f(j)n_j\approx2|P|\approx50\ \gg\ |Q|\approx25\ ⟹\ \text{仍平凡}\ ✗}$$
$$\boxed{\text{④ ⚠️ 弱相关}:\ \text{slice 成立组 }n_{0..3}\ \text{均值 }1.7\ \text{vs 不成立组 }2.7\ (\text{方向对，证据弱})}$$

## §1 度数集中（✓✓ 本轮主要发现）

$$\text{实测 }(25\ \text{样本}):\ n_0+n_1+n_2+n_3\in[0,5];\quad \text{典型}\ n_j:\ \{4{:}8,\ 5{:}6,\ 6{:}4,\ 7{:}5\}\ (|P|{=}24)$$
$$\therefore\ G_3(P)\ \text{几乎无低度顶点};\ \text{多数 }p\ \text{之}\ \deg\in\{4,5,6,7\}✓$$
$$\text{（与度数界 }m_p\le D(9,3,2)=12\ \text{相容};\ \text{实测最大 }9）$$

## §2 ✗ 为什么这条路线到不了（诚实判定）

$$u\le\sum_{j\ge1}f(j)n_j;\qquad f=(6,4,3,3,2,2,2,1,0)$$
$$\text{度数集中 ⟹ 主导项为 }f(4..7)\cdot n_{4..7}\approx(3,2,2,2)\ \Longrightarrow\ \sum f n_j\approx2|P|\approx50✗$$
$$\text{而 }u\le|Q|\approx25\ \text{本身已成立}\Longrightarrow\ \boxed{\text{该上界无新信息}✗}$$
$$\therefore\ \text{想由此得 }u\le U\ \text{常数，须 }\sum_j f(j)n_j<|Q|,\ \text{即需 }|P|\ \text{极小的 }\sum f;\ \text{实测不成立}✗$$

## §3 ⚠️ 弱相关（保留观察）

$$\text{slice 成立（}\mathrm{Def}\le9a-406\text{）组}:\ n_{0..3}\ \text{均值 }1.7;\qquad \text{不成立组}:\ 2.7$$
$$\text{方向与唐先生之"低度 ⟹ 耗容量"直觉一致，但样本弱，}\textbf{不作为依据}⚠️$$

## §4 slice 条件之精确形式（✓ 供后续）

$$|D_A|\le106-a\iff512-|N_1(A)|\le106-a\iff\boxed{\mathrm{Def}(A)\le9a-406}$$
$$\therefore\ \text{最终目标}\ =\ \text{证}\ F(A)=2(A_1+A_2)-T>9a-406\ (\text{实测 }a{=}53:\ F{=}79>71✓)$$

## §5 边界（硬 ✓）

- **实测（度数分布、$u$、$\mathrm{Def}$、slice 判定）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；本文**明确判定该子路线被截断** ✗

## §6 【技术词回查】（**提交前实跑，逐字粘贴**）

```
低度顶点惩罚 : 技术词 低度顶点惩罚 命中文件数=0    ::
度数集中 : 技术词 度数集中     命中文件数=0    ::
slice缺口环节 : 技术词 slice缺口环节  命中文件数=0    ::
```
