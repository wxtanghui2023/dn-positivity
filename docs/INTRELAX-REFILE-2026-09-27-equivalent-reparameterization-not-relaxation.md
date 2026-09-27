已查地图：已跑 scripts/prework_map_check.sh 整数覆盖 重参数化 vs 松弛 ⟹ 续 `INTRELAX-2026-09-27-...`（等价定理 PA-1 ✓）＋ 唐先生 15:54 指令（改档定性 ✓）；本档 = **A-INTRELAX-1 正式改档：等价重参数化（NOT a relaxation）✓ ＋ 状态锁定 ✓**。
D0: 本档对象 = A-INTRELAX-1 之定性归位与 119 状态锁定
D1: 3（**改档定性 ✓（非松弛）**；**状态锁定 ＋ 不做清单 ✓**；**旁线审计：为何"更宽变量域"只改搜索效率、不改数学对象 ✓**）

# A-INTRELAX-1 改档：等价重参数化（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(QA-1 ✅改档定性（唐先生 ✓）)}\ \text{A-INTRELAX-1 正式归类为}\ \boxed{\text{整数覆盖的\textbf{等价重参数化}（equivalent reparameterization）}}\ \textbf{而\textbf{不是} relaxation ✗✓}$$
$$\qquad\textbf{依据（PA-1 ✓）}:\ \boxed{\min\{\mathbf 1^{\mathsf T}f:\ Tf\ge1,\ f\in\mathbb Z_{\ge0}\}=K(n,1)}\ ✓ \Longrightarrow \text{它与原问题\textbf{最优值相同、可行集一一对应} ⟹ \textbf{既不变弱也不变强} ✗}$$
$$\qquad\textbf{归位后果 ✓}:\ \boxed{\text{它\textbf{不得}列入松弛族（profile／}A_d\text{／local-SA／Lasserre ✗）}}\ \text{—— 那些是\textbf{弱化}（下界 ≤ 真值 ✓）；本项是\textbf{换坐标}（值恰等 ✓）};\ \text{可免未来误称 relaxation ✓}$$
$$\qquad\textbf{正确定位 ✓}:\ \text{它是"面向 solver 的\textbf{重述}"}，服务于同一个决策问题：}\boxed{\textbf{P1：119 feasibility}}$$
$$\boxed{\textbf{(QB-1 🔒状态锁定（唐先生 ✓）)}\ \textbf{唯一运行}:\ \min\sum f,\ Tf\ge1,\ f\in\mathbb Z_{\ge0}\ (\text{ILP},\ \text{HIGHS},\ \text{后台 ✓});\ \textbf{不轮询 ✗}}$$
$$\qquad\textbf{暂不做（清单 ✓）}:\ \text{① 第二个 CP-SAT ✗；② Level-4 Lasserre ✗；③ R2 修复 ✗；④ 新 }\delta\ \text{恒等式 ✗；⑤ 第 22 个"候选机制" ✗}$$
$$\qquad\textbf{结果分叉表 ✓}:\ \begin{array}{c|l}
\text{ILP 结果} & \text{下一步}\\
\hline
\text{找到 }\sum f=119 & \text{取 }C=\mathrm{supp}(f)\ \text{得 119-cover ⟹ \textbf{正向突破}（进 P2 验证 ✓）}\\
\text{证 optimum}=120 & \textbf{P1 完成} ⟹ K(10,1)\ge120\ ✓\\
\text{UNKNOWN} & \text{才考虑 Level-4／其它 exact 方法 ⚠️}
\end{array}$$
$$\qquad\textbf{验收协议 ✓（唐先生强调 ✓）}:\ \text{若得 }119,\ \textbf{不得}只采信 HIGHS 目标值 ⟹ 必须\textbf{取支撑}并\textbf{独立逐点验证}:\ \boxed{|C|=119\ \wedge\ \forall x:\ |C\cap B_1(x)|\ge1}\ ✓✓$$
$$
$$
```

## §1 旁线审计：为何"更宽变量域"只改搜索效率（**✓**）

```
$$\textbf{直觉 ✓}:\ f\in\mathbb Z_{\ge0}\ \text{比 }f\in\{0,1\}\ \text{"更宽" ⟹ 每个 node 的 LP 更松 ⟹ 通常更好解 ✓（MIP 的舍入/启发式空间更大 ✓）}$$
$$\textbf{但数学对象不变 ✓（关键 ✓）}:\ \text{任一整数解 }\Longrightarrow C=\mathrm{supp}(f)\ \text{是 0-1 覆盖码且 }|C|\le\sum f\ ✓ \Longrightarrow \text{整数模型\textbf{不}引入新对象类型 ✗（若得 119，它\textbf{就是}一个 119-code ✓）}$$
$$\textbf{且它也不能给出"更强"的不可行证书 ✗}:\ \text{因 }K_{\mathbb Z}(n,1)=K(n,1)\ \text{（PA-1 ✓）} \Longrightarrow \text{两问题的（不可）可行性\textbf{完全同步} ⟹ 整数形只是\textbf{不同搜索顺序} ✓}$$
$$\qquad\Longrightarrow\ \textbf{本轮的净价值 = \textbf{搜索效率}（换 solver／换启发式）而非\textbf{新信息源} ✓；}\ \text{故①不追加第二 solver（同源 ✗）②结果仍须过验收协议 ✓}$$
$$
$$
```

## §2 状态（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{唯一在跑 = 该 ILP；}\ \text{不写禁止表述 ✓};\ \text{不加新计算 ✗}}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：A-INTRELAX-1 之改档（等价重参数化，非 relaxation）、状态锁定与不做清单、验收协议、旁线审计（变量域宽 ⟹ 仅搜索效率）
- **档案已有（引用，不列为提出）**：A-INTRELAX-1（等价定理 PA-1）、M-2A、CP-SAT UNKNOWN、Level-4/R2 项


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 等价重参数化 命中文件数=1    :: ./INTRELAX-REFILE-2026-09-27-equivalent-reparameterization-not-relaxation.md 
技术词 验收协议     命中文件数=2    :: ./E4-2-falsifiable-conditions-spec-for-line-enforcing-localization.md ./INTRELAX-REFILE-2026-09-27-equivalent-reparameterization-not-relaxation.md
```
- **本档新增**：A-INTRELAX-1 之改档（等价重参数化，非 relaxation）、状态锁定与不做清单、验收协议、旁线审计（变量域宽 ⟹ 仅搜索效率）（见上方命中数；0 命中者为自造语／内部标签 ✓）
