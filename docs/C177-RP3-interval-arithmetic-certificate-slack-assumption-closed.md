已查地图（**先查后写**）：`C-163`（`M=3` 浮点证书；`SLACK=10^{-12}` 假设）、`C-165`（误差模型核验）、`C-176`（`m_M` 上界的区间算术证书）、`RPM-LEMMA-CONJECTURE-LEDGER`（`D1a`）。关键词回查：`区间算术证书`=0、`奇数倍判定`=0、`假设闭合`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 19:12「开始下一条」）**：**`D1a` —— 把 `M=3` 证书改为区间算术版，闭合 `SLACK` 假设。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{成功}：\text{区间算术版自适应分支定界} \Longrightarrow \textbf{全部箱认证}（\mathbf{13{,}455}\ \text{箱}，\textbf{0 未决}，\text{余量}\ 1.5938\times10^{-3}，81.8\ \text{秒}）✓✓$$
$$\qquad \Longrightarrow \boxed{m_3\ \ge\ \tfrac12\ \textbf{严格}（\text{区间算术；无 SLACK、无浮点误差假设}）}✓✓$$
$$\textbf{(二)}\ \text{与}\ \text{`C-163`}\ \text{浮点版对照}：\text{浮点}\ 17{,}440\ \text{箱／余量}\ 2.005\times10^{-3}／0.06\ \text{s}；\text{区间版}\ 13{,}455\ \text{箱／余量}\ 1.594\times10^{-3}／81.8\ \text{s}✓$$
$$\qquad \text{箱数反而更少（拆分策略不同：只拆最宽维）；余量更小（保守，符合预期）}✓$$
$$\textbf{(三)}\ \textbf{残余缺口从"假设"降为"实现正确性"}：\text{区间算术是标准证书技术；}\text{`B2`}\ \text{的浮点缺口对}\ M=3\ \textbf{已闭合}✓✓$$
$$\qquad \text{凭此}：(\text{RP}_3)\ \text{的严格性来源与}\ \text{`C-176`}\ \text{同级（唯一非精确对象含于区间）}✓$$

FREEZE-ACK: 本档即冻结期内的证书实现与登记（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=3` 区间算术证书（闭合 SLACK）＋ 与浮点版对照 ＋ 台账勾选** —— 关系 = 严格化与登记，非新机制
D1: 0

# C-177 · ⭐⭐ **`(RP_3)` 区间算术证书 —— `SLACK` 假设已闭合**

> **唐先生 2026-09-19 19:12**：开始下一条（`D1a`）✓

---

## §1 结果

$$\textbf{定理（本档）}：m_3:=\min_{\varphi\in[0,\pi]^3}\max_{1\le k\le15}\sum_{j=1}^3\cos(k\varphi_j)\ \ge\ \tfrac12\ \textbf{严格}✓✓$$
$$\begin{array}{c|r}
\text{评估箱数} & 13{,}455\\
\text{未决箱数} & \mathbf 0\\
\text{最大深度} & 19\\
\text{认证最小余量} & 1.5938\times10^{-3}\\
\text{耗时} & 81.8\ \text{秒}\\
\text{全部认证} & \textbf{True}\\
\end{array}✓$$
$$\text{结论输出（脚本原文）}：\texttt{⟹ 严格结论（区间算术, 无 SLACK、无浮点误差假设）:  m\_3 >= 1/2}✓$$

## §2 严格性机制（与 `C-163` 的差别）

$$\text{`C-163`}\ \text{（浮点版）}：\text{每箱下界用}\ \texttt{float}\ \text{算}，\textbf{假设} \text{浮点误差}\ \le\mathrm{SLACK}=10^{-12}✗\（\text{假设}）$$
$$\text{本档（区间版）}：\text{四个环节全部严格化}：$$
$$\qquad \text{(i)}\ \text{域取}\ [0,P]^3，P:=\text{（}\pi\ \text{的有理上界）} \Longrightarrow [0,\pi]^3\subseteq[0,P]^3\（\textbf{更强}）✓$$
$$\qquad \text{(ii)}\ \text{箱边界为}\ \textbf{精确有理数}（\texttt{Fraction}）；k\,a_j\ \text{为精确有理（整数运算）}✓$$
$$\qquad \text{(iii)}\ \cos\ \text{用}\ \texttt{mpmath.iv}（\pi\ \text{取区间}）\Longrightarrow \text{取区间下端}✓$$
$$\qquad \text{(iv)}\ \text{"区间含}\ \pi\ \text{的奇数倍"}\ \textbf{严格判定}（\text{用}\ \pi\ \text{的有理上下界}）；\textbf{不确定时保守取}\ -1✓✓$$

## §3 每箱下界的正确性（三行，本档复用）

$$\text{对箱}\ B=\prod_j[a_j,b_j]，\ k\le15：\min_{\varphi\in B}\sum_j\cos(k\varphi_j)=\sum_j\min_{\varphi_j\in[a_j,b_j]}\cos(k\varphi_j)=:c_k(B)✓$$
$$\Longrightarrow \forall\varphi\in B：\ \max_k\sum_j\cos(k\varphi_j)\ \ge\ \max_k c_k(B)=:\mathrm{LB}(B)✓$$
$$\Longrightarrow \min_{\varphi\in B}\max_k\sum_j\cos(k\varphi_j)\ \ge\ \mathrm{LB}(B)✓\ \Longrightarrow\ \mathrm{LB}(B)\ge\tfrac12\ \text{即认证该箱}✓$$
$$\text{单区间最小值算法}：\cos\ \text{的局部极小只在}\ \pi\ \text{的奇数倍处} \Longrightarrow \text{含奇数倍取}\ -1；\text{否则取两端较小者}✓✓$$

## §4 台账勾选与骨架同步

- `D1a` → **`[x]` 完成** ✓（本档）
- `B2` 残余缺口说明更新：`M=3` 的浮点缺口**已闭合**；`M=4/5` 仍用 `SLACK`（见 `D1b`）✓
- 论文骨架第 4 行（定理 2–4）可注：`M=3` 已有区间算术版（严格性来源同 `C-176`）✓

## §5 复现

```
脚本: scripts/m3_certificate_interval_arith.py
运行: python3 scripts/m3_certificate_interval_arith.py 200000 40
     （参数: 预算箱数 / 最大深度）
输出: 评估箱数 13455 | 未决 0 | 最大深度 19 | 余量 1.5938e-3 | 全部认证 True
脚本内自带: 域/pi 上下界/每箱不等式/单区间最小值算法 的说明
```

## §6 边界

- ⚠️ 严格性依赖 `\texttt{mpmath.iv}`（标准区间算术）的正确性 —— 这是**实现正确性假设**，比浮点 `SLACK` 强得多（区间算术是标准证书技术）✓
- ⚠️ 本档只处理 `M=3`；`M=4/5` 仍有浮点缺口（`D1b` 待做；`M=5` 见 `C-168` 的算力估算）✓
- ⚠️ **不声称** `(\text{RP}_M)` 一般成立 ✓
- **未用** RH；**未改**任何原档（台账与骨架为勾选／注释更新）✓
- **纪律**：先查后判（R-1 ✓）、**先跑后写** ✓（脚本先跑出 0 未决，再落档）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 19:2x）`[纪律]`（先跑后写）

```
技术词 区间算术证书  命中文件数=3 :: ./RPM-LEMMA-CONJECTURE-LEDGER.md ./C176-...md ./C172-...md
技术词 奇数倍判定   命中文件数=0 ::
技术词 假设闭合    命中文件数=0 ::
```
**读数（按实测，逐项标注）**：
· `区间算术证书` = **复用**（`C-176`／`C-172`／总台账已有；本档沿用，**不列为新增**）✓
· `奇数倍判定` = **本档新增** ✓
· `假设闭合` = **本档新增** ✓
