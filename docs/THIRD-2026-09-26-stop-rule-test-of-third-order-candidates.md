已查地图：已跑 scripts/prework_map_check.sh K(10,1) 三阶 三角 Fourier 独立量 ⟹ 执行自 `FACE-CLOSURE-2026-09-26`（停止条件 ✓）＋ `GAPTHEOREM-2026-09-26`（缺口＝支撑型 ✓）；本档为**三轮候选的 STOP RULE 测试**（唐先生 2026-09-26 21:43 指令 ✓）；含一次构造性计算 ✓。
D0: 本档对象 = 三类候选量（谱型／三阶／外部）与 STOP RULE 判据（既有对象）
D1: 0（产出为判据表、独立性构造证明与判定）

# THIRD-2026-09-26 · 三阶/外部候选的 STOP RULE 测试

## §0 判据表（本档主产出 ✓）

```
$$\textbf{规则（唐先生 2026-09-26 21:43 立）}:\ \text{候选 }X:\ \text{若 }X=f(A_1,A_2)\ \text{则立即 STOP ✗};\ \text{仅当 }X\notin\langle A_1,A_2\rangle\ \text{且产生独立不等式/等式才进 P1/P2}\ ✓$$
$$
$$

$$\begin{array}{l|l|l|l}
X & \in\langle A_1,A_2\rangle? & \text{标准假设下受约束?} & \text{判定}\\
\hline
\sum_x\binom{b(x)}3 & \text{否（由 profile 定）} & \textbf{被强制}=1 & \textbf{STOP} ✗\ \text{已钉死}\\
q_F\le2\ (\text{分支 A}) & \text{结构式} & \textbf{被强制} & \textbf{STOP} ✗\ \text{已钉死}\\
\text{无 }d{=}1\ \text{樱桃} & \text{结构式} & \textbf{被强制}（d_1\le1） & \textbf{STOP} ✗\ \text{已钉死}\\
\text{谱壳能量 }G_k & \text{否} & \textbf{被两矩式钉死} & \textbf{STOP} ✗\ \text{已钉死}\\
d{=}2\ \text{樱桃数 }p & \textbf{否} ✓ & \text{自由}（区间极宽） & \text{过规则，\textbf{但无约束}} ✗\\
(2,2,2)\ \text{三角数 }\tau_2 & \textbf{否} ✓ & \text{自由}（z-星 }\Rightarrow\ \ge1） & \text{过规则，\textbf{但无约束}} ✗\\
\text{私有数 }p(c)\ \text{分布} & \textbf{否} ✓ & \text{自由}（\sum p(c)=740\ \text{固定}） & \text{过规则，\textbf{但无约束}} ✗\\
\text{Booleanity}\ f^2=f & \textbf{否} ✓ & \textbf{确有约束} & \approx\ \textbf{原问题} ⚠️
\end{array}$$
$$
$$
```

---

## §1 独立性构造证明（本档计算 ✓）

```
$$\textbf{命题}:\ d{=}2\ \text{图（}n=119\ \text{顶点、}2A_2=188\ \text{条边）的樱桃数 }p\ \textbf{不由 }(A_1,A_2)\ \text{决定}\ ✓✓$$
$$\textbf{构造（两图同边数}188\text{）}:\quad \text{(i) 189 顶点长路径}\Longrightarrow p=187\ ✓;\quad \text{(ii) 星 }K_{1,188}\Longrightarrow p=\binom{188}{2}=17578\ ✓$$
$$\qquad\Longrightarrow\ 187\ne17578\ \text{而边数相同}\ \Longrightarrow\ p\notin\langle A_1,A_2\rangle\ \textbf{（过 STOP RULE）}\ ✓✓$$
$$\textbf{（注：初版脚本含自环 (0,0) 使数值偏 188}\ ✗\ \text{，上表为更正后数值 ✓）}$$
$$
$$
```

---

## §2 自由性（必要界极宽 ⟹ 无约束 ✗）

```
$$\textbf{下界（Kim--Vu）}:\ p\ \ge\ \frac{(2A_2)^2}{2n}-\frac n2\ =\ \frac{188^2}{238}-59.5\ \approx\ \mathbf{89}\ ✓$$
$$\textbf{上界（}\sum_cd_2(c)=2A_2=188,\ d_2\le45\text{）}:\ p\ \le\ 4\binom{45}2+\binom82=\mathbf{3988}\ ✓$$
$$\Longrightarrow\ p\in[89,3988]\ \text{——区间宽度 }44\times \Longrightarrow\ \textbf{标准假设（}Q{=}1\ \text{profile ＋ 匹配 ＋ Delsarte）不给约束}\ ✗$$
$$\text{同理}\ \tau_2\ge1\ (\text{z-星}\ ✓)\ \text{而上界同量级}\ ✗;\quad p(c)\ \text{仅 }\sum p(c)=740\ ✓\ ✗$$
$$
$$
```

---

## §3 判定（诚实 ✓）

```
$$\textbf{结论}:\ \text{三类候选呈\textbf{二分}:\ 被钉死（}\Longrightarrow\text{STOP ✗）或 自由（}\Longrightarrow\text{无不等式 ✗）。}$$
$$\qquad\textbf{唯一"既有约束又独立"的对象＝Booleanity（}f^2=f\text{）} —— 但它\ \textbf{等价于原覆盖问题}\ ⚠️\ \text{（见 }\texttt{FOURIER}\ \S4\ ✓）$$
$$\Longrightarrow\ \textbf{本类候选未发现 P1}\ ✗\ \text{（第 13 次同向汇合 ⚠️）};\ \text{但注意：本档\textbf{不}主张"独立量不存在"}\ ✗\ \text{（只报告所试候选之判定 ✓）}$$
$$\textbf{未试的真正一类}:\ \text{三阶 (Terwilliger／3-point) 不等式} —— \text{它能\textbf{约束}三阶量（如 }p,\tau_2\text{）}，\ \text{但需\textbf{实现}一套三点 Delsarte 系统}\ ⚠️\ \text{（研究级工作量）}$$
$$
$$
```

---

## §4 建议（二选一 ✓）

```
$$\textbf{路 A（研究级 ⚠️）}:\ \text{实现\textbf{三点/Terwilliger 不等式}，只针对 }A_1\ \text{窗（目标：与 }A_1\le49\ \text{形成 P3）}\ ✓;\ \text{风险：文献同类工具（2504.01932）在 }(2,10,1)\ \text{只给 105 ✗}\ ⚠️$$
$$\textbf{路 B（工程级 ✓）}:\ \text{转 }\texttt{FRONTIER-R1}\ \text{（RoSQS 5 格 ＋ 校准门 G-CAL）} —— \text{对象不同类、每格有限可证书、可复用 A23-D4 模板}\ ✓✓$$
$$\qquad\textbf{本档倾向}:\ \text{若唐先生愿承担研究级风险 → 路 A};\ \text{若要先取可验证产出 → 路 B}\ ⚠️$$
$$
$$
```

---

## §5 边界（诚实标注）

- §0 判据表为**逐项推导＋已有细档比对** ✓（"被强制"各项皆已在前档证明 ✓）
- §1 为**构造性证明** ✓（数值已更正 ✓）；§2 为**必要界**（非充分界 ✓）
- **未**主张独立量不存在 ✗；**未**排除 $Q=1$ ✗、**未**排除 119 ✗
- **未跑** solver ✓（仅 §1 的图计数 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 STOP RULE 判据表 命中文件数=1    :: ./THIRD-2026-09-26-stop-rule-test-of-third-order-candidates.md 
技术词 p not in span 构造证明 命中文件数=0    ::
```
- **本档新增**：STOP RULE 判据表、$p\notin\langle A_1,A_2\rangle$ 构造证明（见上方命中数）
- ⚠️ 若某词命中 0 ⟹ 该词为自造描述语，**不列为新命名** ✓
- **档案已有（引用，不列为提出）**：Kim–Vu 下界、$q_F\le2$、匹配定理、Booleanity 等价、$A_1\le49$
