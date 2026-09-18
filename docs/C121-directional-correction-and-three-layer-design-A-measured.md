已查地图（**先查后写**）：`IMPL-1/2/3`、`CEILING-AUDIT-3`、`lean-frontier-audit/lp/ceiling_lp_recompute.py`（本档实测其变体）、`V185/V186/V316`（同址记录）、`EXT-SCAN-3/4`（二分结构与 oracle 形式）。关键词回查：`单调性基线`＝0、`联合几何约束`＝0、`认证污染`＝0 ⟹ 均本档新增 ✓。

# C-121 · **方向性纠正 ＋ 三层设计（A 已实测）**

> **时间**：2026-09-18 23:16 唐先生：**「开 (ii)，但这里有一个必须先纠正的方向性问题」** ✓

**C-121 第一行硬检查（唐先生指定；本档最高优先级）**：

$$\boxed{\ \text{若}\ p_*=\inf_{r\in\mathcal F}L(r)\ \text{且}\ \mathcal F'\subseteq\mathcal F,\ \text{则}\ \inf_{r\in\mathcal F'}L(r)\ \ge\ \inf_{r\in\mathcal F}L(r)=p_*\ }✓✓$$
$$\boxed{\ \text{故：}\textbf{单纯收紧可行域绝不可能把}\ p\ \text{压低};\ \text{它只能}\ \textbf{pin／certify}\ \text{一个已知目标}\ }✓✓$$
$$\boxed{\ \text{要得到}\ p_{\text{marks}}<p_0,\ \text{必须}\ \textbf{改变 primal 问题本身}（\text{marks 几何}）;\ \textbf{不是加约束}\ }✓✓$$

FREEZE-ACK: 本档即冻结期内的方向纠正与基线实测（依 `§8.1`；不产候选结论）

D0: 本档对象 = **方向性纠正（收紧⇏降 p）＋ C-121 三层设计 ＋ A 层实测基线** —— 关系 = 方向纠正与基线实测，非新机制
D1: 0

---

## §0 结论（先行）

$$\textbf{(一)}\ ⭐\ \text{方向纠正}\ \textbf{接受并前置为第一行硬检查}（\text{见上框}）✓✓$$
$$\textbf{(二)}\ ⭐\ \text{A 层}\ \textbf{已实测}：\text{族收紧有}\ \textbf{单调效应};\ \text{盒收紧在数据精度下}\ \textbf{完全惰性}✓✓$$
$$\textbf{(三)}\ ⭐\ \text{实测给出}\ \textbf{逼近曲线}：\text{认证下界}\ \text{随族收紧}\ \textbf{自下逼近}\ p_0，\ \text{未越过}✓✓$$

---

## §1 C-121-A **单调性基线（已执行）**

$$\textbf{测法}：\text{用前沿自有 LP（}\texttt{lp/ceiling\_lp\_recompute.py}\text{），}\text{分两方向收紧，}\text{比较}\ \delta_{\text{box}}✓$$
$$\qquad \text{（}\delta_{\text{box}}\ \text{为}\ \textbf{对偶侧最大值}\ \max_r[\int rx\,dx-B_{\text{box}}(r)];\quad p_{\min}=\text{target}-\delta_{\text{box}}）✓$$

**方向 1：证书族收紧（正则上界 $B$）—— 有单调效应 ✓**

| 族（正则上界 $B$） | $\delta_{\text{box}}$（实测） | $p_{\min}=\text{target}-\delta$ | 与 $p_0=0.681828687$ 之差 |
|:--|:--|:--|:--|
| $B=8.2$（较大族） | $2.085367838\times10^{-5}$ | $0.6818078$ | $-2.085\times10^{-5}$ |
| $B=1.0$（较小族） | $2.543131510\times10^{-6}$ | $0.6818261$ | $-2.543\times10^{-6}$ |
| $\Rightarrow\ \mathcal F_{B=1}\subset\mathcal F_{B=8.2}$ | **减小 ✓** | **升高 ✓** | **缺口缩小 8.2× ✓** |

$$\Longrightarrow ⭐\ \textbf{单调性实测成立}：\text{限制族}\ \mathcal F'\subset\mathcal F \Longrightarrow \max_{\mathcal F'}\le\max_{\mathcal F} \Longrightarrow p_{\min}\ \textbf{升高}（\text{自下逼近}\ p_0）✓✓$$

**方向 2：盒收紧（包络端点）—— 在数据精度下完全惰性 ✓✓**

$$\text{变体 A2}（h_j\ \text{改用}\ lo\ \text{端点}）：\delta_{\text{box}}=2.08537\times10^{-5}（B=8.2）／2.54313\times10^{-6}（B=1.0）\quad \textbf{与原值逐位相同}✓✓$$
$$\text{变体 A3}（h_j\ \text{改用中点}）：\delta_{\text{box}}\ \textbf{同上，逐位相同}✓✓$$
$$\text{原因}：\text{包络自身已紧到}\ \tau\approx1.8367\times10^{-40} \Longrightarrow lo\ \text{与}\ hi\ \text{之差}\sim10^{-40} \Longrightarrow \textbf{无可测效应}✓✓$$
$$\Longrightarrow ⭐\ \text{即：}\textbf{盒已经是一个点};\ \delta_{\text{box}}\ \text{的来源}\ \textbf{不是盒的松弛}✓✓$$

**方向 3：族规模 $M$（分段线性基数）—— 惰性 ✓**

$$M=20／50／100：\delta_{\text{box}}\ \textbf{三者相同}（\text{到}\ 1\times10^{-11}\ \text{内}） \Longrightarrow \textbf{族在}\ M\ \text{方向已饱和}✓✓$$

$$\Longrightarrow ⭐⭐\ \textbf{基线净结论}：\text{当前}\ \delta_{\text{box}}\ \text{既}\ \textbf{不是族尺寸} \text{造成、}\ \textbf{也不是盒松弛} \text{造成} \Longrightarrow \text{唯一剩下的来源＝}\textbf{网格离散化／最坏情形项}✓✓$$
$$\qquad \text{（此即"为何收紧数据无济于事"的}\ \textbf{实测版}）✓✓$$

---

## §2 C-121-B · **marks 几何清单（下一步核心；未执行）**

$$\text{已知：}S(256)=211.432\neq256 \Longrightarrow \text{整数位置假设}\ \textbf{不可用} \Longrightarrow \text{Parseval 刚性}\ \textbf{不可恢复}✓$$
$$\text{要问：}\boxed{\ \text{marks 满足什么}\ \textbf{原始几何关系}，\ \text{而 256 行包络}\ \textbf{未表达}？\ }✓$$
$$\textbf{三类}：G_1＝\text{位置约束};\quad G_2＝\text{相对位置／间距约束};\quad ⭐\ G_3＝\textbf{不同 marks 之间的联合约束}✓✓$$
$$\qquad ⭐\ \text{关键判据（唐先生）}：\text{若每行只是}\ \textbf{单点约束} \Longrightarrow \text{本质仍是 envelope};\quad \text{只有}\ \textbf{联合结构} \text{才可能加信息}✓✓$$
$$\qquad \text{与我方多体线经验一致}：\textbf{新增阶数本身无价值，只有新的联合结构有价值}✓✓$$
$$\Longrightarrow ⭐\ \text{本档的候选（来自 }\text{`IMPL-3`}\text{，}\textbf{属 G}_3\text{ 型}）：\textbf{Toeplitz 正定}（S=|\hat\mu|^2/N \Longrightarrow (S(|i-j|))\succeq0）✓✓$$
$$\qquad \text{它是}\ \textbf{跨行联合约束}（\text{不同}\ j\ \text{之间耦合}），\ \text{不属 envelope 的线性组合} \Longrightarrow \text{过 K2}✓$$

## §3 C-121-C · **pin test（未执行）**

$$\text{对每种新几何信息，}\textbf{同时算两个 LP}：p_{\text{old}},\ p_{\text{new}};\quad \Delta p=p_{\text{new}}-p_{\text{old}}✓$$
$$\text{若只}\ \Delta p>0\ \text{而}\ \textbf{未锁定真}\ p_* \Longrightarrow \text{只是更强的界，}\ \textbf{不是突破}✓$$
$$\text{真正有价值（}\textbf{pin}\text{）}：\ p_{\text{new}}=p_0\ \wedge\ \mathcal F_{\text{true}}\subseteq\mathcal F_{\text{new}}\ \wedge\ \exists\ \text{真实 admissible 构型取到该界}✓✓$$

## §4 **四条预注册判死条件（唐先生指定，逐字）**

$$K_1：\text{新增约束只是}\ \mathcal F'\subset\mathcal F \Longrightarrow \textbf{不能降低}\ p✓$$
$$K_2：\text{新增信息只是已有 envelope 的线性组合} \Longrightarrow \textbf{repackaging}✓$$
$$K_3：\text{新增 marks geometry 是}\ \textbf{人为挑选以命中}\ p_0 \Longrightarrow \textbf{certificate contamination}✓✓$$
$$K_4：\text{geometry 若来自原问题的}\ \textbf{独立必要条件} \Longrightarrow \textbf{进入真正的 primal test}✓$$
$$\qquad ⚠️\ K_3\ \text{尤其重要}：\text{已知识}\ p_0=1-a_N\ \text{与 primal optimum 对得很漂亮} \Longrightarrow \textbf{必须禁止反向设计}✓✓$$

## §5 对 `IMPL-3` 的**措辞更正**（依本档第一行）

$$\text{`IMPL-3` §4 判据原文：}\text{"若加 T1--T4 后}\ p_{\min}\ \text{显著上移} \Longrightarrow \text{原天花板被收紧"}\quad ⚠️\ \textbf{措辞须精确化}✓$$
$$\qquad \text{正确区分}：\quad \textbf{(a)}\ p_{\min}\ \text{上移} \Longrightarrow \textbf{pin／certify}（\text{有用的，但不是突破}）;$$
$$\qquad \qquad \qquad \textbf{(b)}\ p<p_0 \Longrightarrow \textbf{只能来自新 primal}（\text{marks 几何}），\ \textbf{不可能} \text{由加约束得到}✓✓$$

## §6 边界与回查

- ⚠️ §1 为**本档实测**（变体 A2／A3 在 `/tmp`，未入库；LP 为前沿自有代码，**未改其数学**）✓
- ⚠️ §2／§3 为**设计**（未执行）；§4 K1--K4 为**唐先生逐字**✓
- ⚠️ **不声称**能 pin；**不声称**能得 $p<p_0$；**不声称**与 RH 相关（该 LP 只关于 bandwidth-one 证书类）✓
- **未用** RH；**未改**前沿档案；**未覆盖**其 JSON（变体输出改写至 `/tmp`）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓
- ⚠️ 下次执行顺序（唐先生指定）：**A（完成）→ B（清单）→ C（pin test）**；**不直接扩大 LP** ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:1x）`[纪律]`（先跑后写）

```
技术词 单调性基线       命中文件数=0  ⟹ 本档新增
技术词 联合几何约束      命中文件数=0  ⟹ 本档新增
技术词 认证污染        命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
