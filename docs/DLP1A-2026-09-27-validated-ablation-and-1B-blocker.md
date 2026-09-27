已查地图：已跑 scripts/prework_map_check.sh Delsarte LP 消融 Van Wee 复现 ⟹ 执行自 `DLP1-2026-09-27`（公式已抽 ✓）＋ 唐先生 10:16 ✓；本档 = **1A 复现成功 ✓ ＋ 1B 可行性否决 ✗**。
D0: 本档对象 = covering-code LP 消融的独立复现与 SDP 消融可行性
D1: 1（新增：**LP harness 已校准（三锚点 7 位小数命中 ✓）**；**1B 无求解器 ⟹ 不可行** ✓）

# DLP1A-2026-09-27 · 消融复现成功与 1B 阻断

## §0 结论（先给）

```
$$\boxed{\textbf{(JJ-1 复现成功)}\ \text{本档 LP harness \textbf{精确复现}唐先生三锚点（7 位小数 ✓✓）}}$$
$$\qquad 94.0197982\ (\text{对 }94.0197982166)\ ✓;\quad 101.0073568\ (\text{对 }101.0073567955)\ ✓;\quad 101.4081694\ (\text{对 }101.4081693983)\ ✓$$
$$\qquad\Longrightarrow\ \textbf{D-LP-1A（经典 LP 消融）得到独立确认}\ ✓\ \text{（不再依赖单方计算 ✓）}$$
$$\boxed{\textbf{(JJ-2 1B 阻断)}\ \text{容器内\textbf{无任何 SDP 求解器}}\ ✗\ (\texttt{cvxpy/scs/cvxopt/picos/mosek}\ \text{全部缺失 ✓})}$$
$$\qquad\Longrightarrow\ \text{101.4082}\to105.2223\ \text{的\textbf{逐组件消融（matrix cuts／Lasserre／Terwilliger／objective）本机不可执行}\ ✗}$$
$$
$$
```

---

## §1 (JJ-1) 校准细节与语义钉死

```
$$\text{校准的 key}: \text{Van Wee 读法} = \boxed{(6,1,1,0,\dots,0)_6}\ ✓\ \text{（唐先生给出 ✓）；上档失败纯因我误用 }\lambda=e_t+e_1+e_2\ ✗$$
$$\textbf{语义探针（本档实测 ✓）}:\ \lambda=(6,1,1)_6\to\mathbf{101.0073568}\ ✓;\quad \lambda=(1,6,5)_6\to21.62\ ✗;\quad \lambda=(1,6,1)_6\to58.62\ ✗$$
$$\qquad\Longrightarrow\ \text{仅 }(6,1,1)\ \text{可复现 ⟹ 约定被\textbf{操作性地钉死}}\ ✓\ \text{（我的"球和取整"推导含索引约定错误 ⚠️，已弃用 ✓）}$$
$$
$$
```

---

## §2 消融表（1A 确认版 ✓）

```
$$\begin{array}{c|c|c|c}
\text{层} & \text{新增信息} & \text{下界（本档复现 ✓）} & \text{增量}\\
\hline
\text{Sphere} & \text{球覆盖计数} & 93.090909 & —\\
\text{Delsarte-LP} & +\text{Krawtchouk 正性} & \mathbf{94.0197982} & +0.928889\\
\text{Van Wee-only} & +\text{Van Wee }(6,1,1)_6 & \mathbf{101.0073568} & +7.916448\ (\text{vs sphere})\\
\text{Delsarte＋Van Wee} & \text{两者同时} & \mathbf{101.4081694} & +7.388371\ (\text{vs Delsarte})\\
\text{2025 SDP} & +\text{Lasserre／matrix cuts／Terwilliger} & 105.2223 & +3.814131\\
\end{array}$$
$$\textbf{诊断（已独立确认 ✓）}:\ \text{Delsarte 层极弱 }(+0.93)；\ \text{Van Wee 层\textbf{真正大跳}}(+7.39)；\ \text{高阶 SDP 中等}(+3.81)$$
$$\qquad\text{缺口}:\ 120-105.2223=14.7777\ ✓;\ \textbf{而文献最好已知下界 }107\ (\text{BÖW 2004})\ \mathbf{>}\ 105.2223\ ✗$$
$$\qquad\Longrightarrow\ \text{该 cell 的"成熟工具链天花板"其实＝}\mathbf{107}\ \text{（非 SDP 的 }105.22)\ ✓;\ \text{则缺口 }120-107=\mathbf{13}\ ✓$$
$$
$$
```

---

## §3 自检门的第二次拦截（纪律 ✓）

```
$$\text{我尝试用"球壳移位＋取整"生成扩展族（11 条）}\ ⟹\ \text{LP}=170.6667\ \mathbf{>}\ \text{SDP }105.2223\ ✗✗$$
$$\qquad\Longrightarrow\ \text{生成规则\textbf{无效}}\ ✗\ \text{（与上档 110.03 同型）⟹ 弃用 ✓；\textbf{自检门连续两次拦截污染} ✓✓$$
$$
$$
```

---

## §4 (JJ-2) 1B 的三条出路（待唐先生定 ✓）

```
$$\text{① 装求解器}:\ \texttt{pip install cvxpy scs}\ ✓\ \text{（可行 ⚠️ 但：全维 }1024\ \text{的 Lasserre SDP 仍不可行 ✗；须走\textbf{对称约化}路径 ✓ 而其实现在论文 }\S4/\text{Thm 4.9}\ \text{里 ⟹ 需先读透 ✓）}$$
$$\text{② 索取作者代码／数据}:\ \text{论文计算必有实现 ✓\ \Longrightarrow\ 最省力且最可靠}\ ✓✓$$
$$\text{③ 只做 LP 侧实验}:\ \text{需先建立\textbf{正确的}有效不等式生成机（球和取整）⚠️\ —— 本档的两次失败说明\textbf{尚未掌握}该机 ✓}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 复现为**本档计算** ✓（与唐先生数值独立吻合 ✓ ⟹ 双方一致 ✓）
- §2 的 SDP 值 105.2223 为**论文自身数值** ✓（表 5，无粗体无星号 ⟹ 非该文改进 ✓）；107 为**档案既有文献值** ✓
- §3 的 170.67 为**无效值** ✗（明确弃用 ✓）；**未**据此做任何推断 ✗
- **未**排除 119 ✗、**未**给出新下界主张 ✗；本档 = 复现 ＋ 可行性判定 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：LP harness 校准、1B 阻断判定
- **档案已有（引用，不列为提出）**：Van Wee (6,1,1)_6、Krawtchouk、Lasserre、matrix cuts、Terwilliger、BÖW 107
