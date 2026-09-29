# RESULT-h（2026-09-29）—— 极值表 **复核无误** ✓；单射性 **获证** ✓✓；"缺口强制"**仍属假设** ⚠️

> **性质**：**纯符号核对（无枚举）**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:55 ✓

**已查地图**：`RESULT-g`（三归约）／`RESULT-f`（$r_q{=}2t_q$）✓

D0: 本档对象 ＝ **档案已有**（线性超图度数界—经典 ✓）
D1: 0（产出＝**一处表复核 ＋ 一处订正 ＋ 一单射获证 ＋ 一假设点名** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 极值表逐项正确}:\ 3m_p\le\tbinom{v_p}2\Longrightarrow v_p\ \text{表}\ (3,4,5,6,6,7,7,8,8)\ ✓}$$
$$\boxed{\text{② ✗ 订正}:\ u_p>0\Longrightarrow v_p\le8\Longrightarrow m_p\le\mathbf{8}\ (\textbf{非 }5)✓}$$
$$\boxed{\text{③ ✓✓ 单射（重要）}:\ (p,i)\mapsto p\oplus e_i\ \text{在 }U_p\ \text{上单射}\Longrightarrow u=\text{真全局点数}}$$
$$\boxed{\text{④ ⚠️ "缺口强制"仍属假设}:\ q\ \text{已被}\ p\ \text{覆盖}\Longrightarrow\ \text{该处无缺口};\ \text{局部机制未找到}}✗$$
$$\boxed{\text{⑤ 度数加强}:\ \forall x:\ d_x\le4\ (2d_x\le8)\Longrightarrow m_p\le12\ (\text{STS}(9)\ \text{界})✓}$$

## §1 极值表（✓ 复核）

$$T_p\ \text{线性}\Longrightarrow\text{不同三元边之点对互不重复}\Longrightarrow3m_p\le\tbinom{v_p}2✓$$
$$v_p\ge\Bigl\lceil\tfrac{1+\sqrt{1+24m_p}}2\Bigr\rceil;\quad u_p\le9-v_p$$
| $m_p$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
|---|---|---|---|---|---|---|---|---|---|
| $v_p\ge$ | $3$ | $4$ | $5$ | $6$ | $6$ | $7$ | $7$ | $8$ | $8$ |
| $u_p\le$ | $6$ | $5$ | $4$ | $3$ | $3$ | $2$ | $2$ | $1$ | $1$ |

$$\textbf{订正}:\ u_p>0\Rightarrow v_p\le8\Rightarrow m_p\le8\ (\text{原稿写 }5\ ✗)$$
$$\textbf{度数界}:\ \text{每点 }x\ \text{之三边共用 2 对内点对},\ \text{而点 }x\ \text{共有 8 对内点对}\Rightarrow d_x\le4\Rightarrow3m_p\le36\Rightarrow m_p\le12✓$$

## §2 单射性（✓✓ 获证）

$$q=p\oplus e_i=p'\oplus e_j\ (p\ne p')\Longrightarrow d(p,p')=|\{i\}\triangle\{j\}|=2\ \text{与 3-packing 矛盾}✓$$
$$\therefore\ \boxed{u=\sum_p|U_p|\ \text{无重复};\quad u\ \text{＝这类 private }Q\text{-点之真实个数}}✓✓$$

## §3 ⚠️ 未获证者（诚实标注）

$$\text{唐先生之 }(\S2,\S4):\ \text{"每个 }i\in U_p\ \text{强制}\ Q_9\setminus N_1(A)\ \text{之独立缺口"}\ \Longrightarrow\ |Q_9\setminus N_1(A)|\ge c\,u$$
$$\textbf{障碍}:\ q=p\oplus e_i\ \text{由 }p\ \text{覆盖}✓\Longrightarrow\ \textbf{该点处无缺口};\ \text{缺口须在"别处"被逼出，尚无机制}✗$$
$$\therefore\ \text{本档不宣称此引理；标注为\ \textbf{假设}}\ ⚠️$$

## §4 状态与下一刀

$$\boxed{\text{已严格}:\ \S1\ \text{表}✓,\ \S2\ \text{单射}✓✓,\ u_p\le9-v_p,\ m_p\le8\ (u_p>0)}$$
$$\boxed{\text{下一步选项}:\ \text{（甲）找 }U_p\text{-点的缺口机制（未果）};\ \text{（乙）另寻 }u\ \text{之上界来源}}$$

## §5 边界（硬 ✓）

- **全部为符号论证（$3m\le\binom v2$、度数界、单射性）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；$\S2/\S4$ **标为假设** ⚠️

---

## §6 【技术词回查】（**本档提交前实跑，逐字粘贴**）

```
线性超图度数界 : 技术词 线性超图度数界 命中文件数=1    :: ./RESULT-2026-09-29h-extremal-table-checked-injectivity-proved-forcing-hypothesis-open.md
单射性 : 技术词 单射性        命中文件数=13   :: ./ASSETS-REGISTRY.md ./C3850-bridgeA-odd-frequency-discrepancy-entrance.md ./C349-cancellation-ideal-and-bridge-inequality-candidate.md
缺口强制 : 技术词 缺口强制     命中文件数=2    :: ./ASSETS-REGISTRY.md ./RESULT-2026-09-29h-extremal-table-checked-injectivity-proved-forcing-hypothesis-open.md
极值表 : 技术词 极值表        命中文件数=3    :: ./ASSETS-REGISTRY.md ./S2-30-PASS-2-evidence-audit.md ./RESULT-2026-09-29h-extremal-table-checked-injectivity-proved-forcing-hypothesis-open.md
三坐标归约 : 技术词 三坐标归约  命中文件数=0
```

$$\textbf{分类}:\ \text{本档新增} ＝ \text{无（仅"三坐标归约"为 }0\text{ 命中，但本档未以此命名）}$$
$$\textbf{档案已有（引用，不列为提出）}:\ \text{"单射性"}13\ \text{命中（含空间 A 之 }C3850/C349\text{，属\ \textbf{他线同名}}）;\ \text{"极值表"}3\ \text{命中}$$
$$\textbf{通用词（不计）}:\ \text{线性超图度数界／缺口强制（命中皆本档或登记表自身）}$$
