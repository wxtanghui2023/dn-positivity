已查地图：已跑 scripts/prework_map_check.sh Ψ_mid 新颖性审计 距离分布 缩短 n=9 ⟹ 执行自 PSI2-2026-09-26 档；本档为**A（Ψ_mid）判定性审计：按预设规则关闭** ✗ ＋ **B（n=9）启动** ✓（唐先生 2026-09-26 13:29 指令）。
D0: 本档对象 = 中点泛函的新颖性审计，及其判定结果
D1: 1（新增：**A 被审计关闭** ✗（Ψ_mid 在极值壳由距离分布决定）；新增 (5,8) 中段例外 ✓；B 启动 ✓）

# PSIMID-2026-09-26

## §1 唐先生判据（预设 ✓）

```
$$\boxed{\Psi_{\mathrm{mid}}\ \text{必须出现\textbf{无法由已有二点数据解释}的 }Q=0\ \text{特异性};\ \text{否则 A 立即关线，转 B }(n=9)}\ ✓$$
$$

## §2 ⛔ 判据结果：**A 关线** ✗（我方审计 ✓）

```
$$\text{定义（本轮脚本 ✓）}: \mathrm{PM}=\sum_{\{c,c'\}:\ d(c,c')=2}o(m_1)\,o(m_2)\ ✓,\quad \mathrm{SM}=\sum(o(m_1)+o(m_2))\ ✓$$
$$\textbf{按 }(\text{距离分布},Q)\ \text{分组，组内 }(\Psi_2,Z_2,\mathrm{SM},\mathrm{PM})\ \text{取值数}:$$
$$\begin{array}{c|c|c|c}
(n,M) & \text{分组数} & \text{组内恒定组数} & \text{固定分布下(跨 }Q\text{)出现多值} \\
\hline
(4,4)=K & 2 & \textbf{2/2}\ ✓ & 0/2\ ✗\\
(5,7)=K & 1 & \textbf{1/1}\ ✓ & 0/1\ ✗\\
(6,12)=K & 2 & \textbf{2/2}\ ✓ & 0/2\ ✗\\
(4,5)>K & 5 & 5/5\ ✓ & 0/5\ ✗\\
(5,8)>K & 21 & 21/21\ ✓ & \textbf{4/21}\ ✓⚠️\\
\end{array}$$
$$\Longrightarrow\ \textbf{在极值壳（}M=K\text{）上，}\mathrm{PM},\Psi_2\ \textbf{完全被距离分布决定}\ ✗\ \Longrightarrow\ \textbf{按预设规则：A 关线}\ ✗✓$$
$$

## §3 诚实附注（两条 ✓）

```
$$\text{① 低功效警告}: (5,7)\ \text{的距离分布\textbf{唯一}（}(2,4,10,5,0)\ ✓)\ \Longrightarrow\ \text{该处"组内恒定"是\textbf{平凡}的}\ ✗\ (\text{任何函数都恒定}\ ✓)$$
$$\qquad\text{即}: \text{A 的关闭结论在 }n=5\ \text{处证据最弱}\ ⚠️;\ \text{在 }n=4,6\ \text{处（各有 2 个分布族）证据较强}\ ✓$$
$$\text{② 中段例外（值得记录 ✓）}: (5,8)\ (M>K)\ \text{有 }4/21\ \text{个距离分布族允许 }(Q,\mathrm{SM},\mathrm{PM})\ \text{多值}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{二阶泛函\textbf{在一般情况下确含超出距离分布的信息}}\ ✓\ ——\ \text{但\textbf{在极值壳上不含}}\ ✗\ (\text{§2}\ ✓)$$
$$

## §4 B（n=9）启动：**缩短构造法** ✓

```
$$\text{目标}: \text{构造一个 }(9,M)_1\ \text{覆盖码、尽量逼近 }K(9,1)\ \text{（文献记 62 ⚠️ 待核）},\ \text{并算 }Q\ ✓$$
$$\text{方法（低成本 ✓）}: \text{由已有的 Kamenetsky }(10,120)_1\ \text{码\textbf{缩短}}\ ✓: C_v=\{c\setminus\{i\}:\ c\in C,\ c_i=v\}\ ✓$$
$$\text{理论（我方推导 ✓）}: \text{未被 }C_v\ \text{覆盖的点恰好落在 }C_{1-v}\ \text{中}\ ✓\ \Longrightarrow\ \text{缺口 }\le|C_{1-v}|\approx60\ ✓\ \text{可贪心\textbf{增补}修复}\ ✓,\ \text{再去冗余}\ ✓$$
$$\text{判据}: \text{若得 }M=62\ \text{且 }Q=0\ \Longrightarrow\ \textbf{C1 被反驳}\ ✓✓\ (\text{重要！});\ \text{若 }Q\ge2\ \Longrightarrow\ \text{C1 得支持}\ ✓$$
$$\qquad(\text{因 }n=9\ \text{奇}: E=62\cdot10-512=108\ \text{偶}\ \Longrightarrow\ Q\ \text{偶}\ ✓\ \Longrightarrow\ \text{C1 预测 }Q\ge2\ ✓)$$
$$

## §5 边界（诚实标注）

- §2 为**我方审计**（n=4,5 全枚举 ✓；n=5 M=8、n=6 M=12 采样 ✓）；§3 的附注为**我方自我限定** ✓
- §4 的 B 为**进行中** ⏳；其结论将同时作用于 C1 与"生死测试" ✓
- **未**触碰 119 结论 ✗；**119 保持 UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

```
技术词 中点泛函审计 命中文件数=0    :: 
技术词 距离分布决定 命中文件数=0    :: 
技术词 中段例外     命中文件数=0    :: 
技术词 缩短构造     命中文件数=1    :: ./FRONTIER-2026-09-25-K10-1-status-and-reassessment.md
```

- **本档新增**（命中数=0）：中点泛函审计、距离分布决定、中段例外
- **档案已有（引用，不列为提出）**：缩短构造
