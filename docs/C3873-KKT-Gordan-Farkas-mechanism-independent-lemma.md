已查地图（**先查后写**）：`C-3872`（**Gordan 证书 ⟹ 结构非奇异性；`c_* = 1/L` 定理化** ✓✓）、`C-3870`（**取到步；六活跃方阵** ✓✓）、`C-3869`（**单边桥引理；步 4 方向更正** ✓✓）、`C-3868`（**证书同构** ✓✓）、`C-3864`（**锥退化** ✓✓）、`C-3863`（**KKT 点与乘子** ✓✓）；地图档 `CLOSED-ROUTES-MAP.md`／`MASTER-STATUS-AND-CLOSURES.md` ✓

D0: 本档对象 = **C-380-73：C-3873 —— KKT–Gordan–Farkas 机制独立化（可复用命题）**（唐先生 2026-09-21 22:52 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

# C-3873 · KKT–Gordan–Farkas 机制（独立命题）

$$\textbf{定位}✓✓：\text{本档}\ \textbf{不增加计算}✓,\ \text{而是把}\ C\text{-3863}\to C\text{-}3864\to C\text{-}3872\ \text{的链}\ \textbf{抽象成可被下一层调用的独立命题}✓✓$$

## §1 命题（假设 → 结论）

$$\textbf{设定}✓：G = (g_1;\dots;g_m) \in \mathbb R^{m\times n}✓;\ \text{本实例}\ m = n+1 = 6✓,\ n = 5✓✓$$

$$\textbf{(H1) 严格正 KKT 证书（}\textbf{strict-complementarity／positive-KKT certificate hypothesis}✓✓）}：\exists y \in \mathbb R^m\ \text{使}\ \boxed{y > 0\ (\text{逐分量})}\ \text{且}\ \boxed{G^{\top}y = 0}✓✓$$

$$\textbf{(H2) 问题形态}✓：\text{行集}\ \{g_i\}\ \text{分为 odd 组}\ \{v_1,\dots,v_r\}\ \text{与 even 组}\ \{w_q\}✓；\ \text{目标}\ \min_h\max_q(w_qh)✓\ \text{s.t.}\ v_ih \le -1✓✓$$

$$\textbf{(H3) 活跃方阵可解（取到步）}✓：\exists(h^*,c^*)\ \text{使}\ v_ih^* = -1\ (i \le r)✓,\ w_qh^* = c^*\ (\forall q)✓✓$$

---

$$\textbf{引理 1（}\textbf{平凡下降锥}✓✓）}：\text{由 (H1)} \Longrightarrow \boxed{\{h:\ Gh \le 0\} = \{0\}}✓✓$$

$$\qquad \textbf{证明}✓✓：\text{Gordan 择一定理}✓：\textbf{恰有一个} \text{成立} —— \textbf{(i)}\ \exists h \ne 0,\ Gh \le 0✓；\ \textbf{(ii)}\ \exists y > 0,\ G^{\top}y = 0✓✓；\ \text{(H1) 即 (ii)} \Longrightarrow \text{(i) 假} \square✓✓$$

$$\textbf{推论 2（}\textbf{结构满列秩}✓✓）}：\text{由 (H1)} \Longrightarrow \boxed{\operatorname{rank}G = n}✓✓$$

$$\qquad \textbf{证明}✓：\text{若}\ \operatorname{rank}G < n \Longrightarrow \ker G \ne 0✓ \Longrightarrow \text{取}\ 0 \ne h \in \ker G\ \text{得}\ Gh = 0 \le 0✗\ \text{与引理 1 矛盾} \square✓✓$$

$$\textbf{推论 3（}\textbf{列空间不含非零非负向量}✓✓）}：\text{由 (H1)} \Longrightarrow \boxed{\operatorname{col}(G) \cap \{z:\ z \ge 0,\ z \ne 0\} = \varnothing}✓✓$$

$$\qquad \textbf{证明}✓✓：\text{设}\ 0 \ne z \ge 0\ \text{且}\ z \in \operatorname{col}G✓ \Longrightarrow -z \in \operatorname{col}G✓ \Longrightarrow \exists h:\ Gh = -z \le 0✓\ \text{且}\ h \ne 0✓（z \ne 0✓）\ \text{与引理 1 矛盾} \square✓✓$$

$$\qquad \Longrightarrow \text{特例}✓✓：\boxed{e_E \notin \operatorname{col}G}✓\ \text{（}e_E = (0,0,1,1,1,1) \ge 0\ \text{且} \ne 0✓）$$

$$\textbf{推论 4（}\textbf{增广矩阵满秩＝结构性非奇异}✓✓）}：\text{由 (H1) ＋ 推论 2 ＋ 推论 3} \Longrightarrow \boxed{\operatorname{rank}\widetilde M = n+1\ \text{即}\ \det\widetilde M \ne 0}✓✓$$

$$\qquad \text{其中}\ \widetilde M = [\,G \mid -e_E\,]✓;\ \text{注意：}\textbf{不是}"\text{行列式数值非零故结构非奇异}"✗✓,\ \text{而是}\ G^{\top}y = 0,\ y > 0 \Rightarrow \{Gh \le 0\} = \{0\} \Rightarrow e_E \notin \operatorname{col}G✓,\ \text{再合}\ \operatorname{rank}G = n✓✓$$

$$\textbf{定理 5（}\textbf{精确桥常数}✓✓）}：\text{由 (H1) ＋ (H3)}⟹\boxed{c_* = \dfrac{1}{L}},\ L := \sum_q\lambda_q✓✓$$

$$\qquad \textbf{下界（}\text{只用 (H1)}✓）}：\text{对任意 primal-feasible}\ h✓：\sum_i\omega_i(v_ih) \le -\sum_i\omega_i = -1✓（\text{odd 归一化}\ \sum_i\omega_i = 1✓）;$$

$$\qquad \qquad \text{代入}\ G^{\top}y = 0\ ⟹\ -\sum_q\lambda_q(w_qh) \le -1 \Longrightarrow \sum_q\lambda_q(w_qh) \ge 1 \Longrightarrow L\max_q(w_qh) \ge 1 \Longrightarrow \boxed{c_* \ge \frac1L}✓✓$$

$$\qquad \textbf{上界（}\text{用 (H3)}✓）}：\text{把}\ G^{\top}y = 0\ \text{乘}\ h^*✓：\sum_i\omega_i(-1) + \sum_q\lambda_qc^* = 0 \Longrightarrow -1 + c^*L = 0 \Longrightarrow \boxed{c^* = \frac1L}✓✓$$

$$\qquad \qquad \text{且}\ h^*\ \text{由 (H3) 即 primal-feasible}✓ \Longrightarrow c_* \le c^* = \frac1L✓✓$$

$$\qquad \Longrightarrow \text{两侧合并} \Longrightarrow \boxed{c_* = \frac1L} \square✓✓$$

$$\qquad \textbf{充分条件三层必须分清}✓✓：\text{(a) KKT 给}\ \textbf{下界}✓；\ \text{(b) 活跃方阵给}\ \textbf{可行取值}✓；\ \text{(c) 二者相等才得}\ \textbf{精确最优}✓✓$$

$$\textbf{推论 6（}\textbf{证书归一化同构}✓✓）}：\text{dual-feasible 证书}\ (\nu_i,\mu_q) = (\omega_i/L,\ \lambda_q/L)✓\ \text{值} = 1/L = c_*✓ \Longrightarrow \textbf{对偶最优}✓✓$$

$$\qquad \text{且}\ \mu_q = c_*\lambda_q✓,\ \nu_i = c_*\omega_i✓ \Longrightarrow \boxed{(\mu,\nu) = c_*(\lambda,\omega)}✓✓$$

## §2 与 γ^(13) 实例的对应（✓✓）

| 命题对象 ✓ | 实例取值 ✓ |
|---|---|
| `n`／`m` ✓ | 5／6 ✓✓ |
| odd 行 ✓ | 频率 13, 19（`\gamma_j = \sigma_j`）✓ |
| even 行 ✓ | `F_6,F_8,F_{14},F_{18}` ⟹ **真实频率 12,16,28,36** ✓✓ |
| `y` ✓ | `(\omega_{13},\omega_{19},\lambda_6,\lambda_8,\lambda_{14},\lambda_{18})` **全部 > 0** ✓✓ |
| `L` ✓ | `1.99676941227516035204325246457` ✓ |
| `c_*` ✓ | `0.500808953629041885590052265792` ✓✓ |
| `(\mu,\nu) = c_*(\lambda,\omega)` ✓ | C-3868 已高精度闭合 ✓✓ |
| 引理 1 的数值镜像 ✓ | `\{Gh \le 0\}` 上 `max h_j = 0\ (j = 1..5)` ✓；C-3864 `t^* = 0` ✓✓ |

## §3 适用范围与失效条件（✓✓）

$$\textbf{适用}✓：\text{任何}\ (H1)\ \text{成立（严格正 KKT 证书）＋ 活跃集恰为题中}\ G\ \text{的行集}✓ \Longrightarrow \text{引理 1／推论 2–4／定理 5 均可调用}✓✓$$

$$\textbf{失效条件}✓✓：$$

$$\qquad \text{① 若某}\ \lambda_q = 0\ \text{或}\ \omega_i = 0✓ \Longrightarrow \text{(H1) 不成立}✗ \Longrightarrow \text{Gordan} \text{不可用}✗ \Longrightarrow \text{锥可能非平凡}✗ \Longrightarrow \text{秩／非奇异性}\ \textbf{不自动}✓\ \text{（须单独分析}✓）$$

$$\qquad \text{② 若活跃集不是全部 even 行}（\text{有}\ w_q\ \text{未取等}✓） \Longrightarrow \text{定理 5 的}\ h^*\ \text{构造需重做}✓$$

$$\qquad \text{③ 严格正性}\ \textbf{不是普遍定理假设}✗✓：\text{当前 γ 点满足}✓；\ \textbf{一般退化点不自动满足}✓✓$$

## §4 边界（**必写** ✓✓）

$$\boxed{\text{KKT–Gordan–Farkas mechanism} \ne \text{arithmetic bridge}}✓✓$$

$$\qquad \text{本命题证明的是}\ \textbf{局部几何中的定量分离机制}✓✓：\text{正 KKT 证书} \Rightarrow \text{平凡下降锥} \Rightarrow \text{结构分离} \Rightarrow c_* = \frac1{\sum\lambda_q}✓✓$$

$$\qquad \text{它}\ \textbf{尚未} \text{解释}✗✓：\textbf{为什么} \text{这个}\ G✓、\text{这个}\ c_*✓、\text{这个 active-frequency 结构}✓\ \text{具有 RH 所需的}\ \textbf{算术含义}✓✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 严格正证书假设 命中文件数=0
技术词 平凡下降锥   命中文件数=0
技术词 机制资产    命中文件数=2  :: ./ASSETS-REGISTRY.md ./C300-asset-registration-external-FSD-arithmetic-mechanism.md
```
$$\Longrightarrow \text{前两项}\ \textbf{本档新增}✓✓；\ \text{"机制资产"}\ \textbf{档案已有}✓ \Longrightarrow \text{本档}\ \textbf{仅引用、不列为提出}✓✓$$

## §6 本档**不**做的事 ✓✓

$$\textbf{不}增加计算✗；\ \textbf{不}新优化✗；\ \textbf{不}碰二阶✗；\ \textbf{不}做}\ V_\sigma\ \text{全局证书}（\text{下一刀}✓）$$

## §7 下一步（唐先生令：**CLOSED 后立即转 C-3874** ✓✓）

$$\textbf{C-3874}✓✓：\ \textbf{全局}\ V_\sigma\ \textbf{证书}✓ —— \text{把}\ V_\sigma \le 0.86885034832244940011✓\ \text{由"找到一个可行点"升级为}\ \textbf{全局上界证书}✓✓$$
$$\qquad \textbf{目标不是} \text{再做数值 minimization}✗✓；\ \text{而是}\ \textbf{构造可认证的全局界}✓（\text{例：凸松弛／对偶证书／区间算术}✓）$$
