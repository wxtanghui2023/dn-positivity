已查地图：已跑 scripts/prework_map_check.sh K(10,1) 算子路 封档 RoSQS 状态 ⟹ 执行自 `LGREEN1-2026-09-26`（核符号否证 ✓）＋ `FRONTIER-R1-CHECK-2026-09-26`（五格核查 ✓）；本档为**封档＋状态登记**（唐先生 2026-09-26 21:59 裁定 ✓）。
D0: 本档对象 = 119 线算子路封档与 FRONTIER-R1 状态（既有对象）
D1: 0（产出为四路排除图、G-CAL 硬 STOP 与证据分层）

# CLOSURE-2026-09-26 · 算子路封档 ＋ FRONTIER-R1 状态

## §1 L-GREEN-1：**STRUCTURAL NO-GO** ✓

```
$$\boxed{\text{L-GREEN-1 — STRUCTURAL NO-GO}}\ ✓\ \text{（结构性，非"这组数没撞出矛盾"的偶然失败 ✓）}$$
$$
$$

$$\text{四条路的排除图（本档汇总 ✓）}:$$
$$\begin{array}{c|l|l}
\text{路线} & \text{机制} & \text{否定原因}\\
\hline
\texttt{FACE} & \text{二阶 incidence（face occupancy／对-面多重度）} & \text{反复汇合到 }(A_1,A_2)\Longrightarrow\text{无独立 P3}\ ✗\\
\texttt{FOURIER} & \text{谱壳能量 }G_k & \text{被已有两矩式钉死}\ ✗\\
\texttt{GREEN} & G=(11I-L)^{-1}\ \text{距离核} & \textbf{核混号}（正 }\{0,1,4,5,8,9\}\text{／负 }\{2,3,6,7,10\}\text{）}\Longrightarrow\text{非 order-preserving}\Longrightarrow\textbf{maximum principle 不存在}\ ✗\\
\texttt{HEAT} & e^{-tL}\ \text{恢复 positivity} & \text{完全谱展开 }\langle f,e^{-tL}f\rangle=\sum_ke^{-2kt}G_k\ \text{回到 Fourier shells}\Longrightarrow\text{无新独立机制}\ ✗
\end{array}$$
$$\qquad\textbf{结构性根源}:\ 11I-L\ \text{本征值有正有负（}11,\dots,-9\text{）}\Longrightarrow\text{算子不定}\Longrightarrow\text{Green 核必变号}\ ✓\ \text{（与计算无关 ✓）}$$
$$
$$
```

---

## §2 FRONTIER-R1：**OPEN / CALIBRATION PENDING** ✓

```
$$\boxed{\text{FRONTIER-R1 — OPEN / CALIBRATION PENDING}}\ ✓$$
$$\qquad\text{五目标格}:\ v=56,\ 70,\ 82,\ 86,\ 98\ ✓\ \text{（各已立 fingerprint：基块证书 }\lesssim150\text{--}440\ \text{块}\ ✓）$$
$$\qquad\textbf{先做 }\texttt{G-CAL}\ ✓;\ \textbf{不直接进入 SAT／搜索}\ ✗\ \text{（唐先生 21:59 ✓）}$$
$$\qquad\textbf{calibration 的判据（关键 ✓）}:\ \textbf{不是}"能否找到一个设计"\ ✗,\ \text{而是}\ \textbf{验证 A23-D4 pipeline 能否从已有 RoSQS 实例稳定提取可检验的结构量/证书}\ ✓✓$$
$$
$$

$$\textbf{硬 STOP（唐先生指定 ✓）}:$$
$$\boxed{\text{若 }\texttt{G-CAL}\ \text{只验证"已有 RoSQS 可被重新编码/验证"}\ \Longrightarrow\ \textbf{不计 G4}\ ✗}$$
$$\boxed{\text{只有当 calibration 暴露出\textbf{此前文献未使用、且能导出 P1/P2 数学约束}的结构机制}\ \Longrightarrow\ \text{才继续五格目标}\ ✓}$$
$$
$$
```

---

## §3 证据分层（**严格分开** ✓，唐先生 21:59 ✓）

```
$$\textbf{(1) frontier／status}:\ \text{Ji--Zhu 2002, J. Combin. Des. \textbf{10}, 433--443（Table I ＝ RoSQS 开放表 ✓）};\ \text{KKW 2025 (arXiv:2509.23483; DCC \textbf{94}:157, 2026) → 构造 RoSQS}(46),(92)\ ✓$$
$$\textbf{(2) calibration}:\ \text{作者站点 }\texttt{steiner3.html}\ \text{＝\textbf{GAP 可读}的已知 }S(3,k,v)\ (v\le50)\ \text{数据库}\ ✓$$
$$\qquad\Longrightarrow\ \textbf{明确}:\ \text{这是 \textbf{calibration data}}，\ \textbf{不是 frontier evidence} ✗\ \text{（不可混写 ✓，唐先生指定 ✓）}$$
$$\textbf{(3) target certificate}:\ \text{RoSQS 对应数据源 ＝ 论文 [29]（\textbf{Zenodo data set}）＋ 作者页 }\texttt{steiner3.html}\ ✓$$
$$\qquad\Longrightarrow\ ⚠️\ \textbf{本档不写"已验证"}：\ \text{[29] 内容\textbf{尚未下载}}\ ✗\ \text{（唐先生 21:59 ✓）}$$
$$\textbf{(4) 自己的新结果}:\ \text{A23-D4／G-CAL 输出}\ ✓\ \text{（尚未产生 ✗）}$$
$$
$$
```

---

## §4 附：本档附带可复用的两条结构性否证（可迁移 ✓）

```
$$\text{(i)}\ \textbf{Green 核混号性}\ \text{（任意距离-transitive 图上 }(cI+L)^{-1}\ \text{型算子，只要谱有正负 ⟹ 核必变号 ✓）}$$
$$\text{(ii)}\ \textbf{匹配定理封死 }d{=}1\text{-Gram}\ \text{（}d_1\le1\Longrightarrow\text{距离-1 指示向量的 Gram 成对角}\Longrightarrow\text{PSD 平凡 ✓）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 四条路的否定**均有细档** ✓（FACE-CLOSURE／FOURIER／LGREEN1／＋HEAT 为 GREEN 档内 §3 ✓）
- §2 的"OPEN/CALIBRATION PENDING"为**状态登记** ✓；未声称任何 G-CAL 结果 ✓
- §3 的分层为**纪律性区分** ✓；第 (3)(4) 层**明确未产生** ✗
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗、**未**主张 119 线终止 ✗（状态仍为 `OPEN — structurally audited` ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 四路排除图  命中文件数=1    :: ./CLOSURE-2026-09-26-operator-routes-and-frontier-status.md 
技术词 G-CAL 硬 STOP   命中文件数=1    :: ./CLOSURE-2026-09-26-operator-routes-and-frontier-status.md 
技术词 证据四层分层 命中文件数=1    :: ./CLOSURE-2026-09-26-operator-routes-and-frontier-status.md
```
- **本档新增**：四路排除图、G-CAL 硬 STOP、证据四层分层（见上方命中数；0 命中者为自造语 ✓）
- **档案已有（引用，不列为提出）**：Green 核、FACE 收敛、Fourier 钉死、A23-D4 模板、Ji–Zhu 2002、KKW 2025
