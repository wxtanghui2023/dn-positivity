已查地图：已跑 scripts/prework_map_check.sh Delsarte LP covering Krawtchouk Van Wee ⟹ 执行自 `FRONTIER-R4-2026-09-27` ✓＋ 唐先生 10:13（D-LP-0/1 ✓）；本档 = **公式已抽 ✓ ＋ 重建未过内检 ✗（数值不予采信 ✓）**。
D0: 本档对象 = Gijswijt–Polak 的 covering-code Delsarte 类 LP 与其重建
D1: 0（产出：论文精确公式（资产 ✓）＋ 重建失败记录 ＋ 新自检门）

# DLP1-2026-09-27 · 公式抽取成功，但重建无效

## §0 结论（先给）

```
$$\boxed{\textbf{(II-1 成功)}\ \text{论文 §1 的 covering-code Delsarte 类 LP \textbf{精确公式已抽出}}\ ✓\ \text{（可复现形式，见 §1 ✓）}$$
$$\boxed{\textbf{(II-2 失败)}\ \text{本档按公式重建的 LP \textbf{未过内检}}\ ✗\ \Longrightarrow\ \textbf{数值不予采信}\ ✗\ \text{（不写入任何结论 ✓）}$$
$$\qquad\textbf{内检（决定性 ✓）}:\ \text{重建给出 sphere+VW}(t=0)\to\mathbf{110.0262}\ \mathbf{>}\ \text{论文自身 SDP }\mathbf{105.2223}\ ✗✗$$
$$\qquad\Longrightarrow\ \text{任何\textbf{有效}松弛必 }\le\ \text{SDP}\ ✓\ \Longrightarrow\ \text{我对 Van Wee (5) 的读法\textbf{必有误}}\ ✗\ \text{（自检抓到 ✓，未外泄 ✓）}$$
$$
$$
```

---

## §1 (II-1) 已抽出的精确公式（资产 ✓）

```
$$K_q(n,r)\ \ge\ \min_{x}\ q^n x_0\quad\text{s.t.}\ x=(x_0,\dots,x_n)^{\sf T}\ge0:$$
$$\qquad\text{(i)}\ \sum_{i=0}^{n}x_iP_k(i)\ \ge\ 0\qquad\text{(Krawtchouk 正性 ✓)}$$
$$\qquad\text{(ii)}\ \sum_{i=0}^{n}x_i\sum_{j=0}^{n}\lambda_j\alpha^k_{i,j}\ \ge\ \beta x_0$$
$$\qquad\text{(iii)}\ \sum_{i=0}^{n}(x_0-x_i)\sum_{j=0}^{n}\lambda_j\alpha^k_{i,j}\ \ge\ \beta(1-x_0)\qquad\forall k=0,\dots,n$$
$$P_k(i)=\sum_{s}(-1)^s\binom{i}{s}\binom{n-i}{k-s}(q-1)^{k-s}\ ✓;\quad \alpha^k_{i,j}=\sum_{t:\,2t=k+i-j}\binom{k}{t}\binom{n-k}{i-t}\ (q=2)\ ✓$$
$$\text{Van Wee (5)}:\quad A_i(u)+A_r(u)+A_{r+1}(u)\ \ge\ \left\lceil\frac{n+1}{r+1}\right\rceil\ \text{（读法待定 ⚠️，见 §2 ✓）}$$
$$
$$
```

---

## §2 (II-2) 重建结果与可疑点（诚实列全 ✓）

```
$$\begin{array}{c|c|c}
\text{配置} & \text{本档重建值} & \text{唐先生锚点}\\
\hline
\text{Sphere only} & \mathbf{94.0198} & \text{① }93.0909\ \text{（而 94.0198 是其②）}\ ⚠️\\
\text{+ Krawtchouk (i)} & 94.0198\ (\textbf{完全无变化}\ ⚠️) & \text{② }94.0198\\
\text{+ Van Wee}(t=1) & 101.6183 & \text{③ }101.0074\ ⚠️\\
\text{+ Van Wee}(t=0) & \mathbf{110.0262}\ ✗ & \text{（> SDP ⟹ 不可能 ✓）}\\
\text{+ Van Wee}(t=2) & 98.4615 & —\\
\end{array}$$
$$\textbf{三处异常（全部指向建模误差 ✓）}:\ \text{① sphere 值偏高（多出 }0.93\ \text{）；\ ② Krawtchouk 项在我模型中\textbf{冗余}（真模型应\textbf{有效}）；\ ③ Van Wee 家族读法致 \textbf{LP>SDP 不可能} ✗}$$
$$\Longrightarrow\ \text{根因判断}:\ \text{(ii)/(iii) 的\textbf{推导与缩放}（}x_i\ \text{是 counts 还是概率？}k\ \text{如何进入？）与 Van Wee (5) 的 \textbf{精确读法} 我均为\textbf{猜测} ⚠️\ \text{——不可靠 ✓}$$
$$
$$
```

---

## §3 需要唐先生提供的三件（拿到即可复现 ✓）

```
$$\text{① (ii)/(iii) 的\textbf{精确推导与缩放}}（x_i\ \text{归一化？}k\ \text{的角色？})\ ✓$$
$$\text{② Van Wee (5) 的\textbf{精确读法}}（A_i\ \text{的下标 }i\ \text{指什么？"对每个 }i"\ \text{还是一次一条？})\ ✓$$
$$\text{③ 你的 LP 构建\textbf{代码或伪码}}（既已复现 }93.0909/94.0198/101.0074/101.4082\ ✓\text{）}$$
$$\Longrightarrow\ \text{齐备后：单脚本复现四个锚点 ⟹ 才做\textbf{可信}的约束贡献分解（D-LP-1 ✓）}$$
$$
$$
```

---

## §4 副产品：新增强制自检门（建议登记 ✓）

```
$$\boxed{\text{LP/SDP 重建\textbf{强制内检}:\quad \text{任意有效松弛}\ \le\ \text{已知 SDP}\ ✓}}\ \text{——违反 ⟹ 建模必错 ⟹ 数值\textbf{禁止}入档}\ ✗$$
$$\qquad\textbf{本次实证}:\ 110.0262>105.2223\ \text{即被该门拦下}\ ✓\ \text{（否则会污染档案 ✓）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 为**论文公式引用** ✓（逐字抽取 ✓）；§2 的数值为**本档重建**，**未过内检 ⟹ 不作为结果** ✗
- 唐先生锚点（93.0909／94.0198／101.0074／101.4082）**本档未能复现** ⇒ 记为"**待复核**" ⚠️（不确认为事实 ✓）
- 论文自身表 5 值 $105.2223$（$n=10,R=1$，**无粗体、无星号** ⟹ 非该文改进 ✓）为**已核实** ✓
- **未**排除 119 ✗、**未**给出任何新的下界主张 ✗；本档=**方法与自检记录** ✓


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 重建未过内检 命中文件数=1    :: ./DLP1-2026-09-27-formula-extracted-but-reconstruction-invalid.md 
技术词 LP 小于等于 SDP 自检门 命中文件数=0    ::
```
- **本档新增**：重建未过内检、LP ≤ SDP 自检门（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：Delsarte LP、Krawtchouk、Van Wee、Gijswijt–Polak
