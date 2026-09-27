已查地图：已跑 scripts/prework_map_check.sh surfeit 全局塌缩 A 仿射 ζ ⟹ 执行自 `PHASE2-AUDIT-...-surfeit-validity-refuted`（✓）＋ 唐先生 12:18（全局塌缩 ✓）；本档 = **M-2A′ 正式升级为 STOP（global pair-collapse）** ✓。
D0: 本档对象 = $\zeta$ 的全局代数塌缩及其诱导界
D1: 1（新增：**恒等式 $\zeta=M(n^2{+}2n{+}2)-(n{+}2)2^n-4(A_1{+}A_2)$ 验证 ✓**；**诱导界 $U_\zeta$ 与 Delsarte 的比较 ✓**）

# surfeit 全局塌缩（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AI-1 恒等式 ✓✓ 已验证)}\ \zeta=M(n^2+2n+2)-(n+2)2^n-4(A_1+A_2)\ ✓\ \text{——$\zeta$ 对 $A$ \textbf{仿射} ✓}}$$
$$\qquad\text{核对（本机 ✓）}:\ n=5,6\ \text{各 3 个随机码}\ \textbf{6/6 逐位精确吻合} ✓✓\ \text{（如 }n=5:\ \zeta=119\ \text{vs 公式 }119\ ✓\text{）}$$
$$\boxed{\textbf{(AI-2 判定: STOP ✓)}\ \text{quadratic term }x_vx_c\ \text{全局塌缩成 }2(A_1+A_2)\ ✗\ \Longrightarrow\ \textbf{无独立 quadratic 维度} \Longrightarrow\ \textbf{M-2A′ = STOP（global pair-collapse）} ✓✓}$$
$$\qquad\Longleftrightarrow\ \boxed{\text{pair-level in definition}\ \ne\ \text{independent quadratic constraint}}\ ✓\ \text{（唐先生 ✓——本档核心 ✓）}$$
$$\boxed{\textbf{(AI-3 诱导界 ✓ 但 non-leveraging)}\ U_\zeta=\frac{M(n^2+2n+3)-(n+1)2^n}{4}\ \text{是\textbf{有效}上界} ✓\ \text{（由 }\delta\ge0\ \text{两行可得 ✓）}}$$
$$\qquad\text{且在 6 例中 5 例 }\textbf{强于} U_{\rm Delsarte}\ ✗\ \text{（非 }2^m\ \text{情形 ✓）}\ \Longrightarrow\ U_\zeta\ \textbf{不在 Delsarte 的线性包络内} ✓\ \text{（否则矛盾 ✓）}$$
$$\qquad\text{但仍\textbf{远高于}实测（}3\times\sim8\times\ ✓\text{）}\ \Longrightarrow\ \text{归档类别} = \textbf{valid but non-leveraging} ✓\ \text{（不堆 cut ✓）}$$
$$
$$
```

---

## §1 全局塌缩的推导（**✓，逐步可核**）

```
$$x_c=\mathbf1_{\{c\in C\}}\ ✓;\quad \zeta=\sum_v(1-x_v)\Big[2\sum_cx_c\mathbf1_{\{1\le d(v,c)\le2\}}-(n+2)\Big]\ ✓\ \text{（用 AH-1 ✓）}$$
$$\zeta=2\underbrace{\sum_{v,c}(1-x_v)x_c\mathbf1_{\{1\le d(v,c)\le2\}}}_{=:S}-(n+2)(2^n-M)\ ✓$$
$$S=\underbrace{\sum_{v,c}x_c\mathbf1_{\{1\le d\le2\}}}_{=M(n+\binom n2)\ ✓}-\underbrace{\sum_{v,c}x_vx_c\mathbf1_{\{1\le d\le2\}}}_{=2(A_1+A_2)\ ✓}=M\Big(n+\binom n2\Big)-2(A_1+A_2)\ ✓$$
$$\text{（第一项：固定 }c\ \text{的 }d\in\{1,2\}\ \text{点数}=n+\binom n2\ ✓；\text{第二项：距离 }1,2\ \text{的无序对每对计两次 ✓）}$$
$$2\Big(n+\binom n2\Big)-...\ \Longrightarrow\ \zeta=M(n^2+2n+2)-(n+2)2^n-4(A_1+A_2)\ ✓\qquad\square$$
$$\textbf{关键}:\ \text{看似二次的 }x_vx_c\ \text{全部被"距离 }1,2\ \text{的码字对"吸收} \Longrightarrow \text{余下}\textbf{无} x_ax_bx_c / \sum K(u,v)x_ux_v\ \text{型结构} ✓$$
$$
$$
```

---

## §2 诱导界与比较（**✓ 本机表**）

```
$$U_\zeta(n,M)=\frac{M(n^2+2n+3)-(n+1)2^n}{4}\ ✓\ \text{（由 }\zeta\ge-(2^n-M)\ \text{整理 ✓）}$$
$$\begin{array}{c|c|c|c|c|c}
n & M=K(n,1) & U_\zeta & U_{\rm Delsarte}\ (\text{纯 LP ✓}) & \text{实测 }A_{\le2} & \text{判定}\\
\hline
4 & 4 & 7.000 & 6.000 & 2 & \text{Delsarte 更强 ⟹ }U_\zeta\ \text{被包含} ⚠️\\
5 & 7 & 18.500 & 19.250 & 6 & U_\zeta\ \text{更强} ✓\\
6 & 12 & 41.000 & 51.000 & 12 & U_\zeta\ \text{更强} ✓\\
7 & 16 & 8.000 & 87.111 & 0 & U_\zeta\ \text{更强} ✓\\
8 & 32 & 88.000 & 256.000 & 16 & U_\zeta\ \text{更强} ✓\\
9 & 62 & 301.000 & 706.219 & 73 & U_\zeta\ \text{更强} ✓\\
\end{array}$$
$$\textbf{推理（✓ 无需 LP 对偶）}:\ U_\zeta<U_{\rm Delsarte}\ \text{于 5 例 ⟹ 若 }U_\zeta\ \text{属 Delsarte 包络，则 Delsarte 的 }\max\ \text{必}\le U_\zeta\ ✗\ \text{矛盾 ⟹ }\textbf{不属于} ✓$$
$$\qquad\Longrightarrow\ \text{唐先生所预期的"属于 Delsarte 包络 ⟹ 纯 STOP"}\ \textbf{不成立} ✓\ \text{——而是\textbf{新的独立（虽弱）有效界} ✓$$
$$
$$
```

---

## §3 状态更新（**含对前档的更正 ⚠️**）

```
$$\boxed{\textbf{M-2A′ 最终状态}:\ \textbf{STOP = pair-level appearance but global collapse}\ ✓\ \text{（唐先生 12:18 ✓——强于"SDP 没做出来" ✓）}}$$
$$\text{两条 STOP 的\textbf{证明方式不同}（值得记录 ✓）}:\ \text{excess：直接代数恒等式 ⟹ }A\ \text{重参数化} ✓;\ \text{surfeit：先入 pair-level ⟹ 全局 incidence 计数塌缩到 }A\ ✓$$
$$\textbf{前档更正 ⚠️}:\ \text{本会话档 }d7861b7\ \text{曾写"}\zeta\ \text{依赖码字排列（非仅 profile）⟹ 非换皮"} ✗\ \text{——\textbf{现更正} ✓}:\ \zeta\ \text{对 }(n,M,A)\ \text{仿射 ⟹ 携带\textbf{恰为 }A\ \text{的信息} ✓\ \text{（不多不少 ✓）}$$
$$\qquad\Longrightarrow\ \text{正确表述}:\ \zeta\ \text{是 }A\text{-坐标的量} ✓\ \text{（非"排列量" ✗）；因此 }\zeta\text{-界}\ \textbf{恰是}\ A\text{-界} ✓$$
$$\text{已关闭}:\ \zeta\ge0\ \text{（反例 ✗）};\ \text{excess 矩（换皮 ✗）};\ \text{QCQP/SDP 二次化（无新维度 ✗）} ✓$$
$$
$$
```

---

## §4 登记（**小但真 ✓**）

```
$$\boxed{\textbf{A-ZETABOUND-1}:\ \text{对任意 radius-1 覆盖码 }C\subseteq\{0,1\}^n,\ |C|=M:\ A_1+A_2\le\frac{M(n^2+2n+3)-(n+1)2^n}{4}\ ✓}$$
$$\qquad\text{性质}:\ \text{有效 ✓（}\delta\ge0\ \text{两行 ⟹ 无条件 ✓）、显式 ✓、6 例中 5 例强于纯 Delsarte ✓、}\textbf{但完全不锋利} ✗\ \text{（3–8× }\text{高于实测 ✓）}$$
$$\qquad\text{诚实备注}:\ \text{该界实质等价于"}\zeta\ge-(2^n-M)\ \text{"的重写 ✓ ⟹ 可能是已知弱界的等价形式 ⚠️（文献未查 ✓）；登记为\textbf{小资产}，\textbf{不}计为机制 ✓}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§2 为**推导 ＋ 本机验证** ✓（恒等式 6/6 ✓、比较表 ✓）；§3–§4 为**状态更新 ＋ 资产登记** ✓
- **未**声称新机制 ✗；**未**声称该界在文献中为新 ⚠️（未查证 ✓）；**未**改动 119 UNKNOWN ✓
- 遵唐先生："不堆 cut" ✓ —— 本档**不**再向 LP 加入任何约束 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\zeta$ 全局塌缩恒等式、诱导界 $U_\zeta$、$A$-坐标量更正
- **档案已有（引用，不列为提出）**：$\zeta$、$A_{\le2}$、M-2A′、Delsarte LP、van Wee、excess


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 全局塌缩恒等式 命中文件数=1    :: ./PHASE2-AUDIT-2026-09-27-surfeit-global-pair-collapse.md 
技术词 A-坐标量更正 命中文件数=0    ::
```
- **本档新增**：$\zeta$ 全局塌缩恒等式、诱导界 $U_\zeta$、$A$-坐标量更正（见上方命中数；0 命中者为自造语／内部标签 ✓）
