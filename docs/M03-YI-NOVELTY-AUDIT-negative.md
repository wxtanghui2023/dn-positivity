已查地图：命中（`M03-W0-REAL-LOCAL-CONSTRUCTION-success`）⟹ 新性审计（`乙`），不开新案
D0: 本档对象 = ⭐**新性审计（负面结论）**：四项窄谱核验 ＋ **族 `(1,\lambda_2,\lambda_2,\lambda_5,\lambda_5)` 已被文献明确研究** ＋ **已知充分区覆盖我方点** ＋ **`R\setminus W\ne`"未知区"的关键校准** ＋ 后续建议
D1: 0（审计型，无新自由度）
[REVIEW]

# **`(乙)` 新性审计：结论为负面**

## §1 先生指定的四项核验

```
$$\textbf{① 2026 论文的 }R,W\ \text{定义与 }R\setminus W\ \text{是否留下未覆盖区}:\ \checkmark\ (\text{已知},\ \text{我方点确在 }R\setminus W)$$
$$\textbf{② 该侧是否已有非负实对称实现}:\ \boxed{\text{大概率已有}}\ \Longrightarrow\ \textbf{新性不成立}\ \times$$
$$\textbf{③ 更老文献是否有等价参数化的构造}:\ \boxed{\text{有}}\ (\text{见 §2})$$
$$\textbf{④ 是否已有矩阵族覆盖我方局部族}:\ \boxed{\text{有}}\ (\text{见 §2})$$
```

## §2 ⭐ 关键文献发现（三处）

```
$$\textbf{(A) 2026-05 WSU 学位论文（NIEP 主题）}:\ \text{明确研究}\ \boxed{\sigma=(1,\lambda_2,\lambda_2,\lambda_5,\lambda_5)}\ \text{族（即我方族）}，给出$$
$$\quad \textbf{Conjecture 5.1.2}:\ \sigma\ \text{可实现}\iff s_1(\sigma)\ge0\ \wedge\ \big(1+4\lambda_2\lambda_5\ge0\ \vee\ 1+\lambda_2+2\lambda_5\ge0\big)$$
$$\quad \text{并明言}:\ \text{“该区域}\textbf{已知充分}\text{”}（"we already know that it is sufficient"）;\quad \text{且给出边界参数化矩阵的可取法}$$ ✓✓
$$\qquad \textbf{我方点代入}:\ \lambda_2=\tfrac14,\ \lambda_5=-\tfrac58-10^{-4}\Longrightarrow 1+4\lambda_2\lambda_5=1-\tfrac58-10^{-4}=0.3749>0\ \wedge\ s_1=0.2498\ge0$$
$$\qquad \Longrightarrow\ \boxed{\text{我方点落在“已知充分区”内}}\ \Longrightarrow\ \textbf{构造是已知结果的重验证，非新结果}$$ ✗✗
$$\textbf{(B) 2023 SINGACOM《A note for the SNIEP in size 5》}:\ \text{含}\ \boxed{a\le\tfrac{\sqrt5-1}4\ \text{时谱恒可对称实现（常对角）}}$$
$$\qquad \text{（}\tfrac{\sqrt5-1}4\approx0.309>t=\tfrac14\ \text{——与我方 }t\ \text{同量级，提示该族已被处理；需原文确认参数含义）}$$ ⚠️
$$\textbf{(C) 高迹区定理（2023 转述 [3,Thm4]}）:\ \Sigma\lambda_i\ge\lambda_1/2\ \text{时充要条件为 }\lambda_2+\lambda_5\le\Sigma\lambda_i,\ \lambda_3\le\Sigma\lambda_i\ (\text{非我方低迹区})$$ ✓
```

## §3 ⭐ 关键校准：`R\setminus W\ne`"未知区"

```
$$\boxed{\text{2026 论文的 }R\setminus W\ \text{只是"2026 方法未覆盖"，}\textbf{不等于"未知/未实现"}}$$ ✓✓✓
$$\quad \text{该区域可被\textbf{其它已知充分条件}（如 (A) 中的 }1+4\lambda_2\lambda_5\ge0\text{）大面积覆盖};\ \text{我方点即是例证}$$ ✓✓
$$\textbf{真正开放的部分（按 (A) 的 iff 猜想）}:\ s_1\ge0\ \wedge\ 1+4\lambda_2\lambda_5<0\ \wedge\ 1+\lambda_2+2\lambda_5<0$$
$$\qquad \text{以 }(t,s)\ \text{表述}:\ \boxed{4ts>1\ \wedge\ 2s>1+t\ \wedge\ s\le\tfrac{1+2t}2}\ (\text{窗口非空}\iff t>\tfrac{\sqrt5-1}4\approx0.309)$$ ✓✓
$$\qquad \text{（}\textbf{与 2023 注记的常数 }\tfrac{\sqrt5-1}4\ \text{一致，}\text{强烈提示该族已被系统研究}）$$ ✓✓
$$\Longrightarrow\ \textbf{元教训（AMEND-9 型）}:\ \text{我们先前把 }R\setminus W\ \text{当作"逃逸区/可攻区"，但未重跑}\textbf{问题形态变化后}\ \text{的文献核查}$$ ⚠️
```

## §4 建议（不据负面结论擅自转向）

```
$$\textbf{不做}:\ \text{不据本构造走 Krawczyk 的"新性路线"（节省算力，避免把已知结果包装成新结果）}$$ ✓
$$\textbf{可选路线}:\ \text{(i) 降格为**独立复核**（对 (A) 的已知充分区做交叉验证，本身有校准价值）};$$
$$\qquad \text{(ii) 转向**真正开放区** }\{4ts>1,\ 2s>1+t,\ s\le\tfrac{1+2t}2\}\ \text{——但那是\textbf{不可能性}方向（更难，且 2026 的 }W\ \text{只覆盖其一部分）};$$
$$\qquad \text{(iii) 收口 Stage Report。}$$
$$\textbf{前置条件}:\ \text{任何进一步动作前，应取得 (A)(B) 原文（学位论文 + 2023 注记）做逐条比对，而非依赖搜索摘要}$$ ✓✓
【⛔ 纪律】 本轮为**文献审计**（零计算）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §2 的结论基于**搜索摘要**（未逐字核验原文），故措辞为"大概率/提示"；**不得**据此写成"确定已知"或"确定未知" ✓

## §附 【技术词回查】（补录）
```
技术词 novelty audit    命中文件数=2    :: ./ASSETS-REGISTRY.md ./C-alpha-ledger-lock-and-novelty-audit.md 
技术词 known sufficient 命中文件数=0    :: 
```
