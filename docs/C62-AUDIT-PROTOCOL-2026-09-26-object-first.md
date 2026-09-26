已查地图：已跑 scripts/prework_map_check.sh C_62 审计 指纹 ⟹ 执行自 UNIONV-2026-09-26 档；本档为**C₆₂ 到手后的审计协议（对象优先 ✓）**（唐先生 2026-09-26 16:14 裁定 ✓）；未跑 solver ✓。
D0: 本档对象 = C₆₂ 的获取路线与到手后的固定审计清单（不做任何前置计算 ✓）
D1: 0（协议档，未新增数学对象 ✓）

# C62-AUDIT-PROTOCOL-2026-09-26

## §0 状态标签（唐先生 ✓）

```
$$\boxed{\text{SHELL = ARCHIVED / SUPPORTING ASSET}}\ ✓;\qquad \boxed{\text{MAIN = RECOVER }C_{62}\text{ FIRST}}\ ✓;\qquad \boxed{\text{THEN = attack }h/d_C\text{ with the actual extremal fingerprint}}\ ✓$$
$$

## §1 获取路线（按可及性排序 ✓，不再扩大 SAT ✗）

```
$$\textbf{① 文献（首选 ✓）}: \text{Fagioli 1984 / Wille 1996（IEEE TIT 42:300--302）}\ ✓;\ \text{Kéri 论文已给 4 词锚点}\ ✓$$
$$\qquad\text{需唐先生下载（付费墙）}\ ✓;\ \text{已确认 }K(9,1)=62\ \text{的两构造在\textbf{同一 switching class}}\ [L]\ ✓$$
$$\textbf{② 公开数据源（我方继续探）}: \text{Östergård 站点命名模式、covering-code 数据仓、arXiv 附录}\ ⚠️$$
$$\textbf{③ 不再做}: \text{扩大 SAT 模型}\ ✗;\ \text{盲目 SA}\ ✗\ (\text{已试，未达 62}\ ✓)$$
$$

## §2 到手后的固定审计清单（一次算全 ✓）

```
$$C_{62}\ \longrightarrow\ \boxed{\big(A_1,\ A_2,\ I,\ S,\ Q_2,\ S_q,\ |V_\square|,\ I_{\rm nw},\ d_{\max},\ (N_j)\big)}\ ✓$$
$$\textbf{逐项判据}:$$
$$\quad\text{(i) }d_{\max}:=\max_c d_C(c)\quad\Longrightarrow\ \textbf{是否恒为 }2\ ?\ \text{(即 }h=0\text{)}$$
$$\quad\text{(ii) }I_{\rm nw}=I-|V_\square|\quad\Longrightarrow\ 0\ \text{还是} >0\ ?$$
$$\quad\text{(iii) }S_q>0\ ?\ (\text{Wille 构造成分含方阵}\ [L]\ \Longrightarrow\ \text{预期 }>0\ ✓)$$
$$\quad\text{(iv) }L_\square=0\ ?\ (\text{shell 洁净性——与 }(9,64)\ \text{对照}\ ✓)$$
$$\quad\text{(v) }(N_j)\ \text{剖面与 }K=62\ \text{下的恒等式 }2A_{\le2}=E+Q_2\ \text{自洽}\ ✓$$
$$
$$

## §3 审计后的三分支决策（预先锁定 ✓）

```
$$\textbf{若 }I_{\rm nw}=0\ \wedge\ d_{\max}=2:\ \text{则"压 }I\text{"方向需\textbf{重新定位}}\ ⚠️;\ \text{极值机制须从别处找}\ ✓$$
$$\textbf{若 }I_{\rm nw}>0\ \text{或 }d_{\max}\ge3:\ \text{则可从\textbf{真实极值对象反推必然机制}}\ ✓\ (\text{比抽象搜索干净}\ ✓)$$
$$\textbf{若 }C_{62}\ \text{与 }(9,64)\ \text{的不变量谱一致}:\ \text{提示 }n=9\ \text{的极值层"扁平"}\ ⚠️$$
$$

## §4 边界（诚实标注）

- 本档**不含任何新计算** ✓；**未跑 solver** ✓
- `C_62` **仍未获得** ✗；119 **UNKNOWN** ✓；问题 G **KEEP OPEN** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：对象优先协议、三分支决策
- **档案已有（引用，不列为提出）**：fingerprint、switching class、shell
