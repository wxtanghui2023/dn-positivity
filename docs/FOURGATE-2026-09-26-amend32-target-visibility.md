已查地图：已跑 scripts/prework_map_check.sh 目标可见性 四门链 RH 119 共同失败机制 ⟹ 执行自 `PROGRESS-GATE-2026-09-26`（AMEND-31 ✓）＋ `FREEDOM-AUDIT-2026-09-26`（单侧耦合 ✓）；本档为**研究框架升级**（唐先生 2026-09-26 22:19 裁定 ✓）；未跑计算 ✓。
D0: 本档对象 = 目标可见性框架与四门链（方法论对象）
D1: 0（产出为 AMEND-32 条文、回溯四门表与 FRONTIER 筛选器）

# FOURGATE-2026-09-26 · AMEND-32：目标可见性与四门链

## §0 统一框架（RH 与 119 同构 ✓）

```
$$\boxed{\text{Target}\ \to\ \text{target-sensitive observable}\ \to\ \text{correct-direction constraint}\ \to\ \text{collision}}\ ✓$$
$$\text{RH}:\quad \beta\ \to\ \mathcal O_\beta\ \to\ \text{零点位置约束}\ \to\ \beta=\tfrac12\ ✓$$
$$\text{119}:\quad A_1\ \to\ \mathcal O_{A_1}\ \to\ \textbf{上界型约束}\ \to\ A_1\le49\ ✓$$
$$\textbf{共同失败模式}:\ \boxed{\text{observable exists}\ \not\Rightarrow\ \text{correct-direction constraint exists}}\ ✓✓$$
$$
$$
```

---

## §1 二分结构（同构 ✓）

```
$$\text{RH}:\ \beta\text{-sensitive}\quad/\quad\beta\text{-blind}\ ✓\qquad\text{119}:\ A_1\text{-sensitive}\quad/\quad A_1\text{-blind}\ ✓$$
$$\text{且 }\beta\text{-盲}\Rightarrow\text{不能推进 RH}\ ✓;\quad A_1\text{-盲}\Rightarrow\text{不能推进 }A_1\le49\ ✓$$
$$\textbf{信息矩阵}:\ \begin{array}{c|cc} & \text{有约束力} & \text{无约束力}\\ \hline \text{target-sensitive} & \boxed{\text{真正突破}}\ (\textbf{缺}\ ✗) & \text{RH }\beta\text{-盲／119 方向反的大量成果}\\ \text{target-blind} & \text{强但无法对接目标} & \text{纯背景} \end{array}$$
$$
$$
```

---

## §2 两条纪律不等式（并列 ✓）

```
$$\boxed{\text{independence}\ \ne\ \text{usefulness}}\ ✓\qquad \boxed{\text{sensitivity}\ \ne\ \text{leverage}}\ ✓✓$$
$$\textbf{可用判据（119 语）}:\ \text{需}\ I\le C\ \textbf{且}\ I\ \text{随}\ A_1\ \textbf{单调增}\ \Longrightarrow\ A_1>C'\Rightarrow I>C\ \Longrightarrow\ \text{排除 }A_1>49\ ✓$$
$$\qquad\text{反向（下界型）}:\ I\ge f(A_1)\ \text{且}\ f\ \text{随 }A_1\ \textbf{下降}\ \Longrightarrow\ \textbf{压不住}\ ✗\ \text{（本线绝大多数情形 ✓）}$$
$$
$$
```

---

## §3 四门链（AMEND-32 核心条文 ✓）

```
$$\boxed{\textbf{Novel}\ \to\ \textbf{Independent}\ \to\ \textbf{Target-sensitive}\ \to\ \textbf{Correct-direction}}\ ✓$$
$$\qquad\text{四门全过}\ \Longrightarrow\ \text{方可进入 }\textbf{P1/P2 attack}\ ✓;\quad \text{任一失败}\ \Longrightarrow\ \text{出局（可存为审计记录 ✓，不计推进 ✗）}$$
$$\textbf{与 AMEND-31 的关系}:\ \text{AMEND-31 的 }D\ \text{＝第 3＋4 门的合取}\ ✓\ \text{（本档把 }D\ \textbf{拆成两个独立门}\ ✓✓）$$
$$
$$

$$\textbf{搜索顺序反转（RH 线最昂贵教训 ✓）}:$$
$$\text{旧}:\ \text{mechanism}\to\text{observable}\ \to\ \text{再问能否用于目标}\ ✗\qquad\text{新}:\ \boxed{\text{target}\to\text{direction}\to\text{mechanism}\to\text{observable}}\ ✓✓$$
$$
$$
```

---

## §4 FRONTIER-R1 筛选器（按目标类型 ✓）

```
$$\text{目标＝存在性}\ \exists S:\ \text{需}\ \text{结构量}\to\textbf{必要条件}\to\textbf{不可实现}\ ✓$$
$$\text{目标＝最小参数 }v_{\min}:\ \text{需}\ \text{结构量}\to v\text{-依赖界}\ ✓$$
$$\text{目标＝分类}:\ \text{需}\ \text{结构量}\to\textbf{class separator}\ ✓$$
$$\Longrightarrow\ \text{今后任何 invariant 必须声明}:\ \boxed{\text{对哪个 target variable sensitive？}}\ ＋\ \boxed{\text{约束方向？}}\ ✓\ \text{（不得只写"很新" ✗）}$$
$$
$$
```

---

## §5 回溯四门表（诚实 ✓）

```
$$\begin{array}{l|c|c|c|c}
\text{产出} & Novel & Independent & Target-sensitive & Correct-direction\\
\hline
\mathbf{A_1\le49} & ✓ & ✓ & ✓\ (\text{即 }A_1\ \text{本身}) & ✓\ (\text{上界}) & \Longrightarrow\ \textbf{唯一过四门者}\ ✓\ \text{（但 }L\ \text{弱 ⚠️）}\\
|I|\ge21 & ✗\ (\text{推论}) & - & - & -\\
9{:}1\ \text{面多重度} & ✓ & ✗\ (=f(A_1,A_2)) & - & -\\
q_F\le2 & ✗\ (\text{匹配推论}) & - & - & -\\
p\ \text{下界（凸性）} & ✓ & ✓ & ✓\ (\text{单侧}) & \mathbf{✗}\ (\text{方向反}) & \Longrightarrow\ \text{第四门被截}\ ✓✓\\
\tau_2 & ✓ & ✓ & ✗\ (\text{已解耦：}\tau_{M,D}=0) & -\\
G_k\ \text{壳能量} & ✓ & ✗\ (\text{两矩钉死}) & - & -\\
\text{Green 核} & ✓ & ✓\ (\text{混号}) & ✗\ (\text{非 order-preserving}) & -\\
\end{array}$$
$$\Longrightarrow\ \text{与 }\texttt{FREEDOM-AUDIT}\ \text{一致}:\ \text{近期\textbf{唯一过四门＝}A_1\le49};\ \text{其余全部在第 3／4 门被截}\ ✓✓\ \text{（这正是 RH 线的同一机制 ✓）}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §0–§4 为**方法论条文**（AMEND-32 写入 `RESEARCH-CONSTITUTION.md` ✓）
- §5 为**回溯判定** ✓（依四门链 ✓）；不删既有档案 ✓（仅改判 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张四门链充分（只主张必要 ✓）
- 本轮**未跑**计算 ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 目标可见性框架 命中文件数=1    :: ./FOURGATE-2026-09-26-amend32-target-visibility.md 
技术词 四门链        命中文件数=1    :: ./FOURGATE-2026-09-26-amend32-target-visibility.md 
技术词 FRONTIER 筛选器 命中文件数=1    :: ./FOURGATE-2026-09-26-amend32-target-visibility.md
```
- **本档新增**：目标可见性框架、四门链、FRONTIER 筛选器（见上方命中数；0 命中者为自造语 ✓）
- **档案已有（引用，不列为提出）**：AMEND-31、FREEDOM-AUDIT、T3MIN1 的 A₁-盲、凸性下界方向
