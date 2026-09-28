# AUDIT-2026-09-28b — **★换层门 $P_{-1}$（representation break）＋ 119 表示审计（第一轮）**

> **性质**：**审计**（非研究轮）——遵唐先生令「找到 invariant 前不加 C 编号」⟹ 本档**不占 C 号** ✓
> **空间隔离**：空间 B（119 线）✓；**不作路线裁定** ✗

**已查地图**：承 `AUDIT-2026-09-28`（四类分档）／C-548（$P_0\to P_5$）✓

D0: 本档对象 ＝ **审计/制度**（无新数学对象 ✗）
D1: 0（产出＝换层门 ＋ 表示审计 ＋ ★依赖诊断 ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{我们\ \textbf{不是失败了很多次}；} \text{我们是在\ \textbf{同一层}失败了很多次}}\ ✓✓$$
$$\boxed{\text{缺的不是 }P_1\text{，而是更早的 }\mathbf{P_{-1}:\ \textbf{representation break}}\ ✓}$$

## §1 ★依赖诊断：一个**可证**的硬事实（本档实测 ✓✓）

$$\text{Best 码 }I\ \text{为 }(10,40,4)\ \text{之唯一码（Litsyn–Vardy 1994）} \Longrightarrow I\ \text{由参数完全确定}$$
$$\text{实测}\ \checkmark:\ |I|{=}40;\ I\ \text{内距离}\ \{4{:}440,6{:}240,8{:}100\};\ |\{x:|own(x)|{=}3\}|{=}160$$

$$\boxed{\text{一切建在 }I\ \text{上的 }\Phi\ \text{（owner 超图／三角关联／}H_1,H_2\ \text{／掩码族／对易代数）}\ \textbf{对一切 }C\ \text{皆相同}}$$
$$\Longrightarrow\ \boxed{\text{它们承载\ \textbf{ambient 几何}，不是 }C\ \text{的自由度}}$$
$$\Longrightarrow\ \boxed{\text{它们\ \textbf{无法区分 }K{=}118\ \text{与}\ K{=}119}\ \text{（对任何 }K\ \text{一样）}}\ \Longrightarrow\ \text{不能单独给出 }|C|\ \text{之界}\ ✓✓$$

$$\text{故}:\ \text{只有 }\Phi(I,S)\ \text{中\ \textbf{真正依赖 }S\ (\text{即依赖 }C)\ \text{的部分才有 leverage}}\ ✓$$

**这解释了为何 122 档未产生相变** ⚠️：对象多为 $I$-确定 ⟹ **不含 $C$-信息** ✓

## §2 换层门 $P_{-1}$（**制度 ✓**）

$$\boxed{P_{-1}:\ \text{我们现在使用的数学对象，是否已把 119 的关键差异\ \textbf{压扁}？}}$$
$$\text{若"是"}\ \Longrightarrow\ \text{继续证明无意义}\ ✗$$

**要求的分层（按"是否改变表示层"分类，非按成败 ✓）**：

| 层 | 语言 | 我们在哪 |
|---|---|---|
| **Layer 0** | 原始 covering（$C{\subset}Q_{10}$，$\rho{=}1$） | 深 ✓ |
| **Layer 1** | 几何分解（distance／owners／$A_r$／$F,G$） | 深 ✓ |
| **Layer 2** | 局部结构（profiles／禁配／parity／capacity） | 深 ✓ |
| **Layer 3** | **尚未找到** | ⚠️ **目标** |

$$\boxed{\text{Layer 3 之硬条件}:\ \Phi(C)\ \text{之定义\ \textbf{不能只是 Layer 0–2 之重新打包}}\ ✓}$$

## §3 核心区别（**旧 vs 应做**）

$$\text{旧}:\quad C\overset{\text{lemma}}{\longrightarrow}C\overset{\text{lemma}}{\longrightarrow}C\qquad(\text{同一表示层内}\ ✗)$$
$$\text{应做}:\quad \boxed{C\to\Phi(C)\to\Psi(\Phi(C))\to\text{obstruction}}\qquad(\text{中间必有\ \textbf{非 covering-码语言} 之核心对象}\ ✓)$$

## §4 119 表示审计（第一轮）— 六项检验

$$\text{候选 }\Phi\ \text{须过}:\ (1)\ \text{严格新对象？}(2)\ 119\ \text{对应什么？}(3)\ 118\ \text{对应什么？}(4)\ \text{有无现成、非 covering-bound 同族之 obstruction？}(5)\ \text{能否由已知结构导出？}(6)\ \textbf{是否真改变自由度，而非重编码？}$$

| 候选 $\Phi$ | 依赖 $C$？ | 语言 | 过 (6)？ | 判定 |
|---|---|---|---|---|
| owner 超图 $H_{\rm Best}$（C-480） | **否**（只依赖 $I$） | 超图 | ✗ | **关闭** ✗ |
| 三角关联（160↔160，$v{=}160,k{=}r{=}128$）（C-487/488） | **否** | 关联 | ✗ | **关闭** ✗ |
| 对易代数 $A_0..A_3$／$H_0{\sqcup}H_1{\sqcup}H_2$（C-489/491） | **否** | 谱/代数 | ✗ | **关闭** ✗ |
| 4-槽掩码族 $M(O)$（C-504/505） | **否** | 集族 | ✗ | **关闭** ✗ |
| 距离分布／Krawtchouk（Delsarte） | 是 ✓ | 谱 | ✗（Layer 0） | **已死** ✗（C-546） |
| 加权覆盖／surfeit 泛函 | 是 ✓ | 泛函 | ✗（Layer 0） | **已死** ✗（Haas 族） |
| **次正规划分** $C{=}C_0{\sqcup}C_1$（Honkala 1991） | 是 ✓ | **着色/划分** | **?（待检）** | ⚠️ **活口候选** |
| **私有覆盖** $\rho(c)$（`AUDIT-a` §4） | 是 ✓ | incidence | **?（待检）** | ⚠️ **活口候选** |

$$\boxed{\text{结论}:\ \text{本线 122 档中，凡"新对象"几乎皆}\ I\text{-确定} \Longrightarrow \textbf{系统性 fail }(6)}$$

## §5 两个活口候选之初判

$$\textbf{(α) 次正规划分}:\ \text{Honkala 1991 证\ \textbf{一切} binary radius-1 covering code 皆次正规（}d(x,C_0){+}d(x,C_1){\le}3\text{）}$$
$$\qquad\Longrightarrow\ \text{是\ \textbf{必要}条件（120-码亦满足）} \Longrightarrow \text{单独不分离；须与别的量耦合}\ ⚠️$$
$$\textbf{(β) 私有覆盖}\ \rho(c)\ (\textbf{不可重复计数}\ ✓):\quad \text{私有性逐点互斥} \Longrightarrow \textbf{非 covering 线性重写}\ ✓$$
$$\qquad\Longrightarrow\ \text{须证}\ |C|{\le}118\Rightarrow R{>}118r\Rightarrow\lceil R/r\rceil{=}119\ ⚠️\ (\text{C-515 之 overlap 教训须显式处理})$$

## §6 结论与下一步

$$\boxed{\text{不再在同一层造 lemma}}\ ✗;\quad \boxed{\text{只为 }(\alpha)/(\beta)\ \text{两类做\ \textbf{六项检验}}\ ✓}$$
$$\text{（其余候选已按 §4 关闭，不再投入 ✗）}$$

## §7 边界（硬 ✓）

- 依赖诊断（实测）＋ 既有档引证 ✓；**无新数学** ✗；**不加 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §1 之"$I$-确定 ⟹ 无 $C$-信息"为**本档实测 ＋ 唯一性引用**；**不主张**该推理已排除一切 $I$-型桥（V290 ✓）
